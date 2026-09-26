# UC2 Eligibility Criteria Freeze — Evidence Record

Date: 2026-09-26
Phase: UC2-P2
Mode: PROSPECTIVE_ELIGIBILITY_FREEZE

## Purpose

Freeze the UC2 document-level eligibility rubric before acquisition and before
any document-level inclusion decision.

## Frozen artifact

- Path: `corpus/use_cases/UC2/eligibility_criteria.md`
- Status: `frozen`
- SHA256: `d35c735e88ff5c4a6a9241cc928e772d3a9940c453ef7ec20b93fe091b0c96ea`

## Pre-freeze bindings

- Branch: `research/uc2-green-freeports-corpus-intake`
- Parent HEAD: `8705987d8350c741416fd91481667e9c928ef33a`
- Candidate count: `18`
- Candidate IDs: `UC2-C01` through `UC2-C18`
- Source inventory SHA256:
  `04efdfc15a27f6ac2894f8788575601d955518867bc96c460111988207d3b8e8`
- P0/P1 evidence SHA256:
  `1c0abf188f513556445f8f4e7b678681ce02b75be4b3e7044ce354ed5d6da907`
- Scope contract SHA256 before P2 state binding:
  `d6502c58a0e7e37feca5fb1559349648dc7a7cda633f7be5ede4c8dec3797980`
- Scope contract SHA256 after P2 state binding:
  `c90b8884d916c83fd401fcb69965ff2c875ca8f593e40bcb30666c4dde141184`

## Chronology guard

Before this freeze:

- candidate discovery had occurred;
- the candidate inventory had been expanded through a pre-eligibility
  completeness audit;
- no candidate had been accepted;
- acquisition had not started;
- no raw UC2 document directory existed;
- no processed UC2 document directory existed;
- no document-level eligibility adjudication had occurred;
- no preprocessing had occurred;
- no embeddings had been materialized;
- no retrieval diagnostic had run;
- no UC2 benchmark tasks had been created;
- scientific benchmark execution had not started.

This project claims only that the rubric precedes acquisition and all
document-level eligibility decisions. It does not claim that the rubric
preceded candidate discovery.

## Freeze semantics

The rubric is outcome-independent and contains no target corpus size.

Later document-level decisions must use this frozen rubric.

A substantive rubric change after adjudication begins must be treated as a
protocol deviation and may not be justified by desired inclusion count,
retrieval outcomes, or benchmark results.

## State

UC2_P2_ELIGIBILITY_FREEZE=PASS
CANDIDATE_COUNT=18
CANDIDATES_ACCEPTED=0
DOCUMENT_ACQUISITION_STARTED=NO
DOCUMENT_LEVEL_ADJUDICATION_STARTED=NO
ELIGIBILITY_CRITERIA_FROZEN=YES
CORPUS_MEMBERSHIP_FROZEN=NO
EMBEDDINGS_MATERIALIZED=NO
RETRIEVAL_DIAGNOSTIC_STARTED=NO
BENCHMARK_TASKS_CREATED=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
