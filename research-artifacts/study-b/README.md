# Study B — synthetic mechanism evaluation

**Status:** Public companion data derived from recorded experimental evidence; not the original raw-run archive.

This controlled, fictional-source mechanism study includes 24 distinct task families (8 per use-case label), B1 and G1, and three repetitions per condition: 144 executions and 72 matched pairs. The original analysis reports 21/24 successful family outcomes for both policies, 72/72 identical final-output pairs, and an 11.84% reduction in model tokens for G1 (155,701 to 137,262). Four of six predefined recoverable families had successful recovery under both policies. The nine policy-action divergences occurred on three unresolved-conflict families.

## Included files

- `data/execution_integrity.csv`: 144 derived run IDs, statuses, and flags **recorded** by the original validation reports, plus native record hashes. The 144 raw native workflow records are **not included**. This CSV cannot independently re-run the original byte-level verifier.
- `data/reported_metrics.json`: historical aggregate results and exact source-file hashes; figures are transcribed from the source unified synthesis.
- `reproduce.py`: Python standard-library checks for balanced run IDs, the published recorded validation flags, reported token arithmetic, and the 11.84% reduction.

From the repository root: `python research-artifacts/study-b/reproduce.py --output /tmp/usn-study-b-reconstructed`

**Inference boundary:** Fictional documents and staged-evidence fixtures, not live dense retrieval. Task-level success and final-output identity are source-reported; no complete raw response/candidate set is released. Semantic ratings were AI-assisted and not independently human-adjudicated. The 72 repeated matched runs do not represent 72 independent task families. Recovery efficiency is conditional on the three conflict families, not a general reliability improvement.
