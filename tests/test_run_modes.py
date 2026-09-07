import pytest

from responsible_agentic_workflows.logging import (
    RunConfiguration,
    RunRecorder,
    validate_run_record,
)


def _configuration() -> RunConfiguration:
    return RunConfiguration(
        model_provider="engineering-test",
        model_name="no-model",
        model_config_id="engineering-no-model-v0.1",
        temperature=None,
        prompt_version="test-v0.1",
        retrieval_config_id="test-retriever-v0.1",
    )


def test_engineering_run_has_no_benchmark_condition() -> None:
    recorder = RunRecorder(
        run_id="engineering-run-001",
        experiment_id="engineering-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=_configuration(),
    )

    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )

    assert record["execution_mode"] == "engineering"
    assert record["condition"] is None

    validate_run_record(record)


def test_benchmark_run_requires_named_condition() -> None:
    recorder = RunRecorder(
        run_id="benchmark-run-001",
        experiment_id="benchmark-test",
        task_id="T901",
        execution_mode="benchmark",
        condition="B1",
        code_revision="abcdef1",
        configuration=_configuration(),
    )

    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )

    assert record["execution_mode"] == "benchmark"
    assert record["condition"] == "B1"

    validate_run_record(record)


def test_engineering_run_rejects_benchmark_condition() -> None:
    with pytest.raises(
        ValueError,
        match="Engineering runs require condition=None",
    ):
        RunRecorder(
            run_id="engineering-run-invalid",
            experiment_id="engineering-test",
            task_id="T901",
            execution_mode="engineering",
            condition="B1",
            code_revision="abcdef1",
            configuration=_configuration(),
        )


def test_benchmark_run_rejects_missing_condition() -> None:
    with pytest.raises(
        ValueError,
        match="Benchmark runs require condition",
    ):
        RunRecorder(
            run_id="benchmark-run-invalid",
            experiment_id="benchmark-test",
            task_id="T901",
            execution_mode="benchmark",
            condition=None,
            code_revision="abcdef1",
            configuration=_configuration(),
        )
