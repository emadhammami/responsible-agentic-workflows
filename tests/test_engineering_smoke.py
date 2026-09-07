import json
from pathlib import Path

from responsible_agentic_workflows.engineering import (
    run_retrieval_smoke,
)
from responsible_agentic_workflows.logging import validate_run_record


def test_engineering_smoke_creates_valid_run(
    tmp_path: Path,
) -> None:
    output = tmp_path / "engineering-smoke.json"

    written = run_retrieval_smoke(
        output_path=output,
        run_id="engineering-smoke-test",
        code_revision="abcdef1",
    )

    assert written == output
    assert output.is_file()

    record = json.loads(
        output.read_text(encoding="utf-8")
    )

    validate_run_record(record)

    assert record["schema_version"] == "0.2"
    assert record["run_id"] == "engineering-smoke-test"
    assert record["experiment_id"] == "engineering-smoke"
    assert record["task_id"] == "T901"

    assert record["configuration"]["model_provider"] == (
        "engineering-test"
    )
    assert record["configuration"]["model_name"] == "no-model"

    assert record["usage"]["llm_calls"] == 0
    assert record["usage"]["retrieval_calls"] == 1

    calls = record["retrieval"]["calls"]

    assert len(calls) == 1
    assert calls[0]["sequence"] == 1
    assert calls[0]["top_k"] == 3
    assert calls[0]["latency_ms"] >= 0
    assert calls[0]["retrieved_chunks"]

    assert record["errors"] == []
    assert record["final_output"]["answer"] is None


def test_engineering_smoke_contains_no_gold_data(
    tmp_path: Path,
) -> None:
    output = tmp_path / "engineering-smoke.json"

    run_retrieval_smoke(
        output_path=output,
        run_id="engineering-smoke-gold-check",
        code_revision="abcdef1",
    )

    text = output.read_text(encoding="utf-8")

    forbidden_fields = {
        "reference_answer",
        "reference_evidence",
        "required_documents",
        "task_type",
        "validation_status",
    }

    for field in forbidden_fields:
        assert field not in text
