"""Framework-neutral retrieval utilities."""

from .configuration import (
    load_retrieval_configuration,
    require_frozen_retrieval_configuration,
    validate_retrieval_configuration,
)
from .dense import DenseExactRetriever
from .embedding import (
    EmbeddingClient,
    OllamaEmbeddingClient,
)
from .lexical import LexicalRetriever
from .models import RetrievedChunk, Retriever

__all__ = [
    "DenseExactRetriever",
    "EmbeddingClient",
    "LexicalRetriever",
    "OllamaEmbeddingClient",
    "RetrievedChunk",
    "Retriever",
    "load_retrieval_configuration",
    "require_frozen_retrieval_configuration",
    "validate_retrieval_configuration",
]
