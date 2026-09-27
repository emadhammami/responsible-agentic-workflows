import json

import pytest

from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.logging import RunConfiguration, RunRecorder
from responsible_agentic_workflows.modeling import (
    ModelResponse,
    TokenUsage,
)
from responsible_agentic_workflows.retrieval import RetrievedChunk
from responsible_agentic_workflows.workflow.agentic_execution import (
    AGENTIC_PROMPT_VERSION,
)
from responsible_agentic_workflows.workflow.agentic_nodes import (
    AgenticNodeAssembler,
    ExecutionResourceStop,
)
from responsible_agentic_workflows.workflow.b1_policy import (
    B1FixedRecoveryPolicy,
)
from responsible_agentic_workflows.workflow.control import (
    BlockedLimit,
    CriticControlState,
    ResourceLimits,
)
from responsible_agentic_workflows.workflow.critic import parse_critic_result
from responsible_agentic_workflows.workflow.g1_policy import G1ERGRPolicy
from responsible_agentic_workflows.workflow.graph import build_graph
from responsible_agentic_workflows.workflow.state import initial_workflow_state


def _chunk(cid="C1", rank=1):
    return RetrievedChunk(
        chunk=DocumentChunk(
            document_id="D1",
            chunk_id=cid,
            title="Synthetic",
            section="S",
            section_index=0,
            text=f"evidence-{cid}",
            source_file="synthetic.txt",
            page=rank,
        ),
        rank=rank,
        score=1.0 / rank,
    )


class FakeRetriever:
    config_id = "synthetic-retrieval-v0.1"

    def __init__(self):
        self.calls = []

    def retrieve(self, query, *, top_k):
        self.calls.append((query, top_k))
        return (_chunk(),)


class FakeModel:
    config_id = "synthetic-model-v0.1"
    provider = "engineering-test"
    model_name = "synthetic-model"

    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.requests = []

    def generate(self, request):
        self.requests.append(request)
        if not self.outputs:
            raise AssertionError("unexpected model call")
        return ModelResponse(
            text=self.outputs.pop(0),
            usage=TokenUsage(input_tokens=10, output_tokens=2),
            finish_reason="stop",
            provider_response_id=f"r{len(self.requests)}",
        )


def _critic_json(*, supported, sufficient, gaps=(), conflict=False):
    return json.dumps(
        {
            "schema_version": "0.1",
            "support_status": (
                "SUPPORTED" if supported else "PARTIAL_SUPPORT"
            ),
            "evidence_sufficiency": (
                "SUFFICIENT" if sufficient else "INSUFFICIENT"
            ),
            "unresolved_conflict": conflict,
            "gap_types": list(gaps),
            "unsupported_claims": [],
            "incomplete_support": [],
            "evidence_gaps": (
                ["Need additional evidence"] if gaps else []
            ),
            "explanation": None,
        }
    )


def _recorder():
    return RunRecorder(
        run_id="agentic-node-run",
        experiment_id="engineering-agentic",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="0f61123",
        configuration=RunConfiguration(
            model_provider="engineering-test",
            model_name="synthetic-model",
            model_config_id="synthetic-model-v0.1",
            model_version=None,
            temperature=0.0,
            max_output_tokens=128,
            prompt_version=AGENTIC_PROMPT_VERSION,
            retrieval_config_id="synthetic-retrieval-v0.1",
            workflow_config_id="agentic-engineering-v0.1",
            random_seed=20260927,
        ),
    )


def _limits(**overrides):
    values = {
        "max_llm_calls": 8,
        "max_retrieval_calls": 3,
        "max_retries": 1,
        "max_total_tokens": 10_000,
        "timeout_ms": None,
    }
    values.update(overrides)
    return ResourceLimits(**values)


def _state(limits=None):
    return initial_workflow_state(
        task_id="T901",
        question="What does the synthetic policy require?",
        execution_mode="engineering",
        condition_metadata=None,
        ResourceLimits=limits or _limits(),
    )


def _event_types(recorder):
    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )
    return [e["event_type"] for e in record["events"]]


def test_accept_path_real_nodes():
    recorder = _recorder()
    model = FakeModel(
        [
            "Find the relevant requirement.",
            "The synthetic policy requires approval.",
            _critic_json(supported=True, sufficient=True),
        ]
    )
    retriever = FakeRetriever()

    assembler = AgenticNodeAssembler(
        model=model,
        retriever=retriever,
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )
    out = build_graph(assembler.components()).invoke(_state())

    assert out["terminal_status"] == "completed"
    assert out["final_answer"] == "The synthetic policy requires approval."
    assert len(model.requests) == 3
    assert retriever.calls == [
        ("What does the synthetic policy require?", 1)
    ]
    assert _event_types(recorder) == [
        "plan_completed",
        "initial_retrieval_completed",
        "draft_completed",
        "initial_critic_completed",
        "policy_decision",
    ]


def test_revise_only_real_nodes_emit_recovery_started_once():
    recorder = _recorder()
    model = FakeModel(
        [
            "Inspect evidence and answer.",
            "Initial answer.",
            _critic_json(supported=False, sufficient=True),
            "Revised grounded answer.",
            _critic_json(supported=True, sufficient=True),
        ]
    )
    retriever = FakeRetriever()

    assembler = AgenticNodeAssembler(
        model=model,
        retriever=retriever,
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )
    out = build_graph(assembler.components()).invoke(_state())

    assert out["terminal_status"] == "completed_after_recovery"
    assert out["final_answer"] == "Revised grounded answer."
    events = _event_types(recorder)
    assert events.count("recovery_started") == 1
    assert events == [
        "plan_completed",
        "initial_retrieval_completed",
        "draft_completed",
        "initial_critic_completed",
        "policy_decision",
        "recovery_started",
        "revision_completed",
        "post_recovery_critic_completed",
    ]


def test_model_guard_blocks_before_provider_call():
    recorder = _recorder()
    recorder.record_model_call(
        status="completed",
        latency_ms=1.0,
        usage=TokenUsage(input_tokens=1, output_tokens=1),
        finish_reason="stop",
        provider_response_id="pre",
    )
    model = FakeModel(["must-not-run"])
    assembler = AgenticNodeAssembler(
        model=model,
        retriever=FakeRetriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )

    with pytest.raises(ExecutionResourceStop) as exc:
        assembler.plan(_state(_limits(max_llm_calls=1)))

    assert exc.value.stage == "plan"
    assert model.requests == []


def test_retrieval_guard_blocks_before_tool_call():
    recorder = _recorder()
    recorder.record_retrieval(
        query="prior",
        top_k=1,
        latency_ms=1.0,
        results=(_chunk(),),
    )
    retriever = FakeRetriever()
    assembler = AgenticNodeAssembler(
        model=FakeModel([]),
        retriever=retriever,
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )

    with pytest.raises(ExecutionResourceStop) as exc:
        assembler.initial_retrieve(
            _state(_limits(max_retrieval_calls=1))
        )

    assert exc.value.stage == "initial_retrieve"
    assert retriever.calls == []


def test_begin_recovery_timeout_is_execution_only(monkeypatch):
    recorder = _recorder()
    monkeypatch.setattr(
        type(recorder),
        "elapsed_ms",
        property(lambda self: 1.0),
    )
    assembler = AgenticNodeAssembler(
        model=FakeModel([]),
        retriever=FakeRetriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )
    state = _state(_limits(timeout_ms=1.0))
    result_json = _critic_json(supported=False, sufficient=True)

    result = parse_critic_result(result_json)
    state["latest_CriticResult"] = result
    state["latest_CriticControlState"] = (
        CriticControlState.from_critic_result(result)
    )
    state["critic_iteration"] = 1

    with pytest.raises(ExecutionResourceStop) as exc:
        assembler.recovery_policy(state)

    assert exc.value.stage == "begin_recovery"
    assert exc.value.blocked_limits == (BlockedLimit.TIMEOUT_LIMIT,)
    assert _event_types(recorder) == ["policy_decision"]


def test_components_expose_exact_frozen_eight_nodes():
    assembler = AgenticNodeAssembler(
        model=FakeModel([]),
        retriever=FakeRetriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=_recorder(),
        top_k=1,
    )
    assert set(assembler.components().__dataclass_fields__) == {
        "plan",
        "initial_retrieve",
        "draft",
        "initial_critic",
        "recovery_policy",
        "recovery_retrieve",
        "revision",
        "post_recovery_critic",
    }



def test_reretrieve_path_query_merge_and_event_order():
    class SequencedRetriever(FakeRetriever):
        def retrieve(self, query, *, top_k):
            self.calls.append((query, top_k))
            if len(self.calls) == 1:
                return (_chunk("C1", 1),)
            return (_chunk("C2", 1),)

    recorder = _recorder()
    retriever = SequencedRetriever()
    model = FakeModel(
        [
            "Inspect the relevant evidence.",
            "Initial answer.",
            _critic_json(
                supported=False,
                sufficient=False,
                gaps=("MISSING_EVIDENCE",),
            ),
            "Revised answer using both passages.",
            _critic_json(supported=True, sufficient=True),
        ]
    )

    assembler = AgenticNodeAssembler(
        model=model,
        retriever=retriever,
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )
    out = build_graph(assembler.components()).invoke(_state())

    question = "What does the synthetic policy require?"
    assert retriever.calls == [
        (question, 1),
        (
            question
            + "\n\nEvidence gaps:\n- Need additional evidence",
            1,
        ),
    ]
    assert [
        item.chunk.chunk_id for item in out["merged_evidence"]
    ] == ["C1", "C2"]
    assert out["recovery_iteration"] == 1
    assert out["final_answer"] == "Revised answer using both passages."

    events = _event_types(recorder)
    assert events == [
        "plan_completed",
        "initial_retrieval_completed",
        "draft_completed",
        "initial_critic_completed",
        "policy_decision",
        "recovery_started",
        "recovery_retrieval_completed",
        "revision_completed",
        "post_recovery_critic_completed",
    ]
    assert events.count("recovery_started") == 1

    revision_prompt = model.requests[3].messages[-1].content
    assert revision_prompt.index("chunk_id=C1") < revision_prompt.index(
        "chunk_id=C2"
    )


def test_policy_resource_stop_preserves_path_logging_without_recovery():
    recorder = _recorder()
    model = FakeModel(
        [
            "Inspect evidence.",
            "Initial answer.",
            _critic_json(supported=False, sufficient=True),
        ]
    )

    assembler = AgenticNodeAssembler(
        model=model,
        retriever=FakeRetriever(),
        recovery_policy=B1FixedRecoveryPolicy("b1-test"),
        recorder=recorder,
        top_k=1,
    )
    out = build_graph(assembler.components()).invoke(
        _state(_limits(max_retries=0))
    )

    assert out["terminal_status"] == "resource_stopped"
    assert out["final_answer"] is None
    assert out["abstained_flag"] is False
    assert out["recovery_iteration"] == 0
    assert out["latest_RecoveryDecision"].reason_code.value == (
        "HARD_LIMIT_BLOCKED"
    )

    record = recorder.build_record(
        status="resource_stopped",
        answer=None,
        abstained=False,
    )
    assert _event_types(recorder) == [
        "plan_completed",
        "initial_retrieval_completed",
        "draft_completed",
        "initial_critic_completed",
        "policy_decision",
    ]
    details = record["events"][-1]["details"]
    assert details["selected_recovery_path"] == "REVISE_ONLY"
    assert details["hard_recovery_feasible"] is False
    assert details["blocked_limits"] == ["RETRY_LIMIT"]
    assert details["path_reserve_satisfied"] is None


def test_g1_conflict_abstains_without_opening_recovery():
    recorder = _recorder()
    model = FakeModel(
        [
            "Inspect evidence.",
            "Initial answer.",
            _critic_json(
                supported=False,
                sufficient=True,
                gaps=("EVIDENCE_CONFLICT",),
                conflict=True,
            ),
        ]
    )

    assembler = AgenticNodeAssembler(
        model=model,
        retriever=FakeRetriever(),
        recovery_policy=G1ERGRPolicy("g1-test"),
        recorder=recorder,
        top_k=1,
    )
    out = build_graph(assembler.components()).invoke(_state())

    assert out["terminal_status"] == "completed"
    assert out["final_answer"] is None
    assert out["abstained_flag"] is True
    assert out["recovery_iteration"] == 0
    assert out["latest_RecoveryDecision"].reason_code.value == (
        "G1_RECOVERY_NOT_WORTHWHILE"
    )
    assert "recovery_started" not in _event_types(recorder)
