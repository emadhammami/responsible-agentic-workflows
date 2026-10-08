# R7 Hosted LLM Judge Qualification Contract
Date: 2026-10-08
Status: PROSPECTIVE — frozen before API inference.

## Methodology amendment

The original two-local/open-weight judge requirement is
prospectively amended to permit two externally hosted,
independently operated model families.

Reason: qualification failures and operational feasibility
of R1–R6. R6 was formally frozen as incomplete at commit
5c440fca5170bdca87bdc6c605400567fa11bf8f.

The benchmark, answers, rubric, scoring definitions,
expert-validation protocol, atomic gold and acceptance
thresholds remain unchanged.

No primary benchmark judging has occurred.

## Fixed candidates and order

J1: Google Gemini, `gemini-3.8-flash`
Endpoint:
https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent
Credential: GEMINI_API_KEY environment variable.

J2: NVIDIA Nemotron,
`nvidia/nemotron-3-ultra-550b-a55b`
Endpoint:
https://integrate.api.nvidia.com/v1/chat/completions
Credential: NVIDIA_API_KEY environment variable.

No aliases, model substitutions, fallback or adaptive
candidate selection. Test J1 then J2.

## Frozen qualification inputs

9 atomic cases A01–A09, two repetitions per model,
18 scheduled judgments per model, 36 total.

Prompt SHA256:
c57ad42fcef1e6382dd2b72572898a6fd21ae780bd2e9189467d6512dfeb913c

Cases SHA256:
b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2

Unchanged R6 frozen validator SHA256:
925891d326cc3138f74fe2198a7786df21b1bf2de8a4c9d62984c2aae72527fd

Use the existing R6 frozen validator and exact gold
signatures. The R6 capsule is read-only provenance.

Use the same system prompt and user JSON object as R6,
with Python json.dumps default serialization and
identical field order. Gold and previous judgments
must never appear in a model request.

## Provider transport and decoding

Exactly one independent system instruction and user
message per judgment. No conversation history.

Common:
temperature=0; top_p=1; output cap=8192 tokens;
stream=false; one candidate response; timeout=300s.

Gemini: thinkingLevel=medium, maxOutputTokens=8192.
NVIDIA: reasoning_effort=medium, reasoning_budget=4096,
max_tokens=8192.

Provider-specific thinking is disclosed; identical
reasoning budgets across providers are not claimed.

No JSON-schema-constrained generation or provider-
specific semantic prompting. Both use the exact frozen
JSON instructions and the same strict local validation.
This prospective transport choice differs from R6's
structured-output enforcement.

Parse only the final response content. Do not parse
thinking/reasoning content as a judgment.

No tools, search, retrieval, web grounding, caching
substitutions, or external evidence.

## Acceptance gate — unchanged

SCHEMA = 18/18.
EXACT_GOLD >= 15/18.
REPEATABILITY >= 8/9.
All three abstention classes covered.
All four grounding classes covered, including
PARTIALLY_SUPPORTED on A07.
Pure-abstention claim-list integrity checked.

Every condition is mandatory. No threshold relaxation,
prompt tuning, gold correction or semantic retries.

## Failure and quota policy

Each accepted inference request occupies one scheduled
slot, regardless of incorrect or malformed output.

Record HTTP errors, timeouts, truncations and refusals.
No response repair, silent retry or replacement model.

Authentication, unavailable endpoint, exhausted quota,
payment requirement or rate-limit blockage stops the
affected candidate with INCOMPLETE status, preserving
all evidence. No claim of qualification is allowed.

Do not enable billing or upgrade paid tiers automatically.
Free access and usable quotas must be checked separately.
No primary scoring without explicit subsequent approval.

## Evidence and safety

Archive sanitized requests, SHA256 payload hashes,
raw response content, parsed results, validation,
exact-gold and repeatability checks, durations,
model IDs, response metadata and error information.

Never log keys, authorization headers or secret values.

No primary generated answers, benchmark scoring inputs,
expert responses or private research documents are
permitted in R7 qualification calls.

Primary-judge calls must remain zero.

## Final-pair eligibility

Both candidates must pass every gate. Otherwise,
FINAL_PAIR_STATUS=INSUFFICIENT_QUALIFIED_MODELS
(or INCOMPLETE if blocked operationally).

Qualification on small atomic cases does not prove
long-document scoring capacity. Before primary judging,
conduct a separate input-budget, context, privacy,
quota and scoring preflight without changing the
frozen rubric.

Freeze the exact qualification harness and provider
request configurations before the first inference.
No R7 API inference is authorized by this document
creation step.
