# UC3 T021–T030 Human Approval Evidence

Date: 2026-09-27

APPROVAL_TEXT=APPROVE UC3 T021-T030
APPROVAL_SCOPE=T021-T030
APPROVED_STAGE=latest reviewed pre-freeze candidates
PROTOCOL_VERSION=0.2
T029_T030_APPROVED_VERSION=RESEARCHER_DIRECTED_REVISION_1
HUMAN_VERIFICATION_COMPLETED=YES
RESULT_DRIVEN_REVISION=NO
BENCHMARK_RESULT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_STARTED=NO
TASKS_FROZEN=NO

The researcher explicitly supplied the approval text above in this session. It approves the latest reviewed candidate questions, types, reference-answer candidates and document/evidence bindings for T021–T030, including the appended researcher-directed Revision 1 for T029 and T030. This records human verification and authorizes canonical materialization with validation_status human_verified. It does not authorize benchmark execution or claim cryptographic task freeze. Historical authoring/review artifacts are preserved unchanged; their earlier NO status fields remain true of their recorded stages.

BRANCH=research/benchmark-task-construction-uc2-uc3
BASE_HEAD=55d6e33b2674b01969773ee8b99bf71839f94997
PROTOCOL_FREEZE_COMMIT=55d6e33b2674b01969773ee8b99bf71839f94997
UC3_FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a

## Approved source and review bindings

INVENTORY_PATH=evidence/engineering/uc3_task_authoring_inventory_2026-09-26.md
INVENTORY_SHA256=f73f3c06bb96eeec47e0602b1d9d521f346a003bb39be39dfdf2f8f3ec0ef476
CANDIDATE_AUDIT_PATH=evidence/engineering/uc3_task_candidate_evidence_audit_2026-09-26.md
CANDIDATE_AUDIT_SHA256=9ab8222b7526cca0325855a2b3e7abf6746b2fb411ce0f91f9d71f99468f181f
ABSENCE_AUDIT_PATH=evidence/engineering/uc3_insufficient_evidence_absence_audit_2026-09-27.md
ABSENCE_AUDIT_SHA256=577031ef70ae369ee0b3b9b1291b23a8453c4f3de6e00b5b0bf265ed3b593fad
DOSSIER_PATH=evidence/engineering/uc3_task_human_review_dossier_2026-09-27.md
DOSSIER_SHA256=4376a5dcc36c1bb2f9590949cf71db32dc3faf5d6d6ea4cf0da887f91dc049be
PROTOCOL_PATH=benchmark/task_authoring_protocol_v0.2.json
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6

SCHEMA_PATH=benchmark/schema/task.schema.json
SCHEMA_SHA256=34ddb275e659b86d759d5fabcf3500bc963c34b60425f601677b88bbb858145f
CANONICAL_PUBLIC_CORPUS_PATH=corpus/use_cases/UC3/processed/chunks/index.json and nine indexed per-document chunk files
CORPUS_DOCUMENT_COUNT=9
CORPUS_SOURCE_UNIT_COUNT=664
CORPUS_CHUNK_COUNT=850

## Approved allocation and evidence status

TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2

| Tasks | Type | Approved evidence status |
| --- | --- | --- |
| T021–T023 | direct_retrieval | Exact REQUIRED localized source bindings from candidate audit/dossier. |
| T024–T026 | within_document_reasoning | Distinct REQUIRED source locations in one document. |
| T027–T028 | cross_document_reasoning | Both named documents contribute material evidence. |
| T029–T030 | insufficient_evidence | Latest Revision 1; required_documents and reference_evidence intentionally empty; bound to complete revised-question corpus-wide absence audit. |

T021–T028 retain their exact recorded questions and answers. T029/T030 use only the latest precision-revision question and reference-answer candidate. Difficulty values are the reviewed dossier candidates. Canonical positive evidence carries native document_id, physical page, section and chunk_id. No optional SUPPORTING or REDUNDANT chunk is added as mandatory evidence.

VALIDATION_STATUS_ALL=human_verified
CRYPTOGRAPHIC_TASK_FREEZE_COMPLETED=NO
FREEZE_MANIFEST_CREATED=NO
FROZEN_PUBLIC_CORPUS_ONLY=YES
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
BENCHMARK_TASK_EXECUTION=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
STAGE=NO
COMMIT=NO
PUSH=NO
