import hashlib
import json
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pytest
from numpy.typing import NDArray

from responsible_agentic_workflows.retrieval.materialize import (
    load_embedding_artifacts,
    materialize_embedding_artifacts,
)


class _FakeEmbeddingClient:
    @property
    def dimensions(self) -> int:
        return 3

    def embed_query(
        self,
        query: str,
    ) -> NDArray[np.float32]:
        del query

        return np.asarray(
            [1.0, 0.0, 0.0],
            dtype=np.float32,
        )

    def embed_documents(
        self,
        texts: Sequence[str],
    ) -> NDArray[np.float32]:
        rows = []

        for index, _ in enumerate(
            texts,
        ):
            vector = np.zeros(
                3,
                dtype=np.float32,
            )
            vector[index % 3] = 1.0
            rows.append(vector)

        return np.stack(rows)


def _sha256(path: Path) -> str:
    return hashlib.sha256(
        path.read_bytes()
    ).hexdigest()


def _write_fixture(
    root: Path,
) -> tuple[
    Path,
    Path,
    Path,
]:
    chunk_directory = (
        root / "chunks"
    )
    chunk_directory.mkdir()

    chunk_artifact = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "document_id": "DOC001",
        "title": "Synthetic policy",
        "source_sha256": "a" * 64,
        "chunking_config_id": (
            "chunk-v1"
        ),
        "chunk_count": 3,
        "chunks": [
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0001-C001"
                ),
                "title": (
                    "Synthetic policy"
                ),
                "section": "Page 1",
                "section_index": 1,
                "text": (
                    "Forest biodiversity "
                    "policy text."
                ),
                "source_file": (
                    "DOC001.pdf"
                ),
                "page": 1,
            },
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0001-C002"
                ),
                "title": (
                    "Synthetic policy"
                ),
                "section": "Page 1",
                "section_index": 1,
                "text": (
                    "Climate adaptation "
                    "policy text."
                ),
                "source_file": (
                    "DOC001.pdf"
                ),
                "page": 1,
            },
            {
                "document_id": "DOC001",
                "chunk_id": (
                    "DOC001-P0002-C001"
                ),
                "title": (
                    "Synthetic policy"
                ),
                "section": "Page 2",
                "section_index": 2,
                "text": (
                    "Timber market "
                    "policy text."
                ),
                "source_file": (
                    "DOC001.pdf"
                ),
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
            chunk_artifact,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    index = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "status": "working",
        "artifact_type": (
            "retrieval_chunks"
        ),
        "chunking_config_id": (
            "chunk-v1"
        ),
        "document_count": 1,
        "total_chunks": 3,
        "documents": [
            {
                "document_id": (
                    "DOC001"
                ),
                "artifact_file": (
                    "DOC001.chunks.json"
                ),
                "source_sha256": (
                    "a" * 64
                ),
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

    retrieval_config_path = (
        root / "retrieval.json"
    )

    retrieval_config = {
        "schema_version": "0.1",
        "retrieval_config_id": (
            "retrieval-v1"
        ),
        "status": "working",
        "backend": (
            "dense-exact-cosine"
        ),
        "chunking_config_id": (
            "chunk-v1"
        ),
        "embedding": {
            "provider": "fake",
            "model_name": (
                "fake-model"
            ),
            "model_tag": (
                "fake-model:v1"
            ),
            "model_digest": (
                "b" * 64
            ),
            "provider_version": (
                "1.0"
            ),
            "output_dimensions": 3,
            "normalized": True,
            "truncate": False,
            "query_instruction": None,
            "document_instruction": None,
        },
        "index": {
            "backend": "numpy",
            "backend_version": (
                np.__version__
            ),
            "index_type": "flat-exact",
            "distance_metric": "cosine",
            "dtype": "float32",
        },
    }

    retrieval_config_path.write_text(
        json.dumps(
            retrieval_config,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    artifact_directory = (
        root / "embeddings"
    )

    materialize_embedding_artifacts(
        chunk_directory=(
            chunk_directory
        ),
        retrieval_config_path=(
            retrieval_config_path
        ),
        output_directory=(
            artifact_directory
        ),
        embedding_client=(
            _FakeEmbeddingClient()
        ),
        batch_size=2,
    )

    return (
        chunk_directory,
        retrieval_config_path,
        artifact_directory,
    )


def test_load_verified_artifact(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    chunks, matrix, metadata = (
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )
    )

    assert [
        chunk.chunk_id
        for chunk in chunks
    ] == [
        "DOC001-P0001-C001",
        "DOC001-P0001-C002",
        "DOC001-P0002-C001",
    ]

    assert matrix.shape == (3, 3)
    assert matrix.dtype == np.float32

    assert (
        metadata[
            "retrieval_config_id"
        ]
        == "retrieval-v1"
    )


def test_matrix_tampering_is_rejected(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    matrix_path = (
        artifact_directory
        / "embeddings.npy"
    )

    matrix = np.load(
        matrix_path,
        allow_pickle=False,
    )

    matrix[0, 0] = 0.5

    np.save(
        matrix_path,
        matrix,
        allow_pickle=False,
    )

    with pytest.raises(
        ValueError,
        match=(
            "hash mismatch: "
            "embeddings_sha256"
        ),
    ):
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )


def test_chunk_id_order_tampering_is_rejected(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    chunk_ids_path = (
        artifact_directory
        / "chunk_ids.json"
    )

    metadata_path = (
        artifact_directory
        / "metadata.json"
    )

    payload = json.loads(
        chunk_ids_path.read_text(
            encoding="utf-8"
        )
    )

    payload["chunk_ids"][0:2] = (
        reversed(
            payload["chunk_ids"][0:2]
        )
    )

    chunk_ids_path.write_text(
        json.dumps(
            payload,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    metadata = json.loads(
        metadata_path.read_text(
            encoding="utf-8"
        )
    )

    metadata[
        "chunk_ids_sha256"
    ] = _sha256(
        chunk_ids_path
    )

    metadata_path.write_text(
        json.dumps(
            metadata,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="ordering",
    ):
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )


def test_source_chunk_tampering_is_rejected(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    artifact_path = (
        chunk_directory
        / "DOC001.chunks.json"
    )

    payload = json.loads(
        artifact_path.read_text(
            encoding="utf-8"
        )
    )

    payload["chunks"][0]["text"] = (
        "Deliberately modified text."
    )

    artifact_path.write_text(
        json.dumps(
            payload,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=(
            "hash mismatch: "
            "source_chunk_artifacts_sha256"
        ),
    ):
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )


def test_retrieval_config_tampering_is_rejected(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    config = json.loads(
        config_path.read_text(
            encoding="utf-8"
        )
    )

    config["index"][
        "backend_version"
    ] = "changed"

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
        match=(
            "hash mismatch: "
            "retrieval_config_sha256"
        ),
    ):
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )


def test_embedding_identity_metadata_mismatch_is_rejected(
    tmp_path: Path,
) -> None:
    (
        chunk_directory,
        config_path,
        artifact_directory,
    ) = _write_fixture(tmp_path)

    metadata_path = (
        artifact_directory
        / "metadata.json"
    )

    metadata = json.loads(
        metadata_path.read_text(
            encoding="utf-8"
        )
    )

    metadata["embedding_model"] = (
        "different-model:v1"
    )

    metadata_path.write_text(
        json.dumps(
            metadata,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=(
            "metadata mismatch: "
            "embedding_model"
        ),
    ):
        load_embedding_artifacts(
            chunk_directory=(
                chunk_directory
            ),
            retrieval_config_path=(
                config_path
            ),
            artifact_directory=(
                artifact_directory
            ),
        )
