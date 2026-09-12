# Generation Model Qualification Q4 Fixture Amendment

Date: 2026-09-12

## Preserved failed attempt

The first generation-model qualification attempt is preserved without
modification in:

`evidence/engineering/generation_model_qualification_2026-09-12.json`

SHA256: `f1d4017f220341c8342a99712bdce921639117de5fcfc27468b7cab995a1b2d8`

The attempt contained eight local inference calls: four synthetic fixtures
with two repetitions each.

Observed gate outcome:

- Q1 grounded extraction: PASS
- Q2 insufficient evidence: PASS
- Q3 cross-document synthesis: PASS
- Q4 structured output: FAIL
- Q5 thinking disabled: PASS
- Q6 local execution identity: PASS

## Q4 diagnosis

The Q4 failure is classified as an engineering-fixture validation defect,
not as evidence of a model structured-output failure.

The synthetic source described the values as `Project Pine` and `Tier B`.
The model returned valid JSON with the exact required keys and the
source-faithful values `Project Pine`, `Tier B`, and `18` in both
repetitions.

The validator nevertheless expected normalized values `Pine` and `B`.
That normalization requirement was not stated in the qualification prompt.
The validator therefore imposed an unstated transformation requirement.

The failed attempt remains recorded as FAIL and is not retroactively
reclassified as PASS.

## Corrective action

Only Q4 will be repeated with an unambiguous synthetic fixture.

The revised fictional source will state:

- project identifier: `Pine`
- tier code: `B`
- review interval: `18` months

The requested JSON remains:

```json
{"project": "Pine", "tier": "B", "review_months": 18}
```

This preserves the original Q4 purpose: testing valid structured output
with exact keys and source-supported values. It removes the unintended
normalization ambiguity.

## Configuration boundary

No model or generation configuration is changed for the Q4 retest:

- model: `qwen3.8-27b-48k:latest`
- context: `49152`
- temperature: `0`
- seed: `20260912`
- num_predict: `1024`
- thinking: `false`

The frozen UC1 benchmark tasks, reference answers, and reference evidence
will not be used in the retest.

Q1, Q2, and Q3 will not be rerun because their two pre-specified
repetitions already passed and their fixtures were not defective.

Q5 will also be checked on both new Q4 calls. Q6 local execution identity
will be reconfirmed after the retest.

This amendment is recorded before the Q4 retest.

## Status

- `FAILED_ATTEMPT_PRESERVED=YES`
- `Q4_FAILURE_CLASSIFICATION=FIXTURE_VALIDATOR_DEFECT`
- `MODEL_CONFIGURATION_CHANGED=NO`
- `UC1_BENCHMARK_TASKS_USED=NO`
- `Q4_RETEST_EXECUTED=NO`
- `MODEL_FROZEN=NO`
- `BENCHMARK_RUN=NO`
