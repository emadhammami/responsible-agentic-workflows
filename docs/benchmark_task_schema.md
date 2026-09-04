# Benchmark Task Schema

**Schema version:** 0.1  
**Status:** Working definition

## Purpose

The benchmark task schema defines the minimum information required for every
task used in the technical benchmark.

The schema is defined before model implementation and full benchmark
construction so that task design is not adapted to the behavior of a specific
system.

## Experimental unit

One benchmark task is the primary experimental unit.

A task contains:

- a stable task identifier;
- the user-facing question;
- a predefined task category;
- any documents known to be required;
- a human-validated reference answer;
- human-validated reference evidence;
- validation status.

## Task categories

### Direct retrieval

The answer can be found explicitly in one relevant document or section.

### Within-document reasoning

The answer requires combining information from multiple locations within one
document.

### Cross-document reasoning

The answer requires combining evidence from two or more documents.

### Insufficient evidence

The available corpus does not contain enough evidence to answer the question
reliably.

The expected behavior is therefore an appropriate abstention or statement of
insufficient evidence.

### Conflicting-document reasoning

Relevant documents contain conflicting, superseding, or context-dependent
information that must be identified or resolved.

This category will only be used if the real corpus contains suitable cases.

## Reference evidence

Reference evidence identifies the document provenance supporting the benchmark
answer.

Where available, evidence should preserve:

- document ID;
- page number;
- section;
- chunk ID after ingestion.

The public benchmark metadata must not reproduce restricted document text
unless publication permission exists.

## Human validation

An LLM may assist in proposing candidate questions, but final benchmark tasks
must not be accepted automatically.

The intended progression is:

    draft
      |
      v
    human_verified
      |
      v
    frozen

Only tasks marked `frozen` should be used in the final benchmark.

## Reference-answer isolation

Reference answers and reference evidence are evaluation data.

They must not be included in the workflow input, retrieval index, generation
prompt, or other model-accessible runtime state.

## Versioning

Changes to the task format require an explicit schema-version update.

Changes to individual benchmark tasks after the benchmark is frozen must be
documented rather than silently replacing prior task definitions.