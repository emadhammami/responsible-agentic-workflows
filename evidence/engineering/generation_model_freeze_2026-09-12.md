# Generation Model Freeze

Date: 2026-09-12

## Decision

The local generation model identity and fixed request-level generation behavior
are frozen before scientific benchmark execution.

Frozen model configuration:

`benchmark/config/model/OLLAMA-QWEN38-27B-48K-v0.1.json`

Configuration SHA256:

`f507c2d4270ad64a81ebaaef2c18a7236fba26dd30a99ed79ceed5d9b728b5e1`

## Frozen identity

- provider: Ollama
- provider version: 0.34.0
- model: `qwen3.8-27b-48k:latest`
- tag digest: `a68eeb5701b0a627f513a134f7ec029477a04b66a4605b32e27917ac93bd67a3`
- base weights: `sha256-f5f1dd8920d417aac2718b0bda3403da274301efdd6760b4f0f4b864ff2ad57d`
- parameter size: 27.3B
- quantization: Q4_K_M
- configured context: 49,152 tokens
- temperature: 0
- seed: 20260912
- thinking: false

The same frozen generation-model identity is used for B0, B1, and G1.

## Qualification basis

The candidate passed the pre-specified synthetic engineering gates for:

- grounded extraction;
- insufficient-evidence behavior;
- cross-document synthesis;
- structured output;
- disabled model-internal thinking;
- local execution identity.

The initial Q4 failure remains preserved. It resulted from an unstated
normalization requirement in the engineering fixture validator. The defect was
documented before Q4-v2 was executed. Q4-v2 then passed both repetitions using
the unchanged model configuration.

No frozen UC1 benchmark task, reference answer, reference evidence, or
scientific benchmark result was used to select the model.

## Freeze boundary

The following are frozen:

- generation model identity;
- Ollama version;
- model tag and digest;
- base model weights;
- context window;
- temperature;
- random seed;
- thinking disabled.

The following remain open until the benchmark configuration is finalized:

- final per-call maximum output tokens;
- B0/B1/G1 workflow resource limits;
- prompts and workflow configurations.

The engineering qualification value `num_predict=1024` is not treated as the
final scientific benchmark output-token limit.

## Change control

The generation model must not be changed in response to later benchmark
performance.

A genuine pre-benchmark technical incompatibility would require a documented
amendment, renewed engineering qualification, and a new freeze before
benchmark execution.

## Status

- `GENERATION_MODEL_FROZEN=YES`
- `SAME_MODEL_B0_B1_G1=YES`
- `THINKING=FALSE`
- `CONTEXT=49152`
- `BENCHMARK_TASKS_USED_FOR_SELECTION=NO`
- `SCIENTIFIC_BENCHMARK_RESULT_USED_FOR_SELECTION=NO`
- `FINAL_MAX_OUTPUT_TOKENS_FROZEN=NO`
- `RESOURCE_LIMITS_FROZEN=NO`
- `BENCHMARK_RUN=NO`
