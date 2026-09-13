"""Deterministic recovery-cycle bookkeeping, query construction, and evidence merge.

Shared across the B1 and G1 LangGraph workflows. The functions in this module
are pure and perform zero LLM calls. The recovery query format and the
evidence-merge algorithm are frozen by the B1/G1 runtime contract (sections
29.5 and 29.6) and must not change without a contract revision.
"""

from __future__ import annotations

from dataclasses import dataclass

from responsible_agentic_workflows.retrieval.models import RetrievedChunk
from responsible_agentic_workflows.workflow.control import RecoveryAction

__all__ = [
    "MAX_RECOVERY_CYCLES",
    "RecoveryCycleState",
    "begin_recovery_cycle",
    "build_recovery_query",
    "mark_recovery_completed",
    "merge_evidence",
]

MAX_RECOVERY_CYCLES: int = 1


@dataclass(frozen=True, slots=True)
class RecoveryCycleState:
    """Immutable bookkeeping state for recovery-cycle bookkeeping."""

    recovery_iteration: int
    completed: bool


def begin_recovery_cycle(
    *,
    recovery_iteration: int,
    completed: bool = False,
    action: RecoveryAction,
) -> RecoveryCycleState:
    """Validate and advance recovery-cycle bookkeeping by one cycle.

    Raises ``ValueError`` if a second recovery cycle is attempted
    (``MAX_RECOVERY_CYCLES`` is 1 per run) or if the action is not a
    valid recovery path (``REVISE_ONLY`` or ``RERETRIEVE_REVISE``).
    """

    _recovery_actions = {RecoveryAction.REVISE_ONLY, RecoveryAction.RERETRIEVE_REVISE}

    if action not in _recovery_actions:
        raise ValueError(
            f"begin_recovery_cycle requires a recovery action, got {action!r}"
        )

    if recovery_iteration >= MAX_RECOVERY_CYCLES:
        raise ValueError(
            f"MAX_RECOVERY_CYCLES ({MAX_RECOVERY_CYCLES}) exceeded; "
            f"recovery_iteration is already {recovery_iteration}"
        )

    if completed:
        raise ValueError(
            "cannot begin a recovery cycle that has already completed"
        )

    return RecoveryCycleState(
        recovery_iteration=recovery_iteration + 1,
        completed=False,
    )


def mark_recovery_completed(state: RecoveryCycleState) -> RecoveryCycleState:
    """Return a new state with the recovery cycle marked completed."""

    if state.completed:
        raise ValueError("recovery cycle is already marked completed")

    return RecoveryCycleState(
        recovery_iteration=state.recovery_iteration,
        completed=True,
    )


def build_recovery_query(
    *,
    question: str,
    evidence_gaps: tuple[str, ...],
) -> str:
    """Construct a deterministic recovery-retrieval query.

    Frozen format (runtime contract 29.5):

    - If ``evidence_gaps`` is empty: return ``question`` unchanged.
    - Otherwise: ``question + "\\n\\nEvidence gaps:\\n"`` followed by one
      ``"\\n- <gap>"`` line per gap in the order reported by the critic.

    The literal strings ``Evidence gaps:`` and ``- `` are part of the frozen
    format and must appear verbatim. The ``question`` is always included
    unchanged and is never mutated.
    """

    if not isinstance(question, str) or not question.strip():
        raise ValueError("question must be a non-empty string")

    if not isinstance(evidence_gaps, tuple):
        raise ValueError("evidence_gaps must be a tuple of strings")

    if any(not isinstance(gap, str) for gap in evidence_gaps):
        raise ValueError("evidence_gaps entries must be strings")

    if not evidence_gaps:
        return question

    lines = [question, "", "Evidence gaps:"]
    for gap in evidence_gaps:
        lines.append(f"- {gap}")

    return "\n".join(lines)


def merge_evidence(
    *,
    current: tuple[RetrievedChunk, ...],
    recovery: tuple[RetrievedChunk, ...],
) -> tuple[RetrievedChunk, ...]:
    """Merge the current evidence context with recovery-retrieved chunks.

    Frozen algorithm (runtime contract 29.6):

    1. Retain the current evidence-context ordering unchanged.
    2. Iterate the recovery-retrieved chunks in their reported rank order
       (rank 1 first).
    3. For each recovery chunk, if its ``chunk_id`` is not already present
       in the current evidence context or earlier in the recovery traversal,
       append it at the end.
    4. If its ``chunk_id`` is already present, skip it. The first occurrence
       (the current-context copy, or the earlier recovery copy) wins.

    Forbidden behaviors: score fusion, reranking, reordering of the current
    context, duplicate ``chunk_id`` retention, condition-specific branching.
    """

    if not isinstance(current, tuple):
        raise ValueError("current must be a tuple of RetrievedChunk")

    if not isinstance(recovery, tuple):
        raise ValueError("recovery must be a tuple of RetrievedChunk")

    if any(not isinstance(chunk, RetrievedChunk) for chunk in current):
        raise ValueError("current entries must be RetrievedChunk instances")

    if any(not isinstance(chunk, RetrievedChunk) for chunk in recovery):
        raise ValueError("recovery entries must be RetrievedChunk instances")

    if not recovery:
        return current

    # Stable sort by reported rank so rank 1 is traversed first regardless of
    # the caller's input ordering.
    ranked = sorted(recovery, key=lambda chunk: chunk.rank)

    seen_ids = {chunk.chunk.chunk_id for chunk in current}
    appended = list[RetrievedChunk]()
    for chunk in ranked:
        chunk_id = chunk.chunk.chunk_id
        if chunk_id not in seen_ids:
            seen_ids.add(chunk_id)
            appended.append(chunk)

    return current + tuple(appended)
