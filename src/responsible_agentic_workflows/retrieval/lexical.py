"""Deterministic lexical retrieval for engineering validation only."""

import re
from collections.abc import Iterable

from responsible_agentic_workflows.ingestion import DocumentChunk

from .models import RetrievedChunk

_TOKEN_PATTERN = re.compile(r"[a-z0-9]+(?:'[a-z0-9]+)?")

_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "before",
        "by",
        "for",
        "from",
        "how",
        "in",
        "is",
        "it",
        "must",
        "of",
        "on",
        "or",
        "the",
        "to",
        "what",
        "when",
        "which",
        "who",
        "with",
    }
)


def _tokens(text: str) -> frozenset[str]:
    return frozenset(
        token
        for token in _TOKEN_PATTERN.findall(text.lower())
        if token not in _STOPWORDS
    )


class LexicalRetriever:
    """Simple deterministic overlap retriever for engineering tests.

    This implementation is intentionally framework-neutral and must not be
    described as the thesis B0 reference baseline. It exists to validate the
    ingestion, retrieval, provenance, and logging pipeline before external
    retrieval components are introduced.
    """

    CONFIG_ID = "engineering-lexical-overlap-v0.1"

    def __init__(self, chunks: Iterable[DocumentChunk]) -> None:
        ordered_chunks = tuple(chunks)

        if not ordered_chunks:
            raise ValueError("At least one chunk is required")

        chunk_ids = [chunk.chunk_id for chunk in ordered_chunks]

        if len(chunk_ids) != len(set(chunk_ids)):
            raise ValueError("Duplicate chunk IDs detected")

        self._chunks = ordered_chunks

        self._token_index = {
            chunk.chunk_id: _tokens(
                " ".join(
                    (
                        chunk.title,
                        chunk.section,
                        chunk.text,
                    )
                )
            )
            for chunk in ordered_chunks
        }

        self._section_token_index = {
            chunk.chunk_id: _tokens(chunk.section)
            for chunk in ordered_chunks
        }

    @property
    def config_id(self) -> str:
        return self.CONFIG_ID

    def retrieve(
        self,
        query: str,
        *,
        top_k: int,
    ) -> tuple[RetrievedChunk, ...]:
        if not query.strip():
            raise ValueError("Query must not be empty")

        if top_k < 1:
            raise ValueError("top_k must be at least 1")

        query_tokens = _tokens(query)

        scored: list[tuple[float, str, DocumentChunk]] = []

        for chunk in self._chunks:
            chunk_tokens = self._token_index[chunk.chunk_id]
            section_tokens = self._section_token_index[chunk.chunk_id]

            content_overlap = query_tokens & chunk_tokens
            section_overlap = query_tokens & section_tokens

            if query_tokens:
                score = (
                    len(content_overlap)
                    + (2 * len(section_overlap))
                ) / (3 * len(query_tokens))
            else:
                score = 0.0

            scored.append(
                (
                    score,
                    chunk.chunk_id,
                    chunk,
                )
            )

        scored.sort(
            key=lambda item: (
                -item[0],
                item[1],
            )
        )

        selected = scored[: min(top_k, len(scored))]

        return tuple(
            RetrievedChunk(
                chunk=chunk,
                rank=rank,
                score=score,
            )
            for rank, (score, _, chunk) in enumerate(
                selected,
                start=1,
            )
        )
