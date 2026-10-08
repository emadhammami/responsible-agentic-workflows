#!/usr/bin/env python3
"""R7 prospective hosted-judge atomic qualification. No API requests except explicit 'run'.

Modes:
  self-test: local tests, no data/network
  prepare:  create a byte-frozen local capsule from the R6 synthetic input files
  verify:   verify local capsule and frozen repository contract (no network)
  run:      one-shot 36-slot at-most qualification, strict no retry/resume

Only sources of judge evidence are the nine immutable synthetic cases.
No primary benchmark paths are accepted by this program.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE_COMMIT = "1b119f2a95f65005d14cdb3632e4a4a463b49c61"
CONTRACT_REL = "evidence/engineering/llm_judge_r7_hosted_qualification_contract_2026-10-08.md"
CONTRACT_SHA = "3a43967dda1848c66641673c50cfc90f96d923565300df5f6d411f09e68c90ca"
R6 = Path.home() / "primary-benchmark-results/LLM-JUDGE-R6-QUALIFICATION-2026-10-07"
D = Path.home() / "primary-benchmark-results/LLM-JUDGE-R7-QUALIFICATION-2026-10-08"
SOURCES = {
    "prompt.txt": ("inputs/prompt.txt", "c57ad42fcef1e6382dd2b72572898a6fd21ae780bd2e9189467d6512dfeb913c"),
    "cases.json": ("inputs/cases.json", "b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2"),
    "frozen_validator.py": ("scripts/frozen_validator.py", "925891d326cc3138f74fe2198a7786df21b1bf2de8a4c9d62984c2aae72527fd"),
}
CANDIDATES = [
    ("J1", "google", "gemini-3.8-flash", "GEMINI_API_KEY"),
    ("J2", "nvidia", "nvidia/nemotron-3-ultra-550b-a55b", "NVIDIA_API_KEY"),
]
ABSTENTION = ("correct_abstention", "failed_to_abstain", "incorrect_abstention")
GROUNDING = ("SUPPORTED", "PARTIALLY_SUPPORTED", "UNSUPPORTED", "CONTRADICTED")
EXPECTED_CASES = [f"A{i:02d}" for i in range(1, 10)]


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def write_new(path, obj):
    path = Path(path)
    with path.open("x", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, ensure_ascii=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())


def append(path, obj):
    with Path(path).open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=True, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


def guard_repo():
    if git("branch", "--show-current") != "research/b1-g1-real-execution-wiring":
        raise RuntimeError("Unexpected branch; stop")
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD"], check=True)
    if git("status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Dirty repository; stop")
    if sha(Path(CONTRACT_REL).read_bytes()) != CONTRACT_SHA:
        raise RuntimeError("R7 prospective contract mutated; stop")


def verify_cases(cases):
    if not isinstance(cases, list) or len(cases) != 9:
        raise ValueError("Exact nine synthetic cases required")
    if [x[0] for x in cases] != EXPECTED_CASES:
        raise ValueError("Frozen case order changed")
    for x in cases:
        if not isinstance(x, list) or len(x) != 7 or not isinstance(x[6], list) or len(x[6]) != 3:
            raise ValueError("Frozen case schema unexpected")
        if not (isinstance(x[6][0], int) and not isinstance(x[6][0], bool)):
            raise ValueError("Gold score type unexpected")
    return True


def prepare():
    guard_repo()
    if D.exists():
        raise RuntimeError("R7 capsule already exists. No overwrite; inspect with verify.")
    for name, (rel, expected_sha) in SOURCES.items():
        p = R6 / rel
        if sha(p.read_bytes()) != expected_sha:
            raise RuntimeError("R6 immutable material mismatch: " + name)
    # All guards precede any write; D.mkdir is the only initial mutation.
    D.mkdir(mode=0o700, parents=False, exist_ok=False)
    (D / "inputs").mkdir()
    (D / "scripts").mkdir()
    pinned = {}
    for name, (rel, expected_sha) in SOURCES.items():
        target = D / ("scripts/" if name.endswith(".py") else "inputs/") / name
        target.write_bytes((R6 / rel).read_bytes())
        pinned[str(target.relative_to(D))] = expected_sha
    runner = Path(__file__).resolve()
    runner_dst = D / "scripts/r7_hosted_qualification.py"
    runner_dst.write_bytes(runner.read_bytes())
    pinned["scripts/r7_hosted_qualification.py"] = sha(runner.read_bytes())
    frozen_contract = D / "inputs/llm_judge_r7_hosted_qualification_contract_2026-10-08.md"
    frozen_contract.write_bytes(Path(CONTRACT_REL).read_bytes())
    pinned[str(frozen_contract.relative_to(D))] = CONTRACT_SHA
    write_new(D / "harness_freeze.json", {
        "frozen_at_utc": now(), "repo_head": git("rev-parse", "HEAD"),
        "prospective_contract_commit": BASE_COMMIT,
        "primary_llm_judge_runs": 0, "files_sha256": pinned,
        "candidate_order": [x[0] for x in CANDIDATES],
        "run_authorized": False,
    })
    print("R7_HARNESS_FROZEN=YES")
    print("R7_CAPSULE=" + str(D))
    print("RUN_AUTHORIZED_BY_PREPARE=NO")
    print("API_REQUESTS=0")


def verify():
    guard_repo()
    manifest = json.loads((D / "harness_freeze.json").read_text())
    if manifest.get("primary_llm_judge_runs") != 0 or manifest.get("candidate_order") != ["J1", "J2"]:
        raise RuntimeError("Frozen manifest is inconsistent")
    for rel, expected in manifest["files_sha256"].items():
        if sha((D / rel).read_bytes()) != expected:
            raise RuntimeError("Frozen material changed: " + rel)
    if sha(Path(__file__).resolve().read_bytes()) != manifest["files_sha256"]["scripts/r7_hosted_qualification.py"]:
        raise RuntimeError("Invoking an unfrozen runner; stop")
    cases = json.loads((D / "inputs/cases.json").read_text())
    verify_cases(cases)
    # Load audited, byte-identical *pure* validator module; does not read primary data.
    p = D / "scripts/frozen_validator.py"
    spec = importlib.util.spec_from_file_location("r7_pinned_validator", p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, "valid", None)):
        raise RuntimeError("Frozen validator cannot be loaded")
    return cases, (D / "inputs/prompt.txt").read_text(), module.valid


def user_message(case):
    cid, q, generated, reference, ref_ev, retrieved_ev, _ = case
    obj = {
        "evaluation_id": cid,
        "question": q,
        "generated_output": generated,
        "reference_answer": reference,
        "reference_evidence": [{"text": ref_ev}],
        "retrieved_evidence": [{"text": retrieved_ev}],
    }
    return json.dumps(obj)   # frozen R6 default serialization and insertion order


def request(provider, model, prompt, user):
    if provider == "google":
        payload = {
            "systemInstruction": {"parts": [{"text": prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {
                "temperature": 0, "topP": 1, "maxOutputTokens": 8192,
                "candidateCount": 1,
                "thinkingConfig": {"thinkingLevel": "medium"},
            },
        }
        return "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent", payload
    if provider == "nvidia":
        payload = {
            "model": model,
            "messages": [{"role": "system", "content": prompt},
                         {"role": "user", "content": user}],
            "temperature": 0, "top_p": 1, "max_tokens": 8192,
            "reasoning_effort": "medium", "reasoning_budget": 4096,
            "stream": False,
        }
        return "https://integrate.api.nvidia.com/v1/chat/completions", payload
    raise ValueError("Unknown provider")


def strict_json(s):
    if not isinstance(s, str):
        raise TypeError("Judgment final content must be string")
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise ValueError("Duplicate JSON key: " + str(k))
            out[k] = v
        return out
    def invalid_constant(x):
        raise ValueError("Nonfinite JSON constant: " + x)
    return json.loads(s, object_pairs_hook=pairs, parse_constant=invalid_constant)


def final_text(provider, response):
    if provider == "google":
        cs = response["candidates"]
        if len(cs) != 1 or cs[0].get("finishReason") != "STOP":
            raise ValueError("Gemini failed/truncated: " + str(cs[0].get("finishReason") if cs else "empty"))
        parts = cs[0]["content"]["parts"]
        texts = [p["text"] for p in parts if isinstance(p, dict) and not p.get("thought", False) and "text" in p]
        if not texts:
            raise ValueError("No final text in Gemini response")
        return "".join(texts)
    choices = response["choices"]
    if len(choices) != 1 or choices[0].get("finish_reason") != "stop":
        raise ValueError("NVIDIA failed/truncated: " + str(choices[0].get("finish_reason") if choices else "empty"))
    return choices[0]["message"]["content"]


def signature(j):
    return [j["correctness_score"], j["abstention_outcome"], [x["label"] for x in j["claim_judgments"]]]


def summarize(rows, cases):
    golds = {c[0]: c[6] for c in cases}
    by_case = {cid: [r for r in rows if r["case"] == cid] for cid in golds}
    repeat = sum(len(rs) == 2 and all(r["schema_ok"] for r in rs) and rs[0]["signature"] == rs[1]["signature"] for rs in by_case.values())
    coverage = {}
    for label in ABSTENTION:
        coverage["abstention:" + label] = any(r["schema_ok"] and golds[r["case"]][1] == label and r["signature"][1] == label for r in rows)
    for label in GROUNDING:
        coverage["grounding:" + label] = any(r["schema_ok"] and label in golds[r["case"]][2] and r["signature"][2] == golds[r["case"]][2] for r in rows)
    schema = sum(r["schema_ok"] for r in rows)
    gold = sum(r["gold_ok"] for r in rows)
    return {"schema": schema, "gold": gold, "repeatability": repeat,
            "class_coverage": coverage,
            "pure_abstention_empty_claims": sum(r["schema_ok"] and r["signature"][2] == [] for r in rows if r["case"] in ("A04", "A06")),
            "mean_seconds": statistics.mean(r["seconds"] for r in rows),
            "median_seconds": statistics.median(r["seconds"] for r in rows),
            "qualified": len(rows) == 18 and schema == 18 and gold >= 15 and repeat >= 8 and all(coverage.values())}


def send_one(url, payload, provider, api_key):
    # Authentication only in HTTP headers, never in URL/body/telemetry.
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if provider == "google":
        headers["x-goog-api-key"] = api_key
    else:
        headers["Authorization"] = "Bearer " + api_key
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        status = resp.status
        body = resp.read(12 * 1024 * 1024 + 1)
        if len(body) > 12 * 1024 * 1024:
            raise ValueError("Oversized API response")
    if status != 200:
        raise urllib.error.HTTPError(url, status, "Unexpected non-200 API status", None, None)
    return json.loads(body)


def count_rows(path):
    return sum(1 for _ in path.open(encoding="utf-8")) if path.exists() else 0


def run():
    cases, prompt, valid = verify()
    if any((D / x).exists() for x in ("run_started.json", "results.json", "run_status.json")):
        raise RuntimeError("Run already attempted; no rerun or resume")
    if any((D / code).exists() for code in ("J1", "J2")):
        raise RuntimeError("Candidate directory already exists; no overwrite")
    for _code, _provider, _model, key in CANDIDATES:
        if not os.environ.get(key):
            raise RuntimeError("Missing API key: " + key)
    write_new(D / "run_started.json", {"started_utc": now(), "explicit_run_invocation": True, "primary_llm_judge_runs": 0})
    summaries = []
    for code, provider, model, key_env in CANDIDATES:
        folder = D / code
        folder.mkdir(mode=0o700)
        rows = []
        for rep in (1, 2):
            for case in cases:
                cid = case[0]
                url, payload = request(provider, model, prompt, user_message(case))
                slot = {"candidate": code, "rep": rep, "case": cid, "model": model,
                        "provider": provider, "request_sha256": sha(json.dumps(payload).encode()),
                        "url": url, "payload": payload, "started_utc": now()}
                # Write ahead to prevent silent replay after interruption or ambiguous delivery.
                append(folder / "requests.jsonl", slot)
                start = time.monotonic()
                raw, error, j, ok, sig = None, None, None, False, None
                transport_stop = False
                try:
                    raw = send_one(url, payload, provider, os.environ[key_env])
                    content = final_text(provider, raw)
                    j = strict_json(content)
                    ok = bool(valid(j, cid))
                    if ok:
                        sig = signature(j)
                except urllib.error.HTTPError as e:
                    error = "HTTP_ERROR_" + str(e.code)
                    transport_stop = True
                except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                    error = "TRANSPORT_ERROR_" + type(e).__name__
                    transport_stop = True
                except Exception as e:
                    error = "CONTENT_OR_PROTOCOL_ERROR_" + type(e).__name__ + ": " + str(e)[:160]
                elapsed = time.monotonic() - start
                append(folder / "raw_responses.jsonl", {"candidate": code, "rep": rep, "case": cid,
                        "request_sha256": slot["request_sha256"], "response": raw,
                        "error": error, "seconds": elapsed, "finished_utc": now()})
                row = {"rep": rep, "case": cid, "schema_ok": ok,
                       "gold_ok": bool(ok and sig == case[6]), "signature": sig,
                       "judgment": j, "error": error, "seconds": elapsed}
                append(folder / "parsed_judgments.jsonl", row)
                rows.append(row)
                print(f"R7_RESULT={code}|REP={rep}|CASE={cid}|SCHEMA={int(ok)}|GOLD={int(row['gold_ok'])}|SEC={elapsed:.2f}" + ("|ERROR=" + error if error else ""), flush=True)
                if transport_stop:
                    status = {"candidate": code, "status": "INCOMPLETE_TRANSPORT_OR_QUOTA",
                              "completed_slots": len(rows), "primary_llm_judge_runs": 0,
                              "reason": error, "stopped_at_utc": now()}
                    write_new(D / "run_status.json", status)
                    print("R7_STATUS=INCOMPLETE_TRANSPORT_OR_QUOTA")
                    print("NO_RETRY_PERFORMED=YES")
                    return 2
        summary = {"code": code, "provider": provider, "model": model,
                   "n_scheduled": 18, **summarize(rows, cases)}
        write_new(folder / "summary.json", summary)
        summaries.append(summary)
        print(f"R7_CANDIDATE={code}|SCHEMA={summary['schema']}/18|GOLD={summary['gold']}/18|REPEAT={summary['repeatability']}/9|QUALIFIED={int(summary['qualified'])}", flush=True)
    pair_status = "PASS" if len(summaries) == 2 and all(x["qualified"] for x in summaries) else "INSUFFICIENT_QUALIFIED_MODELS"
    write_new(D / "results.json", {"models": summaries, "qualified_count": sum(x["qualified"] for x in summaries),
               "pair_status": pair_status, "completed_at_utc": now(), "primary_llm_judge_runs": 0})
    print("R7_FINAL_PAIR_STATUS=" + pair_status)
    print("PRIMARY_LLM_JUDGE_RUNS=0")
    return 0


def self_test():
    obj = {"a": 1}
    assert strict_json(json.dumps(obj)) == obj
    for s in ('{"a":1,"a":2}', '{"a":NaN}', '```json\n{}\n```'):
        try:
            strict_json(s)
        except (ValueError, json.JSONDecodeError):
            pass
        else:
            raise AssertionError("Strict parser accepted invalid form")
    sys_prompt = "synthetic system"
    case = ["A01", "question", {"text": "answer"}, "reference", "gold", "evidence", [2, "not_applicable", ["SUPPORTED"]]]
    um = user_message(case)
    assert list(json.loads(um)) == ["evaluation_id", "question", "generated_output", "reference_answer", "reference_evidence", "retrieved_evidence"]
    for provider, model in (("google", CANDIDATES[0][2]), ("nvidia", CANDIDATES[1][2])):
        url, p = request(provider, model, sys_prompt, um)
        assert url.startswith("https://") and "secret" not in json.dumps(p)
    assert final_text("google", {"candidates": [{"finishReason": "STOP", "content": {"parts": [{"thought": True, "text": "invisible"}, {"text": "{}"}]}}]}) == "{}"
    assert final_text("nvidia", {"choices": [{"finish_reason": "stop", "message": {"content": "{}"}}]}) == "{}"
    for name, response in (("google", {"candidates": [{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": "{}"}]}}]}),
                           ("nvidia", {"choices": [{"finish_reason": "length", "message": {"content": "{}"}}]})):
        try:
            final_text(name, response)
        except ValueError:
            pass
        else:
            raise AssertionError("Accepted truncated response")
    print("R7_OFFLINE_SELF_TEST=PASS")
    print("API_REQUESTS=0")
    print("PRIMARY_LLM_JUDGE_RUNS=0")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("self-test", "prepare", "verify", "run"))
    args = parser.parse_args()
    if args.mode == "self-test":
        self_test()
    elif args.mode == "prepare":
        prepare()
    elif args.mode == "verify":
        verify()
        print("R7_FROZEN_CAPSULE_VERIFIED=YES")
        print("API_REQUESTS=0")
    elif args.mode == "run":
        return run()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("R7_ABORT=" + type(e).__name__ + ": " + str(e), file=sys.stderr)
        sys.exit(1)
