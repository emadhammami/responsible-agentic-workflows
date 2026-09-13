"""Deterministic B1 fixed recovery policy."""

from __future__ import annotations

from dataclasses import dataclass

from .control import (
    EvidenceSufficiency,
    HardRecoveryFeasibility,
    RecoveryAction,
    RecoveryDecision,
    RecoveryPath,
    RecoveryPolicyContext,
    RecoveryReasonCode,
)


@dataclass(frozen=True, slots=True)
class B1FixedRecoveryPolicy:
    """Fixed B1 recovery policy: release, revise, or stop on hard limits."""

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

        selected_path = self._select_path(context)

        feasibility = self._selected_path_feasibility(
            context, selected_path
        )

        if not feasibility.feasible:
            return RecoveryDecision(
                action=RecoveryAction.RESOURCE_STOP,
                reason_code=RecoveryReasonCode.HARD_LIMIT_BLOCKED,
                policy_id=self.policy_id,
            )

        if selected_path is RecoveryPath.REVISE_ONLY:
            return RecoveryDecision(
                action=RecoveryAction.REVISE_ONLY,
                reason_code=RecoveryReasonCode.B1_FIXED_REVISE_ONLY,
                policy_id=self.policy_id,
            )

        return RecoveryDecision(
            action=RecoveryAction.RERETRIEVE_REVISE,
            reason_code=(RecoveryReasonCode.B1_FIXED_RERETRIEVE_REVISE),
            policy_id=self.policy_id,
        )

    @staticmethod
    def _select_path(context: RecoveryPolicyContext) -> RecoveryPath:
        critic = context.critic

        if (
            critic.evidence_sufficiency is EvidenceSufficiency.SUFFICIENT
            and critic.unresolved_conflict is False
        ):
            return RecoveryPath.REVISE_ONLY

        return RecoveryPath.RERETRIEVE_REVISE

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
