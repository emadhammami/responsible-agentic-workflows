# UC1 Embedding Materialization Hash Repair

Date: 2026-09-12

## Purpose

This record documents the correction of the source chunk artifact aggregate
hash convention after the full UC1 embedding materialization.

This is engineering evidence only. It is not a benchmark result.

## Prior failure

The original materialization completed all 2853 embeddings before post-build
verification detected a mismatch in the aggregate source chunk artifact hash.

The root cause was recorded separately as a hash delimiter convention mismatch.

No embedding content failure was found.

## Canonical hash convention

The aggregate source chunk artifact hash now uses one canonical record per
source artifact:

`UTF-8 filename + NUL byte + ASCII SHA256 + LF byte`

The records are processed in the document order stored in the chunk index.

The corrected canonical UC1 source artifact hash is:

`ce308f891d5b21bca80ce5b004f2fa0e6843bc2db951c057bcbd33c0821840ba`

The previous non-canonical value was:

`f66b7c9745e1def0282939e65fb63d374623537beff762c97fe405073787f283`

## Regression protection

A regression test was added to verify the exact byte-level delimiter convention.

After the fix:

- targeted embedding materialization tests: `7 passed`;
- full repository tests: `128 passed`;
- Ruff: passed;
- Git diff check: passed.

## Existing embedding artifact preservation

The existing full-corpus embedding artifact was preserved.

Embedding matrix SHA256 before and after the repair:

`b110906c30f7f0f3ffcb8902cdf4429abe4df7ddf7bf734b2bfd7755bf7d52c0`

Chunk-ID artifact SHA256 before and after the repair:

`f62aa825797144a3ebff4a7fee0cd08e3cf86525a8bbfc7c4d041ea3bc1c3673`

The embedding matrix therefore remained unchanged.

The chunk-ID artifact also remained unchanged.

No text was resubmitted to the embedding model and no re-embedding occurred.

## Local metadata repair

Only the ignored local `metadata.json` provenance record was updated to contain
the canonical source artifact hash.

The repaired metadata SHA256 is:

`2e7be2db424baf7cc17e807d5a478f96d4fb7a0cb06e0296782629ed29b1f0dc`

The materialized artifact remains in `working` status.

## Result

- `CANONICAL_HASH_FIX=PASS`
- `EMBEDDING_MATRIX_PRESERVED=YES`
- `CHUNK_IDS_PRESERVED=YES`
- `LOCAL_METADATA_REPAIRED=YES`
- `REEMBEDDING_PERFORMED=NO`
- `MODEL_ACCEPTANCE_DECISION=DEFERRED`

## Research safeguards

- No benchmark question was used.
- No benchmark gold evidence was used.
- No retrieval accuracy was evaluated.
- No benchmark run was executed.
- No corpus freeze occurred.
- No chunking freeze occurred.
- No retrieval configuration freeze occurred.
