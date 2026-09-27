# Primary Analysis and Visualization Contract v0.1

Status: PRE-RESULT FROZEN CANDIDATE
Date: 2026-09-27

## Principle
Analysis is specified before inspection of primary benchmark outcomes.
B1 vs G1 is the primary matched agentic comparison.
B0 vs B1 vs G1 is a supporting three-condition comparison.
No condition may be selected for presentation because it looks favorable.

## Core reporting
Report task-level and aggregate results with appropriate uncertainty for:
- correctness / rubric score;
- grounding and evidence support;
- reliability and terminal status;
- correct/incorrect abstention where applicable;
- latency;
- input, output and total tokens;
- LLM calls;
- retrieval calls;
- retries/recovery;
- resource-stop and recovery-policy behavior where recorded.

## Required comparative tables
1. Overall B0/B1/G1 descriptive results.
2. Primary B1-vs-G1 matched comparison.
3. Results by UC1/UC2/UC3.
4. Results by frozen task type.
5. Resource-use comparison.
6. Reliability/control outcomes.
7. Abstention/insufficient-evidence results.
8. Recovery-path outcomes.
9. Effect sizes and confidence intervals for prespecified primary comparisons.
10. Per-task supplementary table for all T001-T030.

## Required figures
Figures SHOULD compare multiple conditions or dimensions where scientifically
meaningful rather than producing only isolated single-series plots.

Required families:
1. B0/B1/G1 overall performance comparison.
2. B1-vs-G1 primary comparison with uncertainty.
3. Condition x use-case comparison.
4. Condition x task-type comparison.
5. Score distributions across repetitions/tasks.
6. Latency distributions.
7. Token-use distributions.
8. LLM/retrieval-call comparison.
9. Quality-versus-total-token trade-off.
10. Quality-versus-latency trade-off.
11. Quality-versus-LLM-call trade-off.
12. Reliability/terminal-outcome comparison.
13. Recovery and abstention comparison.
14. Task-level paired B1-vs-G1 difference visualization.

Use box/violin/ECDF/scatter/paired-point/bar-with-CI forms as appropriate to
the actual metric type. Do not combine incompatible units on a misleading
shared axis.

## Statistical discipline
Use the frozen repeated-task structure.
Report descriptive statistics and uncertainty.
Use paired/matched analyses for B1 vs G1 where the design supports them.
Report effect sizes with confidence intervals alongside inferential tests.
Do not treat repetitions from the same task as independent evidence when the
analysis requires task-level clustering/matching.
Any exploratory post-hoc analysis MUST be explicitly labelled exploratory.

## Thesis and paper outputs
Thesis:
- full comparative tables;
- full breakdowns;
- distributions;
- resource-quality plots;
- reliability/control plots;
- supplementary per-task results.

Paper:
- smaller subset selected by direct relevance to RQ1/RQ3 and readability,
  while preserving null/negative findings and the primary B1-vs-G1 comparison.

No primary benchmark result has been inspected in defining this contract.
