# UC3 Retrieval Foundation Freeze

Date: 2026-09-24

## Purpose

This record defines the pre-benchmark freeze boundary for the UC3 retrieval
foundation.

The freeze was performed only after corpus intake, provenance validation,
formal eligibility adjudication, chunking, embedding materialization, artifact
verification, and pre-specified identity and semantic retrieval diagnostics had
completed.

The freeze establishes cryptographic identity (provenance-verified SHA256
rebinding of the frozen configuration), not byte-reproducible rematerialization.

## Frozen methodological scope

The following UC3 components are frozen:

- corpus scope: 9 accepted retrieval-active documents
  (`DOC032` through `DOC040`);
- chunking configuration: `UC3-PAGE-W450-O75-v0.1`
  (inherited from UC1: W450-O75, page-aware, no cross-page boundaries);
- chunk count: 850 chunks;
- embedding model: `qwen3-embedding:4b-q4_K_M`;
- embedding model digest: `df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907`;
- embedding output dimensions: 2560;
- retrieval backend: exact cosine over the materialized NumPy embeddings;
- retrieval configuration:
  `UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1`.

Benchmark-owned settings such as `top_k` are not defined by this detailed
retrieval configuration and are not frozen by this record.

## Configuration transition

| Artifact | Before SHA256 | Frozen SHA256 |
| --- | --- | --- |
| UC3 benchmark scope | `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` | `751eea55b97e188ab633aae34ed7935336c91cee8817f6055a249789b53b5cde` |
| UC3 chunking config | `cca30db2427243711cb9ce3ae6cbb78cd204479a60d209b4452fe15df7b4c188` | `5937238395de208321edb1a698fc5fcea704b0b7a572214c88b9a39971adab90` |
| UC3 retrieval config | `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef` | `cbc006fbab5623af240613e4348bccd17107943e0556a5746409130cd073bac1` |
| UC3 embedding metadata | `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866` | `6b80cd3d7910cd1a635a65b3df392af960ab6b2fda3ddf1e246792309b0dd64b` |

The tracked status transitions were:

- corpus scope: `working` to `frozen`;
- corpus frozen flag: `false` to `true`;
- chunking status: `working` to `frozen`;
- chunking frozen marker: ABSENT to true (the documentary frozen marker was
  added at freeze time to match the established UC1 frozen chunking pattern,
  which carries both `status: frozen` and `frozen: true`);
- retrieval configuration status: `working` to `frozen`;
- embedding metadata status: `working` to `frozen`;
- embedding metadata `retrieval_config_sha256` rebound to the frozen
  retrieval configuration.

`PRE_FREEZE_STALE_STATE_TEXT_CORRECTION=YES`: four stale state-text fields in
the benchmark scope (`benchmark_scope_rule` and notes[0], notes[1], notes[3])
were brought to consistent frozen state as part of the scope transition; the
factual note (notes[2]) and all membership and `source_groups` fields were left
unchanged.

## Provenance wording correction (POST-4B4)

The pre-frozen benchmark scope note (notes[0]) described the nine documents as
"a supervisor-provided, independently verified authoritative public set." The
pre-retrieval records do not support the "supervisor-provided" attribution:
`source_selection.tsv` lists all nine documents with public source URLs (EC JRC,
CoE, EU EUR-Lex, UNESCO), and `eligibility_review.tsv` records every document's
runtime-independence basis (criterion G) as an "independently public" source —
no record states that the documents were "supervisor-provided."

`SUPERVISOR_PROVIDED_WORDING_SUPPORTED=NO`

Only notes[0] was corrected to be faithful to the corroborating records; all
membership, `source_groups`, `controls`, and `benchmark_scope_rule` fields were
left unchanged. The correction produced a new benchmark-scope SHA256:

- before: `751eea55b97e188ab633aae34ed7935336c91cee8817f6055a249789b53b5cde`
- after: `25d71d5dda11ec20000e0b4038329ad0886f18401d2d3d5323223aa014ae14ea`

`POST_FREEZE_PROVENANCE_WORDING_CORRECTION=YES`

## Chunking frozen-marker provenance

The documentary chunking frozen marker was not a tracked `false` -> `true`
transition; the `"frozen": true` key was ABSENT before freeze and added at freeze
time to match the established UC1 frozen chunking pattern (which carries both
`status: frozen` and `frozen: true`).

- `UC3_CHUNKING_FROZEN_MARKER_PRE_FREEZE=ABSENT`
- `UC3_CHUNKING_FROZEN_MARKER_POST_FREEZE=true`

## Preserved source and embedding artifacts

The local processed chunk index was not modified:

- before: `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e`
- after: `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e`

The embedding matrix was not modified:

- before: `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450`
- after: `7c7cdbd63f3fd1d2fded22b35407309d7ad41b0b41b8a0a2ce198f6b385e2450`

The chunk-ID artifact was not modified:

- before: `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62`
- after: `7ee115260ad10f5fb89a42e34262261197dfe9b31229e7b3e532a1e28a186a62`

Canonical aggregate source chunk artifact SHA256:

`ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563`

No re-chunking and no re-embedding occurred.

## Local embedding metadata

The ignored local embedding metadata was transitioned from `working` to
`frozen` and rebound to the frozen retrieval configuration SHA256.

- metadata SHA256 before: `12129813eef60501ced56cbc17e4108090fccbb0388d95279fdeccfe0c708866`
- metadata SHA256 after: `6b80cd3d7910cd1a635a65b3df392af960ab6b2fda3ddf1e246792309b0dd64b`
- frozen retrieval config SHA256: `cbc006fbab5623af240613e4348bccd17107943e0556a5746409130cd073bac1`

The provenance-verified loader passed after the transition: 850 chunks,
embedding matrix shape (850, 2560), frozen status, and SHA256 binding re-verified
against the frozen retrieval configuration.

Non-retrieval structural tests passed: `tests/test_retrieval_configuration.py`
(6 tests) and `tests/test_embedding_artifact_loading.py` (6 tests) — 12 passed.

## Research controls

- No benchmark question was used to select the corpus.
- No benchmark result was used to select the chunking configuration.
- The chunking configuration was inherited from UC1 (W450-O75) as a fixed
  technical reference; no UC3-specific benchmark observation was used to tune
  `max_words`, `overlap_words`, or cross-page behavior.
- No benchmark gold evidence was used for embedding-model selection.
- No benchmark run occurred before this freeze.
- The embedding matrix and chunk IDs remained byte-identical.
- No second embedding model is required by the research design.

## Status

- `UC3_CORPUS_FREEZE=YES`
- `UC3_CHUNKING_FREEZE=YES`
- `UC3_RETRIEVAL_FREEZE=YES`
- `EMBEDDING_ARTIFACT_FREEZE=YES`
- `REEMBEDDING_PERFORMED=NO`
- `BENCHMARK_RUN_BEFORE_FREEZE=NO`
- `PRE_FREEZE_STALE_STATE_TEXT_CORRECTION=YES`

## Post-freeze serialization normalization

A final static-file quality audit found that `benchmark_scope.json` lacked a
terminal newline. One LF byte was appended after Phase 4B4. Parsed JSON content
was verified identical before and after this serialization-only normalization.

- scope SHA256 before: `25d71d5dda11ec20000e0b4038329ad0886f18401d2d3d5323223aa014ae14ea`
- scope SHA256 after: `2ea34f7a75def7a9a0c65671a54b0aa131c588acbab89d6ab92788b7e956542e`
- `SCOPE_JSON_CONTENT_UNCHANGED=YES`
- `CORPUS_MEMBERSHIP_CHANGED=NO`
- `FREEZE_STATE_CHANGED=NO`
- `SCIENTIFIC_CONFIGURATION_CHANGED=NO`

## Post-freeze manifest synchronization

A final independent audit found that `corpus/manifest.json` retained
pre-freeze UC3 descriptive wording even though formal eligibility
adjudication and Phase 4B4 retrieval-foundation freeze had completed.

Only documentary/provenance fields were synchronized:

- the UC3 use-case note was updated from pre-adjudication/pre-freeze wording
  to the established post-4B4 state;
- DOC032-DOC040 `discovered_via` wording was changed from the unsupported
  "Supervisor-provided UC3 source selection" attribution to the neutral
  "UC3 curation/source-identification process";
- the file's missing final newline was normalized.

No document ID, membership, accepted/excluded status, source organization,
source reference, source URL, source-file SHA256, rights note, frozen
retrieval configuration, chunking configuration, embedding artifact,
diagnostic protocol, diagnostic result, or benchmark state changed.

- manifest SHA256 before: `0bb07d29f6beecc5fa72c50bebd36078b732461bfc3abcb4d432583a20f7c958`
- manifest SHA256 after: `9858ca4f656078add7e876d831a3551438672e1e978c218c8fe08522311133a1`
- `MANIFEST_DOCUMENT_MEMBERSHIP_CHANGED=NO`
- `MANIFEST_DOCUMENT_ACCEPTANCE_CHANGED=NO`
- `SCIENTIFIC_CONFIGURATION_CHANGED=NO`
- `BENCHMARK_STARTED=NO`
