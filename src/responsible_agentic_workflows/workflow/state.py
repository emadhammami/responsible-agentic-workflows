"""Shared LangGraph workflow state for the B1 and G1 recovery workflows.

This module defines the single frozen top-level state surface used by the
B1 and G1 LangGraph topologies. Field names, field order, and field types are
frozen by the B1/G1 workflow and runtime contracts and must not change without
a contract revision. The 18 fields listed in ``WORKFLOW_STATE_FIELDS`` are the
only top-level state fields; no additional top-level fields may be introduced.
"""

from __future__ import annotations

from typing import Literal, TypedDict

from responsible_agentic_workflows.retrieval.models import RetrievedChunk

from .control import (
    CriticControlState,
    CriticResult,
    RecoveryDecision,
    ResourceLimits,
)

ResourceLimitsType = ResourceLimits

__all__ = [
    "CONDITION_METADATA_VALUES",
    "ConditionMetadata",
    "EXECUTION_MODES",
    "ExecutionMode",
    "WorkflowState",
    "WORKFLOW_STATE_FIELDS",
    "initial_workflow_state",
]

EXECUTION_MODES: tuple[str, ...] = ("engineering", "benchmark")
ExecutionMode = Literal["engineering", "benchmark"]

#: Logging-only condition label. B1 and G1 share the identical graph and state
#: surface; this field must never drive routing or behavior.
CONDITION_METADATA_VALUES: tuple[str, ...] = ("B1", "G1")
ConditionMetadata = Literal["B1", "G1"]

WORKFLOW_STATE_FIELDS: tuple[str, ...] = (
    "task_id",
    "question",
    "execution_mode",
    "condition_metadata",
    "plan",
    "initial_retrieval",
    "recovery_retrieval",
    "merged_evidence",
    "current_answer_candidate",
    "latest_CriticResult",
    "latest_CriticControlState",
    "critic_iteration",
    "recovery_iteration",
    "latest_RecoveryDecision",
    "ResourceLimits",
    "terminal_status",
    "final_answer",
    "abstained_flag",
)


class WorkflowState(TypedDict, total=False):
    """Frozen shared state surface for the B1 and G1 recovery workflows.

    All top-level fields are optional (``total=False``) so that individual
    LangGraph nodes may return partial updates. The 18 keys above are the
    only permitted top-level fields.
    """

    task_id: str
    question: str
    execution_mode: ExecutionMode
    condition_metadata: ConditionMetadata | None
    plan: object | None
    initial_retrieval: tuple[RetrievedChunk, ...]
    recovery_retrieval: tuple[RetrievedChunk, ...] | None
    merged_evidence: tuple[RetrievedChunk, ...] | None
    current_answer_candidate: str | None
    latest_CriticResult: CriticResult | None
    latest_CriticControlState: CriticControlState | None
    critic_iteration: int | None
    recovery_iteration: int
    latest_RecoveryDecision: RecoveryDecision | None
    ResourceLimits: ResourceLimits
    terminal_status: str | None
    final_answer: str | None
    abstained_flag: bool


def initial_workflow_state(
    *,
    task_id: str,
    question: str,
    execution_mode: ExecutionMode,
    condition_metadata: ConditionMetadata | None = None,
    ResourceLimits: ResourceLimits,
) -> WorkflowState:
    """Construct the initial workflow state with reset bookkeeping counters.

    The returned state starts with ``critic_iteration`` as ``None`` (no
    numeric convention is frozen), ``recovery_iteration`` at zero, no terminal
    status, no final answer, and the abstained flag set to ``False``. All
    other optional fields start as ``None`` so that downstream nodes populate
    them as the workflow advances. ``condition_metadata`` is a logging-only
    label and must never influence routing or behavior.
    """

    if not isinstance(task_id, str) or not task_id.strip():
        raise ValueError("task_id must be a non-empty string")

    if not isinstance(question, str) or not question.strip():
        raise ValueError("question must be a non-empty string")

    if execution_mode not in EXECUTION_MODES:
        raise ValueError(
            f"Unsupported execution mode: {execution_mode!r}; "
            f"expected one of {', '.join(EXECUTION_MODES)}"
        )

    if condition_metadata is not None and (
        condition_metadata not in CONDITION_METADATA_VALUES
    ):
        raise ValueError(
            f"Unsupported condition_metadata: {condition_metadata!r}; "
            f"expected one of {', '.join(CONDITION_METADATA_VALUES)} "
            f"or None"
        )

    if not isinstance(ResourceLimits, ResourceLimitsType):
        raise ValueError("ResourceLimits must be a ResourceLimits instance")

    return {
        "task_id": task_id,
        "question": question,
        "execution_mode": execution_mode,
        "condition_metadata": condition_metadata,
        "plan": None,
        "initial_retrieval": (),
        "recovery_retrieval": None,
        "merged_evidence": None,
        "current_answer_candidate": None,
        "latest_CriticResult": None,
        "latest_CriticControlState": None,
        "critic_iteration": None,
        "recovery_iteration": 0,
        "latest_RecoveryDecision": None,
        "ResourceLimits": ResourceLimits,
        "terminal_status": None,
        "final_answer": None,
        "abstained_flag": False,
    }
