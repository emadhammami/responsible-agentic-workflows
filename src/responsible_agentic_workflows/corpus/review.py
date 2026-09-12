"""Record corpus selection decisions."""

import argparse
import json
from pathlib import Path

from .manifest import (
    load_corpus_manifest,
    sha256_file,
    validate_corpus_manifest,
)


def _candidate(
    manifest: dict[str, object],
    document_id: str,
) -> dict[str, object]:
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

    if document["status"] != "candidate":
        raise ValueError(
            f"Document is not a candidate: {document_id}"
        )

    return document


def _verify_source(
    document: dict[str, object],
    *,
    repository_root: Path,
) -> str:
    source_path = (
        repository_root
        / str(document["local_raw_path"])
    )

    if not source_path.is_file():
        raise FileNotFoundError(
            f"Source file not found: {source_path}"
        )

    digest = sha256_file(source_path)

    if digest != document["sha256"]:
        raise ValueError(
            f"Source hash mismatch for "
            f'{document["document_id"]}'
        )

    return digest


def _write_manifest(
    manifest: dict[str, object],
    manifest_path: Path,
) -> None:
    validate_corpus_manifest(manifest)

    temporary = manifest_path.with_suffix(
        ".json.tmp"
    )

    temporary.write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary.replace(manifest_path)


def _write_review(
    *,
    document: dict[str, object],
    decision: str,
    digest: str,
    rationale: str,
    repository_root: Path,
    reviews_directory: str | Path | None,
) -> dict[str, object]:
    if reviews_directory is None:
        directory = (
            repository_root
            / "corpus"
            / "reviews"
            / str(document["use_case_id"])
        )
    else:
        directory = Path(
            reviews_directory
        )

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    record = {
        "schema_version": "0.1",
        "document_id": document["document_id"],
        "use_case_id": document["use_case_id"],
        "decision": decision,
        "source_sha256": digest,
        "rationale": rationale.strip(),
    }

    (
        directory
        / f'{document["document_id"]}.json'
    ).write_text(
        json.dumps(
            record,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    return record


def accept_candidate_document(
    document_id: str,
    *,
    rationale: str,
    manifest_path: str | Path = "corpus/manifest.json",
    reviews_directory: str | Path | None = None,
) -> dict[str, object]:
    """Accept one reviewed candidate document."""

    if not rationale.strip():
        raise ValueError(
            "Acceptance rationale must not be empty"
        )

    manifest_path = Path(
        manifest_path
    )

    manifest = load_corpus_manifest(
        manifest_path
    )

    document = _candidate(
        manifest,
        document_id,
    )

    repository_root = (
        manifest_path.resolve().parent.parent
    )

    digest = _verify_source(
        document,
        repository_root=repository_root,
    )

    document["status"] = "accepted"
    document["exclusion_reason"] = None

    _write_manifest(
        manifest,
        manifest_path,
    )

    return _write_review(
        document=document,
        decision="accepted",
        digest=digest,
        rationale=rationale,
        repository_root=repository_root,
        reviews_directory=reviews_directory,
    )


def exclude_candidate_document(
    document_id: str,
    *,
    rationale: str,
    manifest_path: str | Path = "corpus/manifest.json",
    reviews_directory: str | Path | None = None,
) -> dict[str, object]:
    """Exclude one reviewed candidate document."""

    if not rationale.strip():
        raise ValueError(
            "Exclusion rationale must not be empty"
        )

    manifest_path = Path(
        manifest_path
    )

    manifest = load_corpus_manifest(
        manifest_path
    )

    document = _candidate(
        manifest,
        document_id,
    )

    repository_root = (
        manifest_path.resolve().parent.parent
    )

    digest = _verify_source(
        document,
        repository_root=repository_root,
    )

    document["status"] = "excluded"
    document["exclusion_reason"] = rationale.strip()

    _write_manifest(
        manifest,
        manifest_path,
    )

    return _write_review(
        document=document,
        decision="excluded",
        digest=digest,
        rationale=rationale,
        repository_root=repository_root,
        reviews_directory=reviews_directory,
    )


def main() -> None:
    """Record a corpus selection decision."""

    parser = argparse.ArgumentParser(
        description="Record a corpus document review decision."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    for command in (
        "accept",
        "exclude",
    ):
        subparser = subparsers.add_parser(
            command,
        )

        subparser.add_argument(
            "document_id",
        )

        subparser.add_argument(
            "--rationale",
            required=True,
        )

    args = parser.parse_args()

    if args.command == "accept":
        review = accept_candidate_document(
            args.document_id,
            rationale=args.rationale,
        )
    else:
        review = exclude_candidate_document(
            args.document_id,
            rationale=args.rationale,
        )

    print(
        f'DOCUMENT_ID={review["document_id"]}'
    )
    print(
        f'DECISION={review["decision"]}'
    )
    print(
        f'SHA256={review["source_sha256"]}'
    )


if __name__ == "__main__":
    main()
