"""Benchmark task loading with explicit gold-data isolation."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class ReferenceEvidence:
    """Gold evidence used only by the benchmark evaluation layer."""

    document_id: str
    page: int | None
    section: str | None
    chunk_id: str | None


@dataclass(frozen=True, slots=True)
class RuntimeTask:
    """Minimal task information permitted to reach an evaluated workflow."""

    task_id: str
    question: str

    def as_dict(self) -> dict[str, str]:
        """Return the model-visible runtime representation."""

        return {
            "task_id": self.task_id,
            "question": self.question,
        }


@dataclass(frozen=True, slots=True)
class BenchmarkTask:
    """Full benchmark-side task including evaluation-only gold data."""

    schema_version: str
    task_id: str
    question: str
    task_type: str
    required_documents: tuple[str, ...]
    reference_answer: str
    reference_evidence: tuple[ReferenceEvidence, ...]
    difficulty: str | None
    notes: str | None
    validation_status: str

    def to_runtime_task(self) -> RuntimeTask:
        """Project a benchmark task into the model-visible runtime form."""

        return RuntimeTask(
            task_id=self.task_id,
            question=self.question,
        )


def _require_string(
    data: dict[str, Any],
    key: str,
) -> str:
    value = data.get(key)

    if not isinstance(value, str) or not value:
        raise ValueError(f"Expected non-empty string field: {key}")

    return value


def _load_reference_evidence(
    value: Any,
) -> tuple[ReferenceEvidence, ...]:
    if not isinstance(value, list):
        raise ValueError("reference_evidence must be a list")

    evidence: list[ReferenceEvidence] = []

    for item in value:
        if not isinstance(item, dict):
            raise ValueError("Each reference_evidence item must be an object")

        document_id = _require_string(item, "document_id")

        page = item.get("page")
        section = item.get("section")
        chunk_id = item.get("chunk_id")

        if page is not None and (
            not isinstance(page, int) or isinstance(page, bool) or page < 1
        ):
            raise ValueError("Evidence page must be null or a positive integer")

        if section is not None and not isinstance(section, str):
            raise ValueError("Evidence section must be null or a string")

        if chunk_id is not None and not isinstance(chunk_id, str):
            raise ValueError("Evidence chunk_id must be null or a string")

        evidence.append(
            ReferenceEvidence(
                document_id=document_id,
                page=page,
                section=section,
                chunk_id=chunk_id,
            )
        )

    return tuple(evidence)


def load_benchmark_task(path: str | Path) -> BenchmarkTask:
    """Load one full benchmark-side task from JSON."""

    source = Path(path)

    if not source.is_file():
        raise FileNotFoundError(source)

    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {source.name}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Task root must be an object: {source.name}")

    schema_version = _require_string(data, "schema_version")
    task_id = _require_string(data, "task_id")
    question = _require_string(data, "question")
    task_type = _require_string(data, "task_type")
    reference_answer = _require_string(data, "reference_answer")
    validation_status = _require_string(data, "validation_status")

    if source.stem != task_id:
        raise ValueError(
            f"Filename/task ID mismatch: {source.stem} != {task_id}"
        )

    required_documents_raw = data.get("required_documents", [])

    if not isinstance(required_documents_raw, list) or not all(
        isinstance(item, str) and item
        for item in required_documents_raw
    ):
        raise ValueError("required_documents must be a list of strings")

    if len(required_documents_raw) != len(set(required_documents_raw)):
        raise ValueError("required_documents contains duplicates")

    difficulty = data.get("difficulty")
    notes = data.get("notes")

    if difficulty is not None and not isinstance(difficulty, str):
        raise ValueError("difficulty must be null or a string")

    if notes is not None and not isinstance(notes, str):
        raise ValueError("notes must be null or a string")

    return BenchmarkTask(
        schema_version=schema_version,
        task_id=task_id,
        question=question,
        task_type=task_type,
        required_documents=tuple(required_documents_raw),
        reference_answer=reference_answer,
        reference_evidence=_load_reference_evidence(
            data.get("reference_evidence")
        ),
        difficulty=difficulty,
        notes=notes,
        validation_status=validation_status,
    )


def load_benchmark_task_directory(
    directory: str | Path,
) -> tuple[BenchmarkTask, ...]:
    """Load benchmark task JSON files in deterministic filename order."""

    root = Path(directory)

    if not root.is_dir():
        raise NotADirectoryError(root)

    tasks = tuple(
        load_benchmark_task(path)
        for path in sorted(root.glob("T*.json"))
    )

    if not tasks:
        raise ValueError(f"No T*.json benchmark tasks found in {root}")

    task_ids = [task.task_id for task in tasks]

    if len(task_ids) != len(set(task_ids)):
        raise ValueError("Duplicate task IDs detected")

    return tasks


def load_runtime_task(path: str | Path) -> RuntimeTask:
    """Load one task and expose only information permitted at runtime."""

    return load_benchmark_task(path).to_runtime_task()
