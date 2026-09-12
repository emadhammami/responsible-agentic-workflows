# Targeted Literature and Novelty Review

**Date:** 2026-09-12
**Status:** Working review
**Novelty conclusion:** Algorithmic novelty not established
**Benchmark started:** No

## 1. Purpose

This review tests the provisional technical contribution against the closest
prior work before B1 and G1 are implemented.

The goal is not to maximize a novelty claim. The goal is to identify what can
be claimed defensibly and to prevent the benchmark design from being built
around a contribution that is already substantially covered by prior work.

The review focuses on five dimensions:

- evidence sufficiency;
- adaptive retrieval and recovery;
- selective verification;
- explicit resource or budget awareness;
- stopping, commitment, and abstention.

## 2. Closest prior work

| Work | Evidence state | Adaptive recovery | Explicit resource state | Selective stop / verify | Main overlap |
| --- | --- | --- | --- | --- | --- |
| FLARE | indirect uncertainty | active retrieval | no explicit remaining budget | retrieval triggered as needed | adaptive retrieval |
| Self-RAG | reflection over evidence and output | retrieval and reflection | no explicit remaining budget | adaptive retrieval and critique | self-reflective RAG |
| CRAG | retrieval-quality evaluation | corrective retrieval | no explicit remaining budget | corrective action based on evaluator | evidence-triggered recovery |
| Adaptive-RAG | task-complexity signal | chooses retrieval strategy | no explicit remaining budget | strategy routing | adaptive retrieval policy |
| DRAGIN | information need during generation | dynamic retrieval | no explicit remaining budget | retrieval when needed | selective retrieval |
| SURE-RAG | explicit support / refute / insufficient evidence | primarily selective answering | no explicit remaining budget | abstention unless support is established | evidence sufficiency and abstention |
| BATS | task and trajectory state | planning and verification adapt to budget | explicit tool-call and token cost | budget-aware strategy changes | budget-aware agent control |
| BAVT | step-level progress / value | search expansion and pruning | explicit remaining token and tool budgets | value threshold and budget backstop | fine-grained budget-aware agent control |
| SEVRA | serving-visible attempt state | active verification | verification compute is explicitly costed | accept vs verify selectively | selective verification allocation |
| Inference-Time Budget Control for LLM Search Agents | accumulated evidence and search state | retrieval, decomposition, finalization | explicit dual token/tool budget | evidence sufficiency and answer commitment | multi-action evidence- and budget-aware control |
| SLEUTH | structured confirmed facts, hypotheses, open questions | evidence-driven next actions | budget exhaustion is explicitly studied | commitment trigger avoids needless verification | evidence-state commitment |
| EVAR | source-linked evidence and unresolved gaps | hypothesis refinement and validation | instance-specific inference budget | sufficiency-based stopping | evidence validation plus budget control |
| Budget-Aware Active RAG evaluation | retrieval utility | selective retrieval | explicit evidence-usage/cost budget | evaluates retrieval trigger operating points | budget-aware evaluation methodology |
| VP-CONTROL | evidence lineage and execution state | verification-plan selection | explicit verification cost | cost-aware commit gate | cost-aware verification portfolios |

## 3. High-overlap findings

### 3.1 Evidence sufficiency is not novel

SURE-RAG directly formulates evidence sufficiency as a three-way
support/refute/insufficient decision and uses it for selective answering and
abstention.

EVAR also performs explicit evidence validation and uses a sufficiency-based
stopping rule.

The thesis therefore must not claim evidence sufficiency, evidence-gated
answering, or abstention as standalone technical novelties.

### 3.2 Selective verification is not novel

SEVRA treats verification as a serving-time allocation decision and chooses
when an initial answer should be preserved or additional verification should be
performed.

SLEUTH also shows that agents can waste resources by continuing verification
after sufficient evidence has already been obtained.

The thesis therefore must not claim that selectively invoking a verifier is
itself novel.

### 3.3 Remaining-budget-aware control is not novel

BATS adapts planning and verification behavior according to explicit resource
budgets.

BAVT represents remaining token and tool budgets as runtime state and performs
fine-grained step-level budget-aware control.

Inference-Time Budget Control for LLM Search Agents explicitly controls search
under token and tool budgets.

The thesis therefore must not claim that adapting an agent according to
remaining tokens, calls, or tools is itself novel.

### 3.4 Joint evidence and resource control is already substantially covered

The strongest overlap with the provisional ERGR idea comes from three recent
directions.

Inference-Time Budget Control for LLM Search Agents combines accumulated
evidence, remaining token/tool budget, value-of-information estimates, and
choices among retrieval, decomposition, and answer commitment.

EVAR combines source-linked evidence validation, uncertainty or unresolved
gaps, an instance-specific inference budget, and sufficiency-based stopping.

BAVT combines step-level value assessment, evidence-oriented termination,
remaining resource state, and budget-aware action selection.

Consequently, the broad claim that this thesis introduces the first controller
to combine evidence state and resource state is not defensible.

## 4. Assessment of the current ERGR draft

The current working mechanism, Evidence- and Resource-Gated Recovery (ERGR),
contains useful engineering ideas, but its broad algorithmic framing has high
novelty risk.

The following candidate actions are individually well represented in the
literature:

- accept or commit;
- verify;
- retrieve additional information;
- revise;
- abstain;
- stop because further computation is not justified.

Likewise, the signals proposed for ERGR have substantial precedent:

- evidence sufficiency;
- uncertainty;
- verification state;
- remaining tokens;
- remaining tool or retrieval calls;
- estimated usefulness of further computation.

ERGR should therefore not currently be presented as a novel algorithm.

## 5. Defensible thesis positioning

The strongest defensible contribution at the current stage is a controlled
empirical systems study rather than a first-of-kind controller claim.

The technical contribution can consist of:

1. a pre-specified, auditable guardrail policy for document-based agentic RAG;
2. a matched B1-vs-G1 design in which the core agentic capabilities are held
   constant and the guardrail policy is the principal treatment;
3. measurement of correctness, grounding, abstention, failures, tokens, model
   calls, retrieval calls, and latency under the same experimental controls;
4. explicit reliability-resource trade-off analysis rather than accuracy-only
   evaluation;
5. evaluation across multiple real document-based organizational use cases;
6. integration of technical findings with stakeholder perceptions of
   usefulness, trust, risk, control, and adoption.

This positioning remains aligned with the thesis research questions and does
not depend on claiming that the individual guardrail mechanisms are novel.

## 6. Potentially differentiating technical angle

A narrower technical mechanism may still be publishable, but it requires
additional verification against prior work before being claimed as novel.

A candidate direction is a transparent and deterministic recovery policy for
external document retrieval that explicitly separates:

- evidence adequacy;
- expected benefit of another evidence-acquisition or verification action;
- action cost;
- remaining budget;
- safe termination or abstention.

The important distinction would need to be stronger than simply combining
evidence and budget signals, because recent work already does that.

Any stronger mechanism must be specified only after its exact difference from
Inference-Time Budget Control, EVAR, BAVT, SLEUTH, SURE-RAG, and SEVRA is
documented.

## 7. Recommended scientific claim

The current recommended claim is empirical:

> This study evaluates whether a pre-specified evidence- and resource-aware
> guardrail policy improves the reliability-resource trade-off of an otherwise
> matched agentic workflow in document-based organizational knowledge work.

This statement does not claim invention of evidence sufficiency, adaptive
retrieval, selective verification, abstention, or budget-aware agent control.

The term "proposed guardrail policy" is appropriate.

The terms "novel controller", "first", and "new budget-aware verification
method" are not currently supported.

## 8. Implications for B1 and G1

B1 and G1 should not be implemented until the treatment is specified more
precisely.

B1 should provide the same core capabilities available to G1, including
planning, retrieval, draft generation, verification capability, and bounded
recovery capability.

The scientific treatment should be the policy governing when those capabilities
are invoked, subject to the same overall experimental controls.

G1 must not simply receive more calls, more retrieval opportunities, or a
larger token budget than B1. Any resource difference produced by the policy
must be an observed outcome rather than an unfair initial allocation.

## 9. Evaluation implications

Recent budget-aware RAG work shows that single operating points can be
misleading.

The benchmark should therefore report both quality and realized resource use.

Relevant analyses include:

- reliability at comparable realized cost;
- cost at comparable reliability;
- verification trigger rate;
- retrieval or recovery trigger rate;
- harmful intervention rate;
- abstention rate;
- incorrect abstention rate;
- resource-stop rate;
- realized token and call consumption;
- latency;
- Pareto-style quality-resource frontiers where supported by the data.

The analysis should distinguish an intervention that repairs a failure from one
that unnecessarily changes an already correct answer.

## 10. Closest references requiring direct comparison

The final related-work section should directly compare the thesis against at
least the following:

- Jiang et al., Active Retrieval Augmented Generation / FLARE.
- Asai et al., Self-RAG.
- Yan et al., Corrective Retrieval Augmented Generation.
- Jeong et al., Adaptive-RAG.
- Su et al., DRAGIN.
- Chen, Zaharia, and Zou, FrugalGPT.
- Liu et al., Budget-Aware Tool-Use Enables Effective Agent Scaling (BATS),
  arXiv:2511.17006.
- Li et al., Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM
  Agents (BAVT), arXiv:2603.12634.
- Qiu, Han, and Huang, SURE-RAG, arXiv:2605.03534.
- Fang et al., Inference-Time Budget Control for LLM Search Agents,
  arXiv:2605.05701.
- Dip, Zhou, and Zhang, Think Again or Think Longer? Selective Verification for
  Budget-Aware Reasoning (SEVRA), arXiv:2606.19808.
- Liu, Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning
  in Language Agents (SLEUTH), arXiv:2607.12267.
- Qian et al., When Should Active RAG Retrieve? A Budget-Aware Evaluation of
  Utility, Calibration, and Cost, arXiv:2607.24010.
- Liu, Ji, and Ping, EVAR: Evidence-Validated Hypothesis Admission for
  Budget-Aware Narrative Reasoning, arXiv:2608.29835.
- Zheng et al., Engineering Reliable Commit Gates for Agentic AI:
  Cost-Aware Verification Portfolios under Common-Mode Data Failures,
  arXiv:2609.10969.

## 11. Novelty decision at this checkpoint

**Algorithmic novelty of ERGR: not established.**

**Risk of broad novelty claim: high.**

**Controlled empirical contribution: defensible.**

**Potential for a narrower technical contribution: open, pending a precise
mechanism-level distinction from the closest prior work.**

No B1 or G1 implementation should begin until `docs/proposed_contribution.md`
is revised to reflect this conclusion and the exact B1/G1 treatment is
pre-specified.

## 12. Research integrity rule

The mechanism may be refined because of this pre-benchmark literature review.

It must not later be refined because benchmark results are favorable or
unfavorable.

Once the treatment and hypotheses are frozen, performance-driven redesign is
outside the primary confirmatory comparison and must be reported separately.
