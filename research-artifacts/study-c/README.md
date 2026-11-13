# Study C — real-retrieval supplement

**Status:** Public derived task-level results. Raw source passages, full generated answers, and raw workflow logs are not included.

Study C comprises 18 distinct tasks, six each in UC1/UC2/UC3 and six each in sufficient-evidence/missing-evidence/grounding strata. Two policies and three repetitions yield 108 usable outcomes and 54 matched execution pairs, as reported in the original study. All final outputs are reported identical within each matched pair. This is **not** 108 independent semantic ratings.

The separate **post-hoc AI-assisted secondary semantic evaluation** assigned 15 grade-2, two grade-1, and one grade-0 tasks, for **32/36 possible points per policy (88.89%)**. Grade 2 represents complete core content or appropriate withholding; it is not a validated full-correctness or benchmark accuracy rate. T21008 was graded 0 for an unjustified abstention on an answerable task. One original provider failure was replaced by a documented verified outcome; the failed attempt's zero usage must not be counted as model-token savings.

## Included files

- `data/secondary_task_scores.csv`: derived nonverbatim task-level grades, strata, answerability, abstention flags and response-truncation flags; no source text, reference answers, personal records, or complete responses.
- `data/reported_metrics.json`: separate source-reported execution/resource and latency aggregates, their provenance and limitations.
- `reproduce.py`: recomputes the **18-task** ordinal distribution and 32/36 summary from published task rows; checks structural consistency of the reported execution aggregates. It cannot reconstruct those aggregates from raw logs.

From the repository root: `python research-artifacts/study-c/reproduce.py --output /tmp/usn-study-c-reconstructed`

**Inference boundary:** These grades reflect the historical source-based AI-assisted review accepted by the researcher; they are not independent expert judgments, not blinded human scoring and not a prespecified primary endpoint. This release does not make substantive correctness independently auditable without the original tasks, references, source documents and raw answers, which remain subject to separate rights and content review. The reported paired latency interval spans zero.
