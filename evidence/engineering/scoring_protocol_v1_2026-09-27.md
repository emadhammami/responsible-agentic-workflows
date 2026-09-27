# Primary Benchmark Scoring Protocol v1

Status: FROZEN POST-EXECUTION / PRE-SCORING / PRE-ANALYSIS
Date: 2026-09-27

This protocol supplements evaluation_rubric.md v0.1. It does not
retroactively claim that the implementation choices below were frozen
before primary execution.

## Frozen sources
- Raw records: 270
- Raw bundle SHA256:
  cd6299e13820a22eaad7e6737102972b268f844af82795272b642c23574ca073
- Task-source bundle SHA256:
  66b5b98fb343f9910b983b705f9afa37bc8da72e2f9600e8a15051684635a9bf
- Rubric SHA256:
  b032c2c8b756f3d8f433815b3bb0830b7dd9b348aa065842b6d846c898f57ad6

## Blinding
Evaluators receive run_id, task question, generated answer, reference
answer/evidence, and required evidence needed for scoring, but not B0/B1/G1
condition labels, policy actions, token use, latency, or recovery status.

## Correctness
Primary score is the frozen ordinal 2/1/0 rubric.
Task success is defined as correctness=2.
No lexical-similarity metric is used as benchmark correctness.

## Human evaluation
Evaluator A independently scores all 270 runs.
Evaluator B independently scores the frozen 90-run secondary subset.
The subset contains exactly one repetition for every task-condition pair
and is selected deterministically before answer inspection.

Pre-adjudication judgments are retained.
Disagreements are discussed after independent scoring.
If agreement cannot be reached, a third human adjudicator evaluates only
the unresolved item.

Report exact agreement and quadratic-weighted Cohen's kappa for 2/1/0
correctness on the 90-run subset. Abstention agreement is reported
separately using exact agreement and Cohen's kappa.

## Claim segmentation and grounding
A factual claim is a minimal independently verifiable proposition.
Compound statements are split when their components can independently be
true or false. Purely stylistic, structural, or conversational text is
not a factual claim. Exact duplicate claims within one answer count once.

Claim segmentation is performed blinded to condition before grounding
labels are assigned and is stored as raw scoring data.

Each claim is labeled:
SUPPORTED, PARTIALLY_SUPPORTED, UNSUPPORTED, or CONTRADICTED
using evidence available to the workflow.

For an abstention containing no substantive factual claim, claim count is
zero and claim-level grounding is N/A.

Report counts and rates separately. Unsupported-claim rate is:
UNSUPPORTED / factual claims. Contradicted claims are reported separately.

## Abstention
Use the frozen rubric categories:
correct_abstention, failed_to_abstain, incorrect_abstention,
not_applicable.

## Retrieval metrics
Use unique retrieved evidence across calls.
For answerable tasks report:
- initial reference-chunk recall;
- cumulative reference-chunk recall;
- initial required-document recall;
- cumulative required-document recall;
- whether at least one reference chunk was retrieved.

For insufficient-evidence tasks these recall metrics are N/A.
No subjective irrelevant-chunk metric is used in the primary analysis.

## Resource/runtime
Use only frozen runtime fields:
input/output/total tokens, LLM calls, retrieval calls, retries,
end_to_end_ms, llm_ms, retrieval_ms.

## Recovery interpretation
Policy action and recovery occurrence are directly reportable.
Because primary records do not preserve a scorable pre-recovery answer,
the study will not claim direct beneficial/neutral/harmful intervention
classification from before-vs-after answer quality.
Final correctness among recovered runs may be reported descriptively.

## Statistical analysis
Primary comparison: B1 versus G1.
B0 comparisons are supporting context.

The task is the inferential cluster. The three repetitions are first
aggregated within each task-condition pair.

For primary B1-G1 endpoints report paired task-level differences and
95% paired bootstrap confidence intervals using 10,000 task resamples
with seed 20260912.

Secondary two-sided paired permutation tests use 100,000 sign-flip
samples with seed 20260912 for:
1. mean correctness;
2. unsupported-claim rate;
3. total tokens;
4. LLM calls;
5. end-to-end latency.

Holm adjustment is applied across these five tests.
Abstention, retrieval, recovery, and use-case analyses are reported
descriptively with uncertainty where appropriate because of smaller
subsets and sparse events.

No composite benchmark score is created.
Null and negative results are retained.
