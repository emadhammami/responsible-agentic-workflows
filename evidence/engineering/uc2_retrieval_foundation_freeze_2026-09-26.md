# UC2 Retrieval Foundation Freeze

Date: 2026-09-26

Accepted retrieval-active documents: 17
Excluded: DOC054
Canonical chunks: 293
Embedding dimensions: 2560
Embedding model: qwen3-embedding:4b-q4_K_M
Retrieval backend: exact cosine
Retrieval config: UC2-QWEN3-EMBED4B-EXACT-COSINE-v0.1

Semantic qualification: PASS
Observed: TOP10=16, TOP5=16, TOP3=16, STABLE_TOP1=17
Frozen gate: 15/13/9/15

Scope contract SHA256: b2e94ed40ef91c9ad74aeb250428bb6909cd1a54ac8e4fb211a582b7f4c39cec
Benchmark scope SHA256: 87f8de97ee51645ef140398c02ce94f047d5107412d17e08139551353d3d268d
Frozen embedding metadata SHA256: 1901048651cb93b4b52f9529a9706c0ec81ea0ded9f92ea0fd48b88e1032618e
Canonical embeddings SHA256: 621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f
Retrieval config SHA256: 6df4b73e262261e907f8e6e227619be1b996ced6b688eca478c7f56748acc169

The freeze establishes cryptographic identity of the qualified canonical
artifacts; it does not claim byte-reproducible embedding rematerialization.

No corpus membership change, re-embedding, benchmark task construction,
benchmark top_k selection, or benchmark execution occurred.

UC2_RETRIEVAL_FOUNDATION_FROZEN=YES
BENCHMARK_STARTED=NO
