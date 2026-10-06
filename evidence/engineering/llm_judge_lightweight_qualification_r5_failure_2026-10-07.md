# Lightweight LLM Judge Qualification R5 — Frozen Failure Record

Date: 2026-10-07

## Classification

FAILED_CANDIDATE_QUALIFICATION

This qualification used synthetic atomic cases only.
It did not execute any primary benchmark judging and did not
read primary benchmark outputs.

R5 is not claimed to be a byte-for-byte replay of R4.
It uses the frozen R4 atomic evaluation semantics.

## Pre-result contract

- Cases: A01–A09
- Repetitions: 2
- Candidates:
  - gemma3:12b
  - olmo-3:7b-instruct
- Total model calls: 36
- Qualification gate:
  - schema 18/18
  - gold 18/18
  - repeatability 9/9
- Prompt tuning after results: prohibited
- Gate relaxation after results: prohibited

## Results

### Gemma 3 12B

- Schema: 18/18
- Gold: 6/18
- Repeatability: 9/9
- Qualified: NO

### OLMo 3 7B Instruct

- Schema: 18/18
- Gold: 0/18
- Repeatability: 9/9
- Qualified: NO

Both candidates are rejected as primary benchmark judges.

## Artifact identities

- execution log SHA256: 688594199f98e9f3e28ad55c6dd037152a49c79c1af9d14f569347ae733f4039
- prompt SHA256: c57ad42fcef1e6382dd2b72572898a6fd21ae780bd2e9189467d6512dfeb913c
- cases SHA256: b3b1548c5e53d876fde24f48e95eb9ebd114f5291f7c22e98b29545e2a1e7de2
- runner SHA256: 250af63eba5bec19666923affd466736dc3abe0cd5e85400040c08ccdbd33a90
- raw-response artifact SHA256: b9ff16509acc1f6ad994e1f042a68a278ed47055f930e7b8881a6112c5eea696
- parsed-judgment artifact SHA256: d42959aac1a437e19a1434e466b041ced978c31c454ec3f52406feed8a924a4b

## Governance

- R5 contract frozen before execution: YES
- Prompt tuning after results: NO
- Benchmark-result-driven tuning: NO
- Primary benchmark outputs read: NO
- Primary benchmark judge runs: 0
- Statistical benchmark analysis started: NO
