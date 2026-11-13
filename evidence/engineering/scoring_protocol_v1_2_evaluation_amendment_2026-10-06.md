# Scoring Protocol v1.2 — Evaluation Amendment

**Date:** 2026-10-06  
**Status:** To be frozen before new judging or statistical outcome analysis  
**Applies to:** Thesis benchmark (270 executions across UC1–UC3)

## 1. Reason for amendment

The original scoring protocol assigned one human evaluator to all 270 benchmark outputs, with a second independent human evaluator on a subset. After implementing and piloting the blinded evaluation workflow, full manual review of all 270 outputs was judged impractical. This feasibility issue motivated the documented amendment before statistical outcome analysis.

The revised design replaces the planned 270-output manual review with two independent blinded LLM judges, while retaining independent expert human validation on a pre-specified 27-output subset.

The single human judgment already recorded under the earlier protocol is retained as a **pilot/provenance artifact only**. It is not part of the confirmatory human-validation design.

The earlier frozen **90-output secondary-human subset** is also retained unchanged as a historical/provenance artifact from protocol v1. It is **superseded for confirmatory human validation by this v1.2 amendment** and will not be used or repurposed as the new validation sample.

## 2. Full 270-output evaluation

All 270 frozen benchmark outputs will be evaluated independently by:

- **LLM Judge 1**
- **LLM Judge 2**

Both judges must be open-source models and independent of the model used to generate the benchmark outputs. Preferably, the two judges will also come from different model families.

### 2.1 Blinding

The judge may receive only information needed for semantic evaluation:

- opaque evaluation identifier;
- task question;
- generated output or abstention;
- frozen reference answer;
- resolved reference evidence;
- retrieved evidence included in the blinded scoring package.

The judge must not receive:

- B0/B1/G1 condition;
- repetition number;
- original run identifier;
- execution sequence;
- recovery-policy action or path;
- latency;
- token counts;
- LLM/retrieval call counts;
- resource-use fields;
- aggregate or condition-level results.

### 2.2 Evaluation rubric

The existing frozen semantic rubric remains the basis for judging:

- **Correctness:** 2 = correct, 1 = partially correct, 0 = incorrect;
- **Abstention outcome:** according to the frozen abstention categories;
- **Claim-level grounding:** Supported / Partially Supported / Unsupported / Contradicted;
- brief reasons sufficient to audit the judgment.

The amendment changes **who/what performs the complete evaluation**, not the meaning of the outcome labels.

### 2.3 Reproducibility

Before execution, freeze for each judge:

- exact model name/version/quantization where applicable;
- inference runtime and version;
- context length;
- temperature and sampling settings;
- seed where supported;
- system and evaluation prompts;
- structured output schema;
- parser/validation rules;
- operational-failure and retry rules.

Raw judge responses and parsed judgments must be saved immutably. A valid completed judgment must not be overwritten or rerun because its score is undesirable.

## 3. Expert human validation

A **27-output blinded validation set** will be frozen before inspecting new judge outcomes:

- UC1: 9 outputs;
- UC2: 9 outputs;
- UC3: 9 outputs.

Within each UC, the selection should be balanced across B0/B1/G1 as closely and cleanly as possible (target: 3 outputs per condition) and preserve coverage of the main task types. Selection must be deterministic/random within pre-defined strata and must not depend on judge scores or benchmark outcomes.

Domain-relevant expert validators for the three use cases will evaluate a simple blinded package using the same core correctness/abstention/grounding semantics needed for validation.

Expert validators are **different people from the interview participants**.

## 4. Agreement analysis

The evaluation study will report, as applicable:

- LLM Judge 1 ↔ LLM Judge 2 agreement on the full 270;
- LLM Judge 1 ↔ Expert Human agreement on the 27;
- LLM Judge 2 ↔ Expert Human agreement on the 27.

For ordinal correctness, report exact agreement and quadratic-weighted Cohen's kappa. Abstention agreement and grounding agreement will be reported separately using metrics appropriate to those labels.

Disagreements remain part of the evidence and must not be silently reconciled. Any adjudication, if later required, must be explicitly documented as a separate step.

The 27-item expert set validates the judging process; it is **not a replacement outcome sample**. Primary condition-level quality conclusions use the complete 270-output judged dataset together with the pre-specified statistical design.

## 5. Separate interview study

Interview participants / end-user evaluators are a separate group from the expert validators.

They may have mixed professional backgrounds relevant to document-based knowledge work and do not all need to be domain experts in one use case. Each participant will see only a small number of blinded scenarios and provide short structured ratings followed by semi-structured discussion.

Candidate constructs include:

- trust;
- usefulness;
- perceived reliability;
- perceived control;
- perceived risk;
- willingness to use/adopt.

A perceived-correctness/confidence rating may be included if retained in the final interview protocol, but it is a **participant-perception measure**, not the formal benchmark correctness label.

The interview data will be analysed separately from the benchmark expert-validation data.

## 6. Role terminology

Use these labels consistently:

- **LLM Judge 1** — independent full 270-output evaluator;
- **LLM Judge 2** — independent full 270-output evaluator;
- **Expert Human Validators** — blinded 27-output validation set;
- **Interview Participants / End-user Evaluators** — human/organizational study.

Do not call the interview participants "Reviewer B" in the thesis.

## 7. Paper/thesis boundary

The thesis retains all 270 benchmark executions across UC1–UC3 plus expert validation and the interview study.

The planned paper remains **UC1-only**:

- 10 tasks;
- 3 conditions;
- 3 repetitions;
- 90 executions;
- B1 vs G1 is the primary comparison;
- B0 is a supporting conventional-RAG reference.

UC2/UC3 outcomes must not be used to support UC1-only paper claims.

## 8. Execution gate

No new judge execution or confirmatory statistical outcome analysis may begin until all of the following are frozen:

1. this v1.2 amendment;
2. the 27-output validation-sampling rule and selected opaque IDs;
3. Judge 1 model/configuration/prompt/schema;
4. Judge 2 model/configuration/prompt/schema;
5. operational-failure/retry rules.

Only after these gates pass should the two 270-output judging runs begin.
