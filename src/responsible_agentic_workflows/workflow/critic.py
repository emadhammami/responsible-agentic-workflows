"""Provider-neutral structured critic shared by all workflow conditions."""

from __future__ import annotations

import json
from enum import Enum

from responsible_agentic_workflows.modeling import (
    LanguageModel,
    ModelMessage,
    ModelRequest,
)

from .control import (
    CriticResult,
    EvidenceSufficiency,
    GapType,
    SupportStatus,
)

__all__ = [
    "CRITIC_PROMPT_VERSION",
    "CRITIC_SCHEMA_VERSION",
    "CriticParseError",
    "StructuredCritic",
    "parse_critic_result",
]

CRITIC_SCHEMA_VERSION = "0.1"
CRITIC_PROMPT_VERSION = "critic-engineering-v0.1"

_REQUIRED_KEYS = (
    "schema_version",
    "support_status",
    "evidence_sufficiency",
    "unresolved_conflict",
    "gap_types",
    "unsupported_claims",
    "incomplete_support",
    "evidence_gaps",
    "explanation",
)

_SYSTEM_PROMPT = (
    "You are a strict evidence evaluator for document-grounded answers. "
    "Evaluate only the QUESTION, CURRENT ANSWER, and EVIDENCE supplied by "
    "the user. Do not use outside knowledge. "
    "Assess answer grounding and evidence sufficiency as separate dimensions. "
    "support_status must be exactly one of SUPPORTED, PARTIAL_SUPPORT, or "
    "UNSUPPORTED. SUPPORTED means the material claims in the current answer "
    "are supported by the supplied evidence. PARTIAL_SUPPORT means only some "
    "material claims are adequately supported. UNSUPPORTED means the material "
    "answer claims are not supported by the supplied evidence. "
    "evidence_sufficiency must be exactly SUFFICIENT or INSUFFICIENT and "
    "indicates whether the supplied evidence is sufficient to answer the "
    "question, independently of how well the current answer uses that evidence. "
    "unresolved_conflict must be a JSON boolean and should be true only when "
    "the supplied evidence contains a material unresolved conflict relevant "
    "to answering the question. If unresolved_conflict is true, gap_types "
    "must include EVIDENCE_CONFLICT. "
    "gap_types may contain only DRAFT_GROUNDING, MISSING_EVIDENCE, "
    "INCOMPLETE_EVIDENCE, and EVIDENCE_CONFLICT. DRAFT_GROUNDING identifies "
    "answer claims that are not grounded in the supplied evidence. "
    "MISSING_EVIDENCE identifies information needed to answer the question "
    "that is absent from the supplied evidence. INCOMPLETE_EVIDENCE identifies "
    "evidence that addresses a needed point but is insufficiently complete. "
    "EVIDENCE_CONFLICT identifies materially conflicting supplied evidence. "
    "unsupported_claims, incomplete_support, and evidence_gaps must contain "
    "concise diagnostic strings and must be empty arrays when there are no "
    "entries. gap_types must also be an empty array when there are no gaps. "
    "explanation must be null or a concise non-empty string. "
    "Do not output a benchmark correctness score, recovery action, policy "
    "decision, resource judgment, or recommendation. "
    "Return exactly one JSON object and nothing else. Do not use Markdown, "
    "code fences, or prose before or after the JSON. All nine keys are "
    "required: schema_version, support_status, evidence_sufficiency, "
    "unresolved_conflict, gap_types, unsupported_claims, incomplete_support, "
    "evidence_gaps, explanation. schema_version must be exactly \"0.1\". "
    "A valid no-gap shape is: "
    '{\"schema_version\":\"0.1\",'
    '\"support_status\":\"SUPPORTED\",'
    '\"evidence_sufficiency\":\"SUFFICIENT\",'
    '\"unresolved_conflict\":false,'
    '\"gap_types\":[],'
    '\"unsupported_claims\":[],'
    '\"incomplete_support\":[],'
    '\"evidence_gaps\":[],'
    '\"explanation\":null}.'
)


class CriticParseError(ValueError):
    """Raised when structured critic output cannot be parsed strictly."""


def _reject_duplicate_keys(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}

    for key, value in pairs:
        if key in result:
            raise CriticParseError(f"duplicate key in critic JSON: {key!r}")

        result[key] = value

    return result


def _required_string(value: object, key: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CriticParseError(f"{key} must be a non-empty string")

    return value


def _to_enum(enum_cls: type[Enum], value: object, key: str) -> Enum:
    if not isinstance(value, str):
        raise CriticParseError(f"{key} must be a string")

    try:
        return enum_cls(value)
    except ValueError as exc:
        raise CriticParseError(f"unsupported value for {key}: {value!r}") from exc


def _string_list(value: object, key: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise CriticParseError(f"{key} must be a list of strings")

    items: list[str] = []

    for entry in value:
        if not isinstance(entry, str):
            raise CriticParseError(f"{key} entries must be strings")

        items.append(entry)

    return tuple(items)


def _gap_types(value: object) -> tuple[GapType, ...]:
    if not isinstance(value, list):
        raise CriticParseError("gap_types must be a list of strings")

    result: list[GapType] = []

    for entry in value:
        result.append(_to_enum(GapType, entry, "gap_types"))

    return tuple(result)


def parse_critic_result(text: str) -> CriticResult:
    """Parse one strict structured critic document into a CriticResult."""

    if not isinstance(text, str) or not text.strip():
        raise CriticParseError("critic output must be a non-empty string")

    try:
        document = json.loads(text, object_pairs_hook=_reject_duplicate_keys)
    except CriticParseError:
        raise
    except json.JSONDecodeError as exc:
        raise CriticParseError(f"critic output is not valid JSON: {exc.msg}") from exc

    if not isinstance(document, dict):
        raise CriticParseError("critic output must be a single JSON object")

    missing = (key for key in _REQUIRED_KEYS if key not in document)

    for key in missing:
        raise CriticParseError(f"critic JSON is missing required key: {key!r}")

    known = set(_REQUIRED_KEYS)
    unknown = (key for key in document if key not in known)

    for key in unknown:
        raise CriticParseError(f"critic JSON has unknown key: {key!r}")

    schema_version = _required_string(
        document["schema_version"],
        "schema_version",
    )

    if schema_version != CRITIC_SCHEMA_VERSION:
        raise CriticParseError(
            "schema_version must equal "
            f"{CRITIC_SCHEMA_VERSION!r}"
        )

    unresolved_conflict = document["unresolved_conflict"]

    if not isinstance(unresolved_conflict, bool):
        raise CriticParseError("unresolved_conflict must be a boolean")

    explanation = document["explanation"]

    if explanation is not None and not isinstance(explanation, str):
        raise CriticParseError("explanation must be a string or null")

    return CriticResult(
            schema_version=schema_version,
            support_status=_to_enum(
                SupportStatus, document["support_status"], "support_status"
            ),
            evidence_sufficiency=_to_enum(
                EvidenceSufficiency,
                document["evidence_sufficiency"],
                "evidence_sufficiency",
            ),
            unresolved_conflict=unresolved_conflict,
            gap_types=_gap_types(document["gap_types"]),
            unsupported_claims=_string_list(
                document["unsupported_claims"], "unsupported_claims"
            ),
            incomplete_support=_string_list(
                document["incomplete_support"], "incomplete_support"
            ),
            evidence_gaps=_string_list(
                document["evidence_gaps"], "evidence_gaps"
            ),
            explanation=explanation,
        )


def _non_empty_field(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")

    return value


def _build_user_message(
    *,
    question: str,
    answer: str,
    evidence_context: str,
) -> str:
    return (
        "QUESTION\n"
        f"{question}\n\n"
        "CURRENT ANSWER\n"
        f"{answer}\n\n"
        "EVIDENCE\n"
        f"{evidence_context}\n\n"
        "Return exactly one JSON object matching the schema. "
        "Do not add any other text."
    )


class StructuredCritic:
    """Model-driven structured critic with strict JSON output parsing."""

    CRITIC_SCHEMA_VERSION = CRITIC_SCHEMA_VERSION
    CRITIC_PROMPT_VERSION = CRITIC_PROMPT_VERSION

    def __init__(self, *, model: LanguageModel) -> None:
        if not isinstance(model, LanguageModel):
            raise TypeError("model must satisfy the LanguageModel contract")

        self._model = model

    @property
    def model(self) -> LanguageModel:
        """Return the wrapped language model."""

        return self._model

    def assess(
        self,
        *,
        question: str,
        answer: str,
        evidence_context: str,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
    ) -> CriticResult:
        """Run exactly one model call and parse one strict critic document."""

        assessed_question = _non_empty_field(question, "question")
        assessed_answer = _non_empty_field(answer, "answer")
        assessed_evidence = _non_empty_field(
            evidence_context, "evidence_context"
        )

        request = ModelRequest(
            messages=(
                ModelMessage(
                    role="system",
                    content=_SYSTEM_PROMPT,
                ),
                ModelMessage(
                    role="user",
                    content=_build_user_message(
                        question=assessed_question,
                        answer=assessed_answer,
                        evidence_context=assessed_evidence,
                    ),
                ),
            ),
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

        response = self._model.generate(request)

        return parse_critic_result(response.text)
