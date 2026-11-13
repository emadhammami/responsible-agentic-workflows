"""Verify frozen source membership and file identities without model execution.

Default verification accepts the explicitly partial public corpus. --require-full
requires all 56 logical documents (64 exact physical files) in a separate tree.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path


def read_tsv(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path,
                        help='Root containing UC1/raw, UC2/raw and UC3/raw.')
    parser.add_argument('--require-full', action='store_true')
    parser.add_argument('--research-root', type=Path,
                        help='Optional research checkout for comparison with original scope/acquisition manifests.')
    args = parser.parse_args()
    package = Path(__file__).resolve().parent
    source_root = args.source_root or package
    identity = json.loads((package/'CORPUS_IDENTITY.json').read_text())
    docs = read_tsv(package/'DOCUMENT_RIGHTS.tsv')
    files = read_tsv(package/'SOURCE_FILES.tsv')
    assert len(docs) == 56 and len(files) == 64
    assert len({r['document_id'] for r in docs}) == 56
    assert len({r['expected_relative_path'] for r in files}) == 64
    active = identity['active_documents']
    for uc, count in [('UC1',30),('UC2',17),('UC3',9)]:
        declared = {r['document_id'] for r in docs if r['use_case_id']==uc}
        assert len(declared) == count and declared == set(active[uc])
        ids = json.loads((package.parent/f'retrieval/{uc}/chunk_ids.json').read_text())['chunk_ids']
        assert {c.split('-')[0] for c in ids} == declared
    expected_ids = {r['document_id'] for r in files}
    assert expected_ids == {r['document_id'] for r in docs}
    available, missing, failures = [], [], []
    for row in files:
        file = source_root/row['expected_relative_path']
        if not file.is_file():
            missing.append(row['expected_relative_path'])
            if row['decision']=='PUBLISH ORIGINAL' or args.require_full:
                failures.append('Required source missing: '+row['expected_relative_path'])
        elif sha(file)!=row['sha256']:
            failures.append('Source digest mismatch: '+row['expected_relative_path'])
        else:
            available.append(row['document_id'])
    # Reject extra corpus files: missing rights-held files are explicit, while
    # newly invented/replaced documents must never become benchmark members.
    actual = {str(f.relative_to(source_root)) for uc in active
              for f in (source_root/uc/'raw').rglob('*') if f.is_file()}
    expected = {r['expected_relative_path'] for r in files}
    assert actual <= expected, 'Unexpected source files: '+repr(sorted(actual-expected))
    if source_root.resolve()==package.resolve():
        assert actual == {r['expected_relative_path'] for r in files if r['decision']=='PUBLISH ORIGINAL'}
    if args.research_root:
        research = args.research_root
        assert sha(research/'corpus/manifest.json')==identity['corpus_manifest_sha256']
        for uc in active:
            scope_path=research/f'corpus/use_cases/{uc}/benchmark_scope.json'
            assert sha(scope_path)==identity['scope_sha256'][uc]
            assert set(json.loads(scope_path.read_text())['benchmark_active_document_ids'])==set(active[uc])
        metadata_path=research/'corpus/use_cases/UC2/acquisition_http_metadata.json'
        assert sha(metadata_path)==identity['uc2_acquisition_metadata_sha256']
        acquired=json.loads(metadata_path.read_text())['UC2-C11']
        bundle=[r for r in files if r['document_id']=='DOC051']
        assert len(acquired)==len(bundle)==9
        assert {x['file']:x['sha256'] for x in acquired} == {
            str(Path(x['expected_relative_path']).relative_to('UC2/raw')):x['sha256'] for x in bundle}
    report=dict(status='FAIL' if failures else 'PASS',logical_documents_in_benchmark=56,
                physical_files_in_benchmark=64,verified_available_logical_documents=len(set(available)),
                verified_available_physical_files=len(available),missing_physical_files=missing,
                full_corpus_available=not missing,failures=failures,
                original_scope_checked=bool(args.research_root),
                doc051='Nine component identities checked. Historical aggregate hash retained; its original encoding was not recovered.',
                scope='Membership and exact byte identity, not semantic evaluation or regenerated retrieval.')
    print(json.dumps(report,indent=2))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
