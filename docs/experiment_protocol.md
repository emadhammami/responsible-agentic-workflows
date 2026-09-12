# Experiment Protocol

**Project:** Responsible Agentic Workflows
**Study:** USN Master's Thesis
**Protocol version:** 0.5
**Status:** Working protocol

## 1. Study objective

This study investigates how selected guardrails affect the performance,
reliability, resource efficiency, and runtime behavior of LLM-based agentic
workflows for document-based knowledge work.

The technical system is evaluated through a **technical benchmark**.

Although many benchmark measurements are numerical, the thesis does not label
the benchmark as the quantitative component of the research design. Accuracy,
task success, grounding, reliability, resource use, model calls, and latency
are reported as **benchmark measurements and benchmark results**.

The semi-structured interview study is used to collect the qualitative and,
where structured rating items are included, quantitative empirical interview
data. Open-ended responses provide qualitative data for thematic analysis.
Structured rating items may provide descriptive quantitative interview data.

The technical benchmark findings and the interview findings will subsequently
be considered together when discussing responsible organizational adoption.

## 2. Research questions

### RQ1 - Technical benchmark

How do selected guardrails affect the performance, reliability, and resource
efficiency of LLM-based agentic workflows in document-based knowledge work?

### RQ2 - Human and organizational evaluation

How do users and relevant stakeholders perceive the usefulness,
trustworthiness, risks, and adoption implications of guardrailed LLM-based
agentic workflows?

### RQ3 - Integration

How can technical benchmark results and stakeholder perceptions be combined
to identify conditions for responsible organizational adoption of LLM-based
agentic workflows?

## 3. Benchmark conditions

Three system conditions are planned.

### B0 - External reference baseline

The external reference baseline follows the official **LangChain 2-step RAG**
architecture. Retrieval is performed before answer generation. Concrete package
versions and shared retrieval/model settings will be frozen before the full
benchmark.

### B1 - Matched agentic baseline

The thesis workflow with the selected guardrails disabled.

### G1 - Guardrailed agentic workflow

The same core workflow as B1 with the selected guardrails enabled.

The primary scientific comparison is:

**B1 vs G1**

B0 provides an external reference point.

## 4. Controlled components

For B1 and G1, the following should remain the same unless a guardrail
necessarily changes a component:

- document corpus;
- benchmark tasks;
- LLM and model parameters;
- retrieval system;
- embedding model;
- chunking;
- retrieval settings;
- prompts outside guardrail-specific instructions;
- execution environment;
- logging;
- evaluation procedure.

Any unavoidable differences must be documented.

## 5. Guardrail families

The initial design considers three guardrail families:

1. **Evidence grounding**
   - Answers should be supported by retrieved evidence.
   - The workflow may abstain when evidence is insufficient.

2. **Verification / critic**
   - A draft answer is checked against supporting evidence before release.
   - Controlled retrieval or revision may occur when verification fails.

3. **Resource control**
   - Model calls, retries, token use, and resources required by later workflow
     stages are controlled and recorded.

The exact implementations will be frozen before the full benchmark.

## 6. Benchmark task taxonomy

The expected task categories are:

1. direct retrieval;
2. within-document reasoning;
3. cross-document reasoning;
4. insufficient-evidence / abstention;
5. conflicting-document reasoning, if supported by the corpus.

Final questions, reference answers, and reference evidence must be
human-verified.

The primary benchmark task-set design is frozen separately in
`benchmark/task_set_plan.json`.

The primary benchmark contains 30 tasks across three use cases, with 10 tasks
per use case. Each use case contains 3 direct-retrieval, 3 within-document
reasoning, 2 cross-document reasoning, and 2 insufficient-evidence tasks.

Conflicting-document reasoning remains supported by the task schema but is not
a required category in the balanced primary benchmark because a genuine
document conflict cannot be assumed across all three use cases.

## 7. Benchmark dimensions

### Task performance

- answer correctness;
- task success;
- completeness where relevant.

### Reliability and grounding

- evidence correctness;
- evidence relevance;
- unsupported claims;
- workflow completion;
- verification completion;
- recovery behavior;
- correct and incorrect abstention;
- execution failures.

### Resource efficiency

- input tokens;
- output tokens;
- total tokens;
- LLM calls;
- retrieval/tool calls;
- retries;
- budget utilization where applicable.

### Runtime performance

- end-to-end latency;
- stage-level latency where available.

The benchmark will report multiple dimensions rather than reducing system
performance to one metric.

## 8. Experimental unit

The primary experimental unit is one benchmark task.

The same task should be evaluated across comparable system conditions.

Each task-condition combination will be executed three times to characterize
run-to-run variability. Repeated runs of the same task are repetitions and will
not be treated as independent tasks.

With 30 primary benchmark tasks, three system conditions (B0, B1, and G1), and
three repetitions, the planned primary benchmark contains 270 runs.

## 9. Research integrity rules

Before the full benchmark:

- freeze the benchmark task set;
- freeze reference answers and evidence;
- freeze evaluated configurations;
- prevent access to reference answers during execution;
- preserve failed and interrupted runs;
- record configuration and version information for every run;
- do not selectively remove unfavorable results;
- do not intentionally weaken B0 or B1;
- separate engineering-pilot results from final benchmark results;
- document post-freeze corrections transparently.

## 10. Document corpus

The primary benchmark is planned across three real document-based use cases:
UC1, UC2, and UC3.

UC1 uses the frozen OptFor-EU forest-policy corpus. UC2 and UC3 will be selected
and documented as distinct real organizational or knowledge-work contexts
before their benchmark tasks are frozen.

The overall corpus is expected to contain approximately 60 real documents,
subject to documented source availability and inclusion criteria. Corpus size
will not be adjusted in response to benchmark performance.

The architecture must support the three use cases without changing the core
B0, B1, and G1 comparison.

Publication rights for the real documents will be assessed separately.
Restricted documents must not be committed to the public repository.

## 11. Decisions still open

Protocol version 0.5 intentionally does not yet freeze:

- exact LangChain package version and B0 implementation parameters;
- exact LLM/model version;
- embedding model;
- vector store;
- chunking strategy;
- retrieval top-k;
- prompt templates;
- resource limits;
- final benchmark task questions, reference answers, and evidence;
- UC2 and UC3 corpus selection and retrieval artifacts;
- statistical tests;
- automatic/human evaluation implementation.

The scoring definitions for correctness, grounding, evidence, abstention, and
workflow outcomes are defined in docs/evaluation_rubric.md.

These decisions will be documented and frozen before the full benchmark.

The selected values will be represented in a machine-readable benchmark
configuration conforming to `benchmark/config/benchmark_config.schema.json`.
Final benchmark execution will require a configuration whose status is
explicitly `frozen`.
