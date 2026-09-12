import hashlib
import json
from pathlib import Path

import pytest

from responsible_agentic_workflows.corpus.download import (
    download_batch,
    load_download_queue,
)


def _manifest_schema() -> Path:
    return Path(
        "corpus/manifest.schema.json"
    ).resolve()


def _download_schema() -> Path:
    return Path(
        "corpus/download_queue.schema.json"
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
        _manifest_schema().read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )

    (
        corpus / "download_queue.schema.json"
    ).write_text(
        _download_schema().read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )

    return repository, manifest_path, raw


def _queue(
    repository: Path,
    documents: list[dict[str, str]],
) -> Path:
    path = (
        repository
        / "corpus"
        / "download_queue.json"
    )

    path.write_text(
        json.dumps(
            {
                "schema_version": "0.1",
                "use_case_id": "UC1",
                "documents": documents,
            }
        ),
        encoding="utf-8",
    )

    return path


class _Response:
    def __init__(
        self,
        data: bytes,
        url: str,
    ) -> None:
        self.data = data
        self.url = url

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        return False

    def read(self) -> bytes:
        return self.data

    def geturl(self) -> str:
        return self.url


def _pdf(label: bytes) -> bytes:
    return (
        b"%PDF-1.5\n"
        + label
        + b"\n"
        + b"x" * 2000
    )


def test_empty_queue_is_valid(
    tmp_path,
) -> None:
    repository, _, _ = _repository(
        tmp_path
    )

    path = _queue(
        repository,
        [],
    )

    queue = load_download_queue(
        path,
        schema_path=(
            repository
            / "corpus"
            / "download_queue.schema.json"
        ),
    )

    assert queue["documents"] == []


def test_batch_downloads_multiple_pdfs(
    tmp_path,
    monkeypatch,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    first = _pdf(b"first")
    second = _pdf(b"second")

    responses = {
        "https://example.org/first.pdf": first,
        "https://example.org/second.pdf": second,
    }

    def fake_urlopen(
        request,
        timeout,
    ):
        assert timeout == 60

        url = request.full_url

        return _Response(
            responses[url],
            url,
        )

    monkeypatch.setattr(
        "responsible_agentic_workflows.corpus.download.urlopen",
        fake_urlopen,
    )

    path = _queue(
        repository,
        [
            {
                "title": "First",
                "pdf_url": "https://example.org/first.pdf",
                "target_filename": "first.pdf",
            },
            {
                "title": "Second",
                "pdf_url": "https://example.org/second.pdf",
                "target_filename": "second.pdf",
            },
        ],
    )

    result = download_batch(
        path,
        manifest_path=manifest_path,
        schema_path=(
            repository
            / "corpus"
            / "download_queue.schema.json"
        ),
    )

    assert len(result) == 2
    assert (
        raw / "first.pdf"
    ).read_bytes() == first
    assert (
        raw / "second.pdf"
    ).read_bytes() == second

    assert result[0]["sha256"] == hashlib.sha256(
        first
    ).hexdigest()


def test_non_pdf_aborts_batch(
    tmp_path,
    monkeypatch,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    responses = {
        "https://example.org/first.pdf": _pdf(b"first"),
        "https://example.org/not-pdf": b"<html>" + b"x" * 2000,
    }

    def fake_urlopen(
        request,
        timeout,
    ):
        return _Response(
            responses[request.full_url],
            request.full_url,
        )

    monkeypatch.setattr(
        "responsible_agentic_workflows.corpus.download.urlopen",
        fake_urlopen,
    )

    path = _queue(
        repository,
        [
            {
                "title": "First",
                "pdf_url": "https://example.org/first.pdf",
                "target_filename": "first.pdf",
            },
            {
                "title": "Invalid",
                "pdf_url": "https://example.org/not-pdf",
                "target_filename": "invalid.pdf",
            },
        ],
    )

    with pytest.raises(
        ValueError,
        match="not a PDF",
    ):
        download_batch(
            path,
            manifest_path=manifest_path,
            schema_path=(
                repository
                / "corpus"
                / "download_queue.schema.json"
            ),
        )

    assert not (
        raw / "first.pdf"
    ).exists()

    assert not (
        raw / "invalid.pdf"
    ).exists()


def test_existing_target_is_rejected(
    tmp_path,
) -> None:
    repository, manifest_path, raw = _repository(
        tmp_path
    )

    (
        raw / "existing.pdf"
    ).write_bytes(
        _pdf(b"existing")
    )

    path = _queue(
        repository,
        [
            {
                "title": "Existing",
                "pdf_url": "https://example.org/existing.pdf",
                "target_filename": "existing.pdf",
            }
        ],
    )

    with pytest.raises(
        FileExistsError,
        match="Target already exists",
    ):
        download_batch(
            path,
            manifest_path=manifest_path,
            schema_path=(
                repository
                / "corpus"
                / "download_queue.schema.json"
            ),
        )


def test_duplicate_target_is_rejected(
    tmp_path,
) -> None:
    repository, _, _ = _repository(
        tmp_path
    )

    path = _queue(
        repository,
        [
            {
                "title": "First",
                "pdf_url": "https://example.org/first.pdf",
                "target_filename": "same.pdf",
            },
            {
                "title": "Second",
                "pdf_url": "https://example.org/second.pdf",
                "target_filename": "same.pdf",
            },
        ],
    )

    with pytest.raises(
        ValueError,
        match="Duplicate target_filename",
    ):
        load_download_queue(
            path,
            schema_path=(
                repository
                / "corpus"
                / "download_queue.schema.json"
            ),
        )
