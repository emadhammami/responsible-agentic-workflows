# Primary Run-Order Protocol v0.1

Status: PRE-RESULT FROZEN CANDIDATE
Date: 2026-09-27

## Scope
Primary benchmark: T001-T030.
Conditions: B0, B1, G1.
Repetitions: 1, 2, 3.
Total scheduled runs: 270.

## Generation
The complete Cartesian product of:
30 tasks x 3 conditions x 3 repetitions
MUST contain exactly 270 unique runs.

The execution order MUST be generated exactly once using an isolated
deterministic Python random.Random(20260912) instance.

Canonical pre-shuffle construction order:
1. task_id ascending T001-T030;
2. condition B0, B1, G1;
3. repetition 1, 2, 3.

The complete 270-entry list is then shuffled once.

Each entry MUST bind:
- execution_sequence: 1..270
- task_id
- condition
- repetition
- run_id
- experiment_id
- output relative path

run_id format:
primary-tNNN-{condition_lower}-r{repetition}

experiment_id:
PRIMARY-BENCHMARK-V1

No duplicate tuple, run_id, output path or execution_sequence is permitted.

## Freeze
The generated manifest MUST be schema/contract validated, SHA256 hashed,
reviewed without executing any task, and committed before primary execution.

After generation:
- no regeneration;
- no re-shuffle;
- no order changes based on outputs, failures, latency or condition;
- interrupted execution resumes from immutable persisted state under the
  separately frozen execution/recovery procedure.

Generation MUST NOT load primary task answers, inspect model outputs, invoke
retrieval, embeddings or Ollama, or execute B0/B1/G1.
