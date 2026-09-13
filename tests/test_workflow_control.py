import pytest

from responsible_agentic_workflows.workflow import (
    BlockedLimit,
    CriticControlState,
    CriticResult,
    EvidenceSufficiency,
    GapType,
    HardRecoveryFeasibility,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryPolicy,
    RecoveryPolicyContext,
    RecoveryReasonCode,
    ResourceLimits,
    ResourceSnapshot,
    SupportStatus,
    release_ok,
)


def test_enum_member_sets_are_exact() -> None:
    assert set(SupportStatus) == {
        SupportStatus.SUPPORTED,
        SupportStatus.PARTIAL_SUPPORT,
        SupportStatus.UNSUPPORTED,
    }

    assert set(EvidenceSufficiency) == {
        EvidenceSufficiency.SUFFICIENT,
        EvidenceSufficiency.INSUFFICIENT,
    }

    assert set(GapType) == {
        GapType.DRAFT_GROUNDING,
        GapType.MISSING_EVIDENCE,
        GapType.INCOMPLETE_EVIDENCE,
        GapType.EVIDENCE_CONFLICT,
    }

    assert set(RecoveryAction) == {
        RecoveryAction.ACCEPT,
        RecoveryAction.REVISE_ONLY,
        RecoveryAction.RERETRIEVE_REVISE,
        RecoveryAction.ABSTAIN,
        RecoveryAction.RESOURCE_STOP,
    }

    assert set(RecoveryPath) == {
        RecoveryPath.REVISE_ONLY,
        RecoveryPath.RERETRIEVE_REVISE,
    }

    assert set(BlockedLimit) == {
        BlockedLimit.LLM_CALL_LIMIT,
        BlockedLimit.RETRIEVAL_CALL_LIMIT,
        BlockedLimit.RETRY_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
        BlockedLimit.TIMEOUT_LIMIT,
    }

    assert set(RecoveryReasonCode) == {
        RecoveryReasonCode.RELEASE_OK,
        RecoveryReasonCode.HARD_LIMIT_BLOCKED,
        RecoveryReasonCode.B1_FIXED_REVISE_ONLY,
        RecoveryReasonCode.B1_FIXED_RERETRIEVE_REVISE,
        RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE,
        RecoveryReasonCode.G1_REVISE_ONLY,
        RecoveryReasonCode.G1_RERETRIEVE_REVISE,
        RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED,
    }


def test_critic_result_release_predicate() -> None:
    result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.SUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )

    assert release_ok(result) is True

    result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.PARTIAL_SUPPORT,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )

    assert release_ok(result) is False

    result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.SUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
    )

    assert release_ok(result) is False

    result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.SUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    assert release_ok(result) is False


def test_critic_result_requires_conflict_gap_type() -> None:
    with pytest.raises(ValueError, match="EVIDENCE_CONFLICT"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=True,
            gap_types=(GapType.MISSING_EVIDENCE,),
        )

    with pytest.raises(ValueError, match="EVIDENCE_CONFLICT"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.UNSUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
            unresolved_conflict=True,
        )


def test_critic_result_rejects_duplicate_and_empty_strings() -> None:
    with pytest.raises(ValueError, match="unsupported_claims"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.UNSUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
            unsupported_claims=("claim-a", "claim-a"),
        )

    with pytest.raises(ValueError, match="incomplete_support"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.PARTIAL_SUPPORT,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
            incomplete_support=("supported claim", ""),
        )

    with pytest.raises(ValueError, match="evidence_gaps"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
            unresolved_conflict=False,
            gap_types=(GapType.INCOMPLETE_EVIDENCE,),
            evidence_gaps=("gap", "gap"),
        )


def test_critic_result_rejects_whitespace_only_diagnostics() -> None:
    base = {
        "schema_version": "0.1",
        "support_status": SupportStatus.SUPPORTED,
        "evidence_sufficiency": EvidenceSufficiency.SUFFICIENT,
        "unresolved_conflict": False,
    }

    for field in (
        "unsupported_claims",
        "incomplete_support",
        "evidence_gaps",
    ):
        with pytest.raises(ValueError):
            CriticResult(
                **base,
                **{field: ("   ",)},
            )


def test_critic_result_rejects_invalid_types() -> None:
    with pytest.raises(ValueError, match="support_status"):
        CriticResult(
            schema_version="0.1",
            support_status="SUPPORTED",
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
        )

    with pytest.raises(ValueError, match="evidence_sufficiency"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency="SUFFICIENT",
            unresolved_conflict=False,
        )

    with pytest.raises(ValueError, match="gap_types"):
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
            gap_types=(GapType.DRAFT_GROUNDING, 5),
        )


def test_critic_result_is_immutable() -> None:
    result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.SUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )

    with pytest.raises(AttributeError):
        result.explanation = "mutated"


def test_release_ok_truth_table() -> None:
    assert release_ok(
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
        )
    ) is True

    assert release_ok(
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=True,
            gap_types=(GapType.EVIDENCE_CONFLICT,),
        )
    ) is False

    assert release_ok(
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.SUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
            unresolved_conflict=False,
        )
    ) is False

    assert release_ok(
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.PARTIAL_SUPPORT,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            unresolved_conflict=False,
        )
    ) is False

    assert release_ok(
        CriticResult(
            schema_version="0.1",
            support_status=SupportStatus.UNSUPPORTED,
            evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
            unresolved_conflict=True,
            gap_types=(GapType.EVIDENCE_CONFLICT,),
        )
    ) is False


def test_critic_control_state_from_critic_result() -> None:
    critic_result = CriticResult(
        schema_version="0.1",
        support_status=SupportStatus.PARTIAL_SUPPORT,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
        gap_types=(
            GapType.DRAFT_GROUNDING,
            GapType.INCOMPLETE_EVIDENCE,
        ),
        unsupported_claims=("claim-a",),
        incomplete_support=("supported claim",),
        evidence_gaps=("gap-1",),
        explanation="free-form audit note",
    )

    state = CriticControlState.from_critic_result(critic_result)

    assert state.support_status is SupportStatus.PARTIAL_SUPPORT
    assert (
        state.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT
    )
    assert state.unresolved_conflict is False
    assert state.gap_types == (
        GapType.DRAFT_GROUNDING,
        GapType.INCOMPLETE_EVIDENCE,
    )
    assert state.release_ok is False

    assert not hasattr(state, "explanation")
    assert not hasattr(state, "unsupported_claims")
    assert not hasattr(state, "incomplete_support")
    assert not hasattr(state, "evidence_gaps")


def test_resource_limits_allow_unlimited_axes() -> None:
    all_limited = ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=2,
        max_retries=3,
        max_total_tokens=1000,
        timeout_ms=90000.0,
    )

    assert all_limited.max_llm_calls == 4
    assert all_limited.max_retrieval_calls == 2
    assert all_limited.max_retries == 3
    assert all_limited.max_total_tokens == 1000
    assert all_limited.timeout_ms == 90000.0

    unlimited = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=None,
    )

    assert unlimited.max_llm_calls is None
    assert unlimited.timeout_ms is None


def test_resource_limits_reject_invalid_configured_ceilings() -> None:
    base = {
        "max_llm_calls": None,
        "max_retrieval_calls": None,
        "max_retries": None,
        "max_total_tokens": None,
        "timeout_ms": None,
    }

    invalid = (
        ("max_llm_calls", 0),
        ("max_retrieval_calls", 0),
        ("max_retries", -1),
        ("max_total_tokens", 0),
        ("timeout_ms", 0.0),
    )

    for field, value in invalid:
        values = {**base, field: value}
        with pytest.raises(ValueError):
            ResourceLimits(**values)


def test_resource_snapshot_validates_counters() -> None:
    snapshot = ResourceSnapshot(
        llm_calls_used=2,
        retrieval_calls_used=1,
        retries_used=0,
        input_tokens_used=700,
        output_tokens_used=300,
        total_tokens_used=1000,
    )

    assert snapshot.total_tokens_used == 1000

    with pytest.raises(ValueError, match="must not be negative"):
        ResourceSnapshot(
            llm_calls_used=-1,
            retrieval_calls_used=1,
            retries_used=0,
            input_tokens_used=1,
            output_tokens_used=1,
            total_tokens_used=2,
        )

    with pytest.raises(ValueError, match="input_tokens_used"):
        ResourceSnapshot(
            llm_calls_used=1,
            retrieval_calls_used=1,
            retries_used=1,
            input_tokens_used=-5,
            output_tokens_used=5,
            total_tokens_used=0,
        )

    with pytest.raises(ValueError, match="total_tokens_used"):
        ResourceSnapshot(
            llm_calls_used=1,
            retrieval_calls_used=1,
            retries_used=1,
            input_tokens_used=700,
            output_tokens_used=300,
            total_tokens_used=900,
        )


def test_resource_snapshot_remaining_accounts_for_none_and_excess() -> None:
    limits = ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=None,
        max_retries=3,
        max_total_tokens=1000,
        timeout_ms=None,
    )

    snapshot = ResourceSnapshot(
        llm_calls_used=2,
        retrieval_calls_used=7,
        retries_used=5,
        input_tokens_used=700,
        output_tokens_used=300,
        total_tokens_used=1000,
    )

    assert snapshot.llm_calls_remaining(limits) == 2
    assert snapshot.retrieval_calls_remaining(limits) is None
    assert snapshot.retries_remaining(limits) == 0
    assert snapshot.total_tokens_remaining(limits) == 0

    exhausted = ResourceSnapshot(
        llm_calls_used=6,
        retrieval_calls_used=1,
        retries_used=0,
        input_tokens_used=0,
        output_tokens_used=0,
        total_tokens_used=0,
    )

    assert exhausted.llm_calls_remaining(limits) == 0


def test_hard_recovery_feasibility_invariants() -> None:
    feasible = HardRecoveryFeasibility(
        recovery_path=RecoveryPath.REVISE_ONLY,
        feasible=True,
    )

    assert feasible.blocked_limits == ()

    infeasible = HardRecoveryFeasibility(
        recovery_path=RecoveryPath.RERETRIEVE_REVISE,
        feasible=False,
        blocked_limits=(
            BlockedLimit.RETRIEVAL_CALL_LIMIT,
            BlockedLimit.TOKEN_LIMIT,
        ),
    )

    assert infeasible.blocked_limits == (
        BlockedLimit.RETRIEVAL_CALL_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
    )

    with pytest.raises(ValueError, match="feasible recovery"):
        HardRecoveryFeasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            feasible=True,
            blocked_limits=(BlockedLimit.RETRY_LIMIT,),
        )

    with pytest.raises(ValueError, match="infeasible recovery"):
        HardRecoveryFeasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            feasible=False,
            blocked_limits=(),
        )

    with pytest.raises(ValueError, match="recovery_path"):
        HardRecoveryFeasibility(
            recovery_path="REVISE_ONLY",
            feasible=True,
        )

    with pytest.raises(ValueError, match="blocked_limits"):
        HardRecoveryFeasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            feasible=False,
            blocked_limits=(BlockedLimit.RETRY_LIMIT, BlockedLimit.RETRY_LIMIT),
        )


def _context() -> RecoveryPolicyContext:
    critic = CriticControlState(
        support_status=SupportStatus.PARTIAL_SUPPORT,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
        gap_types=(GapType.DRAFT_GROUNDING,),
        release_ok=False,
    )

    snapshot = ResourceSnapshot(
        llm_calls_used=1,
        retrieval_calls_used=1,
        retries_used=0,
        input_tokens_used=500,
        output_tokens_used=200,
        total_tokens_used=700,
    )

    limits = ResourceLimits(
        max_llm_calls=4,
        max_retrieval_calls=2,
        max_retries=2,
        max_total_tokens=2000,
        timeout_ms=60000.0,
    )

    feasibility = (
        HardRecoveryFeasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            feasible=True,
        ),
        HardRecoveryFeasibility(
            recovery_path=RecoveryPath.RERETRIEVE_REVISE,
            feasible=False,
            blocked_limits=(BlockedLimit.TOKEN_LIMIT,),
        ),
    )

    return RecoveryPolicyContext(
        critic=critic,
        recovery_iteration=1,
        resources=snapshot,
        limits=limits,
        hard_recovery_feasibility=feasibility,
    )


def test_recovery_policy_context_validates_structure() -> None:
    context = _context()

    assert context.recovery_iteration == 1
    assert isinstance(context.critic, CriticControlState)
    assert isinstance(context.resources, ResourceSnapshot)
    assert isinstance(context.limits, ResourceLimits)
    assert context.hard_recovery_feasibility[1].recovery_path is (
        RecoveryPath.RERETRIEVE_REVISE
    )

    with pytest.raises(ValueError, match="recovery_iteration"):
        RecoveryPolicyContext(
            critic=_context().critic,
            recovery_iteration=-1,
            resources=_context().resources,
            limits=_context().limits,
            hard_recovery_feasibility=_context().hard_recovery_feasibility,
        )

    with pytest.raises(ValueError, match="duplicate recovery paths"):
        duplicate = HardRecoveryFeasibility(
            recovery_path=RecoveryPath.REVISE_ONLY,
            feasible=True,
        )

        RecoveryPolicyContext(
            critic=_context().critic,
            recovery_iteration=0,
            resources=_context().resources,
            limits=_context().limits,
            hard_recovery_feasibility=(duplicate, duplicate),
        )

    with pytest.raises(ValueError, match="critic"):
        RecoveryPolicyContext(
            critic="free-form",
            recovery_iteration=0,
            resources=_context().resources,
            limits=_context().limits,
            hard_recovery_feasibility=(),
        )


def test_recovery_decision_requires_policy_id() -> None:
    decision = RecoveryDecision(
        action=RecoveryAction.REVISE_ONLY,
        reason_code=RecoveryReasonCode.B1_FIXED_REVISE_ONLY,
        policy_id="b1-fixed-v0.1",
    )

    assert decision.action is RecoveryAction.REVISE_ONLY
    assert decision.reason_code is RecoveryReasonCode.B1_FIXED_REVISE_ONLY
    assert decision.policy_id == "b1-fixed-v0.1"

    with pytest.raises(ValueError, match="policy_id"):
        RecoveryDecision(
            action=RecoveryAction.ACCEPT,
            reason_code=RecoveryReasonCode.RELEASE_OK,
            policy_id="",
        )

    with pytest.raises(ValueError, match="action"):
        RecoveryDecision(
            action="REVISE_ONLY",
            reason_code=RecoveryReasonCode.B1_FIXED_REVISE_ONLY,
            policy_id="b1-fixed-v0.1",
        )

    with pytest.raises(ValueError, match="reason_code"):
        RecoveryDecision(
            action=RecoveryAction.ACCEPT,
            reason_code="RELEASE_OK",
            policy_id="b1-fixed-v0.1",
        )


def test_recovery_decision_rejects_invalid_policy_id() -> None:
    for policy_id in ("", "   ", 123):
        with pytest.raises(ValueError):
            RecoveryDecision(
                action=RecoveryAction.ACCEPT,
                reason_code=RecoveryReasonCode.RELEASE_OK,
                policy_id=policy_id,
            )


def test_recovery_policy_protocol_is_runtime_checkable() -> None:
    class FixedPolicy:
        def decide(
            self, context: RecoveryPolicyContext
        ) -> RecoveryDecision:
            return RecoveryDecision(
                action=RecoveryAction.ACCEPT,
                reason_code=RecoveryReasonCode.RELEASE_OK,
                policy_id="fixed-v0.1",
            )

    class MissingDecide:
        pass

    assert isinstance(FixedPolicy(), RecoveryPolicy)
    assert not isinstance(MissingDecide(), RecoveryPolicy)
    assert not isinstance(object(), RecoveryPolicy)


def test_recovery_dataclasses_are_immutable() -> None:
    snapshot = ResourceSnapshot(
        llm_calls_used=1,
        retrieval_calls_used=1,
        retries_used=1,
        input_tokens_used=10,
        output_tokens_used=10,
        total_tokens_used=20,
    )

    limits = ResourceLimits(
        max_llm_calls=None,
        max_retrieval_calls=None,
        max_retries=None,
        max_total_tokens=None,
        timeout_ms=None,
    )

    decision = RecoveryDecision(
        action=RecoveryAction.ABSTAIN,
        reason_code=RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE,
        policy_id="g1-v0.1",
    )

    context = _context()

    frozen = (
        snapshot,
        limits,
        decision,
        context,
        context.critic,
    )

    for value in frozen:
        with pytest.raises((AttributeError, TypeError)):
            # frozen dataclasses reject every set-attribute operation.
            value.__setattr__("policy_id", "mutated")
