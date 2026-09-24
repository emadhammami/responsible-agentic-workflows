# UC3 Retrieval Diagnostic Protocol Freeze — 2026-09-24

MODE=AUTHORIZED_PROTOCOL_FREEZE_ONLY

## Freeze declaration

- The UC3 identity diagnostic protocol is frozen **BEFORE any UC3 identity diagnostic** execution.
- The UC3 semantic diagnostic protocol is frozen **BEFORE any UC3 semantic diagnostic** execution.
- Both protocols are frozen **BEFORE 4B4**.
- Both protocols are frozen **BEFORE any benchmark execution**.

## Frozen protocol summary

| Field | Identity | Semantic |
|---|---|---|
| Status at freeze | `frozen_before_execution` | `frozen_before_execution` |
| Probe count | 9 (one per accepted UC3 document) | 9 (one per accepted UC3 document) |
| Document coverage | 9/9 (DOC032–DOC040) | 9/9 (DOC032–DOC040) |
| top_k | 10 | 10 |
| repeats per probe | 3 | 3 |
| ranking unit | chunk | chunk (ranking unit per UC1 core design) |
| expected-document measure | rank of first retrieved chunk of expected document | rank of first retrieved chunk of expected document |
| per-probe source basis | 9/9 | 9/9 |
| acceptance gate | n/a (identity diagnostic) | TOP10=8, TOP5=7, TOP3=5, STABLE_TOP1=8 |

- The semantic probe-count adaptation from the UC1 baseline of 8 to 9 was **prospective**:
  it was derived from the accepted UC3 document count before any diagnostic execution.
- The gate thresholds were prospectively scaled from the frozen UC1 gate (7/6/4/7 of 8)
  using `ceil(9 * threshold / 8)` = 8/7/5/8 before any UC3 diagnostic execution or result
  observation.

## Design-purity statements

- **No retrieval result** was used to design any probe, expected document, or threshold.
- **No benchmark question, gold, or answer** was used.
- **Semantic probe source support** came only from pre-retrieval metadata:
  `corpus/use_cases/UC3/source_selection.tsv`, `corpus/use_cases/UC3/eligibility_review.tsv`,
  `corpus/use_cases/UC3/README.md`, and `corpus/use_cases/UC3/benchmark_scope.json`.
- **Byte-level embedding non-determinism** (observed in the 4B3 Run-1/Run-2 materialization)
  remains a documented reproducibility observation only. It did **not** alter these protocols,
  their queries, expected documents, execution parameters, or thresholds.

## Frozen protocol artifacts

| Artifact | SHA256 |
|---|---|
| `evidence/engineering/uc3_retrieval_identity_probe_protocol_v0.1.json` | `6221b933ae21058bee73b1eb7dbd0c6169a6f16a6457ac5c348c8672276da9fd` |
| `evidence/engineering/uc3_retrieval_semantic_probe_protocol_v0.1.json` | `ca8a0979edb090ebc63b7d702f4edb2003ca83b21dbea344dfff81ebe34721c4` |
| approved identity draft (temp) | `e4fa6a34ee010d951c4fd830664a164cbcc47a727cad653728f9d875a0e17cfe` |
| approved semantic draft (temp) | `ccd907a7f40e42c160c20abf45893f36eabbe690494cbf73292f1b6afb285c98` |

Status-only transformation proof: After normalizing only the `status` field, the approved draft and
frozen repository copy are deep-object equivalent in every other field. This is a
content-equivalence proof, not a byte-for-byte file-identity claim, because the repository copies
were re-serialized. `IDENTITY_STATUS_ONLY_TRANSFORMATION=PASS`,
`SEMANTIC_STATUS_ONLY_TRANSFORMATION=PASS`.

This evidence-only wording correction was completed before the first UC3 diagnostic retrieval
execution and does not alter either frozen protocol.

## Frozen source-basis bindings (pre-retrieval metadata)

| Artifact | SHA256 |
|---|---|
| `corpus/use_cases/UC3/source_selection.tsv` | `f8a254b0e9446040f2e7fefb3e726ed66a540ce1259991ab74acd0b1a2f0ba88` |
| `corpus/use_cases/UC3/eligibility_review.tsv` | `65c1965cf3a81813d266b7e147a64815453e99e8748ea18541d431aa7e48aada` |
| `corpus/use_cases/UC3/README.md` | `0b6a5662098050f5b1e0c9ec52bf1f9db3703eb872a3983a0c9431598414d663` |
| `corpus/use_cases/UC3/benchmark_scope.json` | `4ba17151cf9795b4ab24b58c49ed608dca84aed824d2eb97ee73390a28c115bb` |
| `evidence/engineering/uc3_embedding_materialization_2026-09-24.md` (4B3 evidence) | `a25ea8d8f10204cf3f45569b91ed5f73b30fcd3820fba9251d50cd65176bcf44` |

## Semantic probe audit table (six columns)

| PROBE_ID | EXPECTED_DOCUMENT | QUERY | SOURCE_BASIS | SUPPORTED_CONCEPTS | TITLE_LEAKAGE |
|---|---|---|---|---|---|
| SEM01 | DOC032 | What a person needs to know and be able to do with digital technologies in work, education and everyday civic life, organised across competence areas and proficiency levels. | eligibility_review.tsv UC3-C01 (D_uc3_scope: core digital-competence framework; 5 competence areas, 21 competences, 4 proficiency levels; E_evidentiary: component tables, learning outcomes); benchmark_scope.json competence_framework (DOC032); README.md family 1 | core digital-competence framework; competence areas; proficiency levels; work/education/everyday contexts | NO |
| SEM02 | DOC033 | Values, attitudes, dispositions, knowledge and skills that underpin democratic participation and how each of them is articulated as a competence. | eligibility_review.tsv UC3-C02 (D_uc3_scope: democratic/civic competence model; 4 areas, 20 competences; digital citizenship education); benchmark_scope.json competence_framework (DOC033); README.md family 2 | values/attitudes/dispositions; knowledge and skills; democratic participation; competences | NO |
| SEM03 | DOC034 | A set of key expectations and descriptors that spell out concrete behaviours and skills in line with competence areas for civic participation. | eligibility_review.tsv UC3-C03 (D_uc3_scope: operational descriptors for the 20-competence model; 135 key + 447 descriptors across 3 levels; E_evidentiary: structured descriptor tables); benchmark_scope.json competence_framework (DOC034); README.md family 2 | key expectations; descriptors; concrete behaviours and skills; competence areas; level structure | NO |
| SEM04 | DOC035 | Practical guidance about how to embed, practise and assess these competences across curriculum, pedagogy, assessment, teacher education and whole-school settings. | eligibility_review.tsv UC3-C04 (D_uc3_scope: implementation guidance applying the 20 competences across curriculum, pedagogy, assessment, teacher education, whole-school); benchmark_scope.json competence_framework (DOC035); README.md family 2 | implementation guidance; embedding/practising/assessing competences; curriculum, pedagogy, assessment, teacher education, whole-school | NO |
| SEM05 | DOC036 | A European recommendation setting out the key competences all citizens should develop over a lifetime, including how to use, apply, create and participate through digital means, including the definition and scope of digital competence. | eligibility_review.tsv UC3-C05 (D_uc3_scope: EU key-competence framework incl. digital competence definition; 8 key competences; E_evidentiary: primary legal/normative Recommendation text); benchmark_scope.json policy_and_reference (DOC036); README.md family 3 | European Recommendation (normative text); key competences over a lifetime; use/apply/create/participate digitally; digital competence definition and scope | NO |
| SEM06 | DOC037 | A competency framework aimed at educators, describing what they should know and be able to do with information and communication technologies, including digital content, collaboration and learner support. | eligibility_review.tsv UC3-C06 (D_uc3_scope: educator digital-competence framework; 18 competencies, 6 aspects, 3 levels; E_evidentiary: KA/KD/KC indicators); benchmark_scope.json competence_framework (DOC037); README.md supporting framework 4 | educator competency framework; ICT knowledge and abilities; digital content; collaboration; learner support | NO |
| SEM07 | DOC038 | A primary declaratory source organised into six chapters and twenty-four numbered normative items setting out rights-related normative principles for a digital context. | eligibility_review.tsv UC3-C07 (D_uc3_scope: digital rights & principles for the Digital Decade; E_evidentiary: 24 numbered normative items across 6 chapters; primary normative declaratory source); benchmark_scope.json policy_and_reference (DOC038); README.md supporting framework 5 | primary/declaratory source; 6 chapters; 24 numbered normative items; rights-related principles; digital context | NO |
| SEM08 | DOC039 | A structured set of educator capabilities organised into twenty-two competences, six areas and six proficiency levels, with per-level descriptors, typical activities and an evaluation rubric. | eligibility_review.tsv UC3-C08 (D_uc3_scope: educator digital-competence framework; 22 competences, 6 areas, 6 levels A1–C2; E_evidentiary: per-competence x per-level descriptors + typical activities + rubric); benchmark_scope.json competence_framework (DOC039); README.md supporting framework 6 | educator capabilities; 22 competences; 6 areas; 6 proficiency levels; per-level descriptors; typical activities; evaluation rubric | NO |
| SEM09 | DOC040 | An organisational and institutional digital-competence framework structured into seven elements, fifteen sub-elements and seventy-four descriptors presented in tables. | eligibility_review.tsv UC3-C09 (D_uc3_scope: organisational/institutional digital-competence framework; 7 elements, 15 sub-elements, 74 descriptors; E_evidentiary: element/sub-element/descriptor tables); benchmark_scope.json competence_framework (DOC040); README.md supporting framework 7 | organisational/institutional digital-competence framework (documented wording, not "digital capability"); 7 elements; 15 sub-elements; 74 descriptors; table presentation | NO |

Leakage checks (performed per row, not as a single global boolean):

- A. automated prohibited-token scan (canonical titles, aliases DigComp/RFCDC/DigCompEdu/DigCompOrg,
  DOIs, JRC IDs, OJ/CELEX/legal citations, URLs, "Digital Decade", "use case") — all 9 rows clean.
- B. manual near-title comparison — no query is an essentially-reworded canonical title;
  SEM07/SEM08/SEM09 are structural/role paraphrases grounded in the recorded
  scope/evidentiary metadata.

`SEMANTIC_TITLE_LEAKAGE_COUNT=0` (derived from the 9 individual NO rows above).

`SEM01_SOURCE_SUPPORT=PASS` through `SEM09_SOURCE_SUPPORT=PASS` (each derived from the
SUPPORTED_CONCEPTS column, each concept mapped to the cited pre-retrieval metadata fields).

## Git state at freeze (recorded honestly)

The repository already contains pre-existing UC3 work from earlier phases; the tree was dirty
before this freeze and remains dirty after it. Not claimed clean:

- `PREEXISTING_REPO_WORKTREE_DIRTY=YES`
- Tracked modified at guard time (1 file): `corpus/manifest.json` (pre-existing, from earlier
  UC3 phases). New tracked-file addition by this freeze: none — the two frozen protocols are
  new untracked files.
- `TRACKED_SRC_TEST_CHANGES=0` (among the modified tracked files, 0 are under source or test
  paths; the single modified tracked file is `corpus/manifest.json`)
- `STAGED_CHANGES=0`
- `NEW_FILES_CREATED_BY_THIS_FREEZE=`
  - `evidence/engineering/uc3_retrieval_identity_probe_protocol_v0.1.json`
  - `evidence/engineering/uc3_retrieval_semantic_probe_protocol_v0.1.json`
  - `evidence/engineering/uc3_retrieval_diagnostic_protocol_freeze_2026-09-24.md`

## Immutability declaration

After this prospective freeze, the UC3 diagnostic probes, expected
documents, execution parameters, semantic acceptance thresholds, and
source-basis definitions must not be changed in response to identity
diagnostic results, semantic diagnostic results, retrieval behaviour,
or benchmark outcomes.

## Out-of-scope confirmations

- `UC3_DIAGNOSTICS_EXECUTED=NO`
- `RETRIEVAL_CONFIG_STATUS=working`
- `CORPUS_FROZEN=false` (benchmark_scope.json `controls.corpus_frozen=false`)
- `BENCHMARK_STARTED=NO`
- `SOURCE_CODE_MODIFIED=NO`
- `TESTS_MODIFIED=NO`
- `COMMIT=NO`
- `PUSH=NO`
