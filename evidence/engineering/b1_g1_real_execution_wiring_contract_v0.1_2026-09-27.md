# B1/G1 Real Execution Wiring Contract v0.1

Date: 2026-09-27
Base: ac22f1419ffbd3f3872c470c676b41517ba0f065
Status: prospective design, pre-implementation, pre-benchmark.

## Shared execution boundary

B1 and G1 MUST use the same graph topology, node implementations, prompt bundle,
model, retriever, top_k, state, execution guards, recorder, evidence formatter,
and terminal handling. The only behavioral condition-specific dependency is the
injected RecoveryPolicy. condition_metadata is logging-only and MUST NOT affect
execution or routing.

graph.py topology and the frozen 18-field WorkflowState MUST NOT change.
No guard-specific graph nodes, extra state fields, or routing edges are allowed.
Existing BEGIN_RECOVERY, MERGE_EVIDENCE, and graph finalizers remain unchanged.

## Real injected nodes

PLAN: one guarded model call from the question; produce a non-empty textual
execution plan in state.plan.

INITIAL_RETRIEVE: one guarded retrieval using the task question exactly; write
initial_retrieval. top_k is externally supplied and remains unfrozen here.

DRAFT: one guarded model call using question + plan + initial evidence; answer
only from supplied evidence; write current_answer_candidate.

INITIAL_CRITIC: one guarded StructuredCritic call over question, candidate and
current evidence; write CriticResult + CriticControlState; critic_iteration=1.

RECOVERY_POLICY: build RecoveryPolicyContext identically for both conditions;
invoke injected policy exactly once; record exactly one policy_decision.

RECOVERY_RETRIEVE: use the frozen deterministic recovery-query helper; one
guarded retrieval; write recovery_retrieval.

REVISE: one guarded model call using question + plan + current candidate +
current evidence + critic diagnostics; no gold/reference data; write candidate.

POST_RECOVERY_CRITIC: one guarded StructuredCritic call; update critic result
and control state; critic_iteration=2. No second policy invocation.

Current evidence means merged_evidence when present, otherwise initial_retrieval.
One deterministic formatter MUST be shared by DRAFT, REVISE and critic evidence
construction and preserve document_id, chunk_id, page, section and text without
reranking or changing retrieval order/scores.

## Guards and resource stopping

Before every model call:
build_resource_snapshot -> model_call_blockers.

Before every retrieval:
build_resource_snapshot -> retrieval_call_blockers.

After a recovery policy decision selecting recovery, but before graph entry to
BEGIN_RECOVERY:
build_resource_snapshot -> begin_recovery_blockers.

A guard block performs zero provider/tool calls, is not abstention, does not
fabricate/overwrite RecoveryDecision, and terminates through a runner-level
internal control-flow signal with:
status=resource_stopped, answer=None, abstained=False.

The runner records resource_stopped exactly once with stage and ordered
blocked_limits. No new graph edge/state field is introduced.

timeout_ms may remain present in ResourceLimits because that is the frozen type,
but MUST NOT affect B1/G1 policy outcomes or policy-time hard feasibility.
Timeout is enforced only by execution-level guards.

If the POLICY returns RESOURCE_STOP, preserve that decision, log
policy_decision, route through frozen FINALIZE_RESOURCE_STOP, then let the runner
record the single terminal resource_stopped event.

## Policy-decision logging

RecoveryDecision MUST NOT change.

selected_recovery_path:
- ACCEPT/ABSTAIN -> None
- REVISE_ONLY -> REVISE_ONLY
- RERETRIEVE_REVISE -> RERETRIEVE_REVISE
- RESOURCE_STOP -> reconstruct the already-selected path:
  REVISE_ONLY iff evidence_sufficiency=SUFFICIENT and unresolved_conflict=false;
  otherwise RERETRIEVE_REVISE.

This matches frozen B1 selection. Frozen G1 can reach RESOURCE_STOP only after
a non-null path is selected; conflict/no-worthy-path cases abstain earlier.
Tests MUST verify reconstruction against representative frozen-policy states.
No private policy methods or condition_metadata branching.

path_reserve_satisfied is derived from reason/action semantics:
- G1_RESOURCE_RESERVE_BLOCKED -> false
- successful G1 recovery reason codes -> true
- HARD_LIMIT_BLOCKED -> None
- B1, ACCEPT and ABSTAIN -> None.

## Event ownership and ordering

Injected successful stage nodes emit their own frozen stage event.
RECOVERY_POLICY emits policy_decision.
The runner owns exactly one terminal event and workflow_failed.

recovery_started is emitted only after BEGIN_RECOVERY has succeeded:
- RECOVERY_RETRIEVE emits it on the reretrieve branch before retrieval;
- REVISE emits it only on revise-only when recovery_retrieval is None.
Thus it is emitted exactly once without modifying graph.py.

Canonical successful ordering:
plan_completed -> initial_retrieval_completed -> draft_completed ->
initial_critic_completed -> policy_decision -> optional recovery_started ->
optional recovery_retrieval_completed -> optional revision_completed ->
optional post_recovery_critic_completed -> exactly one of
answer_accepted / abstained / resource_stopped.

Unhandled provider/retrieval/parser/state failures emit workflow_failed exactly
once and never become abstention. If a LoggedLanguageModel/LoggedRetriever
attempt recorded a model/retrieval error before the exception escaped, the run
status is tool_error; other unhandled execution/invariant/parser failures are
failed.

## Runner and prompts

Implement one shared immutable agentic result containing at least final_answer,
abstained, terminal_status, raw validated record, and final WorkflowState.

B1/G1 use one provisional versioned agentic prompt bundle. The bundle binds
PLAN/DRAFT/REVISE prompts plus the existing StructuredCritic prompt version.
RunConfiguration.prompt_version records that bundle ID. Final scientific prompt
content is frozen later. Prompts MUST NOT mention condition labels, ERGR, gold,
reference answers, expected correctness, scores, or policy selection.

## Known configuration gap

benchmark_config.schema.json currently lacks timeout_ms although ResourceLimits
supports it. Do not change the schema during wiring. If timeout is retained, a
prospective schema amendment is required before final experiment-config freeze.

Final freeze MUST also enforce b1_prompt_version == g1_prompt_version, even
though the current JSON schema does not express that cross-field equality.

## Qualification boundary

Only T901-T907 or in-memory synthetic tasks/documents may be used during wiring
and E2E qualification. T001-T030 MUST NOT execute.

Proposed implementation surface: add a dedicated shared agentic execution module
containing the runner/result, real-node assembler, deterministic evidence/prompt
formatters, guard signal/helpers, policy logging derivation, and event handling.
Do not expand graph.py or modify frozen policies/state.

PROSPECTIVE_DESIGN=YES
RESULT_DRIVEN_REVISION=NO
BENCHMARK_TASK_EXECUTION=NO
BENCHMARK_STARTED=NO
FROZEN_GRAPH_CHANGE=NO
FROZEN_STATE_CHANGE=NO
FROZEN_POLICY_CHANGE=NO
BENCHMARK_CONFIG_CHANGE=NO
