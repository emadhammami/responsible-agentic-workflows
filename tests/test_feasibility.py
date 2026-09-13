"""Synthetic tests for the shared hard-recovery feasibility calculation."""

import dataclasses
import inspect
import pathlib

import pytest

from responsible_agentic_workflows.workflow import (
    BlockedLimit,
    HardRecoveryFeasibility,
    RecoveryPath,
    ResourceLimits,
    ResourceSnapshot,
    calculate_hard_recovery_feasibility,
)

REVISE_ONLY = RecoveryPath.REVISE_ONLY
RERETRIEVE_REVISE = RecoveryPath.RERETRIEVE_REVISE


def _snapshot(
    *,
    llm: int = 0,
    retrieval: int = 0,
    retries: int = 0,
    input_tokens: int = 0,
    output_tokens: int = 0,
) -> ResourceSnapshot:
    return ResourceSnapshot(
        llm_calls_used=llm,
        retrieval_calls_used=retrieval,
        retries_used=retries,
        input_tokens_used=input_tokens,
        output_tokens_used=output_tokens,
        total_tokens_used=input_tokens + output_tokens,
    )


def _limits(
    *,
    llm: int | None = None,
    retrieval: int | None = None,
    retries: int | None = None,
    tokens: int | None = None,
    timeout_ms: float | None = 1000.0,
) -> ResourceLimits:
    return ResourceLimits(
        max_llm_calls=llm,
        max_retrieval_calls=retrieval,
        max_retries=retries,
        max_total_tokens=tokens,
        timeout_ms=timeout_ms,
    )


def _calc(
    path: RecoveryPath,
    snapshot: ResourceSnapshot,
    limits: ResourceLimits,
) -> HardRecoveryFeasibility:
    return calculate_hard_recovery_feasibility(
        recovery_path=path,
        resources=snapshot,
        limits=limits,
    )


# --- A. Basic feasibility ---------------------------------------------------


def test_a1_revise_only_all_limits_disabled_feasible() -> None:
    result = _calc(REVISE_ONLY, _snapshot(), _limits())
    assert result.feasible is True
    assert result.blocked_limits == ()


def test_a2_reretrieve_revise_all_limits_disabled_feasible() -> None:
    result = _calc(RERETRIEVE_REVISE, _snapshot(), _limits())
    assert result.feasible is True
    assert result.blocked_limits == ()


def test_a3_revise_only_minimal_capacity_feasible() -> None:
    result = _calc(
        REVISE_ONLY,
        _snapshot(llm=1, retries=1, output_tokens=1),
        _limits(llm=2, retries=2, tokens=2),
    )
    assert result.feasible is True


def test_a4_reretrieve_revise_minimal_capacity_feasible() -> None:
    result = _calc(
        RERETRIEVE_REVISE,
        _snapshot(llm=1, retrieval=1, retries=1, output_tokens=1),
        _limits(llm=2, retrieval=2, retries=2, tokens=2),
    )
    assert result.feasible is True


def test_a5_recovery_path_preserved_exactly() -> None:
    for path in (REVISE_ONLY, RERETRIEVE_REVISE):
        assert _calc(path, _snapshot(), _limits()).recovery_path is path


# --- B. LLM limit -----------------------------------------------------------


def test_b1_exhausted_llm_blocks_revise_only() -> None:
    result = _calc(REVISE_ONLY, _snapshot(llm=3), _limits(llm=3))
    assert result.feasible is False
    assert result.blocked_limits == (BlockedLimit.LLM_CALL_LIMIT,)


def test_b2_exhausted_llm_blocks_reretrieve_revise() -> None:
    result = _calc(RERETRIEVE_REVISE, _snapshot(llm=1), _limits(llm=1))
    assert result.feasible is False
    assert BlockedLimit.LLM_CALL_LIMIT in result.blocked_limits


def test_b3_unconfigured_llm_never_blocks() -> None:
    result = _calc(REVISE_ONLY, _snapshot(llm=999), _limits(llm=None))
    assert result.feasible is True


# --- C. Retrieval limit -----------------------------------------------------


def test_c1_exhausted_retrieval_does_not_block_revise_only() -> None:
    result = _calc(REVISE_ONLY, _snapshot(retrieval=5), _limits(retrieval=5))
    assert result.feasible is True
    assert BlockedLimit.RETRIEVAL_CALL_LIMIT not in result.blocked_limits


def test_c2_exhausted_retrieval_blocks_reretrieve_revise() -> None:
    result = _calc(
        RERETRIEVE_REVISE, _snapshot(retrieval=2), _limits(retrieval=2)
    )
    assert result.feasible is False
    assert BlockedLimit.RETRIEVAL_CALL_LIMIT in result.blocked_limits


def test_c3_unconfigured_retrieval_does_not_block_reretrieve_revise() -> None:
    result = _calc(
        RERETRIEVE_REVISE, _snapshot(retrieval=999), _limits(retrieval=None)
    )
    assert BlockedLimit.RETRIEVAL_CALL_LIMIT not in result.blocked_limits


# --- D. Retry / recovery-cycle limit ----------------------------------------


def test_d1_zero_retry_limit_blocks_revise_only() -> None:
    result = _calc(REVISE_ONLY, _snapshot(retries=0), _limits(retries=0))
    assert result.feasible is False
    assert result.blocked_limits == (BlockedLimit.RETRY_LIMIT,)


def test_d2_zero_retry_limit_blocks_reretrieve_revise() -> None:
    result = _calc(
        RERETRIEVE_REVISE, _snapshot(retries=0), _limits(retries=0)
    )
    assert BlockedLimit.RETRY_LIMIT in result.blocked_limits


def test_d3_all_retries_used_blocks_both_paths() -> None:
    snapshot = _snapshot(retries=4)
    limits = _limits(retries=4)
    assert _calc(REVISE_ONLY, snapshot, limits).blocked_limits == (
        BlockedLimit.RETRY_LIMIT,
    )
    assert BlockedLimit.RETRY_LIMIT in _calc(
        RERETRIEVE_REVISE, snapshot, limits
    ).blocked_limits


def test_d4_one_retry_slot_remains_allows_recovery() -> None:
    assert _calc(REVISE_ONLY, _snapshot(retries=1), _limits(retries=2)).feasible


def test_d5_unconfigured_retries_never_block() -> None:
    assert (
        _calc(REVISE_ONLY, _snapshot(retries=42), _limits(retries=None)).feasible
    )


# --- E. Token limit ---------------------------------------------------------


def test_e1_tokens_exhausted_blocks_revise_only() -> None:
    result = _calc(REVISE_ONLY, _snapshot(output_tokens=5), _limits(tokens=5))
    assert result.feasible is False
    assert result.blocked_limits == (BlockedLimit.TOKEN_LIMIT,)


def test_e2_tokens_exhausted_blocks_reretrieve_revise() -> None:
    result = _calc(
        RERETRIEVE_REVISE,
        _snapshot(input_tokens=3, output_tokens=2),
        _limits(tokens=5),
    )
    assert BlockedLimit.TOKEN_LIMIT in result.blocked_limits


def test_e3_tokens_over_limit_block() -> None:
    assert BlockedLimit.TOKEN_LIMIT in _calc(
        REVISE_ONLY, _snapshot(output_tokens=8), _limits(tokens=5)
    ).blocked_limits


def test_e4_one_token_remaining_does_not_block() -> None:
    assert (
        _calc(REVISE_ONLY, _snapshot(output_tokens=9), _limits(tokens=10)).feasible
    )


def test_e5_unconfigured_tokens_never_block() -> None:
    result = _calc(
        RERETRIEVE_REVISE, _snapshot(output_tokens=10_000), _limits(tokens=None)
    )
    assert result.feasible


# --- F. Multiple blockers ---------------------------------------------------


def test_f1_revise_only_collects_all_blockers_in_order() -> None:
    result = _calc(
        REVISE_ONLY,
        _snapshot(llm=2, retries=2, output_tokens=100),
        _limits(llm=2, retries=2, tokens=100),
    )
    assert result.blocked_limits == (
        BlockedLimit.LLM_CALL_LIMIT,
        BlockedLimit.RETRY_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
    )


def test_f2_reretrieve_revise_collects_all_blockers_in_order() -> None:
    result = _calc(
        RERETRIEVE_REVISE,
        _snapshot(llm=5, retrieval=3, retries=1, output_tokens=7),
        _limits(llm=5, retrieval=3, retries=1, tokens=7),
    )
    assert result.blocked_limits == (
        BlockedLimit.LLM_CALL_LIMIT,
        BlockedLimit.RETRIEVAL_CALL_LIMIT,
        BlockedLimit.RETRY_LIMIT,
        BlockedLimit.TOKEN_LIMIT,
    )


def test_f3_blocked_limits_have_no_duplicates() -> None:
    result = _calc(
        RERETRIEVE_REVISE,
        _snapshot(llm=9, retrieval=9, retries=9, output_tokens=9),
        _limits(llm=9, retrieval=9, retries=9, tokens=9),
    )
    limits = result.blocked_limits
    assert len(limits) == len(set(limits))


# --- G. Timeout isolation ---------------------------------------------------


def test_g1_timeout_changes_do_not_affect_revise_only() -> None:
    snapshot = _snapshot(llm=1, retries=1, output_tokens=1)
    base_limits = _limits(llm=2, retries=2, tokens=2, timeout_ms=1000.0)
    tight_limits = _limits(llm=2, retries=2, tokens=2, timeout_ms=1.0)
    disabled_limits = _limits(llm=2, retries=2, tokens=2, timeout_ms=None)
    base = _calc(REVISE_ONLY, snapshot, base_limits)
    tightened = _calc(REVISE_ONLY, snapshot, tight_limits)
    disabled = _calc(REVISE_ONLY, snapshot, disabled_limits)
    assert base == tightened == disabled


def test_g2_timeout_limit_never_returned() -> None:
    snapshot = _snapshot(llm=5, retrieval=5, retries=5, output_tokens=5)
    limits = _limits(llm=5, retrieval=5, retries=5, tokens=5)
    for path in (REVISE_ONLY, RERETRIEVE_REVISE):
        result = _calc(path, snapshot, limits)
        assert BlockedLimit.TIMEOUT_LIMIT not in result.blocked_limits


# --- H. Irrelevant-resource invariance --------------------------------------


def test_h1_retrieval_capacity_irrelevant_to_revise_only() -> None:
    snapshot = _snapshot(llm=1, retries=1, output_tokens=1)
    baseline = _calc(REVISE_ONLY, snapshot, _limits(llm=2, retries=2, tokens=2))
    for retrieval_limit in (None, 1, 2, 100):
        variant = _calc(
            REVISE_ONLY,
            snapshot,
            _limits(llm=2, retrieval=retrieval_limit, retries=2, tokens=2),
        )
        assert variant == baseline


def test_h2_token_composition_invariance() -> None:
    limits = _limits(llm=2, retries=2, tokens=10)
    a = _calc(REVISE_ONLY, _snapshot(input_tokens=5, output_tokens=2), limits)
    b = _calc(REVISE_ONLY, _snapshot(input_tokens=2, output_tokens=5), limits)
    assert a == b


def test_h3_disabled_limits_irrelevant_regardless_of_usage() -> None:
    heavy = _snapshot(
        llm=10_000, retrieval=10_000, retries=10_000, output_tokens=10**9
    )
    for path in (REVISE_ONLY, RERETRIEVE_REVISE):
        assert _calc(path, heavy, _limits()).feasible is True


# --- I. Input validation ----------------------------------------------------


def test_i1_string_recovery_path_rejected() -> None:
    with pytest.raises(TypeError):
        _calc("REVISE_ONLY", _snapshot(), _limits())


def test_i2_invalid_resources_type_rejected() -> None:
    with pytest.raises(TypeError):
        _calc(REVISE_ONLY, {}, _limits())


def test_i3_invalid_limits_type_rejected() -> None:
    with pytest.raises(TypeError):
        _calc(REVISE_ONLY, _snapshot(), {})


def test_i4_none_recovery_path_rejected() -> None:
    with pytest.raises(TypeError):
        _calc(None, _snapshot(), _limits())


# --- J. Purity / determinism ------------------------------------------------


def test_j1_repeated_calls_are_equal() -> None:
    snapshot = _snapshot(llm=2, retries=2, output_tokens=2)
    limits = _limits(llm=2, retries=2, tokens=2)
    results = [_calc(REVISE_ONLY, snapshot, limits) for _ in range(3)]
    assert results[0] == results[1] == results[2]


def test_j2_feasibility_invariants_hold() -> None:
    for path in (REVISE_ONLY, RERETRIEVE_REVISE):
        feasible = _calc(
            path,
            _snapshot(llm=0, retries=0),
            _limits(llm=1, retries=1),
        )
        assert feasible.feasible is True
        assert feasible.blocked_limits == ()

        blocked = _calc(
            path,
            _snapshot(llm=1, retries=1),
            _limits(llm=1, retries=1),
        )
        assert blocked.feasible is False
        assert len(blocked.blocked_limits) >= 1


def test_j3_result_is_frozen() -> None:
    result = _calc(REVISE_ONLY, _snapshot(), _limits())
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.feasible = False  # type: ignore[misc]


def test_j4_function_has_keyword_only_parameters() -> None:
    signature = inspect.signature(calculate_hard_recovery_feasibility)
    kinds = set(signature.parameters.values())
    for parameter in kinds:
        assert parameter.kind is inspect.Parameter.KEYWORD_ONLY


def test_g3_timeout_changes_do_not_affect_reretrieve_revise() -> None:
    snapshot = _snapshot(
        llm=1,
        retrieval=1,
        retries=1,
        output_tokens=1,
    )

    base = _calc(
        RERETRIEVE_REVISE,
        snapshot,
        _limits(
            llm=2,
            retrieval=2,
            retries=2,
            tokens=2,
            timeout_ms=1000.0,
        ),
    )

    tightened = _calc(
        RERETRIEVE_REVISE,
        snapshot,
        _limits(
            llm=2,
            retrieval=2,
            retries=2,
            tokens=2,
            timeout_ms=1.0,
        ),
    )

    disabled = _calc(
        RERETRIEVE_REVISE,
        snapshot,
        _limits(
            llm=2,
            retrieval=2,
            retries=2,
            tokens=2,
            timeout_ms=None,
        ),
    )

    assert base == tightened == disabled


def test_g4_feasibility_source_has_no_clock_reads() -> None:
    import responsible_agentic_workflows.workflow.feasibility as module

    source = pathlib.Path(module.__file__).read_text(encoding="utf-8")

    forbidden = (
        "time.time",
        "time.monotonic",
        "time.perf_counter",
        "datetime.",
        "clock_gettime",
        "process_time",
    )

    for token in forbidden:
        assert token not in source


def test_j5_input_objects_are_not_mutated() -> None:
    snapshot = _snapshot(
        llm=1,
        retrieval=1,
        retries=1,
        input_tokens=4,
        output_tokens=2,
    )
    limits = _limits(
        llm=3,
        retrieval=3,
        retries=3,
        tokens=20,
        timeout_ms=5000.0,
    )

    snapshot_before = (
        snapshot.llm_calls_used,
        snapshot.retrieval_calls_used,
        snapshot.retries_used,
        snapshot.input_tokens_used,
        snapshot.output_tokens_used,
        snapshot.total_tokens_used,
    )
    limits_before = (
        limits.max_llm_calls,
        limits.max_retrieval_calls,
        limits.max_retries,
        limits.max_total_tokens,
        limits.timeout_ms,
    )

    calculate_hard_recovery_feasibility(
        recovery_path=RERETRIEVE_REVISE,
        resources=snapshot,
        limits=limits,
    )

    snapshot_after = (
        snapshot.llm_calls_used,
        snapshot.retrieval_calls_used,
        snapshot.retries_used,
        snapshot.input_tokens_used,
        snapshot.output_tokens_used,
        snapshot.total_tokens_used,
    )
    limits_after = (
        limits.max_llm_calls,
        limits.max_retrieval_calls,
        limits.max_retries,
        limits.max_total_tokens,
        limits.timeout_ms,
    )

    assert snapshot_after == snapshot_before
    assert limits_after == limits_before


def test_j6_result_is_hard_recovery_feasibility() -> None:
    result = _calc(
        REVISE_ONLY,
        _snapshot(),
        _limits(),
    )

    assert isinstance(result, HardRecoveryFeasibility)


def test_j7_source_has_no_condition_or_policy_logic() -> None:
    import responsible_agentic_workflows.workflow.feasibility as module

    source = pathlib.Path(module.__file__).read_text(encoding="utf-8")

    forbidden = (
        "B0Baseline",
        "B1FixedRecoveryPolicy",
        "CriticResult",
        "CriticControlState",
        "RecoveryAction",
        "RecoveryDecision",
        "RecoveryPolicy",
        "policy_id",
        "recovery worthiness",
        "resource reserve",
        "benchmark gold",
        "reference answer",
    )

    for token in forbidden:
        assert token not in source
