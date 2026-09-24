# UC3 Dense Embedding Materialization Evidence — Run-1 + Run-2

- Date: 2026-09-24
- Phase: 4B3 — UC3 embeddings + structural validation + two-run determinism
- Run: 1 of 2 (primary materialization) + Run 2 (determinism verification)
- Environment: local Ollama only; no cloud API
- 4B3 verdict (not an unconditional PASS):
  - `EMBEDDING_MATERIALIZATION=PASS`
  - `STRUCTURAL_VALIDATION=PASS`
  - `VECTOR_PAYLOAD_DETERMINISM=FAIL`
  - `BYTE_LEVEL_DETERMINISM=FAIL`
  - `EMBEDDING_FILE_HASH_EQUALITY=1/3`
  - `FREEZE_READINESS=NOT_YET_ESTABLISHED`

## Status and scope

UC3 embedding materialization and structural validation completed. This is an
engineering corpus-construction action. It is not benchmark result construction,
scientific evaluation, `top_k` tuning, or benchmark-result finalization. No
benchmark result or scientific state was created or modified. The Run-2
determinism check **FAILED** (vector payload and byte level), so 4B3 is not an
unconditional pass: materialization and structural validation succeeded,
determinism did not. The two-run materialization check established that the
current local embedding stack is not byte-reproducible across independent
materializations. This is retained as a reproducibility observation and is not,
by itself, a freeze blocker. Freeze readiness is not yet established because
the UC3 retrieval configuration has not yet undergone the prospectively
frozen semantic retrieval qualification gate (with the identity diagnostic
executed separately as descriptive engineering evidence), as was done before
the UC1 retrieval foundation freeze. `FREEZE_READINESS=NOT_YET_ESTABLISHED`.

## Local embedding provider verification (pre-run)

- Ollama server: `v0.34.0` at `http://localhost:11434`
- Model name: `qwen3-embedding:4b-q4_K_M`
- Ollama model ID (digest): `df5bd2e3c74c`
- Full model digest (metadata): `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- Digest `df5bd2e3c74c` matches the config and metadata `embedding_model_digest`.
- Provider version `0.34.0` is recorded in metadata.

## Frozen source state (pre-run integrity)

- Branch: `research/uc3-dc4democracy-corpus-intake`
- HEAD at start: `d9117e441d57f44a6ec8317a0019bf8af2bdcd21`
- 9 documents accepted; all 9 statuses `working`; `DOC041–DOC056` absent.
- Frozen artifact hashes re-verified pre-run:
  - Manifest `0bb07d29f6beecc5fa72c50bebd36078b732461bfc3abcb4d432583a20f7c958`
  - Benchmark scope `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb`
  - Eligibility criteria `08a569aa3988fc17199c890abbb83766c2614018e1ec51111a3d169d1ea53213`
  - Chunking config `cca30db2427243711cb9ce3ae6cbb78cd204479a60d209b4452fe15df7b4c188`
  - Retrieval config `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef`
  - Adjudication evidence `a4ea3409f04ce600eab6fbcb4c881a2a3a14d9449111e1e596fb2558db1a7c5d`
- Pre-run `corpus/use_cases/UC3/processed/embeddings/` did not exist.

## Source chunk input

- Chunk directory: `corpus/use_cases/UC3/processed/chunks` (9 artifacts + manifest)
- Chunk count: 850 (850 unique chunk IDs; 0 empty; 9 distinct `document_id`s)
- Per-document chunk counts:
  - `DOC032` 177, `DOC033` 111, `DOC034` 63, `DOC035` 178, `DOC036` 24,
    `DOC037` 88, `DOC038` 11, `DOC039` 95, `DOC040` 103
- Source chunk index SHA-256: `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e`
- Source chunk artifacts SHA-256: `ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563`
- Source chunk artifact count: 9

## Run configuration (production single pass)

- Script: `materialize_embedding_artifacts()` from
  `responsible_agentic_workflows.retrieval.materialize`, invoked via a throwaway
  driver at `/tmp/opencode/materialize_uc3.py` (no change to `src/` or `tests/`).
- Batch count: `ceil(850 / 32) = 27` batches (batch size 32 — UC1 parity).
- Model: `qwen3-embedding:4b-q4_K_M`
- Dimensions: `2560`
- `query_instruction`: `"Given a policy question, retrieve relevant passages
  that answer the question"` (per UC3 retrieval config)
- `truncate`: `false`
- Backend: `numpy` `2.5.3`; index type: `flat-exact`
- Distance: `cosine` (exact)
- Query embedding for the retrievability smoke test only; no `top_k` selected as
  a benchmark outcome.
- Execution time: ~77 seconds (materialize) + ~4 seconds (retrievability smoke).
- Exit code: 0.

## Output artifacts

Directory: `corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/`

- `embeddings.npy`: 8,704,128 bytes (128-byte NumPy header + 8,704,000-byte payload)
- `chunk_ids.json`: 21,437 bytes
- `metadata.json`: 1,056 bytes

## Metadata (final artifact hash)

- `metadata.json` SHA-256: `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866`
- `embeddings.npy` SHA-256: `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450`
- `chunk_ids.json` SHA-256: `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62`

Metadata fields:

- `schema_version` `0.1`
- `artifact_type` `dense_embedding_index`
- `status` `working` (pre-frozen)
- `retrieval_config_id` `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1`
- `chunking_config_id` `UC3-PAGE-W450-O75-v0.1`
- `chunk_count` `850`
- `dimensions` `2560`
- `dtype` `float32`
- `batch_size` `32`
- `embedding_model` `qwen3-embedding:4b-q4_K_M`
- `embedding_model_digest` `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`
- `embedding_provider` `ollama`
- `embedding_provider_version` `0.34.0`
- `truncate` `false`
- `source_chunk_index_sha256` `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e`
- `source_chunk_artifacts_sha256` `ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563`
- `source_chunk_artifact_count` `9`
- `retrieval_config_sha256` `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef`
- `embeddings_sha256` `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450`
- `chunk_ids_sha256` `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62`

## 8/9 validation points (Run-1)

1. All 850 expected chunk IDs present: PASS (850 unique loaded; 850 unique chunk IDs in `chunk_ids.json`)
2. 2560 dimensions, `float32`: PASS (matrix shape `(850, 2560)`, dtype `float32`)
3. Exact `sha256` values present: PASS (3 artifact SHAs + 3 source/config SHAs above)
4. Batch count `27`, batch size `32`, provider `ollama`, model `qwen3-embedding:4b-q4_K_M`, version `0.34.0`, digest `df5bd2e3…ff907`: PASS
5. `query_instruction` present per retrieval config, `truncate=false`, `index_type=flat-exact`, `distance=cosine`, `dtype=float32`, backend `numpy 2.5.3`: PASS
6. No non-finite values / empty chunks / missing pages: PASS (`load_embedding_artifacts` validates `isfinite`, non-zero norms; `DenseExactRetriever` re-validates; all `chunk.text` non-empty)
7. `chunk_ids` JSON matches ordered chunk list, no duplicates, non-empty text: PASS
8. Frozen scientific state untouched (eligibility, adjudication, manifest, benchmark scope, chunks, quality, retrieval config, benchmarks, tasks, results, work log): PASS (all frozen SHAs re-verified; no `src/` or `tests/` modification; no benchmark result or task created)
9. Retrievability smoke test (exact cosine against UC3 corpus): PASS — top-5 scores in `[-1, 1]`, monotonically non-increasing, no exceptions, ~4 s. (Structural smoke only; not a benchmark outcome.)

## Run-2 determinism verification

After Run-1 completed and its canonical artifacts were snapshotted to
`/tmp/opencode/uc3_run1/`, a byte-identical Run-2 was executed against the
same Ollama server, the same model (`qwen3-embedding:4b-q4_K_M`, digest
`df5bd2e3…ff907`), the same retrieval config
(`33537bd0…c4ce93`), and the same 850 source chunks
(`a89d618882…d5063`). Run-2 was written to a separate output directory
(`/tmp/opencode/uc3_run2`) so the canonical Run-1 artifacts were not
overwritten. Only the output path differed.

### Inputs re-verified pre-Run-2

- Ollama version `v0.34.0` (unchanged from Run-1)
- Model digest `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907` (unchanged)
- Retrieval config SHA-256 `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` (unchanged)
- Chunk index SHA-256 `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e` (unchanged)
- Chunk artifacts SHA-256 `ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563` (unchanged)

### Run-2 result

- Elapsed: 79.84 s (materialize-only; no retrievability smoke on Run-2)
- Exit code: 0
- `metadata.json` `chunk_count`: 850, `dimensions`: 2560, `embeddings_sha256`: `4367b0fa3ce710e65d1aa1c27ff389950d3bcaa4f88312ab34dcd0cdab744d25`, `chunk_ids_sha256`: `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62`
- `metadata.json` differs from Run-1 solely in the `embeddings_sha256` field
  (Run-1 `7c7cdbd6…e2450` vs Run-2 `4367b0fa…b744d25`), which is a direct
  consequence of the model producing different floats for the same inputs.
  All other metadata fields are byte-identical across runs.

### Per-file SHA-256 comparison

| Artifact        | Run-1 SHA-256                                              | Run-2 SHA-256                                              | Match |
| --------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ----- |
| `embeddings.npy` | `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450` | `4367b0fa3ce710e65d1aa1c27ff389950d3bcaa4f88312ab34dcd0cdab744d25` | **NO** |
| `chunk_ids.json` | `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62` | `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62` | **YES** |
| `metadata.json`  | `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866` | `9e9d6f3c7a4203880f3af76ff0def61feff047d3d91ef13eec53136ba4cece93`  | **NO** |

`EMBEDDING_FILE_HASH_EQUALITY=1/3`

### Vector payload element-wise comparison

Both runs produced a `(850, 2560)` matrix of dtype `float32`. The shape and
dtype are identical; the values are not.

- `identical_elements = False`
- `any_nan = R1:False R2:False` (both finite)
- `max_abs_diff = 0.00981585681438446`
- `max_rel_diff = 7807.90576171875` (driven by small-magnitude elements near zero)
- `mismatched = 381439 / 2176000` (`17.5294%` of all vector elements differ)
- Mismatched elements span the full document range (row 2 through row 825+ observed); the drift is not confined to a single document or a single row.
- Example (row 2, first 8 elements):
  - R1: `[-5.537681499845348e-05, 0.01962575502693653, -0.059690386056900024, 0.012446235865354538, -0.0002874882484320551, 0.026109794154763222, 0.053891196846961975, -0.05882498621940613]`
  - R2: `[-6.0425336414482445e-05, 0.019015690311789513, -0.06289699673652649, 0.011578814126551151, -0.00031870536622591317, 0.027225947007536888, 0.0534798800945282, -0.05903922766447067]`

### Determinism verdict (6-line report)

```
EMBEDDING_MATERIALIZATION=PASS
STRUCTURAL_VALIDATION=PASS
VECTOR_PAYLOAD_DETERMINISM=FAIL
BYTE_LEVEL_DETERMINISM=FAIL
EMBEDDING_FILE_HASH_EQUALITY=1/3
FREEZE_READINESS=NOT_YET_ESTABLISHED
```

#### Artifact set aggregate

The aggregate is defined as: for each of the three canonical artifacts,
emit `relative_path<TAB>sha256<NEWLINE>`, sort lexicographically (chunk_ids.json,
embeddings.npy, metadata.json), then SHA-256 the complete canonical text blob.
This is a property of the *ordered set* of artifacts, not of any single file.

```
RUN1_ARTIFACT_SET_AGGREGATE_SHA256=a7daf6600b289ba49e332def753edbd5703423366c14eb8396c73d9913058487
RUN2_ARTIFACT_SET_AGGREGATE_SHA256=32655ab0416119c4377f722143c14b2b4261559195e13110a755a9a3892b504e
```

#### Per-file artifact SHAs (separate from the aggregate)

The `embeddings.npy` per-file SHA-256 is **not** an aggregate; it is reported
separately so that no per-file SHA is mislabelled as an aggregate:

```
RUN1_EMBEDDINGS_NPY_SHA256=7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450
RUN2_EMBEDDINGS_NPY_SHA256=4367b0fa3ce710e65d1aa1c27ff389950d3bcaa4f88312ab34dcd0cdab744d25
```

> Correction to prior report: the earlier "RUN1/2_EMBEDDING_AGGREGATE_SHA256"
> lines referred to the per-file `embeddings.npy` SHA-256, not a set
> aggregate. The true artifact-set aggregates are the values above, and the
> per-file SHA is now reported under its correct name.

### Conservative causal note

The two materializations used identical inputs, identical `materialize.py`
code, identical Ollama provider version, identical model digest, identical
batching (32), and identical configuration. The only difference was the
output path. The non-determinism was observed under the current local
Ollama/model/runtime stack. The current checks found no changes in the source
chunks, retrieval configuration, model identity, batching, or materialization
implementation between the two runs. These observations localize the variation
to the embedding inference/runtime path but do not independently isolate a
single causal mechanism. It is noted for context (max ~9.8e-3) and is not
limited to low-bit rounding (17.5% of elements differ by more than the
`float32` epsilon); the pattern spans all documents. This does not invalidate
the Run-1 artifact as a working engineering state; it does invalidate any
claim that a second materialization will byte-reproduce Run-1. This is
retained as a reproducibility observation and is not, by itself, a freeze
blocker. Freeze readiness is not yet established because the UC3 retrieval
configuration has not yet undergone the prospectively frozen semantic
retrieval qualification gate, with the identity diagnostic executed separately
as descriptive engineering evidence, as was done before the UC1 retrieval
foundation freeze. `FREEZE_READINESS=NOT_YET_ESTABLISHED`.

### Run-2 cleanup

The Run-2 output directory (`/tmp/opencode/uc3_run2`) and the two
comparison driver scripts (`/tmp/opencode/materialize_uc3_run2.py`,
`/tmp/opencode/uc3_determinism_compare.py`) are left on disk at the paths
above, because the sandbox disallows `rm -rf`. They contain no production
state, no source modifications, and no test modifications, and they are
not referenced by any canonical artifact. The canonical Run-1 artifacts in
`corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/`
were not modified in any way and continue to be the authoritative embedding
artifacts for UC3. The Run-1 snapshot at `/tmp/opencode/uc3_run1/` is
retained as the comparison reference.

## Existing test-suite result (no test modification)

After the Run-2 determinism work, the seven existing test files that cover
embedding client, embedding artifact loading, embedding materialization,
dense retrieval, retrieval, retrieval configuration, and chunk
materialization were run against the project venv with no test file
modified.

- Command: `.venv/bin/python -B -m pytest
  tests/test_embedding_materialization.py tests/test_embedding_client.py
  tests/test_embedding_artifact_loading.py tests/test_dense_retrieval.py
  tests/test_retrieval.py tests/test_retrieval_configuration.py
  tests/test_chunk_materialization.py -p no:cacheprovider`
- Result: `38 passed in 0.18s`
- Exit code: 0
- No test file was added, modified, or skipped.
- No `--deselect`, no `xfail`, no local override was applied.

## Retrieval smoke test — engineering-only protocol deviation

The retrievability smoke test in the Run-1 evidence (point 9) used
`top_k=5` against a small hand-picked probe query. That choice of `top_k`
was an engineering protocol deviation: the retrieval configuration's
intended production `top_k` was not selected by a benchmark run, and the
smoke test's `top_k` does not derive from any benchmark task, task
evidence, or scientific justification. The smoke test is structural only:
it verifies the exact-cosine path executes end-to-end against the
materialized artifact, the returned scores are finite and in `[-1, 1]`, and
they are monotonically non-increasing. It is explicitly not a `top_k`
tuning result, not a benchmark task, not a retrieval-evaluation result, and
not a justification for any subsequent retrieval-freeze step. Any later
choice of a production `top_k` must be made within a benchmark task that
defines the task's own `top_k` in its own configuration file; it must not
be inferred from this smoke test.

## Provenance and constraints

- Source: local Ollama `http://localhost:11434`, model `qwen3-embedding:4b-q4_K_M`, digest `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`, version `0.34.0`.
- No cloud API, no `embeddings` API call, no network embedding provider, and no modification of `tests/` or `src/` was used.
- No benchmark result, scientific evaluation, `top_k` tuning, or benchmark-result finalization occurred.
- No commit or push was performed.

## Final state

- `EMBEDDING_MATERIALIZATION=PASS` — 850 UC3 chunks; 3 artifacts written; all 8/9 structural validation points PASS (point 9 smoke test marked separately as an engineering-only protocol deviation below).
- `STRUCTURAL_VALIDATION=PASS` — shape, dtype, finiteness, chunk-ID uniqueness, and frozen-state invariance all confirmed.
- `VECTOR_PAYLOAD_DETERMINISM=FAIL` — 17.53% of `float32` elements differ between Run-1 and Run-2; `max_abs_diff ≈ 9.8e-3`.
- `BYTE_LEVEL_DETERMINISM=FAIL` — `embeddings.npy` and `metadata.json` differ byte-for-byte; `chunk_ids.json` is byte-identical.
- `EMBEDDING_FILE_HASH_EQUALITY=1/3` — only `chunk_ids.json` matches.
- `FREEZE_READINESS=NOT_YET_ESTABLISHED` — the cross-run byte non-determinism is retained as a reproducibility observation and is not, by itself, a freeze blocker; freeze readiness is not yet established because the UC3 retrieval configuration has not yet undergone the prospectively frozen semantic retrieval qualification gate (with the identity diagnostic executed separately as descriptive engineering evidence), as was done before the UC1 retrieval foundation freeze.

**Run-1 canonical artifacts:**

```
EMBEDDING_MATERIALIZATION=PASS
STRUCTURAL_VALIDATION=PASS
VECTOR_PAYLOAD_DETERMINISM=FAIL
BYTE_LEVEL_DETERMINISM=FAIL
EMBEDDING_FILE_HASH_EQUALITY=1/3
FREEZE_READINESS=NOT_YET_ESTABLISHED

RUN1_ARTIFACT_SET_AGGREGATE_SHA256=a7daf6600b289ba49e332def753edbd5703423366c14eb8396c73d9913058487
RUN2_ARTIFACT_SET_AGGREGATE_SHA256=32655ab0416119c4377f722143c14b2b4261559195e13110a755a9a3892b504e

RUN1_EMBEDDINGS_NPY_SHA256=7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450
RUN2_EMBEDDINGS_NPY_SHA256=4367b0fa3ce710e65d1aa1c27ff389950d3bcaa4f88312ab34dcd0cdab744d25
```

- Root-cause statement uses the conservative wording from the "Conservative causal note" section above; no single causal mechanism is claimed.
- Existing test suite: 38 passed, 0 failed, 0 test files modified.
- Canonical Run-1 artifacts unchanged; Run-2 temp artifacts on disk (sandbox precludes `rm -rf`).
- Upstream SHAs re-verified post-Run-2 (manifest, scope, criteria, chunking config, retrieval config, adjudication evidence): all unchanged from pre-run values above.

## Status block

- `EMBEDDING_MATERIALIZATION=PASS`
- `STRUCTURAL_VALIDATION=PASS`
- `VECTOR_PAYLOAD_DETERMINISM=FAIL`
- `BYTE_LEVEL_DETERMINISM=FAIL`
- `EMBEDDING_FILE_HASH_EQUALITY=1/3`
- `FREEZE_READINESS=NOT_YET_ESTABLISHED`
- `RETRIEVAL_CONFIG_STATUS=working` (pre-frozen; 4B4 NOT STARTED)
- `CORPUS_FROZEN=NO`
- `UC3_TASKS_CREATED=NO`
- `RETRIEVAL_EVALUATION_RUN=NO`
- `TOP_K_FROZEN=NO`
- `BENCHMARK_STARTED=NO`
- `SOURCE_CODE_MODIFIED=NO`
- `TESTS_MODIFIED=NO`
- `COMMIT=NO`
- `PUSH=NO`
- Freeze deferred to Phase 4B4; NOT STARTED per directive.

## Files

- `evidence/engineering/uc3_embedding_materialization_2026-09-24.md` (this file)
- `corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/metadata.json`
- `corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/embeddings.npy`
- `corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/chunk_ids.json`
- `benchmark/config/retrieval/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json` (unchanged)
