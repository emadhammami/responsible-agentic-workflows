import json
import urllib.request

import numpy as np
import pytest

from responsible_agentic_workflows.retrieval import (
    OllamaEmbeddingClient,
)


class _FakeResponse:
    def __init__(
        self,
        payload: dict[str, object],
    ) -> None:
        self._payload = payload

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(
            self._payload
        ).encode("utf-8")


def _client(
    *,
    dimensions: int = 3,
) -> OllamaEmbeddingClient:
    return OllamaEmbeddingClient(
        model="test-embedding-model",
        dimensions=dimensions,
        query_instruction=(
            "Retrieve relevant policy passages"
        ),
        truncate=False,
    )


def test_query_instruction_and_request_payload(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    def fake_urlopen(
        request: urllib.request.Request,
        *,
        timeout: float,
    ) -> _FakeResponse:
        captured["url"] = request.full_url
        captured["timeout"] = timeout
        captured["payload"] = json.loads(
            request.data.decode("utf-8")
        )

        return _FakeResponse(
            {
                "embeddings": [
                    [0.6, 0.8, 0.0],
                ]
            }
        )

    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        fake_urlopen,
    )

    vector = _client().embed_query(
        "How is biodiversity protected?"
    )

    assert captured["url"] == (
        "http://localhost:11434/api/embed"
    )
    assert captured["timeout"] == 300.0
    assert captured["payload"] == {
        "model": "test-embedding-model",
        "input": [
            "Instruct: Retrieve relevant policy passages\n"
            "Query: How is biodiversity protected?"
        ],
        "truncate": False,
    }

    assert vector.dtype == np.float32
    assert vector.shape == (3,)


def test_document_texts_are_not_given_query_instruction(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    def fake_urlopen(
        request: urllib.request.Request,
        *,
        timeout: float,
    ) -> _FakeResponse:
        del timeout

        captured["payload"] = json.loads(
            request.data.decode("utf-8")
        )

        return _FakeResponse(
            {
                "embeddings": [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ]
            }
        )

    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        fake_urlopen,
    )

    matrix = _client().embed_documents(
        (
            "First policy passage.",
            "Second policy passage.",
        )
    )

    assert captured["payload"] == {
        "model": "test-embedding-model",
        "input": [
            "First policy passage.",
            "Second policy passage.",
        ],
        "truncate": False,
    }

    assert matrix.shape == (2, 3)
    assert matrix.dtype == np.float32


def test_invalid_response_dimensions_are_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_urlopen(
        request: urllib.request.Request,
        *,
        timeout: float,
    ) -> _FakeResponse:
        del request
        del timeout

        return _FakeResponse(
            {
                "embeddings": [
                    [1.0, 0.0],
                ]
            }
        )

    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        fake_urlopen,
    )

    with pytest.raises(
        ValueError,
        match="dimensionality",
    ):
        _client().embed_query(
            "Policy question"
        )


def test_empty_embedding_inputs_are_rejected() -> None:
    client = _client()

    with pytest.raises(
        ValueError,
        match="Query must not be empty",
    ):
        client.embed_query("")

    with pytest.raises(
        ValueError,
        match="At least one document",
    ):
        client.embed_documents(())

    with pytest.raises(
        ValueError,
        match="non-empty strings",
    ):
        client.embed_documents(
            ("valid text", " ")
        )
