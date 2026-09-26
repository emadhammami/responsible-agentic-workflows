# UC2 draft task-candidate evidence audit — 26 September 2026

This is an LLM-assisted evidence audit of the eight already selected draft candidates T011–T018, not benchmark execution or human verification. Questions, task types, document assignments and expected evidence targets are preserved exactly. Seven candidates are ready for human review; T014 requires review for a material task-type defect. Successful completion of this audit does not mean all candidates pass scientific review.

## Frozen base and audit method

- Branch: `research/benchmark-task-construction-uc2-uc3`.
- Expected and observed HEAD: `4ca03cde8dd969c07590670615008b17d5448a2e`.
- Initial worktree: clean, including untracked files.
- Canonical text: `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl`.
- Membership: `corpus/use_cases/UC2/corpus_membership.json`, status `membership_frozen`.
- Protocol: `benchmark/task_authoring_protocol_v0.1.json`, protocol ID `PRIMARY-UC2-UC3-TASK-AUTHORING-v0.1`, status `frozen_before_task_authoring`.

Verification used exact chunk-ID equality in the canonical JSONL, document/use-case metadata, accepted membership, and recomputed UTF-8 text SHA256. All 21 named targets occur exactly once and their stored text hashes match. Reference-answer claims below use only the named frozen chunks. Literal, unranked checks of the two document pairs were used only to inspect whether either document supplied the other side of the comparison: DOC056 has 3 chunks, DOC057 4, DOC052 45 and DOC053 50. These checks found no alternative-allowance content in DOC056/DOC057, no Forth content in DOC052, and only an announcement naming Inverness and Cromarty Firth in DOC053 (not its seed-capital programme). A £260m occurrence in DOC053 concerns Forth land-value uplift, not Inverness seed-capital project expenditure. No additional chunks supply reference-answer claims here.

No live sources, diagnostic retrieval results, rankings, embeddings, benchmark prompts, model inference for task execution, or benchmark outputs were used. Reference answers are authoring candidates derived by reading frozen text; they are not responses from an executed benchmark. The protocol's historical base-commit field is retained as protocol metadata; the audit worktree base is the user-specified HEAD above.

Classification is relative to the exact question and a minimal complete answer, accounting for overlapping text:

- **REQUIRED**: supplies a material answer component not otherwise fully provided by the other named targets.
- **SUPPORTING**: adds relevant detail or corroboration without being necessary for a minimal complete answer.
- **REDUNDANT**: adds no material answer fact beyond another named target, including chunk-overlap continuations.
- **INSUFFICIENT**: cannot support the answer component for which it is proposed.

A supporting or redundant target does not by itself constitute a candidate defect. Multiple chunk IDs do not establish reasoning: synthesis must be materially needed. Every candidate is assessed against the frozen source snapshot, not current policy or observed delivery. Ambiguity assessments cover timeframe, actor, interpretation, terminology and accidental answer clues. No candidate has been rewritten, replaced, frozen or marked human-verified.

## T011

- **task_id:** T011
- **task_type:** direct_retrieval
- **required_documents:** DOC046

**Exact candidate question**

> Under Green Freeport NDR relief, for how long can relief run from first eligibility, and by what date must it be applied for, subject to the 2028 review?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC046-U0001-C0002 | REQUIRED | Timespan and Eligibility: up to five years from beneficiary eligibility; relief applied for by 30 September 2034, subject to the 2028 mid-point review. Other relief awarded in lieu counts within that five-year period. Relevant tax-site establishment/designation is a prerequisite. |

**Evidence-supported reference-answer candidate**

Relief can run for up to five years from when the beneficiary first becomes eligible, including any period in which another relief is awarded in its place. It must be applied for by 30 September 2034, subject to the outcome of the 2028 mid-point review. Availability also depends on the relevant tax site having been established and designated. [DOC046-U0001-C0002]

**Task-type integrity:** Valid. One localized timespan-and-eligibility passage supplies both requested facts and their qualifications. The ten-year tax-relief window is distinct from the beneficiary's maximum five-year relief period.

**Ambiguity assessment:** No material defect. The timeframe starts at first eligibility, not application or first payment. The actor is the beneficiary/ratepayer. NDR identifies the rates relief context; GF is the source's Green Freeport abbreviation. The reference to the review supplies a necessary qualification without revealing the duration or application deadline. The answer does not interpret the 2034 deadline as a universal end date for all awards.

**Source sufficiency:** Sufficient in the named chunk; no external policy update is needed or assumed.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T012

- **task_id:** T012
- **task_type:** direct_retrieval
- **required_documents:** DOC047

**Exact candidate question**

> What proportion of chargeable consideration must relate to qualifying Green Freeport land for full LBTT relief, and what minimum proportion permits partial relief?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC047-U0001-C0001 | REQUIRED | Full relief at at least 90% of chargeable consideration relating to qualifying land on a designated Green Freeport tax site; partial relief at at least 10%. |

**Evidence-supported reference-answer candidate**

Full relief requires at least 90% of the transaction's chargeable consideration to relate to qualifying land on a designated Green Freeport tax site. The minimum threshold for partial relief is at least 10%. [DOC047-U0001-C0001]

**Task-type integrity:** Valid. Both thresholds are stated together in one localized passage.

**Ambiguity assessment:** No material defect. The denominator is chargeable consideration, not land area. The percentages are inclusive thresholds. The question asks for the minimum partial-relief threshold; the source's “at least 10%” does not justify treating partial relief as the only available relief at or above 90%. There is no unclear actor or timeframe for this threshold question. Qualifying land is used in the source's tax-site context; eligibility definitions and calculation of the partial amount are outside the requested answer. No numerical answer clues appear in the wording.

**Source sufficiency:** Sufficient for the two requested thresholds. The chunk's unfinished qualifying-land definition is not needed to answer them.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T013

- **task_id:** T013
- **task_type:** direct_retrieval
- **required_documents:** DOC058

**Exact candidate question**

> What location and project-approval conditions must be satisfied for a Scottish Green Freeport seed-capital subsidy to support a project?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC058-U0001-C0002 | REQUIRED | Eligible location and Eligible activity rules: outer boundary or justified economically connected location; relevant Freeport FBC or government-approved formal change request; project business-case approval by accountable body under local assurance and by Green Freeport Board. Another local authority needs accountable-body permission and confirmation of project business-case approval. |

**Evidence-supported reference-answer candidate**

The project must be within the outer boundary of Forth or Inverness and Cromarty Firth Green Freeport, or in an economically connected location where justified in the Full Business Case. It must be set out and agreed in the relevant Freeport's Full Business Case, or subsequently approved by government through a formal change request. Its own business case must also be approved by the accountable body under local assurance processes and by the Green Freeport Board. If another local authority awards the subsidy, it needs the relevant accountable body's permission and confirmation that the accountable body approved the project business case under those processes. [DOC058-U0001-C0002]

**Task-type integrity:** Valid. All requested location and approval conditions occur in adjacent rules within this single chunk. Enumerating those rules does not materially require distinct evidence locations.

**Ambiguity assessment:** No material defect. The Freeport-level FBC and the project's own business case are separate approval layers; government, accountable body, Board and awarding authority are distinguished. “Seed-capital subsidy” matches the source scheme. The source contains the awkward phrase “an approval Full Business Case”; the answer preserves the substantive requirement of justification in the FBC without inventing a separate approval stage. The question concerns location/project approval, not every eligibility, cumulative-subsidy or recovery condition. No unclear current-policy timeframe or answer-bearing clue is introduced.

**Source sufficiency:** Sufficient for the specified conditions. The recovery clause cut off at the chunk end is not relied on.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T014

- **task_id:** T014
- **task_type:** within_document_reasoning
- **required_documents:** DOC043

**Exact candidate question**

> How are the Business Case, Tax Site and Customs Site processes linked during setup, and what sequencing conditions connect OBC, tax-site designation and FBC approval?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC043-U0001-C0001 | REQUIRED | Section 1.1.2 names the three approval processes; 1.1.3 explicitly explains their reciprocal linkage and both sequencing conditions: OBC before tax-site designation, and at least one designated customs site before FBC approval. |
| DOC043-U0001-C0002 | SUPPORTING | Sections 2.2–2.3 add tax-site criteria/value-for-money safeguards, possible unfulfilled OBC conditions, HMRC site checks and separate business authorisation. These elaborate process operation but are not required to answer the exact linkage/sequencing question. |

**Evidence-supported reference-answer candidate**

The Business Case Process scrutinises the strategic vision, economic impact and delivery structures for tax and customs sites; the Tax Site and Customs Site Processes activate the policy levers needed to deliver that vision. Tax sites cannot be designated until the Outline Business Case (OBC) has been approved, and at least one customs site must have been designated before the Full Business Case (FBC) can be approved. [DOC043-U0001-C0001, section 1.1.3]

**Task-type integrity:** Invalid for the assigned type. The complete minimal answer is explicit in section 1.1.3 of C0001 alone. C0002 provides operational detail, but the question does not require that detail or its synthesis with C0001. Two supplied targets therefore do not meet the frozen requirement for material synthesis across at least two distinct evidence locations. This finding preserves the assigned type and question for human adjudication; it is not an automatic reclassification.

**Ambiguity assessment:** No separate material ambiguity defect. OBC/FBC refer to the Outline/Full Business Cases, and the two site-approval processes are distinguished. The setup-phase timeframe is clear. Naming the processes and milestones identifies the subject without stating the order. Do not infer from these chunks an additional rule that every tax site must be designated before FBC approval.

**Source sufficiency:** Sufficient to answer the substantive question, but insufficient to justify its assigned reasoning type.

**Verdict:** DEFECT_REQUIRES_REVIEW

**Exact defect:** A complete answer to the exact candidate question is obtainable from DOC043-U0001-C0001 alone, so the candidate does not materially require synthesis across at least two distinct evidence locations as mandated for within_document_reasoning. DOC043-U0001-C0002 is supporting rather than necessary. Human review must adjudicate this mismatch; no revision or replacement is made here.

## T015

- **task_id:** T015
- **task_type:** within_document_reasoning
- **required_documents:** DOC045

**Exact candidate question**

> How does the national planning protocol seek to accelerate Green Freeport consenting while retaining normal statutory decision frameworks, and what roles do councils, consultees and developers play?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC045-U0001-C0002 | REQUIRED | Retains legislative/development-plan and other regulatory frameworks; accelerates processing through joint working, early evidence/EIA/Habitats work, processing agreements, infrastructure clarity and qualified two-/four-month planning timescales. |
| DOC045-U0001-C0003 | REQUIRED | Sets out distinct council, statutory consultee/agency and developer responsibilities, including contacts, coordination, deadlines, community engagement and timely high-quality information. |
| DOC045-U0001-C0004 | SUPPORTING | Repeats the developer-information/Habitats duties at the end of C0003; adds Scottish Government support/call-in handling and the 12-week statutory pre-application consultation note for major/national development. The extra note corroborates statutory safeguards; it is not needed for the minimal requested account of the three actors. |

**Evidence-supported reference-answer candidate**

The protocol accelerates consenting through coordinated early engagement, shared evidence, early environmental screening/scoping and processing agreements with agreed timelines and infrastructure arrangements. Planning decisions still follow legislation and the development plan unless material considerations indicate otherwise; other consents retain their established regulatory frameworks. It seeks decisions within two months for local and four months for major/national planning applications without legal agreements; where legal agreements are involved, committee or delegated decisions should be taken within those periods wherever possible. More complex applications may have longer agreed timescales. [DOC045-U0001-C0002]

Councils align consent processes, provide senior and application contacts, coordinate pre-application information requirements, agree consultee deadlines, review processing dates with developers within four weeks of validation and discuss conditions/contributions and legal agreements early. Statutory consultees provide contacts, clarify information needs early and adhere to reasonable response dates, contacting authority leads if deadlines are missed. Developers engage early with councils/agencies and communities, submit and supply timely high-quality information, consider reasonable legal-agreement/contribution requests and agree Habitats assessment information and surveys early. [DOC045-U0001-C0003]

**Task-type integrity:** Valid. C0002 supplies the framework-preservation and acceleration commitments; C0003 supplies the complete division of actor responsibilities. C0003's overlapping opening lacks C0002's statutory-framework explanation, while C0002 lacks the substantive consultee/developer account. Neither alone supports the complete answer. C0004 need not be necessary for the type to be valid.

**Ambiguity assessment:** No material defect. “Accelerate” means efficient processing, not a relaxed legal test or guaranteed permission. The question distinguishes councils, consultees and developers; the answer uses statutory consultees/agencies where the source does. Timelines are qualified rather than absolute. The protocol is assessed as frozen guidance, not as proof of achieved speed. The question names the policy mechanism but contains no answer-bearing dates or role assignments.

**Source sufficiency:** Sufficient across C0002–C0003; C0004 supports additional context without repairing an answer gap.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T016

- **task_id:** T016
- **task_type:** within_document_reasoning
- **required_documents:** DOC051

**Exact candidate question**

> How do the customs-site-operator role and Freeport business authorisation differ and interact, including when a customs site operator needs an additional Freeport customs procedure authorisation?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC051-U0004-C0002 | REQUIRED | Business authorisation for declarations/activities, transfer exception, agreement with site operator, and additional procedure authorisation when an operator itself imports or conducts activities on goods declared to the Freezone procedure. |
| DOC051-U0005-C0001 | REQUIRED | Operator controls goods movement and people's access, prevents unauthorised activity, keeps records and fulfils designation-order/security/HMRC access obligations. |
| DOC051-U0005-C0002 | SUPPORTING | Additional accountability and interaction: conditional joint/several import-duty liability and consequences for authorised businesses when site designation is revoked. These deepen, but are not essential to, the basic role/authorisation distinction and operator-agreement interaction. |

**Evidence-supported reference-answer candidate**

The customs site operator is the responsible authority controlling goods movement and people's access, taking reasonable steps to prevent unauthorised activity and meeting designation-order requirements for records, site security and HMRC access/facilities. [DOC051-U0005-C0001] A business separately needs HMRC authorisation to declare goods for the free-zone procedure and conduct industrial, service or commercial activities on those goods; the specified transfer-of-free-zone-goods activity is excepted. It must confirm at application that it has an agreement with the relevant operator allowing it to operate on the site. The operator also needs Freeport customs procedure authorisation, in addition to its operator role, if it wishes to import goods to the site or carry out activities on goods declared to that procedure. [DOC051-U0004-C0002]

**Task-type integrity:** Valid. C0002 of U0004 explains the business authorisation and additional-authorisation trigger but does not supply the substantive operator-duty account; C0001 of U0005 explains those duties without the business-authorisation conditions. Their synthesis distinguishes site management from authorised goods activity and explains their agreement/dual-role connection. These are distinct source units, not merely overlapping chunks.

**Ambiguity assessment:** No material defect. “Business authorisation” maps to the Freeport customs procedure authorisation described in U0004; it is distinct from the operator role/designation. The actor may occupy both roles, which is exactly what the final clause addresses. The answer preserves the transfer exception and does not equate authorisation with site ownership. No current timeframe, alternative legal opinion or trigger beyond the stated conditions is inferred. The question identifies the distinction to explain without revealing its answer.

**Source sufficiency:** Sufficient across the two required locations. C0002 of U0005 ends mid-sentence on final revocation consequences; the candidate answer does not rely on that unfinished sentence.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T017

- **task_id:** T017
- **task_type:** cross_document_reasoning
- **required_documents:** DOC056, DOC057

**Exact candidate question**

> How do enhanced Structures and Buildings Allowance and Enhanced Capital Allowance differ in eligible assets, relief structure and qualifying use/location conditions in Scottish Green Freeport tax sites?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC056-U0001-C0001 | REQUIRED | Structures/buildings qualifying expenditure; Scottish designation-to-30 September 2034 window; construction, qualifying-use and expenditure location/timing conditions; Corporation Tax or Income Tax registration. |
| DOC056-U0001-C0002 | REQUIRED | 10% per year for ten years, allowance start date and enhanced/normal apportionment for partly out-of-site or late qualifying use. |
| DOC057-U0001-C0001 | REQUIRED | Unused/non-second-hand plant and machinery for qualifying trading activity, primary special-tax-site use, Corporation Tax registration, Scottish window and 100% accounting-period relief. |
| DOC057-U0001-C0002 | REQUIRED | Five-year primary special-tax-site use requirement and withdrawal; completes the specific mixed-use/main-purpose restriction begun in C0001. |

**Evidence-supported reference-answer candidate**

Enhanced Structures and Buildings Allowance covers qualifying expenditure on structures/buildings and provides 10% annually for ten years, starting at the later of first non-residential use and incurring qualifying expenditure. Construction must begin while the asset is in a special tax site (first contract or construction work, whichever is earlier); qualifying use and expenditure must occur while in the site and by 30 September 2034 for Scottish Green Freeports. The claimant must meet the ordinary structures/buildings allowance requirements and be registered for Corporation Tax or Income Tax. Enhanced and normal rates are apportioned where part lies outside the site or part enters qualifying use after the deadline. [DOC056-U0001-C0001; DOC056-U0001-C0002]

Enhanced Capital Allowance covers unused, non-second-hand plant/machinery for trading activity or a land activity taxed as trading. It provides 100% of qualifying expenditure against qualifying-activity profits in the accounting period of expenditure; the claimant must be registered for Corporation Tax. At expenditure the asset must be intended primarily for use in a designated special tax site; Scottish qualifying expenditure runs from designation to 30 September 2034. Primary special-tax-site use must continue for five years from first qualifying use or keeping for qualifying use there; cessation within that period requires withdrawal and notification within three months. For mixed use, the restriction to expenditure attributable to site use applies when the asset is also for use outside a site and the main purpose of expenditure is to obtain the enhanced allowance for that outside-site part. [DOC057-U0001-C0001; DOC057-U0001-C0002]

Both concern tax sites, which the guidance distinguishes from separately authorised customs sites. [DOC056-U0001-C0001; DOC057-U0001-C0001]

**Task-type integrity:** Valid. DOC056 supplies the structures/buildings side; DOC057 supplies the plant/machinery side. Neither supplies the other allowance's asset, relief-rate and continuing-use rules. Comparing the three requested dimensions therefore materially requires both documents, not merely two documents repeating a shared designation window.

**Ambiguity assessment:** No material defect. Scottish conditions are selected expressly, so the English 2031 deadline is not substituted. Allowance duration, qualifying-expenditure deadline and continuing-use duration are kept distinct. Tax-site location is not confused with customs-site authorisation. The named allowances and comparison dimensions do not reveal the answer. General eligibility guidance linked from the chunks is not imported: this is a comparison of the supported conditions, not an exhaustive legal eligibility determination for a hypothetical asset.

**Source sufficiency:** Sufficient for the requested comparison. The mixed-use ECA limitation is stated with both conditions; no generic pro-rata restriction is invented. Examples and linked pages are not needed.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## T018

- **task_id:** T018
- **task_type:** cross_document_reasoning
- **required_documents:** DOC052, DOC053

**Exact candidate question**

> How do the Inverness and Cromarty Firth and Forth Green Freeports use seed capital to unlock investment, including funding scale, project selection/deployment and governance/accountability arrangements?

**Evidence chunks and classification**

| Chunk | Classification | Frozen support |
|---|---|---|
| DOC052-U0012-C0001 | REQUIRED | £25m enabling infrastructure to unlock tax-site land; 11 preferred projects and Council OBC gateway assessment using Green Book principles, economic benefits, viability and affordability. |
| DOC052-U0012-C0002 | REDUNDANT | Repeats the final 75 words of C0001 and adds the concluding word “delivery.” This completes the sentence but adds no independent material fact needed by the minimal answer. |
| DOC052-U0014-C0001 | REQUIRED | FBC review after award confirmation by investment subgroup, subsidy control/change requests, Council accountable-body role versus partner delivery, and complementary public/private funding scale. |
| DOC053-U0008-C0001 | REQUIRED | Expected £24.5m + £8m public + £64.4m private = circa £96.9m project expenditure; procurement, operating-company oversight and compliance/audit/reporting functions. |
| DOC053-U0027-C0001 | REQUIRED | Investment Hierarchy/local-authority assessment, four core projects, £17.9m minimum ask and maximum £24.5m enabling six further projects. |
| DOC053-U0028-C0001 | REQUIRED | Early seed capital as investment lever; tax-site Investment Principles agreements, monitoring by landowners/OpCo, reporting to Governance Board and Accountable Body (Falkirk Council). The accountability evidence here concerns tax-site investment governance, not a separately stated seed-grant disbursement procedure. |

**Evidence-supported reference-answer candidate**

Inverness and Cromarty Firth proposes £25m of seed capital for enabling infrastructure that unlocks tax-site land. Sponsors of 11 preferred projects submitted project OBCs for Council gateway assessment toward FBC, using Green Book principles and considering benefits, viability and affordability. [DOC052-U0012-C0001] Following confirmation of the award, sponsors are to submit FBCs to the accountable body, reviewed by an investment subgroup comprising Freeport-company and Highland Council representatives, with further subsidy-control checks and government change requests for reserve-list alternatives if necessary. Highland Council is accountable for accounting and public governance; the Freeport and partners deliver the programme and manage delivery, risk and outcomes. The £25m is to be complemented by over £60m further public funding and almost £175m private funding, giving around £260m total seed-capital project expenditure. [DOC052-U0014-C0001]

Forth uses early seed capital as an investment lever. [DOC053-U0028-C0001] Proposals were assessed/prioritised in line with the Scottish Government Investment Hierarchy and considered by local-authority partners. Four core projects—Forth Ports Leith land preparation, Babcock integrated energy system, Grangemouth utility capacity and INEOS low-carbon hydrogen preparation—require a minimum £17.9m ask, attracting at least £17.9m private match funding. The maximum £24.5m ask enables six additional projects costing £6.6m, with £12.9m partner match funding. [DOC053-U0027-C0001] The financial case expects £24.5m seed capital to attract £8m further public and £64.4m private funding, for circa £96.9m overall project expenditure; these are the financial-case totals, distinct from the proposal-level match-funding figures. Procurement is by private landowners and other sponsors, including public bodies, aligned with general public procurement rules. Forth Green Freeport Operating Ltd delivers under Forth Green Freeport Ltd oversight; operating functions include financial compliance/audit, reporting and monitoring/evaluation. [DOC053-U0008-C0001] In tax-site investment governance, Investment Principles are implemented through agreements addressing reporting, monitoring/evaluation and subsidy obligations; landowners and the operating company monitor compliance, reporting to the Governance Board and accountable body, Falkirk Council. [DOC053-U0028-C0001]

Both use public seed capital and enabling projects to attract wider investment, with local-authority accountability and Freeport/partner delivery structures. The frozen reports describe proposals, expectations and approval/deployment arrangements; these figures do not establish completed expenditure or realised investment.

**Task-type integrity:** Valid. DOC052 provides Inverness and Cromarty Firth's programme, scale and Highland accountability; DOC053 provides Forth's programme, scale, selection and governance. Neither alone supplies a complete comparison of both Freeports. DOC053's naming of the other successful bid is not evidence of its programme. The redundant short continuation in DOC052 does not undermine the genuine cross-document requirement.

**Ambiguity assessment:** No material defect, with interpretation boundaries stated. “Use” is read as the reports' described/proposed mechanism, not a demand for realised results at the audit date. Seed funding, total project expenditure, match funding and unrelated investment/land-value figures are kept distinct. Inverness's Council is identified as Highland; Forth's accountable body is Falkirk, distinct from Edinburgh's membership in Forth governance. Governance includes programme delivery and tax-site investment accountability; U0028's tax-site obligations are not asserted to be universal seed-grant recipient terms. The question specifies the two actors and comparison dimensions without supplying amounts or outcomes.

**Source sufficiency:** Sufficient to describe each programme's scale, selection/deployment and governance at the reports' level. The named targets do not support an audit of actual disbursement, complete grant-contract terms or realised investment; none is requested or asserted. The two Forth sets of match/total figures are reported in their respective contexts rather than forced into a fabricated reconciliation.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified.

## Aggregate checks and adjudication

| Check | Result | Basis |
|---|---|---|
| DIRECT_COUNT | 3 | T011, T012, T013; matches frozen protocol slots. |
| WITHIN_DOCUMENT_COUNT | 3 | T014, T015, T016; assigned types retained despite T014 defect. |
| CROSS_DOCUMENT_COUNT | 2 | T017, T018; matches frozen protocol slots. |
| ALL_REFERENCED_CHUNKS_EXIST | PASS | 21/21 unique named targets exist exactly once with matching document/use-case IDs and text hashes. |
| REQUIRED_DOCUMENTS_MEMBERSHIP_VALID | PASS | All 10 unique required documents are accepted: DOC043, DOC045, DOC046, DOC047, DOC051, DOC052, DOC053, DOC056, DOC057, DOC058. All are outside the excluded set. |
| TASK_TYPE_INTEGRITY | FAIL — T014 requires review | 7/8 valid; T014 is fully answerable from a single localized passage. |
| AMBIGUITY_AUDIT | PASS — no material ambiguity defect identified | All eight assessed; source-snapshot, terminology, actor and qualification boundaries recorded above. |
| REFERENCE_SUPPORT_AUDIT | PASS | Every reference-answer claim is supported by named frozen targets, including explicit conditions and prospective status. T014's answer support passes while its type fails. |

```text
DIRECT_COUNT=3
WITHIN_DOCUMENT_COUNT=3
CROSS_DOCUMENT_COUNT=2
ALL_REFERENCED_CHUNKS_EXIST=YES
REQUIRED_DOCUMENTS_MEMBERSHIP_VALID=YES
TASK_TYPE_INTEGRITY=FAIL_T014_REQUIRES_REVIEW
AMBIGUITY_AUDIT=PASS
REFERENCE_SUPPORT_AUDIT=PASS
READY_FOR_HUMAN_REVIEW_COUNT=7
DEFECT_REQUIRES_REVIEW_COUNT=1
```

| task_id | Assigned task_type | Verdict |
|---|---|---|
| T011 | direct_retrieval | READY_FOR_HUMAN_REVIEW |
| T012 | direct_retrieval | READY_FOR_HUMAN_REVIEW |
| T013 | direct_retrieval | READY_FOR_HUMAN_REVIEW |
| T014 | within_document_reasoning | DEFECT_REQUIRES_REVIEW |
| T015 | within_document_reasoning | READY_FOR_HUMAN_REVIEW |
| T016 | within_document_reasoning | READY_FOR_HUMAN_REVIEW |
| T017 | cross_document_reasoning | READY_FOR_HUMAN_REVIEW |
| T018 | cross_document_reasoning | READY_FOR_HUMAN_REVIEW |

## Mandatory provenance

```text
LLM_ASSISTED_CANDIDATE_AUTHORING=YES
B0_B1_G1_OUTPUT_USED=NO
RETRIEVAL_RANKING_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
BENCHMARK_RESULT_USED=NO
TASKS_HUMAN_VERIFIED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
```

No benchmark task JSON was created. The corpus, schemas, protocol, source code, tests, existing evidence and frozen artifacts were not modified. No staging, commit or push was performed. Human review remains required for all reference answers and evidence, including adjudication of T014. Audit completion is separate from candidate approval.

## Frozen-source fingerprint ledger

These hashes identify the exact bytes inspected; per-chunk text hashes identify the supporting frozen text without relying on current contents of the source URLs. Word ranges are zero-based with exclusive end offsets within the source unit. PDF page numbers refer to canonical metadata.

| File | SHA256 |
|---|---|
| `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl` | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| `corpus/use_cases/UC2/corpus_membership.json` | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| `benchmark/task_authoring_protocol_v0.1.json` | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |

| Chunk | Canonical line | Source unit | Word range | PDF page | Text SHA256 |
|---|---|---|---|---|---|
| DOC046-U0001-C0002 | 122 | DOC046-U0001 | [375, 825) | — (HTML) | `43663cab2ac84b0b54dcd33e0d807b978eb1ad19e987a67d52cca3648cb912b5` |
| DOC047-U0001-C0001 | 129 | DOC047-U0001 | [0, 450) | — (HTML) | `fa069a33efb872292b8973d62a10a6354d4b364968470bb05871d51ae1a4263a` |
| DOC058-U0001-C0002 | 292 | DOC058-U0001 | [375, 825) | — (HTML) | `a87859c86f6410c4ea80228c62be1986f8dbaad4435726cd6b1d1298e89237ec` |
| DOC043-U0001-C0001 | 64 | DOC043-U0001 | [0, 450) | — (HTML) | `1c5efcdd90a3d9e2dba80ce3b0e2471b80b07617d0748547c7721edf15e8751d` |
| DOC043-U0001-C0002 | 65 | DOC043-U0001 | [375, 825) | — (HTML) | `23428b5df0659c5bde465e8ab0d669b0acd997f60bf0fa1c35a86dc5e48edbac` |
| DOC045-U0001-C0002 | 118 | DOC045-U0001 | [375, 825) | — (HTML) | `a506381d377985cdb69d6a61bcdb83bfb828f608c310ccb9a3cc05e124673a3f` |
| DOC045-U0001-C0003 | 119 | DOC045-U0001 | [750, 1200) | — (HTML) | `69e486edfc05a05a5849821173e715874223986cdd054a4b425bc49cee11ea27` |
| DOC045-U0001-C0004 | 120 | DOC045-U0001 | [1125, 1279) | — (HTML) | `bc676fcf7e78f928de1bfafb631ba7e544a145f82a29f4b49743c2cb44029af7` |
| DOC051-U0004-C0002 | 169 | DOC051-U0004 | [375, 701) | — (HTML) | `70bdbf8f9adf895ede400aee8d38827f2123266e5bc668597fb4822947f5c879` |
| DOC051-U0005-C0001 | 170 | DOC051-U0005 | [0, 450) | — (HTML) | `5f2e48c16af1d40cea75fb3acf0fa7ab43b85de074ee52ffc7be23358a6db411` |
| DOC051-U0005-C0002 | 171 | DOC051-U0005 | [375, 825) | — (HTML) | `e9f4ac8f10801f5df61552c3660d7353060c3c433138b22ea82b6b09f83bf7bc` |
| DOC056-U0001-C0001 | 284 | DOC056-U0001 | [0, 450) | — (HTML) | `850c8f841a6964039b5cd1667fc700d25b85369ceb4ebeed74b6b1b63c59ad2f` |
| DOC056-U0001-C0002 | 285 | DOC056-U0001 | [375, 825) | — (HTML) | `59448e424670bb8a46b0bfb8a74798faf9149c155a52e302c0807c2a2ea86d62` |
| DOC057-U0001-C0001 | 287 | DOC057-U0001 | [0, 450) | — (HTML) | `ae6e863d5300a974fef0ff52cf9ad52ebc0c3e6848140fc2cc1780d0697f6edb` |
| DOC057-U0001-C0002 | 288 | DOC057-U0001 | [375, 825) | — (HTML) | `3d3a615ce5a96557e53bd9b7addc30d609866f24b7b45667b136c7b0bc09c5eb` |
| DOC052-U0012-C0001 | 202 | DOC052-U0012 | [0, 450) | 12 | `67964d32e0d957be9ca28c2cf124cc6b9960f727f7a0bd85fc5ad66057f14ce3` |
| DOC052-U0012-C0002 | 203 | DOC052-U0012 | [375, 451) | 12 | `5830417614601aa74cccbaa8f64c068e81af3db3dc4dda4062523b6226ae867c` |
| DOC052-U0014-C0001 | 206 | DOC052-U0014 | [0, 450) | 14 | `b4a5454740f28208a58d3ad3572309a252f479ff71a48f6fa9825d75deb60154` |
| DOC053-U0008-C0001 | 236 | DOC053-U0008 | [0, 438) | 8 | `f0d4496da0da8c33582a7a15f3d712761a67e3c1d772e3809d5606ed529ba4e0` |
| DOC053-U0027-C0001 | 256 | DOC053-U0027 | [0, 243) | 27 | `9e530375a51793b8e24666f31533369b9686a0e2c5271fada92aa1251405af33` |
| DOC053-U0028-C0001 | 257 | DOC053-U0028 | [0, 393) | 28 | `b86f1b34a4b4877452cc9bbb4ce2417424eb44917b6b5d5bb95297725961475c` |

## T014 Human-Directed Pre-Freeze Revision 1

This section records the user-authorized revision of T014 only, on 26 September 2026. The original T014 question, evidence assessment, `DEFECT_REQUIRES_REVIEW` verdict and initial aggregate findings above remain unchanged as the historical audit. This revision addresses the original task-type integrity defect through the exact new question supplied by the user. It is based solely on frozen-source inspection and the requirement for material within-document synthesis, with no retrieval-performance or benchmark/model-result input. Human direction authorizes this revision; it does not constitute human verification or task freeze.

**Revision preconditions:** The branch remains `research/benchmark-task-construction-uc2-uc3`, HEAD remains `4ca03cde8dd969c07590670615008b17d5448a2e`, and before appending there was exactly one untracked file: this audit. Its original SHA256 was `849a094f3936600a85199ae2926a303a5cdc44ca5739bdb5769d29649a223a4d`. The canonical JSONL, membership and protocol hashes still match the frozen-source fingerprint ledger above. DOC043 is accepted UC2 membership and is not excluded; T014 remains a within_document_reasoning slot under the frozen protocol.

- **task_id:** T014
- **task_type:** within_document_reasoning
- **required_documents:** DOC043
- **primary evidence assessed:** DOC043-U0001-C0004; DOC043-U0001-C0009
- **optional supporting evidence assessed:** DOC043-U0001-C0005; DOC043-U0001-C0010; DOC043-U0001-C0032

**Exact revised candidate question**

> How are seed capital and retained non-domestic rates intended to play different financing roles in Green Freeport delivery, and how do their accountability and governance arrangements differ?

### Evidence verification and classifications

All five named IDs occur exactly once in the frozen canonical `chunks.jsonl`. All five have `document_id=DOC043`, `use_case_id=UC2`, and `source_unit_id=DOC043-U0001`; all recomputed UTF-8 text SHA256 values match their stored `text_sha256`. Classifications use the definitions in the original audit and are relative to this revised question and its minimal complete answer.

| Evidence chunk | Classification | Evidence-supported contribution and boundary |
|---|---|---|
| DOC043-U0001-C0004 | REQUIRED | Section 3.1.7 expects seed capital for projects deliverable in the short term and longer-term public investment to be financed using retained NDR. Section 3.1.8 states capital funding is paid to the accountable body in annual tranches; that body ensures relevant regulations/best practice, including public procurement, Value for Money and policy objectives, using local project assurance/business-case processes. Section 3.1.6 assigns Business Case approval to the Programme Board with joint government representation. This chunk does not state retained-NDR local-authority accountability, governing-body strategic direction or the 25-year retention guarantee. |
| DOC043-U0001-C0009 | REQUIRED | Section 6.1.1 continuation identifies tax-site NDR growth above an agreed pre-designation baseline, minus an agreed displacement factor, with retention guaranteed for 25 years to give local authorities certainty to borrow for regeneration/infrastructure. Section 6.1.3 keeps local authorities accountable for retained NDR as public funds and places its strategic direction with the Green Freeport governing body. Sections 6.1.2 and 6.1.5–6.1.6 set Green Freeport-related purposes and eligible uses, including operating costs and investment-supporting activity. This chunk does not supply seed-capital payment, project-assurance or Programme Board provisions. |
| DOC043-U0001-C0005 | SUPPORTING | The opening overlaps C0004's local-assurance passage, but the chunk adds project procurement/contract-management/risk-transfer detail (3.1.9), accountable-body subsidy-control consideration across capital, revenue and NDR measures (3.1.10), and expected first payment after FBC approval and an agreed MoU, with later payments subject to annual assurance reviews (3.1.11). These deepen governance detail; C0004 already supports the minimal seed-capital account. |
| DOC043-U0001-C0010 | SUPPORTING | Section 6.1.8 adds governing bodies' proposed displacement factors, matched to Economic Case assumptions. Section 7.1.3 gives retained NDR or business contributions as possible support for planning-measure costs. These contextualize retained-NDR calculation/use without supplying a missing core financing/accountability comparison. The overlapping opening adds no need to treat it as required. |
| DOC043-U0001-C0032 | SUPPORTING | Sections 13.4.6–13.4.7 state that, following FBC approval, an agreed MoU covers accountable-body and governing-body roles and planned retained-NDR use, formalises delivery expectations and can be amended by agreement. Section 13.5.1 distinguishes OBC summaries from fuller FBC seed-capital activities and retained-NDR strategy. This provides governance formalisation but does not independently provide the short-term/long-term roles, seed-capital assurance duties or 25-year guarantee. |

### Minimal complete reference-answer candidate

Seed capital is intended for projects deliverable in the short term; longer-term public investment projects are expected to use retained non-domestic rates. Seed capital is paid to each coalition's accountable body in annual tranches. That body is responsible for ensuring relevant regulations and best-practice standards, including public procurement, are met and that Value for Money and policy objectives are delivered, taking individual projects through local assurance/business-case processes. Business Cases are approved by the Green Freeport Programme Board, with joint representation from the governments. [DOC043-U0001-C0004, sections 3.1.6–3.1.8]

Retained NDR concerns tax-site rates growth above an agreed pre-designation baseline, minus an agreed displacement factor. Retention is guaranteed for 25 years, providing local authorities certainty to borrow for regeneration and infrastructure supporting further growth. The local authority or authorities remain accountable for its use as public funds, while strategic direction should be set by the Green Freeport governing body. The retained funds are expected to support Green Freeport-associated purposes, including operating costs and investment-supporting infrastructure and other activities. [DOC043-U0001-C0009, section 6.1.1 continuation and sections 6.1.2–6.1.6]

### Task-type integrity and evidence-removal assessment

**Assigned task type is valid.** A complete answer requires comparison of both the financing roles and the accountability/governance arrangements across the two distinct evidence locations in DOC043:

- **Seed-capital side alone (C0004/C0005):** C0004 explicitly contrasts short-term seed projects with longer-term retained-NDR investment, so financing-role contrast alone would not establish synthesis. C0004/C0005 supply seed payment/assurance and approval arrangements, but not the retained-NDR 25-year guarantee or the separation between local-authority public-fund accountability and governing-body strategic direction. They cannot answer the complete revised question alone.
- **Retained-NDR side alone (C0009/C0010):** These supply retention, investment purposes, accountability, strategic direction and displacement-factor detail, but not seed capital's short-term deliverability focus, payment to the accountable body in annual tranches, local project assurance or Programme Board approval. They likewise cannot answer the complete revised question alone.
- **Optional C0032:** It formalises roles and NDR planning through an MoU but does not fill either missing substantive financing/assurance account. It corroborates governance rather than eliminating the need for C0004 and C0009.

The two required chunks occupy disjoint source-unit word ranges, [1125, 1575) and [3000, 3450), and different substantive sections (3.1 and 6.1). This is material synthesis within one document, not counting overlapping chunks or importing evidence from another document. The optional chunks are not necessary for the minimal complete answer.

### Ambiguity, terminology, timeframe and answer-clue audit

**Ambiguity assessment:** No material ambiguity defect identified.

- **Financing roles:** The temporal division is an expressed expectation for public investment, not an exclusive legal allocation of every activity. Retained NDR also supports operating costs and other listed purposes; the answer does not assert that it funds only long-term capital projects or that seed capital alone funds all short-term activity.
- **Terminology:** NDR means non-domestic rates. Retention concerns growth above the agreed baseline after a displacement adjustment, not all collected rates and not NDR relief granted to a beneficiary. Seed capital is the capital funding in section 3.1, distinct from ongoing retained rates revenue.
- **Actors and governance:** The accountable body, local authority/authorities, Green Freeport Programme Board and Green Freeport governing body are identified by the source's distinct roles. The comparison does not assert that accountable bodies and local authorities must be different organizations. It distinguishes seed-project assurance and approval from retained-fund accountability and strategic direction. Shared public-fund controls are not represented as absent on either side; C0005 expressly describes subsidy-control consideration across funding and NDR measures.
- **Timeframe:** “Intended” anchors the answer to the frozen setup guidance's prospective delivery arrangements, not realised expenditure or current policy. The chunks do not define an exact number of years for “short-term” or “longer-term”; the answer retains those terms without inventing a cutoff. The 25-year figure is a guarantee of retention, not a claim that revenue amounts or borrowing returns are guaranteed. No unsupported start date or end date is assigned to it.
- **Accidental answer clues:** The wording identifies the two financing mechanisms and comparison dimensions but gives no duration, payment arrangement, approval actor or allocation of accountability. The premise of different roles is supported by section 3.1.7 and does not disclose the substantive comparison.

### Source sufficiency and revised verdict

**Source sufficiency:** Sufficient strictly from frozen DOC043. C0004 and C0009 jointly support every claim in the minimal reference answer, including the six substantive points specified in the human instruction. Optional evidence supports additional governance detail without introducing mandatory answer elements. No claim relies on the unfinished ending of C0004 or the separate guidance referenced in C0009. No live source, external law, inferred revenue amount, borrowing mechanism detail or completed funding outcome has been added.

**Information-use confirmation:** Only frozen corpus text, membership, the frozen authoring protocol and the user-supplied revision were used. No retrieval operation, ranking, diagnostic retrieval result, embeddings, task-execution model inference, B0/B1/G1 output or benchmark result was used. The reference answer is an LLM-assisted authoring candidate, not an executed benchmark response.

**Original T014 verdict:** DEFECT_REQUIRES_REVIEW — unchanged historical record.

**Final revised T014 verdict:** READY_FOR_HUMAN_REVIEW

**Exact revised defect:** None identified. Human verification of the revised question, answer and evidence remains outstanding. This revised assessment resolves the original single-location task-type defect for the new question only; it does not erase or retroactively change the original question's failure or initial aggregate audit.

### Revision provenance

```text
REVISION_REASON=TASK_TYPE_INTEGRITY_DEFECT
REVISION_STAGE=PRE_FREEZE
HUMAN_DIRECTED_REVISION=YES
RESULT_DRIVEN_REVISION=NO
B0_B1_G1_OUTPUT_USED=NO
RETRIEVAL_RANKING_USED=NO
RETRIEVAL_DIAGNOSTIC_RESULTS_USED=NO
BENCHMARK_RESULT_USED=NO
TASKS_HUMAN_VERIFIED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
```

### Revision evidence fingerprints

The five source records have the same source-unit text SHA256: `92883531159d5c264937dd3cdb210ffd1b97f399e9619efe001c95e251013997`. Canonical line numbers refer to the unchanged JSONL. Word offsets are zero-based with exclusive end offsets.

| Chunk | Canonical line | Source unit | Word range | Text SHA256 |
|---|---|---|---|---|
| DOC043-U0001-C0004 | 67 | DOC043-U0001 | [1125, 1575) | `95663526d60c0445717fa1cfef26de5225ff2da92cac571c97bb172b9e91b7b6` |
| DOC043-U0001-C0009 | 72 | DOC043-U0001 | [3000, 3450) | `804fa98a7dcf9806e5590166d1b81762e91c77a781e8e4ae90ad169d31438e04` |
| DOC043-U0001-C0005 | 68 | DOC043-U0001 | [1500, 1950) | `be31504d4f7db8ffd18dfb5d0f68b2bb84df632d807614ca647e53824ca06530` |
| DOC043-U0001-C0010 | 73 | DOC043-U0001 | [3375, 3825) | `9be4229d0548cf76f93fdfe82fde98809ff1a33e8d8b386442246b6f4b3be701` |
| DOC043-U0001-C0032 | 95 | DOC043-U0001 | [11625, 12075) | `2ac8bd96b032ad8c8bf2a3dbda8368eaf19cc3cdb1f93761a2cca27cac1279be` |
