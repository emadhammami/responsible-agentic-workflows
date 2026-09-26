# Prospective Task Authoring Protocol v0.2 Amendment

Date: 2026-09-26

## Decision and exact omissions

The UC3 Step-0 protocol gate stopped with `T3B_PROTOCOL_GATE=FAIL` before creating any candidate. Direct inspection of v0.1 and its historical freeze evidence found two missing explicit controls:

1. No ordered prospective authoring chronology specified the complete sequence from frozen-corpus inspection and information-need identification through question/type drafting, minimal reference-answer drafting, direct evidence binding, corpus-wide absence audit, structural/quality validation, researcher review/corrections, explicit approval before human_verified, and final validation/cryptographic freeze before benchmark execution. Existing separate rules did not explicitly establish that sequence.
2. No explicit non-trivial-task rule prohibited information needs consisting only of document identity, document title, legal/reference citation or trivial metadata lookup, or stated that technical answerability of a title/reference/name alone was insufficient. No explicit substantive-content requirement for localized direct retrieval supplied that omission.

V0_1_AUTHORING_CHRONOLOGY_EXPLICIT=NO
V0_1_NONTRIVIAL_TASK_RULE_EXPLICIT=NO
PROTOCOL_DEFECT_TYPE=EXPLICITNESS_AND_PROVENANCE_CONTROL
SCIENTIFIC_RESULT_DEFECT=NO

## Immutable history and additive amendment

v0.1 and its freeze evidence are immutable historical artifacts. Editing them would obscure what was actually explicit at the historical freeze. v0.2 preserves the complete original scientific content and adds the two controls prospectively, together with exact predecessor binding and historical/prospective metadata. It does not retroactively claim that v0.1 contained either control.

Only `schema_version` (0.1 to 0.2) and the version suffix of `protocol_id` change among original fields. The original `base_commit`, `status`, design bindings, allocation, authoring rules and controls are preserved exactly. The inherited base identifies the historical design base; `amendment_base_commit` identifies the actual amendment state. The inherited frozen-before-authoring status applies to v0.2's prospective governing scope and does not claim an amendment before UC2 authoring.

The new `authoring_chronology` has nine explicitly numbered steps in the researcher-directed order. The new `nontrivial_task_rule` requires realistic document-based information needs, prohibits the four lookup-only categories, rejects title/reference/name-only answerability as sufficient, and requires substantive content for localized direct retrieval. No original corpus, allocation, task-type, result-independence, human-verification or runtime gold-isolation requirement disappears or weakens.

## Historical / prospective boundary

UC2 T011-T020 were already frozen in the commit below before this amendment. Their recorded qualification includes candidate evidence audits, task-type checks, ambiguity review, explicit researcher approval, gold-isolation validation and cryptographic freeze. The UC2 freeze evidence and final researcher-approval section in its dossier corroborate that history. UC2 is neither changed nor re-authored, and its historical evidence is not relabeled as governed prospectively by v0.2.

UC3 has a source inventory only. Candidate questions T021-T030 have not been created. v0.2 governs UC3 candidate authoring and subsequent primary-benchmark task authoring. This amendment occurs after UC2 authoring/freeze and before UC3 candidate authoring. No B0/B1/G1 benchmark execution has occurred, the benchmark has not started, and no benchmark results or retrieval performance influenced this amendment. No candidates, reference answers or task JSON were created in this step.

UC2_ALREADY_FROZEN=YES
UC2_REAUTHORING_REQUIRED=NO
UC3_CANDIDATE_AUTHORING_STARTED=NO
BENCHMARK_STARTED=NO
RESULT_DRIVEN_AMENDMENT=NO

## Identity bindings

BRANCH=research/benchmark-task-construction-uc2-uc3
AMENDMENT_BASE_HEAD=a24c6d6e8ceffcc149b09c148a0bf69f562eb31c
V0_1_PATH=benchmark/task_authoring_protocol_v0.1.json
V0_1_SHA256=c537f2a627c8f0734b3e4addc8a52ce96132a2cde762b0dca6be338aee1fe169
V0_1_FREEZE_EVIDENCE_PATH=evidence/engineering/primary_task_authoring_protocol_freeze_2026-09-26.md
V0_1_FREEZE_EVIDENCE_SHA256=a2ea4a51c0925773b2b9153b783b059e3bb3c549f3e7b619471a917bdd168213
V0_2_PATH=benchmark/task_authoring_protocol_v0.2.json
V0_2_SHA256=13e360d22ef94f670603c0349058ba0244a085493c69a26266b45f22d1a2b7e6
UC2_FREEZE_COMMIT=a24c6d6e8ceffcc149b09c148a0bf69f562eb31c
UC3_INVENTORY_PATH=evidence/engineering/uc3_task_authoring_inventory_2026-09-26.md
UC3_INVENTORY_SHA256=f73f3c06bb96eeec47e0602b1d9d521f346a003bb39be39dfdf2f8f3ec0ef476

The v0.1 hash agrees with its historical freeze evidence. The historical freeze evidence's own hash was computed before mutation and compared again afterward. The inventory retains the exact expected hash. Protected UC1 task files, frozen UC2 task/manifest files and tracked UC2 evidence were also hashed before and after this amendment and remain byte-identical.

## Additive-equivalence and scope validation

A recursive programmatic comparison visits every v0.1 field/value in v0.2. Dict keys must remain present and nested values and lists remain exactly equal; only the two explicitly enumerated top-level version-identity fields are exempt. Their new values are checked explicitly. Original authoring rules and controls are unchanged, not paraphrased. All new top-level fields are additive metadata or controls. JSON parsing and the exact nine-step order and four prohibited-only categories are validated.

V0_1_CONTENT_PRESERVED=PASS
V0_2_ADDITIVE_CONTROLS=PASS
AUTHORING_CHRONOLOGY_EXPLICIT=YES
NONTRIVIAL_TASK_RULE_EXPLICIT=YES
V0_1_IMMUTABLE=YES
HISTORICAL_V0_1_FREEZE_EVIDENCE_UNCHANGED=YES
UC3_INVENTORY_UNCHANGED=YES
FROZEN_UC2_FILES_UNCHANGED=YES
UC1_TASK_FILES_UNCHANGED=YES
TRACKED_MODIFIED_COUNT=0
STAGED_COUNT=0
UNTRACKED_COUNT=3
DIFF_CHECK=PASS

The exact untracked set consists of the existing UC3 inventory, the new v0.2 JSON protocol and this amendment evidence. No scientific task content, source corpus, runtime code or historical artifact was edited. No retrieval, embeddings, model inference, B0/B1/G1 execution or benchmark tasks were run.

TASK_CANDIDATES_CREATED=NO
TASK_JSON_CREATED=NO
RESULT_DRIVEN_AMENDMENT=NO
UC3_CANDIDATE_AUTHORING_STARTED=NO
BENCHMARK_STARTED=NO
COMMIT=NO
PUSH=NO
