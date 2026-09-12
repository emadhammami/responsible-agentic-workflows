# UC1 Embedding Materialization Preflight

Date: 2026-09-12

## Purpose

This engineering-only preflight evaluated whether the accepted UC1 retrieval
chunks were ready for dense embedding materialization and selected a practical
embedding batch size before full-corpus embedding.

No benchmark questions, reference answers, gold evidence, or benchmark results
were used.

## Repository state

- Branch: `research/retrieval-foundation`
- Git base commit: `587949c`
- Retrieval configuration status: `working`
- Corpus frozen: no
- Retrieval configuration frozen: no

## Corpus chunk audit

The local materialized UC1 chunk artifacts were checked before embedding.

Observed:

- Document files: `30`
- Total chunks: `2853`
- Unique chunk IDs: `2853`
- Document IDs: `30`
- Minimum chunk words: `1`
- Maximum chunk words: `450`
- Mean chunk words: `334.53`
- Excluded document `DOC011`: absent
- Expected float32 embedding matrix size:
  `29214720` bytes
- Expected float32 embedding matrix size:
  `27.86 MiB`

The chunk artifact audit passed.

## Embedding model identity

- Model: `qwen3-embedding:4b-q4_K_M`
- Model digest:
  `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Embedding dimensions: `2560`
- Truncation: disabled

The local model digest matched the working retrieval configuration.

## Warmup

Observed warmup time:

- `3282.784 ms`

The warmup observation is engineering evidence only and is not a benchmark
result.

## Batch feasibility

Four candidate batch sizes were evaluated using evenly spaced samples from the
UC1 chunk corpus.

| Batch size | Wall time (ms) | ms/chunk |
| ---: | ---: | ---: |
| 8 | 1103.188 | 137.898 |
| 16 | 1443.125 | 90.195 |
| 32 | 2472.250 | 77.258 |
| 64 | 5997.598 | 93.712 |

All evaluated batches:

- returned the expected number of embeddings;
- returned `2560` dimensions;
- produced approximately unit-normalized vectors;
- completed without truncation or API failure.

Observed normalization ranges:

- Batch 8: `0.999999354` to `1.000000714`
- Batch 16: `0.999999287` to `1.000000766`
- Batch 32: `0.999999199` to `1.000000590`
- Batch 64: `0.999999354` to `1.000000845`

## Batch-size decision

`32` is selected as the working materialization batch size.

The decision is based only on engineering throughput and successful embedding
validation before benchmark execution. Among the evaluated candidates, batch
size 32 had the lowest observed milliseconds per chunk.

Batch size 64 was not selected because its observed per-chunk time increased
relative to batch size 32.

This decision was not based on retrieval accuracy, benchmark task performance,
gold evidence, or model answer quality.

## Runtime resource snapshot

Observed after the feasibility pilot:

- Ollama runtime model size:
  `8720272588` bytes
- Ollama reported VRAM:
  `8720272588` bytes
- Ollama runtime context length:
  `32768`
- NVIDIA GPU memory used:
  `9289 MiB`
- NVIDIA GPU memory total:
  `24463 MiB`
- GPU utilization snapshot:
  `91%`

## Interpretation

The preflight supports proceeding to full UC1 embedding materialization with
batch size 32.

This does not constitute acceptance of the embedding model for the final thesis
benchmark. Model acceptance remains deferred until corpus-level retrieval
validation is completed.

## Research safeguards

- No benchmark question was used.
- No benchmark gold evidence was used.
- No retrieval accuracy was evaluated.
- No benchmark run was executed.
- No corpus freeze occurred.
- No chunking freeze occurred.
- No retrieval configuration freeze occurred.
- Full-corpus embedding had not started at this checkpoint.
