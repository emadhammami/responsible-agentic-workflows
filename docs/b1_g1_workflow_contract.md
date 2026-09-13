# B1/G1 Common Workflow Contract

**Status:** Design frozen; B1 policy implemented, G1 policy implemented, shared workflow execution semantics frozen, LangGraph workflow implementation pending
**Primary comparison:** B1 vs G1
**Primary treatment:** Recovery decision policy
**Benchmark started:** No

## 1. Purpose

This document specifies the common B1/G1 agentic workflow.

The purpose is to isolate the primary treatment as narrowly as possible.

B1 and G1 should therefore be implementations of one common workflow graph
with shared nodes and shared state. The condition-specific behavior should be
injected through a recovery policy rather than implemented as two substantially
different workflow graphs.

This specification is pre-benchmark. It may be refined during engineering, but
it must not be changed later in response to primary benchmark performance.

## 2. Design principle

The primary comparison is:

**B1 fixed recovery policy vs G1 evidence- and resource-aware recovery policy**

The comparison is not:

- no critic vs critic;
- simple RAG vs agentic RAG;
- fewer capabilities vs more capabilities;
- smaller resource allowance vs larger resource allowance.

Both conditions receive the same core agentic capabilities and the same
initial externally imposed resource limits.

## 3. Shared graph (frozen routing)

The shared common graph is frozen. It consists of exactly the following
named nodes and edges. B1 and G1 use this identical graph; the only
condition-specific element is the recovery policy object injected into
`RECOVERY_POLICY`.

    START
      -> PLAN
      -> INITIAL_RETRIEVE
      -> DRAFT
      -> INITIAL_CRITIC
      -> RECOVERY_POLICY
           -> FINALIZE_ACCEPT        -> END
           -> FINALIZE_ABSTAIN       -> END
           -> FINALIZE_RESOURCE_STOP -> END
           -> BEGIN_RECOVERY
                -> REVISE            (path: REVISE_ONLY)
                -> RECOVERY_RETRIEVE (path: RERETRIEVE_REVISE only)
                     -> MERGE_EVIDENCE
                          -> REVISE
                -> POST_RECOVERY_CRITIC
                     -> POST_RECOVERY_FINALIZE
                          -> END

Edge semantics:

- `START`, `PLAN`, `INITIAL_RETRIEVE`, `DRAFT`, `INITIAL_CRITIC`, and
  `RECOVERY_POLICY` are sequential; every run traverses them exactly once.
- `RECOVERY_POLICY` selects exactly one outgoing branch:
  - `ACCEPT` routes to `FINALIZE_ACCEPT`;
  - `ABSTAIN` routes to `FINALIZE_ABSTAIN`;
  - `RESOURCE_STOP` routes to `FINALIZE_RESOURCE_STOP`;
  - `REVISE_ONLY` and `RERETRIEVE_REVISE` both route to `BEGIN_RECOVERY`.
- `BEGIN_RECOVERY` emits the `recovery_started` event, then:
  - for `REVISE_ONLY`, routes directly to `REVISE`;
  - for `RERETRIEVE_REVISE`, routes to `RECOVERY_RETRIEVE`, then
    `MERGE_EVIDENCE`, then `REVISE`.
- `REVISE` routes to `POST_RECOVERY_CRITIC`; the two are unconditional.
- `POST_RECOVERY_FINALIZE` is terminal. The workflow never returns to
  `RECOVERY_POLICY` and never invokes a second recovery cycle.
- `END` is the single terminal node.

At the `RECOVERY_POLICY` node, the policy may issue at most one recovery
action per run. The workflow-level configuration `MAX_RECOVERY_CYCLES` is
frozen at `1`; after `POST_RECOVERY_FINALIZE` the run terminates unconditionally.
The LangGraph code implementing this graph is not yet written; the routing
above is the frozen specification it must implement.

## 4. One graph, injected policy

B1 and G1 should not be implemented as unrelated graphs.

The preferred implementation is one shared LangGraph state graph whose
condition-specific recovery decision is supplied through a small policy
interface.

Conceptually:

    CommonAgenticWorkflow(policy=B1FixedRecoveryPolicy)

and:

    CommonAgenticWorkflow(policy=G1EvidenceResourceRecoveryPolicy)

All non-policy nodes should use the same implementation objects in both
conditions.

This architecture makes the treatment difference explicit and auditable.

## 5. Shared workflow state (frozen)

The workflow state contains exactly the following 18 conceptual fields, and no
others. This is the authoritative field list; prose elsewhere in this
document must agree with it.

| # | Field | Notes |
| --- | --- | --- |
| 1 | `task_id` | task identity |
| 2 | `question` | original task question |
| 3 | `execution_mode` | `engineering` or `benchmark` (no other values) |
| 4 | `condition_metadata` | benchmark condition label; **logging and correlation only** |
| 5 | `plan` | shared plan structure |
| 6 | `initial_retrieval` | chunks + provenance from `INITIAL_RETRIEVE` |
| 7 | `recovery_retrieval` | chunks + provenance from `RECOVERY_RETRIEVE` (empty before recovery) |
| 8 | `merged_evidence` | current evidence context after `MERGE_EVIDENCE` (equals `initial_retrieval` content ordering pre-recovery) |
| 9 | `current_answer_candidate` | latest draft or post-revision candidate |
| 10 | `latest_CriticResult` | full structured critic assessment (all fields, including diagnostics) |
| 11 | `latest_CriticControlState` | the five control-relevant fields the release predicate and policy consume |
| 12 | `critic_iteration` | identifies the critic assessment/iteration associated with the latest `CriticResult` and the associated `policy_decision` log; no independent numeric convention is frozen in this pass |
| 13 | `recovery_iteration` | `0` until `BEGIN_RECOVERY`; `1` after |
| 14 | `latest_RecoveryDecision` | `RecoveryDecision` (action + reason code) from `RECOVERY_POLICY` (unset before that node) |
| 15 | `ResourceLimits` | immutable configured limits |
| 16 | `terminal_status` | terminal `RunStatus` |
| 17 | `final_answer` | released answer, or unset |
| 18 | `abstained_flag` | `true` exactly when the run's terminal decision is `ABSTAIN` |

The workflow state must never contain benchmark reference answers, reference
evidence, adjudication labels, benchmark correctness scores, or other gold
information.

### State boundary (frozen)

- The 18-field table above is the complete workflow-state contract. Any field
  not in that table is forbidden in the state.
- Field-ownership clarifications (none of these add fields to the state):
  - `query` and `subgoals` are not separate state fields; they are conceptual
    contents of `plan`.
  - Chunk and provenance data live inside the retrieval and evidence fields
    (`initial_retrieval`, `recovery_retrieval`, `merged_evidence`); they are
    not separate state fields.
  - `unsupported_claims`, `incomplete_support`, `evidence_gaps`, and
    `explanation` are field-level details of `latest_CriticResult`, not
    separate state fields.
  - `support_status`, `evidence_sufficiency`, `unresolved_conflict`, and
    `gap_types` are field-level details of `latest_CriticControlState` (or its
    source `CriticResult`), not separate state fields.
  - `action` and `reason_code` are field-level details of
    `latest_RecoveryDecision`, not separate state fields.
  - `ResourceSnapshot` is not a mutable state field. It is constructed from
    the run recorder (model-call, retrieval-call, and token accounting) and
    passed read-only to the policy and hard execution guard at decision time.
  - `cited_chunk_ids` is not part of the frozen state in the current contract.
- Forbidden specific fields: `revision_count`, `recovery_attempted`,
  `recovery_completed`, and any independent mutable resource counters. Call
  counters and token counters live in the run recorder; the workflow reads
  them only as immutable `ResourceSnapshot` instances at decision time and
  never holds separate mutable counters.
- The following are forbidden in the workflow state:
  - benchmark reference answers;
  - benchmark reference evidence;
  - human adjudication labels;
  - benchmark correctness or scoring information;
  - any label derived from benchmark gold.

### Condition metadata (frozen, logging and correlation only)

The `condition_metadata` field (field 4) holds the benchmark condition label
(`B1` or `G1`) and exists **for logging and experiment correlation only**.

It is not a permissible behavioral input to any component, including:

- the planner;
- retrieval (initial or recovery);
- draft generation;
- `StructuredCritic`;
- revision;
- recovery retrieval;
- evidence merge;
- the hard execution guard;
- `B1FixedRecoveryPolicy`;
- `G1ERGRPolicy`.

The only mechanism by which the two conditions can behave differently at
runtime is the injected recovery-policy object: `B1FixedRecoveryPolicy` for
B1 runs and `G1ERGRPolicy` for G1 runs. The scientific treatment difference
is the policy object, not the condition label.

## 6. Planner contract

The planner is shared by B1 and G1.

Its role is to transform the task into a bounded execution plan suitable for
document retrieval and answer generation.

The exact planner prompt and structured schema remain open.

The planner must not:

- inspect benchmark gold information;
- know whether the run belongs to B1 or G1 unless technically unavoidable;
- alter its planning strategy based on benchmark results;
- allocate a larger initial execution allowance to G1.

The planner output should be bounded and machine-validated.

## 7. Retrieval contract

Initial retrieval is shared between B1 and G1.

The same retrieval implementation, frozen corpus, embedding model, vector
store, chunking policy, ranking method, and initial retrieval parameters must
be used for comparable runs.

Recovery retrieval uses the same retrieval infrastructure.

A recovery query may differ from the initial query because it can be informed
by the shared critic's identified evidence gap.

The method that constructs a recovery query must be shared between B1 and G1.

## 8. Draft-generation contract

The draft-generation node is shared.

It receives:

- the original question;
- the relevant plan information;
- retrieved evidence with provenance.

It produces an answer candidate.

The same prompt version and generation configuration must be used in B1 and G1.

The draft node does not decide whether its answer should be accepted.

## 9. Shared critic contract

The critic is a shared capability and must use the same implementation,
model identity, prompt version, and structured output contract in B1 and G1.

The critic evaluates the answer candidate against the runtime evidence.

It should report assessment information, not choose the workflow action.

The critic must therefore not directly output:

- `REVISE_ONLY`;
- `RERETRIEVE_REVISE`;
- `RESOURCE_STOP`;
- a B1/G1-specific action;
- a resource-allocation decision.

The critic result separates answer support from evidence sufficiency.

The conceptual fields are:

### Answer-support status

`support_status` describes whether the current answer candidate is supported by
 the evidence currently available to the workflow.

The values are:

- `SUPPORTED`;
- `PARTIAL_SUPPORT`;
- `UNSUPPORTED`.

### Evidence sufficiency

`evidence_sufficiency` describes whether the currently available evidence is
 adequate to support a defensible answer to the task.

The values are:

- `SUFFICIENT`;
- `INSUFFICIENT`.

### Additional evidence assessment

The critic should also expose:

- `unresolved_conflict`, as a boolean;
- identified unsupported claims;
- identified incomplete support;
- evidence gaps;
- structured explanation required for auditing.

Answer support and evidence sufficiency are intentionally separate.

An answer may be unsupported because the draft is poor even when sufficient
evidence exists, while an answer may be impossible to support because the
available evidence is itself insufficient.

A shared release predicate should be derived from the critic result.

Conceptually, `release_ok` is true only when:

- `support_status` is `SUPPORTED`;
- `evidence_sufficiency` is `SUFFICIENT`;
- no unresolved conflicting evidence is present.

The exact critic schema and release predicate are frozen.

The same release predicate must be used by B1 and G1. The recovery policy must
not redefine what counts as an acceptable supported answer.

The critic must not have access to benchmark reference answers or reference
evidence.

## 10. Separation of assessment and control

The critic answers:

> What is the evidential state of the current answer?

The recovery policy answers:

> Given that evidential state and the applicable control rules, what happens
> next?

This separation is a methodological requirement.

It prevents the G1 treatment from being hidden inside a different critic prompt
or critic implementation.

## 11. Recovery-policy interface

Both conditions use the same policy interface.

Conceptually, the policy receives:

- critic result;
- recovery iteration;
- runtime resource snapshot;
- applicable hard limits.

It returns one action:

- `ACCEPT`;
- `REVISE_ONLY`;
- `RERETRIEVE_REVISE`;
- `ABSTAIN`;
- `RESOURCE_STOP`.

It also returns a structured reason code suitable for logging.

The policy must not receive benchmark gold information.

## 12. B1 fixed recovery policy

B1 uses a fixed, pre-specified policy.

For the first critic result, the working rule is:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### Otherwise

B1 selects among the shared recovery paths using a fixed mapping from the shared
critic state, without any resource-value reasoning.

The working mapping is:

1. If `evidence_sufficiency` is `SUFFICIENT` and no unresolved conflicting
   evidence is present, select `REVISE_ONLY`.
2. Otherwise select `RERETRIEVE_REVISE`.

The selected path is then subject to the common hard execution guard:

- For `RERETRIEVE_REVISE`, the guard must permit both a recovery retrieval call
  and a revision call.
- For `REVISE_ONLY`, the guard must permit a revision call.

If the hard guard does not permit the required calls for the selected path, the
policy returns `RESOURCE_STOP` instead of initiating that path.

B1 does not select recovery according to:

- remaining token percentage;
- estimated recovery value;
- remaining model-call allowance beyond hard feasibility;
- remaining retrieval allowance beyond hard feasibility;
- resource-efficiency optimization.

B1 therefore follows the same bounded recovery response mapping for every
non-supported initial draft.

After the single recovery cycle, B1 uses the shared post-recovery finalization
rule.

## 13. G1 evidence- and resource-aware recovery policy

G1 uses the same critic result and shared resource accounting.

For the first critic result:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### Otherwise

G1 first applies a frozen recovery-worthiness rule to the shared critic state.

The recovery-worthiness rule determines whether the current state is
recoverable at all, and if so, which shared recovery path is appropriate.

Working structure:

1. If the rule selects no further recovery, return `ABSTAIN`.
2. If the rule selects `REVISE_ONLY`, check the path-specific hard-feasibility
   requirement and the frozen path-specific resource reserve for `REVISE_ONLY`.
   If both are satisfied, return `REVISE_ONLY`; otherwise return
   `RESOURCE_STOP`.
3. If the rule selects `RERETRIEVE_REVISE`, check the path-specific
   hard-feasibility requirement and the frozen path-specific resource reserve
   for `RERETRIEVE_REVISE`.
   If both are satisfied, return `RERETRIEVE_REVISE`; otherwise return
   `RESOURCE_STOP`.

The path-specific hard-feasibility requirements are defined by the common hard
execution guard:

- `REVISE_ONLY` requires that the guard can permit the revision model call.
- `RERETRIEVE_REVISE` requires that the guard can additionally permit one
  recovery retrieval call.

The reserve rules are path-specific and are part of the treatment. The reserve
for `REVISE_ONLY` must not be conflated with the reserve for
`RERETRIEVE_REVISE`, and neither reserve may include the initial draft cost,
which has already been paid.

The recovery-worthiness rule and the two path-specific reserve rules are
frozen and implemented in `src/responsible_agentic_workflows/workflow/g1_policy.py`.

They were selected from engineering evidence and prior literature, not from
primary benchmark outcomes, and they will not be re-derived from benchmark
results.

## 14. Shared hard execution guard

A common hard execution guard applies to B1 and G1.

Its purpose is operational safety and experimental comparability, not the
scientific treatment.

The hard guard prevents a node from starting when doing so would violate a
frozen execution ceiling.

Possible ceilings include:

- maximum model calls;
- maximum retrieval or tool calls;
- maximum retries;
- workflow token limit where enforceable;
- execution timeout.

The same hard ceilings must apply to B1 and G1.

B1 may therefore be stopped by the common hard guard even though its policy is
not resource-adaptive.

This is distinct from G1 proactively using resource state as part of its
recovery decision.

## 15. Recovery implementation

The recovery implementation is shared by B1 and G1.

When `REVISE_ONLY` is selected:

1. revise the current answer using the currently available evidence and the
   shared critic result;
2. invoke the same critic again.

When `RERETRIEVE_REVISE` is selected:

1. construct the recovery retrieval query using the exact frozen algorithm in
   the runtime contract (built only from the original `question` and, when
   non-empty, the current critic result's `evidence_gaps`; `current evidence`
   is not an input to query construction);
2. perform bounded recovery retrieval;
3. combine the permitted evidence according to the frozen context policy;
4. revise the current answer;
5. invoke the same critic again.

Neither condition receives a stronger recovery implementation.

The number of permitted recovery cycles is the same for B1 and G1.

## 16. Shared post-recovery finalization

To keep the treatment narrow, the shared design uses the same
post-recovery finalization rule in B1 and G1.

After the final permitted recovery cycle:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### If the shared `release_ok` predicate is false

Return:

`ABSTAIN`

unless the common hard execution guard has already produced a distinct
resource-stopped outcome.

This post-recovery rule is identical for B1 and G1.

This rule is frozen.

Using a shared post-recovery rule prevents condition differences from being
introduced after both systems have already consumed the same recovery
capability.

## 17. Terminal outcomes (frozen)

The workflow terminates in exactly one of the five `RunStatus` values below.
This mapping is frozen, and it applies identically to B1 and G1.

`answer` and `abstained` are the two output fields that together distinguish
terminal outcomes. A run with `abstained = true` is a deliberate abstention,
is distinguishable from system failure, and is a legitimate terminal outcome
in scoring.

### `completed` — before recovery

- `ACCEPT` (the initial critic produced `release_ok = true`, the pre-recovery
  policy returned `ACCEPT`, and `FINALIZE_ACCEPT` terminated the run):
  - `status`: `completed`;
  - `answer`: the initial draft candidate, unchanged;
  - `abstained`: `false`.
- `ABSTAIN` (the initial critic produced `release_ok = false`, the pre-recovery
  policy returned `ABSTAIN`, and `FINALIZE_ABSTAIN` terminated the run; recovery
  was not attempted):
  - `status`: `completed`;
  - `answer`: `None`;
  - `abstained`: `true`.

### `completed_after_recovery`

- `ACCEPT` (the pre-recovery policy returned a recovery action,
  `POST_RECOVERY_CRITIC` produced `release_ok = true`, and
  `POST_RECOVERY_FINALIZE` returned `ACCEPT`):
  - `status`: `completed_after_recovery`;
  - `answer`: the revised (post-revision) answer candidate;
  - `abstained`: `false`.
- `ABSTAIN` (the pre-recovery policy returned a recovery action,
  `POST_RECOVERY_CRITIC` produced `release_ok = false`, and
  `POST_RECOVERY_FINALIZE` returned `ABSTAIN`):
  - `status`: `completed_after_recovery`;
  - `answer`: `None`;
  - `abstained`: `true`.

A run with `abstained = true` is a deliberate abstention, is distinguishable
from system failure, and is a legitimate terminal outcome in scoring. Both
ABSTAIN terminal mappings have `answer = None` and `abstained = true`; they
share the `final_output` shape exactly, and they differ only in `RunStatus`
(`completed` vs `completed_after_recovery`).

### `resource_stopped`

- the pre-recovery policy returned `RESOURCE_STOP`, or the shared hard
  execution guard blocked a required call before the run could terminate
  normally;
- `answer`: `None`;
- `abstained`: `false`.

`POST_RECOVERY_FINALIZE` never produces `RESOURCE_STOP`. After the single
recovery cycle it terminates unconditionally in `ACCEPT`
(`release_ok = true`) or `ABSTAIN` (`release_ok = false`). A
`resource_stopped` outcome following recovery arises only from a
pre-recovery `RESOURCE_STOP` decision or an execution-level hard guard that
blocked a required call before `POST_RECOVERY_FINALIZE` could run.

A resource stop is not an abstention. It must not be counted as a correct
abstention in scoring, and the blocked `BlockedLimit` value must be preserved
in the recorded event payload. When a guard blocks a path, the run terminates
in `resource_stopped` without performing the blocked external call, and it is
never converted to `ABSTAIN`.

### `tool_error`

- a tool or model call failed in a way that cannot be retried within the
  frozen limits;
- `answer`: `None`;
- `abstained`: `false`.

The failed run is preserved, including the failed call and its error.

### `failed`

- the workflow itself failed (state corruption, schema validation failure,
  unexpected exception);
- `answer`: `None`;
- `abstained`: `false`.

Failures are never silently converted to abstention.

### Additional terminal-output rules

- An unreleased candidate (a draft that never passed a `release_ok = true`
  verdict at the terminating critic) is never published in
  `final_output.answer`, even when a `resource_stopped` or `tool_error` run
  has a partial candidate in state.
- `cited_chunk_ids` remains empty until explicit citation generation is
  frozen and enabled; it must not be populated heuristically in the
  interim.

## 18. Resource accounting

Resource accounting is shared.

Every model call and retrieval attempt should be recorded using the common
logging infrastructure.

The policy must use the same resource counters that are later reported by the
benchmark.

No hidden condition-specific counters or unlogged recovery calls are allowed.

The runtime resource state is descriptive for B1 except where common hard
limits apply.

It is an explicit control input for G1.

## 19. Required policy logging

Every recovery-policy decision must produce a single `policy_decision` event
containing, at decision time:

- `policy_id` (the identity of the injected recovery policy object);
- `action` (`ACCEPT`, `REVISE_ONLY`, `RERETRIEVE_REVISE`, `ABSTAIN`, or
  `RESOURCE_STOP`);
- `reason_code` (the structured `RecoveryReasonCode`);
- `critic_iteration` and `recovery_iteration`;
- the full `CriticControlState` fields supplied to the policy;
- the full `ResourceSnapshot` fields supplied to the policy
  (`llm_calls_used`, `retrieval_calls_used`, `retries_used`,
  `input_tokens_used`, `output_tokens_used`, `total_tokens_used`);
- remaining capacity for each of the four limits relevant to the selected
  path (`max_llm_calls`, `max_retrieval_calls`, `max_retries`,
  `max_total_tokens`), recorded as `null` when that limit is unconfigured;
- the `HardRecoveryFeasibility` entry computed for the selected path (only
  when a recovery path was selected).

The event is a pure logging artifact of the policy inputs and output. It must
not include benchmark gold information, and it must not be altered after
emission.

## 20. Required workflow events (frozen)

The implementation must make it possible to reconstruct the execution path.

Exactly the following 13 workflow event identifiers are required. This list is
frozen: no other identifier may be introduced and no listed identifier may be
renamed. Note in particular that `critic_completed` is not an event
identifier; critic results are reported by `initial_critic_completed` and
`post_recovery_critic_completed`.

1. `plan_completed`;
2. `initial_retrieval_completed`;
3. `draft_completed`;
4. `initial_critic_completed`;
5. `policy_decision`;
6. `recovery_started`;
7. `recovery_retrieval_completed` (emitted only on the `RERETRIEVE_REVISE`
   path);
8. `revision_completed`;
9. `post_recovery_critic_completed`;
10. `answer_accepted`;
11. `abstained`;
12. `resource_stopped`;
13. `workflow_failed` (emitted only when the run terminates in failure).

The `policy_decision` event must preserve, at decision time:

- policy identity (`policy_id`);
- selected action (`ACCEPT`, `REVISE_ONLY`, `RERETRIEVE_REVISE`, `ABSTAIN`,
  or `RESOURCE_STOP`);
- structured reason code;
- critic iteration and recovery iteration;
- the full `CriticControlState` fields supplied to the policy;
- the full `ResourceSnapshot` values supplied to the policy
  (`llm_calls_used`, `retrieval_calls_used`, `retries_used`,
  `input_tokens_used`, `output_tokens_used`, `total_tokens_used`);
- remaining capacity for each limit relevant to the selected path;
- the `HardRecoveryFeasibility` computed for the selected path.

The event must not contain benchmark reference answers, reference evidence,
adjudication labels, or benchmark correctness information.

## 21. Treatment-isolation matrix

| Component | B1 | G1 | Must match? |
| --- | --- | --- | --- |
| Planner | shared | shared | yes |
| Initial retrieval | shared | shared | yes |
| Draft generator | shared | shared | yes |
| Critic | shared | shared | yes |
| Recovery retrieval capability | shared | shared | yes |
| Revision implementation | shared | shared | yes |
| Recovery path capability set (REVISE_ONLY, RERETRIEVE_REVISE) | shared | shared | yes |
| Maximum recovery cycles | same | same | yes |
| Initial resource limits | same | same | yes |
| Hard execution guard | shared | shared | yes |
| Post-recovery finalization | shared | shared | yes |
| Recovery decision policy | fixed | evidence/resource-aware | no |
| Policy reason codes | condition-specific as needed | condition-specific as needed | no |

The intended scientific treatment is therefore concentrated in the
pre-recovery policy decision.

## 22. Testable implementation invariants

Before real benchmark execution, synthetic tests should demonstrate that:

1. B1 and G1 instantiate the same graph structure;
2. all non-policy nodes are shared;
3. both conditions use the same critic implementation;
4. both conditions use the same recovery implementation;
5. both conditions receive the same initial resource limits;
6. B1 policy does not branch on resource state except common hard feasibility;
7. G1 policy can branch on the frozen evidence and resource inputs;
8. neither policy can access benchmark gold information;
9. only the configured number of recovery cycles can occur;
10. all model and retrieval calls are logged;
11. all policy decisions are reconstructable from recorded events;
12. resource stops remain distinct from abstentions;
13. failed executions are preserved;
14. no benchmark task content is required by workflow unit tests;
15. both conditions have access to the same shared recovery path set
    (REVISE_ONLY and RERETRIEVE_REVISE), and both can select either path when
    the policy indicates that path;
16. the shared post-recovery finalization node is reached after both shared
    recovery paths.

## 23. Engineering-test boundary

Before the workflow is frozen, synthetic engineering tasks may be used to test:

- graph routing;
- state transitions;
- critic schema validation;
- policy actions;
- hard-limit behavior;
- recovery-cycle bounds;
- logging;
- error handling.

These tests are not scientific benchmark runs.

UC1 benchmark performance must not be used to tune the policy.

## 24. Decisions still open

This contract intentionally does not yet freeze:

- planner prompt and structured output;
- exact planning granularity;
- critic prompt wording and prompt-version identifier
  (the critic structured-output schema and release predicate are frozen);
- numerical resource limit values:
  - maximum model calls;
  - maximum retrieval calls;
  - retry limits;
  - total workflow token ceiling;
  - per-call output limit;
  - timeout;
- final abstention text;
- workflow configuration identifiers;
- UC2/UC3 corpus preparation.

The following execution semantics are frozen even though the shared
LangGraph workflow code has not been implemented:

- the common graph routing with exactly the frozen node set (`START`,
  `PLAN`, `INITIAL_RETRIEVE`, `DRAFT`, `INITIAL_CRITIC`, `RECOVERY_POLICY`,
  `FINALIZE_ACCEPT`, `FINALIZE_ABSTAIN`, `FINALIZE_RESOURCE_STOP`,
  `BEGIN_RECOVERY`, `REVISE`, `RECOVERY_RETRIEVE`, `MERGE_EVIDENCE`,
  `POST_RECOVERY_CRITIC`, `POST_RECOVERY_FINALIZE`);
- `MAX_RECOVERY_CYCLES = 1` per run, with `recovery_iteration` moving from
  0 to 1 at most once and the policy invoked exactly once per run;
- deterministic recovery query construction with zero LLM calls, using
  `question` plus non-empty critic `evidence_gaps` in the frozen listing
  format and excluding the frozen forbidden inputs;
- evidence merge for `RERETRIEVE_REVISE` (retain current order, append unseen
  `chunk_id` in recovery rank order, first-occurrence-wins, no score fusion,
  no reranking);
- exactly one revision model call per recovery, with the frozen revision
  inputs (question, plan, merged evidence, current draft, critic assessment,
  critic `evidence_gaps` and `unsupported_claims`);
- exactly one post-recovery critic call using the identical
  `StructuredCritic` implementation as the initial critic;
- `POST_RECOVERY_FINALIZE` as the unconditional terminal node after recovery,
  applying the shared `release_ok` rule;
- the shared hard execution guard and its blocked-limit vocabulary
  (five `BlockedLimit` values: `LLM_CALL_LIMIT`, `RETRIEVAL_CALL_LIMIT`,
  `RETRY_LIMIT`, `TOKEN_LIMIT`, `TIMEOUT_LIMIT`; the first four are
  evaluated by `calculate_hard_recovery_feasibility`, `TIMEOUT_LIMIT` is
  reserved and not yet evaluated; guard checks are execution-level and are
  distinct from policy-time feasibility, are evaluated before each external
  call, and a blocked path terminates in `RESOURCE_STOP` without any
  external call and without conversion to `ABSTAIN`);
- terminal outcome representation (the five `RunStatus` literals:
  `completed`, `completed_after_recovery`, `resource_stopped`, `tool_error`,
  `failed`), with the frozen `answer` and `abstained` value per status and
  the unreleased-candidate exclusion rule;
- the workflow event names (exactly 13, listed in §20);
- the workflow-state gold boundary (allowed and forbidden categories listed
  in §5);
- policy-time resource accounting (`retries_used = recovery_iteration`,
  snapshot-derived counters, dual pre-policy feasibility computation).

These remaining decisions must be resolved and frozen before scientific
benchmark execution.

## 25. Implementation sequence

The intended implementation sequence is:

1. define typed shared workflow state — done;
2. define critic-result contract — done;
3. define recovery-action and policy protocols — done;
4. implement B1 fixed policy — done;
5. implement G1 policy — done;
6. implement hard recovery feasibility — done;
7. implement common shared nodes and assemble one common LangGraph workflow;
8. extend execution logging for policy and stage events;
9. test all routing with synthetic components;
10. run synthetic real-model engineering validation;
11. freeze prompts, policies, and resource limits, including numerical
    resource-limit values;
12. only then permit scientific benchmark execution.

Steps 1 through 6 are complete.

## 26. Current boundary

At this checkpoint:

- B0 engineering validation is complete;
- contribution positioning is recorded;
- algorithmic novelty is not claimed;
- B1 policy, G1 policy, the critic contract and release predicate, hard
  recovery feasibility, and the shared typed workflow state are implemented;
- the common shared workflow nodes and the single LangGraph workflow graph
  have not been implemented;
- the scientific benchmark has not started.

The next engineering step after review of this contract is to implement the
common shared nodes and assemble the single LangGraph workflow.
