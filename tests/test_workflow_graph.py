from __future__ import annotations

from collections.abc import Callable

import pytest

from responsible_agentic_workflows.ingestion import DocumentChunk
from responsible_agentic_workflows.retrieval.models import RetrievedChunk
from responsible_agentic_workflows.workflow import (
    CriticResult,
    EvidenceSufficiency,
    GraphComponents,
    RecoveryAction,
    RecoveryDecision,
    RecoveryReasonCode,
    ResourceLimits,
    SupportStatus,
)
from responsible_agentic_workflows.workflow.graph import (
    NODE_BEGIN_RECOVERY,
    NODE_DRAFT,
    NODE_FINALIZE_ABSTAIN,
    NODE_FINALIZE_ACCEPT,
    NODE_FINALIZE_RESOURCE_STOP,
    NODE_INITIAL_CRITIC,
    NODE_INITIAL_RETRIEVE,
    NODE_MERGE_EVIDENCE,
    NODE_PLAN,
    NODE_POST_RECOVERY_CRITIC,
    NODE_POST_RECOVERY_FINALIZE,
    NODE_RECOVERY_POLICY,
    NODE_RECOVERY_RETRIEVE,
    NODE_REVISE,
    TERMINAL_COMPLETED,
    TERMINAL_COMPLETED_AFTER_RECOVERY,
    TERMINAL_RESOURCE_STOPPED,
    _begin_recovery_node,
    _finalize_accept,
    _finalize_post_recovery,
    _merge_evidence_node,
    build_graph,
    route_after_begin_recovery,
    route_after_recovery_policy,
)
from responsible_agentic_workflows.workflow.state import WorkflowState


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


def _decision(action: RecoveryAction) -> RecoveryDecision:
    return RecoveryDecision(
        action=action,
        reason_code=RecoveryReasonCode.RELEASE_OK,
        policy_id="test-policy",
    )


def releasable_critic() -> CriticResult:
    return CriticResult(
        schema_version="v1",
        support_status=SupportStatus.SUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.SUFFICIENT,
        unresolved_conflict=False,
    )


def non_releasable_critic() -> CriticResult:
    return CriticResult(
        schema_version="v1",
        support_status=SupportStatus.UNSUPPORTED,
        evidence_sufficiency=EvidenceSufficiency.INSUFFICIENT,
        unresolved_conflict=False,
    )


class NodeTracker:
    """Records the tracked node order and emits the configured decision/critic.

    The two retrieve nodes emit the configured chunk tuples (both defaulting to
    the empty tuple) so that the internal ``MERGE_EVIDENCE`` node receives a
    non-``None`` value on both sides of the shared merge. The structural nodes
    (``BEGIN_RECOVERY``, ``MERGE_EVIDENCE``, and the four finalizers) are the
    module's internal shared implementations and are never injected here.
    """

    def __init__(self, decision: RecoveryDecision, critic: CriticResult | None):
        self.decision = decision
        self.critic = critic
        self.order: list[str] = []
        self.initial_chunks: tuple[RetrievedChunk, ...] = ()
        self.recovery_chunks: tuple[RetrievedChunk, ...] = ()

    def make(self, name: str) -> Callable[[WorkflowState], dict[str, object]]:
        def node(state: WorkflowState) -> dict[str, object]:
            del state
            self.order.append(name)
            updates: dict[str, object] = {}
            if name == NODE_RECOVERY_POLICY:
                updates["latest_RecoveryDecision"] = self.decision
            if name in (NODE_INITIAL_CRITIC, NODE_POST_RECOVERY_CRITIC) and self.critic:
                updates["latest_CriticResult"] = self.critic
            if name == NODE_INITIAL_RETRIEVE:
                updates["initial_retrieval"] = self.initial_chunks
            if name == NODE_RECOVERY_RETRIEVE:
                updates["recovery_retrieval"] = self.recovery_chunks
            return updates

        return node

    def components(self) -> GraphComponents:
        return GraphComponents(
            plan=self.make(NODE_PLAN),
            initial_retrieve=self.make(NODE_INITIAL_RETRIEVE),
            draft=self.make(NODE_DRAFT),
            initial_critic=self.make(NODE_INITIAL_CRITIC),
            recovery_policy=self.make(NODE_RECOVERY_POLICY),
            recovery_retrieve=self.make(NODE_RECOVERY_RETRIEVE),
            revision=self.make(NODE_REVISE),
            post_recovery_critic=self.make(NODE_POST_RECOVERY_CRITIC),
        )


def _initial(
    candidate: str | None = "answer", condition: str | None = None
) -> WorkflowState:
    return {
        "task_id": "t",
        "question": "q",
        "execution_mode": "engineering",
        "condition_metadata": condition,
        "ResourceLimits": ResourceLimits(
            max_llm_calls=4,
            max_retrieval_calls=3,
            max_retries=2,
            max_total_tokens=4096,
            timeout_ms=60_000,
        ),
        "current_answer_candidate": candidate,
    }


# ---- Routing (pure, decision-driven) ----------------------------------------


@pytest.mark.parametrize(
    ("action", "expected"),
    [
        (RecoveryAction.ACCEPT, NODE_FINALIZE_ACCEPT),
        (RecoveryAction.ABSTAIN, NODE_FINALIZE_ABSTAIN),
        (RecoveryAction.RESOURCE_STOP, NODE_FINALIZE_RESOURCE_STOP),
        (RecoveryAction.REVISE_ONLY, NODE_BEGIN_RECOVERY),
        (RecoveryAction.RERETRIEVE_REVISE, NODE_BEGIN_RECOVERY),
    ],
)
def test_route_after_recovery_policy(action: RecoveryAction, expected: str) -> None:
    state: WorkflowState = {"latest_RecoveryDecision": _decision(action)}
    assert route_after_recovery_policy(state) == expected


def test_route_after_recovery_policy_requires_decision() -> None:
    with pytest.raises(ValueError, match="RecoveryDecision"):
        route_after_recovery_policy({})


@pytest.mark.parametrize(
    ("action", "expected"),
    [
        (RecoveryAction.REVISE_ONLY, NODE_REVISE),
        (RecoveryAction.RERETRIEVE_REVISE, NODE_RECOVERY_RETRIEVE),
    ],
)
def test_route_after_begin_recovery(action: RecoveryAction, expected: str) -> None:
    state: WorkflowState = {"latest_RecoveryDecision": _decision(action)}
    assert route_after_begin_recovery(state) == expected


@pytest.mark.parametrize(
    "action",
    [RecoveryAction.ACCEPT, RecoveryAction.ABSTAIN, RecoveryAction.RESOURCE_STOP],
)
def test_route_after_begin_recovery_rejects_other(action: RecoveryAction) -> None:
    state: WorkflowState = {"latest_RecoveryDecision": _decision(action)}
    with pytest.raises(ValueError, match="recovery action"):
        route_after_begin_recovery(state)


def test_route_after_begin_recovery_requires_decision() -> None:
    with pytest.raises(ValueError, match="RecoveryDecision"):
        route_after_begin_recovery({})


# ---- Topology -----------------------------------------------------------------


def test_graph_registers_all_14_nodes() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.ACCEPT), None)
    graph = build_graph(tracker.components())
    graph_nodes = set(graph.get_graph().nodes)
    expected = {
        NODE_PLAN,
        NODE_INITIAL_RETRIEVE,
        NODE_DRAFT,
        NODE_INITIAL_CRITIC,
        NODE_RECOVERY_POLICY,
        NODE_FINALIZE_ACCEPT,
        NODE_FINALIZE_ABSTAIN,
        NODE_FINALIZE_RESOURCE_STOP,
        NODE_BEGIN_RECOVERY,
        NODE_RECOVERY_RETRIEVE,
        NODE_MERGE_EVIDENCE,
        NODE_REVISE,
        NODE_POST_RECOVERY_CRITIC,
        NODE_POST_RECOVERY_FINALIZE,
    }
    assert expected.issubset(graph_nodes)
    assert len(expected) == 14


# ---- Pre-recovery finalization semantics -------------------------------------


def test_accept_pre_recovery_completes_and_releases_candidate() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.ACCEPT), None)
    out = build_graph(tracker.components()).invoke(_initial("answer"))

    assert out["terminal_status"] == TERMINAL_COMPLETED
    assert out["final_answer"] == "answer"
    assert out["abstained_flag"] is False
    # The ACCEPT path terminates before the recovery cycle is opened.
    assert tracker.order == [
        NODE_PLAN,
        NODE_INITIAL_RETRIEVE,
        NODE_DRAFT,
        NODE_INITIAL_CRITIC,
        NODE_RECOVERY_POLICY,
    ]
    assert NODE_BEGIN_RECOVERY not in tracker.order


def test_abstain_pre_recovery_completes_without_answer() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.ABSTAIN), None)
    out = build_graph(tracker.components()).invoke(_initial("answer"))

    assert out["terminal_status"] == TERMINAL_COMPLETED
    assert out["final_answer"] is None
    assert out["abstained_flag"] is True
    assert NODE_BEGIN_RECOVERY not in tracker.order


def test_resource_stop_terminates_resource_stopped_pre_recovery() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.RESOURCE_STOP), None)
    out = build_graph(tracker.components()).invoke(_initial("answer"))

    assert out["terminal_status"] == TERMINAL_RESOURCE_STOPPED
    assert out["final_answer"] is None
    assert out["abstained_flag"] is False
    assert NODE_BEGIN_RECOVERY not in tracker.order


# ---- Post-recovery (recovery-cycle) semantics ---------------------------------


def test_revise_only_recovery_topology() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.REVISE_ONLY), releasable_critic())
    out = build_graph(tracker.components()).invoke(_initial("answer"))

    # BEGIN_RECOVERY is an internal shared node (bookkeeping only); it is not
    # tracked and performs no retrieval. The tracked path ends at the critic and
    # the internal post-recovery finalizer releases per the shared predicate.
    assert tracker.order == [
        NODE_PLAN,
        NODE_INITIAL_RETRIEVE,
        NODE_DRAFT,
        NODE_INITIAL_CRITIC,
        NODE_RECOVERY_POLICY,
        NODE_REVISE,
        NODE_POST_RECOVERY_CRITIC,
    ]
    assert NODE_RECOVERY_RETRIEVE not in tracker.order
    assert NODE_MERGE_EVIDENCE not in tracker.order
    assert out["terminal_status"] == TERMINAL_COMPLETED_AFTER_RECOVERY
    assert out["final_answer"] == "answer"
    assert out["abstained_flag"] is False
    # BEGIN_RECOVERY advanced the shared counter exactly once (0 -> 1).
    assert out["recovery_iteration"] == 1


def test_reretrieve_revise_recovery_topology() -> None:
    tracker = NodeTracker(
        _decision(RecoveryAction.RERETRIEVE_REVISE),
        non_releasable_critic(),
    )
    out = build_graph(tracker.components()).invoke(_initial("answer"))

    # reretrieve traverses RECOVERY_RETRIEVE -> MERGE_EVIDENCE -> REVISE;
    # both BEGIN_RECOVERY and MERGE_EVIDENCE are internal (untracked).
    assert tracker.order == [
        NODE_PLAN,
        NODE_INITIAL_RETRIEVE,
        NODE_DRAFT,
        NODE_INITIAL_CRITIC,
        NODE_RECOVERY_POLICY,
        NODE_RECOVERY_RETRIEVE,
        NODE_REVISE,
        NODE_POST_RECOVERY_CRITIC,
    ]
    assert NODE_BEGIN_RECOVERY not in tracker.order
    assert NODE_MERGE_EVIDENCE not in tracker.order
    # release decided by the shared critic; non-release -> abstain (never
    # RESOURCE_STOP post-recovery).
    assert out["terminal_status"] == TERMINAL_COMPLETED_AFTER_RECOVERY
    assert out["final_answer"] is None
    assert out["abstained_flag"] is True
    assert out["recovery_iteration"] == 1


def test_reretrieve_revise_merges_evidence() -> None:
    tracker = NodeTracker(
        _decision(RecoveryAction.RERETRIEVE_REVISE),
        releasable_critic(),
    )
    tracker.initial_chunks = (_rc("a", 1), _rc("b", 2))
    tracker.recovery_chunks = (_rc("a", 1), _rc("c", 3))
    out = build_graph(tracker.components()).invoke(_initial("revised"))

    # first-occurrence-wins: "a" deduped, "c" appended; current ordering kept.
    assert [rc.chunk.chunk_id for rc in out["merged_evidence"]] == ["a", "b", "c"]
    assert out["terminal_status"] == TERMINAL_COMPLETED_AFTER_RECOVERY
    assert out["final_answer"] == "revised"
    assert out["abstained_flag"] is False


def test_post_recovery_resource_stop_is_not_emitted() -> None:
    tracker = NodeTracker(
        _decision(RecoveryAction.RERETRIEVE_REVISE),
        non_releasable_critic(),
    )
    out = build_graph(tracker.components()).invoke(_initial("answer"))
    assert out["terminal_status"] != TERMINAL_RESOURCE_STOPPED
    assert out["terminal_status"] == TERMINAL_COMPLETED_AFTER_RECOVERY


# ---- Structural nodes are shared internal implementations --------------------


def test_graph_components_exposes_exactly_the_eight_injected_nodes() -> None:
    fields = set(GraphComponents.__dataclass_fields__)
    assert fields == {
        "plan",
        "initial_retrieve",
        "draft",
        "initial_critic",
        "recovery_policy",
        "recovery_retrieve",
        "revision",
        "post_recovery_critic",
    }


def test_internal_shared_nodes_are_not_injectable() -> None:
    from responsible_agentic_workflows.workflow import graph as g

    for name in (
        "_begin_recovery_node",
        "_merge_evidence_node",
        "_finalize_accept",
        "_finalize_abstain",
        "_finalize_resource_stop",
        "_finalize_post_recovery",
    ):
        assert callable(getattr(g, name))

    fields = set(GraphComponents.__dataclass_fields__)
    for name in (
        "begin_recovery",
        "merge_evidence",
        "finalize_accept",
        "finalize_abstain",
        "finalize_resource_stop",
        "post_recovery_finalize",
    ):
        assert name not in fields


# ---- Finalization strictness -------------------------------------------------


def test_finalize_accept_requires_answer_candidate() -> None:
    state: WorkflowState = {"current_answer_candidate": None}
    with pytest.raises(ValueError, match="current_answer_candidate"):
        _finalize_accept(state)


def test_finalize_post_recovery_requires_critic_result() -> None:
    state: WorkflowState = {"latest_CriticResult": None}
    with pytest.raises(ValueError, match="latest_CriticResult"):
        _finalize_post_recovery(state)


def test_finalize_post_recovery_release_ok_requires_candidate() -> None:
    state: WorkflowState = {
        "latest_CriticResult": releasable_critic(),
        "current_answer_candidate": None,
    }
    with pytest.raises(ValueError, match="current_answer_candidate"):
        _finalize_post_recovery(state)


# ---- BEGIN_RECOVERY / MERGE_EVIDENCE error paths ----------------------------


def test_begin_recovery_node_requires_decision() -> None:
    with pytest.raises(ValueError, match="RecoveryDecision"):
        _begin_recovery_node({})


def test_begin_recovery_node_enforces_max_cycles() -> None:
    state: WorkflowState = {
        "recovery_iteration": 1,
        "latest_RecoveryDecision": _decision(RecoveryAction.REVISE_ONLY),
    }
    with pytest.raises(ValueError, match="MAX_RECOVERY_CYCLES"):
        _begin_recovery_node(state)


def test_begin_recovery_node_advances_iteration_once() -> None:
    state: WorkflowState = {
        "recovery_iteration": 0,
        "latest_RecoveryDecision": _decision(RecoveryAction.RERETRIEVE_REVISE),
    }
    out = _begin_recovery_node(state)
    assert out["recovery_iteration"] == 1


def test_merge_evidence_node_requires_initial_retrieval() -> None:
    state: WorkflowState = {"initial_retrieval": None, "recovery_retrieval": ()}
    with pytest.raises(ValueError, match="initial_retrieval"):
        _merge_evidence_node(state)


def test_merge_evidence_node_requires_recovery_retrieval() -> None:
    state: WorkflowState = {"initial_retrieval": (), "recovery_retrieval": None}
    with pytest.raises(ValueError, match="recovery_retrieval"):
        _merge_evidence_node(state)


def test_merge_evidence_node_empty_recovery_preserves_current() -> None:
    current = (_rc("a", 1), _rc("b", 2))
    out = _merge_evidence_node({"initial_retrieval": current, "recovery_retrieval": ()})
    assert list(out["merged_evidence"]) == list(current)


def test_merge_evidence_node_prefers_merged_evidence_context() -> None:
    initial = (_rc("a", 1),)
    merged = (_rc("a", 1), _rc("b", 2))
    recovery = (_rc("c", 3),)
    out = _merge_evidence_node(
        {
            "initial_retrieval": initial,
            "merged_evidence": merged,
            "recovery_retrieval": recovery,
        }
    )
    # The current context is merged_evidence when set, not initial_retrieval.
    assert [rc.chunk.chunk_id for rc in out["merged_evidence"]] == ["a", "b", "c"]


def test_merge_evidence_node_requires_current_context() -> None:
    state: WorkflowState = {"initial_retrieval": None, "recovery_retrieval": ()}
    with pytest.raises(ValueError, match="initial_retrieval"):
        _merge_evidence_node(state)


# ---- condition_metadata isolation -------------------------------------------


@pytest.mark.parametrize("condition", [None, "B1", "G1"])
def test_condition_metadata_never_drives_routing(condition: str | None) -> None:
    state: WorkflowState = {
        "latest_RecoveryDecision": _decision(RecoveryAction.RERETRIEVE_REVISE),
        "condition_metadata": condition,
    }
    # Routing reads only the decision action; the label never participates.
    assert route_after_recovery_policy(state) == NODE_BEGIN_RECOVERY
    assert route_after_begin_recovery(state) == NODE_RECOVERY_RETRIEVE


@pytest.mark.parametrize("condition", ["B1", "G1"], ids=["B1", "G1"])
def test_b1_and_g1_share_identical_traversal_and_outcome(condition: str) -> None:
    tracker = NodeTracker(
        _decision(RecoveryAction.RERETRIEVE_REVISE),
        releasable_critic(),
    )
    tracker.initial_chunks = (_rc("a", 1), _rc("b", 2))
    tracker.recovery_chunks = (_rc("a", 1), _rc("c", 3))
    out = build_graph(tracker.components()).invoke(_initial("revised", condition))

    assert out["terminal_status"] == TERMINAL_COMPLETED_AFTER_RECOVERY
    assert out["final_answer"] == "revised"
    assert out["abstained_flag"] is False
    assert [rc.chunk.chunk_id for rc in out["merged_evidence"]] == ["a", "b", "c"]
    assert out["recovery_iteration"] == 1
    # The label is carried but never influences any of the above.
    assert out.get("condition_metadata") == condition


def _topology(graph) -> tuple[set[str], set[tuple[str, str]]]:
    """Extract (node-name set, directed edge set) from a compiled graph.

    Node and callable object identity are intentionally ignored; only the
    structural names and directed connectivity are compared.
    """

    sg = graph.get_graph()
    node_names = {node.id for node in sg.nodes.values()}
    edges = {(edge.source, edge.target) for edge in sg.edges}
    return node_names, edges


@pytest.mark.parametrize("condition", ["B1", "G1"])
def test_b1_and_g1_topology_identity(condition: str) -> None:
    decision = _decision(RecoveryAction.RERETRIEVE_REVISE)

    def make_components(policy: Callable[[WorkflowState], dict[str, object]]):
        tracker = NodeTracker(decision, releasable_critic())
        components = tracker.components()
        return type(components)(
            plan=components.plan,
            initial_retrieve=components.initial_retrieve,
            draft=components.draft,
            initial_critic=components.initial_critic,
            recovery_policy=policy,
            recovery_retrieve=components.recovery_retrieve,
            revision=components.revision,
            post_recovery_critic=components.post_recovery_critic,
        )

    def synthetic_b1_policy_node(state: WorkflowState) -> dict[str, object]:
        del state
        return {"latest_RecoveryDecision": decision}

    def synthetic_g1_policy_node(state: WorkflowState) -> dict[str, object]:
        del state
        return {"latest_RecoveryDecision": decision}

    b1 = _topology(build_graph(make_components(synthetic_b1_policy_node)))
    g1 = _topology(build_graph(make_components(synthetic_g1_policy_node)))

    assert b1 == g1


@pytest.mark.parametrize(
    "action", [RecoveryAction.REVISE_ONLY, RecoveryAction.RERETRIEVE_REVISE]
)
def test_recovery_policy_invoked_exactly_once(action: RecoveryAction) -> None:
    tracker = NodeTracker(_decision(action), releasable_critic())
    build_graph(tracker.components()).invoke(_initial("answer"))

    assert tracker.order.count(NODE_RECOVERY_POLICY) == 1
    assert tracker.order.index(NODE_RECOVERY_POLICY) < tracker.order.index(
        NODE_POST_RECOVERY_CRITIC
    )


def test_second_recovery_cycle_is_rejected_end_to_end() -> None:
    tracker = NodeTracker(_decision(RecoveryAction.REVISE_ONLY), releasable_critic())
    state = _initial("answer")
    state["recovery_iteration"] = 1
    with pytest.raises(ValueError, match="MAX_RECOVERY_CYCLES"):
        build_graph(tracker.components()).invoke(state)
