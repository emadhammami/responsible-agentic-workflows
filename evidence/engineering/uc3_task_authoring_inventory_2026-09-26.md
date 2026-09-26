# UC3 Frozen-Source Task Authoring Inventory — 2026-09-26

## Scope and repository guard

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=a24c6d6e8ceffcc149b09c148a0bf69f562eb31c
TRACKING_HEAD=a24c6d6e8ceffcc149b09c148a0bf69f562eb31c
REMOTE_BRANCH_HEAD=a24c6d6e8ceffcc149b09c148a0bf69f562eb31c
WORKTREE_CLEAN_BEFORE=YES

Source-inspection foundation only. No task questions, reference answers or task candidates are formulated. The prospective regions below are an inventory for later researcher decisions, not a task selection or an absence audit. No benchmark execution occurred.

## Frozen foundation identity

FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a
FOUNDATION_FREEZE_COMMIT_IS_ANCESTOR=YES
HISTORICAL_GLOBAL_MANIFEST_SHA256=9858ca4f656078add7e876d831a3551438672e1e978c218c8fe08522311133a1
CURRENT_GLOBAL_MANIFEST_SHA256=bd01315f1f6d035e4105ae4d89378c6df24af4d877411e9228a2fcf704368e89
HISTORICAL_UC3_DOCUMENT_RECORDS_UNCHANGED=YES
HISTORICAL_UC3_USE_CASE_RECORD_UNCHANGED=YES

The historical global manifest matches the supplied freeze hash. The current global manifest also contains subsequent UC2 intake; its different whole-file hash does not replace the historical identity. All nine UC3 document records and the UC3 use-case record are identical to the freeze commit. Tracked UC3 scope/configuration/freeze records inspected here are byte-identical to that commit. The final scope hash includes the historical provenance correction and terminal-newline normalization documented in the freeze evidence. Existing `working` labels in page/chunk indexes and the global use-case entry are preserved; frozen scope and cryptographic bindings establish the qualified foundation.

UC3_CANONICAL_CHUNKS_PATH=corpus/use_cases/UC3/processed/chunks/index.json (indexes nine DOC032–DOC040.chunks.json files)
UC3_CANONICAL_SOURCE_UNITS_PATH=corpus/use_cases/UC3/processed/pages/index.json (indexes nine DOC032–DOC040.pages.json files)
UC3_MEMBERSHIP_PATH=corpus/manifest.json (use_case_id=UC3; status=accepted)
UC3_SCOPE_PATH=corpus/use_cases/UC3/benchmark_scope.json
UC3_FREEZE_EVIDENCE_PATH=evidence/engineering/uc3_retrieval_foundation_freeze_2026-09-24.md
UC3_DOCUMENT_COUNT=9
UC3_SOURCE_UNIT_COUNT=664
UC3_CHUNK_COUNT=850
CHUNK_BEARING_SOURCE_UNIT_COUNT=638
SOURCE_UNITS_WITHOUT_CHUNKS=26
SOURCE_PAGE_WORD_COUNT=224540
CHUNK_WORD_COUNT_WITH_OVERLAP=240440

UC3 has no canonical `chunks.jsonl` and no separate corpus-membership file. Its unambiguous canonical representation is the frozen chunk index and its nine per-document JSON artifacts. Source units are the 664 extracted physical PDF pages. Of those, 638 produce chunks; empty pages produce none. Native metadata uses `page_id`, `page` and C-ordinal chunk IDs. Bundle source-unit fields are mechanical aliases of those frozen fields, not a new source-unit segmentation.

### Frozen artifact bindings

| Artifact | SHA256 |
| --- | --- |
| `corpus/use_cases/UC3/benchmark_scope.json` | `2ea34f7a75def7a9a0c65671a54b0aa131c588acbab89d6ab92788b7e956542e` |
| `corpus/use_cases/UC3/chunking_config.json` | `5937238395de208321edb1a698fc5fcea704b0b7a572214c88b9a39971adab90` |
| `benchmark/config/retrieval/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json` | `cbc006fbab5623af240613e4348bccd17107943e0556a5746409130cd073bac1` |
| `evidence/engineering/uc3_retrieval_foundation_freeze_2026-09-24.md` | `7b7dc03cf3e205bc78fed54fb4b23cb719f2067e1f2a2f1c3830eb419d535b4c` |
| `corpus/use_cases/UC3/processed/chunks/index.json` | `a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e` |
| `corpus/use_cases/UC3/processed/embeddings/UC3-QWEN3-EMBED4B-EXACT-COSINE-v0.1/metadata.json` | `6b80cd3d7910cd1a635a65b3df392af960ab6b2fda3ddf1e246792309b0dd64b` |

CANONICAL_CHUNK_ARTIFACT_AGGREGATE_SHA256=ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563

Aggregate algorithm: in frozen chunk-index document order, concatenate UTF-8 artifact filename, NUL, ASCII SHA256 of that artifact, and LF; SHA256 the resulting byte stream. All nine artifact source hashes also match their accepted manifest records and the actual approved raw PDFs. Embedding metadata was read only to verify the existing source/configuration bindings; no embedding matrix, retrieval index execution, model or diagnostic result was consumed.

## Sensitive/public-source boundary

SENSITIVE_SOURCE_IN_RUNTIME_CORPUS=NO
PUBLIC_SOURCE_BOUNDARY=PASS
SENSITIVE_REPORT_TEXT_COPIED=NO

The UC3 README explicitly excludes the sensitive internal DC4Democracy curation material from public/runtime evidence. Membership, active scope, chunk index, page index and all chunk document/source identities resolve to exactly DOC032–DOC040. All nine eligibility decisions are ELIGIBLE. The approved public URLs, PDF identities and page-derived chunk text were checked; every chunk matches its approved public page window. Thus the boundary check uses positive public-source provenance and complete source identity, not a keyword zero-match. The sensitive report was neither opened nor used for this bundle.

## Complete document inventory

Documents appear in deterministic document-ID order. All metadata below is from frozen membership/page/chunk artifacts. Page numbers are physical PDF indexes, not necessarily printed page labels. Section metadata is synthetic `Page n`; semantic headings below are inspected text topics, not native section identifiers. Word counts use whitespace-separated extracted page text and exclude chunk overlap. Character counts sum Unicode characters across page texts.

### DOC032

DOCUMENT_ID=DOC032
TITLE / COMPONENT=DigComp 3.0: European Digital Competence Framework (JRC144121) / DOC032_digcomp_3_0.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=European Commission, Joint Research Centre
PUBLICATION_DATE=2025
PUBLIC_SOURCE_URL=https://publications.jrc.ec.europa.eu/repository/bitstream/JRC144121/JRC144121_01.pdf
SOURCE_UNIT_COUNT=123
CHUNK_BEARING_SOURCE_UNIT_COUNT=123
CHUNK_COUNT=177
AVAILABLE PAGE/SECTION METADATA=page_id DOC032-P0001–DOC032-P0123; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=542723 Unicode characters; 49840 page-text words
PUBLIC_SOURCE_SHA256=203896c478b72ebb86446c017be78d313be75b03eb9ca1139d061299dfdec84d
CHUNK_ARTIFACT_SHA256=31ff428f15298c2f22e44d695cc0acbd99570ef7f375073855a2a095c08de136
PAGE_ARTIFACT_SHA256=0a08ae673a61590f6e51a0568eb46ec02d15b5f58ca34de4c9095e065f7c38c9

Citizen digital competence: competence areas and descriptions, proficiency levels, AI integration conventions, learning outcomes, application guidance, glossary and development methodology. The annex distinguishes intended from achieved learning outcomes.

### DOC033

DOCUMENT_ID=DOC033
TITLE / COMPONENT=Reference Framework of Competences for Democratic Culture, Volume 1: Context, concepts and model / DOC033_rfcdc_volume_1.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=Council of Europe
PUBLICATION_DATE=2018
PUBLIC_SOURCE_URL=https://rm.coe.int/prems-008318-gbr-2508-reference-framework-of-competences-vol-1-8573-co/16807bc66c
SOURCE_UNIT_COUNT=89
CHUNK_BEARING_SOURCE_UNIT_COUNT=81
CHUNK_COUNT=111
AVAILABLE PAGE/SECTION METADATA=page_id DOC033-P0001–DOC033-P0089; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=214907 Unicode characters; 29762 page-text words
PUBLIC_SOURCE_SHA256=a93866bccc575a825b4cc9e9b5f25c115d7c1ffd29dc677a1acc0aa226daa612
CHUNK_ARTIFACT_SHA256=227a40b3df7e2853501aeb6333f943c2fdd321fe506bc7e80c16c24236e156b2
PAGE_ARTIFACT_SHA256=5683f3c9b86ad01b35674ba1be6fa80246151d73db39e554df270d603d9e3a29

Democratic-culture framework rationale, contextual conditions, values, attitudes, skills, knowledge and critical understanding; the competence model and the purpose, development and use of proficiency descriptors.

### DOC034

DOCUMENT_ID=DOC034
TITLE / COMPONENT=Reference Framework of Competences for Democratic Culture, Volume 2: Descriptors of competences / DOC034_rfcdc_volume_2.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=Council of Europe
PUBLICATION_DATE=2018
PUBLIC_SOURCE_URL=https://rm.coe.int/prems-008418-gbr-2508-reference-framework-of-competences-vol-2-8573-co/16807bc66d
SOURCE_UNIT_COUNT=65
CHUNK_BEARING_SOURCE_UNIT_COUNT=58
CHUNK_COUNT=63
AVAILABLE PAGE/SECTION METADATA=page_id DOC034-P0001–DOC034-P0065; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=155460 Unicode characters; 15636 page-text words
PUBLIC_SOURCE_SHA256=ca73e93bcd8c4a0f4076207c80ab221555ced0b0fd58b2a752d40fc849c7853b
CHUNK_ARTIFACT_SHA256=d39dc4a040e87e0b2fecb3cb308ac54e0563f584dffcf620676c2d3927c90cd0
PAGE_ARTIFACT_SHA256=6ad5d73f555a4beb06be72027bf90b012be1b44436d82252fc3ad4ec339e4bb4

Observable competence descriptors: key-descriptor tables, the wider descriptor bank, proficiency labels and guidance on selecting and using descriptors. These are behavioural indicators rather than population attainment statistics.

### DOC035

DOCUMENT_ID=DOC035
TITLE / COMPONENT=Reference Framework of Competences for Democratic Culture, Volume 3: Guidance for implementation / DOC035_rfcdc_volume_3.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=Council of Europe
PUBLICATION_DATE=2018
PUBLIC_SOURCE_URL=https://rm.coe.int/prems-008518-gbr-2508-reference-framework-of-competences-vol-3-8575-co/16807bc66e
SOURCE_UNIT_COUNT=129
CHUNK_BEARING_SOURCE_UNIT_COUNT=125
CHUNK_COUNT=178
AVAILABLE PAGE/SECTION METADATA=page_id DOC035-P0001–DOC035-P0129; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=348342 Unicode characters; 49100 page-text words
PUBLIC_SOURCE_SHA256=0effd90fcd0f6702becaaae11217acac3da0914269b12d0203152c099b285239
CHUNK_ARTIFACT_SHA256=248007fdccbc757b93a376f43c0f3656c62be448b39c399a5441ee11e325a1a1
PAGE_ARTIFACT_SHA256=512d539b144b93870d2c93e3cf8958e48b3d63b950608b055447a85e749af910

Implementation guidance covering curriculum, pedagogy, assessment, teacher education, whole-school approaches and resilience to radicalisation; purposes, constraints, actors and classroom/school practices.

### DOC036

DOCUMENT_ID=DOC036
TITLE / COMPONENT=Council Recommendation of 22 May 2018 on key competences for lifelong learning / DOC036_key_competences_lifelong_learning.pdf
SOURCE_TYPE=public PDF; council recommendation
SOURCE_ORGANIZATION=Council of the European Union
PUBLICATION_DATE=2018-05-22
PUBLIC_SOURCE_URL=https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=oj:JOC_2018_189_R_0001
SOURCE_UNIT_COUNT=13
CHUNK_BEARING_SOURCE_UNIT_COUNT=13
CHUNK_COUNT=24
AVAILABLE PAGE/SECTION METADATA=page_id DOC036-P0001–DOC036-P0013; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=57345 Unicode characters; 7308 page-text words
PUBLIC_SOURCE_SHA256=dd77e4fe40133869ab29ff7b2232d487786711d50e3687002e02d6a8495a507e
CHUNK_ARTIFACT_SHA256=30874450493323ed59a0c37f09678c99e4de9e28dbdb44fe89f55bb502d3f8a8
PAGE_ARTIFACT_SHA256=7634cd13da92793866ed66d92ad726db435d3f57dc4b3e67e6198cd27733a481

Council recommendations and an annex defining lifelong-learning key competences through knowledge, skills and attitudes; includes digital competence, citizenship and support for competence development.

### DOC037

DOCUMENT_ID=DOC037
TITLE / COMPONENT=ICT Competency Framework for Teachers, Version 3 / DOC037_unesco_ict_cft_v3.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=UNESCO
PUBLICATION_DATE=2018
PUBLIC_SOURCE_URL=https://unesdoc.unesco.org/in/rest/annotationSVC/DownloadWatermarkedAttachment/attach_import_d7d2d5d0-c418-48ae-b932-4005d4d665c6?_=265721eng.pdf
SOURCE_UNIT_COUNT=66
CHUNK_BEARING_SOURCE_UNIT_COUNT=66
CHUNK_COUNT=88
AVAILABLE PAGE/SECTION METADATA=page_id DOC037-P0001–DOC037-P0066; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=281212 Unicode characters; 23548 page-text words
PUBLIC_SOURCE_SHA256=2c7264c00a453ba71ec5ac75a5213b7a24c8ff165adbcd4b0fc231e950b79534
CHUNK_ARTIFACT_SHA256=fa6c3055a87e08e6e60ec4b68a8932f334a9b9e0b62d6f7e9888d26d8f0e7dcf
PAGE_ARTIFACT_SHA256=e166e3d814ce064e6dbe575a10a5116aa496b5304892470825621cea77bba8cf

Teacher ICT competence structured through knowledge acquisition, knowledge deepening and knowledge creation across six aspects of teaching work; detailed objectives/activities and contextual implementation guidance.

### DOC038

DOCUMENT_ID=DOC038
TITLE / COMPONENT=European Declaration on Digital Rights and Principles for the Digital Decade / DOC038_eu_digital_rights.pdf
SOURCE_TYPE=public PDF; declaration
SOURCE_ORGANIZATION=European Union
PUBLICATION_DATE=2023-01-23
PUBLIC_SOURCE_URL=https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=oj:JOC_2023_023_R_0001
SOURCE_UNIT_COUNT=7
CHUNK_BEARING_SOURCE_UNIT_COUNT=7
CHUNK_COUNT=11
AVAILABLE PAGE/SECTION METADATA=page_id DOC038-P0001–DOC038-P0007; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=26354 Unicode characters; 3312 page-text words
PUBLIC_SOURCE_SHA256=9bf3caf8ea2be13f27f1e376eea9d39e9664c308234a20db0a7fb61f873cb32c
CHUNK_ARTIFACT_SHA256=673a73109e48d106caa67c1cff48c5ce368a128186a64e817bd67860ebf70802
PAGE_ARTIFACT_SHA256=cdc9b6f907684fd7d976f2592fc32d8fa749e9846e1c60ccd2c5c08a187a377c

European declaration covering people-centred digital transformation, solidarity and inclusion, freedom of choice, democratic digital participation, safety/security/empowerment and sustainability; principles and commitments.

### DOC039

DOCUMENT_ID=DOC039
TITLE / COMPONENT=European Framework for the Digital Competence of Educators (DigCompEdu), EUR 28775 EN / DOC039_digcompedu.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=European Commission, Joint Research Centre
PUBLICATION_DATE=2017
PUBLIC_SOURCE_URL=https://publications.jrc.ec.europa.eu/repository/bitstream/JRC107466/pdf_digcomedu_a4_final.pdf
SOURCE_UNIT_COUNT=95
CHUNK_BEARING_SOURCE_UNIT_COUNT=88
CHUNK_COUNT=95
AVAILABLE PAGE/SECTION METADATA=page_id DOC039-P0001–DOC039-P0095; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=202869 Unicode characters; 20078 page-text words
PUBLIC_SOURCE_SHA256=253e583b818c4913ee8b6d84a8ef2f21faeb347576777f1659d4d16e01186d2b
CHUNK_ARTIFACT_SHA256=07957a35bd95c3d9f07e92acde88ff8fe69502b8714b57469623363490a46b66
PAGE_ARTIFACT_SHA256=5f04f101c348281e7bf26272996e35ff26cc1583c14c9750290d4e6e082438ec

Educator digital competence: professional engagement, digital resources, teaching and learning, assessment, empowering learners and facilitating learner digital competence; activities, proficiency statements and a progression model.

### DOC040

DOCUMENT_ID=DOC040
TITLE / COMPONENT=European Framework for Digitally-Competent Educational Organisations (DigCompOrg), EUR 27599 EN / DOC040_digcomporg.pdf
SOURCE_TYPE=public PDF; competence framework
SOURCE_ORGANIZATION=European Commission, Joint Research Centre
PUBLICATION_DATE=2015
PUBLIC_SOURCE_URL=https://publications.jrc.ec.europa.eu/repository/bitstream/JRC98209/jrc98209_r_digcomporg_final.pdf
SOURCE_UNIT_COUNT=77
CHUNK_BEARING_SOURCE_UNIT_COUNT=77
CHUNK_COUNT=103
AVAILABLE PAGE/SECTION METADATA=page_id DOC040-P0001–DOC040-P0077; page/page_number; section_index; section='Page n'; no native semantic heading labels
TEXT_LENGTH_OR_WORD_COUNT=250191 Unicode characters; 25956 page-text words
PUBLIC_SOURCE_SHA256=3981f1a2f6ed9ef46777b5d22ce0d11e58610f8f592d8c62e3e5b1f02bcafa09
CHUNK_ARTIFACT_SHA256=7b93b8bed558531d08280fc609a2470a02d6859a6a8616867d40e8fe02dd0312
PAGE_ARTIFACT_SHA256=e97bb1386f7af93a20c9a629e461bebdba46ba9b903d333dc1e6f8342e776c9c

Educational-organisation digital capacity: leadership/governance, teaching/learning, professional development, assessment, content/curricula, collaboration/networking and infrastructure; self-reflection descriptors, development methodology and comparative framework/tool fact sheets.

## Complete source coverage methodology

All nine indexed page and chunk files were parsed in full. All 664 page units and all 850 canonical chunks were enumerated. Page openings and the complete chunk-opening inventory were inspected in document/page/chunk order; substantive text regions were read directly for the topic inventory. The complete raw text is transcribed into the authoring bundle so researcher inspection is not limited to openings or thematic excerpts. This is not a claim that corpus-wide semantic absence has been established.

For each approved page, the existing W450/O75 page-window definition was checked against its canonical chunk IDs and exact text without persisting new chunks. All chunk/source identities, ordinal order, metadata and word counts were verified. No new extraction, corpus materialization or retrieval was run. All 850 texts are copied verbatim, including overlap and layout; no relevant-text filtering is applied.

AUTHORING_BUNDLE_PATH=/home/emadh/UC3_T3A1_AUTHORING_SOURCE_BUNDLE.txt
AUTHORING_BUNDLE_SHA256=aab297778225ab73a3a589f3ed4793737c16960a07e65a4ceb772eddeb9e2413
BUNDLE_ORDER=document_id,source_unit_index,chunk_index
BUNDLE_CHUNK_COVERAGE=PASS
UNKNOWN_BUNDLE_CHUNKS=0
DUPLICATE_BUNDLE_CHUNKS=0
ALL_ACCEPTED_DOCUMENTS_REPRESENTED=YES

The UTF-8 bundle includes chunk/document/source-unit identifiers, physical page and section metadata, source component and title, source SHA256 and the exact text. `TEXT_UTF8_BYTES` frames each raw text for independent parsing even if source text contains delimiter-like strings. Source-unit index is the physical page number; chunk index is the C-ordinal integer. A separate parse verified exact text, identifiers, order, uniqueness, complete coverage and EOF. The 26 pages without canonical chunks have no invented bundle entries. The bundle header and record-field whitelist contain no ranking, score, similarity, condition label, task/gold or result metadata. Public source text mentioning assessment or ranking is preserved as source text; it is not retrieval metadata.

## Prospective information regions — inventory only

Locations below are physical PDF pages, mapping directly to `DOCxxx-Pnnnn-Cnnn` identifiers in the complete bundle. No region is allocated to a task. Later task construction must test localized sufficiency or genuine synthesis and preserve qualifications; repeated tables, overlapping windows and framework summaries do not by themselves establish reasoning requirements.

### Direct retrieval regions

- DOC032: framework structure, proficiency conventions and AI integration (pages 18–27); localized definitions/tables and competence statements (pages 31–51).
- DOC034: key-descriptor tables and proficiency labels (pages 17–25), with the broader descriptor bank available for direct source grounding.
- DOC036: annex competence definitions and knowledge/skills/attitudes (pages 7–11); digital competence starts in DOC036-P0009-C002.
- DOC038: inclusion, education and digital choices/participation commitments (pages 4–6). Treat these as declarations, not measured implementation.
- DOC039: progression/proficiency conventions (pages 28–31) and individual educator competence/activity descriptions (pages 34–87).

### Within-document synthesis regions

- DOC032: proficiency conventions (pages 23–27), competence statements (31–51) and learning-outcome adaptation/measurement guidance (86–113). The intended/achieved distinction is explicit in DOC032-P0088-C002.
- DOC033: competence concepts/model (pages 31–59) and descriptor purpose/use (61–66). Model structure and use qualifications occupy distinct locations; later questions must require both.
- DOC035: assessment purposes and quality/ethical constraints (55–62), assessment approaches/context (66–76), and whole-school implementation (91–101). These concern distinct levels and actors.
- DOC037: framework matrix/levels (22–26), objectives and activities (28–47), and contextual implementation (48–58). Structure and contextual implementation are distinct evidence regions.
- DOC039: selection/protection/sharing of resources (44–49) and accessibility, differentiation and learner engagement (70–75). Distinguish competence descriptions from repeated proficiency rubrics.
- DOC040: leadership/governance (23–24), assessment practices (28–29), and infrastructure (34–35). Organisational conditions and practice requirements appear separately.

### Cross-document complementary regions

| Documents | Complementary information | Integrity caution |
| --- | --- | --- |
| DOC033 + DOC034 | Democratic competence concepts/model versus detailed observable descriptor tables/bank. | Both volumes repeat descriptor counts and usage context; repeated material alone does not require both. |
| DOC034 + DOC035 | Operational descriptors versus assessment/implementation purposes, constraints and practices. | A later synthesis must need descriptor content and implementation guidance independently. |
| DOC037 + DOC039 | Teacher ICT matrix and contextual implementation versus educator digital practices/progression. | Different actors/structures and proficiency conventions; no unsupported level equivalence. |
| DOC039 + DOC040 | Educator competences/actions versus organisation governance, infrastructure and capacity. | Distinguish individual practice from institutional provision; no inferred causal guarantee. |
| DOC032 + DOC038 | Citizen competence/AI and digital participation descriptions versus digital-rights principles and commitments. | Competence statements and normative rights commitments are different evidence types, not outcomes. |
| DOC032 + DOC036 | Detailed digital framework/proficiency descriptions versus broad lifelong-learning competence definitions. | Publication/version differences must remain explicit; no assumed one-to-one framework equivalence. |

### Insufficient-evidence authoring domains — absence NOT established

- Intended competences, descriptors and learning outcomes versus measured attainment for a specified population. DOC032 explicitly separates intended from achieved outcomes; DOC033/DOC034 also contain empirical descriptor-development/validation material that must be inspected in a later absence audit.
- Guidance and objectives for teacher/organisation digital capacity versus observed implementation coverage or effectiveness. DOC037 implementation passages and DOC040 framework/tool fact sheets contain contextual and reported practice information; they cannot be dismissed as universally hypothetical.
- Digital-rights declarations/commitments versus measured fulfilment or effects in a specified jurisdiction or population. DOC038 offers plausible policy near misses, but no absence conclusion is drawn here.
- Competence-framework progression conventions versus independently measured changes attributable to an intervention. Framework-development evidence, validation studies and implementation examples across all nine documents require full inspection before any absence finding.

These are broad information domains only. No target population, cutoff, candidate question or gold response is selected. A later insufficient-evidence candidate requires complete 850-chunk enumeration, deterministic broad term-family scans, manual classification of plausible hits and explicit separation of normative/intended, illustrative and observed evidence. This inventory cannot substitute for that audit.

## Prospective authoring allocation

| IDs | Task type |
| --- | --- |
| T021–T023 | direct_retrieval |
| T024–T026 | within_document_reasoning |
| T027–T028 | cross_document_reasoning |
| T029–T030 | insufficient_evidence |

The allocation is supplied by the researcher. No questions, answers, evidence bindings or difficulty labels have been selected.

## No-leakage / no-result controls and validation

RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
MODEL_OUTPUT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
DIAGNOSTIC_RETRIEVAL_RESULTS_USED=NO
CONDITION_LABELS_USED=NO
FUTURE_TASK_PERFORMANCE_USED=NO

MODEL_OUTPUT_USED=NO denotes no task/model inference or benchmark output consumed; this source-inspection inventory itself is LLM-assisted. Historical freeze evidence was used for identity/provenance only. Diagnostic result files, ranking outputs and embedding matrices were not inspected. No workflow/task execution or benchmark tests were run.

BUNDLE_CHUNK_COVERAGE=PASS
PUBLIC_SOURCE_BOUNDARY=PASS
FOUNDATION_FILES_UNCHANGED=YES
REPOSITORY_ARTIFACT_SCOPE=one new untracked inventory only
DIFF_CHECK=PASS

TASK_CANDIDATES_CREATED=NO
TASK_JSON_CREATED=NO
HUMAN_VERIFICATION=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO

The task-status fields refer to prospective UC3 tasks; the qualified UC3 source/retrieval foundation and already frozen UC1/UC2 tasks retain their historical status.
