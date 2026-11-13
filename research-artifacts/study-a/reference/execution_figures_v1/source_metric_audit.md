# Frozen 270-run execution metric audit

Status: PASS. Audit completed before plotting.

## Authoritative sources

- `/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1/run_records/*.json`: exactly 270 raw records, authoritative usage, timing, event and terminal-status telemetry.
- `RAW_RECORD_SHA256SUMS.txt` and `primary_benchmark_raw_freeze_manifest.json`: every raw record hash verified; raw bundle matches the frozen digest.
- Repository `evidence/engineering/primary_execution_order_v1.json`: authoritative run/task/condition/repetition mapping, frozen hash verified.
- Repository `benchmark/tasks/primary_benchmark_freeze_manifest.json`: use-case assignment comes from frozen task-file paths; task hashes verified without using reference answers or rubric content.
- Existing `analysis/runtime_v1` is a derived projection and is not used as the numeric source. No scored/evaluated dataset is parsed or joined.
- Raw execution code revision: `58b9e656dd57e62a5fb8640c2d3c990e4c93e530`. Instrumentation semantics checked read-only at that revision; no runner or workflow is executed.

## Design checks

TOTAL_RUNS=270; B0/B1/G1=90 each; UC1/UC2/UC3=90 each; UNIQUE_TASKS=30; exactly 3 repetitions for every task-condition.
Terminal telemetry: {'completed': 225, 'completed_after_recovery': 45}. All 270 raw observations are preserved; no run exclusion or task filtering.
B1/G1 task identities align exactly: 30 paired tasks overall, 10 in each UC.

## Metric inventory

| Metric | Unit | Definition / authoritative field | Applicability | Valid values / missing |
|---|---|---|---|---|
| input_tokens | tokens | usage.input_tokens; verified sum of model.calls[].input_tokens | all | n=270, range 4140–31744; 0 structural N/A |
| output_tokens | tokens | usage.output_tokens; verified sum of model.calls[].output_tokens | all | n=270, range 67–3485; 0 structural N/A |
| total_tokens | tokens | usage.total_tokens; input_tokens + output_tokens | all | n=270, range 4257–35229; 0 structural N/A |
| llm_calls | calls | usage.llm_calls; verified len(model.calls) | all | n=270, range 1–5; 0 structural N/A |
| retrieval_calls | calls | usage.retrieval_calls; verified len(retrieval.calls) | all | n=270, range 1–2; 0 structural N/A |
| tool_calls | calls | usage.tool_calls; separate from retrieval_calls, always 0 | all | n=270, range 0–0; 0 structural N/A |
| retries | recovery cycles | usage.retries; frozen AgenticRunner supplies recovery_iteration, not transport retries | all | n=270, range 0–1; 0 structural N/A |
| end_to_end_ms | ms | timing.end_to_end_ms; recorder elapsed monotonic milliseconds | all | n=270, range 13618.6–105588; 0 structural N/A |
| llm_ms | ms | timing.llm_ms; verified sum of model-call latency_ms | all | n=270, range 10633.6–97051.2; 0 structural N/A |
| retrieval_ms | ms | timing.retrieval_ms; verified sum of retrieval-call latency_ms | all | n=270, range 2943.22–8520.32; 0 structural N/A |
| error_count | errors | len(errors); not an outcome score | all | n=270, range 0–0; 0 structural N/A |
| completed_execution | 0/1 per run | status in {completed, completed_after_recovery} | all | n=270, range 1–1; 0 structural N/A |
| resource_stop | 0/1 per run | status == resource_stopped | all | n=270, range 0–0; 0 structural N/A |
| final_abstention | 0/1 per run | final_output.abstained; logged action, not correct/incorrect abstention | all | n=270, range 0–1; 0 structural N/A |
| recovery_trigger_count | triggers | policy_decision.details.selected_action in {REVISE_ONLY, RERETRIEVE_REVISE} | B1/G1 | n=180, range 0–1; 90 structural N/A |
| recovery_attempt_count | starts | count(events[].event_type == recovery_started) | B1/G1 | n=180, range 0–1; 90 structural N/A |
| recovery_retrieval_count | completed stages | count(recovery_retrieval_completed events) | B1/G1 | n=180, range 0–1; 90 structural N/A |
| revision_completed_count | completed stages | count(revision_completed events) | B1/G1 | n=180, range 0–1; 90 structural N/A |
| post_recovery_verification_count | completed calls | count(post_recovery_critic_completed events); frozen node executes one model call | B1/G1 | n=180, range 0–1; 90 structural N/A |
| verification_calls | completed calls | count(initial_critic_completed) + count(post_recovery_critic_completed); no critic assessment labels used | B1/G1 | n=180, range 1–2; 90 structural N/A |
| abstention_event_count | events | count(abstained events) | B1/G1 | n=180, range 0–1; 90 structural N/A |
| policy_decision_count | decisions | count(policy_decision events) | B1/G1 | n=180, range 1–1; 90 structural N/A |
| pre_recovery_abstention | 0/1 per run | selected_action == ABSTAIN at the logged policy decision | B1/G1 | n=180, range 0–1; 90 structural N/A |
| recovery_finalized | 0/1 per run | status == completed_after_recovery; also checked revision and post-recovery verification events | B1/G1 | n=180, range 0–1; 90 structural N/A |
| prepolicy_input_tokens | tokens | policy_decision.details.input_tokens_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 9491–17114; 90 structural N/A |
| prepolicy_output_tokens | tokens | policy_decision.details.output_tokens_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 289–2004; 90 structural N/A |
| prepolicy_total_tokens | tokens | policy_decision.details.total_tokens_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 9809–17982; 90 structural N/A |
| prepolicy_llm_calls | calls | policy_decision.details.llm_calls_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 3–3; 90 structural N/A |
| prepolicy_retrieval_calls | calls | policy_decision.details.retrieval_calls_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 1–1; 90 structural N/A |
| prepolicy_retries | recovery cycles | policy_decision.details.retries_used; direct pre-decision usage snapshot | B1/G1 | n=180, range 0–0; 90 structural N/A |

All reported token totals are checked against individual model-call telemetry; no missing provider-token fields. Call counts and model/retrieval timing sums are cross-checked. The end-to-end unit is the logged millisecond throughout.

## Control semantics and unavailable measures

- `retries` is a bounded recovery-cycle counter, supplied by `recovery_iteration` in the frozen runner. Network/provider retry counts are not separately logged and are unavailable.
- Recovery requested and recovery started are distinguished. In these records each requested path starts and reaches logged revision/post-recovery verification; resource-stop count is zero. B0 has no agentic event trace or policy decision, so event-derived control metrics are N/A for B0 rather than invented zeros.
- Verification calls count completed initial/post-recovery critic invocations only. Critic assessment content, support/grounding labels, release flags and evidence-sufficiency labels are neither exported nor used.
- `completed_after_recovery` is operational finalization, including runs that end in abstention. It does not establish answer correctness, support, reliability improvement, or successful recovery in a judged sense. No successful-recovery quality metric is available or constructed.
- `final_abstention` is the raw final abstention flag. `abstention_event_count` and pre-recovery ABSTAIN are distinct operational events/actions; no correct/incorrect abstention labeling.
- Action divergence compares logged selected actions; event-trace divergence compares ordered event_type lists, for the same task and repetition. This is a descriptive trace comparison, not a quality effect.
- Tool calls are logged separately and are all zero. The core retrieval/tool panel therefore reports actual retrieval calls; it does not relabel a sum as a measured tool quantity.
- Configuration limits, model identity, provider response IDs, retrieved text/scores, answer content/citations, critic judgments, references, rubric labels, scoring and expert results are outside this execution-analysis dataset.

## Analysis and figure decisions

- Core metrics fixed by the requested design: total tokens, model calls, retrieval calls, end-to-end latency. All appear in Figures 1–3; no result-driven subset is selected.
- For each task-condition compute the arithmetic mean of exactly three repetitions. Pair B1/G1 by task and compute G1 mean − B1 mean. Negative means less resource/time for G1. Repetitions are not independent tasks.
- Figures 1 and 5 retain raw executions only as descriptive distributions (90 per condition; 30 per condition-UC). Figure 4 reports operational counts with denominators and task-mean verification-call distributions. B0 is supporting reference only.
- Sample standard deviation uses n−1. Quartiles use linear interpolation (NumPy method="linear"). Box whiskers extend to the most extreme observation within 1.5 IQR; every observation is additionally shown, including outliers. Black diamonds mark arithmetic means; box center lines mark medians. No confidence intervals, significance tests or inferential claims.
- Latency stays on a linear millisecond scale with all data included and zero visible. No silent transform; no log plot is needed for the observed range.
- Supplement S1 separates input/output token resources. Supplement S2 shows within-task latency sample SD across three repetitions: replication variability is distinct from marginal latency distribution. Every within-task token SD is zero, documented numerically; a redundant all-zero token-variability chart is omitted.

## Mutation and scoring boundaries

The regeneration pipeline hashes protected benchmark/corpus/scoring/expert artifacts before and after. Hashing is integrity checking only: no scoring or expert content is parsed, modeled, plotted or used for metric selection. Git HEAD/status are checked before and after; outputs are written only under execution_figures_v1.
