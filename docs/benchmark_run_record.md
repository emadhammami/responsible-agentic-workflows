# Execution Run Record

**Schema version:** 0.4
**Status:** Working definition

## Purpose

The same structured raw execution format is used for engineering validation and
thesis benchmark runs.

The `execution_mode` field separates the two purposes explicitly. Engineering
runs are not assigned a B0, B1, or G1 condition and are excluded from thesis
benchmark analysis.

The run record captures what happened during system execution before benchmark
scoring is applied.

## Separation of execution and evaluation

A raw run record must not contain:

- the reference answer;
- reference evidence unavailable to the workflow;
- correctness scores;
- grounding scores;
- final benchmark judgments.

These belong to the separate evaluation stage.

This separation reduces the risk that benchmark gold information becomes
available to the runtime workflow.

## Run identity

Every run records:

- experiment ID;
- run ID;
- benchmark task ID;
- execution mode;
- system condition where applicable;
- Git revision;
- configuration identifiers;
- start and finish timestamps.

A run ID must identify one execution only.

Retries inside a workflow belong to the same run when they are part of the
defined workflow behavior.

A complete restart of a benchmark task is a new run and receives a new run ID.

## Execution modes

Two execution modes are defined:

- `engineering` - software validation only; `condition` must be null;
- `benchmark` - thesis benchmark execution; `condition` must be B0, B1, or G1.

Engineering runs are excluded from thesis benchmark analysis.

## System conditions

The allowed benchmark conditions are:

- B0 - external LangChain 2-step RAG reference;
- B1 - matched agentic baseline without selected guardrails;
- G1 - matched agentic workflow with selected guardrails.

## Retrieval trace

Retrieval is recorded per retrieval call rather than as one flattened list.

Each retrieval call records:

- call sequence;
- query;
- requested top-k;
- retrieval latency;
- retrieved document IDs;
- retrieved chunk IDs;
- page and section where available;
- retrieval rank;
- retrieval score where the backend provides one.

This structure preserves the relationship between each query and the evidence
returned for that query.

It is required because B1 and G1 may perform multiple retrieval calls during
planning, verification, revision, or recovery.

The aggregate `retrieval_calls` field in resource usage records the total number
of retrieval calls for the run.

Restricted source text should not be copied into public run artifacts unless
publication permission exists.

## Model-call trace

Language model calls are recorded individually.

Each model-call record includes:

- call sequence;
- completion or failure status;
- measured call latency;
- provider-reported input and output tokens when available;
- total reported tokens;
- finish reason when available;
- provider response identifier when available.

Prompt content and generated response text are not duplicated in the model-call
trace. This keeps resource instrumentation separate from workflow content and
reduces unnecessary replication of document-derived text.

Aggregate token counts, model-call count, and model latency are derived from the
recorded calls rather than supplied independently.

## Resource measurements

Runtime resource fields include:

- input tokens;
- output tokens;
- total tokens;
- LLM calls;
- retrieval calls;
- tool calls;
- retries.

Provider-native accounting should be used when available.

## Runtime measurements

The minimum runtime measure is end-to-end latency.

Retrieval and model-call timing should also be recorded when they can be
measured consistently.

Timing definitions will be frozen before the full benchmark.

## Workflow events

Agentic workflows may contain several internal stages.

The event list provides an ordered trace for events such as:

- planning;
- retrieval;
- generation;
- verification;
- revision;
- recovery;
- resource-control decisions.

B0 may have a much shorter event trace than B1 or G1.

This architectural difference is expected and should not be artificially
removed.

## Failures

Failed and interrupted runs remain benchmark artifacts.

A failure should produce a valid run record whenever technically possible,
including:

- status;
- completed measurements;
- error type;
- stage;
- error message.

Runs must not disappear simply because execution was unsuccessful.

## Benchmark terminology

Token counts, runtime, task outcomes, grounding, reliability, and related
system measurements are reported as technical benchmark measurements.

They are not described as the quantitative component of the thesis research
design.

Qualitative and any structured quantitative empirical interview data are
collected through the semi-structured interview study.

## Versioning

The raw run format is versioned independently from:

- benchmark task schema;
- evaluation rubric;
- workflow configuration.

Changes to required runtime fields require a schema-version update.
