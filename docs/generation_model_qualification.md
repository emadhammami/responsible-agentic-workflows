# Generation Model Qualification

**Status:** Pre-specified engineering qualification before model inference

## Purpose

The benchmark requires one generation-model configuration to be used
consistently across B0, B1, and G1.

Model qualification is an engineering step performed before final benchmark
execution. Frozen benchmark tasks, reference answers, and reference evidence
must not be used to select or tune the generation model.

## Local candidate

The local Ollama inventory contains two Qwen generation tags:

- `qwen3.8-27b-48k:latest`
- `qwen3.8:27b`

Both tags resolve to the same base model blob:

`sha256-f5f1dd8920d417aac2718b0bda3403da274301efdd6760b4f0f4b864ff2ad57d`

They therefore represent the same underlying model weights rather than two
independent generation models.

The 48K tag is the qualification candidate because its local configuration
explicitly fixes the context window to 49,152 tokens.

Candidate identity:

- provider: Ollama
- Ollama version: 0.34.0
- model tag: `qwen3.8-27b-48k:latest`
- tag digest:
  `a68eeb5701b0a627f513a134f7ec029477a04b66a4605b32e27917ac93bd67a3`
- base model blob:
  `sha256-f5f1dd8920d417aac2718b0bda3403da274301efdd6760b4f0f4b864ff2ad57d`
- parameter size: 27.3B
- quantization: Q4_K_M
- configured context: 49,152 tokens
- model-reported native context: 262,144 tokens

The native maximum context is not treated as the benchmark context. The
configured 49,152-token context is the candidate execution context.

## Qualification configuration

The first qualification attempt will use:

- `num_ctx = 49152`
- `temperature = 0`
- `seed = 20260912`
- `num_predict = 1024`
- `thinking = false`
- local Ollama only
- no cloud model or paid API

`thinking = false` is tested first because the thesis evaluates explicit
workflow-level planning, execution, verification, and resource control.
Disabling model-internal thinking makes those workflow stages and their
resource costs easier to interpret.

Thinking mode will not be tested merely to search for a better benchmark
score. It will be considered only if the pre-specified non-thinking
configuration fails functional qualification.

## Qualification material

Qualification prompts will be synthetic engineering fixtures created
independently of UC1 benchmark tasks.

They must not contain or reproduce:

- T001-T010 questions;
- UC1 reference answers;
- UC1 reference-evidence passages;
- benchmark results.

Synthetic prompts may test generic policy-document behavior but must use
invented facts and document names.

## Functional gates

The candidate must pass all of the following gates.

### Q1 - Grounded extraction

Given a short synthetic source containing explicit facts, the model must return
the requested facts without replacing them with invented values.

### Q2 - Insufficient evidence

Given a synthetic source that does not contain the requested fact, the model
must state that the information cannot be determined from the supplied
evidence rather than fabricate a substantive answer.

### Q3 - Cross-document synthesis

Given two synthetic documents containing complementary information, the model
must combine the relevant facts needed to answer the question.

### Q4 - Structured output

When instructed to return a small JSON object with an exact schema, the model
output must parse as JSON and contain the required keys and expected values.

### Q5 - Thinking disabled

The qualification call must explicitly request non-thinking generation. The
response must not expose a separate model reasoning trace.

### Q6 - Local execution identity

After loading the candidate:

- Ollama must report context 49,152;
- the model must remain the expected candidate tag;
- execution must remain local;
- GPU placement must be recorded.

Full GPU placement is preferred for stable local execution. Any CPU offload
must be documented before the model configuration is frozen.

## Repetition rule

Each synthetic functional fixture will be run twice using the same
qualification configuration.

A gate passes only if both repetitions satisfy its functional requirement.

The repetitions are engineering checks, not benchmark repetitions and not
scientific benchmark results.

## Measurements recorded

For each qualification call, record where available:

- prompt token count;
- generated token count;
- total duration;
- prompt-evaluation duration;
- generation duration;
- finish state;
- whether a separate thinking field was returned.

These measurements are engineering diagnostics only.

No candidate will be selected because it happens to have lower latency or
token use on these synthetic fixtures.

## Decision rule

If the candidate passes all functional gates and can execute stably with the
specified local configuration, it is eligible to be frozen as the generation
model for B0, B1, and G1.

If a gate fails:

1. preserve the failure;
2. identify whether the cause is model capability, API configuration, or the
   engineering fixture;
3. do not use frozen benchmark tasks for diagnosis;
4. document any revised qualification configuration before retesting.

The benchmark model will not be changed in response to later benchmark
performance.

## Current boundary

- UC1 corpus: frozen.
- UC1 retrieval: frozen.
- UC1 tasks: frozen.
- Generation model: not yet frozen.
- B0/B1/G1 benchmark execution: not started.
