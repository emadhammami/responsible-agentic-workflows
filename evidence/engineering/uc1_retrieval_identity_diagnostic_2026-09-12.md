# UC1 Retrieval Identity Diagnostic

Date: 2026-09-12

## Purpose

This record preserves the first real-corpus dense retrieval identity
diagnostic for UC1.

The diagnostic is engineering evidence only. It is not a benchmark
result and is not sufficient by itself to accept or reject the
embedding model.

## Pre-execution protocol

- Protocol: `UC1-METADATA-IDENTITY-PROBES-v0.1`
- Protocol commit: `6f1848f194a627d18af266aafde782e367344585`
- Protocol SHA256: `4106971dc1e21c899e3f967d9395ccbf93a78a04b6f3c41152fdda707be92792`
- Protocol frozen before retrieval results were observed: yes
- Probe source: pre-existing policy title and reference metadata
- Raw document text used to design probes: no
- Benchmark questions used: no
- Benchmark gold used: no

## Retrieval configuration

- Retrieval configuration: `UC1-QWEN3-EMBED4B-EXACT-COSINE-v0.1`
- Retrieval configuration SHA256: `a83e43e8c4d3a7ff742bd7d785ba094388d063791032c696f1da2aae65c25da8`
- Embedding model: `qwen3-embedding:4b-q4_K_M`
- Embedding model digest: `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Embedding provider version: `0.34.0`
- Embedding artifact metadata SHA256: `2e7be2db424baf7cc17e807d5a478f96d4fb7a0cb06e0296782629ed29b1f0dc`

## Execution

- Probes: `8`
- Repeats per probe: `3`
- Query runs: `24`
- Top-k: `10`
- Diagnostic wall time: `4.770 seconds`
- Local result artifact SHA256: `7bf840d14c170495665d87124f2bd00e40ee00fe18a37d5d23173ae0c133b371`

## Per-probe observations

| Probe | Expected document | Expected document ranks | Stable Top-1 document | Top-10 order variants | Mean latency ms | Min Top-1 margin | Mean Top-1 margin |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| ID01 | DOC017 | 3,3,3 | DOC005 | 1 | 1134.044 | 0.024122 | 0.024925 |
| ID02 | DOC018 | 1,1,1 | DOC018 | 1 | 67.987 | 0.026712 | 0.027152 |
| ID03 | DOC019 | 1,1,1 | DOC019 | 1 | 87.923 | 0.092855 | 0.092880 |
| ID04 | DOC021 | 1,1,1 | DOC021 | 2 | 70.634 | 0.058625 | 0.059516 |
| ID05 | DOC023 | 1,1,1 | DOC023 | 1 | 51.984 | 0.044560 | 0.044643 |
| ID06 | DOC027 | 2,2,2 | DOC010 | 1 | 75.982 | 0.024319 | 0.024807 |
| ID07 | DOC029 | 1,1,1 | DOC029 | 2 | 41.224 | 0.073276 | 0.073737 |
| ID08 | DOC030 | 1,1,1 | DOC030 | 1 | 59.969 | 0.033188 | 0.033287 |

## Aggregate observations

- Expected document at rank 1 in all repeats: `6/8`
- Expected document within Top-3 in all repeats: `8/8`
- Expected document within Top-10 in all repeats: `8/8`
- Stable Top-1 document across repeats: `8/8`
- Stable Top-1 chunk across repeats: `8/8`
- Exact Top-10 chunk order stable across repeats: `6/8`

The expected document was not the Top-1 result for two probes:

- `ID01`: expected `DOC017`, observed first expected-document rank `3`.
- `ID06`: expected `DOC027`, observed first expected-document rank `2`.

The exact Top-10 chunk ordering varied across repeats for two probes,
while the Top-1 document and Top-1 chunk remained stable for all probes.

## Interpretation

The result supports successful end-to-end real-corpus dense retrieval
and strong identity retrieval for the fixed metadata-derived probes.

It does not establish semantic retrieval quality. Identity probes include
canonical document titles and legal references and are therefore easier
than paraphrased knowledge-work queries.

The embedding-model acceptance decision remains deferred until a
separately frozen semantic retrieval diagnostic is completed.

## Research safeguards

- No benchmark question was used.
- No benchmark gold evidence was used.
- No benchmark answer was used.
- No benchmark run was executed.
- No corpus freeze occurred.
- No chunking freeze occurred.
- No retrieval configuration freeze occurred.
- No model acceptance decision was made from this diagnostic alone.
