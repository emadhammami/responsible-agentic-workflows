import json
from pathlib import Path

RUN_SCHEMA = Path("benchmark/schema/run.schema.json")


def test_run_schema_uses_per_call_retrieval_trace() -> None:
    schema = json.loads(RUN_SCHEMA.read_text(encoding="utf-8"))

    assert schema["properties"]["schema_version"]["const"] == "0.2"

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

    properties = retrieval_call["properties"]

    assert properties["sequence"]["minimum"] == 1
    assert properties["query"]["minLength"] == 1
    assert properties["top_k"]["minimum"] == 1
    assert properties["latency_ms"]["minimum"] == 0

    assert (
        properties["retrieved_chunks"]["items"]["$ref"]
        == "#/$defs/retrievedChunk"
    )
