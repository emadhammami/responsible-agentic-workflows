"""End-to-end retrieval smoke test for the research software pipeline."""

from datetime import UTC, datetime
from pathlib import Path
from subprocess import CalledProcessError, run

from responsible_agentic_workflows.benchmark import load_runtime_task
from responsible_agentic_workflows.ingestion import ingest_markdown_directory
from responsible_agentic_workflows.logging import (
    LoggedRetriever,
    RunConfiguration,
    RunRecorder,
    write_validated_run_record,
)
from responsible_agentic_workflows.retrieval import LexicalRetriever

SYNTHETIC_DOCUMENTS = Path("benchmark/synthetic/documents")
SYNTHETIC_TASK = Path("benchmark/synthetic/tasks/T901.json")
ENGINEERING_ARTIFACTS = Path("artifacts/engineering")


def _git_revision() -> str:
    try:
        result = run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (CalledProcessError, FileNotFoundError) as exc:
        raise RuntimeError("Unable to determine Git revision") from exc

    revision = result.stdout.strip()

    if len(revision) < 7:
        raise RuntimeError("Invalid Git revision")

    return revision


def _new_run_id() -> str:
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    return f"engineering-smoke-{timestamp}"


def run_retrieval_smoke(
    *,
    output_path: str | Path,
    run_id: str,
    code_revision: str,
) -> Path:
    """Execute one retrieval-only engineering run.

    This run validates the execution pipeline and is not a thesis benchmark
    result. Engineering runs are explicitly separated from B0, B1, and G1.
    """

    runtime_task = load_runtime_task(SYNTHETIC_TASK)

    documents = ingest_markdown_directory(
        SYNTHETIC_DOCUMENTS
    )

    retriever = LexicalRetriever(
        chunk
        for document in documents
        for chunk in document.chunks
    )

    configuration = RunConfiguration(
        model_provider="engineering-test",
        model_name="no-model",
        model_config_id="engineering-no-model-v0.1",
        model_version=None,
        temperature=None,
        max_output_tokens=None,
        prompt_version="engineering-smoke-v0.1",
        retrieval_config_id=retriever.config_id,
        workflow_config_id="retrieval-smoke-v0.1",
        random_seed=None,
    )

    recorder = RunRecorder(
        run_id=run_id,
        experiment_id="engineering-smoke",
        task_id=runtime_task.task_id,
        execution_mode="engineering",
        condition=None,
        code_revision=code_revision,
        configuration=configuration,
    )

    logged_retriever = LoggedRetriever(
        retriever,
        recorder,
    )

    logged_retriever.retrieve(
        runtime_task.question,
        top_k=3,
    )

    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )

    return write_validated_run_record(
        record,
        output_path,
    )


def main() -> None:
    """Create one local engineering artifact."""

    run_id = _new_run_id()
    output_path = ENGINEERING_ARTIFACTS / f"{run_id}.json"

    written = run_retrieval_smoke(
        output_path=output_path,
        run_id=run_id,
        code_revision=_git_revision(),
    )

    print(f"ENGINEERING_RUN_ID={run_id}")
    print(f"ENGINEERING_RUN_PATH={written.as_posix()}")
    print("ENGINEERING_RUN=PASS")


if __name__ == "__main__":
    main()
