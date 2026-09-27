"""Synthetic, in-memory coverage of the shared B1/G1 runner."""

import json

import pytest

import responsible_agentic_workflows.workflow.agentic_nodes as agentic_nodes
from responsible_agentic_workflows.benchmark.tasks import RuntimeTask
from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.logging import (
    RunConfiguration,
    RunRecorder,
    validate_run_record,
)
from responsible_agentic_workflows.modeling import ModelResponse, TokenUsage
from responsible_agentic_workflows.retrieval import RetrievedChunk
from responsible_agentic_workflows.workflow.agentic_execution import (
    AGENTIC_PROMPT_VERSION,
)
from responsible_agentic_workflows.workflow.agentic_runner import AgenticRunner
from responsible_agentic_workflows.workflow.b1_policy import B1FixedRecoveryPolicy
from responsible_agentic_workflows.workflow.control import (
    BlockedLimit,
    ResourceLimits,
)
from responsible_agentic_workflows.workflow.g1_policy import G1ERGRPolicy

TASK = RuntimeTask("T901", "What does DOC901 require?")
TERMINAL_EVENTS = {
    "answer_accepted",
    "abstained",
    "resource_stopped",
    "workflow_failed",
}


def _critic(*, supported: bool, sufficient: bool = True, conflict: bool = False):
    return json.dumps(
        {
            "schema_version": "0.1",
            "support_status": "SUPPORTED" if supported else "PARTIAL_SUPPORT",
            "evidence_sufficiency": (
                "SUFFICIENT" if sufficient else "INSUFFICIENT"
            ),
            "unresolved_conflict": conflict,
            "gap_types": ["EVIDENCE_CONFLICT"] if conflict else [],
            "unsupported_claims": [],
            "incomplete_support": [],
            "evidence_gaps": [],
            "explanation": None,
        }
    )


class Model:
    config_id = "synthetic-model-v1"
    provider = "synthetic"
    model_name = "synthetic-model"

    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.requests = []

    def generate(self, request):
        self.requests.append(request)
        value = self.outputs.pop(0)
        if isinstance(value, Exception):
            raise value
        return ModelResponse(
            text=value,
            usage=TokenUsage(input_tokens=10, output_tokens=2),
            finish_reason="stop",
            provider_response_id=f"synthetic-{len(self.requests)}",
        )


class Retriever:
    config_id = "synthetic-retrieval-v1"

    def __init__(self):
        self.calls = []

    def retrieve(self, query, *, top_k):
        self.calls.append((query, top_k))
        return (
            RetrievedChunk(
                chunk=DocumentChunk(
                    document_id="DOC901",
                    chunk_id="DOC901-C1",
                    title="Synthetic policy",
                    section="Requirement",
                    section_index=0,
                    text="DOC901 requires approval.",
                    source_file="synthetic.txt",
                    page=1,
                ),
                rank=1,
                score=1.0,
            ),
        )


def _recorder(*, task_id="T901"):
    return RunRecorder(
        run_id="synthetic-agentic-run",
        experiment_id="synthetic-engineering",
        task_id=task_id,
        execution_mode="engineering",
        condition=None,
        code_revision="8b502d96",
        configuration=RunConfiguration(
            model_provider="synthetic",
            model_name="synthetic-model",
            model_config_id="synthetic-model-v1",
            temperature=0.0,
            prompt_version=AGENTIC_PROMPT_VERSION,
            retrieval_config_id="synthetic-retrieval-v1",
            max_output_tokens=128,
        ),
    )


def _limits(**overrides):
    values = dict(
        max_llm_calls=8,
        max_retrieval_calls=3,
        max_retries=1,
        max_total_tokens=1000,
        timeout_ms=None,
    )
    values.update(overrides)
    return ResourceLimits(**values)


def _run(outputs, *, policy=None, limits=None, recorder=None):
    model = Model(outputs)
    retriever = Retriever()
    recorder = recorder or _recorder()
    runner = AgenticRunner(
        model=model,
        retriever=retriever,
        recovery_policy=policy or B1FixedRecoveryPolicy("b1-synthetic"),
        top_k=2,
    )
    result = runner.run(
        TASK,
        recorder=recorder,
        resource_limits=limits or _limits(),
    )
    validate_run_record(result.record)
    events = [event["event_type"] for event in result.record["events"]]
    assert len([event for event in events if event in TERMINAL_EVENTS]) == 1
    assert result.record["usage"]["tool_calls"] == 0
    assert result.record["final_output"]["cited_chunk_ids"] == []
    assert result.record["usage"]["retries"] == result.final_state[
        "recovery_iteration"
    ]
    return result, model, retriever, recorder


def test_accept_success_records_valid_terminal_and_defensive_snapshots():
    result, model, retriever, recorder = _run(
        ["Plan", "DOC901 requires approval.", _critic(supported=True)]
    )
    assert result.terminal_status == "completed"
    assert result.final_answer == "DOC901 requires approval."
    assert result.abstained is False
    assert result.final_state["final_answer"] == result.final_answer
    assert result.record["events"][-1]["event_type"] == "answer_accepted"
    assert result.record["usage"]["retries"] == 0
    assert len(model.requests) == 3
    assert retriever.calls == [(TASK.question, 2)]
    result.final_state["plan"] = "changed"
    result.record["events"].clear()
    assert recorder.build_record(
        status="completed", answer=result.final_answer, abstained=False
    )["events"][-1]["event_type"] == "answer_accepted"


def test_revise_only_success_counts_one_retry():
    result, model, retriever, _ = _run(
        [
            "Plan",
            "Initial answer",
            _critic(supported=False),
            "Revised answer",
            _critic(supported=True),
        ]
    )
    assert result.terminal_status == "completed_after_recovery"
    assert result.final_answer == "Revised answer"
    assert result.record["usage"]["retries"] == 1
    assert result.record["events"][-1]["event_type"] == "answer_accepted"
    assert len(model.requests) == 5
    assert len(retriever.calls) == 1


def test_policy_resource_stop_preserves_decision():
    result, _, _, _ = _run(
        ["Plan", "Initial answer", _critic(supported=False)],
        limits=_limits(max_retries=0),
    )
    assert result.terminal_status == "resource_stopped"
    assert result.final_answer is None
    assert result.abstained is False
    assert result.final_state["latest_RecoveryDecision"].action == "RESOURCE_STOP"
    assert result.record["events"][-1]["event_type"] == "resource_stopped"


def test_execution_guard_stop_before_provider_call_retains_ordered_limits():
    recorder = _recorder()
    recorder.record_model_call(
        status="completed",
        latency_ms=0.0,
        usage=TokenUsage(input_tokens=10, output_tokens=2),
        finish_reason="stop",
        provider_response_id="earlier",
    )
    result, model, _, _ = _run(
        [],
        recorder=recorder,
        limits=_limits(max_llm_calls=1, max_total_tokens=12),
    )
    assert model.requests == []
    assert result.terminal_status == "resource_stopped"
    assert result.final_state["latest_RecoveryDecision"] is None
    assert result.final_state["final_answer"] is None
    assert result.final_state["abstained_flag"] is False
    event = result.record["events"][-1]
    assert event["event_type"] == "resource_stopped"
    assert event["stage"] == "plan"
    assert event["details"]["blocked_stage"] == "plan"
    assert event["details"]["blocked_limits"] == [
        "LLM_CALL_LIMIT",
        "TOKEN_LIMIT",
    ]
    assert "workflow_failed" not in [
        item["event_type"] for item in result.record["events"]
    ]


def test_later_guard_preserves_latest_successful_state():
    result, model, retriever, _ = _run(
        ["Plan"], limits=_limits(max_llm_calls=1)
    )
    assert len(model.requests) == 1
    assert len(retriever.calls) == 1
    assert result.terminal_status == "resource_stopped"
    assert result.final_state["plan"] == "Plan"
    assert len(result.final_state["initial_retrieval"]) == 1
    assert result.record["events"][-1]["stage"] == "draft"


def test_provider_failure_is_tool_error_and_retains_logged_error():
    result, model, _, _ = _run([RuntimeError("synthetic provider failure")])
    assert len(model.requests) == 1
    assert result.terminal_status == "tool_error"
    assert result.abstained is False
    assert result.final_answer is None
    assert result.record["events"][-1]["event_type"] == "workflow_failed"
    assert result.record["errors"] == [
        {
            "error_type": "RuntimeError",
            "stage": "model",
            "message": "synthetic provider failure",
            "retryable": None,
        }
    ]


def test_critic_parser_failure_is_failed_and_never_abstained():
    result, _, _, _ = _run(["Plan", "Answer", "not JSON"])
    assert result.terminal_status == "failed"
    assert result.abstained is False
    assert result.final_state["abstained_flag"] is False
    assert result.record["events"][-1]["event_type"] == "workflow_failed"
    assert result.record["errors"][0]["stage"] == "initial_critic"


def test_prior_tool_error_does_not_classify_new_parser_failure():
    recorder = _recorder()
    recorder.record_error(
        error_type="EarlierError",
        message="unrelated prior execution",
        stage="model",
        retryable=None,
    )
    result, _, _, _ = _run(["Plan", "Answer", "not JSON"], recorder=recorder)
    assert result.terminal_status == "failed"
    assert [error["stage"] for error in result.record["errors"]] == [
        "model",
        "initial_critic",
    ]


def test_g1_abstention_uses_injected_policy():
    result, _, _, _ = _run(
        ["Plan", "Answer", _critic(supported=False, conflict=True)],
        policy=G1ERGRPolicy("g1-synthetic"),
    )
    assert result.terminal_status == "completed"
    assert result.final_answer is None
    assert result.abstained is True
    assert result.record["events"][-1]["event_type"] == "abstained"


def test_task_id_mismatch_is_rejected_before_execution():
    runner = AgenticRunner(
        model=Model([]),
        retriever=Retriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-synthetic"),
        top_k=2,
    )
    with pytest.raises(ValueError, match="task_id"):
        runner.run(TASK, recorder=_recorder(task_id="T902"), resource_limits=_limits())



def test_retrieval_backend_failure_is_tool_error():
    class FailingRetriever:
        config_id = "synthetic-retrieval-v1"

        def retrieve(self, query, *, top_k):
            raise RuntimeError("synthetic retrieval failure")

    recorder = _recorder()
    model = Model(["Plan"])
    runner = AgenticRunner(
        model=model,
        retriever=FailingRetriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-synthetic"),
        top_k=2,
    )
    result = runner.run(TASK, recorder=recorder, resource_limits=_limits())

    assert result.terminal_status == "tool_error"
    assert result.abstained is False
    assert result.record["errors"][-1]["stage"] == "retrieval"
    assert result.record["events"][-1]["event_type"] == "workflow_failed"
    assert result.record["usage"]["retrieval_calls"] == 1


def test_begin_recovery_execution_stop_is_not_policy_resource_stop(monkeypatch):
    monkeypatch.setattr(
        agentic_nodes,
        "begin_recovery_blockers",
        lambda **kwargs: (BlockedLimit.TIMEOUT_LIMIT,),
    )
    result, _, _, _ = _run(
        ["Plan", "Initial answer", _critic(supported=False)]
    )

    events = [e["event_type"] for e in result.record["events"]]
    assert result.terminal_status == "resource_stopped"
    assert result.final_state["latest_RecoveryDecision"] is None
    assert result.record["usage"]["retries"] == 0
    assert events[-2:] == ["policy_decision", "resource_stopped"]
    assert "workflow_failed" not in events
    assert result.record["events"][-1]["stage"] == "begin_recovery"
    assert result.record["events"][-1]["details"]["blocked_limits"] == [
        "TIMEOUT_LIMIT"
    ]


def test_post_recovery_failure_to_release_abstains_once():
    result, _, _, _ = _run(
        [
            "Plan",
            "Initial answer",
            _critic(supported=False),
            "Revised answer",
            _critic(supported=False),
        ]
    )
    events = [e["event_type"] for e in result.record["events"]]
    assert result.terminal_status == "completed_after_recovery"
    assert result.final_answer is None
    assert result.abstained is True
    assert events[-1] == "abstained"
    assert events.count("abstained") == 1
