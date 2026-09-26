# UC1 T008 Pre-Benchmark Defect Diagnosis and Repair-Proposal Record

Date: 2026-09-27

## Outcome: alleged redundancy not confirmed

CURRENT_T008_CROSS_DOCUMENT_VALID=YES
DEFECT_CONFIRMED=NO
REPAIR_CANDIDATES_READY=0

The earlier T4A finding that DOC001 alone provides a complete current T008 answer was too strong. DOC001 supplies most of the ambition-to-action account, but not the explicit commitment that **at least one third of protected areas** should be strictly protected. That substantive protection-ambition proposition is in the frozen reference answer and is supported by DOC003. DOC001 separately supplies the published Forest Strategy implementation provisions, notably avoiding deterioration pending application of the protection regime. Thus neither document alone supplies the full currently approved answer requirement. In accordance with the diagnosis gate, no repair candidates are proposed.

This conclusion evaluates the existing question together with its frozen reference answer; it does not invent a new answer requirement. The question names both strategies and asks about the protection ambition, making the proportional commitment relevant. However, its broad wording does not expressly enumerate the quantitative qualifiers. A shorter DOC001-only ambition-to-action account could be defensible under a looser reading of the question. That residual adjudication risk should be made visible to the researcher; it is not proof that the current full gold answer is obtainable from DOC001 alone. No wording or scoring changes have been applied.

## Repository and historical identity

BRANCH=research/benchmark-task-construction-uc2-uc3
HEAD=f25d11d9fae3eb2a60dcf15900cc4c18ba3dc615
INITIAL_WORKTREE_CLEAN=YES
INITIAL_STAGED_COUNT=0
INITIAL_UNTRACKED_COUNT=0
ORIGINAL_UC1_FREEZE_COMMIT=9b6b9c66a8555ab44346d3860c0a6e67896f507a
ORIGINAL_UC1_HUMAN_VERIFICATION_COMMIT=b548c4371b42c4cd6299d4e46c375884dc1b40c6
ORIGINAL_UC1_DRAFT_COMMIT=b684faaed75c99cfb52658587d79096ffe714cea
T008_SHA256=8ff3a00c053afb66e1b060d2a52faf65b4125fdff1b5a1d5e9d110b7a1627cb9
UC1_FREEZE_MANIFEST_SHA256=ba8e6c564d7d7c673ddbcc531bf08bb532d56e7860fd132878e61959902a90b9
CURRENT_T008_AND_MANIFEST_EQUAL_ORIGINAL_FREEZE_BLOBS=YES

The current T008 and UC1 manifest are byte-identical to their blobs in the original UC1 freeze commit, which is an ancestor of the guarded HEAD. The 2026-09-12 human-review record changed the gold wording from requiring strict protection to calling for strict protection to preserve the Strategy’s legal force; it records no task-type or evidence change. The historical freeze record permits documented, human-reviewed pre-benchmark amendments for genuine defects. No amendment is applied here.

Historical records retain their original dates and scope. Their older UC2/UC3 status statements are not rewritten or treated as current global status. BENCHMARK_STARTED=NO is the current researcher-specified pre-benchmark boundary, not a field invented in the original UC1 manifest.

## Exact frozen T008 record

```json
{
  "schema_version": "0.1",
  "task_id": "T008",
  "question": "How does the New EU Forest Strategy for 2030 translate the EU Biodiversity Strategy's protection ambition for primary and old-growth forests into forest-policy actions?",
  "task_type": "cross_document_reasoning",
  "required_documents": [
    "DOC001",
    "DOC003"
  ],
  "reference_answer": "The Biodiversity Strategy calls for at least 30% of EU land to be protected and for at least one third of protected areas, representing 10% of EU land, to be strictly protected, including all remaining primary and old-growth forests. The Forest Strategy carries this ambition into forest policy by calling for strict protection of primary and old-growth forests and by calling for their definition, mapping, monitoring, and protection regime, together with guidance and implementation measures intended to prevent deterioration and strengthen forest protection and restoration.",
  "reference_evidence": [
    {
      "document_id": "DOC003",
      "page": 5,
      "section": null,
      "chunk_id": "DOC003-P0005-C001"
    },
    {
      "document_id": "DOC001",
      "page": 12,
      "section": null,
      "chunk_id": "DOC001-P0012-C001"
    },
    {
      "document_id": "DOC001",
      "page": 12,
      "section": null,
      "chunk_id": "DOC001-P0012-C002"
    },
    {
      "document_id": "DOC001",
      "page": 19,
      "section": null,
      "chunk_id": "DOC001-P0019-C002"
    }
  ],
  "difficulty": "high",
  "notes": "Benchmark task requiring synthesis across the Biodiversity Strategy and Forest Strategy. Human verified on 2026-09-12 and frozen on 2026-09-12 after final validation.",
  "validation_status": "frozen"
}
```

CURRENT_T008_QUESTION=How does the New EU Forest Strategy for 2030 translate the EU Biodiversity Strategy's protection ambition for primary and old-growth forests into forest-policy actions?
CURRENT_T008_TYPE=cross_document_reasoning
CURRENT_T008_REQUIRED_DOCUMENTS=["DOC001", "DOC003"]


## Direct-source method and identity

Both canonical chunk files were parsed completely, preserving native document/page/chunk identity. All current reference-evidence bindings were checked for existence and page identity. Relevant protection passages were inspected directly, including the complete currently bound chunks and contextual passages on the announced Forest Strategy and restoration. A deterministic, unranked scan across all 95 chunks checked proportional commitments, numerical protection targets and primary/old-growth terminology; it was used to locate passages for inspection, never to score or rank evidence. No diagnostic or runtime outputs were inspected.

CANONICAL_SOURCE=corpus/use_cases/UC1/processed/chunks/DOC001.chunks.json
CANONICAL_CHUNK_FILE_SHA256=ce006c22d36843643cf6e001caa48c7669af141ae23fe472da2016b33821bb42
CHUNKS_ENUMERATED=54

CANONICAL_SOURCE=corpus/use_cases/UC1/processed/chunks/DOC003.chunks.json
CANONICAL_CHUNK_FILE_SHA256=2001f30f7503e090d0d32790fb155b8504865c3414416d11f264ede21f9d9f03
CHUNKS_ENUMERATED=41

PAGE_METADATA_CONVENTION=canonical PDF page/page_id and section; printed page numbers can differ.
ONE_THIRD_COMMITMENT_LOCATIONS=["DOC003-P0005-C001", "DOC003-P0006-C001"]

## Proposition-by-proposition mapping

Uniqueness is assessed between DOC001 and DOC003 for the complete stated proposition, not merely for individual shared words. Context locations supplement this diagnosis only; no task evidence binding is changed.

### Proposition 1

PROPOSITION=The Biodiversity Strategy calls for at least 30% of EU land to be protected.
DOC001_SUPPORT=DOC001-P0012-C001 explicitly attributes the at-least-30% land target to the Biodiversity Strategy.
DOC003_SUPPORT=DOC003-P0005-C001 states at least 30% of land; DOC003-P0006-C001 repeats the commitment.
UNIQUE_TO_DOC001=NO
UNIQUE_TO_DOC003=NO

### Proposition 2

PROPOSITION=At least one third of protected areas should be strictly protected.
DOC001_SUPPORT=Not stated in DOC001. Its DOC001-P0012-C001 gives at least 30% of EU land protected and 10% of EU land strictly protected, without this proportional commitment.
DOC003_SUPPORT=DOC003-P0005-C001 explicitly states at least one third; DOC003-P0006-C001 repeats it.
UNIQUE_TO_DOC001=NO
UNIQUE_TO_DOC003=YES

### Proposition 3

PROPOSITION=The strict-protection ambition represents 10% of EU land.
DOC001_SUPPORT=DOC001-P0012-C001 explicitly states 10% of EU land under strict legal protection.
DOC003_SUPPORT=DOC003-P0005-C001 explicitly gives 10% of EU land.
UNIQUE_TO_DOC001=NO
UNIQUE_TO_DOC003=NO

### Proposition 4

PROPOSITION=Strict protection includes all remaining primary and old-growth forests.
DOC001_SUPPORT=DOC001-P0012-C001 says all primary and old-growth forests will have to be strictly protected.
DOC003_SUPPORT=DOC003-P0005-C001 and DOC003-P0006-C001 explicitly include all remaining EU primary and old-growth forests.
UNIQUE_TO_DOC001=NO
UNIQUE_TO_DOC003=NO

### Proposition 5

PROPOSITION=The New EU Forest Strategy carries the protection ambition into forest policy through its own call for strict protection.
DOC001_SUPPORT=DOC001-P0012-C001 states the Biodiversity Strategy ambition and the Forest Strategy forest-specific application in the same section.
DOC003_SUPPORT=DOC003-P0005-C001 states the ambition; DOC003-P0010-C001 announces a future dedicated Forest Strategy, but does not establish what the subsequently published Forest Strategy itself calls for.
UNIQUE_TO_DOC001=YES
UNIQUE_TO_DOC003=NO

### Proposition 6

PROPOSITION=Forest-policy actions include definition, mapping and monitoring of primary and old-growth forests.
DOC001_SUPPORT=DOC001-P0012-C001/C002 and DOC001-P0019-C002 explicitly provide these actions.
DOC003_SUPPORT=DOC003-P0005-C001 also explicitly calls for defining, mapping and monitoring these forests.
UNIQUE_TO_DOC001=NO
UNIQUE_TO_DOC003=NO

### Proposition 7

PROPOSITION=The Forest Strategy calls for a common forest definition and strict protection regime, with Member States completing mapping and monitoring.
DOC001_SUPPORT=DOC001-P0012-C002 identifies the common forest definition and strict protection regime, Commission cooperation with Member States and stakeholders, and Member State mapping/monitoring.
DOC003_SUPPORT=DOC003-P0005-C001 has forest mapping/monitoring; DOC003-P0006-C001 has general strict-protection definition and designation guidance. Neither supplies this complete Forest Strategy-specific arrangement.
UNIQUE_TO_DOC001=YES
UNIQUE_TO_DOC003=NO

### Proposition 8

PROPOSITION=Member States should ensure no deterioration of these forests until the protection regime starts to apply.
DOC001_SUPPORT=DOC001-P0012-C002 explicitly states the interim no-deterioration instruction.
DOC003_SUPPORT=No matching forest-specific interim instruction in the relevant DOC003 passages. General habitat no-deterioration ambitions do not establish this Forest Strategy instruction.
UNIQUE_TO_DOC001=YES
UNIQUE_TO_DOC003=NO

### Proposition 9

PROPOSITION=Forest Strategy guidance and implementation measures strengthen forest protection and restoration.
DOC001_SUPPORT=DOC001-P0019-C002 gives forest-specific guidelines on definition/mapping/monitoring/strict protection, biodiversity-friendly afforestation/reforestation and closer-to-nature forestry. Its restoration-instrument list item begins in adjacent DOC001-P0019-C001; DOC001-P0004-C001 explicitly describes strengthening forest protection and restoration.
DOC003_SUPPORT=DOC003-P0006-C001 provides general designation/management guidance and DOC003-P0010-C001 discusses forest health/restoration and a future Forest Strategy. This is contextual overlap, not the published Forest Strategy measures.
UNIQUE_TO_DOC001=YES
UNIQUE_TO_DOC003=NO

## Material necessity and counterfactual completeness

DOC001_CURRENT_COMPLETE_ANSWER=NO
DOC003_CURRENT_COMPLETE_ANSWER=NO
DOC003_MATERIALLY_NECESSARY=YES
CURRENT_T008_CROSS_DOCUMENT_VALID=YES

DOC001 alone: the 30% land target, 10% land strict-protection target, all-primary/old-growth scope, mapping, monitoring, regime, interim protection and guidelines are available. The explicitly proportional at-least-one-third commitment is not. Computing 10/30 gives one third only for the stated baseline percentages; it does not establish a commitment to strictly protect at least one third of the protected area when total protected land exceeds 30%. Substituting arithmetic for the proportional source statement would lose a substantive qualification in the approved answer. This is not a document-title, reference or identity lookup.

DOC003 alone: the proportional ambition and general define/map/monitor/strictly-protect actions are available. Its announcement of a future Forest Strategy does not supply the published Forest Strategy’s common-definition/protection-regime arrangements or the forest-specific no-deterioration instruction pending application. General earlier strategy objectives cannot substitute for the later document’s implementation provisions.

The two-document contribution is therefore asymmetric but non-redundant: DOC003 establishes the proportional protection commitment; DOC001 supplies the specific Forest Strategy implementation account. Heavy overlap is real, but overlap is different from complete substitutability. The earlier T4A diagnosis overlooked this gold qualifier and conflated a sufficient broad summary with a complete answer preserving the approved ambition.

## Source proof: complete currently bound chunks

### DOC003-P0005-C001

DOCUMENT_ID=DOC003
PAGE_OR_SOURCE_UNIT=PDF page 5; DOC003-P0005; Page 5
CHUNK_TEXT_SHA256=abdb5eef77cb533169f54faeeac5be655e72d1e84221d86481299463488afa96

```text
efforts are needed and the EU itself needs to do more and better for nature and build a
truly coherent Trans-European Nature Network.

Enlarging protected areas is also an economic imperative. Studies on marine systems
estimate that every euro invested in marine protected areas would generate a return of at
least €319. Similarly, the Nature Fitness Check20 showed that the benefits of Natura 2000
are valued at between €200-300 billion per year. The investment needs of the network are
expected to support as many as 500,000 additional jobs21.

For the good of our environment and our economy, and to support the EU’s recovery
from the COVID-19 crisis, we need to protect more nature. In this spirit, at least 30% of
the land and 30% of the sea should be protected in the EU. This is a minimum of an
extra 4% for land and 19% for sea areas as compared to today22. The target is fully in line
with what is being proposed23 as part of the post-2020 global biodiversity framework
(see Section 4).

Within this, there should be specific focus on areas of very high biodiversity value or
potential. These are the most vulnerable to climate change and should be granted special
care in the form of strict protection24. Today, only 3% of land and less than 1% of marine
areas are strictly protected in the EU. We need to do better to protect these areas. In this
spirit, at least one third of protected areas – representing 10% of EU land and 10% of
EU sea – should be strictly protected. This is also in line with the proposed global
ambition.

As part of this focus on strict protection, it will be crucial to define, map, monitor and
strictly protect all the EU’s remaining primary and old-growth forests25. It will also
be important to advocate for the same globally and ensure that EU actions do not result in
deforestation in other regions of the world. Primary and old-growth forests are the richest
forest ecosystems that remove carbon from the atmosphere, while storing significant
carbon stocks. Significant areas of other carbon-rich ecosystems, such as peatlands,
grasslands, wetlands, mangroves and seagrass meadows should also be strictly protected,
taking into account projected shifts in vegetation zones.

Member States will be responsible for designating the additional protected and strictly
protected areas26. Designations should either help to complete the Natura 2000 network
or be under national protection schemes. All protected areas will need to have clearly
defined conservation objectives and measures. The Commission, working with Member

19
     Brander et al. (2015), The benefits to people of expanding Marine Protected Areas.
20
     Fitness Check of the EU Nature Legislation (SWD(2016) 472).
21
     Member States’
```

### DOC001-P0012-C001

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012; Page 12
CHUNK_TEXT_SHA256=b2f5ea66f12be368c97ca3affd8a3b082bbf796de171d8cdb646ce736dbd4c12

```text
transition. According to the World Economic Forum, the conservation, restoration and
sustainable management of forests could generate EUR 190 billion in business opportunities and
16 million jobs worldwide by 203039.

In addition, we need robust approaches to risk reduction in the context of significant uncertainty
related to future forests. The onset of climate change means forest change. Europe’s vegetation
zones have started to shift upwards and northwards, triggering the transformation of forest
ecosystems in most places. This means that very few forests will either not be strongly affected
by climate change, or will not require immediate management action to reduce their
vulnerability to climate change.

Forest owners and managers across Europe are already strongly aware of climate change and are
concerned with its impacts. This awareness needs to be increasingly translated into sufficient
and tangible adaptation actions and resilience-enhancing forest management practices. For that,
technical knowledge and information as well as targeted regulatory and financial incentives and
support need to be developed. This Strategy aims to address these issues to support forest
owners and managers in their efforts, scale up best practices and ensure an increase in the
quantity and quality of EU’s forest cover for decades to come.

3.1.       Protecting EU’s last remaining primary and old-growth forests

To leave space for nature to thrive, the EU Biodiversity Strategy for 2030 has proposed an
overall target to protect at least 30% of the EU land area under effective management regime,
out of which 10% of the EU land should be put under strict legal protection. Forest ecosystems
will need to make a contribution to this target.

All primary and old growth forests, in particular, will have to be strictly protected. Their
estimated cover is only around 3% of EU forested land and patches are generally small and
fragmented. Primary and old-growth forests are not only among the richest EU forest
ecosystems, but they store significant carbon stocks and also remove carbon from the
atmosphere, while being of paramount importance for biodiversity and the provision of critical
ecosystem services40.

Yet, there is still an immediate need to map the primary and old-growth forests and
establish their protection regime, including increased efforts to protect the primary forests in
outermost regions and overseas territories of the Union, given their exceptionally high and
unique biodiversity value. To maintain the undisturbed character of strictly protected forests it is
essential to leave the dynamic of the forest cycle in these forests as much as possible to natural
processes, limiting extractive human activities, while finding synergies with sustainable
ecotourism and recreational opportunities.

The Commission is working in cooperation with Member States and stakeholders to agree, by
the end of 2021, on a common definition for primary and
```

### DOC001-P0012-C002

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 12; DOC001-P0012; Page 12
CHUNK_TEXT_SHA256=163894543c1e473bdb940e8aa3b39b31e0f88fbb58fd2e27fcd55f07928b3de1

```text
their exceptionally high and
unique biodiversity value. To maintain the undisturbed character of strictly protected forests it is
essential to leave the dynamic of the forest cycle in these forests as much as possible to natural
processes, limiting extractive human activities, while finding synergies with sustainable
ecotourism and recreational opportunities.

The Commission is working in cooperation with Member States and stakeholders to agree, by
the end of 2021, on a common definition for primary and old-growth forests and the strict
protection regime. Member States should urgently engage in completing the mapping and
monitoring of these forests, and ensuring no deterioration until they start to apply the
protection regime.
39
       https://www.weforum.org/press/2020/08/us-businesses-governments-and-non-profits-join-global-push-
       for-1-trillion-trees/.
40
       Barredo Cano, J.I., Brailescu, C., Teller, A., Sabatini, F.M., Mauri, A. and Janouskova, K., Mapping and
       assessment of primary and old-growth forests in Europe, EUR 30661 EN, Publications Office of the European
       Union, Luxembourg, 2021, ISBN 978-92-76-34229-8, doi:10.2760/13239, JRC124671.
                                                     11
```

### DOC001-P0019-C002

DOCUMENT_ID=DOC001
PAGE_OR_SOURCE_UNIT=PDF page 19; DOC001-P0019; Page 19
CHUNK_TEXT_SHA256=e7f0d778370998b438cbba23114e9c3b09c8bf2fa5be9fe65dd08633285752e1

```text
forest
      ecosystems, by the end of 2021.
   2. Develop guidelines on the definition of primary and old-growth forests, including their
      definition, mapping, monitoring and strict protection, by the end of 2021.
   3. Together with the Member States and in close cooperation with different forest
      stakeholders, identify the additional indicators as well as thresholds or ranges for
      sustainable forest management, and assess how these could best be used, starting on a
      voluntary basis, by the Q1 2023.
   4. Develop guidelines on biodiversity friendly afforestation and reforestation, by Q1 2022.
   5. Develop a definition and adopt guidelines for closer-to-nature-forestry practices, by Q2
      2022, as well as voluntary closer-to-nature forest management certification scheme, by
      Q1 2023.
   6. Provide guidance and promote knowledge exchanges on good practices on climate
      adaptation and resilience, using inter alia the Climate-ADAPT platform.
   7. Supplement the revision of the legislation on forest reproductive material with measures to

50
     https://enrd.ec.europa.eu/.
                                              18
```

## Repair gate and bounded review notes

REPAIR_GATE=STOP_CURRENT_TASK_TYPE_VALID
REPAIR_CANDIDATES_PROPOSED=0
REPAIR_CANDIDATES_READY=0
REPAIR_APPLIED=NO
HUMAN_APPROVAL_REQUIRED=YES

No replacement designs or revised reference answers are authored after this gate. No UC1 distribution changes occur; the historical allocation remains direct 3, within-document 3, cross-document 2, insufficient-evidence 2. The historical task-set plan was inspected without modification.

AMBIGUITY_ASSESSMENT=The proportional ambition is relevant and explicit in the current gold, but not enumerated in the question; a broad shorter answer may omit it. Researcher review should assess that adjudication risk without assuming the document is wholly redundant.
TEMPORAL_SCOPE_ASSESSMENT=The task concerns the frozen strategies’ ambitions and provisions, not realised implementation or current external policy.
REFERENCE_ANSWER_BOUNDEDNESS=The current gold is limited to protection ambition and forest-policy actions; proposed measures must not be described as enacted obligations or realised achievements.
DUPLICATION_ASSESSMENT=Existing T004 overlaps the Forest Strategy protection/management measures. T008 additionally requires the Biodiversity Strategy proportional ambition and its relation to Forest Strategy actions. This overlap should remain visible to the researcher, but no replacement or joint task redesign is authorised by this diagnosis.

## Protected input hashes

benchmark/tasks/UC1/T001.json SHA256=6f6bd0a21c6998bdc953a535dc327f750602ac139ae492f69e43fe90ce5c941a
benchmark/tasks/UC1/T002.json SHA256=70df44f45004610ec0f3882f4382ae7c5851786dea3cad8282e400d1af4a1837
benchmark/tasks/UC1/T003.json SHA256=6ca0a20f8736e9524004deaedbb3c08a3f6fc125bea79a252d85158b87cdcd87
benchmark/tasks/UC1/T004.json SHA256=704fff83f51729448a0d7075daf5b5570d960cb3be07d125353ecf2300e30340
benchmark/tasks/UC1/T005.json SHA256=f2fb453ff006208b4b8384f78ece3f63e09c4e8ba48c0533d2ea4997e3885c23
benchmark/tasks/UC1/T006.json SHA256=aec0964d32042a8107a0d57aab3bd7871b710e58f48c0df6f2b3e301d692e340
benchmark/tasks/UC1/T007.json SHA256=e8f784adfc8f0b24fb6b98ac85d44eb30ab8356fcb01da78e6d50a8fa3c2fa0d
benchmark/tasks/UC1/T008.json SHA256=8ff3a00c053afb66e1b060d2a52faf65b4125fdff1b5a1d5e9d110b7a1627cb9
benchmark/tasks/UC1/T009.json SHA256=a1f7bc496bf1f83b267e3e513b52d8fbf0437fae4f10f3e4d3f7aa896e78612a
benchmark/tasks/UC1/T010.json SHA256=7aa9d9c5ee24678b41ba6361f3c80d39c7cc5a5bd2798cb8417136c0c0cf976b
benchmark/tasks/UC1/freeze_manifest.json SHA256=ba8e6c564d7d7c673ddbcc531bf08bb532d56e7860fd132878e61959902a90b9
benchmark/task_set_plan.json SHA256=137bcef783e124e3410301f1fc89bead7f375b6b8bad94f3a0f0c04c1cce1958
evidence/engineering/uc1_task_human_review_2026-09-12.md SHA256=9c17034676073667f93c209172586b9bb9505953a83120f3fff96cee1914010e
evidence/engineering/uc1_task_freeze_2026-09-12.md SHA256=a7f80e0cbb7a57f53ced596c7a29a234fb5f6c2d0dc3d05e83c964ec5c79bbf2

## Provenance and final validation

DEFECT_DISCOVERED_DURING=combined_30_task_prebenchmark_structural_audit
DEFECT_TYPE=task_type_source_redundancy
DEFECT_TYPE_STATUS=ALLEGED_NOT_CONFIRMED
BENCHMARK_STARTED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
RETRIEVAL_RANKING_USED=NO
EMBEDDINGS_USED=NO
B0_B1_G1_OUTPUT_USED=NO
ORIGINAL_T008_PRESERVED=YES
ORIGINAL_UC1_FREEZE_HISTORY_PRESERVED=YES
REPAIR_APPLIED=NO
HUMAN_APPROVAL_REQUIRED=YES
TASK_JSON_CREATED=NO
COMMIT=NO
PUSH=NO

The defect-type field preserves the allegation’s origin; it does not assert confirmation. The conclusion is DEFECT_CONFIRMED=NO. Only this evidence artifact is created. All protected inputs remain byte-identical; no tracked or staged changes occur. Final untracked scope is exactly this artifact. Git diff --check passes.
