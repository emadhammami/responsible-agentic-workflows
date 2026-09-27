"""Real shared injected nodes for the frozen B1/G1 LangGraph."""

from __future__ import annotations

from responsible_agentic_workflows.logging import (
    LoggedLanguageModel,
    LoggedRetriever,
    RunRecorder,
)
from responsible_agentic_workflows.modeling import LanguageModel
from responsible_agentic_workflows.retrieval import Retriever

from .agentic_execution import (
    AGENTIC_PROMPT_VERSION,
    build_draft_request,
    build_plan_request,
    build_revision_request,
    format_evidence_context,
    path_reserve_satisfied_for_logging,
    selected_recovery_path_for_logging,
)
from .control import (
    BlockedLimit,
    CriticControlState,
    CriticResult,
    RecoveryAction,
    RecoveryPolicy,
    ResourceLimits,
)
from .critic import StructuredCritic
from .execution import (
    begin_recovery_blockers,
    build_recovery_policy_context,
    build_resource_snapshot,
    model_call_blockers,
    record_policy_decision,
    record_workflow_event,
    retrieval_call_blockers,
)
from .graph import GraphComponents
from .recovery import build_recovery_query
from .state import WorkflowState


class ExecutionResourceStop(RuntimeError):
    """Internal runner-level signal for an execution guard block."""

    def __init__(
        self,
        *,
        stage: str,
        blocked_limits: tuple[BlockedLimit, ...],
    ) -> None:
        self.stage = stage
        self.blocked_limits = blocked_limits
        joined = ",".join(value.value for value in blocked_limits)
        super().__init__(f"{stage} blocked by {joined}")


def _non_empty(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value


def _limits(state: WorkflowState) -> ResourceLimits:
    value = state.get("ResourceLimits")
    if not isinstance(value, ResourceLimits):
        raise ValueError("ResourceLimits must be present")
    return value


def _iteration(state: WorkflowState) -> int:
    value = state.get("recovery_iteration", 0)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("recovery_iteration must be a non-negative integer")
    return value


def _evidence(state: WorkflowState):
    value = state.get("merged_evidence")
    if value is None:
        value = state.get("initial_retrieval")
    if value is None:
        raise ValueError("workflow evidence context is missing")
    return value


class AgenticNodeAssembler:
    """Build the eight injected behavioral nodes shared by B1 and G1."""

    def __init__(
        self,
        *,
        model: LanguageModel,
        retriever: Retriever,
        recovery_policy: RecoveryPolicy,
        recorder: RunRecorder,
        top_k: int,
    ) -> None:
        if not isinstance(model, LanguageModel):
            raise TypeError("model must satisfy LanguageModel")
        if not callable(getattr(retriever, "retrieve", None)):
            raise TypeError("retriever must expose retrieve")
        if not isinstance(recovery_policy, RecoveryPolicy):
            raise TypeError("recovery_policy must satisfy RecoveryPolicy")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer")
        if recorder.configuration.prompt_version != AGENTIC_PROMPT_VERSION:
            raise ValueError(
                "recorder prompt_version does not match agentic prompt bundle"
            )

        self._recorder = recorder
        self._policy = recovery_policy
        self._top_k = top_k
        self._model = LoggedLanguageModel(model, recorder)
        self._retriever = LoggedRetriever(retriever, recorder)
        self._critic = StructuredCritic(model=self._model)

    def _model_guard(self, state: WorkflowState, stage: str) -> None:
        limits = _limits(state)
        resources = build_resource_snapshot(
            recorder=self._recorder,
            recovery_iteration=_iteration(state),
        )
        blocked = model_call_blockers(
            resources=resources,
            limits=limits,
            elapsed_ms=self._recorder.elapsed_ms,
        )
        if blocked:
            raise ExecutionResourceStop(stage=stage, blocked_limits=blocked)

    def _retrieval_guard(self, state: WorkflowState, stage: str) -> None:
        limits = _limits(state)
        resources = build_resource_snapshot(
            recorder=self._recorder,
            recovery_iteration=_iteration(state),
        )
        blocked = retrieval_call_blockers(
            resources=resources,
            limits=limits,
            elapsed_ms=self._recorder.elapsed_ms,
        )
        if blocked:
            raise ExecutionResourceStop(stage=stage, blocked_limits=blocked)

    def plan(self, state: WorkflowState) -> dict[str, object]:
        question = _non_empty(state.get("question"), "question")
        self._model_guard(state, "plan")
        response = self._model.generate(
            build_plan_request(
                question=question,
                temperature=self._recorder.configuration.temperature,
                max_output_tokens=self._recorder.configuration.max_output_tokens,
            )
        )
        plan = _non_empty(response.text, "plan")
        record_workflow_event(
            recorder=self._recorder,
            event_type="plan_completed",
            stage="plan",
        )
        return {"plan": plan}

    def initial_retrieve(self, state: WorkflowState) -> dict[str, object]:
        question = _non_empty(state.get("question"), "question")
        self._retrieval_guard(state, "initial_retrieve")
        results = self._retriever.retrieve(question, top_k=self._top_k)
        record_workflow_event(
            recorder=self._recorder,
            event_type="initial_retrieval_completed",
            stage="initial_retrieve",
        )
        return {"initial_retrieval": tuple(results)}

    def draft(self, state: WorkflowState) -> dict[str, object]:
        question = _non_empty(state.get("question"), "question")
        plan = _non_empty(state.get("plan"), "plan")
        evidence = _evidence(state)
        self._model_guard(state, "draft")
        response = self._model.generate(
            build_draft_request(
                question=question,
                plan=plan,
                evidence=evidence,
                temperature=self._recorder.configuration.temperature,
                max_output_tokens=self._recorder.configuration.max_output_tokens,
            )
        )
        candidate = _non_empty(response.text, "current_answer_candidate")
        record_workflow_event(
            recorder=self._recorder,
            event_type="draft_completed",
            stage="draft",
        )
        return {"current_answer_candidate": candidate}

    def initial_critic(self, state: WorkflowState) -> dict[str, object]:
        question = _non_empty(state.get("question"), "question")
        answer = _non_empty(
            state.get("current_answer_candidate"),
            "current_answer_candidate",
        )
        self._model_guard(state, "initial_critic")
        result = self._critic.assess(
            question=question,
            answer=answer,
            evidence_context=format_evidence_context(_evidence(state)),
            temperature=self._recorder.configuration.temperature,
            max_output_tokens=self._recorder.configuration.max_output_tokens,
        )
        control = CriticControlState.from_critic_result(result)
        record_workflow_event(
            recorder=self._recorder,
            event_type="initial_critic_completed",
            stage="initial_critic",
        )
        return {
            "latest_CriticResult": result,
            "latest_CriticControlState": control,
            "critic_iteration": 1,
        }

    def recovery_policy(self, state: WorkflowState) -> dict[str, object]:
        result = state.get("latest_CriticResult")
        if not isinstance(result, CriticResult):
            raise ValueError("latest_CriticResult must be present")

        iteration = _iteration(state)
        limits = _limits(state)

        context = build_recovery_policy_context(
            critic_result=result,
            recovery_iteration=iteration,
            recorder=self._recorder,
            limits=limits,
        )
        decision = self._policy.decide(context)

        selected_path = selected_recovery_path_for_logging(
            decision=decision,
            critic=context.critic,
        )
        record_policy_decision(
            recorder=self._recorder,
            decision=decision,
            critic=context.critic,
            critic_iteration=state.get("critic_iteration"),
            decision_sequence=1,
            recovery_iteration=iteration,
            resources=context.resources,
            limits=limits,
            hard_recovery_feasibility=context.hard_recovery_feasibility,
            selected_recovery_path=selected_path,
            path_reserve_satisfied=path_reserve_satisfied_for_logging(decision),
        )

        if decision.action in {
            RecoveryAction.REVISE_ONLY,
            RecoveryAction.RERETRIEVE_REVISE,
        }:
            blocked = begin_recovery_blockers(
                resources=context.resources,
                limits=limits,
                elapsed_ms=self._recorder.elapsed_ms,
                recovery_iteration=iteration,
            )
            if blocked:
                raise ExecutionResourceStop(
                    stage="begin_recovery",
                    blocked_limits=blocked,
                )

        return {"latest_RecoveryDecision": decision}

    def recovery_retrieve(self, state: WorkflowState) -> dict[str, object]:
        result = state.get("latest_CriticResult")
        if not isinstance(result, CriticResult):
            raise ValueError("latest_CriticResult must be present")

        record_workflow_event(
            recorder=self._recorder,
            event_type="recovery_started",
            stage="recovery",
        )
        self._retrieval_guard(state, "recovery_retrieve")

        query = build_recovery_query(
            question=_non_empty(state.get("question"), "question"),
            evidence_gaps=result.evidence_gaps,
        )
        retrieved = self._retriever.retrieve(query, top_k=self._top_k)

        record_workflow_event(
            recorder=self._recorder,
            event_type="recovery_retrieval_completed",
            stage="recovery_retrieve",
        )
        return {"recovery_retrieval": tuple(retrieved)}

    def revision(self, state: WorkflowState) -> dict[str, object]:
        if state.get("recovery_retrieval") is None:
            record_workflow_event(
                recorder=self._recorder,
                event_type="recovery_started",
                stage="recovery",
            )

        critic = state.get("latest_CriticResult")
        if not isinstance(critic, CriticResult):
            raise ValueError("latest_CriticResult must be present")

        self._model_guard(state, "revision")
        response = self._model.generate(
            build_revision_request(
                question=_non_empty(state.get("question"), "question"),
                plan=_non_empty(state.get("plan"), "plan"),
                current_answer=_non_empty(
                    state.get("current_answer_candidate"),
                    "current_answer_candidate",
                ),
                evidence=_evidence(state),
                critic_result=critic,
                temperature=self._recorder.configuration.temperature,
                max_output_tokens=self._recorder.configuration.max_output_tokens,
            )
        )
        candidate = _non_empty(response.text, "current_answer_candidate")
        record_workflow_event(
            recorder=self._recorder,
            event_type="revision_completed",
            stage="revision",
        )
        return {"current_answer_candidate": candidate}

    def post_recovery_critic(
        self,
        state: WorkflowState,
    ) -> dict[str, object]:
        self._model_guard(state, "post_recovery_critic")
        result = self._critic.assess(
            question=_non_empty(state.get("question"), "question"),
            answer=_non_empty(
                state.get("current_answer_candidate"),
                "current_answer_candidate",
            ),
            evidence_context=format_evidence_context(_evidence(state)),
            temperature=self._recorder.configuration.temperature,
            max_output_tokens=self._recorder.configuration.max_output_tokens,
        )
        control = CriticControlState.from_critic_result(result)
        record_workflow_event(
            recorder=self._recorder,
            event_type="post_recovery_critic_completed",
            stage="post_recovery_critic",
        )
        return {
            "latest_CriticResult": result,
            "latest_CriticControlState": control,
            "critic_iteration": 2,
        }

    def components(self) -> GraphComponents:
        return GraphComponents(
            plan=self.plan,
            initial_retrieve=self.initial_retrieve,
            draft=self.draft,
            initial_critic=self.initial_critic,
            recovery_policy=self.recovery_policy,
            recovery_retrieve=self.recovery_retrieve,
            revision=self.revision,
            post_recovery_critic=self.post_recovery_critic,
        )
