# Execution-only figure captions

## Figure 1 — Overall execution resource profile

Distributions of (a) total tokens, (b) model calls, (c) retrieval calls and (d) end-to-end latency in logged milliseconds for B0, B1 and G1. All 270 raw executions are retained (90 per condition: 30 tasks × 3 repetitions); points are descriptive execution observations and are not independent task replicates. Horizontal jitter affects the categorical coordinate only. Boxes show Q1–Q3 with a median line; whiskers reach the most extreme observation within 1.5 IQR. All observations, including outliers, are drawn. Labels n in the discrete-call panels give exact frequencies at each call count, making tied observations explicit. Black diamonds denote arithmetic means. Resource/time axes include zero. B1 versus G1 is the primary comparison; B0 is a supporting external reference. The figure contains no scored answer outcome.

## Figure 2 — Primary paired B1-versus-G1 resource differences

Task-level differences in (a) total tokens, (b) model calls, (c) retrieval calls and (d) end-to-end latency (logged ms), defined as G1 − B1. Each condition’s value is the arithmetic mean of its three frozen repetitions for the same task, yielding 30 paired tasks overall. Dots retain every paired task; exactly equal values are stacked only along the nonnumeric coordinate. Boxes show the difference distribution (Q1–Q3, median and 1.5-IQR whiskers), and black diamonds show mean paired differences. The dashed vertical reference is zero: negative differences indicate less resource/time for G1, positive differences indicate more. Limits are symmetric about zero. B0 is omitted because this is the primary matched B1/G1 comparison. No confidence intervals or significance tests are implied.

## Figure 3 — Paired execution resource differences by use case

G1 − B1 differences in (a) total tokens, (b) model calls, (c) retrieval calls and (d) logged latency (ms), separately for UC1, UC2 and UC3. The analysis unit is a paired task after arithmetic averaging of three repetitions within each task-condition (10 paired tasks per UC; 30 overall). Dots retain individual paired tasks, boxes summarize Q1–Q3/median/1.5-IQR whiskers, and black diamonds show UC-specific mean differences. Different task-marker shapes distinguish use cases without requiring color. Each metric uses the same symmetric difference scale across all three UCs, with a dashed zero reference; negative values indicate less resource/time for G1. B1/G1 is primary; the supporting B0 reference is omitted. This descriptive breakdown assesses execution-resource heterogeneity without scored-quality interpretation.

## Figure 4 — Logged recovery and control behavior

Operational telemetry for B1 and G1. (a) Counts of runs with a logged recovery start, completed recovery re-retrieval, pre-recovery ABSTAIN action, final abstention flag, or resource-stop terminal status, with 90 executions per condition as the denominator. Every displayed event/flag occurs at most once per eligible run. (b) Completed verification model calls per run, averaged over three repetitions per task-condition; 30 task means per condition are shown, with quartile boxes, 1.5-IQR whiskers, median lines and mean diamonds. Verification counts use initial/post-recovery critic-completion events, not critic assessment labels. (c) The complete distribution of logged pre-recovery policy actions, totaling 90 runs per condition; hatch patterns identify action categories in grayscale. B0 is omitted because it lacks the agentic policy/event instrumentation. Recovery-finalization status is retained in the companion data and does not constitute judged recovery success; no correctness, grounding, or appropriate-abstention labels are used.

## Figure 5 — Latency distributions

Empirical cumulative distributions of logged end-to-end latency in milliseconds: (a) B0/B1/G1 overall (90 raw executions per condition), and (b–d) the primary B1/G1 comparison within UC1, UC2 and UC3 (30 raw executions per condition-UC). All 270 runs contribute to the overall panel; 180 agentic executions additionally contribute to the UC panels. Steps retain every raw execution latency, including the complete observed upper tail. Axes use a common linear millisecond scale beginning at zero; values are neither log-transformed nor normalized. Line styles and marker shapes distinguish conditions in grayscale. Raw repetitions describe the execution distribution rather than independent task-level evidence. B0 is supporting in the overall panel only; B1/G1 is primary. No quality/reliability conclusion or inferential claim is attached to latency.

## Supplementary Figure S1 — Input/output token decomposition

Input and output token distributions for B0/B1/G1, shown separately in (a) and (b), in unnormalized tokens. Each point is a task-condition arithmetic mean of exactly three raw repetitions (30 tasks per condition; all 270 source runs represented). Quartile boxes, median lines and 1.5-IQR whiskers summarize task-level distributions; black diamonds show arithmetic means. Both axes include zero. B1/G1 is the primary matched agentic comparison, and B0 is a supporting external reference. Separate token components prevent total-token differences from obscuring input versus generation resource use; no answer scoring or reference content enters the figure.

## Supplementary Figure S2 — Latency variability across repetitions

Within-task sample standard deviations of logged end-to-end latency (ms) for B0, B1 and G1. Every plotted value is computed from exactly three repetitions for one task-condition, with the n−1 denominator; there are 30 task-condition values per condition. Points, quartile boxes, median lines, 1.5-IQR whiskers and mean diamonds summarize the distribution of replication variability rather than uncertainty in a treatment effect. The axis begins at zero and uses the original millisecond unit without normalization. All 270 source executions contribute. B1/G1 is primary; B0 is supporting. Within-task token SDs are exactly zero for this frozen dataset and are retained in the numeric companion rather than displayed as a redundant chart. No judged outcome is used.

## Native publication sizes

Every family is independently rendered at 3.5 in (88.9 mm, single column) and 7.1 in (180.34 mm, full width). Single-column layouts stack panels; full-width layouts use a wider arrangement. Both retain minimum 7.5 pt text, 8.5 pt axis labels and 9 pt panel titles. Use the caption above for either native version; panel lettering and data are identical.
