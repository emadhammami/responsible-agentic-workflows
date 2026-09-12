# Qwen3 Embedding 4B Engineering Pilot Failure

Date: 2026-09-12

## Purpose

This engineering-only pilot evaluated local feasibility and basic embedding
properties before implementing the thesis retrieval backend.

It did not use benchmark tasks, reference answers, gold evidence, or benchmark
results. It is not part of the final technical benchmark.

## Environment

- Git branch: `research/retrieval-foundation`
- Git base commit: `635b2ee`
- Ollama version: `0.34.0`
- Model: `qwen3-embedding:4b-q4_K_M`
- Model digest:
  `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Parameter size: `4.0B`
- Quantization: `Q4_K_M`
- Format: `gguf`
- Family: `qwen3`
- Model metadata context length: `40960`
- Embedding length: `2560`

## Passed checks before first failure

- Ollama API availability.
- Exact model identity and digest.
- Model metadata inspection.
- Embedding dimensionality: `2560`.
- Approximate L2 normalization.

Observed norms:

- Query: `1.0000005809`
- Repeated query: `0.9999996457`
- Positive passage: `0.9999997063`
- Negative passage: `1.0000001097`

## First failure

The original pilot required repeated embeddings of the same query to have a
maximum component-wise absolute difference no greater than `1e-6`.

Observed:

- Maximum component-wise difference:
  `0.0034044569999999996`
- Original required threshold:
  `<= 0.000001`

Result:

`FIRST_FAILURE=REPEATABILITY_0.0034044569999999996`

Execution stopped at the first failure.

The original criterion was not changed after observing this result.

## Interpretation status

The component-wise repeatability failure was preserved as an engineering
observation. It did not by itself establish whether the variation was material
for cosine-based retrieval.

A separate follow-up diagnostic was therefore performed to measure vector-level
agreement and retrieval-ranking stability without changing the original pilot
criterion.

## Research safeguards

- No benchmark task was executed.
- No benchmark gold data was used.
- No UC1 retrieval performance was evaluated.
- No retrieval configuration was frozen.
- No chunking configuration was frozen.
- No corpus freeze occurred.
- No model was accepted or rejected from this pilot alone.
