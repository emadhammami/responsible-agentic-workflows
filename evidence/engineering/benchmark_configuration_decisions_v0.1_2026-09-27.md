# Prospective Primary Benchmark Configuration Decisions v0.1

Date: 2026-09-27
Base HEAD: 6a8f3cbb9a333058bc9deb023eb5d93667882df2
Status: prospective pre-benchmark configuration decision
Benchmark started: NO

## 1. Frozen generation foundation

Model configuration:
benchmark/config/model/OLLAMA-QWEN38-27B-48K-v0.1.json

SHA256: f507c2d4270ad64a81ebaaef2c18a7236fba26dd30a99ed79ceed5d9b728b5e1

Already-frozen behavior:
- provider: Ollama 0.34.0
- model: qwen3.8-27b-48k:latest
- configured context: 49152
- temperature: 0
- generation seed: 20260912
- thinking: false
- same model identity for B0/B1/G1

New prospective benchmark decision:
- max_output_tokens: 1024

## 2. Retrieval

Frozen retrieval configurations:
- UC1 SHA256: b3feaf22eb7126751837c6dc1dade05afc5b289dd353155e7644cdd83557109c
- UC2 SHA256: 6df4b73e262261e907f8e6e227619be1b996ced6b688eca478c7f56748acc169
- UC3 SHA256: cbc006fbab5623af240613e4348bccd17107943e0556a5746409130cd073bac1

Prospective benchmark decision:
- top_k: 10
- same initial top_k for B0/B1/G1
- B1/G1 recovery retrieval uses the same top_k
- no condition-specific retrieval tuning

top_k=10 is newly selected here for the scientific benchmark.
Earlier top_k=10 uses were engineering diagnostics only and are not
retroactively reclassified as benchmark freezes.

Rationale: all three retrieval foundations were already exercised at this
common engineering operating point. Selecting it now avoids introducing a new,
unqualified retrieval breadth and does not use primary benchmark outcomes.

## 3. Prompts

- B0 prompt version: b0-engineering-v0.1
- B1 prompt version: agentic-engineering-v0.1
- G1 prompt version: agentic-engineering-v0.1
- B1 and G1 prompt bundles MUST remain identical.
- Existing source prompt bytes will be cryptographically bound at final freeze.

## 4. Workflow identifiers

- B0: b0-two-step-rag-v0.1
- B1: b1-agentic-fixed-recovery-v0.1
- G1: g1-agentic-ergr-v0.1

The B1/G1 graph and execution implementation remain shared; only the injected
RecoveryPolicy is condition-specific.

## 5. Resource limits

Prospective common limits:
- max_llm_calls_per_run: 5
- max_retrieval_calls_per_run: 2
- max_retries_per_run: 1
- max_total_tokens_per_run: null
- timeout_ms: null

Rationale:
The finite call/retrieval/retry ceilings correspond to the maximum legitimate
single-recovery frozen graph path. Total token use remains a measured outcome,
not an arbitrary stopping threshold. Timeout is disabled to avoid
machine-load-dependent scientific censoring; latency remains measured.

## 6. Execution

- repetitions_per_task_condition: 3
- primary tasks: 30
- conditions: B0, B1, G1
- planned primary runs: 270
- orchestration seed: 20260912

A complete 270-run execution-order manifest MUST be generated once,
cryptographically frozen, and treated as authoritative before the first
primary benchmark run. It MUST NOT be regenerated in response to outcomes.

## 7. Configuration structure

Because UC1, UC2, and UC3 have distinct frozen retrieval configuration and
chunking identities, the primary benchmark will use one configuration instance
per use case, sharing all non-retrieval scientific settings.

Planned IDs:
- benchmark-config-primary-uc1-v0.2
- benchmark-config-primary-uc2-v0.2
- benchmark-config-primary-uc3-v0.2

## 8. Schema amendment

Current benchmark configuration schema v0.1 does not represent timeout_ms.

Before configuration freeze:
1. preserve the current v0.1 schema byte-for-byte as historical provenance;
2. prospectively revise the canonical schema to v0.2;
3. add required nullable timeout_ms to resource_limits;
4. validate all three final configuration instances against v0.2.

## 9. Scientific controls

RESULT_DRIVEN_REVISION=NO
BENCHMARK_TASK_EXECUTION=NO
BENCHMARK_STARTED=NO
TOP_K_SELECTED_FROM_PRIMARY_RESULTS=NO
MODEL_SELECTED_FROM_PRIMARY_RESULTS=NO
PROMPTS_SELECTED_FROM_PRIMARY_RESULTS=NO
RESOURCE_LIMITS_SELECTED_FROM_PRIMARY_RESULTS=NO
