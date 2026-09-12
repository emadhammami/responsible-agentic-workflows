"""Materialize deterministic retrieval chunks from page artifacts."""

import argparse
import json
import shutil
from pathlib import Path

from responsible_agentic_workflows.ingestion import (
    DocumentPage,
    ExtractedPdfDocument,
    chunk_pdf_document,
)


def _load_json(path: Path) -> dict[str, object]:
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def build_chunk_artifacts(
    *,
    use_case_id: str,
    page_directory: Path,
    config_path: Path,
    output_directory: Path,
) -> dict[str, object]:
    """Build retrieval chunk artifacts from page-level source artifacts."""

    config = _load_json(config_path)

    if config["use_case_id"] != use_case_id:
        raise ValueError(
            "Chunking config use_case_id does not match requested use case"
        )

    if config["status"] != "working":
        raise ValueError(
            "Chunking config must be working during materialization"
        )

    if config["strategy"] != "page_aware_word_windows":
        raise ValueError(
            f"Unsupported chunking strategy: {config['strategy']}"
        )

    if config["cross_page_boundaries"] is not False:
        raise ValueError(
            "Cross-page chunking is not supported"
        )

    if config["empty_pages_generate_chunks"] is not False:
        raise ValueError(
            "Empty pages must not generate retrieval chunks"
        )

    max_words = config["max_words"]
    overlap_words = config["overlap_words"]

    if not isinstance(max_words, int):
        raise ValueError("max_words must be an integer")

    if not isinstance(overlap_words, int):
        raise ValueError("overlap_words must be an integer")

    page_index_path = page_directory / "index.json"

    if not page_index_path.is_file():
        raise FileNotFoundError(page_index_path)

    page_index = _load_json(page_index_path)

    if page_index["use_case_id"] != use_case_id:
        raise ValueError(
            "Page index use_case_id mismatch"
        )

    staging = output_directory.with_name(
        output_directory.name + ".staging"
    )

    if staging.exists():
        shutil.rmtree(staging)

    if output_directory.exists():
        existing = [
            path
            for path in output_directory.rglob("*")
            if path.is_file()
        ]

        if existing:
            raise FileExistsError(
                f"Chunk artifacts already exist: "
                f"{output_directory}"
            )

        output_directory.rmdir()

    staging.mkdir(
        parents=True,
        exist_ok=False,
    )

    index_documents: list[dict[str, object]] = []
    all_chunk_ids: set[str] = set()
    pages_with_chunks: set[str] = set()

    total_chunks = 0
    total_chunk_words = 0

    try:
        for item in page_index["documents"]:
            document_id = item["document_id"]

            page_artifact_path = (
                page_directory
                / item["artifact_file"]
            )

            page_artifact = _load_json(
                page_artifact_path
            )

            pages = tuple(
                DocumentPage(
                    document_id=page["document_id"],
                    page_id=page["page_id"],
                    title=page["title"],
                    page_number=page["page_number"],
                    text=page["text"],
                    source_path=page["source_path"],
                    source_sha256=page["source_sha256"],
                )
                for page in page_artifact["pages"]
            )

            document = ExtractedPdfDocument(
                document_id=document_id,
                title=page_artifact["title"],
                source_path=page_artifact["source_path"],
                source_sha256=page_artifact["source_sha256"],
                pages=pages,
            )

            chunks = chunk_pdf_document(
                document,
                max_words=max_words,
                overlap_words=overlap_words,
            )

            chunk_ids = [
                chunk.chunk_id
                for chunk in chunks
            ]

            if len(chunk_ids) != len(set(chunk_ids)):
                raise ValueError(
                    f"Duplicate chunk IDs in {document_id}"
                )

            overlap = (
                all_chunk_ids
                & set(chunk_ids)
            )

            if overlap:
                raise ValueError(
                    "Duplicate chunk IDs across documents: "
                    + ",".join(sorted(overlap))
                )

            all_chunk_ids.update(chunk_ids)

            artifact_chunks = []

            for chunk in chunks:
                word_count = len(
                    chunk.text.split()
                )

                if word_count > max_words:
                    raise ValueError(
                        f"Chunk exceeds max_words: "
                        f"{chunk.chunk_id}"
                    )

                page_id = (
                    f"{chunk.document_id}-"
                    f"P{chunk.page:04d}"
                )

                pages_with_chunks.add(page_id)

                artifact_chunks.append(
                    {
                        "document_id": chunk.document_id,
                        "chunk_id": chunk.chunk_id,
                        "title": chunk.title,
                        "section": chunk.section,
                        "section_index": chunk.section_index,
                        "text": chunk.text,
                        "source_file": chunk.source_file,
                        "page": chunk.page,
                        "page_id": page_id,
                        "source_sha256": (
                            page_artifact["source_sha256"]
                        ),
                        "word_count": word_count,
                    }
                )

                total_chunk_words += word_count

            total_chunks += len(chunks)

            artifact_name = (
                f"{document_id}.chunks.json"
            )

            artifact = {
                "schema_version": "0.1",
                "use_case_id": use_case_id,
                "document_id": document_id,
                "title": document.title,
                "source_sha256": document.source_sha256,
                "chunking_config_id": config["config_id"],
                "chunk_count": len(chunks),
                "chunks": artifact_chunks,
            }

            (
                staging
                / artifact_name
            ).write_text(
                json.dumps(
                    artifact,
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            index_documents.append(
                {
                    "document_id": document_id,
                    "artifact_file": artifact_name,
                    "source_sha256": document.source_sha256,
                    "page_count": len(pages),
                    "chunk_count": len(chunks),
                }
            )

        index = {
            "schema_version": "0.1",
            "use_case_id": use_case_id,
            "status": "working",
            "artifact_type": "retrieval_chunks",
            "chunking_config_id": config["config_id"],
            "strategy": config["strategy"],
            "max_words": max_words,
            "overlap_words": overlap_words,
            "document_count": len(index_documents),
            "total_chunks": total_chunks,
            "total_chunk_words": total_chunk_words,
            "pages_with_chunks": len(pages_with_chunks),
            "documents": index_documents,
        }

        (
            staging
            / "index.json"
        ).write_text(
            json.dumps(
                index,
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

        staging.replace(output_directory)

        return index

    except Exception:
        if staging.exists():
            shutil.rmtree(staging)

        raise


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--use-case",
        required=True,
    )

    parser.add_argument(
        "--page-directory",
        type=Path,
    )

    parser.add_argument(
        "--config",
        type=Path,
    )

    parser.add_argument(
        "--output-directory",
        type=Path,
    )

    args = parser.parse_args()

    use_case = args.use_case

    page_directory = (
        args.page_directory
        or Path(
            f"corpus/use_cases/{use_case}/"
            "processed/pages"
        )
    )

    config_path = (
        args.config
        or Path(
            f"corpus/use_cases/{use_case}/"
            "chunking_config.json"
        )
    )

    output_directory = (
        args.output_directory
        or Path(
            f"corpus/use_cases/{use_case}/"
            "processed/chunks"
        )
    )

    index = build_chunk_artifacts(
        use_case_id=use_case,
        page_directory=page_directory,
        config_path=config_path,
        output_directory=output_directory,
    )

    print(
        f"DOCUMENT_COUNT={index['document_count']}"
    )
    print(
        f"TOTAL_CHUNKS={index['total_chunks']}"
    )
    print(
        f"TOTAL_CHUNK_WORDS="
        f"{index['total_chunk_words']}"
    )
    print(
        f"PAGES_WITH_CHUNKS="
        f"{index['pages_with_chunks']}"
    )
    print(
        f"OUTPUT_DIRECTORY={output_directory}"
    )


if __name__ == "__main__":
    main()
