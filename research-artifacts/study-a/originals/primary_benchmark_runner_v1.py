import json, sys, time, hashlib
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "src"))

from responsible_agentic_workflows.benchmark.tasks import load_runtime_task
from responsible_agentic_workflows.benchmark.orchestration import execute_primary_runtime_task
from responsible_agentic_workflows.logging import validate_run_record
from responsible_agentic_workflows.retrieval.materialize import load_embedding_artifacts
from responsible_agentic_workflows.benchmark.legacy_uc2 import load_legacy_uc2_artifacts

EXPECTED_HEAD = "872f8de38c79a78e4e016cedf5597bc21323a374"
CODE_REV = "58b9e656dd57e62a5fb8640c2d3c990e4c93e530"
ORDER = ROOT / "evidence/engineering/primary_execution_order_v1.json"
OUTDIR = Path('/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1/run_records')

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def uc_for(task_id):
    n = int(task_id[1:])
    return "UC1" if n <= 10 else "UC2" if n <= 20 else "UC3"

def paths_for(uc):
    config = ROOT / f"benchmark/config/primary/benchmark-config-primary-{uc.lower()}-v0.2.json"
    cfg = json.loads(config.read_text())
    rid = cfg["retrieval"]["retrieval_config_id"]
    retrieval = ROOT / f"benchmark/config/retrieval/{rid}.json"

    base = ROOT / f"corpus/use_cases/{uc}/processed"

    if uc in {"UC1","UC3"}:
        chunk_dir = base / "chunks"
        candidates = []
        for emb in base.rglob("embeddings.npy"):
            d = emb.parent
            try:
                load_embedding_artifacts(
                    chunk_directory=chunk_dir,
                    artifact_directory=d,
                    retrieval_config_path=retrieval,
                )
                candidates.append(d)
            except Exception:
                pass
        assert len(candidates) == 1, (uc, candidates)
        return dict(
            config_path=config,
            retrieval_config_path=retrieval,
            artifact_directory=candidates[0],
            chunk_directory=chunk_dir,
        )

    chunks = base / "UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl"
    assert sha(chunks) == "b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2"

    artifact_candidates = []
    for emb in base.rglob("embeddings.npy"):
        if sha(emb) == "621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f":
            artifact_candidates.append(emb.parent)
    assert len(artifact_candidates) == 1, artifact_candidates
    artifact = artifact_candidates[0]

    valid = []
    for inv in (ROOT / "corpus/use_cases/UC2").rglob("source_inventory.tsv"):
        try:
            load_legacy_uc2_artifacts(
                chunks_path=chunks,
                artifact_directory=artifact,
                retrieval_config_path=retrieval,
                source_inventory_path=inv,
            )
            valid.append(inv)
        except Exception:
            pass
    assert len(valid) == 1, valid

    return dict(
        config_path=config,
        retrieval_config_path=retrieval,
        artifact_directory=artifact,
        chunks_path=chunks,
        source_inventory_path=valid[0],
    )

def main():
    import subprocess
    head = subprocess.check_output(["git","rev-parse","HEAD"], text=True).strip()
    assert head == EXPECTED_HEAD, head
    assert not subprocess.check_output(["git","status","--porcelain"], text=True).strip()

    manifest = json.loads(ORDER.read_text())
    runs = manifest["runs"]
    assert len(runs) == 270
    assert [r["execution_sequence"] for r in runs] == list(range(1,271))

    runtime_paths = {uc: paths_for(uc) for uc in ("UC1","UC2","UC3")}
    print("RUNTIME_PATH_RESOLUTION=PASS", flush=True)
    for uc, p in runtime_paths.items():
        print(uc, {k:str(v) for k,v in p.items()}, flush=True)

    # Validate/load all RuntimeTasks before first primary call.
    tasks = {}
    for n in range(1,31):
        tid = f"T{n:03d}"
        uc = uc_for(tid)
        task = load_runtime_task(ROOT / f"benchmark/tasks/{uc}/{tid}.json")
        assert task.task_id == tid
        tasks[tid] = task
    print("RUNTIME_TASK_ISOLATION_30=PASS", flush=True)

    OUTDIR.mkdir(parents=True, exist_ok=True)

    # Resume only from an exact valid prefix.
    completed = 0
    for r in runs:
        out = OUTDIR / r["output_relative_path"]
        if not out.exists():
            break
        rec = json.loads(out.read_text())
        validate_run_record(rec)
        assert rec["run_id"] == r["run_id"]
        assert rec["task_id"] == r["task_id"]
        assert rec["condition"] == r["condition"]
        assert rec["experiment_id"] == r["experiment_id"]
        assert rec["code_revision"] == CODE_REV
        completed += 1

    expected_existing = {
        runs[i]["output_relative_path"] for i in range(completed)
    }
    actual_existing = {p.name for p in OUTDIR.glob("*.json")}
    assert actual_existing == expected_existing, (
        "Non-prefix/unexpected existing outputs",
        actual_existing - expected_existing,
    )

    print(f"RESUME_PREFIX={completed}/270", flush=True)
    start = time.monotonic()

    for idx in range(completed, 270):
        r = runs[idx]
        uc = uc_for(r["task_id"])
        out = OUTDIR / r["output_relative_path"]

        print(
            f"RUN_START {idx+1}/270 "
            f"seq={r['execution_sequence']} "
            f"run_id={r['run_id']} uc={uc}",
            flush=True,
        )

        t0 = time.monotonic()
        try:
            record = execute_primary_runtime_task(
                task=tasks[r["task_id"]],
                use_case_id=uc,
                condition=r["condition"],
                run_id=r["run_id"],
                experiment_id=r["experiment_id"],
                code_revision=CODE_REV,
                output_path=out,
                **runtime_paths[uc],
            )
        except Exception as exc:
            print(
                f"UNPERSISTED_EXECUTION_EXCEPTION seq={idx+1} "
                f"type={type(exc).__name__} error={exc!r}",
                flush=True,
            )
            return 2

        dt = time.monotonic() - t0
        done = idx + 1
        elapsed = time.monotonic() - start
        new_done = done - completed
        avg = elapsed / new_done
        eta = avg * (270 - done)

        print(
            f"RUN_COMPLETE {done}/270 "
            f"run_id={r['run_id']} status={record['status']} "
            f"run_seconds={dt:.1f} "
            f"elapsed_min={elapsed/60:.1f} "
            f"eta_min={eta/60:.1f}",
            flush=True,
        )

    print("PRIMARY_EXECUTION_COMPLETE=YES", flush=True)
    print("PERSISTED_RECORDS=270", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
