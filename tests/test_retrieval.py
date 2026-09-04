from pathlib import Path

import pytest

from responsible_agentic_workflows.ingestion import ingest_markdown_directory
from responsible_agentic_workflows.retrieval import LexicalRetriever

SYNTHETIC_DOCUMENTS = Path("benchmark/synthetic/documents")


def _retriever() -> LexicalRetriever:
    documents = ingest_markdown_directory(SYNTHETIC_DOCUMENTS)

    chunks = (
        chunk
        for document in documents
        for chunk in document.chunks
    )

    return LexicalRetriever(chunks)


def test_retriever_preserves_provenance() -> None:
    retriever = _retriever()

    results = retriever.retrieve(
        "How long must expense receipts be retained?",
        top_k=3,
    )

    first = results[0]

    assert first.rank == 1
    assert first.chunk.document_id == "DOC902"
    assert first.chunk.section == "Expense records"
    assert first.chunk.chunk_id == "DOC902-S001"
    assert first.score > 0


def test_retrieval_is_deterministic() -> None:
    retriever = _retriever()

    first = retriever.retrieve(
        "external collaborator access review",
        top_k=5,
    )

    second = retriever.retrieve(
        "external collaborator access review",
        top_k=5,
    )

    assert first == second


def test_high_risk_query_returns_addendum_evidence() -> None:
    retriever = _retriever()

    results = retriever.retrieve(
        "approval for international high risk travel",
        top_k=3,
    )

    assert results[0].chunk.document_id == "DOC905"
    assert results[0].chunk.section == "High-risk destinations"


def test_runtime_retrieval_does_not_require_gold_fields() -> None:
    retriever = _retriever()

    question = "Who must approve ordinary international business travel?"

    results = retriever.retrieve(
        question,
        top_k=2,
    )

    assert results
    assert results[0].chunk.document_id == "DOC901"

    for result in results:
        assert not hasattr(result, "reference_answer")
        assert not hasattr(result, "required_documents")
        assert not hasattr(result, "task_type")


def test_invalid_retrieval_arguments_are_rejected() -> None:
    retriever = _retriever()

    with pytest.raises(ValueError, match="Query must not be empty"):
        retriever.retrieve("", top_k=3)

    with pytest.raises(ValueError, match="top_k must be at least 1"):
        retriever.retrieve("expense receipts", top_k=0)
