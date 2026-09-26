# UC2 Materialization and Chunking Contract Freeze

Date: 2026-09-26
Phase: UC2-P5A

Corpus membership SHA256:
e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4

Materialization config SHA256:
7ec0e41b7ee8d1355d4d0908ca51adc782a47f2ab12612a8b95d4c1009c0e1a4

Chunking config SHA256:
a439204fc1382d9d2b1c57e587422fe0dcd9fece3ced3e3b40a0466ebfea45a8

## Boundary

UC2 corpus membership was frozen before this contract.

Only the 17 ELIGIBLE documents may be materialized.

UC2-C14 / DOC054 is excluded and cannot generate source units,
chunks, embeddings, retrieval evidence, or benchmark evidence.

## Mixed-media rule

PDF:
- one physical page = one source unit.

HTML_SINGLE:
- one acquired HTML document = one source unit.

HTML_BUNDLE:
- each frozen acquired HTML component = one source unit.

HTML extraction prefers the first main element and otherwise falls
back to body/document text. Navigation and non-content structural
elements listed in materialization_config.json are excluded.

## Chunking

The experiment-wide W450/O75 reference is retained:
- maximum 450 whitespace-delimited words;
- 75-word overlap;
- 375-word stride;
- no cross-source-unit chunks.

These values were not selected from UC2 retrieval or benchmark outcomes.

MATERIALIZATION_STARTED=NO
EMBEDDINGS_STARTED=NO
RETRIEVAL_DIAGNOSTIC_STARTED=NO
BENCHMARK_TASKS_CREATED=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
