"""Deterministic hard-recovery feasibility calculation.

Pure execution guard shared by the recovery workflows. It evaluates only the
configured hard resource ceilings and the recorded counter snapshot, for one
recovery cycle.

Semantics:
- A ``None`` configured limit is disabled and never blocks.
- ``timeout_ms`` is an execution-level ceiling and is not evaluated here.
- Only recorded remaining capacity is considered; no future token or latency
  cost is estimated.
"""

from __future__ import annotations

from responsible_agentic_workflows.workflow.control import (
    BlockedLimit,
    HardRecoveryFeasibility,
    RecoveryPath,
    ResourceLimits,
    ResourceSnapshot,
)

__all__ = [
    "calculate_hard_recovery_feasibility",
]


def _exhausted(remaining: int | None) -> bool:
    return remaining is not None and remaining <= 0


def calculate_hard_recovery_feasibility(
    *,
    recovery_path: RecoveryPath,
    resources: ResourceSnapshot,
    limits: ResourceLimits,
) -> HardRecoveryFeasibility:
    """Return the hard-guard feasibility outcome for one recovery path.

    A single recovery cycle consumes one LLM-call slot, one retry/recovery
    slot, and requires non-exhausted total-token capacity. The
    RERETRIEVE_REVISE path additionally consumes one retrieval-call slot.

    A ``None`` configured limit is disabled and never blocks. ``timeout_ms``
    is an execution-level ceiling and is not evaluated here.
    """

    if not isinstance(recovery_path, RecoveryPath):
        raise TypeError("recovery_path must be a RecoveryPath")

    if not isinstance(resources, ResourceSnapshot):
        raise TypeError("resources must be a ResourceSnapshot")

    if not isinstance(limits, ResourceLimits):
        raise TypeError("limits must be a ResourceLimits")

    blocked: list[BlockedLimit] = []

    if _exhausted(resources.llm_calls_remaining(limits)):
        blocked.append(BlockedLimit.LLM_CALL_LIMIT)

    if recovery_path is RecoveryPath.RERETRIEVE_REVISE:
        if _exhausted(resources.retrieval_calls_remaining(limits)):
            blocked.append(BlockedLimit.RETRIEVAL_CALL_LIMIT)

    if _exhausted(resources.retries_remaining(limits)):
        blocked.append(BlockedLimit.RETRY_LIMIT)

    if _exhausted(resources.total_tokens_remaining(limits)):
        blocked.append(BlockedLimit.TOKEN_LIMIT)

    if not blocked:
        return HardRecoveryFeasibility(
            recovery_path=recovery_path,
            feasible=True,
            blocked_limits=(),
        )

    return HardRecoveryFeasibility(
        recovery_path=recovery_path,
        feasible=False,
        blocked_limits=tuple(blocked),
    )
