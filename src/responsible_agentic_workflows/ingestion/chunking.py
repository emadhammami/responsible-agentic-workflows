"""Deterministic page-aware chunking for extracted PDF documents."""

import re
from pathlib import Path

from .models import DocumentChunk, ExtractedPdfDocument

_WORD = re.compile(r"\S+")


def _word_spans(text: str) -> tuple[tuple[int, int], ...]:
    return tuple(
        (match.start(), match.end())
        for match in _WORD.finditer(text)
    )


def _window_text(
    text: str,
    spans: tuple[tuple[int, int], ...],
    start_word: int,
    end_word: int,
) -> str:
    start_character = spans[start_word][0]
    end_character = spans[end_word - 1][1]

    return text[start_character:end_character].strip()


def chunk_pdf_document(
    document: ExtractedPdfDocument,
    *,
    max_words: int,
    overlap_words: int,
) -> tuple[DocumentChunk, ...]:
    """Create deterministic chunks without crossing physical page boundaries.

    Empty pages remain represented by the page-extraction artifact but do not
    produce retrieval chunks. Exact chunking parameters are supplied by the
    caller and remain a separate benchmark configuration decision.
    """

    if max_words < 1:
        raise ValueError("max_words must be at least 1")

    if overlap_words < 0:
        raise ValueError("overlap_words must not be negative")

    if overlap_words >= max_words:
        raise ValueError(
            "overlap_words must be smaller than max_words"
        )

    chunks: list[DocumentChunk] = []

    for page in document.pages:
        spans = _word_spans(page.text)

        if not spans:
            continue

        start_word = 0
        page_chunk_index = 1

        while start_word < len(spans):
            end_word = min(
                start_word + max_words,
                len(spans),
            )

            chunk_text = _window_text(
                page.text,
                spans,
                start_word,
                end_word,
            )

            chunks.append(
                DocumentChunk(
                    document_id=document.document_id,
                    chunk_id=(
                        f"{document.document_id}-"
                        f"P{page.page_number:04d}-"
                        f"C{page_chunk_index:03d}"
                    ),
                    title=document.title,
                    section=f"Page {page.page_number}",
                    section_index=page.page_number,
                    text=chunk_text,
                    source_file=Path(
                        document.source_path
                    ).name,
                    page=page.page_number,
                )
            )

            if end_word == len(spans):
                break

            start_word = (
                end_word - overlap_words
            )

            page_chunk_index += 1

    chunk_ids = [
        chunk.chunk_id
        for chunk in chunks
    ]

    if len(chunk_ids) != len(set(chunk_ids)):
        raise ValueError(
            "Duplicate chunk IDs detected"
        )

    return tuple(chunks)
