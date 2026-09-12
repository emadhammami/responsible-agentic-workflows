import hashlib
import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.batch_intake import (
    load_intake_queue,
    register_candidate_batch,
)


def _schema_path() -> Path:
    return Path(
        "corpus/manifest.schema.json"
    ).resolve()


def _queue_schema_path() -> Path:
    return Path(
        "corpus/intake_queue.schema.json"
    ).resolve()


def _repository(
    tmp_path: Path,
) -> tuple[Path, Path, Path]:
    repository = tmp_path / "repository"

    corpus = repository / "corpus"

    raw = (
        corpus
        / "use_cases"
        / "UC1"
        / "raw"
    )

    raw.mkdir(parents=True)

    existing = raw / "DOC001_existing.pdf"
    existing.write_bytes(
        b"existing policy"
    )

    existing_digest = hashlib.sha256(
        existing.read_bytes()
    ).hexdigest()

    manifest = {
        "schema_version": "0.1",
        "corpus_id": "thesis-real-corpus-v0.1",
        "status": "working",
        "use_cases": [
            {
                "use_case_id": "UC1",
                "name": "OptFor-EU Forest Policy",
                "source_organization": "OptFor-EU",
                "source_url": "https://optforeu.eu/policy-map/",
                "status": "working",
                "notes": None,
            }
        ],
        "documents": [
            {
                "document_id": "DOC001",
                "use_case_id": "UC1",
                "title": "Existing Policy",
                "source_organization": "Example",
                "source_reference": "Existing",
                "source_url": None,
                "discovered_via": "OptFor-EU Policy Map",
                "publication_date": None,
                "language": "en",
                "document_type": "policy",
                "rights_note": None,
                "local_raw_path": (
                    "corpus/use_cases/UC1/raw/"
                    "DOC001_existing.pdf"
                ),
                "local_processed_path": None,
                "sha256": existing_digest,
                "status": "accepted",
                "exclusion_reason": None,
            }
        ],
    }

    manifest_path = (
        corpus / "manifest.json"
    )

    manifest_path.write_text(
        json.dumps(manifest),
        encoding="utf-8",
    )

    (
        corpus / "manifest.schema.json"
    ).write_text(
        _schema_path().read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )

    (
        corpus / "intake_queue.schema.json"
    ).write_text(
        _queue_schema_path().read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )

    return repository, manifest_path, raw


def _entry(
    source_file: str,
    *,
    title: str,
) -> dict[str, object]:
    return {
        "source_file": source_file,
        "title": title,
        "source_organization": "Example Organisation",
        "source_reference": title,
        "source_url": "https://example.org/policy",
        "discovered_via": "OptFor-EU Policy Map",
        "publication_date": "2025-01-01",
        "language": "en",
        "document_type": "policy",
        "rights_note": "Research source",
    }


def _write_queue(
    repository: Path,
    documents: list[dict[str, object]],
) -> Path:
    queue_path = (
        repository
        / "corpus"
        / "queue.json"
    )

    queue = {
        "schema_version": "0.1",
        "use_case_id": "UC1",
        "documents": documents,
    }

    queue_path.write_text(
        json.dumps(queue),
        encoding="utf-8",
    )

    return queue_path


def test_empty_queue_is_valid(
    tmp_path,
) -> None:
    repository, _, _ = _repository(
        tmp_path
    )

    queue_path = _write_queue(
        repository,
        [],
    )

    queue = load_intake_queue(
        queue_path,
        schema_path=(
            repository
            / "corpus"
            / "intake_queue.schema.json"
        ),
    )

    assert queue["documents"] == []


def test_batch_registration_assigns_sequential_ids(
    tmp_path,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    second = raw / "second.pdf"
    third = raw / "third.pdf"

    second.write_bytes(b"second policy")
    third.write_bytes(b"third policy")

    queue_path = _write_queue(
        repository,
        [
            _entry(
                "corpus/use_cases/UC1/raw/second.pdf",
                title="Second Policy",
            ),
            _entry(
                "corpus/use_cases/UC1/raw/third.pdf",
                title="Third Policy",
            ),
        ],
    )

    registered = register_candidate_batch(
        queue_path,
        manifest_path=manifest_path,
        queue_schema_path=(
            repository
            / "corpus"
            / "intake_queue.schema.json"
        ),
    )

    assert [
        document["document_id"]
        for document in registered
    ] == [
        "DOC002",
        "DOC003",
    ]

    assert all(
        document["status"] == "candidate"
        for document in registered
    )

    saved = json.loads(
        manifest_path.read_text(
            encoding="utf-8"
        )
    )

    assert len(saved["documents"]) == 3


def test_missing_file_leaves_manifest_unchanged(
    tmp_path,
) -> None:
    repository, manifest_path, _ = _repository(
        tmp_path
    )

    before = manifest_path.read_text(
        encoding="utf-8"
    )

    queue_path = _write_queue(
        repository,
        [
            _entry(
                "corpus/use_cases/UC1/raw/missing.pdf",
                title="Missing Policy",
            )
        ],
    )

    with pytest.raises(
        FileNotFoundError,
        match="Source file not found",
    ):
        register_candidate_batch(
            queue_path,
            manifest_path=manifest_path,
            queue_schema_path=(
                repository
                / "corpus"
                / "intake_queue.schema.json"
            ),
        )

    assert (
        manifest_path.read_text(
            encoding="utf-8"
        )
        == before
    )


def test_duplicate_queue_content_leaves_manifest_unchanged(
    tmp_path,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    first = raw / "first.pdf"
    second = raw / "second.pdf"

    first.write_bytes(b"duplicate")
    second.write_bytes(b"duplicate")

    before = manifest_path.read_text(
        encoding="utf-8"
    )

    queue_path = _write_queue(
        repository,
        [
            _entry(
                "corpus/use_cases/UC1/raw/first.pdf",
                title="First Policy",
            ),
            _entry(
                "corpus/use_cases/UC1/raw/second.pdf",
                title="Second Policy",
            ),
        ],
    )

    with pytest.raises(
        ValueError,
        match="Duplicate document content",
    ):
        register_candidate_batch(
            queue_path,
            manifest_path=manifest_path,
            queue_schema_path=(
                repository
                / "corpus"
                / "intake_queue.schema.json"
            ),
        )

    assert (
        manifest_path.read_text(
            encoding="utf-8"
        )
        == before
    )


def test_existing_content_is_rejected(
    tmp_path,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    duplicate = raw / "duplicate.pdf"
    duplicate.write_bytes(
        b"existing policy"
    )

    queue_path = _write_queue(
        repository,
        [
            _entry(
                "corpus/use_cases/UC1/raw/duplicate.pdf",
                title="Duplicate Policy",
            )
        ],
    )

    with pytest.raises(
        ValueError,
        match="already registered",
    ):
        register_candidate_batch(
            queue_path,
            manifest_path=manifest_path,
            queue_schema_path=(
                repository
                / "corpus"
                / "intake_queue.schema.json"
            ),
        )
