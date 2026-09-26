# UC2-C13 Acquisition Recovery

Date: 2026-09-26
Phase: UC2-P3C targeted recovery
Mode: TARGETED_ACQUISITION_TRANSPORT_RECOVERY

## Trigger

The frozen acquisition-plan endpoint for UC2-C13 returned HTTP 403.

Planned endpoint:

`https://democracy.edinburgh.gov.uk/documents/s73468/7.15%20Forth%20Green%20Freeport%20Full%20Business%20Case.pdf`

No other candidate failed.

The successful 17 acquisitions were retained and were not re-downloaded.

## Recovery basis

The City of Edinburgh Council official FOI disclosure log, request 50906,
publishes the same document:

"Forth Green Freeport - Full Business Case - referral from the Policy and
Sustainability Committee".

The Council disclosure link resolves to a publicly accessible 49-page PDF
hosted at:

`https://edinburgh.axlr8.uk/documents/50906/50906%20Forth%20Green%20Freeport%20-%20Full%20Business%20Case%20-%20referral%20from%20the%20Policy%20and%20Sustainability%20Committee.pdf`

This is an endpoint/transport recovery for the same authoritative public
document identity. It is not substitution based on document content,
eligibility outcome, retrieval performance, or benchmark performance.

## Frozen-state handling

The frozen acquisition plan was NOT modified.

- acquisition plan SHA256:
  `fb0a93b729fb245aa33ed4bd50d0561fee2ed7d69aa8008ada5ad8e22475a71b`
- eligibility criteria SHA256:
  `d35c735e88ff5c4a6a9241cc928e772d3a9940c453ef7ec20b93fe091b0c96ea`
- targeted recovery-plan SHA256:
  `814c068e993d08f2fedb78e361adca0a0aa7aece9f1a7406b59e0301fa3910d9`

Pre-recovery records:

- acquisition audit SHA256: `70cef7e7a40a7dbd942b4b8c6da67a6460bfbc9249ee28e2768b29ef51fdce9e`
- HTTP metadata SHA256: `c0d45ea471fba0a30d105fcfb6a96a25cf518824324e900f5ea9f73346b69557`
- source inventory SHA256: `18d9770e9848dd511ba1f7753c0fd07458c108bf1db3e1e78e742afd71d3f322`

## Recovered artifact

- Candidate: `UC2-C13`
- File: `UC2-C13_forth_fbc_committee_report.pdf`
- Bytes: `858415`
- SHA256: `9e1d146a78e83e4bb6dcdfbf54974af8ccfe322cb226cf786ea8c62daccaccdb`
- Media type: `application/pdf`
- Recovery status: `ACQUIRED`

## Scientific-state guard

CANDIDATES_ACCEPTED=0
ELIGIBILITY_DECISIONS=0
DOCUMENT_LEVEL_ADJUDICATION_STARTED=NO
CORPUS_MEMBERSHIP_FROZEN=NO
BENCHMARK_STARTED=NO
