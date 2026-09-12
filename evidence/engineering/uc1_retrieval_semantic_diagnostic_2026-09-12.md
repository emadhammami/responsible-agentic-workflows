# UC1 Semantic Retrieval Diagnostic

Date: 2026-09-12

## Purpose

This record preserves the final engineering semantic retrieval gate used
for UC1 embedding-model selection.

This is engineering evidence only. It is not a benchmark result.

## Pre-execution protocol

- Protocol: `UC1-SEMANTIC-RETRIEVAL-PROBES-v0.1`
- Protocol commit: `0cf4989498787bd974cd711363d7715734e82bf6`
- Protocol SHA256: `c5f7fb4021f3850de1d6af8ba397bb80d10c8fad72699ca4ed973da50aae142b`
- Protocol frozen before retrieval results were observed: yes
- Semantic queries excluded canonical document titles, legal references,
  CELEX identifiers, and document IDs by design.
- Identity-diagnostic results were not used to select semantic targets.
- Benchmark questions used: no
- Benchmark gold used: no

## Retrieval configuration

- Retrieval configuration: `UC1-QWEN3-EMBED4B-EXACT-COSINE-v0.1`
- Retrieval configuration SHA256: `a83e43e8c4d3a7ff742bd7d785ba094388d063791032c696f1da2aae65c25da8`
- Embedding model: `qwen3-embedding:4b-q4_K_M`
- Embedding model digest: `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Provider version: `0.34.0`
- Embedding artifact metadata SHA256: `2e7be2db424baf7cc17e807d5a478f96d4fb7a0cb06e0296782629ed29b1f0dc`

## Execution

- Probes: `8`
- Repeats per probe: `3`
- Query runs: `24`
- Top-k: `10`
- Diagnostic wall time: `4.540 seconds`
- Local result artifact SHA256: `3f8cbe46785423fa89cf4af48b152541a1dd33e1d26e489880502773158d6aec`

## Per-probe observations

| Probe | Expected document | Expected document ranks | Stable Top-1 document | Top-10 order variants | Mean latency ms | Min Top-1 margin | Mean Top-1 margin |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| SEM01 | DOC001 | 1,1,1 | DOC001 | 2 | 1041.370 | 0.035691 | 0.035828 |
| SEM02 | DOC003 | 2,2,2 | DOC002 | 1 | 75.878 | 0.005580 | 0.005727 |
| SEM03 | DOC006 | 1,1,1 | DOC006 | 1 | 48.067 | 0.024905 | 0.025062 |
| SEM04 | DOC016 | 1,1,1 | DOC016 | 1 | 71.895 | 0.012855 | 0.013117 |
| SEM05 | DOC020 | 1,1,1 | DOC020 | 1 | 57.223 | 0.011436 | 0.012062 |
| SEM06 | DOC022 | 1,1,1 | DOC022 | 1 | 70.541 | 0.050938 | 0.051200 |
| SEM07 | DOC025 | 1,1,1 | DOC025 | 1 | 70.660 | 0.017772 | 0.018287 |
| SEM08 | DOC028 | 1,1,1 | DOC028 | 1 | 76.364 | 0.016738 | 0.017157 |

## Aggregate observations

- Expected document at rank 1 in all repeats: `7/8`
- Expected document within Top-3 in all repeats: `8/8`
- Expected document within Top-5 in all repeats: `8/8`
- Expected document within Top-10 in all repeats: `8/8`
- Stable Top-1 document across repeats: `8/8`
- Stable Top-1 chunk across repeats: `8/8`
- Exact Top-10 chunk order stable across repeats: `7/8`

The expected document was Rank 1 in all repeats for seven probes.

For `SEM02`, the expected document `DOC003` was Rank 2 in all three
repeats, while `DOC002` was the stable Top-1 document.

## Pre-specified engineering gate

- Minimum Top-10 probes: `7/8`; observed `8/8` - PASS
- Minimum Top-5 probes: `6/8`; observed `8/8` - PASS
- Minimum Top-3 probes: `4/8`; observed `8/8` - PASS
- Minimum stable Top-1 probes: `7/8`; observed `8/8` - PASS

`SEMANTIC_GATE=PASS`

## Interpretation

The fixed semantic diagnostic met every pre-specified engineering
sufficiency criterion. Together with the earlier identity diagnostic,
this provides sufficient pre-benchmark evidence to retain the selected
embedding model for the thesis retrieval stack.

This does not claim that the model is universally optimal or better than
other embedding models. No comparative embedding-model study is part of
the thesis research design.

## Research safeguards

- No benchmark question was used.
- No benchmark gold evidence was used.
- No benchmark run was executed.
- No corpus freeze occurred in this diagnostic.
- No retrieval configuration freeze occurred in this diagnostic.
