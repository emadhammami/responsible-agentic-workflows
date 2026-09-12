# B0 synthetic real-model smoke

Date: 2026-09-12

Status: PASS

This record documents an engineering-only end-to-end smoke test of the B0
two-step RAG baseline with the frozen local generation model.

It is not a scientific benchmark result and did not use UC1 benchmark tasks,
reference answers, reference evidence, or the frozen UC1 corpus.

## Code revision

`2859f7ce6899f9143997ad72ababc55ee02eb1c0`

## Model

- config: `OLLAMA-QWEN38-27B-48K-v0.1`
- model: `qwen3.8-27b-48k:latest`
- tag digest:
  `a68eeb5701b0a627f513a134f7ec029477a04b66a4605b32e27917ac93bd67a3`
- Ollama: `0.34.0`
- context: `49152`
- temperature: `0`
- seed: `20260912`
- thinking: `false`

The smoke used `max_output_tokens=128` and a 180 second timeout as
engineering-only settings. These values are not frozen benchmark parameters.

## Synthetic execution

- task ID: `T990`
- synthetic document ID: `DOC990`
- execution mode: `engineering`
- condition: `None`
- retrieval calls: `1`
- model calls in the successful run: `1`
- input tokens: `166`
- output tokens: `25`
- total tokens: `191`
- finish reason: `stop`
- automatic cited chunk IDs: none

The answer correctly identified the employee's department head as the required
approver from the synthetic retrieved context.

## Attempt accounting

Three real model calls were made across the engineering smoke work:

1. The first model call completed, after which run validation failed because
   the temporary synthetic task ID did not satisfy the run schema.
2. The second model call completed, after which run validation failed because
   the temporary synthetic document ID did not satisfy the run schema.
3. The third model call produced the completed schema-valid smoke record.

An additional identifier preflight attempt failed before inference and consumed
no model call.

These failures were smoke-harness validation defects, not B0 model or retrieval
failures.

## Research boundary

- scientific benchmark started: no
- UC1 used: no
- benchmark condition assigned: no
- model selected or changed based on smoke performance: no
- B0/B1/G1 benchmark comparison performed: no

The successful raw engineering record is stored alongside this note.

Raw record SHA256:

`247cd1d4dcf5478f0699713c5fe365e6dde7a47d5190161d4cbba650d7dedfd2`
