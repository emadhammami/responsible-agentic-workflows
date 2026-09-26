# UC2 Embedding / Retrieval Configuration Freeze

Date: 2026-09-26
Phase: UC2-P6A

Retrieval config:
`UC2-QWEN3-EMBED4B-EXACT-COSINE-v0.1`

Config SHA256:
`6df4b73e262261e907f8e6e227619be1b996ced6b688eca478c7f56748acc169`

Frozen input:
- materialization freeze: 04ac8a17aca7bd7c5f930e6efab551fafda366f1ee46cd13b4b0bf4de15df00a
- canonical chunks: b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2
- chunk count: 293

The embedding/retrieval foundation inherits the existing UC1/UC3 technical
contract without UC2-specific tuning.

Model: qwen3-embedding:4b-q4_K_M
Digest: df5bd2e3c74cd8d069d21dc038f1b359fcdc9458fce1c99bd43c9eb1518ff907
Ollama: 0.34.0
Dimensions: 2560
Normalized: true
Truncate: false
Index: NumPy 2.5.3 flat-exact cosine float32

Benchmark top_k is intentionally NOT frozen by this configuration.

EMBEDDING_CONFIG_FROZEN=YES
TOP_K_FROZEN=NO
EMBEDDINGS_STARTED=NO
RETRIEVAL_DIAGNOSTIC_STARTED=NO
BENCHMARK_STARTED=NO
