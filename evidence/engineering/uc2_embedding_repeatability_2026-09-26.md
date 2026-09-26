# UC2 Embedding Repeatability Diagnostic

Date: 2026-09-26
Phase: UC2-P6B-R

Canonical Run-1 embeddings SHA256:
621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f

Run-2 embeddings SHA256:
1c86de0a9d648821318b4b425767fbee5096f9b3fcc4d5ba48fb4ca66e3e7d89

Repeatability result SHA256:
b17322ddaef5c18a681a5d8540def7a7f0392efcf3ef3fa2a0be3a47244bdf3d

Both runs used:
- 293 frozen chunks
- qwen3-embedding:4b-q4_K_M
- frozen model digest
- Ollama 0.34.0
- batch size 32
- 2560-dimensional float32 vectors
- identical retrieval configuration

Run-1 remains the canonical embedding artifact.

This diagnostic is descriptive engineering evidence. No new or relaxed
post-hoc acceptance threshold is introduced. Byte-level equality is not
required for acceptance. Retrieval qualification remains pending the
prospectively frozen identity and semantic diagnostic protocols.

EMBEDDING_REPEATABILITY_DIAGNOSTIC=COMPLETE
CANONICAL_RUN1_UNCHANGED=YES
RETRIEVAL_QUALIFICATION_STARTED=NO
RETRIEVAL_FOUNDATION_FROZEN=NO
BENCHMARK_STARTED=NO
