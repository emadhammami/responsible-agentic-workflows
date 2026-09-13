"""Synthetic contract tests for the frozen G1 recovery policy."""

import dataclasses
import importlib

import pytest

import responsible_agentic_workflows.workflow.g1_policy as g1_policy_module
from responsible_agentic_workflows.workflow import (
    BlockedLimit,
    CriticControlState,
    EvidenceSufficiency,
    G1ERGRPolicy,
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

POLICY_ID = "g1-ergr-v0.1"


def _critic(
    *,
    release_ok: bool,
    evidence_sufficiency: EvidenceSufficiency,
    unresolved_conflict: bool = False,
    gap_types: tuple[GapType, ...] = (GapType.DRAFT_GROUNDING,),
    support_status: SupportStatus = SupportStatus.PARTIAL_SUPPORT,
) -> CriticControlState:
    return CriticControlState(
        support_status=support_status,
        evidence_sufficiency=evidence_sufficiency,
        unresolved_conflict=unresolved_conflict,
        gap_types=gap_types,
        release_ok=release_ok,
    )


def _snapshot(
    *,
    llm_calls_used: int = 1,
    retrieval_calls_used: int = 1,
    retries_used: int = 0,
    total_tokens_used: int = 700,
) -> ResourceSnapshot:
    output_tokens_used = min(200, total_tokens_used)
    return ResourceSnapshot(
        llm_calls_used=llm_calls_used,
        retrieval_calls_used=retrieval_calls_used,
        retries_used=retries_used,
        input_tokens_used=total_tokens_used - output_tokens_used,
        output_tokens_used=output_tokens_used,
        total_tokens_used=total_tokens_used,
    )


def _limits(
    *,
    max_llm_calls: int | None = 5,
    max_retrieval_calls: int | None = 3,
    max_retries: int | None = 3,
    max_total_tokens: int | None = 10000,
    timeout_ms: float | None = 60000.0,
) -> ResourceLimits:
    return ResourceLimits(
        max_llm_calls=max_llm_calls,
        max_retrieval_calls=max_retrieval_calls,
        max_retries=max_retries,
        max_total_tokens=max_total_tokens,
        timeout_ms=timeout_ms,
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
        resources=resources or _snapshot(),
        limits=limits or _limits(),
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


def _policy() -> G1ERGRPolicy:
    return G1ERGRPolicy(policy_id=POLICY_ID)


# Section A: constructor and protocol contract.


def test_a1_policy_id_valid() -> None:
    assert _policy().policy_id == POLICY_ID


def test_a2_policy_id_preserved_exactly() -> None:
    assert G1ERGRPolicy(policy_id="  padded id  ").policy_id == "  padded id  "


@pytest.mark.parametrize("invalid", ["", "   ", None, 42])
def test_a3_policy_id_invalid_raises(invalid: object) -> None:
    with pytest.raises(ValueError):
        G1ERGRPolicy(policy_id=invalid)  # type: ignore[arg-type]


def test_a4_protocol_conformance() -> None:
    assert isinstance(_policy(), RecoveryPolicy)


def test_a5_policy_is_frozen() -> None:
    policy = _policy()
    with pytest.raises(dataclasses.FrozenInstanceError):
        policy.policy_id = "other"  # type: ignore[misc]


# Section B: release_ok dominates every other check.


def test_b1_release_ok_accepts() -> None:
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    decision = _policy().decide(_context(critic, ()))

    assert decision.action is RecoveryAction.ACCEPT
    assert decision.reason_code is RecoveryReasonCode.RELEASE_OK
    assert decision.policy_id == POLICY_ID


def test_b2_release_ok_precedes_conflict_check() -> None:
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    decision = _policy().decide(_context(critic, ()))

    assert decision.action is RecoveryAction.ACCEPT
    assert decision.reason_code is RecoveryReasonCode.RELEASE_OK


def test_b3_release_ok_without_feasibility_entries() -> None:
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    decision = _policy().decide(_context(critic, ()))

    assert decision.action is RecoveryAction.ACCEPT


def test_b4_release_ok_with_exhausted_resources() -> None:
    critic = _critic(
        release_ok=True,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(),
    )

    decision = _policy().decide(
        _context(
            critic,
            (),
            resources=_snapshot(
                llm_calls_used=5, retrieval_calls_used=3, retries_used=3
            ),
            limits=_limits(max_total_tokens=700, timeout_ms=None),
        )
    )

    assert decision.action is RecoveryAction.ACCEPT
    assert decision.reason_code is RecoveryReasonCode.RELEASE_OK


def test_b5_release_ok_regardless_of_support_status() -> None:
    outcomes = set()
    for status in (
        SupportStatus.SUPPORTED,
        SupportStatus.PARTIAL_SUPPORT,
        SupportStatus.UNSUPPORTED,
    ):
        critic = _critic(
            release_ok=True,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            support_status=status,
        )
        outcomes.add(_policy().decide(_context(critic, ())))

    assert len(outcomes) == 1


# Section C: unresolved conflict abstains before feasibility or reserve.


def test_c1_conflict_sufficient_abstains() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.REVISE_ONLY),))
    )

    assert decision.action is RecoveryAction.ABSTAIN
    assert decision.reason_code is RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE


def test_c2_conflict_insufficient_recoverable_abstains() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT, GapType.MISSING_EVIDENCE),
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),))
    )

    assert decision.action is RecoveryAction.ABSTAIN
    assert decision.reason_code is RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE


def test_c3_conflict_without_feasibility_does_not_raise() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    decision = _policy().decide(_context(critic, ()))

    assert decision.action is RecoveryAction.ABSTAIN


def test_c4_conflict_with_exhausted_resources_does_not_raise() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=True,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    decision = _policy().decide(
        _context(
            critic,
            (),
            resources=_snapshot(llm_calls_used=5, retries_used=3),
            limits=_limits(max_llm_calls=5, max_retries=3),
        )
    )

    assert decision.action is RecoveryAction.ABSTAIN
    assert decision.reason_code is RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE


# Section D: SUFFICIENT without conflict selects REVISE_ONLY.


def test_d1_sufficient_nonconflict_revise_success() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.REVISE_ONLY),))
    )

    assert decision.action is RecoveryAction.REVISE_ONLY
    assert decision.reason_code is RecoveryReasonCode.G1_REVISE_ONLY
    assert decision.policy_id == POLICY_ID


@pytest.mark.parametrize(
    "gap_types",
    [
        (GapType.MISSING_EVIDENCE,),
        (GapType.INCOMPLETE_EVIDENCE,),
        (GapType.DRAFT_GROUNDING,),
        (GapType.MISSING_EVIDENCE, GapType.INCOMPLETE_EVIDENCE),
    ],
)
def test_d2_sufficient_with_any_gaps_still_revise(
    gap_types: tuple[GapType, ...],
) -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        gap_types=gap_types,
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.REVISE_ONLY),))
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_d3_revise_only_ignores_blocked_other_path() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )
    feasibility = (
        _feasible(RecoveryPath.REVISE_ONLY),
        _blocked(RecoveryPath.RERETRIEVE_REVISE),
    )

    decision = _policy().decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.REVISE_ONLY
    assert decision.reason_code is RecoveryReasonCode.G1_REVISE_ONLY


def test_d4_revise_only_ignores_support_status() -> None:
    outcomes = set()
    for status in (
        SupportStatus.SUPPORTED,
        SupportStatus.PARTIAL_SUPPORT,
        SupportStatus.UNSUPPORTED,
    ):
        critic = _critic(
            release_ok=False,
            evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
            support_status=status,
        )
        outcomes.add(

                _policy().decide(
                    _context(
                        critic, (_feasible(RecoveryPath.REVISE_ONLY),)
                    )
                )

        )

    assert len(outcomes) == 1


def test_d5_revise_only_requires_revise_feasibility_entry() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    with pytest.raises(ValueError, match="REVISE_ONLY"):
        _policy().decide(
            _context(critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),))
        )


# Section E: INSUFFICIENT with a retrieve signal selects RERETRIEVE_REVISE.


@pytest.mark.parametrize(
    "gap_types",
    [
        (GapType.MISSING_EVIDENCE,),
        (GapType.INCOMPLETE_EVIDENCE,),
        (GapType.DRAFT_GROUNDING, GapType.MISSING_EVIDENCE),
        (GapType.DRAFT_GROUNDING, GapType.INCOMPLETE_EVIDENCE),
    ],
)
def test_e1_insufficient_recoverable_selects_reretrieve(
    gap_types: tuple[GapType, ...],
) -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=gap_types,
    )

    decision = _policy().decide(
        _context(
            critic,
            (
                _blocked(RecoveryPath.REVISE_ONLY),
                _feasible(RecoveryPath.RERETRIEVE_REVISE),
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE
    assert decision.reason_code is RecoveryReasonCode.G1_RERETRIEVE_REVISE


def test_e2_reretrieve_revise_ignores_blocked_other_path() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.MISSING_EVIDENCE,),
    )
    feasibility = (
        _blocked(RecoveryPath.REVISE_ONLY),
        _feasible(RecoveryPath.RERETRIEVE_REVISE),
    )

    decision = _policy().decide(_context(critic, feasibility))

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE
    assert decision.reason_code is RecoveryReasonCode.G1_RERETRIEVE_REVISE


def test_e3_reretrieve_revise_requires_reretrieve_feasibility_entry() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.MISSING_EVIDENCE,),
    )

    with pytest.raises(ValueError, match="RERETRIEVE_REVISE"):
        _policy().decide(
            _context(critic, (_feasible(RecoveryPath.REVISE_ONLY),))
        )


def test_e4_reretrieve_revise_ignores_support_status() -> None:
    outcomes = set()
    for status in (
        SupportStatus.SUPPORTED,
        SupportStatus.PARTIAL_SUPPORT,
        SupportStatus.UNSUPPORTED,
    ):
        critic = _critic(
            release_ok=False,
            evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
            gap_types=(GapType.INCOMPLETE_EVIDENCE,),
            support_status=status,
        )
        outcomes.add(

                _policy().decide(
                    _context(
                        critic,
                        (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
                    )
                )

        )

    assert len(outcomes) == 1


# Section F: INSUFFICIENT without a retrieve signal abstains.


def test_f1_insufficient_no_gaps_abstains() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(),
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),))
    )

    assert decision.action is RecoveryAction.ABSTAIN
    assert decision.reason_code is RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE


def test_f2_insufficient_draft_grounding_only_abstains() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.DRAFT_GROUNDING,),
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),))
    )

    assert decision.action is RecoveryAction.ABSTAIN
    assert decision.reason_code is RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE


def test_f3_insufficient_evidence_conflict_gap_without_flag_abstains() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
        gap_types=(GapType.EVIDENCE_CONFLICT,),
    )

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),))
    )

    assert decision.action is RecoveryAction.ABSTAIN


def test_f4_abstain_without_feasibility_entries_does_not_raise() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(),
    )

    decision = _policy().decide(_context(critic, ()))

    assert decision.action is RecoveryAction.ABSTAIN


def test_f5_abstain_with_exhausted_resources_does_not_raise() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(),
    )

    decision = _policy().decide(
        _context(
            critic,
            (),
            resources=_snapshot(llm_calls_used=5, retries_used=3),
            limits=_limits(max_llm_calls=5, max_retries=3),
        )
    )

    assert decision.action is RecoveryAction.ABSTAIN


# Section G: hard feasibility gates dominate the reserve.


def test_g1_selected_revise_hard_blocked() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    decision = _policy().decide(
        _context(critic, (_blocked(RecoveryPath.REVISE_ONLY),))
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


def test_g2_selected_reretrieve_hard_blocked() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.MISSING_EVIDENCE,),
    )

    decision = _policy().decide(
        _context(critic, (_blocked(RecoveryPath.RERETRIEVE_REVISE),))
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


def test_g3_hard_block_precedes_reserve_block() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )

    decision = _policy().decide(
        _context(
            critic,
            (_blocked(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(llm_calls_used=5, retries_used=3),
            limits=_limits(max_llm_calls=5, max_retries=3),
        )
    )

    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED
    assert decision.action is RecoveryAction.RESOURCE_STOP


def test_g4_hard_block_reports_regardless_of_reserve_state() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.INCOMPLETE_EVIDENCE,),
    )

    decision = _policy().decide(
        _context(
            critic,
            (_blocked(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=5, retrieval_calls_used=3, retries_used=3
            ),
            limits=_limits(
                max_llm_calls=5, max_retrieval_calls=3, max_retries=3
            ),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


# Section H: REVISE_ONLY structural reserve (llm >= 2 and retries >= 1).


def _revise_critic() -> CriticControlState:
    return _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
    )


def test_h1_revise_reserve_boundary_passes() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(llm_calls_used=3, retries_used=2),
            limits=_limits(max_llm_calls=5, max_retries=3),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


@pytest.mark.parametrize(
    ("max_llm_calls", "llm_calls_used"),
    [(3, 3), (2, 1), (2, 2), (1, 0), (1, 1)],
)
def test_h2_revise_llm_remaining_below_two_blocks(
    max_llm_calls: int, llm_calls_used: int
) -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(llm_calls_used=llm_calls_used),
            limits=_limits(max_llm_calls=max_llm_calls),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED


def test_h3_revise_retries_exhausted_blocks() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(retries_used=3),
            limits=_limits(max_retries=3),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED


def test_h4_revise_disabled_llm_limit_passes() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(llm_calls_used=99),
            limits=_limits(max_llm_calls=None),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_h5_revise_disabled_retry_limit_passes() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(retries_used=99),
            limits=_limits(max_retries=None),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_h6_revise_disabled_limits_all_pass() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(llm_calls_used=99, retries_used=99),
            limits=_limits(max_llm_calls=None, max_retries=None),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_h7_revise_token_exhaustion_does_not_block() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(total_tokens_used=10000),
            limits=_limits(max_total_tokens=10000),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_h8_revise_timeout_absent_does_not_block() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            limits=_limits(timeout_ms=None),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


def test_h9_revise_reserve_block_beats_success_but_not_hard_block() -> None:
    feasible = _feasible(RecoveryPath.REVISE_ONLY)
    blocked = _blocked(RecoveryPath.REVISE_ONLY)
    exhausted = _context(
        _revise_critic(),
        (feasible,),
        resources=_snapshot(llm_calls_used=5, retries_used=3),
        limits=_limits(max_llm_calls=5, max_retries=3),
    )

    blocked_decision = _policy().decide(
        _context(
            _revise_critic(),
            (feasible,),
            resources=exhausted.resources,
            limits=exhausted.limits,
        )
    )
    hard_decision = _policy().decide(
        _context(
            _revise_critic(),
            (blocked,),
            resources=exhausted.resources,
            limits=exhausted.limits,
        )
    )

    assert blocked_decision.reason_code is (
        RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED
    )
    assert hard_decision.reason_code is RecoveryReasonCode.HARD_LIMIT_BLOCKED


# Section I: RERETRIEVE_REVISE structural reserve.


def _retrieve_critic() -> CriticControlState:
    return _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.MISSING_EVIDENCE,),
    )


def test_i1_retrieve_reserve_boundary_passes() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=3, retrieval_calls_used=2, retries_used=2
            ),
            limits=_limits(
                max_llm_calls=5, max_retrieval_calls=3, max_retries=3
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE
    assert decision.reason_code is RecoveryReasonCode.G1_RERETRIEVE_REVISE


@pytest.mark.parametrize("max_retrieval_calls", [1, 2, 3])
def test_i2_retrieve_exhausted_retrieval_blocks(
    max_retrieval_calls: int,
) -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(retrieval_calls_used=max_retrieval_calls),
            limits=_limits(max_retrieval_calls=max_retrieval_calls),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED


def test_i3_retrieve_llm_exhausted_blocks() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(llm_calls_used=5),
            limits=_limits(max_llm_calls=5),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED


def test_i4_retrieve_retries_exhausted_blocks() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(retries_used=3),
            limits=_limits(max_retries=3),
        )
    )

    assert decision.action is RecoveryAction.RESOURCE_STOP
    assert decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED


def test_i5_retrieve_disabled_limits_all_pass() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=99, retrieval_calls_used=99, retries_used=99
            ),
            limits=_limits(
                max_llm_calls=None,
                max_retrieval_calls=None,
                max_retries=None,
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_i6_retrieve_partial_disable_mixed() -> None:
    enabled = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=3, retrieval_calls_used=99, retries_used=2
            ),
            limits=_limits(
                max_llm_calls=5, max_retrieval_calls=None, max_retries=3
            ),
        )
    )
    disabled = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=99, retrieval_calls_used=2, retries_used=99
            ),
            limits=_limits(max_llm_calls=None, max_retrieval_calls=3),
        )
    )

    assert enabled.action is RecoveryAction.RERETRIEVE_REVISE
    assert disabled.action is RecoveryAction.RESOURCE_STOP


def test_i7_retrieve_token_exhaustion_does_not_block() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(total_tokens_used=10000),
            limits=_limits(max_total_tokens=10000),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_i8_retrieve_timeout_value_does_not_block() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            limits=_limits(timeout_ms=1.0),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_i9_revise_path_never_checks_retrieval_reserve() -> None:
    decision = _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            resources=_snapshot(retrieval_calls_used=3),
            limits=_limits(max_retrieval_calls=3),
        )
    )

    assert decision.action is RecoveryAction.REVISE_ONLY


# Section J: token and timeout invariance.


def test_j1_token_usage_invariance() -> None:
    critic = _revise_critic()
    feasibility = (_feasible(RecoveryPath.REVISE_ONLY),)

    first = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=_snapshot(total_tokens_used=100),
            limits=_limits(max_total_tokens=10000),
        )
    )
    second = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=_snapshot(total_tokens_used=9999),
            limits=_limits(max_total_tokens=10000),
        )
    )

    assert first == second


def test_j2_token_limit_invariance() -> None:
    critic = _retrieve_critic()
    feasibility = (_feasible(RecoveryPath.RERETRIEVE_REVISE),)

    first = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=_snapshot(total_tokens_used=700),
            limits=_limits(max_total_tokens=10000),
        )
    )
    second = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=_snapshot(total_tokens_used=700),
            limits=_limits(max_total_tokens=500),
        )
    )

    assert first == second


def test_j3_timeout_invariance() -> None:
    critic = _revise_critic()
    feasibility = (_feasible(RecoveryPath.REVISE_ONLY),)

    first = _policy().decide(
        _context(
            critic,
            feasibility,
            limits=_limits(timeout_ms=60000.0),
        )
    )
    second = _policy().decide(
        _context(
            critic,
            feasibility,
            limits=_limits(timeout_ms=None),
        )
    )

    assert first == second


def test_j4_snapshot_token_split_irrelevant() -> None:
    critic = _retrieve_critic()
    feasibility = (_feasible(RecoveryPath.RERETRIEVE_REVISE),)

    first = _policy().decide(
        _context(critic, feasibility, resources=_snapshot(total_tokens_used=1))
    )
    second = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=_snapshot(
                llm_calls_used=1,
                retrieval_calls_used=1,
                retries_used=0,
                total_tokens_used=1,
            ),
        )
    )

    assert first == second


# Section K: source isolation and treatment separation.


def test_k1_g1_module_imports_only_control() -> None:
    module = importlib.import_module(g1_policy_module.__name__)
    source = module.__file__
    with open(source, encoding="utf-8") as handle:
        text = handle.read()

    for forbidden in (
        "b0_baseline",
        "b1_policy",
        "from .critic",
        "calculate_hard_recovery_feasibility",
        "modeling",
        "logging",
        "benchmark",
        "corpus",
    ):
        assert forbidden not in text


def test_k2_g1_does_not_reexport_forbidden_symbols() -> None:
    for name in (
        "B0Baseline",
        "B0Result",
        "B1FixedRecoveryPolicy",
        "StructuredCritic",
        "parse_critic_result",
        "calculate_hard_recovery_feasibility",
    ):
        assert not hasattr(g1_policy_module, name)


def test_k3_repeated_decisions_do_not_mutate_state() -> None:
    critic = _retrieve_critic()
    context = _context(
        critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),)
    )
    policy = _policy()

    before = dataclasses.astuple(context)

    first = policy.decide(context)
    for _ in range(3):
        assert policy.decide(context) == first

    assert dataclasses.astuple(context) == before


def test_k4_g1_abstains_where_b1_would_reretrieve() -> None:
    from responsible_agentic_workflows.workflow import B1FixedRecoveryPolicy

    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        gap_types=(GapType.DRAFT_GROUNDING,),
    )
    feasibility = (
        _feasible(RecoveryPath.REVISE_ONLY),
        _feasible(RecoveryPath.RERETRIEVE_REVISE),
    )
    context = _context(critic, feasibility)

    b1 = B1FixedRecoveryPolicy(policy_id="b1-fixed-v0.1")
    g1 = G1ERGRPolicy(policy_id=POLICY_ID)

    assert b1.decide(context).action is RecoveryAction.RERETRIEVE_REVISE
    assert g1.decide(context).action is RecoveryAction.ABSTAIN


# Section L: determinism and immutability.


def test_l1_deterministic_repeated_calls() -> None:
    critic = _revise_critic()
    context = _context(
        critic,
        (
            _feasible(RecoveryPath.REVISE_ONLY),
            _feasible(RecoveryPath.RERETRIEVE_REVISE),
        ),
    )
    policy = _policy()

    first = policy.decide(context)

    for _ in range(5):
        assert policy.decide(context) == first


def test_l2_decision_instance_is_immutable() -> None:
    critic = _revise_critic()

    decision = _policy().decide(
        _context(critic, (_feasible(RecoveryPath.REVISE_ONLY),))
    )

    with pytest.raises(dataclasses.FrozenInstanceError):
        decision.action = RecoveryAction.ABSTAIN  # type: ignore[misc]


def test_l3_independent_instances_agree() -> None:
    critic = _retrieve_critic()
    context = _context(
        critic, (_feasible(RecoveryPath.RERETRIEVE_REVISE),)
    )

    assert G1ERGRPolicy(policy_id="a").decide(context).action == (
        RecoveryAction.RERETRIEVE_REVISE
    )
    assert G1ERGRPolicy(policy_id="b").decide(context).action == (
        RecoveryAction.RERETRIEVE_REVISE
    )


def test_l4_decide_returns_recovery_decision() -> None:
    critic = _critic(release_ok=True, evidence_sufficiency=
                     EvidenceSufficiency.SUFFICIENT)

    decision = _policy().decide(_context(critic, ()))

    assert isinstance(decision, RecoveryDecision)

# Additional frozen-contract verification coverage.


def test_e5_evidence_conflict_gap_does_not_override_retrieval_signal() -> None:
    critic = _critic(
        release_ok=False,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
        gap_types=(
            GapType.EVIDENCE_CONFLICT,
            GapType.MISSING_EVIDENCE,
        ),
    )

    decision = _policy().decide(
        _context(
            critic,
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE
    assert decision.reason_code is RecoveryReasonCode.G1_RERETRIEVE_REVISE


def test_i10_reretrieve_disabled_llm_dimension_independently_passes() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=999,
                retrieval_calls_used=2,
                retries_used=2,
            ),
            limits=_limits(
                max_llm_calls=None,
                max_retrieval_calls=3,
                max_retries=3,
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_i11_reretrieve_disabled_retrieval_dimension_independently_passes() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=3,
                retrieval_calls_used=999,
                retries_used=2,
            ),
            limits=_limits(
                max_llm_calls=5,
                max_retrieval_calls=None,
                max_retries=3,
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_i12_reretrieve_disabled_retry_dimension_independently_passes() -> None:
    decision = _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=_snapshot(
                llm_calls_used=3,
                retrieval_calls_used=2,
                retries_used=999,
            ),
            limits=_limits(
                max_llm_calls=5,
                max_retrieval_calls=3,
                max_retries=None,
            ),
        )
    )

    assert decision.action is RecoveryAction.RERETRIEVE_REVISE


def test_j5_max_total_tokens_none_is_irrelevant_to_g1_reserve() -> None:
    critic = _revise_critic()
    feasibility = (_feasible(RecoveryPath.REVISE_ONLY),)
    resources = _snapshot(total_tokens_used=700)

    configured = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=resources,
            limits=_limits(max_total_tokens=1),
        )
    )

    disabled = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=resources,
            limits=_limits(max_total_tokens=None),
        )
    )

    assert configured == disabled
    assert configured.action is RecoveryAction.REVISE_ONLY


def test_j6_token_input_output_composition_is_irrelevant() -> None:
    critic = _retrieve_critic()
    feasibility = (_feasible(RecoveryPath.RERETRIEVE_REVISE),)

    mostly_input = ResourceSnapshot(
        llm_calls_used=1,
        retrieval_calls_used=1,
        retries_used=0,
        input_tokens_used=999,
        output_tokens_used=1,
        total_tokens_used=1000,
    )

    mostly_output = ResourceSnapshot(
        llm_calls_used=1,
        retrieval_calls_used=1,
        retries_used=0,
        input_tokens_used=1,
        output_tokens_used=999,
        total_tokens_used=1000,
    )

    first = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=mostly_input,
        )
    )

    second = _policy().decide(
        _context(
            critic,
            feasibility,
            resources=mostly_output,
        )
    )

    assert first == second
    assert first.action is RecoveryAction.RERETRIEVE_REVISE


def test_k5_recovery_iteration_is_not_a_treatment_input() -> None:
    critic = _retrieve_critic()

    base = _context(
        critic,
        (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
    )

    iteration_zero = dataclasses.replace(
        base,
        recovery_iteration=0,
    )

    iteration_later = dataclasses.replace(
        base,
        recovery_iteration=7,
    )

    first = _policy().decide(iteration_zero)
    second = _policy().decide(iteration_later)

    assert first == second
    assert first.action is RecoveryAction.RERETRIEVE_REVISE


def test_k6_source_excludes_nonfrozen_policy_inputs_and_side_effects() -> None:
    source_path = g1_policy_module.__file__
    assert source_path is not None

    with open(source_path, encoding="utf-8") as handle:
        source = handle.read()

    forbidden = (
        "timeout_ms",
        "total_tokens_remaining",
        "recovery_iteration",
        "unsupported_claims",
        "incomplete_support",
        "evidence_gaps",
        ".explanation",
        "raw_question",
        "question_text",
        "gold_answer",
        "reference_answer",
        "benchmark_score",
        "human_adjudication",
        "record_event",
        "RunRecorder",
        "logger",
        "logging",
        "retriever",
        ".generate(",
        "time.time",
        "time.monotonic",
        "time.perf_counter",
        "datetime.now",
        "clock_gettime",
        "process_time",
        "os.environ",
        "getenv(",
        "random.",
    )

    for token in forbidden:
        assert token not in source


def test_k7_source_does_not_recompute_shared_hard_feasibility() -> None:
    source_path = g1_policy_module.__file__
    assert source_path is not None

    with open(source_path, encoding="utf-8") as handle:
        source = handle.read()

    assert "calculate_hard_recovery_feasibility" not in source
    assert "from .feasibility" not in source


def test_l5_resource_snapshot_remains_exactly_unchanged() -> None:
    resources = _snapshot(
        llm_calls_used=1,
        retrieval_calls_used=1,
        retries_used=0,
        total_tokens_used=777,
    )

    before = dataclasses.astuple(resources)

    _policy().decide(
        _context(
            _retrieve_critic(),
            (_feasible(RecoveryPath.RERETRIEVE_REVISE),),
            resources=resources,
        )
    )

    assert dataclasses.astuple(resources) == before


def test_l6_resource_limits_remain_exactly_unchanged() -> None:
    limits = _limits(
        max_llm_calls=5,
        max_retrieval_calls=3,
        max_retries=2,
        max_total_tokens=9000,
        timeout_ms=1234.0,
    )

    before = dataclasses.astuple(limits)

    _policy().decide(
        _context(
            _revise_critic(),
            (_feasible(RecoveryPath.REVISE_ONLY),),
            limits=limits,
        )
    )

    assert dataclasses.astuple(limits) == before


def test_l7_feasibility_entry_remains_exactly_unchanged() -> None:
    feasibility = _feasible(RecoveryPath.REVISE_ONLY)
    before = dataclasses.astuple(feasibility)

    _policy().decide(
        _context(
            _revise_critic(),
            (feasibility,),
        )
    )

    assert dataclasses.astuple(feasibility) == before
