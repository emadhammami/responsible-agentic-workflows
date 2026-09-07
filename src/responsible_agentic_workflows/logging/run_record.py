"""Raw execution run recording and schema validation."""

import json
from copy import deepcopy
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter_ns
from typing import Literal

from jsonschema import Draft202012Validator, FormatChecker

from responsible_agentic_workflows.modeling import TokenUsage
from responsible_agentic_workflows.retrieval import RetrievedChunk

Condition = Literal["B0", "B1", "G1"]
ExecutionMode = Literal["engineering", "benchmark"]

RunStatus = Literal[
    "completed",
    "completed_after_recovery",
    "resource_stopped",
    "tool_error",
    "failed",
]

DEFAULT_RUN_SCHEMA = Path("benchmark/schema/run.schema.json")


def _utc_now() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def _elapsed_ms(start_ns: int) -> float:
    return max(
        0.0,
        (perf_counter_ns() - start_ns) / 1_000_000,
    )


@dataclass(frozen=True, slots=True)
class RunConfiguration:
    """Configuration fields stored with every raw benchmark run."""

    model_provider: str
    model_name: str
    model_config_id: str
    temperature: float | None
    prompt_version: str
    retrieval_config_id: str
    model_version: str | None = None
    max_output_tokens: int | None = None
    workflow_config_id: str | None = None
    random_seed: int | None = None

    def as_dict(self) -> dict[str, object]:
        """Return the schema-compatible configuration representation."""

        return {
            "model_provider": self.model_provider,
            "model_name": self.model_name,
            "model_config_id": self.model_config_id,
            "model_version": self.model_version,
            "temperature": self.temperature,
            "max_output_tokens": self.max_output_tokens,
            "prompt_version": self.prompt_version,
            "retrieval_config_id": self.retrieval_config_id,
            "workflow_config_id": self.workflow_config_id,
            "random_seed": self.random_seed,
        }


class RunRecorder:
    """Accumulate raw execution data without benchmark gold information."""

    def __init__(
        self,
        *,
        run_id: str,
        experiment_id: str,
        task_id: str,
        execution_mode: ExecutionMode,
        condition: Condition | None,
        code_revision: str,
        configuration: RunConfiguration,
    ) -> None:
        if not run_id:
            raise ValueError("run_id must not be empty")

        if not experiment_id:
            raise ValueError("experiment_id must not be empty")

        if execution_mode not in {"engineering", "benchmark"}:
            raise ValueError(
                f"Unsupported execution mode: {execution_mode}"
            )

        if execution_mode == "benchmark":
            if condition not in {"B0", "B1", "G1"}:
                raise ValueError(
                    "Benchmark runs require condition B0, B1, or G1"
                )
        elif condition is not None:
            raise ValueError(
                "Engineering runs require condition=None"
            )

        if len(code_revision) < 7:
            raise ValueError("code_revision must contain at least 7 characters")

        self.run_id = run_id
        self.experiment_id = experiment_id
        self.task_id = task_id
        self.execution_mode = execution_mode
        self.condition = condition
        self.code_revision = code_revision
        self.configuration = configuration

        self._started_at = _utc_now()
        self._started_ns = perf_counter_ns()

        self._retrieval_calls: list[dict[str, object]] = []
        self._model_calls: list[dict[str, object]] = []
        self._events: list[dict[str, object]] = []
        self._errors: list[dict[str, object]] = []

    @property
    def retrieval_call_count(self) -> int:
        """Return the number of retrieval attempts recorded so far."""

        return len(self._retrieval_calls)

    def record_retrieval(
        self,
        *,
        query: str,
        top_k: int,
        latency_ms: float,
        results: tuple[RetrievedChunk, ...],
    ) -> None:
        """Record one retrieval attempt and its ranked provenance."""

        if not query.strip():
            raise ValueError("Retrieval query must not be empty")

        if top_k < 1:
            raise ValueError("top_k must be at least 1")

        if latency_ms < 0:
            raise ValueError("latency_ms must not be negative")

        retrieved_chunks = [
            {
                "document_id": result.chunk.document_id,
                "chunk_id": result.chunk.chunk_id,
                "page": result.chunk.page,
                "section": result.chunk.section,
                "rank": result.rank,
                "retrieval_score": result.score,
            }
            for result in results
        ]

        self._retrieval_calls.append(
            {
                "sequence": len(self._retrieval_calls) + 1,
                "query": query,
                "top_k": top_k,
                "latency_ms": latency_ms,
                "retrieved_chunks": retrieved_chunks,
            }
        )

    @property
    def model_call_count(self) -> int:
        """Return the number of model-call attempts recorded so far."""

        return len(self._model_calls)

    def record_model_call(
        self,
        *,
        status: Literal["completed", "failed"],
        latency_ms: float,
        usage: TokenUsage | None,
        finish_reason: str | None,
        provider_response_id: str | None,
    ) -> None:
        """Record one model-call attempt and its resource measurements."""

        if status not in {"completed", "failed"}:
            raise ValueError(f"Unsupported model-call status: {status}")

        if latency_ms < 0:
            raise ValueError("latency_ms must not be negative")

        if status == "completed" and usage is None:
            raise ValueError(
                "Completed model calls require token usage"
            )

        if usage is None:
            input_tokens = None
            output_tokens = None
            total_tokens = None
        else:
            input_tokens = usage.input_tokens
            output_tokens = usage.output_tokens
            total_tokens = usage.total_tokens

        self._model_calls.append(
            {
                "sequence": len(self._model_calls) + 1,
                "status": status,
                "latency_ms": latency_ms,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens,
                "finish_reason": finish_reason,
                "provider_response_id": provider_response_id,
            }
        )

    def record_error(
        self,
        *,
        error_type: str,
        message: str,
        stage: str | None,
        retryable: bool | None,
    ) -> None:
        """Record one runtime error without benchmark evaluation data."""

        if not error_type:
            raise ValueError("error_type must not be empty")

        if not message:
            raise ValueError("message must not be empty")

        self._errors.append(
            {
                "error_type": error_type,
                "stage": stage,
                "message": message,
                "retryable": retryable,
            }
        )

    def build_record(
        self,
        *,
        status: RunStatus,
        answer: str | None,
        abstained: bool,
        cited_chunk_ids: tuple[str, ...] = (),
        tool_calls: int = 0,
        retries: int = 0,
    ) -> dict[str, object]:
        """Build one complete raw run record."""

        counters = {
            "tool_calls": tool_calls,
            "retries": retries,
        }

        for name, value in counters.items():
            if value < 0:
                raise ValueError(f"{name} must not be negative")

        if len(cited_chunk_ids) != len(set(cited_chunk_ids)):
            raise ValueError("cited_chunk_ids contains duplicates")

        retrieval_ms = sum(
            float(call["latency_ms"])
            for call in self._retrieval_calls
        )

        llm_ms = sum(
            float(call["latency_ms"])
            for call in self._model_calls
        )

        input_tokens = sum(
            int(call["input_tokens"])
            for call in self._model_calls
            if call["input_tokens"] is not None
        )

        output_tokens = sum(
            int(call["output_tokens"])
            for call in self._model_calls
            if call["output_tokens"] is not None
        )

        return {
            "schema_version": "0.4",
            "run_id": self.run_id,
            "experiment_id": self.experiment_id,
            "task_id": self.task_id,
            "execution_mode": self.execution_mode,
            "condition": self.condition,
            "started_at": self._started_at,
            "finished_at": _utc_now(),
            "status": status,
            "code_revision": self.code_revision,
            "configuration": self.configuration.as_dict(),
            "retrieval": {
                "calls": deepcopy(self._retrieval_calls),
            },
            "model": {
                "calls": deepcopy(self._model_calls),
            },
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens,
                "llm_calls": len(self._model_calls),
                "retrieval_calls": len(self._retrieval_calls),
                "tool_calls": tool_calls,
                "retries": retries,
            },
            "timing": {
                "end_to_end_ms": _elapsed_ms(self._started_ns),
                "retrieval_ms": retrieval_ms,
                "llm_ms": llm_ms,
            },
            "final_output": {
                "answer": answer,
                "abstained": abstained,
                "cited_chunk_ids": list(cited_chunk_ids),
            },
            "events": deepcopy(self._events),
            "errors": deepcopy(self._errors),
        }


def validate_run_record(
    record: dict[str, object],
    *,
    schema_path: str | Path = DEFAULT_RUN_SCHEMA,
) -> None:
    """Validate one run against the frozen JSON Schema contract."""

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    validator.validate(record)


def write_validated_run_record(
    record: dict[str, object],
    output_path: str | Path,
    *,
    schema_path: str | Path = DEFAULT_RUN_SCHEMA,
) -> Path:
    """Validate and atomically write one raw run artifact.

    Existing run files are never overwritten.
    """

    validate_run_record(
        record,
        schema_path=schema_path,
    )

    output = Path(output_path)

    if output.exists():
        raise FileExistsError(
            f"Run artifact already exists: {output}"
        )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary = output.with_name(
        f".{output.name}.tmp"
    )

    temporary.write_text(
        json.dumps(
            record,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary.replace(output)

    return output
