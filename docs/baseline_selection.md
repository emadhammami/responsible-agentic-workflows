# External Baseline Selection

**Decision:** B0 reference architecture  
**Selected approach:** LangChain 2-step RAG  
**Decision status:** Selected; implementation parameters not yet frozen

## 1. Purpose

B0 provides an external reference point for the technical benchmark.

It is not the primary causal comparison. The primary comparison remains the
matched agentic baseline B1 against the guardrailed workflow G1.

The purpose of B0 is to show how the evaluated systems compare with a
recognizable, established open-source RAG architecture rather than with a
deliberately simplified custom baseline.

## 2. Selection criteria

The external baseline should:

- be open source under a permissive license;
- be actively maintained;
- have official documentation;
- represent a recognizable RAG architecture;
- allow the same document corpus to be used;
- allow the same LLM and embedding model where technically possible;
- expose retrieval and generation behavior clearly enough for measurement;
- avoid unnecessary agentic or guardrail behavior;
- be reproducible using pinned package versions;
- require minimal thesis-specific modification.

## 3. Candidates considered

### LangChain

LangChain provides an official 2-step RAG architecture in which retrieval is
performed before generation.

Its documentation distinguishes:

- 2-step RAG;
- agentic RAG;
- hybrid RAG.

The 2-step architecture is described as simple and predictable, with high
control over execution.

This distinction maps directly to the thesis design because B0 should represent
a conventional RAG reference rather than another guardrailed or self-correcting
agent.

Repository: langchain-ai/langchain  
License: MIT

### Haystack

Haystack is a mature open-source framework with modular pipelines for RAG,
retrieval, agents, routing, and generation.

It is technically suitable, but its broader orchestration and agent facilities
introduce more framework behavior than is necessary for the external reference
condition.

Repository: deepset-ai/haystack  
License: Apache-2.0

### LlamaIndex

LlamaIndex is a mature open-source framework focused strongly on document
indexing, retrieval, query engines, RAG, and document agents.

Its standard VectorStoreIndex/query-engine pattern would also provide a
credible document QA baseline.

For this study, however, LangChain's explicit separation between 2-step,
agentic, and hybrid RAG provides a clearer methodological mapping to B0, B1,
and G1.

Repository: run-llama/llama_index  
License: MIT

## 4. Selected B0 architecture

B0 will follow the official LangChain 2-step RAG pattern:

    question
       |
       v
    retrieval
       |
       v
    relevant document chunks
       |
       v
    answer generation
       |
       v
    final answer

Retrieval occurs before generation.

B0 will not include:

- an autonomous planning loop;
- a critic or verifier;
- self-correction;
- conditional re-retrieval;
- guardrail-triggered revision;
- resource reservation logic.

These capabilities belong to the agentic and guardrailed conditions rather
than the external conventional-RAG reference.

## 5. Fair-comparison requirements

Where technically possible, B0 should use the same:

- real document corpus;
- benchmark tasks;
- LLM;
- model parameters;
- embedding model;
- chunking policy;
- retrieval top-k;
- vector-store data;
- execution environment;
- benchmark logger;
- evaluation procedure.

Framework-specific behavior that cannot be made identical must be documented.

The goal is not to make B0 artificially equivalent to B1/G1, but to prevent
irrelevant implementation differences from dominating the comparison.

## 6. Scientific role

The comparisons have different purposes.

### Primary comparison

B1 vs G1

This estimates the effect of adding the selected guardrails to an otherwise
matched agentic workflow.

### Supporting comparison

B0 vs B1 vs G1

This places the agentic systems relative to an established conventional RAG
reference.

No causal claim about guardrails will be based primarily on B0 vs G1 because
those conditions differ architecturally.

## 7. Decisions intentionally left open

This selection freezes the B0 architecture, but not yet its full experimental
configuration.

The following remain to be decided and pinned later:

- LangChain package version;
- exact LLM;
- embedding model;
- vector store;
- document loader;
- chunking parameters;
- retrieval top-k;
- generation prompt;
- token/output limits;
- timeout behavior.

These parameters will be selected before the engineering pilot and frozen
before the full benchmark.