"""Shared prospective execution helpers for B1/G1 agentic workflows."""

from __future__ import annotations

from responsible_agentic_workflows.modeling import ModelMessage, ModelRequest
from responsible_agentic_workflows.retrieval import RetrievedChunk

from .control import (
    CriticControlState,
    CriticResult,
    EvidenceSufficiency,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryReasonCode,
)

AGENTIC_PROMPT_VERSION = "agentic-engineering-v0.1"

_PLAN_SYSTEM = (
    "Create a concise execution plan for answering the question from "
    "document evidence. Do not answer the question or invent facts."
)
_DRAFT_SYSTEM = (
    "Answer using only the supplied document evidence. Use the execution "
    "plan only as organizational guidance. Do not invent unsupported facts."
)
_REVISE_SYSTEM = (
    "Revise the current answer using only the supplied document evidence "
    "and critic diagnostics. Do not invent unsupported facts."
)


def format_evidence_context(
    evidence: tuple[RetrievedChunk, ...],
) -> str:
    """Format evidence deterministically without reordering it."""
    if not isinstance(evidence, tuple):
        raise ValueError("evidence must be a tuple")

    blocks: list[str] = []
    for item in evidence:
        if not isinstance(item, RetrievedChunk):
            raise ValueError("evidence entries must be RetrievedChunk")
        c = item.chunk
        blocks.append(
            f"[rank={item.rank}; score={item.score!r}; "
            f"document_id={c.document_id}; chunk_id={c.chunk_id}; "
            f"page={c.page}; section={c.section}]\n{c.text}"
        )
    return "\n\n".join(blocks) if blocks else "[NO RETRIEVED EVIDENCE]"


def build_plan_request(
    *,
    question: str,
    temperature: float | None,
    max_output_tokens: int | None,
) -> ModelRequest:
    return ModelRequest(
        messages=(
            ModelMessage(role="system", content=_PLAN_SYSTEM),
            ModelMessage(role="user", content=f"QUESTION\n{question}"),
        ),
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )


def build_draft_request(
    *,
    question: str,
    plan: str,
    evidence: tuple[RetrievedChunk, ...],
    temperature: float | None,
    max_output_tokens: int | None,
) -> ModelRequest:
    context = format_evidence_context(evidence)
    return ModelRequest(
        messages=(
            ModelMessage(role="system", content=_DRAFT_SYSTEM),
            ModelMessage(
                role="user",
                content=(
                    f"QUESTION\n{question}\n\nPLAN\n{plan}\n\n"
                    f"EVIDENCE\n{context}"
                ),
            ),
        ),
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )


def format_critic_diagnostics(result: CriticResult) -> str:
    return (
        f"support_status={result.support_status.value}\n"
        f"evidence_sufficiency={result.evidence_sufficiency.value}\n"
        f"unresolved_conflict={result.unresolved_conflict}\n"
        f"gap_types={[x.value for x in result.gap_types]}\n"
        f"unsupported_claims={list(result.unsupported_claims)}\n"
        f"incomplete_support={list(result.incomplete_support)}\n"
        f"evidence_gaps={list(result.evidence_gaps)}"
    )


def build_revision_request(
    *,
    question: str,
    plan: str,
    current_answer: str,
    evidence: tuple[RetrievedChunk, ...],
    critic_result: CriticResult,
    temperature: float | None,
    max_output_tokens: int | None,
) -> ModelRequest:
    return ModelRequest(
        messages=(
            ModelMessage(role="system", content=_REVISE_SYSTEM),
            ModelMessage(
                role="user",
                content=(
                    f"QUESTION\n{question}\n\nPLAN\n{plan}\n\n"
                    f"CURRENT ANSWER\n{current_answer}\n\n"
                    f"EVIDENCE\n{format_evidence_context(evidence)}\n\n"
                    f"CRITIC DIAGNOSTICS\n"
                    f"{format_critic_diagnostics(critic_result)}"
                ),
            ),
        ),
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )


def selected_recovery_path_for_logging(
    *,
    decision: RecoveryDecision,
    critic: CriticControlState,
) -> RecoveryPath | None:
    if decision.action in {RecoveryAction.ACCEPT, RecoveryAction.ABSTAIN}:
        return None
    if decision.action is RecoveryAction.REVISE_ONLY:
        return RecoveryPath.REVISE_ONLY
    if decision.action is RecoveryAction.RERETRIEVE_REVISE:
        return RecoveryPath.RERETRIEVE_REVISE

    if (
        critic.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT
        and not critic.unresolved_conflict
    ):
        return RecoveryPath.REVISE_ONLY
    return RecoveryPath.RERETRIEVE_REVISE


def path_reserve_satisfied_for_logging(
    decision: RecoveryDecision,
) -> bool | None:
    if decision.reason_code is RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED:
        return False
    if decision.reason_code in {
        RecoveryReasonCode.G1_REVISE_ONLY,
        RecoveryReasonCode.G1_RERETRIEVE_REVISE,
    }:
        return True
    return None
