"""Data structures shared by document ingestion implementations."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DocumentChunk:
    """One provenance-preserving unit produced during ingestion."""

    document_id: str
    chunk_id: str
    title: str
    section: str
    section_index: int
    text: str
    source_file: str
    page: int | None = None


@dataclass(frozen=True, slots=True)
class DocumentPage:
    """One extracted PDF page with stable source provenance."""

    document_id: str
    page_id: str
    title: str
    page_number: int
    text: str
    source_path: str
    source_sha256: str


@dataclass(frozen=True, slots=True)
class ExtractedPdfDocument:
    """A PDF source represented as ordered extracted pages."""

    document_id: str
    title: str
    source_path: str
    source_sha256: str
    pages: tuple[DocumentPage, ...]


@dataclass(frozen=True, slots=True)
class ParsedDocument:
    """A parsed source document and its ordered chunks."""

    document_id: str
    title: str
    metadata: dict[str, str]
    source_file: str
    chunks: tuple[DocumentChunk, ...]
