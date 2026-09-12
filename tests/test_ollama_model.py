import json
import urllib.error
import urllib.request
from typing import Any

import pytest

from responsible_agentic_workflows.modeling import (
    LanguageModel,
    ModelMessage,
    ModelRequest,
    OllamaChatModel,
)


class FakeResponse:
    def __init__(self, payload: dict[str, Any] | str) -> None:
        if isinstance(payload, str):
            self._body = payload.encode("utf-8")
        else:
            self._body = json.dumps(payload).encode("utf-8")

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *exc_info: object) -> None:
        return None


@pytest.fixture
def captured():
    """Capture the payload passed to the mocked Ollama endpoint."""

    state: dict[str, object] = {}

    def fake_urlopen(request: urllib.request.Request, **kwargs: object) -> Any:
        state["request"] = request
        state["kwargs"] = kwargs
        return FakeResponse(state["response"])  # type: ignore[arg-type]

    state["fake_urlopen"] = fake_urlopen
    state["response"] = {
        "message": {"role": "assistant", "content": "Synthetic answer"},
        "done": True,
        "done_reason": "stop",
        "prompt_eval_count": 42,
        "eval_count": 7,
    }

    yield state


def make_model() -> OllamaChatModel:
    return OllamaChatModel(
        model_name="synthetic-model:latest",
        config_id="OLLMATEST-v0.1",
        context_length=49152,
        seed=20260912,
        base_url="http://127.0.0.1:11434",
        thinking=False,
        timeout=30.0,
    )


def request(
    *,
    temperature: float | None = 0.0,
    max_output_tokens: int | None = 200,
) -> ModelRequest:
    return ModelRequest(
        messages=(
            ModelMessage(role="system", content="Answer from evidence only."),
            ModelMessage(role="user", content="Synthetic question"),
        ),
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )


def post(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> dict[str, Any]:
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        captured["fake_urlopen"],  # type: ignore[arg-type]
    )
    model = make_model()
    model.generate(request())
    raw = captured["request"].data  # type: ignore[union-attr]
    return json.loads(raw.decode("utf-8"))


def test_satisfies_language_model_protocol() -> None:
    assert isinstance(make_model(), LanguageModel)


def test_exposes_config_id_provider_and_model_name() -> None:
    model = make_model()

    assert model.provider == "ollama"
    assert model.config_id == "OLLMATEST-v0.1"
    assert model.model_name == "synthetic-model:latest"


def test_request_fields_map_to_ollama_payload(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    payload = post(monkeypatch, captured)

    assert payload["model"] == "synthetic-model:latest"
    assert payload["stream"] is False
    assert payload["messages"] == [
        {"role": "system", "content": "Answer from evidence only."},
        {"role": "user", "content": "Synthetic question"},
    ]

    options = payload["options"]
    assert options["num_ctx"] == 49152
    assert options["seed"] == 20260912
    assert options["temperature"] == 0.0
    assert options["num_predict"] == 200


def test_thinking_false_is_explicit_in_payload(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    payload = post(monkeypatch, captured)

    assert "think" in payload
    assert payload["think"] is False


def test_omits_temperature_and_num_predict_when_unset(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        captured["fake_urlopen"],  # type: ignore[arg-type]
    )

    make_model().generate(
        request(temperature=None, max_output_tokens=None),
    )

    options = json.loads(
        captured["request"].data,  # type: ignore[union-attr]
    )["options"]

    assert "temperature" not in options
    assert "num_predict" not in options
    assert 1024 not in options.values()
    assert options["num_ctx"] == 49152
    assert options["seed"] == 20260912


def test_response_maps_to_model_response(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        captured["fake_urlopen"],  # type: ignore[arg-type]
    )

    response = make_model().generate(request())

    assert response.text == "Synthetic answer"
    assert response.usage.input_tokens == 42
    assert response.usage.output_tokens == 7
    assert response.usage.total_tokens == 49
    assert response.finish_reason == "stop"
    assert response.provider_response_id is None


def test_invalid_json_raises_runtime_error(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    captured["response"] = "{not-json"

    with pytest.raises(RuntimeError, match="invalid JSON"):
        post(monkeypatch, captured)


@pytest.mark.parametrize(
    "payload",
    [
        {"message": {"content": 5}, "prompt_eval_count": 1, "eval_count": 1},
        {"prompt_eval_count": 1, "eval_count": 1},
        {"message": {"content": "x"}, "eval_count": 1},
        ["not-an-object"],
    ],
)
def test_malformed_response_fails_clearly(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
    payload: object,
) -> None:
    captured["response"] = payload

    with pytest.raises(RuntimeError, match="Ollama response"):
        post(monkeypatch, captured)


def test_http_error_raises_without_retry(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    calls: list[object] = []

    def raising_urlopen(*args: object, **kwargs: object) -> Any:
        calls.append(args)
        raise urllib.error.HTTPError(
            url="http://127.0.0.1:11434/api/chat",
            code=500,
            msg="error",
            hdrs=None,
            fp=None,
        )

    monkeypatch.setattr(urllib.request, "urlopen", raising_urlopen)

    with pytest.raises(RuntimeError, match="Ollama returned HTTP 500"):
        make_model().generate(request())

    assert len(calls) == 1


def test_connection_failure_raises_without_retry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[object] = []

    def raising_urlopen(*args: object, **kwargs: object) -> Any:
        calls.append(args)
        raise OSError("connection refused")

    monkeypatch.setattr(urllib.request, "urlopen", raising_urlopen)

    with pytest.raises(RuntimeError, match="connection failed"):
        make_model().generate(request())

    assert len(calls) == 1


def test_request_timeout_is_forwarded(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    post(monkeypatch, captured)

    assert captured["kwargs"] == {"timeout": 30.0}


def test_endpoint_uses_explicit_base_url(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    post(monkeypatch, captured)

    assert (
        captured["request"].full_url  # type: ignore[union-attr]
        == "http://127.0.0.1:11434/api/chat"
    )

def test_incomplete_response_fails_clearly(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    captured["response"] = {
        "message": {"role": "assistant", "content": "Partial answer"},
        "done": False,
        "prompt_eval_count": 10,
        "eval_count": 2,
    }

    with pytest.raises(RuntimeError, match="did not complete"):
        post(monkeypatch, captured)


def test_provider_error_field_fails_clearly(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    captured["response"] = {
        "error": "synthetic provider failure",
    }

    with pytest.raises(RuntimeError, match="synthetic provider failure"):
        post(monkeypatch, captured)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("thinking", None, "thinking must be a boolean"),
        ("timeout", 0.0, "timeout must be a positive number"),
    ],
)
def test_research_settings_must_be_explicit_and_valid(
    field: str,
    value: object,
    message: str,
) -> None:
    kwargs = {
        "model_name": "synthetic-model:latest",
        "config_id": "OLLMATEST-v0.1",
        "context_length": 49152,
        "seed": 20260912,
        "thinking": False,
        "timeout": 30.0,
    }
    kwargs[field] = value

    with pytest.raises((TypeError, ValueError), match=message):
        OllamaChatModel(**kwargs)
