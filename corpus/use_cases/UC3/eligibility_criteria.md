# UC3 Eligibility Criteria

Status: frozen
Use case: UC3 — Digital Competences for Democratic Participation
Frozen: 2026-09-24
Candidate documents: DOC032, DOC033, DOC034, DOC035, DOC036, DOC037, DOC038, DOC039, DOC040

## Purpose

This document freezes the formal eligibility rubric used to adjudicate final
corpus inclusion for the nine UC3 candidate documents. It is outcome-
independent: the criteria do not reference benchmark scores, retrieval
quality, model answers, chunk counts, embedding behavior, or any other
performance outcome, and they do not require a target number of eligible
documents.

## Criteria

### A. Authoritative provenance / document identity

The document must be attributable to an authoritative public institution or
organization relevant to the UC3 domain, and the acquired file must
correspond to the cited document identity.

### B. Stable identification

The record must provide sufficient stable identification: title, publishing
organization, source reference and/or authoritative URL, publication/
version/date where applicable, and SHA256 of the acquired file.

### C. Technical usability

The document must contain substantive English machine-readable text suitable
for deterministic document processing.

This criterion is technical usability only. It must NOT be defined using
observed benchmark or retrieval performance.

### D. UC3 scope relevance

The document must substantively address at least one part of the predefined
UC3 construct:

- digital competence,
- democratic/civic competence,
- digital rights/principles,
- educator digital competence,
- organizational/institutional digital competence,
- or competence frameworks directly supporting democratic participation,
  deliberation, education, or digitally mediated civic participation.

Do not broaden this criterion to unrelated digital policy merely to retain a
candidate.

### E. Evidentiary sufficiency

The document must contain enough primary normative/framework/source content
to support grounded factual or cross-document knowledge-work questions.

Landing pages, citation-only records, or short summaries without substantive
source content are insufficient.

### F. Runtime independence

Final inclusion must not depend on the sensitive internal curation material.

Each included document must independently exist as an authoritative public
source and must be usable as runtime evidence without the sensitive internal
material.

The sensitive internal material must never enter:

- the runtime corpus,
- the retrieval index,
- task evidence,
- benchmark input,
- the public repository.

### G. Rights / access handling

Public availability must NOT be treated as equivalent to an open
redistribution licence.

For each document, record:

- the authoritative public access location,
- known licence/rights information if explicitly available,
- redistribution status if known,
- uncertainty if rights are unclear.

A document may remain eligible for local academic experimental use when
authoritative public access is established and repository redistribution is
avoided where rights are unclear.

Do not invent licence terms or make unsupported legal conclusions.

## Fixed decision logic

- **ELIGIBLE**: A–F pass and G establishes sufficient documented
  public/research access with appropriate redistribution handling.
- **NEEDS_REVIEW**: one or more required facts remain genuinely uncertain and
  cannot yet be responsibly adjudicated.
- **INELIGIBLE**: one or more required A–F criteria fail, or G shows the
  document cannot be used under the defined local research handling.

The following semantics are fixed and non-negotiable:

- The criteria are applied per document.
- Uncertainty cannot be converted to PASS merely to preserve corpus size.
- Inclusion cannot depend on retrieval or benchmark performance.
- No target number of eligible documents is required.
- Null or negative eligibility outcomes are valid.
- The criteria cannot be altered after seeing document-level decisions merely
  to retain or exclude candidates.

## Timing / limitation statement

The nine UC3 candidates had already been identified and provisionally
accepted during intake before this formal eligibility rubric was written.
Therefore this project does not claim that the rubric preceded candidate
identification or provisional acceptance. The rubric is being frozen before
final corpus inclusion, embedding materialization, retrieval evaluation,
benchmark-task construction, scientific benchmark execution, and final corpus
freeze.

Page and chunk artifacts had already been generated before this formal
rubric was frozen. Those artifacts are treated as provisional engineering
outputs only and provide no basis for eligibility decisions.
