"""Synthetic qualification of the read-only legacy UC2 adapter."""

import json
from dataclasses import replace

import numpy as np
import pytest

from responsible_agentic_workflows.benchmark.legacy_uc2 import (
    LegacyUC2Bindings,
    _load_legacy_uc2_artifacts,
    _sha256,
    load_legacy_uc2_artifacts,
)
from responsible_agentic_workflows.ingestion import DocumentChunk


def _fixture(tmp_path, *, change=None):
    artifact_directory = tmp_path / "artifacts"
    artifact_directory.mkdir()
    chunks_path = tmp_path / "chunks.jsonl"
    retrieval_config_path = tmp_path / "retrieval.json"
    source_inventory_path = tmp_path / "source_inventory.tsv"
    config = {
        "status": "frozen",
        "retrieval_config_id": "UC2-QWEN3-EMBED4B-EXACT-COSINE-v0.1",
        "chunking_config_id": "UC2-SOURCEUNIT-W450-O75-v0.1",
        "embedding": {
            "model_tag": "synthetic-embedder",
            "model_digest": "synthetic-digest",
            "query_instruction": "synthetic instruction",
            "truncate": False,
            "output_dimensions": 2560,
        },
        "index": {"dtype": "float32"},
    }
    rows = [
        {
            "document_id": "DOC-SYNTHETIC",
            "chunk_id": f"C{i:03d}",
            "text": f"Exact synthetic text {i}\nsecond line",
            "candidate_id": "SYNTHETIC-C01",
            "use_case_id": "UC2",
            "source_unit_id": f"U{i:03d}",
            "source_unit_index": i,
            "source_component_path": "synthetic/source.pdf",
            "pdf_page_number": i + 1,
        }
        for i in range(293)
    ]
    ids = [row["chunk_id"] for row in rows]
    matrix = np.ones((293, 2560), dtype=np.float32)
    inventory = "candidate_id\ttitle\nSYNTHETIC-C01\tSynthetic title\n"
    if change is not None:
        change(rows, ids, matrix, config)
    retrieval_config_path.write_text(json.dumps(config))
    chunks_path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    np.save(artifact_directory / "embeddings.npy", matrix)
    ids_path = artifact_directory / "chunk_ids.json"
    ids_path.write_text(json.dumps({
        "retrieval_config_id": config["retrieval_config_id"],
        "chunking_config_id": config["chunking_config_id"],
        "use_case_id": "UC2",
        "chunk_count": 293,
        "chunk_ids": ids,
    }))
    source_inventory_path.write_text(inventory)
    bindings = LegacyUC2Bindings(
        chunks=_sha256(chunks_path),
        chunk_ids=_sha256(ids_path),
        embeddings=_sha256(artifact_directory / "embeddings.npy"),
        metadata="unused",
        retrieval_config=_sha256(retrieval_config_path),
    )
    metadata_path = artifact_directory / "metadata.json"
    metadata_path.write_text(json.dumps({
        "status": "frozen",
        "retrieval_config_id": config["retrieval_config_id"],
        "retrieval_config_sha256": bindings.retrieval_config,
        "source_chunks_sha256": bindings.chunks,
        "chunk_ids_sha256": bindings.chunk_ids,
        "embeddings_sha256": bindings.embeddings,
        "embedding_model": config["embedding"]["model_tag"],
        "embedding_model_digest": config["embedding"]["model_digest"],
        "query_instruction": config["embedding"]["query_instruction"],
        "truncate": False,
        "dimensions": 2560,
        "dtype": "float32",
        "use_case_id": "UC2",
        "chunk_count": 293,
    }))
    bindings = replace(bindings, metadata=_sha256(metadata_path))
    return {
        "chunks_path": chunks_path,
        "artifact_directory": artifact_directory,
        "retrieval_config_path": retrieval_config_path,
        "source_inventory_path": source_inventory_path,
        "bindings": bindings,
    }


def test_synthetic_success_and_exact_adaptation(tmp_path):
    paths = _fixture(tmp_path)
    chunks, matrix, metadata = _load_legacy_uc2_artifacts(**paths)
    assert len(chunks) == 293
    assert matrix.shape == (293, 2560)
    assert matrix.dtype == np.float32
    assert metadata["status"] == "frozen"
    assert chunks[0] == DocumentChunk(
        document_id="DOC-SYNTHETIC", chunk_id="C000",
        text="Exact synthetic text 0\nsecond line", title="Synthetic title",
        section="U000", section_index=0,
        source_file="synthetic/source.pdf", page=1,
    )
    assert chunks[-1].chunk_id == "C292"
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        load_legacy_uc2_artifacts(**{k: v for k, v in paths.items() if k != "bindings"})


def test_hash_failure(tmp_path):
    paths = _fixture(tmp_path)
    paths["chunks_path"].write_text(paths["chunks_path"].read_text() + " ")
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        _load_legacy_uc2_artifacts(**paths)


@pytest.mark.parametrize(
    "kind", ["order", "duplicate", "dimension", "zero", "nonfinite"]
)
def test_matrix_and_ids_fail_closed(tmp_path, kind):
    def change(rows, ids, matrix, config):
        if kind == "order":
            ids[0], ids[1] = ids[1], ids[0]
        elif kind == "duplicate":
            rows[1]["chunk_id"] = rows[0]["chunk_id"]
            ids[1] = ids[0]
        elif kind == "dimension":
            config["embedding"]["output_dimensions"] = 2559
        elif kind == "zero":
            matrix[0] = 0
        else:
            matrix[0, 0] = np.nan

    paths = _fixture(tmp_path, change=change)
    with pytest.raises(ValueError, match="mismatch"):
        _load_legacy_uc2_artifacts(**paths)


def test_missing_or_ambiguous_title_fails(tmp_path):
    paths = _fixture(tmp_path)
    inventory = paths["source_inventory_path"]
    inventory.write_text("candidate_id\ttitle\nOTHER\tOther title\n")
    with pytest.raises(ValueError, match="no unique inventory title"):
        _load_legacy_uc2_artifacts(**paths)
    inventory.write_text(
        "candidate_id\ttitle\nSYNTHETIC-C01\tTitle\nSYNTHETIC-C01\tOther\n"
    )
    with pytest.raises(ValueError, match="ambiguous"):
        _load_legacy_uc2_artifacts(**paths)
