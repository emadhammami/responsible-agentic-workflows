# B1/G1 Runtime Control Contracts

**Status:** Frozen; G1 decision logic, critic contract, and resource-feasibility implementation committed
**Primary comparison:** B1 vs G1
**Primary treatment:** Recovery decision policy
**Benchmark started:** No

## 1. Purpose

This document refines the common B1/G1 workflow architecture into explicit
runtime data contracts.

It specifies:

- the structured critic result;
- the shared release predicate;
- the policy-visible critic state;
- resource limits and resource snapshots;
- the common recovery-policy interface;
- policy actions and reason codes;
- the logging contract required to reconstruct decisions.

It does not yet freeze numerical resource limit values.

Those decisions must be resolved before scientific benchmark execution.

## 2. Methodological boundary

B1 and G1 use the same:

- workflow graph;
- planner;
- initial retrieval;
- draft generator;
- critic;
- release predicate;
- recovery implementation;
- hard execution ceilings;
- post-recovery finalization.

The primary treatment remains the pre-recovery decision policy.

The critic assesses the current answer and evidence.

The policy decides what to do with that assessment.

The policy must not redefine what counts as a releasable answer.

## 3. Critic result contract

The critic should return one machine-validated structured result.

Conceptually:

    CriticResult
      schema_version
      support_status
      evidence_sufficiency
      unresolved_conflict
      gap_types
      unsupported_claims
      incomplete_support
      evidence_gaps
      explanation

The exact Python representation may use immutable dataclasses, enums, tuples,
or equivalent typed structures.

### 3.1 Support status

`support_status` uses exactly these values:

- `SUPPORTED`;
- `PARTIAL_SUPPORT`;
- `UNSUPPORTED`.

It describes the relationship between the current answer candidate and the
evidence available to the workflow.

### 3.2 Evidence sufficiency

`evidence_sufficiency` uses exactly these values:

- `SUFFICIENT`;
- `INSUFFICIENT`.

It describes whether the available evidence is adequate to support a defensible
answer to the task.

Support and sufficiency are intentionally separate.

### 3.3 Unresolved conflict

`unresolved_conflict` is a boolean.

It is true only when the evidence contains a conflict material to the requested
answer that remains unresolved in the current answer candidate.

The field describes evidence state.

It is not itself a policy action.

### 3.4 Gap types

`gap_types` provides categorical evidence-state information.

The vocabulary is:

- `DRAFT_GROUNDING`;
- `MISSING_EVIDENCE`;
- `INCOMPLETE_EVIDENCE`;
- `EVIDENCE_CONFLICT`.

An empty tuple means that the critic identified no material gap.

The vocabulary is frozen.

New categories must not be introduced in response to benchmark performance.

### 3.5 Diagnostic text

The full critic result may also contain:

- `unsupported_claims`;
- `incomplete_support`;
- `evidence_gaps`;
- `explanation`.

These fields support recovery-query construction, debugging, and auditability.

They are not automatically policy inputs.

Free-text critic explanation must not become an undocumented control channel
for G1.

## 4. Shared release predicate

The release predicate is a pure shared function of the structured critic
result.

Conceptually:

    release_ok =
        support_status == SUPPORTED
        and evidence_sufficiency == SUFFICIENT
        and unresolved_conflict == false

The same function must be used by B1 and G1.

Neither policy may override it.

When `release_ok` is true, both conditions return `ACCEPT` before recovery.

The release predicate must not depend on:

- condition identity;
- remaining tokens;
- remaining calls;
- latency;
- benchmark gold information;
- free-text critic explanation.

## 5. Critic-result invariants

The implementation should reject malformed critic results.

Required invariants include:

1. every enum value belongs to the frozen vocabulary;
2. `gap_types` contains no duplicates;
3. diagnostic collections contain no duplicate entries;
4. empty diagnostic strings are rejected;
5. `unresolved_conflict=true` requires `EVIDENCE_CONFLICT` in `gap_types`;
6. `release_ok=true` requires no unresolved conflict;
7. the result contains no benchmark reference answer or evaluation score;
8. policy actions are not fields of `CriticResult`.

Semantic combinations that are unusual but possible should not be rejected
without justification.

For example, an answer candidate can contain one supported statement while the
evidence remains insufficient to answer the full task.

## 6. Policy-visible critic state

The recovery policy should receive a restricted projection of the critic
result rather than unrestricted critic text.

Conceptually:

    CriticControlState
      support_status
      evidence_sufficiency
      unresolved_conflict
      gap_types
      release_ok

The G1 policy must not branch directly on:

- `unsupported_claims` text;
- `incomplete_support` text;
- `evidence_gaps` free text;
- critic explanation;
- raw benchmark question text;
- document text;
- benchmark gold information.

This restriction keeps the treatment structured, inspectable, and
reproducible.

The shared recovery implementation may use critic diagnostic text after the
policy has already selected `REVISE_ONLY` or `RERETRIEVE_REVISE`.

## 7. Resource accounting source of truth

Runtime resource state must be derived from the same recorded execution
activity that produces final benchmark usage measurements.

The implementation must not maintain an independent hidden resource counter for
G1.

Recorded model-call usage is the source for:

- LLM calls used;
- input tokens used;
- output tokens used;
- total tokens used.

Recorded retrieval attempts are the source for:

- retrieval calls used.

Retry accounting must also use one shared recorded source.

A policy-time resource snapshot may be stored in workflow state for
reproducibility, but it must be derived from authoritative recorded activity.

## 8. Resource limits contract

A common immutable `ResourceLimits` value should be supplied to both B1 and G1.

The working fields are:

    ResourceLimits
      max_llm_calls
      max_retrieval_calls
      max_retries
      max_total_tokens
      timeout_ms

A limit may be optional only where the experiment configuration explicitly
declares it unused.

The same values must be supplied to B1 and G1 for matched runs.

Per-call output-token limits remain part of model/workflow configuration and
must also be matched between conditions.

The numerical values remain open at this checkpoint.

## 9. Resource snapshot contract

A policy-time immutable snapshot should contain:

    ResourceSnapshot
      llm_calls_used
      retrieval_calls_used
      retries_used
      input_tokens_used
      output_tokens_used
      total_tokens_used

Derived values may include:

    llm_calls_remaining
    retrieval_calls_remaining
    retries_remaining
    total_tokens_remaining

Remaining values must be derived from limits and used counters.

They must not be maintained as separately mutable counters.

If a limit is not configured, its corresponding remaining value should be
represented explicitly as unavailable rather than approximated.

## 10. Latency treatment

Latency remains an important reported benchmark outcome.

At this checkpoint, wall-clock latency is not a G1 policy input.

This avoids making the primary treatment depend on transient machine load,
operating-system scheduling, or other nondeterministic runtime effects.

If latency is later proposed as a policy input, that change requires explicit
pre-benchmark justification and freeze.

## 11. Common hard-feasibility check

Before starting a recovery path, the shared execution guard determines whether
the requested path can begin without violating the determinable hard execution
ceilings represented in the policy-time resource snapshot.

The hard-feasibility calculation is deterministic and shared by B1 and G1.

One bounded recovery cycle consumes one retry/recovery slot.

The frozen path requirements are:

### REVISE_ONLY

The path requires:

- at least one remaining LLM-call slot when that limit is configured;
- at least one remaining retry/recovery slot when that limit is configured;
- non-exhausted total-token capacity when that limit is configured.

It does not require a recovery retrieval-call slot.

### RERETRIEVE_REVISE

The path requires:

- at least one remaining LLM-call slot when that limit is configured;
- at least one remaining retrieval-call slot when that limit is configured;
- at least one remaining retry/recovery slot when that limit is configured;
- non-exhausted total-token capacity when that limit is configured.

If a corresponding resource limit is `None`, that limit is disabled and does
not block the path.

The token hard guard does not estimate future model-call token consumption.
`TOKEN_LIMIT` blocks policy-time hard feasibility only when configured total
token capacity is already exhausted.

`timeout_ms` is not evaluated by the policy-time hard-feasibility calculator
because the current `ResourceSnapshot` deliberately contains no elapsed-runtime
field. The timeout remains a shared execution-level hard ceiling to be enforced
by the workflow runtime.

When more than one determinable limit is exhausted, all applicable blockers are
reported in this fixed order:

1. `LLM_CALL_LIMIT`;
2. `RETRIEVAL_CALL_LIMIT`, where applicable;
3. `RETRY_LIMIT`;
4. `TOKEN_LIMIT`.

The result is represented as:

    HardRecoveryFeasibility
      recovery_path
      feasible
      blocked_limits

Hard feasibility is not the G1 treatment. Both B1 and G1 consume the same
calculation.

## 12. Frozen G1 recovery-worthiness and completion-reserve rule

The G1 Evidence- and Resource-Gated Recovery policy uses only the restricted
`CriticControlState`, the shared hard-feasibility result, and the common
resource snapshot and limits.

The pre-recovery decision order is frozen and implemented in
`src/responsible_agentic_workflows/workflow/g1_policy.py` as follows.

### 12.1 Release first

If `critic.release_ok` is true:

    ACCEPT / RELEASE_OK

This decision occurs before any recovery-path feasibility or reserve check.

### 12.2 Unresolved evidence conflict

If `critic.release_ok` is false and `critic.unresolved_conflict` is true:

    ABSTAIN / G1_RECOVERY_NOT_WORTHWHILE

The current treatment does not contain a source-priority or conflict-arbitration
mechanism. A material unresolved conflict therefore does not trigger a bounded
recovery attempt.

### 12.3 Sufficient evidence with an unreleased answer

If:

- `critic.release_ok` is false;
- `critic.evidence_sufficiency` is `SUFFICIENT`; and
- `critic.unresolved_conflict` is false;

then recovery is considered worthwhile and the selected path is:

    REVISE_ONLY

This treats the remaining problem as answer construction or grounding rather
than missing evidence.

### 12.4 Insufficient but bounded-recoverable evidence

If:

- `critic.release_ok` is false;
- `critic.evidence_sufficiency` is `INSUFFICIENT`;
- `critic.unresolved_conflict` is false; and
- `critic.gap_types` contains `MISSING_EVIDENCE` or
  `INCOMPLETE_EVIDENCE`;

then recovery is considered worthwhile and the selected path is:

    RERETRIEVE_REVISE

The structured gap signal supplies the pre-specified justification for one
additional bounded retrieval/revision cycle.

### 12.5 Insufficient evidence without a bounded retrieval signal

If evidence is `INSUFFICIENT`, there is no unresolved conflict, and neither
`MISSING_EVIDENCE` nor `INCOMPLETE_EVIDENCE` is present in `gap_types`:

    ABSTAIN / G1_RECOVERY_NOT_WORTHWHILE

G1 does not trigger retrieval merely because the answer failed the release
predicate.

### 12.6 Shared hard-feasibility gate

After G1 selects a recovery path, it must use the supplied
`HardRecoveryFeasibility` entry for that path.

A missing feasibility entry for the selected path is malformed runtime context
and must raise an error rather than being converted into a policy outcome.

If the selected path is hard-infeasible:

    RESOURCE_STOP / HARD_LIMIT_BLOCKED

G1 must not reinterpret a common hard-limit failure as abstention.

### 12.7 Path-specific G1 completion reserve

If the selected path is hard-feasible, G1 applies an additional deterministic
completion-reserve check.

This reserve is the resource-aware component of the treatment and is distinct
from the shared hard guard.

For a configured limit, the required remaining capacity is:

#### REVISE_ONLY

- at least two remaining LLM-call slots;
- at least one remaining retry/recovery slot.

#### RERETRIEVE_REVISE

- at least two remaining LLM-call slots;
- at least one remaining retrieval-call slot;
- at least one remaining retry/recovery slot.

A corresponding limit of `None` is disabled and automatically satisfies that
reserve dimension.

The two LLM-call slots represent the shared recovery structure that follows the
policy decision:

1. the revision generation call; and
2. the required shared post-recovery critic call.

The retrieval slot for `RERETRIEVE_REVISE` represents its one bounded recovery
retrieval call.

The retry slot represents the one bounded recovery cycle.

If the path-specific completion reserve is unavailable:

    RESOURCE_STOP / G1_RESOURCE_RESERVE_BLOCKED

If the reserve is available:

    REVISE_ONLY / G1_REVISE_ONLY

or:

    RERETRIEVE_REVISE / G1_RERETRIEVE_REVISE

according to the selected path.

### 12.8 No token-percentage or latency reserve

The G1 completion reserve does not introduce:

- a token percentage threshold;
- an estimated average recovery-token cost;
- a safety multiplier;
- an empirical token threshold;
- a wall-clock latency threshold.

Token exhaustion remains governed by the common hard guard.

No future token-cost estimate is used by the frozen G1 rule.

Latency remains a measured benchmark outcome and shared execution-level concern,
not a G1 policy input.

### 12.9 Treatment isolation

The frozen G1 rule must not branch on:

- free-text critic explanation;
- diagnostic string contents;
- raw benchmark question text;
- document text;
- benchmark gold information;
- human adjudication;
- final correctness labels;
- wall-clock latency.

The exact structured treatment inputs are therefore limited to the frozen
policy-visible critic state, common resource state, common limits, and shared
hard-feasibility result.

The rule must not be changed in response to primary benchmark outcomes.

## 13. Recovery-policy context

Both conditions use the same conceptual policy interface.

The policy receives:

    RecoveryPolicyContext
      critic
      recovery_iteration
      resources
      limits
      hard_recovery_feasibility

where `critic` is the restricted `CriticControlState`.

The interface may contain configuration identifiers required for reproducible
logging.

It must not contain:

- benchmark reference answer;
- benchmark reference evidence;
- adjudication result;
- correctness score;
- task difficulty label derived from benchmark outcomes.

## 14. Recovery actions

The policy action enum contains exactly:

- `ACCEPT`;
- `REVISE_ONLY`;
- `RERETRIEVE_REVISE`;
- `ABSTAIN`;
- `RESOURCE_STOP`.

These actions are mutually exclusive.

`REVISE_ONLY` and `RERETRIEVE_REVISE` are distinct shared recovery paths. Both
end at the same shared revision and critic re-evaluation nodes. Only
`RERETRIEVE_REVISE` additionally performs bounded recovery retrieval.

`RESOURCE_STOP` is not an abstention.

`ABSTAIN` is not a runtime failure.

`ACCEPT` is valid before recovery only when the shared release predicate is
true.

## 15. Policy decision contract

Conceptually:

    RecoveryDecision
      action
      reason_code
      policy_id

For G1, the logged event must additionally identify the frozen recovery-rule
and resource-reserve rule versions used by the decision.

A decision must be reproducible from its recorded structured inputs and frozen
policy configuration.

Free-text rationale may be logged for debugging but must not be required to
reconstruct the action.

## 16. Reason-code vocabulary

Common reason codes are:

- `RELEASE_OK`;
- `HARD_LIMIT_BLOCKED`.

B1-specific reason codes are:

- `B1_FIXED_REVISE_ONLY`;
- `B1_FIXED_RERETRIEVE_REVISE`.

G1-specific reason codes are:

- `G1_RECOVERY_NOT_WORTHWHILE`;
- `G1_REVISE_ONLY`;
- `G1_RERETRIEVE_REVISE`;
- `G1_RESOURCE_RESERVE_BLOCKED`.

`G1_RESOURCE_RESERVE_BLOCKED` is used for either path-specific reserve, and the
logged event must identify which path the reserve check applied to.

These names describe why the pre-recovery action was selected.

They are not scientific outcome labels.

The vocabulary is frozen and matches the reason codes implemented in
`control.py`.

## 17. B1 fixed-policy decision rule

The B1 rule is intentionally simple and fixed.

Conceptually:

    if release_ok:
        ACCEPT
    else if path-specific hard feasibility allows the selected path:
        path-specific shared recovery path
    else:
        RESOURCE_STOP

The fixed path mapping is:

    if release_ok:
        ACCEPT
    else if evidence_sufficiency == SUFFICIENT and not unresolved_conflict:
        REVISE_ONLY
            -> path-specific hard feasibility check for REVISE_ONLY
    else:
        RERETRIEVE_REVISE
            -> path-specific hard feasibility check for RERETRIEVE_REVISE

The corresponding reason codes are:

    ACCEPT
      -> RELEASE_OK

    REVISE_ONLY
      -> B1_FIXED_REVISE_ONLY

    RERETRIEVE_REVISE
      -> B1_FIXED_RERETRIEVE_REVISE

    RESOURCE_STOP
      -> HARD_LIMIT_BLOCKED

B1 does not use the raw resource snapshot to optimize recovery.

Changing tokens or remaining-call values while holding `release_ok`, the
structured critic state, and path-specific hard feasibility constant must not
change the B1 action.

## 18. G1 decision-rule skeleton

The G1 rule is frozen and implemented.

Numerical resource-limit values are not yet frozen.

Conceptually:

    if release_ok:
        ACCEPT
    else:
        evaluate frozen recovery-worthiness rule

    if recovery is not worthwhile:
        ABSTAIN
    else if selected_path hard feasibility is not satisfied:
        RESOURCE_STOP
    else if selected_path frozen reserve is unavailable:
        RESOURCE_STOP
    else:
        selected_path

where `selected_path` is one of:

- `REVISE_ONLY`;
- `RERETRIEVE_REVISE`.

The recovery-worthiness rule and the path-specific reserve rules determine
which of the two shared recovery paths, if any, is selected.

The G1 recovery-worthiness rule is frozen in `g1_policy.py`:

- `unresolved_conflict` is true → `ABSTAIN`
- `evidence_sufficiency` is `SUFFICIENT` → `REVISE_ONLY`
- gap types include `MISSING_EVIDENCE` or `INCOMPLETE_EVIDENCE` →
  `RERETRIEVE_REVISE`
- otherwise → `ABSTAIN`

The path-specific reserve rules are frozen in `g1_policy.py`:

- `REVISE_ONLY` requires 2 LLM calls and 1 retry
- `RERETRIEVE_REVISE` requires 2 LLM calls, 1 retrieval call, and 1 retry
- `None` limit means disabled (no lower bound)

The corresponding reason classes are:

    ACCEPT
      -> RELEASE_OK

    ABSTAIN
      -> G1_RECOVERY_NOT_WORTHWHILE

    RESOURCE_STOP
      -> HARD_LIMIT_BLOCKED
          or G1_RESOURCE_RESERVE_BLOCKED

    REVISE_ONLY
      -> G1_REVISE_ONLY

    RERETRIEVE_REVISE
      -> G1_RERETRIEVE_REVISE

## 19. Recovery-worthiness constraints

The G1 recovery-worthiness function in `g1_policy.py` is deterministic.

It uses only the fields frozen as policy inputs:

- support status;
- evidence sufficiency;
- unresolved-conflict flag;
- categorical gap types.

The policy does not infer additional hidden signals from free text.

If a confidence score or other continuous critic signal is later proposed, its
definition, calibration procedure, and threshold must be specified before it
becomes a primary benchmark policy input.

## 20. Post-recovery boundary

The condition-specific recovery policy is invoked for the pre-recovery decision.

After the single permitted recovery cycle, B1 and G1 use the same shared
post-recovery finalization function.

Conceptually:

    if release_ok:
        ACCEPT
    else:
        ABSTAIN

A hard execution stop remains a distinct terminal outcome.

This shared finalization rule prevents a second condition-specific treatment
from being introduced after recovery.

## 21. Policy-decision event

Every pre-recovery policy decision should be logged as one structured workflow
event.

Working event type:

`policy_decision`

The event details should contain:

    policy_id
    decision_sequence
    critic_iteration
    support_status
    evidence_sufficiency
    unresolved_conflict
    gap_types
    release_ok
    recovery_iteration
    selected_action
    reason_code
    llm_calls_used
    retrieval_calls_used
    retries_used
    input_tokens_used
    output_tokens_used
    total_tokens_used
    llm_calls_remaining
    retrieval_calls_remaining
    retries_remaining
    total_tokens_remaining
    selected_recovery_path
    hard_recovery_feasible
    blocked_limits
    path_reserve_satisfied

where `selected_recovery_path` is the path the recovery-worthiness rule
indicated (`REVISE_ONLY`, `RERETRIEVE_REVISE`, or `NONE`),
`hard_recovery_feasible` is the path-specific hard-guard result, and
`path_reserve_satisfied` is the path-specific G1 reserve result when G1 is the
active policy.

For G1, the event should additionally contain the identifiers and inputs needed
to reconstruct the frozen recovery-worthiness and path-specific reserve
calculations.

The event must not contain benchmark gold information.

## 22. Integration with the existing run record

The existing run record already separates:

- individual retrieval calls;
- individual model calls;
- aggregate usage;
- timing;
- final output;
- workflow events;
- errors.

B1/G1 should extend this logging model rather than create a second scientific
run-record format.

Policy and stage information should be represented through structured workflow
events unless a later schema review demonstrates that a dedicated top-level
field is necessary.

The final aggregate usage must remain derivable from the same underlying
recorded calls used to produce policy-time resource snapshots.

## 23. Recorder implementation requirement

Before B1/G1 execution, the logging layer needs a public, validated way to append
structured workflow events.

The implementation should not mutate recorder-private event storage directly
from workflow nodes.

A small `record_event` interface should validate at least:

- non-empty event type;
- optional stage;
- object-or-null details;
- event ordering through the recorder's sequence counter.

This is an engineering requirement, not a scientific treatment difference.

The same event API must be used by B1 and G1.

## 24. Runtime-state relationship

The LangGraph workflow state may retain:

- latest critic result;
- latest policy decision;
- policy-time resource snapshot;
- recovery iteration;
- current execution outcome.

Authoritative cumulative resource accounting remains tied to recorded runtime
activity.

Duplicated mutable counters must be avoided.

## 25. Treatment-isolation tests

Synthetic unit tests should demonstrate at least the following before
real-model engineering validation:

1. identical `CriticResult` produces identical `release_ok` in B1 and G1;
2. both conditions accept whenever `release_ok=true`;
3. B1 recovery decision is unchanged when non-binding resource values change;
4. B1 stops when the common hard guard blocks the selected path;
5. B1 selects `REVISE_ONLY` when `evidence_sufficiency` is `SUFFICIENT` and
   `unresolved_conflict` is false, and selects `RERETRIEVE_REVISE` otherwise,
   given the same structured critic state;
6. G1 can abstain only through its frozen recovery-worthiness rule;
7. G1 can resource-stop through either path-specific hard infeasibility or its
   path-specific frozen reserve rule, with distinct reason codes;
8. G1 path-specific reserve checks are independent: a `REVISE_ONLY` reserve
   failure does not affect a `RERETRIEVE_REVISE` reserve decision;
9. changing critic diagnostic free text does not change G1 action when all
   structured policy inputs remain identical;
10. no policy receives benchmark gold information;
11. resource snapshots agree with the final recorded call and token usage;
12. `RESOURCE_STOP` never sets `abstained=true` solely because of the stop;
13. post-recovery finalization is identical in B1 and G1;
14. policy events contain sufficient structured information to reconstruct the
    selected action and the path-specific feasibility and reserve results.

## 26. Determinism requirement

Given:

- the same structured policy input;
- the same frozen policy configuration;
- the same resource snapshot;
- the same resource limits;

the policy must return the same action and reason code.

No random sampling is permitted inside the recovery policy itself.

Model stochasticity, if any, belongs to the shared model configuration rather
than the policy implementation.

## 27. Open decisions

The following remain deliberately open:

- final critic prompt wording and prompt-version identifier;
- whether diagnostic explanation is required in the prompt;
- numerical LLM-call limit;
- numerical retrieval-call limit;
- numerical retry limit;
- numerical total-token ceiling;
- timeout;
- per-call output-token limit;
- workflow configuration identifiers;
- UC2/UC3 corpus preparation.

The following are already frozen and therefore are not open:

- the critic structured-output schema and release predicate;
- the gap-type vocabulary, recovery-action vocabulary, and recovery-path
  vocabulary (see `src/responsible_agentic_workflows/workflow/control.py`);
- the exact G1 recovery-worthiness rule and the G1 path-specific reserve
  rules (implemented in `g1_policy.py`);
- the exact B1 fixed-policy decision rule (implemented in `b1_policy.py`);
- the shared hard execution guard and its blocked-limit vocabulary
  (five `BlockedLimit` values: `LLM_CALL_LIMIT`, `RETRIEVAL_CALL_LIMIT`,
  `RETRY_LIMIT`, `TOKEN_LIMIT`, `TIMEOUT_LIMIT`; the first four are
  evaluated by `calculate_hard_recovery_feasibility`, `TIMEOUT_LIMIT` is
  reserved and not yet evaluated);
- the terminal `RunStatus` vocabulary (five literals);
- the workflow event names;
- the workflow-state gold boundary;
- policy-time resource accounting (`retries_used = recovery_iteration`);
- `MAX_RECOVERY_CYCLES = 1` (a structural freeze, distinct from the
  separate numeric `ResourceLimits.max_retries` value, which is still open).

These remaining open decisions must be resolved using engineering
validation, methodological reasoning, and prior literature before the
scientific benchmark.

They must not be selected from primary benchmark performance.

## 28. Freeze sequence

The intended sequence is:

1. review this runtime contract; (done)
2. implement typed critic, resource, and policy interfaces; (done)
3. implement public structured event recording; (done)
4. test the interfaces using synthetic deterministic inputs; (done)
5. specify critic prompt and structured parser; (done)
6. specify G1 recovery-worthiness rule; (done)
7. specify G1 resource-reserve rule; (done)
8. freeze resource limits and output limits;
9. implement the common graph and shared nodes;
10. run synthetic real-model engineering validation;
11. freeze the full B1/G1 workflow configuration;
12. only then permit scientific benchmark execution.

## 29. Frozen execution semantics (shared, condition-identical)

The rules below are frozen normative requirements. They bind B1 and G1
identically. The LangGraph code that will implement them is not yet written;
none of these rules are an open decision.

### 29.1 Recovery-cycle bound

- `MAX_RECOVERY_CYCLES = 1` per run.
- `recovery_iteration` starts at `0` and may move to `1` at most once per
  run.
- The recovery policy is invoked exactly once per run, at
  `RECOVERY_POLICY`. It is never re-invoked after `POST_RECOVERY_FINALIZE`.
- `retries_used = recovery_iteration` is the policy-time accounting
  identity: the single recovery cycle consumes exactly one retry slot.
- `MAX_RECOVERY_CYCLES` is a workflow-configuration freeze. It is not the
  same quantity as `ResourceLimits.max_retries` (which remains an open
  numerical limit) and is not a count of model retries.

### 29.2 Resource snapshot (frozen field set)

The `ResourceSnapshot` consumed by the policy and the hard feasibility
calculator has exactly the following fields, in this order:

- `llm_calls_used`;
- `retrieval_calls_used`;
- `retries_used`;
- `input_tokens_used`;
- `output_tokens_used`;
- `total_tokens_used`.

- Every snapshot value must be derived from recorded execution activity
  using the same source of truth that produces the final benchmark usage
  measurement (see §7).
- The six fields are defined by these equations, applied to the recorded
  call/event stream up to the decision point:
  - `llm_calls_used` = number of recorded LLM call attempts (each model
    call the runtime issued, regardless of whether it succeeded);
  - `retrieval_calls_used` = number of recorded retrieval call attempts;
  - `retries_used` = `recovery_iteration` (0 before recovery, 1 after
    `BEGIN_RECOVERY`);
  - `input_tokens_used` = sum of `input_tokens` over recorded LLM calls;
  - `output_tokens_used` = sum of `output_tokens` over recorded LLM calls;
  - `total_tokens_used` = `input_tokens_used` + `output_tokens_used`.
- `retrieval_calls_used` counts every retrieval attempt, including those
  that completed and those that failed at the transport/tool level. A failed
  retrieval still consumes the retrieval-call slot; it is not refunded. The
  recorder's retrieval-call accounting is not being modified in this pass;
  the requirement is that workflow-level `retrieval_calls_used` reflects the
  attempted calls.
- A schema-valid failing retrieval attempt (query non-empty, `top_k >= 1`) is
  recorded through `record_retrieval(..., results=())` so that it contributes
  one count to `retrieval_calls_used`; the accompanying failure is reported
  through a separate error record. Invalid parameter invocations (empty
  query or `top_k < 1`) do not produce a retrieval-call record and are not
  counted.
- Unlike the model-call record (which carries an explicit `status` of
  `completed` or `failed`), the retrieval-call record does **not** carry a
  status field. The retrieval-call record identifies an attempted call and
  its ranked results; it is not stamped `completed` or `failed`.
- A snapshot is immutable once constructed for a decision. There is no
  second, mutable snapshot in the workflow state.

### 29.3 Pre-policy dual feasibility (frozen)

- Before the recovery policy is invoked, the runtime must compute
  `calculate_hard_recovery_feasibility` for **both** shared paths in the
  same pass, using the same `ResourceSnapshot` and the same
  `ResourceLimits`:
  - `HardRecoveryFeasibility(recovery_path=REVISE_ONLY, ...)`, and
  - `HardRecoveryFeasibility(recovery_path=RERETRIEVE_REVISE, ...)`.
- Both results are supplied to the policy via `RecoveryPolicyContext.
  hard_recovery_feasibility`.
- The policy must consume the supplied entries. It must not recompute
  feasibility from the snapshot and limits. Missing entries for the
  selected path are malformed context and must raise, not be silently
  converted to a policy outcome (mirroring §12.6 for G1).

### 29.4 Execution-level guard (frozen)

The execution-level guard is a distinct mechanism from
`calculate_hard_recovery_feasibility`. Feasibility is a policy-time
deterministic computation; the guard is a pre-call enforcement applied in
the workflow runtime.

- Before any model call node is invoked (draft, revision, or critic), the
  runtime must check:
  - remaining `max_llm_calls` (if configured);
  - remaining `max_total_tokens` (if configured), using only the recorded
    `total_tokens_used`, with no estimation of future token consumption.
- Before any retrieval node is invoked (initial or recovery retrieval),
  the runtime must check remaining `max_retrieval_calls` (if configured).
- Before `BEGIN_RECOVERY` is entered, the runtime must check remaining
  `max_retries` (if configured) against `retries_used + 1`, and confirm
  `recovery_iteration < MAX_RECOVERY_CYCLES`.
- `TIMEOUT_LIMIT` is an execution-level guard only. It is not part of the
  G1 policy input, is not evaluated by
  `calculate_hard_recovery_feasibility`, and its numerical `timeout_ms`
  value remains open.
- When a guard blocks a call or a transition:
  - the blocked external call is not performed;
  - the run terminates with `RunStatus = resource_stopped`;
  - the applicable `BlockedLimit` value is preserved verbatim in the
    recorded event payload;
  - the termination is **not** converted to `ABSTAIN`, **not** converted to
    `failed`, and **not** re-decided by the policy.
- All five `BlockedLimit` values appear in the runtime guard vocabulary;
  `calculate_hard_recovery_feasibility` evaluates the first four
  (`LLM_CALL_LIMIT`, `RETRIEVAL_CALL_LIMIT`, `RETRY_LIMIT`,
  `TOKEN_LIMIT`), consistent with §11.

### 29.5 Recovery query algorithm (frozen)

When the selected path is `RERETRIEVE_REVISE`, the recovery retrieval
query is constructed deterministically from `CriticResult.evidence_gaps` and
the original `question`, with zero LLM calls, by the exact algorithm below:

- If `evidence_gaps` is empty:
  - `recovery_query = question`
- Otherwise (for the non-empty gap list `gaps = [g1, g2, ...]` in the order
  the critic reported them):
  - `recovery_query =
      question
      + "\n\n"
      + "Evidence gaps:"
      + "\n"
      + "- " + g1
      + "\n"
      + "- " + g2
      + ...` (one `- <gap>` line per gap, in reported order)

The literal strings `Evidence gaps:` (the section header) and the `- `
per-gap bullet, plus the blank-line (`\n\n`) separator, are part of the
frozen format and must appear verbatim. `question` is always included
unchanged and is never mutated.

No other inputs are permitted. Specifically, the following are forbidden
inputs to the recovery query:

- benchmark gold information (reference answer, reference evidence,
  adjudication labels, correctness scores);
- the shared critic's `support_status` free text, `evidence_sufficiency`
  free text, `unresolved_conflict` explanation, or `evidence_gaps`
  structured explanation, other than the `evidence_gaps` items themselves;
- the policy identity, the condition identity (`B1`/`G1`), the
  `RecoveryReasonCode`, or the benchmark outcome;
- another LLM call (the query must not be produced by a model);
- the initial retrieval query text (which must not be mutated or
  concatenated into the recovery query).

### 29.6 Evidence merge (frozen)

The evidence-merge step has two frozen cases:

- For `REVISE_ONLY`, the evidence context is unchanged. `MERGE_EVIDENCE`
  is skipped; the recovery-retrieved set is empty.
- For `RERETRIEVE_REVISE`, `MERGE_EVIDENCE` produces a new evidence
  context from the current evidence context and the recovery-retrieved
  chunks as follows:
  1. retain the current evidence-context ordering unchanged;
  2. iterate the recovery-retrieved chunks in their reported rank order
     (rank 1 first);
  3. for each recovery chunk, if its `chunk_id` is not already present in
     the current evidence context, append it at the end;
  4. if its `chunk_id` is already present, skip it. The first occurrence
     (the current-context copy) wins.

Forbidden merge behaviors:

- score fusion between current and recovery chunks;
- reranking of existing chunks;
- reordering of the current context;
- duplicate `chunk_id` retention;
- any condition-specific (`B1`/`G1`) branch.

### 29.7 Revision call (frozen)

The revision model call is exactly one per recovery cycle, regardless of
path.

- `REVISE_ONLY`: 1 revision call.
- `RERETRIEVE_REVISE`: 1 revision call (following the 1 recovery
  retrieval call).

Frozen revision inputs:

- the original `question`;
- the shared plan information;
- the merged evidence context with provenance;
- the current draft / current answer candidate;
- the **full `CriticResult` diagnostics** that motivated the recovery,
  namely:
  - `unsupported_claims` (list, if non-empty);
  - `incomplete_support` (list, if non-empty);
  - `evidence_gaps` (list, if non-empty);
  - `explanation` (the critic's free-text explanation);
  - and the control fields `support_status`, `evidence_sufficiency`,
    `unresolved_conflict`, `gap_types`.

Forbidden in revision inputs:

- benchmark gold information;
- a condition-identity branch (`B1`/`G1`);
- the recovery reason code;
- the policy's internal selection state beyond the structured fields
  above.

After the revision call, `POST_RECOVERY_CRITIC` invokes the identical
`StructuredCritic` implementation used at `INITIAL_CRITIC` (one call),
then `POST_RECOVERY_FINALIZE` applies the shared §20 rule and terminates
the run.

### 29.8 Model-call counts (frozen)

Across a completed run, the model call counts are:

- `REVISE_ONLY` path: PLAN (1, if planner is a model call), DRAFT (1),
  INITIAL_CRITIC (1), REVISE (1), POST_RECOVERY_CRITIC (1).
- `RERETRIEVE_REVISE` path: PLAN (1, if planner is a model call), DRAFT (1),
  INITIAL_CRITIC (1), RECOVERY_RETRIEVE (0 — retrieval is not an LLM call),
  REVISE (1), POST_RECOVERY_CRITIC (1).
- Initial path (no recovery): PLAN (1, if planner is a model call), DRAFT (1),
  INITIAL_CRITIC (1).

The exact planner model-call status (whether the plan is one LLM call or
is produced by a non-LLM component) is an open decision; every other count
in this list is frozen.

### 29.9 Terminal output (frozen)

The terminal output mapping is the same as workflow §17 and applies
identically to B1 and G1:

| `RunStatus` | `final_output.answer` | `final_output.abstained` |
| --- | --- | --- |
| `completed` (ABSTAIN before recovery) | `None` | `true` |
| `completed` (ACCEPT before recovery) | released initial draft | `false` |
| `completed_after_recovery` (ACCEPT after recovery) | released post-revision candidate | `false` |
| `completed_after_recovery` (ABSTAIN after recovery) | `None` | `true` |
| `resource_stopped` | `None` | `false` |
| `tool_error` | `None` | `false` |
| `failed` | `None` | `false` |

- An unreleased candidate is never written to
  `final_output.answer`, regardless of the `RunStatus`.
- `cited_chunk_ids` in `final_output` remains empty until the
  citation-generation design is frozen.

These rules are normative body text, not summary bullets.

## 30. Current boundary

At this checkpoint:

- contribution positioning is recorded;
- the common B1/G1 architecture is recorded;
- critic semantics are specified at the contract level and implemented;
- resource accounting semantics are specified at the contract level and the hard feasibility calculator is implemented;
- the policy interface is specified at the contract level and both B1 and G1 policies are implemented;
- exact G1 thresholds and numerical resource limits are not frozen;
- the common shared graph and shared nodes are not implemented;
- scientific benchmark runs remain zero;
- benchmark execution has not started.
