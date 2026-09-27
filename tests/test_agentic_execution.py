from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.retrieval import RetrievedChunk
from responsible_agentic_workflows.workflow.agentic_execution import (
    AGENTIC_PROMPT_VERSION,
    format_evidence_context,
    path_reserve_satisfied_for_logging,
    selected_recovery_path_for_logging,
)
from responsible_agentic_workflows.workflow.control import (
    CriticControlState,
    EvidenceSufficiency,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryReasonCode,
    SupportStatus,
)


def _rc(cid: str, rank: int) -> RetrievedChunk:
    return RetrievedChunk(
        chunk=DocumentChunk(
            document_id=f"D-{cid}",
            chunk_id=cid,
            title="Synthetic",
            section="S",
            section_index=0,
            text=f"text-{cid}",
            source_file="synthetic.txt",
            page=rank,
        ),
        rank=rank,
        score=1.0 / rank,
    )


def _critic(sufficient=True, conflict=False):
    return CriticControlState(
        support_status=SupportStatus.PARTIAL_SUPPORT,
        evidence_sufficiency=(
            EvidenceSufficiency.SUFFICIENT
            if sufficient else EvidenceSufficiency.INSUFFICIENT
        ),
        unresolved_conflict=conflict,
        gap_types=(),
        release_ok=False,
    )


def _decision(action, reason=RecoveryReasonCode.HARD_LIMIT_BLOCKED):
    return RecoveryDecision(action=action, reason_code=reason, policy_id="p")


def test_prompt_version_is_provisional_shared_bundle():
    assert AGENTIC_PROMPT_VERSION == "agentic-engineering-v0.1"


def test_context_preserves_input_order_and_provenance():
    text = format_evidence_context((_rc("C2", 2), _rc("C1", 1)))
    assert text.index("chunk_id=C2") < text.index("chunk_id=C1")
    for value in ("document_id=D-C2", "page=2", "section=S", "text-C2"):
        assert value in text


def test_resource_stop_path_reconstruction():
    d = _decision(RecoveryAction.RESOURCE_STOP)
    assert selected_recovery_path_for_logging(
        decision=d, critic=_critic(True, False)
    ) is RecoveryPath.REVISE_ONLY
    assert selected_recovery_path_for_logging(
        decision=d, critic=_critic(False, False)
    ) is RecoveryPath.RERETRIEVE_REVISE


def test_direct_action_path_mapping():
    assert selected_recovery_path_for_logging(
        decision=_decision(RecoveryAction.ACCEPT), critic=_critic()
    ) is None
    assert selected_recovery_path_for_logging(
        decision=_decision(RecoveryAction.REVISE_ONLY), critic=_critic()
    ) is RecoveryPath.REVISE_ONLY


def test_g1_reserve_logging_semantics():
    blocked = _decision(
        RecoveryAction.RESOURCE_STOP,
        RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED,
    )
    ok = _decision(
        RecoveryAction.REVISE_ONLY,
        RecoveryReasonCode.G1_REVISE_ONLY,
    )
    hard = _decision(
        RecoveryAction.RESOURCE_STOP,
        RecoveryReasonCode.HARD_LIMIT_BLOCKED,
    )
    assert path_reserve_satisfied_for_logging(blocked) is False
    assert path_reserve_satisfied_for_logging(ok) is True
    assert path_reserve_satisfied_for_logging(hard) is None
