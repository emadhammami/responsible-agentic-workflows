import re
from pathlib import Path

import pytest

from responsible_agentic_workflows.logging import (
    RunConfiguration,
    RunRecorder,
    validate_run_record,
)

TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z"
)


def _recorder() -> RunRecorder:
    return RunRecorder(
        run_id="unit-run-001",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=RunConfiguration(
            model_provider="engineering-test",
            model_name="no-model",
            model_config_id="engineering-no-model-v0.1",
            model_version=None,
            temperature=None,
            max_output_tokens=None,
            prompt_version="engineering-test-v0.1",
            retrieval_config_id="engineering-lexical-v0.1",
            workflow_config_id="unit-test",
            random_seed=None,
        ),
    )


def test_record_event_keywords_only_and_sequence_numbering() -> None:
    recorder = _recorder()

    with pytest.raises(TypeError):
        recorder.record_event("critic_completed", "critic", None)

    recorder.record_event(
        event_type="recovery_policy_evaluated",
        stage="policy",
        details={"iteration": 1, "policy_id": "g1-v0.1"},
    )
    recorder.record_event(
        event_type="hard_guard_passed",
    )
    recorder.record_event(
        event_type="run_completed",
        details={},
    )

    events = recorder._events

    assert [event["sequence"] for event in events] == [1, 2, 3]

    first = events[0]

    assert set(first) == {
        "sequence",
        "event_type",
        "stage",
        "timestamp",
        "details",
    }
    assert first["event_type"] == "recovery_policy_evaluated"
    assert first["stage"] == "policy"
    assert first["details"] == {"iteration": 1, "policy_id": "g1-v0.1"}
    assert TIMESTAMP_PATTERN.fullmatch(first["timestamp"])

    assert events[1]["stage"] is None
    assert events[1]["details"] is None

    assert events[2]["details"] == {}


def test_record_event_validates_inputs() -> None:
    recorder = _recorder()

    with pytest.raises(ValueError, match="event_type"):
        recorder.record_event(event_type="")

    with pytest.raises(ValueError, match="event_type"):
        recorder.record_event(event_type="   ")

    with pytest.raises(ValueError, match="event_type"):
        recorder.record_event(event_type=123)

    with pytest.raises(ValueError, match="stage"):
        recorder.record_event(
            event_type="run_started",
            stage="",
        )

    with pytest.raises(ValueError, match="stage"):
        recorder.record_event(
            event_type="run_started",
            stage=123,
        )

    with pytest.raises(ValueError, match="details"):
        recorder.record_event(
            event_type="run_started",
            details=("not", "an", "object"),
        )

    assert recorder._events == []


def test_record_event_details_are_deep_copied() -> None:
    recorder = _recorder()

    details = {
        "iteration": 1,
        "blocked_limits": [("T", "OKEN_LIMIT")],
    }

    recorder.record_event(
        event_type="recovery_blocked",
        stage="guard",
        details=details,
    )

    details["iteration"] = 99
    details["blocked_limits"].clear()
    details["extra"] = "late"

    stored = recorder._events[0]["details"]

    assert stored == {
        "iteration": 1,
        "blocked_limits": [("T", "OKEN_LIMIT")],
    }
    assert "extra" not in stored


def test_record_event_builds_schema_valid_record() -> None:
    recorder = _recorder()

    nested = {
        "iteration": 0,
        "nested": {
            "reason_code": "G1_RECOVERY_NOT_WORTHWHILE",
            "feasible_paths": ["REVISE_ONLY"],
        },
    }

    recorder.record_event(
        event_type="recovery_policy_evaluated",
        stage="policy",
        details=dict(nested),
    )
    recorder.record_event(event_type="abstention_issued")

    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=True,
    )

    assert record["events"] == recorder._events

    validate_run_record(record)

    events = record["events"]

    assert len(events) == 2
    assert events[0]["sequence"] == 1
    assert events[1]["sequence"] == 2
    assert events[0]["details"] == nested
    assert events[1]["stage"] is None
    assert events[1]["details"] is None


def test_record_event_preserves_event_order_in_written_artifact() -> None:
    recorder = _recorder()

    for index in range(5):
        recorder.record_event(
            event_type=f"step_{index}",
            stage="audit",
            details={"index": index},
        )

    record = recorder.build_record(
        status="completed",
        answer="Engineering test output.",
        abstained=False,
    )

    schema_path = Path("benchmark/schema/run.schema.json")

    validate_run_record(record, schema_path=schema_path)

    assert [event["event_type"] for event in record["events"]] == [
        "step_0",
        "step_1",
        "step_2",
        "step_3",
        "step_4",
    ]
