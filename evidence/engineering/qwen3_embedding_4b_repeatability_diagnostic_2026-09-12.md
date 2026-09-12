# Qwen3 Embedding 4B Repeatability and Ranking Diagnostic

Date: 2026-09-12

## Purpose

This engineering-only follow-up investigated the component-level variation
observed in the initial embedding pilot.

The original repeatability criterion was not relaxed or replaced. This
diagnostic collected additional evidence about cosine agreement, vector-level
error, ranking stability, timing, and runtime resource use.

No thesis benchmark task or gold evidence was used.

## Model

- Model: `qwen3-embedding:4b-q4_K_M`
- Model digest:
  `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Embedding dimensions: `2560`
- Ollama version: `0.34.0`

## Sequential repeatability

Ten sequential embeddings of the same synthetic query were evaluated.

Observed:

- Minimum repeat cosine:
  `0.999582569392`
- Mean repeat cosine:
  `0.999582569392`
- Maximum component-wise difference:
  `0.002937220000`
- Maximum repeat RMSE:
  `0.000571067052`
- Mean repeat RMSE:
  `0.000571067052`

The sequential calls were therefore highly similar in cosine space but were not
component-wise identical.

## Same-request batch repeatability

Ten copies of the identical query were embedded in one API request.

Observed:

- Minimum batch repeat cosine:
  `1.000000000000`
- Mean batch repeat cosine:
  `1.000000000000`
- Maximum component-wise difference:
  `0.000000000000`
- Maximum batch repeat RMSE:
  `0.000000000000`

The repeated vectors within the same batch were identical in this diagnostic.

## Normalization

Observed query norms:

- Minimum: `0.999999624203`
- Maximum: `1.000000116012`
- Mean: `1.000000066831`

The vectors remained approximately unit normalized.

## Synthetic retrieval-ranking stability

Five synthetic passages were used only as an engineering sanity check:

1. biodiversity policy;
2. forest climate;
3. timber market;
4. employee travel;
5. software access.

Across all ten sequential query embeddings:

- Unique ranking orders: `1`
- Unique Top-1 documents: `1`
- Top-1 document: `BIODIVERSITY`
- Minimum Top-1 margin: `0.229227141811`
- Maximum Top-1 margin: `0.231346420127`

The complete ranking order was stable across all ten runs.

## Timing

- Sequential minimum: `15.966 ms`
- Sequential median: `18.181 ms`
- Sequential maximum: `177.982 ms`
- Batch of 10 queries: `110.133 ms`
- Batch of 5 document passages: `103.229 ms`

These timings are engineering observations only and are not benchmark results.

## Runtime state

Observed after the diagnostic:

- Ollama runtime model size:
  `8720272588` bytes
- Ollama reported VRAM:
  `8720272588` bytes
- Ollama runtime context length:
  `32768`
- NVIDIA memory used:
  `9275 MiB`
- NVIDIA memory total:
  `24463 MiB`
- GPU utilization snapshot:
  `51%`

The difference between the model metadata context length (`40960`) and the
runtime context length (`32768`) is preserved for later configuration review.

## Interpretation status

The diagnostic shows that the original component-wise repeatability criterion
failed while cosine similarity and synthetic retrieval ordering remained highly
stable.

No post-hoc acceptance threshold has been introduced.

The embedding candidate remains under engineering evaluation. A model acceptance
decision should be made only after the retrieval implementation and controlled
corpus-level engineering validation are completed.

## Research safeguards

- Original pilot failure preserved.
- Original repeatability criterion preserved.
- No threshold relaxed after observing results.
- No benchmark task executed.
- No benchmark gold data used.
- No UC1 benchmark performance evaluated.
- No retrieval configuration frozen.
- No corpus or chunking freeze performed.
