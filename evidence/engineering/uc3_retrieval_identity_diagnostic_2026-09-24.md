# UC3 Retrieval Identity Diagnostic Evidence

- **Phase:** 4B3-ID (frozen identity diagnostic execution)
- **Status:** EXECUTED
- **Date (UTC):** 2026-09-24
- **Interpretation type:** Descriptive engineering evidence only — **not** an embedding-model acceptance test, not a benchmark task, and not a threshold derivation.
- **Raw result artifact:** `evidence/engineering/uc3_retrieval_identity_diagnostic_result_2026-09-24.json` (SHA-256 `ff34bb0220a10c423e99e96c2ff3ed0d4a40aaf5ab85261969964b5dd86c6379`)
- **Corresponding protocol:** `evidence/engineering/uc3_retrieval_identity_probe_protocol_v0.1.json` (frozen, `status=frozen_before_execution`)
- **Semantic probe protocol (separate, untouched):** `evidence/engineering/uc3_retrieval_semantic_probe_protocol_v0.1.json`

## Scope and interpretation boundary

This identity diagnostic answers **retrieval-identity** questions for the UC3 working corpus (9 accepted documents / 850 chunks; `controls.corpus_frozen=false`) and the exact cosine retriever, using the frozen 9 identity probes. It is **descriptive**: it reports where the expected document lands and whether top-level retrieval is stable across repeated query runs.

This is explicitly **not**:

- An embedding-model acceptance test.
- A definition of acceptance thresholds (none are introduced here).
- A benchmark task or dataset.
- A freeze of `top_k`, `batch_size`, `retrieval_config_id`, or retrieval settings.
- A decision that the corpus, chunking config, or semantic diagnostic scope are complete.

The frozen semantic diagnostic is the pre-specified engineering retrieval-configuration acceptance gate. It is not a benchmark result. It is a later phase and is not this identity diagnostic.

## Execution environment

- **UC3 working corpus state:** 9 accepted documents / 850 chunks; `controls.corpus_frozen=false` (`benchmark_scope.json`).
- **UC3 retrieval configuration:** `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1` (status=working; it has not yet undergone the later corpus/retrieval freeze).
  - Backend: `dense_exact_cosine`; top_k=10 (from the frozen diagnostic protocol only, not from the retrieval config); ranking unit = chunk
  - Embedding: `qwen3-embedding:4b-q4_K_M` (Ollama 0.34.0), dim 2560, truncation off, asymmetric (query instruction applied only at query time)
  - `retrieval_config_id`: `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1`

## Embedding and query execution

- The canonical Run-1 corpus embedding matrix (`embeddings.npy`, 850 × 2560 float32) was **reused unchanged**; corpus embeddings were **not rematerialized**.
- Each query was **embedded freshly** for each `retrieve()` call. Query vectors were not persisted or reused across repeats.
- The retrieval implementation reuses the canonical corpus matrix: `DenseExactRetriever` (exact cosine over a normalized float32 matrix).
- **top_k=10** belongs to the frozen identity diagnostic protocol only. **Benchmark top_k remains unfrozen.**
- Model/provider: `qwen3-embedding:4b-q4_K_M` @ Ollama 0.34.0 (local).

## Pre-execution immutable SHAs (Step 1 guard — all satisfied)

| Artifact | SHA-256 |
| --- | --- |
| Identity protocol | `6221b933ae21058bee73b1eb7dbd0c6169a6f16a6457ac5c348c8672276da9fd` |
| Semantic probe protocol (untouched) | `ca8a0979edb090ebc63b7d702f4edb2003ca83b21dbea344dfff81ebe34721c4` |
| Retrieval config | `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` |
| benchmark_scope.json | `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` |
| chunk_ids.json | `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62` |
| embeddings.npy | `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450` |
| metadata.json | `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866` |

## Execution parameters (from frozen identity diagnostic protocol)

- `top_k` = 10 (frozen diagnostic protocol only; benchmark top_k remains unfrozen)
- `repeats_per_probe` = 3
- `rank_unit` = chunk
- `expected_document_measure` = rank of the first retrieved chunk belonging to the expected document
- Probes executed: 9; total `retrieve()` query runs: 27

## Aggregate diagnostics

Counts are over the 9 identity probes. "Rank-1 / Top-3 / Top-10" is the expected document's position in **every** of the 3 repeats for that probe. Stability is whether the top-level retrieved identifiers were identical across the 3 repeats.

| Diagnostic | Count | Interpretation |
| --- | --- | --- |
| EXPECT_DOCUMENT_RANK1_PROBES | 7/9 | 7 probes place the expected document at rank 1 in all 3 repeats. (ID02 → rank 2 in all repeats; ID04 → rank 4 in all repeats.) |
| EXPECT_DOCUMENT_TOP3_PROBES | 8/9 | 8 probes place the expected document within the top 3 in all 3 repeats. (ID04 → rank 4 in all repeats.) |
| EXPECT_DOCUMENT_TOP10_PROBES | 9/9 | All 9 probes place the expected document within the top 10 in every repeat. |
| STABLE_TOP1_DOCUMENT_PROBES | 9/9 | All 9 probes return the same top-1 document in all 3 repeats. |
| STABLE_TOP1_CHUNK_PROBES | 8/9 | 8 probes return the same top-1 chunk in all 3 repeats. (ID01 varies.) |
| EXACT_TOP10_ORDER_STABLE_PROBES | 4/9 | 4 probes return an identical fully-ordered top-10 chunk list in all 3 repeats. |
| VARIATION_PROBES | 5 | ID01, ID05, ID06, ID08, ID09 exhibit at least one unstable attribute (top-1 chunk and/or exact top-10 order). |

## Per-probe observations

| Probe | Expected doc | Top-1 doc (all 3 repeats) | First rank (all 3 repeats) | Top-10 order stable | Variation? |
| --- | --- | --- | --- | --- | --- |
| ID01 | DOC032 | DOC032 | 1 | No | **Yes** (top-1 chunk varies) |
| ID02 | DOC033 | DOC034 | 2 | Yes | No |
| ID03 | DOC034 | DOC034 | 1 | Yes | No |
| ID04 | DOC035 | DOC034 | 4 | Yes | No |
| ID05 | DOC036 | DOC036 | 1 | No | **Yes** (top-10 order varies) |
| ID06 | DOC037 | DOC037 | 1 | No | **Yes** (top-10 order varies) |
| ID07 | DOC038 | DOC038 | 1 | Yes | No |
| ID08 | DOC039 | DOC039 | 1 | No | **Yes** (top-10 order varies) |
| ID09 | DOC040 | DOC040 | 1 | No | **Yes** (top-10 order varies) |

### Variation probe observations

**ID01 (expected DOC032):**
ID01 returned DOC032 as the top-1 document in all three repeats.
The top-1 chunk differed: repeat 1 returned DOC032-P0053-C001,
while repeats 2 and 3 returned DOC032-P0009-C001.

**ID05 (DOC036), ID06 (DOC037), ID08 (DOC039), ID09 (DOC040):**
For ID05, ID06, ID08 and ID09, the top-1 document and top-1 chunk
were stable across repeats, while the exact ordering of the complete
Top-10 chunk list varied.

### Cross-repeat variation and causal limitation

Cross-repeat ranking variation was observed while the canonical corpus
embedding matrix, retrieval configuration, frozen protocols, and retrieval
implementation remained unchanged. Query embeddings were recomputed for
each retrieve() call. This diagnostic did not persist the query vectors or
perform a controlled cold-versus-warm runtime experiment, so it does not
independently isolate the causal source of the observed variation.

The exact cosine ranking computation is deterministic conditional on
fixed input vectors and fixed implementation state; however, that fact
alone does not establish which upstream runtime mechanism produced the
observed cross-repeat differences.

## Findings

1. Expected document Top-10 coverage = **9/9** across all 3 repeats.
2. Stable Top-1 document = **9/9** (same top-1 document in all 3 repeats).
3. Expected document Rank-1 in all repeats = **7/9** (ID02 stable at rank 2; ID04 stable at rank 4).
4. ID02 expected-document ranks = [2, 2, 2]; ID04 expected-document ranks = [4, 4, 4].
5. Stable Top-1 chunk = **8/9** (ID01 top-1 chunk varies across repeats).
6. Exact Top-10 chunk order stable across repeats = **4/9**.
7. Cross-repeat variation exists at the chunk and/or order level (5 of 9 probes).
8. **Cause of that variation was NOT isolated by this diagnostic.**
9. No acceptance or rejection decision is made by the identity diagnostic.
10. The frozen semantic diagnostic is the pre-specified engineering retrieval-configuration acceptance gate. It is not a benchmark result.

## Immutable artifact preservation (verified post-run)

- Identity protocol SHA unchanged: `6221b933ae21058bee73b1eb7dbd0c6169a6f16a6457ac5c348c8672276da9fd`
- Semantic probe protocol SHA unchanged: `ca8a0979edb090ebc63b7d702f4edb2003ca83b21dbea344dfff81ebe34721c4`
- Retrieval config SHA unchanged: `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` (status=working)
- benchmark_scope.json SHA unchanged: `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` (corpus_frozen=false)
- Run-1 artifacts (chunk_ids.json, embeddings.npy, metadata.json) unchanged
- No corpus, chunking, embedding, or retrieval settings were modified
- No commit, push, or new source/test artifact added

## Next step (for reference — not started)

The frozen semantic diagnostic is the pre-specified engineering retrieval-configuration acceptance gate. It is not a benchmark result. It is a separate later phase, not substituted by this identity diagnostic.
