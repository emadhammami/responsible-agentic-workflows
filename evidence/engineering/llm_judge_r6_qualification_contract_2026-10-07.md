# Prospective R6 local judge qualification contract — 2026-10-07

Status: FROZEN BEFORE MODEL ACQUISITION OR CANDIDATE INFERENCE. This contract and the candidate-search record are committed together before execution. No primary benchmark judging is authorized.

## Scope and immutable atomic materials

Qualification uses exactly **9 frozen R5 atomic cases, 2 repetitions per candidate, 18 calls per candidate**. All six shortlisted candidates receive the same prompt, cases, gold labels, serialization, parser, scoring and acceptance gates. Historical qualification results confer no eligibility.

The only judgment inputs are the following files from `/tmp/t5g6_lightweight_judge_atomic_qualification_r5`, copied byte-for-byte into the separate R6 execution capsule after the prospective commit:

| Material | SHA256 |
|---|---|
| `prompt.txt` | `c57ad42fcef1e6382dd2b72572898a6fd21ae780bd2e9189467d6512dfeb913c` |
| `cases.json` | `b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2` |
| R5 `run.py`, static validator provenance only | `250af63eba5bec19666923affd466736dc3abe0cd5e85400040c08ccdbd33a90` |

R5 `run.py` must never be executed or imported. Its pure `valid` function is extracted using the Python AST, preserving its validation semantics. The interrupted R6 draft must not be executed. The new harness must have an explicit atomic-input allowlist and no path capable of reading primary benchmark answers/results or expert responses.

Correctness uses reference answer and reference evidence. Grounding uses only retrieved evidence and only claims actually asserted. Abstention uses the frozen four-class definition. Pure abstention has an empty claim list. Prompt meaning, text, cases, gold labels and order cannot be rewritten, corrected or tuned after results.

Frozen case order and gold signatures:

| Case | Correctness | Abstention | Ordered grounding labels |
|---|---:|---|---|
| A01 | 2 | not_applicable | SUPPORTED |
| A02 | 1 | not_applicable | SUPPORTED |
| A03 | 0 | not_applicable | CONTRADICTED |
| A04 | 2 | correct_abstention | empty |
| A05 | 0 | failed_to_abstain | UNSUPPORTED |
| A06 | 0 | incorrect_abstention | empty |
| A07 | 2 | not_applicable | PARTIALLY_SUPPORTED |
| A08 | 2 | not_applicable | UNSUPPORTED |
| A09 | 2 | not_applicable | CONTRADICTED |

## Frozen candidate order and identities

All six are attempted sequentially, with no concurrent model inference. First run A01–A09 as repetition 1, then A01–A09 as repetition 2. No adaptive shortlist expansion, substitutions or early stopping based on observed judgments.

| Order | Exact Ollama tag | Family | Pinned registry manifest SHA256 |
|---|---|---|---|
| C01 | `gpt-oss:20b` | GPT-OSS | `17052f91a42e97930aa6e28a6c6c06a983e6a58dbb00434885a0cf5313e376f7` |
| C02 | `glm-4.7-flash:q4_K_M` | GLM | `4475827791a269b02c8ec49b1c3bc1abb5846bacf3fae015b75d33986322d8f6` |
| C03 | `phi4-reasoning:14b-plus-q8_0` | Phi-4 | `ecd8f64ff87733b8c8eff20e0faddea21c3f9645bac6c74a2940c09a219eb410` |
| C04 | `gemma4:26b-a4b-it-q4_K_M` | Gemma 4 | `5571076f3d70050487b26b341705799e0ab29b808164f90d20d4cf84f699d251` |
| C05 | `nemotron-3-nano:30b-a3b-q4_K_M` | Nemotron | `b725f11174073334edd0c2ff396b8d4e66d7dab22a5a63717ccad5a08a270cf1` |
| C06 | `deepseek-r1:8b-llama-distill-q8_0` | Llama / DeepSeek-R1 distill | `744d1ee47c3d56281edaa5747df5e44f892b9f6ff66c1101ee4bc73725feb6a1` |

Exact remote manifests were retrieved without weights. A changed tag/digest is an identity failure, not permission to silently test a replacement. Model metadata and compatibility settings are archived before that candidate's first call.

## Identical request and decoding policy

Each independent request has exactly two messages: the frozen system prompt, then the following user object serialized with Python `json.dumps` using its default options and insertion order:

```python
{"evaluation_id": cid, "question": q, "generated_output": g,
 "reference_answer": r, "reference_evidence": [{"text": re}],
 "retrieved_evidence": [{"text": ev}]}
```

Gold labels, repetition, model identity and previous judgments are never included in the messages. There is no conversation history, tool use, browsing, retrieval augmentation or external scoring. The only inference endpoint is local Ollama on loopback; cloud/remote model metadata is rejected.

Common settings for every candidate:

```json
{
  "temperature": 0,
  "top_p": 1,
  "top_k": 0,
  "seed": 20260912,
  "num_ctx": 32768,
  "num_predict": 8192,
  "num_thread": 12,
  "repeat_penalty": 1
}
```

`stream=false`, `keep_alive="10m"`, per-call timeout 600 seconds. Retain native model templates and stop sequences; archive them. Automatic CPU offload is permitted without changing server-wide configuration. No speculative variant or cloud tag substitution.

A common JSON Schema constrains the six required root fields and the three required claim fields, types, enums and absence of extra properties. It must not constrain a case's expected score, labels, claim count or gold answer. This is a prospectively declared R6 transport improvement over R5's generic JSON mode; semantic instructions and the R5 validator/scoring remain unchanged. [Ollama structured-output documentation](https://docs.ollama.com/capabilities/structured-outputs).

### Prospective technical thinking compatibility

The sole model-specific interface adjustment is derived from capability metadata before its first qualification call:

- GPT-OSS uses `think="high"`, because its native API accepts named reasoning effort.
- Other models advertising the `thinking` capability use `think=true`.
- Models without that capability omit `think`; native template behavior remains in place.

These rules are identical for applicable architectures and are not selected using outcomes. Record the actual setting before execution. Do not change it after observing failures. Thinking-channel content is retained in raw telemetry but is not parsed as the final judgment. [Ollama thinking-control documentation](https://docs.ollama.com/capabilities/thinking).

No semantic inference retries, prompt repairs, extra warm-up judgments or result-driven decoding changes. Each scheduled call counts once, including HTTP errors, timeouts, malformed outputs and budget truncation. A technically unavailable candidate is nonqualified; no silent rerun under altered settings. Downloads may resume interrupted transport without adding qualification calls.

## Identical parser, validator and scoring

Parse the whole `message.content` as JSON. JSON whitespace is permitted; markdown fences, prefixes, suffixes, partial-JSON extraction, coercion and repairs are not. Duplicate object keys and nonfinite numbers are rejected as malformed JSON. Only the final content channel is parsed.

Apply the unchanged R5 validator to every parsed judgment:

- Exactly `evaluation_id`, `correctness_score`, `correctness_reason`, `abstention_outcome`, `claim_judgments`, `evaluator_notes` at the root.
- EID equals the supplied atomic case ID.
- Correctness has exact integer type, excluding booleans/floats, and is 0, 1 or 2.
- Abstention is exactly `correct_abstention`, `failed_to_abstain`, `incorrect_abstention` or `not_applicable`.
- Correctness reason is a nonempty, non-whitespace string; notes are a string.
- Claims are a list; each has exactly `claim_text`, `label`, `reason`, with string text/reason and a label in `SUPPORTED`, `PARTIALLY_SUPPORTED`, `UNSUPPORTED`, `CONTRADICTED`.
- Empty claim text/reason remains schema-valid under R5; no new model-specific validator rule is introduced.

Substantive signature is `[correctness_score, abstention_outcome, ordered list of claim labels]`. Exact gold match means equality with the immutable case gold signature. Reasons, notes and claim paraphrases do not affect exact-gold or repeatability scoring. Label order and multiplicity do. A schema-invalid output cannot count as gold-correct or repeatable, including when both repetitions fail similarly.

## Non-negotiable acceptance gates

Each model qualifies only if **all** conditions hold:

- **SCHEMA = 18/18** valid judgments: no malformed output or missing required field.
- **GOLD >= 15/18** exact substantive gold matches (83.3%).
- **REPEATABILITY >= 8/9** cases with identical valid substantive signatures across repetitions.
- No systematic inability to classify abstention or grounding, operationalized prospectively below.

For each substantive abstention class (`correct_abstention`, `failed_to_abstain`, `incorrect_abstention`), at least one schema-valid response must predict that component correctly on a case whose gold has that class. These checks use A04, A05 and A06, each with two repetitions.

For each of the four grounding labels, at least one schema-valid response must predict the exact grounding-label list on a case whose gold includes that label. SUPPORTED uses A01/A02; PARTIALLY_SUPPORTED uses A07; UNSUPPORTED uses A05/A08; CONTRADICTED uses A03/A09. Thus failing both A07 repetitions demonstrates a systematic partial-support classification failure even if aggregate gold reaches 15/18. Check empty claim lists on pure abstention separately in the audit; the full gold gate still applies.

No result-driven prompt tuning, gate relaxation, altered gold or selective omission. Historical results do not excuse a narrow failure. All models face the same rules.

## Evidence, model hygiene and final-pair selection

Archive every attempted request identifier and payload hash, raw server response (including thinking if present), parsed judgment/error, schema result, gold result, signature, repetition result and wall-clock duration. Record mean and median seconds across all 18 scheduled calls, including first-call cold loading and failures. Preserve metadata, placement, runtime version, tags/digests, templates and exact options. Report technical errors plainly.

Before deleting any newly acquired failed candidate, freeze its evidence and SHA256 manifest. Never delete or modify any of the six pre-existing model identities, including GPT-OSS and every generator/embedding tag. Keep qualified new candidates. Run one candidate at a time and unload it between candidates.

Only qualified models can enter the final pair. Prefer non-Qwen backbones and different families/vendors. The six shortlisted backbones satisfy the non-Qwen preference; disclosed synthetic-teacher overlap is not proof of independent errors.

Rank eligible pairs prospectively: sort each pair's members by descending gold, schema and repeatability; compare the two sorted quality triples lexicographically. Among equal quality pairs, prefer different architectural families, then fewer known Qwen-generator synthetic-training overlaps (Nemotron has one), then fewer shared OpenAI teacher relationships (the GPT-OSS/Phi pair has one), then lower sum of median call latency, then lexical tag order. Report the selected members in that same descending-quality order with tag order breaking ties. No leaderboard or primary-result evidence is used.

If fewer than two qualify, record `FINAL_PAIR_STATUS=INSUFFICIENT_QUALIFIED_MODELS` and stop. Otherwise freeze `llm_judge_final_pair_v1_2026-10-07.md` with exact identities, metrics, settings and diversity limitations, then stop. This small atomic qualification establishes eligibility, not performance on long primary evidence; future primary execution requires a separate authorized input-budget and scoring phase.

## Research boundary and prospective freeze

`PRIMARY_LLM_JUDGE_RUNS=0` throughout. Do not read primary benchmark generated answers/results, primary judge inputs/results or expert outcomes. Do not alter benchmark tasks, generated answers, corpus or expert validation. The runner has no primary-data path or configurable input-root capability. Integrity checks outside the runner may inspect filesystem metadata only.

Print both prospective files and their SHA256 hashes; verify the repository change scope is exactly the search and this contract; commit both as `methodology: freeze R6 judge search and qualification contract`. Verify a clean working tree and preserved hashes before acquiring any model or running any candidate. Freeze harness and copied atomic inputs afterward, before the first qualification call. The previous interrupted harness is not an execution artifact.
