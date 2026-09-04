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
class ParsedDocument:
    """A parsed source document and its ordered chunks."""

    document_id: str
    title: str
    metadata: dict[str, str]
    source_file: str
    chunks: tuple[DocumentChunk, ...]
