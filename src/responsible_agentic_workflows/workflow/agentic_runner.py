"""Shared execution and terminal recording for the B1/G1 agentic graph."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, fields
from typing import Literal

from responsible_agentic_workflows.benchmark.tasks import RuntimeTask
from responsible_agentic_workflows.logging import RunRecorder, validate_run_record
from responsible_agentic_workflows.modeling import LanguageModel
from responsible_agentic_workflows.retrieval import Retriever

from .agentic_nodes import AgenticNodeAssembler, ExecutionResourceStop
from .control import RecoveryPolicy, ResourceLimits
from .execution import record_workflow_event
from .graph import GraphComponents, NodeFunc, build_graph
from .state import WorkflowState, initial_workflow_state

RunOutcome = Literal[
    "completed",
    "completed_after_recovery",
    "resource_stopped",
    "tool_error",
    "failed",
]


@dataclass(frozen=True, slots=True)
class AgenticRunResult:
    """One terminal outcome with independent record and state snapshots."""

    final_answer: str | None
    abstained: bool
    terminal_status: RunOutcome
    record: dict[str, object]
    final_state: WorkflowState

    def __post_init__(self) -> None:
        object.__setattr__(self, "record", deepcopy(self.record))
        object.__setattr__(self, "final_state", deepcopy(self.final_state))


class _StateTracker:
    """Observe injected nodes without changing the frozen graph topology."""

    def __init__(self, initial_state: WorkflowState) -> None:
        self.latest_state = deepcopy(initial_state)
        self.active_stage: str | None = None

    def wrap(self, stage: str, node: NodeFunc) -> NodeFunc:
        def tracked(state: WorkflowState) -> dict[str, object]:
            self.active_stage = stage
            # A pre-state can include updates from frozen structural nodes.
            self.latest_state = deepcopy(state)
            update = dict(node(state))
            post_state = deepcopy(state)
            post_state.update(deepcopy(update))
            self.latest_state = post_state
            self.active_stage = None
            return update

        return tracked

    def components(self, original: GraphComponents) -> GraphComponents:
        return GraphComponents(
            **{
                field.name: self.wrap(field.name, getattr(original, field.name))
                for field in fields(GraphComponents)
            }
        )


class AgenticRunner:
    """Run either agentic condition using only the injected recovery policy."""

    def __init__(
        self,
        *,
        model: LanguageModel,
        retriever: Retriever,
        recovery_policy: RecoveryPolicy,
        top_k: int,
    ) -> None:
        self._model = model
        self._retriever = retriever
        self._recovery_policy = recovery_policy
        self._top_k = top_k

    def run(
        self,
        task: RuntimeTask,
        *,
        recorder: RunRecorder,
        resource_limits: ResourceLimits,
    ) -> AgenticRunResult:
        """Execute one task and return a validated record for every outcome."""

        if recorder.task_id != task.task_id:
            raise ValueError("Recorder task_id does not match RuntimeTask")
        if recorder.execution_mode == "engineering" and recorder.condition is not None:
            raise ValueError("Engineering runs require condition=None")
        if recorder.execution_mode == "benchmark" and recorder.condition not in {
            "B1",
            "G1",
        }:
            raise ValueError("Agentic benchmark runs require condition B1 or G1")

        state = initial_workflow_state(
            task_id=task.task_id,
            question=task.question,
            execution_mode=recorder.execution_mode,
            condition_metadata=recorder.condition,
            ResourceLimits=resource_limits,
        )
        tracker = _StateTracker(state)
        initial_errors = len(
            recorder.build_record(status="failed", answer=None, abstained=False)[
                "errors"
            ]
        )

        try:
            assembler = AgenticNodeAssembler(
                model=self._model,
                retriever=self._retriever,
                recovery_policy=self._recovery_policy,
                recorder=recorder,
                top_k=self._top_k,
            )
            graph = build_graph(tracker.components(assembler.components()))
            # Graph output includes the frozen finalizers and is authoritative.
            final_state = deepcopy(graph.invoke(state))
            status = final_state["terminal_status"]
            answer = final_state["final_answer"]
            abstained = final_state["abstained_flag"]
            if status in {"completed", "completed_after_recovery"}:
                event_type = "abstained" if abstained else "answer_accepted"
            elif status == "resource_stopped":
                event_type = "resource_stopped"
            else:
                raise ValueError(f"Unsupported graph terminal status: {status!r}")
            record_workflow_event(recorder=recorder, event_type=event_type)
        except ExecutionResourceStop as exc:
            final_state = deepcopy(tracker.latest_state)
            final_state.update(
                terminal_status="resource_stopped",
                final_answer=None,
                abstained_flag=False,
            )
            status, answer, abstained = "resource_stopped", None, False
            record_workflow_event(
                recorder=recorder,
                event_type="resource_stopped",
                stage=exc.stage,
                details={
                    "blocked_stage": exc.stage,
                    "blocked_limits": [limit.value for limit in exc.blocked_limits],
                },
            )
        except Exception as exc:
            final_state = deepcopy(tracker.latest_state)
            new_errors = recorder.build_record(
                status="failed", answer=None, abstained=False
            )["errors"][initial_errors:]
            error_type = type(exc).__name__
            message = str(exc) or repr(exc)
            if not any(
                error["error_type"] == error_type and error["message"] == message
                for error in new_errors
            ):
                recorder.record_error(
                    error_type=error_type,
                    message=message,
                    stage=tracker.active_stage or "workflow",
                    retryable=None,
                )
            status = (
                "tool_error"
                if any(error["stage"] in {"model", "retrieval"} for error in new_errors)
                else "failed"
            )
            answer, abstained = None, False
            final_state.update(
                terminal_status=status,
                final_answer=answer,
                abstained_flag=abstained,
            )
            record_workflow_event(
                recorder=recorder,
                event_type="workflow_failed",
                stage=tracker.active_stage,
            )

        record = recorder.build_record(
            status=status,
            answer=answer,
            abstained=abstained,
            cited_chunk_ids=(),
            tool_calls=0,
            retries=final_state["recovery_iteration"],
        )
        validate_run_record(record)
        return AgenticRunResult(
            final_answer=answer,
            abstained=abstained,
            terminal_status=status,
            record=record,
            final_state=final_state,
        )
