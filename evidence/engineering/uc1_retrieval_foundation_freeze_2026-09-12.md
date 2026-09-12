# UC1 Retrieval Foundation Freeze

Date: 2026-09-12

## Purpose

This record defines the pre-benchmark freeze boundary for the UC1 retrieval
foundation.

The freeze was performed only after corpus intake, provenance validation,
chunking selection, embedding materialization, artifact verification, and
pre-specified identity and semantic retrieval diagnostics had completed.

## Frozen methodological scope

The following UC1 components are frozen:

- corpus scope: 30 accepted retrieval-active documents;
- chunking configuration: `UC1-PAGE-W450-O75-v0.1`;
- embedding model: `qwen3-embedding:4b-q4_K_M`;
- embedding model digest: `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`;
- retrieval backend: exact cosine over the materialized NumPy embeddings;
- retrieval configuration:
  `UC1-QWEN3-EMBED4B-EXACT-COSINE-v0.1`.

Benchmark-owned settings such as `top_k` are not defined by this detailed
retrieval configuration and are not frozen by this record.

## Configuration transition

| Artifact | Before SHA256 | Frozen SHA256 |
| --- | --- | --- |
| UC1 benchmark scope | `842e6e17ba3f05a1036afd78354dbb667078327fa305a8199babfa04d6c0eb79` | `931c589775b3c3ef94cffbfdcfd2add259a3bafee5cdefa728a1af41171020e2` |
| UC1 chunking config | `c51bb8037fc0b077e3038fd8b97365b02697fa62c9f24c8c3177a658a4e9a505` | `c94e14f20a38f539d1e6899051e141e2cf9b58509c132c5599581776919e3006` |
| UC1 retrieval config | `a83e43e8c4d3a7ff742bd7d785ba094388d063791032c696f1da2aae65c25da8` | `b3feaf22eb7126751837c6dc1dade05afc5b289dd353155e7644cdd83557109c` |

The tracked status transitions were:

- corpus scope: `working` to `frozen`;
- corpus frozen flag: `false` to `true`;
- chunking status: `working` to `frozen`;
- chunking frozen flag: `false` to `true`;
- retrieval configuration status: `working` to `frozen`.

## Preserved source and embedding artifacts

The local processed chunk index was not modified:

- before: `18f136ea995b38bcddbb74c2c71ce1e2d2353f0ce23af2a62a9dfadaece320bb`
- after: `18f136ea995b38bcddbb74c2c71ce1e2d2353f0ce23af2a62a9dfadaece320bb`

The embedding matrix was not modified:

- before: `b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0`
- after: `b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0`

The chunk-ID artifact was not modified:

- before: `f62aa825797144a3ebff4a7fee0cd08e3cf86525a8bbfc7c4d041ea3bc1c3673`
- after: `f62aa825797144a3ebff4a7fee0cd08e3cf86525a8bbfc7c4d041ea3bc1c3673`

Canonical aggregate source chunk artifact SHA256:

`ce308f891d5b21bca80ce5b004f2fa0e6843bc2db951c057bcbd33c0821840ba`

No re-chunking and no re-embedding occurred.

## Local embedding metadata

The ignored local embedding metadata was transitioned from `working` to
`frozen` and rebound to the frozen retrieval configuration SHA256.

- metadata SHA256 before: `2e7be2db424baf7cc17e807d5a478f96d4fb7a0cb06e0296782629ed29b1f0dc`
- metadata SHA256 after: `f231b5b93e90d5ee13f2291cae8f0f128e901a5edc525185448970eb82900ce4`
- frozen retrieval config SHA256: `b3feaf22eb7126751837c6dc1dade05afc5b289dd353155e7644cdd83557109c`

The provenance-verified loader passed after the transition.

## Research controls

- No benchmark question was used to select the corpus.
- No benchmark result was used to select the chunking configuration.
- No benchmark gold evidence was used for embedding-model selection.
- No benchmark run occurred before this freeze.
- The embedding matrix and chunk IDs remained byte-identical.
- No second embedding model is required by the research design.

## Status

- `UC1_CORPUS_FREEZE=YES`
- `UC1_CHUNKING_FREEZE=YES`
- `UC1_RETRIEVAL_FREEZE=YES`
- `EMBEDDING_ARTIFACT_FREEZE=YES`
- `REEMBEDDING_PERFORMED=NO`
- `BENCHMARK_RUN_BEFORE_FREEZE=NO`
