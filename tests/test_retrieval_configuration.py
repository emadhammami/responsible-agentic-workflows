import json
from pathlib import Path

import pytest
from jsonschema import ValidationError

from responsible_agentic_workflows.retrieval import (
    load_retrieval_configuration,
    require_frozen_retrieval_configuration,
    validate_retrieval_configuration,
)


def _configuration(
    *,
    status: str = "working",
) -> dict[str, object]:
    return {
        "schema_version": "0.1",
        "retrieval_config_id": "test-retrieval-v0.1",
        "status": status,
        "backend": "dense-exact-cosine",
        "chunking_config_id": "test-chunking-v0.1",
        "embedding": {
            "provider": "ollama",
            "model_name": "example-embedding",
            "model_tag": "example-embedding:1b",
            "model_digest": None,
            "provider_version": None,
            "output_dimensions": None,
            "normalized": True,
            "truncate": False,
            "query_instruction": None,
            "document_instruction": None
        },
        "index": {
            "backend": "numpy",
            "backend_version": None,
            "index_type": "flat-exact",
            "distance_metric": "cosine",
            "dtype": "float32"
        }
    }


def test_working_configuration_validates() -> None:
    validate_retrieval_configuration(
        _configuration()
    )


def test_frozen_configuration_is_accepted() -> None:
    configuration = _configuration(
        status="frozen"
    )

    validate_retrieval_configuration(configuration)
    require_frozen_retrieval_configuration(
        configuration
    )


def test_working_configuration_is_not_execution_ready() -> None:
    with pytest.raises(
        ValueError,
        match="frozen retrieval configuration",
    ):
        require_frozen_retrieval_configuration(
            _configuration()
        )


def test_unknown_fields_are_rejected() -> None:
    configuration = _configuration()
    configuration["unexpected"] = True

    with pytest.raises(ValidationError):
        validate_retrieval_configuration(
            configuration
        )


def test_required_embedding_fields_are_enforced() -> None:
    configuration = _configuration()
    embedding = configuration["embedding"]
    assert isinstance(embedding, dict)

    del embedding["model_tag"]

    with pytest.raises(ValidationError):
        validate_retrieval_configuration(
            configuration
        )


def test_configuration_load_returns_independent_value(
    tmp_path: Path,
) -> None:
    configuration = _configuration()

    path = tmp_path / "retrieval.json"

    path.write_text(
        json.dumps(configuration),
        encoding="utf-8",
    )

    loaded = load_retrieval_configuration(
        path
    )

    assert loaded == configuration
    assert loaded is not configuration
