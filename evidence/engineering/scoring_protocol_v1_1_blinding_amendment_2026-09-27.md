# Scoring Protocol v1.1 — Blinding Amendment

Status: FROZEN POST-EXECUTION / PRE-SCORING / PRE-ANALYSIS
Date: 2026-09-27

This amendment supplements:

- scoring_protocol_v1_2026-09-27.md
- commit 9087ac00d8560e256cdc9da54b51b2541ed9cb65

No benchmark answer has been scored and no statistical analysis has started.

## Reason for amendment

The v1 protocol states that evaluators may receive `run_id` while remaining
blinded to condition.

The frozen primary run identifiers encode the condition directly, for example:

`primary-t017-g1-r1`

Therefore exposing the original `run_id` would violate the intended condition
blinding.

This amendment corrects that implementation detail before scoring begins.

## Blinded evaluation identifier

Every primary run receives a deterministic opaque `evaluation_id`.

The evaluator-facing scoring package MUST NOT contain:

- original run_id;
- condition;
- repetition;
- workflow/policy identifiers;
- selected policy action;
- recovery status;
- token/resource measurements;
- latency measurements;
- filenames that encode B0, B1, or G1.

Evaluator-facing rows may contain:

- evaluation_id;
- task_id;
- task question;
- generated final answer;
- cited chunk IDs where required for grounding evaluation;
- frozen reference answer;
- frozen reference evidence;
- required documents;
- task type;
- fields required to record human judgments.

## Hidden identity mapping

A separate mapping file links:

evaluation_id -> run_id, condition, repetition

The mapping is not part of the evaluator-facing scoring package and must not be
consulted during independent scoring.

It is used only after scoring to join judgments back to the frozen runtime
dataset.

## Identifier generation

Identifiers are generated deterministically from the frozen execution sequence
using:

E0001 through E0270

The execution sequence itself is NOT included in the evaluator-facing package.

## Secondary evaluator subset

The already-frozen 90-run secondary subset remains unchanged.

For evaluator B, the selected run IDs are converted to their corresponding
opaque evaluation IDs before presentation.

The evaluator-facing secondary package must not expose the original run IDs,
conditions, repetitions, or selection hashes.

## Integrity

This amendment changes no:

- raw benchmark record;
- benchmark task;
- reference answer;
- reference evidence;
- runtime-derived metric;
- scoring rule;
- secondary-subset membership;
- statistical analysis rule.

It changes only the mechanism used to preserve evaluator blinding.
