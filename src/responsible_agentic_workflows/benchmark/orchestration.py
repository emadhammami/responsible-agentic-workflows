"""Frozen primary benchmark construction and RuntimeTask execution boundary."""

import json
from pathlib import Path
from typing import Literal

from responsible_agentic_workflows.benchmark.configuration import (
    load_benchmark_configuration,
    require_frozen_benchmark_configuration,
)
from responsible_agentic_workflows.benchmark.legacy_uc2 import load_legacy_uc2_artifacts
from responsible_agentic_workflows.benchmark.tasks import RuntimeTask
from responsible_agentic_workflows.logging import (
    RunConfiguration,
    RunRecorder,
    validate_run_record,
    write_validated_run_record,
)
from responsible_agentic_workflows.modeling.ollama import OllamaChatModel
from responsible_agentic_workflows.retrieval.dense import DenseExactRetriever
from responsible_agentic_workflows.retrieval.embedding import OllamaEmbeddingClient
from responsible_agentic_workflows.retrieval.materialize import load_embedding_artifacts
from responsible_agentic_workflows.workflow.agentic_runner import AgenticRunner
from responsible_agentic_workflows.workflow.b0_baseline import B0Baseline
from responsible_agentic_workflows.workflow.b1_policy import B1FixedRecoveryPolicy
from responsible_agentic_workflows.workflow.control import ResourceLimits
from responsible_agentic_workflows.workflow.g1_policy import G1ERGRPolicy

UseCase = Literal["UC1", "UC2", "UC3"]
Condition = Literal["B0", "B1", "G1"]
_ROOT = Path(__file__).resolve().parents[3]
_POLICY_IDS = {
    "B1": "b1-fixed-recovery-policy-v0.1",
    "G1": "g1-ergr-policy-v0.1",
}


def _frozen_config(use_case_id: UseCase, config_path: Path) -> dict[str, object]:
    if use_case_id not in {"UC1", "UC2", "UC3"}:
        raise ValueError(f"Unsupported primary use case: {use_case_id}")
    config = load_benchmark_configuration(config_path)
    require_frozen_benchmark_configuration(config)
    canonical_path = _ROOT / "benchmark/config/primary" / (
        f"benchmark-config-primary-{use_case_id.lower()}-v0.2.json"
    )
    if config != json.loads(canonical_path.read_text(encoding="utf-8")):
        raise ValueError("Primary configuration differs from frozen configuration")
    return config


def _frozen_retrieval_config(
    *, use_case_id: UseCase, retrieval_config_path: Path, config: dict[str, object]
) -> dict[str, object]:
    retrieval_config = json.loads(retrieval_config_path.read_text(encoding="utf-8"))
    config_id = config["retrieval"]["retrieval_config_id"]
    canonical_path = _ROOT / "benchmark/config/retrieval" / f"{config_id}.json"
    if (
        retrieval_config.get("status") != "frozen"
        or retrieval_config.get("retrieval_config_id") != config_id
        or retrieval_config.get("chunking_config_id")
        != config["retrieval"]["chunking_config_id"]
        or retrieval_config.get("embedding", {}).get("model_tag")
        != config["retrieval"]["embedding_model"]
        or retrieval_config != json.loads(canonical_path.read_text(encoding="utf-8"))
    ):
        raise ValueError(f"{use_case_id} retrieval configuration is not frozen")
    return retrieval_config


def execute_primary_runtime_task(
    *,
    task: RuntimeTask,
    use_case_id: UseCase,
    condition: Condition,
    run_id: str,
    experiment_id: str,
    code_revision: str,
    output_path: str | Path,
    config_path: str | Path,
    retrieval_config_path: str | Path,
    artifact_directory: str | Path,
    chunk_directory: str | Path | None = None,
    chunks_path: str | Path | None = None,
    source_inventory_path: str | Path | None = None,
) -> dict[str, object]:
    """Execute one caller-scheduled runtime task and persist its terminal record."""
    if type(task) is not RuntimeTask:
        raise TypeError("Primary execution accepts RuntimeTask only")
    if condition not in {"B0", "B1", "G1"}:
        raise ValueError(f"Unsupported primary condition: {condition}")
    output = Path(output_path)
    if output.exists():
        raise FileExistsError(f"Run artifact already exists: {output}")

    config = _frozen_config(use_case_id, Path(config_path))
    retrieval_config = _frozen_retrieval_config(
        use_case_id=use_case_id,
        retrieval_config_path=Path(retrieval_config_path),
        config=config,
    )
    if use_case_id == "UC2":
        if chunks_path is None or source_inventory_path is None:
            raise ValueError("UC2 requires chunks_path and source_inventory_path")
        chunks, embeddings, _ = load_legacy_uc2_artifacts(
            chunks_path=Path(chunks_path),
            artifact_directory=Path(artifact_directory),
            retrieval_config_path=Path(retrieval_config_path),
            source_inventory_path=Path(source_inventory_path),
        )
    else:
        if chunk_directory is None:
            raise ValueError(f"{use_case_id} requires chunk_directory")
        chunks, embeddings, _ = load_embedding_artifacts(
            chunk_directory=Path(chunk_directory),
            artifact_directory=Path(artifact_directory),
            retrieval_config_path=Path(retrieval_config_path),
        )

    embedding = retrieval_config["embedding"]
    query_embedder = OllamaEmbeddingClient(
        model=embedding["model_tag"],
        dimensions=embedding["output_dimensions"],
        query_instruction=embedding["query_instruction"],
        truncate=embedding["truncate"],
        timeout_seconds=300.0,
    )
    retriever = DenseExactRetriever(
        chunks=chunks,
        embeddings=embeddings,
        query_embedder=query_embedder,
        config_id=config["retrieval"]["retrieval_config_id"],
    )
    model_config = config["model"]
    model = OllamaChatModel(
        model_name=model_config["model_name"],
        config_id=model_config["model_config_id"],
        context_length=49152,
        seed=config["execution"]["random_seed"],
        thinking=False,
        timeout=300.0,
    )
    prompt_key = f"{condition.lower()}_prompt_version"
    workflow_key = f"{condition.lower()}_config_id"
    recorder = RunRecorder(
        run_id=run_id,
        experiment_id=experiment_id,
        task_id=task.task_id,
        execution_mode="benchmark",
        condition=condition,
        code_revision=code_revision,
        configuration=RunConfiguration(
            model_provider=model_config["provider"],
            model_name=model_config["model_name"],
            model_config_id=model_config["model_config_id"],
            model_version=model_config["model_version"],
            temperature=model_config["temperature"],
            max_output_tokens=model_config["max_output_tokens"],
            prompt_version=config["prompts"][prompt_key],
            retrieval_config_id=config["retrieval"]["retrieval_config_id"],
            workflow_config_id=config["workflows"][workflow_key],
            random_seed=config["execution"]["random_seed"],
        ),
    )
    top_k = config["retrieval"]["top_k"]
    if condition == "B0":
        initial_errors = len(recorder.build_record(
            status="failed", answer=None, abstained=False
        )["errors"])
        try:
            baseline = B0Baseline(retriever=retriever, model=model, top_k=top_k)
            record = baseline.run(task, recorder=recorder).record
        except Exception as exc:
            errors = recorder.build_record(
                status="failed", answer=None, abstained=False
            )["errors"]
            new_errors = errors[initial_errors:]
            error_type = type(exc).__name__
            message = str(exc) or repr(exc)
            if not any(
                error["error_type"] == error_type and error["message"] == message
                for error in new_errors
            ):
                recorder.record_error(
                    error_type=error_type,
                    message=message,
                    stage="workflow",
                    retryable=None,
                )
            status = (
                "tool_error"
                if any(error["stage"] in {"retrieval", "model"} for error in new_errors)
                else "failed"
            )
            record = recorder.build_record(
                status=status, answer=None, abstained=False
            )
    else:
        limits = config["resource_limits"]
        resource_limits = ResourceLimits(
            max_llm_calls=limits["max_llm_calls_per_run"],
            max_retrieval_calls=limits["max_retrieval_calls_per_run"],
            max_retries=limits["max_retries_per_run"],
            max_total_tokens=limits["max_total_tokens_per_run"],
            timeout_ms=limits["timeout_ms"],
        )
        policy = (
            B1FixedRecoveryPolicy(policy_id=_POLICY_IDS["B1"])
            if condition == "B1"
            else G1ERGRPolicy(policy_id=_POLICY_IDS["G1"])
        )
        record = AgenticRunner(
            model=model,
            retriever=retriever,
            recovery_policy=policy,
            top_k=top_k,
        ).run(task, recorder=recorder, resource_limits=resource_limits).record

    validate_run_record(record)
    write_validated_run_record(record, output)
    return record
