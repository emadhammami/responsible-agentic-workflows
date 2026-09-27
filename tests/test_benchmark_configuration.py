import json
from hashlib import sha256
from pathlib import Path

import pytest
from jsonschema import ValidationError

from responsible_agentic_workflows.benchmark import (
    load_benchmark_configuration,
    require_frozen_benchmark_configuration,
    validate_benchmark_configuration,
)

ARCHIVED_SCHEMA_PATH = Path("benchmark/config/benchmark_config.schema.v0.1.json")
PRIMARY_CONFIG_PATH = Path("benchmark/config/primary")
PRIMARY_FREEZE_MANIFEST_PATH = (
    PRIMARY_CONFIG_PATH / "primary_benchmark_config_freeze_manifest.json"
)


def _configuration(
    *,
    status: str = "working",
) -> dict[str, object]:
    return {
        "schema_version": "0.2",
        "config_id": "benchmark-config-unit-test-v0.2",
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
            "g1_prompt_version": "b1-prompt-v0.1",
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
            "timeout_ms": None,
        },
        "execution": {
            "repetitions": 1,
            "random_seed": None,
        },
    }


def test_archived_v01_schema_preserves_bytes_and_validates_v01() -> None:
    archived_bytes = ARCHIVED_SCHEMA_PATH.read_bytes()
    assert sha256(archived_bytes).hexdigest() == (
        "bf6935fb64198bcec87fbac837f05aec85d731c940cc4910973c3c8489db48a7"
    )

    configuration = _configuration()
    configuration["schema_version"] = "0.1"
    del configuration["resource_limits"]["timeout_ms"]
    validate_benchmark_configuration(configuration, schema_path=ARCHIVED_SCHEMA_PATH)


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


def test_v02_requires_timeout_ms() -> None:
    configuration = _configuration()
    del configuration["resource_limits"]["timeout_ms"]

    with pytest.raises(ValidationError, match="timeout_ms"):
        validate_benchmark_configuration(configuration)


@pytest.mark.parametrize("timeout_ms", [None, 1, 1.5])
def test_valid_timeout_ms(timeout_ms: float | None) -> None:
    configuration = _configuration()
    configuration["resource_limits"]["timeout_ms"] = timeout_ms

    validate_benchmark_configuration(configuration)


@pytest.mark.parametrize("timeout_ms", [0, -1, -0.5])
def test_nonpositive_timeout_ms_is_rejected(timeout_ms: float) -> None:
    configuration = _configuration()
    configuration["resource_limits"]["timeout_ms"] = timeout_ms

    with pytest.raises(ValidationError, match="minimum"):
        validate_benchmark_configuration(configuration)


def test_b1_g1_prompt_mismatch_is_rejected() -> None:
    configuration = _configuration()
    configuration["prompts"]["g1_prompt_version"] = "different-prompt-v0.1"

    with pytest.raises(
        ValidationError,
        match=r"prompts\.b1_prompt_version must equal prompts\.g1_prompt_version",
    ):
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


@pytest.mark.parametrize(
    ("use_case", "chunking_config_id"),
    [
        ("uc1", "UC1-PAGE-W450-O75-v0.1"),
        ("uc2", "UC2-SOURCEUNIT-W450-O75-v0.1"),
        ("uc3", "UC3-PAGE-W450-O75-v0.1"),
    ],
)
def test_frozen_primary_configuration(
    use_case: str, chunking_config_id: str
) -> None:
    config_id = f"benchmark-config-primary-{use_case}-v0.2"
    configuration = load_benchmark_configuration(
        PRIMARY_CONFIG_PATH / f"{config_id}.json"
    )

    assert configuration == {
        "schema_version": "0.2",
        "config_id": config_id,
        "status": "frozen",
        "model": {
            "provider": "ollama",
            "model_name": "qwen3.8-27b-48k:latest",
            "model_config_id": "OLLAMA-QWEN38-27B-48K-v0.1",
            "model_version": (
                "a68eeb5701b0a627f513a134f7ec029477a04b66a4605b32e27917ac93bd67a3"
            ),
            "temperature": 0,
            "max_output_tokens": 1024,
        },
        "retrieval": {
            "retrieval_config_id": (
                f"{use_case.upper()}-QWEN3-EMBED4B-EXACT-COSINE-v0.1"
            ),
            "backend": "dense-exact-cosine",
            "embedding_model": "qwen3-embedding:4b-q4_K_M",
            "vector_store": None,
            "chunking_config_id": chunking_config_id,
            "top_k": 10,
        },
        "prompts": {
            "b0_prompt_version": "b0-engineering-v0.1",
            "b1_prompt_version": "agentic-engineering-v0.1",
            "g1_prompt_version": "agentic-engineering-v0.1",
        },
        "workflows": {
            "b0_config_id": "b0-two-step-rag-v0.1",
            "b1_config_id": "b1-agentic-fixed-recovery-v0.1",
            "g1_config_id": "g1-agentic-ergr-v0.1",
        },
        "resource_limits": {
            "max_total_tokens_per_run": None,
            "max_llm_calls_per_run": 5,
            "max_retrieval_calls_per_run": 2,
            "max_retries_per_run": 1,
            "timeout_ms": None,
        },
        "execution": {
            "repetitions": 3,
            "random_seed": 20260912,
        },
    }

    assert configuration["prompts"]["b1_prompt_version"] == (
        configuration["prompts"]["g1_prompt_version"]
    )
    require_frozen_benchmark_configuration(configuration)


def test_primary_freeze_manifest_bindings_and_pending_execution() -> None:
    manifest = json.loads(PRIMARY_FREEZE_MANIFEST_PATH.read_text(encoding="utf-8"))

    assert manifest["schema_version"] == "0.1"
    assert manifest["freeze_id"] == "PRIMARY-BENCHMARK-CONFIG-FREEZE-v0.1"
    assert manifest["status"] == "frozen"
    assert manifest["implementation_parent_head"] == (
        "e3febd8fd0eb68dedf543519c7808d758132eedf"
    )
    assert manifest["benchmark_started"] is False
    assert manifest["result_driven_revision"] is False
    assert manifest["benchmark_ready_to_execute"] is False
    assert manifest["execution_order_manifest_frozen"] is False
    assert "NOT YET FROZEN" in manifest["execution_order_manifest_status"]
    assert "pending" in manifest["execution_order_manifest_status"]
    assert manifest["final_benchmark_execution_code_revision_frozen"] is False
    assert "orchestration/harness qualification remains pending" in (
        manifest["final_benchmark_execution_code_revision_status"]
    )

    expected_configs = {
        uc: f"benchmark/config/primary/benchmark-config-primary-{uc.lower()}-v0.2.json"
        for uc in ("UC1", "UC2", "UC3")
    }
    expected_artifacts = {
        "canonical_v0_2_schema": "benchmark/config/benchmark_config.schema.json",
        "archived_v0_1_schema": (
            "benchmark/config/benchmark_config.schema.v0.1.json"
        ),
        "frozen_decision_artifact": (
            "evidence/engineering/benchmark_configuration_decisions_v0.1_2026-09-27.md"
        ),
        "generation_model_configuration": (
            "benchmark/config/model/OLLAMA-QWEN38-27B-48K-v0.1.json"
        ),
        "task_set_plan": "benchmark/task_set_plan.json",
        "primary_30_task_freeze_manifest": (
            "benchmark/tasks/primary_benchmark_freeze_manifest.json"
        ),
    }
    expected_retrieval = {
        uc: f"benchmark/config/retrieval/{uc}-QWEN3-EMBED4B-EXACT-COSINE-v0.1.json"
        for uc in ("UC1", "UC2", "UC3")
    }
    expected_sources = {
        f"src/responsible_agentic_workflows/workflow/{name}.py"
        for name in (
            "b0_baseline",
            "agentic_execution",
            "graph",
            "agentic_nodes",
            "agentic_runner",
            "b1_policy",
            "g1_policy",
        )
    }

    for bindings, expected in (
        (manifest["authoritative_configs"], expected_configs),
        (manifest["artifact_bindings"], expected_artifacts),
        (manifest["retrieval_configuration_bindings"], expected_retrieval),
    ):
        assert set(bindings) == set(expected)
        for key, path in expected.items():
            assert bindings[key] == {
                "path": path,
                "sha256": sha256(Path(path).read_bytes()).hexdigest(),
            }

    assert set(manifest["source_bindings"]) == expected_sources
    for path in expected_sources:
        assert manifest["source_bindings"][path] == {
            "path": path,
            "sha256": sha256(Path(path).read_bytes()).hexdigest(),
        }
