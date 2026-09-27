# UC1 Full Pre-Benchmark Task-Type Integrity Audit

Date: 2026-09-27

## Guard and scope

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=76c315d814781bb91534072f2a337766b0676f46
INITIAL_WORKTREE_CLEAN=YES
INITIAL_STAGED_COUNT=0
INITIAL_UNTRACKED_COUNT=0
T008_ADJUDICATION_BINDING=PASS
T008_ADJUDICATION_SHA256=1a4a112186ed3361ac2037e82745e3260bf2b9b252e06fd051d114a894f1bb14
T008_DIAGNOSIS_SHA256=b860c551e2a8b95230a7820ded4f16222efa135c6acb9055f20e15ba7c2642f7
T008_SHA256=8ff3a00c053afb66e1b060d2a52faf65b4125fdff1b5a1d5e9d110b7a1627cb9
UC1_FREEZE_MANIFEST_SHA256=ba8e6c564d7d7c673ddbcc531bf08bb532d56e7860fd132878e61959902a90b9
UC1_ABSENCE_AUDIT_PATH=evidence/engineering/uc1_insufficient_evidence_task_audit_2026-09-12.md
UC1_ABSENCE_AUDIT_SHA256=57649311fcd8de17324779b06c223109205db7e2e21cdc81f3b38ee9e2902770

This audit identifies task-type integrity defects before any task amendment. It changes no question, answer, evidence binding, label or lifecycle status. No repair task or repair candidate is created. All ten current task hashes reproduce the original manifest bindings. T008 is valid unchanged under the explicit researcher adjudication; its source/file identities are unchanged.

## Method and interpretation

Each frozen task and every cited canonical source chunk was read directly. Neighboring/related canonical passages were inspected where needed for paragraph continuity, overlap and alternative single-location sufficiency. Parsing, native source identifiers and deterministic literal-term scans support traceability; no ranked retrieval, similarity search or model workflow was used. Two-column PDF content is interpreted by its original column/section layout rather than falsely joining horizontal lines. Source text is preserved exactly in the appendix.

Strict rules: direct retrieval permits one localized sufficient unit; within-document reasoning requires at least two materially distinct locations and fails if one cited/location-equivalent chunk contains the complete answer; cross-document reasoning requires non-redundant propositions from both documents. Adjacent overlapping chunk windows are not counted as independent locations. Numerical material-location counts describe the retained answer-support cover, not a globally unique mathematical minimum over every possible equivalent phrasing. Counts do not inflate a page into multiple locations merely because two overlapping windows cover it.

Complete-answer availability is judged against the frozen question and every material frozen gold proposition. For insufficient-evidence tasks, YES/NO concerns availability of the requested substantive observed value, not whether the benchmark gold abstention sentence exists in the task file. Their material counts are zero positive-answer locations/documents. Their historical absence-audit and review bindings are checked; no new corpus-wide absence proof is claimed here.

## Results by task

### T001

TASK_ID=T001
DECLARED_TYPE=direct_retrieval
REQUIRED_DOCUMENTS=["DOC004"]
REFERENCE_EVIDENCE_COUNT=1
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=YES
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=1
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=DOC004-P0023-C002 contains Article 5(2): 30% by 2030, 60% by 2040 and 100% by 2050 of additional surface for absent marine habitat types in groups 1–6. The same chunk contains the paragraph-3 derogation and paragraph-4 treatment of remaining surface. Paragraph-1 restoration of existing degraded habitats, in neighboring DOC004-P0023-C001, is a different denominator and does not replace this answer.

EXACT_FROZEN_QUESTION=For marine habitat types in Annex II groups 1 to 6 that do not occur in an area, what staged coverage of the additional surface needed to reach the favourable reference area must restoration measures achieve by 2030, 2040, and 2050?
EXACT_FROZEN_REFERENCE_ANSWER=The restoration measures must cover at least 30% of the additional surface needed to reach the favourable reference area by 2030, at least 60% by 2040, and 100% by 2050, subject to the Regulation's stated derogation mechanism.
TASK_SHA256=6f6bd0a21c6998bdc953a535dc327f750602ac139ae492f69e43fe90ce5c941a
REFERENCE_EVIDENCE=[{"document_id": "DOC004", "page": 23, "section": null, "chunk_id": "DOC004-P0023-C002"}]

DOCUMENT_ID=DOC004
CHUNK_ID=DOC004-P0023-C002
PAGE_OR_SOURCE_UNIT=PDF page 23; DOC004-P0023; Page 23
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Entire staged additional-surface requirement and derogation qualification in one localized chunk.

### T002

TASK_ID=T002
DECLARED_TYPE=direct_retrieval
REQUIRED_DOCUMENTS=["DOC005"]
REFERENCE_EVIDENCE_COUNT=1
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=YES
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=1
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=DOC005-P0018-C001 Article 4(2) contains every gold proposition: submit the due diligence statement before market placement/export, make it available to competent authorities through the information system, include Annex II information and declare exercised due diligence and no/negligible risk. The neighboring operator/SME/trader provisions do not add a required answer element.

EXACT_FROZEN_QUESTION=What must an operator do before placing a relevant product on the EU market or exporting it after due diligence concludes that the product complies with Article 3?
EXACT_FROZEN_REFERENCE_ANSWER=Before placing the product on the market or exporting it, the operator must make a due diligence statement available to the competent authorities through the information system. The statement must contain the required information and declare that due diligence was exercised and that no or only a negligible risk was found.
TASK_SHA256=70df44f45004610ec0f3882f4382ae7c5851786dea3cad8282e400d1af4a1837
REFERENCE_EVIDENCE=[{"document_id": "DOC005", "page": 18, "section": null, "chunk_id": "DOC005-P0018-C001"}]

DOCUMENT_ID=DOC005
CHUNK_ID=DOC005-P0018-C001
PAGE_OR_SOURCE_UNIT=PDF page 18; DOC005-P0018; Page 18
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Timing, submission channel, required contents and risk declaration together.

### T003

TASK_ID=T003
DECLARED_TYPE=direct_retrieval
REQUIRED_DOCUMENTS=["DOC020"]
REFERENCE_EVIDENCE_COUNT=1
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=YES
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=1
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=DOC020-P0009-C001 expressly states six interlinked thematic priority objectives through 31 December 2030 and enumerates them. The requested count and timeframe are localized. This conclusion concerns the declared direct-retrieval type; it does not independently amend historical task-quality policy.

EXACT_FROZEN_QUESTION=How many interlinked thematic priority objectives does the 8th Environment Action Programme establish for the period up to 31 December 2030?
EXACT_FROZEN_REFERENCE_ANSWER=The 8th Environment Action Programme establishes six interlinked thematic priority objectives for the period up to 31 December 2030.
TASK_SHA256=6ca0a20f8736e9524004deaedbb3c08a3f6fc125bea79a252d85158b87cdcd87
REFERENCE_EVIDENCE=[{"document_id": "DOC020", "page": 9, "section": null, "chunk_id": "DOC020-P0009-C001"}]

DOCUMENT_ID=DOC020
CHUNK_ID=DOC020-P0009-C001
PAGE_OR_SOURCE_UNIT=PDF page 9; DOC020-P0009; Page 9
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Explicit count of six and endpoint of 31 December 2030.

### T004

TASK_ID=T004
DECLARED_TYPE=within_document_reasoning
REQUIRED_DOCUMENTS=["DOC001"]
REFERENCE_EVIDENCE_COUNT=2
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=2
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=The complete frozen gold combines the overarching protection/restoration, sustainable management, monitoring and effective decentralised planning account in DOC001-P0004-C001 with the specific management instruments in DOC001-P0019-C002. Page 4 does not state the additional indicators/thresholds and specific closer-to-nature/biodiversity-friendly guidance package; page 19 does not contain the full general monitoring/decentralised-planning account. Neighboring DOC001-P0019-C001 starts the restoration item and overlaps items 2–3, but does not contain the whole answer. DOC001 pages 14–16 and 20 provide alternative detail on parts of the package, not a single complete cited/location-equivalent unit. Broad protection/management overlap is not complete gold coverage.

EXACT_FROZEN_QUESTION=How does the New EU Forest Strategy for 2030 combine forest protection and forest management measures to improve resilience and biodiversity?
EXACT_FROZEN_REFERENCE_ANSWER=The Strategy combines stronger forest protection and restoration with sustainable forest management, monitoring, and planning intended to create resilient forest ecosystems. It also calls for strict protection of primary and old-growth forests, additional indicators and thresholds for sustainable forest management, guidance for closer-to-nature forestry, biodiversity-friendly afforestation and reforestation, and knowledge exchange on climate adaptation and resilience.
TASK_SHA256=704fff83f51729448a0d7075daf5b5570d960cb3be07d125353ecf2300e30340
REFERENCE_EVIDENCE=[{"document_id": "DOC001", "page": 4, "section": null, "chunk_id": "DOC001-P0004-C001"}, {"document_id": "DOC001", "page": 19, "section": null, "chunk_id": "DOC001-P0019-C002"}]

DOCUMENT_ID=DOC001
CHUNK_ID=DOC001-P0004-C001
PAGE_OR_SOURCE_UNIT=PDF page 4; DOC001-P0004; Page 4
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant overarching combination: forest protection/restoration plus sustainable management, monitoring and effective decentralised planning for resilience.

DOCUMENT_ID=DOC001
CHUNK_ID=DOC001-P0019-C002
PAGE_OR_SOURCE_UNIT=PDF page 19; DOC001-P0019; Page 19
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant specific package: strict primary/old-growth protection, additional sustainable-management indicators/thresholds, closer-to-nature guidance, biodiversity-friendly afforestation/reforestation and adaptation/resilience knowledge exchange.

### T005

TASK_ID=T005
DECLARED_TYPE=within_document_reasoning
REQUIRED_DOCUMENTS=["DOC010"]
REFERENCE_EVIDENCE_COUNT=2
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=YES
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=1
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=NO
DEFECT_TYPE=within_document_source_redundancy
EVIDENCE_JUSTIFICATION=DOC010-P0155-C001 alone contains the complete frozen answer. Its left column, section 4.4.1, gives slow growth at northern latitudes, few measurable effects by 2030, starting measures now for 2030–2050, declining removals without new/strengthened measures and expected reversal through strengthening measures. Its right column, section 4.4.2, identifies all three existing grant schemes: higher planting densities after harvesting, forest tree breeding and targeted fertilisation. Although this chunk spans two subsection headings and PDF columns, the strict criterion explicitly excludes a within-document task whose complete answer is in one canonical chunk. DOC010-P0162-C001 corroborates declining removals, the same grants and scaling-up expectations; its extra historical counts, diagram and research detail are not required by the frozen question or gold. It does not add a materially necessary proposition.

EXACT_FROZEN_QUESTION=Why does Norway's Climate Action Plan argue that forest mitigation must include both near-term and long-term measures, and which existing measures are highlighted for increasing forest removals?
EXACT_FROZEN_REFERENCE_ANSWER=The Plan explains that forests at high northerly latitudes grow slowly, so relatively few measures can produce measurable effects by 2030, while measures started now can have important effects from 2030 to 2050. It also notes that net forest removals have been declining and are expected to continue declining without stronger measures. Existing measures highlighted for increasing removals include grants for higher planting densities after harvesting, forest tree breeding, and targeted forest fertilisation. Scaling up forest mitigation measures is expected to help reverse the declining trend in removals.
TASK_SHA256=f2fb453ff006208b4b8384f78ece3f63e09c4e8ba48c0533d2ea4997e3885c23
REFERENCE_EVIDENCE=[{"document_id": "DOC010", "page": 155, "section": null, "chunk_id": "DOC010-P0155-C001"}, {"document_id": "DOC010", "page": 162, "section": null, "chunk_id": "DOC010-P0162-C001"}]

DOCUMENT_ID=DOC010
CHUNK_ID=DOC010-P0155-C001
PAGE_OR_SOURCE_UNIT=PDF page 155; DOC010-P0155; Page 155
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Complete gold: time-horizon rationale, decline, all three grant measures and expected reversal.

DOCUMENT_ID=DOC010
CHUNK_ID=DOC010-P0162-C001
PAGE_OR_SOURCE_UNIT=PDF page 162; DOC010-P0162; Page 162
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=SUPPORTING
SUPPORTED_PROPOSITION=Corroborative decline, measures and expected reversal; extra numerical/research details are not requested gold requirements.

DOC010-P0155-C001_COMPLETE_GOLD=YES
DOC010-P0162-C001_MATERIALLY_NECESSARY=NO
REPAIR_APPLIED=NO

The defect is in the declared multi-location necessity, not factual falsity of the source-supported gold. The two subsection headings within page 155 cannot rescue the label under the strict single-chunk exclusion. Reclassification or question redesign would require a separate researcher-directed amendment; neither is applied.

### T006

TASK_ID=T006
DECLARED_TYPE=within_document_reasoning
REQUIRED_DOCUMENTS=["DOC025"]
REFERENCE_EVIDENCE_COUNT=3
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=YES
MATERIAL_LOCATION_COUNT=3
MATERIAL_DOCUMENT_COUNT=1
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=The cited locations have distinct substantive roles. DOC025-P0011-C001 recitals 62–65 establish voluntariness and environmental/climate ambition beyond conditionality; they describe payment purposes but omit the complete annual-eligible-hectares rule. DOC025-P0041-C001 Article 31(5) supplies the specific statutory/GAEC/other mandatory-baseline requirements. DOC025-P0042-C001 Article 31(7) supplies annual eligible-hectare payment, additional-income-support versus costs/income-foregone compensation, and potential transaction costs. No cited chunk contains all three. Neighboring DOC025-P0040-C002 supports voluntariness/beneficial commitments, and DOC025-P0041-C002 repeats baseline provisions; neither supplies the payment rule. The adjacent Article 31 paragraphs are different substantive requirements, not duplicate overlapping windows of one statement.

EXACT_FROZEN_QUESTION=How are CAP eco-schemes designed to add environmental and climate ambition beyond baseline conditionality, and how may participating farmers be paid?
EXACT_FROZEN_REFERENCE_ANSWER=Eco-schemes are voluntary schemes for farmers that support practices beneficial to the climate, environment, animal welfare, or antimicrobial-resistance objectives. Their commitments must go beyond relevant statutory management requirements, GAEC standards, and other applicable minimum or mandatory requirements. Support is provided as an annual payment for eligible hectares, either as a payment additional to basic income support or as compensation for all or part of the additional costs and income foregone from the commitments, with transaction costs also potentially covered.
TASK_SHA256=aec0964d32042a8107a0d57aab3bd7871b710e58f48c0df6f2b3e301d692e340
REFERENCE_EVIDENCE=[{"document_id": "DOC025", "page": 11, "section": null, "chunk_id": "DOC025-P0011-C001"}, {"document_id": "DOC025", "page": 41, "section": null, "chunk_id": "DOC025-P0041-C001"}, {"document_id": "DOC025", "page": 42, "section": null, "chunk_id": "DOC025-P0042-C001"}]

DOCUMENT_ID=DOC025
CHUNK_ID=DOC025-P0011-C001
PAGE_OR_SOURCE_UNIT=PDF page 11; DOC025-P0011; Page 11
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant cited-source contribution: schemes voluntary for farmers and intended to enhance environmental/climate performance beyond conditionality.

DOCUMENT_ID=DOC025
CHUNK_ID=DOC025-P0041-C001
PAGE_OR_SOURCE_UNIT=PDF page 41; DOC025-P0041; Page 41
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant specific commitments must exceed statutory management requirements, GAEC and other applicable minimum/mandatory requirements.

DOCUMENT_ID=DOC025
CHUNK_ID=DOC025-P0042-C001
PAGE_OR_SOURCE_UNIT=PDF page 42; DOC025-P0042; Page 42
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant annual eligible-hectare payment and payment alternatives, including possible transaction-cost coverage.

### T007

TASK_ID=T007
DECLARED_TYPE=cross_document_reasoning
REQUIRED_DOCUMENTS=["DOC006", "DOC007"]
REFERENCE_EVIDENCE_COUNT=3
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=NO
MATERIAL_LOCATION_COUNT=3
MATERIAL_DOCUMENT_COUNT=2
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=DOC006-P0008-C002 explicitly establishes the original no-debit commitment for BOTH 2021–2025 and 2026–2030. DOC007-P0012-C001 supplies revised flexibilities tied to 2026–2030 targets/budgets; DOC007-P0014-C002 refers to the Union 310-million-tonne 2030 target and the new compensation/compliance mechanism against targets/budgets. Necessary neighboring context DOC007-P0009-C001/C002 spells out replacement Article 4 target/budget rules, and DOC007-P0014-C001 starts the inserted Article 13b mechanism. DOC007 restates the no-debit rule for 2021–2025, but does not thereby reproduce the original rule for BOTH periods. Its recitals on revised accounting/targets likewise do not establish that exact earlier two-period commitment. DOC006 cannot supply the subsequently introduced target/budget/land-use provisions. Neither document alone supplies every material gold proposition.

EXACT_FROZEN_QUESTION=How did the 2023 amendment change the LULUCF framework for 2026-2030 compared with the commitment in the 2018 framework?
EXACT_FROZEN_REFERENCE_ANSWER=The 2018 framework required each Member State to ensure that accounted LULUCF emissions did not exceed removals for 2021-2025 and 2026-2030. The 2023 amendment introduced a more explicitly quantified target and budget framework for 2026-2030 and tied it to a Union target of 310 million tonnes of CO2-equivalent net removals in 2030, together with updated flexibilities and a land-use mechanism for compliance with Member State targets or budgets.
TASK_SHA256=e8f784adfc8f0b24fb6b98ac85d44eb30ab8356fcb01da78e6d50a8fa3c2fa0d
REFERENCE_EVIDENCE=[{"document_id": "DOC006", "page": 8, "section": null, "chunk_id": "DOC006-P0008-C002"}, {"document_id": "DOC007", "page": 12, "section": null, "chunk_id": "DOC007-P0012-C001"}, {"document_id": "DOC007", "page": 14, "section": null, "chunk_id": "DOC007-P0014-C002"}]

DOCUMENT_ID=DOC006
CHUNK_ID=DOC006-P0008-C002
PAGE_OR_SOURCE_UNIT=PDF page 8; DOC006-P0008; Page 8
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant DOC006 contribution: original accounted emissions cannot exceed removals in both 2021–2025 AND 2026–2030.

DOCUMENT_ID=DOC007
CHUNK_ID=DOC007-P0012-C001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC007-P0012; Page 12
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant DOC007 contribution: updated general flexibility/compliance provisions referring to the 2026–2030 target/budget framework.

DOCUMENT_ID=DOC007
CHUNK_ID=DOC007-P0014-C002
PAGE_OR_SOURCE_UNIT=PDF page 14; DOC007-P0014; Page 14
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant DOC007 contribution: 310 million tonnes CO2-equivalent Union target and land-use compensation/compliance provisions; read with the mechanism start in neighboring C001.

### T008

TASK_ID=T008
DECLARED_TYPE=cross_document_reasoning
REQUIRED_DOCUMENTS=["DOC001", "DOC003"]
REFERENCE_EVIDENCE_COUNT=4
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=NO
MATERIAL_LOCATION_COUNT=3
MATERIAL_DOCUMENT_COUNT=2
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=The unchanged task is governed by explicit researcher adjudication APPROVE UC1 T008 AS VALID UNCHANGED. DOC003-P0005-C001 uniquely supplies the substantive at-least-one-third-of-protected-areas strict-protection commitment in the frozen gold. DOC001 repeats headline 30%/10% land targets, not that proportional commitment. DOC001-P0012-C001/C002 supplies the Forest Strategy definition/mapping/monitoring/regime and interim no-deterioration provisions; DOC001-P0019-C002 supplies the guideline/action package. The two page-12 windows are treated as one location-equivalent page passage, not two independent locations merely because they overlap. The full gold materially requires both documents. The adjudicated broad-wording risk is preserved and not reopened as a redundancy defect.

EXACT_FROZEN_QUESTION=How does the New EU Forest Strategy for 2030 translate the EU Biodiversity Strategy's protection ambition for primary and old-growth forests into forest-policy actions?
EXACT_FROZEN_REFERENCE_ANSWER=The Biodiversity Strategy calls for at least 30% of EU land to be protected and for at least one third of protected areas, representing 10% of EU land, to be strictly protected, including all remaining primary and old-growth forests. The Forest Strategy carries this ambition into forest policy by calling for strict protection of primary and old-growth forests and by calling for their definition, mapping, monitoring, and protection regime, together with guidance and implementation measures intended to prevent deterioration and strengthen forest protection and restoration.
TASK_SHA256=8ff3a00c053afb66e1b060d2a52faf65b4125fdff1b5a1d5e9d110b7a1627cb9
REFERENCE_EVIDENCE=[{"document_id": "DOC003", "page": 5, "section": null, "chunk_id": "DOC003-P0005-C001"}, {"document_id": "DOC001", "page": 12, "section": null, "chunk_id": "DOC001-P0012-C001"}, {"document_id": "DOC001", "page": 12, "section": null, "chunk_id": "DOC001-P0012-C002"}, {"document_id": "DOC001", "page": 19, "section": null, "chunk_id": "DOC001-P0019-C002"}]

DOCUMENT_ID=DOC003
CHUNK_ID=DOC003-P0005-C001
PAGE_OR_SOURCE_UNIT=PDF page 5; DOC003-P0005; Page 5
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant DOC003 contribution: explicitly at least one third of protected areas should be strictly protected.

DOCUMENT_ID=DOC001
CHUNK_ID=DOC001-P0012-C001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012; Page 12
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=DOC001 Forest Strategy-specific protection/regime and mapping account; shares a page passage with C002.

DOCUMENT_ID=DOC001
CHUNK_ID=DOC001-P0012-C002
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012; Page 12
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=Non-redundant DOC001 implementation detail: common definition/regime, urgent mapping/monitoring and avoiding deterioration pending protection.

DOCUMENT_ID=DOC001
CHUNK_ID=DOC001-P0019-C002
PAGE_OR_SOURCE_UNIT=PDF page 19; DOC001-P0019; Page 19
EVIDENCE_CLASSIFICATION_FOR_THIS_AUDIT=REQUIRED
SUPPORTED_PROPOSITION=DOC001 specific forest guideline/implementation package; separate from page 12.

### T009

TASK_ID=T009
DECLARED_TYPE=insufficient_evidence
REQUIRED_DOCUMENTS=[]
REFERENCE_EVIDENCE_COUNT=0
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=NO
MATERIAL_LOCATION_COUNT=0
MATERIAL_DOCUMENT_COUNT=0
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=The existing corpus-wide absence audit, bound by the original UC1 manifest, records 30 retrieval-active documents and 2853 frozen chunks; it found no sufficient actual additional-tree planting count at 31 December 2025. The pledge, 2030 target and counting/monitoring arrangements are near misses, not a realised end-2025 value. required_documents and reference_evidence remain empty. This step confirms the historical absence-audit binding and intended abstention; it does not redo an absence audit or assert absence outside the frozen corpus.

EXACT_FROZEN_QUESTION=As of 31 December 2025, how many additional trees had actually been planted toward the EU pledge to plant at least 3 billion additional trees by 2030?
EXACT_FROZEN_REFERENCE_ANSWER=The frozen UC1 corpus does not provide sufficient evidence to determine how many of the pledged additional trees had actually been planted by 31 December 2025. A substantive numerical answer should therefore not be given.
TASK_SHA256=a1f7bc496bf1f83b267e3e513b52d8fbf0437fae4f10f3e4d3f7aa896e78612a
REFERENCE_EVIDENCE=[]

CORPUS_WIDE_ABSENCE_AUDIT_BINDING=PASS
ABSENCE_AUDIT_REPEATED=NO
POSITIVE_EVIDENCE_BINDING=NONE

### T010

TASK_ID=T010
DECLARED_TYPE=insufficient_evidence
REQUIRED_DOCUMENTS=[]
REFERENCE_EVIDENCE_COUNT=0
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_CHUNK=NO
COMPLETE_ANSWER_AVAILABLE_FROM_SINGLE_DOCUMENT=NO
MATERIAL_LOCATION_COUNT=0
MATERIAL_DOCUMENT_COUNT=0
DECLARED_TYPE_VALID=YES
DEFECT_TYPE=NONE
EVIDENCE_JUSTIFICATION=The same cryptographically bound corpus-wide absence audit found no explicit actual strict-protection percentage for 31 December 2025. Earlier baseline and 2030 target are not the requested observed end-2025 value. required_documents and reference_evidence remain empty. The human-reviewed terminology change to strict protection in the question and the retained strict-legal-protection phrase in gold are preserved as historical wording; no historical content is normalised. This step confirms the absence-audit binding rather than re-running retrieval or claiming an outside-world absence.

EXACT_FROZEN_QUESTION=As of 31 December 2025, what percentage of EU land was actually under strict protection?
EXACT_FROZEN_REFERENCE_ANSWER=The frozen UC1 corpus does not provide sufficient evidence to determine the percentage of EU land that was actually under strict legal protection as of 31 December 2025. A substantive numerical answer should therefore not be given.
TASK_SHA256=7aa9d9c5ee24678b41ba6361f3c80d39c7cc5a5bd2798cb8417136c0c0cf976b
REFERENCE_EVIDENCE=[]

CORPUS_WIDE_ABSENCE_AUDIT_BINDING=PASS
ABSENCE_AUDIT_REPEATED=NO
POSITIVE_EVIDENCE_BINDING=NONE

## UC1-wide result

UC1_TOTAL_TASKS=10
UC1_VALID_TASKS=9
UC1_DEFECTIVE_TASKS=1
UC1_DEFECT_IDS=T005
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
ALLOCATION_CHANGED=NO
T008_ADJUDICATION_BINDING=PASS
T008_VALID_UNCHANGED=YES

The declared allocation remains frozen and unchanged. This audit does not silently count T005 as direct retrieval or substitute a new design. The other nine declared types pass the strict material-necessity assessment. T004 and T008 share forest-policy facts, but their complete gold requirements differ; that overlap is not a reason to reopen the adjudicated T008 type. Historical quality/wording limitations remain distinct from this structural task-type result.

## Context locations inspected for interpretation

DOC004-P0023-C001 | PDF page 23 | text SHA256=ffa0aa53c7ca825a8f25d2aba4d5c8c646df7748c2ba62c160b20c1680e6bb72
DOC005-P0017-C001 | PDF page 17 | text SHA256=b791a8f2132cee04a8ca196e211bad110ba09cfcf8c7a0ccf86bca3cb1e184d1
DOC005-P0018-C002 | PDF page 18 | text SHA256=2cb7d1e37a9346a48b08b599919412e8bed122f5def660bbd89e4e0979d9ebfa
DOC001-P0019-C001 | PDF page 19 | text SHA256=ea2848e46221b73ce13f5a634015223974d1f91a35d7d2c8ef6d8f08cbfa3e94
DOC001-P0014-C001 | PDF page 14 | text SHA256=43a400448fc55267de9d9c3f5aff0351144b7fa634482dc7956cb1a94ea00800
DOC001-P0014-C002 | PDF page 14 | text SHA256=9beebb997483fd15c5af166e227fe2645aa42c9985f6e638b859ee018357f40e
DOC001-P0015-C001 | PDF page 15 | text SHA256=79a51f98e63809155567e300a74c005b84994fb73d40690126248eee5eaaf514
DOC001-P0015-C002 | PDF page 15 | text SHA256=0d6ea6b1e9d622e194b03edba22d0c770adc75707baaa26f319c8e9606d234c8
DOC001-P0016-C001 | PDF page 16 | text SHA256=f6b723c35f0a2783c0ed0db4b561c04bede3036eaacb469ab624230cd03af0e3
DOC001-P0020-C001 | PDF page 20 | text SHA256=e3356010f2d62782c39ec0c70cd30d162c824b178f8417d0d597c8edf380b6d9
DOC025-P0040-C002 | PDF page 40 | text SHA256=2b5d4ea4aea307b5457f6e43238ba035f19a71b9057a6db1096b14a8d9a29b8b
DOC025-P0041-C002 | PDF page 41 | text SHA256=05f3c29c3eb226ce377d45be7d2d2ef6517c9df687eecdf62e2c72e779123c0e
DOC007-P0003-C001 | PDF page 3 | text SHA256=ae87eafb57c4c481e22426ee812c2b22a10270b54203dda9b242349959bfd65d
DOC007-P0003-C002 | PDF page 3 | text SHA256=5cdfbdd058e4ab6e0dfc51d40431fa5f9bf8c9f9873097c3abf54452bf1c151f
DOC007-P0009-C001 | PDF page 9 | text SHA256=f7f18e53fefffbc46f73e57ba8ed547383d9b24c3fbf76ffab29459b65d8e8e0
DOC007-P0009-C002 | PDF page 9 | text SHA256=ee454ede3f04e36549741332b4f55febd3f3fa3fc717e461094e7b05a5ec4165
DOC007-P0014-C001 | PDF page 14 | text SHA256=056360951ead27b7f39878ca6116ac218f769a37cf75accadacd42791bfa5c5a
DOC010-P0155-C002 | PDF page 155 | text SHA256=05d626ded7691eb3f4cab3814bb0fbfd77cfe1cbd8b677d163a8ff0d9c8cef8c
DOC003-P0005-C002 | PDF page 5 | text SHA256=b5d5c838fa540bfc6be86467f8d8214894ffff31163724258640f4db030ce0f1
DOC003-P0006-C001 | PDF page 6 | text SHA256=60de4f4dd7fb6fb1fc441cdc7ec989b787f6893ed3fe186489a2f512fd55a7ba

These are inspection context, not additions to frozen task reference_evidence. T007’s Article 4 replacement and Article 13b start provide particularly useful context for the target/budget and land-use-mechanism references in the current cited chunks.

## Immutable input identities

benchmark/tasks/UC1/T001.json SHA256=6f6bd0a21c6998bdc953a535dc327f750602ac139ae492f69e43fe90ce5c941a
benchmark/tasks/UC1/T002.json SHA256=70df44f45004610ec0f3882f4382ae7c5851786dea3cad8282e400d1af4a1837
benchmark/tasks/UC1/T003.json SHA256=6ca0a20f8736e9524004deaedbb3c08a3f6fc125bea79a252d85158b87cdcd87
benchmark/tasks/UC1/T004.json SHA256=704fff83f51729448a0d7075daf5b5570d960cb3be07d125353ecf2300e30340
benchmark/tasks/UC1/T005.json SHA256=f2fb453ff006208b4b8384f78ece3f63e09c4e8ba48c0533d2ea4997e3885c23
benchmark/tasks/UC1/T006.json SHA256=aec0964d32042a8107a0d57aab3bd7871b710e58f48c0df6f2b3e301d692e340
benchmark/tasks/UC1/T007.json SHA256=e8f784adfc8f0b24fb6b98ac85d44eb30ab8356fcb01da78e6d50a8fa3c2fa0d
benchmark/tasks/UC1/T008.json SHA256=8ff3a00c053afb66e1b060d2a52faf65b4125fdff1b5a1d5e9d110b7a1627cb9
benchmark/tasks/UC1/T009.json SHA256=a1f7bc496bf1f83b267e3e513b52d8fbf0437fae4f10f3e4d3f7aa896e78612a
benchmark/tasks/UC1/T010.json SHA256=7aa9d9c5ee24678b41ba6361f3c80d39c7cc5a5bd2798cb8417136c0c0cf976b
benchmark/tasks/UC1/freeze_manifest.json SHA256=ba8e6c564d7d7c673ddbcc531bf08bb532d56e7860fd132878e61959902a90b9
evidence/engineering/uc1_t008_prebenchmark_defect_repair_proposal_2026-09-27.md SHA256=b860c551e2a8b95230a7820ded4f16222efa135c6acb9055f20e15ba7c2642f7
evidence/engineering/uc1_t008_prebenchmark_adjudication_2026-09-27.md SHA256=1a4a112186ed3361ac2037e82745e3260bf2b9b252e06fd051d114a894f1bb14
evidence/engineering/uc1_insufficient_evidence_task_audit_2026-09-12.md SHA256=57649311fcd8de17324779b06c223109205db7e2e21cdc81f3b38ee9e2902770
evidence/engineering/uc1_task_human_review_2026-09-12.md SHA256=9c17034676073667f93c209172586b9bb9505953a83120f3fff96cee1914010e
evidence/engineering/uc1_task_freeze_2026-09-12.md SHA256=a7f80e0cbb7a57f53ced596c7a29a234fb5f6c2d0dc3d05e83c964ec5c79bbf2
benchmark/task_set_plan.json SHA256=137bcef783e124e3410301f1fc89bead7f375b6b8bad94f3a0f0c04c1cce1958
corpus/use_cases/UC1/processed/chunks/DOC001.chunks.json SHA256=ce006c22d36843643cf6e001caa48c7669af141ae23fe472da2016b33821bb42
corpus/use_cases/UC1/processed/chunks/DOC003.chunks.json SHA256=2001f30f7503e090d0d32790fb155b8504865c3414416d11f264ede21f9d9f03
corpus/use_cases/UC1/processed/chunks/DOC004.chunks.json SHA256=229dab55798b4dd1323af88189b112fb11728638776c876962813c08484d7a0a
corpus/use_cases/UC1/processed/chunks/DOC005.chunks.json SHA256=0110a1dcf6090e64917d9c0a3ab8270db0872b582b5200bdc2f07dfbe2eb76d6
corpus/use_cases/UC1/processed/chunks/DOC006.chunks.json SHA256=550af6426cf55e353138349d29417f543c3ede3833f1a874e08457c2f40b2c68
corpus/use_cases/UC1/processed/chunks/DOC007.chunks.json SHA256=2e7c276f5f5852d6ef29e0b3c5265c70218cc16f64aac6a64d8d56a7fa9528f6
corpus/use_cases/UC1/processed/chunks/DOC010.chunks.json SHA256=ef5e8ae60c11421479fa1138dd0d6ef11ee6253171887ec84b18caf345d5422c
corpus/use_cases/UC1/processed/chunks/DOC020.chunks.json SHA256=c451bbc189a5e735e8cc7a1c12f1f7b5437935e69f6eae97a49ddc46054177ce
corpus/use_cases/UC1/processed/chunks/DOC025.chunks.json SHA256=72f48c3055622c6ae4736f0dc160105ff774d98083a6c6aa979cd587322dc2b8

## Complete cited-source appendix

Every currently cited UC1 chunk appears once below in chunk-ID order, including the corroborative T005 page-162 chunk. Empty evidence arrays for T009/T010 remain empty.

### DOC001-P0004-C001

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 4; DOC001-P0004
CHUNK_TEXT_SHA256=17b1179311ad48e1b21e66149a319edba1156fcd22e530327b2ba21bf1a5cf92

```text
The EU Forest Strategy is written at the onset of rapidly accelerating climate and biodiversity
crises. The next decade is crucial and the Strategy therefore presents a concrete plan for 2030,
combining regulatory, financial and voluntary measures.

It includes measures for strengthening forest protection and restoration, enhancing sustainable
forest management, and improving the monitoring and effective decentralised planning on forests
in the EU with a view to ensuring resilient forest ecosystems and enabling forests to deliver on
their multifunctional role. To further support sustainable forest-based bioeconomy for a climate
neutral future, the strategy proposes measures for innovation and promotion of new materials and
products to replace fossil-based counterparts as well as for boosting the non-wood forest
economy, including ecotourism. The Strategy also focuses on sustainable re- and afforestation and
is accompanied by a roadmap for planting at least 3 billion additional trees in the EU by 2030.

With this strategy, the Commission is presenting an ambitious vision, building on the strong
engagement, motivation and dedication of all forest and land owners and managers. Their role in
the provisions of ecosystem services is key and needs to be supported. The Strategy seeks to
develop, among other things, financial incentives, in particular for private forest owners and
managers, for the provision of these ecosystem services.

All the measures are to be designed and implemented in close cooperation with the Member
States as well as public and private forest owners and other caretakers of forests, as they are the
enablers of the necessary changes and of a vibrant and sustainable forest-based bioeconomy in the
EU. The Strategy seeks the active engagement of all relevant actors and levels of governance,
from Member States to forest owners and managers, forest-based industries, scientists, civil
society and other stakeholders.

While the Strategy is focussed only on EU forests and aims to make an important contribution
from the EU to the UN 2030 Sustainable Development Goals, in particular the Goal 1514, it
recognises that forest-related challenges are inherently global and that forest area continues a
deeply worrying decrease by an average of 4.7 million hectares per year, with deforestation
occurring at a rate of 10 million hectares per year15. The Commission reaffirms its full
commitment to deliver on its 2019 Communication to Protect and Restore the World’s Forests 16,
including by working in close partnership with its global partners on forest protection, restoration
and sustainable forest management, as well as adopting a legislative proposal to ensure that
products, whether sourced in the EU or from third countries, sold on the EU market do not
contribute to global deforestation. EU cooperation will promote integrated approaches towards
forests that address governance, sustainability and legality of value chains, biodiversity and
livelihoods
```

### DOC001-P0012-C001

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012
CHUNK_TEXT_SHA256=b2f5ea66f12be368c97ca3affd8a3b082bbf796de171d8cdb646ce736dbd4c12

```text
transition. According to the World Economic Forum, the conservation, restoration and
sustainable management of forests could generate EUR 190 billion in business opportunities and
16 million jobs worldwide by 203039.

In addition, we need robust approaches to risk reduction in the context of significant uncertainty
related to future forests. The onset of climate change means forest change. Europe’s vegetation
zones have started to shift upwards and northwards, triggering the transformation of forest
ecosystems in most places. This means that very few forests will either not be strongly affected
by climate change, or will not require immediate management action to reduce their
vulnerability to climate change.

Forest owners and managers across Europe are already strongly aware of climate change and are
concerned with its impacts. This awareness needs to be increasingly translated into sufficient
and tangible adaptation actions and resilience-enhancing forest management practices. For that,
technical knowledge and information as well as targeted regulatory and financial incentives and
support need to be developed. This Strategy aims to address these issues to support forest
owners and managers in their efforts, scale up best practices and ensure an increase in the
quantity and quality of EU’s forest cover for decades to come.

3.1.       Protecting EU’s last remaining primary and old-growth forests

To leave space for nature to thrive, the EU Biodiversity Strategy for 2030 has proposed an
overall target to protect at least 30% of the EU land area under effective management regime,
out of which 10% of the EU land should be put under strict legal protection. Forest ecosystems
will need to make a contribution to this target.

All primary and old growth forests, in particular, will have to be strictly protected. Their
estimated cover is only around 3% of EU forested land and patches are generally small and
fragmented. Primary and old-growth forests are not only among the richest EU forest
ecosystems, but they store significant carbon stocks and also remove carbon from the
atmosphere, while being of paramount importance for biodiversity and the provision of critical
ecosystem services40.

Yet, there is still an immediate need to map the primary and old-growth forests and
establish their protection regime, including increased efforts to protect the primary forests in
outermost regions and overseas territories of the Union, given their exceptionally high and
unique biodiversity value. To maintain the undisturbed character of strictly protected forests it is
essential to leave the dynamic of the forest cycle in these forests as much as possible to natural
processes, limiting extractive human activities, while finding synergies with sustainable
ecotourism and recreational opportunities.

The Commission is working in cooperation with Member States and stakeholders to agree, by
the end of 2021, on a common definition for primary and
```

### DOC001-P0012-C002

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012
CHUNK_TEXT_SHA256=163894543c1e473bdb940e8aa3b39b31e0f88fbb58fd2e27fcd55f07928b3de1

```text
their exceptionally high and
unique biodiversity value. To maintain the undisturbed character of strictly protected forests it is
essential to leave the dynamic of the forest cycle in these forests as much as possible to natural
processes, limiting extractive human activities, while finding synergies with sustainable
ecotourism and recreational opportunities.

The Commission is working in cooperation with Member States and stakeholders to agree, by
the end of 2021, on a common definition for primary and old-growth forests and the strict
protection regime. Member States should urgently engage in completing the mapping and
monitoring of these forests, and ensuring no deterioration until they start to apply the
protection regime.
39
       https://www.weforum.org/press/2020/08/us-businesses-governments-and-non-profits-join-global-push-
       for-1-trillion-trees/.
40
       Barredo Cano, J.I., Brailescu, C., Teller, A., Sabatini, F.M., Mauri, A. and Janouskova, K., Mapping and
       assessment of primary and old-growth forests in Europe, EUR 30661 EN, Publications Office of the European
       Union, Luxembourg, 2021, ISBN 978-92-76-34229-8, doi:10.2760/13239, JRC124671.
                                                     11
```

### DOC001-P0019-C002

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 19; DOC001-P0019
CHUNK_TEXT_SHA256=e7f0d778370998b438cbba23114e9c3b09c8bf2fa5be9fe65dd08633285752e1

```text
forest
      ecosystems, by the end of 2021.
   2. Develop guidelines on the definition of primary and old-growth forests, including their
      definition, mapping, monitoring and strict protection, by the end of 2021.
   3. Together with the Member States and in close cooperation with different forest
      stakeholders, identify the additional indicators as well as thresholds or ranges for
      sustainable forest management, and assess how these could best be used, starting on a
      voluntary basis, by the Q1 2023.
   4. Develop guidelines on biodiversity friendly afforestation and reforestation, by Q1 2022.
   5. Develop a definition and adopt guidelines for closer-to-nature-forestry practices, by Q2
      2022, as well as voluntary closer-to-nature forest management certification scheme, by
      Q1 2023.
   6. Provide guidance and promote knowledge exchanges on good practices on climate
      adaptation and resilience, using inter alia the Climate-ADAPT platform.
   7. Supplement the revision of the legislation on forest reproductive material with measures to

50
     https://enrd.ec.europa.eu/.
                                              18
```

### DOC003-P0005-C001

DOCUMENT_ID=DOC003
PAGE_OR_SOURCE_UNIT=PDF page 5; DOC003-P0005
CHUNK_TEXT_SHA256=abdb5eef77cb533169f54faeeac5be655e72d1e84221d86481299463488afa96

```text
efforts are needed and the EU itself needs to do more and better for nature and build a
truly coherent Trans-European Nature Network.

Enlarging protected areas is also an economic imperative. Studies on marine systems
estimate that every euro invested in marine protected areas would generate a return of at
least €319. Similarly, the Nature Fitness Check20 showed that the benefits of Natura 2000
are valued at between €200-300 billion per year. The investment needs of the network are
expected to support as many as 500,000 additional jobs21.

For the good of our environment and our economy, and to support the EU’s recovery
from the COVID-19 crisis, we need to protect more nature. In this spirit, at least 30% of
the land and 30% of the sea should be protected in the EU. This is a minimum of an
extra 4% for land and 19% for sea areas as compared to today22. The target is fully in line
with what is being proposed23 as part of the post-2020 global biodiversity framework
(see Section 4).

Within this, there should be specific focus on areas of very high biodiversity value or
potential. These are the most vulnerable to climate change and should be granted special
care in the form of strict protection24. Today, only 3% of land and less than 1% of marine
areas are strictly protected in the EU. We need to do better to protect these areas. In this
spirit, at least one third of protected areas – representing 10% of EU land and 10% of
EU sea – should be strictly protected. This is also in line with the proposed global
ambition.

As part of this focus on strict protection, it will be crucial to define, map, monitor and
strictly protect all the EU’s remaining primary and old-growth forests25. It will also
be important to advocate for the same globally and ensure that EU actions do not result in
deforestation in other regions of the world. Primary and old-growth forests are the richest
forest ecosystems that remove carbon from the atmosphere, while storing significant
carbon stocks. Significant areas of other carbon-rich ecosystems, such as peatlands,
grasslands, wetlands, mangroves and seagrass meadows should also be strictly protected,
taking into account projected shifts in vegetation zones.

Member States will be responsible for designating the additional protected and strictly
protected areas26. Designations should either help to complete the Natura 2000 network
or be under national protection schemes. All protected areas will need to have clearly
defined conservation objectives and measures. The Commission, working with Member

19
     Brander et al. (2015), The benefits to people of expanding Marine Protected Areas.
20
     Fitness Check of the EU Nature Legislation (SWD(2016) 472).
21
     Member States’
```

### DOC004-P0023-C002

DOCUMENT_ID=DOC004
PAGE_OR_SOURCE_UNIT=PDF page 23; DOC004-P0023
CHUNK_TEXT_SHA256=3330fc3c9d17c9902ebfbdf12bcceeaaba3b70c897c3db8ee010d9732b055fd3

```text
2.    Member States shall put in place the restoration measures that are necessary to re-establish the habitat types in groups
      1 to 6 listed in Annex II in areas where those habitat types do not occur, with the aim of reaching the favourable reference
      area for those habitat types. Such measures shall be in place on areas representing at least 30 % of the additional surface
      needed to reach the favourable reference area for each group of habitat types, as quantified in the national restoration plan
      referred to in Article 15, by 2030, on areas representing at least 60 % of that surface by 2040, and on 100 % of that surface
      by 2050.


      3.    By way of derogation from paragraph 2 of this Article, if a Member State considers that it is not possible to put in
      place restoration measures by 2050 that are necessary to reach the favourable reference area for a specific habitat type on
      100 % of the surface, the Member State concerned may set a lower percentage at a level between 90 % and 100 % in its
      national restoration plan as referred to in Article 15 and provide adequate justification. In such a case, the Member State
      shall gradually put in place restoration measures that are necessary to achieve that lower percentage by 2050. By 2030,
      those restoration measures shall cover at least 30 % of the additional surface needed to achieve such lower percentage by
      2050, and by 2040, they shall cover at least 60 % of the additional surface needed to achieve such lower percentage by
      2050.

      4.    If a Member State applies the derogation pursuant to paragraph 3 to specific habitat types, the obligation set out in
      paragraph 2 shall apply to the remaining additional surface needed to reach the favourable reference area of each group of
      habitat types listed in Annex II to which those specific habitat types belong.

      5.    Member States shall put in place restoration measures for the marine habitats of species listed in Annex III to this
      Regulation and in Annexes II, IV and V to Directive 92/43/EEC and for the marine habitats of wild birds falling within the
      scope of Directive 2009/147/EC that are, in addition to the restoration measures referred to in paragraphs 1 and 2 of this
      Article, necessary to improve the quality and quantity of those habitats, including by re-establishing them, and to enhance
      connectivity, until sufficient quality and quantity of those habitats is achieved.

ELI: http://data.europa.eu/eli/reg/2024/1991/oj                                                                                           23/93
```

### DOC005-P0018-C001

DOCUMENT_ID=DOC005
PAGE_OR_SOURCE_UNIT=PDF page 18; DOC005-P0018
CHUNK_TEXT_SHA256=4c4f4b98d7f8b56febdc77a7e28b3acbf868a9561e78e06dd430a587d439a232

```text
9.6.2023           EN                          Official Journal of the European Union                                       L 150/223


     2.    Operators shall not place relevant products on the market or export them without prior submission of a due
     diligence statement. Operators who, on the basis of the due diligence exercised in accordance with Article 8, conclude
     that the relevant products comply with Article 3 shall, before placing the relevant products on the market or exporting
     them, make available a due diligence statement to the competent authorities through the information system referred to
     in Article 33. Such electronically available and transmittable due diligence statement shall contain the information set
     out in Annex II for the relevant products and a declaration by the operator that the operator exercised due diligence and
     that no or only a negligible risk was found.

     3.    By making available the due diligence statement to competent authorities, the operator shall assume responsibility
     for the compliance of the relevant product with Article 3. Operators shall keep a record of the due diligence statements
     for five years from the date the statement is submitted through the information system referred to in Article 33.

     4.    Operators shall not place relevant products on the market or export them where one or more of the following
     cases apply:

     (a) the relevant products are non-compliant;

     (b) the exercise of due diligence has revealed a non-negligible risk that the relevant products are non-compliant;

     (c) the operator was unable to fulfil the obligations referred to in paragraphs 1 and 2.

     5.    Operators that obtain or are made aware of relevant new information, including substantiated concerns, indicating
     that a relevant product that they have placed on the market is at risk of not complying with this Regulation shall
     immediately inform the competent authorities of the Member States in which they placed the relevant product on the
     market, as well as traders to whom they supplied the relevant product. In the case of exports, the operators shall inform
     the competent authority of the Member State which is the country of production.

     6.   Operators shall offer all necessary assistance to the competent authorities to facilitate the carrying out of the
     checks under Article 18, including access to premises and the making available of documentation and records.

     7.    Operators shall communicate to operators and to traders further down the supply chain of the relevant products
     they placed on the market or exported all information necessary to demonstrate that due diligence was exercised and
     that no or only a negligible risk was found, including the reference numbers of the due diligence statements associated
     to those products.

     8.    By way of derogation from paragraph 1 of this Article, operators that are SMEs (‘SME operators’) shall not be
     required to exercise due
```

### DOC006-P0008-C002

DOCUMENT_ID=DOC006
PAGE_OR_SOURCE_UNIT=PDF page 8; DOC006-P0008
CHUNK_TEXT_SHA256=a60b9e9119ca4832210e44a80e07d785e6e885d88bd7421b3b55b25e7d726e54

```text
emissions;


     (10) ‘instantaneous oxidation’ means an accounting method that assumes that the release into the atmosphere of the
          entire quantity of carbon stored in harvested wood products occurs at the time of harvest.


     2.    The Commission is empowered to adopt delegated acts in accordance with Article 16, to amend or delete the
     definitions contained in paragraph 1 of this Article, or add new definitions thereto, in order to adapt that paragraph to
     scientific developments or technical progress and to ensure consistency between those definitions and any changes to
     relevant definitions in the IPCC Guidelines as adopted by the Conference of the Parties to the UNFCCC or the Conference
     of the Parties serving as the Meeting of the Parties to the Paris Agreement.


                                                              Article 4
                                                           Commitments
     For the periods from 2021 to 2025 and from 2026 to 2030, taking into account the flexibilities provided for in Articles
     12 and 13, each Member State shall ensure that emissions do not exceed removals, calculated as the sum of total
     emissions and total removals on its territory in all of the land accounting categories referred to in Article 2 combined, as
     accounted in accordance with this Regulation.


                                                              Article 5
                                                     General accounting rules
     1.   Each Member State shall prepare and maintain accounts that accurately reflect the emissions and removals resulting
     from the land accounting categories referred to in Article 2. Member States shall ensure that their accounts and other data
     provided under this Regulation are accurate, complete, consistent, comparable and transparent. Member States shall
     denote emissions by a positive sign (+) and removals by a negative sign (-).
```

### DOC007-P0012-C001

DOCUMENT_ID=DOC007
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC007-P0012
CHUNK_TEXT_SHA256=89a9445f36900b4125c9c9e73a89f465a3c367a8e27181933bc6bda242dede5f

```text
L 107/12           EN                          Official Journal of the European Union                                          21.4.2023


           Finland may, besides the flexibilities referred to in the first subparagraph, use additional compensation pursuant to
           Article 13a.

           2.   If a Member State is not in compliance with the monitoring requirements laid down in Article 26 of Regulation
           (EU) 2018/1999, the Central Administrator designated under Article 20 of Directive 2003/87/EC (the “Central
           Administrator”) shall temporarily prohibit that Member State from transferring pursuant to Article 12(2) of this
           Regulation or using the managed forest land flexibility pursuant to Article 13 of this Regulation. The Commission
           may also provide additional technical support to that Member State.


           Article 12


           General flexibilities

           1.     Where, in the period from 2021 to 2025, total emissions exceed total removals in a Member State, or, in the
           period from 2026 to 2030, the difference between the sum of the greenhouse gas emissions and removals on the
           territory of a Member State and the commitment, target or budget set for that Member State in accordance with
           Article 4 of this Regulation is positive, and that Member State has chosen to use its flexibility, and has requested to
           delete annual emission allocations under Regulation (EU) 2018/842, the quantity of deleted emission allocations
           shall be taken into account with respect to the Member State’s compliance with its commitment, target or budget,
           respectively, set in accordance with Article 4 of this Regulation.

           2.     To the extent that, in the period from 2021 to 2025, total removals exceed total emissions in a Member State,
           or, in the period from 2026 to 2030, the difference between the sum of the greenhouse gas emissions and removals
           on the territory of a Member State and the commitment, target or budget set for that Member State in accordance
           with Article 4 of this Regulation is negative, and after subtraction of any quantity taken into account under Article 7
           of Regulation (EU) 2018/842, that Member State may transfer the remaining quantity of removals to another Member
           State. The quantity transferred shall be taken into account when assessing the recipient Member State’s compliance
           with its commitment, target or budget, respectively, set in accordance with Article 4 of this Regulation.

           3.   In order to avoid double counting, the quantity of net removals taken into account under Article 7 of
           Regulation (EU) 2018/842 shall be subtracted from that Member State’s quantity available for transfer to another
           Member State pursuant to paragraph 2 of this Article.

           4.    Member States should use revenues, or their equivalent in financial value, generated by transfers pursuant to
           paragraph 2 to tackle climate change in the Union or in third countries. Member States shall inform the Commission
           of any actions taken pursuant to this paragraph and shall
```

### DOC007-P0014-C002

DOCUMENT_ID=DOC007
PAGE_OR_SOURCE_UNIT=PDF page 14; DOC007-P0014
CHUNK_TEXT_SHA256=f94a5cf0b9eeb040f1e35eb66c028291fbd6bd0b26d860f92db8e8c9c172a384

```text
Union between the annual sum of all greenhouse gas emissions and removals on its territory
               and in all of the land reporting categories referred to in Article 2(2), points (a) to (j), and the Union target of 310
               million tonnes of CO2 equivalent of net removals is negative, in 2030.

               When assessing whether, within the Union, the condition as referred to in the first subparagraph, point (c), of this
               paragraph has been fulfilled, the Commission shall include up to 30 %, but not more than 20 Mt CO2 equivalent,
               of the unused surplus to the commitments of Member States under Article 4(1) from the period from 2021 to
               2025, provided that one or more Member States submit evidence to the Commission concerning the impact of
               natural disturbances in accordance with paragraph 5 of this Article. The Commission shall ensure that double
               counting is avoided by Member States, in particular in the exercise of the flexibilities set out in Article 12 of this
               Regulation and Article 7(1) of Regulation (EU) 2018/842.

           4.    The amount of the compensation referred to in paragraph 3 of this Article may, for the period from 2026 to 2030,
           not exceed 50 % of the maximum amount of compensation for the Member State concerned set out in Annex VII.

           5.     Member States shall submit evidence to the Commission concerning the impact of natural disturbances
           calculated pursuant to Annex VI, in order to be eligible for compensation of net emissions or net removals, or both,
           accounted for as emissions against the targets set for those Member States in accordance with Article 4(3), or against
           the budget set for those Member States in accordance with Article 4(4), up to the amount unused by other Member
           States of the full amount of compensation for the period from 2026 to 2030 set out in Annex VII. Where the
           demand for compensation exceeds the amount of unused compensation available, that unused compensation shall be
           distributed on a pro rata basis among the Member States concerned.

           6.    Member States shall be entitled to compensate net emissions or net removals, or both, accounted for as
           emissions against the targets set for those Member States in accordance with Article 4(3) or against the budget set for
           those Member States in accordance with Article 4(4), up to the amount unused by other Member States of the full
           amount of compensation for the period from 2021 to 2030 set out in Annex VII, after taking into account
           Article 13(4) and paragraph 5 of this Article, provided that those Member States:

           (a) have exhausted the flexibilities available pursuant to Article 12(1), and paragraphs 3 and 5 of this Article; and
```

### DOC010-P0155-C001

DOCUMENT_ID=DOC010
PAGE_OR_SOURCE_UNIT=PDF page 155; DOC010-P0155
CHUNK_TEXT_SHA256=a178bcb3f948e360484e91b1a6c9a679e0147d42cfec5b479df4d0957c945cdd

```text
2020–2021            Meld. St. 13 (2020–2021) Report to the Storting (white paper)                                  153
                                   Norway’s Climate Action Plan for 2021–2030


                                                          and the Government will further develop existing
4.4   How the Government plans to                         mitigation measures for forest. This can provide
      enhance removals and the carbon                     benefits for business and industry and a basis for
      stock in forests                                    increasing value creation and employment in Nor-
                                                          way. Biodiversity, outdoor recreation and other
4.4.1 Introduction                                        environmental interests must be taken into
Forests at high northerly latitudes, like those in        account when measures and policy instruments
Norway, are slow-growing. This means that there           are initiated in this sector.
are few policy instruments and measures that can
give measurable effects by 2030. The measures
that will have the greatest short-term effects are        4.4.2    Grants for higher planting densities,
improving practices for tending young-growth                       forest tree breeding and fertilisation of
stands, reducing harvesting of young-growth                        forest
stands and fertilisation. However, the slow pace of       In 2016, three grant schemes were introduced
growth also means that it is important to start           with the aim of increasing CO2 removals in forest.
other, more long-term measures. These will have           The first is designed to encourage planting seed-
effects in the period from 2030 and up to 2050,           lings at higher densities when regenerating forest
when Norway’s target is to be a low-emission soci-        after harvesting. This increases the standing
ety.                                                      stock and thus CO2 removals in forest. The sec-
    Net removals in forest have been declining            ond is a grant scheme to improve forest tree
since 2009, and this trend will continue up to 2050       breeding. The aim is to use the genetic variation
unless new measures are introduced or the exist-          in forest trees to breed tree seed that yields
ing measures are strengthened. Strengthening              higher production than unimproved seed from
existing mitigation measures will result in more          ordinary forest stands, and that is more resilient
rapid reversal of the declining trend in removals,        to climate change. The third grant scheme is for
and a much higher long-term level of removals in          targeted fertilisation of forest as a climate mitiga-
forest (see Figure 4.7). The Norwegian Institute          tion measure, with accompanying environmental
of Bioeconomy Research and the Norwegian                  criteria. In forest areas where a lack of nitrogen is
Environment Agency have estimated that the                a limiting factor for growth, application of nitrogen
long-term effect of the measures discussed in this        fertiliser results in increased growth in tree
white paper may be to increase annual net remov-          height and diameter over a ten-year period. This
als in forest to about 6.5–8 million tonnes CO2 by        also increases CO2 uptake by the trees. The grant
2100, depending on the scope of the
```

### DOC010-P0162-C001

DOCUMENT_ID=DOC010
PAGE_OR_SOURCE_UNIT=PDF page 162; DOC010-P0162
CHUNK_TEXT_SHA256=7f126099927ec6755655137bded7d701e25d240d0f1e8682a9556cc86c48273b

```text
160                       Meld. St. 13 (2020–2021) Report to the Storting (white paper)                     2020–2021
                                         Norway’s Climate Action Plan for 2021–2030




         Rising net
         emissions



                                                                                                     Year
                       2018                                                                   2100




                                                                                                     Current
       -27,8 million                                                                                 management
      tonnes CO2eq                                                                                   practices
         Rising net                                                                                  Scaled-up
          removals                                                                                   mitigation




Figure 4.7 Illustration of the possible effects of scaling up some measures to enhance removals in managed
forest land. The diagram shows that intensifying management will reverse the declining trend in net removals,
after which annual removals will rise. If more mitigation measures are implemented, annual removals may rise
further, and measures such as minimum age requirements for tree felling may give a clearer effect more
rapidly.
Source: Norwegian Institute of Bioeconomy Research (6(153), 2020)


    A research project called Climate-Smart Fore-               into account effects on the industry, biodiversity,
stry Norway 2020–2024 has been established to                   outdoor recreation and other interests.
identify robust forest management approaches
and provide management guidelines and advice
that will make forests more resilient to climate                4.4.11 Overall effect of mitigation measures in
change. The research project also aims to help                           managed forest land
forest owners ensure higher, sustainable econo-                 Annual net removals in forest in Norway have
mic returns from their forests and to contribute to             been declining since 2009. Net removals in 2009
reductions in greenhouse gas emissions through                  totalled 35 million tonnes CO2eq, but were down
the replacement of fossil raw materials with woo-               to just under 28 million tonnes CO2eq in 2018
den products. The project is funded through rese-               (National Inventory Report 2020). The decline in
arch funding for agriculture and the food industry              annual net removals is expected to continue in the
administered by the Norwegian Agriculture                       years ahead unless new measures are introduced.
Agency and through the BIONÆR research pro-                     The volume of net removals will gradually level off
gramme, and is coordinated by the Norwegian                     and then start to increase again.
University of Life Sciences. The project involves                   In 2016, the Government initiated several mea-
cooperation between Norwegian, Finnish and                      sures to increase net removals in forest. The three
Dutch forest research institutes.                               grant schemes for forest tree breeding, higher
    In addition to this long-term research project,             planting densities after harvesting and fertilisa-
the Ministry of Agriculture and Food and the                    tion of forest were introduced, and at the same
Ministry of Climate and Environment believe that                time, follow-up of compliance with regeneration
a study of climate change adaptation in the fore-               obligations was intensified. If these measures are
stry industry is called for. This would provide a               scaled up and the new measures for enhancing
basis for management advice that would also take                removals in managed forest land described in this
                                                                climate action plan are introduced, the declining
```

### DOC020-P0009-C001

DOCUMENT_ID=DOC020
PAGE_OR_SOURCE_UNIT=PDF page 9; DOC020-P0009
CHUNK_TEXT_SHA256=cefb3896f841bed871eb9bfdab2b8d797d8a3d3e2a25babd0cf9e34a4340a910

```text
L 114/30           EN                          Official Journal of the European Union                                           12.4.2022


     of all people and is an environment in which biodiversity is conserved, ecosystems thrive, and nature is protected and
     restored, leading to increased resilience to climate change, weather- and climate-related disasters and other environmental
     risks. The Union sets the pace for ensuring the prosperity of present and future generations globally, guided by
     intergenerational responsibility.



     2.    The 8th EAP shall have the following six interlinked thematic priority objectives for the period up to 31 December 2030:

     (a) swift and predictable reduction of greenhouse gas emissions and, at the same time, enhancement of removals by natural
         sinks in the Union to attain the 2030 greenhouse gas emission reduction target as laid down in Regulation (EU)
         2021/1119, in line with the Union’s climate and environment objectives, whilst ensuring a just transition that leaves
         no one behind;

     (b) continuous progress in enhancing and mainstreaming adaptive capacity, including on the basis of ecosystem
         approaches, strengthening resilience and adaptation and reducing the vulnerability of the environment, society and all
         sectors of the economy to climate change, while improving prevention of, and preparedness for, weather- and climate-
         related disasters;

     (c) advancing towards a well-being economy that gives back to the planet more than it takes and accelerating the transition
         to a non-toxic circular economy, where growth is regenerative, resources are used efficiently and sustainably, and the
         waste hierarchy is applied;

     (d) pursuing zero pollution, including in relation to harmful chemicals, in order to achieve a toxic-free environment,
         including for air, water and soil, as well as in relation to light and noise pollution, and protecting the health and well-
         being of people, animals and ecosystems from environment-related risks and negative impacts;

     (e) protecting, preserving and restoring marine and terrestrial biodiversity and the biodiversity of inland waters inside and
         outside protected areas by, inter alia, halting and reversing biodiversity loss and improving the state of ecosystems and
         their functions and the services they provide, and by improving the state of the environment, in particular air, water
         and soil, as well as by combating desertification and soil degradation;

     (f) promoting environmental aspects of sustainability and significantly reducing key environmental and climate pressures
         related to the Union’s production and consumption, in particular in the areas of energy, industry, buildings and
         infrastructure, mobility, tourism, international trade and the food system.




                                                                Article 3



                                       Enabling conditions to attain the priority objectives



     The attainment of the priority objectives set out in Article 2 shall require the following from the Commission, Member
     States, regional and local authorities and stakeholders, as appropriate:

     (a)   ensuring effective, swift and full implementation of Union legislation and strategies on the environment and the
           climate and striving for excellence in environmental
```

### DOC025-P0011-C001

DOCUMENT_ID=DOC025
PAGE_OR_SOURCE_UNIT=PDF page 11; DOC025-P0011
CHUNK_TEXT_SHA256=e8cd1f58774c5777d6832b2c5a12bf3d24d8663fb29d9ab912d43240b243830a

```text
6.12.2021          EN                           Official Journal of the European Union                                             L 435/11



     (62)   The CAP should ensure that Member States increase the environmental delivery by respecting local needs and
            farmers’ actual circumstances. Member States should, under direct payments in the CAP Strategic Plan, set up eco-
            schemes which are voluntary for farmers, and which should be fully coordinated with the other relevant
            interventions. They should be determined by the Member States as a payment granted either for incentivising and
            remunerating the provision of public goods by agricultural practices beneficial to the environment and climate, or
            as compensation for carrying out those practices. In both cases, they should aim to enhance the environmental and
            climate-related performance of the CAP and should consequently be conceived to go beyond the mandatory
            requirements already prescribed by the system of conditionality.



     (63)   To ensure efficiency, eco-schemes should as a general rule cover at least two areas of action for the climate, the
            environment, animal welfare and combatting antimicrobial resistance. For the same purpose, while compensation
            should be based on costs incurred, income loss and transaction costs stemming from the agricultural practices
            committed, taking into account the targets set under eco-schemes, the payments additional to basic income support
            need to reflect the level of ambition of the practices committed. Member States should have the possibility to set up
            eco-schemes for agricultural practices carried out by farmers on agricultural areas, in particular agricultural activities
            but also certain practices going beyond agricultural activities. Those practices may include the enhanced
            management of permanent pastures and landscape features, the rewetting of peatlands, paludiculture, and organic
            farming.



     (64)   Organic farming, regulated by Regulation (EU) 2018/848 of the European Parliament and of the Council (24), is a
            farming system that has the potential to substantially contribute to the achievement of multiple specific objectives
            of the CAP, and in particular to its specific environmental and climate-related objectives. In view of the positive
            effects of organic farming on the environment and the climate, Member States should in particular be able to
            consider organic farming when setting up eco-schemes for agricultural practices and assess in that context the level
            of support needed for agricultural land managed under the organic farming scheme.



     (65)   It should be possible for Member States to establish eco-schemes as ‘entry-level schemes’ as a condition for farmers
            for taking up more ambitious environmental, climate-related and animal welfare commitments under rural
            development. To ensure simplification, Member States should be able to establish enhanced eco-schemes.
            Member States should also be able to establish eco-schemes for supporting practices on animal welfare and
            combatting antimicrobial resistance.



     (66)   In order to ensure a level playing field between farmers, a maximum allocation should be set for the coupled income
            support
```

### DOC025-P0041-C001

DOCUMENT_ID=DOC025
PAGE_OR_SOURCE_UNIT=PDF page 41; DOC025-P0041
CHUNK_TEXT_SHA256=2da8cb4d08c66a1c6ed71c4a51fbf9b29d58cd8efcda6879e479b22102f94735

```text
6.12.2021          EN                          Official Journal of the European Union                                            L 435/41



     3.    Member States shall establish a list of the agricultural practices beneficial for the climate, the environment and animal
     welfare and combatting antimicrobial resistance referred to in paragraph 2. Those practices shall be designed to meet one or
     more of the specific objectives set out in Article 6(1), points (d), (e) and (f) and, as regards improving animal welfare and
     combatting antimicrobial resistance, in Article 6(1), point (i).


     4.    Each eco-scheme shall in principle cover at least two of the following areas of actions for the climate, the
     environment, animal welfare and combatting antimicrobial resistance:

     (a) climate change mitigation, including reduction of greenhouse gas emissions from agricultural practices, as well as
         maintenance of existing carbon stores and enhancement of carbon sequestration;

     (b) climate change adaptation, including actions to improve resilience of food production systems and animal and plant
         diversity for stronger resistance to diseases and climate change;

     (c) protection or improvement of water quality and reduction of pressure on water resources;

     (d) prevention of soil degradation, soil restoration, improvement of soil fertility and of nutrient management and soil
         biota;

     (e) protection of biodiversity, conservation or restoration of habitats or species, including maintenance and creation of
         landscape features or non-productive areas;

     (f) actions for a sustainable and reduced use of pesticides, in particular pesticides that present a risk for human health or
         environment;

     (g) actions to enhance animal welfare or combat antimicrobial resistance.


     5.     Under this Article, Member States shall only provide payments covering commitments which:

     (a) go beyond the relevant statutory management requirements and GAEC standards established under Chapter I,
         Section 2;

     (b) go beyond the relevant minimum requirements for the use of fertiliser and plant protection products, animal welfare, as
         well as other relevant mandatory requirements established by national and Union law;

     (c) go beyond the conditions established for the maintenance of the agricultural area in accordance with Article 4(2), point
         (b);

     (d) are different from commitments in respect of which payments are granted under Article 70.


     For commitments referred to in the first subparagraph, point (b), where national law imposes new requirements which go
     beyond the corresponding minimum requirements laid down in Union law, support may be granted for commitments
     contributing to compliance with those requirements for a maximum of 24 months from the date on which they become
     mandatory for the holding.


     6.    Pursuant to paragraph 5, Member States may, for the description of the commitments to be fulfilled by the
     beneficiary of eco-schemes referred to in this Article, build upon one or more of the requirements and standards
     established under Chapter I, Section 2, provided that the obligations of the eco-schemes go beyond the relevant statutory
```

### DOC025-P0042-C001

DOCUMENT_ID=DOC025
PAGE_OR_SOURCE_UNIT=PDF page 42; DOC025-P0042
CHUNK_TEXT_SHA256=d963f1d2a066b419d30a732baa76a3a0b5eb0c24515babd3a4ed7c5609c9e7d1

```text
L 435/42            EN                         Official Journal of the European Union                                          6.12.2021



     7.  Support for a particular eco-scheme shall take the form of an annual payment for all eligible hectares covered by the
     commitments. Payments shall be granted as either:
     (a) payments additional to the basic income support set out in Subsection 2; or
     (b) payments compensating active farmers or groups of active farmers for all or part of the additional costs incurred and
         income foregone as a result of the commitments made which shall be calculated in accordance with Article 82 and
         taking into account the targets for eco-schemes; those payments may also cover transaction costs.

     By way of derogation from the first subparagraph, payments granted in accordance with point (b) thereof for animal welfare
     commitments, commitments combatting antimicrobial resistance and, if duly justified, commitments for agricultural
     practices beneficial for the climate may also take the form of an annual payment for the livestock units.

     8.    Member States shall demonstrate how the agricultural practices committed under eco-schemes respond to the needs
     referred to in Article 108 and how they contribute to the environmental and climate architecture referred to in Article
     109(2), point (a), and to animal welfare and combatting antimicrobial resistance. They shall use a rating or scoring system
     or any other appropriate methodology to ensure the effectiveness and efficiency of the eco-schemes to deliver on the
     targets set. When establishing the level of payments for different commitments under the eco-schemes pursuant to
     paragraph 7, first subparagraph, point (a), of this Article, Member States shall take into account the level of sustainability
     and ambition of each eco-scheme, based on objective and transparent criteria.

     9.    Member States shall ensure that interventions under this Article are consistent with those based on Article 70.




                                                              Sect ion 3

                                                     Coupled di rec t paym ent s




                                                            S ubsecti on 1

                                                     Coupled in co me suppor t




                                                               Article 32

                                                            General rules

     1.    Member States may grant coupled income support to active farmers under the conditions set out in this Subsection
     and as further specified in their CAP Strategic Plans.

     2.    The Member States’ interventions shall help the supported sectors and productions or specific types of farming
     therein listed in Article 33 to address the difficulties encountered by improving competitiveness, sustainability or quality.
     Member States shall not be required to demonstrate the difficulties encountered in relation to protein crops.

     3.    Coupled income support shall take the form of an annual payment per hectare or animal.



                                                               Article 33

                                                                Scope

     Coupled income support may only be granted to the following sectors and productions or specific types of farming therein
     where they are important for socio-economic or environmental reasons:
     (a) cereals;
     (b) oilseeds excluding confectionary sunflower seeds as laid down in
```

## Provenance and final state

AUDIT_TRIGGER=primary_30_task_prebenchmark_structural_validation
BENCHMARK_STARTED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
RANKED_RETRIEVAL_USED=NO
EMBEDDINGS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
TASK_MUTATION=NO
REPAIR_TASKS_CREATED=NO
HISTORICAL_FREEZE_MUTATION=NO
TRACKED_MODIFIED_COUNT=0
STAGED_COUNT=0
UNTRACKED_COUNT=1
DIFF_CHECK=PASS
COMMIT=NO
PUSH=NO

AUDIT_COMPLETION=PASS means the requested audit was completed; it does not mean every task type is valid. T005 is the one identified defective task.
