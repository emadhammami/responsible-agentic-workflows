import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.benchmark import (
    load_benchmark_task,
    load_benchmark_task_directory,
    load_runtime_task,
)

SYNTHETIC_TASKS = Path("benchmark/synthetic/tasks")


def test_full_task_loads_gold_data_for_evaluation() -> None:
    task = load_benchmark_task(SYNTHETIC_TASKS / "T901.json")

    assert task.task_id == "T901"
    assert task.task_type == "direct_retrieval"
    assert task.required_documents == ("DOC901",)
    assert task.reference_answer
    assert len(task.reference_evidence) == 1
    assert task.reference_evidence[0].document_id == "DOC901"


def test_runtime_projection_contains_only_id_and_question() -> None:
    runtime_task = load_runtime_task(SYNTHETIC_TASKS / "T901.json")

    payload = runtime_task.as_dict()

    assert payload == {
        "task_id": "T901",
        "question": (
            "Who must approve ordinary international business travel "
            "before it is booked?"
        ),
    }

    assert not hasattr(runtime_task, "task_type")
    assert not hasattr(runtime_task, "required_documents")
    assert not hasattr(runtime_task, "reference_answer")
    assert not hasattr(runtime_task, "reference_evidence")
    assert not hasattr(runtime_task, "difficulty")
    assert not hasattr(runtime_task, "validation_status")


def test_insufficient_evidence_label_is_not_exposed_at_runtime() -> None:
    benchmark_task = load_benchmark_task(SYNTHETIC_TASKS / "T904.json")
    runtime_task = benchmark_task.to_runtime_task()

    assert benchmark_task.task_type == "insufficient_evidence"
    assert benchmark_task.required_documents == ()
    assert benchmark_task.reference_evidence == ()

    runtime_payload = runtime_task.as_dict()

    assert set(runtime_payload) == {"task_id", "question"}
    assert "insufficient_evidence" not in runtime_payload.values()


def test_synthetic_tasks_load_in_deterministic_order() -> None:
    tasks = load_benchmark_task_directory(SYNTHETIC_TASKS)

    assert [task.task_id for task in tasks] == [
        "T901",
        "T902",
        "T903",
        "T904",
        "T905",
        "T906",
        "T907",
    ]


def test_filename_must_match_task_id(tmp_path: Path) -> None:
    source_data = json.loads(
        (SYNTHETIC_TASKS / "T901.json").read_text(encoding="utf-8")
    )

    source = tmp_path / "T999.json"
    source.write_text(
        json.dumps(source_data),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="Filename/task ID mismatch",
    ):
        load_benchmark_task(source)


def test_duplicate_required_documents_are_rejected(
    tmp_path: Path,
) -> None:
    source_data = json.loads(
        (SYNTHETIC_TASKS / "T901.json").read_text(encoding="utf-8")
    )

    source_data["task_id"] = "T999"
    source_data["required_documents"] = ["DOC901", "DOC901"]

    source = tmp_path / "T999.json"
    source.write_text(
        json.dumps(source_data),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="required_documents contains duplicates",
    ):
        load_benchmark_task(source)
