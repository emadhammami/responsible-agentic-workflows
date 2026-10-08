# USN MSc — Prospective Option C primary judging amendment

**Status:** ACTIVE only when this document and its runner are committed and their hashes frozen **before the first primary LLM call**. This is not an amendment to R1–R11 findings.

## Research integrity

- Keep all 270 execution artifacts, task assignments, original scoring rubric, frozen metrics, R1–R11 qualifications, and human expert site untouched.
- Option C retains two independent hosted LLM judges and independently acquired expert human validation. Neither judge is characterized as qualified under R11: Cohere Command A+ failed (14/18 Gold, 6/9 repeatability); Gemini 3.5 Flash Lite was untested in R11.
- **Explicit methodological deviation:** earlier qualification-first gate is not claimed to have passed. Primary LLM scores under this amendment are **provisional exploratory automated annotations**, not validated ground truth or a confirmatory comparison of B0/B1/G1. Model agreement alone does not establish correctness.
- Independently collected expert labels remain blinded to both models. Publish model-to-human agreement and mismatches only on verified matching cases; if inadequate/unavailable, do not claim validated full-corpus quality results.

## Fixed evaluation

- Exactly 270 source records from `evaluator_A_blinded_270.jsonl`, source SHA256 `3c2021037eeb39cec5ff90e212edf077fc17b3183e11ba2af44395b57ce26dec`; independently judge each item once with each judge: 540 planned judgments.
- J1 Cohere `command-a-plus-05-2026`, J2 Google `gemini-3.5-flash-lite`. These are distinct providers and use independent requests and results; no shared model output in prompts.
- Use the **existing R11 prompt and validator** for unchanged output score definitions: correctness 0/1/2 relative to reference answer/evidence, abstention outcomes (four categories), and per-factual-claim grounding SUPPORTED/PARTIALLY_SUPPORTED/UNSUPPORTED/CONTRADICTED relative exclusively to retrieved evidence.
- Never invent missing claims, use reference evidence to assess grounding, or create factual-claim annotations for pure abstention.
- Same exact blinded item for both judges; sender remaps original `evaluation_id` to opaque `I001`..`I270`, and includes only `question`, `generated_output`, `reference_answer`, `reference_evidence`, `retrieved_evidence` plus the opaque ID. Excludes original IDs, original `judgment`, task IDs/types, and any arm mapping. The key-to-original mapping stays privately outside Git.
- Keep source order unchanged, freeze model/prompt/runner/source identities, response transport parameters, and strict schema. Do not change them on the basis of observed primary scores.

## Transport and journaling

- Use the already-frozen R11 Cohere V2/Gemini GenerateContent transport request and extraction, temperature 0, output token limit 4096, 120-second timeout, no automatic retry or JSON repair.
- Private capsule outside Git (`~/primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V1`) with source/code/protocol hashes, local opaque-ID mapping, request-intent journal (written durably **before** HTTP), response hashes/raw responses, validator outputs, response status, timing and provider-reported usage where available.
- `audit`, `mock-test`, `prepare`, `verify`, and `status` make **zero API calls**. Only explicitly authorized `sentinel`, `bulk`, and `resume` can contact providers; both private-data-sharing and free-tier confirmations are required each process.
- First real primary sentinel is exactly item I001 judged once independently by each model. Stop if either schema or transport fails; no prompt/model tuning after inspecting results. After a successful sentinel, `bulk` processes the remaining items, one request at a time.
- HTTP 429 is journaled as a definite rejection and paused; only an explicit manual `resume` may repeat that same incomplete slot. Any other transport exception, timeout, ambiguous journal, or schema failure stops without automatic rerun.
- Never replay successful/completed slots or silently substitute a model. Do not copy raw document/judge data into Git, console logs, or public reports.

## Mandatory authorization before first live sentinel

1. Verify all 270 real records and the exact frozen blinded payload schema and IDs without printing their content; no hidden condition-identifying metadata in sent input.
2. Confirm institutional/data-owner permission to transmit *source documents, retrieval snippets, reference answers and evidence* to **both Cohere and Google**, and accept each provider's data-handling terms; Free Tier status is not consent to share. Document the privacy decision privately.
3. Reconfirm free quota and no billable fallback: Cohere Trial and Google Free Tier; inspect Google current project RPM/TPM/RPD (previously 15/250k/500) and Cohere remaining monthly trial limit. Source estimate 5.1–6.7M input tokens for two judges, plus outputs; quotas may vary.
4. Verify exact source SHA, Git commit/clean state, prospective method and runner hashes; complete synthetic mock tests. Only then run the two-item sentinel with explicit permission. User separately authorizes full bulk after checking sentinel metadata, not after optimizing prompts on sentinel scores.

## Reporting boundaries

- Execution resource/latency results derive from frozen 270 execution runs, never judge cost/latency; distinguish task-level paired comparisons and the T017 concentration.
- Automated quality scores are provisional; report missing judgments/transport failures, judge disagreements and expert comparison with denominators, appropriate agreement measures and uncertainty. Never report overall quality superiority as validated absent suitable independent evidence.
- The source package and R11 remain immutable. This amendment's presence in Git alone does not authorize external transmission.
