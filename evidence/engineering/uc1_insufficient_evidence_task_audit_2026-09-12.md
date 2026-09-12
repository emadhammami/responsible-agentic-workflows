# UC1 Insufficient-Evidence Task Authoring Audit

Date: 2026-09-12

## Purpose

This record documents the corpus-wide authoring checks used to construct the
two insufficient-evidence tasks in the UC1 benchmark draft.

The audit is task-authoring evidence. It is not a benchmark result and did not
execute B0, B1, or G1.

## Corpus boundary

The audit used the frozen UC1 corpus:

- 30 retrieval-active documents;
- 2853 frozen chunks;
- no corpus modification;
- no retrieval tuning;
- no LLM call.

Missing publication-date metadata in the manifest was not used as evidence of
absence.

## T009

Question:

> As of 31 December 2025, how many of the EU commitment to plant at least
> 3 billion additional trees by 2030 had actually been planted?

The corpus contains the 3 billion tree commitment, the 2030 target, and
descriptions of monitoring and recording mechanisms.

The corpus-wide scan found no chunk that simultaneously contained the
commitment anchor, a 2025 reference, and an explicit planting-progress
indicator sufficient to establish an actual end-of-2025 count.

The requested numerical outcome is therefore not supported by the frozen UC1
corpus.

## T010

Question:

> As of 31 December 2025, what percentage of EU land was actually under strict
> legal protection?

The corpus contains an earlier baseline for strict protection and the policy
ambition to place 10% of EU land under strict protection.

The corpus-wide scan found no explicit actual strict-protection percentage for
31 December 2025.

The earlier baseline and the policy target must not be substituted for the
requested 2025 observed outcome.

## Expected behavior

For both tasks, the expected behavior is to state that the available corpus
evidence is insufficient to determine the requested 2025 outcome.

A fabricated, inferred, externally sourced, outdated, or target value presented
as the requested observed 2025 result is not a correct answer.

## Methodological limitation

A corpus-wide lexical and manual-context audit does not constitute a general
proof that information is absent from every conceivable source. The benchmark
claim is narrower: the frozen UC1 corpus does not provide sufficient evidence
for the requested outcomes.

Both tasks remain `draft` until human verification.

## Status

- `UC1_INSUFFICIENT_EVIDENCE_AUTHORING_AUDIT=PASS`
- `T009_EXPLICIT_2025_OUTCOME_EVIDENCE_FOUND=NO`
- `T010_EXPLICIT_2025_OUTCOME_EVIDENCE_FOUND=NO`
- `BENCHMARK_RUN_USED=NO`
- `LLM_USED=NO`
- `TASKS_HUMAN_VERIFIED=NO`
- `TASKS_FROZEN=NO`
