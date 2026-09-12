"""PDF page extraction with deterministic source provenance."""

import hashlib
import re
import subprocess
from pathlib import Path

from .models import DocumentPage, ExtractedPdfDocument

_DOCUMENT_ID = re.compile(r"^DOC[0-9]{3,}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_PAGE_COUNT = re.compile(r"^Pages:\s*(?P<count>[0-9]+)\s*$", re.MULTILINE)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def _run_text_command(arguments: list[str]) -> str:
    result = subprocess.run(
        arguments,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        command = arguments[0]
        message = result.stderr.strip() or "unknown error"
        raise RuntimeError(f"{command} failed: {message}")

    return result.stdout


def _page_count(source: Path) -> int:
    output = _run_text_command(
        [
            "pdfinfo",
            str(source),
        ]
    )

    match = _PAGE_COUNT.search(output)

    if match is None:
        raise ValueError(
            f"Could not determine PDF page count: {source}"
        )

    count = int(match.group("count"))

    if count < 1:
        raise ValueError(
            f"PDF must contain at least one page: {source}"
        )

    return count


def _extract_page_texts(
    source: Path,
    expected_pages: int,
) -> tuple[str, ...]:
    output = _run_text_command(
        [
            "pdftotext",
            "-layout",
            str(source),
            "-",
        ]
    )

    pages = output.split("\f")

    # pdftotext normally terminates the document with one form feed.
    # Remove only that terminal sentinel so an empty physical final
    # page is still represented.
    if (
        len(pages) == expected_pages + 1
        and not pages[-1].strip()
    ):
        pages = pages[:-1]

    if len(pages) != expected_pages:
        raise ValueError(
            "Extracted page count does not match pdfinfo: "
            f"{len(pages)} != {expected_pages}"
        )

    return tuple(page.strip() for page in pages)


def extract_pdf_document(
    path: str | Path,
    *,
    document_id: str,
    title: str,
    expected_sha256: str,
) -> ExtractedPdfDocument:
    """Extract one PDF into ordered page records.

    This function preserves page-level provenance only. It does not make
    any benchmark chunking decision.
    """

    source = Path(path)

    if not source.is_file():
        raise FileNotFoundError(source)

    if _DOCUMENT_ID.fullmatch(document_id) is None:
        raise ValueError(
            f"Invalid document ID: {document_id}"
        )

    if not title.strip():
        raise ValueError("Document title must not be empty")

    expected_hash = expected_sha256.lower()

    if _SHA256.fullmatch(expected_hash) is None:
        raise ValueError("expected_sha256 must be a SHA-256 hex digest")

    if not source.name.startswith(f"{document_id}_"):
        raise ValueError(
            "Filename/document ID mismatch: "
            f"{source.name} != {document_id}"
        )

    with source.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ValueError(
                f"Source is not a PDF: {source}"
            )

    actual_hash = _sha256(source)

    if actual_hash != expected_hash:
        raise ValueError(
            "Source SHA-256 does not match manifest: "
            f"{actual_hash} != {expected_hash}"
        )

    page_count = _page_count(source)

    page_texts = _extract_page_texts(
        source,
        page_count,
    )

    source_path = source.as_posix()

    pages = tuple(
        DocumentPage(
            document_id=document_id,
            page_id=f"{document_id}-P{page_number:04d}",
            title=title.strip(),
            page_number=page_number,
            text=text,
            source_path=source_path,
            source_sha256=actual_hash,
        )
        for page_number, text in enumerate(
            page_texts,
            start=1,
        )
    )

    return ExtractedPdfDocument(
        document_id=document_id,
        title=title.strip(),
        source_path=source_path,
        source_sha256=actual_hash,
        pages=pages,
    )
