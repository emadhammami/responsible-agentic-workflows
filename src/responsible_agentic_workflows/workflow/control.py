"""Typed runtime contracts shared by the B1 and G1 recovery workflows."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol, runtime_checkable

__all__ = [
    "BlockedLimit",
    "CriticControlState",
    "CriticResult",
    "EvidenceSufficiency",
    "GapType",
    "HardRecoveryFeasibility",
    "RecoveryAction",
    "RecoveryDecision",
    "RecoveryPath",
    "RecoveryPolicy",
    "RecoveryPolicyContext",
    "RecoveryReasonCode",
    "ResourceLimits",
    "ResourceSnapshot",
    "SupportStatus",
    "release_ok",
]


class SupportStatus(StrEnum):
    SUPPORTED = "SUPPORTED"
    PARTIAL_SUPPORT = "PARTIAL_SUPPORT"
    UNSUPPORTED = "UNSUPPORTED"


class EvidenceSufficiency(StrEnum):
    SUFFICIENT = "SUFFICIENT"
    INSUFFICIENT = "INSUFFICIENT"


class GapType(StrEnum):
    DRAFT_GROUNDING = "DRAFT_GROUNDING"
    MISSING_EVIDENCE = "MISSING_EVIDENCE"
    INCOMPLETE_EVIDENCE = "INCOMPLETE_EVIDENCE"
    EVIDENCE_CONFLICT = "EVIDENCE_CONFLICT"


class RecoveryAction(StrEnum):
    ACCEPT = "ACCEPT"
    REVISE_ONLY = "REVISE_ONLY"
    RERETRIEVE_REVISE = "RERETRIEVE_REVISE"
    ABSTAIN = "ABSTAIN"
    RESOURCE_STOP = "RESOURCE_STOP"


class RecoveryPath(StrEnum):
    REVISE_ONLY = "REVISE_ONLY"
    RERETRIEVE_REVISE = "RERETRIEVE_REVISE"


class BlockedLimit(StrEnum):
    LLM_CALL_LIMIT = "LLM_CALL_LIMIT"
    RETRIEVAL_CALL_LIMIT = "RETRIEVAL_CALL_LIMIT"
    RETRY_LIMIT = "RETRY_LIMIT"
    TOKEN_LIMIT = "TOKEN_LIMIT"
    TIMEOUT_LIMIT = "TIMEOUT_LIMIT"


class RecoveryReasonCode(StrEnum):
    RELEASE_OK = "RELEASE_OK"
    HARD_LIMIT_BLOCKED = "HARD_LIMIT_BLOCKED"
    B1_FIXED_REVISE_ONLY = "B1_FIXED_REVISE_ONLY"
    B1_FIXED_RERETRIEVE_REVISE = "B1_FIXED_RERETRIEVE_REVISE"
    G1_RECOVERY_NOT_WORTHWHILE = "G1_RECOVERY_NOT_WORTHWHILE"
    G1_REVISE_ONLY = "G1_REVISE_ONLY"
    G1_RERETRIEVE_REVISE = "G1_RERETRIEVE_REVISE"
    G1_RESOURCE_RESERVE_BLOCKED = "G1_RESOURCE_RESERVE_BLOCKED"


def _require_unique(values: tuple[str, ...], field: str) -> None:
    if any(not isinstance(value, str) for value in values):
        raise ValueError(f"{field} entries must be strings")

    if any(not value.strip() for value in values):
        raise ValueError(f"{field} entries must not be empty or whitespace")

    if len(values) != len(set(values)):
        raise ValueError(f"{field} contains duplicates")


def _validate_collections(
    *,
    gap_types: tuple[GapType, ...],
    unsupported_claims: tuple[str, ...],
    incomplete_support: tuple[str, ...],
    evidence_gaps: tuple[str, ...],
) -> None:
    _require_unique(tuple(str(value) for value in gap_types), "gap_types")
    _require_unique(unsupported_claims, "unsupported_claims")
    _require_unique(incomplete_support, "incomplete_support")
    _require_unique(evidence_gaps, "evidence_gaps")


@dataclass(frozen=True, slots=True)
class CriticResult:
    """Immutable structured critic assessment of one answer candidate."""

    schema_version: str
    support_status: SupportStatus
    evidence_sufficiency: EvidenceSufficiency
    unresolved_conflict: bool
    gap_types: tuple[GapType, ...] = ()
    unsupported_claims: tuple[str, ...] = ()
    incomplete_support: tuple[str, ...] = ()
    evidence_gaps: tuple[str, ...] = ()
    explanation: str | None = None

    def __post_init__(self) -> None:
        if (
            not isinstance(self.schema_version, str)
            or not self.schema_version.strip()
        ):
            raise ValueError("schema_version must be a non-empty string")

        if not isinstance(self.support_status, SupportStatus):
            raise ValueError("Unsupported support_status value")

        if not isinstance(self.evidence_sufficiency, EvidenceSufficiency):
            raise ValueError("Unsupported evidence_sufficiency value")

        if not isinstance(self.unresolved_conflict, bool):
            raise ValueError("unresolved_conflict must be a boolean")

        if any(not isinstance(value, GapType) for value in self.gap_types):
            raise ValueError("gap_types must contain only GapType values")

        _validate_collections(
            gap_types=self.gap_types,
            unsupported_claims=self.unsupported_claims,
            incomplete_support=self.incomplete_support,
            evidence_gaps=self.evidence_gaps,
        )

        if self.unresolved_conflict and GapType.EVIDENCE_CONFLICT not in (
            self.gap_types
        ):
            raise ValueError(
                "unresolved_conflict requires GapType.EVIDENCE_CONFLICT"
            )

        if self.explanation is not None:
            if (
                not isinstance(self.explanation, str)
                or not self.explanation.strip()
            ):
                raise ValueError(
                    "explanation must be a non-empty string or None"
                )

@dataclass(frozen=True, slots=True)
class CriticControlState:
    """Restricted policy-visible projection of the critic result."""

    support_status: SupportStatus
    evidence_sufficiency: EvidenceSufficiency
    unresolved_conflict: bool
    gap_types: tuple[GapType, ...]
    release_ok: bool

    @classmethod
    def from_critic_result(cls, result: CriticResult) -> CriticControlState:
        return cls(
            support_status=result.support_status,
            evidence_sufficiency=result.evidence_sufficiency,
            unresolved_conflict=result.unresolved_conflict,
            gap_types=result.gap_types,
            release_ok=release_ok(result),
        )


def release_ok(result: CriticResult) -> bool:
    """Return whether a critic result satisfies the shared release rule."""

    return (
        result.support_status is SupportStatus.SUPPORTED
        and result.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT
        and result.unresolved_conflict is False
    )


@dataclass(frozen=True, slots=True)
class ResourceLimits:
    """Immutable hard execution ceilings shared by B1 and G1."""

    max_llm_calls: int | None
    max_retrieval_calls: int | None
    max_retries: int | None
    max_total_tokens: int | None
    timeout_ms: float | None

    def __post_init__(self) -> None:
        if self.max_llm_calls is not None and self.max_llm_calls < 1:
            raise ValueError("max_llm_calls must be at least 1")

        if (
            self.max_retrieval_calls is not None
            and self.max_retrieval_calls < 1
        ):
            raise ValueError("max_retrieval_calls must be at least 1")

        if self.max_retries is not None and self.max_retries < 0:
            raise ValueError("max_retries must not be negative")

        if self.max_total_tokens is not None and self.max_total_tokens < 1:
            raise ValueError("max_total_tokens must be at least 1")

        if self.timeout_ms is not None and self.timeout_ms <= 0:
            raise ValueError("timeout_ms must be greater than zero")


@dataclass(frozen=True, slots=True)
class ResourceSnapshot:
    """Immutable policy-time counter snapshot from recorded execution."""

    llm_calls_used: int
    retrieval_calls_used: int
    retries_used: int
    input_tokens_used: int
    output_tokens_used: int
    total_tokens_used: int

    def __post_init__(self) -> None:
        counters = {
            "llm_calls_used": self.llm_calls_used,
            "retrieval_calls_used": self.retrieval_calls_used,
            "retries_used": self.retries_used,
            "input_tokens_used": self.input_tokens_used,
            "output_tokens_used": self.output_tokens_used,
            "total_tokens_used": self.total_tokens_used,
        }

        for name, value in counters.items():
            if value < 0:
                raise ValueError(f"{name} must not be negative")

        if self.total_tokens_used != (
            self.input_tokens_used + self.output_tokens_used
        ):
            raise ValueError(
                "total_tokens_used must equal input plus output tokens"
            )

    def llm_calls_remaining(self, limits: ResourceLimits) -> int | None:
        return self._remaining(limits.max_llm_calls, self.llm_calls_used)

    def retrieval_calls_remaining(
        self, limits: ResourceLimits
    ) -> int | None:
        return self._remaining(
            limits.max_retrieval_calls, self.retrieval_calls_used
        )

    def retries_remaining(self, limits: ResourceLimits) -> int | None:
        return self._remaining(limits.max_retries, self.retries_used)

    def total_tokens_remaining(self, limits: ResourceLimits) -> int | None:
        return self._remaining(limits.max_total_tokens, self.total_tokens_used)

    @staticmethod
    def _remaining(limit: int | None, used: int) -> int | None:
        if limit is None:
            return None
        return max(0, limit - used)


@dataclass(frozen=True, slots=True)
class HardRecoveryFeasibility:
    """Path-specific hard-guard feasibility outcome for one recovery path."""

    recovery_path: RecoveryPath
    feasible: bool
    blocked_limits: tuple[BlockedLimit, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.recovery_path, RecoveryPath):
            raise ValueError("Unsupported recovery_path value")

        if any(not isinstance(value, BlockedLimit) for value in (
            self.blocked_limits
        )):
            raise ValueError(
                "blocked_limits must contain only BlockedLimit values"
            )

        _require_unique(
            tuple(str(value) for value in self.blocked_limits),
            "blocked_limits",
        )

        if self.feasible and self.blocked_limits:
            raise ValueError("feasible recovery cannot have blocked limits")

        if not self.feasible and not self.blocked_limits:
            raise ValueError(
                "infeasible recovery requires at least one blocked limit"
            )


@dataclass(frozen=True, slots=True)
class RecoveryPolicyContext:
    """Complete structured input to the shared recovery-policy interface."""

    critic: CriticControlState
    recovery_iteration: int
    resources: ResourceSnapshot
    limits: ResourceLimits
    hard_recovery_feasibility: tuple[HardRecoveryFeasibility, ...]

    def __post_init__(self) -> None:
        if self.recovery_iteration < 0:
            raise ValueError("recovery_iteration must not be negative")

        if not isinstance(self.critic, CriticControlState):
            raise ValueError("critic must be a CriticControlState")

        if not isinstance(self.resources, ResourceSnapshot):
            raise ValueError("resources must be a ResourceSnapshot")

        if not isinstance(self.limits, ResourceLimits):
            raise ValueError("limits must be a ResourceLimits")

        if any(
            not isinstance(value, HardRecoveryFeasibility)
            for value in self.hard_recovery_feasibility
        ):
            raise ValueError(
                "hard_recovery_feasibility must contain "
                "HardRecoveryFeasibility entries"
            )

        paths = [
            value.recovery_path for value in self.hard_recovery_feasibility
        ]

        if len(paths) != len(set(paths)):
            raise ValueError(
                "hard_recovery_feasibility contains duplicate recovery paths"
            )


@dataclass(frozen=True, slots=True)
class RecoveryDecision:
    """One structured recovery-policy decision."""

    action: RecoveryAction
    reason_code: RecoveryReasonCode
    policy_id: str

    def __post_init__(self) -> None:
        if not isinstance(self.action, RecoveryAction):
            raise ValueError("Unsupported action value")

        if not isinstance(self.reason_code, RecoveryReasonCode):
            raise ValueError("Unsupported reason_code value")

        if (
            not isinstance(self.policy_id, str)
            or not self.policy_id.strip()
        ):
            raise ValueError("policy_id must be a non-empty string")


@runtime_checkable
class RecoveryPolicy(Protocol):
    """Shared single-method recovery-policy interface for B1 and G1."""

    def decide(
        self, context: RecoveryPolicyContext
    ) -> RecoveryDecision:
        """Return the policy action for one structured decision context."""
        raise NotImplementedError
