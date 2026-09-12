from collections.abc import Sequence

import numpy as np
import pytest
from numpy.typing import NDArray

from responsible_agentic_workflows.ingestion import (
    DocumentChunk,
)
from responsible_agentic_workflows.retrieval import (
    DenseExactRetriever,
)


class _FakeEmbeddingClient:
    def __init__(
        self,
        vector: Sequence[float],
        *,
        dimensions: int | None = None,
    ) -> None:
        self._vector = np.asarray(
            vector,
            dtype=np.float32,
        )
        self._dimensions = (
            len(vector)
            if dimensions is None
            else dimensions
        )

    @property
    def dimensions(self) -> int:
        return self._dimensions

    def embed_query(
        self,
        query: str,
    ) -> NDArray[np.float32]:
        del query
        return self._vector.copy()

    def embed_documents(
        self,
        texts: Sequence[str],
    ) -> NDArray[np.float32]:
        return np.zeros(
            (
                len(texts),
                self._dimensions,
            ),
            dtype=np.float32,
        )


def _chunk(
    chunk_id: str,
    *,
    page: int = 1,
) -> DocumentChunk:
    return DocumentChunk(
        document_id="DOC999",
        chunk_id=chunk_id,
        title="Synthetic policy",
        section=f"Page {page}",
        section_index=page,
        text=f"Text for {chunk_id}",
        source_file="DOC999.pdf",
        page=page,
    )


def test_exact_cosine_ranking_preserves_provenance() -> None:
    chunks = (
        _chunk("DOC999-P0001-C001"),
        _chunk("DOC999-P0002-C001", page=2),
        _chunk("DOC999-P0003-C001", page=3),
    )

    embeddings = np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.8, 0.2, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=np.float32,
    )

    retriever = DenseExactRetriever(
        chunks=chunks,
        embeddings=embeddings,
        query_embedder=_FakeEmbeddingClient(
            [1.0, 0.0, 0.0]
        ),
        config_id="dense-test-v0.1",
    )

    results = retriever.retrieve(
        "policy question",
        top_k=2,
    )

    assert [
        result.chunk.chunk_id
        for result in results
    ] == [
        "DOC999-P0001-C001",
        "DOC999-P0002-C001",
    ]

    assert [
        result.rank
        for result in results
    ] == [1, 2]

    assert results[0].chunk.page == 1
    assert results[1].chunk.page == 2
    assert results[0].score == pytest.approx(1.0)


def test_cosine_ranking_normalizes_document_magnitude() -> None:
    chunks = (
        _chunk("DOC999-P0001-C001"),
        _chunk("DOC999-P0002-C001", page=2),
    )

    retriever = DenseExactRetriever(
        chunks=chunks,
        embeddings=[
            [10.0, 0.0],
            [1.0, 1.0],
        ],
        query_embedder=_FakeEmbeddingClient(
            [1.0, 0.0]
        ),
        config_id="dense-test-v0.1",
    )

    results = retriever.retrieve(
        "query",
        top_k=2,
    )

    assert results[0].chunk.chunk_id == (
        "DOC999-P0001-C001"
    )
    assert results[0].score == pytest.approx(1.0)
    assert results[1].score < results[0].score


def test_equal_scores_use_chunk_id_tie_break() -> None:
    chunks = (
        _chunk("DOC999-P0002-C001", page=2),
        _chunk("DOC999-P0001-C001"),
    )

    retriever = DenseExactRetriever(
        chunks=chunks,
        embeddings=[
            [1.0, 0.0],
            [1.0, 0.0],
        ],
        query_embedder=_FakeEmbeddingClient(
            [1.0, 0.0]
        ),
        config_id="dense-test-v0.1",
    )

    results = retriever.retrieve(
        "query",
        top_k=2,
    )

    assert [
        result.chunk.chunk_id
        for result in results
    ] == [
        "DOC999-P0001-C001",
        "DOC999-P0002-C001",
    ]


def test_duplicate_chunk_ids_are_rejected() -> None:
    chunks = (
        _chunk("DOC999-P0001-C001"),
        _chunk("DOC999-P0001-C001"),
    )

    with pytest.raises(
        ValueError,
        match="Duplicate chunk IDs",
    ):
        DenseExactRetriever(
            chunks=chunks,
            embeddings=[
                [1.0, 0.0],
                [0.0, 1.0],
            ],
            query_embedder=_FakeEmbeddingClient(
                [1.0, 0.0]
            ),
            config_id="dense-test-v0.1",
        )


def test_embedding_row_count_must_match_chunks() -> None:
    with pytest.raises(
        ValueError,
        match="row count",
    ):
        DenseExactRetriever(
            chunks=(
                _chunk("DOC999-P0001-C001"),
            ),
            embeddings=[
                [1.0, 0.0],
                [0.0, 1.0],
            ],
            query_embedder=_FakeEmbeddingClient(
                [1.0, 0.0]
            ),
            config_id="dense-test-v0.1",
        )


def test_invalid_retrieval_arguments_are_rejected() -> None:
    retriever = DenseExactRetriever(
        chunks=(
            _chunk("DOC999-P0001-C001"),
        ),
        embeddings=[
            [1.0, 0.0],
        ],
        query_embedder=_FakeEmbeddingClient(
            [1.0, 0.0]
        ),
        config_id="dense-test-v0.1",
    )

    with pytest.raises(
        ValueError,
        match="Query must not be empty",
    ):
        retriever.retrieve(
            "",
            top_k=1,
        )

    with pytest.raises(
        ValueError,
        match="top_k must be at least 1",
    ):
        retriever.retrieve(
            "query",
            top_k=0,
        )


def test_runtime_query_dimension_mismatch_is_rejected() -> None:
    retriever = DenseExactRetriever(
        chunks=(
            _chunk("DOC999-P0001-C001"),
        ),
        embeddings=[
            [1.0, 0.0],
        ],
        query_embedder=_FakeEmbeddingClient(
            [1.0, 0.0, 0.0],
            dimensions=2,
        ),
        config_id="dense-test-v0.1",
    )

    with pytest.raises(
        ValueError,
        match="Query embedding dimensionality",
    ):
        retriever.retrieve(
            "query",
            top_k=1,
        )
