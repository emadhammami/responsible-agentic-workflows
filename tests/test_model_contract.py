import pytest

from responsible_agentic_workflows.modeling import (
    LanguageModel,
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
            text=request.messages[-1].content,
            usage=TokenUsage(
                input_tokens=10,
                output_tokens=4,
            ),
            finish_reason="stop",
            provider_response_id="test-response-001",
        )


def test_model_request_preserves_message_order() -> None:
    request = ModelRequest(
        messages=(
            ModelMessage(
                role="system",
                content="Answer using the supplied evidence.",
            ),
            ModelMessage(
                role="user",
                content="What is the policy requirement?",
            ),
        ),
        temperature=0.0,
        max_output_tokens=200,
    )

    assert [message.role for message in request.messages] == [
        "system",
        "user",
    ]

    assert request.temperature == 0.0
    assert request.max_output_tokens == 200


def test_token_usage_total_is_derived_consistently() -> None:
    usage = TokenUsage(
        input_tokens=125,
        output_tokens=35,
    )

    assert usage.total_tokens == 160


def test_fake_model_satisfies_shared_protocol() -> None:
    model = FakeModel()

    assert isinstance(model, LanguageModel)

    request = ModelRequest(
        messages=(
            ModelMessage(
                role="user",
                content="Test question",
            ),
        ),
        temperature=None,
        max_output_tokens=None,
    )

    response = model.generate(request)

    assert response.text == "Test question"
    assert response.usage.input_tokens == 10
    assert response.usage.output_tokens == 4
    assert response.usage.total_tokens == 14
    assert response.finish_reason == "stop"


def test_empty_model_message_is_rejected() -> None:
    with pytest.raises(
        ValueError,
        match="content must not be empty",
    ):
        ModelMessage(
            role="user",
            content="   ",
        )


def test_empty_model_request_is_rejected() -> None:
    with pytest.raises(
        ValueError,
        match="at least one message",
    ):
        ModelRequest(
            messages=(),
            temperature=0.0,
            max_output_tokens=100,
        )


@pytest.mark.parametrize(
    "input_tokens, output_tokens",
    [
        (-1, 0),
        (0, -1),
        (True, 0),
        (0, False),
    ],
)
def test_invalid_token_usage_is_rejected(
    input_tokens: int,
    output_tokens: int,
) -> None:
    with pytest.raises(ValueError):
        TokenUsage(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )


def test_invalid_max_output_tokens_is_rejected() -> None:
    with pytest.raises(
        ValueError,
        match="positive integer",
    ):
        ModelRequest(
            messages=(
                ModelMessage(
                    role="user",
                    content="Question",
                ),
            ),
            temperature=0.0,
            max_output_tokens=0,
        )
