"""Create the text-free release projection from an authorized original archive.

Reads only local files. Does not execute workflows, retrieval or evaluation.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project(original, filename, digest):
    record = copy.deepcopy(original)
    for key in ('started_at', 'finished_at'):
        record.pop(key)
    record['final_output'].pop('answer')
    for call in record['retrieval']['calls']:
        call.pop('query')
    for event in record['events']:
        event.pop('timestamp')
    final_digest = hashlib.sha256(json.dumps(
        original['final_output'], sort_keys=True, separators=(',', ':')
    ).encode()).hexdigest()
    return dict(source_file=filename, source_sha256=digest,
                final_output_sha256=final_digest, record=record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    package = Path(__file__).resolve().parent
    inventory = dict((name, digest) for digest, name in (
        line.split() for line in (package/'provenance/RAW_RECORD_SHA256SUMS.txt').read_text().splitlines()
    ))
    order = json.loads((package/'provenance/primary_execution_order_v1.json').read_text())['runs']
    assert len(inventory) == len(order) == 270
    assert {p.name for p in (args.archive/'run_records').glob('*.json')} == set(inventory)
    lines = []
    for entry in order:
        name = entry['output_relative_path']
        source = args.archive/'run_records'/name
        assert sha(source) == inventory[name], name
        record = json.loads(source.read_text())
        for key in ('run_id', 'task_id', 'condition', 'experiment_id'):
            assert record[key] == entry[key]
        lines.append(json.dumps(project(record, name, inventory[name]), sort_keys=True)+'\n')
    # Exclusive creation prevents accidental replacement of any existing record.
    with args.output.open('x') as stream:
        stream.writelines(lines)
    print('Projected 270 records; original inputs unchanged.')


if __name__ == '__main__':
    main()
