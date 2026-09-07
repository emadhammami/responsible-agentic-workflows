import json
from pathlib import Path

RUN_SCHEMA = Path("benchmark/schema/run.schema.json")


def test_run_schema_separates_execution_modes() -> None:
    schema = json.loads(
        RUN_SCHEMA.read_text(encoding="utf-8")
    )

    assert schema["properties"]["schema_version"]["const"] == "0.3"

    assert "execution_mode" in schema["required"]
    assert "condition" in schema["required"]

    assert set(
        schema["properties"]["execution_mode"]["enum"]
    ) == {
        "engineering",
        "benchmark",
    }

    assert set(
        schema["properties"]["condition"]["enum"]
    ) == {
        "B0",
        "B1",
        "G1",
        None,
    }

    assert len(schema["allOf"]) == 2


def test_run_schema_uses_per_call_retrieval_trace() -> None:
    schema = json.loads(
        RUN_SCHEMA.read_text(encoding="utf-8")
    )

    retrieval = schema["$defs"]["retrieval"]

    assert retrieval["required"] == ["calls"]
    assert set(retrieval["properties"]) == {"calls"}

    retrieval_call = schema["$defs"]["retrievalCall"]

    assert set(retrieval_call["required"]) == {
        "sequence",
        "query",
        "top_k",
        "latency_ms",
        "retrieved_chunks",
    }
