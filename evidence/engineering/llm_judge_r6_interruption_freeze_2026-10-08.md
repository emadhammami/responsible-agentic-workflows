# R6 judge qualification interruption freeze — 2026-10-08

## Status

`R6_STATUS=INCOMPLETE_INTERRUPTED`

R6 was interrupted during acquisition of candidate C05.
The interruption occurred before any C05 qualification request and
before any C06 activity.

R6 is therefore **not** interpreted as a completed six-candidate
qualification and no final-pair outcome is inferred from it.

`FINAL_PAIR_STATUS=NOT_DETERMINED_INTERRUPTED`

## Prospective protocol

The frozen prospective R6 artifacts remain unchanged:

- qualification contract SHA256:
  `9d026fb0172b4e79036fa399f02da1e96ef4f519abc67fc70700e1bb3964f5cf`
- candidate-search record SHA256:
  `b7e56744e0d0cf8b16e9f65e676fdfe58a29faf8f12bc6cbf7cafa0dad65e4e9`

No post-result change to the R6 prompt, cases, gold labels, parser,
validator, decoding policy, acceptance gates, or candidate identities
is recorded by this freeze.

## Completed candidate outcomes

| Code | Model | Schema | Gold | Repeatability | Qualified |
|---|---|---:|---:|---:|---|
| C01 | `gpt-oss:20b` | 16/18 | 14/18 | 8/9 | NO |
| C02 | `glm-4.7-flash:q4_K_M` | 18/18 | 16/18 | 9/9 | NO |
| C03 | `phi4-reasoning:14b-plus-q8_0` | 18/18 | 6/18 | 9/9 | NO |
| C04 | `gemma4:26b-a4b-it-q4_K_M` | 18/18 | 16/18 | 9/9 | NO |

C02 and C04 met the aggregate schema/gold/repeatability thresholds but
failed the prospectively frozen PARTIALLY_SUPPORTED grounding-coverage
requirement. C01 failed schema, gold, and coverage requirements. C03
failed the gold threshold and multiple coverage requirements.

These are candidate-level qualification outcomes only. They do not
constitute a final R6 pair-selection result because C05 and C06 were
not completed.

## Interrupted candidates

- C05 `nemotron-3-nano:30b-a3b-q4_K_M`:
  acquisition began; qualification requests = 0.
- C06 `deepseek-r1:8b-llama-distill-q8_0`:
  not started.

## Scientific boundary

- `PRIMARY_LLM_JUDGE_RUNS=0`
- primary benchmark generated answers were not judged in R6
- expert-validation outcomes were not used for candidate selection
- benchmark tasks, corpus, generated outputs, and expert records were
  not modified by this interruption freeze
- no R6 failed candidate is promoted to final-judge status

A later judge-selection protocol, if used, must be frozen prospectively
before any additional qualification inference or primary benchmark
judging.

## Frozen interruption capsule

Capsule:

`/home/emadh/primary-benchmark-results/LLM-JUDGE-R6-QUALIFICATION-2026-10-07`

Snapshot manifest:

`evidence/engineering/llm_judge_r6_interruption_capsule_sha256_2026-10-08.json`

Snapshot-manifest SHA256:

`83e0fde60956fd3401c3b8d671b63ea25c004375373debf6c4b8a313dd7ecd82`

This manifest freezes the byte-level state of the R6 evidence capsule
at interruption registration.
