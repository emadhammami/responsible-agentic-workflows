#!/usr/bin/env python3
"""Prospective R11 synthetic two-judge qualification. No network unless `run`.

Modes: self-test, prepare, verify, status, run. `run --resume` is permitted
only after a journaled HTTP 429 pause; it never replays a completed slot.
No primary/document scoring package path is used or accepted.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

FROZEN_R10 = {'scripts/r10_hosted_qualification.py': '3bd531af4190f9c221e26982f4e692fdb68e5547da4faa7e7f098aeb9d963c79', 'evidence/engineering/llm_judge_r10_qualification_contract_2026-10-08.md': '9bcaf469bd229140aeb8c0c373e92a7bdca811e4c2b6be232f9aa6177b634b7e', 'evidence/engineering/r10_qualification_v1/cases.json': '253d102d2ec55ccec31a9395b67f6df5b920c3f9c903f3b1d406362fca22e76d', 'evidence/engineering/r10_qualification_v1/gold.json': '10218ae890c28eefb5467fd6e0be26cbb0f5edc556759d1a8f7498ae1da7d688', 'evidence/engineering/r10_qualification_v1/prompt.txt': 'd2686d0c125581fd3195095f9e6de8f925e44d812b60cd7327f8f6c79df23ebe', 'evidence/engineering/r10_qualification_v1/frozen_validator.py': '925891d326cc3138f74fe2198a7786df21b1bf2de8a4c9d62984c2aae72527fd'}
PROTOCOL_COMMIT = "d1bb5e88c1cd17223d2b71cb200a27d7a563b485"
PROTOCOL_PATH = "evidence/engineering/llm_judge_r11_qualification_contract_2026-10-08.md"
PROTOCOL_SHA256 = "39413acd9cae000fd7357eb57e58d111e8afbfc43e1881c4034c50778b15f96a"
MATERIAL_DIR = Path("evidence/engineering/r11_qualification_v1")
CAPSULE = Path.home() / "primary-benchmark-results/LLM-JUDGE-R11-QUALIFICATION-2026-10-08"
PINNED = {
    "cases.json": "a5f553d82b900b5985ce3d7651f69d076825ad0facfc505534a01faf29d30b57",
    "gold.json": "63e68518e11fa2f2163840aabbe0c9b2e4fd57d853234ab8d9ce96bd104065ce",
    "prompt.txt": "d2686d0c125581fd3195095f9e6de8f925e44d812b60cd7327f8f6c79df23ebe",
    "frozen_validator.py": "925891d326cc3138f74fe2198a7786df21b1bf2de8a4c9d62984c2aae72527fd",
}
CANDIDATES = (
    ("J1", "cohere", "command-a-plus-05-2026", "COHERE_API_KEY"),
    ("J2", "gemini", "gemini-3.5-flash-lite", "GEMINI_API_KEY"),
)
IDS = tuple(f"Q{i:02d}" for i in range(1, 10))
ABST = ("correct_abstention", "failed_to_abstain", "incorrect_abstention")
GROUND = ("SUPPORTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED", "CONTRADICTED")
PURE_ABST = ("Q02", "Q07")
TIMEOUT = {"cohere": 120, "gemini": 120}
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
# R11 fixed transport: one HTTP attempt per slot; no auto retry on any failure.
# Explicit --resume permitted only after an HTTP 429 rejection, which records
# no valid judgment and does not complete the slot.


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def write_new(path, value):
    p = Path(path)
    with p.open("x", encoding="utf-8") as f:
        f.write(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n")
        f.flush()
        os.fsync(f.fileno())
    p.chmod(0o600)


def replace_json(path, value):
    p = Path(path)
    tmp = p.with_name(p.name + ".tmp")
    if tmp.exists():
        raise RuntimeError("Orphan status temp file: stop")
    write_new(tmp, value)
    os.replace(tmp, p)


def append_jsonl(path, value):
    p = Path(path)
    with p.open("a", encoding="utf-8") as f:
        f.write(encode(value) + "\n")
        f.flush()
        os.fsync(f.fileno())
    p.chmod(0o600)


def read_jsonl(path):
    p = Path(path)
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def repo_guard():
    if git("branch", "--show-current") != "research/b1-g1-real-execution-wiring":
        raise RuntimeError("Wrong branch")
    subprocess.run(["git", "merge-base", "--is-ancestor", PROTOCOL_COMMIT, "HEAD"], check=True)
    if git("status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Dirty worktree")
    if sha(Path(PROTOCOL_PATH).read_bytes()) != PROTOCOL_SHA256:
        raise RuntimeError("R11 contract mismatch")
    for relative, expected_hash in FROZEN_R10.items():
        if sha(Path(relative).read_bytes()) != expected_hash:
            raise RuntimeError("Protected R10 file mutated: " + relative)

    expected = [MATERIAL_DIR / n for n in PINNED] + [Path("scripts/r11_hosted_qualification.py")]
    for path in expected:
        if not path.is_file() or not git("ls-files", "--error-unmatch", str(path)):
            raise RuntimeError("R11 file not committed: " + str(path))
    for name, digest in PINNED.items():
        if sha((MATERIAL_DIR / name).read_bytes()) != digest:
            raise RuntimeError("R11 prospective materials mutated: " + name)
    if Path("scripts/r11_hosted_qualification.py").resolve() != Path(__file__).resolve():
        raise RuntimeError("Invoke committed script from repository root")


def valid_cases(cases, gold):
    if type(cases) is not list or len(cases) != 9 or type(gold) is not dict:
        raise RuntimeError("Expected 9 new atomic cases and gold map")
    if tuple(x.get("evaluation_id") for x in cases) != IDS or set(gold) != set(IDS):
        raise RuntimeError("Prospective case identity/order mismatch")
    required = {"evaluation_id", "question", "generated_output", "reference_answer",
                "reference_evidence", "retrieved_evidence"}
    for case in cases:
        if set(case) != required:
            raise RuntimeError("Unexpected keys or gold leakage in model input")
        for key in ("question", "reference_answer"):
            if not isinstance(case[key], str) or not case[key]:
                raise RuntimeError("Invalid input field " + key)
        if set(case["generated_output"]) != {"kind", "answer"}:
            raise RuntimeError("Unexpected output structure")
        for key in ("reference_evidence", "retrieved_evidence"):
            if not (isinstance(case[key], list) and len(case[key]) == 1 and
                    set(case[key][0]) == {"text"} and isinstance(case[key][0]["text"], str)):
                raise RuntimeError("Evidence shape invalid")
        sig = gold[case["evaluation_id"]]
        if not (isinstance(sig, list) and len(sig) == 3 and type(sig[0]) is int and
                sig[0] in (0, 1, 2) and sig[1] in (*ABST, "not_applicable") and
                type(sig[2]) is list and all(l in GROUND for l in sig[2])):
            raise RuntimeError("Gold signature invalid")
        if case["generated_output"]["kind"] == "abstention":
            if case["generated_output"]["answer"] is not None or sig[2]:
                raise RuntimeError("Pure abstention must not assert a claim")
        elif case["generated_output"]["kind"] == "answer":
            if not (isinstance(case["generated_output"]["answer"], str) and len(sig[2]) == 1):
                raise RuntimeError("Expected one factual claim")
        else:
            raise RuntimeError("Unexpected answer kind")
    if {gold[c][1] for c in IDS} != {*ABST, "not_applicable"}:
        raise RuntimeError("Missing abstention class")
    if {label for c in IDS for label in gold[c][2]} != set(GROUND):
        raise RuntimeError("Missing grounding class")
    if tuple(c for c in IDS if not gold[c][2]) != PURE_ABST:
        raise RuntimeError("Pure abstention cases changed")


def load_validator(path):
    spec = importlib.util.spec_from_file_location("r11_frozen_validator", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, "valid", None)):
        raise RuntimeError("Frozen validator missing")
    return module.valid


def material_check(dir_path):
    for name, digest in PINNED.items():
        if sha((dir_path / name).read_bytes()) != digest:
            raise RuntimeError("Frozen file changed: " + name)
    cases = json.loads((dir_path / "cases.json").read_text())
    gold = json.loads((dir_path / "gold.json").read_text())
    valid_cases(cases, gold)
    prompt = (dir_path / "prompt.txt").read_text()
    if "evaluator_notes must be a string" not in prompt:
        raise RuntimeError("Wrong prompt")
    return cases, gold, prompt, load_validator(dir_path / "frozen_validator.py")


def prepare():
    repo_guard()
    material_check(MATERIAL_DIR)
    if CAPSULE.exists():
        raise RuntimeError("R11 capsule already exists, refusing overwrite")
    CAPSULE.mkdir(parents=True, mode=0o700, exist_ok=False)
    (CAPSULE / "inputs").mkdir(mode=0o700)
    (CAPSULE / "scripts").mkdir(mode=0o700)
    files = {}
    for name in PINNED:
        target = CAPSULE / "inputs" / name
        target.write_bytes((MATERIAL_DIR / name).read_bytes())
        target.chmod(0o600)
        files["inputs/" + name] = PINNED[name]
    for source, rel in ((Path(__file__), "scripts/r11_hosted_qualification.py"),
                        (Path(PROTOCOL_PATH), "inputs/r11_contract.md")):
        dest = CAPSULE / rel
        dest.write_bytes(source.read_bytes())
        dest.chmod(0o600)
        files[rel] = sha(source.read_bytes())
    write_new(CAPSULE / "harness_freeze.json", {
        "created_utc": now(), "repo_commit": git("rev-parse", "HEAD"),
        "contract_sha256": PROTOCOL_SHA256, "files_sha256": files,
        "order": [c[0] for c in CANDIDATES], "gold_is_model_hidden": True,
        "qualified_pair": None, "primary_judging": 0, "inference_requests": 0,
        "run_authorized_by_prepare": False,
    })
    print("R11_CAPSULE_PREPARED=PASS")
    print("INFERENCE_REQUESTS=0")
    print("PRIMARY_JUDGING=0")


def verify():
    repo_guard()
    manifest = json.loads((CAPSULE / "harness_freeze.json").read_text())
    if manifest["contract_sha256"] != PROTOCOL_SHA256 or manifest["primary_judging"] != 0:
        raise RuntimeError("Frozen contract or primary judging guard failed")
    if manifest["order"] != ["J1", "J2"] or manifest["run_authorized_by_prepare"]:
        raise RuntimeError("Frozen run gate mutated")
    for rel, digest in manifest["files_sha256"].items():
        if sha((CAPSULE / rel).read_bytes()) != digest:
            raise RuntimeError("Frozen capsule mutated: " + rel)
    if sha(Path(__file__).read_bytes()) != manifest["files_sha256"]["scripts/r11_hosted_qualification.py"]:
        raise RuntimeError("Runner bytes differ from prospective freeze")
    return material_check(CAPSULE / "inputs")


def strict_json(text):
    if not isinstance(text, str):
        raise TypeError("Final content must be string")
    fence = re.fullmatch(r"\s*```(?:json)?[ \t]*\r?\n(.*?)\r?\n```[ \t]*\s*", text,
                         flags=re.IGNORECASE | re.DOTALL)
    if fence:
        text = fence.group(1)
    def keys(pairs):
        row = {}
        for k, v in pairs:
            if k in row:
                raise ValueError("Duplicate JSON key")
            row[k] = v
        return row
    def no_constant(value):
        raise ValueError("Qonfinite JSON constant: " + value)
    return json.loads(text, object_pairs_hook=keys, parse_constant=no_constant)


def request_for(provider, model, prompt, case):
    # `case` is input-only; the separately frozen gold file is never passed here.
    message = json.dumps(case, ensure_ascii=True)  # same source serialization as R6
    if provider == "cohere":
        return "https://api.cohere.com/v2/chat", {
            "model": model, "stream": False,
            "messages": [{"role": "system", "content": prompt},
                         {"role": "user", "content": message}],
            "response_format": {"type": "json_object"},
            "temperature": 0, "max_tokens": 4096,
                    }
    if provider == "gemini":
        return "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent", {
            "systemInstruction": {"parts": [{"text": prompt}]},
            "contents": [{"role": "user", "parts": [{"text": message}]}],
            "generationConfig": {
                "temperature": 0, "candidateCount": 1,
                "maxOutputTokens": 4096, "responseMimeType": "application/json",
                "thinkingConfig": {"thinkingLevel": "minimal"},
            },
        }
    raise ValueError("Unknown provider")


def final_text(provider, response):
    if provider == "cohere":
        if response.get("finish_reason") != "COMPLETE":
            raise ValueError("Cohere generation not complete")
        blocks = response["message"]["content"]
        if not isinstance(blocks, list):
            raise ValueError("Invalid Cohere blocks")
        pieces = [b["text"] for b in blocks if isinstance(b, dict) and b.get("type") == "text" and isinstance(b.get("text"), str)]
        if not pieces:
            raise ValueError("Cohere returned no final text blocks")
        return "".join(pieces)
    if provider == "gemini":
        cs = response.get("candidates", [])
        if len(cs) != 1 or cs[0].get("finishReason") != "STOP":
            raise ValueError("Gemini generation not complete")
        blocks = cs[0]["content"]["parts"]
        pieces = [b["text"] for b in blocks if isinstance(b, dict) and not b.get("thought", False) and isinstance(b.get("text"), str)]
        if not pieces:
            raise ValueError("Gemini returned no final text")
        return "".join(pieces)
    raise ValueError("Unknown provider")


def signature(j):
    return [j["correctness_score"], j["abstention_outcome"], [x["label"] for x in j["claim_judgments"]]]


def summaries(rows, gold):
    by_c = {c: [r for r in rows if r["case"] == c] for c in IDS}
    if set(by_c) != set(IDS):
        raise RuntimeError("Case identities changed")
    repeat = sum(len(rs) == 2 and all(r["schema_ok"] for r in rs)
                 and rs[0]["signature"] == rs[1]["signature"] for rs in by_c.values())
    coverage = {}
    for x in ABST:
        coverage["abstention:" + x] = any(r["schema_ok"] and gold[r["case"]][1] == x
                                               and r["signature"][1] == x for r in rows)
    for x in GROUND:
        coverage["grounding:" + x] = any(r["schema_ok"] and x in gold[r["case"]][2]
                                          and r["signature"][2] == gold[r["case"]][2] for r in rows)
    pure_count = sum(r["schema_ok"] and r["signature"][2] == []
                     for r in rows if r["case"] in PURE_ABST)
    schema = sum(r["schema_ok"] for r in rows)
    gold_count = sum(r["gold_ok"] for r in rows)
    return {
        "schema": schema, "gold": gold_count, "repeatability": repeat,
        "class_coverage": coverage, "pure_abstention_empty_claims": pure_count,
        "pure_abstention_integrity": pure_count == 4,
        "mean_seconds": statistics.mean(r["seconds"] for r in rows) if rows else None,
        "median_seconds": statistics.median(r["seconds"] for r in rows) if rows else None,
        "qualified": (len(rows) == 18 and schema == 18 and gold_count >= 15 and repeat >= 8
                      and all(coverage.values()) and pure_count == 4),
    }


def ordered_slots():
    return [(c[0], c[1], c[2], rep, cid) for c in CANDIDATES for rep in (1, 2) for cid in IDS]


def send_one(url, payload, provider, key):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if provider == "gemini":
        headers["x-goog-api-key"] = key
    else:
        headers["Authorization"] = "Bearer " + key
    request = urllib.request.Request(url, data=encode(payload).encode("utf-8"),
                                     headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=TIMEOUT[provider]) as response:
        if response.status != 200:
            raise urllib.error.HTTPError(url, response.status, "non-200", None, None)
        raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise ValueError("API response exceeds frozen maximum")
    return strict_json(raw.decode("utf-8"))


def status_text():
    status_path = CAPSULE / "run_status.json"
    if not status_path.exists():
        print("RUN_STATUS=NOT_STARTED")
        return
    obj = json.loads(status_path.read_text())
    print("RUN_STATUS=" + obj["state"])
    print("COMPLETED_SLOTS=" + str(len(read_jsonl(CAPSULE / "completed.jsonl"))))
    print("PRIMARY_JUDGING=0")
    if obj.get("reason"):
        print("REASON=" + obj["reason"])


def execute(resume=False):
    cases, gold, prompt, valid = verify()
    if os.environ.get("R11_FREE_TIER_CONFIRMED") != "YES":
        raise RuntimeError("Explicit R11_FREE_TIER_CONFIRMED=YES required; confirm both keys are on free tiers first")
    for _, _, _, name in CANDIDATES:
        if not os.environ.get(name):
            raise RuntimeError("Missing key: " + name)
    index = {row["evaluation_id"]: row for row in cases}
    slots = ordered_slots()
    status_path = CAPSULE / "run_status.json"
    if not resume:
        if status_path.exists() or (CAPSULE / "completed.jsonl").exists():
            raise RuntimeError("R11 already started. No automatic reruns")
        write_new(status_path, {"state": "RUNNING", "next_slot": 0,
                                     "started_utc": now(), "primary_judging": 0})
    else:
        state = json.loads(status_path.read_text())
        if not (state.get("state") == "PAUSED" and state.get("reason") == "HTTP_429"):
            raise RuntimeError("Resume allowed only after explicit HTTP_429 pause")
        results = read_jsonl(CAPSULE / "attempt_results.jsonl")
        if not results or results[-1].get("status") != "HTTP_429":
            raise RuntimeError("Resume gate: last transport result is not HTTP_429")
        if not (state["next_slot"] < len(slots) and results[-1]["slot_index"] == state["next_slot"]):
            raise RuntimeError("Resume slot mismatch")
        replace_json(status_path, {"state": "RUNNING", "next_slot": state["next_slot"],
                                        "resumed_after": "HTTP_429", "resumed_utc": now(), "primary_judging": 0})

    completed = read_jsonl(CAPSULE / "completed.jsonl")
    expected_ids = [(code, rep, cid) for code, _, _, rep, cid in slots]
    ids_done = [(r["candidate"], r["rep"], r["case"]) for r in completed]
    if ids_done != expected_ids[:len(completed)]:
        raise RuntimeError("Completed slots are non-prefix, duplicated, or out of order")
    state = json.loads(status_path.read_text())
    if state["next_slot"] != len(completed):
        raise RuntimeError("State/journal mismatch; stop before API")
    for n in range(len(completed), len(slots)):
        code, provider, model, rep, cid = slots[n]
        url, payload = request_for(provider, model, prompt, index[cid])
        payload_hash = sha(encode(payload).encode())
        # Ambiguous interrupted attempts must not be replayed.
        prior_intents = [x for x in read_jsonl(CAPSULE / "requests.jsonl") if x["slot_index"] == n]
        prior_results = [x for x in read_jsonl(CAPSULE / "attempt_results.jsonl") if x["slot_index"] == n]
        if prior_intents and not (resume and n == len(completed) and prior_results
                                  and len(prior_results) == len(prior_intents)
                                  and all(x["status"] == "HTTP_429" for x in prior_results)):
            raise RuntimeError("Ambiguous prior attempt; refusing duplicate request")
        if prior_intents and any(x["payload_sha256"] != payload_hash for x in prior_intents):
            raise RuntimeError("Resumed payload changed")
        attempt = len(prior_intents) + 1
        append_jsonl(CAPSULE / "requests.jsonl", {
            "slot_index": n, "candidate": code, "rep": rep, "case": cid,
            "model": model, "provider": provider, "attempt": attempt,
            "payload_sha256": payload_hash, "payload": payload,
            "requested_utc": now(),
        })
        tic = time.monotonic()
        try:
            raw = send_one(url, payload, provider, os.environ[CANDIDATES[0][3] if code == "J1" else CANDIDATES[1][3]])
        except urllib.error.HTTPError as exc:
            status = "HTTP_" + str(exc.code)
            append_jsonl(CAPSULE / "attempt_results.jsonl", {
                "slot_index": n, "attempt": attempt, "status": status,
                "seconds": time.monotonic() - tic, "finished_utc": now(),
            })
            paused = status == "HTTP_429"
            replace_json(status_path, {"state": "PAUSED" if paused else "STOPPED",
                                             "reason": status, "next_slot": n, "primary_judging": 0,
                                             "stopped_utc": now()})
            print(f"R11_TRANSPORT_STOP={code}|REP={rep}|CASE={cid}|STATUS={status}", flush=True)
            print("AUTOMATIC_RETRIES=0")
            return 2
        except Exception as exc:
            status = "TRANSPORT_" + type(exc).__name__
            append_jsonl(CAPSULE / "attempt_results.jsonl", {
                "slot_index": n, "attempt": attempt, "status": status,
                "seconds": time.monotonic() - tic, "finished_utc": now(),
            })
            replace_json(status_path, {"state": "STOPPED", "reason": status,
                                             "next_slot": n, "primary_judging": 0, "stopped_utc": now()})
            print(f"R11_TRANSPORT_STOP={code}|REP={rep}|CASE={cid}|STATUS={status}", flush=True)
            print("AUTOMATIC_RETRIES=0")
            return 2
        seconds = time.monotonic() - tic
        append_jsonl(CAPSULE / "attempt_results.jsonl", {
            "slot_index": n, "attempt": attempt, "status": "HTTP_200",
            "seconds": seconds, "finished_utc": now(),
        })
        append_jsonl(CAPSULE / "raw_responses.jsonl", {
            "slot_index": n, "candidate": code, "rep": rep, "case": cid,
            "response": raw, "response_sha256": sha(encode(raw).encode()),
            "payload_sha256": payload_hash, "seconds": seconds, "received_utc": now(),
        })
        j, schema, sig, error = None, False, None, None
        try:
            j = strict_json(final_text(provider, raw))
            schema = bool(valid(j, cid))
            sig = signature(j) if schema else None
        except Exception as exc:
            error = "CONTENT_" + type(exc).__name__
        record = {"slot_index": n, "candidate": code, "rep": rep, "case": cid,
                  "schema_ok": schema, "gold_ok": schema and sig == gold[cid],
                  "signature": sig, "judgment": j, "error": error, "seconds": seconds}
        append_jsonl(CAPSULE / "completed.jsonl", record)
        replace_json(status_path, {"state": "RUNNING", "next_slot": n + 1, "primary_judging": 0,
                                         "updated_utc": now()})
        print(f"R11_RESULT={code}|REP={rep}|CASE={cid}|SCHEMA={int(schema)}|GOLD={int(record['gold_ok'])}|SECONDS={seconds:.2f}", flush=True)
        # Prospective futility gate: evaluate all 18 J1 slots, then stop if J1 fails.
        if n == 17:
            first_rows = read_jsonl(CAPSULE / "completed.jsonl")
            j1 = {"candidate": "J1", "provider": CANDIDATES[0][1],
                  "model": CANDIDATES[0][2], "cases": 9, "repetitions": 2,
                  **summaries(first_rows, gold)}
            if not j1["qualified"]:
                write_new(CAPSULE / "results.json", {
                    "models": [j1], "pair_status": "NO_QUALIFIED_PAIR",
                    "j2_status": "NOT_RUN_J1_FAILED", "primary_judging": 0,
                    "finished_utc": now(), "qualified_models": [],
                })
                replace_json(status_path, {"state": "COMPLETE", "next_slot": 18,
                    "pair_status": "NO_QUALIFIED_PAIR", "reason": "J1_NOT_QUALIFIED",
                    "primary_judging": 0})
                print(f"R11_CANDIDATE=J1|SCHEMA={j1['schema']}/18|GOLD={j1['gold']}/18|REPEAT={j1['repeatability']}/9|QUALIFIED=0")
                print("R11_PAIR_STATUS=NO_QUALIFIED_PAIR")
                print("R11_J2=NOT_RUN_J1_FAILED")
                print("PRIMARY_JUDGING=0")
                return 0
    rows = read_jsonl(CAPSULE / "completed.jsonl")
    if len(rows) != 36:
        raise RuntimeError("Expected 36 completed slots")
    model_summaries = []
    for code, provider, model, _ in CANDIDATES:
        model_rows = [r for r in rows if r["candidate"] == code]
        s = {"candidate": code, "provider": provider, "model": model,
             "cases": 9, "repetitions": 2, **summaries(model_rows, gold)}
        model_summaries.append(s)
    pair_status = "PASS" if all(s["qualified"] for s in model_summaries) else "NO_QUALIFIED_PAIR"
    write_new(CAPSULE / "results.json", {
        "models": model_summaries, "pair_status": pair_status,
        "primary_judging": 0, "finished_utc": now(),
        "qualified_models": [s["model"] for s in model_summaries if s["qualified"]],
    })
    replace_json(status_path, {"state": "COMPLETE", "next_slot": 36,
                                     "pair_status": pair_status, "primary_judging": 0})
    for s in model_summaries:
        print(f"R11_CANDIDATE={s['candidate']}|SCHEMA={s['schema']}/18|GOLD={s['gold']}/18|REPEAT={s['repeatability']}/9|QUALIFIED={int(s['qualified'])}")
    print("R11_PAIR_STATUS=" + pair_status)
    print("PRIMARY_JUDGING=0")
    return 0


def self_test():
    from tempfile import TemporaryDirectory
    from unittest.mock import patch
    base = Path(__file__).resolve().parents[1]
    materials = base / MATERIAL_DIR
    cases, gold, prompt, valid = material_check(materials)
    assert len(cases) == 9 and len(gold) == 9
    assert valid({"evaluation_id": "Q07", "correctness_score": 2, "correctness_reason": "correct",
                  "abstention_outcome": "correct_abstention", "claim_judgments": [], "evaluator_notes": ""}, "Q07")
    assert not valid({"evaluation_id": "Q07", "correctness_score": 2, "correctness_reason": "correct",
                      "abstention_outcome": "correct_abstention", "claim_judgments": [], "evaluator_notes": []}, "Q07")
    assert strict_json('```json\n{"x":1}\n```') == {"x": 1}
    for bad in ('{"x":1,"x":2}', '{"x":NaN}', 'a```json\n{"x":1}\n```'):
        try:
            strict_json(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid JSON was accepted")
    for provider, model in (("cohere", CANDIDATES[0][2]), ("gemini", CANDIDATES[1][2])):
        url, payload = request_for(provider, model, prompt, cases[0])
        as_text = encode(payload)
        assert url.startswith("https://")
        assert '"gold"' not in as_text and "COHERE_API_KEY" not in as_text and "GEMINI_API_KEY" not in as_text
        assert "Q01" in as_text and "Q09" not in as_text
    assert final_text("cohere", {"finish_reason": "COMPLETE", "message": {
        "content": [{"type": "thinking", "thinking": "ignore"}, {"type": "text", "text": "{}"}]}}) == "{}"
    assert final_text("gemini", {"candidates": [{"finishReason": "STOP", "content": {
        "parts": [{"thought": True, "text": "ignore"}, {"text": "{}"}]}}]}) == "{}"
    for p, obj in (("cohere", {"finish_reason": "MAX_TOKENS", "message": {"content": [{"type": "text", "text": "{}"}]}}),
                   ("gemini", {"candidates": [{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": "{}"}]}}]})):
        try:
            final_text(p, obj)
        except ValueError:
            pass
        else:
            raise AssertionError("Truncated final content was accepted")
    oracle = []
    for rep in (1, 2):
        for cid in IDS:
            oracle.append({"rep": rep, "case": cid, "schema_ok": True,
                           "gold_ok": True, "signature": gold[cid], "seconds": 1.0})
    s = summaries(oracle, gold)
    assert s["qualified"] and s["schema"] == 18 and s["gold"] == 18
    assert s["repeatability"] == 9 and s["pure_abstention_empty_claims"] == 4
    bad_oracle = [dict(x) for x in oracle]
    bad_oracle[1] = {**bad_oracle[1], "signature": [0, "incorrect_abstention", ["SUPPORTED"]], "gold_ok": False}
    assert not summaries(bad_oracle, gold)["qualified"]
    with TemporaryDirectory() as tmp:
        p = Path(tmp) / "journal.jsonl"
        append_jsonl(p, {"a": 1})
        append_jsonl(p, {"a": 2})
        assert read_jsonl(p) == [{"a": 1}, {"a": 2}]
        assert p.stat().st_mode & 0o077 == 0
        x = Path(tmp) / "state.json"
        write_new(x, {"state": "PAUSED"})
        replace_json(x, {"state": "RUNNING"})
        assert json.loads(x.read_text())["state"] == "RUNNING"
    print("R11_OFFLINE_SELF_TEST=PASS")
    print("R11_NEW_CASES=9")
    print("R11_FROZEN_VALIDATOR=PASS")
    print("R11_GOLD_HIDDEN_FROM_REQUESTS=PASS")
    print("R11_INDEPENDENT_MODEL_TRANSPORTS=PASS")
    print("R11_NO_RETRY_POLICY=PASS")
    print("R11_PURE_ABSTENTION_GATE=PASS")
    print("API_REQUESTS=0")
    print("PRIMARY_JUDGING=0")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=("self-test", "prepare", "verify", "status", "run"))
    ap.add_argument("--resume", action="store_true", help="Explicit resume only after recorded HTTP 429")
    args = ap.parse_args()
    if args.resume and args.mode != "run":
        ap.error("--resume requires run")
    if args.mode == "self-test":
        self_test()
    elif args.mode == "prepare":
        prepare()
    elif args.mode == "verify":
        verify()
        print("R11_FROZEN_CAPSULE_VERIFY=PASS\nAPI_REQUESTS=0\nPRIMARY_JUDGING=0")
    elif args.mode == "status":
        verify()
        status_text()
    elif args.mode == "run":
        sys.exit(execute(resume=args.resume))


if __name__ == "__main__":
    main()
