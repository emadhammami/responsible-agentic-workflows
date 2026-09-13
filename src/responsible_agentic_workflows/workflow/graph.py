"""Shared LangGraph state graph for the B1 and G1 recovery workflows.

This module implements the frozen B1/G1 common graph exactly as specified by
the B1/G1 workflow contract (section 3). B1 and G1 share this identical graph;
the only condition-specific element is the recovery-policy node injected
through :class:`GraphComponents`. Everything here is structural and
deterministic: no model calls, retrieval, or benchmark inputs happen in this
module. Node behavior is supplied entirely through dependency injection so the
graph wiring, routing, and finalization semantics can be exercised in
isolation.

Routing reads only ``latest_RecoveryDecision.action``. ``begin_recovery`` does
not consult resource state, condition labels, or benchmark gold information.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass

from langgraph.graph import END, START, StateGraph

from .control import RecoveryAction, release_ok
from .recovery import begin_recovery_cycle, merge_evidence
from .state import WorkflowState

__all__ = [
    "NODE_BEGIN_RECOVERY",
    "NODE_DRAFT",
    "NODE_INITIAL_CRITIC",
    "NODE_INITIAL_RETRIEVE",
    "NODE_MERGE_EVIDENCE",
    "NODE_PLAN",
    "NODE_POST_RECOVERY_CRITIC",
    "NODE_POST_RECOVERY_FINALIZE",
    "NODE_RECOVERY_POLICY",
    "NODE_RECOVERY_RETRIEVE",
    "NODE_REVISE",
    "NODE_FINALIZE_ACCEPT",
    "NODE_FINALIZE_ABSTAIN",
    "NODE_FINALIZE_RESOURCE_STOP",
    "TERMINAL_COMPLETED",
    "TERMINAL_COMPLETED_AFTER_RECOVERY",
    "TERMINAL_RESOURCE_STOPPED",
    "GraphComponents",
    "NodeFunc",
    "route_after_begin_recovery",
    "route_after_recovery_policy",
    "build_graph",
]

# Frozen node names (section 3 shared graph).
NODE_PLAN = "PLAN"
NODE_INITIAL_RETRIEVE = "INITIAL_RETRIEVE"
NODE_DRAFT = "DRAFT"
NODE_INITIAL_CRITIC = "INITIAL_CRITIC"
NODE_RECOVERY_POLICY = "RECOVERY_POLICY"
NODE_FINALIZE_ACCEPT = "FINALIZE_ACCEPT"
NODE_FINALIZE_ABSTAIN = "FINALIZE_ABSTAIN"
NODE_FINALIZE_RESOURCE_STOP = "FINALIZE_RESOURCE_STOP"
NODE_BEGIN_RECOVERY = "BEGIN_RECOVERY"
NODE_RECOVERY_RETRIEVE = "RECOVERY_RETRIEVE"
NODE_MERGE_EVIDENCE = "MERGE_EVIDENCE"
NODE_REVISE = "REVISE"
NODE_POST_RECOVERY_CRITIC = "POST_RECOVERY_CRITIC"
NODE_POST_RECOVERY_FINALIZE = "POST_RECOVERY_FINALIZE"

# Terminal RunStatus values emitted by the finalize nodes.
TERMINAL_COMPLETED = "completed"
TERMINAL_COMPLETED_AFTER_RECOVERY = "completed_after_recovery"
TERMINAL_RESOURCE_STOPPED = "resource_stopped"

# A node receives the full current state and returns a partial state update.
NodeFunc = Callable[[WorkflowState], Mapping[str, object]]


def _finalize_accept(state: WorkflowState) -> Mapping[str, object]:
    """Release a pre-recovery accepted answer."""

    candidate = state.get("current_answer_candidate")
    if candidate is None:
        raise ValueError(
            "FINALIZE_ACCEPT requires current_answer_candidate to be present"
        )
    return {
        "terminal_status": TERMINAL_COMPLETED,
        "final_answer": candidate,
        "abstained_flag": False,
    }


def _finalize_abstain(state: WorkflowState) -> Mapping[str, object]:
    """Terminate as an abstention without releasing an answer."""

    return {
        "terminal_status": TERMINAL_COMPLETED,
        "final_answer": None,
        "abstained_flag": True,
    }


def _finalize_resource_stop(state: WorkflowState) -> Mapping[str, object]:
    """Terminate without a released answer due to the hard guard."""

    return {
        "terminal_status": TERMINAL_RESOURCE_STOPPED,
        "final_answer": None,
        "abstained_flag": False,
    }


def _finalize_post_recovery(state: WorkflowState) -> Mapping[str, object]:
    """Shared post-recovery finalization rule (runtime contract section 29.4).

    The post-recovery finalizer uses only the shared critic's release
    predicate. A recoverable answer is accepted; an unrecoverable answer is
    abstained. ``RESOURCE_STOP`` is never a post-recovery terminal status, and
    no second recovery cycle is ever initiated.

    Malformed state is an error, not a silent abstention: a missing
    ``latest_CriticResult`` or a missing answer candidate on an accepted
    result raises ``ValueError``.
    """

    result = state.get("latest_CriticResult")
    if result is None:
        raise ValueError(
            "POST_RECOVERY_FINALIZE requires latest_CriticResult to be present"
        )

    if release_ok(result):
        candidate = state.get("current_answer_candidate")
        if candidate is None:
            raise ValueError(
                "POST_RECOVERY_FINALIZE requires current_answer_candidate "
                "for a release-OK critic result"
            )
        return {
            "terminal_status": TERMINAL_COMPLETED_AFTER_RECOVERY,
            "final_answer": candidate,
            "abstained_flag": False,
        }

    return {
        "terminal_status": TERMINAL_COMPLETED_AFTER_RECOVERY,
        "final_answer": None,
        "abstained_flag": True,
    }


def _begin_recovery_node(state: WorkflowState) -> Mapping[str, object]:
    """Shared recovery-cycle bookkeeping node (B1 and G1 identical).

    Increments ``recovery_iteration`` exactly once and enforces the
    ``MAX_RECOVERY_CYCLES`` ceiling. Performs zero LLM calls and no
    condition-specific branching.
    """

    decision = state.get("latest_RecoveryDecision")
    if decision is None:
        raise ValueError("BEGIN_RECOVERY requires a RecoveryDecision")

    cycle = begin_recovery_cycle(
        recovery_iteration=state.get("recovery_iteration", 0),
        action=decision.action,
    )

    return {"recovery_iteration": cycle.recovery_iteration}


def _merge_evidence_node(state: WorkflowState) -> Mapping[str, object]:
    """Shared first-occurrence-wins evidence merge (B1 and G1 identical).

    Deterministic pure merge of the current evidence context with the
    recovery-retrieved chunks. The current context is ``merged_evidence``
    when already set, falling back to ``initial_retrieval``. Performs zero
    LLM calls and no condition-specific branching.
    """

    current = state.get("merged_evidence")
    if current is None:
        current = state.get("initial_retrieval")
    if current is None:
        raise ValueError(
            "MERGE_EVIDENCE requires merged_evidence or initial_retrieval "
            "to be present"
        )

    recovery = state.get("recovery_retrieval")
    if recovery is None:
        raise ValueError("MERGE_EVIDENCE requires recovery_retrieval to be present")

    return {"merged_evidence": merge_evidence(current=current, recovery=recovery)}


def route_after_recovery_policy(state: WorkflowState) -> str:
    """Select the single outgoing branch from ``RECOVERY_POLICY``.

    Reads only ``latest_RecoveryDecision.action``. Both ``REVISE_ONLY`` and
    ``RERETRIEVE_REVISE`` route to ``BEGIN_RECOVERY``; the downstream split is
    handled by :func:`route_after_begin_recovery`.
    """

    decision = state.get("latest_RecoveryDecision")
    if decision is None:
        raise ValueError("route_after_recovery_policy requires a RecoveryDecision")

    action: RecoveryAction = decision.action
    if action is RecoveryAction.ACCEPT:
        return NODE_FINALIZE_ACCEPT
    if action is RecoveryAction.ABSTAIN:
        return NODE_FINALIZE_ABSTAIN
    if action is RecoveryAction.RESOURCE_STOP:
        return NODE_FINALIZE_RESOURCE_STOP

    return NODE_BEGIN_RECOVERY


def route_after_begin_recovery(state: WorkflowState) -> str:
    """Split the recovery path based on the selected recovery action.

    ``REVISE_ONLY`` routes directly to ``REVISE``. ``RERETRIEVE_REVISE``
    routes to ``RECOVERY_RETRIEVE``, which flows to ``MERGE_EVIDENCE`` and
    then to ``REVISE`` via unconditional edges.
    """

    decision = state.get("latest_RecoveryDecision")
    if decision is None:
        raise ValueError("route_after_begin_recovery requires a RecoveryDecision")

    action: RecoveryAction = decision.action
    if action is RecoveryAction.RERETRIEVE_REVISE:
        return NODE_RECOVERY_RETRIEVE
    if action is RecoveryAction.REVISE_ONLY:
        return NODE_REVISE
    raise ValueError(
        f"route_after_begin_recovery requires a recovery action, got {action!r}"
    )


@dataclass(frozen=True, slots=True)
class GraphComponents:
    """Injected node callables for the shared B1/G1 graph.

    The behavioral nodes are supplied by the caller. The structural nodes
    (``BEGIN_RECOVERY``, ``MERGE_EVIDENCE``, and the four finalization nodes)
    are internal shared implementations in this module and are NOT injectable:
    B1 and G1 use them identically. The single condition-specific element is
    ``recovery_policy`` (B1 vs G1), which the workflow invokes exactly once
    per run.
    """

    plan: NodeFunc
    initial_retrieve: NodeFunc
    draft: NodeFunc
    initial_critic: NodeFunc
    recovery_policy: NodeFunc
    revision: NodeFunc
    recovery_retrieve: NodeFunc
    post_recovery_critic: NodeFunc


def build_graph(components: GraphComponents):
    """Wire and compile the frozen B1/G1 common graph.

    B1 and G1 both use this same topology; the only difference is the
    ``recovery_policy`` node supplied by the caller.
    """

    builder = StateGraph(WorkflowState)

    builder.add_node(NODE_PLAN, components.plan)
    builder.add_node(NODE_INITIAL_RETRIEVE, components.initial_retrieve)
    builder.add_node(NODE_DRAFT, components.draft)
    builder.add_node(NODE_INITIAL_CRITIC, components.initial_critic)
    builder.add_node(NODE_RECOVERY_POLICY, components.recovery_policy)
    builder.add_node(NODE_FINALIZE_ACCEPT, _finalize_accept)
    builder.add_node(NODE_FINALIZE_ABSTAIN, _finalize_abstain)
    builder.add_node(NODE_FINALIZE_RESOURCE_STOP, _finalize_resource_stop)
    builder.add_node(NODE_BEGIN_RECOVERY, _begin_recovery_node)
    builder.add_node(NODE_RECOVERY_RETRIEVE, components.recovery_retrieve)
    builder.add_node(NODE_MERGE_EVIDENCE, _merge_evidence_node)
    builder.add_node(NODE_REVISE, components.revision)
    builder.add_node(NODE_POST_RECOVERY_CRITIC, components.post_recovery_critic)
    builder.add_node(NODE_POST_RECOVERY_FINALIZE, _finalize_post_recovery)

    # Sequential spine traversed exactly once per run.
    builder.add_edge(START, NODE_PLAN)
    builder.add_edge(NODE_PLAN, NODE_INITIAL_RETRIEVE)
    builder.add_edge(NODE_INITIAL_RETRIEVE, NODE_DRAFT)
    builder.add_edge(NODE_DRAFT, NODE_INITIAL_CRITIC)
    builder.add_edge(NODE_INITIAL_CRITIC, NODE_RECOVERY_POLICY)

    # RECOVERY_POLICY selects exactly one outgoing branch.
    builder.add_conditional_edges(
        NODE_RECOVERY_POLICY,
        route_after_recovery_policy,
        {
            NODE_FINALIZE_ACCEPT: NODE_FINALIZE_ACCEPT,
            NODE_FINALIZE_ABSTAIN: NODE_FINALIZE_ABSTAIN,
            NODE_FINALIZE_RESOURCE_STOP: NODE_FINALIZE_RESOURCE_STOP,
            NODE_BEGIN_RECOVERY: NODE_BEGIN_RECOVERY,
        },
    )

    # Terminal finalization sinks.
    builder.add_edge(NODE_FINALIZE_ACCEPT, END)
    builder.add_edge(NODE_FINALIZE_ABSTAIN, END)
    builder.add_edge(NODE_FINALIZE_RESOURCE_STOP, END)

    # BEGIN_RECOVERY splits by path; recovery retrieval feeds merge then revise.
    builder.add_conditional_edges(
        NODE_BEGIN_RECOVERY,
        route_after_begin_recovery,
        {
            NODE_REVISE: NODE_REVISE,
            NODE_RECOVERY_RETRIEVE: NODE_RECOVERY_RETRIEVE,
        },
    )
    builder.add_edge(NODE_RECOVERY_RETRIEVE, NODE_MERGE_EVIDENCE)
    builder.add_edge(NODE_MERGE_EVIDENCE, NODE_REVISE)
    builder.add_edge(NODE_REVISE, NODE_POST_RECOVERY_CRITIC)
    builder.add_edge(NODE_POST_RECOVERY_CRITIC, NODE_POST_RECOVERY_FINALIZE)
    builder.add_edge(NODE_POST_RECOVERY_FINALIZE, END)

    return builder.compile()
