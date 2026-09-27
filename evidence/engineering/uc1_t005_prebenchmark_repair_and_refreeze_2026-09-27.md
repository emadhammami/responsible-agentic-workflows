# UC1 T005 Pre-Benchmark Repair and Re-Freeze

Date: 2026-09-27

## Trigger

DEFECT_DISCOVERED_DURING=primary_30_task_prebenchmark_structural_validation
DEFECT_TYPE=within_document_source_redundancy
DEFECT_CONFIRMED=YES

The original T005 failed the strict within-document reasoning criterion because
DOC010-P0155-C001 alone supplied the complete frozen reference answer.

## Researcher approvals

APPROVAL_1=APPROVE UC1 T005-R1 PRE-BENCHMARK REPAIR
APPROVAL_2=APPROVE UC1 T005-R1 SOURCE-COMPLETE REFERENCE ANSWER

## Repair

TASK_ID=T005
TASK_TYPE=within_document_reasoning
REPAIR_APPLIED=YES

SOURCE_LOCATION_1=DOC010-P0154-C001
SOURCE_LOCATION_2=DOC010-P0162-C001
MULTI_LOCATION_SYNTHESIS_REQUIRED=YES

P0154 supplies the Government forest-management actions requested by the task.
P0162 supplies the later trajectory-level assessment of scaling up mitigation.
Neither location alone supplies the complete approved answer.

The canonical PDF extraction is layout-preserving and the page contains two
columns. This can interleave words from adjacent columns; source verification
therefore used proposition-level inspection rather than requiring every phrase
to remain contiguous in extracted text.

## Historical binding

OLD_T005_SHA256=f2fb453ff006208b4b8384f78ece3f63e09c4e8ba48c0533d2ea4997e3885c23
OLD_MANIFEST_SHA256=ba8e6c564d7d7c673ddbcc531bf08bb532d56e7860fd132878e61959902a90b9
OLD_FROZEN_TASK_SET_SHA256=28828661090b42ed452127d624312ffc47536bcbd7124a8fecac8271f8c47efb

FULL_UC1_AUDIT_SHA256=076b4dc84ccdf0aef3c91888deedbc86d47f3434401d026630462f9157070c0c
REPAIR_PROPOSAL_SHA256=a035894268c3e145eb8a8bf44757b61821d991238c5c15891c50d27af6b9d0fe

## Re-freeze binding

NEW_T005_SHA256=91e3db7d666429ea576c3b725816218fe922c900c49d361bdc6231b9c8de5836
NEW_FROZEN_TASK_SET_SHA256=7f442f3417655c5508de37de2988fb1e7ba8d6d03e6b1b47e6d836ce7d1cc755
NEW_MANIFEST_SHA256=0674b63db0ca7fa298598b2d3fd69fcad91aa8295299ec3c61e26d4b950785c3

FROZEN_TASK_SET_HASH_METHOD=sha256_of_canonical_json_sorted_filename_to_file_sha256_map

The v0.1 aggregate hash and per-task identity remain preserved in Git history
and above. The historical aggregate-hash construction was not documented, so
it was not guessed. The v0.2 freeze introduces the explicit deterministic
method stated above.

## Experimental integrity

BENCHMARK_STARTED=NO
BENCHMARK_RESULT_USED=NO
RESULT_DRIVEN_REVISION=NO
RANKED_RETRIEVAL_USED_FOR_REPAIR=NO
B0_B1_G1_OUTPUT_USED=NO
UC1_CORPUS_CHANGED=NO
UC1_RETRIEVAL_CHANGED=NO
TASK_TYPE_ALLOCATION_CHANGED=NO
