# UC3 — Digital Competences for Democratic Participation

Status: frozen (Phase 4B4 retrieval foundation freeze complete; benchmark NOT started)

## Source context

UC3 is derived from a policy-analysis context. The sensitive internal
curation material that informed candidate selection is used only as a
curation and selection source. It is marked sensitive and is therefore
not included in the public benchmark corpus or repository.

The corpus was assembled from the original publicly available policy
and framework documents identified during that curation.

## Initial candidate document set

The policy analysis identifies three core policy families:

1. EC DigComp 3.0
2. Council of Europe RFCDC
3. EU Key Competences for Lifelong Learning

and four additional supporting frameworks:

4. UNESCO ICT Competency Framework for Teachers v3
5. EU Declaration on Digital Rights and Principles
6. EC DigCompEdu
7. EU DigCompOrg

RFCDC consists of three distinct source volumes, therefore the corpus contains
nine source documents.

## Candidate source documents

1. DigComp 3.0: European Digital Competence Framework
2. RFCDC Volume 1: Context, concepts and model
3. RFCDC Volume 2: Descriptors of competences
4. RFCDC Volume 3: Guidance for implementation
5. Council Recommendation on Key Competences for Lifelong Learning
6. UNESCO ICT Competency Framework for Teachers — Version 3
7. European Declaration on Digital Rights and Principles for the Digital Decade
8. European Framework for the Digital Competence of Educators — DigCompEdu
9. European Framework for Digitally-Competent Educational Organisations — DigCompOrg

## Acceptance status (Phase 4A)

All nine candidate documents have passed acquisition auditing and
eligibility review and are recorded as `accepted` in
`corpus/manifest.json`. Candidate-to-document mapping:

| Candidate | Document |
|-----------|----------|
| UC3-C01 | DOC032 |
| UC3-C02 | DOC033 |
| UC3-C03 | DOC034 |
| UC3-C04 | DOC035 |
| UC3-C05 | DOC036 |
| UC3-C06 | DOC037 |
| UC3-C07 | DOC038 |
| UC3-C08 | DOC039 |
| UC3-C09 | DOC040 |

Each record carries its authoritative source URL, verified SHA256 (matching
`acquisition_audit.tsv` and the local raw PDF), and a conservative rights
note. Raw PDFs are gitignored and retained under `raw/`. Processed chunking
and embedding materialization are complete, and the corpus is frozen
(Phase 4B4).

## Scientific boundary

- No benchmark task is constructed yet.
- No document is accepted merely because it appears in this candidate list.
- Each source must be downloaded from an authoritative public source.
- Each source must pass provenance, readability, relevance and rights review.
- SHA256 hashes are recorded before manifest acceptance.
- Reference answers and benchmark questions are constructed only after corpus freeze.
- The sensitive internal curation material is never runtime evidence.

## Retrieval foundation freeze (Phase 4B4)

The UC3 retrieval foundation is frozen. Eligibility adjudication is complete and
all nine documents (`DOC032`-`DOC040`) are accepted and retrieval-active. Chunking and
embedding materialization are complete. The frozen identity diagnostic was
completed as descriptive engineering evidence, while the frozen semantic
diagnostic passed its pre-specified retrieval-configuration qualification gate.
The benchmark task has NOT been started.

See `evidence/engineering/uc3_retrieval_foundation_freeze_2026-09-24.md` for the
freeze record and SHA256 bindings.

BENCHMARK_STARTED=NO
