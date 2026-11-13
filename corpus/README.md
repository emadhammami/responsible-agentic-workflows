# Document Corpus: UC1, UC2, and UC3

This directory documents the source selection, acquisition and frozen retrieval
scope of the three document contexts used in the master's thesis benchmark.
A use case is a source context containing multiple documents, not one document.

| Use case | Document context | Frozen retrieval-active documents | Primary tasks |
| --- | --- | ---: | --- |
| UC1 | OptFor-EU forest policy | 30 | T001–T010 |
| UC2 | Scottish Green Freeports | 17 | T011–T020 |
| UC3 | Digital and democratic competence frameworks | 9 | T021–T030 |
| **Total** | | **56** | **30 tasks** |

All three use cases were included in the primary 270-execution Study A
benchmark: B0, B1 and G1, each repeated three times per task. For the
current task and configuration scope, see the
[primary benchmark freeze](../benchmark/config/primary/primary_benchmark_config_freeze_manifest.json)
and [task definitions](../benchmark/tasks/).

## Corpus provenance and historical status fields

The original [corpus manifest](manifest.json), use-case acquisition records,
and older protocol documents preserve their research-stage provenance. Some
were written before UC2/UC3 or the primary benchmark had been finalized and
therefore contain historical `working`, `not selected` or `not started`
statements. These describe the state at that earlier checkpoint, **not** the
completed benchmark. Do not rewrite frozen manifests or source identities to
make their earlier status fields look current.

The frozen membership definitions are in
[UC1](use_cases/UC1/benchmark_scope.json),
[UC2](use_cases/UC2/benchmark_scope.json), and
[UC3](use_cases/UC3/benchmark_scope.json).
Source provenance records include document identities, publisher/source URLs,
recorded hashes, eligibility and acquisition checks.

## Source-document release and limits

The [Study A source-document release](../research-artifacts/study-a/source-documents/README.md)
contains 41 unchanged, rights-reviewed originals (49 files). Another 15
retrieval-active documents are represented by official links and rights notes,
without redistributing the original bytes. The [Study A companion package](../research-artifacts/study-a/README.md)
provides numerical reconstruction materials for the 270 primary executions.

Working raw/processed corpus files and frozen retrieval artifacts are separate
from the public source subset. Complete replay requires the remaining original
documents, matching processed chunks and order, embedding matrices, model
artifacts and execution environment. The synthetic engineering fixtures under
`benchmark/synthetic/` are separate from this real-document corpus.
