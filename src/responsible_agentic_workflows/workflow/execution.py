"""Shared B1/G1 execution-runtime helpers.

Pure helpers shared by the B1 and G1 LangGraph workflows:
- frozen 13-event vocabulary and deterministic guard-limit order;
- resource-snapshot derivation from a ``RunRecorder``;
- per-path hard-guard feasibility (wraps ``calculate_hard_recovery_feasibility``);
- execution-level guard checkers (model call, retrieval call, recovery begin);
- event-emission validation against the frozen vocabulary;
- recovery-policy-context builder;
- flat policy-decision payload builder (contract §19) and convenience recorder.

No condition branching is introduced.  All helpers are pure (no I/O).
"""

from __future__ import annotations

import math

from responsible_agentic_workflows.logging.run_record import RunRecorder
from responsible_agentic_workflows.workflow.control import (
    BlockedLimit,
    CriticControlState,
    CriticResult,
    HardRecoveryFeasibility,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryPolicyContext,
    ResourceLimits,
    ResourceSnapshot,
)
from responsible_agentic_workflows.workflow.feasibility import (
    calculate_hard_recovery_feasibility,
)
from responsible_agentic_workflows.workflow.recovery import MAX_RECOVERY_CYCLES

__all__ = [
    "BLOCKED_LIMIT_ORDER",
    "WORKFLOW_EVENT_TYPES",
    "begin_recovery_blockers",
    "build_hard_recovery_feasibility",
    "build_policy_decision_event",
    "build_recovery_policy_context",
    "build_resource_snapshot",
    "model_call_blockers",
    "record_policy_decision",
    "record_workflow_event",
    "retrieval_call_blockers",
]

# ---------------------------------------------------------------------------
# 1. Frozen vocabulary and guard ordering (contract §20)
# ---------------------------------------------------------------------------

#: Exact set of 13 workflow event identifiers (frozen by contract §20).
WORKFLOW_EVENT_TYPES: tuple[str, ...] = (
    "plan_completed",
    "initial_retrieval_completed",
    "draft_completed",
    "initial_critic_completed",
    "policy_decision",
    "recovery_started",
    "recovery_retrieval_completed",
    "revision_completed",
    "post_recovery_critic_completed",
    "answer_accepted",
    "abstained",
    "resource_stopped",
    "workflow_failed",
)

#: Deterministic guard-limit evaluation order.
BLOCKED_LIMIT_ORDER: tuple[BlockedLimit, ...] = (
    BlockedLimit.LLM_CALL_LIMIT,
    BlockedLimit.RETRIEVAL_CALL_LIMIT,
    BlockedLimit.RETRY_LIMIT,
    BlockedLimit.TOKEN_LIMIT,
    BlockedLimit.TIMEOUT_LIMIT,
)

# ---------------------------------------------------------------------------
# 2. Internal validation helpers
# ---------------------------------------------------------------------------


def _validate_elapsed_ms(elapsed_ms: float) -> None:
    """Reject bool, non-numeric, negative, or non-finite elapsed values."""

    if isinstance(elapsed_ms, bool) or not isinstance(elapsed_ms, (int, float)):
        raise ValueError(
            f"elapsed_ms must be a non-negative finite number: {elapsed_ms!r}"
        )

    if not math.isfinite(elapsed_ms) or elapsed_ms < 0:
        raise ValueError(
            f"elapsed_ms must be a non-negative finite number: {elapsed_ms!r}"
        )


def _require_positive_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer: {value!r}")
    return value


def _require_non_negative_int(name: str, value: object) -> int:
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or value < 0
    ):
        raise ValueError(f"{name} must be a non-negative integer: {value!r}")
    return value


def _require_critic_iteration(value: object) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(
            f"critic_iteration must be None or a non-negative integer: {value!r}"
        )
    return value


def _require_resource_types(
    *,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
) -> None:
    if not isinstance(resources, ResourceSnapshot):
        raise ValueError("resources must be a ResourceSnapshot instance")

    if not isinstance(limits, ResourceLimits):
        raise ValueError("limits must be a ResourceLimits instance")


def _exhausted(remaining: int | None) -> bool:
    return remaining is not None and remaining <= 0


# ---------------------------------------------------------------------------
# 3. Resource-snapshot builder
# ---------------------------------------------------------------------------


def build_resource_snapshot(
    *,
    recorder: RunRecorder,
    recovery_iteration: int,
) -> ResourceSnapshot:
    """Derive the current ``ResourceSnapshot`` from a ``RunRecorder``.

    ``retries_used`` is set to ``recovery_iteration`` (the current recovery
    cycle count carried in the graph state).  No hidden mutable counters are
    introduced.
    """

    if not isinstance(recorder, RunRecorder):
        raise ValueError("recorder must be a RunRecorder instance")

    _require_non_negative_int("recovery_iteration", recovery_iteration)

    return ResourceSnapshot(
        llm_calls_used=recorder.model_call_count,
        retrieval_calls_used=recorder.retrieval_call_count,
        retries_used=recovery_iteration,
        input_tokens_used=recorder.input_tokens_used,
        output_tokens_used=recorder.output_tokens_used,
        total_tokens_used=recorder.total_tokens_used,
    )


# ---------------------------------------------------------------------------
# 4. Hard-recovery-feasibility helpers (policy-time, existing mechanism A)
# ---------------------------------------------------------------------------


def build_hard_recovery_feasibility(
    *,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
) -> tuple[HardRecoveryFeasibility, ...]:
    """Compute feasibility for both recovery paths in canonical order.

    Returns a tuple of exactly two entries:
    ``(REVISE_ONLY, RERETRIEVE_REVISE)``.
    """

    return (
        calculate_hard_recovery_feasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            resources=resources,
            limits=limits,
        ),
        calculate_hard_recovery_feasibility(
            recovery_path=RecoveryPath.RERETRIEVE_REVISE,
            resources=resources,
            limits=limits,
        ),
    )


# ---------------------------------------------------------------------------
# 5. Execution-level guard checkers (new mechanism B)
#
# These are pre-action guards evaluated at execution time, independent of
# the policy-time feasibility calculation.  They return the deterministic
# tuple of :class:`BlockedLimit` values that block the intended action.
# ---------------------------------------------------------------------------


def model_call_blockers(
    *,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
    elapsed_ms: float,
) -> tuple[BlockedLimit, ...]:
    """Return the limits that block the next model call.

    Order: ``(LLM_CALL_LIMIT, TOKEN_LIMIT, TIMEOUT_LIMIT)`` — only the
    limits actually blocking are present.  A ``None`` configured limit is
    disabled and never blocks.
    """

    _require_resource_types(resources=resources, limits=limits)
    _validate_elapsed_ms(elapsed_ms)

    blocked: list[BlockedLimit] = []

    if _exhausted(resources.llm_calls_remaining(limits)):
        blocked.append(BlockedLimit.LLM_CALL_LIMIT)

    if _exhausted(resources.total_tokens_remaining(limits)):
        blocked.append(BlockedLimit.TOKEN_LIMIT)

    if (
        limits.timeout_ms is not None
        and elapsed_ms >= limits.timeout_ms
    ):
        blocked.append(BlockedLimit.TIMEOUT_LIMIT)

    return tuple(blocked)


def retrieval_call_blockers(
    *,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
    elapsed_ms: float,
) -> tuple[BlockedLimit, ...]:
    """Return the limits that block the next retrieval call.

    Order: ``(RETRIEVAL_CALL_LIMIT, TIMEOUT_LIMIT)`` — only the limits
    actually blocking are present.  A ``None`` configured limit is disabled
    and never blocks.
    """

    _require_resource_types(resources=resources, limits=limits)
    _validate_elapsed_ms(elapsed_ms)

    blocked: list[BlockedLimit] = []

    if _exhausted(resources.retrieval_calls_remaining(limits)):
        blocked.append(BlockedLimit.RETRIEVAL_CALL_LIMIT)

    if (
        limits.timeout_ms is not None
        and elapsed_ms >= limits.timeout_ms
    ):
        blocked.append(BlockedLimit.TIMEOUT_LIMIT)

    return tuple(blocked)


def begin_recovery_blockers(
    *,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
    elapsed_ms: float,
    recovery_iteration: int,
) -> tuple[BlockedLimit, ...]:
    """Return the limits that block beginning a recovery cycle.

    ``recovery_iteration`` is the number of completed recovery cycles
    so far (must equal ``resources.retries_used`` and be strictly less
    than ``MAX_RECOVERY_CYCLES``).  Order:
    ``(RETRY_LIMIT, TIMEOUT_LIMIT)`` — only the limits actually blocking
    are present.
    """

    _require_resource_types(resources=resources, limits=limits)
    _validate_elapsed_ms(elapsed_ms)
    _require_non_negative_int("recovery_iteration", recovery_iteration)

    if recovery_iteration >= MAX_RECOVERY_CYCLES:
        raise ValueError(
            f"recovery_iteration {recovery_iteration} is out of range; "
            f"MAX_RECOVERY_CYCLES is {MAX_RECOVERY_CYCLES}"
        )

    if resources.retries_used != recovery_iteration:
        raise ValueError(
            "recovery_iteration must equal resources.retries_used "
            f"({recovery_iteration} != {resources.retries_used})"
        )

    blocked: list[BlockedLimit] = []

    if (
        limits.max_retries is not None
        and recovery_iteration >= limits.max_retries
    ):
        blocked.append(BlockedLimit.RETRY_LIMIT)

    if (
        limits.timeout_ms is not None
        and elapsed_ms >= limits.timeout_ms
    ):
        blocked.append(BlockedLimit.TIMEOUT_LIMIT)

    return tuple(blocked)


# ---------------------------------------------------------------------------
# 7. Event-emission helper
# ---------------------------------------------------------------------------


def record_workflow_event(
    *,
    recorder: RunRecorder,
    event_type: str,
    stage: str | None = None,
    details: dict[str, object] | None = None,
) -> None:
    """Record a structured workflow event after validating its identifier.

    ``event_type`` must be one of the 13 frozen identifiers in
    ``WORKFLOW_EVENT_TYPES``.  Any other value raises ``ValueError``.
    """

    if event_type not in WORKFLOW_EVENT_TYPES:
        valid = ", ".join(WORKFLOW_EVENT_TYPES)
        raise ValueError(
            f"event_type {event_type!r} is not one of the 13 frozen "
            f"workflow event identifiers.  Valid: {valid}"
        )

    recorder.record_event(
        event_type=event_type,
        stage=stage,
        details=details,
    )


# ---------------------------------------------------------------------------
# 8. Recovery-policy-context builder
# ---------------------------------------------------------------------------


def build_recovery_policy_context(
    *,
    critic_result: CriticResult,
    recovery_iteration: int,
    recorder: RunRecorder,
    limits: ResourceLimits,
) -> RecoveryPolicyContext:
    """Build a ``RecoveryPolicyContext`` from the shared execution state.

    The context is constructed identically for B1 and G1 — no condition
    branching.  ``retries_used`` is set to ``recovery_iteration`` to maintain
    the contract requirement that ``retries_used`` equals
    ``recovery_iteration`` exactly.

    ``hard_recovery_feasibility`` contains the feasibility outcomes for both
    recovery paths, computed via the existing
    ``calculate_hard_recovery_feasibility``.
    """

    critic_state = CriticControlState.from_critic_result(critic_result)
    snapshot = build_resource_snapshot(
        recorder=recorder,
        recovery_iteration=recovery_iteration,
    )
    feasibility = build_hard_recovery_feasibility(
        resources=snapshot,
        limits=limits,
    )

    return RecoveryPolicyContext(
        critic=critic_state,
        recovery_iteration=recovery_iteration,
        resources=snapshot,
        limits=limits,
        hard_recovery_feasibility=feasibility,
    )


# ---------------------------------------------------------------------------
# 9. Policy-decision payload builder (contract §19, flat payload)
# ---------------------------------------------------------------------------


def _validate_path_reserve_satisfied(value: object) -> bool | None:
    if value is None or isinstance(value, bool):
        return value  # type: ignore[return-value]
    raise ValueError(
        "path_reserve_satisfied must be a boolean or None: "
        f"{value!r}"
    )


def _validate_optional_version(name: str, value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string or None")
    return value


def _validate_action_path(
    *,
    action: RecoveryAction,
    path: RecoveryPath | None,
    hard_recovery_feasibility: tuple[HardRecoveryFeasibility, ...],
) -> HardRecoveryFeasibility | None:
    """Cross-validate the explicit recovery path against the action.

    Enforces the mapping rules:
    - ``ACCEPT`` / ``ABSTAIN`` require ``path`` to be ``None``;
    - ``RESOURCE_STOP`` requires ``path`` to be non-``None``;
    - ``REVISE_ONLY`` / ``RERETRIEVE_REVISE`` require the matching path.

    When a non-``None`` path is present, a feasibility entry for that path
    must exist in the tuple; otherwise a ``ValueError`` is raised.
    """

    if action is RecoveryAction.ACCEPT:
        if path is not None:
            raise ValueError(
                "action ACCEPT requires selected_recovery_path to be None, "
                f"got {path!r}"
            )
        return None

    if action is RecoveryAction.ABSTAIN:
        if path is not None:
            raise ValueError(
                "action ABSTAIN requires selected_recovery_path to be None, "
                f"got {path!r}"
            )
        return None

    if action is RecoveryAction.RESOURCE_STOP:
        if path is None:
            raise ValueError(
                "action RESOURCE_STOP requires selected_recovery_path to "
                "be non-None"
            )
    elif action is RecoveryAction.REVISE_ONLY:
        if path is not RecoveryPath.REVISE_ONLY:
            raise ValueError(
                "action REVISE_ONLY requires selected_recovery_path "
                f"{RecoveryPath.REVISE_ONLY.value!r}, got {path!r}"
            )
    elif action is RecoveryAction.RERETRIEVE_REVISE:
        if path is not RecoveryPath.RERETRIEVE_REVISE:
            raise ValueError(
                "action RERETRIEVE_REVISE requires selected_recovery_path "
                f"{RecoveryPath.RERETRIEVE_REVISE.value!r}, got {path!r}"
            )
    else:  # pragma: no cover - RecoveryDecision restricts to known actions
        raise ValueError(f"unsupported action for path validation: {action!r}")

    entry = next(
        (f for f in hard_recovery_feasibility if f.recovery_path is path),
        None,
    )
    if entry is None:
        raise ValueError(
            "hard_recovery_feasibility is missing an entry for path "
            f"{path!r} required by action {action.value}"
        )
    return entry


def build_policy_decision_event(
    *,
    decision: RecoveryDecision,
    critic: CriticControlState,
    critic_iteration: int | None,
    decision_sequence: int,
    recovery_iteration: int,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
    hard_recovery_feasibility: tuple[HardRecoveryFeasibility, ...],
    selected_recovery_path: RecoveryPath | None = None,
    path_reserve_satisfied: bool | None = None,
    recovery_rule_version: str | None = None,
    resource_reserve_rule_version: str | None = None,
) -> dict[str, object]:
    """Build the flat ``policy_decision`` event payload (contract §19).

    The payload is a pure logging artifact of the policy inputs and output,
    using exactly 27 flat keys (no nested dicts).  It must not include
    benchmark gold information, and must not be altered after emission.

    ``decision_sequence`` is a separate parameter (not derived from
    ``critic_iteration``) and ``selected_recovery_path`` is explicit (not
    derived from the action); both are cross-validated.

    ``critic_iteration`` is preserved exactly as supplied: ``None`` stays
    ``None``, and any non-negative integer (including ``0``) is kept as-is.
    """

    if not isinstance(decision, RecoveryDecision):
        raise ValueError("decision must be a RecoveryDecision instance")

    if not isinstance(critic, CriticControlState):
        raise ValueError("critic must be a CriticControlState instance")

    critic_iteration = _require_critic_iteration(critic_iteration)
    _require_positive_int("decision_sequence", decision_sequence)
    _require_non_negative_int("recovery_iteration", recovery_iteration)

    path_reserve_satisfied = _validate_path_reserve_satisfied(
        path_reserve_satisfied
    )
    _validate_optional_version(
        "recovery_rule_version", recovery_rule_version
    )
    _validate_optional_version(
        "resource_reserve_rule_version", resource_reserve_rule_version
    )

    selected = _validate_action_path(
        action=decision.action,
        path=selected_recovery_path,
        hard_recovery_feasibility=hard_recovery_feasibility,
    )

    return {
        "policy_id": decision.policy_id,
        "decision_sequence": decision_sequence,
        "critic_iteration": critic_iteration,
        "support_status": critic.support_status.value,
        "evidence_sufficiency": critic.evidence_sufficiency.value,
        "unresolved_conflict": critic.unresolved_conflict,
        "gap_types": [g.value for g in critic.gap_types],
        "release_ok": critic.release_ok,
        "recovery_iteration": recovery_iteration,
        "selected_action": decision.action.value,
        "reason_code": decision.reason_code.value,
        "llm_calls_used": resources.llm_calls_used,
        "retrieval_calls_used": resources.retrieval_calls_used,
        "retries_used": resources.retries_used,
        "input_tokens_used": resources.input_tokens_used,
        "output_tokens_used": resources.output_tokens_used,
        "total_tokens_used": resources.total_tokens_used,
        "llm_calls_remaining": resources.llm_calls_remaining(limits),
        "retrieval_calls_remaining": resources.retrieval_calls_remaining(
            limits
        ),
        "retries_remaining": resources.retries_remaining(limits),
        "total_tokens_remaining": resources.total_tokens_remaining(limits),
        "selected_recovery_path": (
            selected.recovery_path.value if selected is not None else "NONE"
        ),
        "hard_recovery_feasible": (
            selected.feasible if selected is not None else None
        ),
        "blocked_limits": (
            [b.value for b in selected.blocked_limits]
            if selected is not None
            else []
        ),
        "path_reserve_satisfied": path_reserve_satisfied,
        "recovery_rule_version": recovery_rule_version,
        "resource_reserve_rule_version": resource_reserve_rule_version,
    }


def record_policy_decision(
    *,
    recorder: RunRecorder,
    decision: RecoveryDecision,
    critic: CriticControlState,
    critic_iteration: int | None,
    decision_sequence: int,
    recovery_iteration: int,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
    hard_recovery_feasibility: tuple[HardRecoveryFeasibility, ...],
    selected_recovery_path: RecoveryPath | None = None,
    path_reserve_satisfied: bool | None = None,
    recovery_rule_version: str | None = None,
    resource_reserve_rule_version: str | None = None,
) -> None:
    """Build the ``policy_decision`` payload and record it as an event.

    Convenience wrapper around ``build_policy_decision_event`` +
    ``record_workflow_event``.
    """

    payload = build_policy_decision_event(
        decision=decision,
        critic=critic,
        critic_iteration=critic_iteration,
        decision_sequence=decision_sequence,
        recovery_iteration=recovery_iteration,
        resources=resources,
        limits=limits,
        hard_recovery_feasibility=hard_recovery_feasibility,
        selected_recovery_path=selected_recovery_path,
        path_reserve_satisfied=path_reserve_satisfied,
        recovery_rule_version=recovery_rule_version,
        resource_reserve_rule_version=resource_reserve_rule_version,
    )

    record_workflow_event(
        recorder=recorder,
        event_type="policy_decision",
        details=payload,
    )
