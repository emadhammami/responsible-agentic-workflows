# UC2 insufficient-evidence candidate corpus-wide absence audit — 26 September 2026

T019 and T020 are **READY_FOR_HUMAN_REVIEW** as insufficient-evidence candidates. The frozen canonical UC2 text does not supply either the realised job-creation totals or aggregate actual LBTT claim amounts requested separately for both Scottish Green Freeports by 31 March 2026. This conclusion concerns the contents of the frozen corpus, not whether such values exist outside it, and does not imply zero jobs or zero relief claims.

## Corpus identity, preconditions and scope

- Branch: `research/benchmark-task-construction-uc2-uc3`.
- Expected and observed HEAD: `4ca03cde8dd969c07590670615008b17d5448a2e`.
- Initial status: exactly one untracked artifact, `evidence/engineering/uc2_task_candidate_evidence_audit_2026-09-26.md`; no tracked or staged changes.
- Existing audit SHA256, preserved without modification: `728fe36bcfd3097005594053ffef69cb6ac586a09964be5579a2ee9437f15d56`.
- Canonical source: `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl`.
- Membership: `corpus/use_cases/UC2/corpus_membership.json`, frozen; 17 accepted documents, all represented, with no excluded document or unexpected document in the canonical file. DOC054 is excluded and not scanned as canonical evidence.
- Protocol: `benchmark/task_authoring_protocol_v0.1.json`, `PRIMARY-UC2-UC3-TASK-AUTHORING-v0.1`, status `frozen_before_task_authoring`; T019/T020 are the two UC2 insufficient_evidence slots and require a separate corpus-wide absence audit.
- Parsed records: 293; unique chunk IDs: 293; represented accepted document IDs: 17. Every record is UC2, has matching document/chunk prefix and candidate-membership mapping, and its recomputed UTF-8 text SHA256 matches the stored hash.

The corpus snapshot, not live source pages or current policy, is the evidentiary boundary. Absence is assessed in the canonical chunk text, including its frozen extraction limitations. Some PDF records contain only a page number, appendix label or figure title (notably DOC052 pages 25–32 and DOC053's governance figure). They are enumerated and screened as the text actually supplied; no unseen image contents or linked annexes are inferred. This is not a claim of absence from every original webpage/PDF or outside administrative dataset.

The audit does not simply assume all material predates the cutoff: DOC046 contains a 25 March 2026 update and DOC055 a 6 April 2026 update. Their content remains NDR reporting guidance and NI rules/examples, respectively, not the requested realised values.

## Deterministic method and coverage

1. Parse every nonempty JSONL record in physical file order; check record count, unique IDs, UC2 metadata, membership and text fingerprints.
2. Apply broad, case-insensitive Python regular-expression term families to the `text` field of every record. Each family is independent; screening uses their union, not an intersection that could suppress a plausible hit. No scoring, ranking, top-k truncation or semantic/vector search is used.
3. Inspect matching passage contexts across all documents for job/employment/workforce language, reporting/outcomes, tax relief and claims/values. Broaden the families to workers, hiring, apprenticeships, posts/positions, data/figures/numbers and completion. Read substantive near-miss passages and surrounding framing, including the full DOC047 guidance and DOC048 legislation, to distinguish examples/forecasts from achieved values. Re-read truncated tool-display ranges separately; display truncation is not an evidence-selection rule.
4. Inspect the corpus-wide chunk enumeration, including nonhits, headings/continuations and numeric/currency contexts. The supplementary numeric screen uses `£|\b\d[\d,]{2,}\b`; dates, statutory references, publication prices, map areas and unrelated budgets are not outcome data. Check adjacent/overlapping passages where framing continues, rather than interpreting isolated future/past-tense fragments as statistics.
5. Classify plausible passages through LLM-assisted source inspection using the user-specified taxonomies; retain all material findings below. Keyword matches do not automatically decide classification or sufficiency. The 293-row ledger records every chunk, family hits and analyst dispositions; it includes overlap duplicates explicitly.
6. Test sufficiency for each Freeport and the cutoff. For jobs, require observed job creation, an attributable count and adequate reporting-period scope; projections, baseline employee estimates, appointments and event attendance do not establish aggregate creation. For LBTT, require actual relief claimed, monetary aggregation, attribution and cutoff scope; rates, purchase prices, worked examples and other taxes fail that test.

All matching contexts judged plausible have been classified; broad false positives are explicitly excluded as IRRELEVANT where appropriate. Findings group repeated or related passages, but each named chunk is identifiable. No inference from keyword zero-matches alone supports the conclusion. No extrapolation from forecasts, interpolation to the cutoff, summation of examples or importing of external statistics is performed.

### Exact term families used

The following are reproducible scan definitions, not benchmark prompts:

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
| T020_TAX | 198 | 95 |
| T020_VALUES | 173 | 120 |
| T019 family union | 231 | 62 |
| T020 family union | 244 | 49 |

Nonmatching records are still included in the enumeration and structural/numeric screen. Generic “post,” “position,” “data” and “value” hits include mailing addresses, changed business-case positions, personal-data notices and value-for-money language; these are not automatically employment/claim observations. Hit totals overlap and must not be added to obtain corpus size.

### Document coverage

| Document | Canonical chunks | T019 union hits | T020 union hits | Inspected subject/screening outcome |
|---|---:|---:|---:|---|
| DOC041 | 53 | 50 | 43 | Bidding prospectus: policy, expected outputs, tax offer and monitoring requirements; no requested realised totals. |
| DOC042 | 10 | 9 | 8 | Clarification/Q&A: prospective bidding, relief availability and impact appraisal; no requested realised totals. |
| DOC043 | 40 | 39 | 37 | Setup guidance: financing, delivery, business cases, monitoring and reporting; no requested realised totals. |
| DOC044 | 13 | 13 | 12 | Policy impact assessment: incentives, anticipated benefits and controls; no requested realised totals. |
| DOC045 | 4 | 4 | 4 | Planning/consents protocol; no requested realised totals. |
| DOC046 | 8 | 8 | 8 | NDR relief/retention administration and reporting guidance; no requested realised totals. |
| DOC047 | 11 | 3 | 11 | Revenue Scotland LBTT Green Freeports guidance and examples; no requested realised totals. |
| DOC048 | 10 | 0 | 9 | LBTT Green Freeports relief legislation; no requested realised totals. |
| DOC049 | 5 | 0 | 4 | Inverness/Cromarty special-tax-site designation; no requested realised totals. |
| DOC050 | 4 | 0 | 3 | Forth special-tax-site designation; no requested realised totals. |
| DOC051 | 25 | 12 | 17 | Customs technical handbook; no requested realised totals. |
| DOC052 | 45 | 35 | 30 | Inverness/Cromarty FBC update and executive summary; no requested realised totals. |
| DOC053 | 50 | 47 | 44 | Forth FBC committee report and executive summary; no requested realised totals. |
| DOC055 | 5 | 5 | 5 | Employer NI relief guidance/examples; no requested realised totals. |
| DOC056 | 3 | 2 | 3 | Enhanced structures/buildings allowance guidance/examples; no requested realised totals. |
| DOC057 | 4 | 1 | 4 | Enhanced capital allowance guidance/examples; no requested realised totals. |
| DOC058 | 3 | 3 | 2 | Seed-capital subsidy eligibility/reporting guidance; no requested realised totals. |

## T019 — insufficient_evidence

**Exact candidate question**

> How many jobs had actually been created by each of the Inverness and Cromarty Firth Green Freeport and the Forth Green Freeport by 31 March 2026?

The requested values are realised job-creation counts separately for each Freeport by the stated cutoff. Forecasts, targets, employment baselines, estimates, pipeline jobs and anticipated outputs do not answer this question.

### Material near-miss and exclusion findings

All entries are paraphrases of frozen text. One entry is a grouped passage finding; it is not necessarily one chunk, one number or one independent economic estimate. An overlapping chunk may appear in more than one entry because it contains different passages.

| Finding | Classification | Exact canonical chunks | Frozen content | Why it does not answer the exact candidate |
|---|---|---|---|---|
| J01 | GENERAL_POLICY | DOC041-U0001-C0001; DOC041-U0001-C0002; DOC041-U0001-C0003; DOC041-U0001-C0004; DOC041-U0001-C0005; DOC041-U0001-C0006; DOC041-U0001-C0007; DOC041-U0001-C0008; DOC041-U0001-C0009; DOC041-U0001-C0010; DOC041-U0001-C0011; DOC041-U0001-C0012 | Prospectus job-creation, fair-work, sector and skills ambitions; mechanisms for attracting employment. | Statements of policy intention and economic context, not achieved counts for either Freeport. |
| J02 | TARGET | DOC041-U0001-C0013; DOC041-U0001-C0014 | Expected outcomes include increased jobs and wages, with future assessment through monitoring/evaluation. | Desired directional outcomes, not a numerical achievement return; no totals or 2026 cutoff. |
| J03 | GENERAL_POLICY | DOC041-U0001-C0018; DOC041-U0001-C0019; DOC041-U0001-C0020; DOC042-U0001-C0004; DOC042-U0001-C0005; DOC043-U0001-C0036; DOC043-U0001-C0037; DOC043-U0001-C0038 | Regeneration/underdevelopment tests, above-average unemployment, requests for current employee estimates and estimated additional/future employment. | Instructions to supply baseline and forecast evidence; no supplied realised creation totals. Existing employment or unemployment is not jobs newly created by the Freeports. |
| J04 | GENERAL_POLICY | DOC041-U0001-C0031; DOC041-U0001-C0032; DOC041-U0001-C0036; DOC041-U0001-C0038; DOC041-U0001-C0039; DOC041-U0001-C0040; DOC041-U0001-C0042; DOC041-U0001-C0043; DOC041-U0001-C0047; DOC041-U0001-C0048; DOC041-U0001-C0049; DOC042-U0001-C0005; DOC042-U0001-C0006 | Decarbonisation/job-creation plans, bid-selection criteria, implementation milestones, annual reporting and required data collection on new jobs/realised outcomes. | Reporting obligations and selection/appraisal material do not contain the resulting reported counts. A requirement to collect realised data is not that data. |
| J05 | GENERAL_POLICY | DOC043-U0001-C0006; DOC043-U0001-C0007; DOC043-U0001-C0009; DOC043-U0001-C0014; DOC043-U0001-C0015; DOC043-U0001-C0017; DOC043-U0001-C0018; DOC043-U0001-C0019; DOC043-U0001-C0020; DOC043-U0001-C0021; DOC043-U0001-C0022; DOC043-U0001-C0023; DOC043-U0001-C0024; DOC043-U0001-C0025; DOC043-U0001-C0026; DOC043-U0001-C0027; DOC043-U0001-C0032; DOC043-U0001-C0033; DOC043-U0001-C0034; DOC043-U0001-C0035 | Setup guidance covers workforce/skills, innovation, recruitment planning and future monthly/quarterly/biannual/annual monitoring; Q4 and annual periods can end 31 March. | These are delivery and reporting arrangements, not populated employment returns. A reporting-period date alone cannot supply the requested 31 March 2026 values. |
| J06 | GENERAL_POLICY | DOC044-U0001-C0001; DOC044-U0001-C0002; DOC044-U0001-C0003; DOC044-U0001-C0004; DOC044-U0001-C0005; DOC044-U0001-C0008; DOC044-U0001-C0009; DOC044-U0001-C0010; DOC044-U0001-C0011; DOC044-U0001-C0012; DOC044-U0001-C0013; DOC045-U0001-C0001; DOC046-U0001-C0004; DOC047-U0001-C0001; DOC051-U0002-C0001 | Impact/policy guidance describes high-quality jobs, apprenticeship/skills benefits, controls, monitoring and the programme objectives. | Policy rationale and accountability contain no realised job totals. |
| J07 | FORECAST | DOC052-U0005-C0002 | Proposals estimated to enable 18,300 long-term UK jobs over the next 25 years, alongside investment/NDR projections. | Explicit estimated future programme effect; not jobs achieved by 31 March 2026. |
| J08 | FORECAST | DOC052-U0012-C0001 | 18,300 UK jobs, 11,300 in the Highlands, explicitly forecast with investment/jobs over a 25-year period. | Geographic split does not change forecast status or establish a realised time-specific count. |
| J09 | FORECAST | DOC052-U0021-C0001 | Potential 25-year tax-site development pipeline could create 18,300 UK jobs, 11,300 in the Highlands; estimates include operational, construction, indirect and induced jobs. | Scenario/pipeline estimates, not observed outcomes; scope also combines several job types. |
| J10 | ANTICIPATED_OUTPUT | DOC052-U0001-C0001; DOC052-U0002-C0001; DOC052-U0003-C0001; DOC052-U0003-C0002; DOC052-U0004-C0001; DOC052-U0005-C0001; DOC052-U0006-C0001; DOC052-U0006-C0002; DOC052-U0007-C0001; DOC052-U0011-C0001; DOC052-U0013-C0001; DOC052-U0019-C0001; DOC052-U0020-C0001; DOC052-U0020-C0002 | Expected employment/community benefits, planned green-economy growth and projected project outputs; approved housing is linked to anticipated employment growth. | Progress on planning, investment interest or an unchanged project-output forecast is not measured job creation. These passages supply no achieved aggregate. |
| J11 | GENERAL_POLICY | DOC052-U0008-C0001; DOC052-U0008-C0002; DOC052-U0009-C0001; DOC052-U0009-C0002; DOC052-U0010-C0001; DOC052-U0015-C0001; DOC052-U0016-C0001; DOC052-U0017-C0001; DOC052-U0018-C0001; DOC052-U0022-C0001; DOC052-U0022-C0002; DOC052-U0023-C0001 | Skills provision, equalities baseline update, company governance and monitoring/evaluation/reporting commitments and future collection of indicators. | Monitoring systems or an updated equalities baseline do not provide achieved creation totals. Named directors/CEO identify governance personnel, not a new-jobs total. |
| J12 | IRRELEVANT | DOC052-U0010-C0001; DOC052-U0010-C0002 | A held careers expo attracted more than 600 young people and more than 30 exhibitors. | An actual delivered event and attendance counts are present, but attendees/exhibitors are not jobs created. |
| J13 | ANTICIPATED_OUTPUT | DOC052-U0023-C0001 | CEO is putting together a team of five full-time staff, with potential for two further roles. | Operational staffing plan, not a verified programme-wide achieved employment count; the passage does not say all five have been hired. |
| J14 | FORECAST | DOC053-U0007-C0001; DOC053-U0009-C0001; DOC053-U0009-C0002; DOC053-U0018-C0001 | Projected Forth creation/support of up to 34,500 jobs; 16,000 direct in U0009; economic-impact assessment and ten-year investment context in U0018. | Explicit expectation/projection, repeated across report and summary, not separate realised observations. |
| J15 | ANTICIPATED_OUTPUT | DOC053-U0033-C0001 | Anticipated outputs include 16,000 direct jobs on tax-site land and around £260m land-value uplift. | Forward-looking outputs; neither actual jobs nor actual LBTT claims. Land-value uplift is a different metric. |
| J16 | FORECAST | DOC053-U0037-C0001; DOC053-U0049-C0001 | Forth will generate 16,000 direct jobs, anticipated up to 34,500 gross jobs and likely 13,600 UK net additional in U0037; conclusion seeks approximately 34,500 gross jobs in U0049. | Economic-case benefits and aspirations, not realised results as of the requested date; cannot substitute gross/net forecast figures for actual creation. |
| J17 | ANTICIPATED_OUTPUT | DOC053-U0035-C0001; DOC053-U0036-C0001 | Seed-project appraisal and categories describe creating jobs directly and accelerating creation. U0035 uses past-tense wording about seed capital being employed, within a potential-impact appraisal assuming Maximum Ask funding. | No numerical realised employment count is stated. Project-benefit categories and this wording do not establish completed job outcomes. |
| J18 | ANTICIPATED_OUTPUT | DOC053-U0008-C0001; DOC053-U0046-C0001 | Three remaining operating-company manager posts anticipated before year end; CEO to recruit three staff by Spring 2025. | Planned operational recruitment is neither proof that recruitment occurred nor an aggregate job-creation result. |
| J19 | IRRELEVANT | DOC053-U0008-C0001 | A named Chief Executive has been recruited and is to take up the post in August 2024. | Actual recruitment is reported, so the audit does not assert that every employment-related statement is prospective. This is one staffing appointment, not a stated total of newly created programme jobs for Forth by the cutoff, and supplies no Inverness total. |
| J20 | GENERAL_POLICY | DOC053-U0005-C0001; DOC053-U0011-C0001; DOC053-U0012-C0001; DOC053-U0020-C0001; DOC053-U0021-C0001; DOC053-U0022-C0001; DOC053-U0023-C0001; DOC053-U0024-C0001; DOC053-U0025-C0001; DOC053-U0026-C0001; DOC053-U0028-C0001; DOC053-U0030-C0001; DOC053-U0032-C0001; DOC053-U0039-C0001; DOC053-U0040-C0001; DOC053-U0043-C0001; DOC053-U0045-C0001; DOC053-U0047-C0001 | Skills access, deprivation, clusters, tax-site development, operational/governance roles and worker representation. | Qualitative intended benefits and personnel/governance structure lack the requested realised totals. |
| J21 | GENERAL_POLICY | DOC053-U0008-C0001; DOC053-U0013-C0001; DOC053-U0028-C0001; DOC053-U0045-C0001; DOC053-U0048-C0001; DOC053-U0049-C0001 | Operating-company reporting, annual committee reports, investment monitoring and future bespoke M&E/indicator reporting. | Reporting arrangements do not contain the results of those returns or an achieved jobs table. |
| J22 | IRRELEVANT | DOC053-U0038-C0001 | Monetised employment-multiplier, labour-supply and productivity benefits, with GVA and net-benefit estimates. | Economic valuation is not an observed headcount. No conversion from pounds to actual jobs is supported. |
| J23 | GENERAL_POLICY | DOC041-U0001-C0022; DOC041-U0001-C0023; DOC055-U0001-C0001; DOC055-U0001-C0002 | National Insurance eligibility for employees and payroll/RTI reporting rules. | Rules and required payroll fields do not supply an employee census or a Freeport job-creation outcome. |
| J24 | IRRELEVANT | DOC055-U0001-C0003; DOC055-U0001-C0004; DOC055-U0001-C0005; DOC051-U0006-C0001; DOC051-U0006-C0002 | Hypothetical employee/payroll examples and guidance updates; goods used to support a workforce. | Illustrative employee scenarios and generic workforce references are not observations of jobs created by these two Green Freeports. |

**Corpus-wide sufficiency conclusion:** Insufficient evidence confirmed. The corpus does not state the realised creation total for Inverness/Cromarty or for Forth by 31 March 2026, nor a dataset from which both totals can be calculated. The 18,300/11,300 and 34,500/16,000/13,600 figures are scenario/projection material. Actual expo attendance and a recorded chief-executive recruitment are acknowledged, but neither is a programme-wide job-creation total. No `ACTUAL_REALISED_VALUE` in the requested job-count sense was identified, even for one Freeport's aggregate; there is therefore no partial aggregate result to substitute for the missing pair.

**Minimal reference-answer candidate:** The frozen UC2 corpus does not provide enough evidence to determine how many jobs had actually been created by each Green Freeport by 31 March 2026. Its job-creation figures are forecasts or anticipated outputs rather than realised totals for that date.

**Task-type integrity:** Valid as insufficient_evidence. Asking for observed outcomes that the frozen evidence cannot establish warrants abstention rather than a forecast-based comparison. Near-miss document IDs are audit references only; they are not required answer documents or gold reference evidence.

**Ambiguity assessment:** The date and the two actors are explicit. “Actually” excludes projections. The wording does not specify gross/net, direct/indirect, headcount/FTE or attribution methodology. These distinctions would matter for a numerical answer and remain for human consideration; no scientific metric is selected here. They do not alter this absence finding because the corpus lacks achieved aggregate counts under any of these plausible readings. Counts of employees already present, planned staffing or a hired executive cannot establish jobs newly created across each programme. No wording reveals a number or expressly tells the respondent that the answer is absent. No temporal extrapolation is authorized.

**Answerability:** The requested numerical pair is not answerable strictly from the frozen corpus; the evidence-supported answer is an insufficiency statement. This conclusion makes no assertion about real-world success, failure or zero employment.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified for use as an insufficient-evidence candidate; employment metric distinctions are recorded for human review without rewriting the question.

## T020 — insufficient_evidence

**Exact candidate question**

> By 31 March 2026, what total amount of Land and Buildings Transaction Tax (LBTT) relief had actually been claimed for transactions in each of Scotland's two Green Freeports?

The requested values are aggregate actual LBTT relief claim amounts, separately for each Freeport, by the cutoff. Transaction consideration, relief eligibility percentages, hypothetical calculations, claim-availability dates, other tax reliefs and policy projections do not answer this question.

### Material near-miss and exclusion findings

| Finding | Classification | Exact canonical chunks | Frozen content | Why it does not answer the exact candidate |
|---|---|---|---|---|
| L01 | CLAIM_START_DATE | DOC047-U0001-C0001 | Claims may be made from 8 April 2024 for Inverness/Cromarty and 12 June 2024 for Forth, following tax-site designation. | Potential availability dates do not report actual claims, sums or period totals. |
| L02 | ELIGIBILITY_RULE | DOC047-U0001-C0001; DOC047-U0001-C0002; DOC047-U0001-C0003; DOC047-U0001-C0004; DOC047-U0001-C0005; DOC047-U0001-C0006 | Qualifying-land/transaction rules, at least 90% full relief and at least 10% partial threshold, just-and-reasonable attribution and stated eligibility windows. | Rates and eligibility conditions are not realised uptake or total relief amounts. No transaction population is supplied. |
| L03 | WORKED_EXAMPLE | DOC047-U0001-C0004 | Three illustrative £3m land acquisitions explain full relief, including 90% land and 95% consideration cases. | Hypothetical purchase consideration is not an actual tax-relief aggregate; no named-Freeport totals or requested cutoff. |
| L04 | WORKED_EXAMPLE | DOC047-U0001-C0005 | Illustrative £1,480,000 purchase yields £62,500 pre-relief tax, 62.5% relief and £39,062.50 relief. | Explicit example, not observed claims. The £1,480,000 and £925,000 are consideration values, not claimed relief. |
| L05 | WORKED_EXAMPLE | DOC047-U0001-C0005; DOC047-U0001-C0006 | Illustrative £1,375,000 purchase, 10.04% qualifying proportion and £57,250 tax gives £5,747.90 relief; further examples below 10% show no relief. | Illustrative calculations, not aggregate claims by either Freeport. Do not sum them or infer actual zero claims from a no-relief example. |
| L06 | POLICY_DESCRIPTION | DOC047-U0001-C0006; DOC047-U0001-C0007 | Claims through original returns or timely amendments; guidance on further returns when qualifying use ends. | Procedure and filing obligation, not evidence of the number/value of submitted returns. |
| L07 | ELIGIBILITY_RULE | DOC047-U0001-C0007; DOC047-U0001-C0008; DOC047-U0001-C0009; DOC047-U0001-C0010; DOC047-U0001-C0011 | Withdrawal/control-period, alternative-finance, lease, review/assignation and notifiability conditions. | Rules do not identify aggregate amounts claimed or net amounts after withdrawal. |
| L08 | WORKED_EXAMPLE | DOC047-U0001-C0007; DOC047-U0001-C0008 | £800,000 warehouse destroyed by fire and £3m change-of-use examples; a hypothetical case says full relief was claimed. | Past tense occurs inside examples, not an administrative claim statistic; purchase values are not aggregate relief amounts. |
| L09 | WORKED_EXAMPLE | DOC047-U0001-C0009 | Alternative finance example: a bank buys £1,950,000 land and a relevant person claims relief then ceases qualifying use. | Illustrative arrangement and withdrawal, not a realised Green-Freeport claims return or a £1,950,000 relief amount. |
| L10 | WORKED_EXAMPLE | DOC047-U0001-C0010; DOC047-U0001-C0011 | Lease assignation example: two warehouses, £150,000 annual rent and 60% qualifying use. | Hypothetical rent/qualifying share and return obligations, not observed aggregate relief. |
| L11 | POLICY_DESCRIPTION | DOC048-U0001-C0001; DOC048-U0002-C0001; DOC048-U0007-C0001 | 2023 legislation creates relief/return/interest provisions; explanatory note describes its purpose. | Law establishes relief rather than reporting realised claims. |
| L12 | ELIGIBILITY_RULE | DOC048-U0003-C0001; DOC048-U0004-C0001; DOC048-U0004-C0002; DOC048-U0005-C0001; DOC048-U0005-C0002; DOC048-U0006-C0001 | Statutory full/partial thresholds, qualifying use, withdrawal and alternative-finance rules. | Transaction-level legal rules and amount-chargeable formulas are not population-level claim values. |
| L13 | POLICY_DESCRIPTION | DOC041-U0001-C0020; DOC041-U0001-C0021; DOC044-U0001-C0002; DOC044-U0001-C0003; DOC053-U0006-C0001 | Prospectus/impact assessment/report describe LBTT as part of the tax-incentive package. | Policy offer/description, not a total claimed by Freeport. |
| L14 | POLICY_DESCRIPTION | DOC041-U0001-C0018; DOC041-U0001-C0019; DOC041-U0001-C0036; DOC041-U0001-C0039; DOC041-U0001-C0040; DOC043-U0001-C0006; DOC043-U0001-C0007; DOC043-U0001-C0008; DOC043-U0001-C0025; DOC043-U0001-C0026; DOC043-U0001-C0027; DOC044-U0001-C0007; DOC044-U0001-C0008; DOC044-U0001-C0009 | Revenue Scotland oversight, record access, relief declarations, tax-site compliance and required collection/evaluation of realised relief outcomes. | Authority/data-collection references are plausible leads but contain no populated aggregate LBTT return. Linked external statistics cannot be imported. |
| L15 | POLICY_DESCRIPTION | DOC049-U0001-C0001; DOC049-U0002-C0001; DOC049-U0002-C0002; DOC049-U0003-C0001; DOC050-U0001-C0001; DOC050-U0002-C0001; DOC050-U0003-C0001 | Designations, maps, commencement dates and explanatory notes on special-tax-site allowances. | Legal/geographic availability is not evidence of an amount claimed. These are not Freeport LBTT statistics. |
| L16 | IRRELEVANT | DOC046-U0001-C0001; DOC046-U0001-C0002; DOC046-U0001-C0003; DOC046-U0001-C0004; DOC046-U0001-C0005; DOC046-U0001-C0006; DOC046-U0001-C0007; DOC046-U0001-C0008 | GF relief amounts, NDRI/audited returns, GRG reimbursement, percentage/amount reporting and recipients lists; page updated 25 March 2026. | This is non-domestic-rates relief and retention guidance, not LBTT. It prescribes reporting without supplying the requested LBTT totals. |
| L17 | IRRELEVANT | DOC052-U0005-C0001; DOC052-U0005-C0002; DOC052-U0008-C0001; DOC052-U0008-C0002; DOC052-U0013-C0001; DOC052-U0013-C0002; DOC052-U0014-C0001; DOC052-U0020-C0001; DOC052-U0020-C0002; DOC052-U0022-C0001; DOC053-U0007-C0001; DOC053-U0008-C0001; DOC053-U0009-C0001; DOC053-U0010-C0001; DOC053-U0011-C0001; DOC053-U0012-C0001; DOC053-U0027-C0001; DOC053-U0031-C0001; DOC053-U0037-C0001; DOC053-U0038-C0001; DOC053-U0040-C0001 | Seed-capital/match-funding budgets and project expenditure, skills-fund projections, retained-NDR projections (including an annual income table), land-value/GVA benefits, and tax benefits typically over 7% of private capital investment. | These monetary amounts/proportions describe other measures, budgets or modelled benefits; none is aggregate actual LBTT claimed. Forecast NDR income zeros are not zero LBTT claims. |
| L18 | IRRELEVANT | DOC055-U0001-C0001; DOC055-U0001-C0002; DOC055-U0001-C0003; DOC055-U0001-C0004; DOC055-U0001-C0005; DOC056-U0001-C0001; DOC056-U0001-C0002; DOC056-U0001-C0003; DOC057-U0001-C0001; DOC057-U0001-C0002; DOC057-U0001-C0003; DOC057-U0001-C0004 | NI/SBA/ECA rules and examples, including £120,000/£144,000 total SBA claims, £300,000 ECA and a £133,333 ECA example. | Different tax reliefs and illustrative taxpayer calculations; the word total or claimed cannot turn them into aggregate actual LBTT. |
| L19 | IRRELEVANT | DOC051-U0001-C0001; DOC051-U0003-C0001; DOC051-U0003-C0002; DOC051-U0003-C0003; DOC051-U0003-C0004; DOC051-U0003-C0005; DOC051-U0003-C0006; DOC051-U0003-C0007; DOC051-U0004-C0001; DOC051-U0004-C0002; DOC051-U0005-C0001; DOC051-U0005-C0002; DOC051-U0005-C0003; DOC051-U0006-C0001; DOC051-U0006-C0002; DOC051-U0006-C0003; DOC051-U0006-C0004; DOC051-U0006-C0005; DOC051-U0006-C0006; DOC051-U0006-C0007; DOC051-U0006-C0008; DOC051-U0007-C0001; DOC051-U0008-C0001; DOC051-U0009-C0001; DOC058-U0001-C0001; DOC058-U0001-C0002; DOC058-U0001-C0003 | Customs/excise/VAT procedure and goods records; seed-subsidy cumulative amounts/£100,000 transparency and £25m scheme thresholds. | Other taxes, goods and subsidies, not LBTT. DOC051 expressly excludes direct tax-site incentives. |
| L20 | IRRELEVANT | DOC048-U0008-C0001; DOC049-U0004-C0001; DOC050-U0004-C0001 | Instrument publication prices £8.14 and £5.78. | Printed-document prices, not tax relief. |
| L21 | POLICY_DESCRIPTION | DOC052-U0015-C0001; DOC052-U0016-C0001; DOC052-U0017-C0001; DOC052-U0018-C0001; DOC053-U0008-C0001; DOC053-U0013-C0001; DOC053-U0028-C0001; DOC053-U0045-C0001; DOC053-U0047-C0001; DOC053-U0048-C0001; DOC053-U0049-C0001 | Accountable-body financial assurance, investment monitoring and future reporting/evaluation arrangements in the two business-case reports. | No actual aggregate LBTT claims table appears in the reporting sections. Expenditure assurance is not claimed transaction-tax relief. |

**Corpus-wide sufficiency conclusion:** Insufficient evidence confirmed. No canonical chunk reports aggregate actual LBTT relief claimed for either Green Freeport through 31 March 2026. Neither reporting guidance nor the two business-case reports supplies an actual claim dataset enabling calculation. The explicit relief amounts in DOC047 are examples; records of NDR awards, forecasts of retained revenue and SBA/ECA/NI claim examples concern other measures. Dates from which LBTT claims can be made do not imply any amount was claimed. No `AGGREGATE_ACTUAL_CLAIM_VALUE` was identified for either Freeport; neither a complete pair nor a partial Freeport aggregate is available.

**Minimal reference-answer candidate:** The frozen UC2 corpus does not provide enough evidence to determine the total LBTT relief actually claimed in each Green Freeport by 31 March 2026. It supplies eligibility and claiming guidance and illustrative calculations, rather than aggregate realised claim amounts.

**Task-type integrity:** Valid as insufficient_evidence. The evidence cannot establish the requested historical claim values, even though it explains relief operation and potential start dates. Audit citations to guidance are not reference evidence for an aggregate claim answer.

**Ambiguity assessment:** The tax and cutoff are explicit; “each” requires separate attribution to Inverness/Cromarty and Forth, as identified in DOC047. “Total amount” refers to relief, not purchase consideration, tax payable, rent, investment or NDR. Submitted claims versus accepted claims, gross claims versus amounts remaining after withdrawal, and aggregation start date are not fully specified. These would matter for a numerical statistic and are preserved for human consideration; no netting rule or start date is invented. Because no actual LBTT aggregate or claim records are supplied, none of these plausible interpretations produces a supported value. The question gives neither thresholds nor example amounts, and does not disclose that a statistic is absent.

**Answerability:** The requested monetary pair is not answerable strictly from the frozen corpus; an insufficiency statement is supported. No zero amounts, expenditure-derived approximations or policy-update reconciliation are inferred.

**Verdict:** READY_FOR_HUMAN_REVIEW

**Exact defect:** None identified for use as an insufficient-evidence candidate; claim-accounting distinctions are recorded without revising the question.

## Classification counts

Counts below use the **grouped finding entry** as the unit, separately by task. They count material near misses and explicitly documented exclusions, including IRRELEVANT entries, and do not claim statistical independence of overlapping evidence. The separate ledger contains dispositions for all 293 chunks, so entry counts must not be confused with corpus or hit counts. `ACTUAL_REALISED_VALUE` denotes observed achieved job-count evidence, not any actual event; `AGGREGATE_ACTUAL_CLAIM_VALUE` denotes actual aggregated LBTT claims, not any monetary figure.

| Task | Classification | Grouped finding count |
|---|---|---:|
| T019 | FORECAST | 5 |
| T019 | TARGET | 1 |
| T019 | ANTICIPATED_OUTPUT | 5 |
| T019 | GENERAL_POLICY | 9 |
| T019 | ACTUAL_REALISED_VALUE | 0 |
| T019 | IRRELEVANT | 4 |
| T020 | ELIGIBILITY_RULE | 3 |
| T020 | WORKED_EXAMPLE | 6 |
| T020 | CLAIM_START_DATE | 1 |
| T020 | POLICY_DESCRIPTION | 6 |
| T020 | AGGREGATE_ACTUAL_CLAIM_VALUE | 0 |
| T020 | IRRELEVANT | 5 |

T019 grouped findings: 24. T020 grouped findings: 21. Zero observed-value findings result from semantic inspection of positive near misses and corpus coverage, not a keyword-zero argument.

## Mandatory aggregate fields and provenance

```text
CORPUS_DOCUMENTS_SCANNED=17
CORPUS_CHUNKS_SCANNED=293
RANKED_RETRIEVAL_USED=NO
EMBEDDINGS_USED=NO
MODEL_BENCHMARK_OUTPUT_USED=NO
B0_B1_G1_OUTPUT_USED=NO
BENCHMARK_RESULT_USED=NO
TASK_JSON_CREATED=NO
TASKS_HUMAN_VERIFIED=NO
TASKS_FROZEN=NO
BENCHMARK_STARTED=NO
LLM_ASSISTED_CANDIDATE_AUTHORING=YES
HUMAN_DIRECTED_CANDIDATES=YES
CORPUS_WIDE_ABSENCE_AUDIT=YES
RESULT_DRIVEN_REVISION=NO
T019_VERDICT=READY_FOR_HUMAN_REVIEW
T020_VERDICT=READY_FOR_HUMAN_REVIEW
```

No ranked/vector retrieval, embedding model, retrieval diagnostic, task-execution model inference, B0/B1/G1 or benchmark execution was run. No benchmark/model results were inspected or used. LLM assistance is limited to the authoring/evidence audit itself. No benchmark task JSON was created. The later task-structure convention is `required_documents=[]` and `reference_evidence=[]` for confirmed insufficient-evidence tasks; these arrays are described here only and no task file is instantiated. Human verification and freeze remain outstanding. Nothing was staged, committed or pushed; the existing evidence audit is preserved.

## Input fingerprints

| Input | SHA256 |
|---|---|
| `corpus/use_cases/UC2/processed/UC2-SOURCEUNIT-W450-O75-v0.1/chunks.jsonl` | `b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2` |
| `corpus/use_cases/UC2/corpus_membership.json` | `e9b000a20d470b7cac52f232027f2a8ba9128ad41a92bb8b945b479997a37cc4` |
| `benchmark/task_authoring_protocol_v0.1.json` | `c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169` |

## Complete canonical chunk coverage and disposition ledger

Rows are in physical JSONL order, with one row per record and no omissions. Family codes: **J** = T019_CORE; **O** = T019_OUTCOMES; **T** = T020_TAX; **V** = T020_VALUES; **—** = no family hit. Each disposition is an analyst-assessed classification or set of classifications from distinct passages in that chunk. IRRELEVANT includes broad term-family false positives and nonhits screened structurally/numerically. A relevant classification does not imply answer sufficiency. Finding IDs tie all material grouped findings to exact records; remaining policy hits are generic bid/delivery/site/skills provisions or reporting context rather than an achieved-value return. Overlap duplicate occurrences are retained as separate canonical records, not added into totals.

Text hashes are recomputed SHA256 of each record's UTF-8 text. Line numbers permit exact record lookup, and chunk IDs embed document/source-unit identity. This ledger is evidence of enumeration and screening; absence conclusions also require the substantive classifications above.

| Line | Chunk | Families | T019 disposition | T020 disposition | Findings (T019 / T020) | Text SHA256 |
|---:|---|---|---|---|---|---|
| 1 | DOC041-U0001-C0001 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `3f5c8720db3c10c9f2afb467fd01d72f5831ac0f08959fca2b6cdf82452c71bf` |
| 2 | DOC041-U0001-C0002 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `b6a49f0e24ae65a99a2186928d52bed0498c046796721976f131f635e84e4425` |
| 3 | DOC041-U0001-C0003 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `68e60a3ff69d73c7161fda88cb9d5a7dfc80e17f57e5e99ad1a55bcaa77c9879` |
| 4 | DOC041-U0001-C0004 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `d360d640db024a44f06ced49e412649b64e234505ce6d8ccaf2ad09caa103f0d` |
| 5 | DOC041-U0001-C0005 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `44f5694c5ebe776739e2b34a378a577d7f63f1ef8c4a06f5bcc604b90015e406` |
| 6 | DOC041-U0001-C0006 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `02833acfcbc80acadac9723aa1ecc9396e9ea0c223b7ea78e09fd7a803a1219d` |
| 7 | DOC041-U0001-C0007 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `1ae73a9b022bff0a3b01a9fb47447167cd069359f8831c3623b20513b8454164` |
| 8 | DOC041-U0001-C0008 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `fb952cdf073967821a89838992fc7ace8324020a084cbbf6a51179b3f6cc5f12` |
| 9 | DOC041-U0001-C0009 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `a77a8b36320f550a86a1a6b135816ec72a7b9d068c9426dd2f80f7974103d6ad` |
| 10 | DOC041-U0001-C0010 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `b1d90d85fb5a11bbabafe2d45736c3cd53dee4e1f15a83485f4ec9fb6c05e659` |
| 11 | DOC041-U0001-C0011 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J01 / — | `12e14fcfde6382306f94d3c5166340a29733c20213f34ae1a81132b42ab637df` |
| 12 | DOC041-U0001-C0012 | J,O | GENERAL_POLICY | IRRELEVANT | J01 / — | `2f6c2fa877107fd4845f67d7c3887188bc2812682b972649dcf0f3d2f24e401c` |
| 13 | DOC041-U0001-C0013 | J,O,T,V | TARGET | POLICY_DESCRIPTION | J02 / — | `38b286381f8e18b43a168f57fca009d2794062a0c98a10a73940fccbd5815ca8` |
| 14 | DOC041-U0001-C0014 | J,O,T,V | TARGET | POLICY_DESCRIPTION | J02 / — | `7c7bc5b8874faaef968ba355fe046dabc60b355a469fc2bdade539be3dccbb6b` |
| 15 | DOC041-U0001-C0015 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `f21ba94a0b2bffd63b3b4c3e5669a6db54e8cb9ba242d02f384819abfacaceb7` |
| 16 | DOC041-U0001-C0016 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `3998ded8c73bafb154e2fb1fc3a970644371e5dc819460ceb5cea335f0d6b7a2` |
| 17 | DOC041-U0001-C0017 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `daa857ea80de7efff78ed9b468e7c884deaa2de145dd116d60229f54eca15f23` |
| 18 | DOC041-U0001-C0018 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / L14 | `1954549a1e832da15f076b98bdf429f30a34895f7c0c573e6f8a4378a9df57ae` |
| 19 | DOC041-U0001-C0019 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / L14 | `db1c3a13df3fb1542c20704b7f1602c51ee44b0a9d771f213b8169c1bd0c4bbd` |
| 20 | DOC041-U0001-C0020 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / L13 | `24cc50016b169c8c780ee8f993212ecfe52ec152077ad3f7cd6d1cb88ec05ced` |
| 21 | DOC041-U0001-C0021 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / L13 | `1373abcdbbbe0a6986ff84893b1d73d7ba8cf60c6bf04902b35a4c4918d57379` |
| 22 | DOC041-U0001-C0022 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J23 / — | `88cacec70d1fed46668f9f1c86f58b848c3fd0130068d97e40ce919c919cb216` |
| 23 | DOC041-U0001-C0023 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J23 / — | `551127241153cbcbd945584295fe95311e2147cfe090fecfd4194b072ba6931c` |
| 24 | DOC041-U0001-C0024 | — | IRRELEVANT | IRRELEVANT | — / — | `728e1a7b6dd880df524e87da2afa6f66a8d34abd2b0324b1035874650d0b8b9f` |
| 25 | DOC041-U0001-C0025 | — | IRRELEVANT | IRRELEVANT | — / — | `639aa6d9d2435f569cbb6db985e595a6ee588f5b40dea4a37e8063d5ef3e8b01` |
| 26 | DOC041-U0001-C0026 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `0c4ee69dbdfa930622957cac409a1d00ad6fc036f9cde304dc21f7bbd0831a7f` |
| 27 | DOC041-U0001-C0027 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `1e027a64a722d4477d20e94a3146398a0ec30eb198c220c5ecf4b850f39a4bee` |
| 28 | DOC041-U0001-C0028 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `8c3fd9a5fbb2771f3fd73193c1076261c76db700c99050dadf58634b649c65d5` |
| 29 | DOC041-U0001-C0029 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `a63c344c0ff01f7469e690236f60f63c3abbe75ad3e68c1e7ea6426bbbd98fa6` |
| 30 | DOC041-U0001-C0030 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `ab91a26eabf1478ff3df683adfe2a63af26e604e3d463524b9a1c1a21e25a58d` |
| 31 | DOC041-U0001-C0031 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `beb8eb891de68e21c21999e9dd689cf272c80e98394707f91627a710e57d0ba4` |
| 32 | DOC041-U0001-C0032 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `1082272535ff3943499bd7a02a81c7fa386ffac79ac398efab839cd608b0dc56` |
| 33 | DOC041-U0001-C0033 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `e15f8a82e30c43186fd1e2e090cb03887b0f5209bb04d004e281db40ad5dd4bd` |
| 34 | DOC041-U0001-C0034 | O | GENERAL_POLICY | IRRELEVANT | — / — | `8b842e70cbc659586e7d149b654498dfc3ad648593987251d9eb4fb1604cb0f4` |
| 35 | DOC041-U0001-C0035 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `7ef5b3df5a0c79cb086002b702ee8963fa24cce29454314e3c5c5961f2a8bcfa` |
| 36 | DOC041-U0001-C0036 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / L14 | `1f69fccbf8643f992ba31643b5a644640ccc230bfa6c6d7e19148601093deac1` |
| 37 | DOC041-U0001-C0037 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `1d5315d786f43da615018598f6f0bb981229b87a75639509c25a11bd651461cc` |
| 38 | DOC041-U0001-C0038 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `aa67458288802ccac7ad36caf989547ead73c31830c2457632493655f98951cf` |
| 39 | DOC041-U0001-C0039 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / L14 | `87dc128e4fb8dcd6eeda225b66b5532e2a5d4eb80e1d5277a61d8c8127b77bbf` |
| 40 | DOC041-U0001-C0040 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / L14 | `eb2ccabd571c9ef49f09b3bf9b1cea8a7472eb61469e3c058853b8ab319929cf` |
| 41 | DOC041-U0001-C0041 | T,V | IRRELEVANT | POLICY_DESCRIPTION | — / — | `25fccf700ad5937880c9815be807419dd714aa0e7ee12dc3c2d8efe2c0faf7d0` |
| 42 | DOC041-U0001-C0042 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `65c3ba194431ff04971e08fb6013fa27dc8f8af279e9c72a3ae229693c9a2c32` |
| 43 | DOC041-U0001-C0043 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `1965e72ba4acf25c2c679309d207277bc465de051eb6ee4ef9b4307564c303d7` |
| 44 | DOC041-U0001-C0044 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `7cb0ad030edf1c1f96c8f5151d762a55202696bb721414aa098dd96ae698d679` |
| 45 | DOC041-U0001-C0045 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `7b827b6a664586af4607bd08d065814b6f93c58481d86850b29916124fc67e64` |
| 46 | DOC041-U0001-C0046 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `49b45e53969eb9d339c16a16532f4d96b2b698db5983e34c6765b2c9cfabfa08` |
| 47 | DOC041-U0001-C0047 | J,O | GENERAL_POLICY | IRRELEVANT | J04 / — | `8a223a780932489493b2a5cd1233a99e97348761964bb0cd5d5a7b237419db54` |
| 48 | DOC041-U0001-C0048 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `7d2c25c93e84a456528fcebf56eccf52e58db4835741399227472628f77328b5` |
| 49 | DOC041-U0001-C0049 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J04 / — | `58c0bc141743dd626899e572610ccb55b13189bf7f2373155c1a2befa87275d3` |
| 50 | DOC041-U0001-C0050 | O,V | IRRELEVANT | IRRELEVANT | — / — | `c6edf4da1156ae998d10ea7a69ebedb4ceb480730c9cfc8eded7d8ae77fab900` |
| 51 | DOC041-U0001-C0051 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `946d451d66e7a4c0ff7d20189e860b8c99fd38d431f81c70da1538f0b7159984` |
| 52 | DOC041-U0001-C0052 | O,V | IRRELEVANT | IRRELEVANT | — / — | `2d2d57ec50eda6a06d2001539ea7e1ced21241a1fc53b82be3c5a99a7c8b1a05` |
| 53 | DOC041-U0001-C0053 | J,O,V | IRRELEVANT | IRRELEVANT | — / — | `adde8b710800a3391e5c1d3995552d2c22b058667d5b6e53a636d5b5b9ac4ac1` |
| 54 | DOC042-U0001-C0001 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `eb309589435a41f9dfc7bf5f33268b04aa3b4c5840d44bd80246e584ef9d191e` |
| 55 | DOC042-U0001-C0002 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `002b68d953bb52ea91f8adf50bc528775d1faf3845439cefccc6b3863eb45fb2` |
| 56 | DOC042-U0001-C0003 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `e75463e392472dc3c9e83bbe76b9c1306cc89bcec61446de6e0aad63d51dd7fc` |
| 57 | DOC042-U0001-C0004 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / — | `6cba179f92a35b1aefcc9a7e144b20c11e160e3f70cd0c5e2e9c331686d2fcc5` |
| 58 | DOC042-U0001-C0005 | J,O | GENERAL_POLICY | IRRELEVANT | J03,J04 / — | `01bb60dc1804df40a06c7a6bdc87ae23b36f3206268b11ef3f836ff9b96c4026` |
| 59 | DOC042-U0001-C0006 | O | GENERAL_POLICY | IRRELEVANT | J04 / — | `1f86b386560cf03b9c3d1712057b54322a2000f678f01e99027b13d7bf55447b` |
| 60 | DOC042-U0001-C0007 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `357139d7b6ead79b58f43fcdb0fe2c8034480c34beecd47d95dc5162c00c0fac` |
| 61 | DOC042-U0001-C0008 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `38e0ad30ddeaf2df99b4cd75f8c9b53e1300da1b7d44f58965b4a091cc0d5688` |
| 62 | DOC042-U0001-C0009 | O,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `89bc16653d35a6801b480255d70e95c61f4dcb744c4a791b55ace4e7cda070c0` |
| 63 | DOC042-U0001-C0010 | V | IRRELEVANT | POLICY_DESCRIPTION | — / — | `6e1cfa2889a012109e6f9faff8cd232c322e0542044315af6f30b1bb579c68b9` |
| 64 | DOC043-U0001-C0001 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `1c5efcdd90a3d9e2dba80ce3b0e2471b80b07617d0748547c7721edf15e8751d` |
| 65 | DOC043-U0001-C0002 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `23428b5df0659c5bde465e8ab0d669b0acd997f60bf0fa1c35a86dc5e48edbac` |
| 66 | DOC043-U0001-C0003 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `51ef2dbc2862f696ae887dbcbb3da3d25519331ea489454eeb15909d24e35799` |
| 67 | DOC043-U0001-C0004 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `95663526d60c0445717fa1cfef26de5225ff2da92cac571c97bb172b9e91b7b6` |
| 68 | DOC043-U0001-C0005 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `be31504d4f7db8ffd18dfb5d0f68b2bb84df632d807614ca647e53824ca06530` |
| 69 | DOC043-U0001-C0006 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / L14 | `91d539e3fe0ae3f1e37a7c4a962b9319df66148faddde2dc935959e5ec78e97c` |
| 70 | DOC043-U0001-C0007 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / L14 | `3745ed074d4e64908da6c4c04ae8720d592d8554597576eff4a932659f57b10e` |
| 71 | DOC043-U0001-C0008 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / L14 | `87220e6e72cd4f10caa726dd8ead45396ae19ed766431558f9a8fc070b076897` |
| 72 | DOC043-U0001-C0009 | J,O,T | GENERAL_POLICY | IRRELEVANT | J05 / — | `804fa98a7dcf9806e5590166d1b81762e91c77a781e8e4ae90ad169d31438e04` |
| 73 | DOC043-U0001-C0010 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `9be4229d0548cf76f93fdfe82fde98809ff1a33e8d8b386442246b6f4b3be701` |
| 74 | DOC043-U0001-C0011 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `5312f87de18378aadeda3a957f59ceeb797affbe9f0059196595ae4014ff82e7` |
| 75 | DOC043-U0001-C0012 | O,T | IRRELEVANT | IRRELEVANT | — / — | `261ff2d22f9a2eee54dde9114653f91ad5ae9986c1393e06577893ddb8260748` |
| 76 | DOC043-U0001-C0013 | O,V | IRRELEVANT | IRRELEVANT | — / — | `c9c772bfd379478580aa911b533b1ff4a8f5cce8337fba4fe326de1d2852e9f3` |
| 77 | DOC043-U0001-C0014 | J,O,T | GENERAL_POLICY | IRRELEVANT | J05 / — | `65be0dfff90d5afb74c9f8855989c72d821acfcbf156c9d2781ef97cc4e03a66` |
| 78 | DOC043-U0001-C0015 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J05 / — | `b16a0bb46c1dc2da2a932b2a77f60996f7fe064508372f037d139f63bb391731` |
| 79 | DOC043-U0001-C0016 | O,V | IRRELEVANT | IRRELEVANT | — / — | `2a99a3de4d065fcb36e6ca388347f776a364bba02e269c4e8e461d6cf6bea2ee` |
| 80 | DOC043-U0001-C0017 | J,O,V | GENERAL_POLICY | IRRELEVANT | J05 / — | `e8cffb5b6a196805f2b3e58c1e8419dcf8e9d7d9a2743c1bcf1d69b8a40ea94d` |
| 81 | DOC043-U0001-C0018 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J05 / — | `45a1d79efe3c2e3fed08eac4fe39feb1d84b137bcf3eaae6229ffb5d5f34a205` |
| 82 | DOC043-U0001-C0019 | J,O,V | GENERAL_POLICY | IRRELEVANT | J05 / — | `4e777e034d521a8acfc3c962c883633217fddcd44711decf8c6a90c0bcfd9c29` |
| 83 | DOC043-U0001-C0020 | O,T | GENERAL_POLICY | IRRELEVANT | J05 / — | `c3fb8e767836bea14af72c1109c4c53a0acbe209bedaa9fd9776984e784a1058` |
| 84 | DOC043-U0001-C0021 | J,O | GENERAL_POLICY | IRRELEVANT | J05 / — | `ff51d4cb4fd646592cfbc5fb2740f979c88d4987232dc3e8b39569c45a14c699` |
| 85 | DOC043-U0001-C0022 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `fd20d4e9b080baa6d1bf0d53422dc578e18f418d4773c4fbd597cc6d5805b84f` |
| 86 | DOC043-U0001-C0023 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `f75c207b4572d3cbf4f48573b13c38d81835727239050cb9c8a963aed36cd6e3` |
| 87 | DOC043-U0001-C0024 | J,O,T | GENERAL_POLICY | IRRELEVANT | J05 / — | `eb84631daab6d936547d2a43e62122e93874d265685b67e75c1c89c0661b4a8d` |
| 88 | DOC043-U0001-C0025 | O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / L14 | `6024dca20ca2fcbe9c4484b937b892d3b7c18fa40a68b30dc59fc057f2c31d45` |
| 89 | DOC043-U0001-C0026 | O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / L14 | `2955f4f0344b3688b4538d74e84442cbb87ee13ca8c27afcc782432f51eaad78` |
| 90 | DOC043-U0001-C0027 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / L14 | `22ff956af39e93fba6d1b199e15ab0cfd526caa09d6e7ff38157050ca514bbb1` |
| 91 | DOC043-U0001-C0028 | T | IRRELEVANT | IRRELEVANT | — / — | `5a99c873f8147ae47b047a99a18cb8f02487fd04210a9b46adedca8f248f3630` |
| 92 | DOC043-U0001-C0029 | O,V | IRRELEVANT | IRRELEVANT | — / — | `24dd7d4a079c8ac49f01793428bdce1cea1bbaa4386a40f0206e20adfc303818` |
| 93 | DOC043-U0001-C0030 | O | IRRELEVANT | IRRELEVANT | — / — | `dc6ada96db87ac7ef2a390a4804d692a52a24fc9d95ea2d2c77497ad97081057` |
| 94 | DOC043-U0001-C0031 | O | IRRELEVANT | IRRELEVANT | — / — | `8af77206d20a95906a16a8434dc4cbcc8cf5b919a734f477540ad576a84fdd56` |
| 95 | DOC043-U0001-C0032 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `2ac8bd96b032ad8c8bf2a3dbda8368eaf19cc3cdb1f93761a2cca27cac1279be` |
| 96 | DOC043-U0001-C0033 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `eb951c04163956938f875e18e8f89c7cde20ec24d88b430634c0b3b14b33a912` |
| 97 | DOC043-U0001-C0034 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `bf528b52172f9e8a29f9ec3bdea3793d522902c117e5c7832862a3ea700c88da` |
| 98 | DOC043-U0001-C0035 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J05 / — | `ec0fcf6bcfb568b72ef830835e3d5258a21c0d6d4b8b3fb9f721e12e94bd493b` |
| 99 | DOC043-U0001-C0036 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / — | `ede4b32014c82c72ac81921735bbea492d7a6aab818cc0c82226eef75f5b3db3` |
| 100 | DOC043-U0001-C0037 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / — | `f5bbd47b4232c937f84482ce86fdfa49bd70047344d0905948d2cf39b5ee91ad` |
| 101 | DOC043-U0001-C0038 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J03 / — | `8990b710b39f62559a224818b85431148c192bcd7d11b7ce5e7f774f5a10563a` |
| 102 | DOC043-U0001-C0039 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `03712be6f7af9593f670da53fb773981114010b21188166ee7a088654a9c2067` |
| 103 | DOC043-U0001-C0040 | O,T | IRRELEVANT | IRRELEVANT | — / — | `1f7fc2e974bd338f237479d73ebb7b0d2b06804b6d85c71be553059d09eb4c1a` |
| 104 | DOC044-U0001-C0001 | J,O | GENERAL_POLICY | IRRELEVANT | J06 / — | `00cfc1a41d0ad954fd4ebee8f0303f6b12e5b259c8f912f8954cb576a5153f36` |
| 105 | DOC044-U0001-C0002 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / L13 | `b7051302f54eca6a32c08615be68d440bfc65f1deb33d5442c8b3752a3387fc4` |
| 106 | DOC044-U0001-C0003 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / L13 | `d83412514db21596da5018474c733050e09efd0643f1b586fb54afb72678c164` |
| 107 | DOC044-U0001-C0004 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `5651b436c8b3cbc15e0c6e09b5c68d2f5f4548d1da8840a12d7f7705d67430bf` |
| 108 | DOC044-U0001-C0005 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `bfce320b5749bc568527717f39bb267a317a08bee9f6c994f31997ec6614ecd7` |
| 109 | DOC044-U0001-C0006 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | — / — | `85ccb247492b11057a2223b3a862f50d32114c78e5c75120753cc31bea9b79f7` |
| 110 | DOC044-U0001-C0007 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / L14 | `a67112d475d545fffbd78a94071573a51503dbd233e3178343f0d3c3c16e0e09` |
| 111 | DOC044-U0001-C0008 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / L14 | `9857dfe12a4053cfd4123ac28768cc5526580eac0e47958333f636ca052b975f` |
| 112 | DOC044-U0001-C0009 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / L14 | `00b46a61e2fdbb77cb344207b0b8f3ca23687358968b4099b997eb9aa3d0d8ae` |
| 113 | DOC044-U0001-C0010 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `514ecfcc5a37ae5780dcdd5fb543787991f08e8b67c3765e88d72e2596a09b89` |
| 114 | DOC044-U0001-C0011 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `92a67e39eea813d58baf4fe8f7b5621e90919a53eb4c551e2338070e4ad48074` |
| 115 | DOC044-U0001-C0012 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `fa75fbfd45b398a6aee590cbb27ba33ca5120e59a8e6c0db95f7e5f9a5da9268` |
| 116 | DOC044-U0001-C0013 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J06 / — | `55d2018521af3b5e90ba4b3e868736b1e7017b1ebfb02a01802d5fd4fcc9fcbf` |
| 117 | DOC045-U0001-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J06 / — | `2fff5c14cc8dca24878e8d83f2ff6ddcf1b3ad8f9383d9cb5e3c252f8e416095` |
| 118 | DOC045-U0001-C0002 | O,V | IRRELEVANT | IRRELEVANT | — / — | `a506381d377985cdb69d6a61bcdb83bfb828f608c310ccb9a3cc05e124673a3f` |
| 119 | DOC045-U0001-C0003 | J,O,V | IRRELEVANT | IRRELEVANT | — / — | `69e486edfc05a05a5849821173e715874223986cdd054a4b425bc49cee11ea27` |
| 120 | DOC045-U0001-C0004 | O,V | IRRELEVANT | IRRELEVANT | — / — | `bc676fcf7e78f928de1bfafb631ba7e544a145f82a29f4b49743c2cb44029af7` |
| 121 | DOC046-U0001-C0001 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `74ca79a0b45ac468eeed1e523ef282ecddda439d948dab458dae35e008bb98b6` |
| 122 | DOC046-U0001-C0002 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `43663cab2ac84b0b54dcd33e0d807b978eb1ad19e987a67d52cca3648cb912b5` |
| 123 | DOC046-U0001-C0003 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `e1f5c47c3c8cc5f2a8d1db3227665ba1092607285eec1c47cadf51a3b25f5ac9` |
| 124 | DOC046-U0001-C0004 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J06 / L16 | `8f7d7c889cb97866240edd0aa1214475f7046e08c8da8cb812e607a693be9eeb` |
| 125 | DOC046-U0001-C0005 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `b41e30396516f2ed23b298987de6615e1af8296609910b1ace90c0bbd244f078` |
| 126 | DOC046-U0001-C0006 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `dba0d0e664e122366fc842a86047fc410466b77bc07544480202c5d9ab14c996` |
| 127 | DOC046-U0001-C0007 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `d2e1d8d10433a3de9aa2db223b05006ae0de675cfff7d0e8d86a976e55f4d7dd` |
| 128 | DOC046-U0001-C0008 | O,T,V | IRRELEVANT | IRRELEVANT | — / L16 | `a728232d30c5e1bf49e02cdb67f39ee48fbbcc2ad41981af19c18c8319fbf112` |
| 129 | DOC047-U0001-C0001 | J,O,T,V | GENERAL_POLICY | CLAIM_START_DATE; ELIGIBILITY_RULE | J06 / L01,L02 | `fa069a33efb872292b8973d62a10a6354d4b364968470bb05871d51ae1a4263a` |
| 130 | DOC047-U0001-C0002 | T,V | IRRELEVANT | ELIGIBILITY_RULE | — / L02 | `99855be3102cad1fe9a00c6ee3b2feb38654c4218f14ed33650affe0fcb2b932` |
| 131 | DOC047-U0001-C0003 | O,T,V | IRRELEVANT | ELIGIBILITY_RULE | — / L02 | `eda3c07e43b94efa1388337613aa2f78b154c5e5d13ff85bf01d4bcfdb038d56` |
| 132 | DOC047-U0001-C0004 | T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L02,L03 | `13ffa9b8a5c0725d5ac55a0d3e32fcc9aaee982568cc4d0cbf584ebf8a19e137` |
| 133 | DOC047-U0001-C0005 | T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L02,L04,L05 | `3e80e8820167241c98238e0ca942d844baf7149100897d6d802471129622a6e8` |
| 134 | DOC047-U0001-C0006 | T,V | IRRELEVANT | ELIGIBILITY_RULE; POLICY_DESCRIPTION; WORKED_EXAMPLE | — / L02,L05,L06 | `1b8e131c7a59fa552b9f2deac73f38e12e86a787beeaad7bcaf06f2eab8701d0` |
| 135 | DOC047-U0001-C0007 | T,V | IRRELEVANT | ELIGIBILITY_RULE; POLICY_DESCRIPTION; WORKED_EXAMPLE | — / L06,L07,L08 | `ba124206a2c389ecc843ac0debead477f22fb8d7338d52397730f2ee05a3f996` |
| 136 | DOC047-U0001-C0008 | T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L07,L08 | `db8f3241728ea4221cfe0da4a27a4da303f6e05466b58e3c111b020a4241eff9` |
| 137 | DOC047-U0001-C0009 | T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L07,L09 | `3bf4160189e66ba663b65f3167f50f479a6da6a6cf2e7ce098eedb0088adfb69` |
| 138 | DOC047-U0001-C0010 | J,T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L07,L10 | `58c78dd5618ee223bc22c1c32f201e8f7ec6d1762898bc19494ba17244fd3bae` |
| 139 | DOC047-U0001-C0011 | T,V | IRRELEVANT | ELIGIBILITY_RULE; WORKED_EXAMPLE | — / L07,L10 | `abb49bf6412b8e13db677ff84455246d8e638c33183dc71b48aa98693ea7e045` |
| 140 | DOC048-U0001-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L11 | `1ef1be96ef873823a26b8da2411b18988d88ff18e351c3cf03fab5ac302a36cd` |
| 141 | DOC048-U0002-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L11 | `1c0088e4a23a497f89b99cebaf42d302558d39ef3b1bffe0c8cd57fc3da8bd94` |
| 142 | DOC048-U0003-C0001 | T | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `c0e494ef84be9e3230ba59ee881af5b11fc2f5a700e14a9f63bfd8f274051321` |
| 143 | DOC048-U0004-C0001 | T,V | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `9a6b9c6924c2a523b440c14233f1fdb4334ba797f2efa6c3611663e924448b5d` |
| 144 | DOC048-U0004-C0002 | V | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `b3431bb1cc0f6f692665a8d566a9ad38ce7ea0f1e45b006c083181fad8af37b3` |
| 145 | DOC048-U0005-C0001 | T,V | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `da5719cbdf3b8462bfe2812e686f352e1b9b257f736f7ca26a25ab123b131a51` |
| 146 | DOC048-U0005-C0002 | T,V | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `83f9dde2252a7c04424c875a568d4f44d6a769be61d2adb784aa2fa347b4fdd4` |
| 147 | DOC048-U0006-C0001 | T | IRRELEVANT | ELIGIBILITY_RULE | — / L12 | `b476eede12e4e50d99aa63018916bc909d431d9c9cc24f5cbafd810b82464087` |
| 148 | DOC048-U0007-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L11 | `a884f5497296c68c4cdfaa0c3947223eb63ddbe4d275f82e529ffba18d5f6923` |
| 149 | DOC048-U0008-C0001 | — | IRRELEVANT | IRRELEVANT | — / L20 | `0db84f3c2405da5b8e52ae1b6bf659fe1f5cf78001dba978e6497b8ece0e6749` |
| 150 | DOC049-U0001-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `80d04001dacdbd138d63adf207b4b9940683f53d6620b6e6cf2748bb8d3a9b3c` |
| 151 | DOC049-U0002-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `71e8f17b83e2d4a9ccb55923487095773d7042af659ad350892f010413727052` |
| 152 | DOC049-U0002-C0002 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `cce309deb61dc2b0541d1d0da46d2d9011cca8f7ff6d5553de967ba6fb742965` |
| 153 | DOC049-U0003-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `6872da2b01ddb22006fca94296a1d85c83de42d4b16562cda624b3701a644306` |
| 154 | DOC049-U0004-C0001 | — | IRRELEVANT | IRRELEVANT | — / L20 | `4200df454756f6ed7430b7cf7c701f6446052d25ae888973800bc7a155458428` |
| 155 | DOC050-U0001-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `d6bf19390cab6f7811ac84b5ad0e666efefd561281f37a5f7116aa2af81377be` |
| 156 | DOC050-U0002-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `5fa7c3defa71f8d60cf150ee01ec817d2937947178c9a95173d694ad32eae588` |
| 157 | DOC050-U0003-C0001 | T | IRRELEVANT | POLICY_DESCRIPTION | — / L15 | `6872da2b01ddb22006fca94296a1d85c83de42d4b16562cda624b3701a644306` |
| 158 | DOC050-U0004-C0001 | — | IRRELEVANT | IRRELEVANT | — / L20 | `c24a37ee9cc6bb8cee9d21371b7048c8d9ac13d242fe371d4acb0f9973aa98ed` |
| 159 | DOC051-U0001-C0001 | O,T | IRRELEVANT | IRRELEVANT | — / L19 | `fccd2a446089fa4cac0b8d1a58b212dfd1250795b0aeed4be440776d14db6494` |
| 160 | DOC051-U0002-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J06 / — | `c6c84e74373cbeb272f6ad9b52f3e5df5355adfc038619246d0bf8a19040759b` |
| 161 | DOC051-U0003-C0001 | T | IRRELEVANT | IRRELEVANT | — / L19 | `42568fb94fbe68e90372ad798e52c01e31c4f4bf53eda5334bdbc352b67b0066` |
| 162 | DOC051-U0003-C0002 | T,V | IRRELEVANT | IRRELEVANT | — / L19 | `1d290ad2b4a0836e9a937d9382555cd29f1f62a096fd45a3f14637a9fea1341d` |
| 163 | DOC051-U0003-C0003 | V | IRRELEVANT | IRRELEVANT | — / L19 | `cd51d39cc15ea75be812f71db3c47566c8a5ef0cf8bef2b628fff09cd2a00bb0` |
| 164 | DOC051-U0003-C0004 | — | IRRELEVANT | IRRELEVANT | — / L19 | `2c60f45c850b5f6077973775069c56fa756821398ca252d70dca713b6484a645` |
| 165 | DOC051-U0003-C0005 | — | IRRELEVANT | IRRELEVANT | — / L19 | `589ba7f3b3633aa67522144d07e66dcf9f0e86e4b62ab6295f998ae8b2f7e646` |
| 166 | DOC051-U0003-C0006 | — | IRRELEVANT | IRRELEVANT | — / L19 | `642c16b43001e4f9686d5b87326769f801f2158bebe4d4536cca148b48029d20` |
| 167 | DOC051-U0003-C0007 | T,V | IRRELEVANT | IRRELEVANT | — / L19 | `1b83e46ad08cfb5e18948851fadf2b41bd77f987c5011ad50fcb2bef4250d1ad` |
| 168 | DOC051-U0004-C0001 | O,V | IRRELEVANT | IRRELEVANT | — / L19 | `d8eab695f4e99851a006c184f6f366cc977a97f8188bee61c8ef27b331fc7a27` |
| 169 | DOC051-U0004-C0002 | J,O,V | IRRELEVANT | IRRELEVANT | — / L19 | `70bdbf8f9adf895ede400aee8d38827f2123266e5bc668597fb4822947f5c879` |
| 170 | DOC051-U0005-C0001 | T | IRRELEVANT | IRRELEVANT | — / L19 | `5f2e48c16af1d40cea75fb3acf0fa7ab43b85de074ee52ffc7be23358a6db411` |
| 171 | DOC051-U0005-C0002 | T | IRRELEVANT | IRRELEVANT | — / L19 | `e9f4ac8f10801f5df61552c3660d7353060c3c433138b22ea82b6b09f83bf7bc` |
| 172 | DOC051-U0005-C0003 | V | IRRELEVANT | IRRELEVANT | — / L19 | `b02855bc68b4fc1f2cf2f09423ffaa5b20f82a5dca7758018ea6f2d33ee68c83` |
| 173 | DOC051-U0006-C0001 | J | IRRELEVANT | IRRELEVANT | J24 / L19 | `a54e3940fdd15c25232939e0c3d4df1d44ce333761c47187d90d8d7ecad32eb3` |
| 174 | DOC051-U0006-C0002 | J | IRRELEVANT | IRRELEVANT | J24 / L19 | `6b6f8ba6c8ada819b14d14cc64839e527a196a6dbd03a90f8101434d2fe8b1a7` |
| 175 | DOC051-U0006-C0003 | O,T,V | IRRELEVANT | IRRELEVANT | — / L19 | `657e882c948a9ab464f7b0d522903a7bf09cadfa11ddf658fdbcc2e823b2e1e4` |
| 176 | DOC051-U0006-C0004 | O,V | IRRELEVANT | IRRELEVANT | — / L19 | `9fd1e436540f46a8bddff996a7064d594165ce05f33315ed4f5ea84a86349d9c` |
| 177 | DOC051-U0006-C0005 | O,V | IRRELEVANT | IRRELEVANT | — / L19 | `cd8c17907409b4a2d33490a970476222763a13dcbab21abb3f556bca44eeb4a7` |
| 178 | DOC051-U0006-C0006 | O,T,V | IRRELEVANT | IRRELEVANT | — / L19 | `558c8b7e30ffa3b48e61742298cbe4df98c559389d3b9c0b2e7bc1ccd45d7a2a` |
| 179 | DOC051-U0006-C0007 | O,T,V | IRRELEVANT | IRRELEVANT | — / L19 | `856523f6c3381a32e691cd4b635f07869d914ec2ab3b3cce5c62bad68913e506` |
| 180 | DOC051-U0006-C0008 | O,T,V | IRRELEVANT | IRRELEVANT | — / L19 | `29061d7ab5ec27e860018421fa63193751d447e2f5b222c6d8b1ee57827a4acf` |
| 181 | DOC051-U0007-C0001 | — | IRRELEVANT | IRRELEVANT | — / L19 | `ff1fd95abcba1b266447626f8904a8e447a49b74c823aba1c9e3c1fb5ef7b6a8` |
| 182 | DOC051-U0008-C0001 | — | IRRELEVANT | IRRELEVANT | — / L19 | `5abceefb1eea5dcdbabeb918a4a2b0fdd83d3cdac2764a2f36c29ccd1d5c9646` |
| 183 | DOC051-U0009-C0001 | — | IRRELEVANT | IRRELEVANT | — / L19 | `77dee1cc96588ffa0471bcc89d8de5f4f224ca7e28aad50dd72042b78f7a5b90` |
| 184 | DOC052-U0001-C0001 | J,O,T | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `b74ace550ec2fdb48ae745da9bfe5eb901d77d4b5e6de92438c40808e7c905e9` |
| 185 | DOC052-U0002-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `90578c50940bdcfdd690f02e82e2bd01333966c3e6f065a1d0e69e39dc720cd2` |
| 186 | DOC052-U0003-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `e8e1bdaa58afe55407ecec39f1649bb81129f94fff766101c5b6a2ee36f88ff3` |
| 187 | DOC052-U0003-C0002 | O,T | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `ab10a1905d4ffa3140090786ad2c30737e2cc19dc6755248eb39954b8868ede7` |
| 188 | DOC052-U0004-C0001 | J,O,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `082e1535623492c7fa31f26ce895e23daabfbedadb22f2ed8b6f087917733014` |
| 189 | DOC052-U0005-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / L17 | `a46332fa986339089268939cd8f86e26d31ee511691b2a4157d86df8cf50896e` |
| 190 | DOC052-U0005-C0002 | J,O | FORECAST | IRRELEVANT | J07 / L17 | `1fea294a5ad382ad629add8c1148c18f9b806ac8072147185cc1b3358b0767d5` |
| 191 | DOC052-U0006-C0001 | J,O,T | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `b05ba2068987165886ffbaf92e7fe7f1a7f11c1f000f340fa89c8ad364f2d73c` |
| 192 | DOC052-U0006-C0002 | J,O | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `6ad235f197f298effb6bdfa3f28135b9a4557f9f009d728ec0644f1081779cab` |
| 193 | DOC052-U0007-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `8c490803c607f06163e83725cdae27a694e5ee5efcc852e8e023048be0b19130` |
| 194 | DOC052-U0007-C0002 | T,V | IRRELEVANT | IRRELEVANT | — / — | `3ba104682b981859fdea7980b56cbdd56b8b569e097943ec9698c700fcce8b3d` |
| 195 | DOC052-U0008-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J11 / L17 | `a378044c16c5c5df45d5a68d5b50ac397c4d57a7d71b60e31dbb1272c0c245c5` |
| 196 | DOC052-U0008-C0002 | O | GENERAL_POLICY | IRRELEVANT | J11 / L17 | `ce127f7f34edb115324a21703e399b087c205e5a2b91610586a941b777f93fb0` |
| 197 | DOC052-U0009-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J11 / — | `81ad84941e0bb3142f83c038350aef4ca8dba2e0985438fed3cac40797bbf750` |
| 198 | DOC052-U0009-C0002 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J11 / — | `6f4961d825319a41d641291add7e81705a8db6870d552173f12dd7f9de9bef9b` |
| 199 | DOC052-U0010-C0001 | J,O,V | GENERAL_POLICY; IRRELEVANT | IRRELEVANT | J11,J12 / — | `97d3e90703b7e0571317b43fc318bf7a0cb041bd367da40ef6f27844179fe8d1` |
| 200 | DOC052-U0010-C0002 | J,O | IRRELEVANT | IRRELEVANT | J12 / — | `c4cdd9a69ee59443e66106a370ebfffa379b820af5ff33b2e6e37aba65203362` |
| 201 | DOC052-U0011-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `3c33bb675d1a90deb042118706698317e1edeb27da38ea9a792262d4505c424c` |
| 202 | DOC052-U0012-C0001 | J,O,T,V | FORECAST | IRRELEVANT | J08 / — | `67964d32e0d957be9ca28c2cf124cc6b9960f727f7a0bd85fc5ad66057f14ce3` |
| 203 | DOC052-U0012-C0002 | O | GENERAL_POLICY | IRRELEVANT | — / — | `5830417614601aa74cccbaa8f64c068e81af3db3dc4dda4062523b6226ae867c` |
| 204 | DOC052-U0013-C0001 | O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / L17 | `cc5e7fc9270d450a09d24d537a379d10b26e1a81bd8de57ad57af85e6417d342` |
| 205 | DOC052-U0013-C0002 | O | GENERAL_POLICY | IRRELEVANT | — / L17 | `be92a603704ac5c6246cb4e878b42ceab1ad02153fd92a263fd9111ef7809ee4` |
| 206 | DOC052-U0014-C0001 | O,T,V | GENERAL_POLICY | IRRELEVANT | — / L17 | `b4a5454740f28208a58d3ad3572309a252f479ff71a48f6fa9825d75deb60154` |
| 207 | DOC052-U0014-C0002 | O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `3187c228245484d2bef59963b4b544c277d9f5dbdf3fa6f6c9c7e813ed8161ba` |
| 208 | DOC052-U0015-C0001 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J11 / L21 | `5a4cdefd84b7acc35110ef86947448ac487201fdf0734cb617f967344e85afac` |
| 209 | DOC052-U0015-C0002 | J | GENERAL_POLICY | IRRELEVANT | — / — | `89c12f0f8a430fe972c48fec1c0073e84435e12ea4f00768bef0cd42a5ef2175` |
| 210 | DOC052-U0016-C0001 | O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J11 / L21 | `885928065cbefca206bb1eeadbe22360564bebf8ed7bc68a7004b7dc55308358` |
| 211 | DOC052-U0017-C0001 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J11 / L21 | `fc78edc690d37b3e3759040c367cbb926b3dbf32acbdbca0d511e8408bb01136` |
| 212 | DOC052-U0018-C0001 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J11 / L21 | `ae93f6f4bebd16cf2346c6e352a1e709760cc31b9377d7ebbc794842ec06f535` |
| 213 | DOC052-U0019-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / — | `95eaf273c35ea8228c86fea9ad913b0ab12985cd5ae4b7946e77068e262fd069` |
| 214 | DOC052-U0020-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / L17 | `247fc564a6003061e8be2b6a1861c061062dbf15f15688ec75890c3cbf2b2f96` |
| 215 | DOC052-U0020-C0002 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J10 / L17 | `792e966356e486124ea9ab680349e526c872f716e4b610346edbe330f8db8024` |
| 216 | DOC052-U0021-C0001 | J,O,T,V | FORECAST | IRRELEVANT | J09 / — | `c4c0cd587677f842e71b7f34c3d6aaded928dde3906081253d186c58688a431b` |
| 217 | DOC052-U0022-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J11 / L17 | `be54b8cb2d4d47957d9cfbeab8648b6bb62e65ec738c7ce53ca9d1b441d50d52` |
| 218 | DOC052-U0022-C0002 | O,T | GENERAL_POLICY | IRRELEVANT | J11 / — | `ea28571a9a5a6e9c414aca1c2983acce4ad296992803cc3f6b82fa859536276e` |
| 219 | DOC052-U0023-C0001 | J,O,V | ANTICIPATED_OUTPUT; GENERAL_POLICY | IRRELEVANT | J11,J13 / — | `166f424a6fdc9363993adfd3a985990a0006f91cf852d9152d0e0ce6c62a5e0a` |
| 220 | DOC052-U0024-C0001 | T | IRRELEVANT | IRRELEVANT | — / — | `2b61114805b2505c1a35810e2fc7a69122e1bbc4b986265e6792ec0347806701` |
| 221 | DOC052-U0025-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `b7a56873cd771f2c446d369b649430b65a756ba278ff97ec81bb6f55b2e73569` |
| 222 | DOC052-U0026-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `5f9c4ab08cac7457e9111a30e4664920607ea2c115a1433d7be98e97e64244ca` |
| 223 | DOC052-U0027-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `670671cd97404156226e507973f2ab8330d3022ca96e0c93bdbdb320c41adcaf` |
| 224 | DOC052-U0028-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `59e19706d51d39f66711c2653cd7eb1291c94d9b55eb14bda74ce4dc636d015a` |
| 225 | DOC052-U0029-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `68821fd280c7970f2a92f785f9e930193b04e1d0d626638ab59e6084f4d8c224` |
| 226 | DOC052-U0030-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `624b60c58c9d8bfb6ff1886c2fd605d2adeb6ea4da576068201b6c6958ce93f4` |
| 227 | DOC052-U0031-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `eb1e33e8a81b697b75855af6bfcdbcbf7cbbde9f94962ceaec1ed8af21f5a50f` |
| 228 | DOC052-U0032-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `e29c9c180c6279b0b02abd6a1801c7c04082cf486ec027aa13515e4f3884bb6b` |
| 229 | DOC053-U0001-C0001 | O | IRRELEVANT | IRRELEVANT | — / — | `57f69d564c9010a899e71d8502f2cc3b4fed2b1922614e144e8e0c0e431c5bc5` |
| 230 | DOC053-U0002-C0001 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `6228e9d83bd3a0e8b08b440013d2f244bffcf285c4a7c5fce30cfeb23041abbc` |
| 231 | DOC053-U0003-C0001 | O,T,V | IRRELEVANT | IRRELEVANT | — / — | `d1843c988ac16928d17864da6de71f65462819bfbf933726554379916a21e572` |
| 232 | DOC053-U0004-C0001 | O,V | IRRELEVANT | IRRELEVANT | — / — | `2d22de9dd2c4618f7b3359b97ad744ed8d074ece50f1f415fdf6ad24d9c73613` |
| 233 | DOC053-U0005-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `a1d09f8e169a57201ad9f08e68eae9276b6ba37c729dbbc8e1b0351c3015a230` |
| 234 | DOC053-U0006-C0001 | J,T | GENERAL_POLICY | POLICY_DESCRIPTION | — / L13 | `f3b74949a77ca9c4664521197fbf9d0a6acd2242545d1b9b4b22c2577bbca183` |
| 235 | DOC053-U0007-C0001 | J,O,T,V | FORECAST | IRRELEVANT | J14 / L17 | `b451241ba120af3be12e906190844d67a1fcea424ecb5a2c418d25cbc75aa237` |
| 236 | DOC053-U0008-C0001 | J,O,T,V | ANTICIPATED_OUTPUT; GENERAL_POLICY; IRRELEVANT | IRRELEVANT; POLICY_DESCRIPTION | J18,J19,J21 / L17,L21 | `f0d4496da0da8c33582a7a15f3d712761a67e3c1d772e3809d5606ed529ba4e0` |
| 237 | DOC053-U0009-C0001 | J,O,T | FORECAST | IRRELEVANT | J14 / L17 | `a8904a723f9f6945fa97e205716dd3f90dfa484b7268c7d06eba9edb95a43158` |
| 238 | DOC053-U0009-C0002 | J,O | FORECAST | IRRELEVANT | J14 / — | `53d3f308bbbc4620f09bf3644a07939f28806704b1deb5423f689e9cec43d861` |
| 239 | DOC053-U0010-C0001 | J,O,V | GENERAL_POLICY | IRRELEVANT | — / L17 | `0bb5deb89bf6b1e1cb2b473ab3d68b17f89c0c846e1d7b9adfec00adcaf9a80f` |
| 240 | DOC053-U0011-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / L17 | `54af4471cddd278ddd8a8c9499fb16537e9aff20b9c6e4bbdb50c7e1bd1ea8c3` |
| 241 | DOC053-U0012-C0001 | J,O,V | GENERAL_POLICY | IRRELEVANT | J20 / L17 | `2239be452666c4c254a09c05e58028681ed8ec11f92e08d9dc865ac48fef700b` |
| 242 | DOC053-U0013-C0001 | O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J21 / L21 | `96a73d18b9689cda31837799c276a93129e8e50ac75b18781baf6077e9ca81a1` |
| 243 | DOC053-U0014-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `0279f349268e645898611160831c8be8a56d03eca9744d00ebc366146ec99c62` |
| 244 | DOC053-U0015-C0001 | J,O,T,V | IRRELEVANT | IRRELEVANT | — / — | `9640e13ca0f1c7b600edd3c4555ec46350d73aade129c0e6ffd166208eb44133` |
| 245 | DOC053-U0016-C0001 | J,O,T,V | IRRELEVANT | IRRELEVANT | — / — | `82907fe4eec2a6146e6a0a0ae3760184203344c44cf34a97c27e4c73d009e52c` |
| 246 | DOC053-U0017-C0001 | O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `0d00b7e8b738d10c5c7b88a5694a6df0b52226ba260877c2897e9079e0af5013` |
| 247 | DOC053-U0018-C0001 | J,O,V | FORECAST | IRRELEVANT | J14 / — | `d673444c2fa859b8a3c4a859cf84b7524bfb327cefa74d0750b528c5cc0e969a` |
| 248 | DOC053-U0019-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | — / — | `94f7995f80bba73481283bd78535d9b8c768476085e821efc9875a454a753071` |
| 249 | DOC053-U0020-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J20 / — | `ed853ec12b5d87dcfd1a6d4b1457c1242c32e0d9d29a41c0f27e0e3a3c1bafb6` |
| 250 | DOC053-U0021-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `2dae65404981df7bfaf42a513a60dcbc753b69e6410d9c8e5157bf92be8fdc4b` |
| 251 | DOC053-U0022-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `afbe286a26114dc52336a22c0d28b3c99db47775b432f36b8fafd70dbc9f0135` |
| 252 | DOC053-U0023-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `2e5dad27b613cbd2e3d9a0c140809f6ac61925dce8d0a44a4a062c6c5c4e129a` |
| 253 | DOC053-U0024-C0001 | J,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `cc6de1018905a7ab11140acb7775d79058dff4166c17b0d32ebccd4b0dc74d86` |
| 254 | DOC053-U0025-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J20 / — | `141d5fb512c5b253a7c5ac49e255abc4cd792cb0a61354891b29835f3ce36b01` |
| 255 | DOC053-U0026-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J20 / — | `cace2da7a58735713dd639acf56bcbd47f0dde3726c9f83b5f3af8b50c2d505c` |
| 256 | DOC053-U0027-C0001 | T,V | IRRELEVANT | IRRELEVANT | — / L17 | `9e530375a51793b8e24666f31533369b9686a0e2c5271fada92aa1251405af33` |
| 257 | DOC053-U0028-C0001 | J,O,T,V | GENERAL_POLICY | POLICY_DESCRIPTION | J20,J21 / L21 | `b86f1b34a4b4877452cc9bbb4ce2417424eb44917b6b5d5bb95297725961475c` |
| 258 | DOC053-U0029-C0001 | O,T,V | GENERAL_POLICY | IRRELEVANT | — / — | `7363a6f0c90828267e87566e6105badce4a6aba98ac3475525ebfec5a53a9f36` |
| 259 | DOC053-U0030-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J20 / — | `c2cf64313aa8ccaec60715dd89fe46a815d51cda3d027c774978d8ff0dd222cf` |
| 260 | DOC053-U0031-C0001 | O,T,V | GENERAL_POLICY | IRRELEVANT | — / L17 | `ac46a29f0bee89e89063aa941ff7a888cae8a6d67875c59a96e7d0dc0673f6ac` |
| 261 | DOC053-U0032-C0001 | J,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `6a873c7c01785d2a985e2fa462bdb4e7251f8af54a0b3778a7e42a5799c7e6f1` |
| 262 | DOC053-U0033-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J15 / — | `63f458b4e111efd45be6b2f9d2a93cbe590ae05984393eeabf69f321ec48f681` |
| 263 | DOC053-U0034-C0001 | O | GENERAL_POLICY | IRRELEVANT | — / — | `35b9dec31f2f7ce19688bb9cafe6f4aab35a706131c61077c4aa29f35f210de0` |
| 264 | DOC053-U0035-C0001 | J,O,T,V | ANTICIPATED_OUTPUT | IRRELEVANT | J17 / — | `c27ba5164b448f1250c5ed785e5e0a64a50a33f9e5995a8976af1ba76bd139ba` |
| 265 | DOC053-U0036-C0001 | J,O,V | ANTICIPATED_OUTPUT | IRRELEVANT | J17 / — | `c79232baeb022e75c3458339887a2d43d849305b254fe33fc5d27ba701bb75cc` |
| 266 | DOC053-U0037-C0001 | J,O,T,V | FORECAST | IRRELEVANT | J16 / L17 | `89bc3cd086dbd0cf9d063cd137264f35c1a9485bf01fe7f054d5a09ef0a0b6ec` |
| 267 | DOC053-U0038-C0001 | J,O,T,V | IRRELEVANT | IRRELEVANT | J22 / L17 | `c9e7974a12159efd20ed0bb71a54416674ec2e6e7bae1b7f0bb562c1d950c538` |
| 268 | DOC053-U0039-C0001 | J,O,T | GENERAL_POLICY | IRRELEVANT | J20 / — | `5cca6059b4b371ef7135db3312afaf772e8c0583efd33f421cd8fdbe0a2f72d6` |
| 269 | DOC053-U0040-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J20 / L17 | `b1f9654f7abb6c6443bfcf9ab234bee04c44d66a8b40c6773ec62c0ea8f7799c` |
| 270 | DOC053-U0041-C0001 | O,T | GENERAL_POLICY | IRRELEVANT | — / — | `62d851d8be3ceb0b9f71003557c891b2d79acc7df142b619a8ebf2db30b776f0` |
| 271 | DOC053-U0042-C0001 | — | IRRELEVANT | IRRELEVANT | — / — | `0af0d9682dec336646e5592d4187609910755af1a2832060728a08c4bdb5a400` |
| 272 | DOC053-U0043-C0001 | J,O,V | GENERAL_POLICY | IRRELEVANT | J20 / — | `3011be58da78e69c43d44f6a780e909d4b5386963270b777a1b646e0f0903892` |
| 273 | DOC053-U0044-C0001 | O,V | IRRELEVANT | IRRELEVANT | — / — | `102c111780440fe69e7722b51ed8f77481f94c98987bb5e48b856c3384808561` |
| 274 | DOC053-U0045-C0001 | J,O,T | GENERAL_POLICY | POLICY_DESCRIPTION | J20,J21 / L21 | `ce9abe63b07b46c78338db87014506a71517d796663af72b3aca3bd0f51953ce` |
| 275 | DOC053-U0046-C0001 | J,O | ANTICIPATED_OUTPUT | IRRELEVANT | J18 / — | `58d28a3c73aa34a01576fa65bdab6cc23b7c4bfafdb4505623a4d41003b8db35` |
| 276 | DOC053-U0047-C0001 | J,O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J20 / L21 | `8661213e7f0fd58498fa01af8b75f56236ce583cbfdd83bcb127fc1fac9c82b6` |
| 277 | DOC053-U0048-C0001 | O,V | GENERAL_POLICY | POLICY_DESCRIPTION | J21 / L21 | `f5a8d2601995a6d4cd07e482afafb9186ba3f0f22d78f3a29edc8614dc4b656c` |
| 278 | DOC053-U0049-C0001 | J,O,V | FORECAST; GENERAL_POLICY | POLICY_DESCRIPTION | J16,J21 / L21 | `bcb54568c9b7a5bf91b038323ffd2f05e6ce9c92fc8a0093ed47af38fcd58f57` |
| 279 | DOC055-U0001-C0001 | J,O,T,V | GENERAL_POLICY | IRRELEVANT | J23 / L18 | `af80911751672c13578276f6fc3f04d8980f1b420030cc34c40e3a30f3ca76fd` |
| 280 | DOC055-U0001-C0002 | J,T,V | GENERAL_POLICY | IRRELEVANT | J23 / L18 | `d6765cb0c332017e20cf1759d607fb6d2f5ac2aa4078e3873accf4992bbaa0c2` |
| 281 | DOC055-U0001-C0003 | J,T,V | IRRELEVANT | IRRELEVANT | J24 / L18 | `df5c179169d50787ef27e9b860afdebdcfc41e919edcc7e9aefd005c7901f650` |
| 282 | DOC055-U0001-C0004 | J,O,T,V | IRRELEVANT | IRRELEVANT | J24 / L18 | `170fa4d13165b2ba43c1ccd09d4eb68fc242d686fda13f9f316076c1b2e218f0` |
| 283 | DOC055-U0001-C0005 | J,O,T,V | IRRELEVANT | IRRELEVANT | J24 / L18 | `138f0d53540c14f4ccda68c0763005d1f3eb23d92fcde51aa2baa059aa938b68` |
| 284 | DOC056-U0001-C0001 | T,V | IRRELEVANT | IRRELEVANT | — / L18 | `850c8f841a6964039b5cd1667fc700d25b85369ceb4ebeed74b6b1b63c59ad2f` |
| 285 | DOC056-U0001-C0002 | O,T,V | IRRELEVANT | IRRELEVANT | — / L18 | `59448e424670bb8a46b0bfb8a74798faf9149c155a52e302c0807c2a2ea86d62` |
| 286 | DOC056-U0001-C0003 | O,T,V | IRRELEVANT | IRRELEVANT | — / L18 | `9ee87b8d07e697fabe72239334c12f4ffd744e76971f75bbf38bbc2c7203f902` |
| 287 | DOC057-U0001-C0001 | T,V | IRRELEVANT | IRRELEVANT | — / L18 | `ae6e863d5300a974fef0ff52cf9ad52ebc0c3e6848140fc2cc1780d0697f6edb` |
| 288 | DOC057-U0001-C0002 | O,T,V | IRRELEVANT | IRRELEVANT | — / L18 | `3d3a615ce5a96557e53bd9b7addc30d609866f24b7b45667b136c7b0bc09c5eb` |
| 289 | DOC057-U0001-C0003 | T | IRRELEVANT | IRRELEVANT | — / L18 | `43aa5987f5061ed5f95012888842fdb56f14d7f0a4262a8458a3fdddb4033832` |
| 290 | DOC057-U0001-C0004 | T | IRRELEVANT | IRRELEVANT | — / L18 | `30176225755e0911c41036b327868819cc3e2f1f75525f1534d3270a5f6a5966` |
| 291 | DOC058-U0001-C0001 | O | IRRELEVANT | IRRELEVANT | — / L19 | `b80fd69bc69e5f46efbaea8b06dd56e4b281d73c111a1cbfdd74814de7aa784a` |
| 292 | DOC058-U0001-C0002 | O,V | IRRELEVANT | IRRELEVANT | — / L19 | `a87859c86f6410c4ea80228c62be1986f8dbaad4435726cd6b1d1298e89237ec` |
| 293 | DOC058-U0001-C0003 | O,V | IRRELEVANT | IRRELEVANT | — / L19 | `0543ea27b769acc779b7b14e674b489fc48d0fb7f6563719aa074509bf1b24e6` |
