import hashlib

import pytest

from responsible_agentic_workflows.corpus import (
    load_corpus_manifest,
    sha256_file,
    validate_corpus_manifest,
)


def _manifest() -> dict[str, object]:
    return {
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


def _document(
    *,
    document_id: str = "DOC001",
    use_case_id: str = "UC1",
    digest: str = "a" * 64,
) -> dict[str, object]:
    return {
        "document_id": document_id,
        "use_case_id": use_case_id,
        "title": "Example forest policy",
        "source_organization": "Example source",
        "source_reference": "Example reference",
        "source_url": None,
        "discovered_via": "OptFor-EU Policy Map",
        "publication_date": None,
        "language": "en",
        "document_type": "policy",
        "rights_note": None,
        "local_raw_path": (
            f"corpus/use_cases/{use_case_id}/raw/"
            f"{document_id}.pdf"
        ),
        "local_processed_path": None,
        "sha256": digest,
        "status": "candidate",
        "exclusion_reason": None,
    }


def test_current_manifest_contains_uc1() -> None:
    manifest = load_corpus_manifest()

    assert manifest["status"] == "working"

    use_case_ids = {
        use_case["use_case_id"]
        for use_case in manifest["use_cases"]
    }

    assert "UC1" in use_case_ids

    uc1 = next(
        use_case
        for use_case in manifest["use_cases"]
        if use_case["use_case_id"] == "UC1"
    )

    assert uc1["name"] == "OptFor-EU Forest Policy"

    for document in manifest["documents"]:
        assert document["use_case_id"] in use_case_ids


def test_one_use_case_is_valid() -> None:
    validate_corpus_manifest(_manifest())


def test_document_must_reference_known_use_case() -> None:
    manifest = _manifest()

    manifest["documents"] = [
        _document(use_case_id="UC2")
    ]

    with pytest.raises(
        ValueError,
        match="Unknown use_case_id",
    ):
        validate_corpus_manifest(manifest)


def test_document_raw_path_must_match_use_case() -> None:
    manifest = _manifest()

    document = _document()
    document["local_raw_path"] = (
        "corpus/use_cases/UC2/raw/DOC001.pdf"
    )

    manifest["documents"] = [document]

    with pytest.raises(
        ValueError,
        match="raw path does not match",
    ):
        validate_corpus_manifest(manifest)


def test_duplicate_document_ids_are_rejected() -> None:
    manifest = _manifest()

    manifest["documents"] = [
        _document(
            document_id="DOC001",
            digest="a" * 64,
        ),
        _document(
            document_id="DOC001",
            digest="b" * 64,
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Duplicate document_id",
    ):
        validate_corpus_manifest(manifest)


def test_duplicate_document_content_is_rejected() -> None:
    manifest = _manifest()

    manifest["documents"] = [
        _document(
            document_id="DOC001",
            digest="a" * 64,
        ),
        _document(
            document_id="DOC002",
            digest="a" * 64,
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Duplicate document content",
    ):
        validate_corpus_manifest(manifest)


def test_sha256_file_matches_file_content(
    tmp_path,
) -> None:
    source = tmp_path / "policy.pdf"
    content = b"synthetic policy source"

    source.write_bytes(content)

    expected = hashlib.sha256(content).hexdigest()

    assert sha256_file(source) == expected
