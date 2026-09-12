import json

import pytest

from responsible_agentic_workflows.benchmark import RuntimeTask
from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.logging import (
    RunConfiguration,
    RunRecorder,
    validate_run_record,
)
from responsible_agentic_workflows.modeling import (
    ModelRequest,
    ModelResponse,
    TokenUsage,
)
from responsible_agentic_workflows.retrieval import RetrievedChunk
from responsible_agentic_workflows.workflow import B0Baseline

STUB_MODEL_CONFIG_ID = "engineering-b0-stub-model-v0.1"
STUB_RETRIEVAL_CONFIG_ID = "engineering-b0-stub-retriever-v0.1"
QUESTION = (
    "Who must approve ordinary international business travel "
    "before it is booked?"
)


def _make_chunk(chunk_id: str, text: str) -> DocumentChunk:
    return DocumentChunk(
        document_id="DOC901",
        chunk_id=chunk_id,
        title="Travel and Expense Policy",
        section="International travel",
        section_index=1,
        text=text,
        source_file="DOC901.md",
        page=None,
    )


_CHUNKS = (
    RetrievedChunk(
        chunk=_make_chunk(
            "DOC901-C001",
            "International business travel must be approved by the "
            "employee's department head before travel is booked.",
        ),
        rank=1,
        score=0.98,
    ),
    RetrievedChunk(
        chunk=_make_chunk(
            "DOC901-C002",
            "Receipts for reimbursable travel expenses are required.",
        ),
        rank=2,
        score=0.91,
    ),
    RetrievedChunk(
        chunk=_make_chunk(
            "DOC901-C003",
            "This policy applies to ordinary business travel.",
        ),
        rank=3,
        score=0.87,
    ),
)


class CountingRetriever:
    config_id = STUB_RETRIEVAL_CONFIG_ID

    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    def retrieve(self, query: str, *, top_k: int):
        self.calls.append((query, top_k))

        return list(_CHUNKS)[:top_k]


class CountingModel:
    config_id = STUB_MODEL_CONFIG_ID
    provider = "engineering-test"
    model_name = "b0-stub"

    def __init__(self) -> None:
        self.requests: list[ModelRequest] = []

    def generate(self, request: ModelRequest) -> ModelResponse:
        self.requests.append(request)

        return ModelResponse(
            text="The employee's department head must approve the travel.",
            usage=TokenUsage(input_tokens=42, output_tokens=9),
            finish_reason="stop",
            provider_response_id="b0-stub-response-001",
        )


class FailingRetriever:
    config_id = STUB_RETRIEVAL_CONFIG_ID

    def __init__(self) -> None:
        self.calls = 0

    def retrieve(self, query: str, *, top_k: int):
        self.calls += 1
        raise RuntimeError("Synthetic retrieval backend failure")


class FailingModel:
    config_id = STUB_MODEL_CONFIG_ID
    provider = "engineering-test"
    model_name = "b0-stub"

    def __init__(self) -> None:
        self.calls = 0

    def generate(self, request: ModelRequest) -> ModelResponse:
        self.calls += 1
        raise RuntimeError("Synthetic model failure")


def _recorder(
    *,
    task_id: str = "T901",
    execution_mode: str = "engineering",
    condition: str | None = None,
    prompt_version: str = B0Baseline.PROMPT_VERSION,
    workflow_config_id: str = B0Baseline.WORKFLOW_CONFIG_ID,
) -> RunRecorder:
    configuration = RunConfiguration(
        model_provider="engineering-test",
        model_name="b0-stub",
        model_config_id=STUB_MODEL_CONFIG_ID,
        model_version=None,
        temperature=0.0,
        max_output_tokens=64,
        prompt_version=prompt_version,
        retrieval_config_id=STUB_RETRIEVAL_CONFIG_ID,
        workflow_config_id=workflow_config_id,
        random_seed=None,
    )

    return RunRecorder(
        run_id="b0-run-001",
        experiment_id="engineering-b0",
        task_id=task_id,
        execution_mode=execution_mode,
        condition=condition,
        code_revision="abcdef1",
        configuration=configuration,
    )


def _task() -> RuntimeTask:
    return RuntimeTask(task_id="T901", question=QUESTION)


def _run_ok(retriever, model, *, top_k: int | None = None):
    recorder = _recorder()
    baseline = B0Baseline(retriever=retriever, model=model, top_k=3)
    result = baseline.run(_task(), recorder=recorder, top_k=top_k)
    return retriever, model, result, recorder


def test_performs_exactly_one_retrieval() -> None:
    retriever, _model, _result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    assert len(retriever.calls) == 1


def test_performs_exactly_one_generation() -> None:
    _retriever, model, _result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    assert len(model.requests) == 1


def test_retrieval_query_is_the_task_question() -> None:
    retriever, _model, _result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    assert retriever.calls[0][0] == QUESTION


def test_top_k_is_passed_through() -> None:
    retriever, _model, result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
        top_k=2,
    )

    assert retriever.calls[0][1] == 2
    assert len(result.chunks) == 2


def test_retrieved_context_is_included_in_the_model_request() -> None:
    _retriever, model, _result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    messages = model.requests[0].messages
    user_content = messages[-1].content
    system_content = messages[0].content

    assert "department head" in user_content
    assert "document_id=DOC901" in user_content
    assert "chunk_id=DOC901-C001" in user_content
    assert "page=unknown" in user_content
    assert "section=International travel" in user_content
    assert QUESTION in user_content
    assert "Answer using only the retrieved context" in system_content


def test_record_preserves_retrieval_provenance() -> None:
    _retriever, _model, result, recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    record = recorder.build_record(
        status="completed",
        answer=result.answer,
        abstained=False,
    )

    calls = record["retrieval"]["calls"]

    assert len(calls) == 1
    assert calls[0]["query"] == QUESTION
    assert calls[0]["top_k"] == 3
    assert [
        entry["chunk_id"] for entry in calls[0]["retrieved_chunks"]
    ] == ["DOC901-C001", "DOC901-C002", "DOC901-C003"]

    assert result.record is record or result.record["run_id"] == (
        "b0-run-001"
    )


def test_record_contains_no_gold_fields() -> None:
    _retriever, _model, result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    serialized = json.dumps(result.record)

    forbidden = {
        "reference_answer",
        "reference_evidence",
        "required_documents",
        "task_type",
        "validation_status",
    }

    for field in forbidden:
        assert field not in serialized


def test_retrieval_failure_performs_no_second_retrieval() -> None:
    retriever = FailingRetriever()

    with pytest.raises(RuntimeError):
        _run_ok(retriever, CountingModel())

    assert retriever.calls == 1


def test_model_failure_performs_no_retry() -> None:
    _retriever, model = CountingRetriever(), FailingModel()

    with pytest.raises(RuntimeError):
        _run_ok(_retriever, model)

    assert model.calls == 1


def test_run_recorder_logs_both_stages() -> None:
    _retriever, _model, _result, recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    record = recorder.build_record(
        status="completed",
        answer="synthetic",
        abstained=False,
    )

    assert len(record["retrieval"]["calls"]) == 1
    assert len(record["model"]["calls"]) == 1

    model_call = record["model"]["calls"][0]

    assert model_call["status"] == "completed"
    assert model_call["input_tokens"] == 42
    assert model_call["output_tokens"] == 9
    assert record["usage"]["retrieval_calls"] == 1
    assert record["usage"]["llm_calls"] == 1


def test_record_validates_against_schema() -> None:
    _retriever, _model, _result, recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    record = recorder.build_record(
        status="completed",
        answer="synthetic",
        abstained=False,
    )

    validate_run_record(record)
    assert record["condition"] in ("B0", None)


def test_retrieved_chunks_are_not_auto_cited() -> None:
    _retriever, _model, result, _recorder = _run_ok(
        CountingRetriever(),
        CountingModel(),
    )

    retrieved = result.record["retrieval"]["calls"][0][
        "retrieved_chunks"
    ]

    assert retrieved
    assert result.record["final_output"]["cited_chunk_ids"] == []

def test_rejects_prompt_version_mismatch() -> None:
    retriever = CountingRetriever()
    model = CountingModel()
    recorder = _recorder(prompt_version="wrong-prompt-v0")

    baseline = B0Baseline(
        retriever=retriever,
        model=model,
        top_k=3,
    )

    with pytest.raises(ValueError, match="prompt_version"):
        baseline.run(
            _task(),
            recorder=recorder,
        )

    assert retriever.calls == []
    assert model.requests == []


def test_rejects_workflow_config_id_mismatch() -> None:
    retriever = CountingRetriever()
    model = CountingModel()
    recorder = _recorder(workflow_config_id="wrong-workflow-v0")

    baseline = B0Baseline(
        retriever=retriever,
        model=model,
        top_k=3,
    )

    with pytest.raises(ValueError, match="workflow_config_id"):
        baseline.run(
            _task(),
            recorder=recorder,
        )

    assert retriever.calls == []
    assert model.requests == []

def test_rejects_recorder_task_id_mismatch() -> None:
    retriever = CountingRetriever()
    model = CountingModel()
    recorder = _recorder(task_id="T999")

    baseline = B0Baseline(
        retriever=retriever,
        model=model,
        top_k=3,
    )

    with pytest.raises(ValueError, match="task_id"):
        baseline.run(
            _task(),
            recorder=recorder,
        )

    assert retriever.calls == []
    assert model.requests == []


def test_rejects_non_b0_benchmark_condition() -> None:
    retriever = CountingRetriever()
    model = CountingModel()
    recorder = _recorder(
        execution_mode="benchmark",
        condition="B1",
    )

    baseline = B0Baseline(
        retriever=retriever,
        model=model,
        top_k=3,
    )

    with pytest.raises(ValueError, match="condition B0"):
        baseline.run(
            _task(),
            recorder=recorder,
        )

    assert retriever.calls == []
    assert model.requests == []


def test_accepts_b0_benchmark_condition() -> None:
    retriever = CountingRetriever()
    model = CountingModel()
    recorder = _recorder(
        execution_mode="benchmark",
        condition="B0",
    )

    baseline = B0Baseline(
        retriever=retriever,
        model=model,
        top_k=3,
    )

    result = baseline.run(
        _task(),
        recorder=recorder,
    )

    assert result.record["condition"] == "B0"
    assert len(retriever.calls) == 1
    assert len(model.requests) == 1
