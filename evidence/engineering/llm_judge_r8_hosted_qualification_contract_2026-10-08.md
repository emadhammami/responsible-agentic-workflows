# R8 prospective hosted-judge qualification protocol — 2026-10-08

Status: PROSPECTIVE; freeze this document, exact harness bytes, inputs and validator before any R8 inference.

## Audit provenance and motivation

R7 was frozen as `INCOMPLETE_TRANSPORT_OR_QUOTA` at Git commit
`c8a18c2613e589a84ba983fc416e58146f502c22`.
Two J1 responses (A01/A02) were returned as Markdown-fenced JSON and rejected by R7's
strict JSON parser. The next request (A03) encountered HTTP 503; J2 did not begin.
The 12-file R7 interruption capsule is preserved with SHA256 manifest
`c0d774c11f01400ccb7046d55ae7fca1b2490ad226f1af72a703b950b0bb9f06`.
R7 is not rescored, resumed, modified, or relabeled; its incomplete status stands.

R8 is a distinct qualification attempt. The changes below are declared before
new requests. Repeated prospective qualification attempts on the same nine
synthetic cases are transparently disclosed in the methods/limitations; model
selection performance on these cases is not treated as independent validation.

## Locked candidates and complete order

J1 = Google Gemini `gemini-3.8-flash` via
`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent`.
J2 = NVIDIA Nemotron `nvidia/nemotron-3-ultra-550b-a55b` via
`https://integrate.api.nvidia.com/v1/chat/completions`.

Test J1 then J2, even if J1 fails qualification gates. No model substitutions,
interactive tuning, fallback, reordering, or adaptive model selection.
Authentication is via `GEMINI_API_KEY` and `NVIDIA_API_KEY` environment variables;
never store, print or commit keys.

## Frozen synthetic inputs and gold

Retain the R6/R7 nine atomic cases A01–A09 in order and the same two repetitions:
18 logical evaluation slots per model, 36 overall. No primary benchmark inputs,
private original documents, expert judgments, or judge feedback are allowed in
qualification requests.

- prompt.txt SHA256: `c57ad42fcef1e6382dd2b72572898a6fd21ae780bd2e9189467d6512dfeb913c`
- cases.json SHA256: `b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2`
- frozen_validator.py SHA256: `925891d326cc3138f74fe2198a7786df21b1bf2de8a4c9d62984c2aae72527fd`

Use unchanged system instruction, unchanged serialized user JSON object, unchanged
case/gold signatures, and the byte-identical frozen validator. Never include gold
or previous responses in prompts. Do not alter the scoring rubric or case order.

## Request/response transport — prospective amendment to R7

Keep R7 provider payloads unchanged, including Google `temperature=0`, `topP=1`,
`maxOutputTokens=8192`, `candidateCount=1`, `thinkingLevel=medium`, and NVIDIA
`temperature=0`, `top_p=1`, `max_tokens=8192`, `reasoning_effort=medium`,
`reasoning_budget=4096`, `stream=false`. Same 300-second HTTP timeout.
No provider-side JSON-schema-enforcement, tool use, retrieval, or extra prompting.

Parse only final response content, not hidden thinking. For *both* providers,
allow exactly one of these fully encompassing response formats:

1. Direct strict JSON object.
2. Exactly one complete Markdown fenced code block with optional language label
   `json` (case-insensitive) or no language label. Strip only the opening and
   closing fence; never repair, reformat or substitute the inner content.

For both formats apply the unchanged strict JSON parser (duplicate-key and NaN
rejection) and unchanged frozen structural validator. Commentary before/after the
fence, multiple fences, unsupported fence labels, malformed JSON, missing fields,
truncated completions, or invalid score signatures are **not** repaired or retried.
Such outputs consume one logical slot and are recorded as failures. All non-
truncated response metadata must be saved for inspection.

## Prospective failure, retry and quota policy

Every scheduled logical slot is written ahead to `requests.jsonl`. Before every
HTTP transmission write an `attempts.jsonl` row; after it, write an
`attempt_results.jsonl` row. Store the final raw provider response, original
format error, parsed result, timing, and exact gold comparison per slot.

Only HTTP 502, 503, or 504 permit up to **two additional attempts for the same
logical slot** (maximum three HTTP attempts including the first). Use fixed
backoffs of 3 seconds and 10 seconds. Log each attempt explicitly. If all three
fail, stop the entire run as `INCOMPLETE_TRANSPORT_OR_QUOTA`.

HTTP 429 (quota), 401/403 (authentication), other HTTP errors, connection errors,
timeouts, malformed JSON, partial provider responses or output-schema problems:
**no retry**. For transport errors immediately stop the entire run and preserve
the incomplete evidence. For well-formed HTTP 200 containing invalid response
content record a failed logical slot and continue, as with R7.

This policy admits at most 36 logical slots and at most 108 HTTP attempts in the
extreme all-retry-eligible case; ordinary successful operation uses 36 attempts.
Never buy paid quota, enable billing, rotate credentials, or call another model
as a fallback automatically. Any blocked/partial attempt is never resumed.

## Qualification gates — identical to R6/R7

- 18/18 schema-valid judgments (both repetitions of A01–A09)
- 15/18 or more exact-gold signatures
- 8/9 or more repeatable case signatures
- Mandatory correct coverage of correct_abstention, failed_to_abstain, and
  incorrect_abstention, and SUPPORTED, PARTIALLY_SUPPORTED, UNSUPPORTED,
  CONTRADICTED (including A07 partially-supported label)
- Original pure-abstention empty-claim-list integrity accounting

All thresholds are mandatory and unchanged. Freeze outcome `PASS` only if both
J1 and J2 qualify. If both complete and fewer than two qualify, report
`INSUFFICIENT_QUALIFIED_MODELS`. If a provider blocks completion, report
`INCOMPLETE_TRANSPORT_OR_QUOTA`, not an invented final selection.

## Execution and scientific boundaries

Freeze the exact implementation and input capsule first. No inference is
permitted in the freeze/preparation phase. The subsequent one-shot `run` must
require separate deliberate user authorization. Never rerun a consumed R8
attempt or relabel earlier R6/R7 evidence. Preserve full provenance of each
qualification attempt in the thesis/paper methodology, including potential
qualification-set overfitting and provider availability limitations.

No primary 270-output judging, inferential comparison, expert validation
mutation, or production website changes are authorized by this R8 contract.
Before authorizing primary judging, separately verify judge eligibility,
provider data governance, practical quota, and capacity for long inputs.
