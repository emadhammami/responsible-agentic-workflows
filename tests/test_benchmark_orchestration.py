"""Synthetic T901-T907 orchestration qualification, with no network access."""

import json
from types import SimpleNamespace

import numpy as np
import pytest

from responsible_agentic_workflows.benchmark import orchestration as harness
from responsible_agentic_workflows.benchmark.tasks import RuntimeTask
from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.logging import validate_run_record
from responsible_agentic_workflows.modeling import ModelResponse, TokenUsage
from responsible_agentic_workflows.workflow.b1_policy import B1FixedRecoveryPolicy
from responsible_agentic_workflows.workflow.g1_policy import G1ERGRPolicy


class FakeEmbedder:
    failure = False

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.dimensions = kwargs["dimensions"]

    def embed_query(self, query):
        if self.failure:
            raise RuntimeError("synthetic retrieval failure")
        return np.ones(self.dimensions, dtype=np.float32)


class FakeModel:
    failure = False

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.config_id = kwargs["config_id"]
        self.model_name = kwargs["model_name"]
        self.provider = "ollama"

    def generate(self, request):
        if self.failure:
            raise RuntimeError("synthetic model failure")
        return ModelResponse(
            text="Synthetic answer",
            usage=TokenUsage(input_tokens=10, output_tokens=3),
            finish_reason="stop", provider_response_id="synthetic-response",
        )


@pytest.fixture
def setup(tmp_path, monkeypatch):
    seen = {"embedder": [], "model": [], "loaders": []}
    chunk = DocumentChunk(
        document_id="DOC901", chunk_id="SYNTHETIC-C001",
        title="Synthetic title", section="Synthetic section",
        section_index=0, text="Synthetic evidence", source_file="synthetic.txt",
    )

    def load(**kwargs):
        seen["loaders"].append(kwargs)
        return (chunk,), np.ones((1, 2560), dtype=np.float32), {}

    def embedder(**kwargs):
        obj = FakeEmbedder(**kwargs)
        seen["embedder"].append(obj)
        return obj

    def model(**kwargs):
        obj = FakeModel(**kwargs)
        seen["model"].append(obj)
        return obj

    monkeypatch.setattr(harness, "load_embedding_artifacts", load)
    monkeypatch.setattr(harness, "load_legacy_uc2_artifacts", load)
    monkeypatch.setattr(harness, "OllamaEmbeddingClient", embedder)
    monkeypatch.setattr(harness, "OllamaChatModel", model)

    def paths(use_case_id="UC1", condition="B0", task_id="T901"):
        config_id = f"benchmark-config-primary-{use_case_id.lower()}-v0.2"
        retrieval_id = f"{use_case_id}-QWEN3-EMBED4B-EXACT-COSINE-v0.1"
        config_path = tmp_path / f"{config_id}.json"
        retrieval_path = tmp_path / f"{retrieval_id}.json"
        config_path.write_bytes((
            harness._ROOT / "benchmark/config/primary" / f"{config_id}.json"
        ).read_bytes())
        retrieval_path.write_bytes((
            harness._ROOT / "benchmark/config/retrieval" / f"{retrieval_id}.json"
        ).read_bytes())
        kwargs = dict(
            task=RuntimeTask(task_id=task_id, question="Synthetic question?"),
            use_case_id=use_case_id, condition=condition,
            run_id=f"synthetic-{task_id}-{condition}",
            experiment_id="synthetic-experiment",
            code_revision="d1ec9281539a0008400ad2b46916343eb1cfe263",
            output_path=tmp_path / f"{task_id}-{condition}.json",
            config_path=config_path, retrieval_config_path=retrieval_path,
            artifact_directory=tmp_path / "synthetic-artifacts",
        )
        if use_case_id == "UC2":
            kwargs["chunks_path"] = tmp_path / "synthetic-chunks.jsonl"
            kwargs["source_inventory_path"] = tmp_path / "synthetic-inventory.tsv"
        else:
            kwargs["chunk_directory"] = tmp_path / "synthetic-chunks"
        return kwargs

    return paths, seen


def test_b0_success_persistence_caller_fields_and_timeouts(setup):
    paths, seen = setup
    kwargs = paths()
    record = harness.execute_primary_runtime_task(**kwargs)
    assert record["status"] == "completed"
    for key in ("run_id", "experiment_id", "code_revision"):
        assert record[key] == kwargs[key]
    assert record["task_id"] == "T901"
    assert record["execution_mode"] == "benchmark"
    assert record["condition"] == "B0"
    assert record["configuration"]["prompt_version"] == "b0-engineering-v0.1"
    assert record["configuration"]["workflow_config_id"] == "b0-two-step-rag-v0.1"
    assert seen["embedder"][0].kwargs["timeout_seconds"] == 300.0
    assert seen["model"][0].kwargs["timeout"] == 300.0
    assert seen["model"][0].kwargs["context_length"] == 49152
    assert seen["model"][0].kwargs["seed"] == 20260912
    assert seen["model"][0].kwargs["thinking"] is False
    assert seen["loaders"][0]["chunk_directory"] == kwargs["chunk_directory"]
    assert json.loads(kwargs["output_path"].read_text()) == record
    validate_run_record(record)
    with pytest.raises(FileExistsError):
        harness.execute_primary_runtime_task(**kwargs)
    assert len(seen["model"]) == 1


@pytest.mark.parametrize("failure,stage", [
    ("retrieval", "retrieval"), ("model", "model"),
])
def test_b0_logged_tool_failures_are_tool_error(setup, failure, stage):
    paths, _ = setup
    kwargs = paths(task_id="T902" if failure == "retrieval" else "T903")
    if failure == "retrieval":
        FakeEmbedder.failure = True
    else:
        FakeModel.failure = True
    try:
        record = harness.execute_primary_runtime_task(**kwargs)
    finally:
        FakeEmbedder.failure = FakeModel.failure = False
    assert record["status"] == "tool_error"
    assert record["final_output"]["abstained"] is False
    assert record["final_output"]["answer"] is None
    assert len(record["errors"]) == 1
    assert record["errors"][0]["stage"] == stage
    assert json.loads(kwargs["output_path"].read_text()) == record
    validate_run_record(record)


def test_b0_unrelated_failure_is_logged_and_persisted(setup, monkeypatch):
    paths, _ = setup
    kwargs = paths(task_id="T904")

    def fail(*args, **kwargs):
        raise ValueError("synthetic unrelated failure")

    monkeypatch.setattr(harness.B0Baseline, "run", fail)
    record = harness.execute_primary_runtime_task(**kwargs)
    assert record["status"] == "failed"
    assert record["final_output"]["abstained"] is False
    assert len(record["errors"]) == 1
    assert record["errors"][0]["stage"] == "workflow"
    assert json.loads(kwargs["output_path"].read_text()) == record
    validate_run_record(record)


def test_b1_g1_policy_distinction_and_runner_records(setup, monkeypatch):
    paths, seen = setup
    calls = []

    class Runner:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def run(self, task, *, recorder, resource_limits):
            calls.append((self.kwargs, resource_limits, recorder.configuration))
            return SimpleNamespace(record=recorder.build_record(
                status="completed_after_recovery", answer="Synthetic runner answer",
                abstained=False,
            ))

    monkeypatch.setattr(harness, "AgenticRunner", Runner)
    for condition, task_id in (("B1", "T905"), ("G1", "T906")):
        kwargs = paths(condition=condition, task_id=task_id)
        record = harness.execute_primary_runtime_task(**kwargs)
        assert record["status"] == "completed_after_recovery"
        assert json.loads(kwargs["output_path"].read_text()) == record
        validate_run_record(record)
    b1_kwargs, b1_limits, b1_config = calls[0]
    g1_kwargs, g1_limits, g1_config = calls[1]
    assert isinstance(b1_kwargs["recovery_policy"], B1FixedRecoveryPolicy)
    assert isinstance(g1_kwargs["recovery_policy"], G1ERGRPolicy)
    assert b1_kwargs["recovery_policy"].policy_id == "b1-fixed-recovery-policy-v0.1"
    assert g1_kwargs["recovery_policy"].policy_id == "g1-ergr-policy-v0.1"
    assert b1_kwargs["top_k"] == g1_kwargs["top_k"] == 10
    assert b1_limits == g1_limits
    assert (b1_limits.max_llm_calls, b1_limits.max_retrieval_calls,
            b1_limits.max_retries, b1_limits.max_total_tokens,
            b1_limits.timeout_ms) == (5, 2, 1, None, None)
    assert b1_config.model_config_id == g1_config.model_config_id
    assert b1_config.retrieval_config_id == g1_config.retrieval_config_id
    assert b1_config.temperature == g1_config.temperature
    assert b1_config.max_output_tokens == g1_config.max_output_tokens
    assert seen["model"][0].kwargs == seen["model"][1].kwargs
    assert seen["embedder"][0].kwargs == seen["embedder"][1].kwargs


def test_rejects_non_frozen_modified_config_and_non_runtime_task(setup):
    paths, seen = setup
    kwargs = paths(task_id="T907")
    config = json.loads(kwargs["config_path"].read_text())
    config["status"] = "working"
    kwargs["config_path"].write_text(json.dumps(config))
    with pytest.raises(ValueError, match="frozen"):
        harness.execute_primary_runtime_task(**kwargs)
    config["status"] = "frozen"
    config["retrieval"]["top_k"] = 9
    kwargs["config_path"].write_text(json.dumps(config))
    with pytest.raises(ValueError, match="differs"):
        harness.execute_primary_runtime_task(**kwargs)
    kwargs["task"] = SimpleNamespace(task_id="T907", question="Synthetic question?")
    with pytest.raises(TypeError, match="RuntimeTask"):
        harness.execute_primary_runtime_task(**kwargs)
    assert seen["model"] == []


@pytest.mark.parametrize("use_case_id", ["UC2", "UC3"])
def test_artifact_loader_routing(setup, use_case_id):
    paths, seen = setup
    kwargs = paths(use_case_id=use_case_id, task_id="T907")
    record = harness.execute_primary_runtime_task(**kwargs)
    assert record["status"] == "completed"
    if use_case_id == "UC2":
        assert seen["loaders"][0]["chunks_path"] == kwargs["chunks_path"]
        assert (
            seen["loaders"][0]["source_inventory_path"]
            == kwargs["source_inventory_path"]
        )
    else:
        assert seen["loaders"][0]["chunk_directory"] == kwargs["chunk_directory"]
