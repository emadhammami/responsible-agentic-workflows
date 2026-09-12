"""Build page-level processed artifacts for a benchmark corpus."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path

from responsible_agentic_workflows.ingestion import (
    extract_pdf_document,
)


def _load_json(path: Path) -> dict[str, object]:
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def _pdftotext_version() -> str:
    result = subprocess.run(
        ["pdftotext", "-v"],
        capture_output=True,
        text=True,
        check=False,
    )

    output = (
        result.stderr.strip()
        or result.stdout.strip()
    )

    first_line = (
        output.splitlines()[0]
        if output
        else "unknown"
    )

    return first_line


def build_page_artifacts(
    *,
    use_case_id: str,
    manifest_path: Path,
    scope_path: Path,
    quality_directory: Path,
    output_directory: Path,
) -> dict[str, object]:
    """Extract all benchmark-active PDFs into page-level JSON artifacts."""

    manifest = _load_json(manifest_path)
    scope = _load_json(scope_path)

    if scope["use_case_id"] != use_case_id:
        raise ValueError(
            "Scope use_case_id does not match requested use case"
        )

    if scope["status"] != "working":
        raise ValueError(
            "Page extraction currently requires a working scope"
        )

    active_ids = tuple(
        scope["benchmark_active_document_ids"]
    )

    if not active_ids:
        raise ValueError(
            "Benchmark scope contains no active documents"
        )

    if len(active_ids) != len(set(active_ids)):
        raise ValueError(
            "Benchmark scope contains duplicate document IDs"
        )

    documents = {
        document["document_id"]: document
        for document in manifest["documents"]
    }

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
                f"Processed page artifacts already exist: "
                f"{output_directory}"
            )

        output_directory.rmdir()

    staging.mkdir(
        parents=True,
        exist_ok=False,
    )

    index_documents: list[dict[str, object]] = []
    all_page_ids: set[str] = set()
    total_pages = 0
    total_words = 0

    try:
        for document_id in active_ids:
            if document_id not in documents:
                raise ValueError(
                    f"Active document missing from manifest: "
                    f"{document_id}"
                )

            record = documents[document_id]

            if record["status"] != "accepted":
                raise ValueError(
                    f"Active document is not accepted: "
                    f"{document_id}"
                )

            if record["use_case_id"] != use_case_id:
                raise ValueError(
                    f"Document belongs to another use case: "
                    f"{document_id}"
                )

            quality_path = (
                quality_directory
                / f"{document_id}.json"
            )

            if not quality_path.is_file():
                raise FileNotFoundError(
                    quality_path
                )

            quality = _load_json(
                quality_path
            )

            if quality["quality_status"] != "pass":
                raise ValueError(
                    f"Quality status is not pass: "
                    f"{document_id}"
                )

            if quality["issues"]:
                raise ValueError(
                    f"Quality issues remain: "
                    f"{document_id}"
                )

            source = Path(
                record["local_raw_path"]
            )

            extracted = extract_pdf_document(
                source,
                document_id=document_id,
                title=record["title"],
                expected_sha256=record["sha256"],
            )

            expected_pages = (
                quality["metrics"]["pages"]
            )

            if len(extracted.pages) != expected_pages:
                raise ValueError(
                    f"Page count mismatch for {document_id}: "
                    f"{len(extracted.pages)} != "
                    f"{expected_pages}"
                )

            page_ids = [
                page.page_id
                for page in extracted.pages
            ]

            if len(page_ids) != len(set(page_ids)):
                raise ValueError(
                    f"Duplicate page IDs within {document_id}"
                )

            overlap = (
                all_page_ids
                & set(page_ids)
            )

            if overlap:
                raise ValueError(
                    "Duplicate page IDs across documents: "
                    + ",".join(sorted(overlap))
                )

            all_page_ids.update(page_ids)

            extracted_words = sum(
                len(page.text.split())
                for page in extracted.pages
            )

            expected_words = (
                quality["metrics"]["words"]
            )

            if extracted_words != expected_words:
                raise ValueError(
                    f"Word count mismatch for {document_id}: "
                    f"{extracted_words} != "
                    f"{expected_words}"
                )

            artifact = {
                "schema_version": "0.1",
                "use_case_id": use_case_id,
                "document_id": document_id,
                "title": extracted.title,
                "source_path": extracted.source_path,
                "source_sha256": extracted.source_sha256,
                "page_count": len(extracted.pages),
                "pages": [
                    {
                        "document_id": page.document_id,
                        "page_id": page.page_id,
                        "page_number": page.page_number,
                        "title": page.title,
                        "text": page.text,
                        "source_path": page.source_path,
                        "source_sha256": page.source_sha256,
                    }
                    for page in extracted.pages
                ],
            }

            artifact_name = (
                f"{document_id}.pages.json"
            )

            artifact_path = (
                staging
                / artifact_name
            )

            artifact_path.write_text(
                json.dumps(
                    artifact,
                    indent=2,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )

            total_pages += len(
                extracted.pages
            )
            total_words += extracted_words

            index_documents.append(
                {
                    "document_id": document_id,
                    "artifact_file": artifact_name,
                    "source_sha256": (
                        extracted.source_sha256
                    ),
                    "page_count": len(
                        extracted.pages
                    ),
                    "word_count": extracted_words,
                }
            )

        index = {
            "schema_version": "0.1",
            "use_case_id": use_case_id,
            "status": "working",
            "artifact_type": "page_extraction",
            "extractor": {
                "tool": "pdftotext",
                "layout": True,
                "version": _pdftotext_version(),
            },
            "document_count": len(
                index_documents
            ),
            "total_pages": total_pages,
            "total_words": total_words,
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

        staging.replace(
            output_directory
        )

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
        "--manifest",
        type=Path,
        default=Path(
            "corpus/manifest.json"
        ),
    )

    parser.add_argument(
        "--scope",
        type=Path,
    )

    parser.add_argument(
        "--quality-directory",
        type=Path,
    )

    parser.add_argument(
        "--output-directory",
        type=Path,
    )

    args = parser.parse_args()

    use_case = args.use_case

    scope = (
        args.scope
        or Path(
            f"corpus/use_cases/"
            f"{use_case}/benchmark_scope.json"
        )
    )

    quality_directory = (
        args.quality_directory
        or Path(
            f"corpus/quality/{use_case}"
        )
    )

    output_directory = (
        args.output_directory
        or Path(
            f"corpus/use_cases/"
            f"{use_case}/processed/pages"
        )
    )

    index = build_page_artifacts(
        use_case_id=use_case,
        manifest_path=args.manifest,
        scope_path=scope,
        quality_directory=quality_directory,
        output_directory=output_directory,
    )

    print(
        f"DOCUMENT_COUNT="
        f"{index['document_count']}"
    )
    print(
        f"TOTAL_PAGES="
        f"{index['total_pages']}"
    )
    print(
        f"TOTAL_WORDS="
        f"{index['total_words']}"
    )
    print(
        f"OUTPUT_DIRECTORY="
        f"{output_directory}"
    )


if __name__ == "__main__":
    main()
