"""Language model wrapper with per-call execution logging."""

from time import perf_counter_ns

from responsible_agentic_workflows.modeling import (
    LanguageModel,
    ModelRequest,
    ModelResponse,
)

from .run_record import RunRecorder


def _elapsed_ms(start_ns: int) -> float:
    return max(
        0.0,
        (perf_counter_ns() - start_ns) / 1_000_000,
    )


class LoggedLanguageModel:
    """Wrap a language model and record each provider call."""

    def __init__(
        self,
        model: LanguageModel,
        recorder: RunRecorder,
    ) -> None:
        configuration = recorder.configuration

        if configuration.model_config_id != model.config_id:
            raise ValueError(
                "Recorder model_config_id does not match model"
            )

        if configuration.model_provider != model.provider:
            raise ValueError(
                "Recorder model_provider does not match model"
            )

        if configuration.model_name != model.model_name:
            raise ValueError(
                "Recorder model_name does not match model"
            )

        self._model = model
        self._recorder = recorder

    @property
    def config_id(self) -> str:
        """Return the wrapped model configuration identifier."""

        return self._model.config_id

    @property
    def provider(self) -> str:
        """Return the wrapped model provider."""

        return self._model.provider

    @property
    def model_name(self) -> str:
        """Return the wrapped provider model identifier."""

        return self._model.model_name

    def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        """Generate one response and record resource metadata."""

        started_ns = perf_counter_ns()

        try:
            response = self._model.generate(request)
        except Exception as exc:
            self._recorder.record_model_call(
                status="failed",
                latency_ms=_elapsed_ms(started_ns),
                usage=None,
                finish_reason=None,
                provider_response_id=None,
            )

            self._recorder.record_error(
                error_type=type(exc).__name__,
                message=str(exc),
                stage="model",
                retryable=None,
            )

            raise

        self._recorder.record_model_call(
            status="completed",
            latency_ms=_elapsed_ms(started_ns),
            usage=response.usage,
            finish_reason=response.finish_reason,
            provider_response_id=response.provider_response_id,
        )

        return response
