# UC3 T021–T030 Researcher Human-Review Dossier

Date: 2026-09-27

## Status, authority and review boundary

This dossier prepares a researcher decision; it does not record researcher approval. All candidate questions, reference-answer candidates and positive-evidence bindings are copied unchanged from their authoritative audits. The open precision issues for T029/T030 are recommendations only. No suggestion has been applied. The earlier READY_FOR_HUMAN_REVIEW verdicts remain historical audit findings and are not replaced in those files.

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=55d6e33b2674b01969773ee8b99bf71839f94997
PROTOCOL_FREEZE_COMMIT=55d6e33b2674b01969773ee8b99bf71839f94997
UC3_FOUNDATION_FREEZE_COMMIT=8705987d8350c741416fd91481667e9c928ef33a
PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
AUTHORITATIVE_ARTIFACT=evidence/engineering/uc3_task_authoring_inventory_2026-09-26.md
ARTIFACT_SHA256=f73f3c06bb96eeec47e0602b1d9d521f346a003bb39be39dfdf2f8f3ec0ef476
AUTHORITATIVE_ARTIFACT=evidence/engineering/uc3_task_candidate_evidence_audit_2026-09-26.md
ARTIFACT_SHA256=9ab8222b7526cca0325855a2b3e7abf6746b2fb411ce0f91f9d71f99468f181f
AUTHORITATIVE_ARTIFACT=evidence/engineering/uc3_insufficient_evidence_absence_audit_2026-09-27.md
ARTIFACT_SHA256=0c428e910348eb3029ad72dcc813e2f38c29ca297304e1841fbf43d5fd26d3a2

The protocol explicitly requires prospective source-based authoring, substantive information needs, result independence, human approval and later runtime gold isolation. The historical inventory and protocol pre-authoring status statements describe their creation stages; candidates have subsequently been drafted in the unchanged audits. No retroactive change is made.

## Corpus and source-traceability foundation

CANONICAL_CHUNKS_PATH=corpus/use_cases/UC3/processed/chunks/index.json and DOC032–DOC040.chunks.json
CANONICAL_SOURCE_UNITS_PATH=corpus/use_cases/UC3/processed/pages/index.json and DOC032–DOC040.pages.json
MEMBERSHIP_PATH=corpus/manifest.json (accepted UC3 records)
SCOPE_PATH=corpus/use_cases/UC3/benchmark_scope.json
DOCUMENT_COUNT=9
SOURCE_UNIT_COUNT=664
CHUNK_COUNT=850
CHUNK_BEARING_SOURCE_UNIT_COUNT=638
SOURCE_UNITS_WITHOUT_CHUNKS=26
CHUNK_INDEX_SHA256=a89d618882c5ffe44ca852e0cc07f1730916cbd01ec464a3eecd22d5063e026e
CANONICAL_CHUNK_ARTIFACT_AGGREGATE_SHA256=ea846ed576b7b4435d67182897a7fee6f9d17f533dc13290b34d2bae33d38563
PUBLIC_SOURCE_BOUNDARY=PASS
SENSITIVE_SOURCE_IN_RUNTIME_CORPUS=NO

All 14 REQUIRED positive-evidence chunks and disclosed SUPPORTING/REDUNDANT locations were resolved directly against canonical public chunks and their audit text hashes. The actual required passages were read to review answer support and actor/temporal qualifications. Distinct source pages remain distinct evidence locations. The 850-row absence ledger was independently checked for exact canonical ID order and original-text hashes; its corpus-wide inspection and scan findings are bound by the unchanged absence-audit hash, not recreated as a ranked search. No external research or sensitive report was consulted. Page numbers below are physical PDF pages, not necessarily printed labels.

Difficulty for T021–T028 is copied from the candidate audit. T029/T030 have no difficulty label in their absence audit: high is proposed here for review because they require distinguishing plausible empirical/process evidence from the requested realised result across the corpus. This is a design estimate, not measured system performance.

## Candidate review records

## T021

TASK_ID=T021
TASK_TYPE=direct_retrieval
DIFFICULTY_CANDIDATE=low
EXACT_LATEST_CANDIDATE_QUESTION=When using DigComp 3.0 learning outcomes to develop measures of achieved learning, what measurement risk does the framework identify and what approach does it recommend?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC032"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC032-P0088-C002"]
REFERENCE_ANSWER_CANDIDATE=DigComp 3.0 provides intended, not achieved, learning outcomes. A strictly empirical measurement approach risks undervaluing or omitting softer or harder-to-measure competences. Outcomes that cannot be directly or easily observed or measured are likely to be as important as those that can. The framework recommends a balanced, context-sensitive approach.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC032
CHUNK_ID=DOC032-P0088-C002
PAGE_OR_SOURCE_UNIT=physical page 88; DOC032-P0088; section Page 88
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Intended/achieved distinction; strictly empirical measurement can undervalue harder-to-measure competences; balanced, context-sensitive recommendation.
CHUNK_TEXT_SHA256=277b0526070a12b20a37015323a2de6c1601dddc272f13a4aa92865d0fe275fe

DOCUMENT_ID=DOC032
CHUNK_ID=DOC032-P0088-C001
PAGE_OR_SOURCE_UNIT=physical page 88; DOC032-P0088; section Page 88
EVIDENCE_CLASSIFICATION=REDUNDANT
SUPPORTED_PROPOSITION=Repeats intended/achieved distinction and undervaluation risk at the end of the overlapping window; the complete requested recommendation is available in C002. Other adaptation steps are outside this question.
CHUNK_TEXT_SHA256=644cbbe2b6756b733d85fafa7cdf9ae531dabcf0f318f6274712ad2d428a1903

### Reviewer checks

QUESTION_QUALITY=PASS; a substantive measurement-design need, bounded to the stated risk and recommendation; no metadata lookup.
TASK_TYPE_INTEGRITY=PASS; A single coherent passage in DOC032-P0088-C002 provides both the measurement risk and the recommended approach. The overlapping C001 is not counted as a second location.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; Both requested propositions and the intended/achieved qualification are explicit in the required chunk.
AMBIGUITY_ASSESSMENT=The question asks about measurement risk and approach, not a prescribed test instrument or a demonstrated learning outcome.
TEMPORAL_SCOPE=DigComp 3.0 guidance as contained in the frozen corpus; no current implementation, population or cutoff is implied.
ACTOR_SCOPE=Users developing measures of achieved learning; not a claim that the framework itself measured learners.
ACCIDENTAL_CLUE_ASSESSMENT=Names the application context but supplies neither the risk nor the recommendation.
REFERENCE_ANSWER_BOUNDEDNESS=Four sentences; no instrument selection, empirical effectiveness or external measurement theory.
DUPLICATION_ASSESSMENT=Low. Distinct from civic skills, descriptor behaviours and educator/organisation analytics.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
HUMAN_REVIEW_NOTES=Review the intended/achieved qualification and preserve the recommendation as contextual, not a validated measurement recipe.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T022

TASK_ID=T022
TASK_TYPE=direct_retrieval
DIFFICULTY_CANDIDATE=medium
EXACT_LATEST_CANDIDATE_QUESTION=What commitments does the European Declaration on Digital Rights and Principles make to protect people's informed choice and fundamental rights when they interact with algorithms and AI systems?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC038"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC038-P0005-C001"]
REFERENCE_ANSWER_CANDIDATE=The Declaration commits to promoting human-centric, trustworthy and ethical AI throughout development, deployment and use; transparency about algorithms and AI, empowerment to use them and information when interacting with them; adequate datasets to avoid discrimination and human supervision of outcomes affecting safety and fundamental rights; preventing AI from pre-empting people's choices; safeguards and appropriate action, including trustworthy standards, for safe systems respecting fundamental rights; and AI research meeting the highest ethical standards and relevant EU law. These are declared commitments, not evidence of their fulfilment.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC038
CHUNK_ID=DOC038-P0005-C001
PAGE_OR_SOURCE_UNIT=physical page 5; DOC038-P0005; section Page 5
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=All six commitments in the algorithms/AI subsection: ethical human-centric AI, transparency/informed interaction, adequate datasets/human supervision, free choice, safeguards and ethical/legal research.
CHUNK_TEXT_SHA256=d4452770967bd72850cd0845e2aa7e0925d8038924eff55a7cfa111695f31828

### Reviewer checks

QUESTION_QUALITY=PASS; a substantive public-rights/AI safeguards need; the algorithms/AI subsection bounds the commitments.
TASK_TYPE_INTEGRITY=PASS; One chunk contains the complete algorithms/AI commitments subsection, including all six commitments.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; The required chunk supports each listed commitment; unrelated fair-market/public-space provisions are excluded.
AMBIGUITY_ASSESSMENT=Algorithms/AI subsection bounds the requested commitments. People means everyone described by the Declaration.
TEMPORAL_SCOPE=The frozen Declaration is normative. No claim about current EU legislation, compliance or implementation is required.
ACTOR_SCOPE=The declaring parties commit; people interacting with systems are beneficiaries. Do not turn the commitments into duties imposed on individual users.
ACCIDENTAL_CLUE_ASSESSMENT=Informed choice and fundamental rights identify the substantive scope but disclose none of the six safeguards.
REFERENCE_ANSWER_BOUNDEDNESS=Six commitments plus normative-status qualification; not an evaluation of AI technologies.
DUPLICATION_ASSESSMENT=Low. Digital rights is distinct from individual competence or analytical-skills instruction.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
HUMAN_REVIEW_NOTES=Confirm inclusion of ethical/legal research and human supervision; do not grade proof of actual policy delivery.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T023

TASK_ID=T023
TASK_TYPE=direct_retrieval
DIFFICULTY_CANDIDATE=medium
EXACT_LATEST_CANDIDATE_QUESTION=According to the Council Recommendation on key competences for lifelong learning, what skills and attitudes underpin constructive civic participation, including engagement with media?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC036"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC036-P0011-C001"]
REFERENCE_ANSWER_CANDIDATE=Citizenship skills include engaging with others in the common or public interest, critical thinking and integrated problem solving, developing arguments, constructive community participation and decision-making from local to international levels. They include accessing, critically understanding and interacting with traditional and new media and understanding media's democratic role. The attitude rests on respect for human rights and willingness to participate in democratic decisions and civic activities, supporting diversity, gender equality, social cohesion, sustainable lifestyles and peace/non-violence, respecting privacy and environmental responsibility. Interest in political and socioeconomic developments, humanities and intercultural communication supports overcoming prejudice, compromise where necessary, social justice and fairness.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC036
CHUNK_ID=DOC036-P0011-C001
PAGE_OR_SOURCE_UNIT=physical page 11; DOC036-P0011; section Page 11
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Citizenship skills, traditional/new media engagement and the human-rights-based participation attitudes, diversity/privacy/environment and compromise/justice qualifications.
CHUNK_TEXT_SHA256=9724b0737170dbdd32ab7436ce09e1aa62178f4564502f699b51cfd2cdcc4e00

### Reviewer checks

QUESTION_QUALITY=PASS; a substantive civic-participation skills/attitudes need, including media; the citizenship paragraphs bound the content.
TASK_TYPE_INTEGRITY=PASS; The first two citizenship paragraphs in one chunk contain the skills and attitudes requested, including media engagement.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; All answer elements map to the citizenship paragraphs; entrepreneurship content in the same chunk is not used.
AMBIGUITY_ASSESSMENT=Constructive civic participation anchors citizenship competence rather than entrepreneurship or personal/social competence.
TEMPORAL_SCOPE=According to the frozen Council Recommendation; no live citizenship test or current political facts.
ACTOR_SCOPE=Citizens/individuals, not teacher professional competence or institutional governance.
ACCIDENTAL_CLUE_ASSESSMENT=Media is a requested substantive facet; the question does not reveal particular skills or attitudes.
REFERENCE_ANSWER_BOUNDEDNESS=Skills and attitudes only; the preceding knowledge-component list is not required or introduced.
DUPLICATION_ASSESSMENT=Minor thinking/argument domain overlap with T027, but this task concerns the complete civic-participation skills/attitudes scope, not a thinking-definition/proficiency comparison.
LOCALIZED_EVIDENCE_SUFFICIENT=YES
HUMAN_REVIEW_NOTES=Review breadth of the attitude paraphrase; preserve compromise where necessary and distinguish responsible participation from proven behaviour.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T024

TASK_ID=T024
TASK_TYPE=within_document_reasoning
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=In RFCDC Volume 3, what cautions should a teacher apply when considering high-stakes assessment of learners' values and attitudes and when using observational assessment of competence clusters across situations?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC035"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC035-P0062-C001", "DOC035-P0069-C001"]
REFERENCE_ANSWER_CANDIDATE=High-stakes assessment of values and attitudes raises respectfulness concerns, including learners' freedom of thought, conscience and religion. Attitudes are complex and personal, so assessment may be perceived as judging the person and may damage future prospects. Users might consider low-stakes assessment for values/attitudes and high-stakes assessment for skills, knowledge and critical understanding, deciding for their context while preserving respectfulness. Observational assessment requires planned situations and records of how learners deploy and adjust competence clusters. Assessor attentiveness, preconceptions and expectations can cause selective perception and inappropriate conclusions; inconsistency across situations can undermine reliability. The text presents contextual choices, not an unconditional ban or a claim that observation is automatically reliable.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0062-C001
PAGE_OR_SOURCE_UNIT=physical page 62; DOC035-P0062; section Page 62
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Respectfulness concerns for high-stakes values/attitudes assessment, danger of judging/damaging the person, and contextual mixed-stakes option.
CHUNK_TEXT_SHA256=9b33e9d8e4bc831013669989dfb702d4591acd1b026923dcce8be69a94ff392f

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0069-C001
PAGE_OR_SOURCE_UNIT=physical page 69; DOC035-P0069; section Page 69
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Observational assessment uses planned situations/records and tracks adjustment of competence clusters; assessor bias/selective perception and cross-context inconsistency challenge reliability.
CHUNK_TEXT_SHA256=8b440741b8a347d6cd5b12809da893073a775bd0bb261cf23e570d9729760cc9

DOCUMENT_ID=DOC035
CHUNK_ID=DOC035-P0061-C001
PAGE_OR_SOURCE_UNIT=physical page 61; DOC035-P0061; section Page 61
EVIDENCE_CLASSIFICATION=SUPPORTING
SUPPORTED_PROPOSITION=Defines stakes and presents competing arguments; high-stakes decisions need reliable/valid methods. Clarifies why page 62 is contextual guidance rather than a categorical prohibition.
CHUNK_TEXT_SHA256=debd4404471c4d5875a85b1c358703e73d034671a7ae06f28457a743ac8eff95

### Reviewer checks

QUESTION_QUALITY=PASS; a teacher assessment-design need connecting ethical stakes and observational reliability, with contextual choices preserved.
TASK_TYPE_INTEGRITY=PASS; Two distinct passages are essential: page 62 supplies stakes/respectfulness cautions; page 69 supplies observational procedure and assessor/reliability limitations. They are seven physical pages apart, not overlapping windows.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; Both sides are explicit in DOC035. Supporting page 61 corroborates the contextual debate without adding a required gold proposition.
AMBIGUITY_ASSESSMENT=The question specifies values/attitudes for stakes and competence clusters for observation. It does not conflate observational method with low stakes by definition.
TEMPORAL_SCOPE=Framework guidance only; no case-specific certification decision or evidence of actual reliability.
ACTOR_SCOPE=Teacher/assessor considering learners; respectfulness protects the learner, and observation limitations concern the assessor.
ACCIDENTAL_CLUE_ASSESSMENT=Names two assessment decisions but not the applicable cautions or a preferred answer.
REFERENCE_ANSWER_BOUNDEDNESS=Stakes concerns, contextual option, observation requirements and reliability vulnerabilities; excludes the full catalogue of assessment methods.
DUPLICATION_ASSESSMENT=Minor shared assessment domain with T028; democratic competence, respectfulness and observation differ from digital evidence/organisational analytics.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
HUMAN_REVIEW_NOTES=Do not read the opening continuation on page 62 as an unconditional ban. Page 61 records competing arguments and page 62 offers a contextual choice.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T025

TASK_ID=T025
TASK_TYPE=within_document_reasoning
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=In the UNESCO ICT Competency Framework for Teachers v3 Pedagogy aspect, how do the teacher's role and proposed learning activities differ between Knowledge Acquisition and Knowledge Creation? Illustrate each level with the lesson- or project-related activities specified in the framework.
REQUIRED_DOCUMENTS_CANDIDATE=["DOC037"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC037-P0029-C001", "DOC037-P0044-C001"]
REFERENCE_ANSWER_CANDIDATE=At Knowledge Acquisition, teachers make appropriate ICT choices to support teaching/learning methodologies and students' acquisition of subject knowledge. They devise ICT-supported lesson plans, for example using tutorials, drill-and-practice or accessible multilingual digital resources; presentation software and inclusive media can support instruction. At Knowledge Creation, teachers determine learning parameters while encouraging student self-management in student-centred collaborative learning, modelling reasoning, problem solving and knowledge creation. They design collaborative research activities and help students plan projects with activities, timelines, milestones and allocated responsibilities, create digital media and reflect on learning through milestone activities such as blogs or video diaries. These are framework objectives and example activities, not observed attainment.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0029-C001
PAGE_OR_SOURCE_UNIT=physical page 29; DOC037-P0029; section Page 29
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Knowledge Acquisition Pedagogy: appropriate ICT choices, subject knowledge, ICT-supported lesson plans/tutorials/drill practice and inclusive presentation/media examples.
CHUNK_TEXT_SHA256=3839399d8d49d5b3888ad62381c0ab2f898cc363905ae42df9464c82dc3ea3a2

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0044-C001
PAGE_OR_SOURCE_UNIT=physical page 44; DOC037-P0044; section Page 44
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Knowledge Creation Pedagogy: self-management, modelling reasoning/knowledge creation, collaborative research, project planning/timelines/responsibilities and milestone reflection.
CHUNK_TEXT_SHA256=9de5f844839f781fcfba12f1f1dfae1c5de387248b935ab424c74ed9754a3777

DOCUMENT_ID=DOC037
CHUNK_ID=DOC037-P0026-C001
PAGE_OR_SOURCE_UNIT=physical page 26; DOC037-P0026; section Page 26
EVIDENCE_CLASSIFICATION=SUPPORTING
SUPPORTED_PROPOSITION=Broad pedagogy transition from traditional/didactic approaches to student-centred project/problem collaboration; does not supply both detailed sets of requested lesson/project examples.
CHUNK_TEXT_SHA256=b57c484c9dc831fb5872b436497d24d422b5ca6200e1d52179c011efe58b3e34

### Reviewer checks

QUESTION_QUALITY=PASS; a teacher-training need comparing two specified Pedagogy levels with source-specified illustrations.
TASK_TYPE_INTEGRITY=PASS; Page 29 provides Acquisition teacher choices and concrete lesson examples; page 44 provides Creation self-management and specific project-planning/reflection activities. Both are needed to complete the requested illustrated comparison.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; The detailed aspect tables support role, objectives and example activities for both levels. Page 26 supplies only a broad transition; it cannot supply the complete detailed illustrated answer.
AMBIGUITY_ASSESSMENT=Pedagogy and the two named levels bound the comparison; Knowledge Deepening and other aspects are not requested.
TEMPORAL_SCOPE=Version 3 framework objectives/examples, not a chronological observation of teacher development or measured attainment.
ACTOR_SCOPE=Teachers support students; the levels describe teacher competencies and curricular training goals, not equivalent student proficiency scores.
ACCIDENTAL_CLUE_ASSESSMENT=Level/aspect names and the request for illustrations bound evidence. No activity or evaluative conclusion is supplied in the question.
REFERENCE_ANSWER_BOUNDEDNESS=Teacher roles and illustrative lesson/project activities only; does not enumerate every objective or demand all examples.
DUPLICATION_ASSESSMENT=Low. Classroom pedagogical roles are distinct from citizen learning measurement and institutional analytics/governance.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
HUMAN_REVIEW_NOTES=A broad two-level summary would not meet this question: preserve the explicit requirement for source-specified activities. Accept equivalent supported examples within the inspected tables; do not require a verbatim list.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T026

TASK_ID=T026
TASK_TYPE=within_document_reasoning
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=What does DigCompOrg call for in assigning responsibility and reviewing a digital-capacity implementation plan, and in protecting data and planning digital-infrastructure procurement?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC040"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC040-P0024-C001", "DOC040-P0035-C001"]
REFERENCE_ANSWER_CANDIDATE=Management responsibility for delivery and monitoring of the digital-capacity implementation plan should be clearly assigned. Staffing and resources should align with organisational budgets/plans; outcomes, quality and impact should be reviewed and reported periodically, with the plan updated for organisational needs and technological/pedagogical developments. Infrastructure requires policies, procedures and safeguards for privacy, confidentiality and safe use of technologies/data, including data-protection/licensing obligations, learning-analytics policies and staff/student guidelines. Procurement should account for general and specialist requirements and use whole-of-life costing; a viable operational plan should address procurement, maintenance, interoperability and security of core ICT services. These are framework provisions, not claims about an institution implementing them.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0024-C001
PAGE_OR_SOURCE_UNIT=physical page 24; DOC040-P0024; section Page 24
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Assigned management responsibility, staffing/budget alignment, periodic review/reporting and updating the digital-capacity implementation plan.
CHUNK_TEXT_SHA256=f6e2a7b5c992a9463c3f3d28fd40737e20245683e4db6f4e23d4b77fbfc332d5

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0035-C001
PAGE_OR_SOURCE_UNIT=physical page 35; DOC040-P0035; section Page 35
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Privacy/confidentiality/safety provisions, data/licensing/learning-analytics policies, specialist procurement requirements, whole-of-life costing and core-ICT operational plan.
CHUNK_TEXT_SHA256=c08c7b347379ed74ba0091ecca1fcd022d6525a35e79595746b3441cc8b2ef7c

### Reviewer checks

QUESTION_QUALITY=PASS; an organisational planning need joining delivery/review governance and data/procurement safeguards.
TASK_TYPE_INTEGRITY=PASS; Page 24 contains plan delivery/review responsibilities; page 35 contains concrete data safeguards/procurement provisions. Neither alone covers the requested combination.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; All answer clauses are explicit in the two required passages; no unsupported causal relationship between governance and infrastructure is inferred.
AMBIGUITY_ASSESSMENT=Responsibility/review and data/procurement bound the answer; not a request for all DigCompOrg elements or an institution-specific plan.
TEMPORAL_SCOPE=Framework provisions, not evidence that any organisation has complied or a current legal advice task.
ACTOR_SCOPE=Educational organisation, management/leadership and infrastructure planning; not individual educator proficiency.
ACCIDENTAL_CLUE_ASSESSMENT=Names the areas requiring comparison but gives no responsible arrangement or safeguard.
REFERENCE_ANSWER_BOUNDEDNESS=Assigned delivery/monitoring, resources, review/update, privacy/safety and procurement/operations only.
DUPLICATION_ASSESSMENT=Minor DOC040/data-policy overlap with T028. T026 centres plan governance and infrastructure lifecycle; T028 centres analytics purposes and educator-versus-organisation responsibilities. Their complete gold requirements differ.
EVIDENCE_LOCATION_COUNT=2
SINGLE_LOCATION_COMPLETE_ANSWER=NO
WITHIN_DOCUMENT_SYNTHESIS_REQUIRED=YES
HUMAN_REVIEW_NOTES=Do not expand whole-of-life costing into numerical calculations or add obligations from current law. General outline tables lack the required review/update and costing detail.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T027

TASK_ID=T027
TASK_TYPE=cross_document_reasoning
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=How does RFCDC's conceptual account distinguish analytical from critical thinking, and what observable behaviours do its Advanced key descriptors specify for these skills?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC033", "DOC034"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC033-P0048-C001", "DOC033-P0049-C001", "DOC034-P0021-C001"]
REFERENCE_ANSWER_CANDIDATE=Volume 1 describes analytical thinking as systematically and logically analysing materials, including breaking them into elements and examining relationships, to reach defensible conclusions. Critical thinking evaluates materials and makes judgments, considering consistency with evidence, assumptions and purposes and using explicit criteria, principles or values. Volume 2's Advanced key descriptors for analytical and critical thinking specify identifying discrepancies, inconsistencies or divergences in analysed materials and using explicit, specifiable criteria, principles or values to make judgments. The conceptual distinction explains the kind of thinking; the descriptors express concrete proficiency-related behaviours rather than document identities or measured population attainment.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0048-C001
PAGE_OR_SOURCE_UNIT=physical page 48; DOC033-P0048; section Page 48
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Analytical thinking definition: systematic/logical analysis and decomposition into organised constituent elements.
CHUNK_TEXT_SHA256=561a3aa7d0fccbba01765ebcec69137c2d1acbeccf0313ea6fb5e1e7639db99e

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0049-C001
PAGE_OR_SOURCE_UNIT=physical page 49; DOC033-P0049; section Page 49
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Continues analytical relationships/conclusions and defines critical thinking as evaluation/judgment involving evidence, assumptions, purposes and explicit criteria.
CHUNK_TEXT_SHA256=f50381ccbc7567848ff58c6154b77bf0cd5e7401892cd77b76706f7c45e24bbd

DOCUMENT_ID=DOC034
CHUNK_ID=DOC034-P0021-C001
PAGE_OR_SOURCE_UNIT=physical page 21; DOC034-P0021; section Page 21
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Advanced key descriptors 68 and 69 for analytical/critical thinking: discrepancies/inconsistencies/divergences and explicit/specifiable criteria/principles/values for judgments.
CHUNK_TEXT_SHA256=d45fdba1255529234463730ca0a9669f3cfef7ac5608100ba65c27cef8c29dac

DOCUMENT_ID=DOC033
CHUNK_ID=DOC033-P0050-C001
PAGE_OR_SOURCE_UNIT=physical page 50; DOC033-P0050; section Page 50
EVIDENCE_CLASSIFICATION=SUPPORTING
SUPPORTED_PROPOSITION=Analytical and critical thinking are inherently linked; useful context but not required to answer the conceptual distinction and Advanced behaviour request.
CHUNK_TEXT_SHA256=2fe8a26822466267553642063381c38596e19b8741ef17b7a21f8e7bdcb5b977

### Reviewer checks

QUESTION_QUALITY=PASS; a substantive conceptual-to-operational mapping of thinking skills and Advanced key behaviours.
TASK_TYPE_INTEGRITY=PASS; DOC033 provides explicit conceptual definitions; DOC034 supplies the Advanced classification and two concrete key behaviours. Shared terminology does not provide the missing level-specific binding in DOC033 or the complete conceptual distinction in DOC034.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; Three required chunks from two documents cover analytical definition, critical evaluation and Advanced behaviours; the optional linkedness passage is context only.
AMBIGUITY_ASSESSMENT=Advanced modifies the key descriptors, not an education level or a claim that a learner has attained them. The task addresses RFCDC analytical/critical thinking only.
TEMPORAL_SCOPE=Frozen RFCDC concepts/descriptors, not empirical population proficiency or a live political-content judgment.
ACTOR_SCOPE=Learners/persons exercising democratic-culture competences; framework concepts are distinct from institutional policy.
ACCIDENTAL_CLUE_ASSESSMENT=Names the competence and proficiency level but gives neither conceptual distinction nor behaviours.
REFERENCE_ANSWER_BOUNDEDNESS=Two conceptual descriptions and the two Advanced key behaviours; no whole descriptor bank or evaluation of real arguments.
DUPLICATION_ASSESSMENT=Minor critical-thinking domain overlap with T023. Concept-to-Advanced-behaviour mapping is materially different from general civic-participation skills/attitudes.
SINGLE_DOCUMENT_COMPLETE_ANSWER=NO
DOCUMENT_A_NONREDUNDANT_CONTRIBUTION=Analytical thinking definition: systematic/logical analysis and decomposition into organised constituent elements.; Continues analytical relationships/conclusions and defines critical thinking as evaluation/judgment involving evidence, assumptions, purposes and explicit criteria.
DOCUMENT_B_NONREDUNDANT_CONTRIBUTION=Advanced key descriptors 68 and 69 for analytical/critical thinking: discrepancies/inconsistencies/divergences and explicit/specifiable criteria/principles/values for judgments.
CROSS_DOCUMENT_SYNTHESIS_REQUIRED=YES
HUMAN_REVIEW_NOTES=Review the distinction between prose concepts and empirically scaled descriptors. Volume 1 illustrates other competences on page 63; it does not provide these Advanced thinking key descriptors.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T028

TASK_ID=T028
TASK_TYPE=cross_document_reasoning
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=How do DigCompEdu and DigCompOrg distinguish educator-level analysis of digital evidence about learners from organisational implementation of learning analytics, in terms of purpose and responsibilities?
REQUIRED_DOCUMENTS_CANDIDATE=["DOC039", "DOC040"]
REFERENCE_EVIDENCE_CANDIDATE=["DOC039-P0064-C001", "DOC040-P0029-C001"]
REFERENCE_ANSWER_CANDIDATE=DigCompEdu asks educators to generate, select, critically analyse and interpret digital evidence of learner activity, performance and progress to inform teaching and learning. Activities include recording/comparing/synthesising progress data, considering and combining different evidence sources and critically valuing the evidence. DigCompOrg gives learning analytics strategic organisational consideration, aiming to optimise individual/group outcomes and organisational performance. Before implementation, the organisation should have a code of practice and processes for safe, secure collection, validation, storage, aggregation, analysis and reporting of student data. Analytics supports immediate personalised feedback and tutorial/remedial interventions; aggregated progress and achievement data inform quality management, course design/review and retention/outcome interventions. These are distinct framework responsibilities, not proven effects or equivalent proficiency scales.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Exact source locations

Only REQUIRED locations bind the reference-evidence candidate. Other classifications remain context, not additional mandatory gold.

DOCUMENT_ID=DOC039
CHUNK_ID=DOC039-P0064-C001
PAGE_OR_SOURCE_UNIT=physical page 64; DOC039-P0064; section Page 64
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Educator competence/activities for generating, selecting, critically interpreting digital learner evidence, combining sources and informing teaching/learning.
CHUNK_TEXT_SHA256=604ebb77dfcd483997fbb2a46e52b03ff64836d06e9999eb1401e3e76ac2170a

DOCUMENT_ID=DOC040
CHUNK_ID=DOC040-P0029-C001
PAGE_OR_SOURCE_UNIT=physical page 29; DOC040-P0029; section Page 29
EVIDENCE_CLASSIFICATION=REQUIRED
SUPPORTED_PROPOSITION=Organisational strategic purposes, pre-implementation safe-data code/processes, feedback/intervention uses and aggregate quality/course/retention uses.
CHUNK_TEXT_SHA256=24e978a160ad8c19bf02f0a1adcc54761ecc26b4bb0e2af6ccfb51af5a6c9f3b

### Reviewer checks

QUESTION_QUALITY=PASS; a substantive comparison of educator evidence interpretation and organisational analytics responsibilities.
TASK_TYPE_INTEGRITY=PASS; DOC039 contributes educator evidence interpretation and source combination; DOC040 contributes organisational strategy, pre-implementation data code/processes and aggregate quality/course uses. Neither supplies the complete other-framework account.
SOURCE_TRACEABILITY=PASS; all named chunks exist once in canonical public documents and match the audit text hashes; required bindings are unchanged.
REFERENCE_ANSWER_SUPPORT=PASS; Two coherent passages supply both named levels and their non-redundant responsibilities without outside data-governance law.
AMBIGUITY_ASSESSMENT=Educator versus organisation and evidence analysis versus analytics implementation are explicit. The task does not equate learner data with measured causality.
TEMPORAL_SCOPE=According to the frozen frameworks, not current practice or a claim of observed intervention effects.
ACTOR_SCOPE=Educator responsibility in DigCompEdu contrasted with organisation-level provision in DigCompOrg; no equivalence of proficiency schemes.
ACCIDENTAL_CLUE_ASSESSMENT=The actor levels define comparison scope but do not disclose analysis activities, data safeguards or organisational uses.
REFERENCE_ANSWER_BOUNDEDNESS=Purposes/responsibilities of the two named sections, not all assessment competences or all organisational assessment practices.
DUPLICATION_ASSESSMENT=Minor assessment domain with T024 and DOC040/privacy domain with T026; no repeated complete answer or interchangeable task requirement.
SINGLE_DOCUMENT_COMPLETE_ANSWER=NO
DOCUMENT_A_NONREDUNDANT_CONTRIBUTION=Educator competence/activities for generating, selecting, critically interpreting digital learner evidence, combining sources and informing teaching/learning.
DOCUMENT_B_NONREDUNDANT_CONTRIBUTION=Organisational strategic purposes, pre-implementation safe-data code/processes, feedback/intervention uses and aggregate quality/course/retention uses.
CROSS_DOCUMENT_SYNTHESIS_REQUIRED=YES
HUMAN_REVIEW_NOTES=The organisational code of practice is explicitly before implementation. Preserve critical evaluation of evidence at educator level; do not infer that the organisation guarantees improved outcomes.
ISSUE=NONE_REQUIRING_CANDIDATE_REVISION_IDENTIFIED; retain the documented scoring/interpretive qualifications.
SUGGESTED_CHANGE=NONE; candidate unchanged.
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION

## T029

TASK_ID=T029
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=According to the frozen UC3 corpus, what measured improvement in learners'
democratic participation was reported after educational settings implemented
RFCDC competences or descriptors?
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the reported realised improvement in learners' democratic participation after RFCDC implementation. Competence/descriptors, implementation and assessment guidance, and descriptor-validation data do not establish that participation change.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Corpus-wide absence evidence

ABSENCE_AUDIT_PATH=evidence/engineering/uc3_insufficient_evidence_absence_audit_2026-09-27.md
ABSENCE_AUDIT_SHA256=0c428e910348eb3029ad72dcc813e2f38c29ca297304e1841fbf43d5fd26d3a2
CORPUS_WIDE_ABSENCE_AUDIT=PASS
CORPUS_DOCUMENTS_AUDITED=9
CORPUS_SOURCE_UNITS_AUDITED=664
CORPUS_CHUNKS_AUDITED=850
PLAUSIBLE_NEAR_MISS_EVIDENCE=YES
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO

The source audit parses every canonical chunk, uses broad deterministic term families, inspects plausible passages and context, and classifies all 850 chunks for this question. Its complete ledger, exact regex families and document coverage remain in the hash-bound audit. Keyword zero matches are not used as an absence proof. The materially plausible findings below are copied verbatim; these audit citations are not positive reference-evidence bindings.

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

### Reviewer checks

QUESTION_QUALITY=Substantive empirical evaluation information need rather than metadata lookup; scope precision needs a researcher decision.
TASK_TYPE_INTEGRITY=PASS_WITH_PRECISION_REVIEW; the requested empirical result is unavailable corpus-wide, despite plausible near misses; final acceptance follows researcher resolution of the issue below.
SOURCE_TRACEABILITY=PASS; complete 850-chunk ledger and all near-miss citations resolve to canonical public chunks; audit hashes bind the conclusions.
REFERENCE_ANSWER_SUPPORT=PASS; the minimal answer reports corpus insufficiency, not zero improvement, zero adoption or zero effect.
AMBIGUITY_ASSESSMENT=The question leaves settings, learner population, participation measure and implementation period open. “Measured improvement” could include quantified or systematically reported qualitative change; it is not restricted to a percentage or a controlled trial. “RFCDC competences or descriptors” must not be broadened to any earlier pedagogy sharing similar competences. Strong general research summaries could tempt that unsupported attribution. The unchanged candidate should receive researcher scrutiny on this interpretation, but no alternative complete empirical answer is supported for the literal requested scope.
TEMPORAL_SCOPE=According to the frozen corpus, with implementation preceding the reported change; no current-world fact or cutoff is added. Later evidence outside the corpus is not inferred absent.
ACTOR_SCOPE=Learners in educational settings; practitioner counts, teacher training, institutional curriculum adoption and framework-development participants are different measures.
ACCIDENTAL_CLUE_ASSESSMENT=The question names an empirical information need and the framework; it does not disclose absence or instruct abstention. The frozen-corpus boundary alone is not an answer clue.
REFERENCE_ANSWER_BOUNDEDNESS=Corpus insufficiency plus a short distinction between framework/process guidance and the requested observed result; no external facts or invented values.
DUPLICATION_ASSESSMENT=Shared RFCDC domain with T024/T027 and empirical-versus-intended distinction with T021; requested realised democratic-participation change differs from assessment cautions, thinking definitions/descriptors and measurement-design advice.
CORPUS_WIDE_SUFFICIENCY=INSUFFICIENT_FOR_REQUESTED_IMPLEMENTATION_LINKED_REALIZED_IMPROVEMENT
ISSUE=The attribution boundary in 'implemented RFCDC competences or descriptors' is not operationally explicit. The corpus contains research on democratic school environments and related competences; a reader could treat those practices as implementation without an explicit RFCDC link. Population, period and the participation-change measure are also unspecified. The absence audit discloses this risk; no contrary sufficient evidence has been found.
SUGGESTED_CHANGE=Before approval, state whether explicit use of RFCDC is required and define the permitted participation-change measures and implementation/population scope. Retain qualitative measured evidence as eligible if intended. Record any researcher-selected wording as a documented pre-freeze revision; no change is applied here.
PROPOSED_REVIEW_VERDICT=REVISION_RECOMMENDED

### Hash-bound near-miss classification counts

| Primary class | Canonical chunks |
| --- | ---: |
| FRAMEWORK_DEFINITION | 117 |
| DESCRIPTOR | 37 |
| ASSESSMENT_GUIDANCE | 47 |
| IMPLEMENTATION_GUIDANCE | 96 |
| INTENDED_OUTCOME | 14 |
| EMPIRICAL_REALIZED_OUTCOME | 3 |
| OTHER_NEAR_MISS | 75 |
| IRRELEVANT | 461 |

CLASSIFICATION_TOTAL=850
Counts are primary chunk classifications, including overlapping windows, not independent studies. Three actual outcome-claim chunks concern cooperative-learning/conflict or complex-thinking outcomes rather than the requested RFCDC-linked participation change. Descriptor-validation data remain genuine empirical process evidence, not implementation improvement.

## T030

TASK_ID=T030
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=high
EXACT_LATEST_CANDIDATE_QUESTION=According to the frozen UC3 corpus, what proportion of educational
organisations implementing DigCompOrg had adopted learning-analytics
governance policies, and what measured effect did this have on learner
retention or learning outcomes?
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the proportion of DigCompOrg implementers adopting learning-analytics governance policies or the measured effect on learner retention or learning outcomes. Framework policy provisions and intended analytics uses are not observed adoption and outcome results.

ORIGINAL_AUDIT_VERDICT=READY_FOR_HUMAN_REVIEW

### Corpus-wide absence evidence

ABSENCE_AUDIT_PATH=evidence/engineering/uc3_insufficient_evidence_absence_audit_2026-09-27.md
ABSENCE_AUDIT_SHA256=0c428e910348eb3029ad72dcc813e2f38c29ca297304e1841fbf43d5fd26d3a2
CORPUS_WIDE_ABSENCE_AUDIT=PASS
CORPUS_DOCUMENTS_AUDITED=9
CORPUS_SOURCE_UNITS_AUDITED=664
CORPUS_CHUNKS_AUDITED=850
PLAUSIBLE_NEAR_MISS_EVIDENCE=YES
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO

The source audit parses every canonical chunk, uses broad deterministic term families, inspects plausible passages and context, and classifies all 850 chunks for this question. Its complete ledger, exact regex families and document coverage remain in the hash-bound audit. Keyword zero matches are not used as an absence proof. The materially plausible findings below are copied verbatim; these audit citations are not positive reference-evidence bindings.

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

### Reviewer checks

QUESTION_QUALITY=Substantive empirical evaluation information need rather than metadata lookup; scope precision needs a researcher decision.
TASK_TYPE_INTEGRITY=PASS_WITH_PRECISION_REVIEW; the requested empirical result is unavailable corpus-wide, despite plausible near misses; final acceptance follows researcher resolution of the issue below.
SOURCE_TRACEABILITY=PASS; complete 850-chunk ledger and all near-miss citations resolve to canonical public chunks; audit hashes bind the conclusions.
REFERENCE_ANSWER_SUPPORT=PASS; the minimal answer reports corpus insufficiency, not zero improvement, zero adoption or zero effect.
AMBIGUITY_ASSESSMENT=No country, sector, sampling frame, period or operational definition of adoption is specified. A proportion requires an observed implementer population and policy-adoption measure, and the outcome clause requires related measured retention/learning evidence. “Effect” is not silently strengthened to randomized causal identification; reported measured related outcomes could qualify. Even broad interpretations supply no complete frozen-corpus answer. Questionnaire participation, target coverage and student-data retention are explicitly excluded. The unchanged question remains for researcher review.
TEMPORAL_SCOPE=Frozen-document reports only. The 2015 conceptual-status statement is preserved as publication-stage evidence and is not extrapolated to a current real-world non-adoption claim.
ACTOR_SCOPE=Educational organisations implementing DigCompOrg; learners are the outcome population. Other tools, individual teachers, leaders attending courses and municipalities answering another survey are not the requested implementer population.
ACCIDENTAL_CLUE_ASSESSMENT=The question names an empirical information need and the framework; it does not disclose absence or instruct abstention. The frozen-corpus boundary alone is not an answer clue.
REFERENCE_ANSWER_BOUNDEDNESS=Corpus insufficiency plus a short distinction between framework/process guidance and the requested observed result; no external facts or invented values.
DUPLICATION_ASSESSMENT=Shared DigCompOrg analytics passages with T026/T028; the observed adoption proportion and measured outcome are unavailable empirical values, whereas those positive tasks ask for governance/infrastructure or framework responsibilities. Answers are not interchangeable.
CORPUS_WIDE_SUFFICIENCY=INSUFFICIENT_FOR_REQUESTED_ADOPTION_RATE_AND_MEASURED_EFFECT
ISSUE=The implementer population, observation period and operational definition of policy adoption are unspecified, and 'effect' may mean an observed related outcome or a causal estimate. These affect a proportion's denominator and adjudication boundaries. The absence audit still finds neither requested component for DigCompOrg; this is a question-precision issue, not new answer evidence.
SUGGESTED_CHANGE=Before approval, define the organisation/population and period scope, what constitutes learning-analytics governance-policy adoption, and whether related measured outcomes or a causal estimate are intended. Preserve the requirement for both adoption and outcome evidence. Record any researcher-selected wording as a documented pre-freeze revision; no change is applied here.
PROPOSED_REVIEW_VERDICT=REVISION_RECOMMENDED

### Hash-bound near-miss classification counts

| Primary class | Canonical chunks |
| --- | ---: |
| FRAMEWORK_PROVISION | 44 |
| ANALYTICS_POLICY_RECOMMENDATION | 1 |
| INTENDED_ANALYTICS_USE | 14 |
| IMPLEMENTATION_GUIDANCE | 4 |
| ADOPTION_RATE | 4 |
| MEASURED_OUTCOME | 0 |
| OTHER_NEAR_MISS | 98 |
| IRRELEVANT | 685 |

CLASSIFICATION_TOTAL=850
Counts are primary chunk classifications, including overlapping windows, not independent studies. Four adoption-rate chunks concern other tools, not DigCompOrg analytics-governance adoption. No requested measured effect is present. DigCompOrg not-yet-piloted status describes publication, not all later practice.

## Joint adversarial researcher review

| Control | Finding and researcher action |
| --- | --- |
| Exact questions / IDs / answers | Ten unique IDs, exact questions and full reference-answer candidates. No repeated full gold requirement. |
| Material duplication | T023/T027 share thinking concepts but differ in full civic scope versus concepts/Advanced behaviours. T024/T029 share RFCDC but differ in normative assessment versus realised participation. T026/T028/T030 share organisational/data material but differ in plan/infrastructure provisions, actor-level analytics comparison and observed adoption/effect. Domain and evidence overlap are disclosed; no complete answer substitutes for another. |
| Topic/framework concentration | All nine accepted documents contribute REQUIRED positive evidence. DOC040 contributes to T026/T028 and is central to T030 absence; RFCDC covers T024/T027/T029 across three volumes. This is a bounded concentration in distinct information needs, not repeated answer requirements; no performance-based balancing or redesign is proposed. |
| Actor ambiguity | Citizens/learners, teachers/assessors, organisations and declaring parties are distinguished. T029 population/intervention and T030 implementer denominator remain precision-review issues. |
| Competence versus right/principle | T022 is a declared rights commitment; T023/T027 concern competences/behaviours; implementation tasks describe framework provisions. None claims normative content establishes observed compliance. |
| Normative versus empirical | T029/T030 require empirical realised evidence; framework purposes, hypothetical examples, descriptors and evaluation recommendations do not fill that requirement. Genuine adjacent research and other-tool rates are preserved, not discarded as universally hypothetical. |
| Validation versus implementation | RFCDC item piloting/Rasch validation measures descriptors, not participation improvement. DigCompOrg mixed-method development is not adoption/learner-effect measurement. |
| Breadth / multiple defensible answers | T022/T023 enumerate bounded subsections. T025 permits equivalent source-specified examples and does not require every example verbatim. T024 permits contextual assessment choices rather than a categorical ban. T029/T030 need precision decisions; no automatic rewrite is made. |
| Single-location / single-document alternatives | T024 uses pages 62/69; T025 29/44; T026 24/35. Overlapping windows are not counted as distinct locations. T027 needs DOC033 concepts plus DOC034 Advanced key behaviours; T028 needs DOC039 educator analysis plus DOC040 organisation provisions. The earlier audit checks alternative summaries; no new complete single-location alternative was identified in direct verification. |
| Accidental clues | Questions contain framework/scope/level names, not answer values, chunk IDs or gold instructions. No question directs abstention. |
| Insufficient tasks too easy/trivial | They ask substantive realised evaluation questions and have substantial near misses: empirical descriptor development/research for T029 and normative analytics provisions plus actual other-tool uptake for T030. Abstention cannot be justified by absence of a keyword alone. Difficulty remains a proposed design label, not a performance result. |
| Source conflict / staleness | No conflicting proposition identified for the cited answer scopes. Framework versions/publication stages are preserved; DigCompOrg 2015 conceptual status is not extended into a present-day non-adoption claim. No corpus-wide claim that all source statements are current is made. |
| Partial evidence / scoring fairness | Empirical claims with wrong endpoints/frameworks are disclosed. T025 equivalent examples need acceptance; T029 qualitative measured change is not excluded solely for lacking a percentage; T030 requires both components and is not silently strengthened to an RCT requirement. Resolve precision issues before final gold approval. |

DUPLICATE_EXACT_QUESTIONS=0
MATERIAL_DUPLICATE_TASKS=0
REPEATED_REFERENCE_ANSWERS=0
TASK_DIVERSITY_AUDIT=PASS_WITH_DOCUMENTED_DOMAIN_OVERLAP
TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
READY_FOR_RESEARCHER_DECISION=8
REVISION_RECOMMENDED=2
REJECT_RECOMMENDED=0
SCHEMA_COMPATIBILITY_PRECHECK=PASS
SOURCE_TRACEABILITY=PASS
TASK_TYPE_INTEGRITY=PASS_WITH_T029_T030_PRECISION_REVIEW
REFERENCE_ANSWER_SUPPORT=PASS
AMBIGUITY_AUDIT=REVIEW_REQUIRED_T029_T030; positive-task qualifications retained
DUPLICATION_AUDIT=PASS
GOLD_LEAKAGE_AUDIT=PASS_FOR_CANDIDATE_QUESTION_CONTENT_AND_ARTIFACT_BOUNDARY
INSUFFICIENT_EVIDENCE_AUDIT=PASS

Schema compatibility is a field/type/binding precheck against the canonical schema identified in the candidate audit (benchmark/schema/task.schema.json; SHA256 34ddb275e659b86d759d5fabcf3500bc963c34b60425f601677b88bbb858145f). Native document/page/chunk locations can populate its evidence objects; IDs, task-type and difficulty enums, non-empty texts and document/type consistency pass. No canonical task JSON was created, no loader or workflow executed, and no task was assigned human_verified or frozen status. Full serialized validation belongs to the later explicitly approved gate.

Gold leakage review checks question content and containment of draft gold/review material in this evidence artifact. It does not claim a new runtime-isolation test. The frozen protocol requires proving runtime exclusion of gold/review/approval material before task freeze; that future gate remains pending.

## Deterministic validation and provenance

EXACT_CANDIDATE_QUESTIONS_PRESERVED=YES
EXACT_REFERENCE_ANSWER_CANDIDATES_PRESERVED=YES
POSITIVE_EVIDENCE_BINDINGS_PRESERVED=YES
T029_T030_REQUIRED_DOCUMENTS_EMPTY=YES
T029_T030_REFERENCE_EVIDENCE_EMPTY=YES
PRIOR_THREE_ARTIFACT_HASHES_UNCHANGED=YES
PROTOCOL_UNCHANGED=YES
FROZEN_SOURCE_FILES_UNCHANGED=YES
TRACKED_MODIFIED_COUNT=0
STAGED_COUNT=0
UNTRACKED_COUNT=4
DIFF_CHECK=PASS

PROTOCOL_VERSION=0.2
LLM_ASSISTED_AUTHORING=YES
FROZEN_PUBLIC_CORPUS_ONLY=YES
SENSITIVE_SOURCE_USED_FOR_TASK_CONTENT=NO
HUMAN_VERIFICATION_COMPLETED=NO
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
TASK_JSON_CREATED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO

## Researcher-Directed Pre-Freeze Precision Revisions

Date: 2026-09-27

PRE_REVISION_DOSSIER_SHA256=c509ee9639c31dab469340ae2c773cf5633b69ebd2b290711247cbb0bd29a3da
PRE_REVISION_ABSENCE_AUDIT_SHA256=0c428e910348eb3029ad72dcc813e2f38c29ca297304e1841fbf43d5fd26d3a2
REVISED_ABSENCE_AUDIT_SHA256=577031ef70ae369ee0b3b9b1291b23a8453c4f3de6e00b5b0bf265ed3b593fad
PROTOCOL_VERSION=0.2
PROTOCOL_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6

All preceding dossier bytes and historical revision recommendations are preserved. These researcher-supplied questions supersede the original T029/T030 candidates for the next decision only; they do not confer approval, human_verified or frozen status. T021–T028 are unchanged. The absence audit now appends a complete revised-question recheck of all 850 chunks, with renewed deterministic broad scans, added change/measure/governance families and explicit near-miss counterchecks.

### T029 Precision Revision 1

TASK_ID=T029
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=high
ORIGINAL_QUESTION=According to the frozen UC3 corpus, what measured improvement in learners'
democratic participation was reported after educational settings implemented
RFCDC competences or descriptors?
EXACT_LATEST_CANDIDATE_QUESTION=According to the frozen UC3 corpus, among educational settings explicitly
reported as implementing RFCDC competences or descriptors, what empirically
measured change in learners' democratic participation was reported using an
explicitly defined participation outcome measure?
REVISION_REASON=The previous wording did not sufficiently distinguish explicit RFCDC implementation from general democratic-education research, and did not require a clearly defined participation outcome measure.
ORIGINAL_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine a measured change in learners' democratic participation using an explicitly defined participation outcome measure after explicit RFCDC implementation. Descriptor-validation data and framework guidance do not establish that implementation outcome.
CORPUS_WIDE_ABSENCE_AUDIT=PASS
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
PLAUSIBLE_NEAR_MISS_EVIDENCE=YES
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO
SOURCE_TRACEABILITY=PASS; appended absence-audit recheck binds all canonical chunks and original text hashes.
REFERENCE_ANSWER_SUPPORT=PASS; only corpus insufficiency and the near-miss distinction are stated; no zero rate/change or outside-world absence is inferred.
TASK_TYPE_INTEGRITY=PASS; no complete requested empirical answer is available from any location or combination.
PRECISION_ISSUE_RESOLUTION=Explicit RFCDC-linked settings and a defined participation outcome replace the prior broader implementation/improvement wording. All directions of measured change were considered; a qualifying qualitative measure is not automatically excluded.
TEMPORAL_SCOPE=As reported in frozen documents; no current external fact or independently selected cutoff.
ACTOR_SCOPE=Learners in educational settings explicitly reported to implement RFCDC; validation practitioners and generic EDC/HRE settings are not substitute populations.
ACCIDENTAL_CLUE_ASSESSMENT=No answer value, absence conclusion or abstention instruction is supplied.
DUPLICATION_ASSESSMENT=Unchanged substantive empirical information need; distinct from normative positive-evidence tasks and from the other insufficient-evidence task.
ISSUE=NONE_REMAINING_REQUIRING_REVISION_IDENTIFIED; final researcher approval is pending.
SUGGESTED_CHANGE=NONE; exact researcher-supplied revision preserved.
REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION
T029_REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION

### T030 Precision Revision 1

TASK_ID=T030
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=high
ORIGINAL_QUESTION=According to the frozen UC3 corpus, what proportion of educational
organisations implementing DigCompOrg had adopted learning-analytics
governance policies, and what measured effect did this have on learner
retention or learning outcomes?
EXACT_LATEST_CANDIDATE_QUESTION=According to the frozen UC3 corpus, among educational organisations explicitly
reported as implementing DigCompOrg, what proportion had a documented
learning-analytics governance policy or code of practice in place, and what
empirically measured change in learner retention or learning outcomes was
reported following that implementation?
REVISION_REASON=The previous wording did not precisely define the implementer population, the adoption criterion, or the meaning of measured effect.
ORIGINAL_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
REFERENCE_ANSWER_CANDIDATE=The frozen UC3 corpus does not provide sufficient empirical evidence to determine the documented learning-analytics policy or code-of-practice adoption proportion among explicit DigCompOrg implementers, or the measured change in learner retention or learning outcomes following implementation. Framework provisions and other-tool uptake figures do not supply those results.
CORPUS_WIDE_ABSENCE_AUDIT=PASS
CORPUS_DOCUMENTS_RECHECKED=9
CORPUS_SOURCE_UNITS_RECHECKED=664
CORPUS_CHUNKS_RECHECKED=850
PLAUSIBLE_NEAR_MISS_EVIDENCE=YES
REQUESTED_EMPIRICAL_EVIDENCE_PRESENT=NO
SOURCE_TRACEABILITY=PASS; appended absence-audit recheck binds all canonical chunks and original text hashes.
REFERENCE_ANSWER_SUPPORT=PASS; only corpus insufficiency and the near-miss distinction are stated; no zero rate/change or outside-world absence is inferred.
TASK_TYPE_INTEGRITY=PASS; no complete requested empirical answer is available from any location or combination.
PRECISION_ISSUE_RESOLUTION=Explicit DigCompOrg implementers define the requested population; documented policy/code adoption and an observed denominator/rate define the first component; empirical change following implementation defines the second without adding a causal-trial requirement.
TEMPORAL_SCOPE=As reported in frozen documents; no current external fact or independently selected cutoff.
ACTOR_SCOPE=Educational organisations explicitly reported to implement DigCompOrg and their learners; other-tool users and individual educator proficiency are not substitute populations.
ACCIDENTAL_CLUE_ASSESSMENT=No answer value, absence conclusion or abstention instruction is supplied.
DUPLICATION_ASSESSMENT=Unchanged substantive empirical information need; distinct from normative positive-evidence tasks and from the other insufficient-evidence task.
ISSUE=NONE_REMAINING_REQUIRING_REVISION_IDENTIFIED; final researcher approval is pending.
SUGGESTED_CHANGE=NONE; exact researcher-supplied revision preserved.
REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION
PROPOSED_REVIEW_VERDICT=READY_FOR_RESEARCHER_DECISION
T030_REVISED_VERDICT=READY_FOR_RESEARCHER_DECISION

### Latest T021–T030 aggregate

| Task | Latest proposed review verdict |
| --- | --- |
| T021 | READY_FOR_RESEARCHER_DECISION |
| T022 | READY_FOR_RESEARCHER_DECISION |
| T023 | READY_FOR_RESEARCHER_DECISION |
| T024 | READY_FOR_RESEARCHER_DECISION |
| T025 | READY_FOR_RESEARCHER_DECISION |
| T026 | READY_FOR_RESEARCHER_DECISION |
| T027 | READY_FOR_RESEARCHER_DECISION |
| T028 | READY_FOR_RESEARCHER_DECISION |
| T029 | READY_FOR_RESEARCHER_DECISION |
| T030 | READY_FOR_RESEARCHER_DECISION |

TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
READY_FOR_RESEARCHER_DECISION=10
REVISION_RECOMMENDED=0
REJECT_RECOMMENDED=0
SCHEMA_COMPATIBILITY_PRECHECK=PASS; fields and enums remain compatible; no task JSON serialized.
SOURCE_TRACEABILITY=PASS
TASK_TYPE_INTEGRITY=PASS
REFERENCE_ANSWER_SUPPORT=PASS
AMBIGUITY_AUDIT=PASS_WITH_DOCUMENTED_REVIEW_QUALIFICATIONS; original precision recommendations resolved by these revisions.
DUPLICATION_AUDIT=PASS
GOLD_LEAKAGE_AUDIT=PASS_FOR_CANDIDATE_QUESTION_CONTENT_AND_ARTIFACT_BOUNDARY; later runtime gate remains pending.
INSUFFICIENT_EVIDENCE_AUDIT=PASS
CORPUS_CHUNKS_RECHECKED=850
RESULT_DRIVEN_REVISION=NO
HUMAN_VERIFICATION_COMPLETED=NO
TASK_JSON_CREATED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
COMMIT=NO
PUSH=NO
