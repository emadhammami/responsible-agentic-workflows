# USN MSc Option C V4 — continuation after an invalid claim-judgment list

**Status:** PROPOSED; must be committed and frozen before any V4 inference. The user already authorized running the original 540-slot provisional primary scoring; V4's change is a new, separately authorized continuation. V1/V2/V3 remain immutable.

## Trigger (already observed)

- V3 on 2026-10-08 stopped at `next_slot=18`, `INVALID_JUDGMENT_SCHEMA`.
- Its first 18 HTTP 200 responses are recorded, with 17 schema-valid and one invalid response (J2, `I009`, zero-indexed slot 17).
- Diagnostic read-only analysis: Gemini finished normally (`STOP`), returned syntactically valid JSON matching the frozen R11 validator, but output `claim_judgments=[]` for an `answer` with nonempty text. Thus the **additional primary purity/coverage gate** rejected the judgment. This is an invalid/missing judgment, **not** a zero correctness score.
- No model restart, prompt/label/schema repair, or re-scoring of historical outputs is authorized.

## One change, forward-looking continuation

- New capsule `OPTION-C-PRIMARY-PROVISIONAL-V4`; take read-only SHA256 snapshots of the exact stopped V3 capsule (7 evidence files), verify parent V2 provenance and the precise slot 17 failure, and copy the original journals and ID map byte-for-byte. Never edit R1–R11, V1, V2, V3, the benchmark, or the evaluation package.
- Continue from **zero-indexed slot 18** (19th intended judgment); never retransmit any prior HTTP 200 response, including the invalid one.
- For subsequent HTTP 200 responses, keep the frozen R11 validator, original `answer`/`abstention` claim-integrity gates, same opaque IDs, order, models, prompt, input serialization, temperatures, output budget 16,384 and free/privacy gates. Mark any invalid response `schema_ok=false`, record its reason and retain raw evidence, **but continue to the next slot**. Invalid responses must never receive numeric quality scores, must not be imputed, normalized into valid judgments, or treated as eligible for a matched-judge comparison.
- This is a **post-failure explicitly versioned amendment**, not a prospective qualification of the already-observed slot. V3 remains STOPPED; V4 preserves the original raw failure.
- Continue V3's strict transport policy: journal before send; at most one additional attempt after definite HTTP 503 (30-second delay), explicit manual resume only for an unambiguous journaled HTTP 429, STOP for ambiguous timeouts or other transport failures. Never replay completed HTTP 200 slots. On completion report total valid/invalid and per-judge coverage, with missingness sensitivity and external human validation before any conclusions about quality.
- Ratings remain **provisional and unqualified**. If coverage or validity is inadequate, restrict conclusions accordingly; two models' agreement does not establish truth. Resources and latency remain separately frozen.
- No paid API calls, new models, production actions, or remote Git push.
