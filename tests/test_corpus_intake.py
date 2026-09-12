import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.intake import (
    next_document_id,
    register_candidate_document,
)


def _write_manifest(
    repository: Path,
) -> Path:
    corpus_directory = repository / "corpus"
    corpus_directory.mkdir()

    manifest_path = corpus_directory / "manifest.json"

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
        "documents": [],
    }

    manifest_path.write_text(
        json.dumps(manifest),
        encoding="utf-8",
    )

    schema_target = corpus_directory / "manifest.schema.json"
    schema_target.write_text(
        _schema_path().read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    return manifest_path


def _schema_path() -> Path:
    return Path("corpus/manifest.schema.json").resolve()


def test_next_document_id_starts_at_doc001() -> None:
    assert next_document_id([]) == "DOC001"


def test_next_document_id_is_sequential() -> None:
    documents = [
        {"document_id": "DOC001"},
        {"document_id": "DOC002"},
    ]

    assert next_document_id(documents) == "DOC003"


def test_register_candidate_document(
    tmp_path,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()

    manifest_path = _write_manifest(repository)

    raw_directory = (
        repository
        / "corpus"
        / "use_cases"
        / "UC1"
        / "raw"
    )
    raw_directory.mkdir(parents=True)

    source = raw_directory / "policy.pdf"
    source.write_bytes(b"forest policy")

    document = register_candidate_document(
        source_file=source,
        use_case_id="UC1",
        title="Forest Policy",
        source_organization="Example Organisation",
        source_reference="Example reference",
        source_url="https://example.org/policy",
        discovered_via="OptFor-EU Policy Map",
        publication_date="2025",
        language="en",
        document_type="policy",
        rights_note="Research source",
        manifest_path=manifest_path,
    )

    assert document["document_id"] == "DOC001"
    assert document["status"] == "candidate"
    assert document["local_raw_path"] == (
        "corpus/use_cases/UC1/raw/policy.pdf"
    )

    saved = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )

    assert saved["documents"] == [document]


def test_duplicate_content_is_rejected(
    tmp_path,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()

    manifest_path = _write_manifest(repository)

    raw_directory = (
        repository
        / "corpus"
        / "use_cases"
        / "UC1"
        / "raw"
    )
    raw_directory.mkdir(parents=True)

    first = raw_directory / "first.pdf"
    second = raw_directory / "second.pdf"

    first.write_bytes(b"same content")
    second.write_bytes(b"same content")

    common = {
        "use_case_id": "UC1",
        "title": "Forest Policy",
        "source_organization": "Example Organisation",
        "source_reference": "Example reference",
        "manifest_path": manifest_path,
    }

    register_candidate_document(
        source_file=first,
        **common,
    )

    with pytest.raises(
        ValueError,
        match="already registered",
    ):
        register_candidate_document(
            source_file=second,
            **common,
        )


def test_source_must_be_inside_use_case_raw_directory(
    tmp_path,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()

    manifest_path = _write_manifest(repository)

    source = repository / "outside.pdf"
    source.write_bytes(b"forest policy")

    with pytest.raises(
        ValueError,
        match="use case raw directory",
    ):
        register_candidate_document(
            source_file=source,
            use_case_id="UC1",
            title="Forest Policy",
            source_organization="Example Organisation",
            source_reference="Example reference",
            manifest_path=manifest_path,
        )


def test_unknown_use_case_is_rejected(
    tmp_path,
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()

    manifest_path = _write_manifest(repository)

    source = repository / "policy.pdf"
    source.write_bytes(b"forest policy")

    with pytest.raises(
        ValueError,
        match="Unknown use_case_id",
    ):
        register_candidate_document(
            source_file=source,
            use_case_id="UC2",
            title="Forest Policy",
            source_organization="Example Organisation",
            source_reference="Example reference",
            manifest_path=manifest_path,
        )
