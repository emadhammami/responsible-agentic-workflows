# Frozen Study A sources: redistribution and identity

The original retrieval corpus has **56 logical documents**: 30 in UC1, 17 in
UC2 and nine in UC3. This release includes **41 unchanged documents in 49
physical files**. The remaining 15 documents have official source links and
recorded hashes; their complete original files require further rights
confirmation or permission. The released subset is not a replacement benchmark
corpus and must not be presented as the complete 56-document retrieval input.

Redistribution decisions use the publisher terms and copyright notices
applicable to each frozen file. Public availability does not itself establish
permission to redistribute. Earlier rights notes in the frozen source catalog
remain historical provenance; this directory records the current
redistribution assessment without editing those notes.

- [DOCUMENT_RIGHTS.tsv](DOCUMENT_RIGHTS.tsv) identifies every document, publisher,
  original location, official link, recorded hash and individual decision.
- [SOURCE_FILES.tsv](SOURCE_FILES.tsv) lists all 64 expected physical files,
  individual byte hashes and release locations.
- [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md) records licence bases,
  attribution and the reasons for retaining link-only documents.
- [CORPUS_IDENTITY.json](CORPUS_IDENTITY.json) binds membership to the original
  scope/acquisition manifests and published frozen row-to-chunk identities.
- [RETRIEVAL_RECONSTRUCTION.md](RETRIEVAL_RECONSTRUCTION.md) explains what source
  release enables and which artifacts still prevent complete retrieval replay.

Original filenames and file bytes are preserved under `UC1/raw/`, `UC2/raw/`
and `UC3/raw/`. DOC051 is a single logical document acquired as nine HTML
components under `UC2/raw/UC2-C11_freeports_technical_handbook/`; do not flatten,
merge, rename or replace these components. All other documents are single files.
The DOC051 recorded bundle identity is preserved; individual hashes are checked
against the frozen acquisition metadata. Its historical aggregate-hash encoding
was not recovered, so the aggregate is not claimed to have been recomputed.

## Verify supplied files

From the repository root, using Python's standard library:

```bash
python3 -B research-artifacts/study-a/source-documents/verify_corpus.py \
  --research-root .
```

PASS means the supplied partial corpus matches its declared membership and
hashes; the report explicitly lists absent originals. For a complete authorized
copy in a separate directory containing `UC1/raw`, `UC2/raw` and `UC3/raw`:

```bash
python3 -B research-artifacts/study-a/source-documents/verify_corpus.py \
  --source-root /path/to/complete-source-tree --require-full --research-root .
```

Current web downloads may differ from the frozen snapshots. Keep the recorded
hashes unchanged; a changed source is a new replication input. Do not overwrite
original research evidence to make a download match.

HTML files are original acquired snapshots. Their external styles, scripts,
logos, thumbnails and other image assets are not mirrored. These files support
text extraction and provenance; offline visual rendering may be incomplete.
Publisher credits and public institutional contact details in original files
are source content, not records of this study's participants or experts.
