# Retrieval reconstruction: capabilities and remaining artifacts

Source release improves independent inspection and removes the need to locate
identical downloads for the 41 included documents. The 15 supplied UC2 documents
comprise three PDFs and 12 logical HTML documents, including the nine-component
customs handbook (20 physical HTML files).
The 15 link-only originals are still required before reproducing full-UC
retrieval. The public subset must not silently replace the original membership.

## Source and construction sequence

1. Use a separate replication checkout and output directory. Retain the primary
   execution-code reference `58b9e656dd57e62a5fb8640c2d3c990e4c93e530` and launch
   revision `872f8de38c79a78e4e016cedf5597bc21323a374`. Do not edit their records.
2. Obtain all 56 authorized originals and check every component hash. Restore
   filenames under the original `corpus/use_cases/UC*/raw/` layout in the new
   checkout. Official URLs are discovery references, not guarantees of the
   original historical bytes.
3. Follow the frozen per-UC chunking/materialization configurations. UC1/UC3
   use `build_page_artifacts` in `corpus/process.py`, followed by
   `build_chunk_artifacts` in `corpus/chunks.py` under
   `src/responsible_agentic_workflows/`. These expose Python interfaces and
   module entry points. The external PDF extractor is `pdftotext`.
4. UC2 uses the already public `corpus/use_cases/UC2/materialize_uc2.py` and its
   `materialization_config.json`, `chunking_config.json`, membership and
   acquisition metadata. It validates component hashes and preserves physical
   PDF pages/individual HTML components as source units. The script exposes
   `--output`; do not point it at the original processed directory.
5. The already public `retrieval/materialize.py` supplies
   `materialize_embedding_artifacts` and `load_embedding_artifacts`, using an
   `EmbeddingClient`. `retrieval/embedding.py` supplies `OllamaEmbeddingClient`.
   These are library interfaces, not a verified one-command corpus rebuild.
6. Compare generated artifacts to recorded identities before describing them
   as matching the original retrieval system. Regenerated outputs belong to
   the new replication and must not replace frozen matrices or chunks.

## Artifacts still needed for original retrieval replay

| Artifact | Recorded identity or role | Availability |
| --- | --- | --- |
| All 56 raw sources | 30/17/9 document membership; DOC051 has nine components | 41 documents supplied; 15 official-link-only |
| Frozen processed pages/chunks and ordered chunk index | UC1 2,853 chunks; UC2 293; UC3 850 | Original local artifacts remain outside this release |
| UC1 embedding matrix | `b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0` | Not supplied |
| UC2 embedding matrix | `621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f` | Not supplied |
| UC3 embedding matrix | `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450` | Not supplied |
| Row order and metadata | Published under `../retrieval/UC*/`; float32, 2,560 dimensions | Supplied; identifiers do not contain vector values |
| Embedding model/provider | `qwen3-embedding:4b-q4_K_M`, digest `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`, recorded Ollama 0.34.0 | Model blob/provider environment not bundled |
| UC2 legacy representation | Frozen `chunks.jsonl`, source inventory, `chunk_ids.json`, matrix and metadata | `benchmark/legacy_uc2.py` validates bindings; original chunks/matrix not supplied |
| Model and execution environment | Generation identity, prompts, top-k and shared limits are already public | Weights, complete historical environment and hardware not bundled |

Dense retrieval is exact cosine using the frozen settings, rather than an
approximate vector index. Re-embedding text with the same model name alone
does not establish the same byte-level vectors or rankings. PDF extraction,
normalization, chunk ordering, model digest and numerical environment matter.
The original UC2 representation must remain compatible with its frozen loader.

Publishing the raw sources does not automatically clear reuse of all processed
text, model outputs or matrices. These need their own artifact-level decision.
No embeddings, retrieval calls, benchmark executions or judgments were
regenerated for this review. Earlier verified numerical result reconstruction
remains independent of source-document/model availability.
