import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.ingestion import (
    ingest_markdown_directory,
)
from responsible_agentic_workflows.logging import (
    LoggedRetriever,
    RunConfiguration,
    RunRecorder,
    validate_run_record,
    write_validated_run_record,
)
from responsible_agentic_workflows.retrieval import LexicalRetriever

SYNTHETIC_DOCUMENTS = Path("benchmark/synthetic/documents")


def _base_retriever() -> LexicalRetriever:
    documents = ingest_markdown_directory(SYNTHETIC_DOCUMENTS)

    return LexicalRetriever(
        chunk
        for document in documents
        for chunk in document.chunks
    )


def _configuration(
    retriever: LexicalRetriever,
) -> RunConfiguration:
    return RunConfiguration(
        model_provider="engineering-test",
        model_name="no-model",
        model_version=None,
        temperature=None,
        max_output_tokens=None,
        prompt_version="engineering-test-v0.1",
        retrieval_config_id=retriever.config_id,
        workflow_config_id="unit-test",
        random_seed=None,
    )


def _recorder(
    retriever: LexicalRetriever,
) -> RunRecorder:
    return RunRecorder(
        run_id="unit-run-001",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=_configuration(retriever),
    )


def test_logged_retrieval_preserves_per_call_trace() -> None:
    retriever = _base_retriever()
    recorder = _recorder(retriever)
    logged = LoggedRetriever(retriever, recorder)

    first_results = logged.retrieve(
        "How long must expense receipts be retained?",
        top_k=3,
    )

    second_results = logged.retrieve(
        "approval for international high risk travel",
        top_k=2,
    )

    record = recorder.build_record(
        status="completed",
        answer="Engineering test output.",
        abstained=False,
    )

    calls = record["retrieval"]["calls"]

    assert len(calls) == 2
    assert calls[0]["sequence"] == 1
    assert calls[1]["sequence"] == 2

    assert calls[0]["query"] == (
        "How long must expense receipts be retained?"
    )
    assert calls[1]["query"] == (
        "approval for international high risk travel"
    )

    assert calls[0]["top_k"] == 3
    assert calls[1]["top_k"] == 2

    assert calls[0]["latency_ms"] >= 0
    assert calls[1]["latency_ms"] >= 0

    assert (
        calls[0]["retrieved_chunks"][0]["chunk_id"]
        == first_results[0].chunk.chunk_id
    )

    assert (
        calls[1]["retrieved_chunks"][0]["chunk_id"]
        == second_results[0].chunk.chunk_id
    )

    assert record["usage"]["retrieval_calls"] == 2
    assert record["timing"]["retrieval_ms"] >= 0


def test_logged_run_contains_no_gold_fields() -> None:
    retriever = _base_retriever()
    recorder = _recorder(retriever)
    logged = LoggedRetriever(retriever, recorder)

    logged.retrieve(
        "Who must approve ordinary international business travel?",
        top_k=3,
    )

    record = recorder.build_record(
        status="completed",
        answer="Engineering test output.",
        abstained=False,
    )

    serialized = json.dumps(record)

    forbidden = {
        "reference_answer",
        "reference_evidence",
        "required_documents",
        "task_type",
        "validation_status",
    }

    for field in forbidden:
        assert field not in serialized


def test_logged_run_validates_against_schema() -> None:
    retriever = _base_retriever()
    recorder = _recorder(retriever)
    logged = LoggedRetriever(retriever, recorder)

    results = logged.retrieve(
        "How long must expense receipts be retained?",
        top_k=3,
    )

    record = recorder.build_record(
        status="completed",
        answer="Seven years.",
        abstained=False,
        cited_chunk_ids=(
            results[0].chunk.chunk_id,
        ),
    )

    validate_run_record(record)


def test_validated_run_writer_round_trip(
    tmp_path: Path,
) -> None:
    retriever = _base_retriever()
    recorder = _recorder(retriever)
    logged = LoggedRetriever(retriever, recorder)

    logged.retrieve(
        "external collaborator access review",
        top_k=2,
    )

    record = recorder.build_record(
        status="completed",
        answer="Engineering test output.",
        abstained=False,
    )

    output = tmp_path / "unit-run-001.json"

    written = write_validated_run_record(
        record,
        output,
    )

    assert written == output

    loaded = json.loads(
        output.read_text(encoding="utf-8")
    )

    assert loaded == record

    with pytest.raises(FileExistsError):
        write_validated_run_record(
            record,
            output,
        )


def test_retrieval_config_mismatch_is_rejected() -> None:
    retriever = _base_retriever()

    bad_configuration = RunConfiguration(
        model_provider="engineering-test",
        model_name="no-model",
        temperature=None,
        prompt_version="engineering-test-v0.1",
        retrieval_config_id="wrong-retriever",
    )

    recorder = RunRecorder(
        run_id="unit-run-002",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=bad_configuration,
    )

    with pytest.raises(
        ValueError,
        match="retrieval_config_id",
    ):
        LoggedRetriever(
            retriever,
            recorder,
        )


def test_invalid_retrieval_request_produces_valid_error_run() -> None:
    retriever = _base_retriever()
    recorder = _recorder(retriever)
    logged = LoggedRetriever(retriever, recorder)

    with pytest.raises(
        ValueError,
        match="top_k must be at least 1",
    ):
        logged.retrieve(
            "expense receipts",
            top_k=0,
        )

    record = recorder.build_record(
        status="tool_error",
        answer=None,
        abstained=False,
    )

    # The invalid request never becomes a malformed retrievalCall.
    assert record["usage"]["retrieval_calls"] == 0
    assert record["retrieval"]["calls"] == []

    assert len(record["errors"]) == 1
    assert record["errors"][0]["error_type"] == "ValueError"
    assert record["errors"][0]["stage"] == "retrieval"

    # Even the failure record must satisfy the frozen raw-run schema.
    validate_run_record(record)


def test_backend_retrieval_failure_is_recorded_and_valid() -> None:
    class FailingRetriever:
        config_id = "engineering-failing-retriever-v0.1"

        def retrieve(
            self,
            query: str,
            *,
            top_k: int,
        ):
            raise RuntimeError("Synthetic retrieval backend failure")

    retriever = FailingRetriever()

    configuration = RunConfiguration(
        model_provider="engineering-test",
        model_name="no-model",
        temperature=None,
        prompt_version="engineering-test-v0.1",
        retrieval_config_id=retriever.config_id,
    )

    recorder = RunRecorder(
        run_id="unit-run-failure-001",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=configuration,
    )

    logged = LoggedRetriever(
        retriever,
        recorder,
    )

    with pytest.raises(
        RuntimeError,
        match="Synthetic retrieval backend failure",
    ):
        logged.retrieve(
            "valid retrieval query",
            top_k=3,
        )

    record = recorder.build_record(
        status="tool_error",
        answer=None,
        abstained=False,
    )

    # A real backend attempt with valid parameters is retained.
    assert record["usage"]["retrieval_calls"] == 1

    calls = record["retrieval"]["calls"]

    assert len(calls) == 1
    assert calls[0]["sequence"] == 1
    assert calls[0]["query"] == "valid retrieval query"
    assert calls[0]["top_k"] == 3
    assert calls[0]["latency_ms"] >= 0
    assert calls[0]["retrieved_chunks"] == []

    assert len(record["errors"]) == 1
    assert record["errors"][0]["error_type"] == "RuntimeError"
    assert record["errors"][0]["stage"] == "retrieval"

    validate_run_record(record)
