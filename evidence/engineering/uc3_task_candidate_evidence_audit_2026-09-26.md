# UC3 T021–T028 Draft Candidate Evidence Audit

Date: 2026-09-26

## Status, prospective chronology and protocol gate

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=55d6e33b2674b01969773ee8b99bf71839f94997
PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
PROTOCOL_FREEZE_COMMIT=55d6e33b2674b01969773ee8b99bf71839f94997
AUTHORING_CHRONOLOGY_EXPLICIT=YES
NONTRIVIAL_TASK_RULE_EXPLICIT=YES
RESULT_INDEPENDENCE_EXPLICIT=YES
HUMAN_VERIFICATION_REQUIRED=YES
GOLD_RUNTIME_ISOLATION_REQUIRED=YES
T3B_PROTOCOL_GATE=PASS

The governing v0.2 blob matches the local protocol and the qualified remote-tracking freeze commit. Its nine-step chronology, four prohibited lookup-only categories, substantive direct-retrieval rule, frozen-corpus requirement, result-independence controls, human-verification requirement and runtime gold-isolation requirement were inspected directly. The protocol’s pre-authoring status records remain historical; this artifact now records draft candidate authoring, not human approval or task freeze.

Authoring followed source inspection/information-need identification, drafting question/type, drafting a minimal source-grounded answer, exact evidence binding by direct inspection, and structural/quality audit. No insufficient-evidence candidate is authored here, so no absence conclusion is asserted. Researcher review, explicit approval, human_verified and final cryptographic task freeze remain future gates. No task was changed in response to a retrieval or model result. No drafted candidate was silently repaired after a defect verdict.

## Frozen public-source guard and complete bundle coverage

FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a
CANONICAL_CHUNKS_INDEX=corpus/use_cases/UC3/processed/chunks/index.json
CANONICAL_CHUNKS_FILES=DOC032.chunks.json through DOC040.chunks.json under processed/chunks
CANONICAL_PAGES_INDEX=corpus/use_cases/UC3/processed/pages/index.json
MEMBERSHIP_PATH=corpus/manifest.json (accepted UC3 entries)
SCOPE_PATH=corpus/use_cases/UC3/benchmark_scope.json
DOCUMENT_COUNT=9
SOURCE_UNIT_COUNT=664
CHUNK_BEARING_SOURCE_UNIT_COUNT=638
CHUNK_COUNT=850
CHUNK_INDEX_SHA256=a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e
CANONICAL_CHUNK_ARTIFACT_AGGREGATE_SHA256=ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563
INVENTORY_SHA256=f73f3c06bb96eeec47e0602b1d9d521f346a003bb39be39dfdf2f8f3ec0ef476
AUTHORING_BUNDLE_PATH=/home/emadh/UC3_T3A1_AUTHORING_SOURCE_BUNDLE.txt
AUTHORING_BUNDLE_SHA256=aab297778225ab73a3a589f3ed4793737c16960a07e65a4ceb772eddeb9e2413
BUNDLE_CHUNK_COVERAGE=PASS
FROZEN_PUBLIC_CORPUS_ONLY=YES
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
SENSITIVE_SOURCE_IN_BUNDLE=NO

The complete length-framed bundle was independently parsed and checked against all 850 canonical chunks for exact ID, document, source hash, raw text, order and uniqueness. All nine accepted documents are represented. The 664 source units are extracted physical PDF pages; 638 have canonical chunks and 26 do not. UC3 has no canonical chunks.jsonl: its qualified representation is the index and nine per-document chunk artifacts.

Membership matches the UC3 records at the foundation freeze commit. Chunk-index and aggregate hashes match the freeze; approved raw PDFs match accepted source hashes. Every bundle entry resolves to one of those public documents with exact canonical text and public source identity. This is a positive provenance/coverage boundary check, not a sensitive-keyword zero-match. The sensitive DC4Democracy report was not opened or used. No diagnostic results, ranking or embedding data were inspected. Direct source reads and unranked deterministic term checks were used to inspect candidate regions and potential single-location alternatives.

All page numbers below are physical PDF indexes; printed page labels may differ. Source units use native page_id. REFERENCE_EVIDENCE lists only REQUIRED chunks for the minimal candidate. SUPPORTING/REDUNDANT locations are disclosed for review and are not additional mandatory gold bindings. Difficulty is a design estimate for review, based on breadth/synthesis, not observed system performance.

## T021

TASK_ID=T021
TASK_TYPE=direct_retrieval
QUESTION=When using DigComp 3.0 learning outcomes to develop measures of achieved learning, what measurement risk does the framework identify and what approach does it recommend?
DIFFICULTY_CANDIDATE=low
REQUIRED_DOCUMENTS=["DOC032"]
REFERENCE_EVIDENCE=["DOC032-P0088-C002"]

REFERENCE_ANSWER_CANDIDATE=DigComp 3.0 provides intended, not achieved, learning outcomes. A strictly empirical measurement approach risks undervaluing or omitting softer or harder-to-measure competences. Outcomes that cannot be directly or easily observed or measured are likely to be as important as those that can. The framework recommends a balanced, context-sensitive approach.

### Exact evidence verification

DOCUMENT_ID=DOC032
CHUNK_ID=DOC032-P0088-C002
PAGE_OR_SOURCE_UNIT=physical page 88; DOC032-P0088; section Page 88
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Intended/achieved distinction; strictly empirical measurement can undervalue harder-to-measure competences; balanced, context-sensitive recommendation.
SOURCE_TEXT_ANCHOR=A balanced and context-sensitive approach
CHUNK_TEXT_SHA256=277b0526070a12b20a37015323a2de6c1601dddc272f13a4aa92865d0fe275fe

DOCUMENT_ID=DOC032
CHUNK_ID=DOC032-P0088-C001
PAGE_OR_SOURCE_UNIT=physical page 88; DOC032-P0088; section Page 88
EVIDENCE_CLASSIFICATION=REDUNDANT
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Repeats intended/achieved distinction and undervaluation risk at the end of the overlapping window; the complete requested recommendation is available in C002. Other adaptation steps are outside this question.
SOURCE_TEXT_ANCHOR=DigComp 3.0 includes intended, not achieved learning outcomes
CHUNK_TEXT_SHA256=644cbbe2b6756b733d85fafa7cdf9ae531dabcf0f318f6274712ad2d428a1903

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=A single coherent passage in DOC032-P0088-C002 provides both the measurement risk and the recommended approach. The overlapping C001 is not counted as a second location.
SOURCE_SUFFICIENCY=Both requested propositions and the intended/achieved qualification are explicit in the required chunk.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
SINGLE_LOCATION_COMPLETE_ANSWER=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=The question asks about measurement risk and approach, not a prescribed test instrument or a demonstrated learning outcome.
TEMPORAL_SCOPE_ASSESSMENT=DigComp 3.0 guidance as contained in the frozen corpus; no current implementation, population or cutoff is implied.
ACTOR_SCOPE_ASSESSMENT=Users developing measures of achieved learning; not a claim that the framework itself measured learners.
ACCIDENTAL_CLUE_ASSESSMENT=Names the application context but supplies neither the risk nor the recommendation.
REFERENCE_ANSWER_BOUNDEDNESS=Four sentences; no instrument selection, empirical effectiveness or external measurement theory.
DUPLICATION_RISK=Low. Distinct from civic skills, descriptor behaviours and educator/organisation analytics.
HUMAN_REVIEW_NOTES=Review the intended/achieved qualification and preserve the recommendation as contextual, not a validated measurement recipe.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T022

TASK_ID=T022
TASK_TYPE=direct_retrieval
QUESTION=What commitments does the European Declaration on Digital Rights and Principles make to protect people's informed choice and fundamental rights when they interact with algorithms and AI systems?
DIFFICULTY_CANDIDATE=medium
REQUIRED_DOCUMENTS=["DOC038"]
REFERENCE_EVIDENCE=["DOC038-P0005-C001"]

REFERENCE_ANSWER_CANDIDATE=The Declaration commits to promoting human-centric, trustworthy and ethical AI throughout development, deployment and use; transparency about algorithms and AI, empowerment to use them and information when interacting with them; adequate datasets to avoid discrimination and human supervision of outcomes affecting safety and fundamental rights; preventing AI from pre-empting people's choices; safeguards and appropriate action, including trustworthy standards, for safe systems respecting fundamental rights; and AI research meeting the highest ethical standards and relevant EU law. These are declared commitments, not evidence of their fulfilment.

### Exact evidence verification

DOCUMENT_ID=DOC038
CHUNK_ID=DOC038-P0005-C001
PAGE_OR_SOURCE_UNIT=physical page 5; DOC038-P0005; section Page 5
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=All six commitments in the algorithms/AI subsection: ethical human-centric AI, transparency/informed interaction, adequate datasets/human supervision, free choice, safeguards and ethical/legal research.
SOURCE_TEXT_ANCHOR=ensuring that technologies such as artificial intelligence are not used to pre-empt people’s choices
CHUNK_TEXT_SHA256=d4452770967bd72850cd0845e2aa7e0925d8038924eff55a7cfa111695f31828

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=One chunk contains the complete algorithms/AI commitments subsection, including all six commitments.
SOURCE_SUFFICIENCY=The required chunk supports each listed commitment; unrelated fair-market/public-space provisions are excluded.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
SINGLE_LOCATION_COMPLETE_ANSWER=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Algorithms/AI subsection bounds the requested commitments. People means everyone described by the Declaration.
TEMPORAL_SCOPE_ASSESSMENT=The frozen Declaration is normative. No claim about current EU legislation, compliance or implementation is required.
ACTOR_SCOPE_ASSESSMENT=The declaring parties commit; people interacting with systems are beneficiaries. Do not turn the commitments into duties imposed on individual users.
ACCIDENTAL_CLUE_ASSESSMENT=Informed choice and fundamental rights identify the substantive scope but disclose none of the six safeguards.
REFERENCE_ANSWER_BOUNDEDNESS=Six commitments plus normative-status qualification; not an evaluation of AI technologies.
DUPLICATION_RISK=Low. Digital rights is distinct from individual competence or analytical-skills instruction.
HUMAN_REVIEW_NOTES=Confirm inclusion of ethical/legal research and human supervision; do not grade proof of actual policy delivery.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T023

TASK_ID=T023
TASK_TYPE=direct_retrieval
QUESTION=According to the Council Recommendation on key competences for lifelong learning, what skills and attitudes underpin constructive civic participation, including engagement with media?
DIFFICULTY_CANDIDATE=medium
REQUIRED_DOCUMENTS=["DOC036"]
REFERENCE_EVIDENCE=["DOC036-P0011-C001"]

REFERENCE_ANSWER_CANDIDATE=Citizenship skills include engaging with others in the common or public interest, critical thinking and integrated problem solving, developing arguments, constructive community participation and decision-making from local to international levels. They include accessing, critically understanding and interacting with traditional and new media and understanding media's democratic role. The attitude rests on respect for human rights and willingness to participate in democratic decisions and civic activities, supporting diversity, gender equality, social cohesion, sustainable lifestyles and peace/non-violence, respecting privacy and environmental responsibility. Interest in political and socioeconomic developments, humanities and intercultural communication supports overcoming prejudice, compromise where necessary, social justice and fairness.

### Exact evidence verification

DOCUMENT_ID=DOC036
CHUNK_ID=DOC036-P0011-C001
PAGE_OR_SOURCE_UNIT=physical page 11; DOC036-P0011; section Page 11
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Citizenship skills, traditional/new media engagement and the human-rights-based participation attitudes, diversity/privacy/environment and compromise/justice qualifications.
SOURCE_TEXT_ANCHOR=Skills for citizenship competence relate to the ability to engage effectively with others in common or public interest
CHUNK_TEXT_SHA256=9724b0737170dbdd32ab7436ce09e1aa62178f4564502f699b51cfd2cdcc4e00

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=The first two citizenship paragraphs in one chunk contain the skills and attitudes requested, including media engagement.
SOURCE_SUFFICIENCY=All answer elements map to the citizenship paragraphs; entrepreneurship content in the same chunk is not used.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
SINGLE_LOCATION_COMPLETE_ANSWER=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Constructive civic participation anchors citizenship competence rather than entrepreneurship or personal/social competence.
TEMPORAL_SCOPE_ASSESSMENT=According to the frozen Council Recommendation; no live citizenship test or current political facts.
ACTOR_SCOPE_ASSESSMENT=Citizens/individuals, not teacher professional competence or institutional governance.
ACCIDENTAL_CLUE_ASSESSMENT=Media is a requested substantive facet; the question does not reveal particular skills or attitudes.
REFERENCE_ANSWER_BOUNDEDNESS=Skills and attitudes only; the preceding knowledge-component list is not required or introduced.
DUPLICATION_RISK=Minor thinking/argument domain overlap with T027, but this task concerns the complete civic-participation skills/attitudes scope, not a thinking-definition/proficiency comparison.
HUMAN_REVIEW_NOTES=Review breadth of the attitude paraphrase; preserve compromise where necessary and distinguish responsible participation from proven behaviour.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T024

TASK_ID=T024
TASK_TYPE=within_document_reasoning
QUESTION=In RFCDC Volume 3, what cautions should a teacher apply when considering high-stakes assessment of learners' values and attitudes and when using observational assessment of competence clusters across situations?
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS=["DOC035"]
REFERENCE_EVIDENCE=["DOC035-P0062-C001", "DOC035-P0069-C001"]

REFERENCE_ANSWER_CANDIDATE=High-stakes assessment of values and attitudes raises respectfulness concerns, including learners' freedom of thought, conscience and religion. Attitudes are complex and personal, so assessment may be perceived as judging the person and may damage future prospects. Users might consider low-stakes assessment for values/attitudes and high-stakes assessment for skills, knowledge and critical understanding, deciding for their context while preserving respectfulness. Observational assessment requires planned situations and records of how learners deploy and adjust competence clusters. Assessor attentiveness, preconceptions and expectations can cause selective perception and inappropriate conclusions; inconsistency across situations can undermine reliability. The text presents contextual choices, not an unconditional ban or a claim that observation is automatically reliable.

### Exact evidence verification

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0062-C001
PAGE_OR_SOURCE_UNIT=physical page 62; DOC035-P0062; section Page 62
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Respectfulness concerns for high-stakes values/attitudes assessment, danger of judging/damaging the person, and contextual mixed-stakes option.
SOURCE_TEXT_ANCHOR=Users of the Framework might wish to consider employing a mixed set of assessment types
CHUNK_TEXT_SHA256=9b33e9d8e4bc831013669989dfb702d4591acd1b026923dcce8be69a94ff392f

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0069-C001
PAGE_OR_SOURCE_UNIT=physical page 69; DOC035-P0069; section Page 69
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Observational assessment uses planned situations/records and tracks adjustment of competence clusters; assessor bias/selective perception and cross-context inconsistency challenge reliability.
SOURCE_TEXT_ANCHOR=A potential vulnerability of observational assessment
CHUNK_TEXT_SHA256=8b440741b8a347d6cd5b12809da893073a775bd0bb261cf23e570d9729760cc9

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0061-C001
PAGE_OR_SOURCE_UNIT=physical page 61; DOC035-P0061; section Page 61
EVIDENCE_CLASSIFICATION=SUPPORTING
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Defines stakes and presents competing arguments; high-stakes decisions need reliable/valid methods. Clarifies why page 62 is contextual guidance rather than a categorical prohibition.
SOURCE_TEXT_ANCHOR=Users of the Framework will need to consider the extent to which they should use high-stakes assessments.
CHUNK_TEXT_SHA256=debd4404471c4d5875a85b1c358703e73d034671a7ae06f28457a743ac8eff95

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=Two distinct passages are essential: page 62 supplies stakes/respectfulness cautions; page 69 supplies observational procedure and assessor/reliability limitations. They are seven physical pages apart, not overlapping windows.
SOURCE_SUFFICIENCY=Both sides are explicit in DOC035. Supporting page 61 corroborates the contextual debate without adding a required gold proposition.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=The question specifies values/attitudes for stakes and competence clusters for observation. It does not conflate observational method with low stakes by definition.
TEMPORAL_SCOPE_ASSESSMENT=Framework guidance only; no case-specific certification decision or evidence of actual reliability.
ACTOR_SCOPE_ASSESSMENT=Teacher/assessor considering learners; respectfulness protects the learner, and observation limitations concern the assessor.
ACCIDENTAL_CLUE_ASSESSMENT=Names two assessment decisions but not the applicable cautions or a preferred answer.
REFERENCE_ANSWER_BOUNDEDNESS=Stakes concerns, contextual option, observation requirements and reliability vulnerabilities; excludes the full catalogue of assessment methods.
DUPLICATION_RISK=Minor shared assessment domain with T028; democratic competence, respectfulness and observation differ from digital evidence/organisational analytics.
HUMAN_REVIEW_NOTES=Do not read the opening continuation on page 62 as an unconditional ban. Page 61 records competing arguments and page 62 offers a contextual choice.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T025

TASK_ID=T025
TASK_TYPE=within_document_reasoning
QUESTION=In the UNESCO ICT Competency Framework for Teachers v3 Pedagogy aspect, how do the teacher's role and proposed learning activities differ between Knowledge Acquisition and Knowledge Creation? Illustrate each level with the lesson- or project-related activities specified in the framework.
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS=["DOC037"]
REFERENCE_EVIDENCE=["DOC037-P0029-C001", "DOC037-P0044-C001"]

REFERENCE_ANSWER_CANDIDATE=At Knowledge Acquisition, teachers make appropriate ICT choices to support teaching/learning methodologies and students' acquisition of subject knowledge. They devise ICT-supported lesson plans, for example using tutorials, drill-and-practice or accessible multilingual digital resources; presentation software and inclusive media can support instruction. At Knowledge Creation, teachers determine learning parameters while encouraging student self-management in student-centred collaborative learning, modelling reasoning, problem solving and knowledge creation. They design collaborative research activities and help students plan projects with activities, timelines, milestones and allocated responsibilities, create digital media and reflect on learning through milestone activities such as blogs or video diaries. These are framework objectives and example activities, not observed attainment.

### Exact evidence verification

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0029-C001
PAGE_OR_SOURCE_UNIT=physical page 29; DOC037-P0029; section Page 29
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Knowledge Acquisition Pedagogy: appropriate ICT choices, subject knowledge, ICT-supported lesson plans/tutorials/drill practice and inclusive presentation/media examples.
SOURCE_TEXT_ANCHOR=KA.3.b. Devise lesson plans
CHUNK_TEXT_SHA256=3839399d8d49d5b3888ad62381c0ab2f898cc363905ae42df9464c82dc3ea3a2

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0044-C001
PAGE_OR_SOURCE_UNIT=physical page 44; DOC037-P0044; section Page 44
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Knowledge Creation Pedagogy: self-management, modelling reasoning/knowledge creation, collaborative research, project planning/timelines/responsibilities and milestone reflection.
SOURCE_TEXT_ANCHOR=KC.3.c. Help students design project
CHUNK_TEXT_SHA256=9de5f844839f781fcfba12f1f1dfae1c5de387248b935ab424c74ed9754a3777

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0026-C001
PAGE_OR_SOURCE_UNIT=physical page 26; DOC037-P0026; section Page 26
EVIDENCE_CLASSIFICATION=SUPPORTING
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Broad pedagogy transition from traditional/didactic approaches to student-centred project/problem collaboration; does not supply both detailed sets of requested lesson/project examples.
SOURCE_TEXT_ANCHOR=III - Aspect: Pedagogy
CHUNK_TEXT_SHA256=b57c484c9dc831fb5872b436497d24d422b5ca6200e1d52179c011efe58b3e34

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=Page 29 provides Acquisition teacher choices and concrete lesson examples; page 44 provides Creation self-management and specific project-planning/reflection activities. Both are needed to complete the requested illustrated comparison.
SOURCE_SUFFICIENCY=The detailed aspect tables support role, objectives and example activities for both levels. Page 26 supplies only a broad transition; it cannot supply the complete detailed illustrated answer.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Pedagogy and the two named levels bound the comparison; Knowledge Deepening and other aspects are not requested.
TEMPORAL_SCOPE_ASSESSMENT=Version 3 framework objectives/examples, not a chronological observation of teacher development or measured attainment.
ACTOR_SCOPE_ASSESSMENT=Teachers support students; the levels describe teacher competencies and curricular training goals, not equivalent student proficiency scores.
ACCIDENTAL_CLUE_ASSESSMENT=Level/aspect names and the request for illustrations bound evidence. No activity or evaluative conclusion is supplied in the question.
REFERENCE_ANSWER_BOUNDEDNESS=Teacher roles and illustrative lesson/project activities only; does not enumerate every objective or demand all examples.
DUPLICATION_RISK=Low. Classroom pedagogical roles are distinct from citizen learning measurement and institutional analytics/governance.
HUMAN_REVIEW_NOTES=A broad two-level summary would not meet this question: preserve the explicit requirement for source-specified activities. Accept equivalent supported examples within the inspected tables; do not require a verbatim list.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T026

TASK_ID=T026
TASK_TYPE=within_document_reasoning
QUESTION=What does DigCompOrg call for in assigning responsibility and reviewing a digital-capacity implementation plan, and in protecting data and planning digital-infrastructure procurement?
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS=["DOC040"]
REFERENCE_EVIDENCE=["DOC040-P0024-C001", "DOC040-P0035-C001"]

REFERENCE_ANSWER_CANDIDATE=Management responsibility for delivery and monitoring of the digital-capacity implementation plan should be clearly assigned. Staffing and resources should align with organisational budgets/plans; outcomes, quality and impact should be reviewed and reported periodically, with the plan updated for organisational needs and technological/pedagogical developments. Infrastructure requires policies, procedures and safeguards for privacy, confidentiality and safe use of technologies/data, including data-protection/licensing obligations, learning-analytics policies and staff/student guidelines. Procurement should account for general and specialist requirements and use whole-of-life costing; a viable operational plan should address procurement, maintenance, interoperability and security of core ICT services. These are framework provisions, not claims about an institution implementing them.

### Exact evidence verification

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0024-C001
PAGE_OR_SOURCE_UNIT=physical page 24; DOC040-P0024; section Page 24
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Assigned management responsibility, staffing/budget alignment, periodic review/reporting and updating the digital-capacity implementation plan.
SOURCE_TEXT_ANCHOR=A process is in place to periodically review and report
CHUNK_TEXT_SHA256=f6e2a7b5c992a9463c3f3d28fd40737e20245683e4db6f4e23d4b77fbfc332d5

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0035-C001
PAGE_OR_SOURCE_UNIT=physical page 35; DOC040-P0035; section Page 35
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Privacy/confidentiality/safety provisions, data/licensing/learning-analytics policies, specialist procurement requirements, whole-of-life costing and core-ICT operational plan.
SOURCE_TEXT_ANCHOR=Whole of life costing models inform decisions
CHUNK_TEXT_SHA256=c08c7b347379ed74ba0091ecca1fcd022d6525a35e79595746b3441cc8b2ef7c

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=Page 24 contains plan delivery/review responsibilities; page 35 contains concrete data safeguards/procurement provisions. Neither alone covers the requested combination.
SOURCE_SUFFICIENCY=All answer clauses are explicit in the two required passages; no unsupported causal relationship between governance and infrastructure is inferred.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
SINGLE_DOCUMENT_COMPLETE_ANSWER=YES

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Responsibility/review and data/procurement bound the answer; not a request for all DigCompOrg elements or an institution-specific plan.
TEMPORAL_SCOPE_ASSESSMENT=Framework provisions, not evidence that any organisation has complied or a current legal advice task.
ACTOR_SCOPE_ASSESSMENT=Educational organisation, management/leadership and infrastructure planning; not individual educator proficiency.
ACCIDENTAL_CLUE_ASSESSMENT=Names the areas requiring comparison but gives no responsible arrangement or safeguard.
REFERENCE_ANSWER_BOUNDEDNESS=Assigned delivery/monitoring, resources, review/update, privacy/safety and procurement/operations only.
DUPLICATION_RISK=Minor DOC040/data-policy overlap with T028. T026 centres plan governance and infrastructure lifecycle; T028 centres analytics purposes and educator-versus-organisation responsibilities. Their complete gold requirements differ.
HUMAN_REVIEW_NOTES=Do not expand whole-of-life costing into numerical calculations or add obligations from current law. General outline tables lack the required review/update and costing detail.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T027

TASK_ID=T027
TASK_TYPE=cross_document_reasoning
QUESTION=How does RFCDC's conceptual account distinguish analytical from critical thinking, and what observable behaviours do its Advanced key descriptors specify for these skills?
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS=["DOC033", "DOC034"]
REFERENCE_EVIDENCE=["DOC033-P0048-C001", "DOC033-P0049-C001", "DOC034-P0021-C001"]

REFERENCE_ANSWER_CANDIDATE=Volume 1 describes analytical thinking as systematically and logically analysing materials, including breaking them into elements and examining relationships, to reach defensible conclusions. Critical thinking evaluates materials and makes judgments, considering consistency with evidence, assumptions and purposes and using explicit criteria, principles or values. Volume 2's Advanced key descriptors for analytical and critical thinking specify identifying discrepancies, inconsistencies or divergences in analysed materials and using explicit, specifiable criteria, principles or values to make judgments. The conceptual distinction explains the kind of thinking; the descriptors express concrete proficiency-related behaviours rather than document identities or measured population attainment.

### Exact evidence verification

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0048-C001
PAGE_OR_SOURCE_UNIT=physical page 48; DOC033-P0048; section Page 48
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Analytical thinking definition: systematic/logical analysis and decomposition into organised constituent elements.
SOURCE_TEXT_ANCHOR=Analytical thinking skills are those skills that are required to analyse
CHUNK_TEXT_SHA256=561a3aa7d0fccbba01765ebcec69137c2d1acbeccf0313ea6fb5e1e7639db99e

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0049-C001
PAGE_OR_SOURCE_UNIT=physical page 49; DOC033-P0049; section Page 49
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Continues analytical relationships/conclusions and defines critical thinking as evaluation/judgment involving evidence, assumptions, purposes and explicit criteria.
SOURCE_TEXT_ANCHOR=Critical thinking skills consist of those skills that are required to evaluate
CHUNK_TEXT_SHA256=f50381ccbc7567848ff58c6154b77bf0cd5e7401892cd77b76706f7c45e24bbd

DOCUMENT_ID=DOC034
CHUNK_ID=DOC034-P0021-C001
PAGE_OR_SOURCE_UNIT=physical page 21; DOC034-P0021; section Page 21
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Advanced key descriptors 68 and 69 for analytical/critical thinking: discrepancies/inconsistencies/divergences and explicit/specifiable criteria/principles/values for judgments.
SOURCE_TEXT_ANCHOR=69 judgments
CHUNK_TEXT_SHA256=d45fdba1255529234463730ca0a9669f3cfef7ac5608100ba65c27cef8c29dac

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0050-C001
PAGE_OR_SOURCE_UNIT=physical page 50; DOC033-P0050; section Page 50
EVIDENCE_CLASSIFICATION=SUPPORTING
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Analytical and critical thinking are inherently linked; useful context but not required to answer the conceptual distinction and Advanced behaviour request.
SOURCE_TEXT_ANCHOR=analytical and critical thinking skills are inherently linked together
CHUNK_TEXT_SHA256=2fe8a26822466267553642063381c38596e19b8741ef17b7a21f8e7bdcb5b977

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=DOC033 provides explicit conceptual definitions; DOC034 supplies the Advanced classification and two concrete key behaviours. Shared terminology does not provide the missing level-specific binding in DOC033 or the complete conceptual distinction in DOC034.
SOURCE_SUFFICIENCY=Three required chunks from two documents cover analytical definition, critical evaluation and Advanced behaviours; the optional linkedness passage is context only.
DOCUMENT_A=DOC033
DOCUMENT_A_NONREDUNDANT_CONTRIBUTION=Analytical thinking definition: systematic/logical analysis and decomposition into organised constituent elements.; Continues analytical relationships/conclusions and defines critical thinking as evaluation/judgment involving evidence, assumptions, purposes and explicit criteria.
DOCUMENT_B=DOC034
DOCUMENT_B_NONREDUNDANT_CONTRIBUTION=Advanced key descriptors 68 and 69 for analytical/critical thinking: discrepancies/inconsistencies/divergences and explicit/specifiable criteria/principles/values for judgments.
SINGLE_DOCUMENT_COMPLETE_ANSWER=NO
CROSS_DOCUMENT_SYNTHESIS_REQUIRED=YES
SINGLE_LOCATION_COMPLETE_ANSWER=NO

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Advanced modifies the key descriptors, not an education level or a claim that a learner has attained them. The task addresses RFCDC analytical/critical thinking only.
TEMPORAL_SCOPE_ASSESSMENT=Frozen RFCDC concepts/descriptors, not empirical population proficiency or a live political-content judgment.
ACTOR_SCOPE_ASSESSMENT=Learners/persons exercising democratic-culture competences; framework concepts are distinct from institutional policy.
ACCIDENTAL_CLUE_ASSESSMENT=Names the competence and proficiency level but gives neither conceptual distinction nor behaviours.
REFERENCE_ANSWER_BOUNDEDNESS=Two conceptual descriptions and the two Advanced key behaviours; no whole descriptor bank or evaluation of real arguments.
DUPLICATION_RISK=Minor critical-thinking domain overlap with T023. Concept-to-Advanced-behaviour mapping is materially different from general civic-participation skills/attitudes.
HUMAN_REVIEW_NOTES=Review the distinction between prose concepts and empirically scaled descriptors. Volume 1 illustrates other competences on page 63; it does not provide these Advanced thinking key descriptors.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## T028

TASK_ID=T028
TASK_TYPE=cross_document_reasoning
QUESTION=How do DigCompEdu and DigCompOrg distinguish educator-level analysis of digital evidence about learners from organisational implementation of learning analytics, in terms of purpose and responsibilities?
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS=["DOC039", "DOC040"]
REFERENCE_EVIDENCE=["DOC039-P0064-C001", "DOC040-P0029-C001"]

REFERENCE_ANSWER_CANDIDATE=DigCompEdu asks educators to generate, select, critically analyse and interpret digital evidence of learner activity, performance and progress to inform teaching and learning. Activities include recording/comparing/synthesising progress data, considering and combining different evidence sources and critically valuing the evidence. DigCompOrg gives learning analytics strategic organisational consideration, aiming to optimise individual/group outcomes and organisational performance. Before implementation, the organisation should have a code of practice and processes for safe, secure collection, validation, storage, aggregation, analysis and reporting of student data. Analytics supports immediate personalised feedback and tutorial/remedial interventions; aggregated progress and achievement data inform quality management, course design/review and retention/outcome interventions. These are distinct framework responsibilities, not proven effects or equivalent proficiency scales.

### Exact evidence verification

DOCUMENT_ID=DOC039
CHUNK_ID=DOC039-P0064-C001
PAGE_OR_SOURCE_UNIT=physical page 64; DOC039-P0064; section Page 64
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Educator competence/activities for generating, selecting, critically interpreting digital learner evidence, combining sources and informing teaching/learning.
SOURCE_TEXT_ANCHOR=To generate, select, critically analyse and interpret digital evidence
CHUNK_TEXT_SHA256=604ebb77dfcd483997fbb2a46e52b03ff64836d06e9999eb1401e3e76ac2170a

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0029-C001
PAGE_OR_SOURCE_UNIT=physical page 29; DOC040-P0029; section Page 29
EVIDENCE_CLASSIFICATION=REQUIRED
EXACT_CHUNK_OCCURRENCES=1
SUPPORTED_PROPOSITION=Organisational strategic purposes, pre-implementation safe-data code/processes, feedback/intervention uses and aggregate quality/course/retention uses.
SOURCE_TEXT_ANCHOR=Before implementing learning analytics, the organisation has
CHUNK_TEXT_SHA256=24e978a160ad8c19bf02f0a1adcc54761ecc26b4bb0e2af6ccfb51af5a6c9f3b

### Type integrity and answerability

TYPE_VALIDITY_JUSTIFICATION=DOC039 contributes educator evidence interpretation and source combination; DOC040 contributes organisational strategy, pre-implementation data code/processes and aggregate quality/course uses. Neither supplies the complete other-framework account.
SOURCE_SUFFICIENCY=Two coherent passages supply both named levels and their non-redundant responsibilities without outside data-governance law.
DOCUMENT_A=DOC039
DOCUMENT_A_NONREDUNDANT_CONTRIBUTION=Educator competence/activities for generating, selecting, critically interpreting digital learner evidence, combining sources and informing teaching/learning.
DOCUMENT_B=DOC040
DOCUMENT_B_NONREDUNDANT_CONTRIBUTION=Organisational strategic purposes, pre-implementation safe-data code/processes, feedback/intervention uses and aggregate quality/course/retention uses.
SINGLE_DOCUMENT_COMPLETE_ANSWER=NO
CROSS_DOCUMENT_SYNTHESIS_REQUIRED=YES
SINGLE_LOCATION_COMPLETE_ANSWER=NO

### Adversarial and human-review record

AMBIGUITY_ASSESSMENT=Educator versus organisation and evidence analysis versus analytics implementation are explicit. The task does not equate learner data with measured causality.
TEMPORAL_SCOPE_ASSESSMENT=According to the frozen frameworks, not current practice or a claim of observed intervention effects.
ACTOR_SCOPE_ASSESSMENT=Educator responsibility in DigCompEdu contrasted with organisation-level provision in DigCompOrg; no equivalence of proficiency schemes.
ACCIDENTAL_CLUE_ASSESSMENT=The actor levels define comparison scope but do not disclose analysis activities, data safeguards or organisational uses.
REFERENCE_ANSWER_BOUNDEDNESS=Purposes/responsibilities of the two named sections, not all assessment competences or all organisational assessment practices.
DUPLICATION_RISK=Minor assessment domain with T024 and DOC040/privacy domain with T026; no repeated complete answer or interchangeable task requirement.
HUMAN_REVIEW_NOTES=The organisational code of practice is explicitly before implementation. Preserve critical evaluation of evidence at educator level; do not infer that the organisation guarantees improved outcomes.
VERDICT=READY_FOR_HUMAN_REVIEW
EXACT_DEFECT=NONE_IDENTIFIED

## Joint adversarial audit

DUPLICATE_EXACT_QUESTIONS=0
MATERIAL_DUPLICATE_TASKS=0
REPEATED_REFERENCE_ANSWERS=0
TASK_DIVERSITY_AUDIT=PASS
AMBIGUITY_AUDIT=PASS_WITH_DOCUMENTED_REVIEW_QUALIFICATIONS
TASK_TYPE_INTEGRITY=PASS
SOURCE_TRACEABILITY=PASS
REFERENCE_SUPPORT=PASS
ACCIDENTAL_GOLD_IN_QUESTIONS=NONE_IDENTIFIED

| Check | Finding |
| --- | --- |
| Duplicate IDs/questions/answers | Eight unique IDs, distinct exact questions and distinct full answer candidates; deterministic equality checks pass. |
| Material information needs | Measurement risk; AI rights commitments; civic skills/attitudes; assessment stakes/observation; two-level pedagogical activities; organisational governance/infrastructure; thinking concepts/Advanced descriptors; educator/organisation analytics. None is interchangeable. |
| Document concentration | All nine accepted documents contribute REQUIRED evidence. DOC040 contributes to two tasks; every other document contributes to one. Maximum required-document use is two tasks. |
| Actor/framework concentration | Citizen learning/participation, public rights, democratic-culture learners/assessors, teachers and educational organisations are all represented. RFCDC appears in two distinct needs; organisational framework use is bounded to different sections. |
| Citizen / educator / organisation | Each question explicitly identifies its source/context or actor level. T028 requests the actor-level comparison rather than treating those roles as equivalent. |
| Competence / rights / mechanism | T022 concerns normative commitments; T023/T027 concern competences/descriptors; T024/T025/T026/T028 concern specified assessment, pedagogy or organisational guidance. Answers do not turn them into empirical outcomes. |
| Dates/current-policy assumptions | Questions are anchored to frozen named texts/framework versions. No cutoff or current-law lookup is needed. Framework publication/version differences remain source context, not a chronological implementation claim. |
| Broad or competing golds | T025 permits equivalent source-specified illustrations, with the two required tables providing the permitted scope. T024 preserves contextual assessment choices. Other answers enumerate the requested bounded subsection, not whole frameworks. |
| Source conflict | No contradictory proposition was identified in the cited evidence for the requested scopes. Different actors and normative/descriptive purposes are preserved; no equivalence of proficiency scales or causal outcome is inferred. This is not a separate corpus-wide conflict/absence audit. |
| Within-document overlap | Three tasks use two distinct physical pages each: 62/69, 29/44 and 24/35. No overlapping windows are treated as separate reasoning locations. |
| Cross-document overlap | T027 needs the conceptual definitions plus Advanced labels/behaviours; T028 needs educator critical evidence interpretation plus organisation strategy/data safeguards and aggregate uses. Shared domain language cannot complete either comparison from one source. |
| Alternative summaries | UNESCO pages 23–26/overview tables give the broad pedagogical transition but not both detailed lesson/project illustrations. DigCompOrg overview tables list governance/infrastructure headings but do not provide periodic update, specialist procurement and whole-of-life detail. RFCDC Volume 1 page 63 illustrates listening and politics/human-rights descriptors, not Advanced analytical/critical-thinking descriptors. |
| Answer clues | Framework/aspect/level labels delimit substantive scope. No answer values, prescribed outcome, evidence IDs or reference-answer text are embedded in questions. Naming a framework does not make the information need a title/identity lookup. |

### Allocation, membership and schema compatibility precheck

AUDITED_TASKS=8
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
READY_FOR_HUMAN_REVIEW=8
DEFECT_REQUIRES_REVIEW=0
REQUIRED_DOCUMENTS_MEMBERSHIP_VALID=PASS
ALL_REFERENCED_CHUNKS_EXIST_EXACTLY_ONCE=PASS
REQUIRED_CHUNK_BINDINGS=14
SCHEMA_COMPATIBILITY_PRECHECK=PASS

The unchanged canonical task schema is benchmark/schema/task.schema.json, SHA256 34ddb275e659b86d759d5fabcf3500bc963c34b60425f601677b88bbb858145f. IDs, task-type/difficulty enums, non-empty text, document-ID bindings and available chunk/page evidence fields were checked against its representation. This is a candidate compatibility/structural precheck, not validation or creation of serialized canonical task files. No loader/workflow was executed. All verdicts remain recommendations for researcher review; none confers human_verified or frozen status. T029/T030 were not drafted and no absence claims were made.

Gold-leakage inspection here concerns question content and keeping draft gold in this engineering artifact. The frozen protocol continues to require actual runtime isolation at the later task-validation gate; this step neither executes runtime nor claims a new runtime-isolation test result.

### Required-document coverage

| Document | Tasks requiring it |
| --- | --- |
| DOC032 | T021 |
| DOC033 | T027 |
| DOC034 | T027 |
| DOC035 | T024 |
| DOC036 | T023 |
| DOC037 | T025 |
| DOC038 | T022 |
| DOC039 | T028 |
| DOC040 | T026, T028 |

## Validation and provenance

INVENTORY_UNCHANGED=YES
EXTERNAL_BUNDLE_UNCHANGED=YES
PROTOCOL_UNCHANGED=YES
CORPUS_FOUNDATION_FILES_UNCHANGED=YES
TRACKED_MODIFIED_COUNT=0
STAGED_COUNT=0
UNTRACKED_COUNT=2
DIFF_CHECK=PASS

PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
LLM_ASSISTED_CANDIDATE_AUTHORING=YES
FROZEN_PUBLIC_CORPUS_ONLY=YES
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
TASK_JSON_CREATED=NO
HUMAN_VERIFICATION=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
