"""Materialize dense retrieval embeddings with provenance metadata."""

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np

from responsible_agentic_workflows.ingestion import (
    DocumentChunk,
)

from .embedding import EmbeddingClient


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for block in iter(
            lambda: handle.read(1024 * 1024),
            b"",
        ):
            digest.update(block)

    return digest.hexdigest()


def _load_json(path: Path) -> dict[str, object]:
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def _chunk_artifacts_sha256(
    *,
    chunk_directory: Path,
    chunk_index: dict[str, object],
) -> str:
    """Hash ordered chunk artifact identities and contents."""

    documents = chunk_index.get("documents")

    if not isinstance(documents, list):
        raise ValueError(
            "Chunk index documents must be a list"
        )

    digest = hashlib.sha256()

    for item in documents:
        if not isinstance(item, dict):
            raise ValueError(
                "Chunk index document entries must be objects"
            )

        artifact_file = item.get("artifact_file")

        if not isinstance(artifact_file, str):
            raise ValueError(
                "Chunk artifact_file must be a string"
            )

        artifact_path = (
            chunk_directory / artifact_file
        )

        if not artifact_path.is_file():
            raise FileNotFoundError(
                artifact_path
            )

        digest.update(
            artifact_file.encode("utf-8")
        )
        digest.update(b"\\0")
        digest.update(
            _sha256(
                artifact_path
            ).encode("ascii")
        )
        digest.update(b"\\n")

    return digest.hexdigest()


def load_ordered_chunks(
    chunk_directory: Path,
) -> tuple[
    tuple[DocumentChunk, ...],
    dict[str, object],
]:
    """Load chunks in the explicit order recorded by the chunk index."""

    index_path = chunk_directory / "index.json"

    if not index_path.is_file():
        raise FileNotFoundError(index_path)

    index = _load_json(index_path)

    if index.get("artifact_type") != "retrieval_chunks":
        raise ValueError(
            "Chunk index artifact_type must be retrieval_chunks"
        )

    documents = index.get("documents")

    if not isinstance(documents, list):
        raise ValueError(
            "Chunk index documents must be a list"
        )

    chunks: list[DocumentChunk] = []
    chunk_ids: set[str] = set()

    for item in documents:
        if not isinstance(item, dict):
            raise ValueError(
                "Chunk index document entries must be objects"
            )

        artifact_file = item.get("artifact_file")

        if not isinstance(artifact_file, str):
            raise ValueError(
                "Chunk artifact_file must be a string"
            )

        artifact_path = (
            chunk_directory / artifact_file
        )

        artifact = _load_json(artifact_path)

        artifact_chunks = artifact.get("chunks")

        if not isinstance(artifact_chunks, list):
            raise ValueError(
                f"Invalid chunks list in {artifact_file}"
            )

        for item_chunk in artifact_chunks:
            if not isinstance(item_chunk, dict):
                raise ValueError(
                    "Chunk entries must be objects"
                )

            chunk = DocumentChunk(
                document_id=item_chunk["document_id"],
                chunk_id=item_chunk["chunk_id"],
                title=item_chunk["title"],
                section=item_chunk["section"],
                section_index=item_chunk[
                    "section_index"
                ],
                text=item_chunk["text"],
                source_file=item_chunk[
                    "source_file"
                ],
                page=item_chunk["page"],
            )

            if chunk.chunk_id in chunk_ids:
                raise ValueError(
                    f"Duplicate chunk ID: "
                    f"{chunk.chunk_id}"
                )

            if not chunk.text.strip():
                raise ValueError(
                    f"Empty chunk text: "
                    f"{chunk.chunk_id}"
                )

            chunk_ids.add(chunk.chunk_id)
            chunks.append(chunk)

    expected_total = index.get("total_chunks")

    if expected_total != len(chunks):
        raise ValueError(
            "Loaded chunk count does not match chunk index"
        )

    return tuple(chunks), index


def materialize_embedding_artifacts(
    *,
    chunk_directory: Path,
    retrieval_config_path: Path,
    output_directory: Path,
    embedding_client: EmbeddingClient,
    batch_size: int,
) -> dict[str, object]:
    """Embed all ordered chunks and atomically write retrieval artifacts."""

    if batch_size < 1:
        raise ValueError(
            "batch_size must be at least 1"
        )

    retrieval_config = _load_json(
        retrieval_config_path
    )

    if retrieval_config.get("status") != "working":
        raise ValueError(
            "Retrieval configuration must be working "
            "during materialization"
        )

    retrieval_config_id = retrieval_config.get(
        "retrieval_config_id"
    )

    if not isinstance(
        retrieval_config_id,
        str,
    ):
        raise ValueError(
            "retrieval_config_id must be a string"
        )

    embedding_config = retrieval_config.get(
        "embedding"
    )

    if not isinstance(
        embedding_config,
        dict,
    ):
        raise ValueError(
            "Embedding configuration is missing"
        )

    dimensions = embedding_config.get(
        "output_dimensions"
    )

    if dimensions != embedding_client.dimensions:
        raise ValueError(
            "Embedding client dimensions do not match "
            "retrieval configuration"
        )

    chunking_config_id = retrieval_config.get(
        "chunking_config_id"
    )

    chunks, chunk_index = load_ordered_chunks(
        chunk_directory
    )

    if (
        chunk_index.get("chunking_config_id")
        != chunking_config_id
    ):
        raise ValueError(
            "Chunk index and retrieval configuration "
            "use different chunking configurations"
        )

    staging = output_directory.with_name(
        output_directory.name + ".staging"
    )

    if staging.exists():
        shutil.rmtree(staging)

    if output_directory.exists():
        existing = [
            path
            for path in output_directory.rglob("*")
            if path.is_file()
        ]

        if existing:
            raise FileExistsError(
                f"Embedding artifacts already exist: "
                f"{output_directory}"
            )

        output_directory.rmdir()

    staging.mkdir(
        parents=True,
        exist_ok=False,
    )

    matrices: list[np.ndarray] = []

    try:
        for start in range(
            0,
            len(chunks),
            batch_size,
        ):
            batch = chunks[
                start : start + batch_size
            ]

            matrix = embedding_client.embed_documents(
                tuple(
                    chunk.text
                    for chunk in batch
                )
            )

            matrix = np.asarray(
                matrix,
                dtype=np.float32,
            )

            expected_shape = (
                len(batch),
                embedding_client.dimensions,
            )

            if matrix.shape != expected_shape:
                raise ValueError(
                    "Embedding batch returned "
                    "unexpected shape"
                )

            if not np.isfinite(matrix).all():
                raise ValueError(
                    "Embedding batch contains "
                    "non-finite values"
                )

            norms = np.linalg.norm(
                matrix,
                axis=1,
            )

            if np.any(norms == 0):
                raise ValueError(
                    "Embedding batch contains "
                    "zero-norm vectors"
                )

            matrices.append(
                np.ascontiguousarray(
                    matrix,
                    dtype=np.float32,
                )
            )

        full_matrix = np.concatenate(
            matrices,
            axis=0,
        )

        expected_full_shape = (
            len(chunks),
            embedding_client.dimensions,
        )

        if full_matrix.shape != expected_full_shape:
            raise ValueError(
                "Final embedding matrix shape mismatch"
            )

        matrix_path = (
            staging / "embeddings.npy"
        )

        np.save(
            matrix_path,
            full_matrix,
            allow_pickle=False,
        )

        chunk_ids_path = (
            staging / "chunk_ids.json"
        )

        chunk_ids_payload = {
            "schema_version": "0.1",
            "retrieval_config_id": (
                retrieval_config_id
            ),
            "chunking_config_id": (
                chunking_config_id
            ),
            "chunk_count": len(chunks),
            "chunk_ids": [
                chunk.chunk_id
                for chunk in chunks
            ],
        }

        chunk_ids_path.write_text(
            json.dumps(
                chunk_ids_payload,
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

        saved_matrix = np.load(
            matrix_path,
            allow_pickle=False,
        )

        if saved_matrix.shape != expected_full_shape:
            raise ValueError(
                "Saved embedding matrix shape mismatch"
            )

        if saved_matrix.dtype != np.float32:
            raise ValueError(
                "Saved embedding matrix dtype mismatch"
            )

        metadata = {
            "schema_version": "0.1",
            "artifact_type": (
                "dense_embedding_index"
            ),
            "status": "working",
            "retrieval_config_id": (
                retrieval_config_id
            ),
            "chunking_config_id": (
                chunking_config_id
            ),
            "chunk_count": len(chunks),
            "dimensions": (
                embedding_client.dimensions
            ),
            "dtype": "float32",
            "batch_size": batch_size,
            "embedding_model": (
                embedding_config.get(
                    "model_tag"
                )
            ),
            "embedding_model_digest": (
                embedding_config.get(
                    "model_digest"
                )
            ),
            "embedding_provider": (
                embedding_config.get(
                    "provider"
                )
            ),
            "embedding_provider_version": (
                embedding_config.get(
                    "provider_version"
                )
            ),
            "truncate": embedding_config.get(
                "truncate"
            ),
            "source_chunk_index_sha256": (
                _sha256(
                    chunk_directory
                    / "index.json"
                )
            ),
            "source_chunk_artifacts_sha256": (
                _chunk_artifacts_sha256(
                    chunk_directory=chunk_directory,
                    chunk_index=chunk_index,
                )
            ),
            "source_chunk_artifact_count": (
                len(
                    chunk_index["documents"]
                )
            ),
            "retrieval_config_sha256": (
                _sha256(
                    retrieval_config_path
                )
            ),
            "embeddings_sha256": (
                _sha256(matrix_path)
            ),
            "chunk_ids_sha256": (
                _sha256(chunk_ids_path)
            ),
        }

        metadata_path = (
            staging / "metadata.json"
        )

        metadata_path.write_text(
            json.dumps(
                metadata,
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

        staging.replace(
            output_directory
        )

        return metadata

    except Exception:
        if staging.exists():
            shutil.rmtree(staging)

        raise
