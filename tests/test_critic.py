import json
import pathlib
import types

import pytest

from responsible_agentic_workflows.modeling import (
    LanguageModel,
    ModelRequest,
    ModelResponse,
    TokenUsage,
)
from responsible_agentic_workflows.workflow import (
    CRITIC_PROMPT_VERSION,
    CRITIC_SCHEMA_VERSION,
    CriticControlState,
    CriticParseError,
    CriticResult,
    EvidenceSufficiency,
    GapType,
    StructuredCritic,
    SupportStatus,
    parse_critic_result,
    release_ok,
)

QUESTION = "What is the capital of France?"
ANSWER = "The capital of France is Paris."
EVIDENCE = "Paris is the capital and largest city of France."

MINIMAL_DOC = {
    "schema_version": CRITIC_SCHEMA_VERSION,
    "support_status": "SUPPORTED",
    "evidence_sufficiency": "SUFFICIENT",
    "unresolved_conflict": False,
    "gap_types": [],
    "unsupported_claims": [],
    "incomplete_support": [],
    "evidence_gaps": [],
    "explanation": None,
}

FULL_DOC = {
    **MINIMAL_DOC,
    "gap_types": ["MISSING_EVIDENCE", "DRAFT_GROUNDING"],
    "unsupported_claims": ["claim one", "claim two"],
    "incomplete_support": ["partial claim"],
    "evidence_gaps": ["missing dates"],
    "explanation": "The answer is supported for one sentence only.",
}


def _doc(**overrides: object) -> str:
    payload = {**MINIMAL_DOC, **overrides}
    return json.dumps(payload)


class FakeModel:
    def __init__(self, response_text: str = _doc()) -> None:
        self._response_text = response_text
        self.requests: list[ModelRequest] = []
        self.call_count = 0

    @property
    def config_id(self) -> str:
        return "fake-config"

    @property
    def provider(self) -> str:
        return "fake"

    @property
    def model_name(self) -> str:
        return "fake-model"

    def generate(self, request: ModelRequest) -> ModelResponse:
        self.requests.append(request)
        self.call_count += 1
        return ModelResponse(
            text=self._response_text,
            usage=TokenUsage(input_tokens=10, output_tokens=5),
        )


def _critic(response_text: str = _doc()) -> tuple[StructuredCritic, FakeModel]:
    model = FakeModel(response_text)
    return StructuredCritic(model=model), model


def _assess(critic: StructuredCritic, **overrides: object):
    kwargs = {
        "question": QUESTION,
        "answer": ANSWER,
        "evidence_context": EVIDENCE,
    }
    kwargs.update(overrides)
    return critic.assess(**kwargs)


def _user_message(request: ModelRequest) -> str:
    return request.messages[1].content


# A. Strict parser accepts valid documents


def test_minimal_valid_document_parses() -> None:
    result = parse_critic_result(_doc())

    assert result.schema_version == CRITIC_SCHEMA_VERSION
    assert result.support_status is SupportStatus.SUPPORTED
    assert result.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT
    assert result.unresolved_conflict is False
    assert result.gap_types == ()
    assert result.unsupported_claims == ()
    assert result.incomplete_support == ()
    assert result.evidence_gaps == ()
    assert result.explanation is None


def test_full_document_round_trips_every_field() -> None:
    result = parse_critic_result(json.dumps(FULL_DOC))

    assert result.gap_types == (
        GapType.MISSING_EVIDENCE,
        GapType.DRAFT_GROUNDING,
    )
    assert result.unsupported_claims == ("claim one", "claim two")
    assert result.incomplete_support == ("partial claim",)
    assert result.evidence_gaps == ("missing dates",)
    assert result.explanation == FULL_DOC["explanation"]


def test_null_explanation_becomes_none() -> None:
    result = parse_critic_result(_doc(explanation=None))
    assert result.explanation is None


def test_gap_types_preserve_order_and_enum_membership() -> None:
    result = parse_critic_result(
        _doc(gap_types=["INCOMPLETE_EVIDENCE", "DRAFT_GROUNDING"])
    )
    assert result.gap_types == (
        GapType.INCOMPLETE_EVIDENCE,
        GapType.DRAFT_GROUNDING,
    )
    assert all(isinstance(value, GapType) for value in result.gap_types)


# B. Strict parser rejects malformed documents


def test_parse_non_string_input_raises() -> None:
    for invalid in (None, 42, b"{}", ["SUPPORTED"]):
        with pytest.raises(CriticParseError):
            parse_critic_result(invalid)  # type: ignore[arg-type]


def test_parse_empty_or_blank_input_raises() -> None:
    for invalid in ("", "   ", "\n\t"):
        with pytest.raises(CriticParseError):
            parse_critic_result(invalid)


def test_reject_prose_before_json() -> None:
    with pytest.raises(CriticParseError):
        parse_critic_result(f"Here is the assessment: {_doc()}")


def test_reject_markdown_fenced_json() -> None:
    with pytest.raises(CriticParseError):
        parse_critic_result(f"```json\n{_doc()}\n```")


def test_reject_trailing_text_after_object() -> None:
    with pytest.raises(CriticParseError):
        parse_critic_result(f"{_doc()} Hope that helps!")


def test_reject_json_array_containing_valid_object() -> None:
    with pytest.raises(CriticParseError):
        parse_critic_result(json.dumps([MINIMAL_DOC, MINIMAL_DOC]))


def test_reject_json_scalar_documents() -> None:
    for invalid in ('"SUPPORTED"', "42", "true"):
        with pytest.raises(CriticParseError):
            parse_critic_result(invalid)


def test_reject_json_null_document() -> None:
    with pytest.raises(CriticParseError, match="single JSON object"):
        parse_critic_result("null")


def test_reject_duplicate_key() -> None:
    with pytest.raises(CriticParseError, match="duplicate"):
        parse_critic_result(
            '{"schema_version": "0.1", "schema_version": "0.2", '
            '"support_status": "SUPPORTED", '
            '"evidence_sufficiency": "SUFFICIENT", '
            '"unresolved_conflict": false}'
        )


@pytest.mark.parametrize(
    "missing_key",
    [
        "schema_version",
        "support_status",
        "evidence_sufficiency",
        "unresolved_conflict",
        "gap_types",
        "unsupported_claims",
        "incomplete_support",
        "evidence_gaps",
        "explanation",
    ],
)
def test_reject_missing_required_key(missing_key: str) -> None:
    payload = {**MINIMAL_DOC}
    del payload[missing_key]
    with pytest.raises(CriticParseError, match=missing_key):
        parse_critic_result(json.dumps(payload))


def test_reject_unknown_key() -> None:
    with pytest.raises(CriticParseError, match="unknown key"):
        parse_critic_result(_doc(notes="extra information"))


def test_reject_invalid_schema_version() -> None:
    for invalid in (42, "", "0.2"):
        with pytest.raises(CriticParseError, match="schema_version"):
            parse_critic_result(_doc(schema_version=invalid))


def test_reject_invalid_support_status() -> None:
    with pytest.raises(CriticParseError, match="must be a string"):
        parse_critic_result(_doc(support_status=42))
    with pytest.raises(CriticParseError, match="unsupported value"):
        parse_critic_result(_doc(support_status="MAYBE_SUPPORTED"))


def test_reject_invalid_evidence_sufficiency() -> None:
    with pytest.raises(CriticParseError, match="evidence_sufficiency"):
        parse_critic_result(_doc(evidence_sufficiency="PARTLY"))


def test_reject_non_boolean_unresolved_conflict() -> None:
    with pytest.raises(CriticParseError, match="boolean"):
        parse_critic_result(_doc(unresolved_conflict="false"))


def test_reject_gap_types_wrong_type_and_bad_entry() -> None:
    with pytest.raises(CriticParseError, match="gap_types"):
        parse_critic_result(_doc(gap_types="DRAFT_GROUNDING"))
    with pytest.raises(CriticParseError, match="gap_types"):
        parse_critic_result(_doc(gap_types=[42]))
    with pytest.raises(CriticParseError, match="unsupported value"):
        parse_critic_result(_doc(gap_types=["NO_SUCH_GAP"]))


def test_reject_gap_types_duplicates() -> None:
    with pytest.raises(ValueError) as exc_info:
        parse_critic_result(
            _doc(gap_types=["DRAFT_GROUNDING", "DRAFT_GROUNDING"])
        )

    assert not isinstance(exc_info.value, CriticParseError)


def test_reject_string_list_violations() -> None:
    with pytest.raises(CriticParseError, match="unsupported_claims"):
        parse_critic_result(_doc(unsupported_claims="claim one"))
    with pytest.raises(ValueError) as exc_info:
        parse_critic_result(_doc(unsupported_claims=["claim one", ""]))

    assert not isinstance(exc_info.value, CriticParseError)
    with pytest.raises(CriticParseError):
        parse_critic_result(_doc(unsupported_claims=[42]))


def test_reject_blank_explanation_when_present() -> None:
    for invalid in ("", "   "):
        with pytest.raises(ValueError) as exc_info:
            parse_critic_result(_doc(explanation=invalid))

        assert not isinstance(exc_info.value, CriticParseError)


# C. Constructor and class contract


def test_constructor_rejects_non_language_model() -> None:
    for invalid in (None, "fake", 42, types.ModuleType("nope")):
        with pytest.raises(TypeError):
            StructuredCritic(model=invalid)  # type: ignore[arg-type]


def test_constructor_accepts_language_model_and_exposes_it() -> None:
    model = FakeModel()
    assert isinstance(model, LanguageModel)
    critic = StructuredCritic(model=model)
    assert critic.model is model


def test_constructor_requires_keyword_only_model() -> None:
    with pytest.raises(TypeError):
        StructuredCritic(FakeModel())  # type: ignore[call-arg]


def test_version_constants_are_consistent() -> None:
    assert CRITIC_SCHEMA_VERSION == "0.1"
    assert CRITIC_PROMPT_VERSION == "critic-engineering-v0.1"
    assert StructuredCritic.CRITIC_SCHEMA_VERSION == CRITIC_SCHEMA_VERSION
    assert StructuredCritic.CRITIC_PROMPT_VERSION == CRITIC_PROMPT_VERSION


# D. assess() behavior


def test_assess_sends_exactly_two_messages_in_order() -> None:
    critic, model = _critic()
    _assess(critic)
    request = model.requests[0]
    assert [message.role for message in request.messages] == ["system", "user"]


def test_user_message_has_sections_and_exact_texts() -> None:
    critic, model = _critic()
    _assess(critic)
    content = _user_message(model.requests[0])
    assert f"QUESTION\n{QUESTION}\n\nCURRENT ANSWER\n{ANSWER}\n\nEVIDENCE\n{EVIDENCE}\n" in content  # noqa: E501


def test_assess_returns_parsed_result() -> None:
    critic, _ = _critic()
    result = _assess(critic)
    assert result == parse_critic_result(_doc())
    assert isinstance(result, CriticResult)


def test_assess_preserves_collections_from_response() -> None:
    critic, _ = _critic(json.dumps(FULL_DOC))
    result = _assess(critic)
    assert result.gap_types == (GapType.MISSING_EVIDENCE, GapType.DRAFT_GROUNDING)
    assert result.unsupported_claims == ("claim one", "claim two")
    assert result.explanation == FULL_DOC["explanation"]


def test_invalid_output_raises_parse_error_without_retry() -> None:
    critic, model = _critic("not json at all")
    with pytest.raises(CriticParseError):
        _assess(critic)
    assert model.call_count == 1


def test_default_sampling_settings_are_none() -> None:
    critic, model = _critic()
    _assess(critic)
    assert model.requests[0].temperature is None
    assert model.requests[0].max_output_tokens is None


def test_forwarded_temperature_and_max_output_tokens() -> None:
    critic, model = _critic()
    _assess(critic, temperature=0.2, max_output_tokens=256)
    assert model.requests[0].temperature == 0.2
    assert model.requests[0].max_output_tokens == 256


@pytest.mark.parametrize(
    "field", ["question", "answer", "evidence_context"]
)
def test_blank_fields_rejected_before_any_model_call(field: str) -> None:
    critic, model = _critic()
    with pytest.raises(ValueError):
        _assess(critic, **{field: "   "})
    assert model.call_count == 0


def test_non_string_fields_rejected() -> None:
    critic, model = _critic()
    for field in ("question", "answer", "evidence_context"):
        with pytest.raises(ValueError):
            _assess(critic, **{field: 42})  # type: ignore[dict-item]
    assert model.call_count == 0


def test_fields_with_special_whitespace_are_preserved() -> None:
    question = "  What about  \nmulti-line\nquestions?  "
    critic, model = _critic()
    _assess(critic, question=question)
    assert question in _user_message(model.requests[0])


def test_system_prompt_is_stable_across_instances() -> None:
    first, first_model = _critic()
    _assess(first)
    second, second_model = _critic()
    _assess(second)
    first_system = first_model.requests[0].messages[0].content
    second_system = second_model.requests[0].messages[0].content
    assert first_system == second_system
    assert first_system.strip()


def test_assess_is_stateless_across_repeated_calls() -> None:
    critic, model = _critic()
    first = _assess(critic)
    second = _assess(critic, temperature=0.1)
    assert first == second
    assert model.call_count == 2
    assert model.requests[1].temperature == 0.1


def test_critic_parse_error_is_a_value_error() -> None:
    assert issubclass(CriticParseError, ValueError)
    assert issubclass(CriticParseError, CriticParseError)


# E. Package contract and condition isolation


def test_module_exports_full_public_api() -> None:
    import responsible_agentic_workflows.workflow.critic as critic_module

    assert critic_module.__all__ == [
        "CRITIC_PROMPT_VERSION",
        "CRITIC_SCHEMA_VERSION",
        "CriticParseError",
        "StructuredCritic",
        "parse_critic_result",
    ]
    for name in critic_module.__all__:
        assert hasattr(critic_module, name)


def test_workflow_package_exports_critic_api() -> None:
    import responsible_agentic_workflows.workflow as workflow

    for name in (
        "CRITIC_PROMPT_VERSION",
        "CRITIC_SCHEMA_VERSION",
        "CriticParseError",
        "StructuredCritic",
        "parse_critic_result",
    ):
        assert name in workflow.__all__
        assert hasattr(workflow, name)


def test_critic_source_has_no_condition_leakage() -> None:
    import responsible_agentic_workflows.workflow.critic as critic_module

    source = pathlib.Path(critic_module.__file__).read_text(encoding="utf-8")
    forbidden = (
        "B0Baseline",
        "B0Result",
        "B1FixedRecoveryPolicy",
        "RecoveryPolicy",
        "RecoveryDecision",
        "RecoveryPath",
        "ResourceLimits",
        "ResourceSnapshot",
        "HardRecoveryFeasibility",
        "RecoveryPolicyContext",
        "RecoveryIterationRecord",
        "G1",
    )
    for name in forbidden:
        assert name not in source, f"forbidden reference leaked: {name}"


def test_structured_critic_state_is_only_the_wrapped_model() -> None:
    model = FakeModel()
    critic = StructuredCritic(model=model)
    assert set(vars(critic)) == {"_model"}
    assert critic._model is model


def test_parsed_result_feeds_control_state_and_release_rule() -> None:
    release_doc = parse_critic_result(_doc())
    state = CriticControlState.from_critic_result(release_doc)
    assert state.release_ok is True
    assert release_ok(release_doc) is True

    blocked_doc = parse_critic_result(
        _doc(
            support_status="PARTIAL_SUPPORT",
            gap_types=["DRAFT_GROUNDING"],
        )
    )
    blocked_state = CriticControlState.from_critic_result(blocked_doc)
    assert blocked_state.release_ok is False
    assert release_ok(blocked_doc) is False


def test_system_prompt_states_complete_critic_contract() -> None:
    critic, model = _critic()
    _assess(critic)

    prompt = model.requests[0].messages[0].content

    required = (
        "SUPPORTED",
        "PARTIAL_SUPPORT",
        "UNSUPPORTED",
        "SUFFICIENT",
        "INSUFFICIENT",
        "DRAFT_GROUNDING",
        "MISSING_EVIDENCE",
        "INCOMPLETE_EVIDENCE",
        "EVIDENCE_CONFLICT",
        "separate dimensions",
        "outside knowledge",
        "empty arrays",
        "schema_version",
        '"0.1"',
        "benchmark correctness score",
        "recovery action",
        "policy decision",
        "resource judgment",
        "All nine keys are required",
    )

    for fragment in required:
        assert fragment in prompt

    assert "If unresolved_conflict is true" in prompt
    assert "must include EVIDENCE_CONFLICT" in prompt
    assert "exactly one JSON object" in prompt
    assert "code fences" in prompt
