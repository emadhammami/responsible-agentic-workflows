from responsible_agentic_workflows.ingestion import (
    DocumentPage,
    ExtractedPdfDocument,
    chunk_pdf_document,
)


def _document(
    *page_texts: str,
) -> ExtractedPdfDocument:
    digest = "a" * 64
    source_path = (
        "corpus/use_cases/UC1/raw/"
        "DOC999_example.pdf"
    )

    pages = tuple(
        DocumentPage(
            document_id="DOC999",
            page_id=f"DOC999-P{number:04d}",
            title="Example Policy",
            page_number=number,
            text=text,
            source_path=source_path,
            source_sha256=digest,
        )
        for number, text in enumerate(
            page_texts,
            start=1,
        )
    )

    return ExtractedPdfDocument(
        document_id="DOC999",
        title="Example Policy",
        source_path=source_path,
        source_sha256=digest,
        pages=pages,
    )


def test_short_page_produces_one_chunk() -> None:
    document = _document(
        "one two three four five"
    )

    chunks = chunk_pdf_document(
        document,
        max_words=10,
        overlap_words=2,
    )

    assert len(chunks) == 1

    chunk = chunks[0]

    assert chunk.chunk_id == "DOC999-P0001-C001"
    assert chunk.document_id == "DOC999"
    assert chunk.page == 1
    assert chunk.section == "Page 1"
    assert chunk.section_index == 1
    assert chunk.text == "one two three four five"
    assert chunk.source_file == "DOC999_example.pdf"


def test_long_page_uses_deterministic_overlap() -> None:
    document = _document(
        "one two three four five six seven eight"
    )

    chunks = chunk_pdf_document(
        document,
        max_words=5,
        overlap_words=2,
    )

    assert [
        chunk.chunk_id
        for chunk in chunks
    ] == [
        "DOC999-P0001-C001",
        "DOC999-P0001-C002",
    ]

    assert chunks[0].text == (
        "one two three four five"
    )

    assert chunks[1].text == (
        "four five six seven eight"
    )


def test_chunks_never_cross_page_boundaries() -> None:
    document = _document(
        "one two three four five six",
        "seven eight nine ten eleven twelve",
    )

    chunks = chunk_pdf_document(
        document,
        max_words=4,
        overlap_words=1,
    )

    assert [
        chunk.page
        for chunk in chunks
    ] == [
        1,
        1,
        2,
        2,
    ]

    assert [
        chunk.chunk_id
        for chunk in chunks
    ] == [
        "DOC999-P0001-C001",
        "DOC999-P0001-C002",
        "DOC999-P0002-C001",
        "DOC999-P0002-C002",
    ]

    assert all(
        "seven" not in chunk.text
        for chunk in chunks
        if chunk.page == 1
    )

    assert all(
        "six" not in chunk.text
        for chunk in chunks
        if chunk.page == 2
    )


def test_empty_pages_do_not_produce_chunks() -> None:
    document = _document(
        "",
        "real policy text",
        "   ",
    )

    chunks = chunk_pdf_document(
        document,
        max_words=100,
        overlap_words=20,
    )

    assert len(chunks) == 1
    assert chunks[0].page == 2
    assert chunks[0].chunk_id == (
        "DOC999-P0002-C001"
    )


def test_original_whitespace_inside_window_is_preserved() -> None:
    document = _document(
        "Article 1\n\n"
        "Forest   management shall apply.\n"
        "Next line."
    )

    chunks = chunk_pdf_document(
        document,
        max_words=20,
        overlap_words=0,
    )

    assert len(chunks) == 1
    assert chunks[0].text == (
        "Article 1\n\n"
        "Forest   management shall apply.\n"
        "Next line."
    )


def test_invalid_chunking_parameters_are_rejected() -> None:
    document = _document(
        "example text"
    )

    invalid = [
        (0, 0),
        (100, -1),
        (100, 100),
        (100, 101),
    ]

    for max_words, overlap_words in invalid:
        try:
            chunk_pdf_document(
                document,
                max_words=max_words,
                overlap_words=overlap_words,
            )
        except ValueError:
            continue

        raise AssertionError(
            "Invalid chunking parameters were accepted"
        )
