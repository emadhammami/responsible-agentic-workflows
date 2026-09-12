import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.review import (
    accept_candidate_document,
)


def _schema_path() -> Path:
    return Path(
        "corpus/manifest.schema.json"
    ).resolve()


def _repository(
    tmp_path: Path,
) -> tuple[Path, Path]:
    repository = tmp_path / "repository"
    corpus = repository / "corpus"
    raw = (
        corpus
        / "use_cases"
        / "UC1"
        / "raw"
    )

    raw.mkdir(parents=True)

    source = raw / "DOC001_policy.pdf"
    source.write_bytes(b"reviewed forest policy")

    import hashlib

    digest = hashlib.sha256(
        source.read_bytes()
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
                "title": "Forest Policy",
                "source_organization": "Example Organisation",
                "source_reference": "Example reference",
                "source_url": None,
                "discovered_via": "OptFor-EU Policy Map",
                "publication_date": None,
                "language": "en",
                "document_type": "policy",
                "rights_note": None,
                "local_raw_path": (
                    "corpus/use_cases/UC1/raw/"
                    "DOC001_policy.pdf"
                ),
                "local_processed_path": None,
                "sha256": digest,
                "status": "candidate",
                "exclusion_reason": None,
            }
        ],
    }

    manifest_path = corpus / "manifest.json"

    manifest_path.write_text(
        json.dumps(manifest),
        encoding="utf-8",
    )

    (corpus / "manifest.schema.json").write_text(
        _schema_path().read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    return repository, manifest_path


def test_accept_candidate_document(
    tmp_path,
) -> None:
    repository, manifest_path = _repository(
        tmp_path
    )

    review = accept_candidate_document(
        "DOC001",
        rationale="Passed selection and quality review.",
        manifest_path=manifest_path,
    )

    saved = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )

    assert saved["documents"][0]["status"] == "accepted"
    assert review["decision"] == "accepted"

    review_path = (
        repository
        / "corpus"
        / "reviews"
        / "UC1"
        / "DOC001.json"
    )

    assert review_path.is_file()


def test_acceptance_requires_rationale(
    tmp_path,
) -> None:
    _, manifest_path = _repository(
        tmp_path
    )

    with pytest.raises(
        ValueError,
        match="rationale",
    ):
        accept_candidate_document(
            "DOC001",
            rationale="",
            manifest_path=manifest_path,
        )


def test_unknown_document_is_rejected(
    tmp_path,
) -> None:
    _, manifest_path = _repository(
        tmp_path
    )

    with pytest.raises(
        ValueError,
        match="Unknown document_id",
    ):
        accept_candidate_document(
            "DOC999",
            rationale="Reviewed.",
            manifest_path=manifest_path,
        )


def test_already_accepted_document_is_rejected(
    tmp_path,
) -> None:
    _, manifest_path = _repository(
        tmp_path
    )

    accept_candidate_document(
        "DOC001",
        rationale="Reviewed.",
        manifest_path=manifest_path,
    )

    with pytest.raises(
        ValueError,
        match="not a candidate",
    ):
        accept_candidate_document(
            "DOC001",
            rationale="Reviewed again.",
            manifest_path=manifest_path,
        )


def test_hash_mismatch_is_rejected(
    tmp_path,
) -> None:
    repository, manifest_path = _repository(
        tmp_path
    )

    source = (
        repository
        / "corpus"
        / "use_cases"
        / "UC1"
        / "raw"
        / "DOC001_policy.pdf"
    )

    source.write_bytes(
        b"modified after registration"
    )

    with pytest.raises(
        ValueError,
        match="hash mismatch",
    ):
        accept_candidate_document(
            "DOC001",
            rationale="Reviewed.",
            manifest_path=manifest_path,
        )


def test_exclude_candidate_document(
    tmp_path,
) -> None:
    from responsible_agentic_workflows.corpus.review import (
        exclude_candidate_document,
    )

    repository, manifest_path = _repository(
        tmp_path
    )

    review = exclude_candidate_document(
        "DOC001",
        rationale="Outside the selected corpus scope.",
        manifest_path=manifest_path,
    )

    saved = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )

    document = saved["documents"][0]

    assert document["status"] == "excluded"
    assert document["exclusion_reason"] == (
        "Outside the selected corpus scope."
    )
    assert review["decision"] == "excluded"

    review_path = (
        repository
        / "corpus"
        / "reviews"
        / "UC1"
        / "DOC001.json"
    )

    assert review_path.is_file()


def test_exclusion_requires_rationale(
    tmp_path,
) -> None:
    from responsible_agentic_workflows.corpus.review import (
        exclude_candidate_document,
    )

    _, manifest_path = _repository(
        tmp_path
    )

    with pytest.raises(
        ValueError,
        match="Exclusion rationale",
    ):
        exclude_candidate_document(
            "DOC001",
            rationale="",
            manifest_path=manifest_path,
        )
