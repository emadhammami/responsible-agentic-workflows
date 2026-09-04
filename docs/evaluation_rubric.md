# Technical Benchmark Evaluation Rubric

**Rubric version:** 0.1
**Status:** Working definition

## 1. Purpose

This rubric defines how outputs from the technical benchmark will be evaluated.

It is specified before implementation of the evaluated workflows so that the
evaluation criteria are not adapted to favor a particular system condition.

The rubric applies to B0, B1, and G1 wherever the metric is applicable.

## 2. Evaluation principles

Evaluation should:

- use the same task definitions across comparable conditions;
- use the human-validated reference answer and evidence;
- keep reference answers unavailable to the runtime workflow;
- distinguish task correctness from evidence grounding;
- distinguish retrieval quality from answer quality;
- evaluate abstention explicitly;
- preserve failed runs rather than excluding them;
- use objective logged measurements where possible;
- document any model-assisted evaluation separately;
- blind human evaluators to system condition where practical.

## 3. Answer correctness

Answer correctness is evaluated against the human-validated reference answer.

### Score 2 - Correct

The response answers the task correctly and contains no material factual error.

Minor differences in wording are allowed.

### Score 1 - Partially correct

The response contains the core of the correct answer but is materially
incomplete, imprecise, or contains a limited error that does not fully reverse
the main conclusion.

### Score 0 - Incorrect

The response:

- gives the wrong answer;
- substantially contradicts the reference answer;
- omits the essential answer;
- provides an answer when the task requires abstention; or
- abstains from an answerable task without valid reason.

Correctness should not be judged by lexical similarity alone.

## 4. Grounding

Grounding measures whether factual claims in the generated answer are supported
by evidence available to the workflow.

A factual claim may be classified as:

### Supported

The retrieved evidence directly supports the claim or supports a reasonable
synthesis required by the benchmark task.

### Partially supported

The available evidence supports part of the claim but not the entire material
claim.

### Unsupported

The claim cannot be justified from the evidence available to the workflow.

### Contradicted

The available evidence materially contradicts the claim.

Where feasible, grounding will be summarized using:

- number of factual claims;
- supported claims;
- partially supported claims;
- unsupported claims;
- contradicted claims;
- unsupported-claim rate.

The exact claim-segmentation procedure will be frozen before the full
benchmark.

## 5. Retrieval evidence

Retrieval quality is evaluated separately from answer correctness.

For each task, the benchmark records the chunks and documents returned by the
retrieval system.

Where reference evidence exists, evaluation may include:

- whether at least one required evidence source was retrieved;
- required-document recall;
- reference-evidence recall where locations can be matched reliably;
- number of irrelevant retrieved chunks where a defensible relevance judgment
  is available.

A generated answer can therefore be:

- correct despite weak retrieval;
- incorrect despite successful retrieval;
- grounded in retrieved evidence but incomplete;
- unsupported even when relevant evidence was retrieved.

These cases must not be collapsed into one score.

## 6. Abstention

Abstention is evaluated explicitly because some benchmark tasks are designed to
contain insufficient evidence.

Possible outcomes are:

### Correct abstention

The task is an insufficient-evidence task and the workflow appropriately states
that the available evidence is insufficient.

### Failed to abstain

The task is an insufficient-evidence task but the workflow provides a
substantive answer not justified by the corpus.

### Incorrect abstention

The task is answerable from the corpus but the workflow incorrectly refuses or
states that evidence is insufficient.

### Not applicable

The task is answerable and the workflow attempts an answer.

Abstention should be judged by behavior rather than exact refusal wording.

## 7. Conflicting-document tasks

For tasks containing conflicting, superseding, or context-dependent evidence,
a correct answer must identify or resolve the conflict according to the
human-validated reference answer.

A response that selects one conflicting statement without acknowledging a
material conflict should not receive full correctness credit unless the task
reference explicitly establishes why that source governs.

## 8. Workflow outcome

Each run receives one workflow outcome independent of answer correctness:

### completed

The workflow completed normally.

### completed_after_recovery

The workflow initially encountered a verification/retrieval problem but
completed through an allowed recovery path.

### resource_stopped

Execution stopped because a configured resource limit prevented continuation.

### tool_error

Execution could not complete because of a retrieval/tool/infrastructure error.

### failed

The workflow did not produce a valid final result for another documented
reason.

Failures remain part of the benchmark record.

## 9. Resource-efficiency measurements

Resource measurements are obtained from runtime logs rather than subjective
scoring.

The benchmark is expected to record:

- input tokens;
- output tokens;
- total provider tokens;
- LLM calls;
- retrieval/tool calls;
- retries;
- resource-limit events;
- budget utilization where applicable.

These values should be collected using provider/runtime accounting where
available.

## 10. Runtime measurements

Runtime measurements are also collected directly from the benchmark runner.

Expected measurements include:

- end-to-end latency;
- model-call latency where available;
- retrieval latency where available;
- stage-level latency for agentic workflows.

Timing boundaries must be defined consistently before the full benchmark.

## 11. Benchmark human adjudication

Some benchmark outcomes may require human judgment, particularly:

This benchmark adjudication is separate from the semi-structured interview
study. It is part of benchmark scoring and should not be described as the
qualitative interview component.

- partial correctness;
- grounding;
- ambiguous evidence;
- conflict resolution.

Where human adjudication of benchmark outputs is required:

1. use the frozen reference answer and evidence;
2. apply this rubric consistently across all conditions;
3. hide the condition label from the evaluator where practical;
4. record the raw judgment rather than only an aggregate score;
5. record reasons for ambiguous decisions.

A subset may be independently reviewed by a second evaluator if feasible.
Any agreement analysis will be reported as supporting information rather than
invented after observing results.

## 12. Model-assisted evaluation

An LLM evaluator may assist with scalable evaluation only if its procedure is
documented and validated against human judgments on a representative subset.

A model evaluator must not be treated as the benchmark gold standard by
default.

The evaluator should not receive information identifying whether an answer was
produced by B0, B1, or G1.

The exact evaluator, prompt, model, and validation procedure remain open until
the engineering phase.

## 13. Aggregation and reporting

The benchmark should report dimensions separately rather than creating one
arbitrary composite score.

Expected reporting includes:

- correctness distribution;
- task success rate;
- unsupported-claim rate;
- abstention outcomes;
- retrieval/evidence measures;
- workflow completion and recovery;
- failure counts;
- token/resource use;
- latency.

The primary comparison remains B1 versus G1.

B0 is an external reference and should not be used as the main causal estimate
of guardrail effects.

## 14. Items not yet frozen

Rubric version 0.1 does not yet freeze:

- claim segmentation method;
- exact automated correctness metric;
- exact grounding evaluator;
- exact retrieval relevance metric;
- number of human evaluators;
- size of any double-scored subset;
- inter-rater agreement statistic;
- final statistical tests;
- LLM evaluator model or prompt, if one is used.

These implementation decisions must be documented before the final benchmark.
