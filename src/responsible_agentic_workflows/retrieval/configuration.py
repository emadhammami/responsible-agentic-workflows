"""Retrieval configuration loading and validation."""

import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator

DEFAULT_RETRIEVAL_CONFIG_SCHEMA = Path(
    "benchmark/config/retrieval_config.schema.json"
)


def validate_retrieval_configuration(
    configuration: dict[str, object],
    *,
    schema_path: str | Path = DEFAULT_RETRIEVAL_CONFIG_SCHEMA,
) -> None:
    """Validate a retrieval configuration against its JSON Schema."""

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)

    validator = Draft202012Validator(schema)
    validator.validate(configuration)


def load_retrieval_configuration(
    path: str | Path,
    *,
    schema_path: str | Path = DEFAULT_RETRIEVAL_CONFIG_SCHEMA,
) -> dict[str, object]:
    """Load and validate one retrieval configuration."""

    configuration = json.loads(
        Path(path).read_text(encoding="utf-8")
    )

    validate_retrieval_configuration(
        configuration,
        schema_path=schema_path,
    )

    return deepcopy(configuration)


def require_frozen_retrieval_configuration(
    configuration: dict[str, object],
) -> None:
    """Require a retrieval configuration frozen for benchmark execution."""

    validate_retrieval_configuration(configuration)

    if configuration["status"] != "frozen":
        raise ValueError(
            "Benchmark execution requires a frozen retrieval configuration"
        )
