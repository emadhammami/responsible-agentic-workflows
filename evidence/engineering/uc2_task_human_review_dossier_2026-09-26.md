# UC2 task human review dossier — 26 September 2026

This dossier prepares researcher decisions on T011–T020. All questions and reference-answer candidates are carried forward unchanged from the authoritative audits, with **T014 Human-Directed Pre-Freeze Revision 1** as the final T014 candidate. The seven other substantive candidates retain their audited questions; T019/T020 retain the human-directed insufficient-evidence questions. Suggested wording changes are explicitly separate and have not been applied.

Proposed decisions: **7 READY_FOR_RESEARCHER_DECISION; 3 REVISION_RECOMMENDED; 0 REJECT_RECOMMENDED**. T018’s prospective framing and one reference-answer completion claim, and T019/T020’s measurement/accounting scope, warrant clarification before freeze. The corpus-absence findings remain intact; these are not researcher decisions. No task is human-verified or frozen.

## Provenance, controls and reviewer use

- Branch: `research/benchmark-task-construction-uc2-uc3`.
- Expected and observed HEAD: `4ca03cde8dd969c07590670615008b17d5448a2e`.
- Initial worktree: exactly the two untracked audits below; no tracked/staged changes. Neither audit is modified.
- Authoritative evidence audit: [uc2_task_candidate_evidence_audit_2026-09-26.md](uc2_task_candidate_evidence_audit_2026-09-26.md).
- Authoritative absence audit: [uc2_insufficient_evidence_absence_audit_2026-09-26.md](uc2_insufficient_evidence_absence_audit_2026-09-26.md).
- Canonical corpus: `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl`; 293 unique chunks across all 17 accepted UC2 documents. All text hashes rechecked; membership and the absence audit’s complete 293-row ledger reconciled to the canonical records.
- Frozen authoring protocol: `benchmark/task_authoring_protocol_v0.1.json`, `PRIMARY-UC2-UC3-TASK-AUTHORING-v0.1`, status `frozen_before_task_authoring`. Allocation and evidence-type requirements are preserved.

**T014 history:** The original process-linkage question was DEFECT_REQUIRES_REVIEW because DOC043-U0001-C0001 alone answered it. The original defect remains in the evidence audit. The user explicitly authorized the replacement question in pre-freeze Revision 1, supported by C0004 and C0009. This dossier presents only Revision 1 for the decision; it does not retroactively change the original verdict. The revision reason is TASK_TYPE_INTEGRITY_DEFECT; it used no performance/results information.

**Reviewer workflow:** A–F below contain explicit checks with LLM-assisted preliminary assessments. Unchecked boxes are for the researcher and do not record approval. Difficulty is a qualitative candidate judgment about evidence handling and reasoning, not a measured model/retrieval result. Low denotes localized fact extraction, medium synthesis within a document, and high comparison/qualification or corpus-wide absence discrimination; the researcher may change these labels.

**Gold candidates:** For answerable tasks the proposed reference-evidence set contains the audit’s REQUIRED chunks supporting its minimal complete answer. SUPPORTING/REDUNDANT targets remain visible as context, without being promoted into mandatory gold. Every proposed evidence item has `document_id`, `chunk_id`, `page` (canonical PDF page or null for HTML) and a section locator, matching the existing schema’s evidence fields. This is a Markdown dossier, not a task JSON or finalized schema instance. For insufficient-evidence tasks both candidate arrays are []; near-miss citations are review evidence only.

**Scoring precision:** Reference answers are preserved verbatim as candidates, not made into a rubric. Equivalently supported concise answers should be considered by the researcher. Details identified as optional below must not accidentally become required because the candidate reference happens to mention them. No new scientific metric or tax-accounting convention is adopted through a suggested change.

## T011

- **TASK_ID:** T011
- **TASK_TYPE:** direct_retrieval
- **DIFFICULTY_CANDIDATE:** low — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC046]

**EXACT_FINAL_CANDIDATE_QUESTION**

> Under Green Freeport NDR relief, for how long can relief run from first eligibility, and by what date must it be applied for, subject to the 2028 review?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC046 | DOC046-U0001-C0002 | null | Timespan and Eligibility | REQUIRED |

**REFERENCE_ANSWER_CANDIDATE**

Relief can run for up to five years from when the beneficiary first becomes eligible, including any period in which another relief is awarded in its place. It must be applied for by 30 September 2034, subject to the outcome of the 2028 mid-point review. Availability also depends on the relevant tax site having been established and designated. [DOC046-U0001-C0002]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A ratepayer/adviser needs the maximum relief period and application deadline.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Beneficiary/ratepayer and first eligibility are clear; the 2028 review anchors the extension guidance.
- [ ] No accidental answer clue: Neutral request; review year is a qualification, not a duration/deadline answer clue.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] Localized evidence genuinely sufficient; no unacknowledged synthesis needed.

Preliminary assessment: One localized DOC046 timespan/eligibility passage contains up to five years from eligibility and the 30 September 2034 deadline subject to review. No second location is necessary.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Preserves up-to-five-years, eligibility rather than payment start, relief-in-lieu counting, designation and the conditional deadline. No ten-year individual entitlement or unconditional 2034 end date is asserted. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Complete target facts are determinate in DOC046; older prospectus wording could support a different start/deadline if source version were ignored.
- [ ] **Ambiguous dates:** First eligibility is distinct from relief first received; five-year individual duration is distinct from the tax-relief application window and the 2028 review.
- [ ] **Ambiguous entity names:** Beneficiary/ratepayer is the actor; NDR relief is not retained NDR.
- [ ] **Source conflict:** DOC041-U0001-C0023 describes first receipt and a 31 March 2028 deadline; DOC046-U0001-C0002 describes first eligibility and conditional 30 September 2034. This is an explicit cross-version discrepancy to be adjudicated using the later, measure-specific guidance, not silently blended.
- [ ] **Stale versus current within frozen corpus:** The DOC046 passage expressly reports the 6 March 2024 extension; this dossier does not claim current live law. The question’s 2028 review qualification signals the later guidance.
- [ ] **Forecasts/examples versus realised/observed values:** No forecasted outcome or illustrative date is used as the asked entitlement period/deadline.
- [ ] **Partial evidence and scoring fairness:** Credit the period, start point, application date and review caveat; do not require a particular illustrative ratepayer example. Researcher should confirm source-version precedence before approval.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. Minor NDR-domain overlap with T014: individual rates-relief duration/deadline versus retained-revenue financing/governance.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T012

- **TASK_ID:** T012
- **TASK_TYPE:** direct_retrieval
- **DIFFICULTY_CANDIDATE:** low — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC047]

**EXACT_FINAL_CANDIDATE_QUESTION**

> What proportion of chargeable consideration must relate to qualifying Green Freeport land for full LBTT relief, and what minimum proportion permits partial relief?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC047 | DOC047-U0001-C0001 | null | Overview — Green Freeports relief | REQUIRED |

**REFERENCE_ANSWER_CANDIDATE**

Full relief requires at least 90% of the transaction's chargeable consideration to relate to qualifying land on a designated Green Freeport tax site. The minimum threshold for partial relief is at least 10%. [DOC047-U0001-C0001]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A transaction adviser needs full/partial LBTT thresholds.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Chargeable consideration and qualifying designated tax-site land are the relevant scope; no transaction date is needed for this threshold-only question.
- [ ] No accidental answer clue: Neutral numerical-threshold request; it supplies no percentages.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] Localized evidence genuinely sufficient; no unacknowledged synthesis needed.

Preliminary assessment: The 90% full and 10% minimum partial thresholds appear together in DOC047-C0001. No synthesis outside the local passage is necessary.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Uses “at least” for both thresholds and chargeable consideration rather than area. Minimal complete threshold answer; no unsupported partial amount or universal partial eligibility above 90% is inferred. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** At-least thresholds are determinate; full versus partial relief categories are not interchangeable.
- [ ] **Ambiguous dates:** No current-policy date is requested; thresholds are assessed as frozen guidance, not a time-sensitive legal opinion.
- [ ] **Ambiguous entity names:** Qualifying Green Freeport land means designated tax-site qualifying land; consideration is not land area.
- [ ] **Source conflict:** DOC048-U0003-C0001 states partial relief is below 90% but at least 10%; this clarifies rather than contradicts DOC047’s minimum threshold wording.
- [ ] **Stale versus current within frozen corpus:** DOC047/DOC048 contain a 2028 LBTT eligibility window; do not borrow 2034 deadlines from other tax measures. No deadline is demanded by this question.
- [ ] **Forecasts/examples versus realised/observed values:** Worked transaction percentages elsewhere in DOC047 illustrate the rules; they are not aggregate observed claims.
- [ ] **Partial evidence and scoring fairness:** The unfinished qualifying-land definition at C0001’s end is not necessary for the threshold answer. Do not penalise a source-correct answer that adds the below-90% partial category.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. Shares LBTT domain with T020, which asks actual aggregate claims, not eligibility thresholds.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T013

- **TASK_ID:** T013
- **TASK_TYPE:** direct_retrieval
- **DIFFICULTY_CANDIDATE:** low — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC058]

**EXACT_FINAL_CANDIDATE_QUESTION**

> What location and project-approval conditions must be satisfied for a Scottish Green Freeport seed-capital subsidy to support a project?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC058 | DOC058-U0001-C0002 | null | Eligibility rules — 1. Eligible location; 2. Eligible activity | REQUIRED |

**REFERENCE_ANSWER_CANDIDATE**

The project must be within the outer boundary of Forth or Inverness and Cromarty Firth Green Freeport, or in an economically connected location where justified in the Full Business Case. It must be set out and agreed in the relevant Freeport's Full Business Case, or subsequently approved by government through a formal change request. Its own business case must also be approved by the accountable body under local assurance processes and by the Green Freeport Board. If another local authority awards the subsidy, it needs the relevant accountable body's permission and confirmation that the accountable body approved the project business case under those processes. [DOC058-U0001-C0002]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A project sponsor or authority needs location and project-approval prerequisites.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Scottish subsidy scheme, project, accountable body, Freeport Board and government/change-request layers are distinguishable.
- [ ] No accidental answer clue: Neutral conditions question; no listed approval or location exception is disclosed.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] Localized evidence genuinely sufficient; no unacknowledged synthesis needed.

Preliminary assessment: Adjacent eligible-location and eligible-activity rules within DOC058-C0002 contain the complete location and project-approval answer. The number of conditions does not itself make this reasoning across locations.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Preserves the economically connected exception and separate Freeport/project business-case approvals and other-authority permissions. Minimal within the requested location/approval scope; unrelated subsidy caps/recovery terms are not needed. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Connected-location exception and alternative formal-change approval route allow multiple lawful routes, which the answer must preserve.
- [ ] **Ambiguous dates:** The question asks scheme conditions in the frozen text; no delivery or actual-award date is requested.
- [ ] **Ambiguous entity names:** Government, accountable body, Board and other awarding local authority are different roles; project business case is not the Freeport FBC.
- [ ] **Source conflict:** No material contradictory location/approval condition identified in the assigned evidence. DOC043 general setup governance is a different stage/scope.
- [ ] **Stale versus current within frozen corpus:** The source’s awkward “approval Full Business Case” is not treated as a new undefined approval tier; no live correction is supplied.
- [ ] **Forecasts/examples versus realised/observed values:** Eligibility guidance is neither proof of awarded funds nor a claim that a particular project delivered benefits.
- [ ] **Partial evidence and scoring fairness:** Stay within location and project approval; do not require unasked cap, subsidy cumulation or incomplete recovery-clause detail.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. Shares seed-capital domain with T014/T018; asks generic location/project-approval eligibility, not financing-instrument comparison or programme implementation.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T014 — final Revision 1

- **TASK_ID:** T014
- **TASK_TYPE:** within_document_reasoning
- **DIFFICULTY_CANDIDATE:** medium — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC043]

**EXACT_FINAL_CANDIDATE_QUESTION**

> How are seed capital and retained non-domestic rates intended to play different financing roles in Green Freeport delivery, and how do their accountability and governance arrangements differ?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC043 | DOC043-U0001-C0004 | null | 3.1.6–3.1.8 — Seed capital funding | REQUIRED |
| DOC043 | DOC043-U0001-C0009 | null | 6.1.1 continuation; 6.1.2–6.1.6 — Retained non-domestic rates | REQUIRED |

Audit context retained: SUPPORTING: DOC043-U0001-C0005 (assurance/payment conditions), C0010 (displacement/planning-use detail), C0032 (MoU/formalisation). None is required for the minimal comparison.

**REFERENCE_ANSWER_CANDIDATE**

Seed capital is intended for projects deliverable in the short term; longer-term public investment projects are expected to use retained non-domestic rates. Seed capital is paid to each coalition's accountable body in annual tranches. That body is responsible for ensuring relevant regulations and best-practice standards, including public procurement, are met and that Value for Money and policy objectives are delivered, taking individual projects through local assurance/business-case processes. Business Cases are approved by the Green Freeport Programme Board, with joint representation from the governments. [DOC043-U0001-C0004, sections 3.1.6–3.1.8]

Retained NDR concerns tax-site rates growth above an agreed pre-designation baseline, minus an agreed displacement factor. Retention is guaranteed for 25 years, providing local authorities certainty to borrow for regeneration and infrastructure supporting further growth. The local authority or authorities remain accountable for its use as public funds, while strategic direction should be set by the Green Freeport governing body. The retained funds are expected to support Green Freeport-associated purposes, including operating costs and investment-supporting infrastructure and other activities. [DOC043-U0001-C0009, section 6.1.1 continuation and sections 6.1.2–6.1.6]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: An authority or delivery partner needs to distinguish financing instruments and responsibility.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Green Freeport delivery; seed capital versus retained NDR; intended policy roles rather than realised expenditure.
- [ ] No accidental answer clue: Neutral comparison; different roles are supported, but no duration or allocation of responsibility is given away.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] At least two materially distinct evidence locations required.
- [ ] One location alone insufficient for the complete answer.

Preliminary assessment: C0004 covers short-term seed capital, annual-tranche payment and accountable-body assurance/Programme Board approval; C0009 covers 25-year retained growth, local-authority public-fund accountability and governing-body direction. C0004 alone mentions the longer-term NDR role but omits its governance and retention guarantee. C0009 alone omits seed payment/assurance. Both disjoint locations are materially required.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Preserves prospective financing expectations, tranche payment, Value for Money assurance, retained growth adjustment and 25-year retention, and separates financial accountability from strategic direction. No guarantee of a revenue amount, exclusive funding partition or assumption that authorities are different organizations is made. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Several eligible retained-NDR uses exist; short-/longer-term financing is an expectation, not an exclusive partition.
- [ ] **Ambiguous dates:** No numeric short-term cutoff is specified in source. Twenty-five years is a retention guarantee, not a guaranteed yield or completion horizon.
- [ ] **Ambiguous entity names:** Accountable body, local authorities, Programme Board and governing body are role labels; an accountable body may itself be a local authority.
- [ ] **Source conflict:** No material contradiction to the finance/governance comparison identified. DOC041/DOC042 also describe 25-year retention, while DOC046 covers a different NDR relief measure.
- [ ] **Stale versus current within frozen corpus:** Use setup guidance’s intended arrangements; do not infer current disbursement or changed governance from audit date.
- [ ] **Forecasts/examples versus realised/observed values:** Payment/borrowing arrangements are prospective policy statements, not recorded spending or outcomes.
- [ ] **Partial evidence and scoring fairness:** C0004 alone has the temporal contrast but misses retained-NDR governance; require synthesis of both roles. Optional MoU and subsidy detail must not become mandatory scoring items.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. Shares governance/seed terms with T013/T018 and NDR with T011; compares seed versus retained rates, not project eligibility or the two Freeports’ programmes.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T015

- **TASK_ID:** T015
- **TASK_TYPE:** within_document_reasoning
- **DIFFICULTY_CANDIDATE:** medium — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC045]

**EXACT_FINAL_CANDIDATE_QUESTION**

> How does the national planning protocol seek to accelerate Green Freeport consenting while retaining normal statutory decision frameworks, and what roles do councils, consultees and developers play?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC045 | DOC045-U0001-C0002 | null | All partners; statutory frameworks and processing agreements | REQUIRED |
| DOC045 | DOC045-U0001-C0003 | null | Councils; other consenting bodies; statutory consultees/agencies; developers | REQUIRED |

Audit context retained: SUPPORTING: DOC045-U0001-C0004 (overlap, government role and statutory pre-application consultation note).

**REFERENCE_ANSWER_CANDIDATE**

The protocol accelerates consenting through coordinated early engagement, shared evidence, early environmental screening/scoping and processing agreements with agreed timelines and infrastructure arrangements. Planning decisions still follow legislation and the development plan unless material considerations indicate otherwise; other consents retain their established regulatory frameworks. It seeks decisions within two months for local and four months for major/national planning applications without legal agreements; where legal agreements are involved, committee or delegated decisions should be taken within those periods wherever possible. More complex applications may have longer agreed timescales. [DOC045-U0001-C0002]

Councils align consent processes, provide senior and application contacts, coordinate pre-application information requirements, agree consultee deadlines, review processing dates with developers within four weeks of validation and discuss conditions/contributions and legal agreements early. Statutory consultees provide contacts, clarify information needs early and adhere to reasonable response dates, contacting authority leads if deadlines are missed. Developers engage early with councils/agencies and communities, submit and supply timely high-quality information, consider reasonable legal-agreement/contribution requests and agree Habitats assessment information and surveys early. [DOC045-U0001-C0003]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A developer or consenting coordinator needs the intended faster process and each actor’s responsibilities.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: National Green Freeport protocol; councils, consultees and developers; normal frameworks remain the decision basis.
- [ ] No accidental answer clue: Neutral mechanism question; retaining statutory frameworks is the premise, not an answer to the requested operational roles.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] At least two materially distinct evidence locations required.
- [ ] One location alone insufficient for the complete answer.

Preliminary assessment: C0002 supplies statutory-framework preservation and processing mechanisms/timescales; C0003 supplies the complete council/consultee/developer responsibility division. The overlap does not reproduce C0002’s legal-framework account or C0003’s substantive consultee/developer roles in one chunk. Both are necessary.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Covers mechanism/framework and all requested actors. Two-/four-month timescales are qualified for legal agreements and complexity. Read its opening “accelerates” as the protocol’s intended mechanism, not measured performance; the question itself says “seek.” No achieved time saving should be credited or required. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Equivalent concise role summaries are defensible; statutory versus non-statutory consultees should not be conflated.
- [ ] **Ambiguous dates:** Two/four months and the four-week processing-date review are different intervals; application complexity/legal agreements qualify the decision targets.
- [ ] **Ambiguous entity names:** Councils coordinate, agencies respond and developers provide information/engagement; permissions are not guaranteed by any actor.
- [ ] **Source conflict:** No material contradiction in the named protocol passages; planning and other consents keep their own statutory frameworks.
- [ ] **Stale versus current within frozen corpus:** Treat the August 2024 protocol as frozen guidance. Do not equate proposed planning mechanisms in older DOC043 with demonstrated consent outcomes.
- [ ] **Forecasts/examples versus realised/observed values:** Timescales are process commitments, not measured results. No worked application is asserted to be observed performance.
- [ ] **Partial evidence and scoring fairness:** C0004’s 12-week statutory pre-application note is supporting context, not a mandatory detail for the minimal actor/mechanism account.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No material information-need overlap with another task; planning-process acceleration and actor duties are unique here.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T016

- **TASK_ID:** T016
- **TASK_TYPE:** within_document_reasoning
- **DIFFICULTY_CANDIDATE:** medium — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC051]

**EXACT_FINAL_CANDIDATE_QUESTION**

> How do the customs-site-operator role and Freeport business authorisation differ and interact, including when a customs site operator needs an additional Freeport customs procedure authorisation?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC051 | DOC051-U0004-C0002 | null | Designation and Authorisation — Authorisation | REQUIRED |
| DOC051 | DOC051-U0005-C0001 | null | Operating a Freeport customs site — responsibilities | REQUIRED |

Audit context retained: SUPPORTING: DOC051-U0005-C0002 (conditional joint liability and revocation interaction).

**REFERENCE_ANSWER_CANDIDATE**

The customs site operator is the responsible authority controlling goods movement and people's access, taking reasonable steps to prevent unauthorised activity and meeting designation-order requirements for records, site security and HMRC access/facilities. [DOC051-U0005-C0001] A business separately needs HMRC authorisation to declare goods for the free-zone procedure and conduct industrial, service or commercial activities on those goods; the specified transfer-of-free-zone-goods activity is excepted. It must confirm at application that it has an agreement with the relevant operator allowing it to operate on the site. The operator also needs Freeport customs procedure authorisation, in addition to its operator role, if it wishes to import goods to the site or carry out activities on goods declared to that procedure. [DOC051-U0004-C0002]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A customs operator or trading business needs to distinguish site management from goods-activity permission.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Customs site operator, authorised business and HMRC are distinct; dual-role operators are specifically in scope.
- [ ] No accidental answer clue: Neutral authorisation comparison; additional authorisation is a stated scenario without disclosing its trigger.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] At least two materially distinct evidence locations required.
- [ ] One location alone insufficient for the complete answer.

Preliminary assessment: U0004-C0002 supplies business authorisation, operator agreement and the dual-role trigger; U0005-C0001 supplies operator duties. Neither alone gives the complete role-and-interaction account. They are distinct source units, not merely overlapping chunks.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Covers operator duties, distinct authorisation, agreement and dual-role trigger; preserves the transfer exception. No authorisation expiry or liability claim is inferred. Revocation detail in supporting evidence is not mandatory for completeness. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** A business may also be the operator; describing role differences must not imply mandatory organizational separation.
- [ ] **Ambiguous dates:** No historical observation date is requested. Do not invent an authorisation expiry or apply future compliance outcomes.
- [ ] **Ambiguous entity names:** “Freeport business authorisation” maps to the customs procedure authorisation described in U0004; customs designation is distinct from tax-site relief eligibility.
- [ ] **Source conflict:** No material inconsistency identified in the operator/authorisation passages; exceptions in transfer activities must be retained.
- [ ] **Stale versus current within frozen corpus:** Frozen customs guidance determines the answer; no newer HMRC procedure is imported.
- [ ] **Forecasts/examples versus realised/observed values:** Authorisation duties/rules are not evidence that a specific business was actually authorised or had breached an obligation.
- [ ] **Partial evidence and scoring fairness:** A correct minimal account of duties, agreement and dual-role trigger is sufficient. Joint-liability/revocation detail from supporting C0002 is not required.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No material information-need overlap with another task; operator/business customs authorisation distinction is unique. Tax-site mentions elsewhere do not duplicate it.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T017

- **TASK_ID:** T017
- **TASK_TYPE:** cross_document_reasoning
- **DIFFICULTY_CANDIDATE:** high — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC056, DOC057]

**EXACT_FINAL_CANDIDATE_QUESTION**

> How do enhanced Structures and Buildings Allowance and Enhanced Capital Allowance differ in eligible assets, relief structure and qualifying use/location conditions in Scottish Green Freeport tax sites?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC056 | DOC056-U0001-C0001 | null | How to qualify — structures/buildings | REQUIRED |
| DOC056 | DOC056-U0001-C0002 | null | How to apportion; how much relief | REQUIRED |
| DOC057 | DOC057-U0001-C0001 | null | How to qualify; how much relief — plant/machinery | REQUIRED |
| DOC057 | DOC057-U0001-C0002 | null | Withdrawal of relief; mixed-use restriction continuation | REQUIRED |

**REFERENCE_ANSWER_CANDIDATE**

Enhanced Structures and Buildings Allowance covers qualifying expenditure on structures/buildings and provides 10% annually for ten years, starting at the later of first non-residential use and incurring qualifying expenditure. Construction must begin while the asset is in a special tax site (first contract or construction work, whichever is earlier); qualifying use and expenditure must occur while in the site and by 30 September 2034 for Scottish Green Freeports. The claimant must meet the ordinary structures/buildings allowance requirements and be registered for Corporation Tax or Income Tax. Enhanced and normal rates are apportioned where part lies outside the site or part enters qualifying use after the deadline. [DOC056-U0001-C0001; DOC056-U0001-C0002]

Enhanced Capital Allowance covers unused, non-second-hand plant/machinery for trading activity or a land activity taxed as trading. It provides 100% of qualifying expenditure against qualifying-activity profits in the accounting period of expenditure; the claimant must be registered for Corporation Tax. At expenditure the asset must be intended primarily for use in a designated special tax site; Scottish qualifying expenditure runs from designation to 30 September 2034. Primary special-tax-site use must continue for five years from first qualifying use or keeping for qualifying use there; cessation within that period requires withdrawal and notification within three months. For mixed use, the restriction to expenditure attributable to site use applies when the asset is also for use outside a site and the main purpose of expenditure is to obtain the enhanced allowance for that outside-site part. [DOC057-U0001-C0001; DOC057-U0001-C0002]

Both concern tax sites, which the guidance distinguishes from separately authorised customs sites. [DOC056-U0001-C0001; DOC057-U0001-C0001]

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A tax/investment adviser needs an asset/relief/conditions comparison.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Scottish Green Freeport tax sites expressly exclude substituting English deadlines; named allowances are distinct.
- [ ] No accidental answer clue: Neutral comparison dimensions, with no rate or eligible asset specified in the question.
- [ ] Wording neutral and precise: no material wording defect identified; preserve source qualifications and the question’s bounded scope.

### B. TASK_TYPE_INTEGRITY

- [ ] Both required documents materially required.
- [ ] Neither document alone supplies the complete comparison.

Preliminary assessment: DOC056 supplies structures/buildings assets, annual relief and qualifying construction/use; DOC057 supplies new plant/machinery, immediate relief and continuing primary use. Neither document supplies the other allowance’s complete rules. Shared deadlines alone are not the basis for the cross-document requirement.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Covers all three requested comparison dimensions and dates/registrations/continuing-use qualifications. Mixed-use ECA restriction retains both specified conditions and is not converted into a universal pro-rata rule. Three-month notification is source-supported additional detail, not a separate question requirement. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Eligible expenditure is qualified, not every structure or asset. Equivalent comparison organization is acceptable.
- [ ] **Ambiguous dates:** 2034 expenditure/use window, ten-year SBA relief and five-year ECA primary-use requirement are distinct. English 2031 is outside Scottish scope.
- [ ] **Ambiguous entity names:** Corporation/Income Tax registration differs; tax sites are distinct from customs sites. Structures/buildings are distinct from plant/machinery.
- [ ] **Source conflict:** Older DOC041-U0001-C0021/C0022 use 30 September 2026; DOC056/DOC057 target guidance states Scottish 30 September 2034. Record this version difference; do not mix deadlines in the gold.
- [ ] **Stale versus current within frozen corpus:** DOC056/DOC057 target pages state update 4 July 2024. Their measure-specific Scottish conditions anchor this frozen comparison, not live legal advice.
- [ ] **Forecasts/examples versus realised/observed values:** Warehouse/forklift examples demonstrate allowances; they do not establish aggregate actual claims or realised investment.
- [ ] **Partial evidence and scoring fairness:** DOC057-C0001 ends mid mixed-use condition, completed by C0002. Do not generalise it or require external eligibility categories linked from the pages.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. Related tax domain to T011/T012/T020, but compares SBA/ECA assets, structures and continuing use.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** READY_FOR_RESEARCHER_DECISION

ISSUE=No material wording issue requiring a candidate change identified.

SUGGESTED_CHANGE=None; retain the exact candidate pending researcher decision.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T018

- **TASK_ID:** T018
- **TASK_TYPE:** cross_document_reasoning
- **DIFFICULTY_CANDIDATE:** high — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** [DOC052, DOC053]

**EXACT_FINAL_CANDIDATE_QUESTION**

> How do the Inverness and Cromarty Firth and Forth Green Freeports use seed capital to unlock investment, including funding scale, project selection/deployment and governance/accountability arrangements?

**REFERENCE_EVIDENCE_CANDIDATE**

| document_id | chunk_id | page | section | Classification |
|---|---|---|---|---|
| DOC052 | DOC052-U0012-C0001 | 12 | 5.3.3 — Seed capital | REQUIRED |
| DOC052 | DOC052-U0014-C0001 | 14 | 5.4.6–5.4.8 — Seed capital accountability/funding | REQUIRED |
| DOC053 | DOC053-U0008-C0001 | 8 | 4.7–4.12 — Financial/commercial/management case | REQUIRED |
| DOC053 | DOC053-U0027-C0001 | 27 | Seed-capital proposal assessment/prioritisation | REQUIRED |
| DOC053 | DOC053-U0028-C0001 | 28 | Tax-site Investment Principles; 2.3c Trade and Investment Promotion | REQUIRED |

Audit context retained: REDUNDANT: DOC052-U0012-C0002 (overlap plus sentence completion); not mandatory reference evidence.

**REFERENCE_ANSWER_CANDIDATE**

Inverness and Cromarty Firth proposes £25m of seed capital for enabling infrastructure that unlocks tax-site land. Sponsors of 11 preferred projects submitted project OBCs for Council gateway assessment toward FBC, using Green Book principles and considering benefits, viability and affordability. [DOC052-U0012-C0001] Following confirmation of the award, sponsors are to submit FBCs to the accountable body, reviewed by an investment subgroup comprising Freeport-company and Highland Council representatives, with further subsidy-control checks and government change requests for reserve-list alternatives if necessary. Highland Council is accountable for accounting and public governance; the Freeport and partners deliver the programme and manage delivery, risk and outcomes. The £25m is to be complemented by over £60m further public funding and almost £175m private funding, giving around £260m total seed-capital project expenditure. [DOC052-U0014-C0001]

Forth uses early seed capital as an investment lever. [DOC053-U0028-C0001] Proposals were assessed/prioritised in line with the Scottish Government Investment Hierarchy and considered by local-authority partners. Four core projects—Forth Ports Leith land preparation, Babcock integrated energy system, Grangemouth utility capacity and INEOS low-carbon hydrogen preparation—require a minimum £17.9m ask, attracting at least £17.9m private match funding. The maximum £24.5m ask enables six additional projects costing £6.6m, with £12.9m partner match funding. [DOC053-U0027-C0001] The financial case expects £24.5m seed capital to attract £8m further public and £64.4m private funding, for circa £96.9m overall project expenditure; these are the financial-case totals, distinct from the proposal-level match-funding figures. Procurement is by private landowners and other sponsors, including public bodies, aligned with general public procurement rules. Forth Green Freeport Operating Ltd delivers under Forth Green Freeport Ltd oversight; operating functions include financial compliance/audit, reporting and monitoring/evaluation. [DOC053-U0008-C0001] In tax-site investment governance, Investment Principles are implemented through agreements addressing reporting, monitoring/evaluation and subsidy obligations; landowners and the operating company monitor compliance, reporting to the Governance Board and accountable body, Falkirk Council. [DOC053-U0028-C0001]

Both use public seed capital and enabling projects to attract wider investment, with local-authority accountability and Freeport/partner delivery structures. The frozen reports describe proposals, expectations and approval/deployment arrangements; these figures do not establish completed expenditure or realised investment.

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A delivery/funding researcher needs to compare the two seed-capital programmes.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Both Freeports and the three comparison dimensions are explicit; report-time/prospective status is not explicit enough for the proposed gold.
- [ ] No accidental answer clue: Neutral comparison without figures; “use” can suggest observed deployment rather than business-case plans.
- [ ] Wording neutral and precise: researcher should decide the ISSUE/SUGGESTED_CHANGE below; candidate wording is unchanged.

### B. TASK_TYPE_INTEGRITY

- [ ] Both required documents materially required.
- [ ] Neither document alone supplies the complete comparison.

Preliminary assessment: DOC052 supplies Inverness/Cromarty selection, funding and Highland accountability; DOC053 supplies Forth selection, funding and company/Falkirk arrangements. Neither alone gives both programmes. Evidence integrity passes even though a wording clarification is recommended.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Covers scale, selection/deployment and governance for both, with prospective qualifiers. Forth financial-case total leverage and project-level match figures remain distinct. Tax-site Investment Principles are identified as investment governance, not universal seed-grant contract terms. The copied reference’s “submitted” phrasing should be revised to the explicitly supported “were invited to submit”; the invitation and completed submissions must not be conflated. This is a fuller reference than the others; equivalent concise coverage of these three dimensions should be accepted without demanding every named project. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Planned programme mechanism and achieved deployment are different defensible readings of “use”; a prospective source anchor is recommended.
- [ ] **Ambiguous dates:** The 2024 reports’ stages/expectations must not be treated as completed expenditure by September 2026. Different funding scenarios/levels must retain their labels.
- [ ] **Ambiguous entity names:** Highland Council is Inverness’s accountable body; Falkirk is Forth’s. Edinburgh’s membership is not a substitute accountable-body identity.
- [ ] **Source conflict:** Forth project-level match figures and financial-case leverage totals have different contexts; no reconciliation is asserted. No demonstrated contradictory programme description is identified. The reference says sponsors of 11 projects “submitted” OBCs, whereas U0012-C0001 says they were invited to submit; U0014-C0001 says individual OBCs informed the refreshed proposition but does not explicitly establish that every one of the 11 sponsors submitted. The stronger completion wording should be clarified.
- [ ] **Stale versus current within frozen corpus:** The frozen reports record 2024 FBC proposals; the reference is not a current implementation update.
- [ ] **Forecasts/examples versus realised/observed values:** Forecast leverage, asks and proposed projects are not realised spending/benefits. Seed capital totals are not LBTT claim totals.
- [ ] **Partial evidence and scoring fairness:** DOC052-U0012-C0002 adds no independent material fact. DOC053-U0028’s accountability passage concerns tax-site investment governance. Do not require unseen grant-contract detail or all project names for a concise complete response.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

Minor material-topic overlap with T013/T014 in approval/accountability, but neither answers the two-programme comparison, funding scales and selection/deployment. Not a duplicate. Job forecasts in its chunks are not part of T018’s requested answer and cannot answer T019.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** REVISION_RECOMMENDED

ISSUE=The question does not explicitly anchor “use” to the frozen business-case plans, while the candidate answer gives expected leverage and proposed deployment rather than achieved outcomes. Additionally, the copied reference says sponsors of 11 projects submitted OBCs; C0001 explicitly records an invitation to submit, and the later refreshed proposition does not explicitly establish completion by all 11 sponsors.

SUGGESTED_CHANGE=For the question: How do the frozen business-case reports describe the intended use of seed capital by the Inverness and Cromarty Firth and Forth Green Freeports to unlock investment, including funding scale, project selection/deployment and governance/accountability arrangements? For the reference answer: replace “Sponsors of 11 preferred projects submitted project OBCs” with “Sponsors of 11 preferred projects were invited to submit project OBCs”. Neither change is applied.

Suggestion only: no text has been applied. The researcher must decide whether to use this wording, retain the original with explicit scoring notes, or direct another revision. No job metric or claim-accounting convention is selected by this dossier.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T019

- **TASK_ID:** T019
- **TASK_TYPE:** insufficient_evidence
- **DIFFICULTY_CANDIDATE:** high — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** []

**EXACT_FINAL_CANDIDATE_QUESTION**

> How many jobs had actually been created by each of the Inverness and Cromarty Firth Green Freeport and the Forth Green Freeport by 31 March 2026?

**REFERENCE_EVIDENCE_CANDIDATE**

`[]` — absence-audit citations below are not gold evidence items.

**REFERENCE_ANSWER_CANDIDATE**

The frozen UC2 corpus does not provide enough evidence to determine how many jobs had actually been created by each Green Freeport by 31 March 2026. Its job-creation figures are forecasts or anticipated outputs rather than realised totals for that date.

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A researcher needs realised employment outcomes by a fixed date.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: Both Freeports and 31 March 2026 are explicit; actual creation excludes projections. Employment measure and attribution remain unspecified.
- [ ] No accidental answer clue: Neutral historical-outcome question; “actually” excludes forecasts without revealing their values or that evidence is absent.
- [ ] Wording neutral and precise: researcher should decide the ISSUE/SUGGESTED_CHANGE below; candidate wording is unchanged.

### B. TASK_TYPE_INTEGRITY

- [ ] No sufficient answer anywhere in all 293 canonical chunks.
- [ ] Plausible near-miss evidence exists.
- [ ] Near misses cannot legitimately satisfy the exact question.
- [ ] required_documents candidate remains [].
- [ ] reference_evidence candidate remains [].

Preliminary assessment: The absence audit covers all 293 chunks in 17 accepted documents. Forecasts/targets and related monitoring provide plausible near misses but no realised count for either programme through the cutoff. Event attendance and one recorded recruitment are not aggregate job-creation totals. REQUIRED_DOCUMENTS_CANDIDATE and REFERENCE_EVIDENCE_CANDIDATE are both [], as they must remain in any later insufficient-evidence task structure.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Minimal abstention says the frozen corpus cannot determine realised totals; forecasts explain the insufficiency. It does not claim zero jobs, no actual recruitment or absence from the world. No external statistics or extrapolated values are introduced. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Jobs could mean direct/gross/net, headcount/FTE or wider supply-chain impacts; attribution differs. This motivates a wording recommendation, not selecting a new metric here.
- [ ] **Ambiguous dates:** Cutoff is explicit. Ten-/25-year forecasts and mid-2040s objectives do not become achieved counts by 31 March 2026.
- [ ] **Ambiguous entity names:** Inverness/Cromarty and Forth are distinct; “Highlands” and “UK” splits are not counts for a different Freeport.
- [ ] **Source conflict:** Forecast totals differing in job scope are not conflicting actual observations; no realised programme count identified anywhere in the absence audit.
- [ ] **Stale versus current within frozen corpus:** The 2024 business-case reports and later NI/NDR guidance updates contain no requested actual totals; document age alone is not the absence proof.
- [ ] **Forecasts/examples versus realised/observed values:** 18,300/11,300 and 34,500/16,000/13,600 are forecasts; more than 600 expo attendees are not jobs; one recorded CEO recruitment is not a programme total.
- [ ] **Partial evidence and scoring fairness:** Accept an evidence-bounded abstention even if it mentions actual isolated recruitment. Never require a literal zero or penalise refusal to substitute forecasts. Define job-measure expectations before any final numerical scoring rule.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. T018 shares programme entities and nearby forecast passages but asks seed-capital mechanisms. T020 shares actual-outcome/date framing but asks a different fiscal measure.

### Corpus-wide absence-audit evidence and near-miss classes

The separate absence audit parsed all 293 chunks, represented all 17 accepted documents, used broad independent deterministic term-family scans and passage inspection, and enumerated every chunk with disposition and text hash. The ledger is reconciled here to all 293 canonical records. Its conclusion is limited to frozen canonical text, including extraction limitations; no live statistics or unseen PDF images/annexes were imported. It is not based on keyword zero-matches.

| Near-miss class | Grouped findings in absence audit | Key review evidence / exclusion |
|---|---:|---|
| FORECAST | 5 | DOC052-U0005-C0002, U0012-C0001, U0021-C0001: 18,300 UK/11,300 Highlands over long horizons; DOC053-U0007-C0001, U0009-C0001/C0002, U0018-C0001, U0037-C0001, U0049-C0001: projected 34,500/16,000/13,600. |
| TARGET | 1 | DOC041-U0001-C0013/C0014: increased jobs/wages as expected outcomes, not achieved counts. |
| ANTICIPATED_OUTPUT | 5 | Programme benefits/project categories and proposed staffing; DOC053-U0033-C0001 anticipates 16,000 direct jobs; DOC053-U0035-C0001 and DOC053-U0036-C0001 describe benefit categories. |
| GENERAL_POLICY | 9 | Skills, NI eligibility and reporting requirements; DOC041-C0036/C0039 and DOC043-C0025–C0027 require collection rather than provide populated returns. |
| ACTUAL_REALISED_VALUE | 0 | No achieved aggregate job-creation count for either programme at the cutoff. This class does not mean every actual event is absent. |
| IRRELEVANT | 4 | DOC052-U0010-C0001/C0002: >600 expo attendees, >30 exhibitors; DOC053-U0008-C0001: named CEO recruited; monetised labour effects and hypothetical employee examples. |

These are 24 grouped findings (J01–J24); overlap chunks and repeated forecasts are not independent counts. The actual CEO recruitment is acknowledged and cannot establish the requested programme totals. Reviewer should inspect the full J findings and 293-row ledger, not only the representative IDs above.

The proposed response is corpus-bounded insufficiency. Nothing in this review converts the audit citations into reference_evidence or required_documents, or changes the absence verdict because of the wording recommendation.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** REVISION_RECOMMENDED

ISSUE=The employment measure and attribution basis are unspecified (direct/gross/net, headcount/FTE and wider impacts). Absence remains confirmed under the plausible readings, but precision should be settled before freeze.

SUGGESTED_CHANGE=What realised job-creation totals, with their reported definitions of job type and attribution, does the frozen UC2 corpus provide separately for the Inverness and Cromarty Firth Green Freeport and the Forth Green Freeport by 31 March 2026?

Suggestion only: no text has been applied. The researcher must decide whether to use this wording, retain the original with explicit scoring notes, or direct another revision. No job metric or claim-accounting convention is selected by this dossier.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## T020

- **TASK_ID:** T020
- **TASK_TYPE:** insufficient_evidence
- **DIFFICULTY_CANDIDATE:** high — for review only
- **REQUIRED_DOCUMENTS_CANDIDATE:** []

**EXACT_FINAL_CANDIDATE_QUESTION**

> By 31 March 2026, what total amount of Land and Buildings Transaction Tax (LBTT) relief had actually been claimed for transactions in each of Scotland's two Green Freeports?

**REFERENCE_EVIDENCE_CANDIDATE**

`[]` — absence-audit citations below are not gold evidence items.

**REFERENCE_ANSWER_CANDIDATE**

The frozen UC2 corpus does not provide enough evidence to determine the total LBTT relief actually claimed in each Green Freeport by 31 March 2026. It supplies eligibility and claiming guidance and illustrative calculations, rather than aggregate realised claim amounts.

### A. QUESTION_QUALITY

- [ ] Realistic document-based information need: A researcher or fiscal analyst needs realised relief uptake separately by Freeport.
- [ ] Not a document-title/reference/identity lookup: the requested answer is substantive policy, process, comparison or outcome information; no title, URL or document ID is the answer.
- [ ] Actor, scope and timeframe clear: LBTT, each Scottish Freeport and 31 March 2026 are clear; gross/net claim accounting and aggregation start require researcher adjudication.
- [ ] No accidental answer clue: Neutral historical fiscal question; no rate, example value or absence clue appears.
- [ ] Wording neutral and precise: researcher should decide the ISSUE/SUGGESTED_CHANGE below; candidate wording is unchanged.

### B. TASK_TYPE_INTEGRITY

- [ ] No sufficient answer anywhere in all 293 canonical chunks.
- [ ] Plausible near-miss evidence exists.
- [ ] Near misses cannot legitimately satisfy the exact question.
- [ ] required_documents candidate remains [].
- [ ] reference_evidence candidate remains [].

Preliminary assessment: The absence audit covers all 293 chunks in 17 accepted documents. Eligibility, examples, start dates and reporting requirements are plausible near misses, but no actual LBTT aggregate exists for either programme through the cutoff. REQUIRED_DOCUMENTS_CANDIDATE and REFERENCE_EVIDENCE_CANDIDATE are both []; near-miss IDs are audit citations only.

### C. GOLD_QUALITY

- [ ] Answer strictly source-supported.
- [ ] Minimal but complete for the exact question.
- [ ] No outside knowledge.
- [ ] Qualifications and timeframes preserved.
- [ ] No unsupported causal or evaluative claims.

Preliminary assessment: Minimal abstention says the corpus cannot determine realised aggregate claims; guidance/examples explain the gap. It does not claim zero relief, deny claim availability or sum hypothetical calculations. No outside Revenue Scotland data are added. Reference prose above is copied from the authoritative audit; all source claims were checked against frozen text. For abstention candidates, the support is the corpus-wide absence audit rather than an answer-bearing chunk.

### D. AMBIGUITY / ADVERSARIAL CHECK

- [ ] **Multiple defensible answers:** Submitted/accepted claims, cumulative gross versus net after withdrawal, and starting period are unspecified; recommendation asks for reported basis rather than imposing one.
- [ ] **Ambiguous dates:** Cutoff is explicit. Designation/claim-start dates, example effective dates and return deadlines are not a reporting-period aggregate.
- [ ] **Ambiguous entity names:** Two Scottish Freeports are identifiable in DOC047. LBTT is distinct from NDR, NI and capital allowances; relief value is distinct from consideration or tax payable.
- [ ] **Source conflict:** No conflicting actual aggregate identified. Differences between legal eligibility windows, later tax measures and monetary projections cannot create a claims statistic.
- [ ] **Stale versus current within frozen corpus:** Frozen LBTT guidance has 2024 revision metadata; DOC046’s March 2026 update concerns NDR. No source is updated or reconciled with live tax statistics.
- [ ] **Forecasts/examples versus realised/observed values:** £39,062.50/£5,747.90 and past-tense “claimed” inside examples are hypothetical. SBA/ECA total claims and projected NDR zeros are not actual LBTT values.
- [ ] **Partial evidence and scoring fairness:** Claim-start dates and procedures give partial rule evidence but no aggregate dataset. Accept insufficiency; do not require zeros, sums of examples, or a net amount not supplied by the corpus.

### E. DUPLICATION CHECK

- [ ] Information need is distinct from the other nine tasks.

No duplicate answer requirement. T012 provides threshold rules but cannot answer realised claims; T019 concerns employment, with a distinct evidence-absence rationale.

### Corpus-wide absence-audit evidence and near-miss classes

The separate absence audit parsed all 293 chunks, represented all 17 accepted documents, used broad independent deterministic term-family scans and passage inspection, and enumerated every chunk with disposition and text hash. The ledger is reconciled here to all 293 canonical records. Its conclusion is limited to frozen canonical text, including extraction limitations; no live statistics or unseen PDF images/annexes were imported. It is not based on keyword zero-matches.

| Near-miss class | Grouped findings in absence audit | Key review evidence / exclusion |
|---|---:|---|
| ELIGIBILITY_RULE | 3 | DOC047 qualifying-use/threshold/withdrawal rules; DOC048 statutory conditions and amount-chargeable formulas. No transaction population. |
| WORKED_EXAMPLE | 6 | DOC047-U0001-C0004–C0011: hypothetical acquisitions, £39,062.50 and £5,747.90 relief in C0005/C0006, warehouse destruction/change of use, alternative finance and leases. |
| CLAIM_START_DATE | 1 | DOC047-U0001-C0001: 8 April/12 June 2024 availability for the two Freeports. No uptake amounts. |
| POLICY_DESCRIPTION | 6 | Relief offer, claim/return procedure, designation, oversight/data collection and programme reporting arrangements. |
| AGGREGATE_ACTUAL_CLAIM_VALUE | 0 | No aggregate actual LBTT claim amount for either Freeport through the cutoff and no underlying claim dataset. |
| IRRELEVANT | 5 | DOC046 NDR returns/awards; seed/NDR/investment projections; NI/SBA/ECA examples; customs/VAT/subsidy thresholds; printed-instrument prices. |

These are 21 grouped findings (L01–L21). Past-tense “claimed” in DOC047-C0007 remains within a worked example. Projected NDR income zeros, £120,000/£144,000 SBA examples and purchase consideration are not actual LBTT amounts. Reviewer should inspect the complete L findings and ledger, not only the representative IDs above.

The proposed response is corpus-bounded insufficiency. Nothing in this review converts the audit citations into reference_evidence or required_documents, or changes the absence verdict because of the wording recommendation.

### F. PROPOSED HUMAN-REVIEW VERDICT

**PROPOSED_HUMAN_REVIEW_VERDICT:** REVISION_RECOMMENDED

ISSUE=The aggregation start, submitted versus accepted claim status and treatment of withdrawn relief are unspecified. Absence remains confirmed, but the claim-accounting scope should be settled before freeze.

SUGGESTED_CHANGE=What cumulative amounts of LBTT relief claims, with their reported claim status, reporting period and treatment of withdrawals, does the frozen UC2 corpus provide separately for each of Scotland’s two Green Freeports up to 31 March 2026?

Suggestion only: no text has been applied. The researcher must decide whether to use this wording, retain the original with explicit scoring notes, or direct another revision. No job metric or claim-accounting convention is selected by this dossier.

**Researcher decision (unfilled):** ____________________

**Reviewer/date/rationale (unfilled):** ____________________

## Aggregate review

```text
TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
READY_FOR_RESEARCHER_DECISION=7
REVISION_RECOMMENDED=3
REJECT_RECOMMENDED=0
```

| Task | Final type | Difficulty candidate | Proposed review verdict |
|---|---|---|---|
| T011 | direct_retrieval | low | READY_FOR_RESEARCHER_DECISION |
| T012 | direct_retrieval | low | READY_FOR_RESEARCHER_DECISION |
| T013 | direct_retrieval | low | READY_FOR_RESEARCHER_DECISION |
| T014 | within_document_reasoning | medium | READY_FOR_RESEARCHER_DECISION |
| T015 | within_document_reasoning | medium | READY_FOR_RESEARCHER_DECISION |
| T016 | within_document_reasoning | medium | READY_FOR_RESEARCHER_DECISION |
| T017 | cross_document_reasoning | high | READY_FOR_RESEARCHER_DECISION |
| T018 | cross_document_reasoning | high | REVISION_RECOMMENDED |
| T019 | insufficient_evidence | high | REVISION_RECOMMENDED |
| T020 | insufficient_evidence | high | REVISION_RECOMMENDED |

The three revision recommendations concern **wording and gold precision for researcher adjudication**. T018 also flags a stronger submission-completion claim than its passage explicitly establishes; the corpus-absence conclusions remain unchanged. The two earlier audits’ verdicts remain intact. Seven ready-for-decision recommendations do not signify approval; all ten require actual researcher review. No rejection is recommended from these inputs.

### Aggregate checks

| Check | Preliminary result | Evidence and limits |
|---|---|---|
| SCHEMA_COMPATIBILITY_PRECHECK | PASS — candidate field shapes only | Existing `benchmark/schema/task.schema.json` accepts the ten task IDs/types, low/medium/high difficulty, document arrays and document/chunk/page/section evidence fields. Empty arrays are permitted for insufficient_evidence. Schema requires schema_version 0.1 and validation_status on eventual tasks; if tasks are later authorized before verification their status must remain draft. Dossier review fields/verdicts are not extra task-schema properties. No task JSON or finalized schema validation is performed. |
| SOURCE_TRACEABILITY | PASS | 18 unique proposed gold chunk IDs exist exactly once, with matching document metadata, accepted membership, source-unit/page locators and text hashes. Audit context and absence-citation IDs also exist; input hashes and source ledger appear below. |
| TASK_TYPE_INTEGRITY | PASS — final candidates | 3 localized, 3 genuine within-document comparisons (including T014 Revision 1), 2 both-document comparisons and 2 corpus-wide absence cases. Original T014 failure is retained as history, not counted as a current candidate. |
| REFERENCE_ANSWER_SUPPORT | REVIEW_REQUIRED — T018 submission wording | Answers copied unchanged from authoritative audits and checked against frozen text or reconciled absence ledger. T018’s “submitted” wording is stronger than the explicit invitation-to-submit passage; proposed correction is shown without changing the candidate. Other answer claims are supported with qualifications. Optional elaboration identified. No model/result-driven gold introduced; researcher verification outstanding. |
| AMBIGUITY_AUDIT | REVIEW_REQUIRED — T018/T019/T020 | All seven adversarial dimensions inspected per task. Prospective phrasing, job definitions and claim-accounting basis motivate three recommendations. Cross-version deadlines in T011/T017 are explicitly visible; researcher should confirm the measure-specific source anchor. No silent question rewrite or live-policy adjudication. |
| DUPLICATION_AUDIT | PASS — no duplicate answer requirement identified | All 45 task pairs considered by information need; related seed/NDR and LBTT subjects require distinct facts/comparisons/outcomes. Per-task overlap assessments above. |
| GOLD_LEAKAGE_AUDIT | PASS — static, bounded check | Dossier stays under evidence/engineering, outside canonical JSONL; no corpus/config/runtime/task JSON changed. Existing task loader projects only task_id/question through RuntimeTask; reference answer/evidence/documents/type/difficulty remain benchmark-side fields. Loader directory reads T*.json, not this Markdown dossier. No runtime execution or end-to-end isolation test is claimed. Researcher dossier itself contains gold and must remain review-side when later packaging tasks. |
| INSUFFICIENT_EVIDENCE_AUDIT | PASS — canonical-text boundary | Authoritative absence ledger reconciles 293/293 records in 17 accepted documents. Broad positive hits are classified, including actual-but-nonaggregate recruitment and hypothetical “claimed” cases. T019/T020 candidate document/evidence arrays remain empty. Extraction limitations and outside-data boundary preserved. |

### Static precheck scope

Read-only inspection of `benchmark/schema/task.schema.json` and `src/responsible_agentic_workflows/benchmark/tasks.py` supports the schema/gold-isolation prechecks. No module, task loader, workflow, model or benchmark was executed. Existing configuration path references were inspected only as text; no model-qualification, retrieval-diagnostic or benchmark-result artifact was opened. Nothing was written outside the new dossier.

### Dossier provenance

```text
LLM_ASSISTED_AUTHORING=YES
HUMAN_DIRECTED_TASK_DESIGN=YES
HUMAN_VERIFICATION_COMPLETED=NO
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
TASK_JSON_CREATED=NO
EMBEDDINGS_USED=NO
MODEL_BENCHMARK_OUTPUT_USED=NO
DIAGNOSTIC_RETRIEVAL_USED=NO
COMMIT=NO
PUSH=NO
```

## Input fingerprints and source locators

| Input | SHA256 |
|---|---|
| `evidence/engineering/uc2_task_candidate_evidence_audit_2026-09-26.md` | `728fe36bcfd3097005594053ffef69cb6ac586a09964be5579a2ee9437f15d56` |
| `evidence/engineering/uc2_insufficient_evidence_absence_audit_2026-09-26.md` | `e068d2c40c378d8b8bb276f6903a0f52502edcab39b301bca9a0106e6eb2f57d` |
| `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl` | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| `benchmark/task_authoring_protocol_v0.1.json` | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |
| `corpus/use_cases/UC2/corpus_membership.json` | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| `benchmark/schema/task.schema.json` | `34ddb275e659b86d759d5fabcf3500bc963c34b60425f601677b88bbb858145f` |
| `src/responsible_agentic_workflows/benchmark/tasks.py` | `f00997f2aba8b089d93a845dbe08329e1165cb89982feb1a582844be6288a18c` |

### Proposed reference-evidence fingerprint ledger

| Task | Chunk | Canonical line | Source unit | Word range | PDF page | Text SHA256 |
|---|---|---:|---|---|---|---|
| T011 | DOC046-U0001-C0002 | 122 | DOC046-U0001 | [375, 825) | null (HTML) | `43663cab2ac84b0b54dcd33e0d807b978eb1ad19e987a67d52cca3648cb912b5` |
| T012 | DOC047-U0001-C0001 | 129 | DOC047-U0001 | [0, 450) | null (HTML) | `fa069a33efb872292b8973d62a10a6354d4b364968470bb05871d51ae1a4263a` |
| T013 | DOC058-U0001-C0002 | 292 | DOC058-U0001 | [375, 825) | null (HTML) | `a87859c86f6410c4ea80228c62be1986f8dbaad4435726cd6b1d1298e89237ec` |
| T014 | DOC043-U0001-C0004 | 67 | DOC043-U0001 | [1125, 1575) | null (HTML) | `95663526d60c0445717fa1cfef26de5225ff2da92cac571c97bb172b9e91b7b6` |
| T014 | DOC043-U0001-C0009 | 72 | DOC043-U0001 | [3000, 3450) | null (HTML) | `804fa98a7dcf9806e5590166d1b81762e91c77a781e8e4ae90ad169d31438e04` |
| T015 | DOC045-U0001-C0002 | 118 | DOC045-U0001 | [375, 825) | null (HTML) | `a506381d377985cdb69d6a61bcdb83bfb828f608c310ccb9a3cc05e124673a3f` |
| T015 | DOC045-U0001-C0003 | 119 | DOC045-U0001 | [750, 1200) | null (HTML) | `69e486edfc05a05a5849821173e715874223986cdd054a4b425bc49cee11ea27` |
| T016 | DOC051-U0004-C0002 | 169 | DOC051-U0004 | [375, 701) | null (HTML) | `70bdbf8f9adf895ede400aee8d38827f2123266e5bc668597fb4822947f5c879` |
| T016 | DOC051-U0005-C0001 | 170 | DOC051-U0005 | [0, 450) | null (HTML) | `5f2e48c16af1d40cea75fb3acf0fa7ab43b85de074ee52ffc7be23358a6db411` |
| T017 | DOC056-U0001-C0001 | 284 | DOC056-U0001 | [0, 450) | null (HTML) | `850c8f841a6964039b5cd1667fc700d25b85369ceb4ebeed74b6b1b63c59ad2f` |
| T017 | DOC056-U0001-C0002 | 285 | DOC056-U0001 | [375, 825) | null (HTML) | `59448e424670bb8a46b0bfb8a74798faf9149c155a52e302c0807c2a2ea86d62` |
| T017 | DOC057-U0001-C0001 | 287 | DOC057-U0001 | [0, 450) | null (HTML) | `ae6e863d5300a974fef0ff52cf9ad52ebc0c3e6848140fc2cc1780d0697f6edb` |
| T017 | DOC057-U0001-C0002 | 288 | DOC057-U0001 | [375, 825) | null (HTML) | `3d3a615ce5a96557e53bd9b7addc30d609866f24b7b45667b136c7b0bc09c5eb` |
| T018 | DOC052-U0012-C0001 | 202 | DOC052-U0012 | [0, 450) | 12 | `67964d32e0d957be9ca28c2cf124cc6b9960f727f7a0bd85fc5ad66057f14ce3` |
| T018 | DOC052-U0014-C0001 | 206 | DOC052-U0014 | [0, 450) | 14 | `b4a5454740f28208a58d3ad3572309a252f479ff71a48f6fa9825d75deb60154` |
| T018 | DOC053-U0008-C0001 | 236 | DOC053-U0008 | [0, 438) | 8 | `f0d4496da0da8c33582a7a15f3d712761a67e3c1d772e3809d5606ed529ba4e0` |
| T018 | DOC053-U0027-C0001 | 256 | DOC053-U0027 | [0, 243) | 27 | `9e530375a51793b8e24666f31533369b9686a0e2c5271fada92aa1251405af33` |
| T018 | DOC053-U0028-C0001 | 257 | DOC053-U0028 | [0, 393) | 28 | `b86f1b34a4b4877452cc9bbb4ce2417424eb44917b6b5d5bb95297725961475c` |

For T019/T020, the authoritative absence audit supplies the complete 293-record fingerprint/disposition ledger and all grouped J/L findings. Its current byte hash is pinned above. Empty gold arrays are intentional, not omitted traceability. All named non-gold context and near-miss IDs in this dossier were verified to exist in canonical text.


## Researcher-Directed Pre-Freeze Precision Revisions

This append-only section records researcher-directed Revision 1 for T018, T019 and T020 on 26 September 2026. It supersedes their earlier proposed questions/answers/verdicts for the **current review candidate** only. All original wording, stronger T018 submission wording, ISSUE/SUGGESTED_CHANGE recommendations and historical aggregate counts remain above, unchanged. T014 remains its previously designated final human-directed Revision 1; its original task-type defect history is preserved. No researcher acceptance, human verification or task freeze is recorded here.

The scope is the three supplied precision revisions, T018's authorised gold correction, and source-only re-evaluation of the two revised absence questions. T011–T017 are carried forward without revision. A proposed READY verdict means a researcher can decide; it does not constitute approval. A remaining T020 entity/scope defect is explicitly retained for decision rather than silently corrected.

### Revision inputs and preservation controls

| Input | SHA256 before this revision |
|---|---|
| Earlier candidate evidence audit (unchanged) | `728fe36bcfd3097005594053ffef69cb6ac586a09964be5579a2ee9437f15d56` |
| Earlier corpus-wide absence audit (unchanged) | `e068d2c40c378d8b8bb276f6903a0f52502edcab39b301bca9a0106e6eb2f57d` |
| Human-review dossier before append | `692fecdccea34e87503926fd1f3632036aff6838eeaf9137a0673a30ab339650` |
| Canonical UC2 chunks.jsonl | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| Frozen corpus_membership.json | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| Frozen task_authoring_protocol_v0.1.json | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |

Branch and HEAD match `research/benchmark-task-construction-uc2-uc3` and `4ca03cde8dd969c07590670615008b17d5448a2e`. The original dossier is 78,632 bytes; those bytes are retained as an identical prefix, with this section appended. The two earlier audit files remain separate immutable inputs for this step. No source, protocol, schema, runtime file or task JSON is changed.

### Repeated corpus-wide insufficiency method and coverage

The canonical JSONL was parsed anew in physical file order: **293 records, 293 unique chunk IDs, 17 accepted documents**, exactly the membership set, with no DOC054. Each text SHA256 was recomputed and validated. All 293 records were reconciled by canonical line, ID and text hash against the earlier absence audit's complete disposition ledger. That ledger and all J01–J24/L01–L21 grouped findings are retained as the complete screening record, tied to its immutable input hash above.

The four broad deterministic term-family scans were rerun against **every** canonical text field, using the definitions below. Matching is case-insensitive, unranked and not limited to top-k. Their unions preserve broad employment/outcome and tax/value/reporting contexts; nonhits remain enumerated in the reconciled ledger. Numeric/currency and structural screening from that corpus-wide audit is retained. All grouped findings were re-assessed for the revised scope in the tables below; focused direct source re-reading checks the job forecasts, tax-site descriptions, individual programme recruitment, future monitoring and LBTT return examples/procedure. This repeat assessment combines complete enumeration, reproducible broad positive scans, the reconciled full screening record and substantive near-miss interpretation. It does not infer absence from zero keyword hits, corpus age, or a small selected evidence set.

**T019_CORE**

```regex
\b(?:jobs?|job[- ]creation|employ\w*|unemploy\w*|workers?|workforce|work[- ]force|labou?r|FTEs?|headcount|recruit\w*|vacanc\w*|staff\w*|skills?|hir\w*|apprentice\w*|redundan\w*|posts?|positions?)\b
```

**T019_OUTCOMES**

```regex
\b(?:outcomes?|outputs?|monitor\w*|report\w*|evaluat\w*|deliver\w*|achiev\w*|realis\w*|realiz\w*|actual\w*|creat\w*|progress|baseline|statistics?|data|figures?|numbers?|complet\w*|2026|31\s+March)\b
```

**T020_TAX**

```regex
\b(?:LBTT|land\s+(?:and|&)\s+buildings?\s+transaction\s+tax|Revenue\s+Scotland|tax\w*|relief\w*|exempt\w*|SDLT|stamp\s+duty)\b
```

**T020_VALUES**

```regex
\b(?:claims?|claimed|claiming|amounts?|values?|statistics?|aggregat\w*|total\w*|cumulat\w*|uptake|take[- ]up|receipts?|refund\w*|repaid|repay\w*|data|figures?|numbers?|2026|31\s+March)\b
```

| Scan | Matching chunks | Nonmatching chunks |
|---|---:|---:|
| T019_CORE | 142 | 151 |
| T019_OUTCOMES | 222 | 71 |
| T019 union | 231 | 62 |
| T020_TAX | 198 | 95 |
| T020_VALUES | 173 | 120 |
| T020 union | 244 | 49 |

| Accepted document | Chunks enumerated | T019 union hits | T020 union hits |
|---|---:|---:|---:|
| DOC041 | 53 | 50 | 43 |
| DOC042 | 10 | 9 | 8 |
| DOC043 | 40 | 39 | 37 |
| DOC044 | 13 | 13 | 12 |
| DOC045 | 4 | 4 | 4 |
| DOC046 | 8 | 8 | 8 |
| DOC047 | 11 | 3 | 11 |
| DOC048 | 10 | 0 | 9 |
| DOC049 | 5 | 0 | 4 |
| DOC050 | 4 | 0 | 3 |
| DOC051 | 25 | 12 | 17 |
| DOC052 | 45 | 35 | 30 |
| DOC053 | 50 | 47 | 44 |
| DOC055 | 5 | 5 | 5 |
| DOC056 | 3 | 2 | 3 |
| DOC057 | 4 | 1 | 4 |
| DOC058 | 3 | 3 | 2 |
| **Total** | **293** | **231** | **244** |

The date cutoff is not treated as evidence that all material is older: DOC046 includes a 25 March 2026 update and DOC055 a 6 April 2026 update. These are NDR/NI guidance, not the requested actual totals. Frozen extraction limits remain: page-number-only or figure-title-only chunks are included as supplied text; unseen images, linked annexes and external administrative datasets are not imported. Absence below concerns this canonical corpus, not real-world nonexistence or zero outcomes.

### T018 Revision 1

```text
TASK_ID=T018
TASK_TYPE=cross_document_reasoning
DIFFICULTY_CANDIDATE=high
REQUIRED_DOCUMENTS_CANDIDATE=[DOC052, DOC053]
REFERENCE_EVIDENCE_CANDIDATE=[DOC052-U0012-C0001, DOC052-U0014-C0001, DOC053-U0008-C0001, DOC053-U0027-C0001, DOC053-U0028-C0001]
ORIGINAL_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
REVISION_REASON=Make business-case planned deployment explicit and correct invitation-to-submit wording without asserting all 11 preferred-project sponsors submitted OBCs.
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
```

**EXACT_FINAL_CANDIDATE_QUESTION — supplied Revision 1**

> According to their business-case documents, how are the Inverness and Cromarty Firth and Forth Green Freeports planned to use seed capital to unlock investment, including funding scale, project selection/deployment, and governance/accountability arrangements?

**Gold correction and evidence re-verification.** DOC052-U0012-C0001 explicitly supports an invitation, not completed submission by all 11 sponsors. The corrected answer states: “project sponsors responsible for the 11 preferred seed capital projects were invited to submit individual project OBCs to the Council for assessment.” DOC052-U0014-C0001 says the proposition was refreshed taking account of individual OBCs; it does not certify that every sponsor submitted. The earlier stronger answer is preserved above as historical text and is superseded for review by the answer below.

| Chunk | Classification | Material answer contribution |
|---|---|---|
| DOC052-U0012-C0001 | REQUIRED | £25m enabling infrastructure, 11 preferred projects, invitation for individual OBCs and Council gateway/Green Book assessment. |
| DOC052-U0014-C0001 | REQUIRED | Award-dependent FBC review, investment subgroup, subsidy-control assessment/change requests, Highland Council accountability versus partner delivery, and planned circa £260m project funding. |
| DOC053-U0008-C0001 | REQUIRED | Expected £96.9m financial-case totals, procurement and operating/parent-company governance/compliance functions. |
| DOC053-U0027-C0001 | REQUIRED | Investment Hierarchy/local-authority appraisal, four core projects, £17.9m minimum/£24.5m maximum asks and additional projects/match funding. |
| DOC053-U0028-C0001 | REQUIRED | Early seed-capital investment lever and tax-site Investment Principles/contractual reporting and compliance, including accountable body Falkirk Council. |
| DOC052-U0012-C0002 | REDUNDANT | Overlap/continuation does not add a necessary substantive answer element. It remains context, outside the proposed gold list. |

All six named chunks exist exactly once, with accepted document membership and matching text hashes. The unchanged earlier dossier fingerprint ledger supplies exact lines, source units, pages and hashes for the five proposed gold chunks.

**REFERENCE_ANSWER_CANDIDATE — corrected, source-supported**

Inverness and Cromarty Firth proposes £25m of seed capital for enabling infrastructure that unlocks tax-site land. Project sponsors responsible for the 11 preferred seed capital projects were invited to submit individual project OBCs to the Council for assessment. The gateway test determines whether projects proceed to FBC; the OBC template followed Green Book principles, with the process assessing expected economic benefits, viability and affordability. [DOC052-U0012-C0001] Following confirmation of the award, sponsors are to submit FBCs to the accountable body, reviewed by an investment subgroup comprising Freeport-company and Highland Council representatives, with further subsidy-control checks and government change requests for reserve-list alternatives if necessary. Highland Council is accountable for accounting and public governance; the Freeport and partners deliver the programme and manage delivery, risk and outcomes. The £25m is to be complemented by over £60m further public funding and almost £175m private funding, giving around £260m total seed-capital project expenditure. [DOC052-U0014-C0001]

Forth plans to use early seed capital as an investment lever. [DOC053-U0028-C0001] Proposals were assessed/prioritised in line with the Scottish Government Investment Hierarchy and considered by local-authority partners. Four core projects—Forth Ports Leith land preparation, Babcock integrated energy system, Grangemouth utility capacity and INEOS low-carbon hydrogen preparation—require a minimum £17.9m ask, attracting at least £17.9m private match funding. The maximum £24.5m ask enables six additional projects costing £6.6m, with £12.9m partner match funding. [DOC053-U0027-C0001] The financial case expects £24.5m seed capital to attract £8m further public and £64.4m private funding, for circa £96.9m overall project expenditure; these are the financial-case totals, distinct from the proposal-level match-funding figures. Procurement is by private landowners and other sponsors, including public bodies, aligned with general public procurement rules. Forth Green Freeport Operating Ltd delivers under Forth Green Freeport Ltd oversight; operating functions include financial compliance/audit, reporting and monitoring/evaluation. [DOC053-U0008-C0001] In tax-site investment governance, Investment Principles are implemented through agreements addressing reporting, monitoring/evaluation and subsidy obligations; landowners and the operating company monitor compliance, reporting to the Governance Board and accountable body, Falkirk Council. [DOC053-U0028-C0001]

Both business cases plan to use public seed capital and enabling projects to attract wider investment, with local-authority accountability and Freeport/partner delivery structures. The frozen reports describe proposals, expectations and approval/deployment arrangements; these figures do not establish completed expenditure or realised investment.

**A. QUESTION_QUALITY.** A realistic comparison of planned delivery and public accountability, rather than a title/identity lookup. Both actors and the three requested dimensions are explicit. “According to their business-case documents” and “planned” anchor the source/timeframe without suggesting realised implementation or leaking funding figures, project choices or the answer.

**B. TASK_TYPE_INTEGRITY.** Both documents remain materially necessary. DOC052 supplies ICFGF's £25m scheme, Council invitation/gateway and accounting-versus-delivery roles; it cannot supply Forth's project-selection asks or financial/governance structure. DOC053 supplies Forth's four/six-project options, financial totals and operating-company/Investment Principles oversight; it cannot establish ICFGF's invitation, subgroup or funding scale. Removing either document leaves an entire side of the requested comparison unanswerable. Cross-document reasoning is valid.

**C. GOLD_QUALITY.** Invitation wording now matches the explicit source; no claim that all 11 sponsors submitted or passed assessment is made. Funding remains planned/expected and conditional review procedures remain conditional. Forth proposal-level match figures remain distinguished from overall financial-case totals. Tax-site governance context is labelled as such, rather than presented as a seed-grant approval process. No outside fact or unsupported realised expenditure/causal result is added.

**D. AMBIGUITY / ADVERSARIAL CHECK.** Multiple source-supported summaries can express the same dimensions; grading should accept semantic equivalents. Business-case chronology is explicit. Named Freeports and their distinct accountable bodies are clear. Minimum/maximum asks and different match-funding scopes are scenarios, not a hidden contradiction. Forecast/planned investment is not realised investment; no worked example is treated as an observation. Partial evidence from either document remains inadequate. No unresolved wording defect identified.

**E. DUPLICATION CHECK.** Domain overlap with T013 (subsidy eligibility) and T014 (generic seed/NDR financing/accountability) is acceptable: this question requires two named business cases, their project choices and funding structures. T019 asks reported actual site jobs; T020 asks actual LBTT claim totals. No duplicate answer requirement.

```text
NEW_PROPOSED_VERDICT=READY_FOR_RESEARCHER_DECISION
ISSUE=NONE_REMAINING_IDENTIFIED
HUMAN_VERIFICATION_COMPLETED=NO
```

### T019 Revision 1

```text
TASK_ID=T019
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=medium
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
ORIGINAL_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
REVISION_REASON=Constrain the requested employment measure to reported actual job creation on designated tax sites, separately for the two Green Freeports, by 31 March 2026.
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
```

**EXACT_FINAL_CANDIDATE_QUESTION — supplied Revision 1**

> By 31 March 2026, how many jobs were reported as actually created on the designated tax sites of each of the Inverness and Cromarty Firth Green Freeport and the Forth Green Freeport?

**Corpus-wide re-evaluation and near misses.** A sufficient observation must establish actual created jobs on designated tax sites, attributed to the relevant Freeport, with reporting scope adequate to the cutoff. A UK/Highlands projection, baseline employment, an event attendee or a programme staff member is not that measure. None of the 293 canonical texts supplies a sufficient realised tax-site count for **either** Freeport; therefore neither a single-side sufficient count nor a complete pair is being concealed by the aggregate conclusion. All original grouped job findings are reconsidered below for this narrower wording. These citations are absence-audit context, not candidate reference_evidence.

| Finding | Classification | Exact canonical chunks | Frozen content (paraphrase) | Revised-question sufficiency test |
|---|---|---|---|---|
| J01 | GENERAL_POLICY | DOC041-U0001-C0001; DOC041-U0001-C0002; DOC041-U0001-C0003; DOC041-U0001-C0004; DOC041-U0001-C0005; DOC041-U0001-C0006; DOC041-U0001-C0007; DOC041-U0001-C0008; DOC041-U0001-C0009; DOC041-U0001-C0010; DOC041-U0001-C0011; DOC041-U0001-C0012 | Prospectus job-creation, fair-work, sector and skills ambitions; mechanisms for attracting employment. | Policy intentions contain no reported actual tax-site job counts for either Freeport. |
| J02 | TARGET | DOC041-U0001-C0013; DOC041-U0001-C0014 | Expected outcomes include increased jobs and wages, with future assessment through monitoring/evaluation. | Desired increased employment is a target, not a reported realised tax-site count by the cutoff. |
| J03 | GENERAL_POLICY | DOC041-U0001-C0018; DOC041-U0001-C0019; DOC041-U0001-C0020; DOC042-U0001-C0004; DOC042-U0001-C0005; DOC043-U0001-C0036; DOC043-U0001-C0037; DOC043-U0001-C0038 | Regeneration/underdevelopment tests, above-average unemployment, requests for current employee estimates and estimated additional/future employment. | Baseline employees, unemployment and requested future employment estimates cannot establish jobs actually created on designated sites. |
| J04 | GENERAL_POLICY | DOC041-U0001-C0031; DOC041-U0001-C0032; DOC041-U0001-C0036; DOC041-U0001-C0038; DOC041-U0001-C0039; DOC041-U0001-C0040; DOC041-U0001-C0042; DOC041-U0001-C0043; DOC041-U0001-C0047; DOC041-U0001-C0048; DOC041-U0001-C0049; DOC042-U0001-C0005; DOC042-U0001-C0006 | Decarbonisation/job-creation plans, bid-selection criteria, implementation milestones, annual reporting and required data collection on new jobs/realised outcomes. | Required collection of realised jobs is not a populated return. No actual tax-site count is supplied. |
| J05 | GENERAL_POLICY | DOC043-U0001-C0006; DOC043-U0001-C0007; DOC043-U0001-C0009; DOC043-U0001-C0014; DOC043-U0001-C0015; DOC043-U0001-C0017; DOC043-U0001-C0018; DOC043-U0001-C0019; DOC043-U0001-C0020; DOC043-U0001-C0021; DOC043-U0001-C0022; DOC043-U0001-C0023; DOC043-U0001-C0024; DOC043-U0001-C0025; DOC043-U0001-C0026; DOC043-U0001-C0027; DOC043-U0001-C0032; DOC043-U0001-C0033; DOC043-U0001-C0034; DOC043-U0001-C0035 | Setup guidance covers workforce/skills, innovation, recruitment planning and future monthly/quarterly/biannual/annual monitoring; Q4 and annual periods can end 31 March. | Future reporting cycles, including 31 March period ends, are not actual 2026 job returns. |
| J06 | GENERAL_POLICY | DOC044-U0001-C0001; DOC044-U0001-C0002; DOC044-U0001-C0003; DOC044-U0001-C0004; DOC044-U0001-C0005; DOC044-U0001-C0008; DOC044-U0001-C0009; DOC044-U0001-C0010; DOC044-U0001-C0011; DOC044-U0001-C0012; DOC044-U0001-C0013; DOC045-U0001-C0001; DOC046-U0001-C0004; DOC047-U0001-C0001; DOC051-U0002-C0001 | Impact/policy guidance describes high-quality jobs, apprenticeship/skills benefits, controls, monitoring and the programme objectives. | Policy rationale and monitoring language supply no actual tax-site employment observation. |
| J07 | FORECAST | DOC052-U0005-C0002 | Proposals estimated to enable 18,300 long-term UK jobs over the next 25 years, alongside investment/NDR projections. | The 25-year UK projection is neither a realised count nor the requested designated-site measure. |
| J08 | FORECAST | DOC052-U0012-C0001 | 18,300 UK jobs, 11,300 in the Highlands, explicitly forecast with investment/jobs over a 25-year period. | Both UK and Highlands figures are explicit forecasts; geographic subdivision does not make them actual site counts. |
| J09 | FORECAST | DOC052-U0021-C0001 | Potential 25-year tax-site development pipeline could create 18,300 UK jobs, 11,300 in the Highlands; estimates include operational, construction, indirect and induced jobs. | Even this tax-site pipeline passage is conditional over 25 years and includes construction, indirect and induced effects beyond on-site operational employment. |
| J10 | ANTICIPATED_OUTPUT | DOC052-U0001-C0001; DOC052-U0002-C0001; DOC052-U0003-C0001; DOC052-U0003-C0002; DOC052-U0004-C0001; DOC052-U0005-C0001; DOC052-U0006-C0001; DOC052-U0006-C0002; DOC052-U0007-C0001; DOC052-U0011-C0001; DOC052-U0013-C0001; DOC052-U0019-C0001; DOC052-U0020-C0001; DOC052-U0020-C0002 | Expected employment/community benefits, planned green-economy growth and projected project outputs; approved housing is linked to anticipated employment growth. | Anticipated benefits and approved housing/infrastructure do not report actual jobs created on designated tax sites. |
| J11 | GENERAL_POLICY | DOC052-U0008-C0001; DOC052-U0008-C0002; DOC052-U0009-C0001; DOC052-U0009-C0002; DOC052-U0010-C0001; DOC052-U0015-C0001; DOC052-U0016-C0001; DOC052-U0017-C0001; DOC052-U0018-C0001; DOC052-U0022-C0001; DOC052-U0022-C0002; DOC052-U0023-C0001 | Skills provision, equalities baseline update, company governance and monitoring/evaluation/reporting commitments and future collection of indicators. | Governance, skills and prospective indicators do not supply a realised tax-site job count. |
| J12 | IRRELEVANT | DOC052-U0010-C0001; DOC052-U0010-C0002 | A held careers expo attracted more than 600 young people and more than 30 exhibitors. | These are actual event attendance/exhibitor counts, not actual jobs on tax sites. |
| J13 | ANTICIPATED_OUTPUT | DOC052-U0023-C0001 | CEO is putting together a team of five full-time staff, with potential for two further roles. | Putting together five staff with possible two later roles is not proof of hires, and company staffing is not the requested aggregate tax-site outcome. |
| J14 | FORECAST | DOC053-U0007-C0001; DOC053-U0009-C0001; DOC053-U0009-C0002; DOC053-U0018-C0001 | Projected Forth creation/support of up to 34,500 jobs; 16,000 direct in U0009; economic-impact assessment and ten-year investment context in U0018. | The repeated 34,500 and 16,000 figures remain projections; none is a reported actual tax-site count by 31 March 2026. |
| J15 | ANTICIPATED_OUTPUT | DOC053-U0033-C0001 | Anticipated outputs include 16,000 direct jobs on tax-site land and around £260m land-value uplift. | The explicit 16,000 direct Tax Site jobs is the closest location-matched near miss, but is introduced as an anticipated output, not a realised report. |
| J16 | FORECAST | DOC053-U0037-C0001; DOC053-U0049-C0001 | Forth will generate 16,000 direct jobs, anticipated up to 34,500 gross jobs and likely 13,600 UK net additional in U0037; conclusion seeks approximately 34,500 gross jobs in U0049. | Will generate, anticipated and likely frame future economic benefits; no actual on-site count or cutoff observation is supplied. |
| J17 | ANTICIPATED_OUTPUT | DOC053-U0035-C0001; DOC053-U0036-C0001 | Seed-project appraisal and categories describe creating jobs directly and accelerating creation. U0035 uses past-tense wording about seed capital being employed, within a potential-impact appraisal assuming Maximum Ask funding. | Maximum-Ask appraisal and create-jobs benefit categories contain no actual numerical site employment return, despite one past-tense phrase. |
| J18 | ANTICIPATED_OUTPUT | DOC053-U0008-C0001; DOC053-U0046-C0001 | Three remaining operating-company manager posts anticipated before year end; CEO to recruit three staff by Spring 2025. | Anticipated three manager posts/Spring 2025 recruitment do not certify recruitment; operating-company staff are not tax-site outcome totals. |
| J19 | IRRELEVANT | DOC053-U0008-C0001 | A named Chief Executive has been recruited and is to take up the post in August 2024. | Actual CEO recruitment is acknowledged. It is an individual programme appointment, not a reported actual designated-tax-site job-creation aggregate for either Freeport. |
| J20 | GENERAL_POLICY | DOC053-U0005-C0001; DOC053-U0011-C0001; DOC053-U0012-C0001; DOC053-U0020-C0001; DOC053-U0021-C0001; DOC053-U0022-C0001; DOC053-U0023-C0001; DOC053-U0024-C0001; DOC053-U0025-C0001; DOC053-U0026-C0001; DOC053-U0028-C0001; DOC053-U0030-C0001; DOC053-U0032-C0001; DOC053-U0039-C0001; DOC053-U0040-C0001; DOC053-U0043-C0001; DOC053-U0045-C0001; DOC053-U0047-C0001 | Skills access, deprivation, clusters, tax-site development, operational/governance roles and worker representation. | Qualitative intended site/skills benefits and company personnel powers contain no achieved site count. |
| J21 | GENERAL_POLICY | DOC053-U0008-C0001; DOC053-U0013-C0001; DOC053-U0028-C0001; DOC053-U0045-C0001; DOC053-U0048-C0001; DOC053-U0049-C0001 | Operating-company reporting, annual committee reports, investment monitoring and future bespoke M&E/indicator reporting. | Reporting arrangements and a future bespoke M&E framework are not the reported results requested. |
| J22 | IRRELEVANT | DOC053-U0038-C0001 | Monetised employment-multiplier, labour-supply and productivity benefits, with GVA and net-benefit estimates. | Monetised labour/economic effects are not a count of actual jobs created on designated tax sites. |
| J23 | GENERAL_POLICY | DOC041-U0001-C0022; DOC041-U0001-C0023; DOC055-U0001-C0001; DOC055-U0001-C0002 | National Insurance eligibility for employees and payroll/RTI reporting rules. | Employee eligibility and required payroll fields do not report actual site-created job counts. |
| J24 | IRRELEVANT | DOC055-U0001-C0003; DOC055-U0001-C0004; DOC055-U0001-C0005; DOC051-U0006-C0001; DOC051-U0006-C0002 | Hypothetical employee/payroll examples and guidance updates; goods used to support a workforce. | Hypothetical payroll examples and generic workforce references are not observed tax-site job creation. |

| Near-miss classification | Grouped findings |
|---|---:|
| FORECAST | 5 |
| TARGET | 1 |
| ANTICIPATED_OUTPUT | 5 |
| GENERAL_POLICY | 9 |
| ACTUAL_REALISED_VALUE (requested metric) | 0 |
| IRRELEVANT | 4 |
| **Total grouped findings** | **24** |

Counts describe J01–J24 grouped passage findings, not unique chunks or independent estimates. Actual recruitment/event observations are acknowledged but classified IRRELEVANT to the requested tax-site measure. Company recruitment plans remain ANTICIPATED_OUTPUT near misses, not observed hires. Repeated forecast statements are not summed.

**REFERENCE_ANSWER_CANDIDATE**

The frozen UC2 corpus does not provide enough evidence to determine how many jobs were reported as actually created on the designated tax sites of either Green Freeport by 31 March 2026. Its job projections, anticipated tax-site outputs and programme staffing passages do not establish those realised counts.

**A. QUESTION_QUALITY.** The revision states actor, designated-site scope, realised/reported status and a fixed date; it asks for a plausible monitoring outcome, not an identity lookup. No forecast number or other accidental answer clue appears. The question remains unchanged as supplied.

**B. TASK_TYPE_INTEGRITY.** The 293-record corpus-wide test confirms insufficient evidence despite plausible numerical near misses, including Forth's anticipated 16,000 direct jobs on Tax Site land. No forecast/target can legitimately answer an actual-count question. Neither programme recruitment nor broad UK/Highlands estimates can substitute. Candidate required_documents and reference_evidence remain empty arrays; absence-context citations are not gold evidence.

**C. GOLD_QUALITY.** The minimal answer states a source limitation without guessing counts or equating missing reports with zero jobs. It requires no external update and preserves cutoff and site scope. It does not require memorising forecast figures to receive credit.

**D. AMBIGUITY / ADVERSARIAL CHECK.** The previous broad employment-measure issue is addressed by reported actual tax-site creation. Different reporting conventions (headcount/FTE, gross/net) cannot yield competing sufficient answers here because no realised tax-site count is provided under any of them; no convention is invented. The two named Freeports are distinct, and “tax sites of each” allows multiple sites per Freeport. Dates describe requested reporting, not eligibility or a future reporting obligation. Site-linked forecasts and actual individual appointments have been explicitly excluded. Future reporting promises are not source conflicts with a completed outcome report. Partial evidence supplies no actual count for either side and cannot support a fair numerical gold.

**E. DUPLICATION CHECK.** T018 asks planned seed-capital deployment, while this asks reported actual tax-site jobs. Tax-site domain overlap with T011–T017 does not duplicate any required answer. T020 is a different realised fiscal measure.

```text
CORPUS_WIDE_SUFFICIENCY_CONCLUSION=INSUFFICIENT_EVIDENCE_CONFIRMED
SUFFICIENT_REALISED_COUNT_ICFGF=NOT_FOUND
SUFFICIENT_REALISED_COUNT_FORTH=NOT_FOUND
NEW_PROPOSED_VERDICT=READY_FOR_RESEARCHER_DECISION
ISSUE=NONE_REMAINING_IDENTIFIED
HUMAN_VERIFICATION_COMPLETED=NO
```

### T020 Revision 1

```text
TASK_ID=T020
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=medium
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
ORIGINAL_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
REVISION_REASON=Specify aggregate monetary value claimed in LBTT returns by the cutoff; supplied wording additionally introduces a two-tax-sites entity/scope defect requiring researcher decision.
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
```

**EXACT_FINAL_CANDIDATE_QUESTION — supplied Revision 1, preserved pending decision**

> By 31 March 2026, what aggregate monetary value of LBTT Green Freeports relief had been claimed in LBTT returns, separately for transactions in each of Scotland's two Green Freeport tax sites?

**Corpus-wide re-evaluation and near misses.** The monetary/return basis now clearly requests actual claimed relief, rather than consideration, tax payable, eligibility, a hypothetical calculation or seed/NDR funds. It does not ask for cash paid/reimbursed or invent a net-of-withdrawals accounting basis. The repeated 293-record screen finds no actual aggregate monetary claims value attributable to either Green Freeport and no sufficient site-specific value either. Thus the insufficiency finding survives both the intended per-Freeport grouping and a literal per-tax-site reading; the remaining geographical defect still prevents recommending this supplied question as ready. All original LBTT grouped findings are reconsidered below. These citations are audit context, outside the empty gold arrays.

| Finding | Classification | Exact canonical chunks | Frozen content (paraphrase) | Revised-question sufficiency test |
|---|---|---|---|---|
| L01 | CLAIM_START_DATE | DOC047-U0001-C0001 | Claims may be made from 8 April 2024 for Inverness/Cromarty and 12 June 2024 for Forth, following tax-site designation. | Claims may start on these dates; neither eligible start date reports actual monetary value claimed in filed returns. |
| L02 | ELIGIBILITY_RULE | DOC047-U0001-C0001; DOC047-U0001-C0002; DOC047-U0001-C0003; DOC047-U0001-C0004; DOC047-U0001-C0005; DOC047-U0001-C0006 | Qualifying-land/transaction rules, at least 90% full relief and at least 10% partial threshold, just-and-reasonable attribution and stated eligibility windows. | Thresholds and qualifying conditions contain no population of actual returns or aggregate monetary value claimed. |
| L03 | WORKED_EXAMPLE | DOC047-U0001-C0004 | Three illustrative £3m land acquisitions explain full relief, including 90% land and 95% consideration cases. | Illustrative consideration of £3m is not actual relief claimed, and examples are not aggregate filed returns. |
| L04 | WORKED_EXAMPLE | DOC047-U0001-C0005 | Illustrative £1,480,000 purchase yields £62,500 pre-relief tax, 62.5% relief and £39,062.50 relief. | The £39,062.50 relief amount sits in an explicit worked LBTT Return example; it is not an observed filed-return aggregate for a Freeport or tax site. |
| L05 | WORKED_EXAMPLE | DOC047-U0001-C0005; DOC047-U0001-C0006 | Illustrative £1,375,000 purchase, 10.04% qualifying proportion and £57,250 tax gives £5,747.90 relief; further examples below 10% show no relief. | The £5,747.90 relief amount is another illustrative calculation; summing examples or inferring actual zero claims is unsupported. |
| L06 | POLICY_DESCRIPTION | DOC047-U0001-C0006; DOC047-U0001-C0007 | Claims through original returns or timely amendments; guidance on further returns when qualifying use ends. | Original-return and amendment procedures explain how to claim; they do not report values from actual filed returns. |
| L07 | ELIGIBILITY_RULE | DOC047-U0001-C0007; DOC047-U0001-C0008; DOC047-U0001-C0009; DOC047-U0001-C0010; DOC047-U0001-C0011 | Withdrawal/control-period, alternative-finance, lease, review/assignation and notifiability conditions. | Withdrawal, lease and notifiability rules contain no monetary aggregation of claims filed by the cutoff. |
| L08 | WORKED_EXAMPLE | DOC047-U0001-C0007; DOC047-U0001-C0008 | £800,000 warehouse destroyed by fire and £3m change-of-use examples; a hypothetical case says full relief was claimed. | Full relief was claimed when an LBTT return was filed occurs inside the warehouse example. It is not an actual administrative claim observation or aggregate. |
| L09 | WORKED_EXAMPLE | DOC047-U0001-C0009 | Alternative finance example: a bank buys £1,950,000 land and a relevant person claims relief then ceases qualifying use. | The bank purchase price and hypothetical relief/withdrawal are not actual claim aggregates. |
| L10 | WORKED_EXAMPLE | DOC047-U0001-C0010; DOC047-U0001-C0011 | Lease assignation example: two warehouses, £150,000 annual rent and 60% qualifying use. | Example rent, qualifying share and filing obligations are not monetary totals actually claimed. |
| L11 | POLICY_DESCRIPTION | DOC048-U0001-C0001; DOC048-U0002-C0001; DOC048-U0007-C0001 | 2023 legislation creates relief/return/interest provisions; explanatory note describes its purpose. | Legislation establishes relief and return obligations; it does not report observed return values. |
| L12 | ELIGIBILITY_RULE | DOC048-U0003-C0001; DOC048-U0004-C0001; DOC048-U0004-C0002; DOC048-U0005-C0001; DOC048-U0005-C0002; DOC048-U0006-C0001 | Statutory full/partial thresholds, qualifying use, withdrawal and alternative-finance rules. | Statutory amount-chargeable formulas concern legal calculation, not totals in actual returns. |
| L13 | POLICY_DESCRIPTION | DOC041-U0001-C0020; DOC041-U0001-C0021; DOC044-U0001-C0002; DOC044-U0001-C0003; DOC053-U0006-C0001 | Prospectus/impact assessment/report describe LBTT as part of the tax-incentive package. | Describing the tax-incentive package gives no observed claim value. |
| L14 | POLICY_DESCRIPTION | DOC041-U0001-C0018; DOC041-U0001-C0019; DOC041-U0001-C0036; DOC041-U0001-C0039; DOC041-U0001-C0040; DOC043-U0001-C0006; DOC043-U0001-C0007; DOC043-U0001-C0008; DOC043-U0001-C0025; DOC043-U0001-C0026; DOC043-U0001-C0027; DOC044-U0001-C0007; DOC044-U0001-C0008; DOC044-U0001-C0009 | Revenue Scotland oversight, record access, relief declarations, tax-site compliance and required collection/evaluation of realised relief outcomes. | Oversight and future data collection are plausible leads but contain no populated LBTT claims dataset. External linked data are outside this audit. |
| L15 | POLICY_DESCRIPTION | DOC049-U0001-C0001; DOC049-U0002-C0001; DOC049-U0002-C0002; DOC049-U0003-C0001; DOC050-U0001-C0001; DOC050-U0002-C0001; DOC050-U0003-C0001 | Designations, maps, commencement dates and explanatory notes on special-tax-site allowances. | Designation/maps establish multiple tax sites and eligibility geography, not actual monetary amounts claimed at any site or Freeport. |
| L16 | IRRELEVANT | DOC046-U0001-C0001; DOC046-U0001-C0002; DOC046-U0001-C0003; DOC046-U0001-C0004; DOC046-U0001-C0005; DOC046-U0001-C0006; DOC046-U0001-C0007; DOC046-U0001-C0008 | GF relief amounts, NDRI/audited returns, GRG reimbursement, percentage/amount reporting and recipients lists; page updated 25 March 2026. | NDR relief, audited NDR returns and reimbursement are a different tax. No aggregate actual LBTT claim amount is provided. |
| L17 | IRRELEVANT | DOC052-U0005-C0001; DOC052-U0005-C0002; DOC052-U0008-C0001; DOC052-U0008-C0002; DOC052-U0013-C0001; DOC052-U0013-C0002; DOC052-U0014-C0001; DOC052-U0020-C0001; DOC052-U0020-C0002; DOC052-U0022-C0001; DOC053-U0007-C0001; DOC053-U0008-C0001; DOC053-U0009-C0001; DOC053-U0010-C0001; DOC053-U0011-C0001; DOC053-U0012-C0001; DOC053-U0027-C0001; DOC053-U0031-C0001; DOC053-U0037-C0001; DOC053-U0038-C0001; DOC053-U0040-C0001 | Seed-capital/match-funding budgets and project expenditure, skills-fund projections, retained-NDR projections (including an annual income table), land-value/GVA benefits, and tax benefits typically over 7% of private capital investment. | Seed-capital budgets, investment, retained NDR forecasts and land-value estimates cannot be treated as actual claimed LBTT relief. |
| L18 | IRRELEVANT | DOC055-U0001-C0001; DOC055-U0001-C0002; DOC055-U0001-C0003; DOC055-U0001-C0004; DOC055-U0001-C0005; DOC056-U0001-C0001; DOC056-U0001-C0002; DOC056-U0001-C0003; DOC057-U0001-C0001; DOC057-U0001-C0002; DOC057-U0001-C0003; DOC057-U0001-C0004 | NI/SBA/ECA rules and examples, including £120,000/£144,000 total SBA claims, £300,000 ECA and a £133,333 ECA example. | Other-tax claimed amounts are hypothetical NI/SBA/ECA examples, not actual aggregate LBTT Green Freeports relief. |
| L19 | IRRELEVANT | DOC051-U0001-C0001; DOC051-U0003-C0001; DOC051-U0003-C0002; DOC051-U0003-C0003; DOC051-U0003-C0004; DOC051-U0003-C0005; DOC051-U0003-C0006; DOC051-U0003-C0007; DOC051-U0004-C0001; DOC051-U0004-C0002; DOC051-U0005-C0001; DOC051-U0005-C0002; DOC051-U0005-C0003; DOC051-U0006-C0001; DOC051-U0006-C0002; DOC051-U0006-C0003; DOC051-U0006-C0004; DOC051-U0006-C0005; DOC051-U0006-C0006; DOC051-U0006-C0007; DOC051-U0006-C0008; DOC051-U0007-C0001; DOC051-U0008-C0001; DOC051-U0009-C0001; DOC058-U0001-C0001; DOC058-U0001-C0002; DOC058-U0001-C0003 | Customs/excise/VAT procedure and goods records; seed-subsidy cumulative amounts/£100,000 transparency and £25m scheme thresholds. | Customs/VAT/excise and subsidy values are different measures, not filed LBTT-return aggregates. |
| L20 | IRRELEVANT | DOC048-U0008-C0001; DOC049-U0004-C0001; DOC050-U0004-C0001 | Instrument publication prices £8.14 and £5.78. | Publication prices are unrelated to relief claimed. |
| L21 | POLICY_DESCRIPTION | DOC052-U0015-C0001; DOC052-U0016-C0001; DOC052-U0017-C0001; DOC052-U0018-C0001; DOC053-U0008-C0001; DOC053-U0013-C0001; DOC053-U0028-C0001; DOC053-U0045-C0001; DOC053-U0047-C0001; DOC053-U0048-C0001; DOC053-U0049-C0001 | Accountable-body financial assurance, investment monitoring and future reporting/evaluation arrangements in the two business-case reports. | Financial assurance and future reporting contain no actual aggregate monetary values of LBTT relief in returns. |

| Near-miss classification | Grouped findings |
|---|---:|
| ELIGIBILITY_RULE | 3 |
| WORKED_EXAMPLE | 6 |
| CLAIM_START_DATE | 1 |
| POLICY_DESCRIPTION | 6 |
| AGGREGATE_ACTUAL_CLAIM_VALUE | 0 |
| IRRELEVANT | 5 |
| **Total grouped findings** | **21** |

Counts describe L01–L21 grouped findings, not unique chunks or administrative claim events. In particular, headings “LBTT Return” and the phrase “Full Green Freeport relief was claimed when an LBTT return was filed” are within examples. They cannot become observed filed-return data merely because this revision mentions returns. Original-return/amendment instructions do not demonstrate uptake or monetary aggregation.

**REFERENCE_ANSWER_CANDIDATE**

The frozen UC2 corpus does not provide enough evidence to determine the aggregate monetary value of LBTT Green Freeports relief actually claimed in LBTT returns by 31 March 2026, separately by Green Freeport or designated tax site. It provides eligibility and filing guidance and worked examples, rather than aggregate actual claim data.

This provisional answer states the common evidence limitation under both scope readings. It does not validate the question's “two tax sites” premise; geographical wording must be resolved before later task packaging.

**A. QUESTION_QUALITY.** This is a realistic administrative information need, with the monetary measure, filing basis and cutoff substantially clearer. It is neutral and contains no answer amount. However, the actor/unit of aggregation is misstated: Scotland has two Green Freeports with multiple designated tax sites. “Each of Scotland's two Green Freeport tax sites” incorrectly treats two Freeports as two tax sites and leaves which sites unidentifiable.

**B. TASK_TYPE_INTEGRITY.** The corpus-wide absence conclusion remains valid: no actual aggregate claimed value is supplied for either Freeport or for a designated site. Plausible examples/claim instructions do not answer it. Required document/evidence arrays remain `[]`. Insufficiency confirmation does not cure an ill-defined population; proposed researcher verdict remains REVISION_RECOMMENDED rather than forcing readiness or reclassifying as NOT_INSUFFICIENT_EVIDENCE.

**C. GOLD_QUALITY.** The provisional answer is source-bounded and does not sum examples, infer zero uptake, substitute tax paid/relief repaid or use policy forecasts. All values in the near-miss table remain correctly labelled. No outside knowledge is introduced. It cannot provide a uniquely defined pair of site totals without fixing the question's scope.

**D. AMBIGUITY / ADVERSARIAL CHECK.** DOC047-U0001-C0001 explicitly describes two Green Freeports and lists multiple sites for each (Deephaven, Invergordon, Nigg for Inverness/Cromarty; Grangemouth, Mid Forth locations and Rosyth for Forth). DOC053-U0027-C0001 explicitly describes three approved Forth tax sites: Grangemouth, Rosyth and Mid-Forth; DOC053-U0028-C0001 also refers to three designated sites. Different grouping of Mid-Forth locations need not be adjudicated to establish that there are more than two sites. These descriptions refute the revised question's two-site premise; they are not aggregate claim data. A reviewer could defensibly read the question as per-Freeport totals or unspecified per-site totals, making scoring unfair. The cutoff and claimed-in-returns concept are clear; rules, hypothetical filed returns, prospective monitoring and unrelated reliefs remain excluded. No sufficient actual amount is hidden in a stale/current conflict.

```text
ISSUE=The supplied question conflates Scotland's two Green Freeports with their multiple designated tax sites, leaving the two aggregation entities incorrectly defined.
SUGGESTED_CHANGE=By 31 March 2026, what aggregate monetary value of LBTT Green Freeports relief had been claimed in LBTT returns, separately for transactions in the designated tax sites of each of Scotland's two Green Freeports?
SUGGESTED_CHANGE_APPLIED=NO
CORPUS_WIDE_SUFFICIENCY_CONCLUSION=INSUFFICIENT_EVIDENCE_CONFIRMED_UNDER_BOTH_SCOPE_READINGS
SUFFICIENT_AGGREGATE_ACTUAL_CLAIM_VALUE_ICFGF=NOT_FOUND
SUFFICIENT_AGGREGATE_ACTUAL_CLAIM_VALUE_FORTH=NOT_FOUND
SUFFICIENT_AGGREGATE_ACTUAL_CLAIM_VALUE_PER_TAX_SITE=NOT_FOUND
NEW_PROPOSED_VERDICT=REVISION_RECOMMENDED
HUMAN_VERIFICATION_COMPLETED=NO
```

**E. DUPLICATION CHECK.** T012 asks LBTT qualifying proportions; this question asks observed aggregate uptake/value in returns. Eligibility facts cannot satisfy the outcome question. T019 concerns jobs, and T018 concerns planned seed-capital investment. No duplicate answer requirement is identified, subject to resolving the geographical scope defect.

### Recomputed current-candidate aggregate review

Only the latest proposed verdict for each task is counted. The original 7/3/0 counts and recommendations above remain historical. T011–T017 are carried forward unchanged, including T014's final Revision 1. The original T014 defect is not reintroduced as the final candidate.

| Task | Current review candidate | Latest proposed verdict |
|---|---|---|
| T011 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T012 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T013 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T014 | Existing human-directed Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T015 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T016 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T017 | Unchanged | READY_FOR_RESEARCHER_DECISION |
| T018 | Researcher-directed precision Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T019 | Researcher-directed precision Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T020 | Researcher-directed precision Revision 1, scope change suggested only | REVISION_RECOMMENDED |

```text
TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
READY_FOR_RESEARCHER_DECISION=9
REVISION_RECOMMENDED=1
REJECT_RECOMMENDED=0
CORPUS_DOCUMENTS_SCANNED=17
CORPUS_CHUNKS_SCANNED=293
ALL_NAMED_REVISION_CHUNKS_EXIST_EXACTLY_ONCE=YES
```

| Aggregate check | Current assessment |
|---|---|
| SCHEMA_COMPATIBILITY_PRECHECK | Earlier static precheck retained: supported task types and difficulty labels; T019/T020 empty arrays. No task JSON or executable validation created. T020 question scope still requires decision. |
| SOURCE_TRACEABILITY | PASS: frozen fingerprints pinned; 293-line absence ledger reconciled; revision evidence IDs verified exactly once. |
| TASK_TYPE_INTEGRITY | PASS for T018's both-document comparison and corpus-wide insufficiency of T019/T020; T020 geography separately flagged. Unchanged seven tasks retain prior assessments. |
| REFERENCE_ANSWER_SUPPORT | T018 corrected to invitation, with prospective/conditional qualifications; T019/T020 source-only absence answers. T020 gold remains provisional pending scope resolution. |
| AMBIGUITY_AUDIT | REVIEW_REQUIRED: one remaining T020 Freeport-versus-tax-site defect. T018 planned timeframe and T019 designated-site employment scope addressed. |
| DUPLICATION_AUDIT | Earlier all-pairs assessment retained; three revised information needs remain distinct from the seven unchanged tasks and from each other. |
| GOLD_LEAKAGE_AUDIT | Earlier static boundary retained: only Markdown dossier append under evidence/engineering; no corpus, runtime, configuration or task JSON mutation/execution. Dossier remains reviewer-side material. |
| INSUFFICIENT_EVIDENCE_AUDIT | CONFIRMED for both revised measures throughout 293 chunks/17 documents; no actual requested counts/amounts found even for one Freeport. Not an assertion about external data or zero results. T020 scope recommendation remains unresolved. |

### Revision provenance and review status

```text
LLM_ASSISTED_AUTHORING=YES
HUMAN_DIRECTED_TASK_DESIGN=YES
RESEARCHER_DIRECTED_PRECISION_REVISION=YES
REVISION_STAGE=PRE_FREEZE
CORPUS_WIDE_ABSENCE_REASSESSMENT=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
RANKED_RETRIEVAL_USED=NO
DIAGNOSTIC_RETRIEVAL_USED=NO
EMBEDDINGS_USED=NO
MODEL_BENCHMARK_OUTPUT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
HUMAN_VERIFICATION_COMPLETED=NO
TASKS_HUMAN_VERIFIED=NO
TASK_JSON_CREATED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
```

No task execution, model test, retrieval diagnostic or benchmark result informed any revision. These remain authoring candidates pending explicit researcher approval. T020's suggested change has not been applied. Completion of this controlled revision step does not signify human verification, readiness of every question, or freeze.


## T020 Researcher-Directed Pre-Freeze Revision 2

This append-only section records the supplied researcher-directed T020 Revision 2 on 26 September 2026. It supersedes T020's preceding Revision 1 question, provisional answer and proposed verdict for the current review candidate. All prior wording, near-miss findings, recommendations and aggregate counts remain unchanged above as history. No other task is revised. READY_FOR_RESEARCHER_DECISION is a proposed review status, not researcher acceptance, human verification or task freeze.

### Candidate and revision provenance

```text
TASK_ID=T020
TASK_TYPE=insufficient_evidence
DIFFICULTY_CANDIDATE=medium
REQUIRED_DOCUMENTS_CANDIDATE=[]
REFERENCE_EVIDENCE_CANDIDATE=[]
ORIGINAL_T020_VERDICT=REVISION_RECOMMENDED
REVISION_STAGE=PRE_FREEZE
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
```

**EXACT_FINAL_CANDIDATE_QUESTION — supplied Revision 2**

> By 31 March 2026, what aggregate monetary value of LBTT Green Freeports relief had been claimed in LBTT returns for transactions across the designated tax sites within each of Scotland's two Green Freeports, reported separately for Inverness and Cromarty Firth Green Freeport and Forth Green Freeport?

**REVISION_REASON:** The previous wording incorrectly implied that Scotland's two Green Freeports correspond to only two individual tax sites. Each Green Freeport contains multiple designated tax sites. The revised wording asks for the aggregate claimed value across the designated tax sites within each Green Freeport.

The authorised Revision 2 replaces the faulty two-site premise with two explicitly named per-Freeport aggregation groups. DOC047-U0001-C0001 lists multiple sites within each Freeport; DOC053-U0027-C0001 identifies three approved Forth tax sites and DOC053-U0028-C0001 refers to three designated sites. These frozen passages support the entity/scope correction, not realised LBTT claims. The previous suggested wording remains history; the current question is the exact new wording supplied by the researcher.

### Corpus-wide source re-verification

The frozen canonical source remains `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl`. It was parsed again in physical file order, with 293 records and 293 unique chunk IDs. All 17 accepted membership documents are represented exactly as the accepted set, with no excluded document. Every text SHA256 was recomputed and checked; all 293 canonical lines/IDs/hashes reconcile to the immutable absence audit's complete screening/disposition ledger.

The two broad T020 term families below were rerun against every canonical text field, case-insensitively and without ranking or top-k limits. The tax family matched 198 chunks, the claim/value family 173, and their union 244; 49 union nonhits were still enumerated and reconciled to the existing structural/numeric screening record. The supplementary `£|\b\d[\d,]{2,}\b` screen was also repeated over all 293 records, matching 186 chunks. Monetary/numeric matches are leads for inspection, not proof of claims, and absence does not rest on keyword zero-matches.

**T020_TAX**

```regex
\b(?:LBTT|land\s+(?:and|&)\s+buildings?\s+transaction\s+tax|Revenue\s+Scotland|tax\w*|relief\w*|exempt\w*|SDLT|stamp\s+duty)\b
```

**T020_VALUES**

```regex
\b(?:claims?|claimed|claiming|amounts?|values?|statistics?|aggregat\w*|total\w*|cumulat\w*|uptake|take[- ]up|receipts?|refund\w*|repaid|repay\w*|data|figures?|numbers?|2026|31\s+March)\b
```

| Accepted document | Canonical chunks re-enumerated | T020 union hits |
|---|---:|---:|
| DOC041 | 53 | 43 |
| DOC042 | 10 | 8 |
| DOC043 | 40 | 37 |
| DOC044 | 13 | 12 |
| DOC045 | 4 | 4 |
| DOC046 | 8 | 8 |
| DOC047 | 11 | 11 |
| DOC048 | 10 | 9 |
| DOC049 | 5 | 4 |
| DOC050 | 4 | 3 |
| DOC051 | 25 | 17 |
| DOC052 | 45 | 30 |
| DOC053 | 50 | 44 |
| DOC055 | 5 | 5 |
| DOC056 | 3 | 3 |
| DOC057 | 4 | 4 |
| DOC058 | 3 | 2 |
| **Total** | **293** | **244** |

All L01–L21 grouped findings were re-assessed against the exact Revision 2 measure. Their complete chunk lists and source-content classifications remain in the immediately preceding Revision 1 table and the immutable absence audit. Focused direct re-reading in this step included all 11 DOC047 guidance chunks, all 10 DOC048 legislative chunks, LBTT/Revenue Scotland contexts elsewhere in the corpus, monitoring/reporting provisions and the multiple-tax-site descriptions. The earlier corpus-wide ledger supplies the complete dispositions for broad policy hits, other-tax financial values and nonhits; its hashes were reconciled record by record, rather than assuming unchanged absence from the prior verdict alone.

The required observation must jointly establish: **aggregate monetary relief actually claimed in LBTT returns; coverage by 31 March 2026; aggregation across the designated sites within a Freeport; and separate attribution to the two named Freeports.** No sufficient aggregate was found for either Freeport, and there is no set of actual transaction/site claim observations from which the requested pair can legitimately be calculated. Rules, hypothetical transactions, other-tax returns and forecasts cannot be summed or extrapolated into the requested realised totals.

### Re-assessed near-miss evidence

These are source-only absence-context citations, not entries in the candidate's empty reference_evidence array. Finding IDs refer to the preserved complete L01–L21 tables; ranges below group findings with the same reason for exclusion.

| Findings | Classification | Material frozen evidence and Revision 2 assessment |
|---|---|---|
| L01 | CLAIM_START_DATE | DOC047-U0001-C0001: Inverness/Cromarty claims may start 8 April 2024 and Forth claims 12 June 2024. Availability is not a report of amounts actually claimed by the cutoff. Multiple sites are explicitly listed for each Freeport. |
| L02, L07, L12 | ELIGIBILITY_RULE | DOC047-U0001-C0001–C0011 and DOC048 statutory qualifying/withdrawal provisions: 90% full/10% partial thresholds, qualifying land/use, relief windows, attribution and withdrawal/lease rules. They supply no observed return population or per-Freeport aggregate. |
| L03 | WORKED_EXAMPLE | DOC047-U0001-C0004: illustrative £3m purchases explain full relief. Purchase consideration is not aggregate relief actually claimed. |
| L04–L05 | WORKED_EXAMPLE | DOC047-U0001-C0005/C0006: hypothetical LBTT Return calculations give £39,062.50 and £5,747.90 relief. The headings do not certify filed administrative returns. The amounts cannot be summed, assigned to these Freeports or treated as cutoff totals. No-relief examples do not establish zero actual uptake. |
| L08–L10 | WORKED_EXAMPLE | DOC047-U0001-C0007–C0011: warehouse fire/change-of-use, alternative finance and lease assignation examples include past-tense claiming and illustrative £800,000/£3m/£1,950,000 consideration or £150,000 rent. These are hypothetical individual transactions, not actual Freeport claim aggregates. |
| L06 | POLICY_DESCRIPTION | DOC047-U0001-C0006/C0007 explains claims in original returns or timely amendments and further returns on withdrawal. This establishes filing procedure, not observed claimed values. |
| L11, L13 | POLICY_DESCRIPTION | DOC048 relief legislation and DOC041/DOC044/DOC053 descriptions establish a tax incentive, not its aggregate realised monetary uptake. |
| L14, L21 | POLICY_DESCRIPTION | Revenue Scotland oversight, reporting/data-collection requirements, accountable-body assurance and future M&E arrangements do not contain populated aggregate LBTT claim returns. DOC043-U0001-C0026/C0027 includes reporting periods ending 31 March, but no 2026 actual claim values. |
| L15 | POLICY_DESCRIPTION | DOC049/DOC050 designation instruments and maps identify eligibility geography/commencement, not amounts claimed. They do not imply one tax site per Freeport. |
| L16 | IRRELEVANT | DOC046 relief amounts, audited returns and reimbursements concern NDR, not LBTT, including its 25 March 2026 guidance update. |
| L17 | IRRELEVANT | DOC052/DOC053 seed/match-funding expenditure, retained-NDR projections, land-value/GVA estimates and tax-benefit assumptions are different measures or forecasts, not actual LBTT-return claim totals. |
| L18 | IRRELEVANT | DOC055/DOC056/DOC057 NI/SBA/ECA rules and illustrative claims concern different taxes; neither monetary values nor the word total makes them actual aggregate LBTT claims. |
| L19–L20 | IRRELEVANT | DOC051 customs/VAT/excise records, DOC058 subsidy values and statutory publication prices are unrelated monetary measures. |

The classification totals remain **3 ELIGIBILITY_RULE, 6 WORKED_EXAMPLE, 1 CLAIM_START_DATE, 6 POLICY_DESCRIPTION, 5 IRRELEVANT and 0 AGGREGATE_ACTUAL_CLAIM_VALUE** across the 21 grouped findings. These are grouped passage findings, not unique-chunk counts or observed administrative events. All full canonical IDs in the preserved finding tables exist exactly once.

### Sufficiency conclusion and reference answer

**CORPUS_WIDE_SUFFICIENCY_CONCLUSION:** Insufficient evidence confirmed for the exact Revision 2 question. No aggregate monetary actual LBTT-return claim value across the designated sites is supplied for Inverness and Cromarty Firth Green Freeport or for Forth Green Freeport by the stated cutoff. No sufficient single-side value has been obscured by only assessing the complete pair. The candidate is not reclassified as NOT_INSUFFICIENT_EVIDENCE because no requested actual aggregate evidence was found.

**REFERENCE_ANSWER_CANDIDATE**

The frozen UC2 corpus does not provide enough evidence to determine the aggregate monetary value of LBTT Green Freeports relief claimed in LBTT returns by 31 March 2026 across the designated tax sites within either Inverness and Cromarty Firth Green Freeport or Forth Green Freeport. It contains eligibility and filing guidance and worked examples, rather than the requested aggregate actual claim values.

The answer concerns the canonical frozen text, not whether administrative data exist elsewhere. It does not assert zero claims, import linked statistics, invent a transaction population, infer uptake from designation, substitute tax paid/refunded or assume a net-of-withdrawals accounting basis. Extraction limitations noted in the preserved audits remain: enumerated page-number/figure-title-only chunks do not establish contents of unseen figures or external annexes. The conclusion does not rely on every source predating the cutoff.

### Reviewer checks for the current T020 candidate

**A. QUESTION_QUALITY:** A realistic document-based administrative information need. The actor, monetary measure, return basis, aggregation geography and date are explicit. The two output groups are named and multiple sites within each are allowed. The question is not a document identity lookup, contains no example amount or accidental answer clue, and is neutral. The previous two-site issue is resolved.

**B. TASK_TYPE_INTEGRITY:** The repeated 293-chunk/17-document audit finds no sufficient actual aggregate value for either group. Plausible positive hits exist; eligibility, procedure, examples, hypothetical claims and forecasts do not satisfy the conjunction of realised measure, attribution and cutoff. Required document/evidence candidates remain `[]`; audit citations are review provenance, not gold evidence. insufficient_evidence remains valid.

**C. GOLD_QUALITY:** The minimal answer preserves both named Freeports, across-site aggregation, claims-in-returns basis and cutoff. It states only the evidence limitation and nearby information type. It contains no outside knowledge, fabricated amount, unsupported causality, example summation or zero-claim inference.

**D. AMBIGUITY / ADVERSARIAL CHECK:** The two-Freeport versus individual-site ambiguity is resolved without needing to settle the grouping of Mid-Forth locations. The cutoff is explicit and is distinct from designation/claim-start dates. Claimed monetary relief is distinct from eligibility, consideration, tax payable and cash reimbursement. Hypothetical filed-return examples and prospective reporting periods cannot be mistaken for realised aggregates. No conflicting actual values or stale/current actual totals were identified. No sufficient partial report exists for one side. Different possible amendment/withdrawal reporting conventions cannot create a competing supported numerical answer because the corpus contains no actual aggregate claims under any such convention; no convention is imposed. No new defect identified.

**E. DUPLICATION CHECK:** T012's LBTT eligibility proportions remain a different answer requirement. T019 concerns reported actual site jobs, and T018 concerns planned seed-capital deployment. The Revision 2 geography correction does not create a duplicate information need among T011–T020.

```text
ISSUE=NONE_REMAINING_IDENTIFIED
T020_FINAL_VERDICT=READY_FOR_RESEARCHER_DECISION
NEW_PROPOSED_VERDICT=READY_FOR_RESEARCHER_DECISION
SUFFICIENT_AGGREGATE_ACTUAL_CLAIM_VALUE_ICFGF=NOT_FOUND
SUFFICIENT_AGGREGATE_ACTUAL_CLAIM_VALUE_FORTH=NOT_FOUND
HUMAN_VERIFICATION_COMPLETED=NO
```

### Final dossier aggregate — latest candidates for review

This table supersedes earlier aggregate counts for the current candidate set while retaining those historical counts above. T011–T017 are unchanged, including T014's final human-directed Revision 1 and its original defect history. T018/T019 retain their precision Revision 1. Only T020 advances to Revision 2. Earlier static checks and source assessments for unchanged tasks are carried forward; no task execution or new scientific design decision is introduced.

| Task | Latest candidate | Final proposed review verdict |
|---|---|---|
| T011 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T012 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T013 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T014 | Existing human-directed Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T015 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T016 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T017 | Existing final candidate | READY_FOR_RESEARCHER_DECISION |
| T018 | Precision Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T019 | Precision Revision 1 | READY_FOR_RESEARCHER_DECISION |
| T020 | Researcher-directed Revision 2 | READY_FOR_RESEARCHER_DECISION |

```text
TOTAL_TASKS=10
DIRECT=3
WITHIN_DOCUMENT=3
CROSS_DOCUMENT=2
INSUFFICIENT_EVIDENCE=2
READY_FOR_RESEARCHER_DECISION=10
REVISION_RECOMMENDED=0
REJECT_RECOMMENDED=0
CORPUS_DOCUMENTS_SCANNED=17
CORPUS_CHUNKS_SCANNED=293
```

| Aggregate check | Latest assessment |
|---|---|
| SCHEMA_COMPATIBILITY_PRECHECK | Earlier static precheck retained; supported task types/difficulty labels and intentional empty arrays for T019/T020. No JSON authoring or executable benchmark check. |
| SOURCE_TRACEABILITY | Frozen hashes and 293-record ledger reconciled; previous source locators retained; Revision 2 context verified directly. |
| TASK_TYPE_INTEGRITY | Prior seven tasks and T018/T019 Revision 1 assessments retained; T020 corpus-wide insufficiency reconfirmed with corrected aggregation scope. |
| REFERENCE_ANSWER_SUPPORT | T018 invitation correction retained; T019 absence answer retained; T020 reference answer explicitly matches Revision 2. Source-only candidate support, human verification outstanding. |
| AMBIGUITY_AUDIT | Previous T020 entity/scope defect resolved. No new defect identified; unchanged source qualifications and researcher-review notes remain above. |
| DUPLICATION_AUDIT | No duplicate answer requirement introduced; earlier pairwise assessment retained. |
| GOLD_LEAKAGE_AUDIT | Earlier static boundary retained: append only reviewer-side Markdown, with no corpus/runtime/config/task JSON mutation or execution. |
| INSUFFICIENT_EVIDENCE_AUDIT | T019 prior full-corpus assessment retained; T020 repeated against all 293 canonical records. No actual aggregate LBTT claim values for either Freeport; no zero-outcome or outside-data assertion. |

### Preservation fingerprints and final provenance

| Input preserved in this step | SHA256 |
|---|---|
| Earlier task-candidate evidence audit | `728fe36bcfd3097005594053ffef69cb6ac586a09964be5579a2ee9437f15d56` |
| Earlier corpus-wide absence audit | `e068d2c40c378d8b8bb276f6903a0f52502edcab39b301bca9a0106e6eb2f57d` |
| Dossier before Revision 2; preserved as its first 125,867 bytes | `7644ba5af349969423d59a6dab54a9d20f2181e3c05634945a266332f975f325` |
| Canonical chunks.jsonl | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| Frozen membership | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| Frozen authoring protocol | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |

Branch and HEAD remain `research/benchmark-task-construction-uc2-uc3` and `4ca03cde8dd969c07590670615008b17d5448a2e`. Only the dossier is appended; all preceding bytes are preserved.

```text
LLM_ASSISTED_AUTHORING=YES
HUMAN_DIRECTED_TASK_DESIGN=YES
HUMAN_DIRECTED_REVISION=YES
REVISION_STAGE=PRE_FREEZE
CORPUS_WIDE_ABSENCE_REASSESSMENT=YES
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
RANKED_RETRIEVAL_USED=NO
DIAGNOSTIC_RETRIEVAL_USED=NO
EMBEDDINGS_USED=NO
MODEL_BENCHMARK_OUTPUT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
HUMAN_VERIFICATION_COMPLETED=NO
TASKS_HUMAN_VERIFIED=NO
TASK_JSON_CREATED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
```

All ten candidates remain pending explicit researcher approval. Proposed readiness records the outcome of source-based authoring/review preparation only; it does not complete human verification or freeze.


# Researcher Final Approval

```text
APPROVAL_TEXT=APPROVE UC2 T011-T020
APPROVAL_DATE=2026-09-26
APPROVED_TASKS=T011-T020
HUMAN_VERIFICATION_COMPLETED=YES
APPROVAL_STAGE=PRE_BENCHMARK
RESULT_DRIVEN_APPROVAL=NO
BENCHMARK_STARTED=NO
```

This explicit researcher approval applies to the latest final candidates: T014 Human-Directed Pre-Freeze Revision 1; T018 Precision Revision 1; T019 Precision Revision 1; T020 Researcher-Directed Pre-Freeze Revision 2; and unchanged T011-T013/T015-T017. Prior review history is preserved. Approval authorizes human_verified status and the requested validation-gated UC2 freeze, and does not authorize benchmark execution.
