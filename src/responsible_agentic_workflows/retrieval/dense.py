"""Exact dense cosine retrieval over precomputed document embeddings."""

from collections.abc import Iterable, Sequence

import numpy as np
from numpy.typing import NDArray

from responsible_agentic_workflows.ingestion import DocumentChunk

from .embedding import EmbeddingClient
from .models import RetrievedChunk


class DenseExactRetriever:
    """Rank precomputed chunk embeddings using exact cosine similarity."""

    def __init__(
        self,
        *,
        chunks: Iterable[DocumentChunk],
        embeddings: Sequence[Sequence[float]]
        | NDArray[np.float32],
        query_embedder: EmbeddingClient,
        config_id: str,
    ) -> None:
        ordered_chunks = tuple(chunks)

        if not ordered_chunks:
            raise ValueError(
                "At least one chunk is required"
            )

        if not config_id.strip():
            raise ValueError(
                "Retrieval config ID must not be empty"
            )

        chunk_ids = [
            chunk.chunk_id
            for chunk in ordered_chunks
        ]

        if len(chunk_ids) != len(set(chunk_ids)):
            raise ValueError(
                "Duplicate chunk IDs detected"
            )

        matrix = np.asarray(
            embeddings,
            dtype=np.float32,
        )

        if matrix.ndim != 2:
            raise ValueError(
                "Document embeddings must be a two-dimensional matrix"
            )

        if matrix.shape[0] != len(ordered_chunks):
            raise ValueError(
                "Embedding row count must match chunk count"
            )

        if matrix.shape[1] != query_embedder.dimensions:
            raise ValueError(
                "Document embedding dimensionality does not match "
                "the query embedder"
            )

        if not np.isfinite(matrix).all():
            raise ValueError(
                "Document embeddings contain non-finite values"
            )

        norms = np.linalg.norm(
            matrix,
            axis=1,
        )

        if np.any(norms == 0):
            raise ValueError(
                "Document embeddings must have non-zero norms"
            )

        normalized = (
            matrix
            / norms[:, np.newaxis]
        ).astype(
            np.float32,
            copy=False,
        )

        self._chunks = ordered_chunks
        self._matrix = np.ascontiguousarray(
            normalized,
            dtype=np.float32,
        )
        self._query_embedder = query_embedder
        self._config_id = config_id

    @property
    def config_id(self) -> str:
        return self._config_id

    def retrieve(
        self,
        query: str,
        *,
        top_k: int,
    ) -> tuple[RetrievedChunk, ...]:
        if not query.strip():
            raise ValueError(
                "Query must not be empty"
            )

        if top_k < 1:
            raise ValueError(
                "top_k must be at least 1"
            )

        query_vector = np.asarray(
            self._query_embedder.embed_query(query),
            dtype=np.float32,
        )

        expected_shape = (
            self._matrix.shape[1],
        )

        if query_vector.shape != expected_shape:
            raise ValueError(
                "Query embedding dimensionality does not match "
                "the document index"
            )

        if not np.isfinite(query_vector).all():
            raise ValueError(
                "Query embedding contains non-finite values"
            )

        query_norm = float(
            np.linalg.norm(query_vector)
        )

        if query_norm == 0:
            raise ValueError(
                "Query embedding must have a non-zero norm"
            )

        normalized_query = (
            query_vector / query_norm
        ).astype(
            np.float32,
            copy=False,
        )

        scores = self._matrix @ normalized_query

        ranked_indices = sorted(
            range(len(self._chunks)),
            key=lambda index: (
                -float(scores[index]),
                self._chunks[index].chunk_id,
            ),
        )

        selected = ranked_indices[
            : min(top_k, len(ranked_indices))
        ]

        return tuple(
            RetrievedChunk(
                chunk=self._chunks[index],
                rank=rank,
                score=float(scores[index]),
            )
            for rank, index in enumerate(
                selected,
                start=1,
            )
        )
