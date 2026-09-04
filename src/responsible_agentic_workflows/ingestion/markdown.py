"""Markdown ingestion with deterministic section provenance."""

import re
from pathlib import Path

from .models import DocumentChunk, ParsedDocument

_DOCUMENT_HEADER = re.compile(
    r"^# (?P<document_id>DOC[0-9]{3,}) - (?P<title>.+)$"
)
_SECTION_HEADER = re.compile(r"^## (?P<section>.+)$")
_METADATA_LINE = re.compile(r"^(?P<key>[^:]+): (?P<value>.+)$")


def _normalise_metadata_key(value: str) -> str:
    return value.strip().lower().replace(" ", "_")


def load_markdown_document(path: str | Path) -> ParsedDocument:
    """Parse one policy-style Markdown document.

    The current engineering parser treats each level-two section as one
    deterministic chunk. Final benchmark chunking parameters remain a separate
    configuration decision.
    """

    source = Path(path)

    if not source.is_file():
        raise FileNotFoundError(source)

    lines = source.read_text(encoding="utf-8").splitlines()

    if not lines:
        raise ValueError(f"Document is empty: {source}")

    header = _DOCUMENT_HEADER.fullmatch(lines[0].strip())

    if header is None:
        raise ValueError(
            f"Expected '# DOC### - Title' header in {source.name}"
        )

    document_id = header.group("document_id")
    title = header.group("title").strip()

    if source.stem != document_id:
        raise ValueError(
            f"Filename/document ID mismatch: {source.stem} != {document_id}"
        )

    metadata: dict[str, str] = {}
    sections: list[tuple[str, str]] = []

    current_section: str | None = None
    current_lines: list[str] = []

    for raw_line in lines[1:]:
        line = raw_line.rstrip()
        section_match = _SECTION_HEADER.fullmatch(line.strip())

        if section_match is not None:
            if current_section is not None:
                section_text = "\n".join(current_lines).strip()
                if not section_text:
                    raise ValueError(
                        f"Empty section '{current_section}' in {source.name}"
                    )
                sections.append((current_section, section_text))

            current_section = section_match.group("section").strip()
            current_lines = []
            continue

        if current_section is not None:
            current_lines.append(line)
            continue

        stripped = line.strip()

        if not stripped:
            continue

        metadata_match = _METADATA_LINE.fullmatch(stripped)

        if metadata_match is None:
            raise ValueError(
                f"Unexpected pre-section line in {source.name}: {stripped}"
            )

        key = _normalise_metadata_key(metadata_match.group("key"))
        value = metadata_match.group("value").strip()
        metadata[key] = value

    if current_section is not None:
        section_text = "\n".join(current_lines).strip()
        if not section_text:
            raise ValueError(
                f"Empty section '{current_section}' in {source.name}"
            )
        sections.append((current_section, section_text))

    if not sections:
        raise ValueError(f"No level-two sections found in {source.name}")

    chunks = tuple(
        DocumentChunk(
            document_id=document_id,
            chunk_id=f"{document_id}-S{index:03d}",
            title=title,
            section=section_name,
            section_index=index,
            text=section_text,
            source_file=source.name,
            page=None,
        )
        for index, (section_name, section_text) in enumerate(
            sections,
            start=1,
        )
    )

    return ParsedDocument(
        document_id=document_id,
        title=title,
        metadata=metadata,
        source_file=source.name,
        chunks=chunks,
    )


def ingest_markdown_directory(
    directory: str | Path,
) -> tuple[ParsedDocument, ...]:
    """Parse all DOC*.md documents from one directory deterministically."""

    root = Path(directory)

    if not root.is_dir():
        raise NotADirectoryError(root)

    documents = tuple(
        load_markdown_document(path)
        for path in sorted(root.glob("DOC*.md"))
    )

    if not documents:
        raise ValueError(f"No DOC*.md documents found in {root}")

    document_ids = [document.document_id for document in documents]

    if len(document_ids) != len(set(document_ids)):
        raise ValueError("Duplicate document IDs detected")

    return documents
