# UC3 Retrieval Semantic Diagnostic Evidence

- **Phase:** 4B3-SEM (frozen semantic diagnostic execution)
- **Status:** EXECUTED
- **Date (UTC):** 2026-09-24
- **Interpretation type:** Pre-specified engineering retrieval-configuration acceptance gate. This is **not** a benchmark result.
- **Raw result artifact:** `evidence/engineering/uc3_retrieval_semantic_diagnostic_result_2026-09-24.json` (SHA-256 `0c7c2124dd37392397105133a6bc5fbf06b3e33a2f0b4f934ebebd35b53129db`)
- **Corresponding protocol:** `evidence/engineering/uc3_retrieval_semantic_probe_protocol_v0.1.json` (frozen, `status=frozen_before_execution`)
- **Identity probe protocol (separate, untouched):** `evidence/engineering/uc3_retrieval_identity_probe_protocol_v0.1.json`

## Scope and interpretation boundary

This semantic diagnostic is the **pre-specified engineering retrieval-configuration acceptance gate** for the UC3 working corpus (9 accepted documents / 850 chunks; `controls.corpus_frozen=false`) and the exact cosine retriever, using the frozen 9 semantic probes. It reports where the pre-specified expected document lands for each probe, the stability of the top-level retrieval across repeated query runs, and whether the frozen pre-specified gate thresholds are met.

The gate thresholds were **frozen before execution** (derived prospectively from the UC1 v0.1 gate via CEILING scaling to the UC3 probe count of 9) and were **not changed after observing results**.

This is explicitly **not**:

- A benchmark task or dataset; not the use of benchmark questions, gold, or answers.
- An embedding-model acceptance test for a general claim.
- A threshold derivation; the thresholds are pre-specified, not derived from these results.
- A freeze of `top_k`, `batch_size`, `retrieval_config_id`, or retrieval settings.
- A decision that the corpus, chunking config, or retrieval are complete beyond this engineering gate.

The identity diagnostic is a separate, earlier phase and is not substituted by this semantic diagnostic.

## Execution environment

- **UC3 working corpus state:** 9 accepted documents / 850 chunks; `controls.corpus_frozen=false` (`benchmark_scope.json`).
- **UC3 retrieval configuration:** `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1` (status=working).
  - Backend: `dense-exact-cosine`; top_k=10 (from the frozen semantic protocol only, not from the retrieval config); ranking unit = chunk
  - Embedding: `qwen3-embedding:4b-q4_K_M` (Ollama 0.34.0), dim 2560, truncation off, asymmetric (query instruction applied only at query time)
  - `retrieval_config_id`: `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1`
- **Retriever:** `DenseExactRetriever` (exact cosine, `src/responsible_agentic_workflows/retrieval/dense.py`).
- **Query embedder:** `OllamaEmbeddingClient` (`src/responsible_agentic_workflows/retrieval/embedding.py`).

## Embedding and query execution

- The canonical Run-1 corpus embedding matrix (`embeddings.npy`, 850 × 2560 float32) was **reused unchanged**; corpus embeddings were **not rematerialized** (`artifact_source: Run-1 materialized corpus embeddings (not rematerialized)`).
- Each query was **embedded freshly** for each `retrieve()` call. Query vectors were not persisted or reused across repeats (`query_embedding_policy: each retrieve() call freshly embeds its query; no query vector reuse across repeats`).
- **top_k=10** belongs to the frozen semantic diagnostic protocol only. **Benchmark top_k remains unfrozen.**

## Pre-execution immutable SHAs (Step 1 guard — all satisfied)

| Artifact | SHA-256 |
| --- | --- |
| Semantic probe protocol | `ca8a0979edb090ebc63b7d702f4edb2003ca83b21dbea344dfff81ebe34721c4` |
| Identity probe protocol (untouched) | `6221b933ae21058bee73b1eb7dbd0c6169a6f16a6457ac5c348c8672276da9fd` |
| Retrieval config | `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` |
| benchmark_scope.json | `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` |
| chunk_ids.json | `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62` |
| embeddings.npy | `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450` |
| metadata.json | `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866` |

## Execution parameters (from frozen semantic probe protocol)

- `top_k` = 10 (frozen diagnostic protocol only; benchmark top_k remains unfrozen)
- `repeats_per_probe` = 3
- `rank_unit` = chunk
- `expected_document_measure` = rank of the first retrieved chunk belonging to the pre-specified expected document
- Probes executed: 9; total `retrieve()` query runs: 27
- `query_style` = semantic purpose paraphrases (canonical titles, aliases, document IDs, URLs, DOIs, JRC identifiers, and legal citations prohibited in every query)

## Pre-specified engineering acceptance gate (frozen before execution)

Thresholds scaled from the UC1 v0.1 gate to the UC3 probe count of 9 using CEILING, before any UC3 diagnostic execution or result observation.

| Gate | Frozen minimum (probes) | Requirement |
| --- | --- | --- |
| SEMANTIC_GATE_TOP10 | 8 | expected document within top 10 in **each** of the 3 repeats |
| SEMANTIC_GATE_TOP5 | 7 | expected document within top 5 in **each** of the 3 repeats |
| SEMANTIC_GATE_TOP3 | 5 | expected document within top 3 in **each** of the 3 repeats |
| SEMANTIC_GATE_STABLE_TOP1_DOCUMENT | 8 | same top-1 document across all 3 repeats |

## Aggregate metrics (over 9 semantic probes)

| Metric | Count |
| --- | --- |
| EXPECTED_DOCUMENT_TOP10_ALL_REPEATS | 9/9 |
| EXPECTED_DOCUMENT_TOP5_ALL_REPEATS | 9/9 |
| EXPECTED_DOCUMENT_TOP3_ALL_REPEATS | 9/9 |
| EXPECTED_DOCUMENT_RANK1_ALL_REPEATS | 9/9 |
| STABLE_TOP1_DOCUMENT_ACROSS_REPEATS | 9/9 |
| STABLE_TOP1_CHUNK_ACROSS_REPEATS | 9/9 |
| EXACT_TOP10_CHUNK_ORDER_STABLE_ACROSS_REPEATS | 3/9 |

## Gate results

| Gate | Frozen minimum | Achieved | Gate result |
| --- | --- | --- | --- |
| SEMANTIC_GATE_TOP10 | 8 | 9/9 | **PASS** |
| SEMANTIC_GATE_TOP5 | 7 | 9/9 | **PASS** |
| SEMANTIC_GATE_TOP3 | 5 | 9/9 | **PASS** |
| SEMANTIC_GATE_STABLE_TOP1_DOCUMENT | 8 | 9/9 | **PASS** |

**SEMANTIC_RETRIEVAL_QUALIFICATION = PASS.** All four frozen gate thresholds are met (each achieved count is at or above its frozen minimum, in every repeat).

## Per-probe observations

| Probe | Expected doc | Query (paraphrase) | Top-1 doc (all 3 repeats) | First rank (all 3 repeats) | Top-1 chunk (all 3 repeats) | Top-10 order stable |
| --- | --- | --- | --- | --- | --- | --- |
| SEM01 | DOC032 | digital-competence framework, competence areas and proficiency levels | DOC032 | 1 | DOC032-P0018-C001 | No |
| SEM02 | DOC033 | values/attitudes/knowledge/skills underpinning democratic participation | DOC033 | 1 | DOC033-P0087-C001 | Yes |
| SEM03 | DOC034 | key expectations and descriptors for civic-participation competences | DOC034 | 1 | DOC034-P0013-C001 | No |
| SEM04 | DOC035 | guidance to embed, practise and assess competences across the school setting | DOC035 | 1 | DOC035-P0003-C001 | No |
| SEM05 | DOC036 | European recommendation on key competences incl. digital competence | DOC036 | 1 | DOC036-P0004-C001 | No |
| SEM06 | DOC037 | educator ICT-competence framework (content, collaboration, learner support) | DOC037 | 1 | DOC037-P0001-C001 | Yes |
| SEM07 | DOC038 | declaratory digital-rights source, six chapters / twenty-four normative items | DOC038 | 1 | DOC038-P0001-C001 | No |
| SEM08 | DOC039 | educator capabilities, 22 competences / 6 levels, per-level descriptors + rubric | DOC039 | 1 | DOC039-P0027-C001 | No |
| SEM09 | DOC040 | organisational/institutional framework, 7 elements / 15 sub-elements / 74 descriptors | DOC040 | 1 | DOC040-P0006-C002 | Yes |

Every probe places its expected document at rank 1 in **all 3 repeats** with a stable top-1 document and stable top-1 chunk. Six probes (SEM01, SEM03, SEM04, SEM05, SEM07, SEM08) show an unstable **exact** top-10 order.

### Variation probe observations

For SEM01, SEM03, SEM04, SEM05, SEM07 and SEM08, the top-1 document and top-1 chunk were stable across the 3 repeats, while the exact ordering of the ranks below top-1 within the complete top-10 chunk list differed between repeat 1 and repeats 2 and 3 (the set of returned chunks and the top-1 document/chunk are unchanged). SEM02, SEM06 and SEM09 returned an identical fully-ordered top-10 list in all 3 repeats.

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
observed cross-repeat differences. **No cause is assigned by this diagnostic.**

## Findings

1. Expected-document top-10 coverage = **9/9**; expected-document rank-1 in all repeats = **9/9**.
2. Stable top-1 document = **9/9**; stable top-1 chunk = **9/9** across the 3 repeats.
3. Exact top-10 chunk order stable across repeats = **3/9** (SEM02, SEM06, SEM09).
4. All four frozen gate thresholds are met; **SEMANTIC_RETRIEVAL_QUALIFICATION = PASS**.
5. The gate thresholds were pre-specified before execution and were not changed after observing results.
6. Cross-repeat variation exists only at the exact lower-rank order level (6 of 9 probes); the expected document is rank 1 in every repeat.
7. **Cause of that variation was NOT isolated by this diagnostic** and no causal attribution is made.
8. This is a pre-specified engineering retrieval-configuration acceptance gate; it is **not** a benchmark result.

## Immutable artifact preservation (verified post-run)

- Semantic probe protocol SHA unchanged: `ca8a0979edb090ebc63b7d702f4edb2003ca83b21dbea344dfff81ebe34721c4`
- Identity probe protocol SHA unchanged: `6221b933ae21058bee73b1eb7dbd0c6169a6f16a6457ac5c348c8672276da9fd`
- Retrieval config SHA unchanged: `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` (status=working)
- benchmark_scope.json SHA unchanged: `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` (corpus_frozen=false)
- Run-1 artifacts (chunk_ids.json, embeddings.npy, metadata.json) unchanged; corpus embeddings not rematerialized
- No corpus, chunking, embedding, or retrieval settings were modified
- No threshold, query, expected-document, or protocol content was modified
- No commit, push, or new source/test artifact added
- No phase later than 4B3-SEM was started (4B4 not started)

## Next step (for reference — not started)

Phase 4B4 (or the next authorized phase) is **not** started by this diagnostic. This gate result is an engineering retrieval-configuration qualification for the working UC3 configuration and is not a benchmark result.
