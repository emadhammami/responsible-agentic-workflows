from dataclasses import dataclass

from langchain_core.runnables import RunnableLambda

from responsible_agentic_workflows.benchmark import RuntimeTask
from responsible_agentic_workflows.logging import (
    LoggedLanguageModel,
    LoggedRetriever,
    RunRecorder,
)
from responsible_agentic_workflows.modeling import (
    LanguageModel,
    ModelMessage,
    ModelRequest,
    TokenUsage,
)
from responsible_agentic_workflows.retrieval import RetrievedChunk, Retriever

PROMPT_VERSION = "b0-engineering-v0.1"
WORKFLOW_CONFIG_ID = "b0-two-step-rag-v0.1"

_SYSTEM_PROMPT = (
    "You are a careful document assistant. "
    "Answer using only the retrieved context."
)


@dataclass(frozen=True, slots=True)
class B0Result:
    answer: str
    chunks: tuple[RetrievedChunk, ...]
    usage: TokenUsage
    finish_reason: str | None
    record: dict[str, object]


def _format_context(
    results: list[RetrievedChunk],
) -> str:
    blocks: list[str] = []

    for result in results:
        chunk = result.chunk
        page = "unknown" if chunk.page is None else str(chunk.page)

        blocks.append(
            f"[rank={result.rank}; "
            f"document_id={chunk.document_id}; "
            f"chunk_id={chunk.chunk_id}; "
            f"page={page}; "
            f"section={chunk.section}]\n"
            f"{chunk.text}"
        )

    return "\n\n".join(blocks)


def _user_prompt(
    question: str,
    results: list[RetrievedChunk],
) -> str:
    context = _format_context(results)

    return (
        "Retrieved context:\n"
        f"{context}\n\n"
        f"Question: {question}\n\n"
        "Answer using only the retrieved context."
    )


def _make_retrieve_step(logged_retriever: LoggedRetriever):
    def retrieve_step(
        payload: dict[str, object],
    ) -> dict[str, object]:
        results = logged_retriever.retrieve(
            str(payload["question"]),
            top_k=int(payload["top_k"]),
        )

        return {
            "question": payload["question"],
            "context": _format_context(list(results)),
            "chunks": list(results),
        }

    return retrieve_step


def _make_generate_step(
    logged_model: LoggedLanguageModel,
    *,
    temperature: float | None,
    max_output_tokens: int | None,
):
    def generate_step(
        payload: dict[str, object],
    ) -> dict[str, object]:
        request = ModelRequest(
            messages=(
                ModelMessage(
                    role="system",
                    content=_SYSTEM_PROMPT,
                ),
                ModelMessage(
                    role="user",
                    content=(
                        _user_prompt(
                            str(payload["question"]),
                            list(payload["chunks"]),
                        )
                    ),
                ),
            ),
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

        response = logged_model.generate(request)

        return {
            "answer": response.text,
            "chunks": payload["chunks"],
            "usage": response.usage,
            "finish_reason": response.finish_reason,
        }

    return generate_step


class B0Baseline:
    PROMPT_VERSION = PROMPT_VERSION
    WORKFLOW_CONFIG_ID = WORKFLOW_CONFIG_ID

    def __init__(
        self,
        *,
        retriever: Retriever,
        model: LanguageModel,
        top_k: int = 3,
    ) -> None:
        if top_k < 1:
            raise ValueError("top_k must be at least 1")
        if not callable(getattr(retriever, "retrieve", None)):
            raise TypeError("retriever must expose a callable retrieve")
        if not isinstance(model, LanguageModel):
            raise TypeError("model must satisfy the LanguageModel contract")

        self._retriever = retriever
        self._model = model
        self._top_k = top_k

    @property
    def top_k(self) -> int:
        return self._top_k

    def run(
        self,
        task: RuntimeTask,
        *,
        recorder: RunRecorder,
        top_k: int | None = None,
    ) -> B0Result:
        effective_top_k = top_k if top_k is not None else self._top_k

        if effective_top_k < 1:
            raise ValueError("top_k must be at least 1")

        configuration = recorder.configuration

        if recorder.task_id != task.task_id:
            raise ValueError(
                "Recorder task_id does not match RuntimeTask"
            )

        if (
            recorder.execution_mode == "benchmark"
            and recorder.condition != "B0"
        ):
            raise ValueError(
                "B0 benchmark execution requires condition B0"
            )

        if configuration.prompt_version != self.PROMPT_VERSION:
            raise ValueError(
                "Recorder prompt_version does not match B0 prompt"
            )

        if configuration.workflow_config_id != self.WORKFLOW_CONFIG_ID:
            raise ValueError(
                "Recorder workflow_config_id does not match B0 workflow"
            )

        logged_retriever = LoggedRetriever(
            self._retriever,
            recorder,
        )

        logged_model = LoggedLanguageModel(
            self._model,
            recorder,
        )

        retrieve_step = _make_retrieve_step(logged_retriever)

        generate_step = _make_generate_step(
            logged_model,
            temperature=configuration.temperature,
            max_output_tokens=configuration.max_output_tokens,
        )

        chain = RunnableLambda(retrieve_step) | RunnableLambda(
            generate_step
        )

        output = chain.invoke(
            {
                "question": task.question,
                "top_k": effective_top_k,
            }
        )

        chunks = tuple(output["chunks"])

        record = recorder.build_record(
            status="completed",
            answer=str(output["answer"]),
            abstained=False,
            cited_chunk_ids=(),
            tool_calls=0,
            retries=0,
        )

        return B0Result(
            answer=str(output["answer"]),
            chunks=chunks,
            usage=output["usage"],
            finish_reason=output.get("finish_reason"),
            record=record,
        )
