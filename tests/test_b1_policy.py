import pytest

from responsible_agentic_workflows.workflow import (
    B1FixedRecoveryPolicy,
    BlockedLimit,
    CriticControlState,
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
)

POLICY_ID = "b1-fixed-v0.1"


def _critic(
    *,
    release_ok: bool,
    evidence_sufficiency: EvidenceSufficiency,
    unresolved_conflict: bool,
) -> CriticControlState:
    return CriticControlState(
        support_status=SupportStatus.PARTIAL_SUPPORT,
        evidence_sufficiency=evidence_sufficiency,
        unresolved_conflict=unresolved_conflict,
        gap_types=(GapType.DRAFT_GROUNDING,),
        release_ok=release_ok,
    )


def _snapshot(
    *,
    llm_calls_used: int = 1,
    retrieval_calls_used: int = 1,
    total_tokens_used: int = 700,
) -> ResourceSnapshot:
    return ResourceSnapshot(
        llm_calls_used=llm_calls_used,
        retrieval_calls_used=retrieval_calls_used,
        retries_used=0,
        input_tokens_used=total_tokens_used - 200,
        output_tokens_used=200,
        total_tokens_used=total_tokens_used,
    )


def _context(
    critic: CriticControlState,
    feasibility: tuple[HardRecoveryFeasibility, ...],
    resources: ResourceSnapshot | None = None,
    limits: ResourceLimits | None = None,
) -> RecoveryPolicyContext:
    return RecoveryPolicyContext(
        critic=critic,
        recovery_iteration=1,
        resources=resources
        or _snapshot(),
        limits=limits
        or ResourceLimits(
            max_llm_calls=4,
            max_retrieval_calls=2,
            max_retries=2,
            max_total_tokens=2000,
            timeout_ms=60000.0,
        ),
        hard_recovery_feasibility=feasibility,
    )


def _feasible(path: RecoveryPath) -> HardRecoveryFeasibility:
    return HardRecoveryFeasibility(recovery_path=path, feasible=True)


def _blocked(path: RecoveryPath) -> HardRecoveryFeasibility:
    return HardRecoveryFeasibility(
        recovery_path=path,
        feasible=False,
        blocked_limits=(BlockedLimit.TOKEN_LIMIT,),
    )


def test_policy_id_validation() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    assert policy.policy_id == POLICY_ID

    preserved = B1FixedRecoveryPolicy(policy_id="  padded id  ")
    assert preserved.policy_id == "  padded id  "

    for invalid in ("", "   ", None, 42):
        with pytest.raises(ValueError):
            B1FixedRecoveryPolicy(policy_id=invalid)


def test_protocol_conformance() -> None:
    assert isinstance(B1FixedRecoveryPolicy(policy_id=POLICY_ID), RecoveryPolicy)


def test_release_ok_accept_even_without_feasibility() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )

    decision = policy.decide(_context(critic, feasibility=()))

    assert decision.action is RecoveryAction.ACCEPT
    assert decision.reason_code is RecoveryReasonCode.RELEASE_OK
    assert decision.policy_id == POLICY_ID


def test_release_ok_precedes_recoverability_feasibility() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=True,
    )

    decision = policy.decide(_context(critic, feasibility=()))

    assert decision.action is RecoveryAction.ACCEPT
    assert decision.reason_code is RecoveryReasonCode.RELEASE_OK


def test_revise_only_mapping() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    feasibility = (_feasible(RecoveryPath.REVISE_ONLY),)

    decision = policy.decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.REVISE_ONLY
    assert decision.reason_code is RecoveryReasonCode.B1_FIXED_REVISE_ONLY
    assert decision.policy_id == POLICY_ID


@pytest.mark.parametrize(
    "evidence_sufficiency,unresolved_conflict",
    [
        (EvidenceSufficiency.INSUFFICIENT, False),
        (EvidenceSufficiency.SUFFICIENT, True),
        (EvidenceSufficiency.INSUFFICIENT, True),
    ],
)
def test_reretrieve_revise_mapping(
    evidence_sufficiency: EvidenceSufficiency,
    unresolved_conflict: bool,
) -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=evidence_sufficiency,
        unresolved_conflict=unresolved_conflict,
    )
    feasibility = (_feasible(RecoveryPath.RERETRIEVE_REVISE),)

    decision = policy.decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE
    assert decision.reason_code is (
        RecoveryReasonCode.B1_FIXED_RERETRIEVE_REVISE
    )
    assert decision.policy_id == POLICY_ID


def test_selected_revise_only_hard_blocked() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    feasibility = (_blocked(RecoveryPath.REVISE_ONLY),)

    decision = policy.decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


def test_selected_reretrieve_revise_hard_blocked() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
    )
    feasibility = (_blocked(RecoveryPath.RERETRIEVE_REVISE),)

    decision = policy.decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


def test_other_path_feasibility_does_not_control_decision() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    # Selected path is REVISE_ONLY (feasible); the other path is blocked.
    feasibility = (
        _feasible(RecoveryPath.REVISE_ONLY),
        _blocked(RecoveryPath.RERETRIEVE_REVISE),
    )

    decision = policy.decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.REVISE_ONLY
    assert decision.reason_code is RecoveryReasonCode.B1_FIXED_REVISE_ONLY


def test_missing_selected_path_feasibility_raises() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)

    # Selected path is REVISE_ONLY, but only RERETRIEVE_REVISE is present.
    revise_critics = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    with pytest.raises(ValueError, match="REVISE_ONLY"):
        policy.decide(
            _context(
                revise_critics,
                (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            )
        )

    # Selected path is RERETRIEVE_REVISE, but only REVISE_ONLY is present.
    reretrieve_critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
    )
    with pytest.raises(ValueError, match="RERETRIEVE_REVISE"):
        policy.decide(
            _context(
                reretrieve_critic,
                (_feasible(RecoveryPath.REVISE_ONLY),),
            )
        )


def test_b1_never_abstains() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    cases = [
        (
            _critic(
                release_ok=True,
                evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
                unresolved_conflict=False,
            ),
            (),
        ),
        (
            _critic(
                release_ok=False,
                evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
                unresolved_conflict=False,
            ),
            (_feasible(RecoveryPath.REVISE_ONLY),),
        ),
        (
            _critic(
                release_ok=False,
                evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
                unresolved_conflict=False,
            ),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
        ),
        (
            _critic(
                release_ok=False,
                evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
                unresolved_conflict=True,
            ),
            (
                _blocked(RecoveryPath.REVISE_ONLY),
                _feasible(RecoveryPath.RERETRIEVE_REVISE),
            ),
        ),
    ]

    for critic, feasibility in cases:
        decision = policy.decide(_context(critic, feasibility))
        assert decision.action is not RecoveryAction.ABSTAIN


def test_resource_invariance() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    feasibility = (_feasible(RecoveryPath.REVISE_ONLY),)

    context_a = _context(
        critic,
        feasibility,
        resources=_snapshot(
            llm_calls_used=1, retrieval_calls_used=1, total_tokens_used=300
        ),
        limits=ResourceLimits(
            max_llm_calls=4,
            max_retrieval_calls=2,
            max_retries=2,
            max_total_tokens=1000,
            timeout_ms=60000.0,
        ),
    )

    context_b = _context(
        critic,
        feasibility,
        resources=_snapshot(
            llm_calls_used=4,
            retrieval_calls_used=2,
            total_tokens_used=9999,
        ),
        limits=ResourceLimits(
            max_llm_calls=None,
            max_retrieval_calls=None,
            max_retries=None,
            max_total_tokens=None,
            timeout_ms=None,
        ),
    )

    assert policy.decide(context_a) == policy.decide(context_b)


def test_policy_id_preserved_exactly() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )

    decision = policy.decide(_context(critic, feasibility=()))

    assert decision.policy_id == POLICY_ID


def test_deterministic_repeated_calls() -> None:
    policy = B1FixedRecoveryPolicy(policy_id=POLICY_ID)
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )
    context = _context(
        critic, (_feasible(RecoveryPath.REVISE_ONLY),)
    )

    first = policy.decide(context)
    for _ in range(3):
        assert policy.decide(context) == first

    assert isinstance(first, RecoveryDecision)
