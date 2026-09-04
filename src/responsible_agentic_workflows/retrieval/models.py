"""Framework-neutral retrieval contracts."""

from dataclasses import dataclass
from typing import Protocol

from responsible_agentic_workflows.ingestion import DocumentChunk


@dataclass(frozen=True, slots=True)
class RetrievedChunk:
    """One ranked retrieval result with preserved source provenance."""

    chunk: DocumentChunk
    rank: int
    score: float


class Retriever(Protocol):
    """Common retrieval interface used by benchmark workflow conditions."""

    @property
    def config_id(self) -> str:
        """Return a stable retrieval configuration identifier."""
        ...

    def retrieve(
        self,
        query: str,
        *,
        top_k: int,
    ) -> tuple[RetrievedChunk, ...]:
        """Return ranked chunks for one runtime query."""
        ...
