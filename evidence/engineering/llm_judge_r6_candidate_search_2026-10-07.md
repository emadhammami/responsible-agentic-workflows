# R6 local LLM judge candidate search — 2026-10-07

Status: PRE-QUALIFICATION SHORTLIST. No weight download or candidate inference preceded this search record. Primary benchmark answers, primary judge inputs/results and expert outcomes were not opened for this mission.

## Search scope and decision rule

Twelve current targeted discovery queries were followed by official model-card, exact Ollama-tag and runtime-documentation checks. Fifteen principal sources are indexed below. Published capabilities screen for instruction following, reasoning, document comparison, JSON control, family independence and workstation feasibility; they do not establish judge qualification. Leaderboard rank is not a selection gate. Only the same frozen R6 atomic qualification can establish eligibility.

Generator: Qwen3.8 27B. Direct Qwen models and Qwen-backbone distills are excluded. One serious candidate per architectural family is shortlisted, with known training-provenance caveats explicitly recorded. Different families/vendors do not guarantee statistically independent judgment errors.

Observed hardware/runtime: RTX 5090 Laptop GPU, 24,463 MiB total VRAM; approximately 599 MiB used before qualification; Ollama 0.34.0; no resident Ollama model. The supplied workstation has 64 GB physical RAM; the OS-visible allocation is approximately 54.9 GiB, with 46.9 GiB available. Model storage has approximately 392.5 GiB free. The existing six local model tags, including every generator tag, embedding model and gpt-oss:20b, are preserved.

Memory ranges below are planning estimates, **not measurements**: decimal GB downloads differ from GiB runtime residency, and cache/buffer requirements depend on architecture/context/backend. A common 32,768-token configured context will be qualified. Automatic CPU offload is allowed. Actual placement and measured response latency are recorded during R6. No full advertised context window is claimed to fit in 24 GB VRAM.

## Frozen shortlist (all six will be attempted sequentially)

| Order / exact tag | Family / vendor | Parameters (total / active) | Quantization / weight download | Native context | License | Estimated 32K memory and speed | Task suitability / decision |
|---|---|---|---|---|---|---|---|
| C01 `gpt-oss:20b` | GPT-OSS / OpenAI | 20.9B / approximately 3.6B | MXFP4; 13.79 GB; already installed | 131,072 | Apache 2.0 | Approximately 16–21 GiB VRAM; 20–30 GiB host working allocation. Fast MoE decode expected; reasoning duration can dominate. | Native structured-output/Harmony support and configurable reasoning; independently requalify, without credit for historical R4. [Card](https://huggingface.co/openai/gpt-oss-20b), [Ollama](https://ollama.com/library/gpt-oss:20b). |
| C02 `glm-4.7-flash:q4_K_M` | GLM / Z.ai | Approximately 30–31B / 3B | Q4_K_M; 19.02 GB | 202,752 | MIT | Approximately 20–24 GiB GPU with possible cache/layer offload; host requirement could reach 30–50 GiB. Active-3B MoE should decode efficiently, but MLA/cache implementation must be observed. | Current reasoning/instruction and agentic capability, distinct non-Qwen backbone. Ollama exceeds its documented minimum version. Document-comparison suitability remains unproven until R6. [Card](https://huggingface.co/zai-org/GLM-4.7-Flash), [Ollama](https://ollama.com/library/glm-4.7-flash:q4_K_M). |
| C03 `phi4-reasoning:14b-plus-q8_0` | Phi-4 / Microsoft | 14.7B dense / all active | Q8_0; 17.06 GB | 32,768 | MIT | Approximately 23–27 GiB GPU demand including FP16 KV/buffers; a small offload may be needed. Approximately 25–40 GiB host working allocation. Dense decode expected to be slower than small-active MoEs. | Reasoning plus SFT/RL; Q8 reduces quantization loss while remaining feasible. Official evaluation is reasoning focused, not LLM judging. Its o3-mini teacher creates a provenance caveat when paired with OpenAI. Native Ollama thinking separation may be absent; the common structured protocol is still applied. [Card](https://huggingface.co/microsoft/Phi-4-reasoning-plus), [Ollama](https://ollama.com/library/phi4-reasoning:14b-plus-q8_0). |
| C04 `gemma4:26b-a4b-it-q4_K_M` | Gemma 4 / Google DeepMind | 25.8B / approximately 4B | Q4_K_M; 17.99 GB | 262,144 | Apache 2.0 | Approximately 20–26 GiB GPU demand; approximately 25–40 GiB host allocation, possible small offload. Sparse activation/shared-cache architecture suggests practical local decode. | New family generation with native system-role support and configurable reasoning. This is not the rejected Gemma3 12B checkpoint. Select the explicit non-MTP GGUF tag rather than mutable default, cloud or MLX variants. [Card](https://ai.google.dev/gemma/docs/core/model_card_4), [Ollama](https://ollama.com/library/gemma4:26b-a4b-it-q4_K_M). |
| C05 `nemotron-3-nano:30b-a3b-q4_K_M` | Nemotron hybrid MoE / NVIDIA | 31.6B GGUF metadata (approximately 30B advertised) / 3.5B | Q4_K_M; 24.27 GB | 1,048,576 | NVIDIA Nemotron Open Model License | Weights alone approximately 22.6 GiB; expect 22–24 GiB GPU residency plus modest CPU offload, approximately 30–45 GiB host allocation. Small active parameter count supports practical decode, but memory pressure is the principal risk. | Trained from scratch, hybrid Mamba/attention architecture; Qwen-generated training data is disclosed, so this is non-Qwen-backbone diversity with a generator-provenance caveat, not completely isolated training lineage. [Card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16), [Ollama](https://ollama.com/library/nemotron-3-nano:30b-a3b-q4_K_M). |
| C06 `deepseek-r1:8b-llama-distill-q8_0` | DeepSeek-R1 distill / Llama 3.1 backbone, DeepSeek + Meta | Approximately 8B dense / all active | Q8_0; 8.54 GB | 131,072 | DeepSeek MIT plus original Llama 3.1 terms | Approximately 13–17 GiB VRAM; approximately 18–28 GiB host allocation. Small dense model expected to be practical, although reasoning length affects latency. | Explicit Llama-based reasoning distill gives compact backbone diversity. The generic updated `deepseek-r1:8b` can be Qwen based and is not substituted. Model-card advice about temperature/system prompts is not used to customize R6; structured comparison performance must pass the common contract. [Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B), [Ollama](https://ollama.com/library/deepseek-r1:8b-llama-distill-q8_0). |

Exact registry manifests and byte sizes were verified with manifest-only requests, before any weight pull. Full digests are frozen in `registry_manifests.json` in the separate qualification audit directory; short identifiers are C01 17052f91a42e, C02 4475827791a2, C03 ecd8f64ff877, C04 5571076f3d70, C05 b725f1117407 and C06 744d1ee47c3d. Registry pinning prevents an unnoticed tag change during qualification.

## Exclusions and alternatives considered

- Previously rejected Mistral candidates, Granite4 32B-A9B-H, Gemma3 12B and OLMo-3 7B Instruct are not downloaded or recycled. GPT-OSS is included solely as the requested incumbent for an equal R6 retest; history does not count as R6 qualification.
- Qwen, QwQ and DeepSeek-R1 Qwen distills (including the newer Qwen3-backed 8B variant) fail the generator-family preference; no broad `8b` alias is used.
- Llama 3.3 70B / 70B distills and Llama 4 large MoEs are not prioritized: substantial CPU weight residency would make this workstation a poor fit for repeated long document comparisons. The exact Llama-3.1-backed 8B distill is the compact serious Llama-family option. [Llama model card](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
- Larger GLM Air/flagship models, DeepSeek flagship MoEs and GPT-OSS 120B are not practical 24-GB primary choices; no model is downloaded only because it tops an external leaderboard.
- Gemma4 31B dense, Nemotron 4B and base Phi4 are plausible alternatives but are not added to the six-model shortlist. The selected checkpoints balance reasoning capacity, family coverage and memory. Extra variants would create an undocumented adaptive search after results.
- Cloud tags, paid inference endpoints, MLX-only artifacts, tools/web browsing and external scoring calls are excluded.

## Principal current sources

1. [OpenAI GPT-OSS official card](https://huggingface.co/openai/gpt-oss-20b).
2. [Exact GPT-OSS Ollama tag](https://ollama.com/library/gpt-oss:20b).
3. [Z.ai GLM-4.7-Flash official card](https://huggingface.co/zai-org/GLM-4.7-Flash).
4. [Exact GLM Ollama tag](https://ollama.com/library/glm-4.7-flash:q4_K_M).
5. [Microsoft Phi-4-reasoning-plus official card](https://huggingface.co/microsoft/Phi-4-reasoning-plus).
6. [Exact Phi Q8 Ollama tag](https://ollama.com/library/phi4-reasoning:14b-plus-q8_0).
7. [Google Gemma 4 official card](https://ai.google.dev/gemma/docs/core/model_card_4).
8. [Exact Gemma 4 GGUF Ollama tag](https://ollama.com/library/gemma4:26b-a4b-it-q4_K_M).
9. [NVIDIA Nemotron 3 Nano official card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16).
10. [Exact Nemotron Q4 Ollama tag](https://ollama.com/library/nemotron-3-nano:30b-a3b-q4_K_M).
11. [DeepSeek official Llama-distill card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B).
12. [Exact non-Qwen DeepSeek tag](https://ollama.com/library/deepseek-r1:8b-llama-distill-q8_0).
13. [Meta Llama 3.1 official card](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).
14. [Ollama structured-output documentation](https://docs.ollama.com/capabilities/structured-outputs).
15. [Ollama thinking-control documentation](https://docs.ollama.com/capabilities/thinking).

## Next phase boundary

Use the exact R5 frozen atomic prompt/cases/gold and validator semantics. Freeze the R6 gates, common decoding policy, technical compatibility rules, call order, class-coverage check and pair ranking before any qualification call. All six receive the same 9 cases × 2 repetitions. No primary 270-run judging is authorized by this mission.
