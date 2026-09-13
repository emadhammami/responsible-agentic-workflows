from __future__ import annotations

import pytest

from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.retrieval.models import RetrievedChunk
from responsible_agentic_workflows.workflow import (
    MAX_RECOVERY_CYCLES,
    RecoveryAction,
    RecoveryCycleState,
    begin_recovery_cycle,
    build_recovery_query,
    mark_recovery_completed,
    merge_evidence,
)


def _chunk(chunk_id: str) -> DocumentChunk:
    return DocumentChunk(
        document_id=f"doc-{chunk_id}",
        chunk_id=chunk_id,
        title=f"title-{chunk_id}",
        section="s",
        section_index=0,
        text=f"text-{chunk_id}",
        source_file="src.txt",
        page=1,
    )


def _rc(chunk_id: str, rank: int) -> RetrievedChunk:
    return RetrievedChunk(chunk=_chunk(chunk_id), rank=rank, score=1.0 / rank)


def test_max_recovery_cycles_is_one() -> None:
    assert MAX_RECOVERY_CYCLES == 1


def test_build_recovery_query_empty_gaps_returns_question_unchanged() -> None:
    assert build_recovery_query(question="Q", evidence_gaps=()) == "Q"


def test_build_recovery_query_exact_frozen_format_with_gaps() -> None:
    out = build_recovery_query(question="Q", evidence_gaps=("g1", "g2"))
    expected = "Q\n\nEvidence gaps:\n- g1\n- g2"
    assert out == expected
    # The frozen literal markers must appear verbatim.
    assert "Evidence gaps:" in out
    assert "- g1" in out
    assert "- g2" in out
    # The question is always included unchanged at the start.
    assert out.startswith("Q\n\n")
    # Single blank line separator before the "Evidence gaps:" header.
    assert "\n\n" in out


def test_build_recovery_query_preserves_gap_order() -> None:
    out = build_recovery_query(question="Q", evidence_gaps=("z", "a", "m"))
    assert out.index("- z") < out.index("- a") < out.index("- m")


def test_build_recovery_query_single_gap() -> None:
    out = build_recovery_query(question="Q", evidence_gaps=("only",))
    assert out == "Q\n\nEvidence gaps:\n- only"


def test_build_recovery_query_rejects_blank_question() -> None:
    with pytest.raises(ValueError, match="question"):
        build_recovery_query(question="", evidence_gaps=())
    with pytest.raises(ValueError, match="question"):
        build_recovery_query(question="   ", evidence_gaps=())


def test_build_recovery_query_rejects_non_tuple_gaps() -> None:
    with pytest.raises(ValueError, match="tuple"):
        build_recovery_query(question="Q", evidence_gaps=["x"])  # type: ignore[arg-type]


def test_build_recovery_query_rejects_non_string_gap() -> None:
    with pytest.raises(ValueError, match="string"):
        build_recovery_query(question="Q", evidence_gaps=("ok", 42))  # type: ignore[arg-type]


def test_merge_evidence_appends_unseen_and_preserves_order() -> None:
    current = (_rc("a", 1), _rc("b", 2))
    recovery = (_rc("c", 1), _rc("d", 2))
    out = merge_evidence(current=current, recovery=recovery)
    assert [c.chunk.chunk_id for c in out] == ["a", "b", "c", "d"]
    # Current-order prefix is intact (no reordering).
    assert out[:2] == current


def test_merge_evidence_first_occurrence_wins() -> None:
    current = (_rc("a", 1), _rc("b", 2))
    # "b" is a duplicate (first-occurrence-wins); "c" is new.
    recovery = (_rc("b", 1), _rc("c", 2))
    out = merge_evidence(current=current, recovery=recovery)
    ids = [c.chunk.chunk_id for c in out]
    assert ids == ["a", "b", "c"]
    # The surviving "b" is the *current-context* copy (rank 2).
    b = next(c for c in out if c.chunk.chunk_id == "b")
    assert b.rank == 2
    # No duplicate chunk_id survives.
    assert len(set(ids)) == len(ids)


def test_merge_evidence_ignores_score_and_rank_for_dedupe() -> None:
    current = (_rc("a", 5),)
    # A recovery chunk with chunk_id "a" but a *higher* score must NOT
    # replace the current copy (no score fusion, no reranking).
    higher_score_dup = RetrievedChunk(chunk=_chunk("a"), rank=1, score=99.0)
    other = _rc("b", 2)
    out = merge_evidence(current=current, recovery=(higher_score_dup, other))
    ids = [c.chunk.chunk_id for c in out]
    assert ids == ["a", "b"]
    assert out[0].rank == 5  # current copy retained, not the high-score dup


def test_merge_evidence_empty_recovery_returns_current_unchanged() -> None:
    current = (_rc("a", 1),)
    out = merge_evidence(current=current, recovery=())
    assert out == current


def test_merge_evidence_empty_current_appends_recovery() -> None:
    recovery = (_rc("c", 1), _rc("d", 2))
    out = merge_evidence(current=(), recovery=recovery)
    assert [c.chunk.chunk_id for c in out] == ["c", "d"]


def test_merge_evidence_traverses_recovery_in_rank_order() -> None:
    current = (_rc("a", 1),)
    # Provided out of rank order: rank 3 first, rank 1 second, rank 2 third.
    recovery = (_rc("c", 3), _rc("b", 1), _rc("d", 2))
    out = merge_evidence(current=current, recovery=recovery)
    assert [c.chunk.chunk_id for c in out] == ["a", "b", "d", "c"]


def test_merge_evidence_dedupes_within_recovery_first_rank_wins() -> None:
    current = (_rc("a", 1),)
    # Two recovery entries share chunk_id "c"; the lower rank (1) must win.
    winner = _rc("c", 1)
    loser = _rc("c", 2)
    out = merge_evidence(current=current, recovery=(loser, winner))
    ids = [c.chunk.chunk_id for c in out]
    assert ids == ["a", "c"]
    c = next(x for x in out if x.chunk.chunk_id == "c")
    assert c.rank == 1


def test_merge_evidence_does_not_mutate_inputs() -> None:
    current = (_rc("a", 1), _rc("b", 2))
    recovery = (_rc("c", 1), _rc("b", 2))
    current_before = [
        (c.chunk.chunk_id, c.rank, c.score) for c in current
    ]
    recovery_before = [
        (c.chunk.chunk_id, c.rank, c.score) for c in recovery
    ]
    merge_evidence(current=current, recovery=recovery)
    assert [
        (c.chunk.chunk_id, c.rank, c.score) for c in current
    ] == current_before
    assert [
        (c.chunk.chunk_id, c.rank, c.score) for c in recovery
    ] == recovery_before
    assert len(current) == 2
    assert len(recovery) == 2


def test_merge_evidence_rejects_non_tuple_and_non_chunk() -> None:
    with pytest.raises(ValueError, match="tuple"):
        merge_evidence(current=[_rc("a", 1)], recovery=())  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="recovery must be a tuple"):
        merge_evidence(current=(), recovery="nope")  # type: ignore[arg-type]


def test_begin_recovery_cycle_advances_iteration_once() -> None:
    state = begin_recovery_cycle(
        recovery_iteration=0,
        action=RecoveryAction.REVISE_ONLY,
    )
    assert state == RecoveryCycleState(recovery_iteration=1, completed=False)


def test_begin_recovery_cycle_works_for_reretrieve_revise() -> None:
    state = begin_recovery_cycle(
        recovery_iteration=0,
        action=RecoveryAction.RERETRIEVE_REVISE,
    )
    assert state.recovery_iteration == 1
    assert state.completed is False


def test_begin_recovery_cycle_rejects_second_cycle() -> None:
    with pytest.raises(ValueError, match="MAX_RECOVERY_CYCLES"):
        begin_recovery_cycle(
            recovery_iteration=1,
            action=RecoveryAction.REVISE_ONLY,
        )


def test_begin_recovery_cycle_rejects_non_recovery_actions() -> None:
    for action in (
        RecoveryAction.ACCEPT,
        RecoveryAction.ABSTAIN,
        RecoveryAction.RESOURCE_STOP,
    ):
        with pytest.raises(ValueError, match="recovery action"):
            begin_recovery_cycle(recovery_iteration=0, action=action)


def test_begin_recovery_cycle_rejects_already_completed() -> None:
    with pytest.raises(ValueError, match="already completed"):
        begin_recovery_cycle(
            recovery_iteration=0,
            completed=True,
            action=RecoveryAction.REVISE_ONLY,
        )


def test_mark_recovery_completed_sets_flag() -> None:
    state = RecoveryCycleState(recovery_iteration=1, completed=False)
    done = mark_recovery_completed(state)
    assert done == RecoveryCycleState(recovery_iteration=1, completed=True)
    # Input state is unchanged (frozen dataclass).
    assert state.completed is False


def test_mark_recovery_completed_rejects_double_complete() -> None:
    already = RecoveryCycleState(recovery_iteration=1, completed=True)
    with pytest.raises(ValueError, match="already marked completed"):
        mark_recovery_completed(already)


def test_recovery_cycle_state_is_immutable() -> None:
    state = RecoveryCycleState(recovery_iteration=0, completed=False)
    with pytest.raises(AttributeError):
        state.recovery_iteration = 1  # type: ignore[misc]
