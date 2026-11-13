# Responsible Agentic Workflows

**Evidence-Gated Recovery, Reliability, and Resource Efficiency in LLM-Based Knowledge Work**

Research software for evaluating bounded agentic workflows in document-based
knowledge work. The project examines task quality, reliability, latency, and
computational resource use. B1 versus G1 is the primary policy comparison;
B0 provides baseline context.

The research was conducted for the 30-ECTS MIS500 master's thesis in Digital
Transformation at the University of South-Eastern Norway (USN):
*Guardrails and Resource Efficiency in LLM-Based Agentic Workflows: An Empirical
Study of Responsible Adoption in Document-Based Knowledge Work*.

## Study design

- **B0:** retrieval-augmented generation baseline.
- **B1:** agentic workflow with a fixed, bounded recovery policy.
- **G1:** the matched agentic workflow with Evidence- and Resource-Gated
  Recovery (ERGR).

B1 and G1 share the graph, model, retrieval, critic, release predicate, recovery
implementation, and hard execution limits. Their pre-recovery decision policy
is the treatment. Resource stops, deliberate abstentions, and execution failures
are distinct outcomes.

The thesis covers three document contexts: UC1, OptFor-EU forest policy;
UC2, Scottish Green Freeports; and UC3, DC4Democracy-related digital, democratic,
and teacher competence frameworks. Study A comprises 30 tasks (10 per use case),
three conditions, and three repetitions: 270 recorded executions retained in
the research archive.

## Thesis research and released evidence

The thesis also reports Study B (24 synthetic task families, 144 executions),
a separate resource-boundary substudy (six families, 36 executions), and
Study C (18 real-retrieval tasks, 108 usable scored outcomes). Their evidence
streams and denominators are separate from Study A. The public companion
package currently supports numerical reconstruction for Study A; equivalent
public reconstruction packages for Studies B and C and the resource-boundary
substudy are not claimed here. Human research responses are not bundled.

## Implementation scope

The principal implementation contains the B0 baseline, shared B1/G1 execution
runtime, recovery policies, dense retrieval integration, frozen primary
configurations, and the complete three-use-case task definitions.
It also retains later scoring protocols and continuation scripts. It is a
research implementation, not a complete public archive of thesis evidence.

The [prospective paper/thesis scope decision](evidence/engineering/paper_thesis_scope_separation_v0.1_2026-09-27.md)
was recorded before primary execution. The planned paper uses UC1 only:
T001–T010 × B0/B1/G1 × three repetitions = 90 executions. The thesis retains
all 270 executions and the broader cross-use-case scope. The separate UC1-only paper scope does not narrow the thesis implementation
or establish publication status for that paper.

## Implementation and materials

| Path | Contents |
| --- | --- |
| `src/responsible_agentic_workflows/workflow/` | B0 baseline, shared B1/G1 graph and runner, critic, recovery, resource guards, and policies |
| `src/responsible_agentic_workflows/benchmark/orchestration.py` | `execute_primary_runtime_task`, the caller-scheduled single-run execution API |
| `src/responsible_agentic_workflows/retrieval/`, `src/responsible_agentic_workflows/modeling/` | Dense/lexical retrieval, embedding artifact loading, and Ollama adapters |
| `benchmark/config/primary/` | Frozen UC1/UC2/UC3 configurations and configuration freeze manifest |
| `benchmark/config/model/`, `benchmark/config/retrieval/` | Generation model identity and per-use-case retrieval configurations |
| `benchmark/tasks/`, `benchmark/schema/` | T001–T030, task freezes, and validation schemas |
| `benchmark/synthetic/` | Fictional T901–T907 engineering fixtures |
| `corpus/` | Source provenance, selection, acquisition, and materialization metadata |
| `docs/` | Protocol, evaluation rubric, and workflow/runtime contracts |
| `evidence/engineering/` | Historical freezes, execution order, qualification evidence, and scoring amendments |
| `tests/` | Software tests, including synthetic workflow and orchestration checks |
| `scripts/` | Hosted LLM-judge qualification and scoring continuation scripts |

The [workflow contract](docs/b1_g1_workflow_contract.md),
[runtime contract](docs/b1_g1_runtime_contract.md), and
[orchestration contract](evidence/engineering/primary_benchmark_orchestration_contract_v0.1_2026-09-27.md)
explain treatment isolation and execution boundaries. Historical documents may
say that implementation or execution has not started; those statements record
their checkpoint and should be read alongside the later freeze records.
The early [corpus overview](corpus/README.md) also predates UC2/UC3; consult the
per-use-case scope and freeze files for the later benchmark.

## Frozen baseline

- Primary execution code:
  [`58b9e656dd57e62a5fb8640c2d3c990e4c93e530`](https://github.com/emadhammami/responsible-agentic-workflows/commit/58b9e656dd57e62a5fb8640c2d3c990e4c93e530).
- Primary launch revision:
  [`872f8de38c79a78e4e016cedf5597bc21323a374`](https://github.com/emadhammami/responsible-agentic-workflows/commit/872f8de38c79a78e4e016cedf5597bc21323a374).
- Later branch reference, including missing-judgment continuation provenance:
  [`91e09dafddfc894b9ad53e30099675d4e0c282d5`](https://github.com/emadhammami/responsible-agentic-workflows/commit/91e09dafddfc894b9ad53e30099675d4e0c282d5).

The [configuration freeze manifest](benchmark/config/primary/primary_benchmark_config_freeze_manifest.json)
binds the execution code, schemas, task freeze, configurations, and
[270-entry execution order](evidence/engineering/primary_execution_order_v1.json).
The launch revision records the final execution-code binding. The later branch
reference is not a replacement primary execution freeze. Frozen files and
original records must remain unchanged; new replication requires a separate
experiment identity and output location.

## Installation and execution boundary

Use Python 3.13 or 3.14, from the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
```

[pyproject.toml](pyproject.toml) pins `jsonschema`, `langchain`, and `numpy`,
with `pytest` and `ruff` in the development extra. The graph imports `langgraph`,
which is not directly pinned in this project. There is no complete environment
lock file. PDF extraction uses the external `pdftotext` executable.

The retrieval-only synthetic entry point is:

```bash
python -m responsible_agentic_workflows.engineering.smoke
```

It uses fictional documents, makes no model call, and writes an engineering
record under `artifacts/engineering/`. It does not execute the primary benchmark.

Real execution uses `execute_primary_runtime_task` with a `RuntimeTask`
containing only task ID and question, a frozen per-use-case configuration,
retrieval configuration, matching artifact paths, and caller-supplied run and
experiment identifiers. Reference answers and reference evidence are excluded
from runtime input. The API refuses an existing output file.
`tests/test_benchmark_orchestration.py` illustrates API construction with test
components; it is not a full primary experiment launcher.

Generation requires the Ollama model identity recorded in
[the model configuration](benchmark/config/model/OLLAMA-QWEN38-27B-48K-v0.1.json)
(`qwen3.8-27b-48k:latest`, with recorded digest and context settings), plus the
configured Qwen embedding model and frozen retrieval artifacts. UC2 uses a
hash-checked legacy artifact loader; replacement or regenerated embeddings
cannot be assumed equivalent. The companion package retains the historical
batch launcher for inspection; its original paths and experiment identity are
not a portable replication command. The complete original raw result archive
is retained separately. The scoring scripts require separate inputs and
provider access and are not benchmark launchers.

## Reconstructing released measurements

The [Study A companion package](research-artifacts/study-a/README.md) provides
text-free projections of all 270 execution records, original resource tables
and figure sources, provisional numeric LLM-judge scores with slot provenance,
and frozen retrieval identities. It includes a portable adapter to reconstruct
resource/control summaries, selected thesis and resource figures, and the
provisional inter-judge agreement matrix without running an LLM.

From the repository root, in a Python environment:

```bash
python -m pip install -r research-artifacts/study-a/requirements-analysis.txt
python -B research-artifacts/study-a/reproduce.py \
  --output /tmp/study-a-reconstruction --figures
```

Use a new output directory. The package documents field omissions, source
bindings, tested dependencies and numerical checks. Original answers, recovery
query text, full judge responses and expert records are retained separately.
The released data support measurement reconstruction; their checksums alone
cannot establish independent correctness or full inference reproducibility.

## Source-document availability

The [corpus release](research-artifacts/study-a/source-documents/README.md)
contains 41 of the 56 retrieval-active originals (49 files, including DOC051's
nine-component HTML bundle). Original filenames, bytes and hashes are retained.
The remaining 15 documents have official links and individual permission notes.
This partial release improves source inspection and reconstruction but does
not replace the complete 30/17/9-document benchmark corpus. Frozen chunks,
embedding matrices, matching models and the construction environment are still
needed for original retrieval replay.

## Evidence and reproducibility limits

Public materials include implementation, tests, task definitions, configuration
and freeze manifests, source metadata, selected engineering records, and
methodological protocols. The rights-reviewed source subset is included;
processed corpus/index files, model weights, the complete original 270-run raw
archive, full scoring records, expert responses, interviews and private research
packages are not bundled.
The companion package releases selected numeric derivatives and provenance.
The corpus release records document-specific redistribution terms;
public access alone is not treated as permission.
The repository supports inspection and engineering checks; it does not provide
self-contained reproduction of the full study.

The scoring protocol was amended to replace planned full manual scoring
with LLM judges and a specified expert subset. The later [Option C amendment](evidence/engineering/option_c_primary_amendment_2026-10-08.md)
records qualification limitations and treats automated quality scores as
provisional. LLM assessments are not independent human validation. Protocols
and qualification records do not establish complete human coverage, final
quality superiority, or public availability of the underlying judgments.
