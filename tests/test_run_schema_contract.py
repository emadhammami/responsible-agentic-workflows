import json
from pathlib import Path

RUN_SCHEMA = Path("benchmark/schema/run.schema.json")


def _schema() -> dict:
    return json.loads(
        RUN_SCHEMA.read_text(encoding="utf-8")
    )


def test_run_schema_separates_execution_modes() -> None:
    schema = _schema()

    assert schema["properties"]["schema_version"]["const"] == "0.4"

    assert "execution_mode" in schema["required"]
    assert "condition" in schema["required"]

    assert set(
        schema["properties"]["execution_mode"]["enum"]
    ) == {
        "engineering",
        "benchmark",
    }


def test_run_schema_uses_per_call_retrieval_trace() -> None:
    schema = _schema()

    retrieval = schema["$defs"]["retrieval"]

    assert retrieval["required"] == ["calls"]

    retrieval_call = schema["$defs"]["retrievalCall"]

    assert set(retrieval_call["required"]) == {
        "sequence",
        "query",
        "top_k",
        "latency_ms",
        "retrieved_chunks",
    }


def test_run_schema_uses_per_call_model_trace() -> None:
    schema = _schema()

    assert "model" in schema["required"]

    model = schema["$defs"]["model"]

    assert model["required"] == ["calls"]

    model_call = schema["$defs"]["modelCall"]

    assert set(model_call["required"]) == {
        "sequence",
        "status",
        "latency_ms",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "finish_reason",
        "provider_response_id",
    }


def test_run_configuration_requires_model_config_id() -> None:
    schema = _schema()

    configuration = schema["$defs"]["configuration"]

    assert "model_config_id" in configuration["required"]
