# Study A: execution telemetry and provisional annotation reconstruction

This package accompanies the frozen 30-task, three-condition, three-repetition
benchmark (270 executions). It supports reconstruction of resource/control
statistics and selected figures without source documents, model access, or
participant records. A separate rights-reviewed source subset is included for
source inspection and future retrieval reconstruction. The thesis includes
UC1–UC3; the prospectively specified paper subset is UC1 only. All-use-case tables and figures here must
not be presented as UC1-only results.

## Contents

- `data/execution_telemetry_270.jsonl`: one derived record for each original
  execution, preserving usage, timing, configuration, retrieval IDs/ranks/scores,
  structured runtime decisions and abstention flags. Each row carries its
  original file hash and a canonical complete-final-output hash.
- `reference/execution_figures_v1/data/`: original metric definitions, 270-row
  metric table, task means, paired differences, descriptive summaries and exact
  figure companions. `reference/runtime_v1/` retains the earlier numeric
  runtime projection, including automated critic/control labels.
- `reference/thesis/data/`, `reference/figures/`, and
  `reference/ieee_figure01/`: existing thesis execution tables, original figure
  PDFs, and the frozen IEEE resource Figure 1 bundle. These are source artifacts,
  not evidence of paper publication or final manuscript inclusion.
- `evaluation/`: 270 pairs of provisional LLM correctness scores, 540 slot
  provenance records, consistency counts, method freeze metadata and a summary
  with human participation metadata removed. These are not expert ratings.
- `retrieval/`: frozen index metadata, row-to-chunk IDs and a catalog of the
  56 active sources.
- [source-documents/](source-documents/README.md): 41 unchanged source documents
  in 49 files, with publisher permissions, attribution and identity checks.
  Fifteen complete originals remain link-only pending rights confirmation.
- `provenance/`: raw-result freeze and hash inventory, public launch metadata,
  run order, task/configuration identities, and the exact field omission log.
- `originals/`: unchanged author-written extraction/plotting sources and the
  historical launcher. Absolute workspace paths remain as provenance. Original
  entry points require their original inputs; use the adapter below for the
  public package. Do not run the archived launcher as a new experiment.
- `adapters/provisional_agreement_plot.py`: the original numerical agreement
  and plotting functions extracted into a separate module. The full evaluation
  script is excluded because it contains private expert-availability assertions.

## Reconstruct tables and figures

Use Python 3.13 or 3.14. From the repository root, with a Python environment:

```bash
python -m pip install -r research-artifacts/study-a/requirements-analysis.txt
python -B research-artifacts/study-a/reproduce.py \
  --output /tmp/study-a-reconstruction --figures
```

The output directory must not already exist. Omit `--figures` to reconstruct
only numeric results. Package contents are verified against `SHA256SUMS.txt`;
outputs are written only to the new directory. No network or model call is
made by reconstruction. A new installation still requires access to dependencies.

The adapter retains original extraction/aggregation functions, substitutes the
released projection for private raw-file loading, and compares 22 existing CSV
companions plus metric definitions. With `--figures`, it renders the 14 v1
resource layouts, three thesis execution figures, the provisional agreement
matrix and frozen IEEE resource Figure 1, checking that figure's two numeric
companions. Existing task-bootstrap settings are retained: 30 task clusters,
10,000 resamples, Python `random.Random(20260912).choices`, linear quantiles.
Repetitions are averaged within task/condition before pairing G1 minus B1.
B0 structural N/A values remain missing rather than being filled with zeros.

Rendering was verified with the versions in `requirements-analysis.txt`.
The historical v1 plotting dependency list is retained separately under
`originals/resource_v1/requirements-lock.txt`. Library and font differences can
change figure bytes; numerical agreement does not establish pixel or PDF-byte
identity. The original frozen IEEE bundle retains its original checksums.

## Omissions and provenance

`provenance/redactions.json` lists every removed field for every original run:
`final_output.answer`, each retrieval `query`, `started_at`, `finished_at`, and
event `timestamp`. No run is excluded. All measurements and structured
runtime/control values are unchanged. The projection is not an original run
record and intentionally does not conform to the complete run-record schema.
Omitted answers are not represented as null answers or fabricated abstentions.

`provenance/launch_manifest.public.json` omits only the absolute `output_root`.
It is not byte-identical to the original manifest bound by the raw freeze.
`evaluation/validation_report.public.json` omits the entire `expert_cutoff`
object. Its historical PASS and source-check counts describe the original
archived check; they do not certify fresh human or semantic evaluation.
`retrieval/source_catalog.csv` selects nine bibliographic/identity columns for
56 active documents from the already public corpus manifest. It omits local
paths, curation notes and inactive candidates.

`provenance/source_bindings.tsv` maps released originals and derivatives to
source filenames and hashes without private archive paths. Original raw hashes
are commitments to retained bytes: a reader without those bytes cannot verify
that this projection faithfully represents them merely by hashing the release.
The projection exporter is provided for authorized archive holders:

```bash
python -B research-artifacts/study-a/export_telemetry.py \
  --archive /path/to/PRIMARY-BENCHMARK-V1 --output /tmp/telemetry-check.jsonl
```

The destination must be new. The exporter checks original record hashes before
omitting fields. It cannot recover withheld text from the public projection.

## Provisional evaluation scope

The numeric composite retains 485 original-valid slots, 29 recovered full
judgments, 25 claim-only hybrid slots and one alias-normalized slot. These are
540 heterogeneous annotation slots, not 540 homogeneous successful first-pass
judgments. Original invalid records remain unchanged in the research archive.
J1 is Cohere and J2 is Gemini; public method amendments record qualification
limitations. The complete composite and the 216 original-valid pairs can be
analyzed separately using the supplied provenance flags.

The model judgments are exploratory, provisional annotations. Independent
expert evaluations are a separate evidence source and are not released here.
The public adapter reconstructs the 3×3 score matrix, agreement coefficients,
composition counts and counts of repeated/matched score variation. Full saved
judge reasons, claim annotations, source packets, blinding maps and expert
responses are not included. A local saved-response audit checked the existing
numeric tables against 294 retained source files without reading expert data;
that private-source check cannot be independently repeated from these numeric
projections alone. Inter-judge agreement is annotation consistency, not answer
correctness, human validation, or a quality treatment effect.

## Remaining requirements

Original inference requires matching source bytes, processed chunks, embedding
matrices, the configured Ollama generation/embedding models and hardware/runtime
conditions. Metadata record 2,853/293/850 chunks for UC1/UC2/UC3, 2,560 dimensions
and the frozen digests. Vectors and model weights are not bundled. The source
release is partial: all 56 originals are required for full-corpus retrieval.
Construction code is already available in the execution branch's
`src/responsible_agentic_workflows/retrieval/materialize.py`, ingestion modules
and `corpus/use_cases/UC2/materialize_uc2.py`. Regeneration is a new replication;
it does not replace the frozen indexes or reproduce original machine timings.

[Source redistribution decisions](source-documents/RIGHTS_AND_ATTRIBUTION.md)
use publisher terms and each frozen file's notices, separately from academic
clearance. Source documents retain their own rights; no blanket project licence
is applied to them. The corpus documentation identifies missing originals and
remaining index-construction/model requirements. Full inference reproduction
and independent semantic evaluation remain outside the verified capabilities.
