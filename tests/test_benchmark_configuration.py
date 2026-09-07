import json
from pathlib import Path

import pytest
from jsonschema import ValidationError

from responsible_agentic_workflows.benchmark import (
    load_benchmark_configuration,
    require_frozen_benchmark_configuration,
    validate_benchmark_configuration,
)


def _configuration(
    *,
    status: str = "working",
) -> dict[str, object]:
    return {
        "schema_version": "0.1",
        "config_id": "benchmark-config-unit-test-v0.1",
        "status": status,
        "model": {
            "provider": "test-provider",
            "model_name": "test-model",
            "model_config_id": "test-model-v0.1",
            "model_version": None,
            "temperature": 0.0,
            "max_output_tokens": 500,
        },
        "retrieval": {
            "retrieval_config_id": "test-retrieval-v0.1",
            "backend": "test-backend",
            "embedding_model": None,
            "vector_store": None,
            "chunking_config_id": "test-chunking-v0.1",
            "top_k": 4,
        },
        "prompts": {
            "b0_prompt_version": "b0-prompt-v0.1",
            "b1_prompt_version": "b1-prompt-v0.1",
            "g1_prompt_version": "g1-prompt-v0.1",
        },
        "workflows": {
            "b0_config_id": "b0-workflow-v0.1",
            "b1_config_id": "b1-workflow-v0.1",
            "g1_config_id": "g1-workflow-v0.1",
        },
        "resource_limits": {
            "max_total_tokens_per_run": None,
            "max_llm_calls_per_run": None,
            "max_retrieval_calls_per_run": None,
            "max_retries_per_run": 0,
        },
        "execution": {
            "repetitions": 1,
            "random_seed": None,
        },
    }


def test_working_configuration_validates() -> None:
    validate_benchmark_configuration(
        _configuration()
    )


def test_frozen_configuration_validates() -> None:
    configuration = _configuration(
        status="frozen",
    )

    validate_benchmark_configuration(configuration)
    require_frozen_benchmark_configuration(configuration)


def test_working_configuration_cannot_be_used_as_frozen() -> None:
    with pytest.raises(
        ValueError,
        match="requires a frozen configuration",
    ):
        require_frozen_benchmark_configuration(
            _configuration(status="working")
        )


def test_invalid_top_k_is_rejected() -> None:
    configuration = _configuration()

    configuration["retrieval"]["top_k"] = 0

    with pytest.raises(ValidationError):
        validate_benchmark_configuration(configuration)


def test_unknown_configuration_field_is_rejected() -> None:
    configuration = _configuration()
    configuration["unexpected"] = "not allowed"

    with pytest.raises(ValidationError):
        validate_benchmark_configuration(configuration)


def test_configuration_loader_round_trip(
    tmp_path: Path,
) -> None:
    configuration = _configuration()

    path = tmp_path / "benchmark-config.json"

    path.write_text(
        json.dumps(
            configuration,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    loaded = load_benchmark_configuration(path)

    assert loaded == configuration
    assert loaded is not configuration


def test_shared_model_and_retrieval_are_single_configuration_blocks() -> None:
    configuration = _configuration()

    assert set(configuration["model"]) == {
        "provider",
        "model_name",
        "model_config_id",
        "model_version",
        "temperature",
        "max_output_tokens",
    }

    assert set(configuration["retrieval"]) == {
        "retrieval_config_id",
        "backend",
        "embedding_model",
        "vector_store",
        "chunking_config_id",
        "top_k",
    }
