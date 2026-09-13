"""Deterministic G1 evidence- and resource-gated recovery policy."""

from __future__ import annotations

from dataclasses import dataclass

from .control import (
    EvidenceSufficiency,
    GapType,
    HardRecoveryFeasibility,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryPolicyContext,
    RecoveryReasonCode,
    ResourceLimits,
    ResourceSnapshot,
)

_RETRIEVE_GAP_TYPES = (GapType.MISSING_EVIDENCE, GapType.INCOMPLETE_EVIDENCE)


@dataclass(frozen=True, slots=True)
class G1ERGRPolicy:
    """Evidence- and resource-gated recovery policy with explicit abstention."""

    policy_id: str

    def __post_init__(self) -> None:
        if not isinstance(self.policy_id, str):
            raise ValueError("policy_id must be a string")

        if not self.policy_id.strip():
            raise ValueError("policy_id must be a non-empty string")

    def decide(self, context: RecoveryPolicyContext) -> RecoveryDecision:
        if context.critic.release_ok:
            return RecoveryDecision(
                action=RecoveryAction.ACCEPT,
                reason_code=RecoveryReasonCode.RELEASE_OK,
                policy_id=self.policy_id,
            )

        if context.critic.unresolved_conflict:
            return self._decision(
                action=RecoveryAction.ABSTAIN,
                reason_code=RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE,
            )

        selected_path = self._select_path(context)

        if selected_path is None:
            return self._decision(
                action=RecoveryAction.ABSTAIN,
                reason_code=RecoveryReasonCode.G1_RECOVERY_NOT_WORTHWHILE,
            )

        feasibility = self._selected_path_feasibility(context, selected_path)

        if not feasibility.feasible:
            return self._decision(
                action=RecoveryAction.RESOURCE_STOP,
                reason_code=RecoveryReasonCode.HARD_LIMIT_BLOCKED,
            )

        if not self._reserve_satisfied(context, selected_path):
            return self._decision(
                action=RecoveryAction.RESOURCE_STOP,
                reason_code=RecoveryReasonCode.G1_RESOURCE_RESERVE_BLOCKED,
            )

        if selected_path is RecoveryPath.REVISE_ONLY:
            return self._decision(
                action=RecoveryAction.REVISE_ONLY,
                reason_code=RecoveryReasonCode.G1_REVISE_ONLY,
            )

        return self._decision(
            action=RecoveryAction.RERETRIEVE_REVISE,
            reason_code=RecoveryReasonCode.G1_RERETRIEVE_REVISE,
        )

    def _decision(
        self,
        *,
        action: RecoveryAction,
        reason_code: RecoveryReasonCode,
    ) -> RecoveryDecision:
        return RecoveryDecision(
            action=action,
            reason_code=reason_code,
            policy_id=self.policy_id,
        )

    @staticmethod
    def _select_path(context: RecoveryPolicyContext) -> RecoveryPath | None:
        critic = context.critic

        if critic.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT:
            return RecoveryPath.REVISE_ONLY

        if any(gap in _RETRIEVE_GAP_TYPES for gap in critic.gap_types):
            return RecoveryPath.RERETRIEVE_REVISE

        return None

    @staticmethod
    def _selected_path_feasibility(
        context: RecoveryPolicyContext, path: RecoveryPath
    ) -> HardRecoveryFeasibility:
        for entry in context.hard_recovery_feasibility:
            if entry.recovery_path is path:
                return entry

        raise ValueError(
            f"hard_recovery_feasibility is missing an entry "
            f"for selected recovery path {path.value!r}"
        )

    @staticmethod
    def _reserve_satisfied(
        context: RecoveryPolicyContext, path: RecoveryPath
    ) -> bool:
        resources: ResourceSnapshot = context.resources
        limits: ResourceLimits = context.limits

        if not _enough(resources.llm_calls_remaining(limits), 2):
            return False

        if path is RecoveryPath.RERETRIEVE_REVISE and not _enough(
            resources.retrieval_calls_remaining(limits), 1
        ):
            return False

        return _enough(resources.retries_remaining(limits), 1)


def _enough(remaining: int | None, required: int) -> bool:
    return remaining is None or remaining >= required
