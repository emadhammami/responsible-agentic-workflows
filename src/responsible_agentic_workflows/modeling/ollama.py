"""Minimal Ollama chat adapter for the shared language model contract."""

import json
import urllib.error
import urllib.request

from .contracts import ModelRequest, ModelResponse, TokenUsage

DEFAULT_BASE_URL = "http://127.0.0.1:11434"


def _required_non_negative_int(
    data: dict[str, object],
    field: str,
) -> int:
    value = data.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise RuntimeError(
            f"Ollama response is missing required field: {field}"
        )
    return value


class OllamaChatModel:
    """Calls the local Ollama chat API for a single frozen model."""

    def __init__(
        self,
        *,
        model_name: str,
        config_id: str,
        context_length: int,
        seed: int,
        thinking: bool,
        timeout: float,
        base_url: str = DEFAULT_BASE_URL,
    ) -> None:
        if not model_name.strip():
            raise ValueError("model_name must not be empty")
        if not config_id.strip():
            raise ValueError("config_id must not be empty")
        if (
            not isinstance(context_length, int)
            or isinstance(context_length, bool)
            or context_length < 1
        ):
            raise ValueError("context_length must be a positive integer")
        if (
            not isinstance(seed, int)
            or isinstance(seed, bool)
            or seed < 0
        ):
            raise ValueError("seed must be a non-negative integer")
        if not isinstance(thinking, bool):
            raise TypeError("thinking must be a boolean")
        if (
            not isinstance(timeout, (int, float))
            or isinstance(timeout, bool)
            or timeout <= 0
        ):
            raise ValueError("timeout must be a positive number")

        self._model_name = model_name
        self._config_id = config_id
        self._endpoint = base_url.rstrip("/") + "/api/chat"
        self._context_length = context_length
        self._seed = seed
        self._thinking = thinking
        self._timeout = timeout

    @property
    def config_id(self) -> str:
        """Return a stable model configuration identifier."""

        return self._config_id

    @property
    def provider(self) -> str:
        """Return the model provider identifier."""

        return "ollama"

    @property
    def model_name(self) -> str:
        """Return the provider model identifier."""

        return self._model_name

    def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        """Generate one response for a provider-neutral request."""

        payload: dict[str, object] = {
            "model": self._model_name,
            "stream": False,
            "think": self._thinking,
            "messages": [
                {"role": message.role, "content": message.content}
                for message in request.messages
            ],
            "options": self._build_options(request),
        }
        return self._parse_response(self._post(payload))

    def _build_options(self, request: ModelRequest) -> dict[str, object]:
        options: dict[str, object] = {
            "num_ctx": self._context_length,
            "seed": self._seed,
        }
        if request.temperature is not None:
            options["temperature"] = request.temperature
        if request.max_output_tokens is not None:
            options["num_predict"] = request.max_output_tokens
        return options

    def _post(self, payload: dict[str, object]) -> dict[str, object]:
        body = json.dumps(payload).encode("utf-8")
        message = urllib.request.Request(
            self._endpoint,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                message,
                timeout=self._timeout,
            ) as response:
                raw = response.read()
        except urllib.error.HTTPError as error:
            raise RuntimeError(
                f"Ollama returned HTTP {error.code}: {error.reason}"
            ) from error
        except OSError as error:
            raise RuntimeError("Ollama provider connection failed") from error

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as error:
            raise RuntimeError("Ollama returned invalid JSON") from error

        if not isinstance(data, dict):
            raise RuntimeError("Ollama response must be a JSON object")
        return data

    def _parse_response(self, data: dict[str, object]) -> ModelResponse:
        provider_error = data.get("error")
        if isinstance(provider_error, str) and provider_error:
            raise RuntimeError(
                f"Ollama provider error: {provider_error}"
            )

        if data.get("done") is not True:
            raise RuntimeError(
                "Ollama response did not complete successfully"
            )

        message = data.get("message")
        if (
            not isinstance(message, dict)
            or not isinstance(message.get("content"), str)
        ):
            raise RuntimeError(
                "Ollama response is missing message.content"
            )

        done_reason = data.get("done_reason")
        finish_reason = done_reason if isinstance(done_reason, str) else None

        return ModelResponse(
            text=message["content"],
            usage=TokenUsage(
                input_tokens=_required_non_negative_int(
                    data,
                    "prompt_eval_count",
                ),
                output_tokens=_required_non_negative_int(
                    data,
                    "eval_count",
                ),
            ),
            finish_reason=finish_reason,
            provider_response_id=None,
        )
