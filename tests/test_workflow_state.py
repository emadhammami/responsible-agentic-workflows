from __future__ import annotations

import dataclasses

import pytest

from responsible_agentic_workflows.workflow import (
    CONDITION_METADATA_VALUES,
    EXECUTION_MODES,
    WORKFLOW_STATE_FIELDS,
    ResourceLimits,
    initial_workflow_state,
)
from responsible_agentic_workflows.workflow.state import WorkflowState


def _limits() -> ResourceLimits:
    return ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=3,
        max_retries=2,
        max_total_tokens=4096,
        timeout_ms=60_000,
    )


def test_workflow_state_field_tuple_is_frozen_18_fields() -> None:
    assert len(WORKFLOW_STATE_FIELDS) == 18
    assert WORKFLOW_STATE_FIELDS == (
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
    # Order is frozen: a re-order would break the contract.
    assert WORKFLOW_STATE_FIELDS[0] == "task_id"
    assert WORKFLOW_STATE_FIELDS[-1] == "abstained_flag"


def test_workflow_state_typeddict_keys_match_frozen_tuple() -> None:
    typed = WorkflowState.__annotations__
    assert tuple(typed.keys()) == WORKFLOW_STATE_FIELDS
    assert not dataclasses.is_dataclass(WorkflowState)
    # The TypedDict is declared total=False.
    assert WorkflowState.__total__ is False


def test_execution_modes_are_exactly_engineering_and_benchmark() -> None:
    assert EXECUTION_MODES == ("engineering", "benchmark")


def test_initial_workflow_state_has_all_18_fields_and_defaults() -> None:
    state = initial_workflow_state(
        task_id="task-1",
        question="What is the capital of France?",
        execution_mode="engineering",
        ResourceLimits=_limits(),
    )

    assert set(state.keys()) == set(WORKFLOW_STATE_FIELDS)
    assert state["task_id"] == "task-1"
    assert state["question"] == "What is the capital of France?"
    assert state["execution_mode"] == "engineering"
    assert state["condition_metadata"] is None
    assert state["plan"] is None
    assert state["initial_retrieval"] == ()
    assert state["recovery_retrieval"] is None
    assert state["merged_evidence"] is None
    assert state["current_answer_candidate"] is None
    assert state["latest_CriticResult"] is None
    assert state["latest_CriticControlState"] is None
    assert state["critic_iteration"] is None
    assert state["recovery_iteration"] == 0
    assert state["latest_RecoveryDecision"] is None
    assert isinstance(state["ResourceLimits"], ResourceLimits)
    assert state["terminal_status"] is None
    assert state["final_answer"] is None
    assert state["abstained_flag"] is False


def test_condition_metadata_values_are_exactly_b1_and_g1() -> None:
    assert CONDITION_METADATA_VALUES == ("B1", "G1")


@pytest.mark.parametrize("label", ["B1", "G1"])
def test_initial_state_preserves_condition_metadata_and_benchmark_mode(
    label: str,
) -> None:
    state = initial_workflow_state(
        task_id="t",
        question="q",
        execution_mode="benchmark",
        condition_metadata=label,  # type: ignore[arg-type]
        ResourceLimits=_limits(),
    )
    assert state["execution_mode"] == "benchmark"
    assert state["condition_metadata"] == label


@pytest.mark.parametrize("bad", ["b1", "G2", "", "B1 ", 42])
def test_initial_state_rejects_invalid_condition_metadata(bad: object) -> None:
    with pytest.raises(ValueError, match="condition_metadata"):
        initial_workflow_state(
            task_id="t",
            question="q",
            execution_mode="engineering",
            condition_metadata=bad,  # type: ignore[arg-type]
            ResourceLimits=_limits(),
        )


@pytest.mark.parametrize(
    ("field", "bad"),
    [
        ("task_id", ""),
        ("task_id", "   "),
        ("question", ""),
        ("question", "  "),
    ],
)
def test_initial_state_rejects_blank_identifiers(field: str, bad: str) -> None:
    kwargs: dict[str, object] = {
        "task_id": "task-1",
        "question": "q",
        "execution_mode": "engineering",
        "ResourceLimits": _limits(),
    }
    kwargs[field] = bad
    with pytest.raises(ValueError):
        initial_workflow_state(**kwargs)  # type: ignore[arg-type]


def test_initial_state_rejects_unknown_execution_mode() -> None:
    with pytest.raises(ValueError, match="execution mode"):
        initial_workflow_state(
            task_id="t",
            question="q",
            execution_mode="unknown",  # type: ignore[arg-type]
            ResourceLimits=_limits(),
        )


def test_initial_state_rejects_non_resource_limits() -> None:
    with pytest.raises(ValueError, match="ResourceLimits"):
        initial_workflow_state(
            task_id="t",
            question="q",
            execution_mode="engineering",
            ResourceLimits=NotARealLimits(),  # type: ignore[arg-type]
        )


class NotARealLimits:
    """A stand-in that is clearly not a ``ResourceLimits`` instance."""
