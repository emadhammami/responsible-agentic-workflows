# Experiment Protocol

**Project:** Responsible Agentic Workflows
**Study:** USN Master's Thesis
**Protocol version:** 0.3
**Status:** Working protocol

## 1. Study objective

This study investigates how selected guardrails affect the performance,
reliability, resource efficiency, and runtime behavior of LLM-based agentic
workflows for document-based knowledge work.

The technical component is evaluated as a **technical benchmark**. A later
semi-structured interview study provides the qualitative component of the
mixed-methods design.

## 2. Research questions

### RQ1 â€” Technical benchmark

How do selected guardrails affect the performance, reliability, and resource
efficiency of LLM-based agentic workflows in document-based knowledge work?

### RQ2 â€” Human and organizational evaluation

How do users and relevant stakeholders perceive the usefulness,
trustworthiness, risks, and adoption implications of guardrailed LLM-based
agentic workflows?

### RQ3 â€” Integration

How can technical benchmark results and stakeholder perceptions be combined
to identify conditions for responsible organizational adoption of LLM-based
agentic workflows?

## 3. Benchmark conditions

Three system conditions are planned.

### B0 â€” External reference baseline

The external reference baseline follows the official **LangChain 2-step RAG**
architecture. Retrieval is performed before answer generation. Concrete package
versions and shared retrieval/model settings will be frozen before the full
benchmark.

### B1 â€” Matched agentic baseline

The thesis workflow with the selected guardrails disabled.

### G1 â€” Guardrailed agentic workflow

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

Repeated runs may be used to characterize stochastic variability, but repeated
runs of the same task will not be treated as independent tasks.

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

The study is expected to begin with approximately 20 real policy/project
documents and may expand toward approximately 60 documents.

The architecture must support corpus expansion without requiring a change in
the experimental design.

Publication rights for the real documents will be assessed separately.
Restricted documents must not be committed to the public repository.

## 11. Decisions still open

Protocol version 0.3 intentionally does not yet freeze:

- exact LangChain package version and B0 implementation parameters;
- exact LLM/model version;
- embedding model;
- vector store;
- chunking strategy;
- retrieval top-k;
- prompt templates;
- resource limits;
- final benchmark size;
- repetition count;
- statistical tests;
- automatic/human evaluation implementation.

The scoring definitions for correctness, grounding, evidence, abstention, and
workflow outcomes are defined in docs/evaluation_rubric.md.

These decisions will be documented and frozen before the full benchmark.
