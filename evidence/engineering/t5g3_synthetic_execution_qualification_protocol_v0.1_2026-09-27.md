# T5G3 Synthetic End-to-End Execution Qualification Protocol v0.1

Date: 2026-09-27
Base implementation:
9f5a38343bf5f57828d0be0c15acef0fba61743e

Status: prospectively frozen before live qualification execution.

BENCHMARK_STARTED=NO
PRIMARY_TASK_EXECUTION=NO
RESULT_DRIVEN_REVISION=NO

## Purpose

Qualify the frozen execution stack against real local Ollama transport using
only the synthetic engineering corpus/tasks.

This is engineering qualification, not scientific benchmark execution and
not benchmark-performance evaluation.

## Inputs

Synthetic documents:
DOC901-DOC905.

Synthetic runtime questions:
T901-T907.

No T001-T030 task may be loaded or executed.

No primary UC1/UC2/UC3 corpus artifact may be used for retrieval.

## Matrix

Execute every synthetic task under all three workflow variants:

T901-T907 x {B0, B1, G1} = 21 scheduled engineering runs.

No run is selected, removed, added, or repeated in response to outputs.

## Execution mode

All RunRecorder instances MUST use:

execution_mode = engineering
condition = null

B0/B1/G1 are engineering variant labels only and MUST be encoded in
run_id / experiment metadata, not as scientific benchmark condition records.

## Live provider identity

Generation:
- provider: Ollama
- version: 0.34.0
- model: qwen3.8-27b-48k:latest
- configured context: 49152
- seed: 20260912
- temperature: 0
- max output tokens: 1024
- thinking: false
- HTTP transport timeout: 300 s

Embedding:
- provider: Ollama
- version: 0.34.0
- model: qwen3-embedding:4b-q4_K_M
- dimensions: 2560
- truncate: false
- query instruction identical to frozen retrieval foundation
- HTTP transport timeout: 300 s

## Synthetic retrieval

The five synthetic Markdown documents are ingested using existing repository
ingestion code.

Document chunks are embedded once for this qualification attempt using the
live frozen embedding model.

All variants share the exact same in-memory chunk tuple, embedding matrix,
DenseExactRetriever implementation, query embedder and top_k=10.

No primary retrieval artifact is read.

## Workflow construction

B0:
- existing B0Baseline
- b0-engineering-v0.1
- b0-two-step-rag-v0.1

B1:
- existing AgenticRunner
- B1FixedRecoveryPolicy
- agentic-engineering-v0.1
- b1-agentic-fixed-recovery-v0.1

G1:
- existing AgenticRunner
- G1ERGRPolicy
- agentic-engineering-v0.1
- g1-agentic-ergr-v0.1

B1/G1 share every non-policy input.

Resource limits:
- max LLM calls = 5
- max retrieval calls = 2
- max retries = 1
- max total tokens = null
- workflow timeout_ms = null

The 300-second HTTP transport timeout is not workflow timeout_ms.

## Runtime-task isolation

Only task_id and question are projected into RuntimeTask.

Reference answer, reference evidence, required documents, task type,
difficulty and notes MUST NOT be supplied to retrieval, model, critic,
policy or workflow execution.

Synthetic gold is not used for qualification acceptance.

## Run identity

Attempt ID:
T5G3-SYNTHETIC-QUALIFICATION-A1

Run IDs are fixed prospectively:

t5g3-a1-{task_id_lower}-{variant_lower}

Exactly 21 unique run IDs are permitted.

Code revision MUST equal the frozen T5G2 implementation revision.

## Persistence

Qualification artifacts are written outside the repository under one
attempt-specific temporary directory.

Existing output files MUST never be overwritten.

Any interrupted attempt is preserved and inspected before any rerun.

## Acceptance criteria

Qualification PASS requires:

1. exactly 21 scheduled runs attempted once;
2. exactly 21 schema-valid immutable run records;
3. all records use execution_mode=engineering and condition=null;
4. exact prospective run IDs and frozen code revision;
5. no status=failed;
6. no status=tool_error;
7. all model calls report non-negative provider token usage;
8. all retrieval calls have finite scores and valid ranked chunk provenance;
9. B0 uses exactly one retrieval and one LLM call per run;
10. B1/G1 never exceed 5 LLM calls, 2 retrieval calls, or 1 retry;
11. every B1/G1 run contains the expected initial plan/retrieval/draft/critic
    execution events unless a valid earlier resource-stop event explains the
    termination;
12. any resource_stopped outcome must have a corresponding structured
    resource-stopped event and is treated as a valid controlled terminal
    outcome, not a correctness result;
13. no answer correctness, gold comparison or benchmark metric is computed;
14. source tree and frozen implementation bytes remain unchanged;
15. no run-order manifest is generated.

A failed engineering/infrastructure criterion blocks qualification and is
diagnosed before any primary benchmark execution.

## Explicit exclusions

PRIMARY_TASK_EXECUTION=NO
PRIMARY_BENCHMARK_CORPUS_RETRIEVAL=NO
SCIENTIFIC_BENCHMARK_RESULT=NO
ANSWER_SCORING=NO
RUN_ORDER_GENERATION=NO
BENCHMARK_STARTED=NO
