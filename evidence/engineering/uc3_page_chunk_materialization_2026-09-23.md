# UC3 Page & Chunk Materialization — Evidence Record

- **Date:** 2026-09-23
- **Phase:** 4B2
- **Branch:** `research/uc3-dc4democracy-corpus-intake`
- **HEAD:** `d9117e441d57f44a6ec8317a0019bf8af2bdcd21`
- **Mode:** `DETERMINISTIC_PAGE_CHUNK_MATERIALIZATION` (not `CORPUS_FREEZE`)

## Pre-execution guard (4B2 Step 2)

| Check | Required | Actual |
|---|---|---|
| Branch | `research/uc3-dc4democracy-corpus-intake` | ✓ match |
| HEAD | `d9117e441d57f44a6ec8317a0019bf8af2bdcd21` | ✓ match |
| `benchmark_scope.json` SHA256 | `d3cfdd25…7102` | ✓ match |
| `chunking_config.json` SHA256 | `cca30db2…c188` | ✓ match |
| retrieval config SHA256 | `33537bd0…37eef` | ✓ match |
| Quality records DOC032–DOC040 SHA256 | 9/9 match evidence record | ✓ 9/9 |
| Raw PDF SHA256 vs manifest | 9/9 match | ✓ 9/9 |
| `corpus/use_cases/UC3/processed/` | absent (no materialization yet) | ✓ absent |
| `corpus/use_cases/UC3/tasks/` | absent | ✓ absent |
| `corpus/use_cases/UC3/processed/embeddings/` | absent | ✓ absent |
| `corpus/USE_CASES.md` UC1 line | `4B1B COMPLETED` (not `FROZEN`) | ✓ |

## Write-semantics inspection (4B2 Step 3 precondition)

Both entry points use atomic staging → `pathlib.replace` and refuse to write
into a non-empty target directory. No destructive overwrite is possible.
`process.py` and `chunks.py` were **not modified** in this task.
`chunking.chunk_pdf_document` is a pure, deterministic function
(`stable_hash` = SHA256 of the pre-specified working chunking config; no
wall-clock, no randomness, no LLM).

- `corpus.process._atomic_write_json`
- `corpus.chunks._atomic_write_json`
- `ingestion.chunking.chunk_pdf_document`

## Materialization execution (4B2 Steps 4–5)

Command 1 (pages):

```
python -m responsible_agentic_workflows.corpus.process --use-case UC3
DOCUMENT_COUNT=9
TOTAL_PAGES=664
TOTAL_WORDS=224540
OUTPUT_DIRECTORY=corpus/use_cases/UC3/processed/pages
```

Command 2 (chunks):

```
python -m responsible_agentic_workflows.corpus.chunks --use-case UC3
DOCUMENT_COUNT=9
TOTAL_CHUNKS=850
TOTAL_CHUNK_WORDS=240440
PAGES_WITH_CHUNKS=638
OUTPUT_DIRECTORY=corpus/use_cases/UC3/processed/chunks
```

## Per-document results

| document_id | total_pages | pages_present | source_sha256_match | pages_json_sha256 | chunk_count | nonempty_chunks | canonical_filename_in_source_file | chunks_json_sha256 |
|---|---|---|---|---|---|---|---|---|
| DOC032 | 123 | 123 | YES | `0a08ae673a61590f6e51a0568eb46ec02d15b5f58ca34de4c9095e065f7c38c9` | 177 | 177 | DOC032_digcomp_3_0.pdf | `31ff428f15298c2f22e44d695cc0acbd99570ef7f375073855a2a095c08de136` |
| DOC033 | 89 | 89 | YES | `5683f3c9b86ad01b35674ba1be6fa80246151d73db39e554df270d603d9e3a29` | 111 | 111 | DOC033_rfcdc_volume_1.pdf | `227a40b3df7e2853501aeb6333f943c2fdd321fe506bc7e80c16c24236e156b2` |
| DOC034 | 65 | 65 | YES | `6ad5d73f555a4beb06be72027bf90b012be1b44436d82252fc3ad4ec339e4bb4` | 63 | 63 | DOC034_rfcdc_volume_2.pdf | `d39dc4a040e87e0b2fecb3cb308ac54e0563f584dffcf620676c2d3927c90cd0` |
| DOC035 | 129 | 129 | YES | `512d539b144b93870d2c93e3cf8958e48b3d63b950608b055447a85e749af910` | 178 | 178 | DOC035_rfcdc_volume_3.pdf | `248007fdccbc757b93a376f43c0f3656c62be448b39c399a5441ee11e325a1a1` |
| DOC036 | 13 | 13 | YES | `7634cd13da92793866ed66d92ad726db435d3f57dc4b3e67e6198cd27733a481` | 24 | 24 | DOC036_key_competences_lifelong_learning.pdf | `30874450493323ed59a0c37f09678c99e4de9e28dbdb44fe89f55bb502d3f8a8` |
| DOC037 | 66 | 66 | YES | `e166e3d814ce064e6dbe575a10a5116aa496b5304892470825621cea77bba8cf` | 88 | 88 | DOC037_unesco_ict_cft_v3.pdf | `fa6c3055a87e08e6e60ec4b68a8932f334a9b9e0b62d6f7e9888d26d8f0e7dcf` |
| DOC038 | 7 | 7 | YES | `cdc9b6f907684fd7d976f2592fc32d8fa749e9846e1c60ccd2c5c08a187a377c` | 11 | 11 | DOC038_eu_digital_rights.pdf | `673a73109e48d106caa67c1cff48c5ce368a128186a64e817bd67860ebf70802` |
| DOC039 | 95 | 95 | YES | `5f04f101c348281e7bf26272996e35ff26cc1583c14c9750290d4e6e082438ec` | 95 | 95 | DOC039_digcompedu.pdf | `07957a35bd95c3d9f07e92acde88ff8fe69502b8714b57469623363490a46b66` |
| DOC040 | 77 | 77 | YES | `e97bb1386f7af93a20c9a629e461bebdba46ba9b903d333dc1e6f8342e776c9c` | 103 | 103 | DOC040_digcomporg.pdf | `7b93b8bed558531d08280fc609a2470a02d6859a6a8616867d40e8fe02dd0312` |

- `SUM_PAGES=664` (123+89+65+129+13+66+7+95+77)
- `SUM_CHUNKS=850` (177+111+63+178+24+88+11+95+103)

## Pre-specified working contract parameter compliance (every chunk)

- `strategy = page_aware_word_windows` — enforced by
  `chunk_pdf_document` (per-page windows).
- `max_words = 450` — validated: **0 chunks exceed 450 words** (max observed
  word count across all 850 chunks ≤ 450).
- `overlap_words = 75` — enforced at window construction. (Overlap is a
  construction parameter, not a per-chunk invariant; the pre-specified value
  is recorded in `chunking_config.json` (status: `working`) and its SHA256
  is unchanged.)
- `cross_page_boundaries = false` — validated: **every chunk has a single
  integer `page` field; no chunk references more than one page**.
- `empty_pages_generate_chunks = false` — validated by
  per-page invariant below.

## Empty-page / overlap invariant (4B2 boundary checks)

Across all 9 documents, 664 pages total:

| Invariant | Required | Actual |
|---|---|---|
| Pages with non-empty text | report | **638** |
| Pages with empty text (blank/whitespace-only) | report, must produce no chunk | **26** |
| **Non-empty pages that got 0 chunks** | 0 | **0 ✓** |
| **Empty pages that produced ≥1 chunk** | 0 | **0 ✓** |
| Chunks with empty text | 0 | **0 ✓** |
| Documents with 0 chunks | 0 | **0 ✓** |
| Chunks spanning more than one page | 0 | **0 ✓** |
| Chunks with word count > 450 | 0 | **0 ✓** |

## Determinism double-run (4B2 Step 6)

- **Run 1:** generated all 18 file hashes (9 pages + 9 chunks) and the 2
  `index.json` files → 20 entries. Combined SHA256 over the sorted
  "KEY SHA256" list:
  `fafcdb43ceefe249cedc517adab7b2482a4875eaf1ca907503b665256a0d2fc2`
  (snapshot preserved at `/tmp/opencode/materialization_hashes_run1.txt`).
- **Run 1→Reset:** deleted all `*.json` under
  `corpus/use_cases/UC3/processed/pages/` and
  `.../processed/chunks/`.
- **Run 2:** re-executed `python -m responsible_agentic_workflows.corpus.process
  --use-case UC3` then
  `python -m responsible_agentic_workflows.corpus.chunks --use-case UC3`.
- **Comparison:** 20/20 file hashes in Run 2 are byte-identical to Run 1
  (0 mismatches). Per-document `pages_json_sha256` and
  `chunks_json_sha256` values above are taken from Run 2 (equivalently Run 1).

`DETERMINISM_2_RUNS=PASS`

## Canonical hash set & aggregate (4B2B Step 2)

Canonical format: one line per artifact,
`relative_path<TAB>sha256<NEWLINE>`, relative to
`corpus/use_cases/UC3/processed/` (e.g. `pages/DOC032.pages.json`), sorted
lexicographically by relative path. 20 lines (9 pages + 9 chunks + 2
`index.json`). Aggregate SHA256 is computed over the UTF-8 bytes of the
concatenated lines.

- `CANONICAL_FILE_COUNT=20`
- `CANONICAL_AGGREGATE_SHA256=12174dc832dae5782f050f7982ce796de0108bae33d973e5b2fbd82c76b5a30d`
- Cross-check against Run 1 snapshot
  (`/tmp/opencode/materialization_hashes_run1.txt`): key sets identical,
  **20/20 per-file hashes equal**, 0 mismatches.
- Aggregate recomputed from Run 1 values equals the Run 2 aggregate
  (`RUN1_RUN2_AGGREGATE_EQUAL=YES`).

`BYTE_LEVEL_DETERMINISM=PASS`

## Global chunk-ID validation (4B2B Step 3)

- ID format regex
  `^DOC0(32|33|34|35|36|37|38|39|40)-P[0-9]{4}-C[0-9]{3}$`: 850/850 valid.
- `GLOBAL_CHUNK_IDS=850`; `GLOBAL_UNIQUE_CHUNK_IDS=850`; unique.
- Document binding (`P` prefix document == chunk `document_id`): 850/850.
- Page binding (page number in ID == chunk `page`): 850/850.
- Per (doc, page) chunk sequences: strictly ordered, unique, starting at
  C001; artifact order follows (doc, page, chunk) sequence: PASS.
- Text non-empty: 850/850; `page` is an integer in every chunk: 850/850.

## Per-document chunk statistics (4B2B Step 4)

| document_id | total_pages | nonempty_pages | empty_pages | chunk_count | min_words | max_words | mean_words |
|---|---|---|---|---|---|---|---|
| DOC032 | 123 | 123 | 0 | 177 | 3 | 450 | 304.46 |
| DOC033 | 89 | 81 | 8 | 111 | 16 | 450 | 288.40 |
| DOC034 | 65 | 58 | 7 | 63 | 18 | 450 | 254.14 |
| DOC035 | 129 | 125 | 4 | 178 | 32 | 450 | 298.17 |
| DOC036 | 13 | 13 | 0 | 24 | 46 | 450 | 338.88 |
| DOC037 | 66 | 66 | 0 | 88 | 8 | 450 | 286.34 |
| DOC038 | 7 | 7 | 0 | 11 | 102 | 450 | 328.36 |
| DOC039 | 95 | 88 | 7 | 95 | 1 | 450 | 216.87 |
| DOC040 | 77 | 77 | 0 | 103 | 21 | 450 | 270.93 |

- `TOTAL_NONEMPTY_PAGES=638`; `TOTAL_EMPTY_PAGES=26`;
  empty pages produced 0 chunks in every case.
- Global min/mean/max chunk words: **1 / 282.87 / 450**
  (240,440 chunk words over 850 chunks).

## Working (not frozen) status (4B2B Step 5)

- `chunking_config.status=working` (SHA256 `cca30db2…b4c188`, unchanged)
- `benchmark_scope.status=working` (SHA256 `d3cfdd25…7102`, unchanged)
- retrieval config `status=working` (SHA256 `33537bd0…37eef`, unchanged)
- `CORPUS_FROZEN=NO`

## Post-execution validation (4B2 Step 7)

| Check | Required | Actual |
|---|---|---|
| 9 raw PDFs unchanged (SHA256 + size) | 9/9 | 9/9 MATCH |
| 9 `DOC*.pages.json` present | YES | YES |
| 9 `DOC*.chunks.json` present | YES | YES |
| No `embeddings` directory / files | absent | ✓ absent |
| No `tasks` directory | absent | ✓ absent |
| `benchmark_scope.json` SHA256 | `d3cfdd25…7102` | ✓ unchanged |
| `chunking_config.json` SHA256 | `cca30db2…c188` | ✓ unchanged |
| retrieval config SHA256 | `33537bd0…37eef` | ✓ unchanged |
| 9/9 `corpus/quality/UC3/DOC*.json` SHA256 | unchanged vs evidence record | ✓ 9/9 |
| `src/` source code | unmodified | ✓ unmodified |
| `tests/` code | unmodified | ✓ unmodified |
| `corpus/USE_CASES.md` | UC1 line still `4B1B COMPLETED`; no line now `FROZEN` | ✓ |
| UC2 / UC4 / any other use case | untouched | ✓ |
| Scientific parameters / retrieval parameters | unchanged | ✓ |
| Benchmark executed | NO | **NO** |

## Tests (4B2 Step 8)

Command:

```
python -m pytest tests/test_chunk_materialization.py \
                 tests/test_pdf_chunking.py \
                 tests/test_pdf_ingestion.py \
                 tests/test_corpus_quality.py -v
```

Result: **19 passed in 0.09s** (5 + 6 + 5 + 3, all green).

```
tests/test_chunk_materialization.py ...                      [ 15%]
tests/test_pdf_chunking.py ......                             [ 47%]
tests/test_pdf_ingestion.py .....                             [ 73%]
tests/test_corpus_quality.py .....                            [100%]
============================== 19 passed in 0.09s ==============================
```

No test file was created or modified; the four files were already present
and are the existing, relevant tests for page materialization, chunking,
PDF ingestion, and corpus quality.

## Git hygiene (4B2 Step 8)

```
$ git diff --check
(clean — no whitespace errors)

$ git status --short --untracked-files=all
 M corpus/manifest.json
?? benchmark/config/retrieval/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json
?? corpus/quality/UC3/DOC032.json
... (9 quality records)
?? corpus/use_cases/UC3/{README.md, acquisition_audit.tsv, benchmark_scope.json,
                         chunking_config.json, download_queue.json,
                         eligibility_review.tsv, source_selection.tsv,
                         processed/ (new)}
?? evidence/engineering/uc3_preprocessing_contract_2026-09-23.md
?? evidence/engineering/uc3_raw_filename_canonicalization_2026-09-23.md
?? evidence/engineering/uc3_page_chunk_materialization_2026-09-23.md   (this file)
```

## Status block

```
UC3_PAGE_CHUNK_MATERIALIZATION=PASS
DOCUMENTS_MATERIALIZED=9
TOTAL_PAGES=664
TOTAL_CHUNKS=850
ALL_CHUNKS_MAX_WORDS_LE_450=YES
ALL_CHUNKS_SINGLE_PAGE_ONLY=YES
EMPTY_PAGES_GENERATED=26
EMPTY_PAGES_GENERATED_CHUNKS=0
EMPTY_CHUNKS=0
ZERO_CHUNK_DOCUMENTS=0
NONEMPTY_PAGES_WITH_CHUNKS=638
CROSS_PAGE_CHUNKS=0
DETERMINISM_2_RUNS=PASS
EMBEDDINGS_CREATED=NO
TASKS_CREATED=0
CORPUS_FROZEN=NO
BENCHMARK_STARTED=NO
RAW_PDF_HASHES_UNCHANGED=YES
QUALITY_RECORDS_UNCHANGED=YES
CHUNKING_CONFIG_UNCHANGED=YES
BENCHMARK_SCOPE_UNCHANGED=YES
TESTS_PASSED=19/19
TESTS_FAILED=0
SOURCE_CODE_MODIFIED=NO
COMMIT=NO
PUSH=NO
```

## Explicit statement

This phase performed deterministic page and chunk materialization for
USE_CASE=UC3 under the pre-specified working chunking configuration
(`page_aware_word_windows`, max_words=450, overlap_words=75,
cross_page_boundaries=false, empty_pages_generate_chunks=false), using the
existing, unmodified entry points
(`python -m responsible_agentic_workflows.corpus.process --use-case UC3`
and `python -m responsible_agentic_workflows.corpus.chunks --use-case
UC3`). No embeddings, no tasks, no retrieval, no answer generation, no
benchmark execution, and no corpus freeze occurred in this phase.
