"""Synthetic-only tests for the shared B1/G1 execution-runtime helpers."""

import inspect
import math

import pytest

from responsible_agentic_workflows.ingestion.models import DocumentChunk
from responsible_agentic_workflows.logging.run_record import (
    RunConfiguration,
    RunRecorder,
)
from responsible_agentic_workflows.modeling.contracts import TokenUsage
from responsible_agentic_workflows.retrieval.models import RetrievedChunk
from responsible_agentic_workflows.workflow import (
    BLOCKED_LIMIT_ORDER,
    MAX_RECOVERY_CYCLES,
    WORKFLOW_EVENT_TYPES,
    BlockedLimit,
    CriticControlState,
    CriticResult,
    EvidenceSufficiency,
    GapType,
    HardRecoveryFeasibility,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryReasonCode,
    ResourceLimits,
    ResourceSnapshot,
    SupportStatus,
    begin_recovery_blockers,
    build_hard_recovery_feasibility,
    build_policy_decision_event,
    build_recovery_policy_context,
    build_resource_snapshot,
    model_call_blockers,
    record_policy_decision,
    record_workflow_event,
    retrieval_call_blockers,
)

EXPECTED_27_KEY_ORDER: tuple[str, ...] = (
    "policy_id",
    "decision_sequence",
    "critic_iteration",
    "support_status",
    "evidence_sufficiency",
    "unresolved_conflict",
    "gap_types",
    "release_ok",
    "recovery_iteration",
    "selected_action",
    "reason_code",
    "llm_calls_used",
    "retrieval_calls_used",
    "retries_used",
    "input_tokens_used",
    "output_tokens_used",
    "total_tokens_used",
    "llm_calls_remaining",
    "retrieval_calls_remaining",
    "retries_remaining",
    "total_tokens_remaining",
    "selected_recovery_path",
    "hard_recovery_feasible",
    "blocked_limits",
    "path_reserve_satisfied",
    "recovery_rule_version",
    "resource_reserve_rule_version",
)


# ---------------------------------------------------------------------------
# fixtures / helpers
# ---------------------------------------------------------------------------


def _chunk(chunk_id: str = "chunk-1") -> DocumentChunk:
    return DocumentChunk(
        document_id="doc-1",
        chunk_id=chunk_id,
        title="Synthetic Source",
        section="§1",
        section_index=0,
        text="synthetic evidence",
        source_file="synthetic.md",
        page=0,
    )


def _make_recorder(
    *,
    model_calls: int = 0,
    retrieval_calls: int = 0,
    input_tokens: int = 0,
    output_tokens: int = 0,
) -> RunRecorder:
    recorder = RunRecorder(
        run_id="unit-run-001",
        experiment_id="unit-test",
        task_id="T901",
        execution_mode="engineering",
        condition=None,
        code_revision="abcdef1",
        configuration=RunConfiguration(
            model_provider="engineering-test",
            model_name="no-model",
            model_config_id="engineering-no-model-v0.1",
            model_version=None,
            temperature=None,
            max_output_tokens=None,
            prompt_version="engineering-test-v0.1",
            retrieval_config_id="unit-test",
            workflow_config_id="unit-test",
            random_seed=None,
        ),
    )
    for _ in range(model_calls):
        recorder.record_model_call(
            status="completed",
            latency_ms=10.0,
            usage=TokenUsage(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
            ),
            finish_reason="stop",
            provider_response_id="resp-synthetic",
        )
    for _ in range(retrieval_calls):
        recorder.record_retrieval(
            query="synthetic query",
            top_k=1,
            latency_ms=5.0,
            results=(
                RetrievedChunk(chunk=_chunk(), rank=1, score=0.9),
            ),
        )
    return recorder


def _fresh_recorder() -> RunRecorder:
    return _make_recorder()


def _events(recorder: RunRecorder) -> list[dict[str, object]]:
    record = recorder.build_record(
        status="completed",
        answer=None,
        abstained=False,
    )
    return list(record["events"])


def _critic_result(
    *,
    support: SupportStatus = SupportStatus.PARTIAL_SUPPORT,
    sufficiency: EvidenceSufficiency = EvidenceSufficiency.INSUFFICIENT,
    conflict: bool = False,
    gaps: tuple[GapType, ...] = (GapType.MISSING_EVIDENCE,),
) -> CriticResult:
    return CriticResult(
        schema_version="0.1",
        support_status=support,
        evidence_sufficiency=sufficiency,
        unresolved_conflict=conflict,
        gap_types=gaps,
    )


def _decision(
    action: RecoveryAction = RecoveryAction.REVISE_ONLY,
) -> RecoveryDecision:
    reason = {
        RecoveryAction.ACCEPT: RecoveryReasonCode.RELEASE_OK,
        RecoveryAction.ABSTAIN: RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE,
        RecoveryAction.RESOURCE_STOP: RecoveryReasonCode.HARD_LIMIT_BLOCKED,
        RecoveryAction.REVISE_ONLY: RecoveryReasonCode.B1_FIXED_REVISE_ONLY,
        RecoveryAction.RERETRIEVE_REVISE: (
            RecoveryReasonCode.B1_FIXED_RERETRIEVE_REVISE
        ),
    }[action]
    return RecoveryDecision(
        action=action,
        reason_code=reason,
        policy_id="b1-fixed-policy",
    )


def _snapshot(
    *,
    llm: int = 2,
    retrieval: int = 1,
    retries: int = 1,
    tok_in: int = 100,
    tok_out: int = 50,
) -> ResourceSnapshot:
    return ResourceSnapshot(
        llm_calls_used=llm,
        retrieval_calls_used=retrieval,
        retries_used=retries,
        input_tokens_used=tok_in,
        output_tokens_used=tok_out,
        total_tokens_used=tok_in + tok_out,
    )


def _open_limits() -> ResourceLimits:
    return ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=3,
        max_retries=3,
        max_total_tokens=200,
        timeout_ms=None,
    )


def _standard_payload_inputs() -> dict[str, object]:
    recorder = _make_recorder(
        model_calls=2, retrieval_calls=1, input_tokens=40, output_tokens=10
    )
    limits = _open_limits()
    snapshot = build_resource_snapshot(
        recorder=recorder, recovery_iteration=1
    )
    feasibility = build_hard_recovery_feasibility(
        resources=snapshot, limits=limits
    )
    critic = CriticControlState.from_critic_result(_critic_result())
    return {
        "decision": _decision(),
        "critic": critic,
        "critic_iteration": 1,
        "decision_sequence": 1,
        "recovery_iteration": 1,
        "resources": snapshot,
        "limits": limits,
        "hard_recovery_feasibility": feasibility,
        "selected_recovery_path": RecoveryPath.REVISE_ONLY,
    }


# ---------------------------------------------------------------------------
# 1. Frozen vocabulary
# ---------------------------------------------------------------------------


def test_workflow_event_vocabulary_is_exactly_thirteen() -> None:
    assert len(WORKFLOW_EVENT_TYPES) == 13
    assert len(set(WORKFLOW_EVENT_TYPES)) == 13
    assert set(WORKFLOW_EVENT_TYPES) == {
        "plan_completed",
        "initial_retrieval_completed",
        "draft_completed",
        "initial_critic_completed",
        "policy_decision",
        "recovery_started",
        "recovery_retrieval_completed",
        "revision_completed",
        "post_recovery_critic_completed",
        "answer_accepted",
        "abstained",
        "resource_stopped",
        "workflow_failed",
    }
    assert "critic_completed" not in WORKFLOW_EVENT_TYPES


def test_blocked_limit_order_is_deterministic() -> None:
    assert BLOCKED_LIMIT_ORDER == (
        BlockedLimit.LLM_CALL_LIMIT,
        BlockedLimit.RETRIEVAL_CALL_LIMIT,
        BlockedLimit.RETRY_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
        BlockedLimit.TIMEOUT_LIMIT,
    )


def test_max_recovery_cycles_is_one() -> None:
    assert MAX_RECOVERY_CYCLES == 1


# ---------------------------------------------------------------------------
# 2. model_call_blockers
# ---------------------------------------------------------------------------


def test_model_call_blockers_none_block_when_capacity_remains() -> None:
    limits = ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=3,
        max_retries=3,
        max_total_tokens=200,
        timeout_ms=None,
    )
    resources = _snapshot(llm=1, retrieval=1, retries=1, tok_in=10, tok_out=5)
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=100
    ) == ()


def test_model_call_blockers_llm_exhausted() -> None:
    limits = ResourceLimits(
        max_llm_calls=1,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=None,
    )
    resources = _snapshot(llm=1)
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=0
    ) == (BlockedLimit.LLM_CALL_LIMIT,)


def test_model_call_blockers_token_limit() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=100,
        timeout_ms=None,
    )
    resources = _snapshot(llm=1, tok_in=60, tok_out=40)  # exactly 100 used
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=0
    ) == (BlockedLimit.TOKEN_LIMIT,)


def test_model_call_blockers_timeout_block() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=500.0,
    )
    resources = _snapshot(llm=0, tok_in=0, tok_out=0)
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=500
    ) == (BlockedLimit.TIMEOUT_LIMIT,)
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=499
    ) == ()


def test_model_call_blockers_canonical_order_llm_then_token_then_timeout() -> None:
    limits = ResourceLimits(
        max_llm_calls=1,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=5,
        timeout_ms=10.0,
    )
    resources = _snapshot(llm=1, tok_in=5, tok_out=0)
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=10
    ) == (
        BlockedLimit.LLM_CALL_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
        BlockedLimit.TIMEOUT_LIMIT,
    )


def test_model_call_blockers_rejects_bad_elapsed() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(llm=0, tok_in=0, tok_out=0)
    for bad in (True, "100", -1, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            model_call_blockers(
                resources=resources, limits=limits, elapsed_ms=bad
            )


def test_model_call_blockers_rejects_wrong_types() -> None:
    with pytest.raises((ValueError, TypeError)):
        model_call_blockers(resources=None, limits=None, elapsed_ms=1)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# 3. retrieval_call_blockers
# ---------------------------------------------------------------------------


def test_retrieval_call_blockers_none_block_when_capacity_remains() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=3,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=None,
    )
    resources = _snapshot(retrieval=1)
    assert retrieval_call_blockers(
        resources=resources, limits=limits, elapsed_ms=100
    ) == ()


def test_retrieval_call_blockers_retrieval_exhausted() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=1,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=None,
    )
    resources = _snapshot(retrieval=1)
    assert retrieval_call_blockers(
        resources=resources, limits=limits, elapsed_ms=0
    ) == (BlockedLimit.RETRIEVAL_CALL_LIMIT,)


def test_retrieval_call_blockers_canonical_order() -> None:
    limits = ResourceLimits(
        None, 1, None, None, 10.0
    )
    resources = _snapshot(retrieval=1)
    assert retrieval_call_blockers(
        resources=resources, limits=limits, elapsed_ms=10
    ) == (
        BlockedLimit.RETRIEVAL_CALL_LIMIT,
        BlockedLimit.TIMEOUT_LIMIT,
    )


def test_retrieval_call_blockers_rejects_bad_elapsed() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(retrieval=0)
    for bad in (True, "1", -5, math.nan, math.inf):
        with pytest.raises(ValueError):
            retrieval_call_blockers(
                resources=resources, limits=limits, elapsed_ms=bad
            )


# ---------------------------------------------------------------------------
# 4. begin_recovery_blockers
# ---------------------------------------------------------------------------


def test_begin_recovery_blockers_none_block_on_first_cycle() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=3,
        max_total_tokens=None,
        timeout_ms=None,
    )
    resources = _snapshot(retries=0)
    assert begin_recovery_blockers(
        resources=resources,
        limits=limits,
        elapsed_ms=10,
        recovery_iteration=0,
    ) == ()


def test_begin_recovery_blockers_retry_limit_block() -> None:
    limits = ResourceLimits(None, None, 0, None, None)
    resources = _snapshot(retries=0)
    assert begin_recovery_blockers(
        resources=resources,
        limits=limits,
        elapsed_ms=0,
        recovery_iteration=0,
    ) == (BlockedLimit.RETRY_LIMIT,)


def test_begin_recovery_blockers_canonical_order_retry_then_timeout() -> None:
    limits = ResourceLimits(None, None, 0, None, 10.0)
    resources = _snapshot(retries=0)
    assert begin_recovery_blockers(
        resources=resources,
        limits=limits,
        elapsed_ms=10,
        recovery_iteration=0,
    ) == (
        BlockedLimit.RETRY_LIMIT,
        BlockedLimit.TIMEOUT_LIMIT,
    )


def test_begin_recovery_blockers_rejects_out_of_range_iteration() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(retries=1)
    with pytest.raises(ValueError, match="out of range"):
        begin_recovery_blockers(
            resources=resources,
            limits=limits,
            elapsed_ms=0,
            recovery_iteration=1,
        )


def test_begin_recovery_blockers_rejects_iteration_mismatch() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(retries=2)
    with pytest.raises(ValueError, match="must equal resources.retries_used"):
        begin_recovery_blockers(
            resources=resources,
            limits=limits,
            elapsed_ms=0,
            recovery_iteration=0,
        )


def test_begin_recovery_blockers_rejects_bad_inputs() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(retries=0)
    for bad_iter in (-1, True, 1.5, "0"):
        with pytest.raises((ValueError, TypeError)):
            begin_recovery_blockers(
                resources=resources,
                limits=limits,
                elapsed_ms=0,
                recovery_iteration=bad_iter,  # type: ignore[arg-type]
            )
    for bad_elapsed in (True, "1", -1, math.nan):
        with pytest.raises(ValueError):
            begin_recovery_blockers(
                resources=resources,
                limits=limits,
                elapsed_ms=bad_elapsed,  # type: ignore[arg-type]
                recovery_iteration=0,
            )


# ---------------------------------------------------------------------------
# 5. resource snapshot builder
# ---------------------------------------------------------------------------


def test_build_resource_snapshot_maps_counters() -> None:
    recorder = _make_recorder(
        model_calls=2, retrieval_calls=3, input_tokens=11, output_tokens=7
    )
    snapshot = build_resource_snapshot(recorder=recorder, recovery_iteration=1)
    assert snapshot.llm_calls_used == 2
    assert snapshot.retrieval_calls_used == 3
    assert snapshot.retries_used == 1
    assert snapshot.input_tokens_used == 22
    assert snapshot.output_tokens_used == 14
    assert snapshot.total_tokens_used == 36
    assert snapshot.retries_used == 1


def test_build_resource_snapshot_rejects_bad_inputs() -> None:
    recorder = _make_recorder()
    for bad in (-1, 1.5, "1", True, False, None):
        with pytest.raises((ValueError, TypeError)):
            build_resource_snapshot(recorder=recorder, recovery_iteration=bad)


# ---------------------------------------------------------------------------
# 6. event recording
# ---------------------------------------------------------------------------


def test_record_workflow_event_validates_vocabulary() -> None:
    recorder = _fresh_recorder()
    with pytest.raises(ValueError, match="not one of the 13"):
        record_workflow_event(recorder=recorder, event_type="critic_completed")
    with pytest.raises(ValueError):
        record_workflow_event(recorder=recorder, event_type="")
    for event in WORKFLOW_EVENT_TYPES:
        record_workflow_event(
            recorder=recorder,
            event_type=event,
            stage="policy",
            details={"k": event},
        )
    events = _events(recorder)
    assert len(events) == 13
    assert [e["event_type"] for e in events] == list(WORKFLOW_EVENT_TYPES)
    assert [e["sequence"] for e in events] == list(range(1, 14))


# ---------------------------------------------------------------------------
# 7. flat 27-key payload
# ---------------------------------------------------------------------------


def test_payload_has_exactly_27_keys_in_order() -> None:
    payload = build_policy_decision_event(**_standard_payload_inputs())
    assert len(payload) == 27
    assert tuple(payload.keys()) == EXPECTED_27_KEY_ORDER


def test_payload_is_flat_no_nested_dicts() -> None:
    payload = build_policy_decision_event(**_standard_payload_inputs())
    for key, value in payload.items():
        if key in ("gap_types", "blocked_limits"):
            assert isinstance(value, list)
            assert all(
                not isinstance(item, dict) for item in value
            ), f"{key} must be a flat list"
            continue
        assert not isinstance(value, dict), f"{key} must not be a nested dict"


def test_payload_reflected_values_revise_only() -> None:
    kw = _standard_payload_inputs()
    payload = build_policy_decision_event(**kw)
    assert payload["policy_id"] == "b1-fixed-policy"
    assert payload["decision_sequence"] == 1
    assert payload["critic_iteration"] == 1
    assert payload["recovery_iteration"] == 1
    assert payload["selected_action"] == "REVISE_ONLY"
    assert payload["reason_code"] == "B1_FIXED_REVISE_ONLY"
    assert payload["support_status"] == "PARTIAL_SUPPORT"
    assert payload["evidence_sufficiency"] == "INSUFFICIENT"
    assert payload["unresolved_conflict"] is False
    assert payload["gap_types"] == ["MISSING_EVIDENCE"]
    assert payload["release_ok"] is False
    assert payload["llm_calls_used"] == 2
    assert payload["retrieval_calls_used"] == 1
    assert payload["retries_used"] == 1
    assert payload["input_tokens_used"] == 80
    assert payload["output_tokens_used"] == 20
    assert payload["total_tokens_used"] == 100
    assert payload["llm_calls_remaining"] == 2
    assert payload["retrieval_calls_remaining"] == 2
    assert payload["retries_remaining"] == 2
    assert payload["total_tokens_remaining"] == 100
    assert payload["selected_recovery_path"] == "REVISE_ONLY"
    assert payload["hard_recovery_feasible"] is True
    assert payload["blocked_limits"] == []


def test_payload_reretrieve_revise() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.RERETRIEVE_REVISE)
    kw["selected_recovery_path"] = RecoveryPath.RERETRIEVE_REVISE
    payload = build_policy_decision_event(**kw)
    assert payload["selected_action"] == "RERETRIEVE_REVISE"
    assert payload["selected_recovery_path"] == "RERETRIEVE_REVISE"
    assert payload["hard_recovery_feasible"] is True


def test_payload_path_none_values() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.ACCEPT)
    kw["selected_recovery_path"] = None
    payload = build_policy_decision_event(**kw)
    assert payload["selected_action"] == "ACCEPT"
    assert payload["selected_recovery_path"] == "NONE"
    assert payload["hard_recovery_feasible"] is None
    assert payload["blocked_limits"] == []


def test_decision_sequence_is_separate_from_critic_iteration() -> None:
    kw = _standard_payload_inputs()
    kw["critic_iteration"] = 1
    kw["decision_sequence"] = 7
    payload = build_policy_decision_event(**kw)
    assert payload["decision_sequence"] == 7
    assert payload["critic_iteration"] == 1


def test_payload_requires_positive_decision_sequence() -> None:
    kw = _standard_payload_inputs()
    for bad in (0, -1, True, 1.5, "1"):
        kw_bad = dict(kw, decision_sequence=bad)
        with pytest.raises((ValueError, TypeError)):
            build_policy_decision_event(**kw_bad)


def test_payload_critic_iteration_none_zero_and_positive_preserved() -> None:
    kw = _standard_payload_inputs()
    # None preserved as None.
    payload = build_policy_decision_event(**dict(kw, critic_iteration=None))
    assert payload["critic_iteration"] is None
    # 0 preserved as 0 (not translated to None or 1).
    payload = build_policy_decision_event(**dict(kw, critic_iteration=0))
    assert payload["critic_iteration"] == 0
    # Positive int preserved exactly.
    payload = build_policy_decision_event(**dict(kw, critic_iteration=7))
    assert payload["critic_iteration"] == 7


def test_payload_critic_iteration_rejects_invalid_types() -> None:
    kw = _standard_payload_inputs()
    for bad in (-1, True, False, 1.5, "1", [], {}):
        with pytest.raises((ValueError, TypeError)):
            build_policy_decision_event(
                **dict(kw, critic_iteration=bad)
            )


def test_payload_requires_non_negative_recovery_iteration() -> None:
    kw = _standard_payload_inputs()
    with pytest.raises((ValueError, TypeError)):
        build_policy_decision_event(**dict(kw, recovery_iteration=-1))
    build_policy_decision_event(**dict(kw, recovery_iteration=0))


def test_payload_optional_defaults_are_null() -> None:
    kw = _standard_payload_inputs()
    for key in (
        "path_reserve_satisfied",
        "recovery_rule_version",
        "resource_reserve_rule_version",
    ):
        assert key in set(EXPECTED_27_KEY_ORDER)
    payload = build_policy_decision_event(**kw)
    assert payload["path_reserve_satisfied"] is None
    assert payload["recovery_rule_version"] is None
    assert payload["resource_reserve_rule_version"] is None
    assert "condition" not in payload
    assert "gold" not in payload
    assert "reference" not in payload
    assert "benchmark" not in payload


# ---------------------------------------------------------------------------
# 8. action / path cross-validation
# ---------------------------------------------------------------------------


def test_action_path_revise_only_requires_matching_path() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.REVISE_ONLY)
    kw["selected_recovery_path"] = RecoveryPath.RERETRIEVE_REVISE
    with pytest.raises(ValueError, match="REVISE_ONLY"):
        build_policy_decision_event(**kw)
    kw["selected_recovery_path"] = None
    with pytest.raises(ValueError, match="REVISE_ONLY"):
        build_policy_decision_event(**kw)


def test_action_path_reretrieve_revise_requires_matching_path() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.RERETRIEVE_REVISE)
    kw["selected_recovery_path"] = RecoveryPath.REVISE_ONLY
    with pytest.raises(ValueError, match="RERETRIEVE_REVISE"):
        build_policy_decision_event(**kw)


def test_action_path_accept_requires_none() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.ACCEPT)
    kw["selected_recovery_path"] = RecoveryPath.REVISE_ONLY
    with pytest.raises(ValueError, match="ACCEPT"):
        build_policy_decision_event(**kw)


def test_action_path_abstain_requires_none() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.ABSTAIN)
    kw["selected_recovery_path"] = RecoveryPath.RERETRIEVE_REVISE
    with pytest.raises(ValueError, match="ABSTAIN"):
        build_policy_decision_event(**kw)


def test_action_path_resource_stop_requires_path() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.RESOURCE_STOP)
    kw["selected_recovery_path"] = None
    with pytest.raises(ValueError, match="RESOURCE_STOP"):
        build_policy_decision_event(**kw)
    # With a valid path it succeeds.
    kw["selected_recovery_path"] = RecoveryPath.REVISE_ONLY
    payload = build_policy_decision_event(**kw)
    assert payload["selected_action"] == "RESOURCE_STOP"
    assert payload["selected_recovery_path"] == "REVISE_ONLY"


def test_action_path_missing_feasibility_entry_raises() -> None:
    kw = _standard_payload_inputs()
    kw["decision"] = _decision(RecoveryAction.REVISE_ONLY)
    kw["selected_recovery_path"] = RecoveryPath.REVISE_ONLY
    kw["hard_recovery_feasibility"] = tuple(
        f for f in kw["hard_recovery_feasibility"]
        if f.recovery_path is RecoveryPath.RERETRIEVE_REVISE
    )
    with pytest.raises(ValueError, match="missing an entry"):
        build_policy_decision_event(**kw)


# ---------------------------------------------------------------------------
# 9. deep-copy on record
# ---------------------------------------------------------------------------


def test_record_policy_decision_emits_event() -> None:
    kw = _standard_payload_inputs()
    recorder = _fresh_recorder()
    record_policy_decision(recorder=recorder, **kw)
    events = _events(recorder)
    assert len(events) == 1
    assert events[0]["event_type"] == "policy_decision"
    expected = build_policy_decision_event(**kw)
    assert events[0]["details"] == expected


def test_record_policy_decision_deepcopies_details() -> None:
    details = {"note": "x", "nested": {"a": 1}}
    recorder = _fresh_recorder()
    record_workflow_event(
        recorder=recorder, event_type="policy_decision", details=details
    )
    # Mutate after recording.
    details["note"] = "mutated"
    details["nested"]["a"] = 999
    details["extra"] = "post-hoc"
    events = _events(recorder)
    assert events[0]["details"] == {"note": "x", "nested": {"a": 1}}


# ---------------------------------------------------------------------------
# 10. build_recovery_policy_context
# ---------------------------------------------------------------------------


def test_policy_context_fields_and_retries_invariant() -> None:
    recorder = _make_recorder(
        model_calls=1, retrieval_calls=2, input_tokens=10, output_tokens=5
    )
    limits = ResourceLimits(5, 4, 2, 100, 1000.0)
    ctx = build_recovery_policy_context(
        critic_result=_critic_result(),
        recovery_iteration=1,
        recorder=recorder,
        limits=limits,
    )
    assert ctx.recovery_iteration == 1
    assert ctx.limits is limits
    assert ctx.resources.retries_used == ctx.recovery_iteration
    critic = ctx.critic
    assert critic.support_status is SupportStatus.PARTIAL_SUPPORT
    assert critic.release_ok is False
    assert len(ctx.hard_recovery_feasibility) == 2


def test_policy_context_rejects_second_cycle() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    build_hard_recovery_feasibility(resources=_snapshot(), limits=limits)
    from responsible_agentic_workflows.workflow import begin_recovery_cycle

    with pytest.raises(ValueError, match="MAX_RECOVERY_CYCLES"):
        begin_recovery_cycle(
            recovery_iteration=1,
            completed=False,
            action=RecoveryAction.REVISE_ONLY,
        )
    state = begin_recovery_cycle(
        recovery_iteration=0,
        completed=False,
        action=RecoveryAction.RERETRIEVE_REVISE,
    )
    assert state.recovery_iteration == 1


def test_policy_context_has_no_forbidden_params() -> None:
    params = set(inspect.signature(build_recovery_policy_context).parameters)
    forbidden = {"condition", "gold", "reference", "benchmark"}
    assert params.isdisjoint(forbidden)
    expected = {
        "critic_result",
        "recovery_iteration",
        "recorder",
        "limits",
    }
    assert expected.issubset(params)


# ---------------------------------------------------------------------------
# 11. evaluate_recovery_path_guard removal
# ---------------------------------------------------------------------------


def test_evaluate_recovery_path_guard_is_removed() -> None:
    import responsible_agentic_workflows.workflow as w
    import responsible_agentic_workflows.workflow.execution as ex

    assert not hasattr(w, "evaluate_recovery_path_guard")
    assert not hasattr(ex, "evaluate_recovery_path_guard")
    with pytest.raises(ImportError):
        from responsible_agentic_workflows.workflow import (  # noqa: F401
            evaluate_recovery_path_guard,
        )


def test_new_guards_are_exported() -> None:
    import responsible_agentic_workflows.workflow as w

    for name in (
        "begin_recovery_blockers",
        "model_call_blockers",
        "retrieval_call_blockers",
    ):
        assert hasattr(w, name)
        assert name in w.__all__


def test_new_guard_signatures() -> None:
    for fn in (
        model_call_blockers,
        retrieval_call_blockers,
        begin_recovery_blockers,
    ):
        params = set(inspect.signature(fn).parameters)
        assert {"resources", "limits", "elapsed_ms"}.issubset(params)
    assert "recovery_iteration" in set(
        inspect.signature(begin_recovery_blockers).parameters
    )


# ---------------------------------------------------------------------------
# 12. failed model call counts without token inflation (§3)
# ---------------------------------------------------------------------------


def test_failed_model_call_counts_without_token_inflation() -> None:
    recorder = _fresh_recorder()
    recorder.record_model_call(
        status="failed",
        latency_ms=10.0,
        usage=None,
        finish_reason=None,
        provider_response_id=None,
    )
    assert recorder.model_call_count == 1
    assert recorder.input_tokens_used == 0
    assert recorder.output_tokens_used == 0
    assert recorder.total_tokens_used == 0
    snapshot = build_resource_snapshot(
        recorder=recorder, recovery_iteration=0
    )
    assert snapshot.llm_calls_used == 1
    assert snapshot.input_tokens_used == 0
    assert snapshot.output_tokens_used == 0
    assert snapshot.total_tokens_used == 0


# ---------------------------------------------------------------------------
# 13. zero activity snapshot (§4)
# ---------------------------------------------------------------------------


def test_zero_activity_snapshot() -> None:
    recorder = _fresh_recorder()
    snapshot = build_resource_snapshot(
        recorder=recorder, recovery_iteration=0
    )
    assert snapshot.llm_calls_used == 0
    assert snapshot.retrieval_calls_used == 0
    assert snapshot.retries_used == 0
    assert snapshot.input_tokens_used == 0
    assert snapshot.output_tokens_used == 0
    assert snapshot.total_tokens_used == 0


# ---------------------------------------------------------------------------
# 14. feasibility calculator called twice in order (§5)
# ---------------------------------------------------------------------------


def test_feasibility_calculator_called_twice_in_order(monkeypatch) -> None:
    import responsible_agentic_workflows.workflow.execution as ex

    calls: list[tuple[object, object, object]] = []
    sentinel = HardRecoveryFeasibility(
        recovery_path=RecoveryPath.REVISE_ONLY,
        feasible=True,
        blocked_limits=(),
    )

    def fake_calculate(
        *,
        recovery_path,  # type: ignore[no-untyped-def]
        resources,  # type: ignore[no-untyped-def]
        limits,  # type: ignore[no-untyped-def]
    ):
        calls.append((recovery_path, resources, limits))
        return sentinel

    monkeypatch.setattr(ex, "calculate_hard_recovery_feasibility", fake_calculate)
    resources = _snapshot()
    limits = _open_limits()
    result = build_hard_recovery_feasibility(
        resources=resources, limits=limits
    )
    assert len(result) == 2
    assert len(calls) == 2
    assert calls[0][0] is RecoveryPath.REVISE_ONLY
    assert calls[1][0] is RecoveryPath.RERETRIEVE_REVISE
    assert calls[0][1] is resources
    assert calls[1][1] is resources
    assert calls[0][2] is limits
    assert calls[1][2] is limits


# ---------------------------------------------------------------------------
# 15. no future token estimation (§6)
# ---------------------------------------------------------------------------


def test_no_future_token_estimation() -> None:
    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=100,
        timeout_ms=None,
    )
    # used=99: remaining=1, NOT blocked (remaining > 0).
    resources = _snapshot(llm=0, retrieval=0, retries=0, tok_in=60, tok_out=39)
    assert resources.total_tokens_used == 99
    assert resources.total_tokens_remaining(limits) == 1
    assert BlockedLimit.TOKEN_LIMIT not in model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=0
    )
    # used=100: remaining=0, blocked by TOKEN_LIMIT.
    resources_full = _snapshot(llm=0, retrieval=0, retries=0, tok_in=70, tok_out=30)
    assert resources_full.total_tokens_used == 100
    assert resources_full.total_tokens_remaining(limits) == 0
    assert BlockedLimit.TOKEN_LIMIT in model_call_blockers(
        resources=resources_full, limits=limits, elapsed_ms=0
    )


# ---------------------------------------------------------------------------
# 16. all limits None -> empty blockers (§7)
# ---------------------------------------------------------------------------


def test_model_call_blockers_all_limits_none() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot()
    assert model_call_blockers(
        resources=resources, limits=limits, elapsed_ms=100
    ) == ()


def test_retrieval_call_blockers_all_limits_none() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot()
    assert retrieval_call_blockers(
        resources=resources, limits=limits, elapsed_ms=100
    ) == ()


def test_begin_recovery_blockers_all_limits_none() -> None:
    limits = ResourceLimits(None, None, None, None, None)
    resources = _snapshot(retries=0)
    assert begin_recovery_blockers(
        resources=resources,
        limits=limits,
        elapsed_ms=0,
        recovery_iteration=0,
    ) == ()


# ---------------------------------------------------------------------------
# 17. RESOURCE_STOP HARD_LIMIT_BLOCKED payload (§8)
# ---------------------------------------------------------------------------


def test_resource_stop_hard_limit_blocked_payload() -> None:
    # LLM limits fully exhausted -> feasibility not feasible, LLM_CALL_LIMIT blocked.
    limits = ResourceLimits(
        max_llm_calls=1,
        max_retrieval_calls=3,
        max_retries=3,
        max_total_tokens=200,
        timeout_ms=None,
    )
    resources = _snapshot(llm=1, retrieval=0, retries=0, tok_in=0, tok_out=0)
    feasibility = build_hard_recovery_feasibility(
        resources=resources, limits=limits
    )
    decision = RecoveryDecision(
        action=RecoveryAction.RESOURCE_STOP,
        reason_code=RecoveryReasonCode.HARD_LIMIT_BLOCKED,
        policy_id="b1-fixed-policy",
    )
    critic = CriticControlState.from_critic_result(_critic_result())
    payload = build_policy_decision_event(
        decision=decision,
        critic=critic,
        critic_iteration=1,
        decision_sequence=1,
        recovery_iteration=0,
        resources=resources,
        limits=limits,
        hard_recovery_feasibility=feasibility,
        selected_recovery_path=RecoveryPath.REVISE_ONLY,
    )
    assert payload["selected_action"] == "RESOURCE_STOP"
    assert payload["reason_code"] == "HARD_LIMIT_BLOCKED"
    assert payload["selected_recovery_path"] == "REVISE_ONLY"
    assert payload["hard_recovery_feasible"] is False
    assert BlockedLimit.LLM_CALL_LIMIT.value in payload["blocked_limits"]


# ---------------------------------------------------------------------------
# 18. G1 reserve blocked payload (§9)
# ---------------------------------------------------------------------------


def test_g1_reserve_blocked_payload() -> None:
    limits = _open_limits()
    resources = _snapshot()
    feasibility = build_hard_recovery_feasibility(
        resources=resources, limits=limits
    )
    decision = RecoveryDecision(
        action=RecoveryAction.RESOURCE_STOP,
        reason_code=RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED,
        policy_id="g1-fixed-policy",
    )
    critic = CriticControlState.from_critic_result(_critic_result())
    payload = build_policy_decision_event(
        decision=decision,
        critic=critic,
        critic_iteration=2,
        decision_sequence=2,
        recovery_iteration=1,
        resources=resources,
        limits=limits,
        hard_recovery_feasibility=feasibility,
        selected_recovery_path=RecoveryPath.RERETRIEVE_REVISE,
        path_reserve_satisfied=False,
    )
    assert payload["selected_action"] == "RESOURCE_STOP"
    assert payload["reason_code"] == "G1_RESOURCE_RESERVE_BLOCKED"
    assert payload["selected_recovery_path"] == "RERETRIEVE_REVISE"
    assert payload["hard_recovery_feasible"] is True
    assert payload["path_reserve_satisfied"] is False
    assert payload["blocked_limits"] == []


# ---------------------------------------------------------------------------
# 19. rule version preserved (§10)
# ---------------------------------------------------------------------------


def test_rule_version_preserved() -> None:
    kw = _standard_payload_inputs()
    kw["recovery_rule_version"] = "rev-b1-v0.1"
    kw["resource_reserve_rule_version"] = "resv-g1-v0.2"
    payload = build_policy_decision_event(**kw)
    assert payload["recovery_rule_version"] == "rev-b1-v0.1"
    assert payload["resource_reserve_rule_version"] == "resv-g1-v0.2"


def test_rule_version_invalid_values_rejected() -> None:
    kw = _standard_payload_inputs()
    for bad in ("", "   ", 123, 1.5, True, b"bin", []):
        with pytest.raises((ValueError, TypeError)):
            build_policy_decision_event(
                **dict(kw, recovery_rule_version=bad)
            )
        with pytest.raises((ValueError, TypeError)):
            build_policy_decision_event(
                **dict(kw, resource_reserve_rule_version=bad)
            )
    # ``None`` is a valid value for both rule-version fields.
    payload = build_policy_decision_event(
        **dict(kw, recovery_rule_version=None,
               resource_reserve_rule_version=None)
    )
    assert payload["recovery_rule_version"] is None
    assert payload["resource_reserve_rule_version"] is None


# ---------------------------------------------------------------------------
# 20. path_reserve_satisfied validation (§11)
# ---------------------------------------------------------------------------


def test_path_reserve_satisfied_accepts_bool_or_none() -> None:
    kw = _standard_payload_inputs()
    for value in (True, False, None):
        payload = build_policy_decision_event(
            **dict(kw, path_reserve_satisfied=value)
        )
        assert payload["path_reserve_satisfied"] is value or (
            value is None and payload["path_reserve_satisfied"] is None
        )


def test_path_reserve_satisfied_rejects_non_bool() -> None:
    kw = _standard_payload_inputs()
    for bad in (0, 1, "true", "false", [], {}, 1.0):
        with pytest.raises((ValueError, TypeError)):
            build_policy_decision_event(
                **dict(kw, path_reserve_satisfied=bad)
            )


# ---------------------------------------------------------------------------
# 21. forbidden policy event fields (§12)
# ---------------------------------------------------------------------------


def test_forbidden_policy_event_fields() -> None:
    kw = _standard_payload_inputs()
    payload = build_policy_decision_event(**kw)
    forbidden = {
        "condition",
        "condition_metadata",
        "reference_answer",
        "reference_evidence",
        "correctness",
        "adjudication",
        "explanation",
        "unsupported_claims",
        "incomplete_support",
        "evidence_gaps",
    }
    keys = set(payload.keys())
    for name in forbidden:
        assert name not in keys, f"forbidden key {name!r} in payload"
    assert keys == set(EXPECTED_27_KEY_ORDER)
