# R11 — final limited prospective hosted judge qualification

Date: 2026-10-08
Status: CANDIDATE PROTOCOL — MUST BE COMMITTED AND FROZEN BEFORE INFERENCE

## Purpose and integrity

Attempt to qualify two independent LLM judges for Option C (two LLM judges plus a separate expert-human validation sample) for the existing 270-execution USN MSc benchmark. R1–R10 evidence and benchmark results stay immutable. R11 is **not** a retrospective rescue of R6 or R10, and no prior failures are relabeled PASS. No primary scoring may begin merely because this capsule is prepared.

## Prospective fixed candidate identities and order

J1 Cohere `command-a-plus-05-2026` via Chat V2, using trial `COHERE_API_KEY`.
J2 Google `gemini-3.5-flash-lite` via GenerateContent, using free-tier `GEMINI_API_KEY`.
No fallback candidates, adaptive selection, or model substitutions within R11. No paid charges, billing activation, automatic upgrades, model downloads, or local inference.

## Synthetic evaluation design

Nine independently authored R11 synthetic microcases `Q01`–`Q09` (no real project documents or 270 outputs), two repetitions per model, candidate order J1 then J2. At most 36 requests for successful transports; a journaled HTTP 429 may require an **explicit** repeat attempt for the same unfinished slot only. Cases and gold labels are independently frozen. The gold file is never sent to models. Same semantic rubric, same cases, same frozen R6/R10 validator. No prompt/answer editing after qualification begins. Before committing, check nonreuse against available historical candidate qualifications and document gaps as described in the prospective archival-evidence exception below; missing source archives are not evidence of nonreuse.

## Prospective archival-evidence exception (authorized 2026-10-08, before R11 inference)

The study owner approved this narrow documentation exception prospectively. It affects **only the completeness of historical case nonreuse verification**, not the synthetic cases, frozen gold, rubric, transport, or any scientific acceptance threshold. This exception does **not** make the original full-history nonreuse assertion PASS.

- **R6, R7, R8, R10:** archived case files were available and compared with R11 Q01–Q09; exact full-case and exact question matches were **zero** for each round. The R6/R7/R8 case archives have identical SHA256 `b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2`.
- **R5 and R9:** only one associated text/evidence file per round was found in the targeted local search; no literal R11 question matches were detected in those inspected files. This is **partial evidence**, not a complete case-set check.
- **R1–R4:** no associated files were found in that search. Case nonreuse relative to these rounds remains **UNKNOWN**, not PASS.
- No claim of exhaustive archival coverage, semantic nonreuse, or independence from all R1–R10 cases is made. This is an explicit **PARTIAL_EVIDENCE / PROSPECTIVE_EXCEPTION** accepted before any R11 live request.

R11's existing 18/18 schema, >=15/18 gold, >=8/9 repeatability, grounding coverage, abstention coverage, and pure-abstention requirements remain fully binding. Prior rounds, all 270 frozen executions, and primary judging remain unaffected. A separate go/no-go is required before R11 live inference.

## Individually mandatory scientific gates (unchanged)

- Strict schema valid: 18/18.
- Exact gold triple (`correctness_score`, `abstention_outcome`, claim grounding labels): >=15/18.
- Repeatability: >=8/9 identical two-repetition triples.
- Correctly covered abstention outcomes: correct_abstention, incorrect_abstention, failed_to_abstain.
- Correctly covered grounding labels: SUPPORTED, PARTIALLY_SUPPORTED, UNSUPPORTED, CONTRADICTED.
- Pure-abstention answers yield no asserted claim judgments, for both repetitions.

These are **pre-specified gates**, never relaxed or retuned after seeing R11 outputs. If J1 finishes all 18 slots without qualification, stop R11 and record `NO_QUALIFIED_PAIR` without sending any J2 request. If J1 succeeds, test J2. HTTP 429 pauses without automatic retries. All other transport errors STOP. No inference replay of completed or ambiguous slots. Manual `--resume` is permitted only after a fully journaled HTTP 429, if the same model/free-tier privileges and study authorization remain valid. It never repairs failures of scientific gates.

## Frozen transports

Both transports use the unchanged semantic prompt and identical input JSON case objects; no tools, retrieval, browsing or external grounding. Cohere: `/v2/chat`, JSON-object output, temperature 0, max_tokens 4096, no unsupported thinking override. Gemini: `v1beta/models/gemini-3.5-flash-lite:generateContent`, application/json output, candidateCount 1, maxOutputTokens 4096, thinkingLevel minimal, temperature 0. Hard HTTP timeout: 120s, single attempt, 4 MiB maximum provider response body. Duplicate JSON keys and nonfinite JSON constants rejected. Complete fenced JSON allowed; no other repair/coercion.

## Evidence and protection

Preserve raw provider responses and usage, request intent/payload hash, parsed judgments, exact-gold comparisons, validation, wall-clock durations, error statuses, and all file hashes in a separate R11 capsule. Retain original R6/R10 records without modification. `prepare` does not authorize inference; an explicit separate human-go/no-go after clean Git freeze and offline tests is needed. R11 `run` requires `R11_FREE_TIER_CONFIRMED=YES`, both existing keys, and the separately frozen artifacts. No inference during packaging/testing.

## Primary-study boundary

Prospective R11 qualification does not itself authorize 540 primary judgments. An additional distinct freeze must ensure context limits, daily/monthly free quotas, and permitted transmission of thesis evidence; Google free-tier data handling may permit provider model improvement. No primary documents, expert ratings, or benchmark answers may be used during R11 qualification. If R11 fails, stop candidate searching pending documented methodological review with thesis supervisor.
