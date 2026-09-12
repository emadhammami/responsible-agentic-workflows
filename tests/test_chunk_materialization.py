import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.chunks import (
    build_chunk_artifacts,
)


def _write_fixture(root: Path) -> tuple[Path, Path]:
    pages = root / "pages"
    pages.mkdir()

    digest = "a" * 64

    artifact = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "document_id": "DOC999",
        "title": "Example",
        "source_path": "raw/DOC999_example.pdf",
        "source_sha256": digest,
        "page_count": 2,
        "pages": [
            {
                "document_id": "DOC999",
                "page_id": "DOC999-P0001",
                "title": "Example",
                "page_number": 1,
                "text": (
                    "one two three four five "
                    "six seven eight"
                ),
                "source_path": "raw/DOC999_example.pdf",
                "source_sha256": digest,
            },
            {
                "document_id": "DOC999",
                "page_id": "DOC999-P0002",
                "title": "Example",
                "page_number": 2,
                "text": "",
                "source_path": "raw/DOC999_example.pdf",
                "source_sha256": digest,
            },
        ],
    }

    (pages / "DOC999.pages.json").write_text(
        json.dumps(artifact),
        encoding="utf-8",
    )

    index = {
        "schema_version": "0.1",
        "use_case_id": "UCX",
        "document_count": 1,
        "documents": [
            {
                "document_id": "DOC999",
                "artifact_file": "DOC999.pages.json",
                "source_sha256": digest,
                "page_count": 2,
                "word_count": 8,
            }
        ],
    }

    (pages / "index.json").write_text(
        json.dumps(index),
        encoding="utf-8",
    )

    config = root / "chunking.json"

    config.write_text(
        json.dumps(
            {
                "schema_version": "0.1",
                "config_id": "test-config",
                "use_case_id": "UCX",
                "status": "working",
                "strategy": "page_aware_word_windows",
                "max_words": 5,
                "overlap_words": 2,
                "cross_page_boundaries": False,
                "empty_pages_generate_chunks": False,
                "frozen": False,
            }
        ),
        encoding="utf-8",
    )

    return pages, config


def test_materialization_preserves_page_provenance(
    tmp_path: Path,
) -> None:
    pages, config = _write_fixture(tmp_path)
    output = tmp_path / "chunks"

    index = build_chunk_artifacts(
        use_case_id="UCX",
        page_directory=pages,
        config_path=config,
        output_directory=output,
    )

    assert index["document_count"] == 1
    assert index["total_chunks"] == 2
    assert index["total_chunk_words"] == 10
    assert index["pages_with_chunks"] == 1

    artifact = json.loads(
        (
            output / "DOC999.chunks.json"
        ).read_text(encoding="utf-8")
    )

    chunks = artifact["chunks"]

    assert [
        chunk["chunk_id"]
        for chunk in chunks
    ] == [
        "DOC999-P0001-C001",
        "DOC999-P0001-C002",
    ]

    assert all(
        chunk["page"] == 1
        for chunk in chunks
    )

    assert all(
        chunk["page_id"] == "DOC999-P0001"
        for chunk in chunks
    )

    assert all(
        chunk["source_sha256"] == "a" * 64
        for chunk in chunks
    )


def test_materialization_refuses_existing_artifacts(
    tmp_path: Path,
) -> None:
    pages, config = _write_fixture(tmp_path)
    output = tmp_path / "chunks"
    output.mkdir()

    (output / "existing.json").write_text(
        "{}",
        encoding="utf-8",
    )

    with pytest.raises(
        FileExistsError,
        match="Chunk artifacts already exist",
    ):
        build_chunk_artifacts(
            use_case_id="UCX",
            page_directory=pages,
            config_path=config,
            output_directory=output,
        )


def test_materialization_rejects_cross_page_config(
    tmp_path: Path,
) -> None:
    pages, config = _write_fixture(tmp_path)

    value = json.loads(
        config.read_text(encoding="utf-8")
    )

    value["cross_page_boundaries"] = True

    config.write_text(
        json.dumps(value),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="Cross-page chunking",
    ):
        build_chunk_artifacts(
            use_case_id="UCX",
            page_directory=pages,
            config_path=config,
            output_directory=tmp_path / "chunks",
        )
