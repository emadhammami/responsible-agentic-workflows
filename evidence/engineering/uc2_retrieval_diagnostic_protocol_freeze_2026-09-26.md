# UC2 Retrieval Diagnostic Protocol Freeze

Date: 2026-09-26
Phase: UC2-P6C0

Identity protocol SHA256:
c2314976329ea65d11b25d2d88d1a0eccf00c2cf5fd934697e6cec11b7c51482

Semantic protocol SHA256:
d12def0c87d30324e6b7fb739de66d03f8193829fff67a637200e764d3b3c95a

Frozen before any UC2 identity or semantic retrieval diagnostic execution.

## Execution
- accepted documents: 17
- identity probes: 17
- semantic probes: 17
- document coverage: 17/17
- ranking unit: chunk
- top_k: 10 (diagnostic only)
- repeats per probe: 3
- expected-document measure: first retrieved chunk belonging to expected document

## Prospective semantic gate

Inherited from UC1's frozen 7/6/4/7-of-8 gate and scaled with CEILING:

- top-10 all repeats: ceil(17 * 7/8) = 15
- top-5 all repeats: ceil(17 * 6/8) = 13
- top-3 all repeats: ceil(17 * 4/8) = 9
- stable top-1 document across repeats: ceil(17 * 7/8) = 15

Identity retrieval is descriptive engineering evidence and has no pass/fail
acceptance gate.

The previously observed embedding Run-1/Run-2 variation did not change probe
queries, expected documents, top_k, repeat count, or semantic thresholds.

No benchmark question, benchmark gold, benchmark answer, or retrieval result was
used to define these protocols.

Benchmark production top_k remains unfrozen and is not set by diagnostic top_k=10.

IDENTITY_PROTOCOL_FROZEN=YES
SEMANTIC_PROTOCOL_FROZEN=YES
RETRIEVAL_DIAGNOSTICS_EXECUTED=NO
RETRIEVAL_FOUNDATION_FROZEN=NO
BENCHMARK_STARTED=NO
