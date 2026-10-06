# Expert Human Validation Response Contract v1

Date: 2026-10-06

Status: FROZEN BEFORE EXPERT RESPONSES AND BEFORE PRIMARY LLM JUDGE EXECUTION

## Scope

The expert validation subset contains 27 previously frozen benchmark outputs:

- UC1: 9
- UC2: 9
- UC3: 9

The expert validation sample is not a replacement for the full 270-output
benchmark evaluation. It validates the semantic evaluation process.

Each expert-facing case remains blinded to:

- B0/B1/G1 condition;
- repetition;
- run ID;
- workflow/policy identity;
- recovery behavior;
- tokens/calls/latency/resources;
- LLM judge outcomes.

## Expert response fields

For every assigned case, the expert records:

### 1. Correctness

- 2 = Correct
- 1 = Partially correct
- 0 = Incorrect

Correctness is judged using the task question, reference answer, and reference
evidence.

### 2. Abstention outcome

One of:

- correct_abstention
- failed_to_abstain
- incorrect_abstention
- not_applicable

### 3. Grounding summary

One of:

- Supported
- Partially supported
- Unsupported
- Contradicted
- Not applicable

Grounding is judged only against retrieved evidence available to the workflow.

### 4. Optional comment

Free-text clarification only when useful.

## LLM-to-expert grounding aggregation

The LLM judges produce claim-level grounding labels.

For comparison with the expert output-level grounding judgment, claim-level
labels are deterministically reduced using this precedence rule:

1. If any claim is CONTRADICTED:
   output grounding = Contradicted

2. Else if any claim is UNSUPPORTED:
   output grounding = Unsupported

3. Else if any claim is PARTIALLY_SUPPORTED:
   output grounding = Partially supported

4. Else if one or more claims exist and all are SUPPORTED:
   output grounding = Supported

5. If the output is a pure abstention with no substantive factual claims:
   output grounding = Not applicable

This rule is frozen before LLM benchmark judging and before expert responses
are inspected.

No post-hoc reconciliation or case-specific override is allowed.

## Agreement analysis

On the 27 frozen expert-validation cases:

- correctness:
  exact agreement and quadratic-weighted Cohen kappa;

- abstention:
  exact agreement and unweighted Cohen kappa when estimable;

- grounding summary:
  exact agreement and unweighted Cohen kappa when estimable.

Comparisons will be reported separately for:

- LLM Judge 1 vs Expert;
- LLM Judge 2 vs Expert.

If kappa is undefined because a marginal category has no variation, exact
agreement will still be reported and kappa will be marked not estimable.

The 27-case expert sample is a process-validation sample and will not replace
the full 270-case benchmark outcome analysis.

## Independence

Expert responses may be collected before or in parallel with LLM judge
execution.

Experts must not see LLM judge outputs before submitting their evaluations.

LLM judges must not see expert responses.

## No result-driven modification

After this contract is frozen:

- the 27-case subset will not be changed based on expert or LLM results;
- response categories will not be changed based on observed agreement;
- grounding aggregation will not be changed based on observed agreement;
- disagreements will not be silently reconciled.
