"""Provider-neutral language model contracts."""

from dataclasses import dataclass
from typing import Literal, Protocol, runtime_checkable

MessageRole = Literal["system", "user", "assistant"]


@dataclass(frozen=True, slots=True)
class ModelMessage:
    """One message supplied to a language model."""

    role: MessageRole
    content: str

    def __post_init__(self) -> None:
        if self.role not in {"system", "user", "assistant"}:
            raise ValueError(f"Unsupported message role: {self.role}")

        if not self.content.strip():
            raise ValueError("Model message content must not be empty")


@dataclass(frozen=True, slots=True)
class ModelRequest:
    """Provider-neutral generation request."""

    messages: tuple[ModelMessage, ...]
    temperature: float | None
    max_output_tokens: int | None

    def __post_init__(self) -> None:
        if not self.messages:
            raise ValueError("Model request must contain at least one message")

        if self.temperature is not None and self.temperature < 0:
            raise ValueError("temperature must not be negative")

        if self.max_output_tokens is not None:
            if (
                not isinstance(self.max_output_tokens, int)
                or isinstance(self.max_output_tokens, bool)
                or self.max_output_tokens < 1
            ):
                raise ValueError(
                    "max_output_tokens must be a positive integer or None"
                )


@dataclass(frozen=True, slots=True)
class TokenUsage:
    """Provider-reported token usage for one model call."""

    input_tokens: int
    output_tokens: int

    def __post_init__(self) -> None:
        for name, value in (
            ("input_tokens", self.input_tokens),
            ("output_tokens", self.output_tokens),
        ):
            if (
                not isinstance(value, int)
                or isinstance(value, bool)
                or value < 0
            ):
                raise ValueError(
                    f"{name} must be a non-negative integer"
                )

    @property
    def total_tokens(self) -> int:
        """Return the total number of tokens reported for the call."""

        return self.input_tokens + self.output_tokens


@dataclass(frozen=True, slots=True)
class ModelResponse:
    """Provider-neutral result from one model call."""

    text: str
    usage: TokenUsage
    finish_reason: str | None = None
    provider_response_id: str | None = None


@runtime_checkable
class LanguageModel(Protocol):
    """Common language model interface used by all workflow conditions."""

    @property
    def config_id(self) -> str:
        """Return a stable model configuration identifier."""
        ...

    @property
    def provider(self) -> str:
        """Return the model provider identifier."""
        ...

    @property
    def model_name(self) -> str:
        """Return the provider model identifier."""
        ...

    def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        """Generate one response for a provider-neutral request."""
        ...
