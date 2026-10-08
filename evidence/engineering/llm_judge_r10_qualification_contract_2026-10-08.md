# R10 — Prospective hosted judge qualification

Date: 2026-10-08
Status: PROTOCOL FROZEN BEFORE QUALIFICATION INFERENCE

## Objective

Qualify two independent external LLM judges for
the existing 270-output thesis benchmark.

Zero paid API charges. No model downloads.
No primary judging before successful qualification.

## Fixed candidates and order

J1: Cohere
Model: command-a-reasoning-08-2025
Credential: COHERE_API_KEY

J2: Google
Model: gemini-3.5-flash
Credential: GEMINI_API_KEY

No substitutions, adaptive selection or fallback.

## Qualification design

Create nine new independent synthetic atomic cases.
No cases from R1–R8 may be reused.

The new cases, gold signatures and complete prompt
must be byte-frozen before any R10 inference.

Use the existing correctness, grounding and
abstention semantics and frozen validator.

Two repetitions per case, per model.
18 logical judgments per model.
36 logical judgments maximum.

## Mandatory qualification thresholds

Schema: exactly 18/18 valid responses.
Exact gold signature: at least 15/18.
Repeatability: at least 8/9.
All three substantive abstention classes covered.
All four grounding classes covered, including
PARTIALLY_SUPPORTED.
Pure-abstention claim integrity required.

The thresholds cannot be relaxed after inference.

## Request/output policy

Use identical semantic judging instructions and
the same case inputs for both model families.

No gold labels in model requests.
No tools, retrieval, browsing or external grounding.

Temperature zero where supported.
Use a frozen, provider-specific transport adapter.

JSON object output required.
A complete Markdown JSON fence may be unwrapped
prospectively, but no content repair, type coercion,
field injection or score normalization is allowed.

The frozen local validator determines schema validity.

Provider request structures, reasoning settings,
timeouts, output budgets and HTTP retry rules must
be frozen in the executable harness before inference.

Every request attempt and response is journaled.
Previously completed logical slots cannot be rerun.
429, authorization and payment errors cause a pause
without silently consuming new logical slots.

## Evidence

Preserve raw responses, parsed outputs, hashes,
usage metadata, timing, errors, validation results,
and provenance for every attempted judgment.

Do not modify earlier R1–R9 evidence.

## Operational and scientific boundaries

Both candidates must pass independently before
a final judging pair can be selected.

Qualification does not authorize primary scoring.

Confirm free quotas, context capacity and permission
to transmit research evidence before primary scoring.

Google Free Tier may use submitted data to improve
Google products; document this limitation and obtain
appropriate data-use authorization.

Do not enable billing, upgrades or paid endpoints.

No primary benchmark inputs, expert answers or
confidential documents may be sent during
synthetic qualification.
