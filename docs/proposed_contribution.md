# Proposed Technical Contribution

**Status:** Revised draft after targeted literature review
**Contribution type:** Controlled empirical systems contribution
**Algorithmic novelty:** Not claimed
**Benchmark started:** No

## 1. Purpose

This document specifies the intended technical contribution and the primary
B1-vs-G1 treatment before either workflow is implemented.

The specification is informed by the targeted literature review in
`docs/literature_novelty_review.md`.

The contribution is not positioned as the invention of evidence sufficiency,
adaptive retrieval, selective verification, abstention, or budget-aware agent
control. Substantial prior work already exists in each of those areas and in
several combinations of them.

The thesis instead evaluates a pre-specified guardrail policy under a matched
agentic workflow design and measures its effect on reliability and realized
resource use in document-based organizational knowledge work.

## 2. Research problem

Agentic document workflows can use planning, retrieval, generation,
verification, and recovery to improve answer quality.

These capabilities also consume resources:

- input and output tokens;
- model calls;
- retrieval calls;
- retries;
- latency;
- additional workflow stages.

A fixed workflow may continue recovery whenever verification reports a problem,
even when the available evidence remains weak or when the expected benefit of
another recovery step does not justify its cost.

Conversely, stopping too early can leave a recoverable answer incomplete or
unsupported.

The empirical question is whether an explicit evidence- and resource-aware
recovery policy provides a better reliability-resource trade-off than an
otherwise matched agentic workflow using a fixed recovery policy.

## 3. Contribution positioning

The primary technical contribution is:

> A controlled empirical evaluation of a pre-specified evidence- and
> resource-aware recovery policy against an otherwise matched fixed-policy
> agentic baseline for document-based organizational knowledge work.

The study contributes through the combination of:

1. a matched B1-vs-G1 workflow design;
2. transparent and pre-specified treatment logic;
3. common model, retrieval, tasks, environment, and evaluation;
4. explicit measurement of reliability and resource consumption;
5. analysis of harmful as well as beneficial interventions;
6. multiple real document-based use cases;
7. integration with stakeholder perceptions of trust, usefulness, risk,
   control, and organizational adoption.

This is an empirical systems contribution.

It does not depend on claiming that the underlying control primitives are
individually novel.

## 4. Working policy name

The working label is:

**Evidence- and Resource-Gated Recovery (ERGR)**

ERGR is a descriptive name for the G1 guardrail policy.

The name does not imply algorithmic novelty.

The policy may be renamed before the benchmark configuration is frozen.

## 5. Common B1 and G1 architecture

B1 and G1 must use the same core workflow capabilities.

The shared conceptual path is:

    task
      |
      v
    planner
      |
      v
    retrieval
      |
      v
    draft generation
      |
      v
    critic / verifier
      |
      v
    recovery / finalization policy
      |
      v
    final answer or abstention

The following components must be shared unless a treatment-specific difference
is explicitly documented:

- planner implementation;
- initial retrieval;
- draft generator;
- critic / verifier;
- recovery implementation;
- generation model;
- generation-model parameters;
- embedding model;
- vector store;
- chunking;
- retrieval configuration;
- benchmark tasks;
- execution environment;
- logging;
- evaluation procedure;
- initial resource limits.

The treatment should therefore be concentrated in the policy that acts on the
critic result and runtime resource state.

## 6. B1 - matched fixed-policy agentic baseline

B1 is the matched agentic baseline.

It contains the same planner, retrieval, generation, critic, and recovery
capabilities as G1.

Its control behavior is fixed rather than resource-adaptive.

The provisional B1 policy is:

1. plan the task;
2. perform initial retrieval;
3. generate an initial draft;
4. always run the shared critic once;
5. if the critic accepts the draft, finalize it;
6. if the critic rejects the draft, select one bounded shared recovery path
   according to the pre-specified fixed mapping;
7. the fixed mapping selects REVISE_ONLY when the evidence is sufficient and
   no unresolved conflict remains, and RERETRIEVE_REVISE otherwise;
8. the selected path revises the answer, with additional retrieval only for
   RERETRIEVE_REVISE;
9. run the shared critic on the revised answer;
10. finalize according to the shared post-recovery rule.

B1 does not use remaining token allowance, remaining model calls, remaining
retrieval calls, or a resource-value decision to choose whether recovery should
occur.

Hard execution limits still apply for safety and comparability.

B1 must not be intentionally weakened.

## 7. G1 - evidence- and resource-gated recovery

G1 uses the same core components as B1.

The initial sequence is also the same:

1. plan;
2. retrieve;
3. generate an initial draft;
4. run the shared critic.

After the critic result is available, G1 enables ERGR.

The pre-recovery ERGR rule is pre-specified before scientific benchmark
execution.

The frozen decision order is:

1. if the shared release predicate is satisfied, `ACCEPT`;
2. if a material unresolved evidence conflict remains, `ABSTAIN`;
3. if evidence is `SUFFICIENT` and no unresolved conflict remains, select
   `REVISE_ONLY`;
4. if evidence is `INSUFFICIENT`, no unresolved conflict remains, and the
   structured gap state contains `MISSING_EVIDENCE` or `INCOMPLETE_EVIDENCE`,
   select `RERETRIEVE_REVISE`;
5. otherwise, `ABSTAIN`;
6. for a selected recovery path, apply the common hard-feasibility result;
7. if the path is hard-infeasible, return `RESOURCE_STOP`;
8. if the path is hard-feasible, apply the path-specific G1 completion reserve;
9. if the reserve is unavailable, return `RESOURCE_STOP`;
10. otherwise execute the selected bounded recovery path.

The path-specific completion reserve is derived from the shared recovery
structure rather than benchmark outcomes.

`REVISE_ONLY` requires capacity for:

- one bounded recovery cycle;
- the revision model call; and
- the required shared post-recovery critic call.

Operationally, when the corresponding limits are configured, this means at
least two remaining LLM-call slots and one remaining retry/recovery slot.

`RERETRIEVE_REVISE` additionally requires one remaining retrieval-call slot.

No token-percentage threshold, average-token estimate, safety multiplier, or
latency threshold is introduced into the G1 reserve.

The common total-token hard guard still prevents recovery when configured total
token capacity is already exhausted.

This design intentionally separates:

- the common hard guard, which asks whether recovery can legally begin; from
- the G1 completion reserve, which asks whether enough structured capacity
  remains to commit to the selected bounded recovery path.

The resulting G1 treatment is therefore both evidence-aware and resource-aware
while remaining deterministic, inspectable, and pre-specified.

## 8. Why verification is shared

The shared critic is intentionally present in both B1 and G1.

This prevents the primary comparison from degenerating into:

> no verification versus verification.

Such a design would confound the effect of the recovery policy with the
existence of a verifier.

The intended comparison is narrower:

> fixed recovery policy versus evidence- and resource-aware recovery policy,
> using the same critic capability.

This design also reduces overlap with prior work whose main contribution is
selective invocation of verification itself.

## 9. Evidence state available to G1

G1 receives the same restricted structured critic projection used by the common
recovery-policy interface:

    CriticControlState
      support_status
      evidence_sufficiency
      unresolved_conflict
      gap_types
      release_ok

The G1 policy does not branch directly on:

- `unsupported_claims` free text;
- `incomplete_support` free text;
- `evidence_gaps` free text;
- critic explanation;
- raw benchmark question text;
- document text;
- benchmark reference answers;
- benchmark reference evidence;
- human adjudication labels;
- final benchmark correctness scores.

Diagnostic text may still be used later by the shared recovery implementation
after the policy has already selected a recovery path.

The evidence-state representation used by the G1 decision rule is therefore
structured and frozen before scientific execution.

## 10. Resource state available to G1

G1 receives the same immutable resource snapshot and resource limits available
through the shared recovery-policy context.

The relevant resource dimensions are:

- LLM calls used and remaining;
- retrieval calls used and remaining;
- retries/recovery cycles used and remaining;
- total tokens used and remaining.

Remaining values are derived from the common limits and authoritative recorded
usage rather than maintained as treatment-specific counters.

The common hard guard is shared by B1 and G1.

The frozen G1 completion reserve is path-specific:

- `REVISE_ONLY`: at least two remaining LLM-call slots and one remaining
  retry/recovery slot when those limits are configured;
- `RERETRIEVE_REVISE`: the same requirements plus at least one remaining
  retrieval-call slot.

A resource limit configured as `None` is disabled and does not block the G1
reserve.

The two LLM-call slots correspond to the revision generation call and the
required shared post-recovery critic call.

No prospective token-cost estimate or latency threshold is used in the G1
policy.

B1 and G1 begin comparable runs with the same externally imposed resource
limits.

## 11. Resource parity

B1 and G1 must begin each comparable task with the same externally imposed
resource limits.

G1 must not receive a larger initial token, call, retrieval, retry, or latency
allowance.

Differences in realized resource consumption should arise from workflow
behavior rather than unequal starting allocations.

The same rule applies across benchmark repetitions.

## 12. Treatment isolation

The intended treatment is the recovery/finalization policy.

The following must not differ merely because a run belongs to G1:

- model identity;
- model context length;
- temperature;
- seed policy;
- embedding model;
- vector store;
- initial top-k retrieval;
- corpus;
- benchmark task;
- core critic implementation;
- core recovery implementation;
- evaluation criteria.

If the policy necessarily introduces a treatment-specific prompt or decision
instruction, that difference must be explicitly documented and frozen.

## 13. Provisional hypotheses

### H1 - reliability

G1 will reduce unsupported or otherwise unreliable final answers relative to
the matched B1 workflow.

### H2 - resource efficiency

G1 will reduce unnecessary recovery activity and realized resource consumption
relative to B1 without a practically important degradation in task
performance.

### H3 - insufficient evidence

G1 will improve appropriate abstention on insufficient-evidence tasks without
an unacceptable increase in incorrect abstention on answerable tasks.

### H4 - recovery efficiency

A greater proportion of G1 recovery actions will result in useful repairs,
while fewer recovery actions will be spent on cases where another step does
not improve the final outcome.

### H5 - reliability-resource trade-off

G1 will show a more favorable reliability-resource trade-off than B1 rather
than obtaining reliability improvements solely by consuming more resources.

These hypotheses remain provisional until the treatment and resource
configuration are frozen.

## 14. Falsification criteria

The proposed policy should not be interpreted as beneficial if:

- G1 consumes more resources without a meaningful reliability benefit;
- G1 achieves reliability gains mainly because it effectively receives more
  usable computation than B1;
- recovery suppression causes preventable task failures;
- abstention substantially reduces useful completion on answerable tasks;
- recovery actions are not more targeted than under B1;
- the policy frequently stops when a bounded recovery would have repaired the
  answer;
- effects disappear under comparable realized resource use;
- effects are unstable across use cases without a defensible explanation.

Negative and null findings remain valid thesis results.

The policy must not be redesigned after primary benchmark results are observed
in order to rescue the hypotheses.

## 15. Intervention outcomes

The analysis should distinguish the effect of guardrail interventions rather
than counting all interventions as beneficial.

Where the benchmark evidence permits, recovery or control actions should be
classified as:

- beneficial intervention;
- neutral intervention;
- harmful intervention;
- unnecessary intervention;
- unsuccessful recovery;
- appropriate abstention;
- incorrect abstention;
- justified resource stop;
- harmful resource stop.

Operational definitions must be frozen before benchmark scoring.

## 16. Resource and runtime measurements

At minimum, the technical benchmark should preserve:

- input tokens;
- output tokens;
- total tokens;
- model calls;
- retrieval or tool calls;
- retries;
- verification calls;
- recovery attempts;
- successful recoveries;
- end-to-end latency;
- stage-level latency where available.

Derived measures may include:

- tokens per completed task;
- model calls per completed task;
- recovery trigger rate;
- recovery success rate;
- abstention rate;
- incorrect abstention rate;
- resource-stop rate;
- harmful intervention rate.

## 17. Reliability-resource analysis

The main analysis should not reduce performance to a single scalar score.

The study should examine:

- reliability at comparable realized resource use;
- resource use at comparable reliability;
- task success under equal initial limits;
- guardrail intervention frequency;
- recovery effectiveness;
- latency-resource trade-offs;
- Pareto-style reliability-resource relationships where supported by the data.

A G1 improvement that is obtained only through systematically greater resource
consumption must be reported as such.

## 18. Relationship to prior work

The targeted literature review shows substantial overlap with the individual
mechanisms involved in ERGR.

Prior work already covers:

- adaptive retrieval;
- corrective retrieval;
- self-reflection;
- evidence sufficiency;
- selective answering;
- abstention;
- selective verification;
- explicit resource budgets;
- budget-aware search;
- answer commitment and stopping.

Accordingly, this thesis makes no priority claim about combining evidence
information and resource information.

The contribution is the pre-specified matched empirical evaluation of this
guardrail policy in the study context and the resulting evidence about its
reliability-resource behavior and organizational adoption implications.

## 19. Publication-oriented claim

The strongest currently defensible technical claim is:

> Under matched model, retrieval, task, and resource constraints, this study
> evaluates whether an evidence- and resource-aware recovery policy changes the
> reliability-resource trade-off of an agentic document workflow relative to a
> fixed-policy agentic baseline.

A stronger algorithmic novelty claim requires additional evidence and is not
part of the current study design.

## 20. Freeze requirements before B1/G1 benchmark execution

Before scientific benchmark execution, the following must be specified and
frozen:

- common B1/G1 state graph;
- planner behavior;
- critic contract;
- evidence-state representation;
- B1 fixed recovery rule;
- G1 ERGR decision rule;
- G1 path-specific resource reserve rules for the `REVISE_ONLY` and
  `RERETRIEVE_REVISE` recovery paths;
- recovery limit;
- abstention rule;
- resource-stop rule;
- maximum model calls;
- maximum retrieval/tool calls;
- retry limit;
- per-call output limit;
- total workflow resource limits if used;
- prompts and prompt versions;
- workflow configuration identifiers;
- logging events required for intervention analysis.

Synthetic engineering tests may be used before freeze.

Scientific benchmark results must not be used to select these values.

## 21. Current decision

At this checkpoint:

- B0 engineering validation is complete;
- algorithmic novelty of broad ERGR is not claimed;
- ERGR is retained as a descriptive composite guardrail policy;
- verification is shared between B1 and G1;
- the primary treatment is fixed versus evidence/resource-aware recovery;
- the B1 fixed recovery policy is implemented;
- the shared structured critic is implemented;
- the common hard-recovery feasibility calculation is implemented;
- the G1 recovery-worthiness rule is frozen for implementation;
- the G1 path-specific completion-reserve rule is frozen for implementation;
- G1 policy code has not yet been implemented;
- the common workflow graph and recovery execution have not yet been
  implemented;
- the scientific benchmark has not started.

The next implementation step is the deterministic G1 policy using the frozen
structured decision rule, shared hard-feasibility result, and path-specific
completion reserve.
