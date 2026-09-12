"""Atomic batch registration of real corpus source documents."""

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from .intake import next_document_id
from .manifest import (
    load_corpus_manifest,
    sha256_file,
    validate_corpus_manifest,
)

DEFAULT_QUEUE_SCHEMA = Path(
    "corpus/intake_queue.schema.json"
)


def load_intake_queue(
    queue_path: str | Path,
    *,
    schema_path: str | Path = DEFAULT_QUEUE_SCHEMA,
) -> dict[str, object]:
    """Load and validate a batch intake queue."""

    queue_path = Path(queue_path)

    queue = json.loads(
        queue_path.read_text(encoding="utf-8")
    )

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(queue)

    return queue


def register_candidate_batch(
    queue_path: str | Path,
    *,
    manifest_path: str | Path = "corpus/manifest.json",
    queue_schema_path: str | Path = DEFAULT_QUEUE_SCHEMA,
) -> list[dict[str, object]]:
    """Register all queue entries atomically as candidates."""

    manifest_path = Path(manifest_path)

    manifest = load_corpus_manifest(
        manifest_path
    )

    queue = load_intake_queue(
        queue_path,
        schema_path=queue_schema_path,
    )

    use_case_id = str(
        queue["use_case_id"]
    )

    known_use_cases = {
        str(use_case["use_case_id"])
        for use_case in manifest["use_cases"]
    }

    if use_case_id not in known_use_cases:
        raise ValueError(
            f"Unknown use_case_id: {use_case_id}"
        )

    repository_root = (
        manifest_path.resolve().parent.parent
    )

    expected_raw_directory = (
        repository_root
        / "corpus"
        / "use_cases"
        / use_case_id
        / "raw"
    ).resolve()

    existing_hashes = {
        str(document["sha256"])
        for document in manifest["documents"]
    }

    existing_paths = {
        str(document["local_raw_path"])
        for document in manifest["documents"]
    }

    prepared: list[
        tuple[dict[str, object], Path, str, str]
    ] = []

    queued_hashes: set[str] = set()
    queued_paths: set[str] = set()

    for entry in queue["documents"]:
        source_path = (
            repository_root
            / str(entry["source_file"])
        ).resolve()

        if not source_path.is_file():
            raise FileNotFoundError(
                f"Source file not found: {source_path}"
            )

        try:
            source_path.relative_to(
                expected_raw_directory
            )
        except ValueError as exc:
            raise ValueError(
                "Queued source file must be stored in "
                "the use case raw directory"
            ) from exc

        relative_path = (
            source_path
            .relative_to(repository_root)
            .as_posix()
        )

        if relative_path in existing_paths:
            raise ValueError(
                f"Source path is already registered: "
                f"{relative_path}"
            )

        if relative_path in queued_paths:
            raise ValueError(
                f"Duplicate source path in intake queue: "
                f"{relative_path}"
            )

        digest = sha256_file(source_path)

        if digest in existing_hashes:
            raise ValueError(
                "Document content is already registered"
            )

        if digest in queued_hashes:
            raise ValueError(
                "Duplicate document content in intake queue"
            )

        queued_paths.add(relative_path)
        queued_hashes.add(digest)

        prepared.append(
            (
                entry,
                source_path,
                relative_path,
                digest,
            )
        )

    documents = list(
        manifest["documents"]
    )

    registered: list[
        dict[str, object]
    ] = []

    for entry, _, relative_path, digest in prepared:
        document_id = next_document_id(
            documents
        )

        document = {
            "document_id": document_id,
            "use_case_id": use_case_id,
            "title": entry["title"],
            "source_organization": (
                entry["source_organization"]
            ),
            "source_reference": (
                entry["source_reference"]
            ),
            "source_url": entry["source_url"],
            "discovered_via": (
                entry["discovered_via"]
            ),
            "publication_date": (
                entry["publication_date"]
            ),
            "language": entry["language"],
            "document_type": (
                entry["document_type"]
            ),
            "rights_note": (
                entry["rights_note"]
            ),
            "local_raw_path": relative_path,
            "local_processed_path": None,
            "sha256": digest,
            "status": "candidate",
            "exclusion_reason": None,
        }

        documents.append(document)
        registered.append(document)

    updated_manifest = dict(manifest)
    updated_manifest["documents"] = documents

    validate_corpus_manifest(
        updated_manifest
    )

    temporary_path = (
        manifest_path.with_suffix(
            ".json.tmp"
        )
    )

    temporary_path.write_text(
        json.dumps(
            updated_manifest,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    temporary_path.replace(
        manifest_path
    )

    return registered


def main() -> None:
    """Register a batch intake queue."""

    parser = argparse.ArgumentParser(
        description=(
            "Register a validated batch of real corpus "
            "documents as candidates."
        )
    )

    parser.add_argument(
        "queue_path",
    )

    args = parser.parse_args()

    registered = register_candidate_batch(
        args.queue_path
    )

    print(
        f"REGISTERED_COUNT={len(registered)}"
    )

    for document in registered:
        print(
            f'{document["document_id"]}='
            f'{document["local_raw_path"]}'
        )


if __name__ == "__main__":
    main()
