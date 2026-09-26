# UC2 Benchmark Task Freeze

Date: 2026-09-26

## Scope

This record freezes T011–T020 for UC2 only, under branch `research/benchmark-task-construction-uc2-uc3` and pre-freeze HEAD `4ca03cde8dd969c07590670615008b17d5448a2e`. UC1 artifacts are unchanged. This does not freeze UC3 or the complete 30-task primary benchmark, and does not authorize benchmark execution.

## Preconditions and explicit researcher approval

All pre-write guards passed: exact branch/HEAD, no tracked/staged changes, exactly the three expected untracked audits/dossier, and all three required SHA256 values. The two earlier audits remain byte-identical.

```text
APPROVAL_TEXT=APPROVE UC2 T011-T020
APPROVAL_DATE=2026-09-26
APPROVED_TASKS=T011-T020
HUMAN_VERIFICATION_COMPLETED=YES
APPROVAL_STAGE=PRE_BENCHMARK
RESULT_DRIVEN_APPROVAL=NO
PRE_APPROVAL_DOSSIER_SHA256=dd5735ef5fe9e5a7ff8f987770959b19e37a4e39700182dee142487f3695f01d
FINAL_APPROVED_DOSSIER_SHA256=db0d81d3e88c8c5e0352dc6bfffaa914c14d55fdbda63644b41e7fcde4c59932
```

The original 143,705 dossier bytes are preserved before the append of `# Researcher Final Approval`. Historical NO-verification fields remain historical; the final approval section records the authorised YES state. Approved questions, answers, difficulty candidates, document and evidence bindings were copied without scientific rewriting, including their inline source citations and paragraph boundaries. JSON formatting and lifecycle/provenance notes are mechanical additions.

Latest candidate bindings: T014 Human-Directed Pre-Freeze Revision 1; T018 Precision Revision 1 including invitation-to-submit correction; T019 Precision Revision 1; T020 Researcher-Directed Pre-Freeze Revision 2. T011–T013/T015–T017 use their unchanged final dossier candidates. Superseded wording is not packaged.

## Canonical format and precedent

- Canonical schema: `benchmark/schema/task.schema.json`, schema version 0.1, identity `https://github.com/emadhammami/responsible-agentic-workflows/benchmark/schema/task.schema.json`.
- Canonical loader: `src/responsible_agentic_workflows/benchmark/tasks.py`.
- UC1 precedent: `benchmark/tasks/UC1/T001.json`–`T010.json`, `benchmark/tasks/UC1/freeze_manifest.json`, and `evidence/engineering/uc1_task_freeze_2026-09-12.md`.
- UC2 layout: `benchmark/tasks/UC2/T011.json`–`T020.json` and `freeze_manifest.json`, mirroring UC1 field order, JSON indentation, status progression and manifest/evidence separation.

No incompatible canonical format was found. Each evidence item retains the approved document ID, page, section and canonical chunk ID. The schema has no per-task use_case_id property; use-case binding is through the canonical UC2 directory/manifest. The existing allocation plan is unchanged.

## Human-verified validation gate

All ten files were first written as `human_verified`. Before freeze, Draft202012Validator checked the canonical schema, the canonical directory loader loaded all ten files, and exact equality against the latest approved dossier candidates passed. The reference answers were compared as complete strings, without shortening or normalising scientific content.

Required document IDs belong to the 17 accepted UC2 documents. Every referenced canonical chunk exists once, matches its document/page and text hash, and the evidence binding equals the approved REQUIRED gold table. Supporting/redundant audit context was not added as mandatory gold. Approved inline answer citations are contained in the gold bindings. The approved source-support and material-synthesis assessments were carried forward without reopening task design or using performance. T019/T020 retain empty document/evidence arrays and their immutable corpus-wide absence audit binding in task notes and the freeze manifest.

```text
TASK_COUNT=10
TASK_IDS_EXACT=T011-T020
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
TASK_SCHEMA_VALIDATION=PASS
TASK_LOADER_VALIDATION=PASS
APPROVED_CONTENT_EQUALITY=PASS
SOURCE_TRACEABILITY=PASS
REFERENCE_SUPPORT=PASS
INSUFFICIENT_EVIDENCE_BINDING=PASS
DUPLICATE_IDS=0
DUPLICATE_EXACT_QUESTIONS=0
TASK_TYPE_INTEGRITY=PASS
```

No materially duplicate answer requirement or accidental gold answer in the approved questions was identified in the approved dossier's pairwise/wording audit; exact final-string equality preserves that assessment. Researcher approval and expected outcome labels are review-side metadata. No benchmark result reference was introduced into a question or answer.

## Gold isolation audit

`BenchmarkTask.to_runtime_task()` / `load_runtime_task()` projects only `task_id` and `question` into the frozen slotted RuntimeTask. On every UC2 file, runtime fields and payload were checked exactly, and gold/metadata attributes were absent. Replacing reference answers, evidence, validation status, notes, task type, documents and difficulty on the benchmark-side object left the runtime payload identical.

Read-only inspection of the actual B0 source path found that its run entry accepts RuntimeTask, feeds only `question` and configured `top_k` to the chain, and forms generation input from question plus retrieved context. It was not invoked. The shared B1/G1 WorkflowState contains only the frozen 18 contract fields; initial_workflow_state parameters and RecoveryPolicyContext expose no gold task fields. A static AST inspection of all workflow modules found no accesses to the prohibited gold/metadata attributes or subscript keys and no full BenchmarkTask loading. The graph uses injected behavioural nodes under this contract; this is structural/contract isolation, not an OS sandbox claim about arbitrary external code.

Frozen contract sources: `docs/benchmark_task_schema.md`, `docs/b1_g1_workflow_contract.md` (state/policy gold boundary) and `docs/b1_g1_runtime_contract.md` (gold exclusion from recovery/revision). The dossier/approval/freeze records are outside the canonical corpus and are not passed as runtime inputs. No corpus or retrieval configuration changed.

Targeted existing engineering tests: `tests/test_benchmark_tasks.py` and `tests/test_workflow_state.py`, **24 passed**, using synthetic loader fixtures/pure state construction only. The final qualification reruns these tests after the status transition. Pytest temporary outputs are directed to `/tmp`; bytecode and pytest cache writes are disabled. No workflow, graph, policy, retrieval operation or model generation is invoked by this selection.

```text
GOLD_REFERENCE_ANSWER_RUNTIME_ACCESS=NO
GOLD_REFERENCE_EVIDENCE_RUNTIME_ACCESS=NO
VALIDATION_STATUS_RUNTIME_ACCESS=NO
TASK_TYPE_RUNTIME_ACCESS=NO
HUMAN_REVIEW_APPROVAL_RUNTIME_ACCESS=NO
EXPECTED_OUTCOME_RUNTIME_ACCESS=NO
BENCHMARK_TASK_EXECUTION=NO
GOLD_ISOLATION=PASS
GOLD_LEAKAGE_AUDIT=PASS
```

## Frozen allocation and identity

T011–T013: direct_retrieval (3). T014–T016: within_document_reasoning (3). T017–T018: cross_document_reasoning (2). T019–T020: insufficient_evidence (2).

- Pre-freeze human-verified task-set SHA256: `9a98dc5a7eea20537d5b4ed0c72467e971d8abe959b41f03ecb5bb57870ea5d8`.
- Frozen task-set SHA256: `8dae88d00cab7fc77024a459dee7d49b6518eacb63077acec9e86d87e5d2de60`.
- Freeze manifest SHA256: `4d15ef3f8dd321b413addbb61f6a80b397282d9670d8ad5f8bf290160fa16e88`.

Hash algorithm, reproduced against the existing UC1 manifest: concatenate UTF-8 records `filename + NUL + lowercase SHA256(file bytes) + LF` in sorted `T*.json` filename order, then SHA256 the concatenation. The manifest is excluded from that task-set digest. Both human-verified and final frozen per-file hashes are bound in `benchmark/tasks/UC2/freeze_manifest.json`. The status transition changed only validation_status from human_verified to frozen; task scientific content and provenance notes remained identical. Complete validation passed again after that transition.

| Final task file | SHA256 |
|---|---|
| T011.json | `9186e34f54d316eb42f60d01d5be698efc5d374f875cd189d1cd076f4f89b326` |
| T012.json | `9698e5ff344ad196585590c1f02c38b91d7213628b464d1bfcd00958a1a8695b` |
| T013.json | `03134ae01701e4ac927eec700bb06b2fd75ea2e0b3716dd7931a800468b9afa8` |
| T014.json | `5b1899d1cdb6b5aa60366d695116c7e233aa80941298149c20642297df6a4f59` |
| T015.json | `f037490c92c3d0d9718708573b429f91620641a5d81663a13bdd6037a17355a8` |
| T016.json | `230908239270ce56b466c2eac369993cf269bd4c64b15029ad2aa06b1ef68a50` |
| T017.json | `040fe84ba5808c8691af6f3f561544cbbff9aa2ca03782e143100f5c30da9732` |
| T018.json | `4b16802c97d3e9ca38e4e047fbe3a39a9c622f7cd4e5eba9749154fae9149610` |
| T019.json | `9c658572a1e42d63956f9a7b80a5320424a46895bc1312352e6220b39bf4c13f` |
| T020.json | `3daf6ead9c7e12e7725b06f3a18c3269684dd25a08ce2cd92da2ee6efcb2f27b` |

## Foundation and review bindings

| Input | SHA256 |
|---|---|
| `benchmark/schema/task.schema.json` | `34ddb275e659b86d759d5fabcf3500bc963c34b60425f601677b88bbb858145f` |
| `corpus/use_cases/UC2/benchmark_scope.json` | `87f8de97ee51645ef140398c02ce94f047d5107412d17e08139551353d3d268d` |
| `corpus/use_cases/UC2/corpus_membership.json` | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl` | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| `benchmark/task_authoring_protocol_v0.1.json` | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |
| `evidence/engineering/uc2_task_candidate_evidence_audit_2026-09-26.md` | `728fe36bcfd3097005594053ffef69cb6ac586a09964be5579a2ee9437f15d56` |
| `evidence/engineering/uc2_insufficient_evidence_absence_audit_2026-09-26.md` | `e068d2c40c378d8b8bb276f6903a0f52502edcab39b301bca9a0106e6eb2f57d` |
| `evidence/engineering/uc2_task_human_review_dossier_2026-09-26.md` | `db0d81d3e88c8c5e0352dc6bfffaa914c14d55fdbda63644b41e7fcde4c59932` |


The canonical corpus identity is UC2-SOURCEUNIT-W450-O75-v0.1, 293 chunks in 17 accepted documents. Membership and frozen UC2 benchmark scope are independently hashed. The authoring protocol is PRIMARY-UC2-UC3-TASK-AUTHORING-v0.1, frozen before authoring. T019/T020's supporting audit covers all 293 records; its citations remain absence provenance rather than positive gold bindings.

## Change control and status

No task may be edited in response to benchmark performance. A genuine post-freeze defect must be recorded, researcher-reviewed, revalidated and frozen again before any affected execution. This record authorizes no execution, commit or push.

```text
LLM_ASSISTED_AUTHORING=YES
HUMAN_VERIFICATION_COMPLETED=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
DIAGNOSTIC_RETRIEVAL_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
TASKS_FROZEN=YES
BENCHMARK_STARTED=NO
UC2_TASKS=10
FROZEN_TASKS=10
UC3_TASKS_FROZEN=NO
PRIMARY_30_TASK_SET_FROZEN=NO
COMMIT=NO
PUSH=NO
```
