# UC3 T029–T030 Corpus-Wide Insufficient-Evidence Absence Audit

Date: 2026-09-27

## Frozen corpus identity and guards

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=55d6e33b2674b01969773ee8b99bf71839f94997
PROTOCOL_FREEZE_COMMIT=55d6e33b2674b01969773ee8b99bf71839f94997
PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
UC3_FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a
HISTORICAL_GLOBAL_MANIFEST_SHA256=9858ca4f656078add7e876d831a3551438672e1e978c218c8fe08522311133a1
CURRENT_GLOBAL_MANIFEST_SHA256=bd01315f1f6d035e4105ae4d89378c6df24af4d877411e9228a2fcf704368e89
UC3_MEMBERSHIP_RECORDS_IDENTICAL_TO_FOUNDATION_FREEZE=YES
UC3_MEMBERSHIP_PATH=corpus/manifest.json (accepted UC3 entries)
UC3_SCOPE_PATH=corpus/use_cases/UC3/benchmark_scope.json
UC3_SCOPE_SHA256=2ea34f7a75def7a9a0c65671a54b0aa131c588acbab89d6ab92788b7e956542e
CANONICAL_CHUNKS_INDEX=corpus/use_cases/UC3/processed/chunks/index.json
CANONICAL_CHUNK_FILES=DOC032.chunks.json through DOC040.chunks.json under processed/chunks
CHUNK_INDEX_SHA256=a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e
CANONICAL_CHUNK_ARTIFACT_AGGREGATE_SHA256=ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563
CANONICAL_SOURCE_UNITS_INDEX=corpus/use_cases/UC3/processed/pages/index.json
PRIOR_INVENTORY_SHA256=f73f3c06bb96eeec47e0602b1d9d521f346a003bb39be39dfdf2f8f3ec0ef476
PRIOR_CANDIDATE_AUDIT_SHA256=9ab8222b7526cca0325855a2b3e7abf6746b2fb411ce0f91f9d71f99468f181f

There is no canonical UC3 chunks.jsonl: the qualified frozen representation is the chunk index plus nine per-document JSON files. The current global manifest includes later UC2 records; its whole-file identity differs from the historical global manifest, while the UC3 membership records remain identical. Every accepted public raw-PDF hash matches its manifest/page/chunk source binding. Every canonical chunk exactly matches its existing page window. The source-unit count includes 26 pages without chunks; no invented chunks are added for them.

CORPUS_DOCUMENTS_SCANNED=9
CORPUS_SOURCE_UNITS_SCANNED=664
CORPUS_CHUNKS_SCANNED=850
CHUNK_BEARING_SOURCE_UNITS=638
SENSITIVE_SOURCE_IN_RUNTIME_CORPUS=NO
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
FROZEN_PUBLIC_CORPUS_ONLY=YES

### Deterministic document and source-artifact coverage

| Document | Title | Page units | Chunk-bearing pages | Chunks | Chunk artifact SHA256 | Page artifact SHA256 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| DOC032 | DigComp 3.0: European Digital Competence Framework (JRC144121) | 123 | 123 | 177 | 31ff428f15298c2f22e44d695cc0acbd99570ef7f375073855a2a095c08de136 | 0a08ae673a61590f6e51a0568eb46ec02d15b5f58ca34de4c9095e065f7c38c9 |
| DOC033 | Reference Framework of Competences for Democratic Culture, Volume 1: Context, concepts and model | 89 | 81 | 111 | 227a40b3df7e2853501aeb6333f943c2fdd321fe506bc7e80c16c24236e156b2 | 5683f3c9b86ad01b35674ba1be6fa80246151d73db39e554df270d603d9e3a29 |
| DOC034 | Reference Framework of Competences for Democratic Culture, Volume 2: Descriptors of competences | 65 | 58 | 63 | d39dc4a040e87e0b2fecb3cb308ac54e0563f584dffcf620676c2d3927c90cd0 | 6ad5d73f555a4beb06be72027bf90b012be1b44436d82252fc3ad4ec339e4bb4 |
| DOC035 | Reference Framework of Competences for Democratic Culture, Volume 3: Guidance for implementation | 129 | 125 | 178 | 248007fdccbc757b93a376f43c0f3656c62be448b39c399a5441ee11e325a1a1 | 512d539b144b93870d2c93e3cf8958e48b3d63b950608b055447a85e749af910 |
| DOC036 | Council Recommendation of 22 May 2018 on key competences for lifelong learning | 13 | 13 | 24 | 30874450493323ed59a0c37f09678c99e4de9e28dbdb44fe89f55bb502d3f8a8 | 7634cd13da92793866ed66d92ad726db435d3f57dc4b3e67e6198cd27733a481 |
| DOC037 | ICT Competency Framework for Teachers, Version 3 | 66 | 66 | 88 | fa6c3055a87e08e6e60ec4b68a8932f334a9b9e0b62d6f7e9888d26d8f0e7dcf | e166e3d814ce064e6dbe575a10a5116aa496b5304892470825621cea77bba8cf |
| DOC038 | European Declaration on Digital Rights and Principles for the Digital Decade | 7 | 7 | 11 | 673a73109e48d106caa67c1cff48c5ce368a128186a64e817bd67860ebf70802 | cdc9b6f907684fd7d976f2592fc32d8fa749e9846e1c60ccd2c5c08a187a377c |
| DOC039 | European Framework for the Digital Competence of Educators (DigCompEdu), EUR 28775 EN | 95 | 88 | 95 | 07957a35bd95c3d9f07e92acde88ff8fe69502b8714b57469623363490a46b66 | 5f04f101c348281e7bf26272996e35ff26cc1583c14c9750290d4e6e082438ec |
| DOC040 | European Framework for Digitally-Competent Educational Organisations (DigCompOrg), EUR 27599 EN | 77 | 77 | 103 | 7b93b8bed558531d08280fc609a2470a02d6859a6a8616867d40e8fe02dd0312 | e97bb1386f7af93a20c9a629e461bebdba46ba9b903d333dc1e6f8342e776c9c |

## Complete coverage and absence-audit method

1. Parse every indexed page and chunk artifact directly; enumerate all 664 page IDs and all 850 unique chunk IDs. Preserve frozen document/page/C-ordinal order. Verify accepted membership, scope and exact public page-derived text; do not load retrieval diagnostics, similarity values, embeddings or a benchmark workflow.
2. Apply the broad deterministic term families below to every full chunk text. For lexical matching only, normalize Unicode to NFC, remove soft hyphens, join word fragments split by a hyphen followed by whitespace, lowercase and collapse whitespace. Preserve original text for evidence and hashes. Family flags indicate matches, never relevance scores or rankings; there is no top-k or ranked filtering.
3. Inspect complete document/page/chunk-opening coverage, all empirical/adoption/outcome contexts, framework-specific passages and their surrounding source paragraphs. Read full high-risk passages: RFCDC descriptor validation/pilots; pedagogical/practice histories and research summaries; whole-school benefits/evaluation guidance; resilience-training claims; DigCompOrg analytics tables, development/conclusion and comparative fact sheets; and analogous statistics/implementation/analytics passages in every other document. Keyword hits are navigational aids, not absence proof. Generic competence/rubric/glossary passages are assessed by their content/genre, not treated as empirical just because they say “measure”, “has” or “I”.
4. Assign an explicit primary content classification and reason code to every chunk for each candidate (complete ledger below). Mixed chunks may contain more than one passage class; the detailed findings record those distinctions. Primary counts are chunk counts including overlaps, not independent study counts, and sum to 850 per candidate. Broad scan hits outside the requested entity/measure are retained in coverage even when classified IRRELEVANT.
5. Test all plausible empirical passages against the requested conjunction. T029 needs a reported realised improvement in learners’ democratic participation after RFCDC competence/descriptor implementation. It does not require an RCT, a particular numerical scale or causal identification; qualitative measured change could count. T030 needs an observed analytics-governance adoption proportion for DigCompOrg implementers and measured related retention/learning outcomes; a recommendation, target or other-tool uptake ratio cannot satisfy it. Actual findings would override the insufficient-evidence designation.
6. Check that no combined passage across documents fills missing entity/intervention/outcome bindings. Do not infer that similar competences, a framework reference, an available measurement tool, an empirical scale-validation process or a cited external report establishes the requested implemented-programme result. No external reference is fetched.

The public-source boundary is established positively by all-nine approved PDF identities, membership/scope, page/chunk provenance and complete enumeration. The sensitive DC4Democracy report was not consulted. This audit is LLM-assisted direct inspection; HUMAN_VERIFICATION=NO is maintained. It establishes absence within this frozen corpus, not absence of real-world evidence or implementation.

### Exact deterministic term families

Regex expressions use Python re, case-insensitive. A match in any family constitutes a broad scan hit. The empirical/adoption context sweep expands every match in source order and merges overlapping context windows; full passages are then inspected for the materially plausible cases catalogued below. No window is selected by a score.

#### T029

| Family flag | Regex |
| --- | --- |
| F | `\brfcdc\b\|\bcdc\b\|reference framework of competences\|democratic.{0,35}competenc\|competenc.{0,35}democratic` |
| P | `participat\w*\|deliberat\w*\|civic\w*\|citizen\w*\|engag\w*\|student voice\|school councils?` |
| L | `learn\w*\|student\w*\|pupil\w*\|teacher\w*\|educat\w*\|school\w*` |
| I | `implement\w*\|deploy\w*\|adopt\w*\|appl\w*\|practic\w*\|whole.school\|interven\w*` |
| D | `descriptor\w*\|competenc\w*\|proficien\w*\|curricul\w*` |
| A | `assess\w*\|evaluat\w*\|measur\w*\|scal\w*\|observ\w*\|test\w*` |
| O | `outcome\w*\|result\w*\|effect\w*\|impact\w*\|improv\w*\|increas\w*\|decreas\w*\|change\w*\|before\|after\|gain\w*` |
| E | `empir\w*\|pilot\w*\|research\w*\|stud(?:y\|ies)\|survey\w*\|evidence\|data\|report\w*\|found\|demonstrat\w*\|significan\w*\|quantit\w*\|qualit\w*\|longitud\w*\|follow.up\|\d\s*%` |

#### T030

| Family flag | Regex |
| --- | --- |
| F | `digcomporg\|digitally.competent educational organis?ations?\|organisation\w*.{0,25}digital capacity\|organization\w*.{0,25}digital capacity` |
| A | `analytics\|analytic\w*\|learning design\|data\|evidence` |
| P | `polic\w*\|code of practice\|governan\w*\|privacy\|confidential\w*\|safeguard\w*` |
| I | `implement\w*\|deploy\w*\|appl\w*\|practic\w*\|interven\w*` |
| G | `organi[sz]\w*\|institution\w*\|school\w*\|educat\w*` |
| U | `adopt\w*\|uptake\|up.take\|reach\w*\|cover\w*\|respond\w*\|response\w*\|return\w*\|participat\w*\|complet\w*` |
| R | `proportion\w*\|percent\w*\|per cent\|ratio\w*\|rates?\|out of\|half\|third\|\d[\d,. ]*%\|\b\d+\b` |
| O | `retention\|retain\w*\|dropout\w*\|drop.out\|attrit\w*\|persist\w*\|learn\w*\|achievement\w*\|outcome\w*\|performance\|improv\w*\|impact\w*\|effect\w*` |
| E | `empir\w*\|pilot\w*\|research\w*\|stud(?:y\|ies)\|survey\w*\|evaluat\w*\|measur\w*\|observ\w*\|report\w*\|evidence\|found\|demonstrat\w*\|significan\w*\|quantit\w*\|qualit\w*` |

### Document-level deterministic scan counts

| Document | Enumerated chunks | T029 any-family hits | T030 any-family hits |
| --- | ---: | ---: | ---: |
| DOC032 | 177 | 166 | 177 |
| DOC033 | 111 | 108 | 111 |
| DOC034 | 63 | 60 | 63 |
| DOC035 | 178 | 175 | 178 |
| DOC036 | 24 | 24 | 24 |
| DOC037 | 88 | 88 | 88 |
| DOC038 | 11 | 11 | 11 |
| DOC039 | 95 | 89 | 91 |
| DOC040 | 103 | 102 | 103 |

Per-family hit counts (chunks, not matched words):

T029_FAMILY_F_CHUNKS=259
T029_FAMILY_P_CHUNKS=359
T029_FAMILY_L_CHUNKS=664
T029_FAMILY_I_CHUNKS=513
T029_FAMILY_D_CHUNKS=659
T029_FAMILY_A_CHUNKS=455
T029_FAMILY_O_CHUNKS=566
T029_FAMILY_E_CHUNKS=476
T029_ANY_FAMILY_CHUNKS=823

T030_FAMILY_F_CHUNKS=31
T030_FAMILY_A_CHUNKS=236
T030_FAMILY_P_CHUNKS=241
T030_FAMILY_I_CHUNKS=489
T030_FAMILY_G_CHUNKS=554
T030_FAMILY_U_CHUNKS=385
T030_FAMILY_R_CHUNKS=831
T030_FAMILY_O_CHUNKS=660
T030_FAMILY_E_CHUNKS=518
T030_ANY_FAMILY_CHUNKS=846

## T029

TASK_ID=T029
TASK_TYPE=insufficient_evidence

### Exact question

According to the frozen UC3 corpus, what measured improvement in learners'
democratic participation was reported after educational settings implemented
RFCDC competences or descriptors?

### Materially plausible near misses and empirical counterchecks

#### T029-N01 — Participation purpose and scope limits

CHUNKS=DOC033-P0013-C001, DOC033-P0029-C001, DOC033-P0030-C001, DOC033-P0040-C001
PASSAGE_CLASSIFICATION=FRAMEWORK_DEFINITION

The model identifies competences needed for democratic participation. Pages 29–30 explicitly say competences are necessary but not sufficient: institutional opportunities, resources, equality and disadvantage matter. This is a conceptual/policy condition, not a reported measured improvement after implementation.

#### T029-N02 — Proficiency and observable behaviour

CHUNKS=DOC034-P0013-C001, DOC034-P0014-C001, DOC034-P0014-C002, DOC034-P0015-C001, DOC034-P0015-C002, DOC034-P0016-C001, DOC034-P0017-C001, DOC034-P0018-C001, DOC034-P0019-C001, DOC034-P0020-C001, DOC034-P0021-C001, DOC034-P0022-C001, DOC034-P0023-C001, DOC034-P0024-C001, DOC034-P0025-C001
PASSAGE_CLASSIFICATION=ASSESSMENT_GUIDANCE / DESCRIPTOR

Concrete descriptors can support assessment and educational interventions; observation should cover situations and time. Key behaviours and Basic/Intermediate/Advanced labels describe proficiency, not how much learners’ democratic participation improved after RFCDC implementation. The remaining full-bank tables on physical pages 27–53 are enumerated/classified in the ledger with the same distinction.

#### T029-N03 — Real empirical descriptor development

CHUNKS=DOC033-P0012-C001, DOC033-P0062-C001, DOC033-P0062-C002, DOC033-P0063-C001, DOC034-P0012-C001, DOC034-P0055-C001, DOC034-P0056-C001, DOC034-P0056-C002, DOC034-P0057-C001, DOC034-P0057-C002, DOC034-P0058-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS

The sources report practitioner feedback, piloting and Rasch scaling: 3,094 practitioners in the development account; 1,236 feedback contributors; 858 teachers from 16 countries in piloting; over 250 responses per piloted descriptor; 447 validated descriptors and 135 key descriptors. Those are genuine empirical development/validation results. Learner observations were used to validate/scale items, not to report an implementation-related improvement in learners’ democratic participation. Do not confuse numbers of descriptors/practitioners or item fit with a participation effect.

#### T029-N04 — Assessment after learning is a possible use

CHUNKS=DOC033-P0064-C001, DOC033-P0064-C002, DOC033-P0065-C001, DOC033-P0065-C002, DOC033-P0066-C001, DOC034-P0059-C001
PASSAGE_CLASSIFICATION=ASSESSMENT_GUIDANCE

The sources permit assessment after a learning period and warn that a single observed behaviour or absence is not sufficient to establish proficiency. They describe how descriptors may be used; they do not report a completed RFCDC implementation and measured participation change.

#### T029-N05 — Actual practice histories and classroom testimony

CHUNKS=DOC035-P0023-C001, DOC035-P0041-C001, DOC035-P0085-C001, DOC035-P0085-C002, DOC035-P0086-C001, DOC035-P0086-C002
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS

Andorran project-based curricula, the Tuning Project, the Life is Diversity student/teacher network, Malta’s diversity course and a teacher’s mathematics activity are described. These are not all hypothetical: practice histories and testimony exist. The described content/implementation and dates do not provide a measured improvement in democratic participation following implementation of RFCDC competences/descriptors; the mathematics observation concerns a classification insight, not a participation change.

#### T029-N06 — Cooperative-learning research and Jigsaw track record

CHUNKS=DOC035-P0036-C001, DOC035-P0046-C001
PASSAGE_CLASSIFICATION=EMPIRICAL_REALIZED_OUTCOME

Page 36 reports studies finding less tension/aggression/conflict and educators’ claims about academic mastery and hostile/intolerant attitudes; page 46 gives the Jigsaw Classroom a four-decade track record of reducing racial/ethnic conflict and improving outcomes. These reported outcome claims are retained as empirical near misses. The 30-student/50-minute reading illustration on page 36 is an illustrative participation-opportunity calculation, not a measured RFCDC intervention result. None of these passages reports the requested measured democratic-participation improvement after identified RFCDC implementation. No controlled-trial requirement is imposed; the entity, intervention and endpoint mismatches suffice.

#### T029-N07 — Action research and teaching/service/project exercises

CHUNKS=DOC035-P0032-C001, DOC035-P0032-C002, DOC035-P0033-C001, DOC035-P0033-C002, DOC035-P0034-C001, DOC035-P0035-C001, DOC035-P0035-C002, DOC035-P0038-C001, DOC035-P0039-C001, DOC035-P0047-C001, DOC035-P0048-C001, DOC035-P0049-C001, DOC035-P0050-C001, DOC035-P0051-C001, DOC035-P0052-C001, DOC035-P0074-C001
PASSAGE_CLASSIFICATION=IMPLEMENTATION_GUIDANCE / DESCRIPTOR

Teachers are advised to pilot practices, interview/survey students and reflect; democratic processes, cooperative work, service learning, Jigsaw, Project Citizen and water-footprint projects give ways to practise or assess CDC. Expected participation opportunities and instructions to evaluate impact are not results of a completed evaluation. Page 49’s competence/descriptor table is likewise not observed learner improvement.

#### T029-N08 — Measurement, evaluation and reliability

CHUNKS=DOC035-P0054-C001, DOC035-P0055-C001, DOC035-P0055-C002, DOC035-P0056-C001, DOC035-P0056-C002, DOC035-P0057-C001, DOC035-P0057-C002, DOC035-P0061-C001, DOC035-P0062-C001, DOC035-P0062-C002, DOC035-P0063-C001, DOC035-P0063-C002, DOC035-P0064-C001, DOC035-P0064-C002, DOC035-P0065-C001, DOC035-P0065-C002, DOC035-P0066-C001, DOC035-P0066-C002, DOC035-P0067-C001, DOC035-P0067-C002, DOC035-P0068-C001, DOC035-P0069-C001, DOC035-P0069-C002, DOC035-P0070-C001, DOC035-P0070-C002, DOC035-P0071-C001, DOC035-P0072-C001, DOC035-P0073-C001, DOC035-P0075-C001, DOC035-P0076-C001
PASSAGE_CLASSIFICATION=ASSESSMENT_GUIDANCE

Assessment describes/measures learner proficiency/achievement; evaluation concerns effectiveness of a system/institution/programme. Guidance addresses validity, reliability, stakes, observation, portfolios and peer/self-assessment. Examples such as improved communication feedback and a planned assessment method cannot substitute for an empirically reported implementation outcome. Qualitative evidence is not excluded merely for lacking a number.

#### T029-N09 — Strong whole-school near misses

CHUNKS=DOC035-P0092-C001, DOC035-P0092-C002, DOC035-P0093-C001, DOC035-P0095-C001, DOC035-P0096-C001, DOC035-P0098-C001, DOC035-P0099-C001, DOC035-P0100-C001, DOC035-P0101-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / INTENDED_OUTCOME / IMPLEMENTATION_GUIDANCE

Pages 92–93 summarize research support/possible benefits for democratic school environments; page 98 explicitly introduces its increases in empathy/cooperation/civic-mindedness as examples of possible benefits. Pages 99–100 describe implementing/evaluating an action plan. Pages 100–101 summarize research associations with civic knowledge, values, engagement and future democratic activity. The corpus does not supply a reported measured change in participation after an identified RFCDC implementation in these passages. General support/association and possible benefits must not be relabeled as such a result.

#### T029-N10 — Training can increase complex thinking

CHUNKS=DOC035-P0115-C001
PASSAGE_CLASSIFICATION=EMPIRICAL_REALIZED_OUTCOME

The source explicitly reports that training has been found to significantly increase complexity of thinking about social issues. This is a genuine positive empirical outcome claim, not a mere recommendation. Its endpoint is thinking complexity, not measured democratic participation, and it is not reported as an RFCDC implementation effect. It therefore does not answer the candidate.

#### T029-N11 — EDC/HRE research and competence alignment

CHUNKS=DOC035-P0118-C001, DOC035-P0119-C001, DOC035-P0119-C002, DOC035-P0120-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS

The text says research favours whole-school delivery of EDC/HRE and summarizes outcomes/associations for open classroom climate, rights-respecting ethos, service learning and school councils. It notes alignment of resilience-building competences with RFCDC and future democratic activity. It does not report measured participation improvement after identified implementation of the RFCDC model or descriptors. Shared competences cannot establish intervention attribution by inference.

#### T029-N12 — References to evaluation/empirical publications

CHUNKS=DOC035-P0102-C001, DOC035-P0123-C001, DOC035-P0124-C001, DOC035-P0125-C001, DOC033-P0081-C001, DOC033-P0082-C001, DOC033-P0083-C001, DOC033-P0084-C001, DOC033-P0085-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS

References include evaluations and research on rights-respecting schools, democratic education, civic engagement and related topics. A title/citation is not the findings of that study. Linked materials outside the frozen corpus were not opened; their results cannot be imported into the answer.

#### T029-N13 — Corpus-wide off-framework checks

CHUNKS=DOC032-P0007-C001, DOC032-P0007-C002, DOC032-P0011-C001, DOC032-P0011-C002, DOC032-P0025-C001, DOC032-P0025-C002, DOC032-P0036-C001, DOC032-P0036-C002, DOC032-P0088-C001, DOC032-P0088-C002, DOC032-P0095-C001, DOC032-P0095-C002, DOC032-P0096-C001, DOC032-P0116-C001, DOC032-P0116-C002, DOC032-P0117-C001, DOC032-P0117-C002, DOC032-P0119-C001, DOC032-P0119-C002, DOC032-P0120-C001, DOC032-P0120-C002, DOC036-P0002-C001, DOC036-P0002-C002, DOC036-P0003-C001, DOC036-P0003-C002, DOC036-P0011-C001, DOC036-P0011-C002, DOC036-P0012-C001, DOC036-P0012-C002, DOC036-P0013-C001, DOC036-P0013-C002, DOC037-P0014-C001, DOC037-P0052-C001, DOC037-P0052-C002, DOC037-P0055-C001, DOC037-P0055-C002, DOC038-P0005-C001, DOC038-P0006-C001, DOC038-P0006-C002, DOC038-P0007-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / INTENDED_OUTCOME / FRAMEWORK_DEFINITION / IMPLEMENTATION_GUIDANCE

DigComp contains actual digital-skills baselines and stakeholder-use percentages, intended citizenship learning outcomes and research-review descriptions; the Council Recommendation mentions RFCDC and citizenship competence; UNESCO reports actual contextualisation, national teacher-competence measurement and course implementation; the Declaration contains participation/rights commitments. These are different frameworks, endpoints, populations or normative evidence. No RFCDC implementation-linked measured participation improvement is reported in them. All other chunks, including generic definition/skills lists and non-results front matter, remain in the complete ledger.

### Corpus-wide sufficiency and ambiguity

CORPUS_WIDE_SUFFICIENCY=INSUFFICIENT_FOR_REQUESTED_IMPLEMENTATION_LINKED_REALIZED_IMPROVEMENT
SUFFICIENT_REQUESTED_OUTCOME_CHUNKS=0

The nearest genuine empirical observations concern descriptor development/scaling, cooperative-learning/conflict outcomes, complex-thinking training and other-framework statistics. The closest participation-related research summaries concern school environments/EDC/HRE and general associations or future engagement. Neither those passages nor their combination provides a reported measured participation improvement after identified RFCDC competence/descriptor implementation. The evidence is not dismissed merely because it lacks a numerical percentage; entity, intervention, endpoint and realised-change bindings are missing.

AMBIGUITY_ASSESSMENT=The question leaves settings, learner population, participation measure and implementation period open. “Measured improvement” could include quantified or systematically reported qualitative change; it is not restricted to a percentage or a controlled trial. “RFCDC competences or descriptors” must not be broadened to any earlier pedagogy sharing similar competences. Strong general research summaries could tempt that unsupported attribution. The unchanged candidate should receive researcher scrutiny on this interpretation, but no alternative complete empirical answer is supported for the literal requested scope.
TEMPORAL_SCOPE_ASSESSMENT=According to the frozen corpus, with implementation preceding the reported change; no current-world fact or cutoff is added. Later evidence outside the corpus is not inferred absent.
ACTOR_SCOPE_ASSESSMENT=Learners in educational settings; practitioner counts, teacher training, institutional curriculum adoption and framework-development participants are different measures.
PARTIAL_EVIDENCE_ASSESSMENT=Real empirical validation and adjacent pedagogical research remain explicitly disclosed. Proficiency items, possible benefits and future engagement cannot serve as realised participation improvement.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED; open measure/population/period and attribution boundary retained as human-review qualifications.

REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the reported realised improvement in learners' democratic participation after RFCDC implementation. Competence/descriptors, implementation and assessment guidance, and descriptor-validation data do not establish that participation change.

Audit citations above support researcher review of absence and are not positive reference-evidence bindings. No benchmark task file is created.

## T030

TASK_ID=T030
TASK_TYPE=insufficient_evidence

### Exact question

According to the frozen UC3 corpus, what proportion of educational
organisations implementing DigCompOrg had adopted learning-analytics
governance policies, and what measured effect did this have on learner
retention or learning outcomes?

### Materially plausible near misses and empirical counterchecks

#### T030-N01 — Closest analytics/governance provision

CHUNKS=DOC040-P0021-C001, DOC040-P0028-C001, DOC040-P0028-C002, DOC040-P0029-C001
PASSAGE_CLASSIFICATION=FRAMEWORK_PROVISION / ANALYTICS_POLICY_RECOMMENDATION / INTENDED_ANALYTICS_USE

The overview and Assessment Practices table identify analytics strategy, a code of practice before implementation, safe data collection/validation/storage/aggregation/analysis/reporting, feedback and aggregate course/quality/retention uses. Page 28 establishes the genre as measures learning organisations may consider. Page 29’s “organisation has” wording belongs to descriptors, not an adoption survey. It supplies neither a numerator/denominator of adopters nor a measured retention/learning effect. Intended uses on the same page are not results.

#### T030-N02 — Explicit publication-stage limitation

CHUNKS=DOC040-P0038-C001, DOC040-P0038-C002
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS

DOC040-P0038-C001 states that DigCompOrg remains a conceptual framework and has not yet been piloted nor implemented in real settings, despite a mixed-method development process. Proposed later SAQ testing/adaptation is future work. This supports the scope of the absence finding at publication; it does not establish zero adopters or zero effect at a later date or everywhere outside the frozen corpus.

#### T030-N03 — Development methods, monitoring and adaptation

CHUNKS=DOC040-P0010-C001, DOC040-P0011-C001, DOC040-P0013-C001, DOC040-P0013-C002, DOC040-P0014-C001, DOC040-P0014-C002, DOC040-P0015-C001, DOC040-P0016-C001, DOC040-P0016-C002, DOC040-P0018-C001, DOC040-P0024-C001, DOC040-P0036-C001, DOC040-P0036-C002, DOC040-P0037-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / IMPLEMENTATION_GUIDANCE

Literature/expert mapping examines existing frameworks and SAQs; the analysis template has an Impact field for qualitative/quantitative outputs. The framework calls for measurable targets, reviewing implementation outcomes/impact and evaluating pilots, and discusses sector-specific adaptation. These are methodological inputs or evaluation provisions, not completed DigCompOrg analytics-policy adoption/outcome observations.

#### T030-N04 — Observed Vensters uptake proportions

CHUNKS=DOC040-P0017-C001, DOC040-P0072-C001
PASSAGE_CLASSIFICATION=ADOPTION_RATE

The report gives 88% of primary schools and more than 95% of secondary schools participating in Vensters, and centralized data at 100% in the fact sheet. These genuine rates refer to a Dutch accountability/transparency tool, not adoption of learning-analytics governance policies by DigCompOrg implementers. No measured retention/learning effect of the requested policy adoption is supplied. The 100% target elsewhere is a separate coverage aim, not an adoption observation.

#### T030-N05 — Other-tool response/coverage figures

CHUNKS=DOC040-P0059-C002, DOC040-P0069-C002
PASSAGE_CLASSIFICATION=ADOPTION_RATE

eLEMER reports over 700 schools responding annually, about half returning, against about 5,800 schools in Hungary. Opeka reports 151 municipalities out of 330, 1,267 schools out of 2,800, and 13,540 respondents out of 50,000. These observed fractions/counts are retained without calculating new percentages. They measure use/response for other tools, not DigCompOrg analytics-policy adoption, and do not provide the requested measured learner effect.

#### T030-N06 — Targets, scales, courses and pilot counts

CHUNKS=DOC040-P0016-C001, DOC040-P0016-C002, DOC040-P0059-C001, DOC040-P0059-C002, DOC040-P0060-C001, DOC040-P0062-C001, DOC040-P0063-C001, DOC040-P0065-C001, DOC040-P0067-C001, DOC040-P0074-C001, DOC040-P0074-C002
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / ADOPTION_RATE

eLEMER suggests responses from two-thirds of teachers and 50% of students; a coverage target of 100% is not an observed adoption rate. Ae-MoYS gives 114 action-plan submissions, no e-maturity submission record, and expected 100 Cypriot/2,000 European schools. Jisc’s 80% claim concerns leaders attending LFHE courses, not institutions adopting analytics policies. School Mentor lacks demo figures; LIKA reports pilot schools from 18 municipalities and a nationwide target. Indicative percentages/questionnaire scales are measurements to be collected or tool properties, not the requested observed proportion and effect.

#### T030-N07 — Full comparative fact-sheet context

CHUNKS=DOC040-P0051-C001, DOC040-P0052-C001, DOC040-P0053-C001, DOC040-P0053-C002, DOC040-P0054-C001, DOC040-P0055-C001, DOC040-P0056-C001, DOC040-P0057-C001, DOC040-P0057-C002, DOC040-P0058-C001, DOC040-P0061-C001, DOC040-P0061-C002, DOC040-P0064-C001, DOC040-P0066-C001, DOC040-P0066-C002, DOC040-P0068-C001, DOC040-P0069-C001, DOC040-P0069-C002, DOC040-P0070-C001, DOC040-P0071-C001, DOC040-P0072-C001, DOC040-P0072-C002, DOC040-P0073-C001, DOC040-P0075-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / ADOPTION_RATE

The annex identifies each separate framework/tool, its purpose, stakeholders, dates, questions, access, uptake and policy links. Potential impact or school-improvement language is a purpose/claim, not a measured retention/learning effect of DigCompOrg analytics governance. These fact sheets explain why actual counts in the corpus cannot be reassigned to DigCompOrg. Counts/ratios and targets are distinguished at passage level; primary ledger labels may summarize a mixed chunk.

#### T030-N08 — DigCompEdu analysis, policies and measurement definition

CHUNKS=DOC039-P0007-C001, DOC039-P0021-C001, DOC039-P0025-C001, DOC039-P0038-C001, DOC039-P0039-C001, DOC039-P0048-C001, DOC039-P0049-C001, DOC039-P0064-C001, DOC039-P0065-C001, DOC039-P0066-C001, DOC039-P0067-C001, DOC039-P0089-C001, DOC039-P0091-C001, DOC039-P0091-C002
PASSAGE_CLASSIFICATION=INTENDED_ANALYTICS_USE / FRAMEWORK_PROVISION / OTHER_NEAR_MISS

Educator competencies require critically analysing learner evidence, identifying at-risk learners, adapting support and innovating evidence-generation/learning-analytics approaches. These are proficiency statements (including first-person “I” rubrics), not a sample of measured educators/organisations. The glossary defines learning analytics using measurement/collection/analysis/reporting, but a measurement definition is not an outcome estimate. General references to companion frameworks provide no requested adoption rate.

#### T030-N09 — UNESCO technology potential, engagement statistics and actual use histories

CHUNKS=DOC037-P0014-C001, DOC037-P0017-C001, DOC037-P0017-C002, DOC037-P0019-C001, DOC037-P0019-C002, DOC037-P0020-C001, DOC037-P0020-C002, DOC037-P0045-C001, DOC037-P0049-C001, DOC037-P0049-C002, DOC037-P0050-C001, DOC037-P0050-C002, DOC037-P0051-C001, DOC037-P0052-C001, DOC037-P0052-C002, DOC037-P0053-C001, DOC037-P0054-C001, DOC037-P0055-C001, DOC037-P0055-C002, DOC037-P0056-C001, DOC037-P0056-C002, DOC037-P0057-C001, DOC037-P0058-C001
PASSAGE_CLASSIFICATION=INTENDED_ANALYTICS_USE / OTHER_NEAR_MISS

VR subject-matter retention language is a claimed potential/learning benefit, not organisation retention data. Teachers are advised to consider LMS/AI diagnostic statistics for engagement. Actual ICT CFT contextualisation, national teacher-profile measurement and course implementation concern UNESCO, not DigCompOrg analytics-governance uptake. Neither the adoption proportion nor the requested measured effect can be derived from those passages.

#### T030-N10 — Other statistics, policy uses and retention homonyms

CHUNKS=DOC032-P0007-C001, DOC032-P0007-C002, DOC032-P0011-C001, DOC032-P0011-C002, DOC032-P0012-C001, DOC032-P0012-C002, DOC032-P0012-C003, DOC032-P0013-C001, DOC032-P0013-C002, DOC032-P0023-C001, DOC032-P0023-C002, DOC032-P0025-C001, DOC032-P0025-C002, DOC032-P0027-C001, DOC032-P0027-C002, DOC032-P0106-C001, DOC032-P0106-C002, DOC032-P0107-C001, DOC032-P0107-C002, DOC032-P0116-C001, DOC032-P0116-C002, DOC032-P0117-C001, DOC032-P0117-C002, DOC032-P0119-C001, DOC032-P0119-C002, DOC032-P0120-C001, DOC032-P0120-C002, DOC036-P0002-C001, DOC036-P0002-C002, DOC036-P0012-C001, DOC036-P0012-C002, DOC036-P0013-C001, DOC036-P0013-C002, DOC038-P0006-C001, DOC038-P0006-C002, DOC038-P0007-C001
PASSAGE_CLASSIFICATION=OTHER_NEAR_MISS / IRRELEVANT

Digital-skills baselines, percentages of framework statements and stakeholder prior DigComp use (70%) concern other populations/measures. Council guidance about SELFIE and digital capacity is not an observed DigCompOrg policy-adoption survey. Data-retention periods and unlawful retention of activity records concern personal-data storage, not learner retention. These off-framework or lexical near misses were checked across the remaining corpus, without importing external implementation results.

### Corpus-wide sufficiency and ambiguity

CORPUS_WIDE_SUFFICIENCY=INSUFFICIENT_FOR_REQUESTED_ADOPTION_RATE_AND_MEASURED_EFFECT
SUFFICIENT_DIGCOMPORG_POLICY_ADOPTION_PROPORTION_CHUNKS=0
SUFFICIENT_DIGCOMPORG_POLICY_MEASURED_EFFECT_CHUNKS=0

Neither component is reported for the requested DigCompOrg analytics-governance implementation. The closest exact-topic text is a normative table and intended-use description; the same document explicitly remained conceptual/not yet piloted at publication. The genuine adoption figures belong to other named tools. Other corpus documents contain different-framework implementation, learner/teacher statistics, intended analytics competences or data-retention meanings. Combining those sources cannot create a DigCompOrg adoption denominator or measured effect. The finding is insufficiency, not a zero adoption rate or zero effect.

AMBIGUITY_ASSESSMENT=No country, sector, sampling frame, period or operational definition of adoption is specified. A proportion requires an observed implementer population and policy-adoption measure, and the outcome clause requires related measured retention/learning evidence. “Effect” is not silently strengthened to randomized causal identification; reported measured related outcomes could qualify. Even broad interpretations supply no complete frozen-corpus answer. Questionnaire participation, target coverage and student-data retention are explicitly excluded. The unchanged question remains for researcher review.
TEMPORAL_SCOPE_ASSESSMENT=Frozen-document reports only. The 2015 conceptual-status statement is preserved as publication-stage evidence and is not extrapolated to a current real-world non-adoption claim.
ACTOR_SCOPE_ASSESSMENT=Educational organisations implementing DigCompOrg; learners are the outcome population. Other tools, individual teachers, leaders attending courses and municipalities answering another survey are not the requested implementer population.
PARTIAL_EVIDENCE_ASSESSMENT=Other-tool observed proportions are present and retained; targets/scales are separate. No partial DigCompOrg adoption/effect observation was found that could legitimately provide either requested component.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED; population/period/adoption-definition qualifications retained for human review.

REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the proportion of DigCompOrg implementers adopting learning-analytics governance policies or the measured effect on learner retention or learning outcomes. Framework policy provisions and intended analytics uses are not observed adoption and outcome results.

Audit citations above support researcher review of absence and are not positive reference-evidence bindings. No benchmark task file is created.

## Classification counts and interpretation

One primary classification per canonical chunk per task. Counts include repeated/overlapping windows and must not be interpreted as independent studies or independent near-miss claims. The detailed passage catalogue can show additional classes within a mixed chunk.

| T029 classification | Canonical chunks |
| --- | ---: |
| FRAMEWORK_DEFINITION | 117 |
| DESCRIPTOR | 37 |
| ASSESSMENT_GUIDANCE | 47 |
| IMPLEMENTATION_GUIDANCE | 96 |
| INTENDED_OUTCOME | 14 |
| EMPIRICAL_REALIZED_OUTCOME | 3 |
| OTHER_NEAR_MISS | 75 |
| IRRELEVANT | 461 |

| T030 classification | Canonical chunks |
| --- | ---: |
| FRAMEWORK_PROVISION | 44 |
| ANALYTICS_POLICY_RECOMMENDATION | 1 |
| INTENDED_ANALYTICS_USE | 14 |
| IMPLEMENTATION_GUIDANCE | 4 |
| ADOPTION_RATE | 4 |
| MEASURED_OUTCOME | 0 |
| OTHER_NEAR_MISS | 98 |
| IRRELEVANT | 685 |

T029 EMPIRICAL_REALIZED_OUTCOME deliberately retains actual outcome claims for cooperative-learning/conflict and complex-thinking training even though the requested participation/intervention binding fails. Its nonzero count does not make T029 answerable. T030 ADOPTION_RATE deliberately retains other-tool observed uptake/fraction data; its nonzero count does not establish DigCompOrg analytics-policy adoption. OTHER_NEAR_MISS includes genuine empirical process/baseline/association information, not an assertion that all such material is hypothetical.

## Complete 850-chunk classification and scan ledger

Every canonical chunk occurs exactly once below in document_id / physical-page / C-ordinal order. Family flags refer to the exact regex definitions above; reason codes refer to the content/scope audit key below. The SHA256 is of the original chunk TEXT encoded UTF-8, not the scan-normalized text. Physical page and page_id identify the native source unit.

| Reason code | Meaning |
| --- | --- |
| X | Front matter, publisher/contact details, references without findings, or source content outside the requested framework/measure; no requested empirical result. |
| F | Competence concepts/model or normative definitions; no reported implementation-linked improvement. |
| D | Observable proficiency descriptor/example; describes an ability, not an observed change after implementation. |
| A | Assessment/observation/scaling guidance; a way of measuring is not a reported outcome of implementation. |
| I | Curriculum, pedagogical, teacher-education or whole-school implementation guidance/examples; no reported requested participation improvement. |
| N | Intended outcomes or possible benefits; not observed implementation outcomes. |
| V | Empirical descriptor development/validation/scaling and practitioner feedback; empirical data exist, but concern instrument development, not improved participation. |
| B | Actual baseline/statistics or implementation/development reports for a different framework, population or endpoint; no RFCDC implementation-linked participation improvement. |
| C | Reported cooperative-learning/conflict or complex-thinking effects; empirical outcome claims retained, but no reported measured democratic-participation change after RFCDC implementation. |
| S | Research-based general association/benefit summary for EDC/HRE or whole-school environments, not a reported measured change after identified RFCDC implementation. |
| Q | Cited evaluation/study title or off-corpus reference; the frozen passage gives no requested result, and linked sources were not followed. |
| K | DigCompOrg framework/descriptor provision or concept; descriptive grammatical tense does not turn a framework indicator into surveyed practice. |
| P | Learning-analytics code/data governance recommended as a framework provision, not an observed adoption proportion. |
| T | Intended analytics use for feedback, quality/course design or retention/outcomes; no measured effect reported. |
| J | Implementation/adaptation/self-assessment guidance; not observed DigCompOrg policy uptake plus outcome evidence. |
| R | Observed uptake proportion, recurrence fraction or numerator/denominator for another tool; neither DigCompOrg analytics-policy adoption nor its measured learner effect. |
| W | Other-tool fact sheet, pilot counts, targets, recommended response shares, scales, course-attendance figures, development data or qualitative purpose; wrong entity/measure and no joint requested evidence. |
| Z | Source explicitly says DigCompOrg remained conceptual and had not yet been piloted/implemented at publication; no adoption/outcome results. |

| Chunk ID | Source/page unit | Words | T029 families | T030 families | T029 primary class / reason | T030 primary class / reason | Original text SHA256 |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| DOC032-P0001-C001 | DOC032-P0001 / 1 | 16 | DE | RE | IRRELEVANT / X | IRRELEVANT / X | 3b9eb616be400e5b12bbfcee6368872dba070aa9a929191ba4471ec645439e00 |
| DOC032-P0002-C001 | DOC032-P0002 / 2 | 368 | IDOE | APIRE | IRRELEVANT / X | IRRELEVANT / X | 1534538dfe1abc970e33644e75e3f455ec6dae7db6613d82f3adf3f4399c9699 |
| DOC032-P0003-C001 | DOC032-P0003 / 3 | 150 | LIDO | IURO | IRRELEVANT / X | IRRELEVANT / X | 1984f272ebbc307649ebf8a247f87376c2c9b43b743cdd05dac5e27df1a4e4a6 |
| DOC032-P0004-C001 | DOC032-P0004 / 4 | 253 | PLIDO | PIGURO | IRRELEVANT / X | IRRELEVANT / X | ff6c7bd57e268aa0fa100e298388072c8f46968ba467876a4d6bf1d32db20d99 |
| DOC032-P0005-C001 | DOC032-P0005 / 5 | 332 | PLIDAOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | 5fa662160fb5056a9085a3c4d387c92c0569042913e38a61d95ef31b1269a190 |
| DOC032-P0006-C001 | DOC032-P0006 / 6 | 450 | PLIE | IGURE | IRRELEVANT / X | IRRELEVANT / X | 0dc86d9d170348818555ee20b08450fb4e9533171028fd6715bf8be50ffc9d8e |
| DOC032-P0006-C002 | DOC032-P0006 / 6 | 159 | L | GUR | IRRELEVANT / X | IRRELEVANT / X | 0c701b87688632ba42cb14b3cd23ef76df8ad605e0e83cb9910099633b53bd28 |
| DOC032-P0007-C001 | DOC032-P0007 / 7 | 450 | LIDAOE | APIGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 5600370cdea9cd8bb3d83d713cce716c9f2d9dabbea4bfbfdfed2ffd4348e6a9 |
| DOC032-P0007-C002 | DOC032-P0007 / 7 | 292 | PLDOE | APUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 5143bc28a1eb09357c389a7b44383406e71ba893bbc539ada33335781b6f37f0 |
| DOC032-P0008-C001 | DOC032-P0008 / 8 | 132 | LDO | RO | IRRELEVANT / X | IRRELEVANT / X | 80dadfd77c8d655fe36e399ababd1d7c140df37452315fa4b26ca48364a1d6e3 |
| DOC032-P0009-C001 | DOC032-P0009 / 9 | 5 | - | R | IRRELEVANT / X | IRRELEVANT / X | 02bdfeb03ab79c8d75ef4de76678ef5f97df26feb18151b300d68c10953d96bf |
| DOC032-P0010-C001 | DOC032-P0010 / 10 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | cd7eeccdf944bc35c7dcd9296b31aa1e0e8d543fe1d47a63fa770cecfee9d930 |
| DOC032-P0011-C001 | DOC032-P0011 / 11 | 450 | PLDOE | APGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | b14e52fd4e1485702b4bf93d3f304cbc764d798dcf09acfe314779e5995e438a |
| DOC032-P0011-C002 | DOC032-P0011 / 11 | 107 | DOE | APURE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 16c1a60d2a8aecc970cb1552a98826175b602288ec67c487c07481d408101752 |
| DOC032-P0012-C001 | DOC032-P0012 / 12 | 450 | PLDOE | APGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | f0667dbc0dc7fe6e213fe8f1f61543abbc98e1a398b0dec171dec9d60bca4fd9 |
| DOC032-P0012-C002 | DOC032-P0012 / 12 | 450 | PLIDO | IGURO | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 6060395b424783c1cac309bc1a68f87c99a10426ee3c60f6f45ced041c68d3a4 |
| DOC032-P0012-C003 | DOC032-P0012 / 12 | 83 | LIO | IGURO | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 1c0dc89c985216a08b9753f59fcf9726bb5f6270b71c649249bc1cb719988acf |
| DOC032-P0013-C001 | DOC032-P0013 / 13 | 450 | FPLIDAE | APGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 6be6bc55fc1eacfa3effccd204d56eb111ceca4911f736587e1b485824836e98 |
| DOC032-P0013-C002 | DOC032-P0013 / 13 | 293 | PLDOE | AGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 52d7883d4e5f93c289e46aa2db9278d46f6df383c02cb881316db1d032a85cfd |
| DOC032-P0014-C001 | DOC032-P0014 / 14 | 450 | LIDOE | APIGRO | IRRELEVANT / X | IRRELEVANT / X | e0e23c1e0607385517f8e250ac277619992e2bdb4c57e4e3fc8afad92a695712 |
| DOC032-P0014-C002 | DOC032-P0014 / 14 | 119 | IDE | APIURE | IRRELEVANT / X | IRRELEVANT / X | 97024dfe9e13a7dda10373356d15bf7f6db8e2d5b033bd6cce960cde8a86c3e3 |
| DOC032-P0015-C001 | DOC032-P0015 / 15 | 97 | LID | PIRO | IRRELEVANT / X | IRRELEVANT / X | 33efe30b1b44ba93177245f6f8e0e4dab8651ce69e639334fb5f8571ba1b24de |
| DOC032-P0016-C001 | DOC032-P0016 / 16 | 8 | - | R | IRRELEVANT / X | IRRELEVANT / X | 2049cd3f2d0d719354b1881ea8d60bece8639d80caa6aba9f9babaf77dd672c1 |
| DOC032-P0017-C001 | DOC032-P0017 / 17 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | f3bc557a487146edeac4266455cb759239cacac836c5a00e4c3381be43990a8c |
| DOC032-P0018-C001 | DOC032-P0018 / 18 | 450 | PLIDOE | AIGURO | IRRELEVANT / X | IRRELEVANT / X | 36fa2105d638fe2fd806ddf99edc25630747f2ff4146b78454f706e43ab1a5f8 |
| DOC032-P0018-C002 | DOC032-P0018 / 18 | 84 | LDO | URO | IRRELEVANT / X | IRRELEVANT / X | 303ee9742a045476f59159e0f1c1bf2f9d48be0d62cea0490eced900d0815e35 |
| DOC032-P0019-C001 | DOC032-P0019 / 19 | 235 | PDAE | APURE | IRRELEVANT / X | IRRELEVANT / X | 42a086515f97ce5a3407619a2784600ca30827eef6097a0af7da6953fc8b129f |
| DOC032-P0020-C001 | DOC032-P0020 / 20 | 450 | PIDAE | AIGURE | IRRELEVANT / X | IRRELEVANT / X | b7c417ea96ae771ba31be3959201e3c4a43a213776fd243a99a7b10b42d35c6d |
| DOC032-P0020-C002 | DOC032-P0020 / 20 | 96 | E | AR | IRRELEVANT / X | IRRELEVANT / X | e681af1dfdd902e00b034d0cf9e1279e12b15393f2ff6fe4128002ea0416a0af |
| DOC032-P0021-C001 | DOC032-P0021 / 21 | 450 | IDAOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | 1c6e69916256d628b94fc4d5c16b574ae3c73dfe6bb7f55babb455b882af7767 |
| DOC032-P0021-C002 | DOC032-P0021 / 21 | 113 | IOE | AIURO | IRRELEVANT / X | IRRELEVANT / X | 9108f3bf52caa967d49c2fb233b3aeadcb640c03cd8f2ed946d93dbc41a21e1a |
| DOC032-P0022-C001 | DOC032-P0022 / 22 | 270 | PLDAO | UROE | IRRELEVANT / X | IRRELEVANT / X | 1b74c90158a4049fa0b73b93d31c61081591722b2c8d70b111bd16e96f746a9a |
| DOC032-P0023-C001 | DOC032-P0023 / 23 | 450 | PLIDAOE | IUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | ff3a5c81f338ac6f704d76f781e411110c9d847cb979333965ebb8f8ee30d33c |
| DOC032-P0023-C002 | DOC032-P0023 / 23 | 206 | LDO | GURO | IRRELEVANT / X | OTHER_NEAR_MISS / W | df5df767d0b977c46b94c31c8bacbdffc66cb5461bf081a4769d12f942b0011f |
| DOC032-P0024-C001 | DOC032-P0024 / 24 | 450 | PLIDOE | PIUROE | IRRELEVANT / X | IRRELEVANT / X | da744c98c1942235d5fab34376a521ae5f995ee51232ece107ca8a7f2b193c6e |
| DOC032-P0024-C002 | DOC032-P0024 / 24 | 178 | PLDE | UROE | IRRELEVANT / X | IRRELEVANT / X | 7b00efeef9e4d36ef9c3d053c984786ef1d2cacd3a2efdc5d697588297991da4 |
| DOC032-P0025-C001 | DOC032-P0025 / 25 | 450 | LIDAOE | PIGUROE | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | aa0a3e87a5a467d7dc0618e75e27e5077201f9f761f51a1633d0cb62fd0b9ae9 |
| DOC032-P0025-C002 | DOC032-P0025 / 25 | 108 | LIDO | PIURO | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | 09ec5564ced91a8e5f95daf876e187cde5b1f7af4951798d9e4c4638cbdc14a3 |
| DOC032-P0026-C001 | DOC032-P0026 / 26 | 450 | LIDOE | PIUROE | IRRELEVANT / X | IRRELEVANT / X | 2b98c2d43f660c28ec6839191c5ff2047242d3371aa34c86308e228f60915c87 |
| DOC032-P0026-C002 | DOC032-P0026 / 26 | 94 | LDO | RO | IRRELEVANT / X | IRRELEVANT / X | 9220e36ba23f0b90c2694e8692951446377a71f06e72487c09ced2da67a823ff |
| DOC032-P0027-C001 | DOC032-P0027 / 27 | 450 | LIDOE | IROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 3e7f2ea2c693ae174d346c9fab441b6ec1d88e67d6c56ba022457d2bc0d0b3d5 |
| DOC032-P0027-C002 | DOC032-P0027 / 27 | 168 | OE | PROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 229fdc9a3f1a623761425863c1e8137234b612afe1d4807f6cdc7ae632c43656 |
| DOC032-P0028-C001 | DOC032-P0028 / 28 | 7 | - | R | IRRELEVANT / X | IRRELEVANT / X | 41eabfea7215bd7bca2ae77ddcbc938bc33f54495e9f831985f67405948e80f8 |
| DOC032-P0029-C001 | DOC032-P0029 / 29 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | e9a3aba0a660fc24de95b5602a4a6fc1e55db064ea6339382c1ab976ac6d7604 |
| DOC032-P0030-C001 | DOC032-P0030 / 30 | 450 | LIDAO | IGUROE | IRRELEVANT / X | IRRELEVANT / X | 9b630441bd54e782f4ed305590a7d7381c33d1fd1d754b0646fa8e30212201a0 |
| DOC032-P0030-C002 | DOC032-P0030 / 30 | 271 | LIDO | IRO | IRRELEVANT / X | IRRELEVANT / X | bb08488f1787d7f4424defdee72068e1d0bcd924e7fea6529d18bfe691cab5b9 |
| DOC032-P0031-C001 | DOC032-P0031 / 31 | 338 | LIDAO | IROE | IRRELEVANT / X | IRRELEVANT / X | bb116dab5bdd8824c32714919d5b9132b32b045728a75478a54fb71c1d900133 |
| DOC032-P0032-C001 | DOC032-P0032 / 32 | 450 | LDAOE | AUROE | IRRELEVANT / X | IRRELEVANT / X | 8679d75e3ef320af320b10b1c73627ea9ad5a826cb76d2d826f1c01c0f0ddaac |
| DOC032-P0032-C002 | DOC032-P0032 / 32 | 121 | LDAO | ROE | IRRELEVANT / X | IRRELEVANT / X | 1757f8587a30d60b0f3602b986be3650855a3acfeb468440b082a28c7137819f |
| DOC032-P0033-C001 | DOC032-P0033 / 33 | 422 | LIDAOE | AIGROE | IRRELEVANT / X | IRRELEVANT / X | 8fd8d9d1eec329ec75be2053d9f4dc83f3a3c899a8e6ef848efeaa4117c5519b |
| DOC032-P0034-C001 | DOC032-P0034 / 34 | 410 | LIDAO | IGURO | IRRELEVANT / X | IRRELEVANT / X | d8612545b97e4d15b2064775fa1bd00933a9ddce3b77479e150271e94390e0a6 |
| DOC032-P0035-C001 | DOC032-P0035 / 35 | 338 | LIDAOE | IROE | IRRELEVANT / X | IRRELEVANT / X | 6b313cd07ec82fe11d6c2121faa3c253dd54f6aeb7961f6bebb90d06daf3e428 |
| DOC032-P0036-C001 | DOC032-P0036 / 36 | 450 | PLIDAO | IUROE | INTENDED_OUTCOME / N | IRRELEVANT / X | b0855013304e597ee4d30a3cee2f3523faf1bbea98410c3c136fbc1ee06e441c |
| DOC032-P0036-C002 | DOC032-P0036 / 36 | 87 | PLDAO | UROE | INTENDED_OUTCOME / N | IRRELEVANT / X | b5fd83e5f1bc79a8ffe222c91a8206fa9da5f4af7ac4f41efe097d8ef8485753 |
| DOC032-P0037-C001 | DOC032-P0037 / 37 | 271 | PLDO | URO | IRRELEVANT / X | IRRELEVANT / X | c71d7f25810ad09fc3ca701afb0520765b1c67c710ce48e8975061dd55cfe813 |
| DOC032-P0038-C001 | DOC032-P0038 / 38 | 338 | LDOE | PUROE | IRRELEVANT / X | IRRELEVANT / X | 8e2b2158452804be87e221f8f3e250dd5331234f57a4d5af4294c856bbeb1eb2 |
| DOC032-P0039-C001 | DOC032-P0039 / 39 | 404 | LIDAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | be68651439c1f4dffdf162804964e35ae721ca1f5fb5d303719f17210500711f |
| DOC032-P0040-C001 | DOC032-P0040 / 40 | 381 | LIDAO | IRO | IRRELEVANT / X | IRRELEVANT / X | 7d28c1574ed78c2ef4d32f16b67ba111c25d1d752326a3b677bafe626495f721 |
| DOC032-P0041-C001 | DOC032-P0041 / 41 | 318 | LIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 7422eb03cb1265eb98fee28af797713a0eadfe722cd23fb25b92574f14232958 |
| DOC032-P0042-C001 | DOC032-P0042 / 42 | 387 | LIDAOE | APIRO | IRRELEVANT / X | IRRELEVANT / X | 3be8a4e3425e7737a5ffbf1e4dc2dca13fa675531d0573f741c3566e9e726ca6 |
| DOC032-P0043-C001 | DOC032-P0043 / 43 | 450 | LIDAE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 4ac7c273895fdf1ac39dedb207db36c8304c8a4f32dc377aa9c85008fedfaff2 |
| DOC032-P0043-C002 | DOC032-P0043 / 43 | 140 | LIDO | IRO | IRRELEVANT / X | IRRELEVANT / X | 7fc3e91c01453147e01f0caa2eee4e70216dd5152446ecc0089e85dfd4d8bab0 |
| DOC032-P0044-C001 | DOC032-P0044 / 44 | 332 | PLIDAO | IUROE | IRRELEVANT / X | IRRELEVANT / X | 648ccb1fb675738f4e15cae7cca669338f97db4772164880c8b4743e34519269 |
| DOC032-P0045-C001 | DOC032-P0045 / 45 | 449 | LIDAOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | ed55accd8ce2c6a5c51eb1543dee36b7d3b5e5909146f6668c5a485e3023b24e |
| DOC032-P0046-C001 | DOC032-P0046 / 46 | 450 | IAO | IURO | IRRELEVANT / X | IRRELEVANT / X | 2fd2cb7a75713fbc143015e2846902b7d7fb44a7a8546a6ec1becb3e504e0f75 |
| DOC032-P0046-C002 | DOC032-P0046 / 46 | 204 | LIDAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | f3c9fe4190ea58527083e05fe45c6c4239afb74b14377ee9862381426689a621 |
| DOC032-P0047-C001 | DOC032-P0047 / 47 | 363 | LIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | fad5c3c0e336175f0b812c0dfa0b03a7747ffc1c36fa5e867ab198d0a75e50f7 |
| DOC032-P0048-C001 | DOC032-P0048 / 48 | 249 | LIDO | IRO | IRRELEVANT / X | IRRELEVANT / X | 787f1f6d336570e057e519da75990a279fb2ea61079e4b95eea4dcd51f7cbc27 |
| DOC032-P0049-C001 | DOC032-P0049 / 49 | 311 | LDAO | UROE | IRRELEVANT / X | IRRELEVANT / X | 15274ae6092ed2b73b4c77c99c9e3d952c730f1d8b4e7743982b50912b2c2f41 |
| DOC032-P0050-C001 | DOC032-P0050 / 50 | 324 | PLIDO | IRO | IRRELEVANT / X | IRRELEVANT / X | b9637e65f69237a18507d7a3d26e30c33f9606ff172b8843169373bd3ec4572d |
| DOC032-P0051-C001 | DOC032-P0051 / 51 | 285 | PLDAO | URO | IRRELEVANT / X | IRRELEVANT / X | 2772f9b93fe4611899c34ad640fcc68a8ce0080bd75d4c8d861df57ae9b2ab49 |
| DOC032-P0052-C001 | DOC032-P0052 / 52 | 6 | - | R | IRRELEVANT / X | IRRELEVANT / X | a8fe2d1340ee96ff2f7c4bbb136ab6d2a723ab02c77af01f5d8d1a7d8173725d |
| DOC032-P0053-C001 | DOC032-P0053 / 53 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | 493857384b0225ca6aba62c5c597e5b170bc33e2656d3598a57ebc56dea50dae |
| DOC032-P0054-C001 | DOC032-P0054 / 54 | 106 | IDO | PGURO | IRRELEVANT / X | IRRELEVANT / X | 37eccadc8fb02b071ea2f8e8d06e3d4edaa342a837698b1037ba1c632e4aeda8 |
| DOC032-P0055-C001 | DOC032-P0055 / 55 | 420 | PLIDAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | 9519e2008d87a7818d101dc25e00a3ac1a2f41e0499c355a822e2e74e5e3d32c |
| DOC032-P0056-C001 | DOC032-P0056 / 56 | 450 | PLDAOE | AGROE | IRRELEVANT / X | IRRELEVANT / X | e406b8fef932e9d56c0615e643c413ad2bea4569aa9c7fa68a5e394cb3a13825 |
| DOC032-P0056-C002 | DOC032-P0056 / 56 | 93 | LDOE | AGRO | IRRELEVANT / X | IRRELEVANT / X | 0998ddb2568fd174e8f64404db943b2769da92b2ae28e9383362a288fc0ff23b |
| DOC032-P0057-C001 | DOC032-P0057 / 57 | 374 | PLIDOE | AIGROE | IRRELEVANT / X | IRRELEVANT / X | ca089c836a735b7fdd23f37f21f5cb2a97d9a9a70e231f42301d0299f0b41a43 |
| DOC032-P0058-C001 | DOC032-P0058 / 58 | 440 | LDAO | GROE | IRRELEVANT / X | IRRELEVANT / X | a24c6f98229c0c178a4fdf75264730e70d7df114ddf5e2ec83ac5f8c9c8ed839 |
| DOC032-P0059-C001 | DOC032-P0059 / 59 | 423 | PLIDAOE | IGUROE | IRRELEVANT / X | IRRELEVANT / X | b81b22c4f59bf62c416de51502abec8dd4d65cf2c3326266e29606c084aab8ce |
| DOC032-P0060-C001 | DOC032-P0060 / 60 | 160 | LE | AGRE | IRRELEVANT / X | IRRELEVANT / X | 0ddf732eb910925245037bf9f666716d9dca59da53b39938f610889cbb2987b1 |
| DOC032-P0061-C001 | DOC032-P0061 / 61 | 310 | IOE | AIRE | IRRELEVANT / X | IRRELEVANT / X | c131a1c1fc676c7c4336adeb67ba499c778fe21a93c3a153360a186dfedcb9b1 |
| DOC032-P0062-C001 | DOC032-P0062 / 62 | 450 | LIDOE | AIGUROE | IRRELEVANT / X | IRRELEVANT / X | 2b0c8cfe508875c4cf36ad2c7f0290a9594f1b9111bf62dc38d2cc20d8257c26 |
| DOC032-P0062-C002 | DOC032-P0062 / 62 | 133 | I | IUR | IRRELEVANT / X | IRRELEVANT / X | bad58b40d65a2b4de101d537b16eb776ccd5d558ce2a56969c9f24d0c80d6143 |
| DOC032-P0063-C001 | DOC032-P0063 / 63 | 436 | LDAOE | APGROE | IRRELEVANT / X | IRRELEVANT / X | 8f5d13f4b67445825b4ceba1e618faeb7ee84e58c331d5739f44e12cdcc76bcb |
| DOC032-P0064-C001 | DOC032-P0064 / 64 | 450 | IAE | APIURE | IRRELEVANT / X | IRRELEVANT / X | ac460bf17e20c01e12d23321e3c7c584fe35f293c1d19e57225ad91a3b67e183 |
| DOC032-P0064-C002 | DOC032-P0064 / 64 | 104 | IE | AIURE | IRRELEVANT / X | IRRELEVANT / X | df683f43ef144a049d8f0d8be79d8eec5c98dfa1b774621102eb7f878e8963c3 |
| DOC032-P0065-C001 | DOC032-P0065 / 65 | 450 | PLIOE | AIGUROE | IRRELEVANT / X | IRRELEVANT / X | a339140c77eb1feb0e79b6bceceee6765958636cc6987d1559595596df268871 |
| DOC032-P0065-C002 | DOC032-P0065 / 65 | 82 | O | R | IRRELEVANT / X | IRRELEVANT / X | fd853d8ce5c73ed39ad98954b82616134b2b916e1b18d53d3c4190d90bbbde4e |
| DOC032-P0066-C001 | DOC032-P0066 / 66 | 450 | PLDE | APGURE | IRRELEVANT / X | IRRELEVANT / X | 6b66dc7fc1a4facc4bd0f34a295033568a3cc3d8508d7b22e319302eed44c141 |
| DOC032-P0066-C002 | DOC032-P0066 / 66 | 115 | PLD | PGUR | IRRELEVANT / X | IRRELEVANT / X | 1c459af9c9479884c2dfe3c6526f33a3431b1b2eeb760a557717bfabdc465d5d |
| DOC032-P0067-C001 | DOC032-P0067 / 67 | 441 | PLOE | APGUROE | IRRELEVANT / X | IRRELEVANT / X | 8033a100c2e5ea8cff57b594a6e37e9acec40a12d14b85be59faa525c6e334a3 |
| DOC032-P0068-C001 | DOC032-P0068 / 68 | 450 | PLIOE | AIGUROE | IRRELEVANT / X | IRRELEVANT / X | d959a228c569d52917711fafc32a934140089c7362f3d834c87c2f812399918a |
| DOC032-P0068-C002 | DOC032-P0068 / 68 | 92 | PLIOE | IUROE | IRRELEVANT / X | IRRELEVANT / X | b5a2b0bdd0c17acf00c7202a0317b35868d999d666fdcb124876b94271ede280 |
| DOC032-P0069-C001 | DOC032-P0069 / 69 | 450 | LIOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | aa030f4707aaaaff9f877698857262a023fae52bc6cfa1fd7a771cb02e560096 |
| DOC032-P0069-C002 | DOC032-P0069 / 69 | 142 | IE | AIR | IRRELEVANT / X | IRRELEVANT / X | 9ca9989af39ec549dc4516fb2fd127b9912a9cb014570c259ebd3a6ac058d26c |
| DOC032-P0070-C001 | DOC032-P0070 / 70 | 447 | LIOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | 015cdf1136c1009df80cb6f667713a0db639dae39e39db74c57021dbaa21ce78 |
| DOC032-P0071-C001 | DOC032-P0071 / 71 | 450 | IOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | 9a0e58b328082e6f569dde3e5998bf03b0090950b888137785d537e83d8c2959 |
| DOC032-P0071-C002 | DOC032-P0071 / 71 | 79 | E | APR | IRRELEVANT / X | IRRELEVANT / X | 8c4c823446563ce47f3fc4ddd07449c72e880fdeb20c0644fe9f0a7234285e93 |
| DOC032-P0072-C001 | DOC032-P0072 / 72 | 450 | PIDAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | 1c8ddde0e12a01bb2fab562928c133e31c5022edb0526ac126e2a746a9ba4daa |
| DOC032-P0072-C002 | DOC032-P0072 / 72 | 177 | POE | UROE | IRRELEVANT / X | IRRELEVANT / X | acefc0966bf1a9903cc9ea4ca1a04b6797c6e1a0cdd115e80316785055cad892 |
| DOC032-P0073-C001 | DOC032-P0073 / 73 | 450 | PLIDOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 295664399929e6574f6d2068b581e613c0015e45f95cafcc3820ea3beaeec5c5 |
| DOC032-P0073-C002 | DOC032-P0073 / 73 | 105 | PO | URO | IRRELEVANT / X | IRRELEVANT / X | 0defdcb5531fdcfaa71e92862e4cad42f078bd7c8444320b1ce35165df4a401c |
| DOC032-P0074-C001 | DOC032-P0074 / 74 | 450 | PLIDAOE | PIUROE | IRRELEVANT / X | IRRELEVANT / X | 1446bb8e5a5f5c4b45b3a431c4f44c52d333f70531aced2a0bf6185651b5c292 |
| DOC032-P0074-C002 | DOC032-P0074 / 74 | 119 | PL | URO | IRRELEVANT / X | IRRELEVANT / X | 038ab7a4538dfa8e915af3b1ae421d72907c30ef7dc3d8bb5c971b5973e527ff |
| DOC032-P0075-C001 | DOC032-P0075 / 75 | 297 | - | UR | IRRELEVANT / X | IRRELEVANT / X | e47e2b57bb8083b07eb36e575b8abdd1ecb2f80cc1f3be327068652ead43607f |
| DOC032-P0076-C001 | DOC032-P0076 / 76 | 271 | LIDO | PIRO | IRRELEVANT / X | IRRELEVANT / X | 06d413ab18c2687d97f4d5a6188a87d59ab8fe31c1159a492305d9cd01e14740 |
| DOC032-P0077-C001 | DOC032-P0077 / 77 | 4 | - | R | IRRELEVANT / X | IRRELEVANT / X | d46cadecd0deb15c79400357ceb91e416fc0371927fe417e6e494dca21d59276 |
| DOC032-P0078-C001 | DOC032-P0078 / 78 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | d17ebb270764281dec90da3822d306ebd83639ad0568fa9807565147ab432b1b |
| DOC032-P0079-C001 | DOC032-P0079 / 79 | 450 | LDOE | PROE | IRRELEVANT / X | IRRELEVANT / X | e5b47cab422d1bd040bc26395a4f0ce296064ff701dbb82063502174e4e2109e |
| DOC032-P0079-C002 | DOC032-P0079 / 79 | 272 | LIDOE | IROE | IRRELEVANT / X | IRRELEVANT / X | 5afa9eddfbbc517ec9eebf6b88e70fcbf80e62d52a2ae1d770a3cffd2b1855d4 |
| DOC032-P0080-C001 | DOC032-P0080 / 80 | 450 | IDAOE | AIGURE | IRRELEVANT / X | IRRELEVANT / X | 706b226519db6335613f2207c2169f71c4244314c4988b2bfadf63a5f064fc9e |
| DOC032-P0080-C002 | DOC032-P0080 / 80 | 251 | DAOE | AGRE | IRRELEVANT / X | IRRELEVANT / X | ddea17a7e1f0da7a4159596aa99f5c72307dca9f9dea3c78da5fd8fffd5080b0 |
| DOC032-P0081-C001 | DOC032-P0081 / 81 | 450 | PIDE | AIUR | IRRELEVANT / X | IRRELEVANT / X | 4afcfa2034511c31b1dc0ab1d97fafd3a5e3d0d54f7be476ad7bbf4646ece92e |
| DOC032-P0081-C002 | DOC032-P0081 / 81 | 382 | PDE | AUR | IRRELEVANT / X | IRRELEVANT / X | dbedf707fe676001fee350dd37d02022f379b830519d4eae2c538299d3f5fbfa |
| DOC032-P0082-C001 | DOC032-P0082 / 82 | 403 | IDO | IURO | IRRELEVANT / X | IRRELEVANT / X | a34de4bd4576120d1e564b9c42fead7cf7409f67dbdd34bb8c22fc0089f73a0d |
| DOC032-P0083-C001 | DOC032-P0083 / 83 | 450 | IDAOE | APIROE | IRRELEVANT / X | IRRELEVANT / X | d2e0a56af2252c6ebd3e97606ed9828f1f2b257a34a7f06b0afd7ce35ff57e73 |
| DOC032-P0083-C002 | DOC032-P0083 / 83 | 383 | IDOE | AIURO | IRRELEVANT / X | IRRELEVANT / X | 750dcd99c518e8063b59f56901e9e19141657b8da7fa557ea27f455fe9997419 |
| DOC032-P0084-C001 | DOC032-P0084 / 84 | 450 | PDAO | UROE | IRRELEVANT / X | IRRELEVANT / X | 1132869e33de8919386621e605f5edd7c350dd77d30110d8385841cd8eb1943f |
| DOC032-P0084-C002 | DOC032-P0084 / 84 | 362 | LDO | RO | IRRELEVANT / X | IRRELEVANT / X | ad8a18515712068ab42b7f48ebd4c933780b05641e5aa045ff25eeda4e0d37e0 |
| DOC032-P0085-C001 | DOC032-P0085 / 85 | 450 | PLIDAO | IUROE | IRRELEVANT / X | IRRELEVANT / X | 6ee805a4070134b8b7e97acdb5d39e9ff833e0bcb1853a02d0b65f0e07071af5 |
| DOC032-P0085-C002 | DOC032-P0085 / 85 | 123 | PLAO | UROE | IRRELEVANT / X | IRRELEVANT / X | fab24f6ecc664faa655c6b944b659f11ab0ca4a80bd2d8463d38e5344115c85a |
| DOC032-P0086-C001 | DOC032-P0086 / 86 | 297 | LIDO | IURO | IRRELEVANT / X | IRRELEVANT / X | 3d1e4a804030b8b0b6503a2d628763bd3c317efded24d5ea143cde4ed8ca184b |
| DOC032-P0087-C001 | DOC032-P0087 / 87 | 450 | PLIDAOE | IUROE | IRRELEVANT / X | IRRELEVANT / X | 1a34c39dc2d5676a73c7f5c40491ffac4eeb298b605679a8a32f1ff67afb8c4d |
| DOC032-P0087-C002 | DOC032-P0087 / 87 | 273 | LIDAO | IUROE | IRRELEVANT / X | IRRELEVANT / X | e3071476bdb952eb579f5d25a47a840e2deb15cfefd292b469ea8658860c7edd |
| DOC032-P0088-C001 | DOC032-P0088 / 88 | 450 | LIDAOE | IUROE | INTENDED_OUTCOME / N | IRRELEVANT / X | 644cbbe2b6756b733d85fafa7cdf9ae531dabcf0f318f6274712ad2d428a1903 |
| DOC032-P0088-C002 | DOC032-P0088 / 88 | 300 | LIDAOE | APIGUROE | INTENDED_OUTCOME / N | IRRELEVANT / X | 277b0526070a12b20a37015323a2de6c1601dddc272f13a4aa92865d0fe275fe |
| DOC032-P0089-C001 | DOC032-P0089 / 89 | 407 | LIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 1175147f944cc29b75367e3c34da921e989956058c3e57bb31b522baae4f5585 |
| DOC032-P0090-C001 | DOC032-P0090 / 90 | 422 | LIDAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | e3cb8ab952b954cc4211274728d55a74ef2021d3c88520dec5a0391711af1edf |
| DOC032-P0091-C001 | DOC032-P0091 / 91 | 437 | LDAOE | AGROE | IRRELEVANT / X | IRRELEVANT / X | e07f947a29fd8cfe0b09bbf2325be7540b9f40aeb7998871dac5da24f6c3718d |
| DOC032-P0092-C001 | DOC032-P0092 / 92 | 450 | IE | AIGRE | IRRELEVANT / X | IRRELEVANT / X | 51fc0655891c040c3d5cae08a575392fcc2d19d9a8434520a38e8635a2b07735 |
| DOC032-P0092-C002 | DOC032-P0092 / 92 | 158 | IOE | AIRO | IRRELEVANT / X | IRRELEVANT / X | 78fe49be675ee81fe54f54306de81f8cbfc1c93b627f0f163263193daf9c1a61 |
| DOC032-P0093-C001 | DOC032-P0093 / 93 | 430 | LDO | URO | IRRELEVANT / X | IRRELEVANT / X | 405afd36684f3b4e518bb3c4909014ee1b9497de9f8f234d09f2f91276f16956 |
| DOC032-P0094-C001 | DOC032-P0094 / 94 | 450 | LIDAOE | IGROE | IRRELEVANT / X | IRRELEVANT / X | f2efed486791488a707c3401f23ebe7131daf8a772a5943d1dbb348c2f2e40ce |
| DOC032-P0094-C002 | DOC032-P0094 / 94 | 79 | AOE | ROE | IRRELEVANT / X | IRRELEVANT / X | 6e9cb2d45bdb5c8408fbb503d538fbff9521c054674c948574f0822908c1c648 |
| DOC032-P0095-C001 | DOC032-P0095 / 95 | 450 | PLDO | GURO | INTENDED_OUTCOME / N | IRRELEVANT / X | 317824e6b81afef13f2166bbc0af2389874de443922d8a16941a73bad375da58 |
| DOC032-P0095-C002 | DOC032-P0095 / 95 | 79 | P | UR | INTENDED_OUTCOME / N | IRRELEVANT / X | 5310235034fad663c32cc2d92da1b64ae3d6df77b76f626f3665ad20808b56d2 |
| DOC032-P0096-C001 | DOC032-P0096 / 96 | 434 | PLIDAO | IUROE | INTENDED_OUTCOME / N | IRRELEVANT / X | 20a3544a00a706e832be6e90a558fc0426b207145f828a4b291f2e18dcdc851e |
| DOC032-P0097-C001 | DOC032-P0097 / 97 | 440 | PLIDAO | IURO | IRRELEVANT / X | IRRELEVANT / X | 4b8425e19759ea610c1cbd2c0343bf605a7edc3c50405cd937c90d0c70181355 |
| DOC032-P0098-C001 | DOC032-P0098 / 98 | 450 | LIDAOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | 35db3ff59cf856f3d6f037b2d24504b7286374302c891e26a59df774f42fcbe0 |
| DOC032-P0098-C002 | DOC032-P0098 / 98 | 89 | IAE | AIRE | IRRELEVANT / X | IRRELEVANT / X | 74879bc47dffd60b0049473ff3a593cd2b91d7ebc10f0343aa977ee01a3c8366 |
| DOC032-P0099-C001 | DOC032-P0099 / 99 | 438 | IAE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | 21a1a6325018349e0eab56b4e48b368d00c5b73761af5af38aa2e3beaaaa4f79 |
| DOC032-P0100-C001 | DOC032-P0100 / 100 | 426 | LIDAO | IRO | IRRELEVANT / X | IRRELEVANT / X | d455a353c20b570d363dc9aab1e4cbbc6e5f8ff5e0e5345bfd8edb630563989e |
| DOC032-P0101-C001 | DOC032-P0101 / 101 | 429 | LIDOE | AIRO | IRRELEVANT / X | IRRELEVANT / X | 6a64ff18febf68bee5d5c2df6836dc8c2f8fd497f3d5448985c695f74d3fda84 |
| DOC032-P0102-C001 | DOC032-P0102 / 102 | 449 | LIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 7be88a928cddac50563019e846cb933998e1a610f609ef28225993f4ccf0bf98 |
| DOC032-P0103-C001 | DOC032-P0103 / 103 | 444 | LIDAOE | APIRO | IRRELEVANT / X | IRRELEVANT / X | 3cea76ecbee92cf395777679f92084741e049d16c4071bc091a63c1ad6b42000 |
| DOC032-P0104-C001 | DOC032-P0104 / 104 | 450 | LIE | AIROE | IRRELEVANT / X | IRRELEVANT / X | aa818356d16fbd8138b90871f2de8bc9cb8728cb49b543df8b1fa14fdf4fca4c |
| DOC032-P0104-C002 | DOC032-P0104 / 104 | 105 | LI | IRO | IRRELEVANT / X | IRRELEVANT / X | 087791c9a9c2b3d13678508929189ca62c591a66f869eb906fcb4c7adc7e4498 |
| DOC032-P0105-C001 | DOC032-P0105 / 105 | 437 | LIDAO | IROE | IRRELEVANT / X | IRRELEVANT / X | a100443fe16de896cfa2f4f0e1b3338c267abd2a207f6050336fb0786573ae6b |
| DOC032-P0106-C001 | DOC032-P0106 / 106 | 450 | PLIDAOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | 25683144a38cfe079d46ffd4bf2de0d31f565417e41de2192f06bda88ff03876 |
| DOC032-P0106-C002 | DOC032-P0106 / 106 | 91 | E | APRO | IRRELEVANT / X | IRRELEVANT / X | 0c61c75ea049c716352d41ac42e07905dd4df355e89bbe79968e1fa3a63490da |
| DOC032-P0107-C001 | DOC032-P0107 / 107 | 450 | LIDAOE | APIURO | IRRELEVANT / X | IRRELEVANT / X | e93ff3a3567ec5c30a9e94883332abcc9ab8fda50179f233169163e3e271fb41 |
| DOC032-P0107-C002 | DOC032-P0107 / 107 | 129 | IAO | IRO | IRRELEVANT / X | IRRELEVANT / X | 2041abf16f837058759ce05d5502873fd72e5e9d96772a2705a58d94e1ffc8f5 |
| DOC032-P0108-C001 | DOC032-P0108 / 108 | 440 | IAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 3f1020f6056638278e5a9517fff7d91106e617f3945ec86711e42bfa29de55c0 |
| DOC032-P0109-C001 | DOC032-P0109 / 109 | 429 | LIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 202a8ffada246256c3acea31a377d3e5d217acc4bf006d4293d9fc613a12136c |
| DOC032-P0110-C001 | DOC032-P0110 / 110 | 450 | LIDO | IURO | IRRELEVANT / X | IRRELEVANT / X | 0afe048b37d19038106f5956f3f70bf9e499a8df61d5a3e3ce146d8257fe39f8 |
| DOC032-P0110-C002 | DOC032-P0110 / 110 | 81 | LO | RO | IRRELEVANT / X | IRRELEVANT / X | 7b7f1670b6e3304a7d15c5f78597b1b928280642f3ea2d1c3ee3fba76a861a0c |
| DOC032-P0111-C001 | DOC032-P0111 / 111 | 401 | LDAO | RO | IRRELEVANT / X | IRRELEVANT / X | 40649ca0da07d34323b54ba7000bdce977deba047680d0204e1213b873d8aa25 |
| DOC032-P0112-C001 | DOC032-P0112 / 112 | 361 | LIDAO | IRO | IRRELEVANT / X | IRRELEVANT / X | d19082ac21b7b4561765538d2dada80c5ce5ea3cb5d67106415b37969738aa80 |
| DOC032-P0113-C001 | DOC032-P0113 / 113 | 156 | PLDA | URO | IRRELEVANT / X | IRRELEVANT / X | 3c52d40f1d4a01c3b4eae4a7a5d5dfd9a41667d6d191b175ead4652cdc6242e2 |
| DOC032-P0114-C001 | DOC032-P0114 / 114 | 450 | LIDAOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | e8401c37be9d40720c0ddd4db8027fce960c9bfe9789c18d33047b39d2ef7ff5 |
| DOC032-P0114-C002 | DOC032-P0114 / 114 | 326 | LIDAOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | b8e76db858ae2ac6d3cbda119558898db96cb200157aa16f9a72cc95ad39cc98 |
| DOC032-P0115-C001 | DOC032-P0115 / 115 | 450 | LDAOE | APROE | IRRELEVANT / X | IRRELEVANT / X | 04170e92f381ff598f3d6fa5069de4bfd5b5181bd995f5dc517a01d4ef700274 |
| DOC032-P0115-C002 | DOC032-P0115 / 115 | 234 | PLIDOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 0f072718180fa435397abf2e12d81ad36d3b8d3d39e3f5aaf55f69eb941245fc |
| DOC032-P0116-C001 | DOC032-P0116 / 116 | 450 | PLDAOE | APGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | d45ba5cb7bc5e4ec223efa6c1425b255b8777b7ee72252a93612a9b19b8984af |
| DOC032-P0116-C002 | DOC032-P0116 / 116 | 277 | PLD | PGURO | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 7b8502f447eb506db58bbaec5ced5d4574441c3c196b5c87c1fb5b98f54f90ba |
| DOC032-P0117-C001 | DOC032-P0117 / 117 | 450 | PLDAOE | AUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | f37cdbfe85dc0acfc6f1a43533480a8c7ffd7a4ef7e007135637fc7d6eb4f7ee |
| DOC032-P0117-C002 | DOC032-P0117 / 117 | 287 | PLDOE | APGURO | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 6136e95d03e87f7bb1d2372e64d382679660fc489abbbf99e7ae2bdbf6e4c7e3 |
| DOC032-P0118-C001 | DOC032-P0118 / 118 | 450 | PLDAO | UROE | IRRELEVANT / X | IRRELEVANT / X | b74190f8b3d0779f6566d77ffa438548a735b1d8e1428345c6f77d937b4c0268 |
| DOC032-P0118-C002 | DOC032-P0118 / 118 | 348 | LDAOE | ROE | IRRELEVANT / X | IRRELEVANT / X | c0bc2a4f7a94743e7d16c808513de628e6ff9d8ee1dbc9333dc5db1bdbf300fe |
| DOC032-P0119-C001 | DOC032-P0119 / 119 | 450 | PLDOE | PGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 3ccdadeeee62bc0d043062890da83368ef765c7b0e3e062722fd38c0aaccd930 |
| DOC032-P0119-C002 | DOC032-P0119 / 119 | 309 | PLAOE | GUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 7ad296ae1deb1b5357b62fbb8d51ec5c523ca50cd3f2bc56c3a2fbd4d21b6281 |
| DOC032-P0120-C001 | DOC032-P0120 / 120 | 450 | PLIDOE | IGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 0aaaeab9c3d0d116844705ffcbd682e3da2055db66e449471ad92b9baada686d |
| DOC032-P0120-C002 | DOC032-P0120 / 120 | 263 | PLIDOE | PIGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | b99108943992de2909b0208f65fa7dec86362270f8af12493aad48eea70306b9 |
| DOC032-P0121-C001 | DOC032-P0121 / 121 | 349 | PLIDAOE | PIUROE | IRRELEVANT / X | IRRELEVANT / X | aff4073454aeb6d55da5093be18be0d65fd996e9846f93f65df64dd1b1c9d92e |
| DOC032-P0122-C001 | DOC032-P0122 / 122 | 218 | E | AGR | IRRELEVANT / X | IRRELEVANT / X | 3eece2705161a0df334d9425d7c24a91ba8caa8303a82da0d009415b2a2dcd79 |
| DOC032-P0123-C001 | DOC032-P0123 / 123 | 35 | OE | APOE | IRRELEVANT / X | IRRELEVANT / X | 32a28f70f2faa896a7f5f93c351129efbca64c1aa152437f538effe3c3295a76 |
| DOC033-P0001-C001 | DOC033-P0001 / 1 | 316 | FPLIDA | PIGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | bdcd12a825b8e75858d9ca1334f7b7874312cb94640b2b594b642c989e210219 |
| DOC033-P0003-C001 | DOC033-P0003 / 3 | 16 | FD | R | IRRELEVANT / X | IRRELEVANT / X | 9700405d7bc85ff7c4ef62cd4df2ee73d4963cdf929b06c63453bab9cef69390 |
| DOC033-P0004-C001 | DOC033-P0004 / 4 | 134 | - | PUR | IRRELEVANT / X | IRRELEVANT / X | d9a7fa7b58336b024f2ff8539af7f785fd9f441f033c0b4c046e430248ff5e98 |
| DOC033-P0005-C001 | DOC033-P0005 / 5 | 104 | FDE | GRE | IRRELEVANT / X | IRRELEVANT / X | 54d50bf484875cb84cc33f1d1ab9a742935ca04ed231ad368a7bdd56743c1f08 |
| DOC033-P0007-C001 | DOC033-P0007 / 7 | 338 | FPLDAO | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 46a401463652b8be9ba4550a3d1cd916c170fc650cd1a97bc81846e21d4c6ef5 |
| DOC033-P0009-C001 | DOC033-P0009 / 9 | 447 | FPLDAOE | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 3e8c77f71739ae6cc09217951be65b0c58a23ee711a5b4e86257e3a529c176b5 |
| DOC033-P0010-C001 | DOC033-P0010 / 10 | 160 | FLDO | GR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | b8a8913abea19315426fe647078855b814ed836d8d6a0f308b8a3428f55aed5f |
| DOC033-P0011-C001 | DOC033-P0011 / 11 | 158 | FLIDA | PIGR | IRRELEVANT / X | IRRELEVANT / X | 06f211c63f7e913ac2e04f978684e264ca1e750386c139d8b53574428077c5d0 |
| DOC033-P0012-C001 | DOC033-P0012 / 12 | 240 | FLDE | GRE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 85c7b8c9a8451bff311b2f14c6000dd257bf0b18e95f24b1db9b2e9aa0f71bd8 |
| DOC033-P0013-C001 | DOC033-P0013 / 13 | 300 | FPLDAO | GURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d422ff4dccad38a1adc3b170f6d6ae32cd9d3dba86d1ad762ebb6e0faba11ce5 |
| DOC033-P0014-C001 | DOC033-P0014 / 14 | 246 | FLIDA | IGUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1fbbb363ffd8d98fdcec7e5e998a68086a00e0fd8e1e3000653bd1f98326c1b5 |
| DOC033-P0015-C001 | DOC033-P0015 / 15 | 209 | PLDO | GUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | e26f58f326891146d50256bcc98026c611fd425927359aac44030a36c845a448 |
| DOC033-P0016-C001 | DOC033-P0016 / 16 | 450 | PLIDOE | APIGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d28ce2d776e275443aa8250cf372d29a0e29c81687b741ba5c03e3a21403ed73 |
| DOC033-P0016-C002 | DOC033-P0016 / 16 | 91 | FPLD | PGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | e22a49e2c85346c336513ddee2d2bd828b0317ed1eb9afacc349329373fd8d0d |
| DOC033-P0017-C001 | DOC033-P0017 / 17 | 450 | FPLIDOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | f1a3ad68e02bf63a965e362d52f42a23fae11d280f7a02859a541335e049ae63 |
| DOC033-P0017-C002 | DOC033-P0017 / 17 | 115 | FPLIDO | PIGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | c37996e58121fba45afac63fdf7db5b5b42ac1ff4eff75e54b86f21aa6398388 |
| DOC033-P0018-C001 | DOC033-P0018 / 18 | 450 | FPLIDE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | ec6102e84d4e5a04b43d7cd8f6698c7c7c871a0b5e9544e5b050aea2e1149aa9 |
| DOC033-P0019-C001 | DOC033-P0019 / 19 | 195 | FPLDOE | GUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 49d9c9947526fbf01a3e75e4113c83a412e0c12af86db326c671fe7f2314f2d2 |
| DOC033-P0021-C001 | DOC033-P0021 / 21 | 297 | FLIDAOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | a303bd016ac1ffd82cb17d47967666fd2f34e8c3672b329bb34b5dfa32fbb1cd |
| DOC033-P0022-C001 | DOC033-P0022 / 22 | 450 | FPLIDAOE | PIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 67a5e59902eafa99e5ff3e4e808afcca57546e284eb9a78c69233a769fc0db4d |
| DOC033-P0022-C002 | DOC033-P0022 / 22 | 147 | FPLIDAO | PIGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | f19500967a7bd35735559663d1ed976cd7962210b25258fcd30a48db1f87015d |
| DOC033-P0023-C001 | DOC033-P0023 / 23 | 111 | FLID | IGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 0b9f54795fac7a4c834c61068fa700d327efb3ef7a5831dfd7f07800dec28e2b |
| DOC033-P0025-C001 | DOC033-P0025 / 25 | 183 | PA | PGR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 16664000adecaacb2ba2900fc84ff28b961462341df304918e32926719d1182d |
| DOC033-P0026-C001 | DOC033-P0026 / 26 | 450 | PIDOE | IGUE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | bbaa767f510c0e5629366e0dbd23ea99647346119a6cd85917fac0f867b9c55a |
| DOC033-P0026-C002 | DOC033-P0026 / 26 | 164 | FPID | PIGUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 89d9a453c75e49c1b42286f1817061144aaf899d144953e54825ada530977af0 |
| DOC033-P0027-C001 | DOC033-P0027 / 27 | 231 | FPLD | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 4b7945f1b535af412e94daa708694737fe7039731dcf0dc845b9a5531c45eec7 |
| DOC033-P0029-C001 | DOC033-P0029 / 29 | 332 | PLD | GURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 98c7b5fa8fd0f5e17c6c780e697572055b8be797e8633c094de1506a97e7fd6d |
| DOC033-P0030-C001 | DOC033-P0030 / 30 | 215 | FPLIDAOE | GURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 308d266a3f6795e58c840f0bad98abf7f175696d597bf081ebec6cc6bd6cc335 |
| DOC033-P0031-C001 | DOC033-P0031 / 31 | 201 | LE | GRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0fcdbb074dd9e9ae351cb78575f9ad8454f1c88c8ee68a78569a36294bf59d03 |
| DOC033-P0032-C001 | DOC033-P0032 / 32 | 450 | PIAO | IGUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 11ad95a4056a76ad2220f9a05a05c20b0e107a326b08010def3c7b2b893effdd |
| DOC033-P0032-C002 | DOC033-P0032 / 32 | 195 | FPIDAO | IUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2ce6bc5678cccd0909adca76365668b3fc259f487a8a59d1262d27979b73fdad |
| DOC033-P0033-C001 | DOC033-P0033 / 33 | 450 | PLIAOE | IGURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 5a9dd5e80f324926ce8024cbfee83b9d18b416da2ab19d21e4eadb04092899c5 |
| DOC033-P0033-C002 | DOC033-P0033 / 33 | 182 | DAE | RE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 84300e3699af3c2a004c06ae53f641a45e57886e82e440cf2a4791625e3fd9f0 |
| DOC033-P0034-C001 | DOC033-P0034 / 34 | 450 | FPLIDO | IGURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9da909a0fd6c308849517d51cff066df26ffa7078a63adc08e0a3d879f4e3d2d |
| DOC033-P0034-C002 | DOC033-P0034 / 34 | 137 | FIDO | IRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2bba0b7929b477b1815bfdd57da044ec401780dedda4c3ef3f6be9f94ee6494c |
| DOC033-P0035-C001 | DOC033-P0035 / 35 | 450 | IDO | IGURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 159b2f57e0ac9326052313238d60d4bd542d874fdfb69040369f1a4352ee478d |
| DOC033-P0035-C002 | DOC033-P0035 / 35 | 164 | IE | AIRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 5ca6cebafe8d58c78c96a8ae6616035104c1e776044d2fcf4aa4759d3828669b |
| DOC033-P0036-C001 | DOC033-P0036 / 36 | 450 | PIDAO | AIUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 241421fe8b4f36393a3d0852ffe2f69355d303a2a663a79ac858eba5216dd072 |
| DOC033-P0036-C002 | DOC033-P0036 / 36 | 186 | FPDOE | UROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 055a720042663f884accbbf24fec75200fd6499e657abbb579e0dbdc6ec89be2 |
| DOC033-P0037-C001 | DOC033-P0037 / 37 | 450 | LIDAO | AIROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | dc74d78807a1132477970b07ca04a54756b4ade3e92e1dcc602fc834bac2c96d |
| DOC033-P0037-C002 | DOC033-P0037 / 37 | 176 | LIDAOE | IUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d2834ceefd2445bec0b908cde8043ddf03ad7d9f03b3d4095e6f0a910460b796 |
| DOC033-P0039-C001 | DOC033-P0039 / 39 | 72 | FPLDO | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | c044ed68f41f13544694de0b48352f0b9fd3c19dd17a7e4f360007b6f1af2979 |
| DOC033-P0040-C001 | DOC033-P0040 / 40 | 394 | FPLIDAOE | AIGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d9d8b053c6f9ab460798a6f3591cc55a4ea4230a6c97175ae414183aed9da385 |
| DOC033-P0041-C001 | DOC033-P0041 / 41 | 450 | FPIDE | IURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 144e3954ddf478c1f26a2ed139b34aa7d0481508ca27f8431584e88d2438dbd3 |
| DOC033-P0041-C002 | DOC033-P0041 / 41 | 130 | FDE | RE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9fb92e31d3fe81118ad439690b33a221f585cbe1935bc9cad4edfdaa184b5c3c |
| DOC033-P0042-C001 | DOC033-P0042 / 42 | 450 | PLIE | IUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 28e4fb1e40c31ff19126aeb59ce1dc6d9a92a39791055105de5383f6d92dc7c8 |
| DOC033-P0042-C002 | DOC033-P0042 / 42 | 121 | FPDE | RE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | ead19f35dea1b38c9be36c1575ae6a7a931b17e33e4790d92606285e08fd4edf |
| DOC033-P0043-C001 | DOC033-P0043 / 43 | 425 | FPLIDAO | IGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 80eb0dbe945e868624ddf364a845150d22be2b3362073430de32188fd78e78d2 |
| DOC033-P0044-C001 | DOC033-P0044 / 44 | 450 | PLIE | IGURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 19a80428eac179fb715d34cd6b072f6bdf4e9aa48cea302af905107a78910bf8 |
| DOC033-P0044-C002 | DOC033-P0044 / 44 | 239 | FIDE | IRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 5d3d48d32d7f2ad6797a5d8702f614bc9ea92dd94b4922556067ba5435a910a6 |
| DOC033-P0045-C001 | DOC033-P0045 / 45 | 450 | PIOE | IUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 3560f6fb5236168e7acab2381e614033f2449a9a378d5b4506915e974a7f9829 |
| DOC033-P0045-C002 | DOC033-P0045 / 45 | 111 | FPD | UR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | ca0e75362daced10e2d02ecd35b412e35f529a0a1a5c7ac1683127284e004704 |
| DOC033-P0046-C001 | DOC033-P0046 / 46 | 450 | PIO | IUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0bcfcf872d783096c91820a27cd2f36ff2352532913aa2642d97ddddee7343bc |
| DOC033-P0046-C002 | DOC033-P0046 / 46 | 150 | FIDE | IRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 6f24f9439d4d2056d55ef7adfdd2df84d6b54aec094a71ef6023654a7d89bc4a |
| DOC033-P0047-C001 | DOC033-P0047 / 47 | 439 | FPIDA | GURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | c15505304ebcbd769d515130109037cd37d3f29c8de6b32c772b32c657a4310b |
| DOC033-P0048-C001 | DOC033-P0048 / 48 | 450 | PLIA | AGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 561a3aa7d0fccbba01765ebcec69137c2d1acbeccf0313ea6fb5e1e7639db99e |
| DOC033-P0048-C002 | DOC033-P0048 / 48 | 84 | FD | AGR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 8f34f153397fdb39df8dd6878ce6fdee08227bb94fa01a5cb662b5b0a89ae787 |
| DOC033-P0049-C001 | DOC033-P0049 / 49 | 450 | PIAOE | AIGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | f50381ccbc7567848ff58c6154b77bf0cd5e7401892cd77b76706f7c45e24bbd |
| DOC033-P0049-C002 | DOC033-P0049 / 49 | 97 | FDAOE | AGRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | a003138cc404c4af3981e013be9d92c32a075043300f88f9b3534a2ddd578f42 |
| DOC033-P0050-C001 | DOC033-P0050 / 50 | 450 | LAO | AROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2fe8a26822466267553642063381c38596e19b8741ef17b7a21f8e7bdcb5b977 |
| DOC033-P0050-C002 | DOC033-P0050 / 50 | 82 | FD | R | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9c179148c9374bbb29b8d43f1f646bbd3cc177448964cd06697479ba2100cd7a |
| DOC033-P0051-C001 | DOC033-P0051 / 51 | 450 | POE | AUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | fa6bd59729215da498f236c12911affde27a0b9016be2e20055aa9a4f6f27844 |
| DOC033-P0051-C002 | DOC033-P0051 / 51 | 198 | FPIDO | IUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 15191cc07d9d1583b3c3e3e0eb42d81c6bca8dd2f8a201e6349a5ea1ce1543ac |
| DOC033-P0052-C001 | DOC033-P0052 / 52 | 450 | IO | IRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | aa3d3ea93b98d86c922b40ed34b2da5094d7dbc32765f3bded8c6712fab3aad5 |
| DOC033-P0052-C002 | DOC033-P0052 / 52 | 112 | FID | IR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 7e8960ee03afba5c1f8b8aabfd3a0926719a97b7982c1693ba4149203deb1c9a |
| DOC033-P0053-C001 | DOC033-P0053 / 53 | 393 | FPDO | URO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 6c05abc018489c43cd5ab95765095d5f48626a99f59250e2e9e76a4644832ab7 |
| DOC033-P0054-C001 | DOC033-P0054 / 54 | 384 | FPDAO | UROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | f94b7b5190fbb4b991a846160a4f1d87c79ae461524ac35bcd6fe3dc90305854 |
| DOC033-P0055-C001 | DOC033-P0055 / 55 | 375 | FIDO | IRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | bde9577ae8e3521fb1113abf9ba2423fed2b440fa566454783a195e705d3bf34 |
| DOC033-P0056-C001 | DOC033-P0056 / 56 | 404 | FPIDE | PIGURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 34d01fab0a795fb92131b2788e9eb5c9ad92ddc35d314f9b4ceff38ae28a9653 |
| DOC033-P0057-C001 | DOC033-P0057 / 57 | 365 | FIDA | IGR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 19bf0476de90ecd223b3c2b818c40288b4338961cad6cc11f7d96c92a7748008 |
| DOC033-P0058-C001 | DOC033-P0058 / 58 | 381 | FPDOE | AROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9f3c8858782836608bea2dc938e9b7308c87067b9202f2cda6755c7080bcfb1e |
| DOC033-P0059-C001 | DOC033-P0059 / 59 | 450 | LIDO | PIGURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 34c773f3b04ecd526e006960f912a34013aebe39caafbf90635cb5e56ffaa102 |
| DOC033-P0059-C002 | DOC033-P0059 / 59 | 103 | FD | UR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | b5766cd11eb1efcb5385499ed55feed6286d9174a5d3a13ef223d3c797a3f2ef |
| DOC033-P0060-C001 | DOC033-P0060 / 60 | 197 | FLID | IRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 7a5949722094dc7405b5d5ece4f85008839eb68fd77491eaf4e8dd3cd7b76086 |
| DOC033-P0061-C001 | DOC033-P0061 / 61 | 201 | FPLIDAO | IGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 371313ea5dcb078908fc7214df69fe811fe077f3af9ad4e970e8240df0abe043 |
| DOC033-P0062-C001 | DOC033-P0062 / 62 | 450 | PLDAOE | AGUROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 7634c40bf35c2cf1b1ae8d9f65a6f57c0217e10958851ab3657a2fd72b327a85 |
| DOC033-P0062-C002 | DOC033-P0062 / 62 | 97 | FDAE | RE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 8c7553be3875cee26efe30903c8147a01b886ca2c73c0b13a6cee2887af7345d |
| DOC033-P0063-C001 | DOC033-P0063 / 63 | 355 | PDAOE | PUROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 4532fa75430dae592f37c1950f1fbb5088c42e1d172a086056621108d77c3ba1 |
| DOC033-P0064-C001 | DOC033-P0064 / 64 | 450 | LIDAO | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 9ac9266a39afb0155f9b406ffdd0e958039005e2a17b78875f56acb4a08165c6 |
| DOC033-P0064-C002 | DOC033-P0064 / 64 | 144 | FLDAO | GRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | e100cfa99b95b029dd9a1b1b775d4630876e9e88d5b81487d10b0b843031d83d |
| DOC033-P0065-C001 | DOC033-P0065 / 65 | 450 | LIDAE | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 327f8bb56371f57363af2a025f480d475294dd91244f9c3fc051c954d8474150 |
| DOC033-P0065-C002 | DOC033-P0065 / 65 | 211 | PLIDAO | IGRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | a397d9988cb7c87a4f19f89119de4bf338c4e469000d7a6e784ba998f4de6801 |
| DOC033-P0066-C001 | DOC033-P0066 / 66 | 83 | FLIDAO | GRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | d600e8d3e133908424bb0e97e42542c8661d3cf5ea4a5dda480c77b70d3f96f0 |
| DOC033-P0067-C001 | DOC033-P0067 / 67 | 271 | PLIDAO | IGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 4e34b60042881ea38d0bc4014ccf1b73801f567cd96452ccb7a7590f66e60efc |
| DOC033-P0068-C001 | DOC033-P0068 / 68 | 201 | FLDAE | AGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 48ea1d918f8120a624993b6eb2d1d29addf068639471ce812eda0482825b9271 |
| DOC033-P0069-C001 | DOC033-P0069 / 69 | 61 | PLDO | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9f1bfee6b674e7958710132d9ff0cfb41b6fd78c4b0b2e6943abe3a2fe204614 |
| DOC033-P0070-C001 | DOC033-P0070 / 70 | 260 | FPLIDAO | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 08b066bac5558645bb6a50012ff6749f46e50b392f2c17ac39175d15399ff9f8 |
| DOC033-P0071-C001 | DOC033-P0071 / 71 | 450 | POE | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | fee3e92f3b76405cc28aa364507b8e93eebd33478f5a4766a02f3144195d266a |
| DOC033-P0071-C002 | DOC033-P0071 / 71 | 101 | P | R | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | c91c2c47137c1b7ca5e8a157124a20c8ac42a925e70d3bf6e8a3bda2c7b75aef |
| DOC033-P0072-C001 | DOC033-P0072 / 72 | 450 | PIDAOE | IGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 4caa177bfae17ef090fa689ef90a48955ef09ee92d4bec1d279b86652ed79edc |
| DOC033-P0072-C002 | DOC033-P0072 / 72 | 111 | FID | IR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 78c0b9e63e2b54c7662b65d94782f07eb26d64cd70f8ba5fcb769bb5a7dd9ec5 |
| DOC033-P0073-C001 | DOC033-P0073 / 73 | 382 | PIAOE | PIGURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | ec82bca3e394a3ca4519034aa6ceebc8070950faec59ac9f26a054c604fbb3d3 |
| DOC033-P0074-C001 | DOC033-P0074 / 74 | 450 | PLIDAE | IGROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | a5fa4d56d464cbb371fb3515910830043ac2a312d1b1628e604935305a8fd401 |
| DOC033-P0074-C002 | DOC033-P0074 / 74 | 125 | FPLD | GUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2a0df4dbc18c3cd87bfdca4ef733d7444b309c6de9d8c17256f60d5251524eea |
| DOC033-P0075-C001 | DOC033-P0075 / 75 | 415 | FLA | GRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 61440dc6d20b8b18dc06da17e3222dd8706b78ebadaf634a0d8aa09bc4ca6c3d |
| DOC033-P0076-C001 | DOC033-P0076 / 76 | 408 | FPLIDO | PIGURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1bf84e2c6412d4b2ad8c441959b365e8bb65ed06900dc9d6dc870dc7bb15fc5b |
| DOC033-P0077-C001 | DOC033-P0077 / 77 | 445 | PLIDOE | IGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d61c688b310b7fcb398ddb24248b5957abbb9717e5de01cf72cd732d0dce9546 |
| DOC033-P0078-C001 | DOC033-P0078 / 78 | 450 | LIDO | IGUO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 83d684fb4aff7f0ba3340d1816636db35aeb3306f3561f907c08c1f64a7f48e1 |
| DOC033-P0078-C002 | DOC033-P0078 / 78 | 89 | FDO | RO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2b5f39f653d9362e07729a8b974f811a299259c5b67eef232ab633c03e1d7b9c |
| DOC033-P0079-C001 | DOC033-P0079 / 79 | 450 | PI | IGR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9f4666ec06ac5e82ddf733c77b61c5a897559c5b5d232cabfb2d7c77831c0bb0 |
| DOC033-P0079-C002 | DOC033-P0079 / 79 | 90 | I | IR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 108b9d763aeded844197bca0be26024f93362289d819ff059ebaa8d0c74888f7 |
| DOC033-P0080-C001 | DOC033-P0080 / 80 | 441 | FIDAOE | GURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | b40781520923b2cd135f91fb6ae6a8315ff69c49cdc58976ea5b9b30953eed44 |
| DOC033-P0081-C001 | DOC033-P0081 / 81 | 295 | FPLIDE | IGURE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 5c343d55d9b88461d868e4ce68b8c5178544470108860dabdf43f3f2d4baac0d |
| DOC033-P0082-C001 | DOC033-P0082 / 82 | 341 | FPLIDAOE | PIGROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 342abc160723621e73f4c8a37f367c41ecbac837fb9f7a83ffa6b547da1aaa7b |
| DOC033-P0083-C001 | DOC033-P0083 / 83 | 365 | PLIDE | PIGRE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 98ab5ac55ff86ec8f16535dcb13ecec727978aa6dcde085ed4533a150932d24b |
| DOC033-P0084-C001 | DOC033-P0084 / 84 | 411 | FPLIDAOE | AIGROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 9de0b9c24a14f7b3b57b1c129f0476551a37ea1eae42898262677844d82e7082 |
| DOC033-P0085-C001 | DOC033-P0085 / 85 | 221 | PLIDAOE | IGUROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 6cfe64ad12fe12af51def7f3fba9281c2bd7be7e71bbf9f969832a4def35c148 |
| DOC033-P0086-C001 | DOC033-P0086 / 86 | 450 | - | R | IRRELEVANT / X | IRRELEVANT / X | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC033-P0086-C002 | DOC033-P0086 / 86 | 244 | - | R | IRRELEVANT / X | IRRELEVANT / X | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC033-P0087-C001 | DOC033-P0087 / 87 | 132 | FPLIDAE | AIROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC033-P0089-C001 | DOC033-P0089 / 89 | 316 | FPLIDA | PIGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | bdcd12a825b8e75858d9ca1334f7b7874312cb94640b2b594b642c989e210219 |
| DOC034-P0001-C001 | DOC034-P0001 / 1 | 290 | FPLIDAO | PIGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0c989069d771c0b92525b21f783fd2d28e5f07f9a555a0c352c7145369411490 |
| DOC034-P0003-C001 | DOC034-P0003 / 3 | 18 | FD | R | IRRELEVANT / X | IRRELEVANT / X | 09f8faed975560989a8412ea8c2422dfd481f9b5eaa6e3d754619308eead0cd3 |
| DOC034-P0004-C001 | DOC034-P0004 / 4 | 134 | - | PUR | IRRELEVANT / X | IRRELEVANT / X | b35ecce502df3fb49e34ad581a153bc9b3933b804bfdf0e462a0b4e8ea311da1 |
| DOC034-P0005-C001 | DOC034-P0005 / 5 | 70 | FDAE | RE | IRRELEVANT / X | IRRELEVANT / X | c210abf1e264664e3aa32379919bd47f36ea4c1390d9210145403ff31f8727da |
| DOC034-P0007-C001 | DOC034-P0007 / 7 | 338 | FPLDAO | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 2b2b68b75880ebfbfe9570a5c2e9b42855035b9bf049ade601b7a31aeb012c41 |
| DOC034-P0009-C001 | DOC034-P0009 / 9 | 422 | FPLDAOE | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 4ca64c0c819df4c3d3424aeb587c0bbd441faa6b90b586c446da2fe816303b40 |
| DOC034-P0010-C001 | DOC034-P0010 / 10 | 177 | FLDO | GR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | a9e88eef278d70d7b5f3b77aa27b2589d419b6a8bba9597fd89b7c9be9c67db4 |
| DOC034-P0011-C001 | DOC034-P0011 / 11 | 158 | FLIDA | PIGR | IRRELEVANT / X | IRRELEVANT / X | 16422f5855c938c3433b431749b71600a9466a0b7513354bf1de6ae8ab1f3b4d |
| DOC034-P0012-C001 | DOC034-P0012 / 12 | 240 | FLDE | GRE | OTHER_NEAR_MISS / V | IRRELEVANT / X | a3c23ae968f124f2b2c870308e0833a442a5748dc106633c814c71a8ad1792eb |
| DOC034-P0013-C001 | DOC034-P0013 / 13 | 235 | FLIDAOE | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 1a644563d77b7695b099a4749ee20e5ee774a999fe4f74ec43904eb3995bce82 |
| DOC034-P0014-C001 | DOC034-P0014 / 14 | 450 | DOE | AURE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | d0d5581d9744d5ac1700ae3788d066fa9583db372fd2755bfdc2c8a7d75fab3e |
| DOC034-P0014-C002 | DOC034-P0014 / 14 | 135 | FLIDO | IGUR | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | e943b775f2874a9e923d167886252b6fe18955d936541322e78c959ce1b990e5 |
| DOC034-P0015-C001 | DOC034-P0015 / 15 | 450 | FLIDAO | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 7581cebea03b96f1a406587f3dbd8c314c9679cce34e7c72b1f677283ef2f7e7 |
| DOC034-P0015-C002 | DOC034-P0015 / 15 | 129 | FDAE | RE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 7e98532e3d8f1fea5df8b16c04b605a891b522ce2485186d262a772a4d2f5998 |
| DOC034-P0016-C001 | DOC034-P0016 / 16 | 254 | FLIDAO | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 9521a496f7a81a2e8430faabcf4a75623405fc7cf1bb2abe63dd09a1cbfc851f |
| DOC034-P0017-C001 | DOC034-P0017 / 17 | 126 | D | GR | DESCRIPTOR / D | IRRELEVANT / X | ba0b3408ad6bef143beb4843319ca477cabc691068aaf91d648c78cc8652a37a |
| DOC034-P0018-C001 | DOC034-P0018 / 18 | 333 | FPLIDOE | PIGROE | DESCRIPTOR / D | IRRELEVANT / X | 6ad0822f983de9369d8394c2de686396306cdbef76dfc2e86ee4afcd0ab5d916 |
| DOC034-P0019-C001 | DOC034-P0019 / 19 | 238 | PLD | RO | DESCRIPTOR / D | IRRELEVANT / X | 02b58a67ee3c50b3efb81a8f657d1c4eaae6108598582486b8c9343b84b2dfc4 |
| DOC034-P0020-C001 | DOC034-P0020 / 20 | 227 | FPDO | R | DESCRIPTOR / D | IRRELEVANT / X | 20143f2cde873de90707e31ededa43a2bf3857cc2d5c5e8e60142df2906b6f9e |
| DOC034-P0021-C001 | DOC034-P0021 / 21 | 273 | LDAOE | AUROE | DESCRIPTOR / D | IRRELEVANT / X | d45fdba1255529234463730ca0a9669f3cfef7ac5608100ba65c27cef8c29dac |
| DOC034-P0022-C001 | DOC034-P0022 / 22 | 325 | FIDO | IUR | DESCRIPTOR / D | IRRELEVANT / X | 9a7c956dd8f937868b3547bb0083c645e1307175191b160685fbe8141c70a6c0 |
| DOC034-P0023-C001 | DOC034-P0023 / 23 | 90 | DO | RO | DESCRIPTOR / D | IRRELEVANT / X | b489a7a79342f9f6bab29363e8940218ed0791de16b231231596ce52b3c54d06 |
| DOC034-P0024-C001 | DOC034-P0024 / 24 | 212 | FDO | RO | DESCRIPTOR / D | IRRELEVANT / X | b88b418f0183c1d2ade67d348af3bad2a7bbc99b72efb260c2ec289da5336d25 |
| DOC034-P0025-C001 | DOC034-P0025 / 25 | 342 | PIDAO | PIRO | DESCRIPTOR / D | IRRELEVANT / X | d3939d4b97584a32ebecee51e2c1e4012f5a26f2c5cc4bf96ffe13c55bf3b942 |
| DOC034-P0027-C001 | DOC034-P0027 / 27 | 150 | LDAE | GRE | DESCRIPTOR / D | IRRELEVANT / X | a1d295c10bc52620ee8a45f430b7b7aebe6b2397c15c85def978cb142c228bf1 |
| DOC034-P0028-C001 | DOC034-P0028 / 28 | 290 | FLID | IGRO | DESCRIPTOR / D | IRRELEVANT / X | 89f4ce38980d00808189fc980ce5dbece587ed27faad2ac57dd49615c5e9f4d6 |
| DOC034-P0029-C001 | DOC034-P0029 / 29 | 297 | PLIDE | IGRE | DESCRIPTOR / D | IRRELEVANT / X | 89a6b423048d6cb756e5f87e131f1347217f6dfd68574422b6facd57cabdb859 |
| DOC034-P0030-C001 | DOC034-P0030 / 30 | 222 | FPIDO | PIGRO | DESCRIPTOR / D | IRRELEVANT / X | 23697189ec905fc98ad29c1592b0d088dfeacc0c4d2a0325cd6dc2e6e3133aab |
| DOC034-P0031-C001 | DOC034-P0031 / 31 | 283 | LID | IURO | DESCRIPTOR / D | IRRELEVANT / X | f063c4020704cef7e650738f9a6bfdfc7d3896e4f2daa8a9fe36f8bcb0836ae4 |
| DOC034-P0032-C001 | DOC034-P0032 / 32 | 292 | FPDO | PGURO | DESCRIPTOR / D | IRRELEVANT / X | 573f9e07e67219d41f4bff1987b3d8aa0d6932493d1025dab828d0ce53f8f9e4 |
| DOC034-P0033-C001 | DOC034-P0033 / 33 | 255 | DOE | ROE | DESCRIPTOR / D | IRRELEVANT / X | 2ae90b25ec4ed7bd4598deafe76d55b9be2601db774e322b4befdac330a360ef |
| DOC034-P0034-C001 | DOC034-P0034 / 34 | 276 | FPDO | RO | DESCRIPTOR / D | IRRELEVANT / X | 7314c840b651872fce252d3dbc1872a47318f45da8d8c9316dbe19b22b3b1ec9 |
| DOC034-P0035-C001 | DOC034-P0035 / 35 | 215 | D | UR | DESCRIPTOR / D | IRRELEVANT / X | 673651f119858d73e16362959e37d79ae7535ad32504990dfa48a91739e12441 |
| DOC034-P0036-C001 | DOC034-P0036 / 36 | 269 | FLDAOE | GUROE | DESCRIPTOR / D | IRRELEVANT / X | f945edcab3085341e74325f7f3b0c57bb087e4e44aede69d35ac902a42ccd8fa |
| DOC034-P0037-C001 | DOC034-P0037 / 37 | 286 | LDAOE | AROE | DESCRIPTOR / D | IRRELEVANT / X | ff6f72bec8ccd0657df597d680a1a999a0cd5664117efcb56cb9f46b54b2a582 |
| DOC034-P0038-C001 | DOC034-P0038 / 38 | 311 | FIDAOE | AIRE | DESCRIPTOR / D | IRRELEVANT / X | 5546ce6723fb1f127d15b30079691db43be36f1b89addea848487078c9ffbb05 |
| DOC034-P0039-C001 | DOC034-P0039 / 39 | 332 | DAO | GROE | DESCRIPTOR / D | IRRELEVANT / X | f538485c11fc9c7ffced46491b5f765ff4a77231ef0fd554f84850505ed146fa |
| DOC034-P0040-C001 | DOC034-P0040 / 40 | 293 | FDA | RE | DESCRIPTOR / D | IRRELEVANT / X | 7b5d57e4a9bfd7133f6dad6f15358326bf778e65771bbec50e9ae387f66ad2e8 |
| DOC034-P0041-C001 | DOC034-P0041 / 41 | 294 | LDO | URO | DESCRIPTOR / D | IRRELEVANT / X | 7594ebac60269cde5095a65f33eea68053b0b7e6950cb6295ac04f2209435a0c |
| DOC034-P0042-C001 | DOC034-P0042 / 42 | 278 | FLIDO | IURO | DESCRIPTOR / D | IRRELEVANT / X | c9dc8af5344b46cf4ce0dd20ed40c7443d059bdd29a744c8ffcc42a9af5d44ae |
| DOC034-P0043-C001 | DOC034-P0043 / 43 | 309 | ID | UR | DESCRIPTOR / D | IRRELEVANT / X | 2e2388880d2e54dd3d7ce4baa6e61d21a3fcae3ac8d56de634a9ea4f1276f012 |
| DOC034-P0044-C001 | DOC034-P0044 / 44 | 310 | FDO | URO | DESCRIPTOR / D | IRRELEVANT / X | 101f5710190d8a376143ecc2a5a344e9e7f8c8145f78d67519dd62798f007451 |
| DOC034-P0045-C001 | DOC034-P0045 / 45 | 335 | PDO | URO | DESCRIPTOR / D | IRRELEVANT / X | 17a7b322c297e15abbd41d38608ce5760dc3c62f13210cf3f21c91ecf2aec45b |
| DOC034-P0046-C001 | DOC034-P0046 / 46 | 310 | FIDO | IRO | DESCRIPTOR / D | IRRELEVANT / X | fc024c463b5dac6bfed04e9f075da687fd9a266bd3005a7a28fe1ee516719929 |
| DOC034-P0047-C001 | DOC034-P0047 / 47 | 60 | DO | RO | DESCRIPTOR / D | IRRELEVANT / X | f60cd3d677c6533b417e860b20e03486c53ec029ed2d7119fef789b951b7807e |
| DOC034-P0048-C001 | DOC034-P0048 / 48 | 218 | FD | R | DESCRIPTOR / D | IRRELEVANT / X | 90c66cb66489b294a7e9e0d24f217fd8348e6747827417a0f117c9c125d2a132 |
| DOC034-P0049-C001 | DOC034-P0049 / 49 | 294 | DO | RO | DESCRIPTOR / D | IRRELEVANT / X | d3f01cd339e1dae1f19b3cd9b320dab88923ab83b04aebedc2bb02dd4a778e9c |
| DOC034-P0050-C001 | DOC034-P0050 / 50 | 309 | FPDE | PRE | DESCRIPTOR / D | IRRELEVANT / X | aae16d6bfa2a9d1dc9f8c2727b6601ca0c98d3abef037a978e3015d4aedc82d7 |
| DOC034-P0051-C001 | DOC034-P0051 / 51 | 320 | IDA | IR | DESCRIPTOR / D | IRRELEVANT / X | d602122105e147b0d2926ea0e139dcd9e16554a8409580b996620cda0fba92f1 |
| DOC034-P0052-C001 | DOC034-P0052 / 52 | 308 | FPIDAOE | IROE | DESCRIPTOR / D | IRRELEVANT / X | 66c6c2f7e117823e68c22af9ff9bf2c62aa6ba687258f773b56a46827f6097d9 |
| DOC034-P0053-C001 | DOC034-P0053 / 53 | 173 | PDO | RO | DESCRIPTOR / D | IRRELEVANT / X | 2f517c9bf8dd778708d3f03d6cbbdbc89cabd2247f3a214e7a5a3492e0eb40ff |
| DOC034-P0055-C001 | DOC034-P0055 / 55 | 128 | FLDAE | GRE | OTHER_NEAR_MISS / V | IRRELEVANT / X | c2ab12d819b6bfbc4869273e3d501b542fc97e38c29d595bd2172d150dc8753b |
| DOC034-P0056-C001 | DOC034-P0056 / 56 | 450 | LDAE | PGUROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | a0847b80f0ac4c87446233124cf62632cf4711789eba314db0f4abe0d2929aa7 |
| DOC034-P0056-C002 | DOC034-P0056 / 56 | 125 | FDAOE | UROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 66a54d5e21891854753747400eb829fdb6f3b42c47a3a008cfb44a69908c2cfa |
| DOC034-P0057-C001 | DOC034-P0057 / 57 | 450 | LIDAOE | IGROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | e2aa83b472e95d0e4b55529bb8ce6a91373ba66eef7033ff45f1332b28132ee7 |
| DOC034-P0057-C002 | DOC034-P0057 / 57 | 121 | LIDAOE | AIUROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | 4ca6b937ff82cf207f00289d01ddc5ac380fd7e70494736a56e756a3b9540a67 |
| DOC034-P0058-C001 | DOC034-P0058 / 58 | 327 | FDAOE | AUROE | OTHER_NEAR_MISS / V | IRRELEVANT / X | fa1b0f9bbf995bb0a830cd4f376723ae5140152b9ae183ab3f37df3ae386a855 |
| DOC034-P0059-C001 | DOC034-P0059 / 59 | 213 | FLIDAO | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 8498299329f2251101dc97bb7c942d4c1355f518590fc81095e86ab76b1e4c70 |
| DOC034-P0061-C001 | DOC034-P0061 / 61 | 126 | LIDAO | IROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | af0084e8d51b01bc9a022e7a8d82fd85c750735465ebdc27efafbeea7aa77df8 |
| DOC034-P0062-C001 | DOC034-P0062 / 62 | 450 | - | R | IRRELEVANT / X | IRRELEVANT / X | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC034-P0062-C002 | DOC034-P0062 / 62 | 244 | - | R | IRRELEVANT / X | IRRELEVANT / X | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC034-P0063-C001 | DOC034-P0063 / 63 | 132 | FPLIDAE | AIROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC034-P0065-C001 | DOC034-P0065 / 65 | 290 | FPLIDAO | PIGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0c989069d771c0b92525b21f783fd2d28e5f07f9a555a0c352c7145369411490 |
| DOC035-P0001-C001 | DOC035-P0001 / 1 | 288 | FPLIDA | PIGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1dfa30f7e3949cbd4e3f44c32c5a04e6da11cad8c398f8a257b48e38d98686f0 |
| DOC035-P0003-C001 | DOC035-P0003 / 3 | 32 | FLIDA | IGR | IRRELEVANT / X | IRRELEVANT / X | 0145a469c9e6d2eb5379315190b6171c2cdd96207bbc9a3c38a339b34197d323 |
| DOC035-P0004-C001 | DOC035-P0004 / 4 | 134 | - | PUR | IRRELEVANT / X | IRRELEVANT / X | 7b00d937868ddea0bea9e2a4c1e2f46749a42693b11ab1bff61b80e6ca7a6c42 |
| DOC035-P0005-C001 | DOC035-P0005 / 5 | 87 | FLIDAE | GRE | IRRELEVANT / X | IRRELEVANT / X | 3d5c385a16aebcb234938cb4c8b4b7d3c2bcb8daa5b4556d6907554e193eb3b8 |
| DOC035-P0007-C001 | DOC035-P0007 / 7 | 338 | FPLDAO | GRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 19105cdeb9afcb4c26351a9c327bc55c2ffa726fd8f27577696f199f785352d0 |
| DOC035-P0009-C001 | DOC035-P0009 / 9 | 448 | FPLDAOE | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 5a0320be837165ce775ddd842ae6b2de93fc76491badd129180ed894f8fef950 |
| DOC035-P0010-C001 | DOC035-P0010 / 10 | 160 | FLDO | GR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | ef767d14aadc9e07ae3e398e27460fbfee0c912826d0b22497044e7ddf71da60 |
| DOC035-P0011-C001 | DOC035-P0011 / 11 | 158 | FLIDA | PIGR | IRRELEVANT / X | IRRELEVANT / X | f51b1b4d5d1c0123d83f8ffc80f878ce0c13d5eed0168953517e06a1e5753c48 |
| DOC035-P0012-C001 | DOC035-P0012 / 12 | 240 | FLDE | GRE | OTHER_NEAR_MISS / V | IRRELEVANT / X | ff010429678e77055c41620d9936292e3df995d5ded8064f83a5929a4a4988e9 |
| DOC035-P0013-C001 | DOC035-P0013 / 13 | 56 | FD | GR | IRRELEVANT / X | IRRELEVANT / X | f4ba8b91e8cf0ec42ac72d7d6d91ca0fbae40bfbb7cd3d450c73d02037e51e16 |
| DOC035-P0014-C001 | DOC035-P0014 / 14 | 450 | FLIDAO | PIGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 1575cb9b7594c3b1210b3da49ff6d32ba07ac11a0749280ffe9e01bf65b7cd2e |
| DOC035-P0014-C002 | DOC035-P0014 / 14 | 90 | FLIDO | IGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 53e569033652faa9bb5a1c49b17af1e90bb06a68aecf81bd97cdb9f8f71d5ec4 |
| DOC035-P0015-C001 | DOC035-P0015 / 15 | 436 | FLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | a8b86847953c45ca91f94429ff1f32530ca2379b71cb07a27f1c135a223c9d6d |
| DOC035-P0016-C001 | DOC035-P0016 / 16 | 450 | FLIDAOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 2cea5d509d326098a66acd61fb92c20929b2ed2a113fe4de31db06b3f7c03d54 |
| DOC035-P0016-C002 | DOC035-P0016 / 16 | 126 | FLDAE | ROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | d00f2c4ddf28ca021ff5c7c19e94f975d0e92ca1416e79c9afb8f4d12d19d558 |
| DOC035-P0017-C001 | DOC035-P0017 / 17 | 450 | FLIDE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5280a14c6d4b65e5ce55390aea5c65f4844f2179a64e8ba8618626951962ed1e |
| DOC035-P0017-C002 | DOC035-P0017 / 17 | 112 | FLD | GRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 8e1e1b7ffdec1263e317a56758fa4745c2a3733ce9889ac6eed735c7c727beb4 |
| DOC035-P0018-C001 | DOC035-P0018 / 18 | 450 | FPLDAOE | GROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 38d264a4993066e256b3d865ffdfb9f5651116f906cd0f829603d5db2464ab6c |
| DOC035-P0018-C002 | DOC035-P0018 / 18 | 104 | FPLDO | GRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | e967402dbb6ed68830235034313de7522e46595956dbdbdcc96928cb48db76b1 |
| DOC035-P0019-C001 | DOC035-P0019 / 19 | 450 | FPLIDOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | d991780583bf84fa387426eef65537f006a1a01ab2845dd7b78137a5fe76d966 |
| DOC035-P0019-C002 | DOC035-P0019 / 19 | 112 | FLDE | ROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 8bf7e80db5301d80fb84983c7897f27912a24d60ce5e845976a48b9444ef834f |
| DOC035-P0020-C001 | DOC035-P0020 / 20 | 450 | FPLIDO | IGUO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | bf01170237dd1b0e5d31e55fab80e929f6075bc347ea0691229151a1c7e105a4 |
| DOC035-P0020-C002 | DOC035-P0020 / 20 | 169 | FPLDE | GUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | b5d7f509ac8fbdf268f33b13da0b19df752094958019997144378b2e04e39b83 |
| DOC035-P0021-C001 | DOC035-P0021 / 21 | 439 | FPLIDAE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 8108a63e3549fe95d1d50baed2edb97be703ce3d88130318d26b0b2868e8525d |
| DOC035-P0022-C001 | DOC035-P0022 / 22 | 450 | FPLID | IGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | f7bfabc9a9b18d0d9afb9db6ab0e99ffbe885b1d54f8941fc5eacd45a68c2323 |
| DOC035-P0022-C002 | DOC035-P0022 / 22 | 97 | FPLD | GURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 656b620d873997dc561a653c423f738615aba538ab6d72ce237f32a684888b91 |
| DOC035-P0023-C001 | DOC035-P0023 / 23 | 450 | FPLIDO | PIGURO | OTHER_NEAR_MISS / B | IRRELEVANT / X | b1fd582edd13166a436a89e101bdfdd029b54944c51e4f37feb89b5df81605a6 |
| DOC035-P0023-C002 | DOC035-P0023 / 23 | 108 | FLD | GRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 9469fe9c3044b5044daac4e60a36aaad893a3acbf440841ed82e437f5c46aa82 |
| DOC035-P0024-C001 | DOC035-P0024 / 24 | 450 | FPLIDAE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 36608ef0db774a544419725e958b92f47ad7e9e0f126cb848240baea2cb0376a |
| DOC035-P0024-C002 | DOC035-P0024 / 24 | 113 | FPLD | GRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | c00aaab34fa17f418c16197e0c9e61969fdb032e2661b76848bfd037e6274760 |
| DOC035-P0025-C001 | DOC035-P0025 / 25 | 356 | FPLDAO | PGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 66cf6e6432c5c74caaeab88c342dc95b75bf8cd5fc489cbf2fc9fc8bb4ec0caf |
| DOC035-P0026-C001 | DOC035-P0026 / 26 | 218 | FPLD | GRO | OTHER_NEAR_MISS / Q | IRRELEVANT / X | e825d5a93d4e84c90b907e72f9a003e4a47458b499061f3387f4851a5042a975 |
| DOC035-P0027-C001 | DOC035-P0027 / 27 | 43 | FD | R | IRRELEVANT / X | IRRELEVANT / X | 08f88b6d94710a0b46d5d9c2f4e8ea33f61c050dbd05cff0e65e07c4b77719c4 |
| DOC035-P0028-C001 | DOC035-P0028 / 28 | 420 | FPLIDA | PIGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | cda426e18d0ec090794aecf1a8fe11f97d93234d53c08259e31e87febe3b2f39 |
| DOC035-P0029-C001 | DOC035-P0029 / 29 | 450 | FPLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5f92409a386df5af102f203b4afe2abbdddcdc0feec9d7b0a060c94b332899a3 |
| DOC035-P0029-C002 | DOC035-P0029 / 29 | 103 | FPLDA | GUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 892075985e03aad1d69daccbdd1ed469e706dc4e08cf542e05beeda71a68c476 |
| DOC035-P0030-C001 | DOC035-P0030 / 30 | 450 | FPLIDA | IGUOE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 65c45ec8d81f4c3420e4bb41b78524062eaf9373823951acf03672e72cb34c7d |
| DOC035-P0030-C002 | DOC035-P0030 / 30 | 155 | FPLID | IGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | e35f95daece0fbbcc25f651f1778c7c01ed8c1e5e0283c8e76ac36d9bf4aeffd |
| DOC035-P0031-C001 | DOC035-P0031 / 31 | 340 | FPLIDO | IGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 91a8b26645ed1d4ddb814805aced4063b96dfce5622075e4c5bb3f24c25c641f |
| DOC035-P0032-C001 | DOC035-P0032 / 32 | 450 | FPLIDAOE | AIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 60442621145383ca8be3d890a0e6f5d0073057410b1ea20e658178f0275ab9d5 |
| DOC035-P0032-C002 | DOC035-P0032 / 32 | 164 | FLIDA | GRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 7cb477d4ce1c22dfbad89db6af6439b65aa05209d94aee8bbb10fc7b768897f0 |
| DOC035-P0033-C001 | DOC035-P0033 / 33 | 450 | FLIDAOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 2a022d1dfd0ea90de7facdb17a469d60ba4e94ec61f5987249413b8a2b22b456 |
| DOC035-P0033-C002 | DOC035-P0033 / 33 | 90 | FLO | UR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | c38cadadc49b8d821f6d74e0399e41153fcd344d0e58e640742efb9f9ffbc848 |
| DOC035-P0034-C001 | DOC035-P0034 / 34 | 436 | FPLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 28b4db028a459137ace48e032b66c0fe6929e974f06f5f107dd99c00bbb07b2a |
| DOC035-P0035-C001 | DOC035-P0035 / 35 | 450 | PLAO | GURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5076b6b641752dd91a96aee8789e2e86f4f1f0eb0930c01701f3c587bdbc9cad |
| DOC035-P0035-C002 | DOC035-P0035 / 35 | 125 | FPLO | URO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | d2ec502e7d00504467ffca5792080e30630ae07f3809861d405d7211f31429d6 |
| DOC035-P0036-C001 | DOC035-P0036 / 36 | 450 | PLIDAOE | GUROE | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | 69808df57df1147fe822fc9bfcfd337344ff94bf466d95f97300a1f4bbe34f0f |
| DOC035-P0036-C002 | DOC035-P0036 / 36 | 146 | FPLDAE | GUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 0eed245e5fcf2eb00af2cb446d62d3ab99f40644757478815b0cb582ea796ab6 |
| DOC035-P0037-C001 | DOC035-P0037 / 37 | 313 | FPLDOE | UROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5c592292bfc4a45e1d3a11e44e6edd9c7001e8377d35968feb425f539ff9d9e7 |
| DOC035-P0038-C001 | DOC035-P0038 / 38 | 434 | FPLIDAOE | AIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | a23209de1f2a3128c08e0f669caa1b5257afa09c926cfee3d6ad069109650222 |
| DOC035-P0039-C001 | DOC035-P0039 / 39 | 420 | FPLIAO | APIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | b439d92c24e6ba473b01fdce207700dc4f0c0882f205299a8922d3598faa1c02 |
| DOC035-P0040-C001 | DOC035-P0040 / 40 | 450 | FPLIDAO | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | fa24a795ab3d5f085112abe65fc3522df5ecb3c53e334b394855f8f05e671049 |
| DOC035-P0040-C002 | DOC035-P0040 / 40 | 81 | FLDAO | GUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 78375b2de59dd46e5b28481e6ef97cf1209f0c2f57328860e4f01346d90c11fe |
| DOC035-P0041-C001 | DOC035-P0041 / 41 | 450 | FPLIDAOE | AIGROE | OTHER_NEAR_MISS / B | IRRELEVANT / X | f53f8772493a217cbba20e8912748e23c07caa8f81d88428e725351c88c14df9 |
| DOC035-P0042-C001 | DOC035-P0042 / 42 | 450 | FPLIDOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | cee97863164da6dbbd6356c8f38e51e8b00d502a2ddaa1e25b14e5e4c8a9f34a |
| DOC035-P0042-C002 | DOC035-P0042 / 42 | 135 | FPLIDO | IURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 3bd8fbd7ac114be36c46cd666b8bfdad6c8ca2ce458c306a30169bb454e6df09 |
| DOC035-P0043-C001 | DOC035-P0043 / 43 | 450 | FLIDAOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 9b3d6c6dc7b7ee5ff3166aa15f7654aa0b47d8a02fe1803aadf286acaaee9096 |
| DOC035-P0043-C002 | DOC035-P0043 / 43 | 106 | FLIDAO | IRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | ed2acd5b0524896c2875fe313da23d724452c2975331d68d24a08500f13e3c23 |
| DOC035-P0044-C001 | DOC035-P0044 / 44 | 400 | FPLIDAOE | AIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 3cbd68a89fbcfaf837dc058bdf3375a2e868b6c2c611190be07cf4caaac4d746 |
| DOC035-P0045-C001 | DOC035-P0045 / 45 | 196 | FPLIDOE | PIGROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 98fef9fd6049b093809c07b433331f2d00c7da8a8336a25f64c605955839fe70 |
| DOC035-P0046-C001 | DOC035-P0046 / 46 | 243 | FPLIDAO | IGUROE | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | f4dc99ea0dcf9ce0028081964e296d0844d34b7f5d8938b7d54ce3ef38db5dcf |
| DOC035-P0047-C001 | DOC035-P0047 / 47 | 419 | FPLIAO | IROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | fcf19dcfeb61f02dfaa8bdfaa70728dc2fc8ba8ac1a3bda789ae12b1cc1ef646 |
| DOC035-P0048-C001 | DOC035-P0048 / 48 | 403 | FPLDO | URO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 61d6dabdd1e1a21ebf0a564f2fa4f9220e7fb5b0eaf1ab950892a58618f86920 |
| DOC035-P0049-C001 | DOC035-P0049 / 49 | 255 | FLDAO | AUROE | DESCRIPTOR / D | IRRELEVANT / X | e6afb4aa27a1250fb09d9248dc57f7a15fb3840d960692cfaa42b092bef15123 |
| DOC035-P0050-C001 | DOC035-P0050 / 50 | 429 | FPLIDO | PGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 41b9236d8b5b98b07ba6c69dbf9f1069322b400d480fca31337be0c563e735ca |
| DOC035-P0051-C001 | DOC035-P0051 / 51 | 442 | FPLIDAOE | AIUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 2731651ce432109f9c1f5d99775af823597fb5c6d9b3d9b008bcedd41628229a |
| DOC035-P0052-C001 | DOC035-P0052 / 52 | 70 | FLDO | RO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 83b3fc8c838ae518f7eb7f3b692b08c10794dc8db1d7fc6a143a15a115c03e22 |
| DOC035-P0053-C001 | DOC035-P0053 / 53 | 76 | FDA | R | IRRELEVANT / X | IRRELEVANT / X | 5563fe3f74101616b070a181444e3a58d7b57c17d9917ba94113f288da9f7c4e |
| DOC035-P0054-C001 | DOC035-P0054 / 54 | 397 | FLIDAOE | PIGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 851be069dc87f5363d073cfe046cdef3b5219b84b34a5d0c1b2f936fa8f60098 |
| DOC035-P0055-C001 | DOC035-P0055 / 55 | 450 | FPLIDAOE | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 510464661c8e7bfc01f632a383a8735cbf23c4ed5e9dae1b0c41c764293aceb4 |
| DOC035-P0055-C002 | DOC035-P0055 / 55 | 78 | FPLA | GRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | b2d78ec26a960c07d3286db16fcba9c62d808628a9b292fe17822237e832f69f |
| DOC035-P0056-C001 | DOC035-P0056 / 56 | 450 | FPLIDAO | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 6f18f20b3dea88203402a1269800a42f9e849f5e4debe158bbafff4064a00825 |
| DOC035-P0056-C002 | DOC035-P0056 / 56 | 117 | FLIDAO | IUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 7df94127345560edaeba7a2bfe614d52d7e4798ed4d004042db5c50c54cc415d |
| DOC035-P0057-C001 | DOC035-P0057 / 57 | 450 | FPLIDAOE | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | a8ff51598eca163258d1a9cd92d1419c7817124f0642ac5eff59bd40ba108386 |
| DOC035-P0057-C002 | DOC035-P0057 / 57 | 97 | FLIDAOE | IROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | d59a480f37fde2fac5f5dda03fd0d920402f51162ba3403904cc7a58ee3b4934 |
| DOC035-P0058-C001 | DOC035-P0058 / 58 | 428 | FLIDAO | IRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 750abda618dc9f3f37215eca6fb5457ec6b858c9b7ce4909ed0fd4d4dbbfb33f |
| DOC035-P0059-C001 | DOC035-P0059 / 59 | 450 | LIAOE | PIGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 0b090022ef72529bdf52f92863509a43903305138df552c337a8f8725bb2e1ad |
| DOC035-P0059-C002 | DOC035-P0059 / 59 | 97 | FLAO | PROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | b21491c67db71fca6a6ff78da0b3d67aee7a5aab8b75c6b2e80ce0871e0b63fc |
| DOC035-P0060-C001 | DOC035-P0060 / 60 | 450 | PLIDAO | PIGRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 2af6b5dd9581a1d122117c0f32d53b88eca5151dca4021653af1947d2aa5e1bf |
| DOC035-P0060-C002 | DOC035-P0060 / 60 | 149 | FLDAO | RO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 4afd6bb8697f84765101ff8dfaaa6ef04c53a4114891ca090abb0d07ce6289ee |
| DOC035-P0061-C001 | DOC035-P0061 / 61 | 448 | FPLDAOE | PGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | debd4404471c4d5875a85b1c358703e73d034671a7ae06f28457a743ac8eff95 |
| DOC035-P0062-C001 | DOC035-P0062 / 62 | 450 | FLIDAOE | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 9b33e9d8e4bc831013669989dfb702d4591acd1b026923dcce8be69a94ff392f |
| DOC035-P0062-C002 | DOC035-P0062 / 62 | 123 | FLDAO | RO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 1d1627f2d461ea97cc5ec427739e052735473d1077c804224bb5ae37fcdfa04f |
| DOC035-P0063-C001 | DOC035-P0063 / 63 | 450 | LDAOE | ROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | eebbc959747a139afa1cb18823767a815931590b4532075bcbfe6741091353be |
| DOC035-P0063-C002 | DOC035-P0063 / 63 | 171 | FLDAO | GRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | f2550ba39152f7a9b252ca5da2febfa652f4e727dc7eee7f39d1ae21cf192134 |
| DOC035-P0064-C001 | DOC035-P0064 / 64 | 450 | FLDAOE | OE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | b96cddfaa5400ade3a8fb6f4242a4d4e795aa2b0d03eed51b1af2579f6893d3e |
| DOC035-P0064-C002 | DOC035-P0064 / 64 | 120 | FLDAE | ROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | ff2db957d2fea0f938f54d2aa86ac6fdebdf72a10279bd3d475d7fd159af51a5 |
| DOC035-P0065-C001 | DOC035-P0065 / 65 | 450 | FLIDAOE | AIGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 6f000d0178dff6bd1c9ff878be646fb6c174224ec6ee4f1b93992ffe3760bc92 |
| DOC035-P0065-C002 | DOC035-P0065 / 65 | 109 | FLIDA | IRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 9b8b825dd84286f167c6f5bed08573b579166142020dd884391c28fdae847013 |
| DOC035-P0066-C001 | DOC035-P0066 / 66 | 450 | FPLIDAO | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 6c73587cdc4f74011bc4e8f4217874b641c3291421ae441db13364f9b55bf84d |
| DOC035-P0066-C002 | DOC035-P0066 / 66 | 135 | FIDAO | IURO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | d7258b4acf84492757fd596bbd08e55f7929c1d507f48c4e25bee53001359a3e |
| DOC035-P0067-C001 | DOC035-P0067 / 67 | 450 | FLIDAO | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 6d35451351da1e4bee8050042e3b96e6c65a079ded525daa12adefecc1535a5c |
| DOC035-P0067-C002 | DOC035-P0067 / 67 | 109 | FLIDA | IRO | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 8ab70f5b78c5901830d3c847178c9ec4ea3e53ae8f70f383b92cc983cb99aaa3 |
| DOC035-P0068-C001 | DOC035-P0068 / 68 | 437 | FLIDAOE | AIUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | aaa14a4e8e3ebc513c7fa21619e36d0727c5802b14720481ed46518fb1690a52 |
| DOC035-P0069-C001 | DOC035-P0069 / 69 | 450 | LIDAO | IOE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 8b440741b8a347d6cd5b12809da893073a775bd0bb261cf23e570d9729760cc9 |
| DOC035-P0069-C002 | DOC035-P0069 / 69 | 120 | FPLA | ROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 4cfba066fa48a30b983ae91157b9764e8c4aacc5b3d926d38d684b4aaf93cb55 |
| DOC035-P0070-C001 | DOC035-P0070 / 70 | 450 | FPLIDAOE | AIROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | 97eb4c46d0463972af5732e636d550b8b80690139c77ab6703998ff2a915bf7b |
| DOC035-P0070-C002 | DOC035-P0070 / 70 | 170 | FLIDAOE | AIGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | e3e88b1f86a520ccb73dbc66a5f2aa85564311a3ee86cc80ae53ac7416a6bb03 |
| DOC035-P0071-C001 | DOC035-P0071 / 71 | 385 | FLIDAO | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | d08f0530e450e75655498349041b448c02122b3d010037a0567ff3fe6afbe683 |
| DOC035-P0072-C001 | DOC035-P0072 / 72 | 409 | FPLIDAOE | AIGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | c1fd8fa182dc36581b3937394098c670ceb279897e39e8cba62b8a99d661d56e |
| DOC035-P0073-C001 | DOC035-P0073 / 73 | 366 | FPLIDAO | IGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | eaaa36dc8fd0c4f0f160b893a5ec9230be16fcfd016aa2d5eae56f92c9bea956 |
| DOC035-P0074-C001 | DOC035-P0074 / 74 | 414 | FPLIDAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 6868d3d509594598e89837644d9ff508612019f28c2ea2eaa5e25d479c1dd554 |
| DOC035-P0075-C001 | DOC035-P0075 / 75 | 443 | FPLIDAOE | AIGUROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | e2f9fc0ed2c0b3e682ee4ce88b60882c4285d1cd6a97f10efa3c55663f28a7bf |
| DOC035-P0076-C001 | DOC035-P0076 / 76 | 275 | FPLIDAOE | IGROE | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | c53694ca6c5f26369ccc0bdf2b4a6fe47ab82152648a986ec21eb5ad5a6a146d |
| DOC035-P0077-C001 | DOC035-P0077 / 77 | 57 | FLI | IGR | IRRELEVANT / X | IRRELEVANT / X | b2c51c68b10bb0312c19f4a207b379e1d4539bbe9eddac07d3eb83e1a6c8ccac |
| DOC035-P0078-C001 | DOC035-P0078 / 78 | 450 | FPLIDOE | PIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | fc7383f1e60df2ad4dc31c5b3b7709a05c1f842d653070541f3e92613232d79c |
| DOC035-P0078-C002 | DOC035-P0078 / 78 | 100 | FLID | IGR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 0506a96442e2d49df5338e3d41eece3667d2fc0ca2dcf9c8a85e46e7104b6efb |
| DOC035-P0079-C001 | DOC035-P0079 / 79 | 446 | FPLIDAOE | AIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 0ca22c2b0cd36e2bfd451085c3adf438739371819d8dc7c49245329ca60ac681 |
| DOC035-P0080-C001 | DOC035-P0080 / 80 | 450 | FLIDAE | PIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 93801bfa8f266bf27421a14c17d62e42f08ac669c394b27f38c779844a8701f6 |
| DOC035-P0080-C002 | DOC035-P0080 / 80 | 94 | FLD | GUR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 496e3b3fcb2fd15275bd825ac5850a51382e0860bf0818d2609d80c660a72409 |
| DOC035-P0081-C001 | DOC035-P0081 / 81 | 450 | FPLIDE | IGRE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 89f97c46d1c9b23129fdca85503a463d6426f3a60151e4c873708d434499a08d |
| DOC035-P0081-C002 | DOC035-P0081 / 81 | 171 | FLID | IGR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 94714cd332c41f8fc3bc06ba8318a038216643b94a997af7dc431addd7d4ee5c |
| DOC035-P0082-C001 | DOC035-P0082 / 82 | 448 | FPLIDE | PIGURE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 85355c087fa50a40ed706a7adeab48b6ec4dbb388f9c3aba304846b6d3106871 |
| DOC035-P0083-C001 | DOC035-P0083 / 83 | 388 | FPLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | d3695519ea6470b6c0faea2fa5aa15a8908d3584528050f600fa8b53a1c9787d |
| DOC035-P0084-C001 | DOC035-P0084 / 84 | 450 | FLIDAE | IGRE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 23e4c75b5c65f7003b6cdfc8aa5687f048f4719ad147ee644dda0245646a89c9 |
| DOC035-P0084-C002 | DOC035-P0084 / 84 | 104 | FLIDE | IGRE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 1acec4696fa31f4c0a3cda51ed0c48b7b8f93ad224073eebb08005840cd7835a |
| DOC035-P0085-C001 | DOC035-P0085 / 85 | 450 | FPLIDOE | IGUROE | OTHER_NEAR_MISS / B | IRRELEVANT / X | 5944933cc50b3a11781f7c116a551fb0f19ebb807466890a300a2cbcb20a4202 |
| DOC035-P0085-C002 | DOC035-P0085 / 85 | 105 | FLIE | IGRE | OTHER_NEAR_MISS / B | IRRELEVANT / X | 6ea0a01e18c7325925c6e579796074e9790ff9372ce7914a513909f7f80cc7c9 |
| DOC035-P0086-C001 | DOC035-P0086 / 86 | 450 | LIOE | IGUROE | OTHER_NEAR_MISS / B | IRRELEVANT / X | bab391b3dff75e115747ecccdce93b575c8852d754537efd6da6746d746b4c7a |
| DOC035-P0086-C002 | DOC035-P0086 / 86 | 141 | FLIDO | IGRO | OTHER_NEAR_MISS / B | IRRELEVANT / X | 9a630f784f94898a884721294b87b5282dc775fcfa77a09f2eb1f9af35bc663d |
| DOC035-P0087-C001 | DOC035-P0087 / 87 | 371 | FPLIDE | PIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 48d0940f1ac2872659cbdad7a90b7af85cf11bf18d9bca8841617b62c65a42b4 |
| DOC035-P0088-C001 | DOC035-P0088 / 88 | 429 | FPLDAOE | PGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 8beb9fc083fd1f1891e939e7ccd153bba1eb3640633f38fb4c582d7709c2f46b |
| DOC035-P0089-C001 | DOC035-P0089 / 89 | 363 | FPLIDAOE | PIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 4fc14946b36ea3a92b66ed2053b218b91ac844ca750eb3916f958baceeaa00bb |
| DOC035-P0090-C001 | DOC035-P0090 / 90 | 195 | FPLDA | GR | OTHER_NEAR_MISS / Q | IRRELEVANT / X | da425ed4dd2416915b51c9672cf9b4570f93d610d285b4bd4a6f2e6249e29f6d |
| DOC035-P0091-C001 | DOC035-P0091 / 91 | 54 | FLI | IGRO | IRRELEVANT / X | IRRELEVANT / X | 0e466da6c2e1564c8cf827de324ab03a1e677ae8e21e2706a2d12782e9c21cfc |
| DOC035-P0092-C001 | DOC035-P0092 / 92 | 450 | FPLIDOE | APIGUROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | 8cc1bd92b41eebff9dbbd56be6b9dda7e615e5ee3975362229b9e5cec90dcf5a |
| DOC035-P0092-C002 | DOC035-P0092 / 92 | 87 | FPLD | PGUR | OTHER_NEAR_MISS / S | IRRELEVANT / X | bbced89796b537127095abd62f176b1a292b765eb145abf24c4acb494684ad67 |
| DOC035-P0093-C001 | DOC035-P0093 / 93 | 423 | FPLIDO | PIGURO | OTHER_NEAR_MISS / S | IRRELEVANT / X | 588e9ff68985836feb85f692c090ff3604b3d47c544b71df1b77a1dc1e48f97d |
| DOC035-P0094-C001 | DOC035-P0094 / 94 | 450 | FPLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 3ab36622612378b57351f68b8bfa3bb9c59070e62be7963bdea56738555462ed |
| DOC035-P0094-C002 | DOC035-P0094 / 94 | 89 | FPLIDE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 7ee98d0d6ac9ab932b155e3d70b318913dbc8e7d9a96c4d3fcdefad7769ad85b |
| DOC035-P0095-C001 | DOC035-P0095 / 95 | 367 | FPLIDAOE | APGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | e4328f14c4cae7f2ecfa33bfb076a9c33fa7d624a8ea8f8fe1df2fab012fe8e5 |
| DOC035-P0096-C001 | DOC035-P0096 / 96 | 363 | FPLIDOE | APIGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 9d94ac3f3540c9e6cb09545b1e8af0125c8aa3c49c99c924e7b063068b3005a7 |
| DOC035-P0097-C001 | DOC035-P0097 / 97 | 391 | FPLID | PGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 69ec535c511aa0723bda80a6279a7bc9c4d8fdb96d60d4c546c8c91f1ffb6edf |
| DOC035-P0098-C001 | DOC035-P0098 / 98 | 321 | FPLIDO | PIGRO | INTENDED_OUTCOME / N | IRRELEVANT / X | 6c74acada77ce8e3314c311e87d64e50470da95f95eb1c52cf0c81c021a73801 |
| DOC035-P0099-C001 | DOC035-P0099 / 99 | 419 | FPLIDAO | IGURO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | fcae74903bd025f60d3bf12870d0f569b4328f1cc68f5762b1b2ef23485eec1b |
| DOC035-P0100-C001 | DOC035-P0100 / 100 | 213 | FPLIDAOE | AIGROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | 067fdc7c3451150b3b343dd9ffed4cf5fbc84a75410873d0a5bfbd950d8e454f |
| DOC035-P0101-C001 | DOC035-P0101 / 101 | 299 | FPLIDOE | PIGROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | f8e14dc2e0452023f80eedcb5b45475e261f01c9762f599c7efc6eecf48aa786 |
| DOC035-P0102-C001 | DOC035-P0102 / 102 | 274 | FPLIDAOE | PIGUROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 58e6bfc680eb8b70363f5a4bc83f1d969ea7d287043f939145f4b8c46e85e86e |
| DOC035-P0103-C001 | DOC035-P0103 / 103 | 93 | FI | IR | IRRELEVANT / X | IRRELEVANT / X | 23c3689caf1409031c51665ea4f4d499e9600ce1a0fd8b17d539ed2507056fa9 |
| DOC035-P0104-C001 | DOC035-P0104 / 104 | 400 | FPLDO | PGRO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 77c9b41dfa06065b2ff1d1b60d4c35fde13bf966bcbb13d26b285ef832d98994 |
| DOC035-P0105-C001 | DOC035-P0105 / 105 | 413 | FPIDAOE | UROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | d120094cdc3f59dde6abf3020daa46ad473fb4fa84bbfd102315f2cde5c13dee |
| DOC035-P0106-C001 | DOC035-P0106 / 106 | 450 | IOE | UROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | e01c554b7e7059f35c6ad87f7f1b2e925a9d0e4cb9f88d564576cfabb86f2ca6 |
| DOC035-P0106-C002 | DOC035-P0106 / 106 | 117 | FDO | RO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | c3014490e09f142df38676cf017ce6534388387599cc3f5210fb4b05a82a42bb |
| DOC035-P0107-C001 | DOC035-P0107 / 107 | 450 | PIE | IURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0ca3d685d6e9a10ceac171be1fbf9e0a6e38bd8f5e7f0e8d19bdaf7ba8410f10 |
| DOC035-P0107-C002 | DOC035-P0107 / 107 | 100 | FE | RE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9da82fbc0c74979fb82b0377bba4465a80569a2b311b4455335d89cdb402aed0 |
| DOC035-P0108-C001 | DOC035-P0108 / 108 | 450 | PLIDE | AIGRE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 0597ef3a03c163e061cea97422f834889b058b4b735f46468cea4c6c15f791a9 |
| DOC035-P0108-C002 | DOC035-P0108 / 108 | 92 | FID | IGR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 731bad6113b24755f27fe9cbba83528cfb57ec8874a060c535c9257321681bf9 |
| DOC035-P0109-C001 | DOC035-P0109 / 109 | 450 | LIOE | GURE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | a88a268f45c852364c5c41ad88ede015b59dbfabbb2468ffb79195c90726f0de |
| DOC035-P0109-C002 | DOC035-P0109 / 109 | 96 | FO | R | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | e74a071a60419d8eddd86cead1fb5437147cccc42df2dc4ca0f15f2a18ce29c6 |
| DOC035-P0110-C001 | DOC035-P0110 / 110 | 450 | PAO | PGURO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | ee794aea27377985eed3a96da55a6cabf12f9b272134ddb4cab10a0850eb0e3a |
| DOC035-P0110-C002 | DOC035-P0110 / 110 | 111 | FPDAO | PUR | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1f40a7f8b1e1b98bddae7d97bba6f0875341a8e88090537bcc2fa828ab095e18 |
| DOC035-P0111-C001 | DOC035-P0111 / 111 | 450 | O | URO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 885b1935bde46990fab4be339ecf77b227984a9b5e2cfb489b239e1acf1db794 |
| DOC035-P0111-C002 | DOC035-P0111 / 111 | 157 | FO | URO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | dbfc43b8d6abd21dd23ef1f5c019452c54244a28bf5e050e61b36c81e3a8a37c |
| DOC035-P0112-C001 | DOC035-P0112 / 112 | 450 | IAOE | UE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 546ce9de7806f35a8bba831d8ac151209c7d74d6e8b6943198d65ce2cc7ac4c1 |
| DOC035-P0112-C002 | DOC035-P0112 / 112 | 143 | FPDE | RE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 000da8b6e04401c2d9ba4bfbb9352cde548c168ac081359c81d7b315e8b37a0f |
| DOC035-P0113-C001 | DOC035-P0113 / 113 | 450 | LIOE | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | ecc59d6957c637891fe2fa09ef69de438e169664f295f135bc0a339ce0b0014e |
| DOC035-P0113-C002 | DOC035-P0113 / 113 | 144 | FOE | GROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 8bc3afb413507d76d0c7d9b25b89e738c1f8bf892672ff62df26ddf893ef5ce8 |
| DOC035-P0114-C001 | DOC035-P0114 / 114 | 450 | OE | GROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | f774b3acec71061bf7848684c04cb920899145bd2867177c242dc6a05fc5c565 |
| DOC035-P0114-C002 | DOC035-P0114 / 114 | 104 | FDO | RO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 7a8630d6d7576f4cbb06ba96f5e5f69f2bff46ebec2bf345993710dedd615571 |
| DOC035-P0115-C001 | DOC035-P0115 / 115 | 450 | PLDAOE | GROE | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | c742ac93884fd9f40cd0e4d59dc263454fc1d0782a7e27fb4d948e5100172b5b |
| DOC035-P0115-C002 | DOC035-P0115 / 115 | 155 | FP | GR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5ac7864f65c8b57fedab0edd9335c36aa5ce03ba36dc7a7af66a03a5f4744bf3 |
| DOC035-P0116-C001 | DOC035-P0116 / 116 | 450 | PLDOE | PGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | dfbe77ecc218aaeea294ed6ae4a25f3dbadc05fa3d279d99aaaecfd6ca336d50 |
| DOC035-P0116-C002 | DOC035-P0116 / 116 | 162 | FPDOE | ROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | e90ec7878b5cb8146e1cc72572c882955981014bdc9784004dd3a3331e4f70a5 |
| DOC035-P0117-C001 | DOC035-P0117 / 117 | 450 | PLIDAO | IGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | ae0c2ea875b40fee0a133433577965a843927c14b2f64bca653c5f2cb6c896d9 |
| DOC035-P0117-C002 | DOC035-P0117 / 117 | 124 | FPL | GR | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | bc9af4315978829027127b6d26cf6523871b87b57293d4f27786cd7d55d2f999 |
| DOC035-P0118-C001 | DOC035-P0118 / 118 | 395 | FPLIDOE | AIGROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | 230e6929889bcd1094ef7989d409dc6ad5d94155a6d66fc344c0343fd85c35c4 |
| DOC035-P0119-C001 | DOC035-P0119 / 119 | 450 | PLIDAOE | APIGUROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | 8c997d33f86d21ea3e1305e8f89ef65846f4a19a7af4311711eccd2a2f42259b |
| DOC035-P0119-C002 | DOC035-P0119 / 119 | 108 | FPLIE | AGUROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | efd4089998cf6f29cd2ee74bf4b833ef45952963c8b4f5a359c25ee4b965eeaa |
| DOC035-P0120-C001 | DOC035-P0120 / 120 | 448 | FPLIDAE | AIGROE | OTHER_NEAR_MISS / S | IRRELEVANT / X | 4d724ab214e26ae011308629e6f894c6ecae9a6454e9ed775bd064e9c8f92947 |
| DOC035-P0121-C001 | DOC035-P0121 / 121 | 444 | FLIDAO | PIGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 05d8411d8243554475175c940fa98d15964a7be9b671e9c3948c609dde760dce |
| DOC035-P0122-C001 | DOC035-P0122 / 122 | 321 | FPLIDA | PIGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | cbd996335379b0e8cff5b7a099d0c79fbffa36a54bcfa69c698dcde6862077ec |
| DOC035-P0123-C001 | DOC035-P0123 / 123 | 309 | FLIAOE | AIGRE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 4dbaa46412f937cb097d549dc16ca19a8b796bab3dedbc5ae3dd788f70e7ea7b |
| DOC035-P0124-C001 | DOC035-P0124 / 124 | 381 | FPLDAOE | PGUROE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | 7c90c2d1ff29fe8fbfaf9db2f1b17fd932c610f4b6c966212edbcf7bb5357f80 |
| DOC035-P0125-C001 | DOC035-P0125 / 125 | 120 | FPLE | AGRE | OTHER_NEAR_MISS / Q | IRRELEVANT / X | f8abddbe9b9c13d41396e7962bc4f1aed9bf340c55123e9c31211fc7cad14cf3 |
| DOC035-P0126-C001 | DOC035-P0126 / 126 | 450 | - | R | IRRELEVANT / X | IRRELEVANT / X | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC035-P0126-C002 | DOC035-P0126 / 126 | 244 | - | R | IRRELEVANT / X | IRRELEVANT / X | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC035-P0127-C001 | DOC035-P0127 / 127 | 132 | FPLIDAE | AIROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC035-P0129-C001 | DOC035-P0129 / 129 | 288 | FPLIDA | PIGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1dfa30f7e3949cbd4e3f44c32c5a04e6da11cad8c398f8a257b48e38d98686f0 |
| DOC036-P0001-C001 | DOC036-P0001 / 1 | 416 | PLIDOE | GUROE | IRRELEVANT / X | IRRELEVANT / X | aacc3d84a262aaac0a48d9090f4d5a5816dd588978d163c5e850bc8da0a7f8c0 |
| DOC036-P0002-C001 | DOC036-P0002 / 2 | 450 | LIDAOE | IGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | feafcf3b00e9e4e47821d7a48c38a7e4ee161c02cac9579af9a0ab998df0c8db |
| DOC036-P0002-C002 | DOC036-P0002 / 2 | 285 | LIDAOE | IGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | b72bf98897cfde02fe02bf96b6b454c1e96bd3022df6b0e5dd0ed93b2340a7e7 |
| DOC036-P0003-C001 | DOC036-P0003 / 3 | 450 | FPLDOE | GUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 760bd10f6d4134024041da4ee801d70140261b692b86795fe8b30d2e7a2bec5d |
| DOC036-P0003-C002 | DOC036-P0003 / 3 | 355 | PLIDOE | APGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1c65f832dff5bc3996ad2c6b75e8475bdda5836a3384fe583373fc77e28daf5f |
| DOC036-P0004-C001 | DOC036-P0004 / 4 | 450 | PLIDOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | c9fce98023ca9cbf392b0f7bb63a89195eee4abeb2a71d5de6a10c1ca4ebd6e2 |
| DOC036-P0004-C002 | DOC036-P0004 / 4 | 133 | PLIDO | IGRO | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 5bd9218100e7a4228ca798d7fa699b28ae32894b1e2d812e5bd1d4187a3f296e |
| DOC036-P0005-C001 | DOC036-P0005 / 5 | 450 | LIDAOE | AIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 387f62add60c75e919a52e6947709a6e533aeff9a5cfe6e4b4412ff2864642fc |
| DOC036-P0005-C002 | DOC036-P0005 / 5 | 146 | LIDAE | PIGROE | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | 18fe4854cc056b22de595d424373a23ea7c0dcdf7f7d27fe8ea3282bbb19e989 |
| DOC036-P0006-C001 | DOC036-P0006 / 6 | 46 | LD | RO | IRRELEVANT / X | IRRELEVANT / X | 143d33539a044d7ae3644c6795d8be389899cc0186826610e8623b6c566bc9ba |
| DOC036-P0007-C001 | DOC036-P0007 / 7 | 450 | PLIDOE | APIGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 3fc24dabd8d1dbfee40e4fbe14f8878a77ea79e252f650ee23439b2bd2dc2a04 |
| DOC036-P0007-C002 | DOC036-P0007 / 7 | 110 | LID | AIG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 1c3f4c31acec5941f8faeb277cf8697f7f4f221185d7ee4aab170f215975e5a8 |
| DOC036-P0008-C001 | DOC036-P0008 / 8 | 450 | PLDAOE | GROE | IRRELEVANT / X | IRRELEVANT / X | ca341e41056da1d1a0811a91badf5ee0c729b373a694ab8350e388a25bb945f8 |
| DOC036-P0008-C002 | DOC036-P0008 / 8 | 332 | LD | RO | IRRELEVANT / X | IRRELEVANT / X | a1fda2c258141109d8e81254c1913c321079c6ddd156e280c289ce13535b59e3 |
| DOC036-P0009-C001 | DOC036-P0009 / 9 | 450 | PIDAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 9770d3ce44f4e03a8d22a2a0da17740e93b004c8964c0744a5ec58da4fbf14b8 |
| DOC036-P0009-C002 | DOC036-P0009 / 9 | 313 | PLDAOE | AUROE | IRRELEVANT / X | IRRELEVANT / X | eb4ad2e79baeed0bcd828c9a184784bc66d57ffffb25eb1300b8f4924493aa2c |
| DOC036-P0010-C001 | DOC036-P0010 / 10 | 450 | PLDAOE | AGUROE | IRRELEVANT / X | IRRELEVANT / X | 1cfc15345d4d93ed683d2813712c29aa6fe419a87bc423ffe9f0cdf12ebfa590 |
| DOC036-P0010-C002 | DOC036-P0010 / 10 | 349 | PLIDO | PIGURO | IRRELEVANT / X | IRRELEVANT / X | 9dc4fa727fd29147153d79bf64ce54342c9139ba2483e58fa826792b4142d5e2 |
| DOC036-P0011-C001 | DOC036-P0011 / 11 | 450 | PDOE | PGUROE | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | 9724b0737170dbdd32ab7436ce09e1aa62178f4564502f699b51cfd2cdcc4e00 |
| DOC036-P0011-C002 | DOC036-P0011 / 11 | 393 | PDO | RO | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | b316f364da4e22e3dbefaef564bbd7e375e5ec66a56ff44191fef1dc3a43bf69 |
| DOC036-P0012-C001 | DOC036-P0012 / 12 | 450 | PLIDAOE | IGUROE | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | b6bcfb4788f18a2eac590d9dcf8b4ce1ad787297aebb93b71139d5b186c35e76 |
| DOC036-P0012-C002 | DOC036-P0012 / 12 | 219 | PLIDAO | IGURO | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | 81893aee468618761ac652545e9796cc02fb1ae61cdd84339378afd67d8d6915 |
| DOC036-P0013-C001 | DOC036-P0013 / 13 | 450 | LIDAOE | IGROE | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | 5a6c0cbd5413704290bca35bda686e37d53e580cfae5872b48b291141538423b |
| DOC036-P0013-C002 | DOC036-P0013 / 13 | 86 | LDA | RO | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | 4b1d0a6407c03eef5d6cbd0a79311fefd1357a0f5c8c071332b430186f673808 |
| DOC037-P0001-C001 | DOC037-P0001 / 1 | 8 | LD | R | IRRELEVANT / X | IRRELEVANT / X | 01cabe42ae196a60ef1ebc368489c4e3ffaf666cf5128048187b839ba15551d4 |
| DOC037-P0002-C001 | DOC037-P0002 / 2 | 66 | LIDA | PIGRO | IRRELEVANT / X | IRRELEVANT / X | 6f62dc0d4fbdb1c318736a4431f384185f2924edc74878489284e22224535b20 |
| DOC037-P0003-C001 | DOC037-P0003 / 3 | 175 | L | GUR | IRRELEVANT / X | IRRELEVANT / X | e66bb9aa360500c722bf9eb23ea8322604e2b2682d783aab165cacc0e453f56e |
| DOC037-P0004-C001 | DOC037-P0004 / 4 | 162 | LE | APGROE | IRRELEVANT / X | IRRELEVANT / X | a34b3810c61b2ceb1964dae30dda3c962a81b1737a4c10eca217f62fd1eb0d5f |
| DOC037-P0005-C001 | DOC037-P0005 / 5 | 127 | LIDA | PIGRO | IRRELEVANT / X | IRRELEVANT / X | c5e9d049d3e2b699a5b03b94bdb500ed02242bb9a8988c2eda739bc06ea19c50 |
| DOC037-P0006-C001 | DOC037-P0006 / 6 | 450 | PLIDOE | PIGUROE | IRRELEVANT / X | IRRELEVANT / X | b12bc00a66903ec9dd9651c0aaee1a0640aaee8db244e454e48479aed22f8dc0 |
| DOC037-P0006-C002 | DOC037-P0006 / 6 | 109 | LDOE | PGUROE | IRRELEVANT / X | IRRELEVANT / X | 8b130cefe67208d02d0416965aca4a6822f8bb757a27cebbe5cf5cbe0c20b61b |
| DOC037-P0007-C001 | DOC037-P0007 / 7 | 150 | LIDE | IGROE | IRRELEVANT / X | IRRELEVANT / X | a82dd3dc16b90c28a4a88b00cef5e7cd15fea14e5227317b36a5f031d6ac256a |
| DOC037-P0008-C001 | DOC037-P0008 / 8 | 80 | LD | GR | IRRELEVANT / X | IRRELEVANT / X | 86fe0943db861419d204563fd3c4d6ac3eb8ba11c539739f8eb051d953db0db7 |
| DOC037-P0009-C001 | DOC037-P0009 / 9 | 450 | PLIDOE | PGUROE | IRRELEVANT / X | IRRELEVANT / X | fd85fac8245586f76f220a53af016eadb53406b6d1842d5af59f524a32b85df1 |
| DOC037-P0009-C002 | DOC037-P0009 / 9 | 168 | PLD | PGRO | IRRELEVANT / X | IRRELEVANT / X | 7dea02032d6047927e5ecafab57a30163442af8f3b40c1bc2963448ec732a9f4 |
| DOC037-P0010-C001 | DOC037-P0010 / 10 | 392 | LIDAOE | PIGUROE | IRRELEVANT / X | IRRELEVANT / X | 8e1ab0150f4a6f363528d7b38c8bb5e19b3c11f8a1aaec9af0fa5727f503d255 |
| DOC037-P0011-C001 | DOC037-P0011 / 11 | 450 | LIDAOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | 8e3fe9b985457b4f7e67dd1d04e31b8f65985f708a76ce2df5dac85874ca5b32 |
| DOC037-P0011-C002 | DOC037-P0011 / 11 | 81 | LID | IGRO | IRRELEVANT / X | IRRELEVANT / X | b3915d26f6637d1a5f2d394448b298a7625ce9cfd5f7522b080723fd9e337966 |
| DOC037-P0012-C001 | DOC037-P0012 / 12 | 325 | LIDAOE | APIGRO | IRRELEVANT / X | IRRELEVANT / X | 67ab650e740b6e99fd8688ce13b4c752aded0fdda5e6a6aa10a07aab80e80b42 |
| DOC037-P0013-C001 | DOC037-P0013 / 13 | 442 | LIDOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | 711597068d072a2a1f05758119dfca48b9567cb8db0a0247612326f7cbe6f6d9 |
| DOC037-P0014-C001 | DOC037-P0014 / 14 | 179 | LDAOE | GRE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | bd2cdaf3362ad2f48e21282c7d7b7d755e70e51833cba01a02134f912dcc9c3d |
| DOC037-P0015-C001 | DOC037-P0015 / 15 | 418 | LIDOE | IGUROE | IRRELEVANT / X | IRRELEVANT / X | c187ef789e916010e9db41a5f0bf64c7f9522e69c313b2a0798b7ed4991e32ad |
| DOC037-P0016-C001 | DOC037-P0016 / 16 | 436 | PLIDAOE | PIGUROE | IRRELEVANT / X | IRRELEVANT / X | 47d36c64b9976c9e8b63fa2370d597816fc303d22ff6561b6661e8dddca6d542 |
| DOC037-P0017-C001 | DOC037-P0017 / 17 | 450 | PLIDOE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 568025c1f2b8531141654994ae17dadf3cbea2bab4f17b9ad95129bf16cfaee7 |
| DOC037-P0017-C002 | DOC037-P0017 / 17 | 148 | LIOE | IGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 5d3c283643be9b160c7152ff52ffce2f56e814c7869eb3a15c1ec716b9f03846 |
| DOC037-P0018-C001 | DOC037-P0018 / 18 | 450 | PLIDO | IGRO | IRRELEVANT / X | IRRELEVANT / X | edae7e769e26e28b1f394ce7aefc7ae77930431b926e85c9ec14a5e0d7cffb3f |
| DOC037-P0018-C002 | DOC037-P0018 / 18 | 76 | LO | GRO | IRRELEVANT / X | IRRELEVANT / X | 13da69dd9e763a951d8ff483557475d08dce3479b2c1dbe9e6c17eb3037f8bc7 |
| DOC037-P0019-C001 | DOC037-P0019 / 19 | 450 | PLIDAOE | AIGURO | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 51aaf17391d1bf72717f822e1587cfa29a9f6cb5031a93909c7c5f7612e98d6d |
| DOC037-P0019-C002 | DOC037-P0019 / 19 | 121 | PLIOE | AIGUROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | d4920930031d31d8103ba3f43a3d08f20501d93dd97552164e826b042c08c3a4 |
| DOC037-P0020-C001 | DOC037-P0020 / 20 | 450 | LIDOE | APIGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 47fe468bd200226cbba7b95a4aa25589ba7ca9c0ae7e50825b6de0704e794c9f |
| DOC037-P0020-C002 | DOC037-P0020 / 20 | 217 | LIDOE | APIGURO | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | f4eafffe9aad7f5e02703abeac2141deb4472543ac7d694a34f28f56871134d7 |
| DOC037-P0021-C001 | DOC037-P0021 / 21 | 260 | LIDA | IGURO | IRRELEVANT / X | IRRELEVANT / X | 77ac41dcbae1ac0bb158eefbeea76368a4fb81fdde28f641a2453fddb57f0e33 |
| DOC037-P0022-C001 | DOC037-P0022 / 22 | 450 | LIDAOE | PIGUROE | IRRELEVANT / X | IRRELEVANT / X | 92ac019c1aae7980bb1f412c895c49133790a1d6711b44e79978c4741b436881 |
| DOC037-P0022-C002 | DOC037-P0022 / 22 | 162 | LDAOE | E | IRRELEVANT / X | IRRELEVANT / X | 1174078de012d729bc07ba2dccb570ee021f56917a615a2b88449b3112b2d7c6 |
| DOC037-P0023-C001 | DOC037-P0023 / 23 | 450 | PLIDAOE | APIGURO | IRRELEVANT / X | IRRELEVANT / X | 7041923d3302847d7c0c1dce2faa844127be5c3a4d1b21fdec2899858b1622f1 |
| DOC037-P0023-C002 | DOC037-P0023 / 23 | 155 | LIDO | IGURO | IRRELEVANT / X | IRRELEVANT / X | 52d048d624e499807fd29ea411c6c9f7ee4401c33a7931097b6e4df61ed71d5b |
| DOC037-P0024-C001 | DOC037-P0024 / 24 | 450 | PLIDAE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | cb01ad2267aa4db3dfa0fc3055704645d92907fb32f2a6a56bdafdf625bc7fc0 |
| DOC037-P0024-C002 | DOC037-P0024 / 24 | 125 | PLDAE | GUROE | IRRELEVANT / X | IRRELEVANT / X | b5ac2f4b58c1ab0c075e553297d1c84310f564ba2c86fd29452162654e17aed0 |
| DOC037-P0025-C001 | DOC037-P0025 / 25 | 450 | PLIDAOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | 7692d2b8ea1e44c1875fb9a4a50539ac58a6412f385d9f5ba118549edcf6c2d0 |
| DOC037-P0025-C002 | DOC037-P0025 / 25 | 108 | LIOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | 966cd703b350116898f60c2860850596b71708d7cacda68b53bbc700d31070fa |
| DOC037-P0026-C001 | DOC037-P0026 / 26 | 450 | PLIDAOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | b57c484c9dc831fb5872b436497d24d422b5ca6200e1d52179c011efe58b3e34 |
| DOC037-P0026-C002 | DOC037-P0026 / 26 | 95 | PLIO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 601263948b5dcf6ec8df11579260a3d994b98d881cbe6d16f16018e2813df769 |
| DOC037-P0027-C001 | DOC037-P0027 / 27 | 204 | PLIDO | PIGURO | IRRELEVANT / X | IRRELEVANT / X | 2c1139506022da403fd9b729c0932eba39202b0bd777c12d18aa5b215e12cf6c |
| DOC037-P0028-C001 | DOC037-P0028 / 28 | 304 | LIDA | PIGURO | IRRELEVANT / X | IRRELEVANT / X | 09627d9ed9b2326f0fa6c89a4794112967b7d1992899f993d66596bd649f36fe |
| DOC037-P0029-C001 | DOC037-P0029 / 29 | 329 | PLIDE | IROE | IRRELEVANT / X | IRRELEVANT / X | 3839399d8d49d5b3888ad62381c0ab2f898cc363905ae42df9464c82dc3ea3a2 |
| DOC037-P0030-C001 | DOC037-P0030 / 30 | 299 | LIDOE | AIGROE | IRRELEVANT / X | IRRELEVANT / X | bc853899b12b606643fbfcb362bf24e344b8ba24ebc26a9fed48b4539e57b52b |
| DOC037-P0031-C001 | DOC037-P0031 / 31 | 252 | LDAE | GROE | IRRELEVANT / X | IRRELEVANT / X | b4761e01e0ee0568f02589191ec18ceb634cbc6cc7a4464a5ed38cc517e84f7a |
| DOC037-P0032-C001 | DOC037-P0032 / 32 | 286 | PLD | GURO | IRRELEVANT / X | IRRELEVANT / X | 6a9a98c05bcc42a1edabf3e45f95739b79c0729fe9e3afb1208b1aea8299781a |
| DOC037-P0033-C001 | DOC037-P0033 / 33 | 294 | PLIDAOE | APIUROE | IRRELEVANT / X | IRRELEVANT / X | 3f58fd5c25b972d3579efdba4b72441399ab59e71acfd266aa812875e41c849d |
| DOC037-P0034-C001 | DOC037-P0034 / 34 | 226 | LIDAOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | 90bab3e8f9fd902776847d8b6a7e9fa22ffa5edab45976c4e13f7022b76eccba |
| DOC037-P0035-C001 | DOC037-P0035 / 35 | 368 | LIDAOE | PIGUROE | IRRELEVANT / X | IRRELEVANT / X | a1469b02c698b263b999961e0219aa021d06eff204dbb23b4c1b7eac32470145 |
| DOC037-P0036-C001 | DOC037-P0036 / 36 | 307 | PLIDAOE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 6d9208582c21c17f87f9391ff36adc7e63dfc34bad04541f8e747cd99c1fc399 |
| DOC037-P0037-C001 | DOC037-P0037 / 37 | 313 | PLIDAE | AIGUROE | IRRELEVANT / X | IRRELEVANT / X | 7efd0380ea7384571b16f326e2a5c057e147486e6f6750f815c844260871be69 |
| DOC037-P0038-C001 | DOC037-P0038 / 38 | 351 | LDAOE | GUROE | IRRELEVANT / X | IRRELEVANT / X | 46d226a4665e755278dcbd356b54e42d18b2fcd234645e18862903b3f81f30b4 |
| DOC037-P0039-C001 | DOC037-P0039 / 39 | 246 | PLDAOE | AGROE | IRRELEVANT / X | IRRELEVANT / X | cf45b2d0ee51d67aba7c8c503f1998c25f4630edb3b679df087d67728f8c8333 |
| DOC037-P0040-C001 | DOC037-P0040 / 40 | 189 | PLDA | GUROE | IRRELEVANT / X | IRRELEVANT / X | 14d45b3ad01f2b3bf66a9a707cbd23753fee4216730aa2c168fc878dd3f234d5 |
| DOC037-P0041-C001 | DOC037-P0041 / 41 | 182 | LIDO | PIGRO | IRRELEVANT / X | IRRELEVANT / X | 59f4744cbe200fc41503dc9df97722c6eff74231f9168d0e858b2b45b25c59de |
| DOC037-P0042-C001 | DOC037-P0042 / 42 | 203 | LIDO | PIGRO | IRRELEVANT / X | IRRELEVANT / X | 7a513434f6ef9eaca2dd0f83d8364ea754adf24fb6180e99826f8792534d8508 |
| DOC037-P0043-C001 | DOC037-P0043 / 43 | 439 | LDAE | GROE | IRRELEVANT / X | IRRELEVANT / X | 74d00aa2d342998e47b8b1df170a323ee9e6f13cc0da25859c604dc5f75321af |
| DOC037-P0044-C001 | DOC037-P0044 / 44 | 318 | PLDE | GUROE | IRRELEVANT / X | IRRELEVANT / X | 9de5f844839f781fcfba12f1f1dfae1c5de387248b935ab424c74ed9754a3777 |
| DOC037-P0045-C001 | DOC037-P0045 / 45 | 272 | PLIDAE | AIROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | cb8e3b943d031ca1dc002b3c68dc40bcedff61ed400dd9dc0f928cee6508c0da |
| DOC037-P0046-C001 | DOC037-P0046 / 46 | 262 | LIDA | IGUROE | IRRELEVANT / X | IRRELEVANT / X | 0a7c3a76395ed30ca2ff7bc3b1cc704030d2a0d72c37acccf04f5f3ae7365466 |
| DOC037-P0047-C001 | DOC037-P0047 / 47 | 299 | PLIDAOE | AIGROE | IRRELEVANT / X | IRRELEVANT / X | 233caf7baceca543fd92473b7df44fcf4f348343185f13f32a58a9b51a974a22 |
| DOC037-P0048-C001 | DOC037-P0048 / 48 | 385 | LIDAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | 12ac32e97c4e460af1c012985010f273a5fa7902ecc4d05b0c2d4a27c5157505 |
| DOC037-P0049-C001 | DOC037-P0049 / 49 | 450 | LIDAOE | PIGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | d4870365c4bd64e06d848083198cca4471ee4f326bf32e450cc43daeadcf0ef8 |
| DOC037-P0049-C002 | DOC037-P0049 / 49 | 125 | LDE | GROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 1b01750c6b980cc611d3c3e54ce3dfeac0b140c01723ea6b95f9bc48cbd38c8a |
| DOC037-P0050-C001 | DOC037-P0050 / 50 | 450 | PLIDAOE | IGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 9c57a0e7ac5f7fbc4c3a2ab45b266046ac012e052cecb2073c3e153fdd7de32a |
| DOC037-P0050-C002 | DOC037-P0050 / 50 | 117 | LID | IGR | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 118f978a7e74e8cc4e94712b913faa65c1f926797b25c9da6c22676924a18197 |
| DOC037-P0051-C001 | DOC037-P0051 / 51 | 345 | PLIDAOE | APIGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 38e02bb1aa69b1b816cae715cadd41f9dd6b1b233f9843cfb81185f00584068a |
| DOC037-P0052-C001 | DOC037-P0052 / 52 | 450 | LIDAOE | AIGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 6a2f49199b6a71643ebe444d3294b0797b193461750205b8e5162b04b9e2d0ae |
| DOC037-P0052-C002 | DOC037-P0052 / 52 | 153 | LDOE | AGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | d8b82f729d7787a3fda6d2fbf9408c3af01d396470d4a38cd3499c50db52801f |
| DOC037-P0053-C001 | DOC037-P0053 / 53 | 201 | LDE | GURE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 16c1e23d17ec9e7696d1d4dd843fe2d09bff9582596a0e75e5ca57ff938a8b79 |
| DOC037-P0054-C001 | DOC037-P0054 / 54 | 267 | LIDAE | IGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 50fc00ffbc00d40c5e07cbb7a75064774ec72f1b665ba5b1b225cf0b58eed241 |
| DOC037-P0055-C001 | DOC037-P0055 / 55 | 450 | LDOE | AGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 1e064942a82faaff15f4822c155e3ac4d1840b776976d7c292d9e961961c4cdb |
| DOC037-P0055-C002 | DOC037-P0055 / 55 | 240 | LDAE | AGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 8a62340b143cc0b90ae62255f4bced6d0f41d6ca8fc5c0a72ae4018b2565926c |
| DOC037-P0056-C001 | DOC037-P0056 / 56 | 450 | PLIDOE | IGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 9a3d3eb8a9a0b659027511b84b575733d158faf6c2be54f23c6e1150479840ce |
| DOC037-P0056-C002 | DOC037-P0056 / 56 | 297 | LDAE | GURE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 222704146a314d0056f28b48bf808445907585ab33a5224f8c3b8e9d821d078b |
| DOC037-P0057-C001 | DOC037-P0057 / 57 | 440 | LIDOE | IGUROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | 56ccc3dab6efe7021eee846c3aa50d6aa285cf8a26124802ca6ec8a1d3d7fa36 |
| DOC037-P0058-C001 | DOC037-P0058 / 58 | 307 | LIDAE | PIGROE | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | d5934c0c6cd2be6b9ba93913e467040a9ac7dc7e651583d1b8863922a1182fb3 |
| DOC037-P0059-C001 | DOC037-P0059 / 59 | 305 | LDAOE | APGROE | IRRELEVANT / X | IRRELEVANT / X | 7aea60cdb19a564001a70141fd985bc92cb58be351aee538e9701dd213845ba5 |
| DOC037-P0060-C001 | DOC037-P0060 / 60 | 323 | LIDAOE | IROE | IRRELEVANT / X | IRRELEVANT / X | 3f9a88fa32b21cad8abb9997050c46665b369d307fa2d23ef69c500f3870dd49 |
| DOC037-P0061-C001 | DOC037-P0061 / 61 | 450 | PLIDAOE | AIUROE | IRRELEVANT / X | IRRELEVANT / X | 8d2d00f1bc5809f887dbaca2e5ed94d98b5883f462d3123a5cf98638762be9d0 |
| DOC037-P0061-C002 | DOC037-P0061 / 61 | 176 | LIAE | AIROE | IRRELEVANT / X | IRRELEVANT / X | 4c42b85ee721f5fb0a91b1955224c401699ac9e0d98dbccf3f2710569a1c8d06 |
| DOC037-P0062-C001 | DOC037-P0062 / 62 | 450 | LDOE | AGRE | IRRELEVANT / X | IRRELEVANT / X | b1f8a978fd5d69953922b03cf8768f6bb16ef38e26259805c3a26ba252542996 |
| DOC037-P0062-C002 | DOC037-P0062 / 62 | 204 | PLIAE | AIGURO | IRRELEVANT / X | IRRELEVANT / X | 25cd36b43df97a874b96a003941256c7a7331764355b3f451bfce1ffbb27e491 |
| DOC037-P0063-C001 | DOC037-P0063 / 63 | 450 | LDAOE | GROE | IRRELEVANT / X | IRRELEVANT / X | 6981ff96b69c1006344c63bef033d5423ef206c952e7f5f77081065452eeda2c |
| DOC037-P0063-C002 | DOC037-P0063 / 63 | 162 | PLIAOE | IUROE | IRRELEVANT / X | IRRELEVANT / X | 4f039528ca5df967bb66463c7d0ec69b6629ac4e2fe8900140a4ef71ec093562 |
| DOC037-P0064-C001 | DOC037-P0064 / 64 | 450 | LIDAOE | AIGUROE | IRRELEVANT / X | IRRELEVANT / X | 0601f181df6e541d3a002c56e2a7a6060320016d6795de77ed2390b20d5932b6 |
| DOC037-P0064-C002 | DOC037-P0064 / 64 | 160 | LI | IO | IRRELEVANT / X | IRRELEVANT / X | 3a901aa91e167a786dcee8aa6af7b47b2aba6868295f9b0acb0c3c3ec256ab81 |
| DOC037-P0065-C001 | DOC037-P0065 / 65 | 450 | LIDAOE | IGUROE | IRRELEVANT / X | IRRELEVANT / X | b97c842f0822dc34bb11f4f39232168f79c9b25fd9d9a4d7932acf8fff1114fc |
| DOC037-P0065-C002 | DOC037-P0065 / 65 | 199 | LD | RO | IRRELEVANT / X | IRRELEVANT / X | de1cd5167d57bcb86624117ca9568451b7c84e44a42022c612b90d0e010494d0 |
| DOC037-P0066-C001 | DOC037-P0066 / 66 | 164 | LIDE | PIGURE | IRRELEVANT / X | IRRELEVANT / X | 2fd286b3bdedcf4e163fdb3ba92e88ab87125f3455c01c21d4eb9a9b91b00300 |
| DOC038-P0001-C001 | DOC038-P0001 / 1 | 355 | IOE | APIRE | IRRELEVANT / X | IRRELEVANT / X | 936071ba81b7bb24a735e5789628459458db848a79edaf559b4633deb2908772 |
| DOC038-P0002-C001 | DOC038-P0002 / 2 | 450 | PLIOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | 4df0e80bb68c8f70d772f797fdcda4283946a50eea8d6aa894314ca85c6f579f |
| DOC038-P0002-C002 | DOC038-P0002 / 2 | 259 | IOE | PIGROE | IRRELEVANT / X | IRRELEVANT / X | 9296d6e57b16218e59b2d6ec5e1302e00b8c968f125fff4ffab0d7a147a2f001 |
| DOC038-P0003-C001 | DOC038-P0003 / 3 | 450 | IDAOE | PIROE | IRRELEVANT / X | IRRELEVANT / X | 36bec81ffcd7f604ac1dce9e0d7dc52d09049162e0649524c4f0c699c99d7bee |
| DOC038-P0003-C002 | DOC038-P0003 / 3 | 108 | E | RE | IRRELEVANT / X | IRRELEVANT / X | 375489a602629e26fe291871d195fd251bb3c6320c76c61dc43710ce501d9d60 |
| DOC038-P0004-C001 | DOC038-P0004 / 4 | 450 | LIDAOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | 0c3314791a7d9ba6854620b89e60c4106c13afaec55d8926c479700e2ec1ecd1 |
| DOC038-P0004-C002 | DOC038-P0004 / 4 | 116 | OE | AO | IRRELEVANT / X | IRRELEVANT / X | 4a738cded9400b2d4f0dc24a7b42b5f839c0ffbfa79ce6deae10c9b1f4abd426 |
| DOC038-P0005-C001 | DOC038-P0005 / 5 | 443 | PLIAOE | APIGUROE | INTENDED_OUTCOME / N | IRRELEVANT / X | d4452770967bd72850cd0845e2aa7e0925d8038924eff55a7cfa111695f31828 |
| DOC038-P0006-C001 | DOC038-P0006 / 6 | 450 | PAOE | APGUROE | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | 108803714e9a6b6f11fa12bba5b77b167c3500369c655ae2509ff92dafd57403 |
| DOC038-P0006-C002 | DOC038-P0006 / 6 | 102 | AOE | APROE | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | bc1285ce6a8f251d46662879c9f958837fc8f24d0041a709c3fb21344e2a81e8 |
| DOC038-P0007-C001 | DOC038-P0007 / 7 | 429 | PIDOE | APIUROE | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | 9f370446cd1d7cccb63f84917dca0233b867eda0d9187b16555fe2e26d366408 |
| DOC039-P0001-C001 | DOC039-P0001 / 1 | 27 | LDE | PGRE | IRRELEVANT / X | IRRELEVANT / X | 63fd3b175bd280351cb43ddb6cae2a5b1a24220fbdf7369c091d191ece97938f |
| DOC039-P0003-C001 | DOC039-P0003 / 3 | 14 | LDE | PGE | IRRELEVANT / X | IRRELEVANT / X | 05271c022e61702a85241604e372bbe06cfb18b1b3b39f03987ff10284a2738a |
| DOC039-P0004-C001 | DOC039-P0004 / 4 | 450 | LIDAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | bf8eed0f779cdd3ab97727c999c9bfd118b12b9fa385a6d573a79fc77e1f25da |
| DOC039-P0004-C002 | DOC039-P0004 / 4 | 93 | LIDO | IGO | IRRELEVANT / X | IRRELEVANT / X | a9109ea40834535b552d9f5d811e32bd45dec395392979037364d7b36f2791ec |
| DOC039-P0005-C001 | DOC039-P0005 / 5 | 89 | PLDA | RO | IRRELEVANT / X | IRRELEVANT / X | 6372c844ba40af63bc6312ef2d159ae36d6e425a1a5cbc7767bbb4525b88708a |
| DOC039-P0006-C001 | DOC039-P0006 / 6 | 1 | - | - | IRRELEVANT / X | IRRELEVANT / X | 7872078d6758f5d336983566ccb975dfa520d32ed74719844c80635d26355736 |
| DOC039-P0007-C001 | DOC039-P0007 / 7 | 290 | PLIDAOE | FAPIGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 44bd4812abd2f53a5d00292a268261cfd26d588f65c62b0d0a69ee8d57aa7417 |
| DOC039-P0008-C001 | DOC039-P0008 / 8 | 65 | LD | GUR | IRRELEVANT / X | IRRELEVANT / X | 6112f34151e911472bbcc0afc165f31961eccc31b06e26b1a370628eaadf649d |
| DOC039-P0009-C001 | DOC039-P0009 / 9 | 403 | LIDAOE | IGROE | IRRELEVANT / X | IRRELEVANT / X | 48a369b662c11a376df224fcf08bc01e146ce535ceeaaf4e78915e0b4b7bdfa5 |
| DOC039-P0010-C001 | DOC039-P0010 / 10 | 265 | PLDOE | GUROE | IRRELEVANT / X | IRRELEVANT / X | 332b89f185034b1a812a79c7faa72a4df919e919e5c75aabe83b9c9ff8be2e2a |
| DOC039-P0011-C001 | DOC039-P0011 / 11 | 419 | LDAE | GROE | IRRELEVANT / X | IRRELEVANT / X | 22ee42be0a73a215741d495acb9456205f4b5d4348238c0562891e362b7c48ab |
| DOC039-P0012-C001 | DOC039-P0012 / 12 | 327 | PLDAOE | PGUROE | IRRELEVANT / X | IRRELEVANT / X | 2f2fb128560cf716839b78be68bd72721475c26615182019bd26ef7aad0c7582 |
| DOC039-P0013-C001 | DOC039-P0013 / 13 | 387 | PLIDAOE | PIGURE | IRRELEVANT / X | IRRELEVANT / X | 48bd6b283a2ce740d3829d2542cbec826720021306158251c949fe6cc17c4e79 |
| DOC039-P0014-C001 | DOC039-P0014 / 14 | 4 | - | - | IRRELEVANT / X | IRRELEVANT / X | 90cec7b45cc623df473f41655555786936238053d58975a9245823d92bcd532b |
| DOC039-P0015-C001 | DOC039-P0015 / 15 | 229 | PLDAOE | GUROE | IRRELEVANT / X | IRRELEVANT / X | 3d9319e06f470c31a3b09be84925073f47543bdd54be25c6fc7e9b8818d45fc0 |
| DOC039-P0016-C001 | DOC039-P0016 / 16 | 254 | PLIDA | IGRO | IRRELEVANT / X | IRRELEVANT / X | 172825f8d60bbe277e24551a815723d5ea73b8dd842bc694091405f8a44b5460 |
| DOC039-P0017-C001 | DOC039-P0017 / 17 | 298 | PLIDO | IGURO | IRRELEVANT / X | IRRELEVANT / X | f6f754af725bc19a8bd0f0a0341a6596ad2e7bb417cffd80f3e9b203a4b7ef35 |
| DOC039-P0018-C001 | DOC039-P0018 / 18 | 2 | - | - | IRRELEVANT / X | IRRELEVANT / X | 397495ce6b68d4a0f9af713e9272ed11145e8d99455d517b13ee751e2052b0d4 |
| DOC039-P0019-C001 | DOC039-P0019 / 19 | 177 | PLIDAO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 09e85643ceda1ced84492991ee22b0885c3ed25804d202ac9aebcfbc96d75095 |
| DOC039-P0020-C001 | DOC039-P0020 / 20 | 450 | LIDAOE | APIGRO | IRRELEVANT / X | IRRELEVANT / X | c95a31d9f9b868e031d6464499ab481a2c532d3540a4b87f98d803a1097f8f7a |
| DOC039-P0020-C002 | DOC039-P0020 / 20 | 79 | LD | GRO | IRRELEVANT / X | IRRELEVANT / X | 0ce51073e96d25ae6255b5a413dcbb53ada95659f089d546087fc79311e13c6a |
| DOC039-P0021-C001 | DOC039-P0021 / 21 | 448 | LIDAOE | AIGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 1db93292856daac8c1f5779e8b330836d50bf570cf690c4630d9f56ca940f2e5 |
| DOC039-P0022-C001 | DOC039-P0022 / 22 | 302 | PLDOE | GUROE | IRRELEVANT / X | IRRELEVANT / X | 47d9235ce53bcbab1878129369024af365709bea01f017133029397bca40667b |
| DOC039-P0023-C001 | DOC039-P0023 / 23 | 323 | PLIDAO | IGUROE | IRRELEVANT / X | IRRELEVANT / X | aedc4e427e6da693335a8f4c6bf7953cb613d557e9b05a0d230e6e92383dc012 |
| DOC039-P0024-C001 | DOC039-P0024 / 24 | 408 | PLIAOE | APIGROE | IRRELEVANT / X | IRRELEVANT / X | a649f7e2274062360166e30163c0169b23e4eaa2b3f96cd403b0ae6a90744675 |
| DOC039-P0025-C001 | DOC039-P0025 / 25 | 450 | PLIDAOE | AIGUROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 9e6b16c5f895d7347697b9605fa15408aeb04bdee6b2a3764e579ed69d484b82 |
| DOC039-P0026-C001 | DOC039-P0026 / 26 | 3 | - | - | IRRELEVANT / X | IRRELEVANT / X | 796c69cf1ed070f19674b5a6dc643bdaf01b1199bea75a92083e8147848ad1e0 |
| DOC039-P0027-C001 | DOC039-P0027 / 27 | 401 | LIDAE | AIGURE | IRRELEVANT / X | IRRELEVANT / X | e987768cdd047424bd95ae5e334595dc06ffd192f63e4dab9c1874199077dbbf |
| DOC039-P0028-C001 | DOC039-P0028 / 28 | 450 | LIDAO | IGROE | IRRELEVANT / X | IRRELEVANT / X | a20e786debddc67114af753e4e1d70ea53c411dc0e6777a7376537290b299aa9 |
| DOC039-P0028-C002 | DOC039-P0028 / 28 | 109 | LD | GRO | IRRELEVANT / X | IRRELEVANT / X | 26ac66edaf6e072dcb5d182bfe79078a6fd146a72c7d04e30aea73bb2bd8c89b |
| DOC039-P0029-C001 | DOC039-P0029 / 29 | 397 | LIDAO | IGROE | IRRELEVANT / X | IRRELEVANT / X | 1033a45f132a3cd2dd30285b211c260e8cb4dee96297793298c462f4c76f0f03 |
| DOC039-P0030-C001 | DOC039-P0030 / 30 | 450 | PLIDO | IGR | IRRELEVANT / X | IRRELEVANT / X | 4f760fab8b234698d6e80a126890921bebaa909f03056ae9ef0236591cd66df8 |
| DOC039-P0030-C002 | DOC039-P0030 / 30 | 256 | LIDO | IGR | IRRELEVANT / X | IRRELEVANT / X | 768c404e150302e6ab48d3787bbf17dce5db1cf5328897b84961505105ab6480 |
| DOC039-P0031-C001 | DOC039-P0031 / 31 | 218 | PLIDAO | IGRO | IRRELEVANT / X | IRRELEVANT / X | fdd859514116796c621aaa9bb3e485f04d3bb10cd70b9c5cc473315affb9c580 |
| DOC039-P0033-C001 | DOC039-P0033 / 33 | 3 | P | R | IRRELEVANT / X | IRRELEVANT / X | 7f104550c7cc3f336b39f3b8684ea894de4ac8a1c1156020a15e800f52c9adbd |
| DOC039-P0034-C001 | DOC039-P0034 / 34 | 171 | LDO | GRO | IRRELEVANT / X | IRRELEVANT / X | 2e49f958cc3a3aabd056623bac0e098df2ec584a103d2a0ceaf537801a0c7dd8 |
| DOC039-P0035-C001 | DOC039-P0035 / 35 | 220 | LDAO | PGROE | IRRELEVANT / X | IRRELEVANT / X | 39a3a00b599e681b3c6b67400295b35cb2063d55f367bbcc0a35271bf0926207 |
| DOC039-P0036-C001 | DOC039-P0036 / 36 | 107 | PLIDO | IGR | IRRELEVANT / X | IRRELEVANT / X | a790d08fc10116b475bb015783438865ed59bf9d2b67b634eea00e7f1198f660 |
| DOC039-P0037-C001 | DOC039-P0037 / 37 | 220 | LIDO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 9c2438f2290a2bd2ad239b63f1ed1faf7010efd3cf43c56d380d1024539df748 |
| DOC039-P0038-C001 | DOC039-P0038 / 38 | 139 | LIDAO | PIGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 1f07af6d3697dbb5baf34b0d8f97a0c9252d4c30ba45495546be8d84df561717 |
| DOC039-P0039-C001 | DOC039-P0039 / 39 | 262 | LIDAOE | PIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 38aa3fe2d99b87b45493d6f0a3bc5052f46af244ca87eb0621ded6c5798e30f7 |
| DOC039-P0040-C001 | DOC039-P0040 / 40 | 120 | LDO | GRO | IRRELEVANT / X | IRRELEVANT / X | 8da4e124726a11c2f2f5c4a9c305bda7b6e11b7c3ea1687f729a0fae7a4dcf73 |
| DOC039-P0041-C001 | DOC039-P0041 / 41 | 223 | PLIDO | IGURO | IRRELEVANT / X | IRRELEVANT / X | 941906349377592b0df47ca7c2186beee62e24e577f3de2778870b74dcb5c02e |
| DOC039-P0043-C001 | DOC039-P0043 / 43 | 3 | - | R | IRRELEVANT / X | IRRELEVANT / X | 1ef5a23434e9cc1b16642854199e4efde10b2534a163715cad2e9895a741ab51 |
| DOC039-P0044-C001 | DOC039-P0044 / 44 | 142 | LDA | GROE | IRRELEVANT / X | IRRELEVANT / X | 455d9de5103492c90ce95d0fd56fdde0c34a9f0fabbed451c0b98308c05b956e |
| DOC039-P0045-C001 | DOC039-P0045 / 45 | 337 | LDAOE | GROE | IRRELEVANT / X | IRRELEVANT / X | 4f070b07808a036fb2a689015ed22ef9e39e2c6112dbc3fa08e1c9e6ff1b3022 |
| DOC039-P0046-C001 | DOC039-P0046 / 46 | 137 | LD | GRO | IRRELEVANT / X | IRRELEVANT / X | 9ade0c4ca6735a3ca53679fe6cf7cb94ba3d636f5b1eb3dd6f7118b2da0db8a9 |
| DOC039-P0047-C001 | DOC039-P0047 / 47 | 280 | LDA | GRO | IRRELEVANT / X | IRRELEVANT / X | ea70953f5eadffa02f48d83b3c97ef94888084e8941902eca8655ea8b73ebd69 |
| DOC039-P0048-C001 | DOC039-P0048 / 48 | 165 | LIDAOE | APIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | b9eaed87311e734aa80e63ae1f9473ab105093ef52960e403b2e4bb483cbd9ca |
| DOC039-P0049-C001 | DOC039-P0049 / 49 | 215 | LIDOE | AIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | bd9ae9bd21a96ed95206d30e29261aa6de0f3400eea0e7edaec7ed66c3c5dcdb |
| DOC039-P0051-C001 | DOC039-P0051 / 51 | 4 | L | RO | IRRELEVANT / X | IRRELEVANT / X | 35729971f1ec7fe215293eca95d2eb0beb24d1768d0628a7504bffa39bbbf7bc |
| DOC039-P0052-C001 | DOC039-P0052 / 52 | 168 | LIDO | IGRO | IRRELEVANT / X | IRRELEVANT / X | bc1bf7c8e2b5885e80fbec11f06b71df9e3ee808b88e75e1e9620e7fcac6a99a |
| DOC039-P0053-C001 | DOC039-P0053 / 53 | 258 | LDAO | GROE | IRRELEVANT / X | IRRELEVANT / X | 4665856995b90dde22ac36faf2a1e65c781b75e2f7791e39441f836c5b70b862 |
| DOC039-P0054-C001 | DOC039-P0054 / 54 | 153 | LID | IGURO | IRRELEVANT / X | IRRELEVANT / X | a1da5437c4e40607e9322391b71148e0158e39bb3dd35a9b1e87cc6b2807b311 |
| DOC039-P0055-C001 | DOC039-P0055 / 55 | 252 | LID | IGURO | IRRELEVANT / X | IRRELEVANT / X | 6c607e83fea6e17d139b82876ae45f235adc53714e89f7c86c385bda0177dd11 |
| DOC039-P0056-C001 | DOC039-P0056 / 56 | 152 | LIDAO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 37c626d20839eb5856992ecae7ccb4dcaccf9b2f27cb2bab2ca607fdf26893c0 |
| DOC039-P0057-C001 | DOC039-P0057 / 57 | 273 | LIDAOE | IGROE | IRRELEVANT / X | IRRELEVANT / X | 93f4af38cc69319228072cc1d76005b5fc422098baa133d614ec6e2b7bd1872e |
| DOC039-P0058-C001 | DOC039-P0058 / 58 | 118 | LDAE | AGROE | IRRELEVANT / X | IRRELEVANT / X | 4b2cc5fbf08cb6901a293178d54e3d45df41256f5d33cc36f9ad219955fca967 |
| DOC039-P0059-C001 | DOC039-P0059 / 59 | 256 | LIDAOE | AIGROE | IRRELEVANT / X | IRRELEVANT / X | 59a54dcb05967c45837c04b158da36532136fae1ad2b45af193ba7b350a54510 |
| DOC039-P0061-C001 | DOC039-P0061 / 61 | 2 | A | R | IRRELEVANT / X | IRRELEVANT / X | 858849f84bbe23f5927d8df0935b1043b74ae6588482f5e3b00d0013a71127d2 |
| DOC039-P0062-C001 | DOC039-P0062 / 62 | 147 | LIDA | IGURO | IRRELEVANT / X | IRRELEVANT / X | 473bcff4c81306769bfeac423fd6a73f781f40f0d2f4110fd0088ba17dfae273 |
| DOC039-P0063-C001 | DOC039-P0063 / 63 | 267 | LDAO | GRO | IRRELEVANT / X | IRRELEVANT / X | 6aa70d0720da146863f619697da627d4d6f10769714d1b8fbab8494cd06e42d8 |
| DOC039-P0064-C001 | DOC039-P0064 / 64 | 132 | LIDAE | AIGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 604ebb77dfcd483997fbb2a46e52b03ff64836d06e9999eb1401e3e76ac2170a |
| DOC039-P0065-C001 | DOC039-P0065 / 65 | 349 | LIDAOE | AIGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 88622f50fac5d67e746092e6419ea9dfe9025807611a196de196b4467b816f86 |
| DOC039-P0066-C001 | DOC039-P0066 / 66 | 203 | LIDAOE | AIGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 9f6fa2064fd727ff31cbe56d3021cb72b45beb00060c5fd29cf5babafba86881 |
| DOC039-P0067-C001 | DOC039-P0067 / 67 | 294 | LIDAOE | AIGUROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 2902008d36bc46b0c88449b51cad0b3a97fa63a69a2ae8ab4d6904eca20087df |
| DOC039-P0069-C001 | DOC039-P0069 / 69 | 3 | L | RO | IRRELEVANT / X | IRRELEVANT / X | f33c8b3bbb47a74512097041d299937827e5169658d03cf5f855eb7821217492 |
| DOC039-P0070-C001 | DOC039-P0070 / 70 | 203 | LIDAO | IGUROE | IRRELEVANT / X | IRRELEVANT / X | 0de3d7f0ea4c5890b759e1fc527bee123839b9ef90099426ddd9e7c6a8460ab2 |
| DOC039-P0071-C001 | DOC039-P0071 / 71 | 328 | PLIDAO | IGUROE | IRRELEVANT / X | IRRELEVANT / X | b4f1e8be1b13f20edff37522273fcb2c04b071fb4733fbe01f812d0ba43293a1 |
| DOC039-P0072-C001 | DOC039-P0072 / 72 | 89 | LID | IGRO | IRRELEVANT / X | IRRELEVANT / X | 78fc30f4fd63767d68b1fa10965f5088711bad1fafcd8313d0cdd1c1ae1505e6 |
| DOC039-P0073-C001 | DOC039-P0073 / 73 | 274 | LIDAO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 966b4c547e1238a0b2d92c51f5d52debede4e405b2db7587a21393da7e32b91e |
| DOC039-P0074-C001 | DOC039-P0074 / 74 | 213 | PLDO | GRO | IRRELEVANT / X | IRRELEVANT / X | 3413851c1bba31497219bc508fd887e88c92bc3dfb19b02e37b332e416d07550 |
| DOC039-P0075-C001 | DOC039-P0075 / 75 | 281 | PLIDO | IGRO | IRRELEVANT / X | IRRELEVANT / X | 4b13f5b520bdcb75864a8b2bf13b07ff7937f5e7825ef4bc1982619cd1291c45 |
| DOC039-P0077-C001 | DOC039-P0077 / 77 | 5 | LD | RO | IRRELEVANT / X | IRRELEVANT / X | 895620156703723be0a7ba82006654322cf0102b9eabd2734dbfca5014a38e42 |
| DOC039-P0078-C001 | DOC039-P0078 / 78 | 155 | LDAE | AGROE | IRRELEVANT / X | IRRELEVANT / X | d791234d83af39fac635670b7126345ee008d3cd820e3c829ecd5df3935aa1bd |
| DOC039-P0079-C001 | DOC039-P0079 / 79 | 217 | LIDA | IGRO | IRRELEVANT / X | IRRELEVANT / X | a9c23c350166fa69d27659c539176a44841f2e4c3da983c839aa64cbe1362465 |
| DOC039-P0080-C001 | DOC039-P0080 / 80 | 209 | PLIDAOE | AIGURO | IRRELEVANT / X | IRRELEVANT / X | d5f5dbf8cfd115bd89b704430640626c4cbc83cff49dba7b86312b82c229e6fc |
| DOC039-P0081-C001 | DOC039-P0081 / 81 | 267 | PLIDO | IGURO | IRRELEVANT / X | IRRELEVANT / X | 5579deed14bbd83ec4bb104e8f51f0bcd489e439936c37c813ecfcc0017e4cf2 |
| DOC039-P0082-C001 | DOC039-P0082 / 82 | 150 | LIDAOE | AIGRO | IRRELEVANT / X | IRRELEVANT / X | 4a520964f41ba0d53a6c984a152d5192ca2750a0ae0e5c1e5767dcbff6a33e5b |
| DOC039-P0083-C001 | DOC039-P0083 / 83 | 267 | LID | IGRO | IRRELEVANT / X | IRRELEVANT / X | 5fabe0c1e8887b4cbe2fa664c0d3d843260b5c628d6c5c9b1dd5a71f51d4493d |
| DOC039-P0084-C001 | DOC039-P0084 / 84 | 214 | LDAOE | APGROE | IRRELEVANT / X | IRRELEVANT / X | ca966b4bd454099ad55dc57ae97669ec393f598c86dec9d1b235fc4c7d388d96 |
| DOC039-P0085-C001 | DOC039-P0085 / 85 | 324 | LIDAOE | APIGUROE | IRRELEVANT / X | IRRELEVANT / X | bab048ed998c91eb93e27f5bc6e0366b4d3a20e344799a76b16b099a40ecb37b |
| DOC039-P0086-C001 | DOC039-P0086 / 86 | 143 | LDAO | GUROE | IRRELEVANT / X | IRRELEVANT / X | a55f55338c9297d3491b87a90aaf6171552f99330e8a85e56b9c1a81494f56bd |
| DOC039-P0087-C001 | DOC039-P0087 / 87 | 287 | LID | IGRO | IRRELEVANT / X | IRRELEVANT / X | a59935da4bf83f84ac22b31a3104c092d58c2381879d3ee5d13cdc8e6168972b |
| DOC039-P0088-C001 | DOC039-P0088 / 88 | 65 | LDE | AGRO | IRRELEVANT / X | IRRELEVANT / X | 280ca5819d8abea7bca3d6ba9d786ba8a99a976dc2b7d297a88f74d667a71664 |
| DOC039-P0089-C001 | DOC039-P0089 / 89 | 294 | LDAOE | APGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 6d6ebafd7b76d52a333a3ccb8a56354bae630fdb3642a2c8926deff3e6a4991b |
| DOC039-P0090-C001 | DOC039-P0090 / 90 | 450 | PLDE | AGUOE | IRRELEVANT / X | IRRELEVANT / X | 141a53e1cd5fe484b83a99419a88fd10c845e521818f538bbb2959a2ff334143 |
| DOC039-P0090-C002 | DOC039-P0090 / 90 | 161 | LDE | AGRE | IRRELEVANT / X | IRRELEVANT / X | 1ed57eaee2b26b740c873f38ce33cd680f79cf0061a07f42489f225973d8b5e3 |
| DOC039-P0091-C001 | DOC039-P0091 / 91 | 450 | PLIAOE | AIGUROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 6263674f64c5e2d8c2ea8d3124038078f8a8ed469ba867d11a193bcba5796812 |
| DOC039-P0091-C002 | DOC039-P0091 / 91 | 175 | PLIDAOE | AIGUROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 53f6bc49e46671c90cfb17fc9d40cca3d9e1eab384a0e8a3772a29d9ca832eb7 |
| DOC039-P0092-C001 | DOC039-P0092 / 92 | 450 | PLIDAOE | IGUROE | IRRELEVANT / X | IRRELEVANT / X | e82ce45b7c309f8c5a59cbb612a00cf10d562690f17fe5263853e6182d652729 |
| DOC039-P0092-C002 | DOC039-P0092 / 92 | 223 | PLIDAOE | IGUROE | IRRELEVANT / X | IRRELEVANT / X | fbb42d4a9cf8f3b5bff0944f7e2c9cb90c97fc9a7874c32a9b9a4b7d8cbc5179 |
| DOC039-P0093-C001 | DOC039-P0093 / 93 | 147 | PLDA | GRO | IRRELEVANT / X | IRRELEVANT / X | 67e45fca3876deed374d1011f9e32e567f3f842271f25d863c1130ea21ef03a9 |
| DOC039-P0094-C001 | DOC039-P0094 / 94 | 126 | - | R | IRRELEVANT / X | IRRELEVANT / X | ed633b662909fa8a2731967bdcd43ac04b26eab6789a359f2439cd6cc66c6d35 |
| DOC039-P0095-C001 | DOC039-P0095 / 95 | 123 | LDE | APGRE | IRRELEVANT / X | IRRELEVANT / X | c595d7da8cf2c2b404c25bb3230716e4c35164ce994b26b70bc8da81e02f8bbe |
| DOC040-P0001-C001 | DOC040-P0001 / 1 | 21 | LO | FGRO | IRRELEVANT / X | IRRELEVANT / X | 851e2496b03fb16b88f94a032803c1e247d81ffc30c8169ff54e9831a64d3884 |
| DOC040-P0002-C001 | DOC040-P0002 / 2 | 287 | PLIAOE | FAPIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 3507a927f771b9790c1601f1d7127543a6e94ed98096b80be9ac46d1a3ab0989 |
| DOC040-P0003-C001 | DOC040-P0003 / 3 | 158 | LIDAO | FPIRO | IRRELEVANT / X | IRRELEVANT / X | ce71cdfcd62817196426b73c4792a7ab75ba044a9739a04fb28a4ea46b56004b |
| DOC040-P0004-C001 | DOC040-P0004 / 4 | 450 | LIDAOE | FPIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | b43786b6af6c6a2133eeb14805703554ee2519717c9b1a8ec7b426cd46cc988d |
| DOC040-P0004-C002 | DOC040-P0004 / 4 | 140 | LOE | FGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | bf92b5af7e895bdd711e216bff049511794ea3affcd6f8716ebdd6f3dfe08ac0 |
| DOC040-P0005-C001 | DOC040-P0005 / 5 | 278 | LAOE | FGROE | IRRELEVANT / X | IRRELEVANT / X | 41b35ddb95360899f37906542b6ae81a5fb8f5787a20e3316475c731a9fd3d41 |
| DOC040-P0006-C001 | DOC040-P0006 / 6 | 450 | LIAOE | FPIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 6fc3024af0c2b490e8f107f26217b9af44744a18027ab2f81b6459f8b5db6140 |
| DOC040-P0006-C002 | DOC040-P0006 / 6 | 122 | LDOE | FGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | d7ffeaa712fd2bfc3227ee28a0ced99bbbec015c2d40cd59e30b590694543d4b |
| DOC040-P0007-C001 | DOC040-P0007 / 7 | 222 | LDAOE | FGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 9b13bd7d57c491e7c009f473dc3a9505b7ea606f01c587d32ed22e6151e0c46a |
| DOC040-P0008-C001 | DOC040-P0008 / 8 | 204 | PLIDA | FPIGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | ca60f75771288d0b71125bb870226e5f605e556921239da03f933774e67f5748 |
| DOC040-P0009-C001 | DOC040-P0009 / 9 | 450 | PLIDAOE | PIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 0c669907be058de59b918f0ac44bdde16ac1090c34af28d9d5b6253fdb7e321c |
| DOC040-P0009-C002 | DOC040-P0009 / 9 | 186 | PLIDOE | PIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 7f6dd261a8f577474a798b9b6df06c2941f42c5e8cc664c176a29e0655784657 |
| DOC040-P0010-C001 | DOC040-P0010 / 10 | 246 | LDAOE | FAPGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 1645264d2a35b0a3fa74dd7039db9a2ead82c73eb082aa9b59afce69820fb521 |
| DOC040-P0011-C001 | DOC040-P0011 / 11 | 421 | LIAOE | FAPIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | a4c37b8b44211f2751f95d64c93331cd1c9ab232fbb81a8789393d167684419c |
| DOC040-P0012-C001 | DOC040-P0012 / 12 | 246 | LIDAE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | f66a7de606c1de2db0669f86d4feb99e963ae077264dcbbca934950e5176589c |
| DOC040-P0013-C001 | DOC040-P0013 / 13 | 450 | LIAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 56aa3f96f9fb4404c6725015add79f32058c8768f4fbdd0348a6ffad0b8cf3fd |
| DOC040-P0013-C002 | DOC040-P0013 / 13 | 79 | LIAOE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 113057392052dde9b30bc1b7b93c0bec399e7dbb29d5fa3116f5b8237d43bc86 |
| DOC040-P0014-C001 | DOC040-P0014 / 14 | 450 | LIDAE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 16fa2c3c42e912d781bf97ab8e204fb4ef3bac1330ad587f803426ccb95749a2 |
| DOC040-P0014-C002 | DOC040-P0014 / 14 | 155 | LIDA | FIRO | IRRELEVANT / X | OTHER_NEAR_MISS / W | 188dda6b0a123f2ab2c070e386f84fd355cea2c43e52bd1bc471057fe153db9d |
| DOC040-P0015-C001 | DOC040-P0015 / 15 | 431 | LIDAOE | FAPIGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | cd8454d2b519395e0f3759e182ab77e4466403a324703684d29a2746d7c2ee35 |
| DOC040-P0016-C001 | DOC040-P0016 / 16 | 450 | LIDAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 3e7c109b1ed013f601fbd566d8999be52f1b617465a605d4921d6cd11840d5d9 |
| DOC040-P0016-C002 | DOC040-P0016 / 16 | 105 | PLAOE | PGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 24ec1aed0b7b35675707b93f7c93d484ec15bcc32f4f3a701c86ff24d73cd11e |
| DOC040-P0017-C001 | DOC040-P0017 / 17 | 288 | LIAOE | APIGROE | IRRELEVANT / X | ADOPTION_RATE / R | faa992e3c6042d350824900ff5a12777871b9d7b2631b23a4776dcf41424dd02 |
| DOC040-P0018-C001 | DOC040-P0018 / 18 | 333 | PLIE | FIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 340bd7a1501bececc6595aa4cf17c04e0df9274c98b2cec66030a6ccbdc7eed6 |
| DOC040-P0019-C001 | DOC040-P0019 / 19 | 307 | LDOE | FGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 8c261a839d7c6aea3965a5aeb7dc7aa2db6fcc08c2dc00f94760cf1ace869d7b |
| DOC040-P0020-C001 | DOC040-P0020 / 20 | 146 | PLID | FPIGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | b917ac9541544874b3f6513307719321bf8fb6a24eb0404a47d9736a8d4e9400 |
| DOC040-P0021-C001 | DOC040-P0021 / 21 | 431 | PLIDAOE | APIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 557a3bef3092cfb795411a348e76af52ff27e7e8202f01868a1b31ef0e1992d2 |
| DOC040-P0022-C001 | DOC040-P0022 / 22 | 233 | PLDAOE | APUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 5d8c5c29c1270cf21b9ff2d54b29864a53a4514b2031e2a67a7b92d7aaa5ef29 |
| DOC040-P0023-C001 | DOC040-P0023 / 23 | 450 | PLIDAOE | FAPIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | aae4a2b9a2d0409d39665c554b2d5141a31b2ab938981f552930d6759b625437 |
| DOC040-P0023-C002 | DOC040-P0023 / 23 | 86 | PLID | PIRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | dae49f5a6e904c8fb43e8a62a3f3dc42f6082b45d6393bb09ba45f89ed67b3d2 |
| DOC040-P0024-C001 | DOC040-P0024 / 24 | 378 | PLIAOE | FPIGUROE | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | f6e2a7b5c992a9463c3f3d28fd40737e20245683e4db6f4e23d4b77fbfc332d5 |
| DOC040-P0025-C001 | DOC040-P0025 / 25 | 450 | PLIDAOE | IGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 94969f9a80d8ab6a7956d9ceb99f4dc9dcdc83c62de5d74c25fbef4ed7a7089f |
| DOC040-P0025-C002 | DOC040-P0025 / 25 | 138 | LAO | GROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 72db5dd22248465815e5af92cc3d0927c05e44b30621c53c6567d43972defc1d |
| DOC040-P0026-C001 | DOC040-P0026 / 26 | 254 | PLIOE | IGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | bc729216bdd94e5ba400a096e935c4c73bbdde16db0813fdcd2c274e212724f3 |
| DOC040-P0027-C001 | DOC040-P0027 / 27 | 404 | PLIDAOE | PIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | dc951272f3797cf8e3d952aba1f966b7589394b2ccf6b9aa37fdae81ffd62b27 |
| DOC040-P0028-C001 | DOC040-P0028 / 28 | 450 | PLIDAO | FAPIGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 71d6bb63a8433125cb058fdda62f8eb97052afaaa9aa8d1c5b0709d4f670ac01 |
| DOC040-P0028-C002 | DOC040-P0028 / 28 | 115 | LDOE | APGROE | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | 3067d3861cf693bc86c3d362a453215a594847c25449d04ea965aa599d4552ad |
| DOC040-P0029-C001 | DOC040-P0029 / 29 | 164 | LIDOE | APIGUROE | IRRELEVANT / X | ANALYTICS_POLICY_RECOMMENDATION / P | 24e978a160ad8c19bf02f0a1adcc54761ecc26b4bb0e2af6ccfb51af5a6c9f3b |
| DOC040-P0030-C001 | DOC040-P0030 / 30 | 450 | PLIDAOE | PIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 5e8e50c62009c18d977ee0fce8eeb98a0442a0515ecc9de14398610ce57f799a |
| DOC040-P0030-C002 | DOC040-P0030 / 30 | 107 | PLIAO | IGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | b9345f2e75e6cd81b7cec74c9ae4001b2c94ace1dd7edbc6bbc2d7e220e78045 |
| DOC040-P0031-C001 | DOC040-P0031 / 31 | 175 | PLIDAOE | IGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | a17fc258173e3b8fe3eb8fffb7931980fda8be2956624a8c506f1cdf6f429a01 |
| DOC040-P0032-C001 | DOC040-P0032 / 32 | 450 | PLIDOE | APIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | cf3a9a6088ca168962686a3fadc7d5deef2c8c154bfc4543de3ee9389b42de77 |
| DOC040-P0032-C002 | DOC040-P0032 / 32 | 111 | LIO | IGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | c5eb4e91ca3059ba379269d90ae9376cb9eaedb4ba7836a3baed13d80190c136 |
| DOC040-P0033-C001 | DOC040-P0033 / 33 | 196 | PLO | GRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 54d6b4f6dd4b4a12ce0279a7605f3caf0caf6a780f2b58efcd501735c7edcdab |
| DOC040-P0034-C001 | DOC040-P0034 / 34 | 450 | LIDAO | FPIGURO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 5ea49dc964483fdfb7442f04c8c8dbd0e877641ff947ccb1ce9a6cf0b55cc61e |
| DOC040-P0034-C002 | DOC040-P0034 / 34 | 159 | LI | PIGURO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | fe3ddb2cc6566de079314624e03f9bc5868958b322e4a64f4bb2e4db639cede3 |
| DOC040-P0035-C001 | DOC040-P0035 / 35 | 300 | LAOE | APGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | c08c7b347379ed74ba0091ecca1fcd022d6525a35e79595746b3441cc8b2ef7c |
| DOC040-P0036-C001 | DOC040-P0036 / 36 | 450 | LIDAE | FIGROE | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | 816ce8bf325b7594840f3a8d4a666226c94283e7708c956677fa2cfeb17a5073 |
| DOC040-P0036-C002 | DOC040-P0036 / 36 | 184 | LIDA | FIGROE | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | c98faaab5d0a5f4da886f47f1b3fad6e045fac5a801dab2a25c5824bf958a1db |
| DOC040-P0037-C001 | DOC040-P0037 / 37 | 397 | LIDAO | FAPIGURO | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | a381cad1764e227a5de15638bb265cec68ea84b2c673ae3779196ada5284dd1c |
| DOC040-P0038-C001 | DOC040-P0038 / 38 | 450 | LIDAOE | FAPIGROE | IRRELEVANT / X | OTHER_NEAR_MISS / Z | 4aab7d25867ddbe140d7fe49eb10b7b2bb88fd20b3e56a7842ab075643aa27f5 |
| DOC040-P0038-C002 | DOC040-P0038 / 38 | 158 | LDAO | FGRO | IRRELEVANT / X | OTHER_NEAR_MISS / Z | 61f93b4dba6183fdcceffd9f3ad73b2fb769d411be183273f79afb9c2ee5e8d6 |
| DOC040-P0039-C001 | DOC040-P0039 / 39 | 300 | LIDAOE | IGROE | IRRELEVANT / X | IRRELEVANT / X | 12198357aa9d58490a90a5ef8fa733748155eecf4cf4a48d49b970e804531558 |
| DOC040-P0040-C001 | DOC040-P0040 / 40 | 450 | PLIDAOE | PIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 5e37d7e611673a420a982088764b18f27fe9ed00d1115d10d3900f2dfe9cc063 |
| DOC040-P0040-C002 | DOC040-P0040 / 40 | 118 | LIDA | FIGRO | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 5799a66f28a5f76a0f91f969c7818360b4bd6637d08278857705dd6f90428946 |
| DOC040-P0041-C001 | DOC040-P0041 / 41 | 450 | PLIDAOE | PIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 9fc25fdd7204bf99e25af39ffdde57d801e69805cab7057af87ef9d16e1b1a98 |
| DOC040-P0041-C002 | DOC040-P0041 / 41 | 143 | PLIOE | IGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | f14d2ca5fb56eaa806738184f365a88424f77ce96869d6588552601bc951782c |
| DOC040-P0042-C001 | DOC040-P0042 / 42 | 450 | LAOE | APGROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | fe274c73875091da521ca57b954ea62e0e4a7f0d14048303c067723ce1d03cda |
| DOC040-P0042-C002 | DOC040-P0042 / 42 | 160 | LIDAOE | AGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 2724821e17e6e71a59859ef0229718fb498dc8819d417dd3b72c184baaae9c53 |
| DOC040-P0043-C001 | DOC040-P0043 / 43 | 432 | LIDOE | APIGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 25ed44ffdd6214499fb60beb0a3bd39d4e241c011d35390ae8b212e26e746337 |
| DOC040-P0044-C001 | DOC040-P0044 / 44 | 450 | PLIAOE | IGUROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 85ac1279e3690183f0f192f23bc9e21f4f2260429609f28ed5d6c9c35b47af92 |
| DOC040-P0044-C002 | DOC040-P0044 / 44 | 116 | PLAO | GROE | IRRELEVANT / X | FRAMEWORK_PROVISION / K | 43c29b352c5a016987f8d0c5604a00787d85f87ca566a1513b4541de7567117c |
| DOC040-P0045-C001 | DOC040-P0045 / 45 | 156 | LA | GUR | IRRELEVANT / X | FRAMEWORK_PROVISION / K | b6f65b324958a386164c185b7cbe9a723eab4a7dd38ec7a2e2bf61828fa921b3 |
| DOC040-P0046-C001 | DOC040-P0046 / 46 | 147 | LIDA | FPIRO | IRRELEVANT / X | IRRELEVANT / X | c106bcc770865778c211d36a03455fef90971245e7b5758703f00a3bbd0a6dcd |
| DOC040-P0047-C001 | DOC040-P0047 / 47 | 177 | LAE | FGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 3e7f0eb0432891ec34bdb383c38e2e0de00ce9f52f0b525bc456db2aaa31e8e9 |
| DOC040-P0048-C001 | DOC040-P0048 / 48 | 163 | PLIDAO | FPIGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | e60ddb884241d38b1627b6e6c584ca34964a683d7c2a7b40f4bc046864210f09 |
| DOC040-P0049-C001 | DOC040-P0049 / 49 | 169 | LIDAO | IGRO | IRRELEVANT / X | OTHER_NEAR_MISS / W | 603c32a4389c46b1c3e3119fe8409a16ef46d9ba8623cddef4dd71645c585d04 |
| DOC040-P0050-C001 | DOC040-P0050 / 50 | 77 | LDAO | RO | IRRELEVANT / X | OTHER_NEAR_MISS / W | 0bde9ae4c47a846b90f2a358142a9811bc8b314d56a57d332403baee6c9ba2dd |
| DOC040-P0051-C001 | DOC040-P0051 / 51 | 386 | LIAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 402090e5564845a8edf0a804fb46f4c0cc35c3746ed6bc7774c9e85c764a889d |
| DOC040-P0052-C001 | DOC040-P0052 / 52 | 206 | LIAOE | PIGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 6418036eb07064ed302c7b36dc6f8dfdbc16d4c4b3ef657501f7702d8e5ca2d0 |
| DOC040-P0053-C001 | DOC040-P0053 / 53 | 450 | LIAOE | PIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 1607c6f87ada64cab14eb375a4f04d4a4e08dd993296a66b5b48a9c5865ba889 |
| DOC040-P0053-C002 | DOC040-P0053 / 53 | 123 | LAO | GRO | IRRELEVANT / X | OTHER_NEAR_MISS / W | 96ad743de397f7e0a6341a77ba6cabba38d2ddc20cc4916b514348dc1eed6536 |
| DOC040-P0054-C001 | DOC040-P0054 / 54 | 148 | LAOE | GUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | e3207e868ff7d9085ee9b0aeec1d4e98e47baeaa5e9846f6046f262c619d316a |
| DOC040-P0055-C001 | DOC040-P0055 / 55 | 440 | PLIDAE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 10b52815092f3fad75f58a8d767b33fa7be308b392ef7279b66c250657716cce |
| DOC040-P0056-C001 | DOC040-P0056 / 56 | 98 | LD | PGRO | IRRELEVANT / X | OTHER_NEAR_MISS / W | eaad2bb40790280974e0d3ee26142441bc6b60e4f3d16273e92eb3c42ca1e347 |
| DOC040-P0057-C001 | DOC040-P0057 / 57 | 450 | LIDAE | PIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 8771de495b4fa3dfb22bf5da06f4f33bba6ddfc4ff6e09c052d3ab06f6607f87 |
| DOC040-P0057-C002 | DOC040-P0057 / 57 | 88 | LDA | PGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 0130df7ec6ce327243b7a6fd4198b4be9cce997cc2325710634e20c8b584f48c |
| DOC040-P0058-C001 | DOC040-P0058 / 58 | 108 | PLI | IGRO | IRRELEVANT / X | OTHER_NEAR_MISS / W | b786e2856b34017a71c7eab0a7d97d0bd02406a93bee30a3c0cb61cb2b80497c |
| DOC040-P0059-C001 | DOC040-P0059 / 59 | 450 | LIAOE | AIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | ccdb311d166692fba5a72e592c61b1301f9809c8783a3c66f58ae24d172b3674 |
| DOC040-P0059-C002 | DOC040-P0059 / 59 | 155 | LOE | AGURE | IRRELEVANT / X | ADOPTION_RATE / R | 90fec51bb9bc65ca4acb0cb524a7a11f7ca2456d8e4048df9b217db4b8293bf1 |
| DOC040-P0060-C001 | DOC040-P0060 / 60 | 125 | LAE | PGRE | IRRELEVANT / X | OTHER_NEAR_MISS / W | a8ed7c18d457bd7346e94f273df74ddf95b3df4f1aff1d01a10b566de11ac176 |
| DOC040-P0061-C001 | DOC040-P0061 / 61 | 450 | LIDAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 24a6dac992c38cbcad6b9bf719736bfefa6d84d01fb800bfc0ade47cdb87cb9c |
| DOC040-P0061-C002 | DOC040-P0061 / 61 | 91 | LDOE | AGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | f1f72617043a8263a68a89d1080b28323cc9fc4f7fc973f17c49ee54e0352b7c |
| DOC040-P0062-C001 | DOC040-P0062 / 62 | 380 | PLIDAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 5d03b50c7d345f436063850529aa3c427d3596dbdbee168b647fa08d6dfc8bac |
| DOC040-P0063-C001 | DOC040-P0063 / 63 | 259 | PLAOE | PGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 8fbbab5bfd786c95a968b093136b0b9b1ded655c6a15daa9addedbcf6ad419e2 |
| DOC040-P0064-C001 | DOC040-P0064 / 64 | 449 | LIAOE | AIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 7a7a4f0a6465a3c89bc1e94e8ba2d814f056a4a435c591f1f04e5c80976f5668 |
| DOC040-P0065-C001 | DOC040-P0065 / 65 | 432 | PLIAOE | PIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 642544d0a215c861998487ee2bc88051eb192c0aca122ae972138135108de223 |
| DOC040-P0066-C001 | DOC040-P0066 / 66 | 450 | LIDAOE | APIGURE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 0d9a40d94293e9bc40147ca57976f378f6c72de230819ed3dd22c0a0fc55dfc2 |
| DOC040-P0066-C002 | DOC040-P0066 / 66 | 193 | LIDAOE | IGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 0307b7559b6359b1743e63e50fcb97757c1a6c77023d0012a23fa0ccaa6403b8 |
| DOC040-P0067-C001 | DOC040-P0067 / 67 | 439 | LIDAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 30af8e821e4b9fa5998b001dda32f3ac77deb1b57591af75f13d1a9e34f3305e |
| DOC040-P0068-C001 | DOC040-P0068 / 68 | 23 | AE | RE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 6b98e24ceb2a69c7f62ddc846817220cdf57fc0f9ff16e10e4020641d720e2b1 |
| DOC040-P0069-C001 | DOC040-P0069 / 69 | 450 | LIDAOE | AIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | c570bd7c8d0cb3053745fea624b7285de2d30fceb16b80c87a34b4818338a352 |
| DOC040-P0069-C002 | DOC040-P0069 / 69 | 166 | LOE | GURE | IRRELEVANT / X | ADOPTION_RATE / R | 5c4a5c03b7de5b8eb57c4919dc378825959527f1bc062ae70d12b82df350557a |
| DOC040-P0070-C001 | DOC040-P0070 / 70 | 283 | LAE | APGROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 2daa48ca103e803b085fa0b34004b0da49997e9b86792b0139c3f3301784eeac |
| DOC040-P0071-C001 | DOC040-P0071 / 71 | 448 | LIAOE | APIGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | bcff83fb1a80174ffddb05d996e6041181c9e559b8ece5971b36033e0a5d178b |
| DOC040-P0072-C001 | DOC040-P0072 / 72 | 450 | PLAOE | APGUROE | IRRELEVANT / X | ADOPTION_RATE / R | a42c21e2b31b24dcdcbe4458a3a807ff80c4583992e184347832d4ef18bb0fee |
| DOC040-P0072-C002 | DOC040-P0072 / 72 | 103 | PLAOE | APGUROE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 08d6cc3157bc76a9f76f4b1fed098a8143d5130ffeeaeb228bb77fa96f97a98d |
| DOC040-P0073-C001 | DOC040-P0073 / 73 | 71 | LAE | RE | IRRELEVANT / X | OTHER_NEAR_MISS / W | a38627f13bbd60970151c8f9a3173a115e3e739731f4bac74147cc9fd3b2408c |
| DOC040-P0074-C001 | DOC040-P0074 / 74 | 450 | LIDAOE | AIGURE | IRRELEVANT / X | OTHER_NEAR_MISS / W | ff56290e5b14d08ff97b6ea9699008eac5fc1b503127da0d76bd5fd0ac029866 |
| DOC040-P0074-C002 | DOC040-P0074 / 74 | 208 | LAOE | PGRE | IRRELEVANT / X | OTHER_NEAR_MISS / W | 63461032ca61e7a0731f14c84443cda48eee692c2954fadc8b5665ff054755fa |
| DOC040-P0075-C001 | DOC040-P0075 / 75 | 62 | LAE | GRE | IRRELEVANT / X | OTHER_NEAR_MISS / W | f519b01c9fe00a982300dcce7e9726503008aba29b583e706a5ddfc067fdc98f |
| DOC040-P0076-C001 | DOC040-P0076 / 76 | 122 | - | R | IRRELEVANT / X | IRRELEVANT / X | 765c7f3cba8e3f0faa3217d35383955098894118d0863b425e51cb96bb639b15 |
| DOC040-P0077-C001 | DOC040-P0077 / 77 | 77 | E | APRE | IRRELEVANT / X | IRRELEVANT / X | 236de04e6d7eb06d72608a98026075ea241e6b1168fd895bf75a10f51bdc8898 |

## Final engineering validation and provenance

ENUMERATED_CHUNK_ID_STREAM_SHA256=f6e21c0121f22ed9825e3f9a239165c462b2fc18ccc5a22243f9093a47eab2ca
ENUMERATED_PAGE_ID_STREAM_SHA256=eea345bde0ffd13e7bd032e0e866dc4d4f351ca46d592e64973f5057756bed3d
CHUNK_ID_STREAM_ENCODING=UTF-8; each ordered native ID followed by LF
ALL_CANONICAL_CHUNKS_ENUMERATED_EXACTLY_ONCE=PASS
ALL_ACCEPTED_DOCUMENTS_REPRESENTED=PASS
UNKNOWN_CHUNKS=0
DUPLICATE_CHUNKS=0
ALL_664_PAGE_UNITS_ENUMERATED=PASS
PUBLIC_SOURCE_BOUNDARY=PASS
PRIOR_TWO_ARTIFACT_HASHES_UNCHANGED=YES
CANONICAL_SOURCE_ARTIFACTS_UNCHANGED=YES
PROTOCOL_UNCHANGED=YES
TRACKED_MODIFIED_COUNT=0
STAGED_COUNT=0
UNTRACKED_COUNT=3
DIFF_CHECK=PASS

CORPUS_DOCUMENTS_SCANNED=9
CORPUS_SOURCE_UNITS_SCANNED=664
CORPUS_CHUNKS_SCANNED=850
RANKED_RETRIEVAL_USED=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
MODEL_BENCHMARK_OUTPUT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
LLM_ASSISTED_CANDIDATE_AUTHORING=YES
CORPUS_WIDE_ABSENCE_AUDIT=YES
HUMAN_DIRECTED_CANDIDATES=YES
FROZEN_PUBLIC_CORPUS_ONLY=YES
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
TASK_JSON_CREATED=NO
HUMAN_VERIFICATION=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO

## Researcher-Directed Pre-Freeze Precision Revisions — T029/T030 Revision 1

Date: 2026-09-27

PRE_REVISION_ABSENCE_AUDIT_SHA256=0c428e910348eb3029ad72dcc813e2f38c29ca297304e1841fbf43d5fd26d3a2
PRE_REVISION_DOSSIER_SHA256=c509ee9639c31dab469340ae2c773cf5633b69ebd2b290711247cbb0bd29a3da
PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
REVISION_STAGE=PRE_FREEZE
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO

All preceding bytes are preserved. This is a fresh direct-source recheck of the revised questions against every canonical chunk, not a conclusion from keyword zero matches and not a performance-driven redesign. Original questions, near-miss findings, taxonomy counts and verdicts above remain historical.

### Complete corpus recheck and method

CANONICAL_CHUNK_INDEX=corpus/use_cases/UC3/processed/chunks/index.json
CANONICAL_CHUNK_FILES=DOC032.chunks.json through DOC040.chunks.json
CANONICAL_SOURCE_UNIT_INDEX=corpus/use_cases/UC3/processed/pages/index.json
UC3_FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
UNKNOWN_CHUNKS=0
DUPLICATE_CHUNKS=0

All nine page/chunk artifacts were reparsed. The 664 page IDs and 850 unique chunk IDs were re-enumerated in native document/page/chunk order. Every chunk original-text hash matches the prior full classification ledger. The existing broad term-family regexes were reapplied to every full chunk and reproduced every recorded family flag. Additional unranked families below test explicit implementation, outcome measurement/definition, any direction of change, and documented governance/population/rate terminology. All flags are navigation/coverage records, not relevance scores or proof of semantic absence.

The prior complete manual near-miss classifications were reconsidered under the new conjunctions. Source-order empirical/pilot/measurement contexts in DOC033–DOC035, analytics/implementation/adoption/outcome passages throughout DOC040 and framework/analytics/retention references in every remaining document were reinspected. Full highest-risk passages include descriptor piloting, validity/participation-frequency warnings, RFCDC action-research guidance, democratic school/EDC-HRE research summaries, actual adjacent pedagogical outcome claims, DigCompOrg tables/concluding limitation and other-tool population figures. No external cited study was fetched. The complete recheck ledger below binds all 850 texts; existing full near-miss findings and classifications remain applicable.

T029 now asks for change, which may be positive, negative or null. The supplementary change scan explicitly includes decrease, decline, reduction, unchanged/no-change and no-effect language. An identified setting, explicitly RFCDC-linked implementation, an explicitly defined participation outcome and empirically reported post-implementation change must be present together, possibly across source locations. A predefined numerical scale or an RCT is not imposed; systematic qualitative measurement with a defined outcome could count. T030 requires the explicit DigCompOrg implementer population, documented policy/code adoption proportion and measured change following implementation; temporal following is not silently strengthened into proof of causal attribution.

| Supplementary flag | Exact case-insensitive regex | Matched chunks |
| --- | --- | ---: |
| X | `\bexplicit\w*\|implement\w*\|deploy\w*\|adopt\w*\|post.implement\w*` | 329 |
| M | `measur\w*\|operational\w*\|defin\w*\|indicator\w*\|baseline\w*\|pre.test\|post.test\|before.and.after` | 210 |
| C | `change\w*\|improv\w*\|increas\w*\|decreas\w*\|declin\w*\|reduc\w*\|unchanged\|no change\|no effect\|no difference\|follow.up\|longitud\w*` | 282 |
| G | `document\w*\|governan\w*\|polic\w*\|code of practice\|denominator\|population\|sample\w*\|proportion\w*\|rates?\|percent\w*\|\d\s*%` | 527 |

| Document | Source units rechecked | Chunks rechecked |
| --- | ---: | ---: |
| DOC032 | 123 | 177 |
| DOC033 | 89 | 111 |
| DOC034 | 65 | 63 |
| DOC035 | 129 | 178 |
| DOC036 | 13 | 24 |
| DOC037 | 66 | 88 |
| DOC038 | 7 | 11 |
| DOC039 | 95 | 95 |
| DOC040 | 77 | 103 |
T029_RECHECK_FAMILY_D_CHUNKS=659
T029_RECHECK_FAMILY_E_CHUNKS=476
T029_RECHECK_FAMILY_ANY_CHUNKS=823
T029_RECHECK_FAMILY_I_CHUNKS=513
T029_RECHECK_FAMILY_O_CHUNKS=566
T029_RECHECK_FAMILY_L_CHUNKS=664
T029_RECHECK_FAMILY_P_CHUNKS=359
T029_RECHECK_FAMILY_A_CHUNKS=455
T029_RECHECK_FAMILY_F_CHUNKS=259
T030_RECHECK_FAMILY_R_CHUNKS=831
T030_RECHECK_FAMILY_E_CHUNKS=518
T030_RECHECK_FAMILY_ANY_CHUNKS=846
T030_RECHECK_FAMILY_A_CHUNKS=236
T030_RECHECK_FAMILY_P_CHUNKS=241
T030_RECHECK_FAMILY_I_CHUNKS=489
T030_RECHECK_FAMILY_U_CHUNKS=385
T030_RECHECK_FAMILY_O_CHUNKS=660
T030_RECHECK_FAMILY_G_CHUNKS=554
T030_RECHECK_FAMILY_F_CHUNKS=31

### T029 Researcher-Directed Pre-Freeze Revision 1

TASK_ID=T029
TASK_TYPE=insufficient_evidence
ORIGINAL_QUESTION=According to the frozen UC3 corpus, what measured improvement in learners'
democratic participation was reported after educational settings implemented
RFCDC competences or descriptors?
REVISED_QUESTION=According to the frozen UC3 corpus, among educational settings explicitly
reported as implementing RFCDC competences or descriptors, what empirically
measured change in learners' democratic participation was reported using an
explicitly defined participation outcome measure?
REVISION_REASON=The previous wording did not sufficiently distinguish explicit RFCDC implementation from general democratic-education research, and did not require a clearly defined participation outcome measure.
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO

#### Revised conjunction and counterevidence review

CHUNKS=DOC034-P0055-C001, DOC034-P0057-C001, DOC034-P0057-C002, DOC034-P0058-C001; DOC033-P0062-C001, DOC033-P0063-C001
CLASSIFICATION=OTHER_NEAR_MISS
SUFFICIENCY_REASONING=Descriptor piloting/scaling is genuine empirical work in education settings. Its reported outcome is validity/proficiency scaling of descriptor items, not measured post-implementation change in an explicitly defined democratic-participation outcome. Observing a learner for item validation does not establish the requested change.

CHUNKS=DOC035-P0055-C001, DOC035-P0057-C001, DOC035-P0084-C001
CLASSIFICATION=ASSESSMENT_GUIDANCE / IMPLEMENTATION_GUIDANCE
SUFFICIENCY_REASONING=Assessment/evaluation definitions and guidance include a warning that frequency of learner contributions may measure personality instead of democratic competence. The action-research section proposes using CDC for empirical studies/systematic evaluation. These acknowledge measures/research opportunities but report neither a completed explicitly RFCDC-linked setting/outcome study nor its measured participation change.

CHUNKS=DOC035-P0036-C001, DOC035-P0046-C001, DOC035-P0115-C001
CLASSIFICATION=EMPIRICAL_REALIZED_OUTCOME
SUFFICIENCY_REASONING=Actual adjacent claims include reduced tension/conflict from cooperative/Jigsaw methods and increased complex thinking from training. They have wrong intervention/endpoint bindings for this question. The broader revised word change does not turn conflict reduction or thinking complexity into a defined democratic-participation change after explicit RFCDC implementation.

CHUNKS=DOC035-P0092-C001, DOC035-P0098-C001, DOC035-P0100-C001, DOC035-P0101-C001, DOC035-P0119-C001, DOC035-P0119-C002, DOC035-P0120-C001
CLASSIFICATION=OTHER_NEAR_MISS / INTENDED_OUTCOME
SUFFICIENCY_REASONING=Democratic school/EDC-HRE research and possible future engagement are disclosed. They do not explicitly report an RFCDC implementation setting, a defined participation outcome and post-implementation empirical change together. Similar competences and future activity cannot supply the missing binding.

CHUNKS=DOC035-P0023-C001, DOC035-P0041-C001, DOC035-P0085-C001, DOC035-P0086-C001; DOC036-P0003-C001
CLASSIFICATION=OTHER_NEAR_MISS / FRAMEWORK_DEFINITION
SUFFICIENCY_REASONING=Practice histories/classroom testimony and the Council framework reference do not give a qualifying defined participation-change result. The earlier off-framework baseline/statistics and external-reference checks remain near misses; no cross-document combination supplies the conjunction.

CORPUS_WIDE_REVISED_SUFFICIENCY=INSUFFICIENT; no single passage or combination supplies all requested empirical bindings.
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REVISED_REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine a measured change in learners' democratic participation using an explicitly defined participation outcome measure after explicit RFCDC implementation. Descriptor-validation data and framework guidance do not establish that implementation outcome.
REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
T029_REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
AMBIGUITY_ASSESSMENT=Explicit RFCDC implementation and an explicitly defined participation outcome remove the prior broad attribution/measure ambiguity. The question seeks settings reported within this frozen corpus; it does not require an invented universal population, an external date or a causal trial. Different measures could qualify if expressly defined and tied to implementation, but none supplies a complete answer here.
ACCIDENTAL_CLUE_ASSESSMENT=The question specifies empirical eligibility conditions without disclosing absence or directing abstention.
TYPE_INTEGRITY=PASS; corpus-wide insufficiency remains despite substantial near misses.
ORIGINAL_RECORD_PRESERVED=YES
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO

### T030 Researcher-Directed Pre-Freeze Revision 1

TASK_ID=T030
TASK_TYPE=insufficient_evidence
ORIGINAL_QUESTION=According to the frozen UC3 corpus, what proportion of educational
organisations implementing DigCompOrg had adopted learning-analytics
governance policies, and what measured effect did this have on learner
retention or learning outcomes?
REVISED_QUESTION=According to the frozen UC3 corpus, among educational organisations explicitly
reported as implementing DigCompOrg, what proportion had a documented
learning-analytics governance policy or code of practice in place, and what
empirically measured change in learner retention or learning outcomes was
reported following that implementation?
REVISION_REASON=The previous wording did not precisely define the implementer population, the adoption criterion, or the meaning of measured effect.
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO

#### Revised conjunction and counterevidence review

CHUNKS=DOC040-P0021-C001, DOC040-P0028-C001, DOC040-P0028-C002, DOC040-P0029-C001, DOC040-P0035-C001
CLASSIFICATION=FRAMEWORK_PROVISION / ANALYTICS_POLICY_RECOMMENDATION / INTENDED_ANALYTICS_USE
SUFFICIENCY_REASONING=Past-tense organisation has adopted/implemented is descriptor wording within a framework table. It is not an observed organisation sample with documented adoption counts. The code-before-implementation provision and desired retention/learning uses give neither an implementer denominator, observed policy-adoption proportion nor measured outcome change.

CHUNKS=DOC040-P0038-C001, DOC040-P0038-C002
CLASSIFICATION=OTHER_NEAR_MISS
SUFFICIENCY_REASONING=The document explicitly states DigCompOrg remains conceptual and has not yet been piloted or implemented in real settings at publication. Subsequent SAQ testing is proposed. This does not justify reporting a zero adoption rate or extrapolating non-implementation to later real-world practice.

CHUNKS=DOC040-P0017-C001, DOC040-P0059-C002, DOC040-P0069-C002, DOC040-P0072-C001
CLASSIFICATION=ADOPTION_RATE
SUFFICIENCY_REASONING=Vensters, eLEMER and Opeka have genuine observed uptake/response rates or counts and denominators. Their named populations belong to those tools, not to explicit DigCompOrg implementers adopting the requested code/policy. They also lack the requested measured following retention/learning change.

CHUNKS=DOC040-P0016-C001, DOC040-P0063-C001, DOC040-P0065-C001, DOC040-P0067-C001, DOC040-P0074-C002; DOC040-P0042-C001, DOC040-P0042-C002, DOC040-P0044-C001
CLASSIFICATION=OTHER_NEAR_MISS / FRAMEWORK_PROVISION
SUFFICIENCY_REASONING=Targets, questionnaire recommendations, leader-course participation, other-tool pilots and planned improvements cannot supply an observed DigCompOrg adoption rate. Analytics definitions and indicator/rate definitions are not a measured implementation finding.

CHUNKS=DOC039-P0007-C001, DOC039-P0064-C001, DOC039-P0065-C001, DOC039-P0091-C001, DOC039-P0091-C002; DOC037-P0019-C001, DOC037-P0020-C002; DOC032-P0106-C001; DOC038-P0007-C001
CLASSIFICATION=INTENDED_ANALYTICS_USE / OTHER_NEAR_MISS / IRRELEVANT
SUFFICIENCY_REASONING=Other sources give educator analytics competences, companion-framework references, UNESCO technology potential or data-retention meanings. None states explicit DigCompOrg implementers, the documented policy adoption proportion and an empirically measured following learner outcome change. All remaining baseline/implementation passages were rechecked against the prior taxonomy and revised entity/outcome conditions.

CORPUS_WIDE_REVISED_SUFFICIENCY=INSUFFICIENT; no single passage or combination supplies all requested empirical bindings.
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REVISED_REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the documented learning-analytics policy or code-of-practice adoption proportion among explicit DigCompOrg implementers, or the measured change in learner retention or learning outcomes following implementation. Framework provisions and other-tool uptake figures do not supply those results.
REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
T030_REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
AMBIGUITY_ASSESSMENT=The population is organisations explicitly reported as DigCompOrg implementers; a rate requires a defined denominator and observed documented policy/code adoption. The outcome must be measured change following that implementation, not a normative purpose or a causal estimate imposed by the reviewer. No country/date is independently added; qualifying corpus reports would define their population and period.
ACCIDENTAL_CLUE_ASSESSMENT=The question specifies empirical eligibility conditions without disclosing absence or directing abstention.
TYPE_INTEGRITY=PASS; corpus-wide insufficiency remains despite substantial near misses.
ORIGINAL_RECORD_PRESERVED=YES
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO

### Complete revised-question recheck ledger

One row per canonical chunk in document/page/chunk order. Original primary classifications/reason codes are retained for traceability; they do not imply sufficiency for the new conjunction. Columns Q29/Q30 mark whether the complete requested evidence is supplied by that chunk; all NO assessments also undergo the above cross-location/cross-document counterchecks. Broad and supplementary flags are deterministic scans, not the semantic verdict algorithm. Original text hashes bind the full frozen passages reviewed through the source/audit coverage.

| Chunk ID | T029 broad flags | T030 broad flags | Supplementary flags | Original T029 class/reason | Original T030 class/reason | Q29 complete evidence | Q30 complete evidence | Original text SHA256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DOC032-P0001-C001 | DE | RE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3b9eb616be400e5b12bbfcee6368872dba070aa9a929191ba4471ec645439e00 |
| DOC032-P0002-C001 | IDOE | APIRE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1534538dfe1abc970e33644e75e3f455ec6dae7db6613d82f3adf3f4399c9699 |
| DOC032-P0003-C001 | LIDO | IURO | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1984f272ebbc307649ebf8a247f87376c2c9b43b743cdd05dac5e27df1a4e4a6 |
| DOC032-P0004-C001 | PLIDO | PIGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ff6c7bd57e268aa0fa100e298388072c8f46968ba467876a4d6bf1d32db20d99 |
| DOC032-P0005-C001 | PLIDAOE | APIGUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 5fa662160fb5056a9085a3c4d387c92c0569042913e38a61d95ef31b1269a190 |
| DOC032-P0006-C001 | PLIE | IGURE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0dc86d9d170348818555ee20b08450fb4e9533171028fd6715bf8be50ffc9d8e |
| DOC032-P0006-C002 | L | GUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0c701b87688632ba42cb14b3cd23ef76df8ad605e0e83cb9910099633b53bd28 |
| DOC032-P0007-C001 | LIDAOE | APIGUROE | MG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 5600370cdea9cd8bb3d83d713cce716c9f2d9dabbea4bfbfdfed2ffd4348e6a9 |
| DOC032-P0007-C002 | PLDOE | APUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 5143bc28a1eb09357c389a7b44383406e71ba893bbc539ada33335781b6f37f0 |
| DOC032-P0008-C001 | LDO | RO | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 80dadfd77c8d655fe36e399ababd1d7c140df37452315fa4b26ca48364a1d6e3 |
| DOC032-P0009-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 02bdfeb03ab79c8d75ef4de76678ef5f97df26feb18151b300d68c10953d96bf |
| DOC032-P0010-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | cd7eeccdf944bc35c7dcd9296b31aa1e0e8d543fe1d47a63fa770cecfee9d930 |
| DOC032-P0011-C001 | PLDOE | APGUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | b14e52fd4e1485702b4bf93d3f304cbc764d798dcf09acfe314779e5995e438a |
| DOC032-P0011-C002 | DOE | APURE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 16c1a60d2a8aecc970cb1552a98826175b602288ec67c487c07481d408101752 |
| DOC032-P0012-C001 | PLDOE | APGUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | f0667dbc0dc7fe6e213fe8f1f61543abbc98e1a398b0dec171dec9d60bca4fd9 |
| DOC032-P0012-C002 | PLIDO | IGURO | XCG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 6060395b424783c1cac309bc1a68f87c99a10426ee3c60f6f45ced041c68d3a4 |
| DOC032-P0012-C003 | LIO | IGURO | X | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 1c0dc89c985216a08b9753f59fcf9726bb5f6270b71c649249bc1cb719988acf |
| DOC032-P0013-C001 | FPLIDAE | APGUROE | XMG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 6be6bc55fc1eacfa3effccd204d56eb111ceca4911f736587e1b485824836e98 |
| DOC032-P0013-C002 | PLDOE | AGROE | MG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 52d7883d4e5f93c289e46aa2db9278d46f6df383c02cb881316db1d032a85cfd |
| DOC032-P0014-C001 | LIDOE | APIGRO | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e0e23c1e0607385517f8e250ac277619992e2bdb4c57e4e3fc8afad92a695712 |
| DOC032-P0014-C002 | IDE | APIURE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 97024dfe9e13a7dda10373356d15bf7f6db8e2d5b033bd6cce960cde8a86c3e3 |
| DOC032-P0015-C001 | LID | PIRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 33efe30b1b44ba93177245f6f8e0e4dab8651ce69e639334fb5f8571ba1b24de |
| DOC032-P0016-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2049cd3f2d0d719354b1881ea8d60bece8639d80caa6aba9f9babaf77dd672c1 |
| DOC032-P0017-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f3bc557a487146edeac4266455cb759239cacac836c5a00e4c3381be43990a8c |
| DOC032-P0018-C001 | PLIDOE | AIGURO | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 36fa2105d638fe2fd806ddf99edc25630747f2ff4146b78454f706e43ab1a5f8 |
| DOC032-P0018-C002 | LDO | URO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 303ee9742a045476f59159e0f1c1bf2f9d48be0d62cea0490eced900d0815e35 |
| DOC032-P0019-C001 | PDAE | APURE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 42a086515f97ce5a3407619a2784600ca30827eef6097a0af7da6953fc8b129f |
| DOC032-P0020-C001 | PIDAE | AIGURE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b7c417ea96ae771ba31be3959201e3c4a43a213776fd243a99a7b10b42d35c6d |
| DOC032-P0020-C002 | E | AR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e681af1dfdd902e00b034d0cf9e1279e12b15393f2ff6fe4128002ea0416a0af |
| DOC032-P0021-C001 | IDAOE | APIUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c6e69916256d628b94fc4d5c16b574ae3c73dfe6bb7f55babb455b882af7767 |
| DOC032-P0021-C002 | IOE | AIURO | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9108f3bf52caa967d49c2fb233b3aeadcb640c03cd8f2ed946d93dbc41a21e1a |
| DOC032-P0022-C001 | PLDAO | UROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1b74c90158a4049fa0b73b93d31c61081591722b2c8d70b111bd16e96f746a9a |
| DOC032-P0023-C001 | PLIDAOE | IUROE | XMCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | ff3a5c81f338ac6f704d76f781e411110c9d847cb979333965ebb8f8ee30d33c |
| DOC032-P0023-C002 | LDO | GURO | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | df5df767d0b977c46b94c31c8bacbdffc66cb5461bf081a4769d12f942b0011f |
| DOC032-P0024-C001 | PLIDOE | PIUROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | da744c98c1942235d5fab34376a521ae5f995ee51232ece107ca8a7f2b193c6e |
| DOC032-P0024-C002 | PLDE | UROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7b00efeef9e4d36ef9c3d053c984786ef1d2cacd3a2efdc5d697588297991da4 |
| DOC032-P0025-C001 | LIDAOE | PIGUROE | XMG | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | NO | NO | aa0a3e87a5a467d7dc0618e75e27e5077201f9f761f51a1633d0cb62fd0b9ae9 |
| DOC032-P0025-C002 | LIDO | PIURO | G | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | NO | NO | 09ec5564ced91a8e5f95daf876e187cde5b1f7af4951798d9e4c4638cbdc14a3 |
| DOC032-P0026-C001 | LIDOE | PIUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2b98c2d43f660c28ec6839191c5ff2047242d3371aa34c86308e228f60915c87 |
| DOC032-P0026-C002 | LDO | RO | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9220e36ba23f0b90c2694e8692951446377a71f06e72487c09ced2da67a823ff |
| DOC032-P0027-C001 | LIDOE | IROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 3e7f2ea2c693ae174d346c9fab441b6ec1d88e67d6c56ba022457d2bc0d0b3d5 |
| DOC032-P0027-C002 | OE | PROE | - | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 229fdc9a3f1a623761425863c1e8137234b612afe1d4807f6cdc7ae632c43656 |
| DOC032-P0028-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 41eabfea7215bd7bca2ae77ddcbc938bc33f54495e9f831985f67405948e80f8 |
| DOC032-P0029-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e9a3aba0a660fc24de95b5602a4a6fc1e55db064ea6339382c1ab976ac6d7604 |
| DOC032-P0030-C001 | LIDAO | IGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9b630441bd54e782f4ed305590a7d7381c33d1fd1d754b0646fa8e30212201a0 |
| DOC032-P0030-C002 | LIDO | IRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bb08488f1787d7f4424defdee72068e1d0bcd924e7fea6529d18bfe691cab5b9 |
| DOC032-P0031-C001 | LIDAO | IROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bb116dab5bdd8824c32714919d5b9132b32b045728a75478a54fb71c1d900133 |
| DOC032-P0032-C001 | LDAOE | AUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8679d75e3ef320af320b10b1c73627ea9ad5a826cb76d2d826f1c01c0f0ddaac |
| DOC032-P0032-C002 | LDAO | ROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1757f8587a30d60b0f3602b986be3650855a3acfeb468440b082a28c7137819f |
| DOC032-P0033-C001 | LIDAOE | AIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8fd8d9d1eec329ec75be2053d9f4dc83f3a3c899a8e6ef848efeaa4117c5519b |
| DOC032-P0034-C001 | LIDAO | IGURO | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d8612545b97e4d15b2064775fa1bd00933a9ddce3b77479e150271e94390e0a6 |
| DOC032-P0035-C001 | LIDAOE | IROE | XMC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6b313cd07ec82fe11d6c2121faa3c253dd54f6aeb7961f6bebb90d06daf3e428 |
| DOC032-P0036-C001 | PLIDAO | IUROE | M | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | b0855013304e597ee4d30a3cee2f3523faf1bbea98410c3c136fbc1ee06e441c |
| DOC032-P0036-C002 | PLDAO | UROE | - | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | b5fd83e5f1bc79a8ffe222c91a8206fa9da5f4af7ac4f41efe097d8ef8485753 |
| DOC032-P0037-C001 | PLDO | URO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c71d7f25810ad09fc3ca701afb0520765b1c67c710ce48e8975061dd55cfe813 |
| DOC032-P0038-C001 | LDOE | PUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8e2b2158452804be87e221f8f3e250dd5331234f57a4d5af4294c856bbeb1eb2 |
| DOC032-P0039-C001 | LIDAOE | APIGROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | be68651439c1f4dffdf162804964e35ae721ca1f5fb5d303719f17210500711f |
| DOC032-P0040-C001 | LIDAO | IRO | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7d28c1574ed78c2ef4d32f16b67ba111c25d1d752326a3b677bafe626495f721 |
| DOC032-P0041-C001 | LIDAOE | AIROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7422eb03cb1265eb98fee28af797713a0eadfe722cd23fb25b92574f14232958 |
| DOC032-P0042-C001 | LIDAOE | APIRO | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3be8a4e3425e7737a5ffbf1e4dc2dca13fa675531d0573f741c3566e9e726ca6 |
| DOC032-P0043-C001 | LIDAE | AIROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4ac7c273895fdf1ac39dedb207db36c8304c8a4f32dc377aa9c85008fedfaff2 |
| DOC032-P0043-C002 | LIDO | IRO | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7fc3e91c01453147e01f0caa2eee4e70216dd5152446ecc0089e85dfd4d8bab0 |
| DOC032-P0044-C001 | PLIDAO | IUROE | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 648ccb1fb675738f4e15cae7cca669338f97db4772164880c8b4743e34519269 |
| DOC032-P0045-C001 | LIDAOE | APIUROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ed55accd8ce2c6a5c51eb1543dee36b7d3b5e5909146f6668c5a485e3023b24e |
| DOC032-P0046-C001 | IAO | IURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2fd2cb7a75713fbc143015e2846902b7d7fb44a7a8546a6ec1becb3e504e0f75 |
| DOC032-P0046-C002 | LIDAOE | AIUROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f3c9fe4190ea58527083e05fe45c6c4239afb74b14377ee9862381426689a621 |
| DOC032-P0047-C001 | LIDAOE | AIROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fad5c3c0e336175f0b812c0dfa0b03a7747ffc1c36fa5e867ab198d0a75e50f7 |
| DOC032-P0048-C001 | LIDO | IRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 787f1f6d336570e057e519da75990a279fb2ea61079e4b95eea4dcd51f7cbc27 |
| DOC032-P0049-C001 | LDAO | UROE | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 15274ae6092ed2b73b4c77c99c9e3d952c730f1d8b4e7743982b50912b2c2f41 |
| DOC032-P0050-C001 | PLIDO | IRO | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b9637e65f69237a18507d7a3d26e30c33f9606ff172b8843169373bd3ec4572d |
| DOC032-P0051-C001 | PLDAO | URO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2772f9b93fe4611899c34ad640fcc68a8ce0080bd75d4c8d861df57ae9b2ab49 |
| DOC032-P0052-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a8fe2d1340ee96ff2f7c4bbb136ab6d2a723ab02c77af01f5d8d1a7d8173725d |
| DOC032-P0053-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 493857384b0225ca6aba62c5c597e5b170bc33e2656d3598a57ebc56dea50dae |
| DOC032-P0054-C001 | IDO | PGURO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 37eccadc8fb02b071ea2f8e8d06e3d4edaa342a837698b1037ba1c632e4aeda8 |
| DOC032-P0055-C001 | PLIDAOE | APIGROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9519e2008d87a7818d101dc25e00a3ac1a2f41e0499c355a822e2e74e5e3d32c |
| DOC032-P0056-C001 | PLDAOE | AGROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e406b8fef932e9d56c0615e643c413ad2bea4569aa9c7fa68a5e394cb3a13825 |
| DOC032-P0056-C002 | LDOE | AGRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0998ddb2568fd174e8f64404db943b2769da92b2ae28e9383362a288fc0ff23b |
| DOC032-P0057-C001 | PLIDOE | AIGROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ca089c836a735b7fdd23f37f21f5cb2a97d9a9a70e231f42301d0299f0b41a43 |
| DOC032-P0058-C001 | LDAO | GROE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a24c6f98229c0c178a4fdf75264730e70d7df114ddf5e2ec83ac5f8c9c8ed839 |
| DOC032-P0059-C001 | PLIDAOE | IGUROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b81b22c4f59bf62c416de51502abec8dd4d65cf2c3326266e29606c084aab8ce |
| DOC032-P0060-C001 | LE | AGRE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0ddf732eb910925245037bf9f666716d9dca59da53b39938f610889cbb2987b1 |
| DOC032-P0061-C001 | IOE | AIRE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c131a1c1fc676c7c4336adeb67ba499c778fe21a93c3a153360a186dfedcb9b1 |
| DOC032-P0062-C001 | LIDOE | AIGUROE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2b0c8cfe508875c4cf36ad2c7f0290a9594f1b9111bf62dc38d2cc20d8257c26 |
| DOC032-P0062-C002 | I | IUR | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bad58b40d65a2b4de101d537b16eb776ccd5d558ce2a56969c9f24d0c80d6143 |
| DOC032-P0063-C001 | LDAOE | APGROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8f5d13f4b67445825b4ceba1e618faeb7ee84e58c331d5739f44e12cdcc76bcb |
| DOC032-P0064-C001 | IAE | APIURE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ac460bf17e20c01e12d23321e3c7c584fe35f293c1d19e57225ad91a3b67e183 |
| DOC032-P0064-C002 | IE | AIURE | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | df683f43ef144a049d8f0d8be79d8eec5c98dfa1b774621102eb7f878e8963c3 |
| DOC032-P0065-C001 | PLIOE | AIGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a339140c77eb1feb0e79b6bceceee6765958636cc6987d1559595596df268871 |
| DOC032-P0065-C002 | O | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fd853d8ce5c73ed39ad98954b82616134b2b916e1b18d53d3c4190d90bbbde4e |
| DOC032-P0066-C001 | PLDE | APGURE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6b66dc7fc1a4facc4bd0f34a295033568a3cc3d8508d7b22e319302eed44c141 |
| DOC032-P0066-C002 | PLD | PGUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c459af9c9479884c2dfe3c6526f33a3431b1b2eeb760a557717bfabdc465d5d |
| DOC032-P0067-C001 | PLOE | APGUROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8033a100c2e5ea8cff57b594a6e37e9acec40a12d14b85be59faa525c6e334a3 |
| DOC032-P0068-C001 | PLIOE | AIGUROE | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d959a228c569d52917711fafc32a934140089c7362f3d834c87c2f812399918a |
| DOC032-P0068-C002 | PLIOE | IUROE | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b5a2b0bdd0c17acf00c7202a0317b35868d999d666fdcb124876b94271ede280 |
| DOC032-P0069-C001 | LIOE | AIUROE | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | aa030f4707aaaaff9f877698857262a023fae52bc6cfa1fd7a771cb02e560096 |
| DOC032-P0069-C002 | IE | AIR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9ca9989af39ec549dc4516fb2fd127b9912a9cb014570c259ebd3a6ac058d26c |
| DOC032-P0070-C001 | LIOE | APIGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 015cdf1136c1009df80cb6f667713a0db639dae39e39db74c57021dbaa21ce78 |
| DOC032-P0071-C001 | IOE | APIUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9a0e58b328082e6f569dde3e5998bf03b0090950b888137785d537e83d8c2959 |
| DOC032-P0071-C002 | E | APR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8c4c823446563ce47f3fc4ddd07449c72e880fdeb20c0644fe9f0a7234285e93 |
| DOC032-P0072-C001 | PIDAOE | APIGROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c8ddde0e12a01bb2fab562928c133e31c5022edb0526ac126e2a746a9ba4daa |
| DOC032-P0072-C002 | POE | UROE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | acefc0966bf1a9903cc9ea4ca1a04b6797c6e1a0cdd115e80316785055cad892 |
| DOC032-P0073-C001 | PLIDOE | AIUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 295664399929e6574f6d2068b581e613c0015e45f95cafcc3820ea3beaeec5c5 |
| DOC032-P0073-C002 | PO | URO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0defdcb5531fdcfaa71e92862e4cad42f078bd7c8444320b1ce35165df4a401c |
| DOC032-P0074-C001 | PLIDAOE | PIUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1446bb8e5a5f5c4b45b3a431c4f44c52d333f70531aced2a0bf6185651b5c292 |
| DOC032-P0074-C002 | PL | URO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 038ab7a4538dfa8e915af3b1ae421d72907c30ef7dc3d8bb5c971b5973e527ff |
| DOC032-P0075-C001 | - | UR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e47e2b57bb8083b07eb36e575b8abdd1ecb2f80cc1f3be327068652ead43607f |
| DOC032-P0076-C001 | LIDO | PIRO | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 06d413ab18c2687d97f4d5a6188a87d59ab8fe31c1159a492305d9cd01e14740 |
| DOC032-P0077-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d46cadecd0deb15c79400357ceb91e416fc0371927fe417e6e494dca21d59276 |
| DOC032-P0078-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d17ebb270764281dec90da3822d306ebd83639ad0568fa9807565147ab432b1b |
| DOC032-P0079-C001 | LDOE | PROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e5b47cab422d1bd040bc26395a4f0ce296064ff701dbb82063502174e4e2109e |
| DOC032-P0079-C002 | LIDOE | IROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 5afa9eddfbbc517ec9eebf6b88e70fcbf80e62d52a2ae1d770a3cffd2b1855d4 |
| DOC032-P0080-C001 | IDAOE | AIGURE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 706b226519db6335613f2207c2169f71c4244314c4988b2bfadf63a5f064fc9e |
| DOC032-P0080-C002 | DAOE | AGRE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ddea17a7e1f0da7a4159596aa99f5c72307dca9f9dea3c78da5fd8fffd5080b0 |
| DOC032-P0081-C001 | PIDE | AIUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4afcfa2034511c31b1dc0ab1d97fafd3a5e3d0d54f7be476ad7bbf4646ece92e |
| DOC032-P0081-C002 | PDE | AUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | dbedf707fe676001fee350dd37d02022f379b830519d4eae2c538299d3f5fbfa |
| DOC032-P0082-C001 | IDO | IURO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a34de4bd4576120d1e564b9c42fead7cf7409f67dbdd34bb8c22fc0089f73a0d |
| DOC032-P0083-C001 | IDAOE | APIROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d2e0a56af2252c6ebd3e97606ed9828f1f2b257a34a7f06b0afd7ce35ff57e73 |
| DOC032-P0083-C002 | IDOE | AIURO | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 750dcd99c518e8063b59f56901e9e19141657b8da7fa557ea27f455fe9997419 |
| DOC032-P0084-C001 | PDAO | UROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1132869e33de8919386621e605f5edd7c350dd77d30110d8385841cd8eb1943f |
| DOC032-P0084-C002 | LDO | RO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ad8a18515712068ab42b7f48ebd4c933780b05641e5aa045ff25eeda4e0d37e0 |
| DOC032-P0085-C001 | PLIDAO | IUROE | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6ee805a4070134b8b7e97acdb5d39e9ff833e0bcb1853a02d0b65f0e07071af5 |
| DOC032-P0085-C002 | PLAO | UROE | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fab24f6ecc664faa655c6b944b659f11ab0ca4a80bd2d8463d38e5344115c85a |
| DOC032-P0086-C001 | LIDO | IURO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3d1e4a804030b8b0b6503a2d628763bd3c317efded24d5ea143cde4ed8ca184b |
| DOC032-P0087-C001 | PLIDAOE | IUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1a34c39dc2d5676a73c7f5c40491ffac4eeb298b605679a8a32f1ff67afb8c4d |
| DOC032-P0087-C002 | LIDAO | IUROE | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e3071476bdb952eb579f5d25a47a840e2deb15cfefd292b469ea8658860c7edd |
| DOC032-P0088-C001 | LIDAOE | IUROE | XM | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 644cbbe2b6756b733d85fafa7cdf9ae531dabcf0f318f6274712ad2d428a1903 |
| DOC032-P0088-C002 | LIDAOE | APIGUROE | XMG | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 277b0526070a12b20a37015323a2de6c1601dddc272f13a4aa92865d0fe275fe |
| DOC032-P0089-C001 | LIDAOE | AIROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1175147f944cc29b75367e3c34da921e989956058c3e57bb31b522baae4f5585 |
| DOC032-P0090-C001 | LIDAOE | AIUROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e3cb8ab952b954cc4211274728d55a74ef2021d3c88520dec5a0391711af1edf |
| DOC032-P0091-C001 | LDAOE | AGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e07f947a29fd8cfe0b09bbf2325be7540b9f40aeb7998871dac5da24f6c3718d |
| DOC032-P0092-C001 | IE | AIGRE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 51fc0655891c040c3d5cae08a575392fcc2d19d9a8434520a38e8635a2b07735 |
| DOC032-P0092-C002 | IOE | AIRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 78fe49be675ee81fe54f54306de81f8cbfc1c93b627f0f163263193daf9c1a61 |
| DOC032-P0093-C001 | LDO | URO | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 405afd36684f3b4e518bb3c4909014ee1b9497de9f8f234d09f2f91276f16956 |
| DOC032-P0094-C001 | LIDAOE | IGROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f2efed486791488a707c3401f23ebe7131daf8a772a5943d1dbb348c2f2e40ce |
| DOC032-P0094-C002 | AOE | ROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6e9cb2d45bdb5c8408fbb503d538fbff9521c054674c948574f0822908c1c648 |
| DOC032-P0095-C001 | PLDO | GURO | XC | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 317824e6b81afef13f2166bbc0af2389874de443922d8a16941a73bad375da58 |
| DOC032-P0095-C002 | P | UR | X | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 5310235034fad663c32cc2d92da1b64ae3d6df77b76f626f3665ad20808b56d2 |
| DOC032-P0096-C001 | PLIDAO | IUROE | XM | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 20a3544a00a706e832be6e90a558fc0426b207145f828a4b291f2e18dcdc851e |
| DOC032-P0097-C001 | PLIDAO | IURO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4b8425e19759ea610c1cbd2c0343bf605a7edc3c50405cd937c90d0c70181355 |
| DOC032-P0098-C001 | LIDAOE | APIUROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 35db3ff59cf856f3d6f037b2d24504b7286374302c891e26a59df774f42fcbe0 |
| DOC032-P0098-C002 | IAE | AIRE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 74879bc47dffd60b0049473ff3a593cd2b91d7ebc10f0343aa977ee01a3c8366 |
| DOC032-P0099-C001 | IAE | APIGROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 21a1a6325018349e0eab56b4e48b368d00c5b73761af5af38aa2e3beaaaa4f79 |
| DOC032-P0100-C001 | LIDAO | IRO | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d455a353c20b570d363dc9aab1e4cbbc6e5f8ff5e0e5345bfd8edb630563989e |
| DOC032-P0101-C001 | LIDOE | AIRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6a64ff18febf68bee5d5c2df6836dc8c2f8fd497f3d5448985c695f74d3fda84 |
| DOC032-P0102-C001 | LIDAOE | AIROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7be88a928cddac50563019e846cb933998e1a610f609ef28225993f4ccf0bf98 |
| DOC032-P0103-C001 | LIDAOE | APIRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3cea76ecbee92cf395777679f92084741e049d16c4071bc091a63c1ad6b42000 |
| DOC032-P0104-C001 | LIE | AIROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | aa818356d16fbd8138b90871f2de8bc9cb8728cb49b543df8b1fa14fdf4fca4c |
| DOC032-P0104-C002 | LI | IRO | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 087791c9a9c2b3d13678508929189ca62c591a66f869eb906fcb4c7adc7e4498 |
| DOC032-P0105-C001 | LIDAO | IROE | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a100443fe16de896cfa2f4f0e1b3338c267abd2a207f6050336fb0786573ae6b |
| DOC032-P0106-C001 | PLIDAOE | APIUROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 25683144a38cfe079d46ffd4bf2de0d31f565417e41de2192f06bda88ff03876 |
| DOC032-P0106-C002 | E | APRO | XM | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0c61c75ea049c716352d41ac42e07905dd4df355e89bbe79968e1fa3a63490da |
| DOC032-P0107-C001 | LIDAOE | APIURO | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e93ff3a3567ec5c30a9e94883332abcc9ab8fda50179f233169163e3e271fb41 |
| DOC032-P0107-C002 | IAO | IRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2041abf16f837058759ce05d5502873fd72e5e9d96772a2705a58d94e1ffc8f5 |
| DOC032-P0108-C001 | IAOE | AIUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3f1020f6056638278e5a9517fff7d91106e617f3945ec86711e42bfa29de55c0 |
| DOC032-P0109-C001 | LIDAOE | AIROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 202a8ffada246256c3acea31a377d3e5d217acc4bf006d4293d9fc613a12136c |
| DOC032-P0110-C001 | LIDO | IURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0afe048b37d19038106f5956f3f70bf9e499a8df61d5a3e3ce146d8257fe39f8 |
| DOC032-P0110-C002 | LO | RO | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7b7f1670b6e3304a7d15c5f78597b1b928280642f3ea2d1c3ee3fba76a861a0c |
| DOC032-P0111-C001 | LDAO | RO | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 40649ca0da07d34323b54ba7000bdce977deba047680d0204e1213b873d8aa25 |
| DOC032-P0112-C001 | LIDAO | IRO | XC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d19082ac21b7b4561765538d2dada80c5ce5ea3cb5d67106415b37969738aa80 |
| DOC032-P0113-C001 | PLDA | URO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3c52d40f1d4a01c3b4eae4a7a5d5dfd9a41667d6d191b175ead4652cdc6242e2 |
| DOC032-P0114-C001 | LIDAOE | APIGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e8401c37be9d40720c0ddd4db8027fce960c9bfe9789c18d33047b39d2ef7ff5 |
| DOC032-P0114-C002 | LIDAOE | APIGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b8e76db858ae2ac6d3cbda119558898db96cb200157aa16f9a72cc95ad39cc98 |
| DOC032-P0115-C001 | LDAOE | APROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 04170e92f381ff598f3d6fa5069de4bfd5b5181bd995f5dc517a01d4ef700274 |
| DOC032-P0115-C002 | PLIDOE | AIUROE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0f072718180fa435397abf2e12d81ad36d3b8d3d39e3f5aaf55f69eb941245fc |
| DOC032-P0116-C001 | PLDAOE | APGUROE | M | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | d45ba5cb7bc5e4ec223efa6c1425b255b8777b7ee72252a93612a9b19b8984af |
| DOC032-P0116-C002 | PLD | PGURO | M | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 7b8502f447eb506db58bbaec5ced5d4574441c3c196b5c87c1fb5b98f54f90ba |
| DOC032-P0117-C001 | PLDAOE | AUROE | C | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | f37cdbfe85dc0acfc6f1a43533480a8c7ffd7a4ef7e007135637fc7d6eb4f7ee |
| DOC032-P0117-C002 | PLDOE | APGURO | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 6136e95d03e87f7bb1d2372e64d382679660fc489abbbf99e7ae2bdbf6e4c7e3 |
| DOC032-P0118-C001 | PLDAO | UROE | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b74190f8b3d0779f6566d77ffa438548a735b1d8e1428345c6f77d937b4c0268 |
| DOC032-P0118-C002 | LDAOE | ROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c0bc2a4f7a94743e7d16c808513de628e6ff9d8ee1dbc9333dc5db1bdbf300fe |
| DOC032-P0119-C001 | PLDOE | PGUROE | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 3ccdadeeee62bc0d043062890da83368ef765c7b0e3e062722fd38c0aaccd930 |
| DOC032-P0119-C002 | PLAOE | GUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 7ad296ae1deb1b5357b62fbb8d51ec5c523ca50cd3f2bc56c3a2fbd4d21b6281 |
| DOC032-P0120-C001 | PLIDOE | IGUROE | XMG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 0aaaeab9c3d0d116844705ffcbd682e3da2055db66e449471ad92b9baada686d |
| DOC032-P0120-C002 | PLIDOE | PIGUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | b99108943992de2909b0208f65fa7dec86362270f8af12493aad48eea70306b9 |
| DOC032-P0121-C001 | PLIDAOE | PIUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | aff4073454aeb6d55da5093be18be0d65fd996e9846f93f65df64dd1b1c9d92e |
| DOC032-P0122-C001 | E | AGR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3eece2705161a0df334d9425d7c24a91ba8caa8303a82da0d009415b2a2dcd79 |
| DOC032-P0123-C001 | OE | APOE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 32a28f70f2faa896a7f5f93c351129efbca64c1aa152437f538effe3c3295a76 |
| DOC033-P0001-C001 | FPLIDA | PIGRO | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | bdcd12a825b8e75858d9ca1334f7b7874312cb94640b2b594b642c989e210219 |
| DOC033-P0003-C001 | FD | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9700405d7bc85ff7c4ef62cd4df2ee73d4963cdf929b06c63453bab9cef69390 |
| DOC033-P0004-C001 | - | PUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d9a7fa7b58336b024f2ff8539af7f785fd9f441f033c0b4c046e430248ff5e98 |
| DOC033-P0005-C001 | FDE | GRE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 54d50bf484875cb84cc33f1d1ab9a742935ca04ed231ad368a7bdd56743c1f08 |
| DOC033-P0007-C001 | FPLDAO | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 46a401463652b8be9ba4550a3d1cd916c170fc650cd1a97bc81846e21d4c6ef5 |
| DOC033-P0009-C001 | FPLDAOE | GUROE | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 3e8c77f71739ae6cc09217951be65b0c58a23ee711a5b4e86257e3a529c176b5 |
| DOC033-P0010-C001 | FLDO | GR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | b8a8913abea19315426fe647078855b814ed836d8d6a0f308b8a3428f55aed5f |
| DOC033-P0011-C001 | FLIDA | PIGR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 06f211c63f7e913ac2e04f978684e264ca1e750386c139d8b53574428077c5d0 |
| DOC033-P0012-C001 | FLDE | GRE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 85c7b8c9a8451bff311b2f14c6000dd257bf0b18e95f24b1db9b2e9aa0f71bd8 |
| DOC033-P0013-C001 | FPLDAO | GURO | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d422ff4dccad38a1adc3b170f6d6ae32cd9d3dba86d1ad762ebb6e0faba11ce5 |
| DOC033-P0014-C001 | FLIDA | IGUR | XM | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1fbbb363ffd8d98fdcec7e5e998a68086a00e0fd8e1e3000653bd1f98326c1b5 |
| DOC033-P0015-C001 | PLDO | GUR | C | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | e26f58f326891146d50256bcc98026c611fd425927359aac44030a36c845a448 |
| DOC033-P0016-C001 | PLIDOE | APIGROE | XMCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d28ce2d776e275443aa8250cf372d29a0e29c81687b741ba5c03e3a21403ed73 |
| DOC033-P0016-C002 | FPLD | PGRO | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | e22a49e2c85346c336513ddee2d2bd828b0317ed1eb9afacc349329373fd8d0d |
| DOC033-P0017-C001 | FPLIDOE | IGUROE | XMCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | f1a3ad68e02bf63a965e362d52f42a23fae11d280f7a02859a541335e049ae63 |
| DOC033-P0017-C002 | FPLIDO | PIGURO | MCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | c37996e58121fba45afac63fdf7db5b5b42ac1ff4eff75e54b86f21aa6398388 |
| DOC033-P0018-C001 | FPLIDE | IGUROE | XC | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | ec6102e84d4e5a04b43d7cd8f6698c7c7c871a0b5e9544e5b050aea2e1149aa9 |
| DOC033-P0019-C001 | FPLDOE | GUROE | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 49d9c9947526fbf01a3e75e4113c83a412e0c12af86db326c671fe7f2314f2d2 |
| DOC033-P0021-C001 | FLIDAOE | IGROE | XMCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | a303bd016ac1ffd82cb17d47967666fd2f34e8c3672b329bb34b5dfa32fbb1cd |
| DOC033-P0022-C001 | FPLIDAOE | PIGROE | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 67a5e59902eafa99e5ff3e4e808afcca57546e284eb9a78c69233a769fc0db4d |
| DOC033-P0022-C002 | FPLIDAO | PIGURO | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | f19500967a7bd35735559663d1ed976cd7962210b25258fcd30a48db1f87015d |
| DOC033-P0023-C001 | FLID | IGRO | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 0b9f54795fac7a4c834c61068fa700d327efb3ef7a5831dfd7f07800dec28e2b |
| DOC033-P0025-C001 | PA | PGR | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 16664000adecaacb2ba2900fc84ff28b961462341df304918e32926719d1182d |
| DOC033-P0026-C001 | PIDOE | IGUE | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | bbaa767f510c0e5629366e0dbd23ea99647346119a6cd85917fac0f867b9c55a |
| DOC033-P0026-C002 | FPID | PIGUR | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 89d9a453c75e49c1b42286f1817061144aaf899d144953e54825ada530977af0 |
| DOC033-P0027-C001 | FPLD | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 4b7945f1b535af412e94daa708694737fe7039731dcf0dc845b9a5531c45eec7 |
| DOC033-P0029-C001 | PLD | GURO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 98c7b5fa8fd0f5e17c6c780e697572055b8be797e8633c094de1506a97e7fd6d |
| DOC033-P0030-C001 | FPLIDAOE | GURE | XMC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 308d266a3f6795e58c840f0bad98abf7f175696d597bf081ebec6cc6bd6cc335 |
| DOC033-P0031-C001 | LE | GRE | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0fcdbb074dd9e9ae351cb78575f9ad8454f1c88c8ee68a78569a36294bf59d03 |
| DOC033-P0032-C001 | PIAO | IGUR | MC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 11ad95a4056a76ad2220f9a05a05c20b0e107a326b08010def3c7b2b893effdd |
| DOC033-P0032-C002 | FPIDAO | IUR | C | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2ce6bc5678cccd0909adca76365668b3fc259f487a8a59d1262d27979b73fdad |
| DOC033-P0033-C001 | PLIAOE | IGURE | MC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 5a9dd5e80f324926ce8024cbfee83b9d18b416da2ab19d21e4eadb04092899c5 |
| DOC033-P0033-C002 | DAE | RE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 84300e3699af3c2a004c06ae53f641a45e57886e82e440cf2a4791625e3fd9f0 |
| DOC033-P0034-C001 | FPLIDO | IGURO | XMC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9da909a0fd6c308849517d51cff066df26ffa7078a63adc08e0a3d879f4e3d2d |
| DOC033-P0034-C002 | FIDO | IRO | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2bba0b7929b477b1815bfdd57da044ec401780dedda4c3ef3f6be9f94ee6494c |
| DOC033-P0035-C001 | IDO | IGURO | XM | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 159b2f57e0ac9326052313238d60d4bd542d874fdfb69040369f1a4352ee478d |
| DOC033-P0035-C002 | IE | AIRE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 5ca6cebafe8d58c78c96a8ae6616035104c1e776044d2fcf4aa4759d3828669b |
| DOC033-P0036-C001 | PIDAO | AIUROE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 241421fe8b4f36393a3d0852ffe2f69355d303a2a663a79ac858eba5216dd072 |
| DOC033-P0036-C002 | FPDOE | UROE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 055a720042663f884accbbf24fec75200fd6499e657abbb579e0dbdc6ec89be2 |
| DOC033-P0037-C001 | LIDAO | AIROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | dc74d78807a1132477970b07ca04a54756b4ade3e92e1dcc602fc834bac2c96d |
| DOC033-P0037-C002 | LIDAOE | IUROE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d2834ceefd2445bec0b908cde8043ddf03ad7d9f03b3d4095e6f0a910460b796 |
| DOC033-P0039-C001 | FPLDO | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | c044ed68f41f13544694de0b48352f0b9fd3c19dd17a7e4f360007b6f1af2979 |
| DOC033-P0040-C001 | FPLIDAOE | AIGROE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d9d8b053c6f9ab460798a6f3591cc55a4ea4230a6c97175ae414183aed9da385 |
| DOC033-P0041-C001 | FPIDE | IURE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 144e3954ddf478c1f26a2ed139b34aa7d0481508ca27f8431584e88d2438dbd3 |
| DOC033-P0041-C002 | FDE | RE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9fb92e31d3fe81118ad439690b33a221f585cbe1935bc9cad4edfdaa184b5c3c |
| DOC033-P0042-C001 | PLIE | IUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 28e4fb1e40c31ff19126aeb59ce1dc6d9a92a39791055105de5383f6d92dc7c8 |
| DOC033-P0042-C002 | FPDE | RE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | ead19f35dea1b38c9be36c1575ae6a7a931b17e33e4790d92606285e08fd4edf |
| DOC033-P0043-C001 | FPLIDAO | IGUROE | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 80eb0dbe945e868624ddf364a845150d22be2b3362073430de32188fd78e78d2 |
| DOC033-P0044-C001 | PLIE | IGURE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 19a80428eac179fb715d34cd6b072f6bdf4e9aa48cea302af905107a78910bf8 |
| DOC033-P0044-C002 | FIDE | IRE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 5d3d48d32d7f2ad6797a5d8702f614bc9ea92dd94b4922556067ba5435a910a6 |
| DOC033-P0045-C001 | PIOE | IUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 3560f6fb5236168e7acab2381e614033f2449a9a378d5b4506915e974a7f9829 |
| DOC033-P0045-C002 | FPD | UR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | ca0e75362daced10e2d02ecd35b412e35f529a0a1a5c7ac1683127284e004704 |
| DOC033-P0046-C001 | PIO | IUR | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0bcfcf872d783096c91820a27cd2f36ff2352532913aa2642d97ddddee7343bc |
| DOC033-P0046-C002 | FIDE | IRE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 6f24f9439d4d2056d55ef7adfdd2df84d6b54aec094a71ef6023654a7d89bc4a |
| DOC033-P0047-C001 | FPIDA | GURE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | c15505304ebcbd769d515130109037cd37d3f29c8de6b32c772b32c657a4310b |
| DOC033-P0048-C001 | PLIA | AGUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 561a3aa7d0fccbba01765ebcec69137c2d1acbeccf0313ea6fb5e1e7639db99e |
| DOC033-P0048-C002 | FD | AGR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 8f34f153397fdb39df8dd6878ce6fdee08227bb94fa01a5cb662b5b0a89ae787 |
| DOC033-P0049-C001 | PIAOE | AIGROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | f50381ccbc7567848ff58c6154b77bf0cd5e7401892cd77b76706f7c45e24bbd |
| DOC033-P0049-C002 | FDAOE | AGRE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | a003138cc404c4af3981e013be9d92c32a075043300f88f9b3534a2ddd578f42 |
| DOC033-P0050-C001 | LAO | AROE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2fe8a26822466267553642063381c38596e19b8741ef17b7a21f8e7bdcb5b977 |
| DOC033-P0050-C002 | FD | R | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9c179148c9374bbb29b8d43f1f646bbd3cc177448964cd06697479ba2100cd7a |
| DOC033-P0051-C001 | POE | AUROE | MC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | fa6bd59729215da498f236c12911affde27a0b9016be2e20055aa9a4f6f27844 |
| DOC033-P0051-C002 | FPIDO | IUR | XM | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 15191cc07d9d1583b3c3e3e0eb42d81c6bca8dd2f8a201e6349a5ea1ce1543ac |
| DOC033-P0052-C001 | IO | IRO | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | aa3d3ea93b98d86c922b40ed34b2da5094d7dbc32765f3bded8c6712fab3aad5 |
| DOC033-P0052-C002 | FID | IR | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 7e8960ee03afba5c1f8b8aabfd3a0926719a97b7982c1693ba4149203deb1c9a |
| DOC033-P0053-C001 | FPDO | URO | CG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 6c05abc018489c43cd5ab95765095d5f48626a99f59250e2e9e76a4644832ab7 |
| DOC033-P0054-C001 | FPDAO | UROE | C | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | f94b7b5190fbb4b991a846160a4f1d87c79ae461524ac35bcd6fe3dc90305854 |
| DOC033-P0055-C001 | FIDO | IRO | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | bde9577ae8e3521fb1113abf9ba2423fed2b440fa566454783a195e705d3bf34 |
| DOC033-P0056-C001 | FPIDE | PIGURE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 34d01fab0a795fb92131b2788e9eb5c9ad92ddc35d314f9b4ceff38ae28a9653 |
| DOC033-P0057-C001 | FIDA | IGR | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 19bf0476de90ecd223b3c2b818c40288b4338961cad6cc11f7d96c92a7748008 |
| DOC033-P0058-C001 | FPDOE | AROE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9f3c8858782836608bea2dc938e9b7308c87067b9202f2cda6755c7080bcfb1e |
| DOC033-P0059-C001 | LIDO | PIGURO | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 34c773f3b04ecd526e006960f912a34013aebe39caafbf90635cb5e56ffaa102 |
| DOC033-P0059-C002 | FD | UR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | b5766cd11eb1efcb5385499ed55feed6286d9174a5d3a13ef223d3c797a3f2ef |
| DOC033-P0060-C001 | FLID | IRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 7a5949722094dc7405b5d5ece4f85008839eb68fd77491eaf4e8dd3cd7b76086 |
| DOC033-P0061-C001 | FPLIDAO | IGROE | XM | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 371313ea5dcb078908fc7214df69fe811fe077f3af9ad4e970e8240df0abe043 |
| DOC033-P0062-C001 | PLDAOE | AGUROE | MCG | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 7634c40bf35c2cf1b1ae8d9f65a6f57c0217e10958851ab3657a2fd72b327a85 |
| DOC033-P0062-C002 | FDAE | RE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 8c7553be3875cee26efe30903c8147a01b886ca2c73c0b13a6cee2887af7345d |
| DOC033-P0063-C001 | PDAOE | PUROE | G | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 4532fa75430dae592f37c1950f1fbb5088c42e1d172a086056621108d77c3ba1 |
| DOC033-P0064-C001 | LIDAO | IGUROE | XMCG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 9ac9266a39afb0155f9b406ffdd0e958039005e2a17b78875f56acb4a08165c6 |
| DOC033-P0064-C002 | FLDAO | GRO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | e100cfa99b95b029dd9a1b1b775d4630876e9e88d5b81487d10b0b843031d83d |
| DOC033-P0065-C001 | LIDAE | IGUROE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 327f8bb56371f57363af2a025f480d475294dd91244f9c3fc051c954d8474150 |
| DOC033-P0065-C002 | PLIDAO | IGRO | XC | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | a397d9988cb7c87a4f19f89119de4bf338c4e469000d7a6e784ba998f4de6801 |
| DOC033-P0066-C001 | FLIDAO | GRO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | d600e8d3e133908424bb0e97e42542c8661d3cf5ea4a5dda480c77b70d3f96f0 |
| DOC033-P0067-C001 | PLIDAO | IGRO | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 4e34b60042881ea38d0bc4014ccf1b73801f567cd96452ccb7a7590f66e60efc |
| DOC033-P0068-C001 | FLDAE | AGROE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 48ea1d918f8120a624993b6eb2d1d29addf068639471ce812eda0482825b9271 |
| DOC033-P0069-C001 | PLDO | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9f1bfee6b674e7958710132d9ff0cfb41b6fd78c4b0b2e6943abe3a2fe204614 |
| DOC033-P0070-C001 | FPLIDAO | GUROE | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 08b066bac5558645bb6a50012ff6749f46e50b392f2c17ac39175d15399ff9f8 |
| DOC033-P0071-C001 | POE | GUROE | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | fee3e92f3b76405cc28aa364507b8e93eebd33478f5a4766a02f3144195d266a |
| DOC033-P0071-C002 | P | R | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | c91c2c47137c1b7ca5e8a157124a20c8ac42a925e70d3bf6e8a3bda2c7b75aef |
| DOC033-P0072-C001 | PIDAOE | IGUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 4caa177bfae17ef090fa689ef90a48955ef09ee92d4bec1d279b86652ed79edc |
| DOC033-P0072-C002 | FID | IR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 78c0b9e63e2b54c7662b65d94782f07eb26d64cd70f8ba5fcb769bb5a7dd9ec5 |
| DOC033-P0073-C001 | PIAOE | PIGURE | XCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | ec82bca3e394a3ca4519034aa6ceebc8070950faec59ac9f26a054c604fbb3d3 |
| DOC033-P0074-C001 | PLIDAE | IGROE | XMG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | a5fa4d56d464cbb371fb3515910830043ac2a312d1b1628e604935305a8fd401 |
| DOC033-P0074-C002 | FPLD | GUR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2a0df4dbc18c3cd87bfdca4ef733d7444b309c6de9d8c17256f60d5251524eea |
| DOC033-P0075-C001 | FLA | GRE | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 61440dc6d20b8b18dc06da17e3222dd8706b78ebadaf634a0d8aa09bc4ca6c3d |
| DOC033-P0076-C001 | FPLIDO | PIGURO | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1bf84e2c6412d4b2ad8c441959b365e8bb65ed06900dc9d6dc870dc7bb15fc5b |
| DOC033-P0077-C001 | PLIDOE | IGUROE | XCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d61c688b310b7fcb398ddb24248b5957abbb9717e5de01cf72cd732d0dce9546 |
| DOC033-P0078-C001 | LIDO | IGUO | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 83d684fb4aff7f0ba3340d1816636db35aeb3306f3561f907c08c1f64a7f48e1 |
| DOC033-P0078-C002 | FDO | RO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2b5f39f653d9362e07729a8b974f811a299259c5b67eef232ab633c03e1d7b9c |
| DOC033-P0079-C001 | PI | IGR | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9f4666ec06ac5e82ddf733c77b61c5a897559c5b5d232cabfb2d7c77831c0bb0 |
| DOC033-P0079-C002 | I | IR | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 108b9d763aeded844197bca0be26024f93362289d819ff059ebaa8d0c74888f7 |
| DOC033-P0080-C001 | FIDAOE | GURE | XMCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | b40781520923b2cd135f91fb6ae6a8315ff69c49cdc58976ea5b9b30953eed44 |
| DOC033-P0081-C001 | FPLIDE | IGURE | XG | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 5c343d55d9b88461d868e4ce68b8c5178544470108860dabdf43f3f2d4baac0d |
| DOC033-P0082-C001 | FPLIDAOE | PIGROE | G | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 342abc160723621e73f4c8a37f367c41ecbac837fb9f7a83ffa6b547da1aaa7b |
| DOC033-P0083-C001 | PLIDE | PIGRE | CG | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 98ab5ac55ff86ec8f16535dcb13ecec727978aa6dcde085ed4533a150932d24b |
| DOC033-P0084-C001 | FPLIDAOE | AIGROE | XM | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 9de0b9c24a14f7b3b57b1c129f0476551a37ea1eae42898262677844d82e7082 |
| DOC033-P0085-C001 | PLIDAOE | IGUROE | XMG | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 6cfe64ad12fe12af51def7f3fba9281c2bd7be7e71bbf9f969832a4def35c148 |
| DOC033-P0086-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC033-P0086-C002 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC033-P0087-C001 | FPLIDAE | AIROE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC033-P0089-C001 | FPLIDA | PIGRO | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | bdcd12a825b8e75858d9ca1334f7b7874312cb94640b2b594b642c989e210219 |
| DOC034-P0001-C001 | FPLIDAO | PIGRO | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0c989069d771c0b92525b21f783fd2d28e5f07f9a555a0c352c7145369411490 |
| DOC034-P0003-C001 | FD | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 09f8faed975560989a8412ea8c2422dfd481f9b5eaa6e3d754619308eead0cd3 |
| DOC034-P0004-C001 | - | PUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b35ecce502df3fb49e34ad581a153bc9b3933b804bfdf0e462a0b4e8ea311da1 |
| DOC034-P0005-C001 | FDAE | RE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c210abf1e264664e3aa32379919bd47f36ea4c1390d9210145403ff31f8727da |
| DOC034-P0007-C001 | FPLDAO | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 2b2b68b75880ebfbfe9570a5c2e9b42855035b9bf049ade601b7a31aeb012c41 |
| DOC034-P0009-C001 | FPLDAOE | GUROE | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 4ca64c0c819df4c3d3424aeb587c0bbd441faa6b90b586c446da2fe816303b40 |
| DOC034-P0010-C001 | FLDO | GR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | a9e88eef278d70d7b5f3b77aa27b2589d419b6a8bba9597fd89b7c9be9c67db4 |
| DOC034-P0011-C001 | FLIDA | PIGR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 16422f5855c938c3433b431749b71600a9466a0b7513354bf1de6ae8ab1f3b4d |
| DOC034-P0012-C001 | FLDE | GRE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | a3c23ae968f124f2b2c870308e0833a442a5748dc106633c814c71a8ad1792eb |
| DOC034-P0013-C001 | FLIDAOE | IGROE | XM | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 1a644563d77b7695b099a4749ee20e5ee774a999fe4f74ec43904eb3995bce82 |
| DOC034-P0014-C001 | DOE | AURE | C | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | d0d5581d9744d5ac1700ae3788d066fa9583db372fd2755bfdc2c8a7d75fab3e |
| DOC034-P0014-C002 | FLIDO | IGUR | CG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | e943b775f2874a9e923d167886252b6fe18955d936541322e78c959ce1b990e5 |
| DOC034-P0015-C001 | FLIDAO | IGUROE | XM | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 7581cebea03b96f1a406587f3dbd8c314c9679cce34e7c72b1f677283ef2f7e7 |
| DOC034-P0015-C002 | FDAE | RE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 7e98532e3d8f1fea5df8b16c04b605a891b522ce2485186d262a772a4d2f5998 |
| DOC034-P0016-C001 | FLIDAO | IGROE | XG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 9521a496f7a81a2e8430faabcf4a75623405fc7cf1bb2abe63dd09a1cbfc851f |
| DOC034-P0017-C001 | D | GR | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | ba0b3408ad6bef143beb4843319ca477cabc691068aaf91d648c78cc8652a37a |
| DOC034-P0018-C001 | FPLIDOE | PIGROE | XG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 6ad0822f983de9369d8394c2de686396306cdbef76dfc2e86ee4afcd0ab5d916 |
| DOC034-P0019-C001 | PLD | RO | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 02b58a67ee3c50b3efb81a8f657d1c4eaae6108598582486b8c9343b84b2dfc4 |
| DOC034-P0020-C001 | FPDO | R | C | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 20143f2cde873de90707e31ededa43a2bf3857cc2d5c5e8e60142df2906b6f9e |
| DOC034-P0021-C001 | LDAOE | AUROE | XM | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | d45fdba1255529234463730ca0a9669f3cfef7ac5608100ba65c27cef8c29dac |
| DOC034-P0022-C001 | FIDO | IUR | XCG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 9a7c956dd8f937868b3547bb0083c645e1307175191b160685fbe8141c70a6c0 |
| DOC034-P0023-C001 | DO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | b489a7a79342f9f6bab29363e8940218ed0791de16b231231596ce52b3c54d06 |
| DOC034-P0024-C001 | FDO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | b88b418f0183c1d2ade67d348af3bad2a7bbc99b72efb260c2ec289da5336d25 |
| DOC034-P0025-C001 | PIDAO | PIRO | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | d3939d4b97584a32ebecee51e2c1e4012f5a26f2c5cc4bf96ffe13c55bf3b942 |
| DOC034-P0027-C001 | LDAE | GRE | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | a1d295c10bc52620ee8a45f430b7b7aebe6b2397c15c85def978cb142c228bf1 |
| DOC034-P0028-C001 | FLID | IGRO | X | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 89f4ce38980d00808189fc980ce5dbece587ed27faad2ac57dd49615c5e9f4d6 |
| DOC034-P0029-C001 | PLIDE | IGRE | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 89a6b423048d6cb756e5f87e131f1347217f6dfd68574422b6facd57cabdb859 |
| DOC034-P0030-C001 | FPIDO | PIGRO | XG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 23697189ec905fc98ad29c1592b0d088dfeacc0c4d2a0325cd6dc2e6e3133aab |
| DOC034-P0031-C001 | LID | IURO | X | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | f063c4020704cef7e650738f9a6bfdfc7d3896e4f2daa8a9fe36f8bcb0836ae4 |
| DOC034-P0032-C001 | FPDO | PGURO | CG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 573f9e07e67219d41f4bff1987b3d8aa0d6932493d1025dab828d0ce53f8f9e4 |
| DOC034-P0033-C001 | DOE | ROE | CG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 2ae90b25ec4ed7bd4598deafe76d55b9be2601db774e322b4befdac330a360ef |
| DOC034-P0034-C001 | FPDO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 7314c840b651872fce252d3dbc1872a47318f45da8d8c9316dbe19b22b3b1ec9 |
| DOC034-P0035-C001 | D | UR | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 673651f119858d73e16362959e37d79ae7535ad32504990dfa48a91739e12441 |
| DOC034-P0036-C001 | FLDAOE | GUROE | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | f945edcab3085341e74325f7f3b0c57bb087e4e44aede69d35ac902a42ccd8fa |
| DOC034-P0037-C001 | LDAOE | AROE | M | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | ff6f72bec8ccd0657df597d680a1a999a0cd5664117efcb56cb9f46b54b2a582 |
| DOC034-P0038-C001 | FIDAOE | AIRE | XG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 5546ce6723fb1f127d15b30079691db43be36f1b89addea848487078c9ffbb05 |
| DOC034-P0039-C001 | DAO | GROE | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | f538485c11fc9c7ffced46491b5f765ff4a77231ef0fd554f84850505ed146fa |
| DOC034-P0040-C001 | FDA | RE | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 7b5d57e4a9bfd7133f6dad6f15358326bf778e65771bbec50e9ae387f66ad2e8 |
| DOC034-P0041-C001 | LDO | URO | CG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 7594ebac60269cde5095a65f33eea68053b0b7e6950cb6295ac04f2209435a0c |
| DOC034-P0042-C001 | FLIDO | IURO | XCG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | c9dc8af5344b46cf4ce0dd20ed40c7443d059bdd29a744c8ffcc42a9af5d44ae |
| DOC034-P0043-C001 | ID | UR | XG | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 2e2388880d2e54dd3d7ce4baa6e61d21a3fcae3ac8d56de634a9ea4f1276f012 |
| DOC034-P0044-C001 | FDO | URO | C | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 101f5710190d8a376143ecc2a5a344e9e7f8c8145f78d67519dd62798f007451 |
| DOC034-P0045-C001 | PDO | URO | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 17a7b322c297e15abbd41d38608ce5760dc3c62f13210cf3f21c91ecf2aec45b |
| DOC034-P0046-C001 | FIDO | IRO | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | fc024c463b5dac6bfed04e9f075da687fd9a266bd3005a7a28fe1ee516719929 |
| DOC034-P0047-C001 | DO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | f60cd3d677c6533b417e860b20e03486c53ec029ed2d7119fef789b951b7807e |
| DOC034-P0048-C001 | FD | R | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 90c66cb66489b294a7e9e0d24f217fd8348e6747827417a0f117c9c125d2a132 |
| DOC034-P0049-C001 | DO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | d3f01cd339e1dae1f19b3cd9b320dab88923ab83b04aebedc2bb02dd4a778e9c |
| DOC034-P0050-C001 | FPDE | PRE | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | aae16d6bfa2a9d1dc9f8c2727b6601ca0c98d3abef037a978e3015d4aedc82d7 |
| DOC034-P0051-C001 | IDA | IR | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | d602122105e147b0d2926ea0e139dcd9e16554a8409580b996620cda0fba92f1 |
| DOC034-P0052-C001 | FPIDAOE | IROE | G | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 66c6c2f7e117823e68c22af9ff9bf2c62aa6ba687258f773b56a46827f6097d9 |
| DOC034-P0053-C001 | PDO | RO | - | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | 2f517c9bf8dd778708d3f03d6cbbdbc89cabd2247f3a214e7a5a3492e0eb40ff |
| DOC034-P0055-C001 | FLDAE | GRE | M | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | c2ab12d819b6bfbc4869273e3d501b542fc97e38c29d595bd2172d150dc8753b |
| DOC034-P0056-C001 | LDAE | PGUROE | MG | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | a0847b80f0ac4c87446233124cf62632cf4711789eba314db0f4abe0d2929aa7 |
| DOC034-P0056-C002 | FDAOE | UROE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 66a54d5e21891854753747400eb829fdb6f3b42c47a3a008cfb44a69908c2cfa |
| DOC034-P0057-C001 | LIDAOE | IGROE | G | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | e2aa83b472e95d0e4b55529bb8ce6a91373ba66eef7033ff45f1332b28132ee7 |
| DOC034-P0057-C002 | LIDAOE | AIUROE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | 4ca6b937ff82cf207f00289d01ddc5ac380fd7e70494736a56e756a3b9540a67 |
| DOC034-P0058-C001 | FDAOE | AUROE | G | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | fa1b0f9bbf995bb0a830cd4f376723ae5140152b9ae183ab3f37df3ae386a855 |
| DOC034-P0059-C001 | FLIDAO | IGROE | XM | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 8498299329f2251101dc97bb7c942d4c1355f518590fc81095e86ab76b1e4c70 |
| DOC034-P0061-C001 | LIDAO | IROE | M | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | af0084e8d51b01bc9a022e7a8d82fd85c750735465ebdc27efafbeea7aa77df8 |
| DOC034-P0062-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC034-P0062-C002 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC034-P0063-C001 | FPLIDAE | AIROE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC034-P0065-C001 | FPLIDAO | PIGRO | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0c989069d771c0b92525b21f783fd2d28e5f07f9a555a0c352c7145369411490 |
| DOC035-P0001-C001 | FPLIDA | PIGUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1dfa30f7e3949cbd4e3f44c32c5a04e6da11cad8c398f8a257b48e38d98686f0 |
| DOC035-P0003-C001 | FLIDA | IGR | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0145a469c9e6d2eb5379315190b6171c2cdd96207bbc9a3c38a339b34197d323 |
| DOC035-P0004-C001 | - | PUR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7b00d937868ddea0bea9e2a4c1e2f46749a42693b11ab1bff61b80e6ca7a6c42 |
| DOC035-P0005-C001 | FLIDAE | GRE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3d5c385a16aebcb234938cb4c8b4b7d3c2bcb8daa5b4556d6907554e193eb3b8 |
| DOC035-P0007-C001 | FPLDAO | GRO | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 19105cdeb9afcb4c26351a9c327bc55c2ffa726fd8f27577696f199f785352d0 |
| DOC035-P0009-C001 | FPLDAOE | GUROE | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 5a0320be837165ce775ddd842ae6b2de93fc76491badd129180ed894f8fef950 |
| DOC035-P0010-C001 | FLDO | GR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | ef767d14aadc9e07ae3e398e27460fbfee0c912826d0b22497044e7ddf71da60 |
| DOC035-P0011-C001 | FLIDA | PIGR | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f51b1b4d5d1c0123d83f8ffc80f878ce0c13d5eed0168953517e06a1e5753c48 |
| DOC035-P0012-C001 | FLDE | GRE | - | OTHER_NEAR_MISS / V | IRRELEVANT / X | NO | NO | ff010429678e77055c41620d9936292e3df995d5ded8064f83a5929a4a4988e9 |
| DOC035-P0013-C001 | FD | GR | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f4ba8b91e8cf0ec42ac72d7d6d91ca0fbae40bfbb7cd3d450c73d02037e51e16 |
| DOC035-P0014-C001 | FLIDAO | PIGURO | XMG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 1575cb9b7594c3b1210b3da49ff6d32ba07ac11a0749280ffe9e01bf65b7cd2e |
| DOC035-P0014-C002 | FLIDO | IGRO | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 53e569033652faa9bb5a1c49b17af1e90bb06a68aecf81bd97cdb9f8f71d5ec4 |
| DOC035-P0015-C001 | FLIDAOE | IGUROE | XM | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | a8b86847953c45ca91f94429ff1f32530ca2379b71cb07a27f1c135a223c9d6d |
| DOC035-P0016-C001 | FLIDAOE | IGROE | XMCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 2cea5d509d326098a66acd61fb92c20929b2ed2a113fe4de31db06b3f7c03d54 |
| DOC035-P0016-C002 | FLDAE | ROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | d00f2c4ddf28ca021ff5c7c19e94f975d0e92ca1416e79c9afb8f4d12d19d558 |
| DOC035-P0017-C001 | FLIDE | IGUROE | XMG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5280a14c6d4b65e5ce55390aea5c65f4844f2179a64e8ba8618626951962ed1e |
| DOC035-P0017-C002 | FLD | GRO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 8e1e1b7ffdec1263e317a56758fa4745c2a3733ce9889ac6eed735c7c727beb4 |
| DOC035-P0018-C001 | FPLDAOE | GROE | MCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 38d264a4993066e256b3d865ffdfb9f5651116f906cd0f829603d5db2464ab6c |
| DOC035-P0018-C002 | FPLDO | GRO | MCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | e967402dbb6ed68830235034313de7522e46595956dbdbdcc96928cb48db76b1 |
| DOC035-P0019-C001 | FPLIDOE | IGROE | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | d991780583bf84fa387426eef65537f006a1a01ab2845dd7b78137a5fe76d966 |
| DOC035-P0019-C002 | FLDE | ROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 8bf7e80db5301d80fb84983c7897f27912a24d60ce5e845976a48b9444ef834f |
| DOC035-P0020-C001 | FPLIDO | IGUO | XC | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | bf01170237dd1b0e5d31e55fab80e929f6075bc347ea0691229151a1c7e105a4 |
| DOC035-P0020-C002 | FPLDE | GUROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | b5d7f509ac8fbdf268f33b13da0b19df752094958019997144378b2e04e39b83 |
| DOC035-P0021-C001 | FPLIDAE | IGUROE | XMG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 8108a63e3549fe95d1d50baed2edb97be703ce3d88130318d26b0b2868e8525d |
| DOC035-P0022-C001 | FPLID | IGURO | XMG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | f7bfabc9a9b18d0d9afb9db6ab0e99ffbe885b1d54f8941fc5eacd45a68c2323 |
| DOC035-P0022-C002 | FPLD | GURO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 656b620d873997dc561a653c423f738615aba538ab6d72ce237f32a684888b91 |
| DOC035-P0023-C001 | FPLIDO | PIGURO | XG | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | b1fd582edd13166a436a89e101bdfdd029b54944c51e4f37feb89b5df81605a6 |
| DOC035-P0023-C002 | FLD | GRO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 9469fe9c3044b5044daac4e60a36aaad893a3acbf440841ed82e437f5c46aa82 |
| DOC035-P0024-C001 | FPLIDAE | IGUROE | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 36608ef0db774a544419725e958b92f47ad7e9e0f126cb848240baea2cb0376a |
| DOC035-P0024-C002 | FPLD | GRO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | c00aaab34fa17f418c16197e0c9e61969fdb032e2661b76848bfd037e6274760 |
| DOC035-P0025-C001 | FPLDAO | PGURO | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 66cf6e6432c5c74caaeab88c342dc95b75bf8cd5fc489cbf2fc9fc8bb4ec0caf |
| DOC035-P0026-C001 | FPLD | GRO | - | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | e825d5a93d4e84c90b907e72f9a003e4a47458b499061f3387f4851a5042a975 |
| DOC035-P0027-C001 | FD | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 08f88b6d94710a0b46d5d9c2f4e8ea33f61c050dbd05cff0e65e07c4b77719c4 |
| DOC035-P0028-C001 | FPLIDA | PIGRO | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | cda426e18d0ec090794aecf1a8fe11f97d93234d53c08259e31e87febe3b2f39 |
| DOC035-P0029-C001 | FPLIDAOE | IGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5f92409a386df5af102f203b4afe2abbdddcdc0feec9d7b0a060c94b332899a3 |
| DOC035-P0029-C002 | FPLDA | GUROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 892075985e03aad1d69daccbdd1ed469e706dc4e08cf542e05beeda71a68c476 |
| DOC035-P0030-C001 | FPLIDA | IGUOE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 65c45ec8d81f4c3420e4bb41b78524062eaf9373823951acf03672e72cb34c7d |
| DOC035-P0030-C002 | FPLID | IGRO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | e35f95daece0fbbcc25f651f1778c7c01ed8c1e5e0283c8e76ac36d9bf4aeffd |
| DOC035-P0031-C001 | FPLIDO | IGURO | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 91a8b26645ed1d4ddb814805aced4063b96dfce5622075e4c5bb3f24c25c641f |
| DOC035-P0032-C001 | FPLIDAOE | AIGROE | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 60442621145383ca8be3d890a0e6f5d0073057410b1ea20e658178f0275ab9d5 |
| DOC035-P0032-C002 | FLIDA | GRO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 7cb477d4ce1c22dfbad89db6af6439b65aa05209d94aee8bbb10fc7b768897f0 |
| DOC035-P0033-C001 | FLIDAOE | IGROE | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 2a022d1dfd0ea90de7facdb17a469d60ba4e94ec61f5987249413b8a2b22b456 |
| DOC035-P0033-C002 | FLO | UR | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | c38cadadc49b8d821f6d74e0399e41153fcd344d0e58e640742efb9f9ffbc848 |
| DOC035-P0034-C001 | FPLIDAOE | IGUROE | XMC | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 28b4db028a459137ace48e032b66c0fe6929e974f06f5f107dd99c00bbb07b2a |
| DOC035-P0035-C001 | PLAO | GURO | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5076b6b641752dd91a96aee8789e2e86f4f1f0eb0930c01701f3c587bdbc9cad |
| DOC035-P0035-C002 | FPLO | URO | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | d2ec502e7d00504467ffca5792080e30630ae07f3809861d405d7211f31429d6 |
| DOC035-P0036-C001 | PLIDAOE | GUROE | XCG | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | NO | NO | 69808df57df1147fe822fc9bfcfd337344ff94bf466d95f97300a1f4bbe34f0f |
| DOC035-P0036-C002 | FPLDAE | GUROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 0eed245e5fcf2eb00af2cb446d62d3ab99f40644757478815b0cb582ea796ab6 |
| DOC035-P0037-C001 | FPLDOE | UROE | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5c592292bfc4a45e1d3a11e44e6edd9c7001e8377d35968feb425f539ff9d9e7 |
| DOC035-P0038-C001 | FPLIDAOE | AIGUROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | a23209de1f2a3128c08e0f669caa1b5257afa09c926cfee3d6ad069109650222 |
| DOC035-P0039-C001 | FPLIAO | APIGUROE | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | b439d92c24e6ba473b01fdce207700dc4f0c0882f205299a8922d3598faa1c02 |
| DOC035-P0040-C001 | FPLIDAO | IGUROE | XC | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | fa24a795ab3d5f085112abe65fc3522df5ecb3c53e334b394855f8f05e671049 |
| DOC035-P0040-C002 | FLDAO | GUROE | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 78375b2de59dd46e5b28481e6ef97cf1209f0c2f57328860e4f01346d90c11fe |
| DOC035-P0041-C001 | FPLIDAOE | AIGROE | MCG | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | f53f8772493a217cbba20e8912748e23c07caa8f81d88428e725351c88c14df9 |
| DOC035-P0042-C001 | FPLIDOE | IGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | cee97863164da6dbbd6356c8f38e51e8b00d502a2ddaa1e25b14e5e4c8a9f34a |
| DOC035-P0042-C002 | FPLIDO | IURO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 3bd8fbd7ac114be36c46cd666b8bfdad6c8ca2ce458c306a30169bb454e6df09 |
| DOC035-P0043-C001 | FLIDAOE | IGROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 9b3d6c6dc7b7ee5ff3166aa15f7654aa0b47d8a02fe1803aadf286acaaee9096 |
| DOC035-P0043-C002 | FLIDAO | IRO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | ed2acd5b0524896c2875fe313da23d724452c2975331d68d24a08500f13e3c23 |
| DOC035-P0044-C001 | FPLIDAOE | AIGUROE | MG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 3cbd68a89fbcfaf837dc058bdf3375a2e868b6c2c611190be07cf4caaac4d746 |
| DOC035-P0045-C001 | FPLIDOE | PIGROE | CG | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 98fef9fd6049b093809c07b433331f2d00c7da8a8336a25f64c605955839fe70 |
| DOC035-P0046-C001 | FPLIDAO | IGUROE | CG | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | NO | NO | f4dc99ea0dcf9ce0028081964e296d0844d34b7f5d8938b7d54ce3ef38db5dcf |
| DOC035-P0047-C001 | FPLIAO | IROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | fcf19dcfeb61f02dfaa8bdfaa70728dc2fc8ba8ac1a3bda789ae12b1cc1ef646 |
| DOC035-P0048-C001 | FPLDO | URO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 61d6dabdd1e1a21ebf0a564f2fa4f9220e7fb5b0eaf1ab950892a58618f86920 |
| DOC035-P0049-C001 | FLDAO | AUROE | C | DESCRIPTOR / D | IRRELEVANT / X | NO | NO | e6afb4aa27a1250fb09d9248dc57f7a15fb3840d960692cfaa42b092bef15123 |
| DOC035-P0050-C001 | FPLIDO | PGURO | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 41b9236d8b5b98b07ba6c69dbf9f1069322b400d480fca31337be0c563e735ca |
| DOC035-P0051-C001 | FPLIDAOE | AIUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 2731651ce432109f9c1f5d99775af823597fb5c6d9b3d9b008bcedd41628229a |
| DOC035-P0052-C001 | FLDO | RO | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 83b3fc8c838ae518f7eb7f3b692b08c10794dc8db1d7fc6a143a15a115c03e22 |
| DOC035-P0053-C001 | FDA | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 5563fe3f74101616b070a181444e3a58d7b57c17d9917ba94113f288da9f7c4e |
| DOC035-P0054-C001 | FLIDAOE | PIGUROE | MG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 851be069dc87f5363d073cfe046cdef3b5219b84b34a5d0c1b2f936fa8f60098 |
| DOC035-P0055-C001 | FPLIDAOE | IGROE | M | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 510464661c8e7bfc01f632a383a8735cbf23c4ed5e9dae1b0c41c764293aceb4 |
| DOC035-P0055-C002 | FPLA | GRO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | b2d78ec26a960c07d3286db16fcba9c62d808628a9b292fe17822237e832f69f |
| DOC035-P0056-C001 | FPLIDAO | IGUROE | MG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 6f18f20b3dea88203402a1269800a42f9e849f5e4debe158bbafff4064a00825 |
| DOC035-P0056-C002 | FLIDAO | IUROE | MG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 7df94127345560edaeba7a2bfe614d52d7e4798ed4d004042db5c50c54cc415d |
| DOC035-P0057-C001 | FPLIDAOE | IGROE | MG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | a8ff51598eca163258d1a9cd92d1419c7817124f0642ac5eff59bd40ba108386 |
| DOC035-P0057-C002 | FLIDAOE | IROE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | d59a480f37fde2fac5f5dda03fd0d920402f51162ba3403904cc7a58ee3b4934 |
| DOC035-P0058-C001 | FLIDAO | IRO | XMG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 750abda618dc9f3f37215eca6fb5457ec6b858c9b7ce4909ed0fd4d4dbbfb33f |
| DOC035-P0059-C001 | LIAOE | PIGROE | XG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 0b090022ef72529bdf52f92863509a43903305138df552c337a8f8725bb2e1ad |
| DOC035-P0059-C002 | FLAO | PROE | G | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | b21491c67db71fca6a6ff78da0b3d67aee7a5aab8b75c6b2e80ce0871e0b63fc |
| DOC035-P0060-C001 | PLIDAO | PIGRO | G | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 2af6b5dd9581a1d122117c0f32d53b88eca5151dca4021653af1947d2aa5e1bf |
| DOC035-P0060-C002 | FLDAO | RO | G | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 4afd6bb8697f84765101ff8dfaaa6ef04c53a4114891ca090abb0d07ce6289ee |
| DOC035-P0061-C001 | FPLDAOE | PGROE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | debd4404471c4d5875a85b1c358703e73d034671a7ae06f28457a743ac8eff95 |
| DOC035-P0062-C001 | FLIDAOE | IGROE | G | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 9b33e9d8e4bc831013669989dfb702d4591acd1b026923dcce8be69a94ff392f |
| DOC035-P0062-C002 | FLDAO | RO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 1d1627f2d461ea97cc5ec427739e052735473d1077c804224bb5ae37fcdfa04f |
| DOC035-P0063-C001 | LDAOE | ROE | XCG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | eebbc959747a139afa1cb18823767a815931590b4532075bcbfe6741091353be |
| DOC035-P0063-C002 | FLDAO | GRO | C | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | f2550ba39152f7a9b252ca5da2febfa652f4e727dc7eee7f39d1ae21cf192134 |
| DOC035-P0064-C001 | FLDAOE | OE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | b96cddfaa5400ade3a8fb6f4242a4d4e795aa2b0d03eed51b1af2579f6893d3e |
| DOC035-P0064-C002 | FLDAE | ROE | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | ff2db957d2fea0f938f54d2aa86ac6fdebdf72a10279bd3d475d7fd159af51a5 |
| DOC035-P0065-C001 | FLIDAOE | AIGUROE | XM | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 6f000d0178dff6bd1c9ff878be646fb6c174224ec6ee4f1b93992ffe3760bc92 |
| DOC035-P0065-C002 | FLIDA | IRO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 9b8b825dd84286f167c6f5bed08573b579166142020dd884391c28fdae847013 |
| DOC035-P0066-C001 | FPLIDAO | IGUROE | XM | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 6c73587cdc4f74011bc4e8f4217874b641c3291421ae441db13364f9b55bf84d |
| DOC035-P0066-C002 | FIDAO | IURO | XC | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | d7258b4acf84492757fd596bbd08e55f7929c1d507f48c4e25bee53001359a3e |
| DOC035-P0067-C001 | FLIDAO | IGROE | XC | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 6d35451351da1e4bee8050042e3b96e6c65a079ded525daa12adefecc1535a5c |
| DOC035-P0067-C002 | FLIDA | IRO | - | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 8ab70f5b78c5901830d3c847178c9ec4ea3e53ae8f70f383b92cc983cb99aaa3 |
| DOC035-P0068-C001 | FLIDAOE | AIUROE | X | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | aaa14a4e8e3ebc513c7fa21619e36d0727c5802b14720481ed46518fb1690a52 |
| DOC035-P0069-C001 | LIDAO | IOE | XC | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 8b440741b8a347d6cd5b12809da893073a775bd0bb261cf23e570d9729760cc9 |
| DOC035-P0069-C002 | FPLA | ROE | M | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 4cfba066fa48a30b983ae91157b9764e8c4aacc5b3d926d38d684b4aaf93cb55 |
| DOC035-P0070-C001 | FPLIDAOE | AIROE | XG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | 97eb4c46d0463972af5732e636d550b8b80690139c77ab6703998ff2a915bf7b |
| DOC035-P0070-C002 | FLIDAOE | AIGROE | XG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | e3e88b1f86a520ccb73dbc66a5f2aa85564311a3ee86cc80ae53ac7416a6bb03 |
| DOC035-P0071-C001 | FLIDAO | IGROE | MCG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | d08f0530e450e75655498349041b448c02122b3d010037a0567ff3fe6afbe683 |
| DOC035-P0072-C001 | FPLIDAOE | AIGROE | XCG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | c1fd8fa182dc36581b3937394098c670ceb279897e39e8cba62b8a99d661d56e |
| DOC035-P0073-C001 | FPLIDAO | IGUROE | G | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | eaaa36dc8fd0c4f0f160b893a5ec9230be16fcfd016aa2d5eae56f92c9bea956 |
| DOC035-P0074-C001 | FPLIDAOE | AIUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6868d3d509594598e89837644d9ff508612019f28c2ea2eaa5e25d479c1dd554 |
| DOC035-P0075-C001 | FPLIDAOE | AIGUROE | MCG | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | e2f9fc0ed2c0b3e682ee4ce88b60882c4285d1cd6a97f10efa3c55663f28a7bf |
| DOC035-P0076-C001 | FPLIDAOE | IGROE | M | ASSESSMENT_GUIDANCE / A | IRRELEVANT / X | NO | NO | c53694ca6c5f26369ccc0bdf2b4a6fe47ab82152648a986ec21eb5ad5a6a146d |
| DOC035-P0077-C001 | FLI | IGR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b2c51c68b10bb0312c19f4a207b379e1d4539bbe9eddac07d3eb83e1a6c8ccac |
| DOC035-P0078-C001 | FPLIDOE | PIGROE | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | fc7383f1e60df2ad4dc31c5b3b7709a05c1f842d653070541f3e92613232d79c |
| DOC035-P0078-C002 | FLID | IGR | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 0506a96442e2d49df5338e3d41eece3667d2fc0ca2dcf9c8a85e46e7104b6efb |
| DOC035-P0079-C001 | FPLIDAOE | AIGROE | XC | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 0ca22c2b0cd36e2bfd451085c3adf438739371819d8dc7c49245329ca60ac681 |
| DOC035-P0080-C001 | FLIDAE | PIGUROE | XMG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 93801bfa8f266bf27421a14c17d62e42f08ac669c394b27f38c779844a8701f6 |
| DOC035-P0080-C002 | FLD | GUR | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 496e3b3fcb2fd15275bd825ac5850a51382e0860bf0818d2609d80c660a72409 |
| DOC035-P0081-C001 | FPLIDE | IGRE | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 89f97c46d1c9b23129fdca85503a463d6426f3a60151e4c873708d434499a08d |
| DOC035-P0081-C002 | FLID | IGR | X | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 94714cd332c41f8fc3bc06ba8318a038216643b94a997af7dc431addd7d4ee5c |
| DOC035-P0082-C001 | FPLIDE | PIGURE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 85355c087fa50a40ed706a7adeab48b6ec4dbb388f9c3aba304846b6d3106871 |
| DOC035-P0083-C001 | FPLIDAOE | IGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | d3695519ea6470b6c0faea2fa5aa15a8908d3584528050f600fa8b53a1c9787d |
| DOC035-P0084-C001 | FLIDAE | IGRE | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 23e4c75b5c65f7003b6cdfc8aa5687f048f4719ad147ee644dda0245646a89c9 |
| DOC035-P0084-C002 | FLIDE | IGRE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 1acec4696fa31f4c0a3cda51ed0c48b7b8f93ad224073eebb08005840cd7835a |
| DOC035-P0085-C001 | FPLIDOE | IGUROE | XG | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | 5944933cc50b3a11781f7c116a551fb0f19ebb807466890a300a2cbcb20a4202 |
| DOC035-P0085-C002 | FLIE | IGRE | XG | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | 6ea0a01e18c7325925c6e579796074e9790ff9372ce7914a513909f7f80cc7c9 |
| DOC035-P0086-C001 | LIOE | IGUROE | XC | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | bab391b3dff75e115747ecccdce93b575c8852d754537efd6da6746d746b4c7a |
| DOC035-P0086-C002 | FLIDO | IGRO | - | OTHER_NEAR_MISS / B | IRRELEVANT / X | NO | NO | 9a630f784f94898a884721294b87b5282dc775fcfa77a09f2eb1f9af35bc663d |
| DOC035-P0087-C001 | FPLIDE | PIGUROE | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 48d0940f1ac2872659cbdad7a90b7af85cf11bf18d9bca8841617b62c65a42b4 |
| DOC035-P0088-C001 | FPLDAOE | PGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 8beb9fc083fd1f1891e939e7ccd153bba1eb3640633f38fb4c582d7709c2f46b |
| DOC035-P0089-C001 | FPLIDAOE | PIGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 4fc14946b36ea3a92b66ed2053b218b91ac844ca750eb3916f958baceeaa00bb |
| DOC035-P0090-C001 | FPLDA | GR | - | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | da425ed4dd2416915b51c9672cf9b4570f93d610d285b4bd4a6f2e6249e29f6d |
| DOC035-P0091-C001 | FLI | IGRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0e466da6c2e1564c8cf827de324ab03a1e677ae8e21e2706a2d12782e9c21cfc |
| DOC035-P0092-C001 | FPLIDOE | APIGUROE | XG | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 8cc1bd92b41eebff9dbbd56be6b9dda7e615e5ee3975362229b9e5cec90dcf5a |
| DOC035-P0092-C002 | FPLD | PGUR | G | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | bbced89796b537127095abd62f176b1a292b765eb145abf24c4acb494684ad67 |
| DOC035-P0093-C001 | FPLIDO | PIGURO | XCG | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 588e9ff68985836feb85f692c090ff3604b3d47c544b71df1b77a1dc1e48f97d |
| DOC035-P0094-C001 | FPLIDAOE | IGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 3ab36622612378b57351f68b8bfa3bb9c59070e62be7963bdea56738555462ed |
| DOC035-P0094-C002 | FPLIDE | IGROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 7ee98d0d6ac9ab932b155e3d70b318913dbc8e7d9a96c4d3fcdefad7769ad85b |
| DOC035-P0095-C001 | FPLIDAOE | APGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | e4328f14c4cae7f2ecfa33bfb076a9c33fa7d624a8ea8f8fe1df2fab012fe8e5 |
| DOC035-P0096-C001 | FPLIDOE | APIGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 9d94ac3f3540c9e6cb09545b1e8af0125c8aa3c49c99c924e7b063068b3005a7 |
| DOC035-P0097-C001 | FPLID | PGURO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 69ec535c511aa0723bda80a6279a7bc9c4d8fdb96d60d4c546c8c91f1ffb6edf |
| DOC035-P0098-C001 | FPLIDO | PIGRO | XMCG | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | 6c74acada77ce8e3314c311e87d64e50470da95f95eb1c52cf0c81c021a73801 |
| DOC035-P0099-C001 | FPLIDAO | IGURO | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | fcae74903bd025f60d3bf12870d0f569b4328f1cc68f5762b1b2ef23485eec1b |
| DOC035-P0100-C001 | FPLIDAOE | AIGROE | XC | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 067fdc7c3451150b3b343dd9ffed4cf5fbc84a75410873d0a5bfbd950d8e454f |
| DOC035-P0101-C001 | FPLIDOE | PIGROE | G | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | f8e14dc2e0452023f80eedcb5b45475e261f01c9762f599c7efc6eecf48aa786 |
| DOC035-P0102-C001 | FPLIDAOE | PIGUROE | G | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 58e6bfc680eb8b70363f5a4bc83f1d969ea7d287043f939145f4b8c46e85e86e |
| DOC035-P0103-C001 | FI | IR | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 23c3689caf1409031c51665ea4f4d499e9600ce1a0fd8b17d539ed2507056fa9 |
| DOC035-P0104-C001 | FPLDO | PGRO | CG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 77c9b41dfa06065b2ff1d1b60d4c35fde13bf966bcbb13d26b285ef832d98994 |
| DOC035-P0105-C001 | FPIDAOE | UROE | XMC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | d120094cdc3f59dde6abf3020daa46ad473fb4fa84bbfd102315f2cde5c13dee |
| DOC035-P0106-C001 | IOE | UROE | XMCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | e01c554b7e7059f35c6ad87f7f1b2e925a9d0e4cb9f88d564576cfabb86f2ca6 |
| DOC035-P0106-C002 | FDO | RO | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | c3014490e09f142df38676cf017ce6534388387599cc3f5210fb4b05a82a42bb |
| DOC035-P0107-C001 | PIE | IURE | X | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0ca3d685d6e9a10ceac171be1fbf9e0a6e38bd8f5e7f0e8d19bdaf7ba8410f10 |
| DOC035-P0107-C002 | FE | RE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9da82fbc0c74979fb82b0377bba4465a80569a2b311b4455335d89cdb402aed0 |
| DOC035-P0108-C001 | PLIDE | AIGRE | MG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 0597ef3a03c163e061cea97422f834889b058b4b735f46468cea4c6c15f791a9 |
| DOC035-P0108-C002 | FID | IGR | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 731bad6113b24755f27fe9cbba83528cfb57ec8874a060c535c9257321681bf9 |
| DOC035-P0109-C001 | LIOE | GURE | XMC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | a88a268f45c852364c5c41ad88ede015b59dbfabbb2468ffb79195c90726f0de |
| DOC035-P0109-C002 | FO | R | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | e74a071a60419d8eddd86cead1fb5437147cccc42df2dc4ca0f15f2a18ce29c6 |
| DOC035-P0110-C001 | PAO | PGURO | CG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | ee794aea27377985eed3a96da55a6cabf12f9b272134ddb4cab10a0850eb0e3a |
| DOC035-P0110-C002 | FPDAO | PUR | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1f40a7f8b1e1b98bddae7d97bba6f0875341a8e88090537bcc2fa828ab095e18 |
| DOC035-P0111-C001 | O | URO | M | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 885b1935bde46990fab4be339ecf77b227984a9b5e2cfb489b239e1acf1db794 |
| DOC035-P0111-C002 | FO | URO | MC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | dbfc43b8d6abd21dd23ef1f5c019452c54244a28bf5e050e61b36c81e3a8a37c |
| DOC035-P0112-C001 | IAOE | UE | XC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 546ce9de7806f35a8bba831d8ac151209c7d74d6e8b6943198d65ce2cc7ac4c1 |
| DOC035-P0112-C002 | FPDE | RE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 000da8b6e04401c2d9ba4bfbb9352cde548c168ac081359c81d7b315e8b37a0f |
| DOC035-P0113-C001 | LIOE | IGROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | ecc59d6957c637891fe2fa09ef69de438e169664f295f135bc0a339ce0b0014e |
| DOC035-P0113-C002 | FOE | GROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 8bc3afb413507d76d0c7d9b25b89e738c1f8bf892672ff62df26ddf893ef5ce8 |
| DOC035-P0114-C001 | OE | GROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | f774b3acec71061bf7848684c04cb920899145bd2867177c242dc6a05fc5c565 |
| DOC035-P0114-C002 | FDO | RO | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 7a8630d6d7576f4cbb06ba96f5e5f69f2bff46ebec2bf345993710dedd615571 |
| DOC035-P0115-C001 | PLDAOE | GROE | CG | EMPIRICAL_REALIZED_OUTCOME / C | IRRELEVANT / X | NO | NO | c742ac93884fd9f40cd0e4d59dc263454fc1d0782a7e27fb4d948e5100172b5b |
| DOC035-P0115-C002 | FP | GR | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5ac7864f65c8b57fedab0edd9335c36aa5ce03ba36dc7a7af66a03a5f4744bf3 |
| DOC035-P0116-C001 | PLDOE | PGUROE | CG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | dfbe77ecc218aaeea294ed6ae4a25f3dbadc05fa3d279d99aaaecfd6ca336d50 |
| DOC035-P0116-C002 | FPDOE | ROE | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | e90ec7878b5cb8146e1cc72572c882955981014bdc9784004dd3a3331e4f70a5 |
| DOC035-P0117-C001 | PLIDAO | IGROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | ae0c2ea875b40fee0a133433577965a843927c14b2f64bca653c5f2cb6c896d9 |
| DOC035-P0117-C002 | FPL | GR | - | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | bc9af4315978829027127b6d26cf6523871b87b57293d4f27786cd7d55d2f999 |
| DOC035-P0118-C001 | FPLIDOE | AIGROE | M | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 230e6929889bcd1094ef7989d409dc6ad5d94155a6d66fc344c0343fd85c35c4 |
| DOC035-P0119-C001 | PLIDAOE | APIGUROE | XG | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 8c997d33f86d21ea3e1305e8f89ef65846f4a19a7af4311711eccd2a2f42259b |
| DOC035-P0119-C002 | FPLIE | AGUROE | - | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | efd4089998cf6f29cd2ee74bf4b833ef45952963c8b4f5a359c25ee4b965eeaa |
| DOC035-P0120-C001 | FPLIDAE | AIGROE | XG | OTHER_NEAR_MISS / S | IRRELEVANT / X | NO | NO | 4d724ab214e26ae011308629e6f894c6ecae9a6454e9ed775bd064e9c8f92947 |
| DOC035-P0121-C001 | FLIDAO | PIGRO | XG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 05d8411d8243554475175c940fa98d15964a7be9b671e9c3948c609dde760dce |
| DOC035-P0122-C001 | FPLIDA | PIGRO | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | cbd996335379b0e8cff5b7a099d0c79fbffa36a54bcfa69c698dcde6862077ec |
| DOC035-P0123-C001 | FLIAOE | AIGRE | G | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 4dbaa46412f937cb097d549dc16ca19a8b796bab3dedbc5ae3dd788f70e7ea7b |
| DOC035-P0124-C001 | FPLDAOE | PGUROE | G | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | 7c90c2d1ff29fe8fbfaf9db2f1b17fd932c610f4b6c966212edbcf7bb5357f80 |
| DOC035-P0125-C001 | FPLE | AGRE | - | OTHER_NEAR_MISS / Q | IRRELEVANT / X | NO | NO | f8abddbe9b9c13d41396e7962bc4f1aed9bf340c55123e9c31211fc7cad14cf3 |
| DOC035-P0126-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1c5051fb7475ad7586988fb54a5eb9bb60c5fc569d019e687dfbe048c125e6b4 |
| DOC035-P0126-C002 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9160105a55094afbc1b385803b4ba9abd067f6311a7a982deb9929df25f4b7fe |
| DOC035-P0127-C001 | FPLIDAE | AIROE | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 7a4887bb61585aaf5bf9e931d3f28459de0d8c7d0418bc2f02f9832d993c51b0 |
| DOC035-P0129-C001 | FPLIDA | PIGUROE | XG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1dfa30f7e3949cbd4e3f44c32c5a04e6da11cad8c398f8a257b48e38d98686f0 |
| DOC036-P0001-C001 | PLIDOE | GUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | aacc3d84a262aaac0a48d9090f4d5a5816dd588978d163c5e850bc8da0a7f8c0 |
| DOC036-P0002-C001 | LIDAOE | IGUROE | XCG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | feafcf3b00e9e4e47821d7a48c38a7e4ee161c02cac9579af9a0ab998df0c8db |
| DOC036-P0002-C002 | LIDAOE | IGROE | XCG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | b72bf98897cfde02fe02bf96b6b454c1e96bd3022df6b0e5dd0ed93b2340a7e7 |
| DOC036-P0003-C001 | FPLDOE | GUROE | MC | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 760bd10f6d4134024041da4ee801d70140261b692b86795fe8b30d2e7a2bec5d |
| DOC036-P0003-C002 | PLIDOE | APGUROE | XMCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1c65f832dff5bc3996ad2c6b75e8475bdda5836a3384fe583373fc77e28daf5f |
| DOC036-P0004-C001 | PLIDOE | IGUROE | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | c9fce98023ca9cbf392b0f7bb63a89195eee4abeb2a71d5de6a10c1ca4ebd6e2 |
| DOC036-P0004-C002 | PLIDO | IGRO | C | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 5bd9218100e7a4228ca798d7fa699b28ae32894b1e2d812e5bd1d4187a3f296e |
| DOC036-P0005-C001 | LIDAOE | AIGROE | XCG | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 387f62add60c75e919a52e6947709a6e533aeff9a5cfe6e4b4412ff2864642fc |
| DOC036-P0005-C002 | LIDAE | PIGROE | G | IMPLEMENTATION_GUIDANCE / I | IRRELEVANT / X | NO | NO | 18fe4854cc056b22de595d424373a23ea7c0dcdf7f7d27fe8ea3282bbb19e989 |
| DOC036-P0006-C001 | LD | RO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 143d33539a044d7ae3644c6795d8be389899cc0186826610e8623b6c566bc9ba |
| DOC036-P0007-C001 | PLIDOE | APIGUROE | MCG | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 3fc24dabd8d1dbfee40e4fbe14f8878a77ea79e252f650ee23439b2bd2dc2a04 |
| DOC036-P0007-C002 | LID | AIG | - | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 1c3f4c31acec5941f8faeb277cf8697f7f4f221185d7ee4aab170f215975e5a8 |
| DOC036-P0008-C001 | PLDAOE | GROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ca341e41056da1d1a0811a91badf5ee0c729b373a694ab8350e388a25bb945f8 |
| DOC036-P0008-C002 | LD | RO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a1fda2c258141109d8e81254c1913c321079c6ddd156e280c289ce13535b59e3 |
| DOC036-P0009-C001 | PIDAOE | AIUROE | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9770d3ce44f4e03a8d22a2a0da17740e93b004c8964c0744a5ec58da4fbf14b8 |
| DOC036-P0009-C002 | PLDAOE | AUROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | eb4ad2e79baeed0bcd828c9a184784bc66d57ffffb25eb1300b8f4924493aa2c |
| DOC036-P0010-C001 | PLDAOE | AGUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1cfc15345d4d93ed683d2813712c29aa6fe419a87bc423ffe9f0cdf12ebfa590 |
| DOC036-P0010-C002 | PLIDO | PIGURO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9dc4fa727fd29147153d79bf64ce54342c9139ba2483e58fa826792b4142d5e2 |
| DOC036-P0011-C001 | PDOE | PGUROE | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | 9724b0737170dbdd32ab7436ce09e1aa62178f4564502f699b51cfd2cdcc4e00 |
| DOC036-P0011-C002 | PDO | RO | G | FRAMEWORK_DEFINITION / F | IRRELEVANT / X | NO | NO | b316f364da4e22e3dbefaef564bbd7e375e5ec66a56ff44191fef1dc3a43bf69 |
| DOC036-P0012-C001 | PLIDAOE | IGUROE | C | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | NO | NO | b6bcfb4788f18a2eac590d9dcf8b4ce1ad787297aebb93b71139d5b186c35e76 |
| DOC036-P0012-C002 | PLIDAO | IGURO | C | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | NO | NO | 81893aee468618761ac652545e9796cc02fb1ae61cdd84339378afd67d8d6915 |
| DOC036-P0013-C001 | LIDAOE | IGROE | XCG | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | NO | NO | 5a6c0cbd5413704290bca35bda686e37d53e580cfae5872b48b291141538423b |
| DOC036-P0013-C002 | LDA | RO | G | IMPLEMENTATION_GUIDANCE / I | OTHER_NEAR_MISS / W | NO | NO | 4b1d0a6407c03eef5d6cbd0a79311fefd1357a0f5c8c071332b430186f673808 |
| DOC037-P0001-C001 | LD | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 01cabe42ae196a60ef1ebc368489c4e3ffaf666cf5128048187b839ba15551d4 |
| DOC037-P0002-C001 | LIDA | PIGRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6f62dc0d4fbdb1c318736a4431f384185f2924edc74878489284e22224535b20 |
| DOC037-P0003-C001 | L | GUR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e66bb9aa360500c722bf9eb23ea8322604e2b2682d783aab165cacc0e453f56e |
| DOC037-P0004-C001 | LE | APGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a34b3810c61b2ceb1964dae30dda3c962a81b1737a4c10eca217f62fd1eb0d5f |
| DOC037-P0005-C001 | LIDA | PIGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c5e9d049d3e2b699a5b03b94bdb500ed02242bb9a8988c2eda739bc06ea19c50 |
| DOC037-P0006-C001 | PLIDOE | PIGUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b12bc00a66903ec9dd9651c0aaee1a0640aaee8db244e454e48479aed22f8dc0 |
| DOC037-P0006-C002 | LDOE | PGUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8b130cefe67208d02d0416965aca4a6822f8bb757a27cebbe5cf5cbe0c20b61b |
| DOC037-P0007-C001 | LIDE | IGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a82dd3dc16b90c28a4a88b00cef5e7cd15fea14e5227317b36a5f031d6ac256a |
| DOC037-P0008-C001 | LD | GR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 86fe0943db861419d204563fd3c4d6ac3eb8ba11c539739f8eb051d953db0db7 |
| DOC037-P0009-C001 | PLIDOE | PGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fd85fac8245586f76f220a53af016eadb53406b6d1842d5af59f524a32b85df1 |
| DOC037-P0009-C002 | PLD | PGRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7dea02032d6047927e5ecafab57a30163442af8f3b40c1bc2963448ec732a9f4 |
| DOC037-P0010-C001 | LIDAOE | PIGUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8e1ab0150f4a6f363528d7b38c8bb5e19b3c11f8a1aaec9af0fa5727f503d255 |
| DOC037-P0011-C001 | LIDAOE | PIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8e3fe9b985457b4f7e67dd1d04e31b8f65985f708a76ce2df5dac85874ca5b32 |
| DOC037-P0011-C002 | LID | IGRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b3915d26f6637d1a5f2d394448b298a7625ce9cfd5f7522b080723fd9e337966 |
| DOC037-P0012-C001 | LIDAOE | APIGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 67ab650e740b6e99fd8688ce13b4c752aded0fdda5e6a6aa10a07aab80e80b42 |
| DOC037-P0013-C001 | LIDOE | APIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 711597068d072a2a1f05758119dfca48b9567cb8db0a0247612326f7cbe6f6d9 |
| DOC037-P0014-C001 | LDAOE | GRE | XG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | bd2cdaf3362ad2f48e21282c7d7b7d755e70e51833cba01a02134f912dcc9c3d |
| DOC037-P0015-C001 | LIDOE | IGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c187ef789e916010e9db41a5f0bf64c7f9522e69c313b2a0798b7ed4991e32ad |
| DOC037-P0016-C001 | PLIDAOE | PIGUROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 47d36c64b9976c9e8b63fa2370d597816fc303d22ff6561b6661e8dddca6d542 |
| DOC037-P0017-C001 | PLIDOE | IGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 568025c1f2b8531141654994ae17dadf3cbea2bab4f17b9ad95129bf16cfaee7 |
| DOC037-P0017-C002 | LIOE | IGROE | X | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 5d3c283643be9b160c7152ff52ffce2f56e814c7869eb3a15c1ec716b9f03846 |
| DOC037-P0018-C001 | PLIDO | IGRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | edae7e769e26e28b1f394ce7aefc7ae77930431b926e85c9ec14a5e0d7cffb3f |
| DOC037-P0018-C002 | LO | GRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 13da69dd9e763a951d8ff483557475d08dce3479b2c1dbe9e6c17eb3037f8bc7 |
| DOC037-P0019-C001 | PLIDAOE | AIGURO | MCG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 51aaf17391d1bf72717f822e1587cfa29a9f6cb5031a93909c7c5f7612e98d6d |
| DOC037-P0019-C002 | PLIOE | AIGUROE | CG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | d4920930031d31d8103ba3f43a3d08f20501d93dd97552164e826b042c08c3a4 |
| DOC037-P0020-C001 | LIDOE | APIGROE | G | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 47fe468bd200226cbba7b95a4aa25589ba7ca9c0ae7e50825b6de0704e794c9f |
| DOC037-P0020-C002 | LIDOE | APIGURO | XG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | f4eafffe9aad7f5e02703abeac2141deb4472543ac7d694a34f28f56871134d7 |
| DOC037-P0021-C001 | LIDA | IGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 77ac41dcbae1ac0bb158eefbeea76368a4fb81fdde28f641a2453fddb57f0e33 |
| DOC037-P0022-C001 | LIDAOE | PIGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 92ac019c1aae7980bb1f412c895c49133790a1d6711b44e79978c4741b436881 |
| DOC037-P0022-C002 | LDAOE | E | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1174078de012d729bc07ba2dccb570ee021f56917a615a2b88449b3112b2d7c6 |
| DOC037-P0023-C001 | PLIDAOE | APIGURO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7041923d3302847d7c0c1dce2faa844127be5c3a4d1b21fdec2899858b1622f1 |
| DOC037-P0023-C002 | LIDO | IGURO | XC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 52d048d624e499807fd29ea411c6c9f7ee4401c33a7931097b6e4df61ed71d5b |
| DOC037-P0024-C001 | PLIDAE | APIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | cb01ad2267aa4db3dfa0fc3055704645d92907fb32f2a6a56bdafdf625bc7fc0 |
| DOC037-P0024-C002 | PLDAE | GUROE | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b5ac2f4b58c1ab0c075e553297d1c84310f564ba2c86fd29452162654e17aed0 |
| DOC037-P0025-C001 | PLIDAOE | PIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7692d2b8ea1e44c1875fb9a4a50539ac58a6412f385d9f5ba118549edcf6c2d0 |
| DOC037-P0025-C002 | LIOE | PIGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 966cd703b350116898f60c2860850596b71708d7cacda68b53bbc700d31070fa |
| DOC037-P0026-C001 | PLIDAOE | PIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b57c484c9dc831fb5872b436497d24d422b5ca6200e1d52179c011efe58b3e34 |
| DOC037-P0026-C002 | PLIO | IGRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 601263948b5dcf6ec8df11579260a3d994b98d881cbe6d16f16018e2813df769 |
| DOC037-P0027-C001 | PLIDO | PIGURO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2c1139506022da403fd9b729c0932eba39202b0bd777c12d18aa5b215e12cf6c |
| DOC037-P0028-C001 | LIDA | PIGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 09627d9ed9b2326f0fa6c89a4794112967b7d1992899f993d66596bd649f36fe |
| DOC037-P0029-C001 | PLIDE | IROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3839399d8d49d5b3888ad62381c0ab2f898cc363905ae42df9464c82dc3ea3a2 |
| DOC037-P0030-C001 | LIDOE | AIGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bc853899b12b606643fbfcb362bf24e344b8ba24ebc26a9fed48b4539e57b52b |
| DOC037-P0031-C001 | LDAE | GROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b4761e01e0ee0568f02589191ec18ceb634cbc6cc7a4464a5ed38cc517e84f7a |
| DOC037-P0032-C001 | PLD | GURO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6a9a98c05bcc42a1edabf3e45f95739b79c0729fe9e3afb1208b1aea8299781a |
| DOC037-P0033-C001 | PLIDAOE | APIUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3f58fd5c25b972d3579efdba4b72441399ab59e71acfd266aa812875e41c849d |
| DOC037-P0034-C001 | LIDAOE | PIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 90bab3e8f9fd902776847d8b6a7e9fa22ffa5edab45976c4e13f7022b76eccba |
| DOC037-P0035-C001 | LIDAOE | PIGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a1469b02c698b263b999961e0219aa021d06eff204dbb23b4c1b7eac32470145 |
| DOC037-P0036-C001 | PLIDAOE | AIROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6d9208582c21c17f87f9391ff36adc7e63dfc34bad04541f8e747cd99c1fc399 |
| DOC037-P0037-C001 | PLIDAE | AIGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7efd0380ea7384571b16f326e2a5c057e147486e6f6750f815c844260871be69 |
| DOC037-P0038-C001 | LDAOE | GUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 46d226a4665e755278dcbd356b54e42d18b2fcd234645e18862903b3f81f30b4 |
| DOC037-P0039-C001 | PLDAOE | AGROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | cf45b2d0ee51d67aba7c8c503f1998c25f4630edb3b679df087d67728f8c8333 |
| DOC037-P0040-C001 | PLDA | GUROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 14d45b3ad01f2b3bf66a9a707cbd23753fee4216730aa2c168fc878dd3f234d5 |
| DOC037-P0041-C001 | LIDO | PIGRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 59f4744cbe200fc41503dc9df97722c6eff74231f9168d0e858b2b45b25c59de |
| DOC037-P0042-C001 | LIDO | PIGRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7a513434f6ef9eaca2dd0f83d8364ea754adf24fb6180e99826f8792534d8508 |
| DOC037-P0043-C001 | LDAE | GROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 74d00aa2d342998e47b8b1df170a323ee9e6f13cc0da25859c604dc5f75321af |
| DOC037-P0044-C001 | PLDE | GUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9de5f844839f781fcfba12f1f1dfae1c5de387248b935ab424c74ed9754a3777 |
| DOC037-P0045-C001 | PLIDAE | AIROE | MG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | cb8e3b943d031ca1dc002b3c68dc40bcedff61ed400dd9dc0f928cee6508c0da |
| DOC037-P0046-C001 | LIDA | IGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0a7c3a76395ed30ca2ff7bc3b1cc704030d2a0d72c37acccf04f5f3ae7365466 |
| DOC037-P0047-C001 | PLIDAOE | AIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 233caf7baceca543fd92473b7df44fcf4f348343185f13f32a58a9b51a974a22 |
| DOC037-P0048-C001 | LIDAOE | APIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 12ac32e97c4e460af1c012985010f273a5fa7902ecc4d05b0c2d4a27c5157505 |
| DOC037-P0049-C001 | LIDAOE | PIGUROE | XG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | d4870365c4bd64e06d848083198cca4471ee4f326bf32e450cc43daeadcf0ef8 |
| DOC037-P0049-C002 | LDE | GROE | - | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 1b01750c6b980cc611d3c3e54ce3dfeac0b140c01723ea6b95f9bc48cbd38c8a |
| DOC037-P0050-C001 | PLIDAOE | IGUROE | CG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 9c57a0e7ac5f7fbc4c3a2ab45b266046ac012e052cecb2073c3e153fdd7de32a |
| DOC037-P0050-C002 | LID | IGR | - | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 118f978a7e74e8cc4e94712b913faa65c1f926797b25c9da6c22676924a18197 |
| DOC037-P0051-C001 | PLIDAOE | APIGROE | XMG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 38e02bb1aa69b1b816cae715cadd41f9dd6b1b233f9843cfb81185f00584068a |
| DOC037-P0052-C001 | LIDAOE | AIGUROE | XMG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 6a2f49199b6a71643ebe444d3294b0797b193461750205b8e5162b04b9e2d0ae |
| DOC037-P0052-C002 | LDOE | AGROE | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | d8b82f729d7787a3fda6d2fbf9408c3af01d396470d4a38cd3499c50db52801f |
| DOC037-P0053-C001 | LDE | GURE | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 16c1e23d17ec9e7696d1d4dd843fe2d09bff9582596a0e75e5ca57ff938a8b79 |
| DOC037-P0054-C001 | LIDAE | IGROE | XG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 50fc00ffbc00d40c5e07cbb7a75064774ec72f1b665ba5b1b225cf0b58eed241 |
| DOC037-P0055-C001 | LDOE | AGROE | C | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 1e064942a82faaff15f4822c155e3ac4d1840b776976d7c292d9e961961c4cdb |
| DOC037-P0055-C002 | LDAE | AGUROE | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 8a62340b143cc0b90ae62255f4bced6d0f41d6ca8fc5c0a72ae4018b2565926c |
| DOC037-P0056-C001 | PLIDOE | IGUROE | C | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 9a3d3eb8a9a0b659027511b84b575733d158faf6c2be54f23c6e1150479840ce |
| DOC037-P0056-C002 | LDAE | GURE | M | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 222704146a314d0056f28b48bf808445907585ab33a5224f8c3b8e9d821d078b |
| DOC037-P0057-C001 | LIDOE | IGUROE | XCG | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | 56ccc3dab6efe7021eee846c3aa50d6aa285cf8a26124802ca6ec8a1d3d7fa36 |
| DOC037-P0058-C001 | LIDAE | PIGROE | G | OTHER_NEAR_MISS / B | OTHER_NEAR_MISS / W | NO | NO | d5934c0c6cd2be6b9ba93913e467040a9ac7dc7e651583d1b8863922a1182fb3 |
| DOC037-P0059-C001 | LDAOE | APGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7aea60cdb19a564001a70141fd985bc92cb58be351aee538e9701dd213845ba5 |
| DOC037-P0060-C001 | LIDAOE | IROE | MCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3f9a88fa32b21cad8abb9997050c46665b369d307fa2d23ef69c500f3870dd49 |
| DOC037-P0061-C001 | PLIDAOE | AIUROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8d2d00f1bc5809f887dbaca2e5ed94d98b5883f462d3123a5cf98638762be9d0 |
| DOC037-P0061-C002 | LIAE | AIROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4c42b85ee721f5fb0a91b1955224c401699ac9e0d98dbccf3f2710569a1c8d06 |
| DOC037-P0062-C001 | LDOE | AGRE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b1f8a978fd5d69953922b03cf8768f6bb16ef38e26259805c3a26ba252542996 |
| DOC037-P0062-C002 | PLIAE | AIGURO | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 25cd36b43df97a874b96a003941256c7a7331764355b3f451bfce1ffbb27e491 |
| DOC037-P0063-C001 | LDAOE | GROE | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6981ff96b69c1006344c63bef033d5423ef206c952e7f5f77081065452eeda2c |
| DOC037-P0063-C002 | PLIAOE | IUROE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4f039528ca5df967bb66463c7d0ec69b6629ac4e2fe8900140a4ef71ec093562 |
| DOC037-P0064-C001 | LIDAOE | AIGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0601f181df6e541d3a002c56e2a7a6060320016d6795de77ed2390b20d5932b6 |
| DOC037-P0064-C002 | LI | IO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3a901aa91e167a786dcee8aa6af7b47b2aba6868295f9b0acb0c3c3ec256ab81 |
| DOC037-P0065-C001 | LIDAOE | IGUROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b97c842f0822dc34bb11f4f39232168f79c9b25fd9d9a4d7932acf8fff1114fc |
| DOC037-P0065-C002 | LD | RO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | de1cd5167d57bcb86624117ca9568451b7c84e44a42022c612b90d0e010494d0 |
| DOC037-P0066-C001 | LIDE | PIGURE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2fd286b3bdedcf4e163fdb3ba92e88ab87125f3455c01c21d4eb9a9b91b00300 |
| DOC038-P0001-C001 | IOE | APIRE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 936071ba81b7bb24a735e5789628459458db848a79edaf559b4633deb2908772 |
| DOC038-P0002-C001 | PLIOE | APIGUROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4df0e80bb68c8f70d772f797fdcda4283946a50eea8d6aa894314ca85c6f579f |
| DOC038-P0002-C002 | IOE | PIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9296d6e57b16218e59b2d6ec5e1302e00b8c968f125fff4ffab0d7a147a2f001 |
| DOC038-P0003-C001 | IDAOE | PIROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 36bec81ffcd7f604ac1dce9e0d7dc52d09049162e0649524c4f0c699c99d7bee |
| DOC038-P0003-C002 | E | RE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 375489a602629e26fe291871d195fd251bb3c6320c76c61dc43710ce501d9d60 |
| DOC038-P0004-C001 | LIDAOE | APIGUROE | MC | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0c3314791a7d9ba6854620b89e60c4106c13afaec55d8926c479700e2ec1ecd1 |
| DOC038-P0004-C002 | OE | AO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4a738cded9400b2d4f0dc24a7b42b5f839c0ffbfa79ce6deae10c9b1f4abd426 |
| DOC038-P0005-C001 | PLIAOE | APIGUROE | XMC | INTENDED_OUTCOME / N | IRRELEVANT / X | NO | NO | d4452770967bd72850cd0845e2aa7e0925d8038924eff55a7cfa111695f31828 |
| DOC038-P0006-C001 | PAOE | APGUROE | MG | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | NO | NO | 108803714e9a6b6f11fa12bba5b77b167c3500369c655ae2509ff92dafd57403 |
| DOC038-P0006-C002 | AOE | APROE | M | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | NO | NO | bc1285ce6a8f251d46662879c9f958837fc8f24d0041a709c3fb21344e2a81e8 |
| DOC038-P0007-C001 | PIDOE | APIUROE | XCG | INTENDED_OUTCOME / N | OTHER_NEAR_MISS / W | NO | NO | 9f370446cd1d7cccb63f84917dca0233b867eda0d9187b16555fe2e26d366408 |
| DOC039-P0001-C001 | LDE | PGRE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 63fd3b175bd280351cb43ddb6cae2a5b1a24220fbdf7369c091d191ece97938f |
| DOC039-P0003-C001 | LDE | PGE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 05271c022e61702a85241604e372bbe06cfb18b1b3b39f03987ff10284a2738a |
| DOC039-P0004-C001 | LIDAOE | APIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bf8eed0f779cdd3ab97727c999c9bfd118b12b9fa385a6d573a79fc77e1f25da |
| DOC039-P0004-C002 | LIDO | IGO | C | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a9109ea40834535b552d9f5d811e32bd45dec395392979037364d7b36f2791ec |
| DOC039-P0005-C001 | PLDA | RO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6372c844ba40af63bc6312ef2d159ae36d6e425a1a5cbc7767bbb4525b88708a |
| DOC039-P0006-C001 | - | - | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7872078d6758f5d336983566ccb975dfa520d32ed74719844c80635d26355736 |
| DOC039-P0007-C001 | PLIDAOE | FAPIGROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 44bd4812abd2f53a5d00292a268261cfd26d588f65c62b0d0a69ee8d57aa7417 |
| DOC039-P0008-C001 | LD | GUR | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6112f34151e911472bbcc0afc165f31961eccc31b06e26b1a370628eaadf649d |
| DOC039-P0009-C001 | LIDAOE | IGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 48a369b662c11a376df224fcf08bc01e146ce535ceeaaf4e78915e0b4b7bdfa5 |
| DOC039-P0010-C001 | PLDOE | GUROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 332b89f185034b1a812a79c7faa72a4df919e919e5c75aabe83b9c9ff8be2e2a |
| DOC039-P0011-C001 | LDAE | GROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 22ee42be0a73a215741d495acb9456205f4b5d4348238c0562891e362b7c48ab |
| DOC039-P0012-C001 | PLDAOE | PGUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2f2fb128560cf716839b78be68bd72721475c26615182019bd26ef7aad0c7582 |
| DOC039-P0013-C001 | PLIDAOE | PIGURE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 48bd6b283a2ce740d3829d2542cbec826720021306158251c949fe6cc17c4e79 |
| DOC039-P0014-C001 | - | - | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 90cec7b45cc623df473f41655555786936238053d58975a9245823d92bcd532b |
| DOC039-P0015-C001 | PLDAOE | GUROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3d9319e06f470c31a3b09be84925073f47543bdd54be25c6fc7e9b8818d45fc0 |
| DOC039-P0016-C001 | PLIDA | IGRO | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 172825f8d60bbe277e24551a815723d5ea73b8dd842bc694091405f8a44b5460 |
| DOC039-P0017-C001 | PLIDO | IGURO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f6f754af725bc19a8bd0f0a0341a6596ad2e7bb417cffd80f3e9b203a4b7ef35 |
| DOC039-P0018-C001 | - | - | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 397495ce6b68d4a0f9af713e9272ed11145e8d99455d517b13ee751e2052b0d4 |
| DOC039-P0019-C001 | PLIDAO | IGRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 09e85643ceda1ced84492991ee22b0885c3ed25804d202ac9aebcfbc96d75095 |
| DOC039-P0020-C001 | LIDAOE | APIGRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c95a31d9f9b868e031d6464499ab481a2c532d3540a4b87f98d803a1097f8f7a |
| DOC039-P0020-C002 | LD | GRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0ce51073e96d25ae6255b5a413dcbb53ada95659f089d546087fc79311e13c6a |
| DOC039-P0021-C001 | LIDAOE | AIGROE | XG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 1db93292856daac8c1f5779e8b330836d50bf570cf690c4630d9f56ca940f2e5 |
| DOC039-P0022-C001 | PLDOE | GUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 47d9235ce53bcbab1878129369024af365709bea01f017133029397bca40667b |
| DOC039-P0023-C001 | PLIDAO | IGUROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | aedc4e427e6da693335a8f4c6bf7953cb613d557e9b05a0d230e6e92383dc012 |
| DOC039-P0024-C001 | PLIAOE | APIGROE | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a649f7e2274062360166e30163c0169b23e4eaa2b3f96cd403b0ae6a90744675 |
| DOC039-P0025-C001 | PLIDAOE | AIGUROE | MCG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 9e6b16c5f895d7347697b9605fa15408aeb04bdee6b2a3764e579ed69d484b82 |
| DOC039-P0026-C001 | - | - | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 796c69cf1ed070f19674b5a6dc643bdaf01b1199bea75a92083e8147848ad1e0 |
| DOC039-P0027-C001 | LIDAE | AIGURE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e987768cdd047424bd95ae5e334595dc06ffd192f63e4dab9c1874199077dbbf |
| DOC039-P0028-C001 | LIDAO | IGROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a20e786debddc67114af753e4e1d70ea53c411dc0e6777a7376537290b299aa9 |
| DOC039-P0028-C002 | LD | GRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 26ac66edaf6e072dcb5d182bfe79078a6fd146a72c7d04e30aea73bb2bd8c89b |
| DOC039-P0029-C001 | LIDAO | IGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1033a45f132a3cd2dd30285b211c260e8cb4dee96297793298c462f4c76f0f03 |
| DOC039-P0030-C001 | PLIDO | IGR | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4f760fab8b234698d6e80a126890921bebaa909f03056ae9ef0236591cd66df8 |
| DOC039-P0030-C002 | LIDO | IGR | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 768c404e150302e6ab48d3787bbf17dce5db1cf5328897b84961505105ab6480 |
| DOC039-P0031-C001 | PLIDAO | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fdd859514116796c621aaa9bb3e485f04d3bb10cd70b9c5cc473315affb9c580 |
| DOC039-P0033-C001 | P | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 7f104550c7cc3f336b39f3b8684ea894de4ac8a1c1156020a15e800f52c9adbd |
| DOC039-P0034-C001 | LDO | GRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 2e49f958cc3a3aabd056623bac0e098df2ec584a103d2a0ceaf537801a0c7dd8 |
| DOC039-P0035-C001 | LDAO | PGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 39a3a00b599e681b3c6b67400295b35cb2063d55f367bbcc0a35271bf0926207 |
| DOC039-P0036-C001 | PLIDO | IGR | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a790d08fc10116b475bb015783438865ed59bf9d2b67b634eea00e7f1198f660 |
| DOC039-P0037-C001 | LIDO | IGRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9c2438f2290a2bd2ad239b63f1ed1faf7010efd3cf43c56d380d1024539df748 |
| DOC039-P0038-C001 | LIDAO | PIGRO | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 1f07af6d3697dbb5baf34b0d8f97a0c9252d4c30ba45495546be8d84df561717 |
| DOC039-P0039-C001 | LIDAOE | PIGROE | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 38aa3fe2d99b87b45493d6f0a3bc5052f46af244ca87eb0621ded6c5798e30f7 |
| DOC039-P0040-C001 | LDO | GRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 8da4e124726a11c2f2f5c4a9c305bda7b6e11b7c3ea1687f729a0fae7a4dcf73 |
| DOC039-P0041-C001 | PLIDO | IGURO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 941906349377592b0df47ca7c2186beee62e24e577f3de2778870b74dcb5c02e |
| DOC039-P0043-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1ef5a23434e9cc1b16642854199e4efde10b2534a163715cad2e9895a741ab51 |
| DOC039-P0044-C001 | LDA | GROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 455d9de5103492c90ce95d0fd56fdde0c34a9f0fabbed451c0b98308c05b956e |
| DOC039-P0045-C001 | LDAOE | GROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4f070b07808a036fb2a689015ed22ef9e39e2c6112dbc3fa08e1c9e6ff1b3022 |
| DOC039-P0046-C001 | LD | GRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 9ade0c4ca6735a3ca53679fe6cf7cb94ba3d636f5b1eb3dd6f7118b2da0db8a9 |
| DOC039-P0047-C001 | LDA | GRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ea70953f5eadffa02f48d83b3c97ef94888084e8941902eca8655ea8b73ebd69 |
| DOC039-P0048-C001 | LIDAOE | APIGROE | M | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | b9eaed87311e734aa80e63ae1f9473ab105093ef52960e403b2e4bb483cbd9ca |
| DOC039-P0049-C001 | LIDOE | AIGROE | G | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | bd9ae9bd21a96ed95206d30e29261aa6de0f3400eea0e7edaec7ed66c3c5dcdb |
| DOC039-P0051-C001 | L | RO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 35729971f1ec7fe215293eca95d2eb0beb24d1768d0628a7504bffa39bbbf7bc |
| DOC039-P0052-C001 | LIDO | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bc1bf7c8e2b5885e80fbec11f06b71df9e3ee808b88e75e1e9620e7fcac6a99a |
| DOC039-P0053-C001 | LDAO | GROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4665856995b90dde22ac36faf2a1e65c781b75e2f7791e39441f836c5b70b862 |
| DOC039-P0054-C001 | LID | IGURO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a1da5437c4e40607e9322391b71148e0158e39bb3dd35a9b1e87cc6b2807b311 |
| DOC039-P0055-C001 | LID | IGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6c607e83fea6e17d139b82876ae45f235adc53714e89f7c86c385bda0177dd11 |
| DOC039-P0056-C001 | LIDAO | IGRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 37c626d20839eb5856992ecae7ccb4dcaccf9b2f27cb2bab2ca607fdf26893c0 |
| DOC039-P0057-C001 | LIDAOE | IGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 93f4af38cc69319228072cc1d76005b5fc422098baa133d614ec6e2b7bd1872e |
| DOC039-P0058-C001 | LDAE | AGROE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4b2cc5fbf08cb6901a293178d54e3d45df41256f5d33cc36f9ad219955fca967 |
| DOC039-P0059-C001 | LIDAOE | AIGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 59a54dcb05967c45837c04b158da36532136fae1ad2b45af193ba7b350a54510 |
| DOC039-P0061-C001 | A | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 858849f84bbe23f5927d8df0935b1043b74ae6588482f5e3b00d0013a71127d2 |
| DOC039-P0062-C001 | LIDA | IGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 473bcff4c81306769bfeac423fd6a73f781f40f0d2f4110fd0088ba17dfae273 |
| DOC039-P0063-C001 | LDAO | GRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 6aa70d0720da146863f619697da627d4d6f10769714d1b8fbab8494cd06e42d8 |
| DOC039-P0064-C001 | LIDAE | AIGROE | XG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 604ebb77dfcd483997fbb2a46e52b03ff64836d06e9999eb1401e3e76ac2170a |
| DOC039-P0065-C001 | LIDAOE | AIGROE | XG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 88622f50fac5d67e746092e6419ea9dfe9025807611a196de196b4467b816f86 |
| DOC039-P0066-C001 | LIDAOE | AIGROE | CG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 9f6fa2064fd727ff31cbe56d3021cb72b45beb00060c5fd29cf5babafba86881 |
| DOC039-P0067-C001 | LIDAOE | AIGUROE | CG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 2902008d36bc46b0c88449b51cad0b3a97fa63a69a2ae8ab4d6904eca20087df |
| DOC039-P0069-C001 | L | RO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | f33c8b3bbb47a74512097041d299937827e5169658d03cf5f855eb7821217492 |
| DOC039-P0070-C001 | LIDAO | IGUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 0de3d7f0ea4c5890b759e1fc527bee123839b9ef90099426ddd9e7c6a8460ab2 |
| DOC039-P0071-C001 | PLIDAO | IGUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | b4f1e8be1b13f20edff37522273fcb2c04b071fb4733fbe01f812d0ba43293a1 |
| DOC039-P0072-C001 | LID | IGRO | X | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 78fc30f4fd63767d68b1fa10965f5088711bad1fafcd8313d0cdd1c1ae1505e6 |
| DOC039-P0073-C001 | LIDAO | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 966b4c547e1238a0b2d92c51f5d52debede4e405b2db7587a21393da7e32b91e |
| DOC039-P0074-C001 | PLDO | GRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 3413851c1bba31497219bc508fd887e88c92bc3dfb19b02e37b332e416d07550 |
| DOC039-P0075-C001 | PLIDO | IGRO | XCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4b13f5b520bdcb75864a8b2bf13b07ff7937f5e7825ef4bc1982619cd1291c45 |
| DOC039-P0077-C001 | LD | RO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 895620156703723be0a7ba82006654322cf0102b9eabd2734dbfca5014a38e42 |
| DOC039-P0078-C001 | LDAE | AGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d791234d83af39fac635670b7126345ee008d3cd820e3c829ecd5df3935aa1bd |
| DOC039-P0079-C001 | LIDA | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a9c23c350166fa69d27659c539176a44841f2e4c3da983c839aa64cbe1362465 |
| DOC039-P0080-C001 | PLIDAOE | AIGURO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | d5f5dbf8cfd115bd89b704430640626c4cbc83cff49dba7b86312b82c229e6fc |
| DOC039-P0081-C001 | PLIDO | IGURO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 5579deed14bbd83ec4bb104e8f51f0bcd489e439936c37c813ecfcc0017e4cf2 |
| DOC039-P0082-C001 | LIDAOE | AIGRO | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 4a520964f41ba0d53a6c984a152d5192ca2750a0ae0e5c1e5767dcbff6a33e5b |
| DOC039-P0083-C001 | LID | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 5fabe0c1e8887b4cbe2fa664c0d3d843260b5c628d6c5c9b1dd5a71f51d4493d |
| DOC039-P0084-C001 | LDAOE | APGROE | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ca966b4bd454099ad55dc57ae97669ec393f598c86dec9d1b235fc4c7d388d96 |
| DOC039-P0085-C001 | LIDAOE | APIGUROE | XMG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | bab048ed998c91eb93e27f5bc6e0366b4d3a20e344799a76b16b099a40ecb37b |
| DOC039-P0086-C001 | LDAO | GUROE | CG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a55f55338c9297d3491b87a90aaf6171552f99330e8a85e56b9c1a81494f56bd |
| DOC039-P0087-C001 | LID | IGRO | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | a59935da4bf83f84ac22b31a3104c092d58c2381879d3ee5d13cdc8e6168972b |
| DOC039-P0088-C001 | LDE | AGRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 280ca5819d8abea7bca3d6ba9d786ba8a99a976dc2b7d297a88f74d667a71664 |
| DOC039-P0089-C001 | LDAOE | APGROE | MCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 6d6ebafd7b76d52a333a3ccb8a56354bae630fdb3642a2c8926deff3e6a4991b |
| DOC039-P0090-C001 | PLDE | AGUOE | M | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 141a53e1cd5fe484b83a99419a88fd10c845e521818f538bbb2959a2ff334143 |
| DOC039-P0090-C002 | LDE | AGRE | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 1ed57eaee2b26b740c873f38ce33cd680f79cf0061a07f42489f225973d8b5e3 |
| DOC039-P0091-C001 | PLIAOE | AIGUROE | MCG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 6263674f64c5e2d8c2ea8d3124038078f8a8ed469ba867d11a193bcba5796812 |
| DOC039-P0091-C002 | PLIDAOE | AIGUROE | XMC | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 53f6bc49e46671c90cfb17fc9d40cca3d9e1eab384a0e8a3772a29d9ca832eb7 |
| DOC039-P0092-C001 | PLIDAOE | IGUROE | XMCG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | e82ce45b7c309f8c5a59cbb612a00cf10d562690f17fe5263853e6182d652729 |
| DOC039-P0092-C002 | PLIDAOE | IGUROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | fbb42d4a9cf8f3b5bff0944f7e2c9cb90c97fc9a7874c32a9b9a4b7d8cbc5179 |
| DOC039-P0093-C001 | PLDA | GRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 67e45fca3876deed374d1011f9e32e567f3f842271f25d863c1130ea21ef03a9 |
| DOC039-P0094-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ed633b662909fa8a2731967bdcd43ac04b26eab6789a359f2439cd6cc66c6d35 |
| DOC039-P0095-C001 | LDE | APGRE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c595d7da8cf2c2b404c25bb3230716e4c35164ce994b26b70bc8da81e02f8bbe |
| DOC040-P0001-C001 | LO | FGRO | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 851e2496b03fb16b88f94a032803c1e247d81ffc30c8169ff54e9831a64d3884 |
| DOC040-P0002-C001 | PLIAOE | FAPIGUROE | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 3507a927f771b9790c1601f1d7127543a6e94ed98096b80be9ac46d1a3ab0989 |
| DOC040-P0003-C001 | LIDAO | FPIRO | MG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | ce71cdfcd62817196426b73c4792a7ab75ba044a9739a04fb28a4ea46b56004b |
| DOC040-P0004-C001 | LIDAOE | FPIGROE | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | b43786b6af6c6a2133eeb14805703554ee2519717c9b1a8ec7b426cd46cc988d |
| DOC040-P0004-C002 | LOE | FGROE | - | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | bf92b5af7e895bdd711e216bff049511794ea3affcd6f8716ebdd6f3dfe08ac0 |
| DOC040-P0005-C001 | LAOE | FGROE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 41b35ddb95360899f37906542b6ae81a5fb8f5787a20e3316475c731a9fd3d41 |
| DOC040-P0006-C001 | LIAOE | FPIGUROE | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 6fc3024af0c2b490e8f107f26217b9af44744a18027ab2f81b6459f8b5db6140 |
| DOC040-P0006-C002 | LDOE | FGUROE | - | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | d7ffeaa712fd2bfc3227ee28a0ced99bbbec015c2d40cd59e30b590694543d4b |
| DOC040-P0007-C001 | LDAOE | FGROE | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 9b13bd7d57c491e7c009f473dc3a9505b7ea606f01c587d32ed22e6151e0c46a |
| DOC040-P0008-C001 | PLIDA | FPIGRO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | ca60f75771288d0b71125bb870226e5f605e556921239da03f933774e67f5748 |
| DOC040-P0009-C001 | PLIDAOE | PIGROE | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 0c669907be058de59b918f0ac44bdde16ac1090c34af28d9d5b6253fdb7e321c |
| DOC040-P0009-C002 | PLIDOE | PIGROE | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 7f6dd261a8f577474a798b9b6df06c2941f42c5e8cc664c176a29e0655784657 |
| DOC040-P0010-C001 | LDAOE | FAPGROE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 1645264d2a35b0a3fa74dd7039db9a2ead82c73eb082aa9b59afce69820fb521 |
| DOC040-P0011-C001 | LIAOE | FAPIGUROE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | a4c37b8b44211f2751f95d64c93331cd1c9ab232fbb81a8789393d167684419c |
| DOC040-P0012-C001 | LIDAE | IGUROE | X | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | f66a7de606c1de2db0669f86d4feb99e963ae077264dcbbca934950e5176589c |
| DOC040-P0013-C001 | LIAOE | APIGUROE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 56aa3f96f9fb4404c6725015add79f32058c8768f4fbdd0348a6ffad0b8cf3fd |
| DOC040-P0013-C002 | LIAOE | IGUROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 113057392052dde9b30bc1b7b93c0bec399e7dbb29d5fa3116f5b8237d43bc86 |
| DOC040-P0014-C001 | LIDAE | IGUROE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 16fa2c3c42e912d781bf97ab8e204fb4ef3bac1330ad587f803426ccb95749a2 |
| DOC040-P0014-C002 | LIDA | FIRO | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 188dda6b0a123f2ab2c070e386f84fd355cea2c43e52bd1bc471057fe153db9d |
| DOC040-P0015-C001 | LIDAOE | FAPIGROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | cd8454d2b519395e0f3759e182ab77e4466403a324703684d29a2746d7c2ee35 |
| DOC040-P0016-C001 | LIDAOE | APIGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 3e7c109b1ed013f601fbd566d8999be52f1b617465a605d4921d6cd11840d5d9 |
| DOC040-P0016-C002 | PLAOE | PGUROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 24ec1aed0b7b35675707b93f7c93d484ec15bcc32f4f3a701c86ff24d73cd11e |
| DOC040-P0017-C001 | LIAOE | APIGROE | XCG | IRRELEVANT / X | ADOPTION_RATE / R | NO | NO | faa992e3c6042d350824900ff5a12777871b9d7b2631b23a4776dcf41424dd02 |
| DOC040-P0018-C001 | PLIE | FIGUROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 340bd7a1501bececc6595aa4cf17c04e0df9274c98b2cec66030a6ccbdc7eed6 |
| DOC040-P0019-C001 | LDOE | FGROE | MC | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 8c261a839d7c6aea3965a5aeb7dc7aa2db6fcc08c2dc00f94760cf1ace869d7b |
| DOC040-P0020-C001 | PLID | FPIGRO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | b917ac9541544874b3f6513307719321bf8fb6a24eb0404a47d9736a8d4e9400 |
| DOC040-P0021-C001 | PLIDAOE | APIGROE | XCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 557a3bef3092cfb795411a348e76af52ff27e7e8202f01868a1b31ef0e1992d2 |
| DOC040-P0022-C001 | PLDAOE | APUROE | XMCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 5d8c5c29c1270cf21b9ff2d54b29864a53a4514b2031e2a67a7b92d7aaa5ef29 |
| DOC040-P0023-C001 | PLIDAOE | FAPIGROE | XMG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | aae4a2b9a2d0409d39665c554b2d5141a31b2ab938981f552930d6759b625437 |
| DOC040-P0023-C002 | PLID | PIRO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | dae49f5a6e904c8fb43e8a62a3f3dc42f6082b45d6393bb09ba45f89ed67b3d2 |
| DOC040-P0024-C001 | PLIAOE | FPIGUROE | XCG | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | NO | NO | f6e2a7b5c992a9463c3f3d28fd40737e20245683e4db6f4e23d4b77fbfc332d5 |
| DOC040-P0025-C001 | PLIDAOE | IGUROE | XMCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 94969f9a80d8ab6a7956d9ceb99f4dc9dcdc83c62de5d74c25fbef4ed7a7089f |
| DOC040-P0025-C002 | LAO | GROE | MC | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 72db5dd22248465815e5af92cc3d0927c05e44b30621c53c6567d43972defc1d |
| DOC040-P0026-C001 | PLIOE | IGROE | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | bc729216bdd94e5ba400a096e935c4c73bbdde16db0813fdcd2c274e212724f3 |
| DOC040-P0027-C001 | PLIDAOE | PIGUROE | G | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | dc951272f3797cf8e3d952aba1f966b7589394b2ccf6b9aa37fdae81ffd62b27 |
| DOC040-P0028-C001 | PLIDAO | FAPIGROE | MCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 71d6bb63a8433125cb058fdda62f8eb97052afaaa9aa8d1c5b0709d4f670ac01 |
| DOC040-P0028-C002 | LDOE | APGROE | CG | IRRELEVANT / X | INTENDED_ANALYTICS_USE / T | NO | NO | 3067d3861cf693bc86c3d362a453215a594847c25449d04ea965aa599d4552ad |
| DOC040-P0029-C001 | LIDOE | APIGUROE | XCG | IRRELEVANT / X | ANALYTICS_POLICY_RECOMMENDATION / P | NO | NO | 24e978a160ad8c19bf02f0a1adcc54761ecc26b4bb0e2af6ccfb51af5a6c9f3b |
| DOC040-P0030-C001 | PLIDAOE | PIGUROE | XCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 5e8e50c62009c18d977ee0fce8eeb98a0442a0515ecc9de14398610ce57f799a |
| DOC040-P0030-C002 | PLIAO | IGRO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | b9345f2e75e6cd81b7cec74c9ae4001b2c94ace1dd7edbc6bbc2d7e220e78045 |
| DOC040-P0031-C001 | PLIDAOE | IGROE | G | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | a17fc258173e3b8fe3eb8fffb7931980fda8be2956624a8c506f1cdf6f429a01 |
| DOC040-P0032-C001 | PLIDOE | APIGUROE | XCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | cf3a9a6088ca168962686a3fadc7d5deef2c8c154bfc4543de3ee9389b42de77 |
| DOC040-P0032-C002 | LIO | IGRO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | c5eb4e91ca3059ba379269d90ae9376cb9eaedb4ba7836a3baed13d80190c136 |
| DOC040-P0033-C001 | PLO | GRO | CG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 54d6b4f6dd4b4a12ce0279a7605f3caf0caf6a780f2b58efcd501735c7edcdab |
| DOC040-P0034-C001 | LIDAO | FPIGURO | XG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 5ea49dc964483fdfb7442f04c8c8dbd0e877641ff947ccb1ce9a6cf0b55cc61e |
| DOC040-P0034-C002 | LI | PIGURO | XMG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | fe3ddb2cc6566de079314624e03f9bc5868958b322e4a64f4bb2e4db639cede3 |
| DOC040-P0035-C001 | LAOE | APGROE | MG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | c08c7b347379ed74ba0091ecca1fcd022d6525a35e79595746b3441cc8b2ef7c |
| DOC040-P0036-C001 | LIDAE | FIGROE | MG | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | NO | NO | 816ce8bf325b7594840f3a8d4a666226c94283e7708c956677fa2cfeb17a5073 |
| DOC040-P0036-C002 | LIDA | FIGROE | XM | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | NO | NO | c98faaab5d0a5f4da886f47f1b3fad6e045fac5a801dab2a25c5824bf958a1db |
| DOC040-P0037-C001 | LIDAO | FAPIGURO | XMG | IRRELEVANT / X | IMPLEMENTATION_GUIDANCE / J | NO | NO | a381cad1764e227a5de15638bb265cec68ea84b2c673ae3779196ada5284dd1c |
| DOC040-P0038-C001 | LIDAOE | FAPIGROE | XMCG | IRRELEVANT / X | OTHER_NEAR_MISS / Z | NO | NO | 4aab7d25867ddbe140d7fe49eb10b7b2bb88fd20b3e56a7842ab075643aa27f5 |
| DOC040-P0038-C002 | LDAO | FGRO | CG | IRRELEVANT / X | OTHER_NEAR_MISS / Z | NO | NO | 61f93b4dba6183fdcceffd9f3ad73b2fb769d411be183273f79afb9c2ee5e8d6 |
| DOC040-P0039-C001 | LIDAOE | IGROE | XG | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 12198357aa9d58490a90a5ef8fa733748155eecf4cf4a48d49b970e804531558 |
| DOC040-P0040-C001 | PLIDAOE | PIGUROE | XMCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 5e37d7e611673a420a982088764b18f27fe9ed00d1115d10d3900f2dfe9cc063 |
| DOC040-P0040-C002 | LIDA | FIGRO | XM | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 5799a66f28a5f76a0f91f969c7818360b4bd6637d08278857705dd6f90428946 |
| DOC040-P0041-C001 | PLIDAOE | PIGUROE | XMCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 9fc25fdd7204bf99e25af39ffdde57d801e69805cab7057af87ef9d16e1b1a98 |
| DOC040-P0041-C002 | PLIOE | IGUROE | C | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | f14d2ca5fb56eaa806738184f365a88424f77ce96869d6588552601bc951782c |
| DOC040-P0042-C001 | LAOE | APGROE | XMCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | fe274c73875091da521ca57b954ea62e0e4a7f0d14048303c067723ce1d03cda |
| DOC040-P0042-C002 | LIDAOE | AGUROE | XMG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 2724821e17e6e71a59859ef0229718fb498dc8819d417dd3b72c184baaae9c53 |
| DOC040-P0043-C001 | LIDOE | APIGUROE | MCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 25ed44ffdd6214499fb60beb0a3bd39d4e241c011d35390ae8b212e26e746337 |
| DOC040-P0044-C001 | PLIAOE | IGUROE | MCG | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 85ac1279e3690183f0f192f23bc9e21f4f2260429609f28ed5d6c9c35b47af92 |
| DOC040-P0044-C002 | PLAO | GROE | M | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | 43c29b352c5a016987f8d0c5604a00787d85f87ca566a1513b4541de7567117c |
| DOC040-P0045-C001 | LA | GUR | M | IRRELEVANT / X | FRAMEWORK_PROVISION / K | NO | NO | b6f65b324958a386164c185b7cbe9a723eab4a7dd38ec7a2e2bf61828fa921b3 |
| DOC040-P0046-C001 | LIDA | FPIRO | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | c106bcc770865778c211d36a03455fef90971245e7b5758703f00a3bbd0a6dcd |
| DOC040-P0047-C001 | LAE | FGROE | - | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 3e7f0eb0432891ec34bdb383c38e2e0de00ce9f52f0b525bc456db2aaa31e8e9 |
| DOC040-P0048-C001 | PLIDAO | FPIGROE | MCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | e60ddb884241d38b1627b6e6c584ca34964a683d7c2a7b40f4bc046864210f09 |
| DOC040-P0049-C001 | LIDAO | IGRO | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 603c32a4389c46b1c3e3119fe8409a16ef46d9ba8623cddef4dd71645c585d04 |
| DOC040-P0050-C001 | LDAO | RO | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 0bde9ae4c47a846b90f2a358142a9811bc8b314d56a57d332403baee6c9ba2dd |
| DOC040-P0051-C001 | LIAOE | APIGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 402090e5564845a8edf0a804fb46f4c0cc35c3746ed6bc7774c9e85c764a889d |
| DOC040-P0052-C001 | LIAOE | PIGROE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 6418036eb07064ed302c7b36dc6f8dfdbc16d4c4b3ef657501f7702d8e5ca2d0 |
| DOC040-P0053-C001 | LIAOE | PIGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 1607c6f87ada64cab14eb375a4f04d4a4e08dd993296a66b5b48a9c5865ba889 |
| DOC040-P0053-C002 | LAO | GRO | C | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 96ad743de397f7e0a6341a77ba6cabba38d2ddc20cc4916b514348dc1eed6536 |
| DOC040-P0054-C001 | LAOE | GUROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | e3207e868ff7d9085ee9b0aeec1d4e98e47baeaa5e9846f6046f262c619d316a |
| DOC040-P0055-C001 | PLIDAE | IGUROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 10b52815092f3fad75f58a8d767b33fa7be308b392ef7279b66c250657716cce |
| DOC040-P0056-C001 | LD | PGRO | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | eaad2bb40790280974e0d3ee26142441bc6b60e4f3d16273e92eb3c42ca1e347 |
| DOC040-P0057-C001 | LIDAE | PIGUROE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 8771de495b4fa3dfb22bf5da06f4f33bba6ddfc4ff6e09c052d3ab06f6607f87 |
| DOC040-P0057-C002 | LDA | PGROE | MG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 0130df7ec6ce327243b7a6fd4198b4be9cce997cc2325710634e20c8b584f48c |
| DOC040-P0058-C001 | PLI | IGRO | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | b786e2856b34017a71c7eab0a7d97d0bd02406a93bee30a3c0cb61cb2b80497c |
| DOC040-P0059-C001 | LIAOE | AIGUROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | ccdb311d166692fba5a72e592c61b1301f9809c8783a3c66f58ae24d172b3674 |
| DOC040-P0059-C002 | LOE | AGURE | G | IRRELEVANT / X | ADOPTION_RATE / R | NO | NO | 90fec51bb9bc65ca4acb0cb524a7a11f7ca2456d8e4048df9b217db4b8293bf1 |
| DOC040-P0060-C001 | LAE | PGRE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | a8ed7c18d457bd7346e94f273df74ddf95b3df4f1aff1d01a10b566de11ac176 |
| DOC040-P0061-C001 | LIDAOE | APIGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 24a6dac992c38cbcad6b9bf719736bfefa6d84d01fb800bfc0ade47cdb87cb9c |
| DOC040-P0061-C002 | LDOE | AGROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | f1f72617043a8263a68a89d1080b28323cc9fc4f7fc973f17c49ee54e0352b7c |
| DOC040-P0062-C001 | PLIDAOE | APIGUROE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 5d03b50c7d345f436063850529aa3c427d3596dbdbee168b647fa08d6dfc8bac |
| DOC040-P0063-C001 | PLAOE | PGUROE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 8fbbab5bfd786c95a968b093136b0b9b1ded655c6a15daa9addedbcf6ad419e2 |
| DOC040-P0064-C001 | LIAOE | AIGUROE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 7a7a4f0a6465a3c89bc1e94e8ba2d814f056a4a435c591f1f04e5c80976f5668 |
| DOC040-P0065-C001 | PLIAOE | PIGUROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 642544d0a215c861998487ee2bc88051eb192c0aca122ae972138135108de223 |
| DOC040-P0066-C001 | LIDAOE | APIGURE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 0d9a40d94293e9bc40147ca57976f378f6c72de230819ed3dd22c0a0fc55dfc2 |
| DOC040-P0066-C002 | LIDAOE | IGUROE | MCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 0307b7559b6359b1743e63e50fcb97757c1a6c77023d0012a23fa0ccaa6403b8 |
| DOC040-P0067-C001 | LIDAOE | APIGUROE | MG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 30af8e821e4b9fa5998b001dda32f3ac77deb1b57591af75f13d1a9e34f3305e |
| DOC040-P0068-C001 | AE | RE | - | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 6b98e24ceb2a69c7f62ddc846817220cdf57fc0f9ff16e10e4020641d720e2b1 |
| DOC040-P0069-C001 | LIDAOE | AIGUROE | XG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | c570bd7c8d0cb3053745fea624b7285de2d30fceb16b80c87a34b4818338a352 |
| DOC040-P0069-C002 | LOE | GURE | G | IRRELEVANT / X | ADOPTION_RATE / R | NO | NO | 5c4a5c03b7de5b8eb57c4919dc378825959527f1bc062ae70d12b82df350557a |
| DOC040-P0070-C001 | LAE | APGROE | MG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 2daa48ca103e803b085fa0b34004b0da49997e9b86792b0139c3f3301784eeac |
| DOC040-P0071-C001 | LIAOE | APIGUROE | XMG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | bcff83fb1a80174ffddb05d996e6041181c9e559b8ece5971b36033e0a5d178b |
| DOC040-P0072-C001 | PLAOE | APGUROE | MCG | IRRELEVANT / X | ADOPTION_RATE / R | NO | NO | a42c21e2b31b24dcdcbe4458a3a807ff80c4583992e184347832d4ef18bb0fee |
| DOC040-P0072-C002 | PLAOE | APGUROE | CG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 08d6cc3157bc76a9f76f4b1fed098a8143d5130ffeeaeb228bb77fa96f97a98d |
| DOC040-P0073-C001 | LAE | RE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | a38627f13bbd60970151c8f9a3173a115e3e739731f4bac74147cc9fd3b2408c |
| DOC040-P0074-C001 | LIDAOE | AIGURE | XCG | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | ff56290e5b14d08ff97b6ea9699008eac5fc1b503127da0d76bd5fd0ac029866 |
| DOC040-P0074-C002 | LAOE | PGRE | G | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | 63461032ca61e7a0731f14c84443cda48eee692c2954fadc8b5665ff054755fa |
| DOC040-P0075-C001 | LAE | GRE | - | IRRELEVANT / X | OTHER_NEAR_MISS / W | NO | NO | f519b01c9fe00a982300dcce7e9726503008aba29b583e706a5ddfc067fdc98f |
| DOC040-P0076-C001 | - | R | - | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 765c7f3cba8e3f0faa3217d35383955098894118d0863b425e51cb96bb639b15 |
| DOC040-P0077-C001 | E | APRE | G | IRRELEVANT / X | IRRELEVANT / X | NO | NO | 236de04e6d7eb06d72608a98026075ea241e6b1168fd895bf75a10f51bdc8898 |

RECHECK_CHUNK_ID_STREAM_SHA256=f6e21c0121f22ed9825e3f9a239165c462b2fc18ccc5a22243f9093a47eab2ca
RECHECK_PAGE_ID_STREAM_SHA256=eea345bde0ffd13e7bd032e0e866dc4d4f351ca46d592e64973f5057756bed3d
RECHECK_ORDER=document_id / physical page / native C ordinal
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
ALL_CANONICAL_CHUNKS_RECHECKED_EXACTLY_ONCE=PASS
PUBLIC_SOURCE_BOUNDARY=PASS
RANKED_RETRIEVAL_USED=NO
EMBEDDINGS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
TASK_JSON_CREATED=NO
HUMAN_VERIFICATION=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
