import hashlib
import json
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pytest
from numpy.typing import NDArray

from responsible_agentic_workflows.retrieval.materialize import (
    load_ordered_chunks,
    materialize_embedding_artifacts,
)


class _FakeEmbeddingClient:
    def __init__(
        self,
        *,
        dimensions: int = 3,
    ) -> None:
        self._dimensions = dimensions
        self.batch_sizes: list[int] = []

    @property
    def dimensions(self) -> int:
        return self._dimensions

    def embed_query(
        self,
        query: str,
    ) -> NDArray[np.float32]:
        del query
        return np.ones(
            self._dimensions,
            dtype=np.float32,
        )

    def embed_documents(
        self,
        texts: Sequence[str],
    ) -> NDArray[np.float32]:
        self.batch_sizes.append(
            len(texts)
        )

        rows = []

        for index, _ in enumerate(
            texts,
            start=1,
        ):
            vector = np.zeros(
                self._dimensions,
                dtype=np.float32,
            )

            vector[
                (index - 1)
                % self._dimensions
            ] = 1.0

            rows.append(vector)

        return np.stack(rows)


def _sha256(path: Path) -> str:
    return hashlib.sha256(
        path.read_bytes()
    ).hexdigest()


def _write_fixture(
    root: Path,
) -> tuple[Path, Path]:
    chunk_directory = (
        root / "chunks"
    )
    chunk_directory.mkdir()

    artifact = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "document_id": "DOC001",
        "title": "Synthetic",
        "source_sha256": "a" * 64,
        "chunking_config_id": "chunk-v1",
        "chunk_count": 3,
        "chunks": [
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0001-C001"
                ),
                "title": "Synthetic",
                "section": "Page 1",
                "section_index": 1,
                "text": "First text",
                "source_file": "DOC001.pdf",
                "page": 1,
            },
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0001-C002"
                ),
                "title": "Synthetic",
                "section": "Page 1",
                "section_index": 1,
                "text": "Second text",
                "source_file": "DOC001.pdf",
                "page": 1,
            },
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0002-C001"
                ),
                "title": "Synthetic",
                "section": "Page 2",
                "section_index": 2,
                "text": "Third text",
                "source_file": "DOC001.pdf",
                "page": 2,
            },
        ],
    }

    artifact_path = (
        chunk_directory
        / "DOC001.chunks.json"
    )

    artifact_path.write_text(
        json.dumps(
            artifact,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    index = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "status": "working",
        "artifact_type": "retrieval_chunks",
        "chunking_config_id": "chunk-v1",
        "document_count": 1,
        "total_chunks": 3,
        "documents": [
            {
                "document_id": "DOC001",
                "artifact_file": (
                    "DOC001.chunks.json"
                ),
                "source_sha256": "a" * 64,
                "page_count": 2,
                "chunk_count": 3,
            }
        ],
    }

    (
        chunk_directory
        / "index.json"
    ).write_text(
        json.dumps(
            index,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    config_path = (
        root / "retrieval.json"
    )

    config = {
        "schema_version": "0.1",
        "retrieval_config_id": "retrieval-v1",
        "status": "working",
        "backend": "dense-exact-cosine",
        "chunking_config_id": "chunk-v1",
        "embedding": {
            "provider": "fake",
            "model_name": "fake-model",
            "model_tag": "fake-model:v1",
            "model_digest": "b" * 64,
            "provider_version": "1.0",
            "output_dimensions": 3,
            "normalized": True,
            "truncate": False,
            "query_instruction": None,
            "document_instruction": None,
        },
        "index": {
            "backend": "numpy",
            "backend_version": np.__version__,
            "index_type": "flat-exact",
            "distance_metric": "cosine",
            "dtype": "float32",
        },
    }

    config_path.write_text(
        json.dumps(
            config,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    return (
        chunk_directory,
        config_path,
    )


def test_load_ordered_chunks_preserves_index_order(
    tmp_path: Path,
) -> None:
    chunk_directory, _ = (
        _write_fixture(tmp_path)
    )

    chunks, index = (
        load_ordered_chunks(
            chunk_directory
        )
    )

    assert index["total_chunks"] == 3
    assert [
        chunk.chunk_id
        for chunk in chunks
    ] == [
        "DOC001-P0001-C001",
        "DOC001-P0001-C002",
        "DOC001-P0002-C001",
    ]


def test_materialization_writes_bound_artifacts(
    tmp_path: Path,
) -> None:
    chunk_directory, config_path = (
        _write_fixture(tmp_path)
    )

    output_directory = (
        tmp_path / "embeddings"
    )

    client = _FakeEmbeddingClient()

    metadata = (
        materialize_embedding_artifacts(
            chunk_directory=chunk_directory,
            retrieval_config_path=(
                config_path
            ),
            output_directory=(
                output_directory
            ),
            embedding_client=client,
            batch_size=2,
        )
    )

    assert client.batch_sizes == [2, 1]

    matrix_path = (
        output_directory
        / "embeddings.npy"
    )

    chunk_ids_path = (
        output_directory
        / "chunk_ids.json"
    )

    metadata_path = (
        output_directory
        / "metadata.json"
    )

    assert matrix_path.is_file()
    assert chunk_ids_path.is_file()
    assert metadata_path.is_file()

    matrix = np.load(
        matrix_path,
        allow_pickle=False,
    )

    assert matrix.shape == (3, 3)
    assert matrix.dtype == np.float32

    chunk_ids = json.loads(
        chunk_ids_path.read_text(
            encoding="utf-8"
        )
    )

    assert chunk_ids["chunk_ids"] == [
        "DOC001-P0001-C001",
        "DOC001-P0001-C002",
        "DOC001-P0002-C001",
    ]

    assert metadata["chunk_count"] == 3
    assert metadata["dimensions"] == 3
    assert metadata["dtype"] == "float32"
    assert metadata["batch_size"] == 2
    assert metadata["embeddings_sha256"] == (
        _sha256(matrix_path)
    )
    assert metadata["chunk_ids_sha256"] == (
        _sha256(chunk_ids_path)
    )


def test_existing_artifacts_are_not_overwritten(
    tmp_path: Path,
) -> None:
    chunk_directory, config_path = (
        _write_fixture(tmp_path)
    )

    output_directory = (
        tmp_path / "embeddings"
    )

    output_directory.mkdir()

    (
        output_directory
        / "existing.txt"
    ).write_text(
        "preserve",
        encoding="utf-8",
    )

    with pytest.raises(
        FileExistsError,
        match="already exist",
    ):
        materialize_embedding_artifacts(
            chunk_directory=chunk_directory,
            retrieval_config_path=(
                config_path
            ),
            output_directory=(
                output_directory
            ),
            embedding_client=(
                _FakeEmbeddingClient()
            ),
            batch_size=2,
        )

    assert (
        output_directory
        / "existing.txt"
    ).read_text(
        encoding="utf-8"
    ) == "preserve"


def test_chunking_config_mismatch_is_rejected(
    tmp_path: Path,
) -> None:
    chunk_directory, config_path = (
        _write_fixture(tmp_path)
    )

    config = json.loads(
        config_path.read_text(
            encoding="utf-8"
        )
    )

    config["chunking_config_id"] = (
        "different-chunk-config"
    )

    config_path.write_text(
        json.dumps(
            config,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="different chunking",
    ):
        materialize_embedding_artifacts(
            chunk_directory=chunk_directory,
            retrieval_config_path=(
                config_path
            ),
            output_directory=(
                tmp_path / "embeddings"
            ),
            embedding_client=(
                _FakeEmbeddingClient()
            ),
            batch_size=2,
        )


def test_client_dimension_mismatch_is_rejected(
    tmp_path: Path,
) -> None:
    chunk_directory, config_path = (
        _write_fixture(tmp_path)
    )

    with pytest.raises(
        ValueError,
        match="dimensions do not match",
    ):
        materialize_embedding_artifacts(
            chunk_directory=chunk_directory,
            retrieval_config_path=(
                config_path
            ),
            output_directory=(
                tmp_path / "embeddings"
            ),
            embedding_client=(
                _FakeEmbeddingClient(
                    dimensions=4
                )
            ),
            batch_size=2,
        )


def test_source_chunk_hash_tracks_chunk_content(
    tmp_path: Path,
) -> None:
    first_root = (
        tmp_path / "first"
    )
    first_root.mkdir()

    chunk_directory, config_path = (
        _write_fixture(first_root)
    )

    first_metadata = (
        materialize_embedding_artifacts(
            chunk_directory=chunk_directory,
            retrieval_config_path=(
                config_path
            ),
            output_directory=(
                first_root / "embeddings"
            ),
            embedding_client=(
                _FakeEmbeddingClient()
            ),
            batch_size=2,
        )
    )

    first_hash = first_metadata[
        "source_chunk_artifacts_sha256"
    ]

    assert isinstance(
        first_hash,
        str,
    )
    assert len(first_hash) == 64
    assert (
        first_metadata[
            "source_chunk_artifact_count"
        ]
        == 1
    )

    second_root = (
        tmp_path / "second"
    )
    second_root.mkdir()

    second_chunks, second_config = (
        _write_fixture(second_root)
    )

    artifact_path = (
        second_chunks
        / "DOC001.chunks.json"
    )

    artifact = json.loads(
        artifact_path.read_text(
            encoding="utf-8"
        )
    )

    artifact["chunks"][0]["text"] = (
        "First text with a deliberate "
        "content change"
    )

    artifact_path.write_text(
        json.dumps(
            artifact,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    second_metadata = (
        materialize_embedding_artifacts(
            chunk_directory=second_chunks,
            retrieval_config_path=(
                second_config
            ),
            output_directory=(
                second_root / "embeddings"
            ),
            embedding_client=(
                _FakeEmbeddingClient()
            ),
            batch_size=2,
        )
    )

    second_hash = second_metadata[
        "source_chunk_artifacts_sha256"
    ]

    assert first_hash != second_hash
