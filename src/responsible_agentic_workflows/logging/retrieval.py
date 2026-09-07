"""Retrieval wrapper that records every retrieval attempt."""

from time import perf_counter_ns

from responsible_agentic_workflows.retrieval import (
    RetrievedChunk,
    Retriever,
)

from .run_record import RunRecorder


def _elapsed_ms(start_ns: int) -> float:
    return max(
        0.0,
        (perf_counter_ns() - start_ns) / 1_000_000,
    )


class LoggedRetriever:
    """Wrap a retriever and preserve a per-call execution trace."""

    def __init__(
        self,
        retriever: Retriever,
        recorder: RunRecorder,
    ) -> None:
        if (
            recorder.configuration.retrieval_config_id
            != retriever.config_id
        ):
            raise ValueError(
                "Recorder retrieval_config_id does not match retriever"
            )

        self._retriever = retriever
        self._recorder = recorder

    @property
    def config_id(self) -> str:
        """Expose the wrapped retrieval configuration identifier."""

        return self._retriever.config_id

    def retrieve(
        self,
        query: str,
        *,
        top_k: int,
    ) -> tuple[RetrievedChunk, ...]:
        """Retrieve and record provenance, rank, score, and latency."""

        started_ns = perf_counter_ns()

        try:
            results = self._retriever.retrieve(
                query,
                top_k=top_k,
            )
        except Exception as exc:
            latency_ms = _elapsed_ms(started_ns)

            # Only schema-valid retrieval attempts become retrieval-call
            # records. Invalid invocation parameters are preserved as errors
            # without creating a malformed raw run artifact.
            if query.strip() and top_k >= 1:
                self._recorder.record_retrieval(
                    query=query,
                    top_k=top_k,
                    latency_ms=latency_ms,
                    results=(),
                )

            self._recorder.record_error(
                error_type=type(exc).__name__,
                message=str(exc),
                stage="retrieval",
                retryable=None,
            )

            raise

        latency_ms = _elapsed_ms(started_ns)

        self._recorder.record_retrieval(
            query=query,
            top_k=top_k,
            latency_ms=latency_ms,
            results=results,
        )

        return results
