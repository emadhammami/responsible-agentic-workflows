"""Mechanical quality checks for real corpus PDF documents."""

import argparse
import json
import shutil
import subprocess
from pathlib import Path

from .manifest import (
    load_corpus_manifest,
    sha256_file,
)


def _require_tool(name: str) -> str:
    path = shutil.which(name)

    if path is None:
        raise RuntimeError(
            f"Required PDF tool is not available: {name}"
        )

    return path


def _pdf_pages(pdfinfo_output: str) -> int:
    for line in pdfinfo_output.splitlines():
        if line.startswith("Pages:"):
            return int(
                line.split(":", 1)[1].strip()
            )

    raise ValueError(
        "PDF page count was not reported by pdfinfo"
    )


def _pdf_encrypted(pdfinfo_output: str) -> bool:
    for line in pdfinfo_output.splitlines():
        if line.startswith("Encrypted:"):
            value = (
                line.split(":", 1)[1]
                .strip()
                .lower()
            )
            return value.startswith("yes")

    return False


def inspect_document_quality(
    document_id: str,
    *,
    manifest_path: str | Path = "corpus/manifest.json",
    reports_directory: str | Path | None = None,
    minimum_characters: int = 1000,
    minimum_nonempty_lines: int = 50,
) -> dict[str, object]:
    """Inspect one registered PDF and persist a quality report."""

    manifest_path = Path(manifest_path)
    manifest = load_corpus_manifest(manifest_path)

    matches = [
        document
        for document in manifest["documents"]
        if document["document_id"] == document_id
    ]

    if not matches:
        raise ValueError(
            f"Unknown document_id: {document_id}"
        )

    document = matches[0]

    repository_root = (
        manifest_path.resolve().parent.parent
    )

    source_path = (
        repository_root
        / str(document["local_raw_path"])
    )

    if not source_path.is_file():
        raise FileNotFoundError(
            f"Source file not found: {source_path}"
        )

    if source_path.read_bytes()[:5] != b"%PDF-":
        raise ValueError(
            f"Source is not a PDF: {document_id}"
        )

    actual_digest = sha256_file(source_path)

    if actual_digest != document["sha256"]:
        raise ValueError(
            f"Source hash mismatch for {document_id}"
        )

    pdfinfo = _require_tool("pdfinfo")
    pdftotext = _require_tool("pdftotext")

    info_result = subprocess.run(
        [
            pdfinfo,
            str(source_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    text_result = subprocess.run(
        [
            pdftotext,
            "-layout",
            str(source_path),
            "-",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    pages = _pdf_pages(
        info_result.stdout
    )
    encrypted = _pdf_encrypted(
        info_result.stdout
    )

    text = text_result.stdout
    lines = text.splitlines()

    character_count = len(text)
    word_count = len(text.split())
    line_count = len(lines)
    nonempty_line_count = sum(
        bool(line.strip())
        for line in lines
    )

    issues: list[str] = []

    if pages < 1:
        issues.append("no_pages")

    if encrypted:
        issues.append("encrypted_pdf")

    if character_count < minimum_characters:
        issues.append(
            "insufficient_extracted_text"
        )

    if nonempty_line_count < minimum_nonempty_lines:
        issues.append(
            "insufficient_content_density"
        )

    report = {
        "schema_version": "0.1",
        "document_id": document_id,
        "use_case_id": document["use_case_id"],
        "source_sha256": actual_digest,
        "document_status": document["status"],
        "quality_status": (
            "pass"
            if not issues
            else "review"
        ),
        "metrics": {
            "pages": pages,
            "file_size_bytes": source_path.stat().st_size,
            "characters": character_count,
            "words": word_count,
            "lines": line_count,
            "nonempty_lines": nonempty_line_count,
            "encrypted": encrypted,
        },
        "issues": issues,
    }

    if reports_directory is None:
        reports_directory = (
            repository_root
            / "corpus"
            / "quality"
            / str(document["use_case_id"])
        )
    else:
        reports_directory = Path(
            reports_directory
        )

    reports_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path = (
        reports_directory
        / f"{document_id}.json"
    )

    report_path.write_text(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    return report


def inspect_use_case_quality(
    use_case_id: str,
    *,
    status: str | None = None,
    manifest_path: str | Path = "corpus/manifest.json",
) -> list[dict[str, object]]:
    """Inspect all matching documents in one use case."""

    manifest = load_corpus_manifest(
        manifest_path
    )

    document_ids = [
        str(document["document_id"])
        for document in manifest["documents"]
        if document["use_case_id"] == use_case_id
        and (
            status is None
            or document["status"] == status
        )
    ]

    return [
        inspect_document_quality(
            document_id,
            manifest_path=manifest_path,
        )
        for document_id in document_ids
    ]


def main() -> None:
    """Run corpus PDF quality checks."""

    parser = argparse.ArgumentParser(
        description=(
            "Run mechanical PDF quality checks for corpus documents."
        )
    )

    parser.add_argument(
        "document_ids",
        nargs="*",
    )

    parser.add_argument(
        "--use-case",
    )

    parser.add_argument(
        "--status",
        choices=[
            "candidate",
            "accepted",
        ],
    )

    args = parser.parse_args()

    if args.document_ids:
        reports = [
            inspect_document_quality(
                document_id
            )
            for document_id in args.document_ids
        ]
    else:
        if not args.use_case:
            parser.error(
                "Provide document IDs or --use-case."
            )

        reports = inspect_use_case_quality(
            args.use_case,
            status=args.status,
        )

    for report in reports:
        metrics = report["metrics"]

        print(
            f'DOCUMENT_ID={report["document_id"]}'
        )
        print(
            f'QUALITY_STATUS={report["quality_status"]}'
        )
        print(
            f'PAGES={metrics["pages"]}'
        )
        print(
            f'WORDS={metrics["words"]}'
        )
        print(
            f'CHARACTERS={metrics["characters"]}'
        )
        print(
            f'NONEMPTY_LINES={metrics["nonempty_lines"]}'
        )
        print(
            f'ISSUES={",".join(report["issues"]) or "none"}'
        )


if __name__ == "__main__":
    main()
