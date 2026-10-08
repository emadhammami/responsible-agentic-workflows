# R9-P0 NVIDIA provider-access smoke protocol

Frozen prospectively before any R9 API inference.

Purpose: verify basic hosted inference access, not judge quality.

Endpoint:
https://integrate.api.nvidia.com/v1/chat/completions

Ordered candidates:
1. nvidia/nemotron-3-ultra-550b-a55b
2. deepseek-ai/deepseek-v4.1-flash

For each candidate:
- one POST only
- messages: [{"role":"user","content":"Reply with the word READY."}]
- temperature: 0
- top_p: 1
- max_tokens: 128
- stream: false
- timeout: 120 seconds
- no retries
- no substitution or fallback

Record HTTP status, latency, presence of a chat completion
response and final-content length. Never log credentials.

Do not send benchmark data, qualification cases, gold labels,
expert responses, or document evidence.

This operational check does not qualify either judge.
No primary judging is authorized.

No paid API or billing activation is authorized.
