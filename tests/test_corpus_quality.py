import hashlib
import json
import subprocess
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.quality import (
    inspect_document_quality,
    inspect_use_case_quality,
)


def _schema_path() -> Path:
    return Path(
        "corpus/manifest.schema.json"
    ).resolve()


def _repository(
    tmp_path: Path,
) -> tuple[Path, Path, Path]:
    repository = tmp_path / "repository"

    raw = (
        repository
        / "corpus"
        / "use_cases"
        / "UC1"
        / "raw"
    )

    raw.mkdir(parents=True)

    source = raw / "DOC001_policy.pdf"
    source.write_bytes(
        b"%PDF-1.5\nsynthetic"
    )

    digest = hashlib.sha256(
        source.read_bytes()
    ).hexdigest()

    corpus = repository / "corpus"

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
        _schema_path().read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )

    return repository, manifest_path, source


def _mock_pdf_tools(
    monkeypatch,
    *,
    text: str,
    pages: int = 10,
    encrypted: bool = False,
) -> None:
    monkeypatch.setattr(
        "responsible_agentic_workflows.corpus.quality.shutil.which",
        lambda name: f"/usr/bin/{name}",
    )

    def fake_run(
        command,
        *,
        check,
        capture_output,
        text: bool,
    ):
        assert check
        assert capture_output
        assert text

        if "pdfinfo" in command[0]:
            encryption = (
                "yes"
                if encrypted
                else "no"
            )

            return subprocess.CompletedProcess(
                command,
                0,
                stdout=(
                    f"Pages:           {pages}\n"
                    f"Encrypted:       {encryption}\n"
                ),
                stderr="",
            )

        return subprocess.CompletedProcess(
            command,
            0,
            stdout=_mock_pdf_tools.extracted_text,
            stderr="",
        )

    _mock_pdf_tools.extracted_text = text

    monkeypatch.setattr(
        "responsible_agentic_workflows.corpus.quality.subprocess.run",
        fake_run,
    )


def test_quality_report_passes_for_usable_pdf(
    tmp_path,
    monkeypatch,
) -> None:
    _, manifest_path, _ = _repository(
        tmp_path
    )

    extracted = (
        "forest policy content\n" * 100
    )

    _mock_pdf_tools(
        monkeypatch,
        text=extracted,
    )

    reports = tmp_path / "reports"

    report = inspect_document_quality(
        "DOC001",
        manifest_path=manifest_path,
        reports_directory=reports,
    )

    assert report["quality_status"] == "pass"
    assert report["metrics"]["pages"] == 10
    assert report["issues"] == []
    assert (
        reports / "DOC001.json"
    ).is_file()


def test_quality_report_flags_insufficient_text(
    tmp_path,
    monkeypatch,
) -> None:
    _, manifest_path, _ = _repository(
        tmp_path
    )

    _mock_pdf_tools(
        monkeypatch,
        text="short text",
    )

    report = inspect_document_quality(
        "DOC001",
        manifest_path=manifest_path,
        reports_directory=tmp_path / "reports",
    )

    assert report["quality_status"] == "review"
    assert (
        "insufficient_extracted_text"
        in report["issues"]
    )


def test_quality_report_flags_encrypted_pdf(
    tmp_path,
    monkeypatch,
) -> None:
    _, manifest_path, _ = _repository(
        tmp_path
    )

    _mock_pdf_tools(
        monkeypatch,
        text="forest policy content\n" * 100,
        encrypted=True,
    )

    report = inspect_document_quality(
        "DOC001",
        manifest_path=manifest_path,
        reports_directory=tmp_path / "reports",
    )

    assert report["quality_status"] == "review"
    assert "encrypted_pdf" in report["issues"]


def test_hash_mismatch_is_rejected(
    tmp_path,
    monkeypatch,
) -> None:
    _, manifest_path, source = _repository(
        tmp_path
    )

    source.write_bytes(
        b"%PDF-1.5\nmodified"
    )

    _mock_pdf_tools(
        monkeypatch,
        text="forest policy content\n" * 100,
    )

    with pytest.raises(
        ValueError,
        match="hash mismatch",
    ):
        inspect_document_quality(
            "DOC001",
            manifest_path=manifest_path,
            reports_directory=tmp_path / "reports",
        )


def test_use_case_quality_can_filter_by_status(
    tmp_path,
    monkeypatch,
) -> None:
    _, manifest_path, _ = _repository(
        tmp_path
    )

    _mock_pdf_tools(
        monkeypatch,
        text="forest policy content\n" * 100,
    )

    reports = inspect_use_case_quality(
        "UC1",
        status="accepted",
        manifest_path=manifest_path,
    )

    assert reports == []
