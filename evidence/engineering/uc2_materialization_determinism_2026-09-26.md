# UC2 Deterministic Materialization Qualification

Date: 2026-09-26
Phase: UC2-P5B

Materializer SHA256:
abd1b0d60f727950789b3cab51e76786e8a74af9b86da9955a8fffe3b6c10069

Materialization config SHA256:
7ec0e41b7ee8d1355d4d0908ca51adc782a47f2ab12612a8b95d4c1009c0e1a4

Chunking config SHA256:
a439204fc1382d9d2b1c57e587422fe0dcd9fece3ced3e3b40a0466ebfea45a8

Source units SHA256:
74bff0c161bc254773c0d4fe20c7aba00828cc88f0267adfa489782f74fb8628

Chunks SHA256:
b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2

Summary SHA256:
50c835d1436eb7023bb67e774742844fcc7fc820865bb5a93cc3f8463fe2d8c2

Aggregate SHA256:
f0d2c677b01dd8df01bc83e7dfbd5174cb2b6ccd75252df84b491679561ac981

Two independent executions from the same frozen raw artifacts and
configuration produced byte-identical source-unit, chunk, and summary files.

Expected source-unit accounting passed:
- PDF physical pages: 97
- HTML source components: 20
- Total source units: 117
- Accepted documents: 17
- DOC054 / UC2-C14: excluded from all runtime materialization

MATERIALIZATION_DETERMINISM=PASS
CORPUS_MEMBERSHIP_FROZEN=YES
MATERIALIZATION_COMPLETED=YES
EMBEDDINGS_STARTED=NO
RETRIEVAL_DIAGNOSTIC_STARTED=NO
BENCHMARK_TASKS_CREATED=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
