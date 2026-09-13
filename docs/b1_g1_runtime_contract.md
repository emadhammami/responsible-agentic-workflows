# B1/G1 Runtime Control Contracts

**Status:** Working specification; G1 decision logic frozen for implementation
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

It does not yet freeze the exact G1 recovery-worthiness rule, resource reserve
rule, or numerical resource limits.

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

`support_status` uses exactly these working values:

- `SUPPORTED`;
- `PARTIAL_SUPPORT`;
- `UNSUPPORTED`.

It describes the relationship between the current answer candidate and the
evidence available to the workflow.

### 3.2 Evidence sufficiency

`evidence_sufficiency` uses exactly these working values:

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

The working vocabulary is:

- `DRAFT_GROUNDING`;
- `MISSING_EVIDENCE`;
- `INCOMPLETE_EVIDENCE`;
- `EVIDENCE_CONFLICT`.

An empty tuple means that the critic identified no material gap.

The vocabulary must be frozen before benchmark execution.

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

The pre-recovery decision order is frozen for implementation as follows.

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

Working common reason codes are:

- `RELEASE_OK`;
- `HARD_LIMIT_BLOCKED`.

Working B1-specific reason codes are:

- `B1_FIXED_REVISE_ONLY`;
- `B1_FIXED_RERETRIEVE_REVISE`.

Working G1-specific reason codes are:

- `G1_RECOVERY_NOT_WORTHWHILE`;
- `G1_REVISE_ONLY`;
- `G1_RERETRIEVE_REVISE`;
- `G1_RESOURCE_RESERVE_BLOCKED`.

`G1_RESOURCE_RESERVE_BLOCKED` is used for either path-specific reserve, and the
logged event must identify which path the reserve check applied to.

These names describe why the pre-recovery action was selected.

They are not scientific outcome labels.

The vocabulary must be frozen before benchmark execution.

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

The G1 rule remains pre-specified structurally but not yet numerically frozen.

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

The exact recovery-worthiness rule remains open.

The two path-specific reserve rules remain open.

Both must be frozen before scientific benchmark execution.

## 19. Recovery-worthiness constraints

The future G1 recovery-worthiness function must be deterministic.

It may use only fields explicitly frozen as policy inputs.

At the current design boundary, eligible evidence-state inputs are limited to:

- support status;
- evidence sufficiency;
- unresolved-conflict flag;
- categorical gap types.

The policy must not infer additional hidden signals from free text.

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

- final critic prompt;
- final critic structured-output representation;
- whether diagnostic explanation is required;
- final gap-type vocabulary;
- exact G1 recovery-worthiness rule;
- exact G1 path-specific reserve rules for `REVISE_ONLY` and
  `RERETRIEVE_REVISE`;
- numerical LLM-call limit;
- numerical retrieval-call limit;
- numerical retry limit;
- numerical total-token ceiling;
- timeout;
- per-call output-token limit;
- exact policy identifiers;
- exact workflow event identifiers.

These must be resolved using engineering validation, methodological reasoning,
and prior literature before the scientific benchmark.

They must not be selected from primary benchmark performance.

## 28. Freeze sequence

The intended sequence is:

1. review this runtime contract;
2. implement typed critic, resource, and policy interfaces;
3. implement public structured event recording;
4. test the interfaces using synthetic deterministic inputs;
5. specify critic prompt and structured parser;
6. specify G1 recovery-worthiness rule;
7. specify G1 resource-reserve rule;
8. freeze resource limits and output limits;
9. implement the common graph and shared nodes;
10. run synthetic real-model engineering validation;
11. freeze the full B1/G1 workflow configuration;
12. only then permit scientific benchmark execution.

## 29. Current boundary

At this checkpoint:

- contribution positioning is recorded;
- the common B1/G1 architecture is recorded;
- critic semantics are specified at the contract level;
- resource accounting semantics are specified at the contract level;
- the policy interface is specified at the contract level;
- exact G1 thresholds and resource limits are not frozen;
- B1 implementation has not started;
- G1 implementation has not started;
- scientific benchmark runs remain zero;
- benchmark execution has not started.
