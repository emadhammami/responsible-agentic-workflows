import hashlib
from pathlib import Path

import pytest

import responsible_agentic_workflows.ingestion.pdf as pdf_ingestion
from responsible_agentic_workflows.ingestion import extract_pdf_document


def _fake_pdf(tmp_path: Path) -> tuple[Path, str]:
    source = tmp_path / "DOC999_example.pdf"
    content = b"%PDF-fake-test-document"
    source.write_bytes(content)

    return source, hashlib.sha256(content).hexdigest()


def test_pdf_pages_preserve_identity_and_provenance(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, digest = _fake_pdf(tmp_path)

    def fake_command(arguments: list[str]) -> str:
        if arguments[0] == "pdfinfo":
            return "Pages:           2\n"

        if arguments[0] == "pdftotext":
            return "First page text.\fSecond page text.\f"

        raise AssertionError(arguments)

    monkeypatch.setattr(
        pdf_ingestion,
        "_run_text_command",
        fake_command,
    )

    document = extract_pdf_document(
        source,
        document_id="DOC999",
        title="Example Policy",
        expected_sha256=digest,
    )

    assert document.document_id == "DOC999"
    assert document.title == "Example Policy"
    assert document.source_sha256 == digest
    assert len(document.pages) == 2

    assert [
        page.page_id
        for page in document.pages
    ] == [
        "DOC999-P0001",
        "DOC999-P0002",
    ]

    assert [
        page.page_number
        for page in document.pages
    ] == [1, 2]

    assert [
        page.text
        for page in document.pages
    ] == [
        "First page text.",
        "Second page text.",
    ]

    for page in document.pages:
        assert page.document_id == "DOC999"
        assert page.title == "Example Policy"
        assert page.source_sha256 == digest
        assert page.source_path == source.as_posix()


def test_pdf_source_hash_must_match_manifest(
    tmp_path: Path,
) -> None:
    source, _ = _fake_pdf(tmp_path)

    with pytest.raises(
        ValueError,
        match="Source SHA-256 does not match manifest",
    ):
        extract_pdf_document(
            source,
            document_id="DOC999",
            title="Example Policy",
            expected_sha256="0" * 64,
        )


def test_pdf_filename_must_match_document_id(
    tmp_path: Path,
) -> None:
    source = tmp_path / "DOC998_example.pdf"
    content = b"%PDF-fake-test-document"
    source.write_bytes(content)

    digest = hashlib.sha256(content).hexdigest()

    with pytest.raises(
        ValueError,
        match="Filename/document ID mismatch",
    ):
        extract_pdf_document(
            source,
            document_id="DOC999",
            title="Example Policy",
            expected_sha256=digest,
        )


def test_pdf_page_count_mismatch_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, digest = _fake_pdf(tmp_path)

    def fake_command(arguments: list[str]) -> str:
        if arguments[0] == "pdfinfo":
            return "Pages: 2\n"

        if arguments[0] == "pdftotext":
            return "Only one extracted page."

        raise AssertionError(arguments)

    monkeypatch.setattr(
        pdf_ingestion,
        "_run_text_command",
        fake_command,
    )

    with pytest.raises(
        ValueError,
        match="Extracted page count does not match pdfinfo",
    ):
        extract_pdf_document(
            source,
            document_id="DOC999",
            title="Example Policy",
            expected_sha256=digest,
        )


def test_empty_physical_page_keeps_stable_page_number(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, digest = _fake_pdf(tmp_path)

    def fake_command(arguments: list[str]) -> str:
        if arguments[0] == "pdfinfo":
            return "Pages: 2\n"

        if arguments[0] == "pdftotext":
            return "First page.\f\f"

        raise AssertionError(arguments)

    monkeypatch.setattr(
        pdf_ingestion,
        "_run_text_command",
        fake_command,
    )

    document = extract_pdf_document(
        source,
        document_id="DOC999",
        title="Example Policy",
        expected_sha256=digest,
    )

    assert len(document.pages) == 2
    assert document.pages[0].text == "First page."
    assert document.pages[1].text == ""
    assert document.pages[1].page_id == "DOC999-P0002"
