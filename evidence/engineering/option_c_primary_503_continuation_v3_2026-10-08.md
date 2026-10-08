# USN MSc — Option C V3: prospectively frozen continuation after journaled HTTP 503

**Status:** PENDING COMMIT / FREEZE. This protocol must be committed before any new V3 inference. V2 remains read-only and STOPPED; V1 and R1–R11 also remain unchanged.

## Observed V2 evidence before this protocol

- The source remains SHA256 `3c2021037eeb39cec5ff90e212edf077fc17b3183e11ba2af44395b57ce26dec`, 270 blinded items, 540 intended judge slots, provisional/unqualified ratings.
- V2 froze output budget 16,384 and produced **five** schema-valid completions at slots 0–4 (three Cohere and two Gemini) including the two sentinel completions. The next request was Gemini J2 for I003 at zero-indexed slot **5**, with explicit journaled HTTP 503, producing `STOPPED`, `next_slot=5`, `reason=HTTP_503`. This is an HTTP service response, not a quality score. The next slot was **not completed**.
- Previous V2 protocol explicitly disallowed resuming after HTTP 503. The user explicitly authorized V3 prospective continuation on 2026-10-08 after the failure. V3 does not reinterpret a V2 failure as success or edit V2.

## Fixed V3 continuation

- Independently versioned private capsule: `~/primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V3`.
- At `prepare`, verify V2 git/frozen source identities and V1 provenance; require the **exact** V2 STOPPED HTTP 503 state, ordered 6 request intents and 6 recorded outcomes, the first 5 schema-valid completions and 5 corresponding raw responses, and the sole pending HTTP 503 attempt at J2/I003, slot 5.
- Copy all V2 journal files and private ID map **byte-for-byte** into the new V3 capsule; pin SHA256 for each V2 file (including status and original freeze) and source/runner/prompt/validator/protocol. Never modify source, V1, V2, or R11. Detect any change in the protected V2 files or copied prefixes before each V3 request.
- Resume at zero-indexed slot 5 (sixth intended judgment), **not** at slot 0. The pending HTTP 503 is the first recorded attempt for that slot. Require the exact payload SHA256; successful first five outputs are never retransmitted.
- Allow **one additional attempt after a journaled HTTP 503 for the affected slot** with a 30-second wait before a retry. For later slots, a first HTTP 503 permits one automatic retry after a 30-second wait; another HTTP 503 causes STOP. Never auto-retry HTTP 429 (manual explicit resume only), invalid JSON/schema, timeouts, exceptions with ambiguous request completion, other HTTP codes, or any successful slot. Every request intent, outcome and raw response is journaled.
- No changes to the models (`command-a-plus-05-2026`, `gemini-3.5-flash-lite`), prompt, rubric, opaque item IDs, serialization, blinded source, input fields, temperature, validator, maximum output tokens (16,384), free/privacy gates or request timeout. Retain original per-provider pacing. This exception changes only the journaled HTTP 503 continuation policy and creates versioned provenance.
- One explicit authorization gates V3 `continue`; no launch if the worktree is not clean, the protocol/scripts are not committed, hashes differ, input differs, five prior completions are not exact, or free-tier/data-sharing permissions are absent.
- If a V3 run stops, do not rerun `continue`. `resume` is available **only after a fully journaled HTTP 429** with fresh explicit authorization. Persistent HTTP 503, schema errors, and other failures STOP without further automatic or manual replay.

## Methodological boundaries

- These are exploratory/provisional **unqualified** LLM judgments until externally validated against the matched blinded human expert sample. The technical sentinel only established JSON/transport viability, not scientific accuracy. Report V1 truncated output, V2 HTTP 503, the V3 prospective restart protocol and the effect of retries in the thesis. Do not treat model agreement as proof of correctness.
- Do not infer superiority of B0/B1/G1 solely from provisional automated scores. Resource/latency statistics remain frozen and separate. Do not silently delete failed attempts, tune on model scores, or change the source order/selection.
- No paid API path, billing activation, new models, production modifications, or public Git push.
