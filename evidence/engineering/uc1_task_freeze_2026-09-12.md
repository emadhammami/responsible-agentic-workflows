# UC1 Benchmark Task Freeze

Date: 2026-09-12

## Scope

This record freezes the ten benchmark tasks for UC1 only.

It does not freeze UC2, UC3, or the complete 30-task primary benchmark.

## Preconditions

- UC1 corpus frozen before task freeze.
- UC1 chunking and retrieval foundation frozen before task freeze.
- Ten UC1 tasks human verified before freeze.
- Positive-task reference evidence bound to frozen source chunks.
- T009 and T010 supported by a separate insufficient-evidence authoring audit.
- Runtime gold isolation verified.
- No B0, B1, or G1 benchmark result was used to select or revise the tasks.

## Frozen allocation

- 3 direct-retrieval tasks
- 3 within-document reasoning tasks
- 2 cross-document reasoning tasks
- 2 insufficient-evidence tasks

## Frozen identity

- Pre-freeze human-verified task-set SHA256: `93e394521149b2b727624aa2e20903075fb53951d2cb7a591a9ed40fda4f106b`
- Frozen task-set SHA256: `28828661090b42ed452127d624312ffc47536bcbd7124a8fecac8271f8c47efb`
- Pre-freeze source commit: `b548c4371b42c4cd6299d4e46c375884dc1b40c6`

The exact frozen per-file hashes are recorded in
`benchmark/tasks/UC1/freeze_manifest.json`.

## Change control

The UC1 tasks must not be changed in response to benchmark performance.

If a genuine task defect is discovered before benchmark execution, the
change must be documented as a pre-benchmark amendment, human reviewed,
revalidated, and frozen again before any affected benchmark execution.

## Status

- `UC1_TASKS=10`
- `FROZEN_TASKS=10`
- `BENCHMARK_RUN_USED_FOR_FREEZE=NO`
- `UC1_CORPUS_FROZEN=YES`
- `UC1_RETRIEVAL_FROZEN=YES`
- `UC2_TASKS_FROZEN=NO`
- `UC3_TASKS_FROZEN=NO`
- `PRIMARY_30_TASK_SET_FROZEN=NO`
