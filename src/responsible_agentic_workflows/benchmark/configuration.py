"""Benchmark configuration loading and validation."""

import json
from copy import deepcopy
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

DEFAULT_BENCHMARK_CONFIG_SCHEMA = Path(
    "benchmark/config/benchmark_config.schema.json"
)


def validate_benchmark_configuration(
    configuration: dict[str, object],
    *,
    schema_path: str | Path = DEFAULT_BENCHMARK_CONFIG_SCHEMA,
) -> None:
    """Validate a benchmark configuration against its JSON Schema."""

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    validator.validate(configuration)


def load_benchmark_configuration(
    path: str | Path,
    *,
    schema_path: str | Path = DEFAULT_BENCHMARK_CONFIG_SCHEMA,
) -> dict[str, object]:
    """Load and validate one benchmark configuration."""

    configuration = json.loads(
        Path(path).read_text(encoding="utf-8")
    )

    validate_benchmark_configuration(
        configuration,
        schema_path=schema_path,
    )

    return deepcopy(configuration)


def require_frozen_benchmark_configuration(
    configuration: dict[str, object],
) -> None:
    """Require a configuration that is frozen for benchmark execution."""

    validate_benchmark_configuration(configuration)

    if configuration["status"] != "frozen":
        raise ValueError(
            "Benchmark execution requires a frozen configuration"
        )
