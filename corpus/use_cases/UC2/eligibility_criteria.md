# UC2 Eligibility Criteria

Status: frozen
Use case: UC2 — Scottish Green Freeports
Frozen: 2026-09-26
Candidate set: UC2-C01 through UC2-C18

## Purpose

This document prospectively freezes the formal document-level eligibility
rubric for UC2 before candidate acquisition, document-level adjudication,
corpus construction, preprocessing, embedding materialization, retrieval
evaluation, benchmark-task construction, or scientific benchmark execution.

The criteria are outcome-independent.

They do not reference:

- benchmark performance;
- retrieval quality;
- model answers;
- embedding behavior;
- chunk counts;
- corpus-size targets; or
- desired inclusion counts.

No target number of eligible documents is required.

## Criteria

### A. Authoritative provenance

The candidate must resolve to an authoritative public source relevant to the
Scottish Green Freeport policy or implementation domain.

Eligible authority classes include:

- Scottish Government;
- UK Government departments;
- HM Revenue & Customs;
- Revenue Scotland;
- official legislation;
- accountable or participating Scottish local authorities.

Commercial promotional material, press coverage, consultancy commentary,
advocacy material, and operator marketing do not satisfy this criterion merely
because they discuss Green Freeports.

### B. Stable document identity and artifact resolution

The acquired evidence unit must have a stable and auditable identity.

Record, where applicable:

- exact title;
- issuing authority;
- publication or revision date;
- authoritative source URL;
- document/version/reference identifier;
- exact acquired artifact or bounded HTML content unit; and
- SHA256 of the acquired artifact or deterministic acquisition representation.

A landing page, disclosure index, meeting index, or publication catalogue does
not by itself satisfy this criterion when it merely points to the substantive
document.

For candidates represented initially by landing pages, the exact authoritative
substantive artifact must be resolved before ELIGIBLE can be assigned.

### C. Technical usability

The acquired document must contain substantive English machine-readable or
deterministically extractable text suitable for reproducible document
processing.

Primarily graphical artifacts, maps, image-only files, navigation pages, or
records containing insufficient textual evidence do not satisfy this
criterion merely because they are authoritative.

This criterion must not use observed retrieval or benchmark performance.

### D. UC2 substantive scope relevance

The document must substantively address at least one predefined UC2 policy
layer:

1. Scottish Green Freeport policy design, objectives, governance, or programme
   architecture;
2. business-case, designation, approval, monitoring, assurance, or delivery
   requirements;
3. fiscal, subsidy, tax, rates, allowance, or seed-capital mechanisms applicable
   to Scottish Green Freeports;
4. customs mechanisms applicable to Scottish Green Freeports;
5. planning or consenting arrangements for Scottish Green Freeports;
6. legal designation or operation of Scottish Green Freeport tax/customs sites;
7. implementation of Inverness and Cromarty Firth Green Freeport; or
8. implementation of Forth Green Freeport.

Do not broaden this criterion to generic regeneration, port, trade, tax,
industrial, or net-zero policy merely to retain a candidate.

### E. Scotland applicability / mechanism directness

A Scotland-specific Green Freeport source satisfies this criterion when its
application to UC2 is explicit.

A generic UK Freeport source is eligible only when at least one of the
following is established from authoritative evidence:

1. the issuing authority explicitly states that the guidance or mechanism
   applies to Green Freeports in Scotland; or
2. an authoritative Scottish/UK Green Freeport source directly binds or
   incorporates that mechanism into the Scottish programme.

Similarity to an English Freeport mechanism, shared terminology, or plausible
policy relevance is insufficient by itself.

### F. Evidentiary sufficiency

The document must contain enough substantive primary legal, normative,
governance, operational, fiscal, customs, planning, or implementation content
to support grounded factual or cross-document knowledge-work questions.

Insufficient by themselves:

- citation records;
- short landing-page descriptions;
- attachment indexes;
- press-release summaries;
- promotional overviews;
- map-only artifacts; or
- pages whose substantive evidence exists only in an unresolved attachment.

### G. Runtime evidence independence and context separation

Final corpus inclusion must rest on the authoritative public document itself.

Discovery aids, contextual pages, maps, marketing pages, news coverage, or
other non-corpus material may help locate or interpret a candidate but must not
be required as hidden runtime evidence for answering benchmark questions.

If contextual material is necessary to establish document identity or
applicability, that dependency must be recorded explicitly during adjudication.

### H. Rights and access handling

Public availability must not be treated as equivalent to an open
redistribution licence.

For every included document, record:

- authoritative public access location;
- known licence or rights information when explicitly stated;
- redistribution status when known; and
- uncertainty when rights are unclear.

A document may remain eligible for local academic experimental use when
authoritative public access is established and repository redistribution is
avoided where rights are unclear.

Do not invent licence terms or unsupported legal conclusions.

## Fixed decision logic

### ELIGIBLE

All criteria A–G pass and criterion H establishes sufficient documented
public/research access with appropriate redistribution handling.

### NEEDS_REVIEW

One or more required facts remain genuinely unresolved and responsible
adjudication cannot yet be completed.

Examples include:

- unresolved exact attachment identity;
- uncertain applicability of generic UK guidance to Scottish Green Freeports;
- uncertain authoritative provenance;
- incomplete rights/access evidence; or
- acquisition failure preventing technical-content assessment.

### INELIGIBLE

One or more required A–G criteria fail, or H establishes that the document
cannot be used under the defined local research handling.

## Fixed semantics

The following rules are non-negotiable:

- Criteria are applied per acquired document/evidence unit.
- Candidate identification is not acceptance.
- Acquisition success is not acceptance.
- Authority alone is not sufficient.
- Uncertainty cannot be converted to PASS to preserve corpus size.
- Inclusion cannot depend on retrieval or benchmark performance.
- No target number of eligible documents is required.
- Null, negative, and NEEDS_REVIEW outcomes are valid.
- C12/C13 landing pages cannot be treated as the FBC documents unless their
  exact authoritative substantive artifacts are resolved.
- Generic UK Freeport guidance cannot be included solely because its subject
  resembles Scottish Green Freeport policy.
- Maps and primarily graphical artifacts remain contextual unless they
  independently satisfy all criteria.
- The rubric cannot be substantively altered after document-level outcomes are
  observed merely to retain or exclude candidates.

## Timing and chronology statement

The 18 candidates were identified before this formal eligibility rubric was
frozen.

No candidate had been accepted into the UC2 corpus before this freeze.

At the time of freeze:

- document acquisition had not started;
- no document-level eligibility adjudication had started;
- no final corpus membership existed;
- no UC2 page/chunk artifacts existed;
- no UC2 embeddings existed;
- no UC2 retrieval diagnostic had run;
- no UC2 benchmark tasks existed; and
- the scientific benchmark had not started.

Therefore the eligibility criteria are frozen prospectively before candidate
acquisition and before every document-level inclusion decision.
