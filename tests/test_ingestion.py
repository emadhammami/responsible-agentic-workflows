from pathlib import Path

import pytest

from responsible_agentic_workflows.ingestion import (
    ingest_markdown_directory,
    load_markdown_document,
)

SYNTHETIC_DOCUMENTS = Path("benchmark/synthetic/documents")


def test_load_document_preserves_identity_and_metadata() -> None:
    document = load_markdown_document(SYNTHETIC_DOCUMENTS / "DOC901.md")

    assert document.document_id == "DOC901"
    assert document.title == "Travel and Expense Policy"
    assert document.source_file == "DOC901.md"

    assert document.metadata["version"] == "1.0"
    assert document.metadata["effective_date"] == "2026-01-01"
    assert document.metadata["status"] == "Synthetic engineering document"


def test_sections_preserve_order_and_provenance() -> None:
    document = load_markdown_document(SYNTHETIC_DOCUMENTS / "DOC903.md")

    assert [chunk.section for chunk in document.chunks] == [
        "External collaborators",
        "Access review",
        "Privileged access",
    ]

    assert [chunk.chunk_id for chunk in document.chunks] == [
        "DOC903-S001",
        "DOC903-S002",
        "DOC903-S003",
    ]

    assert [chunk.section_index for chunk in document.chunks] == [1, 2, 3]

    for chunk in document.chunks:
        assert chunk.document_id == "DOC903"
        assert chunk.source_file == "DOC903.md"
        assert chunk.page is None
        assert chunk.text


def test_synthetic_corpus_ingests_deterministically() -> None:
    documents = ingest_markdown_directory(SYNTHETIC_DOCUMENTS)

    assert [document.document_id for document in documents] == [
        "DOC901",
        "DOC902",
        "DOC903",
        "DOC904",
        "DOC905",
    ]

    chunks = [
        chunk
        for document in documents
        for chunk in document.chunks
    ]

    assert len(documents) == 5
    assert len(chunks) == 13

    chunk_ids = [chunk.chunk_id for chunk in chunks]

    assert len(chunk_ids) == len(set(chunk_ids))


def test_filename_must_match_document_id(tmp_path: Path) -> None:
    source = tmp_path / "DOC999.md"
    source.write_text(
        "# DOC998 - Example\n\n"
        "Version: 1.0\n\n"
        "## Section\n\n"
        "Example text.\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="Filename/document ID mismatch",
    ):
        load_markdown_document(source)


def test_empty_section_is_rejected(tmp_path: Path) -> None:
    source = tmp_path / "DOC999.md"
    source.write_text(
        "# DOC999 - Example\n\n"
        "Version: 1.0\n\n"
        "## Empty section\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Empty section"):
        load_markdown_document(source)
