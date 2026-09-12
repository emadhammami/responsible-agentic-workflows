# Embedding Model Selection

Date: 2026-09-12

## Decision

`qwen3-embedding:4b-q4_K_M` is accepted as the embedding model for the thesis
retrieval stack.

Exact model digest:

`df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`

The decision is an engineering model-selection decision made before benchmark
execution. It is not a thesis benchmark result.

## Basis

The candidate passed the corpus-level engineering validation sequence:

- full UC1 embedding materialization completed for 2853 chunks;
- provenance-verified artifact loading passed;
- identity retrieval diagnostic retrieved the expected document within Top-3
  for all 8 fixed probes across all repeats;
- semantic retrieval diagnostic retrieved the expected document within Top-3
  for all 8 fixed probes across all repeats;
- all four pre-specified semantic engineering acceptance checks passed.

The semantic probe protocol and acceptance gate were committed before retrieval
results were observed.

## Scope decision

No second embedding model will be evaluated unless a later pre-benchmark
technical failure invalidates this selection.

The thesis does not study comparative embedding-model performance. Adding
another embedding model would introduce an unnecessary experimental factor
without answering the research questions on guardrails, reliability, and
resource efficiency.

The selected embedding model should therefore be held constant across B0, B1,
and G1 and, where technically applicable, across the thesis use cases.

## Important limitation

Acceptance means that the model is sufficiently validated for the planned
retrieval role. It does not establish that it is the best available embedding
model or that it outperforms alternatives.

## Status

- `EMBEDDING_MODEL_SELECTION=ACCEPTED`
- `SECOND_EMBEDDING_MODEL_REQUIRED=NO`
- `BENCHMARK_RUN_USED_FOR_SELECTION=NO`
- `GOLD_DATA_USED_FOR_SELECTION=NO`
- `CORPUS_FREEZE=NO`
- `CHUNKING_FREEZE=NO`
- `RETRIEVAL_CONFIG_FREEZE=NO`
