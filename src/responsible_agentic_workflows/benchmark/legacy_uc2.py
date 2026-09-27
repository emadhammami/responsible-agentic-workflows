"""Read-only adapter for the frozen UC2 source-unit embedding artifact."""

import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from responsible_agentic_workflows.ingestion import DocumentChunk


@dataclass(frozen=True, slots=True)
class LegacyUC2Bindings:
    """Byte identities fixed by the primary orchestration contract."""

    chunks: str = "b3dd26958805320420f0dc7e379b0e0f1c2ec85d4b55fffd3cd8884c8e9841f2"
    chunk_ids: str = "05992722b95803df4396ad9fa321876bd4d9023ca2b0196a74eb728edff43c7d"
    embeddings: str = "621a229c066f2b9cf1d2eef257da4ba8215e7bf1513f8113aebaf3717464d78f"
    metadata: str = "1901048651cb93b4b52f9529a9706c0ec81ea0ded9f92ea0fd48b88e1032618e"
    retrieval_config: str = (
        "6df4b73e262261e907f8e6e227619be1b996ced6b688eca478c7f56748acc169"
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_legacy_uc2_artifacts(
    *,
    chunks_path: Path,
    artifact_directory: Path,
    retrieval_config_path: Path,
    source_inventory_path: Path,
) -> tuple[tuple[DocumentChunk, ...], np.ndarray, dict[str, object]]:
    """Verify frozen bytes and adapt rows without changing their order or values."""
    return _load_legacy_uc2_artifacts(
        chunks_path=chunks_path,
        artifact_directory=artifact_directory,
        retrieval_config_path=retrieval_config_path,
        source_inventory_path=source_inventory_path,
        bindings=LegacyUC2Bindings(),
    )


def _load_legacy_uc2_artifacts(
    *,
    chunks_path: Path,
    artifact_directory: Path,
    retrieval_config_path: Path,
    source_inventory_path: Path,
    bindings: LegacyUC2Bindings,
) -> tuple[tuple[DocumentChunk, ...], np.ndarray, dict[str, object]]:
    """Load synthetic fixtures with injected byte identities in unit tests."""
    paths = {
        "chunks": chunks_path,
        "chunk_ids": artifact_directory / "chunk_ids.json",
        "embeddings": artifact_directory / "embeddings.npy",
        "metadata": artifact_directory / "metadata.json",
        "retrieval_config": retrieval_config_path,
    }
    for name, path in paths.items():
        if _sha256(path) != getattr(bindings, name):
            raise ValueError(f"UC2 {name} SHA256 mismatch")

    config = json.loads(retrieval_config_path.read_text(encoding="utf-8"))
    metadata = json.loads(paths["metadata"].read_text(encoding="utf-8"))
    saved = json.loads(paths["chunk_ids"].read_text(encoding="utf-8"))
    embedding = config["embedding"]
    identity = config["retrieval_config_id"]
    if (
        config.get("status") != "frozen"
        or metadata.get("status") != "frozen"
        or identity != "UC2-QWEN3-EMBED4B-EXACT-COSINE-v0.1"
        or metadata.get("retrieval_config_id") != identity
        or saved.get("retrieval_config_id") != identity
        or metadata.get("retrieval_config_sha256") != bindings.retrieval_config
        or metadata.get("source_chunks_sha256") != bindings.chunks
        or metadata.get("chunk_ids_sha256") != bindings.chunk_ids
        or metadata.get("embeddings_sha256") != bindings.embeddings
        or saved.get("chunking_config_id") != config.get("chunking_config_id")
        or metadata.get("embedding_model") != embedding.get("model_tag")
        or metadata.get("embedding_model_digest") != embedding.get("model_digest")
        or metadata.get("query_instruction") != embedding.get("query_instruction")
        or metadata.get("truncate") != embedding.get("truncate")
        or metadata.get("dimensions") != embedding.get("output_dimensions")
        or metadata.get("dtype") != config["index"].get("dtype")
        or metadata.get("use_case_id") != "UC2"
        or saved.get("use_case_id") != "UC2"
    ):
        raise ValueError("UC2 frozen retrieval identity mismatch")

    rows = [
        json.loads(line)
        for line in chunks_path.read_text(encoding="utf-8").splitlines()
    ]
    ids = [row["chunk_id"] for row in rows]
    if (
        len(rows) != 293
        or metadata.get("chunk_count") != 293
        or saved.get("chunk_count") != 293
        or len(set(ids)) != 293
        or saved.get("chunk_ids") != ids
        or embedding.get("output_dimensions") != 2560
        or metadata.get("dimensions") != 2560
        or metadata.get("dtype") != "float32"
    ):
        raise ValueError("UC2 chunk count, ID order, or dimensions mismatch")

    matrix = np.load(paths["embeddings"], allow_pickle=False)
    if (
        matrix.shape != (293, 2560)
        or matrix.dtype != np.dtype("float32")
        or not np.isfinite(matrix).all()
        or np.any(np.linalg.norm(matrix, axis=1) == 0)
    ):
        raise ValueError("UC2 embedding matrix mismatch")

    titles: dict[str, str] = {}
    with source_inventory_path.open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            candidate = row["candidate_id"]
            title = row["title"]
            if not candidate or not title or candidate in titles:
                raise ValueError("UC2 inventory title mapping is ambiguous")
            titles[candidate] = title

    chunks = []
    for row in rows:
        candidate = row["candidate_id"]
        if candidate not in titles or row.get("use_case_id") != "UC2":
            raise ValueError("UC2 chunk has no unique inventory title")
        chunks.append(
            DocumentChunk(
                document_id=row["document_id"],
                chunk_id=row["chunk_id"],
                text=row["text"],
                title=titles[candidate],
                section=row["source_unit_id"],
                section_index=row["source_unit_index"],
                source_file=row["source_component_path"],
                page=row["pdf_page_number"],
            )
        )
    return tuple(chunks), matrix, metadata
