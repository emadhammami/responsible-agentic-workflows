# LLM Judge Candidate Qualification Record v1

Date: 2026-10-06

Status: FROZEN BEFORE ANY PRIMARY BENCHMARK JUDGE EXECUTION

## Purpose

This record documents all LLM-judge qualification attempts performed before
either judge was allowed to evaluate any of the 270 primary benchmark outputs.

The purpose is to prevent undocumented model shopping, result-driven prompt
tuning, or selective omission of failed judge candidates.

No candidate described below had access to primary benchmark outputs during
qualification.

## Generator independence

Primary benchmark generator:

- family: Qwen
- model: qwen3.8-27b-48k:latest

Judge candidates are required to be independent of the benchmark generator.
Different model families are preferred for the two final judges.

## Qualification history

### R1 — initial synthetic qualification

Candidates:

- GPT-OSS 20B
- Mistral Small 3.2 24B

Result:

- schema: 32/32
- synthetic gold: 28/32
- repeatability: 16/16
- overall gate: FAIL

Observed issues were limited to synthetic rubric interpretation.
No benchmark outputs were inspected.

### R2 — rubric-dimension disambiguation

Same candidates.

Result:

- schema: 32/32
- synthetic gold: 30/32
- repeatability: 16/16
- overall gate: FAIL

No benchmark outputs were inspected.

### R3 — claim-segmentation diagnostic qualification

Same candidates.

Result:

- schema: 36/36
- synthetic gold: 26/36
- repeatability: 18/18
- overall gate: FAIL

Mistral Small 3.2 was rejected as a final judge candidate after repeated
semantic-rubric failures.

No benchmark outputs were inspected.

### R4 — frozen-direction atomic qualification

Candidates:

- J1 candidate: GPT-OSS 20B
  - Ollama ID: 17052f91a42e

- J2 candidate: Granite 4 32B-A9B-H
  - Ollama ID: 2f8a7367d441

R4 deliberately removed ambiguous claim-splitting cases and tested atomic
correctness, abstention, and grounding semantics.

Predeclared gate:

- exact structured schema on every call;
- exact synthetic expected semantic labels on every call;
- identical decisive outcome across the two repetitions;
- no prompt tuning after observing R4 results.

Observed result:

- calls: 36/36
- schema: 36/36
- synthetic gold: 15/36
- repeatability: 15/18
- GPT-OSS: 13/18 gold
- Granite 4: 2/18 gold
- overall atomic qualification: FAIL

Decision:

- GPT-OSS 20B is NOT qualified as a final benchmark judge.
- Granite 4 32B-A9B-H is NOT qualified as a final benchmark judge.
- Mistral Small 3.2 remains NOT qualified.

## Candidate-selection rule from this point forward

Future candidate models MUST be evaluated without inspecting primary benchmark
judge outcomes.

The qualification contract from this point forward is:

1. use synthetic cases only;
2. do not expose any of the 270 benchmark outputs;
3. use the same correctness, abstention, and grounding semantics;
4. use atomic, unambiguous qualification cases;
5. use structured JSON output;
6. use deterministic inference settings where supported;
7. perform two independent repetitions of every qualification case;
8. do not tune the prompt for an individual candidate after seeing its result;
9. retain failed candidates and their results in the methodology record;
10. only candidates passing the predeclared qualification gate may become
    final LLM Judge 1 or LLM Judge 2.

A final judge must also have enough context capacity for the frozen blinded
evaluation package.

## Primary benchmark protection

At the time this record is frozen:

- primary benchmark executions: 270 complete;
- expert-human validation subset: 27 already frozen;
- LLM benchmark judgments completed: 0;
- statistical outcome analysis started: NO;
- benchmark-result-driven judge tuning: NO.

The expert-human 27-output validation workflow is independent of judge
qualification and may proceed in parallel.

## Interpretation

Synthetic qualification is an engineering/reliability gate, not benchmark
outcome analysis.

Failure of a candidate is not evidence about B0, B1, or G1 and must not be
used to modify benchmark conditions, tasks, outputs, or expected research
claims.
