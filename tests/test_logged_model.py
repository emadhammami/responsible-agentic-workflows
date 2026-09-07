import json

import pytest

from responsible_agentic_workflows.logging import (
    LoggedLanguageModel,
    RunConfiguration,
    RunRecorder,
    validate_run_record,
)
from responsible_agentic_workflows.modeling import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    TokenUsage,
)


class FakeModel:
    config_id = "fake-model-v0.1"
    provider = "test"
    model_name = "fake"

    def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        return ModelResponse(
            text="Synthetic response",
            usage=TokenUsage(
                input_tokens=11,
                output_tokens=4,
            ),
            finish_reason="stop",
            provider_response_id="response-001",
        )


class FailingModel:
    config_id = "failing-model-v0.1"
    provider = "test"
    model_name = "failing"

    def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        raise RuntimeError("Synthetic model failure")


def _request() -> ModelRequest:
    return ModelRequest(
        messages=(
            ModelMessage(
                role="user",
                content="Sensitive test question",
            ),
        ),
        temperature=0.0,
        max_output_tokens=100,
    )


def _recorder(
    *,
    model_config_id: str,
    model_name: str,
) -> RunRecorder:
    configuration = RunConfiguration(
        model_provider="test",
        model_name=model_name,
        model_config_id=model_config_id,
        model_version=None,
        temperature=0.0,
        max_output_tokens=100,
        prompt_version="unit-test-v0.1",
        retrieval_config_id="no-retrieval",
        workflow_config_id="unit-test",
        random_seed=None,
    )

    return RunRecorder(
        run_id="model-log-test",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=configuration,
    )


def test_logged_model_records_calls_and_usage() -> None:
    recorder = _recorder(
        model_config_id=FakeModel.config_id,
        model_name=FakeModel.model_name,
    )

    model = LoggedLanguageModel(
        FakeModel(),
        recorder,
    )

    first = model.generate(_request())
    second = model.generate(_request())

    record = recorder.build_record(
        status="completed",
        answer=second.text,
        abstained=False,
    )

    validate_run_record(record)

    assert first.text == "Synthetic response"

    calls = record["model"]["calls"]

    assert len(calls) == 2
    assert calls[0]["sequence"] == 1
    assert calls[1]["sequence"] == 2
    assert calls[0]["status"] == "completed"
    assert calls[0]["input_tokens"] == 11
    assert calls[0]["output_tokens"] == 4
    assert calls[0]["total_tokens"] == 15
    assert calls[0]["finish_reason"] == "stop"
    assert calls[0]["provider_response_id"] == "response-001"
    assert calls[0]["latency_ms"] >= 0

    assert record["usage"]["llm_calls"] == 2
    assert record["usage"]["input_tokens"] == 22
    assert record["usage"]["output_tokens"] == 8
    assert record["usage"]["total_tokens"] == 30
    assert record["timing"]["llm_ms"] >= 0


def test_model_trace_does_not_duplicate_prompt_or_response_text() -> None:
    recorder = _recorder(
        model_config_id=FakeModel.config_id,
        model_name=FakeModel.model_name,
    )

    model = LoggedLanguageModel(
        FakeModel(),
        recorder,
    )

    model.generate(_request())

    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )

    model_trace = json.dumps(record["model"])

    assert "Sensitive test question" not in model_trace
    assert "Synthetic response" not in model_trace


def test_failed_model_call_remains_schema_valid() -> None:
    recorder = _recorder(
        model_config_id=FailingModel.config_id,
        model_name=FailingModel.model_name,
    )

    model = LoggedLanguageModel(
        FailingModel(),
        recorder,
    )

    with pytest.raises(
        RuntimeError,
        match="Synthetic model failure",
    ):
        model.generate(_request())

    record = recorder.build_record(
        status="tool_error",
        answer=None,
        abstained=False,
    )

    validate_run_record(record)

    assert record["usage"]["llm_calls"] == 1
    assert record["usage"]["input_tokens"] == 0
    assert record["usage"]["output_tokens"] == 0

    call = record["model"]["calls"][0]

    assert call["status"] == "failed"
    assert call["input_tokens"] is None
    assert call["output_tokens"] is None
    assert call["total_tokens"] is None
    assert call["latency_ms"] >= 0

    assert len(record["errors"]) == 1
    assert record["errors"][0]["stage"] == "model"


def test_model_configuration_mismatch_is_rejected() -> None:
    recorder = _recorder(
        model_config_id="different-config",
        model_name=FakeModel.model_name,
    )

    with pytest.raises(
        ValueError,
        match="model_config_id",
    ):
        LoggedLanguageModel(
            FakeModel(),
            recorder,
        )
