# UC3 Raw Filename Canonicalization — Amendment Record

- **Date:** 2026-09-23
- **Branch:** `research/uc3-dc4democracy-corpus-intake`
- **HEAD:** `d9117e441d57f44a6ec8317a0019bf8af2bdcd21`
- **Mode:** `AUTHORIZED_RAW_FILENAME_NORMALIZATION` (Phase 4B2A)

## Purpose

Before Phase 4B2 page/chunk materialization, Phase 4B0 ingestion code
(`src/responsible_agentic_workflows/ingestion/pdf.py:130`) enforces the
invariant:

- **raw filename must start with `{document_id}_`**

This invariant is verified live for UC1 (which passes) and violated for UC3
(which fails the filename/document-ID gate).

This amendment normalizes the **pathnames only**, so the existing ingestion
invariant can be satisfied without modifying source code, PDF bytes, document
IDs, SHA256 values, document status, or any scientific/retrieval parameter.

## Blocker verification (pre-amendment)

| Check | Expected | Actual |
|---|---|---|
| Branch | `research/uc3-dc4democracy-corpus-intake` | ✓ match |
| HEAD | `d9117e441d57f44a6ec8317a0019bf8af2bdcd21` | ✓ match |
| `corpus/use_cases/UC3/processed/` | absent (no materialization yet) | ✓ absent |
| UC1 raw filename convention | `{DOC_ID}_*.pdf` | ✓ `DOC001_eu_forest_strategy_2030.pdf` etc. |
| UC3 raw filename convention | `{UC3-C##}_*.pdf` (violates invariant) | ✓ 9/9 files start with `UC3-C` |
| Ingestion gate for UC3 | `Filename/document ID mismatch` | ✓ confirmed (live raise) |

## Rename mapping (old → new)

Nine files, filesystem rename/move only (no copy, no duplicate). Inode
preservation before vs. after is recorded in the verification section
(e.g. `UC3-C01` inode `34374861` → `DOC032_digcomp_3_0.pdf` inode
`34374861`, i.e. the same directory entry renamed, not a new file created).

| document_id | old filename | new filename | size (bytes) | SHA256 (pre = post) |
|---|---|---|---:|---|
| `DOC032` | `UC3-C01_digcomp_3_0.pdf` | `DOC032_digcomp_3_0.pdf` | 2824377 | `203896c478b72ebb86446c017be78d313be75b03eb9ca1139d061299dfdec84d` |
| `DOC033` | `UC3-C02_rfcdc_volume_1.pdf` | `DOC033_rfcdc_volume_1.pdf` | 4154359 | `a93866bccc575a825b4cc9e9b5f25c115d7c1ffd29dc677a1acc0aa226daa612` |
| `DOC034` | `UC3-C03_rfcdc_volume_2.pdf` | `DOC034_rfcdc_volume_2.pdf` | 3391875 | `ca73e93bcd8c4a0f4076207c80ab221555ced0b0fd58b2a752d40fc849c7853b` |
| `DOC035` | `UC3-C04_rfcdc_volume_3.pdf` | `DOC035_rfcdc_volume_3.pdf` | 6325206 | `0effd90fcd0f6702becaaae11217acac3da0914269b12d0203152c099b285239` |
| `DOC036` | `UC3-C05_key_competences_lifelong_learning.pdf` | `DOC036_key_competences_lifelong_learning.pdf` | 605891 | `dd77e4fe40133869ab29ff7b2232d487786711d50e3687002e02d6a8495a507e` |
| `DOC037` | `UC3-C06_unesco_ict_cft_v3.pdf` | `DOC037_unesco_ict_cft_v3.pdf` | 1642071 | `2c7264c00a453ba71ec5ac75a5213b7a24c8ff165adbcd4b0fc231e950b79534` |
| `DOC038` | `UC3-C07_eu_digital_rights.pdf` | `DOC038_eu_digital_rights.pdf` | 549354 | `9bf3caf8ea2be13f27f1e376eea9d39e9664c308234a20db0a7fb61f873cb32c` |
| `DOC039` | `UC3-C08_digcompedu.pdf` | `DOC039_digcompedu.pdf` | 22977935 | `253e583b818c4913ee8b6d84a8ef2f21faeb347576777f1659d4d16e01186d2b` |
| `DOC040` | `UC3-C09_digcomporg.pdf` | `DOC040_digcomporg.pdf` | 2415102 | `3981f1a2f6ed9ef46777b5d22ce0d11e58610f8f592d8c62e3e5b1f02bcafa09` |

Raw directory: `corpus/use_cases/UC3/raw/`

## Manifest changes (only field modified)

In `corpus/manifest.json`, the **only** modified field across all 9 UC3
records is `local_raw_path` (re-pointed to the renamed canonical names). All
other fields are unchanged, including:

- `document_id`
- `use_case_id`
- `title`
- `organizations`
- `source_reference`
- `source_url`
- `discovered_via`
- `publication_date`
- `language`
- `document_type`
- `rights_note`
- `local_processed_path` (still `null`)
- `sha256` (unchanged)
- `status` (still `accepted`)
- `exclusion_reason`

The pre/post manifest diff confirms the set of changed keys per UC3 record is
exactly `{local_raw_path}` and that the UC1 record set (and all other
non-UC3 records) is byte-identical across the diff.

## Preserved (intentionally NOT modified)

- `corpus/use_cases/UC3/acquisition_audit.tsv` — its filename column records
  the acquisition-time filename and therefore remains valid provenance of the
  original download naming. SHA256 before and after:
  `f031cb6259f8cf58270840a61da56fc3942520283f222da6e28cecd4a718e79d`
- `corpus/use_cases/UC3/benchmark_scope.json` — unchanged
- `corpus/use_cases/UC3/chunking_config.json` — unchanged
- `benchmark/config/retrieval/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json` — unchanged
- `corpus/quality/UC3/DOC032.json` through `DOC040.json` — unchanged (9/9 SHA256
  match the expected values in
  `evidence/engineering/uc3_preprocessing_contract_2026-09-23.md`)
- All source code under `src/` (no code change was required by this
  amendment; `pdf.py:130` guard remains intact)
- All tests under `tests/`
- `corpus/use_cases/UC3/source_selection.tsv`, `download_queue.json`, `README.md`

## Pre/post verification results

| Check | Required | Actual |
|---|---|---|
| Canonical `DOC032`–`DOC040` raw PDFs present | 9 | 9 |
| Old `UC3-C01`–`UC3-C09` raw PDFs remaining | 0 | 0 |
| Duplicate raw PDFs | 0 | 0 |
| Disk SHA256 = manifest SHA256 (9/9) | 9/9 | 9/9 MATCH |
| File sizes unchanged (9/9) | 9/9 | 9/9 MATCH |
| Every filename starts with `{document_id}_` (9/9) | 9/9 | 9/9 MATCH |
| Ingestion filename guard passes for all 9 | 9/9 | 9/9 PASS |
| Manifest change set (UC3 records) | `{local_raw_path}` only | ✓ exact match |
| Other use-case manifest records | unchanged | ✓ UC1 byte-identical |
| `acquisition_audit.tsv` SHA256 | unchanged | ✓ `f031cb62…a718e79d` |
| `benchmark_scope.json` SHA256 | `d3cfdd25…7102` | ✓ match |
| `chunking_config.json` SHA256 | `cca30db2…c188` | ✓ match |
| retrieval config SHA256 | `33537bd0…37eef` | ✓ match |
| 9/9 `corpus/quality/UC3/DOC*.json` SHA256 | unchanged vs evidence record | ✓ 9/9 match |
| `corpus/use_cases/UC3/processed/` | absent | ✓ absent |
| `corpus/use_cases/UC3/tasks/` | absent | ✓ absent |
| Any pages, chunks, or embeddings | none present | ✓ none |
| Scientific / retrieval parameter changes | none | ✓ none |
| Source code modifications | none | ✓ none |
| Benchmark started | NO | **NO** |
| Corpus frozen | NO | **NO** |
| Commit / push | NO | **NO** |

## Non-mutating ingestion probe (9/9)

`extract_pdf_document` was invoked for each of DOC032–DOC040 as a
non-writing compatibility probe only. Results:

| document_id | gate | pages extracted / expected | words match quality |
|---|---|---|---|
| DOC032 | PASS | 123 / 123 | True |
| DOC033 | PASS | 89 / 89 | True |
| DOC034 | PASS | 65 / 65 | True |
| DOC035 | PASS | 129 / 129 | True |
| DOC036 | PASS | 13 / 13 | True |
| DOC037 | PASS | 66 / 66 | True |
| DOC038 | PASS | 7 / 7 | True |
| DOC039 | PASS | 95 / 95 | True |
| DOC040 | PASS | 77 / 77 | True |

`corpus.process` was **not** invoked in this phase.

## Explicit statement

> This amendment is an implementation-compatibility pathname normalization
> performed before derived corpus materialization and before scientific
> benchmark execution. It does not change document content, corpus
> membership, inclusion decisions, or experimental parameters.

## Status

```
UC3_RAW_FILENAME_CANONICALIZATION=PASS
FILES_RENAMED=9
RAW_PDF_CONTENT_HASHES_UNCHANGED=YES
RAW_FILE_SIZES_UNCHANGED=YES
MANIFEST_LOCAL_RAW_PATHS_UPDATED=9
OTHER_MANIFEST_FIELDS_CHANGED=NO
ACQUISITION_AUDIT_MODIFIED=NO
INGESTION_FILENAME_GUARD_PASS=9/9
PREPROCESSING_CONTRACT_PARAMETERS_CHANGED=NO
PROCESSED_ARTIFACTS_CREATED=NO
EMBEDDINGS_CREATED=NO
CORPUS_FROZEN=NO
TASKS_CREATED=0
BENCHMARK_STARTED=NO
SOURCE_CODE_MODIFIED=NO
COMMIT=NO
PUSH=NO
```
