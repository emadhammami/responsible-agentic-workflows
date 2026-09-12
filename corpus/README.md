# Real Thesis Corpus

This directory contains the real document corpus used for thesis benchmark
development.

A use case represents one organizational or source context, not one individual
document.

Current use cases:

- UC1 - OptFor-EU Forest Policy

UC2 and UC3 are intentionally not defined yet.

Each use case may contain multiple documents from its source context.

The corpus manifest records:

- use-case identity;
- document identity;
- source provenance;
- local source path;
- content hash;
- selection status.

Document selection states are:

- `candidate` - collected but not yet accepted;
- `accepted` - approved for the working corpus;
- `excluded` - reviewed and excluded.

The overall corpus remains `working` while documents and future use cases are
still being selected.

The real corpus is separate from the synthetic engineering fixtures under
`benchmark/synthetic/`.
