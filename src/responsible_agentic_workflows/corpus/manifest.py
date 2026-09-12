"""Real corpus manifest and provenance utilities."""

import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

DEFAULT_MANIFEST = Path("corpus/manifest.json")
DEFAULT_MANIFEST_SCHEMA = Path("corpus/manifest.schema.json")


def sha256_file(path: str | Path) -> str:
    """Return the SHA-256 digest of one source file."""

    digest = hashlib.sha256()

    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def validate_corpus_manifest(
    manifest: dict[str, object],
    *,
    schema_path: str | Path = DEFAULT_MANIFEST_SCHEMA,
) -> None:
    """Validate corpus structure and cross-record constraints."""

    schema = json.loads(
        Path(schema_path).read_text(encoding="utf-8")
    )

    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(manifest)

    use_cases = manifest["use_cases"]
    documents = manifest["documents"]

    use_case_ids = [
        use_case["use_case_id"]
        for use_case in use_cases
    ]

    if len(use_case_ids) != len(set(use_case_ids)):
        raise ValueError(
            "Duplicate use_case_id in corpus manifest"
        )

    document_ids = [
        document["document_id"]
        for document in documents
    ]

    if len(document_ids) != len(set(document_ids)):
        raise ValueError(
            "Duplicate document_id in corpus manifest"
        )

    hashes = [
        document["sha256"]
        for document in documents
    ]

    if len(hashes) != len(set(hashes)):
        raise ValueError(
            "Duplicate document content in corpus manifest"
        )

    known_use_cases = set(use_case_ids)

    for document in documents:
        use_case_id = document["use_case_id"]

        if use_case_id not in known_use_cases:
            raise ValueError(
                f"Unknown use_case_id for document: {use_case_id}"
            )

        expected_prefix = (
            f"corpus/use_cases/{use_case_id}/raw/"
        )

        if not document["local_raw_path"].startswith(
            expected_prefix
        ):
            raise ValueError(
                "Document raw path does not match its use case"
            )


def load_corpus_manifest(
    path: str | Path = DEFAULT_MANIFEST,
) -> dict[str, object]:
    """Load and validate the real corpus manifest."""

    manifest = json.loads(
        Path(path).read_text(encoding="utf-8")
    )

    validate_corpus_manifest(manifest)

    return manifest
