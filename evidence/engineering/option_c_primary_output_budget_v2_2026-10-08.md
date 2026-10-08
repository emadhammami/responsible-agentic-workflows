# USN MSc — Option C V2: prospective output-budget-only technical remediation

**Status:** PENDING FREEZE; only ACTIVE after exact file hashes, Git commit and private V2 capsule are verified before the first V2 inference call. Does not alter or retroactively amend Option C V1, R1–R11, or benchmark execution artifacts.

## Evidence and motivation

- Option C V1 source SHA256: `3c2021037eeb39cec5ff90e212edf077fc17b3183e11ba2af44395b57ce26dec`; 270 blinded records; 540 intended evaluations.
- First V1 primary sentinel response: Cohere J1 I001, HTTP 200, finish_reason=`MAX_TOKENS`, `schema_ok=false`, resulting in `STOPPED`, next slot=1, `INVALID_JUDGMENT_SCHEMA`. J2 was not contacted. V1 generated *no valid* primary quality judgment.
- V1 transport requested 4,096 output tokens. This is a response-budget exhaustion, **not evidence that generated judgments are correct** or that Cohere is qualified. V1 capsule and all six freeze/journal/status files remain immutable. Never delete or rerun V1.
- Cohere Command A+ supports up to 64K output tokens and Gemini 3.5 Flash-Lite up to 65,536; the new budget 16,384 is below both documented model limits. This prospective V2 is motivated only by V1 technical metadata (not its response content, Gold labels or a quality score).

## V2 fixed protocol

- New, independent private capsule: `~/primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V2`, never overwrite V1.
- Fresh V2 pass includes the original 270 frozen blinded items, once per independently requested Cohere (`command-a-plus-05-2026`) and Gemini (`gemini-3.5-flash-lite`), in the same order; up to 540 new calls. V2's I001 request is explicitly **a new versioned attempt after V1 truncation**, not an unrecorded or implied retry under V1 rules. V1 I001 invalid record must remain visible in provenance and limitations.
- **Only transport change:** `max_tokens` (Cohere) and `maxOutputTokens` (Gemini) increase from 4096 to 16384. Everything else remains exactly as V1: original source SHA, models/providers, serialisation, exact R11 prompt and validator, temperature, thinking configuration, per-case inputs and blinding, rubric, journal and one-attempt-per-slot semantics, 120-second timeout, free-tier and data-sharing gates.
- Never read V1 raw judgment content for tuning, use partial JSON as a score, repair JSON post hoc, revise the rubric, alter claim segmentation, or tune on V2 outcomes.
- `prepare` and every `verify`/live run verify V1 is exactly the expected truncated state and pin SHA256 of the V1 capsule files; STOP if V1 records change.
- Before first new V2 call, require offline tests, committed clean branch, and a fresh V2 `prepare` and `verify`; separate user authorization for the two-call sentinel and thereafter bulk. No automatic retries. Only journaled HTTP 429 may be explicitly resumed; other failures STOP without rerun.
- Preserve public-document/data-owner permission to transmit all five fields and the trial/free-tier conditions; no paid fallback, no model substitution.

## Scientific reporting

- Option C models remain **unqualified** per R11, so all V2 LLM annotations remain provisional/exploratory pending independent human validation. Judge–human agreement must be measured on matching blinded cases, not assumed.
- Report V1 first-item output truncation and the subsequent pre-registered V2 adjustment transparently. Do not pool invalid V1 output into V2 estimates or suppress missingness.
- No general B0/B1/G1 quality superiority claim is validated until supported by human expert agreement and uncertainty analysis. Frozen resource/latency metrics remain separate from judging runtime.
