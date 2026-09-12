# B1/G1 Common Workflow Contract

**Status:** Pre-implementation working specification
**Primary comparison:** B1 vs G1
**Primary treatment:** Recovery decision policy
**Benchmark started:** No

## 1. Purpose

This document specifies the common B1/G1 agentic workflow before either
condition is implemented.

The purpose is to isolate the primary treatment as narrowly as possible.

B1 and G1 should therefore be implementations of one common workflow graph
with shared nodes and shared state. The condition-specific behavior should be
injected through a recovery policy rather than implemented as two substantially
different workflow graphs.

This specification is pre-benchmark. It may be refined during engineering, but
it must not be changed later in response to primary benchmark performance.

## 2. Design principle

The primary comparison is:

**B1 fixed recovery policy vs G1 evidence- and resource-aware recovery policy**

The comparison is not:

- no critic vs critic;
- simple RAG vs agentic RAG;
- fewer capabilities vs more capabilities;
- smaller resource allowance vs larger resource allowance.

Both conditions receive the same core agentic capabilities and the same
initial externally imposed resource limits.

## 3. Shared graph

The working common graph is:

    START
      |
      v
    PLAN
      |
      v
    INITIAL_RETRIEVE
      |
      v
    DRAFT
      |
      v
    CRITIC
      |
      v
    RECOVERY_POLICY
      |
      +-------------------- ACCEPT --------------------+
      |                                                |
      +--------------- RERETRIEVE_REVISE --------------+
      |                                                |
      +------------------- ABSTAIN --------------------+
      |                                                |
      +---------------- RESOURCE_STOP -----------------+
                                                       |
                                                       v
                                                    TERMINAL

For `RERETRIEVE_REVISE`, the shared recovery path is:

    RECOVERY_POLICY
      |
      v
    RECOVERY_RETRIEVE
      |
      v
    REVISE
      |
      v
    CRITIC
      |
      v
    POST_RECOVERY_FINALIZE
      |
      +---------- ACCEPT
      |
      +---------- ABSTAIN
      |
      +---------- RESOURCE_STOP
      |
      v
    TERMINAL

The current primary design allows at most one recovery cycle.

This one-cycle limit is provisional until the full workflow configuration is
frozen.

## 4. One graph, injected policy

B1 and G1 should not be implemented as unrelated graphs.

The preferred implementation is one shared LangGraph state graph whose
condition-specific recovery decision is supplied through a small policy
interface.

Conceptually:

    CommonAgenticWorkflow(policy=B1FixedRecoveryPolicy)

and:

    CommonAgenticWorkflow(policy=G1EvidenceResourceRecoveryPolicy)

All non-policy nodes should use the same implementation objects in both
conditions.

This architecture makes the treatment difference explicit and auditable.

## 5. Shared workflow state

The workflow state should contain only runtime information needed for execution,
control, and logging.

A conceptual state contract is:

### Task identity

- task ID;
- question;
- execution mode;
- benchmark condition when applicable.

### Planning state

- structured plan;
- retrieval query or queries;
- answer requirements or subgoals where used.

### Evidence state

- initially retrieved chunks;
- recovery-retrieved chunks;
- currently available evidence;
- provenance for every retrieved chunk.

### Generation state

- current draft;
- revision count;
- current answer candidate.

### Critic state

- latest critic assessment;
- unsupported or incompletely supported claims;
- contradiction indicators;
- evidence sufficiency assessment;
- critic iteration.

### Recovery state

- recovery iteration;
- latest policy action;
- policy reason code;
- whether recovery was attempted;
- whether recovery completed.

### Resource state

- model calls used;
- retrieval or tool calls used;
- retries used;
- input tokens used;
- output tokens used;
- total tokens used;
- corresponding configured limits where applicable.

### Final state

- final answer;
- abstained flag;
- terminal outcome;
- cited chunk IDs if explicit citation generation is later enabled.

The workflow state must never contain benchmark reference answers, reference
evidence, adjudication labels, benchmark correctness scores, or other gold
information.

## 6. Planner contract

The planner is shared by B1 and G1.

Its role is to transform the task into a bounded execution plan suitable for
document retrieval and answer generation.

The exact planner prompt and structured schema remain open.

The planner must not:

- inspect benchmark gold information;
- know whether the run belongs to B1 or G1 unless technically unavoidable;
- alter its planning strategy based on benchmark results;
- allocate a larger initial execution allowance to G1.

The planner output should be bounded and machine-validated.

## 7. Retrieval contract

Initial retrieval is shared between B1 and G1.

The same retrieval implementation, frozen corpus, embedding model, vector
store, chunking policy, ranking method, and initial retrieval parameters must
be used for comparable runs.

Recovery retrieval uses the same retrieval infrastructure.

A recovery query may differ from the initial query because it can be informed
by the shared critic's identified evidence gap.

The method that constructs a recovery query must be shared between B1 and G1.

## 8. Draft-generation contract

The draft-generation node is shared.

It receives:

- the original question;
- the relevant plan information;
- retrieved evidence with provenance.

It produces an answer candidate.

The same prompt version and generation configuration must be used in B1 and G1.

The draft node does not decide whether its answer should be accepted.

## 9. Shared critic contract

The critic is a shared capability and must use the same implementation,
model identity, prompt version, and structured output contract in B1 and G1.

The critic evaluates the answer candidate against the runtime evidence.

It should report assessment information, not choose the workflow action.

The critic must therefore not directly output:

- `RERETRIEVE_REVISE`;
- `RESOURCE_STOP`;
- a B1/G1-specific action;
- a resource-allocation decision.

A provisional critic result should separate answer support from evidence
sufficiency.

The conceptual fields are:

### Answer-support status

`support_status` describes whether the current answer candidate is supported by
the evidence currently available to the workflow.

Working values are:

- `SUPPORTED`;
- `PARTIAL_SUPPORT`;
- `UNSUPPORTED`.

### Evidence sufficiency

`evidence_sufficiency` describes whether the currently available evidence is
adequate to support a defensible answer to the task.

Working values are:

- `SUFFICIENT`;
- `INSUFFICIENT`.

### Additional evidence assessment

The critic should also expose:

- `conflicting_evidence`, as a boolean or equivalent structured field;
- identified unsupported claims;
- identified incomplete support;
- evidence gaps;
- optional structured explanation required for auditing.

Answer support and evidence sufficiency are intentionally separate.

An answer may be unsupported because the draft is poor even when sufficient
evidence exists, while an answer may be impossible to support because the
available evidence is itself insufficient.

A shared release predicate should be derived from the critic result.

Conceptually, `release_ok` is true only when:

- `support_status` is `SUPPORTED`;
- `evidence_sufficiency` is `SUFFICIENT`;
- no unresolved conflicting evidence is present.

The exact critic schema and release predicate must be frozen before the
scientific benchmark.

The same release predicate must be used by B1 and G1. The recovery policy must
not redefine what counts as an acceptable supported answer.

The critic must not have access to benchmark reference answers or reference
evidence.

## 10. Separation of assessment and control

The critic answers:

> What is the evidential state of the current answer?

The recovery policy answers:

> Given that evidential state and the applicable control rules, what happens
> next?

This separation is a methodological requirement.

It prevents the G1 treatment from being hidden inside a different critic prompt
or critic implementation.

## 11. Recovery-policy interface

Both conditions use the same policy interface.

Conceptually, the policy receives:

- critic result;
- recovery iteration;
- runtime resource snapshot;
- applicable hard limits.

It returns one action:

- `ACCEPT`;
- `RERETRIEVE_REVISE`;
- `ABSTAIN`;
- `RESOURCE_STOP`.

It also returns a structured reason code suitable for logging.

The policy must not receive benchmark gold information.

## 12. B1 fixed recovery policy

B1 uses a fixed, pre-specified policy.

For the first critic result, the working rule is:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### Otherwise

If the common hard execution guard permits the configured recovery cycle:

Return:

`RERETRIEVE_REVISE`

B1 does not select recovery according to:

- remaining token percentage;
- estimated recovery value;
- remaining model-call allowance beyond hard feasibility;
- remaining retrieval allowance beyond hard feasibility;
- resource-efficiency optimization.

B1 therefore follows the same bounded recovery response for every non-supported
initial draft.

After the single recovery cycle, B1 uses the shared post-recovery finalization
rule.

## 13. G1 evidence- and resource-aware recovery policy

G1 uses the same critic result and shared resource accounting.

For the first critic result:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### If `release_ok` is false and the evidence state satisfies the frozen
insufficient-evidence rule

Return:

`ABSTAIN`

only when the pre-specified G1 policy determines that the current evidence gap
does not justify another bounded retrieval/revision action.

`INSUFFICIENT` evidence does not automatically imply abstention. A gap may still
be treated as recoverable under the frozen G1 policy.

### If recovery is evidence-justified and the frozen recovery resource reserve
is available

Return:

`RERETRIEVE_REVISE`

### If recovery would otherwise be justified but the required resource reserve
is not available

Return:

`RESOURCE_STOP`

The exact evidence criterion, resource reserve, and decision thresholds remain
open and must be specified before G1 is frozen.

They may be selected from engineering evidence and prior literature.

They must not be selected from primary benchmark outcomes.

## 14. Shared hard execution guard

A common hard execution guard applies to B1 and G1.

Its purpose is operational safety and experimental comparability, not the
scientific treatment.

The hard guard prevents a node from starting when doing so would violate a
frozen execution ceiling.

Possible ceilings include:

- maximum model calls;
- maximum retrieval or tool calls;
- maximum retries;
- workflow token limit where enforceable;
- execution timeout.

The same hard ceilings must apply to B1 and G1.

B1 may therefore be stopped by the common hard guard even though its policy is
not resource-adaptive.

This is distinct from G1 proactively using resource state as part of its
recovery decision.

## 15. Recovery implementation

The recovery implementation is shared by B1 and G1.

When `RERETRIEVE_REVISE` is selected:

1. construct a recovery retrieval query from the task, current evidence, and
   critic-identified evidence gap;
2. perform bounded recovery retrieval;
3. combine the permitted evidence according to the frozen context policy;
4. revise the current answer;
5. invoke the same critic again.

Neither condition receives a stronger recovery implementation.

The number of permitted recovery cycles is the same for B1 and G1.

## 16. Shared post-recovery finalization

To keep the treatment narrow, the preferred working design uses the same
post-recovery finalization rule in B1 and G1.

After the final permitted recovery cycle:

### If the shared `release_ok` predicate is true

Return:

`ACCEPT`

### If the shared `release_ok` predicate is false

Return:

`ABSTAIN`

unless the common hard execution guard has already produced a distinct
resource-stopped outcome.

This post-recovery rule is identical for B1 and G1.

This rule is provisional and must be frozen before benchmark execution.

Using a shared post-recovery rule prevents condition differences from being
introduced after both systems have already consumed the same recovery
capability.

## 17. Terminal outcomes

The workflow must distinguish terminal outcomes explicitly.

### Completed answer

- run status: completed, or completed-after-recovery as applicable;
- final answer: present;
- abstained: false.

### Abstention

- final answer: an explicitly defined abstention representation;
- abstained: true;
- must be distinguishable from system failure.

### Resource stop

- run status: resource-stopped;
- must not automatically count as a correct abstention;
- reason for the stop must be logged.

### Tool or workflow failure

- use the applicable failure status;
- preserve the failed run;
- do not silently convert failure to abstention.

## 18. Resource accounting

Resource accounting is shared.

Every model call and retrieval attempt should be recorded using the common
logging infrastructure.

The policy must use the same resource counters that are later reported by the
benchmark.

No hidden condition-specific counters or unlogged recovery calls are allowed.

The runtime resource state is descriptive for B1 except where common hard
limits apply.

It is an explicit control input for G1.

## 19. Required policy logging

Every recovery-policy decision should produce a structured event containing at
least:

- policy identity;
- decision sequence;
- critic iteration;
- evidence status;
- selected action;
- reason code;
- recovery iteration;
- resource snapshot at decision time.

For G1, the event should additionally preserve the resource variables actually
used by the decision rule.

Logging must capture the inputs to the policy without including benchmark gold
information.

## 20. Required workflow events

The implementation should make it possible to reconstruct the execution path.

Candidate events include:

- `plan_completed`;
- `initial_retrieval_completed`;
- `draft_completed`;
- `critic_completed`;
- `policy_decision`;
- `recovery_retrieval_completed`;
- `revision_completed`;
- `post_recovery_critic_completed`;
- `answer_accepted`;
- `abstained`;
- `resource_stopped`.

Exact event names may change during implementation, but the required
information must remain reconstructable.

## 21. Treatment-isolation matrix

| Component | B1 | G1 | Must match? |
| --- | --- | --- | --- |
| Planner | shared | shared | yes |
| Initial retrieval | shared | shared | yes |
| Draft generator | shared | shared | yes |
| Critic | shared | shared | yes |
| Recovery retrieval | shared | shared | yes |
| Revision implementation | shared | shared | yes |
| Maximum recovery cycles | same | same | yes |
| Initial resource limits | same | same | yes |
| Hard execution guard | shared | shared | yes |
| Post-recovery finalization | shared | shared | yes |
| Recovery decision policy | fixed | evidence/resource-aware | no |
| Policy reason codes | condition-specific as needed | condition-specific as needed | no |

The intended scientific treatment is therefore concentrated in the
pre-recovery policy decision.

## 22. Testable implementation invariants

Before real benchmark execution, synthetic tests should demonstrate that:

1. B1 and G1 instantiate the same graph structure;
2. all non-policy nodes are shared;
3. both conditions use the same critic implementation;
4. both conditions use the same recovery implementation;
5. both conditions receive the same initial resource limits;
6. B1 policy does not branch on resource state except common hard feasibility;
7. G1 policy can branch on the frozen evidence and resource inputs;
8. neither policy can access benchmark gold information;
9. only the configured number of recovery cycles can occur;
10. all model and retrieval calls are logged;
11. all policy decisions are reconstructable from recorded events;
12. resource stops remain distinct from abstentions;
13. failed executions are preserved;
14. no benchmark task content is required by workflow unit tests.

## 23. Engineering-test boundary

Before the workflow is frozen, synthetic engineering tasks may be used to test:

- graph routing;
- state transitions;
- critic schema validation;
- policy actions;
- hard-limit behavior;
- recovery-cycle bounds;
- logging;
- error handling.

These tests are not scientific benchmark runs.

UC1 benchmark performance must not be used to tune the policy.

## 24. Decisions still open

This contract intentionally does not yet freeze:

- planner prompt and structured output;
- exact planning granularity;
- critic prompt;
- critic structured-output schema;
- exact evidence sufficiency criterion;
- exact G1 recovery-worthiness criterion;
- exact resource reserve rule;
- maximum model calls;
- maximum retrieval calls;
- retry limits;
- total workflow token ceiling;
- per-call output limit;
- timeout;
- recovery query construction;
- context-merging policy after re-retrieval;
- final abstention text;
- exact workflow event names;
- workflow configuration identifiers.

These decisions must be resolved and frozen before scientific benchmark
execution.

## 25. Implementation sequence

The intended implementation sequence is:

1. define typed shared workflow state;
2. define critic-result contract;
3. define recovery-action and policy protocols;
4. implement common shared nodes;
5. implement B1 fixed policy;
6. implement G1 policy only after its decision rule is pre-specified;
7. assemble one common LangGraph workflow;
8. extend execution logging for policy and stage events;
9. test all routing with synthetic components;
10. run synthetic real-model engineering validation;
11. freeze prompts, policies, resource limits, and workflow configuration;
12. only then permit scientific benchmark execution.

## 26. Current boundary

At this checkpoint:

- B0 engineering validation is complete;
- contribution positioning is recorded;
- algorithmic novelty is not claimed;
- B1 implementation has not started;
- G1 implementation has not started;
- the scientific benchmark has not started.

The next engineering step after review of this contract is to implement the
shared typed state and policy interfaces without yet implementing the full
agentic workflow.
