#!/usr/bin/env python3
"""Validate frozen primary evidence, export plotting data, and render Chapter 5.

No inference, source mutation, record filtering, or judge data is used.
Run from any directory; see ../PROVENANCE.md for paths and dependencies.
"""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import os
import random
from collections import Counter
from pathlib import Path
from statistics import mean, median

os.environ.setdefault("MPLCONFIGDIR", "/tmp/usn-thesis-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, PercentFormatter
from jsonschema import Draft202012Validator
import numpy as np

OUT = Path(__file__).resolve().parents[1]
CONDITIONS = ("B0", "B1", "G1")
TASKS = tuple(f"T{i:03d}" for i in range(1, 31))
METRICS = ("input_tokens", "output_tokens", "total_tokens", "llm_calls", "retrieval_calls")
TYPES = ("direct_retrieval", "within_document_reasoning", "cross_document_reasoning", "insufficient_evidence")
TYPE_LABELS = ("Direct retrieval", "Within-document", "Cross-document", "Insufficient evidence")
GRAY, BLUE, ORANGE = "#595959", "#0072B2", "#D55E00"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def validate(primary, research):
    """Fail before writing outputs if any source, accounting, or parity check fails."""
    sources = {}

    def source(path, expected=None):
        digest = sha(path)
        require(expected is None or digest == expected, f"SHA256 mismatch: {path}")
        sources[str(path)] = digest
        return load(path) if path.suffix == ".json" else path.read_text()

    freeze = source(primary / "primary_benchmark_raw_freeze_manifest.json")
    require(freeze["status"] == "frozen" and freeze["primary_execution_complete"], "Results are not frozen/complete")
    launch = source(primary / "launch_manifest.json", freeze["launch_manifest_sha256"])
    source(primary / "primary_benchmark_runner_v1.py", freeze["runner_sha256"])
    source(primary / "PRIMARY_BENCHMARK_V1_LIVE.log", freeze["execution_log_sha256"])
    inventory = source(primary / freeze["record_hash_inventory"]["path"], freeze["record_hash_inventory"]["sha256"])
    entries = [line.split() for line in inventory.splitlines()]
    require(len(entries) == 270 and len({name for _, name in entries}) == 270, "Invalid hash inventory")
    # Frozen bundle identity hashes sorted filename<TAB>file-hash<LF> rows.
    bundle = "".join(f"{name}\t{digest}\n" for digest, name in sorted(entries, key=lambda x: x[1]))
    require(hashlib.sha256(bundle.encode()).hexdigest() == freeze["raw_record_bundle_sha256"], "Bundle identity mismatch")
    require({p.name for p in (primary / "run_records").glob("*.json")} == {n for _, n in entries}, "Unexpected/missing raw records")
    records = {name: source(primary / "run_records" / name, digest) for digest, name in entries}

    order = source(research / "evidence/engineering/primary_execution_order_v1.json", launch["primary_order_sha256"])
    require(order["run_count"] == launch["run_count"] == freeze["primary_run_count"] == 270, "Run count mismatch")
    require(order["generation_seed"] == launch["generation_seed"] == 20260912, "Order seed mismatch")
    require(freeze["execution_order"]["sha256"] == launch["primary_order_sha256"], "Order binding mismatch")
    require([r["execution_sequence"] for r in order["runs"]] == list(range(1, 271)), "Incomplete sequence")
    expected = {(t, c, r) for t in TASKS for c in CONDITIONS for r in (1, 2, 3)}
    require({(r["task_id"], r["condition"], r["repetition"]) for r in order["runs"]} == expected, "Incomplete execution matrix")
    require({r["output_relative_path"] for r in order["runs"]} == set(records), "Order/record mismatch")

    task_manifest = source(research / "benchmark/tasks/primary_benchmark_freeze_manifest.json")
    task_hashes = task_manifest["frozen_task_file_sha256"]
    canonical = json.dumps(task_hashes, sort_keys=True, separators=(",", ":"))
    require(hashlib.sha256(canonical.encode()).hexdigest() == task_manifest["frozen_task_set_sha256"], "Task set identity mismatch")
    require(task_manifest["task_ids"] == list(TASKS) and task_manifest["task_count"] == 30, "Wrong task set")
    for binding in task_manifest["use_case_freeze_bindings"].values():
        source(research / binding["manifest_path"], binding["manifest_sha256"])
    task_schema = source(research / task_manifest["task_schema"]["path"], task_manifest["task_schema"]["sha256"])
    task_validator = Draft202012Validator(task_schema)
    tasks = {}
    for relative, digest in task_hashes.items():
        task = source(research / relative, digest)
        task_validator.validate(task)
        tasks[task["task_id"]] = task
    require(Counter(t["task_type"] for t in tasks.values()) == Counter({TYPES[0]: 9, TYPES[1]: 9, TYPES[2]: 6, TYPES[3]: 6}), "Task allocation mismatch")

    # This schema is recorded by its observed hash; the primary freeze does not
    # provide a historical schema hash. Raw bytes are independently freeze-bound.
    run_validator = Draft202012Validator(source(research / "benchmark/schema/run.schema.json"))
    rows, paired = [], {}
    for identity in order["runs"]:
        record = records[identity["output_relative_path"]]
        run_validator.validate(record)
        for key in ("task_id", "condition", "run_id", "experiment_id"):
            require(record[key] == identity[key], f"Identity mismatch: {record['run_id']}/{key}")
        require(record["code_revision"] == launch["final_execution_code_revision"] == freeze["final_execution_code_revision"], "Code identity mismatch")
        require(record["execution_mode"] == "benchmark" and record["schema_version"] == "0.4", "Wrong record type")
        require(not record["errors"], f"Execution error: {record['run_id']}")
        usage, calls = record["usage"], record["model"]["calls"]
        for key in ("input_tokens", "output_tokens", "total_tokens"):
            require(usage[key] == sum(c[key] for c in calls), f"Call accounting mismatch: {record['run_id']}/{key}")
        require(usage["total_tokens"] == usage["input_tokens"] + usage["output_tokens"], "Token sum mismatch")
        require(all(c["total_tokens"] == c["input_tokens"] + c["output_tokens"] and c["status"] == "completed" for c in calls), "Corrupted model call")
        require(usage["llm_calls"] == len(calls) and usage["retrieval_calls"] == len(record["retrieval"]["calls"]), "Call count mismatch")
        seconds = record["timing"]["end_to_end_ms"] / 1000
        require(math.isfinite(seconds) and seconds > 0, "Invalid latency")
        cfg = record["configuration"]
        require(cfg["model_version"] == "a68eeb5701b0a627f513a134f7ec029477a04b66a4605b32e27917ac93bd67a3" and cfg["random_seed"] == 20260912 and cfg["temperature"] == 0 and cfg["max_output_tokens"] == 1024, "Generation configuration mismatch")
        events = record["events"]
        decisions = [e["details"] for e in events if e["event_type"] == "policy_decision"]
        recovery_events = sum(e["event_type"] == "recovery_started" for e in events)
        require(usage["retries"] == recovery_events, "Recovery accounting mismatch")
        require(record["status"] == ("completed_after_recovery" if recovery_events else "completed"), "Terminal status mismatch")
        abstained = record["final_output"]["abstained"]
        if record["condition"] == "B0":
            require(not decisions and not recovery_events and not abstained, "Unexpected B0 control state")
            action = "NONE"
        else:
            require(len(decisions) == 1, "Unexpected decision count")
            action = decisions[0]["selected_action"]
            require(action in ("ACCEPT", "REVISE_ONLY", "RERETRIEVE_REVISE", "ABSTAIN"), "Unexpected/resource-stop decision")
            require(bool(recovery_events) == (action in ("REVISE_ONLY", "RERETRIEVE_REVISE")), "Decision/path mismatch")
            require(sum(e["event_type"] == "abstained" for e in events) == int(abstained), "Abstention event mismatch")
            require(action != "ABSTAIN" or abstained, "Immediate abstention mismatch")
            require(usage["llm_calls"] == (5 if recovery_events else 3), "Agentic call path mismatch")
        row = {"task_id": record["task_id"], "condition": record["condition"], "repetition": identity["repetition"], "run_id": record["run_id"], "use_case": f"UC{(int(record['task_id'][1:])-1)//10+1}", "task_type": tasks[record["task_id"]]["task_type"], **{k: usage[k] for k in METRICS}, "seconds": seconds, "recovered": int(bool(recovery_events)), "abstained": int(abstained), "selected_action": action}
        rows.append(row)
        paired[(row["task_id"], row["condition"], row["repetition"])] = record
    require(Counter(r["condition"] for r in rows) == freeze["condition_counts"], "Condition denominator mismatch")
    require(Counter(r["use_case"] for r in rows) == freeze["use_case_counts"], "Use-case denominator mismatch")
    require(Counter(r["status"] for r in records.values()) == freeze["execution_status_counts"], "Status denominator mismatch")
    for t in TASKS:
        for repetition in (1, 2, 3):
            b, g = (paired[(t, c, repetition)] for c in ("B1", "G1"))
            require(b["final_output"] == g["final_output"], f"Final-output difference: {t}/{repetition}")
            for k in METRICS:
                expected_delta = {"input_tokens": -17739, "output_tokens": -1481, "total_tokens": -19220, "llm_calls": -2, "retrieval_calls": -1}[k] if t == "T017" else 0
                require(g["usage"][k] - b["usage"][k] == expected_delta, f"Unexpected structural difference: {t}/{k}")
            for key in ("model_config_id", "model_version", "retrieval_config_id", "prompt_version"):
                require(b["configuration"][key] == g["configuration"][key], "Paired configuration mismatch")
        for c in CONDITIONS:
            rs = [paired[(t, c, r)] for r in (1, 2, 3)]
            require(all(r["final_output"] == rs[0]["final_output"] and r["usage"] == rs[0]["usage"] for r in rs), "Within-task structural variation")
            require(all([e["details"] for e in r["events"] if e["event_type"] == "policy_decision"] == [e["details"] for e in rs[0]["events"] if e["event_type"] == "policy_decision"] for r in rs), "Within-task decision variation")

    task_rows = []
    for t in TASKS:
        for c in CONDITIONS:
            group = [r for r in rows if r["task_id"] == t and r["condition"] == c]
            require(len(group) == 3, "Missing repetitions")
            task_rows.append({"task_id": t, "condition": c, "use_case": group[0]["use_case"], "task_type": group[0]["task_type"], **{k: mean(r[k] for r in group) for k in (*METRICS, "seconds")}, "recovered": group[0]["recovered"], "abstained": group[0]["abstained"], "selected_action": group[0]["selected_action"]})
    by_task = {(r["task_id"], r["condition"]): r for r in task_rows}
    differences = [{"task_id": t, **{k: by_task[t, "G1"][k] - by_task[t, "B1"][k] for k in (*METRICS, "seconds")}} for t in TASKS]
    summary = {c: {k: mean(r[k] for r in task_rows if r["condition"] == c) for k in (*METRICS, "seconds")} for c in CONDITIONS}
    for c in CONDITIONS:
        for k in (*METRICS, "seconds"):
            require(math.isclose(summary[c][k], mean(r[k] for r in rows if r["condition"] == c), abs_tol=1e-9), "Task/run aggregation mismatch")

    def table(name):
        text = source(OUT.parents[0] / "revision-tables" / name)
        cells = [[cell.strip() for cell in line.removesuffix(r" \\").split(" & ")] for line in text.splitlines() if " & " in line and line.endswith(r" \\")]
        expected_rows = {"execution-overall.tex": 4, "execution-control.tex": 4, "logged-abstention.tex": 4, "per-task-execution.tex": 31, "execution-use-case.tex": 10, "task-type-results.tex": 13, "paired-execution.tex": 5}
        require(len(cells) == expected_rows[name], f"Unexpected table coverage: {name}")
        return cells

    def numeric_equal(values, cells, digits):
        require(len(values) == len(cells), "Table shape mismatch")
        for value, cell, precision in zip(values, cells, digits):
            require(f"{value:.{precision}f}" == f"{float(cell.replace(',', '')):.{precision}f}", f"Published-table mismatch: {value} vs {cell}")

    for cells in table("execution-overall.tex"):
        if cells[0] in CONDITIONS:
            numeric_equal([summary[cells[0]][k] for k in (*METRICS, "seconds")], cells[1:], [1, 1, 1, 2, 2, 2])
    for cells in table("execution-control.tex"):
        if cells[0] in CONDITIONS:
            group = [r for r in rows if r["condition"] == cells[0]]
            recovered = sum(r["recovered"] for r in group)
            numeric_equal([90-recovered, recovered, sum(r["abstained"] for r in group), 0], cells[1:], [0]*4)
    for cells in table("logged-abstention.tex"):
        if cells[0] in CONDITIONS:
            group = [r for r in rows if r["condition"] == cells[0]]
            insufficient = [r for r in group if r["task_type"] == TYPES[3]]
            answerable = [r for r in group if r["task_type"] != TYPES[3]]
            numeric_equal([sum(r["abstained"] for r in insufficient), len(insufficient), sum(r["abstained"] for r in answerable), len(answerable)], cells[1:], [0]*4)
    for cells in table("per-task-execution.tex"):
        if cells[0] in TASKS:
            values = [by_task[cells[0], c][k] for c in CONDITIONS for k in ("total_tokens", "seconds")]
            values.append(by_task[cells[0], "G1"]["total_tokens"] - by_task[cells[0], "B1"]["total_tokens"])
            numeric_equal(values, cells[1:], [0, 2, 0, 2, 0, 2, 0])
    for cells in table("execution-use-case.tex"):
        if cells[0] in ("UC1", "UC2", "UC3"):
            group = [r for r in rows if r["use_case"] == cells[0] and r["condition"] == cells[1]]
            numeric_equal([mean(r["total_tokens"] for r in group), mean(r["seconds"] for r in group), sum(r["recovered"] for r in group), sum(r["abstained"] for r in group)], cells[2:], [1, 2, 0, 0])
    for cells in table("task-type-results.tex"):
        if cells[0] in TYPE_LABELS:
            group = [r for r in task_rows if r["task_type"] == TYPES[TYPE_LABELS.index(cells[0])] and r["condition"] == cells[1]]
            numeric_equal([len(group), mean(r["total_tokens"] for r in group), mean(r["seconds"] for r in group)], [cells[2], *cells[4:]], [0, 0, 2])
    # Reproduce the existing table's task-bootstrap, not a new uncertainty claim.
    # random.Random.choices uses a different seeded stream from NumPy's RNGs.
    paired_metrics = ("total_tokens", "llm_calls", "retrieval_calls", "seconds")
    rng = random.Random(20260912)
    matrix = np.array([[r[k] for k in paired_metrics] for r in differences])
    indices = np.array([rng.choices(range(30), k=30) for _ in range(10000)])
    intervals = np.quantile(matrix[indices].mean(axis=1), [.025, .975], axis=0)
    paired_labels = ("Tokens", "LLM calls", "Retrieval calls", "Seconds")
    for cells in table("paired-execution.tex"):
        if cells[0] in paired_labels:
            index = paired_labels.index(cells[0])
            numeric_equal([mean(matrix[:, index]), median(matrix[:, index])], cells[1:3], [2, 2])
            endpoints = cells[3].strip("[]").split(", ")
            numeric_equal(intervals[:, index], endpoints, [2, 2])
    joint = []
    for task_type in TYPES:
        for c in ("B1", "G1"):
            group = [r for r in task_rows if r["task_type"] == task_type and r["condition"] == c]
            for recovered, abstained in ((0, 0), (1, 0), (1, 1), (0, 1)):
                count = sum(r["recovered"] == recovered and r["abstained"] == abstained for r in group)
                joint.append({"task_type": task_type, "condition": c, "recovered": recovered, "abstained": abstained, "tasks": count, "task_denominator": len(group), "runs": count*3, "run_denominator": len(group)*3})
    return rows, task_rows, differences, joint, summary, sources, freeze, intervals


def style():
    plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 9.5, "axes.labelsize": 10, "axes.titlesize": 10, "xtick.labelsize": 9, "ytick.labelsize": 9, "legend.fontsize": 9, "axes.linewidth": .65, "lines.linewidth": 1.6, "xtick.major.width": .65, "ytick.major.width": .65, "xtick.major.size": 3, "ytick.major.size": 3, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 450, "hatch.linewidth": .55})


def save(fig, name):
    # Fixed physical canvas, no bbox='tight' resizing; inclusion stays at 1:1.
    fig.savefig(OUT / f"{name}.pdf", metadata={"Creator": "Matplotlib; generate_benchmark_figures.py", "CreationDate": None, "ModDate": None})
    fig.savefig(OUT / f"{name}.png", dpi=450)
    plt.close(fig)


def resources(task_rows):
    fig, axes = plt.subplots(1, 2, figsize=(6.668, 2.95), sharey=True)
    fig.subplots_adjust(left=.112, right=.966, bottom=.205, top=.82, wspace=.15)
    for ax, metric, divisor, limit, xlabel in zip(axes, ("total_tokens", "seconds"), (1000, 1), (38, 110), ("Mean total tokens (thousands)", "Mean end-to-end latency (s)")):
        for c, color, linestyle in zip(CONDITIONS, (GRAY, BLUE, ORANGE), ((0, (2, 2)), "-", (0, (5, 2.5)))):
            x = np.sort([r[metric]/divisor for r in task_rows if r["condition"] == c])
            ax.step(np.r_[0, x, limit], np.r_[0, np.arange(1, 31)/30, 1], where="post", color=color, linestyle=linestyle, label=c, zorder=3)
        ax.set(xlim=(0, limit), ylim=(0, 1.02), xlabel=xlabel)
        ax.set_yticks([0, .25, .5, .75, 1])
        ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
        ax.grid(axis="y", color=".88", linewidth=.5, zorder=0)
    axes[0].set_ylabel("Cumulative share of tasks")
    axes[0].xaxis.set_major_locator(MultipleLocator(10))
    axes[1].xaxis.set_major_locator(MultipleLocator(20))
    for ax, label in zip(axes, ("(a) Total tokens", "(b) Latency")):
        ax.set_title(label, loc="left", pad=9)
    x = next(r["seconds"] for r in task_rows if r["task_id"] == "T017" and r["condition"] == "B1")
    axes[1].annotate(f"B1, T017: {x:.1f} s", xy=(x, 1), xytext=(64, .69), fontsize=8.5, arrowprops={"arrowstyle": "-", "color": BLUE, "lw": .7}, color=BLUE)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.55, 1.01), ncol=3, frameon=False, handlelength=3)
    save(fig, "benchmark_task_resource_ecdfs")


def paired_differences(differences):
    fig, axes = plt.subplots(3, 1, figsize=(6.668, 5.1), sharex=True, gridspec_kw={"height_ratios": (1, 1, 1.25)})
    fig.subplots_adjust(left=.125, right=.985, bottom=.13, top=.936, hspace=.49)
    x = np.arange(1, 31)
    delta_tokens = np.array([r["total_tokens"] for r in differences])/1000
    delta_seconds = np.array([r["seconds"] for r in differences])
    for ax, y, ylim in zip(axes, (delta_tokens, delta_seconds, delta_seconds), ((-21.5, 2.8), (-52, 7), (-6, 2.5))):
        ax.axhline(0, color=".55", lw=.7, zorder=1)
        for i, value in zip(x, y):
            if ylim[0] <= value <= ylim[1]:
                color = ORANGE if i == 17 else GRAY
                ax.vlines(i, 0, value, color=color, lw=1.15, zorder=2)
                ax.plot(i, value, marker="D" if i == 17 else "o", color=color, markersize=4 if i == 17 else 3.2, zorder=3)
        ax.set(xlim=(.4, 30.6), ylim=ylim)
        ax.grid(axis="y", color=".9", lw=.5)
        ax.set_xticks(x)
        ax.tick_params(axis="x", labelbottom=False, length=2.5)
    axes[0].set_title("(a) Paired token differences: all 30 tasks", loc="left", pad=7)
    axes[0].set_ylabel("Δ tokens\n(thousands)")
    axes[0].set_yticks([-20, -10, 0])
    axes[0].text(2, -8, "29 tasks: Δ tokens = Δ calls = 0", fontsize=9)
    axes[0].annotate("T017: −19,220 tokens\n−2 model calls; −1 retrieval", xy=(17, -19.22), xytext=(21, -16.6), fontsize=8.5, color=ORANGE, va="center", arrowprops={"arrowstyle": "-", "lw": .7, "color": ORANGE})
    axes[1].set_title("(b) Paired latency differences: full range", loc="left", pad=7)
    axes[1].set_ylabel("Δ latency (s)")
    axes[1].set_yticks([-50, -25, 0])
    axes[1].annotate(f"T017: {delta_seconds[16]:.2f} s", xy=(17, delta_seconds[16]), xytext=(21, -33), color=ORANGE, fontsize=9, arrowprops={"arrowstyle": "-", "lw": .7, "color": ORANGE})
    axes[2].set_title("(c) Latency detail: −6 to +2.5 s (T017 shown in full above)", loc="left", pad=7)
    axes[2].set_ylabel("Δ latency (s)")
    axes[2].set_yticks([-6, -4, -2, 0, 2])
    axes[2].scatter([17], [-5.85], marker="v", color=ORANGE, s=25, clip_on=False, zorder=4)
    axes[2].annotate("T017 below detail range", xy=(17, -5.85), xytext=(19.5, -4.7), fontsize=8, color=ORANGE)
    axes[2].tick_params(axis="x", labelbottom=True, labelsize=7.8)
    axes[2].set_xticklabels([f"{i:02d}" for i in x], rotation=0)
    axes[2].set_xlabel("Task identifier (01 = T001); differences are G1 − B1", labelpad=7)
    save(fig, "benchmark_paired_resource_differences")


def recovery_abstention(joint):
    fig, ax = plt.subplots(figsize=(6.668, 4.1))
    fig.subplots_adjust(left=.085, right=.96, bottom=.15, top=.855)
    keys = ((0, 0), (1, 0), (1, 1), (0, 1))
    styles = (("#E5E5E5", ""), ("#94C6DF", ""), ("#94C6DF", "////"), ("#F2BA9D", "xxxx"))
    labels = ("No recovery; flag false", "Recovery; flag false", "Recovery; flag true", "Immediate abstention; flag true")
    ticks, ticklabels = [], []
    for j, task_type in enumerate(TYPES):
        for ci, c in enumerate(("B1", "G1")):
            y = j*2.6 + ci*.8
            ticks.append(y)
            ticklabels.append(c)
            left = 0
            for key, (color, hatch), label in zip(keys, styles, labels):
                row = next(r for r in joint if (r["task_type"], r["condition"], r["recovered"], r["abstained"]) == (task_type, c, *key))
                count, n = row["tasks"], row["task_denominator"]
                width = count/n
                if count:
                    ax.barh(y, width, height=.58, left=left, color=color, edgecolor=".2", linewidth=.55, hatch=hatch, label=label if j == 0 and ci == 0 else None)
                    ax.text(left+width/2, y, str(count), va="center", ha="center", fontsize=9, bbox={"facecolor": color, "edgecolor": "none", "pad": .4})
                left += width
            require(math.isclose(left, 1), "Joint denominator mismatch")
        n = next(r["task_denominator"] for r in joint if r["task_type"] == task_type)
        ax.text(0, j*2.6-.72, f"{TYPE_LABELS[j]} (n = {n})", ha="left", va="center", transform=ax.get_yaxis_transform(), fontsize=9)
    from matplotlib.patches import Patch
    handles = [Patch(facecolor=color, edgecolor=".2", linewidth=.55, hatch=hatch, label=label) for (color, hatch), label in zip(styles, labels)]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(.55, 1.0), ncol=2, frameon=False, handlelength=2.2, columnspacing=1.5, fontsize=8.8)
    ax.set(xlim=(0, 1), ylim=(-1.25, 9.05), xlabel="Share of task clusters")
    ax.invert_yaxis()
    ax.set_yticks(ticks, ticklabels)
    ax.xaxis.set_major_locator(MultipleLocator(.25))
    ax.xaxis.set_major_formatter(PercentFormatter(1, decimals=0))
    ax.tick_params(axis="y", length=0, pad=6)
    ax.spines["left"].set_visible(False)
    save(fig, "benchmark_recovery_abstention_paths")


def csv_output(name, rows):
    with (OUT / "data" / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary-root", type=Path, default=Path("/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1"))
    parser.add_argument("--research-root", type=Path, default=Path("/home/emadh/projects/responsible-agentic-workflows"))
    args = parser.parse_args()
    rows, task_rows, differences, joint, summary, sources, freeze, intervals = validate(args.primary_root, args.research_root)
    (OUT / "data").mkdir(exist_ok=True)
    csv_output("validated_execution_metrics.csv", sorted(rows, key=lambda r: (r["task_id"], r["condition"], r["repetition"])))
    csv_output("task_resource_means.csv", task_rows)
    csv_output("paired_task_differences.csv", differences)
    csv_output("recovery_abstention_by_type.csv", joint)
    with (OUT / "data/source_sha256.tsv").open("w") as stream:
        stream.write("sha256\tsource_path\n")
        for path, digest in sorted(sources.items()):
            stream.write(f"{digest}\t{path}\n")
    report = {"status": "PASS", "raw_records": 270, "task_clusters": 30, "repetitions_per_task_condition": 3, "paired_final_outputs_identical": 90, "structurally_divergent_tasks": ["T017"], "raw_bundle_sha256": freeze["raw_record_bundle_sha256"], "source_files_checked": len(sources), "summary_means": summary, "summary_task_medians": {c: {k: median(r[k] for r in task_rows if r["condition"] == c) for k in ("total_tokens", "seconds")} for c in CONDITIONS}, "paired_mean": {k: mean(r[k] for r in differences) for k in (*METRICS, "seconds")}, "paired_median": {k: median(r[k] for r in differences) for k in (*METRICS, "seconds")}, "parity_tables": ["execution-overall", "execution-control", "logged-abstention", "per-task-execution", "execution-use-case", "task-type-results (execution columns only)"], "dependencies": {name: importlib.metadata.version(name) for name in ("matplotlib", "numpy", "jsonschema")}, "script_sha256": sha(Path(__file__)), "run_schema_note": "Observed schema hash recorded; no schema hash binding is supplied by the raw freeze.", "excluded_records": 0, "uncertainty_intervals_created": 0}
    report["parity_tables"].append("paired-execution (means, medians and existing intervals)")
    report["existing_interval_reproduction"] = {"resamples": 10000, "seed": 20260912, "rng": "Python random.Random.choices", "quantile_method": "numpy.quantile default linear", "metrics": ["total_tokens", "llm_calls", "retrieval_calls", "seconds"], "bounds": intervals.tolist()}
    (OUT / "data/validation_report.json").write_text(json.dumps(report, indent=2)+"\n")
    style()
    resources(task_rows)
    paired_differences(differences)
    recovery_abstention(joint)
    print(json.dumps({"status": "PASS", "records": len(rows), "task_condition_means": len(task_rows), "figures": 3, "summary_means": summary}, indent=2))


if __name__ == "__main__":
    main()
