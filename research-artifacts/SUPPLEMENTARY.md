# Supplementary reproduction: Study B, boundary, Study C

This directory extends the existing Study A companion with three separate derived-data checking packages.
These scripts run locally with Python 3 and the standard library. No model inference, private data, or download is required.

From the repository root:

```bash
python3 research-artifacts/reproduce_supplementary.py --output /tmp/usn-supplementary-results
```

The output folder must not already exist. This creates three JSON result summaries under the chosen directory.

| Package | What the public files can verify | Scope boundary |
| --- | --- | --- |
| [Study B](study-b/README.md) | 144 recorded integrity rows; study design counts; arithmetic of source-reported token totals | Cannot reconstruct tokens, answers or success labels from native executions |
| [Resource boundary](resource-boundary/README.md) | 36 recorded integrity rows, resource-stopped statuses, arithmetic of reported totals | All 36 runs stopped; 0 released task completions |
| [Study C](study-c/README.md) | 18 secondary task grades, 32/36 points, consistency with reported operational aggregates | Post-hoc AI-assisted rating; not independent human validation or 108 independent ratings |

The Study A companion (`study-a/`) remains separate, as do the distinct per-study denominators and freeze records. Published source record hashes are provenance references, not proof of independent re-execution.
