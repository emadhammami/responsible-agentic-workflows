# Benchmark Configuration

## Purpose

The technical benchmark uses a machine-readable configuration to preserve the
settings that define one comparable experimental setup.

The configuration is separate from individual run records. A run records what
happened during one execution, while the benchmark configuration records the
settings that were intended to remain fixed across comparable executions.

## Shared settings

A benchmark configuration defines one shared model setup and one shared
retrieval setup for the evaluated conditions.

The shared model fields include:

- provider;
- model name and configuration identifier;
- model version where available;
- temperature;
- maximum output tokens.

The shared retrieval fields include:

- retrieval configuration identifier;
- retrieval backend;
- embedding model where applicable;
- vector store where applicable;
- chunking configuration identifier;
- retrieval top-k.

Using one shared model and retrieval definition reduces implementation
differences that are unrelated to the B1 versus G1 comparison.

## Condition-specific identifiers

Prompt and workflow configuration identifiers are recorded separately for B0,
B1, and G1 because the three conditions do not have identical architectures.

Differences between B1 and G1 should remain limited to the selected guardrails
and any changes necessarily caused by those guardrails.

B0 remains an external reference architecture and is not forced to reproduce
the internal workflow structure of B1 or G1.

## Resource and execution settings

The configuration also records:

- token limit per run, where one is imposed;
- model-call limit per run, where one is imposed;
- retrieval-call limit per run, where one is imposed;
- retry limit;
- repetition count;
- random seed where applicable.

A null resource limit means that no explicit limit is configured for that
field. It does not mean that the value was forgotten or left undocumented.

## Working and frozen configurations

Two states are permitted:

- `working` - settings are still being selected or tested;
- `frozen` - settings are fixed for the corresponding benchmark execution.

Engineering and pilot work may use a working configuration.

Final thesis benchmark execution must use a frozen configuration. If a
scientifically relevant setting must change after freezing, a new configuration
identifier should be created and the reason for the change documented rather
than silently modifying the frozen setup.

## Separation from benchmark results

The configuration describes experimental settings. It does not contain:

- benchmark answers;
- reference evidence;
- correctness judgments;
- grounding scores;
- benchmark results.

Those remain separated from execution configuration and runtime data.
