# UC1 Embedding Materialization Hash Verification Failure

Date: 2026-09-12

## Purpose

This record preserves the first failure observed after full UC1 embedding
materialization and the subsequent root-cause diagnostic.

This is engineering evidence only. It is not a benchmark result.

## Repository state

- Branch: `research/retrieval-foundation`
- Git base commit: `24d82b5`
- Retrieval configuration:
  `UC1-QWEN3-EMBED4B-EXACT-COSINE-v0.1`
- Retrieval configuration status: `working`
- Embedding model:
  `qwen3-embedding:4b-q4_K_M`
- Batch size: `32`

## Full materialization execution

The full UC1 embedding materialization completed before the verification
failure occurred.

Observed:

- Chunks: `2853`
- Unique chunk IDs: `2853`
- Documents: `30`
- Embedding dimensions: `2560`
- Total batches: `90`
- Materialization time: `267.174 seconds`
- Materialization time: `4.453 minutes`

All 2853 chunks were embedded before the first failure.

## First failure

The first failure occurred during post-materialization provenance verification:

`FIRST_FAILURE=SHA_MISMATCH_source_chunk_artifacts_sha256`

Recorded source chunk artifact hash:

`f66b7c9745e1def0282939e65fb63d374623537beff762c97fe405073787f283`

Hash independently calculated by the failed verifier:

`ce308f891d5b21bca80ce5b004f2fa0e6843bc2db951c057bcbd33c0821840ba`

No re-embedding was performed after this failure.

## Follow-up diagnostic

The existing materialized artifact was inspected without modifying it.

### Embedding matrix

- Shape: `(2853, 2560)`
- Dtype: `float32`
- Minimum L2 norm: `0.999998629`
- Maximum L2 norm: `1.000001311`
- Mean L2 norm: `1.000000000`

Recorded embedding matrix SHA256:

`b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0`

Actual embedding matrix SHA256:

`b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0`

Result:

`EMBEDDING_MATRIX_INTEGRITY=PASS`

### Chunk-ID binding

Recorded chunk-ID artifact SHA256:

`f62aa825797144a3ebff4a7fee0cd08e3cf86525a8bbfc7c4d041ea3bc1c3673`

Actual chunk-ID artifact SHA256:

`f62aa825797144a3ebff4a7fee0cd08e3cf86525a8bbfc7c4d041ea3bc1c3673`

Chunk ordering and uniqueness also matched the source chunk artifacts.

Result:

`CHUNK_ID_BINDING=PASS`

### Configuration and source index

The retrieval configuration SHA256 and source chunk index SHA256 matched their
recorded metadata values.

Result:

`CONFIG_AND_INDEX_BINDING=PASS`

## Root cause

The source chunk artifact aggregate hash produced by the committed materializer
was:

`f66b7c9745e1def0282939e65fb63d374623537beff762c97fe405073787f283`

This exactly matched the value recorded in the generated metadata.

The independently written verifier produced:

`ce308f891d5b21bca80ce5b004f2fa0e6843bc2db951c057bcbd33c0821840ba`

Inspection of the committed materializer showed that its aggregate hashing
function used the byte literals:

- `b"\\0"`
- `b"\\n"`

These represent literal backslash sequences.

The failed verifier instead used:

- an actual NUL byte;
- an actual newline byte.

The diagnostic therefore established:

`ROOT_CAUSE=HASH_DELIMITER_CONVENTION_MISMATCH`

## Impact assessment

The failure affected only the convention used to calculate the aggregate source
chunk artifact hash.

The following were not found to be corrupted:

- embedding matrix;
- embedding matrix SHA256;
- chunk-ID ordering;
- chunk-ID SHA256;
- retrieval configuration binding;
- chunk index binding.

The existing 2853-vector embedding artifact is therefore reusable.

Results:

- `EMBEDDING_CONTENT_FAILURE=NO`
- `REEMBEDDING_REQUIRED=NO`
- `EXISTING_EMBEDDING_ARTIFACT_REUSABLE=YES`

## Next engineering action

The hash implementation should be corrected to use an explicitly defined
canonical delimiter convention.

The existing embedding matrix must be preserved. Only the provenance hash and
corresponding local metadata should be recalculated after the implementation
fix.

## Research safeguards

- No benchmark question was used.
- No benchmark gold evidence was used.
- No retrieval accuracy was evaluated.
- No benchmark run was executed.
- No corpus freeze occurred.
- No chunking freeze occurred.
- No retrieval configuration freeze occurred.
- No re-embedding occurred after the failure.
