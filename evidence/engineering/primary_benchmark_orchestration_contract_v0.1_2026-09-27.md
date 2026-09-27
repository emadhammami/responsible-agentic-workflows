# Primary Benchmark Orchestration Contract v0.1

Date: 2026-09-27
Base HEAD: 17185aaf21a7633b0515190c12b61e379918c560
Status: prospective pre-implementation, pre-benchmark
BENCHMARK_STARTED=NO
RESULT_DRIVEN_REVISION=NO

## 1. Scope

This contract defines construction and execution plumbing only.
It does not alter frozen tasks, corpora, retrieval foundations, model,
prompts, graph, policies, or scientific configuration.

No T001-T030 execution is permitted during implementation qualification.

## 2. Runtime-task isolation

Primary execution MUST load RuntimeTask only:
- task_id
- question

Reference answers, reference evidence, task type, difficulty, and other gold
fields MUST NOT enter model, retrieval, workflow, policy, or orchestration
execution.

## 3. Frozen configuration

Each run MUST require one frozen primary UC configuration.

Mapping:
UC1 -> benchmark-config-primary-uc1-v0.2
UC2 -> benchmark-config-primary-uc2-v0.2
UC3 -> benchmark-config-primary-uc3-v0.2

Runtime values MUST be read from those frozen configs rather than duplicated
as independent behavioral defaults.

## 4. Retrieval construction

UC1 and UC3:
use the canonical indexed artifact loader
responsible_agentic_workflows.retrieval.materialize.load_embedding_artifacts.

UC2:
use a dedicated read-only compatibility loader for the historically frozen
source-unit representation.

UC2 authoritative bindings:
chunks.jsonl SHA256:
b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2
chunk_ids.json SHA256:
05992722b95803df4396ad9fa321876bd4d9023ca2b0196a74eb728edff43c7d
embeddings.npy SHA256:
621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f
metadata.json SHA256:
1901048651cb93b4b52f9529a9706c0ec81ea0ded9f92ea0fd48b88e1032618e
retrieval config SHA256:
6df4b73e262261e907f8e6e227619be1b996ced6b688eca478c7f56748acc169

The UC2 loader MUST verify:
- frozen status and retrieval identity;
- all bound hashes;
- 293 rows/chunks;
- 2560 dimensions, float32, finite, non-zero rows;
- unique chunk IDs;
- exact chunks.jsonl -> chunk_ids.json -> matrix row-order parity.

It MUST NOT rewrite, normalize, rechunk, reorder, or re-embed anything.

UC2 DocumentChunk adaptation:
- document_id <- document_id
- chunk_id <- chunk_id
- text <- text byte-equivalent Python string content
- title <- source_inventory.tsv title matched by candidate_id
- section <- source_unit_id
- section_index <- source_unit_index
- source_file <- source_component_path
- page <- pdf_page_number

Missing/ambiguous title mapping or any binding mismatch MUST fail closed.

All UCs then use the existing DenseExactRetriever.

## 5. Query embedding

Construct OllamaEmbeddingClient solely from the frozen retrieval configuration:
model tag, dimensions, query instruction, truncate setting.

Transport timeout_seconds = 300.0.

This timeout is an operational HTTP safety cap, not workflow resource control.

## 6. Generation model

Construct OllamaChatModel from the frozen generation identity:
- model qwen3.8-27b-48k:latest
- context 49152
- seed 20260912
- thinking false

Generation temperature and max_output_tokens come from the frozen UC config.

Chat HTTP transport timeout = 300.0 seconds.

The 300-second transport timeout is condition-invariant and is NOT
resource_limits.timeout_ms. Scientific workflow timeout remains null.
Transport expiry is a provider/tool failure, never RESOURCE_STOP.

## 7. Conditions

B0:
- B0Baseline
- frozen top_k
- frozen B0 prompt/workflow IDs.

B1:
- AgenticRunner
- B1FixedRecoveryPolicy
- same model/retriever/top_k as G1
- frozen common ResourceLimits.

G1:
- AgenticRunner
- G1ERGRPolicy
- same model/retriever/top_k as B1
- frozen common ResourceLimits.

B1/G1 differ behaviorally only through injected RecoveryPolicy.

Policy IDs are logging identifiers only:
- b1-fixed-recovery-policy-v0.1
- g1-ergr-policy-v0.1

## 8. Recorder and failure handling

Every primary run uses execution_mode="benchmark" and its assigned condition.

RunConfiguration MUST use the frozen condition-specific prompt/workflow ID and
common model/retrieval values.

AgenticRunner remains authoritative for B1/G1 terminal semantics.

The orchestration layer MUST make B0 failure logging total:
- logged model/retrieval failure -> tool_error;
- other exception -> failed;
- never convert failure to abstention.

Every returned record MUST validate against run.schema.json.

## 9. Persistence

Every completed or failed attempted run MUST be persisted with
write_validated_run_record.

Existing run files MUST never be overwritten.

run_id, experiment_id, output path, repetition, and execution sequence are
supplied by the later frozen execution-order manifest; the harness MUST NOT
invent or randomize them.

## 10. Qualification boundary

Harness qualification uses synthetic T901-T907 / synthetic in-memory fixtures
only.

No primary task execution, no primary answer inspection, and no run-order
generation are permitted during T5G implementation.

Execution-order freeze and final executable code-revision freeze remain
pending after synthetic qualification.

BENCHMARK_TASK_EXECUTION=NO
BENCHMARK_STARTED=NO
