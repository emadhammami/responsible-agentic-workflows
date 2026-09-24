# UC3 Eligibility Adjudication

Status: complete
Use case: UC3 — Digital Competences for Democratic Participation
Phase: 4B2E — Document-Level Eligibility Adjudication
Adjudication date: 2026-09-24
Branch: `research/uc3-dc4democracy-corpus-intake`
HEAD at precheck: `d9117e441d57f44a6ec8317a0019bf8af2bdcd21`

## Purpose

Apply the frozen UC3 eligibility rubric (criteria A–G) to the nine UC3
candidate documents (DOC032–DOC040) and record final corpus membership.
Outcomes are valid regardless of the number eligible; the outcome is
recorded, not targeted, not size-driven, and not determined by benchmark
performance.

## Inputs (frozen)

- Eligibility rubric: `corpus/use_cases/UC3/eligibility_criteria.md`
  (`08a569aa3988fc17199c890abbb83766c2614018e1ec51111a3d169d1ea53213`).
  Status `frozen`. Not modified during adjudication.
- Rubric freeze record:
  `evidence/engineering/uc3_eligibility_criteria_freeze_2026-09-24.md`
  (`69c8c519eae2873ba5d2b0966d1501d8ab0697fd3f0576174661d70c421bb08c`).
- Per-criterion evidence collected from:
  - `corpus/use_cases/UC3/source_selection.tsv`
    (`f8a254b0e9446040f2e7fefb3e726ed66a540ce1259991ab74acd0b1a2f0ba88`)
  - `corpus/use_cases/UC3/acquisition_audit.tsv`
    (`f031cb6259f8cf58270840a61da56fc3942520283f222da6e28cecd4a718e79d`)
  - `corpus/manifest.json` (per-document records, title, organization,
    reference, URL, publication year, SHA256, rights note)
  - `corpus/quality/UC3/DOC03[2-9].json` and `DOC040.json`
    (9 records, quality aggregate
    `de697f7844b74897e76ec9881ecaa300739903df8fb225cb4acf917fc633f4ec`)
  - `evidence/engineering/uc3_page_chunk_materialization_2026-09-23.md`
    (technical usability evidence)

Allowed manifest document statuses (schema
`corpus/manifest.schema.json`, line 179-186): `candidate`, `accepted`,
`excluded`.

## Decision mapping (frozen)

- ELIGIBLE → `accepted`
- INELIGIBLE → `excluded`
- NEEDS_REVIEW → `candidate`

## Precheck (Step 1)

- Branch `research/uc3-dc4democracy-corpus-intake`; HEAD
  `d9117e441d57f44a6ec8317a0019bf8af2bdcd21`.
  `git branch --show-current` = expected branch;
  `git rev-parse HEAD` = expected commit.
- Rubric SHA256 exact match against
  `08a569aa3988fc17199c890abbb83766c2614018e1ec51111a3d169d1ea53213`.
- 9 manifest records DOC032–DOC040 all `accepted` at precheck (pre-normalize);
  statuses normalized to `candidate` (Step 2) before adjudication.
- Schema allowed statuses match: `candidate`, `accepted`, `excluded`.
- Prior A–G adjudication: none. `eligibility_review.tsv` contained only the
  `REVIEW_READY` rows from intake; no document-level A–G verdict, no
  `final_decision`, no `criteria_sha256`.
- Canonical aggregate SHA256 of 20 processed artifacts unchanged from 4B2B
  (`12174dc832dae5782f050f7982ce796de0108bae33d973e5b2fbd82c76b5a30d`);
  recomputed at adjudication time and byte-identical.
- `corpus/status`: `working`; corpus not frozen.
- No embeddings, no UC3 benchmark tasks, no benchmark results, no parquet.
  `benchmark/tasks/` contains UC1-only artifacts (T001–T010, freeze_manifest,
  README.md) — no UC3 entries.

## Normalization and scope-correction steps performed

- Step 2: manifest DOC032–DOC040 status normalized from `accepted`
  (pre-adjudication provisional) to `candidate`. UC3 use-case note in
  `manifest.json` updated to read under formal eligibility adjudication.
- Step 3: `benchmark_scope.json` `benchmark_scope_rule` and `notes` corrected
  to remove the stale "satisfied the predefined UC3 inclusion criteria"
  claim; replaced with provisional/working-language wording and a note that
  `benchmark_active_document_ids` reflects the working set pending
  adjudication.
- Step 4: per-criterion evidence collected per document as listed under
  Inputs.
- Steps 5-6: rubric A–G applied per document (table below).
- Step 7: `eligibility_review.tsv` rewritten into the 14-column format
  (candidate_id, document_id, title, A_provenance_identity,
  B_stable_id, C_technical_usability, D_uc3_scope, E_evidentiary,
  F_runtime_indep, G_rights_access, final_decision, decision_reason,
  adjudication_date, criteria_sha256).
- Step 8: mapping applied: ELIGIBLE → `accepted`. `exclusion_reason`
  set/kept null. Rejected statuses: none.
- Step 9: `benchmark_active_document_ids` set to
  `DOC032..DOC040` (9 documents). NEEDS_REVIEW set: empty.
  INELIGIBLE set: empty.
- Step 10: zero non-ELIGIBLE documents; no page/chunk artifacts need
  provisional labeling. Page and chunk artifacts (20 files, 664 pages,
  850 chunks) untouched; canonical aggregate byte-identical to 4B2B.

## Adjudication table (DOC032–DOC040)

| doc | title | A | B | C | D | E | F | G | Final | Manifest |
|-----|-------|---|---|---|---|---|---|---|-------|----------|
| DOC032 | DigComp 3.0 (JRC 144121, EUR 40491, 2025) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC033 | RfCDC Vol. 1 (Council of Europe, 2018) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC034 | RfCDC Vol. 2 descriptors | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC035 | RfCDC Vol. 3 implementation | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC036 | Council Recommendation 2018/C 189/01 (OJ C 189/1) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC037 | UNESCO ICT CFT v3 (2018) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC038 | European Declaration on Digital Rights 2023/C 23/01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC039 | DigCompEdu (JRC EUR 287, 2017) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |
| DOC040 | DigCompOrg (JRC EUR 27599, 2015) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ELIGIBLE | accepted |

Aggregate: 9 ELIGIBLE, 0 NEEDS_REVIEW, 0 INELIGIBLE.

## Summary of per-criterion evidence (summary; full evidence per row is in eligibility_review.tsv)

- A: Every record carries an authoritative organization (EU Joint Research
  Centre, Council of Europe, EU Council / European Commission, UNESCO) and
  a verifiable document identity confirmed from the PDF text layer / metadata
  (e.g. `DigComp 3.0 European Competence Framework`, `REFERENCE FRAMEWORK OF
  COMPETENCES FOR DEMOCRATIC CULTURE`, `UNESCO ICT Competency Framework for
  Teachers; 2018`, OJ-stamp `2018/C 189/01`, `2023/C 23/01`). Acquisition
  notes record identity verification against the cited reference for every
  document.
- B: `manifest.json` per document carries title, source organization,
  source reference (JRC id, OJ reference, UNESCO arknoid, CoE volume),
  source URL, publication year (2015/2017/2018/2023/2025), and the SHA256 of
  the acquired file; all match `acquisition_audit.tsv` sha256 values.
- C: 9 of 9 quality records `quality_status=pass` with `issues: []`;
  extracted character counts from 26,368 (DOC038) to 561,018 (DOC032);
  languages `en`; page counts 7 to 129; text layer present; no encryption.
- D: Each document substantively addresses one or more of the UC3 named
  constructs (digital competence, democratic/civic competence, digital
  rights, educator digital competence, organizational digital competence).
- E: Each document provides primary normative or framework content sufficient
  to support grounded factual or cross-document knowledge questions (framework
  model tables, descriptor tables, OJ text, declaration items). No landing
  pages or citation-only records.
- F: Runtime use of each document does not depend on sensitive internal
  curation material; each is an independent authoritative public source.
  Sensitive internal material is excluded from the runtime corpus by
  construction.
- G: Public access is established for every document. Rights/redistribution
  notes: EU JRC/OJ publications have explicit EU reuse authorization (recorded
  in `manifest.json` `rights_note` for DOC032, DOC039, DOC040). CoE RfCDC
  volumes (DOC033, DOC034, DOC035) and the UNESCO CFT v3 (DOC037) were
  downloaded from the CoE `rm.coe.int` repository and the UNESCO `unesdoc`
  watermarked attachment respectively; specific redistribution rights are
  flagged as not explicitly licensed in records and treated as
  local-academic-use with redistribution avoided. G criteria are met under
  the "documented local academic use with redistribution avoidance where
  rights are unclear" branch of the rubric.

## Artifacts written or changed by this phase

Changed (tracked in manifest):
- `corpus/manifest.json` — DOC032–DOC040 status: `accepted` → `candidate`
  (Step 2) → `accepted` (Step 8 post-adjudication); UC3 use-case note updated
  to reflect formal adjudication state. SHA256
  `0bb07d29f6beecc5fa72c50bebd36078b732461bfc3abcb4d432583a20f7c958`.
- `corpus/use_cases/UC3/benchmark_scope.json` — `benchmark_scope_rule` and
  `notes` rewritten to remove the stale "satisfied the predefined inclusion
  criteria" claim; `benchmark_active_document_ids` set to the 9 adjudicated
  documents; `controls` unchanged. SHA256
  `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb`.

Written (new):
- `corpus/use_cases/UC3/eligibility_review.tsv` — rewritten to the
  14-column adjudication schema (previously 11-column intake-review rows
  flagged `REVIEW_READY`). SHA256
  `65c1965cf3a81813d266b7e147a64815453e99e8748ea18541d431aa7e48aada`.
- `evidence/engineering/uc3_eligibility_adjudication_2026-09-24.md` — this
  file.

Not touched (integrity verified):
- `corpus/use_cases/UC3/eligibility_criteria.md` — frozen rubric, SHA256
  `08a569aa3988fc17199c890abbb83766c2614018e1ec51111a3d169d1ea53213`.
- `corpus/use_cases/UC3/chunking_config.json` — SHA256
  `cca30db2427243711cb9ce3ae6cbb78cd204479a60d209b4452fe15df7b4c188`
  (byte-unchanged).
- `benchmark/config/retrieval/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json` —
  SHA256 `33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef`
  (byte-unchanged).
- `corpus/use_cases/UC3/source_selection.tsv`,
  `corpus/use_cases/UC3/acquisition_audit.tsv`,
  `corpus/quality/UC3/DOC0[32-4]0.json` (9 records),
  `corpus/use_cases/UC3/raw/` (9 PDFs),
  `corpus/use_cases/UC3/processed/pages/` (9),
  `corpus/use_cases/UC3/processed/chunks/` (9),
  `corpus/use_cases/UC3/processed/pages/index.json`,
  `corpus/use_cases/UC3/processed/chunks/index.json` (2 index files) —
  all 20 page/chunk artifacts byte-identical (aggregate
  `12174dc832dae5782f050f7982ce796de0108bae33d973e5b2fbd82c76b5a30d`).

Status of the corpus at end of Phase 4B2E:
- Corpus status: `working`
- Embeddings: not materialized
- UC3 benchmark tasks: not created
- Benchmark execution: not performed
- Corpus frozen: no

## Final SHA256 block (Phase 4B2E)

```
ELIGIBILITY_CRITERIA_SHA256=08a569aa3988fc17199c890abbb83766c2614018e1ec51111a3d169d1ea53213
ELIGIBILITY_CRITERIA_STATUS=frozen
ELIGIBILITY_REVIEW_TSV_SHA256=65c1965cf3a81813d266b7e147a64815453e99e8748ea18541d431aa7e48aada
QUALITY_RECORDS_AGGREGATE_SHA256=de697f7844b74897e76ec9881ecaa300739903df8fb225cb4acf917fc633f4ec
MANIFEST_SHA256=0bb07d29f6beecc5fa72c50bebd36078b732461bfc3abcb4d432583a20f7c958
BENCHMARK_SCOPE_SHA256=4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb
CHUNKING_CONFIG_SHA256=cca30db2427243711cb9ce3ae6cbb78cd204479a60d209b4452fe15df7b4c188
RETRIEVAL_CONFIG_SHA256=33537bd048416ea5ead63d8e179e815f1dc2cec290db33c3324f41fc84937eef
SOURCE_SELECTION_SHA256=f8a254b0e9446040f2e7fefb3e726ed66a540ce1259991ab74acd0b1a2f0ba88
ACQUISITION_AUDIT_SHA256=f031cb6259f8cf58270840a61da56fc3942520283f222da6e28cecd4a718e79d
CRITERIA_FREEZE_EVIDENCE_SHA256=69c8c519eae2873ba5d2b0966d1501d8ab0697fd3f0576174661d70c421bb08c
CANONICAL_PAGES_CHUNKS_SHA256=12174dc832dae5782f050f7982ce796de0108bae33d973e5b2fbd82c76b5a30d
CANONICAL_AGGREGATE_FILE_COUNT=20
CANONICAL_PAGES=664
CANONICAL_CHUNKS=850
```

## Final decision counts

```
UC3_ELIGIBILITY_ADJUDICATION=COMPLETE
ADJUDICATION_DATE=2026-09-24
DOCS_ADJUDICATED=9
ELIGIBLE=9
NEEDS_REVIEW=0
INELIGIBLE=0
MANIFEST_ACCEPTED=9
MANIFEST_EXCLUDED=0
MANIFEST_CANDIDATE=0
BENCHMARK_ACTIVE=9
EMBEDDINGS_MATERIALIZED=NO
UC3_BENCHMARK_TASKS_CREATED=NO
BENCHMARK_EXECUTED=NO
CORPUS_FROZEN=NO
CANONICAL_PAGES_CHUNKS_AGGREGATE_CHANGED=NO  (byte-identical to 4B2B)
```

## Timing / limitation statement (carried forward)

The nine UC3 candidates had already been identified and provisionally
accepted during intake before the formal eligibility rubric was written.
This project does not claim that the rubric preceded candidate identification
or provisional acceptance. The rubric was frozen (4B2D) before final corpus
inclusion, embedding materialization, retrieval evaluation, benchmark-task
construction, scientific benchmark execution, and final corpus freeze.
The formal adjudication in this phase (4B2E) is the first document-level
application of that frozen rubric. Any prior "accepted" status was
normalized to `candidate` before adjudication; the final status set is the
output of the frozen criteria, not of benchmark performance or corpus-size
pressure.
