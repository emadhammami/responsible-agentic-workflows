# UC1 Document Selection Criteria

## Use case

UC1 represents document-based forest policy knowledge work using policy
resources identified through the OptFor-EU policy environment.

The use case may contain multiple documents from different institutions and
jurisdictions. These documents belong to one use case because they support the
same forest-policy knowledge-work context.

## Inclusion criteria

A document may be included when it:

1. is identified through the OptFor-EU policy environment or a source directly
   referenced by it;
2. is an official policy, strategy, regulation, guideline, management-policy
   document, or closely related authoritative policy source;
3. contains substantive textual content that can support document-grounded
   question answering or reasoning;
4. has identifiable provenance, including a title and source organization;
5. can be stored and processed in a stable document form;
6. is available in English or can be used without introducing uncontrolled
   translation into the benchmark.

## Exclusion criteria

A document should be excluded when it:

1. is only a short web summary, news item, promotional page, or navigation page;
2. duplicates another document already included in the corpus;
3. lacks sufficient provenance to identify its source;
4. contains too little substantive text for benchmark task construction;
5. cannot be reliably extracted or processed;
6. is primarily a scientific publication rather than a policy or operational
   policy source;
7. falls outside the forest-policy knowledge-work context of UC1.

## Source handling

OptFor-EU may be used as the discovery source while the original issuing
organization is recorded as the document source whenever available.

For example, a policy discovered through OptFor-EU but issued by a government
agency should record:

- `discovered_via`: OptFor-EU Policy Map
- `source_organization`: the original issuing organization
- `source_url`: the original document URL when available

The OptFor-EU page should not replace the original document as the authoritative
source when the original source is available.

## Selection status

Newly collected documents are registered as `candidate`.

A candidate becomes `accepted` only after confirming that it satisfies the
inclusion criteria and does not meet an exclusion criterion.

Excluded documents remain recorded where useful, together with an exclusion
reason.

## Freeze rule

Document selection remains open while UC1 has status `working`.

The accepted UC1 corpus will be frozen before final benchmark execution.
Documents will not be added or removed in response to benchmark performance.
