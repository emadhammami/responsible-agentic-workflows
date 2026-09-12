"""Register real source documents in the working corpus."""

import argparse
import json
from pathlib import Path

from .manifest import (
    load_corpus_manifest,
    sha256_file,
    validate_corpus_manifest,
)


def next_document_id(
    documents: list[dict[str, object]],
) -> str:
    """Return the next sequential corpus document identifier."""

    numbers = [
        int(str(document["document_id"])[3:])
        for document in documents
    ]

    next_number = max(numbers, default=0) + 1
    return f"DOC{next_number:03d}"


def register_candidate_document(
    *,
    source_file: str | Path,
    use_case_id: str,
    title: str,
    source_organization: str,
    source_reference: str,
    source_url: str | None = None,
    discovered_via: str | None = None,
    publication_date: str | None = None,
    language: str = "en",
    document_type: str = "policy",
    rights_note: str | None = None,
    manifest_path: str | Path = "corpus/manifest.json",
) -> dict[str, object]:
    """Register one local source file as a candidate document."""

    manifest_path = Path(manifest_path)
    manifest = load_corpus_manifest(manifest_path)

    known_use_cases = {
        use_case["use_case_id"]
        for use_case in manifest["use_cases"]
    }

    if use_case_id not in known_use_cases:
        raise ValueError(
            f"Unknown use_case_id: {use_case_id}"
        )

    source_file = Path(source_file).resolve()

    if not source_file.is_file():
        raise FileNotFoundError(
            f"Source file not found: {source_file}"
        )

    repository_root = manifest_path.resolve().parent.parent
    expected_raw_directory = (
        repository_root
        / "corpus"
        / "use_cases"
        / use_case_id
        / "raw"
    ).resolve()

    try:
        relative_source = source_file.relative_to(
            repository_root
        )
        source_file.relative_to(expected_raw_directory)
    except ValueError as exc:
        raise ValueError(
            "Source file must be stored in the use case raw directory"
        ) from exc

    digest = sha256_file(source_file)

    for document in manifest["documents"]:
        if document["sha256"] == digest:
            raise ValueError(
                "Document content is already registered"
            )

    document_id = next_document_id(
        manifest["documents"]
    )

    document = {
        "document_id": document_id,
        "use_case_id": use_case_id,
        "title": title,
        "source_organization": source_organization,
        "source_reference": source_reference,
        "source_url": source_url,
        "discovered_via": discovered_via,
        "publication_date": publication_date,
        "language": language,
        "document_type": document_type,
        "rights_note": rights_note,
        "local_raw_path": relative_source.as_posix(),
        "local_processed_path": None,
        "sha256": digest,
        "status": "candidate",
        "exclusion_reason": None,
    }

    manifest["documents"].append(document)

    validate_corpus_manifest(manifest)

    temporary_path = manifest_path.with_suffix(
        ".json.tmp"
    )

    temporary_path.write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary_path.replace(manifest_path)

    return document


def _optional(value: str) -> str | None:
    return value or None


def main() -> None:
    """Register one real source document from the command line."""

    parser = argparse.ArgumentParser(
        description=(
            "Register a real source document as a corpus candidate."
        )
    )

    parser.add_argument(
        "source_file",
        help="Path to a file already stored in the use-case raw directory.",
    )
    parser.add_argument(
        "--use-case",
        default="UC1",
    )
    parser.add_argument(
        "--title",
        required=True,
    )
    parser.add_argument(
        "--source-organization",
        required=True,
    )
    parser.add_argument(
        "--source-reference",
        required=True,
    )
    parser.add_argument(
        "--source-url",
        default="",
    )
    parser.add_argument(
        "--discovered-via",
        default="OptFor-EU Policy Map",
    )
    parser.add_argument(
        "--publication-date",
        default="",
    )
    parser.add_argument(
        "--language",
        default="en",
    )
    parser.add_argument(
        "--document-type",
        default="policy",
    )
    parser.add_argument(
        "--rights-note",
        default="",
    )

    args = parser.parse_args()

    document = register_candidate_document(
        source_file=args.source_file,
        use_case_id=args.use_case,
        title=args.title,
        source_organization=args.source_organization,
        source_reference=args.source_reference,
        source_url=_optional(args.source_url),
        discovered_via=_optional(args.discovered_via),
        publication_date=_optional(args.publication_date),
        language=args.language,
        document_type=args.document_type,
        rights_note=_optional(args.rights_note),
    )

    print(
        f'REGISTERED={document["document_id"]}'
    )
    print(
        f'SHA256={document["sha256"]}'
    )
    print("STATUS=candidate")


if __name__ == "__main__":
    main()
