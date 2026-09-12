"""Embedding client contracts and local Ollama implementation."""

import json
import urllib.request
from collections.abc import Sequence
from typing import Protocol

import numpy as np
from numpy.typing import NDArray

FloatVector = NDArray[np.float32]
FloatMatrix = NDArray[np.float32]


class EmbeddingClient(Protocol):
    """Embedding interface used by dense retrieval infrastructure."""

    @property
    def dimensions(self) -> int:
        """Return the configured embedding dimensionality."""
        ...

    def embed_query(self, query: str) -> FloatVector:
        """Embed one retrieval query."""
        ...

    def embed_documents(
        self,
        texts: Sequence[str],
    ) -> FloatMatrix:
        """Embed an ordered batch of document texts."""
        ...


class OllamaEmbeddingClient:
    """Local embedding client for Ollama's embedding API."""

    def __init__(
        self,
        *,
        model: str,
        dimensions: int,
        query_instruction: str | None,
        truncate: bool,
        base_url: str = "http://localhost:11434",
        timeout_seconds: float = 300.0,
    ) -> None:
        if not model.strip():
            raise ValueError("Model must not be empty")

        if dimensions < 1:
            raise ValueError("Dimensions must be at least 1")

        if not base_url.strip():
            raise ValueError("Base URL must not be empty")

        if timeout_seconds <= 0:
            raise ValueError(
                "Timeout must be greater than zero"
            )

        if (
            query_instruction is not None
            and not query_instruction.strip()
        ):
            raise ValueError(
                "Query instruction must be null or non-empty"
            )

        self._model = model
        self._dimensions = dimensions
        self._query_instruction = query_instruction
        self._truncate = truncate
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds

    @property
    def dimensions(self) -> int:
        return self._dimensions

    def embed_query(
        self,
        query: str,
    ) -> FloatVector:
        if not query.strip():
            raise ValueError("Query must not be empty")

        text = query

        if self._query_instruction is not None:
            text = (
                f"Instruct: {self._query_instruction}\n"
                f"Query: {query}"
            )

        matrix = self._embed((text,))

        return matrix[0].copy()

    def embed_documents(
        self,
        texts: Sequence[str],
    ) -> FloatMatrix:
        ordered_texts = tuple(texts)

        if not ordered_texts:
            raise ValueError(
                "At least one document text is required"
            )

        if any(
            not isinstance(text, str)
            or not text.strip()
            for text in ordered_texts
        ):
            raise ValueError(
                "Document texts must be non-empty strings"
            )

        return self._embed(ordered_texts)

    def _embed(
        self,
        texts: Sequence[str],
    ) -> FloatMatrix:
        payload = {
            "model": self._model,
            "input": list(texts),
            "truncate": self._truncate,
        }

        request = urllib.request.Request(
            f"{self._base_url}/api/embed",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

        with urllib.request.urlopen(
            request,
            timeout=self._timeout_seconds,
        ) as response:
            result = json.load(response)

        embeddings = result.get("embeddings")

        if not isinstance(embeddings, list):
            raise ValueError(
                "Ollama response does not contain embeddings"
            )

        try:
            matrix = np.asarray(
                embeddings,
                dtype=np.float32,
            )
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "Ollama returned invalid embedding values"
            ) from exc

        if matrix.ndim != 2:
            raise ValueError(
                "Ollama embeddings must be a two-dimensional matrix"
            )

        if matrix.shape[0] != len(texts):
            raise ValueError(
                "Ollama returned an unexpected embedding count"
            )

        if matrix.shape[1] != self._dimensions:
            raise ValueError(
                "Ollama embedding dimensionality does not match "
                "the configured dimensions"
            )

        if not np.isfinite(matrix).all():
            raise ValueError(
                "Ollama embeddings contain non-finite values"
            )

        return matrix
