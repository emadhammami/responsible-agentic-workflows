"""Reconstruct released Study A numeric tables and optionally render figures.

Only released telemetry/numeric annotations are inputs. No inference, scoring,
source-document access, expert records, or network requests are performed.
"""
import argparse
import collections
import contextlib
import csv
import hashlib
import importlib.util
import inspect
import io
import json
import math
import os
from pathlib import Path
import random
import statistics
import sys

sys.dont_write_bytecode = True
PACKAGE = Path(__file__).resolve().parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_csv(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def compare_csv(actual, expected):
    left, right = read_csv(actual), read_csv(expected)
    assert len(left) == len(right), expected.name
    for a, b in zip(left, right):
        assert a.keys() == b.keys(), expected.name
        for key in a:
            if a[key] == b[key]:
                continue
            try:
                assert math.isclose(float(a[key]), float(b[key]), rel_tol=1e-12, abs_tol=1e-9)
            except (ValueError, AssertionError):
                raise AssertionError(f'{expected.name}: differing {key}') from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='A new output directory; must not already exist.')
    parser.add_argument('--figures', action='store_true')
    args = parser.parse_args()
    output = args.output.resolve()
    assert output != PACKAGE and not output.exists(), 'Use a new output directory'
    # Integrity verifies the released files, not the truth of measurements.
    for line in (PACKAGE/'SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        assert hashlib.sha256((PACKAGE/name).read_bytes()).hexdigest() == digest, name
    output.mkdir(parents=True)
    os.environ.setdefault('MPLCONFIGDIR', str(output/'matplotlib-cache'))
    os.environ.setdefault('MPLBACKEND', 'Agg')
    import numpy as np
    common = load_module('common', PACKAGE/'originals/resource_v1/common.py')
    common.ROOT = PACKAGE/'provenance'
    common.OUT = output/'execution_figures_v1'
    audit = load_module('audit', PACKAGE/'originals/resource_v1/audit.py')
    # Retain original extraction/accounting/aggregation code after its private
    # input loader. Substitute a public projection loader; never claim its
    # bytes match the original raw record hashes.
    tail = inspect.getsource(audit.load_source).split(' raw=[]; traces={}\n', 1)[1]
    old = "path=ROOT/'run_records'/entry['output_relative_path']; d=json.loads(path.read_text())"
    assert old in tail
    tail = tail.replace(old, "path=Path(entry['output_relative_path']); d=projected[path.name]['record']")
    prefix = '''def public_source():
 freeze=json.loads((ROOT/'primary_benchmark_raw_freeze_manifest.json').read_text())
 order=json.loads((ROOT/'primary_execution_order_v1.json').read_text())['runs']
 metadata=json.loads((ROOT/'task_metadata.json').read_text())
 uc_map={t['task_id']:t['use_case_id'] for t in metadata}
 items=[json.loads(line) for line in (ROOT.parent/'data/execution_telemetry_270.jsonl').read_text().splitlines()]
 projected={item['source_file']:item for item in items}
 actual={name:item['source_sha256'] for name,item in projected.items()}
 inventory={name:digest for digest,name in (line.split() for line in (ROOT/'RAW_RECORD_SHA256SUMS.txt').read_text().splitlines())}
 assert len(items)==len(projected)==len(order)==270 and actual==inventory
 assert {entry['output_relative_path'] for entry in order}==set(projected)
 raw=[]; traces={}
'''
    namespace = dict(audit.__dict__)
    exec(compile(prefix+tail, '<public projection adapter>', 'exec'), namespace)
    audit.load_source = namespace['public_source']
    # Do not regenerate the historical audit text, whose claims depend on the
    # private originals. Tables retain original formulas without that claim.
    audit.audit_document = lambda *unused: None
    with contextlib.redirect_stdout(io.StringIO()):
        audit.main()
    compared = []
    for expected in sorted((PACKAGE/'reference/execution_figures_v1/data').glob('*.csv')):
        compare_csv(common.OUT/'data'/expected.name, expected)
        compared.append(str(expected.relative_to(PACKAGE)))
    definitions = json.loads((common.OUT/'data/metric_definitions.json').read_text())
    assert definitions == json.loads((PACKAGE/'reference/execution_figures_v1/data/metric_definitions.json').read_text())
    raw, groups, traces, freeze = audit.load_source()
    metadata = {t['task_id']: t for t in json.loads((PACKAGE/'provenance/task_metadata.json').read_text())}
    rows = []
    metric_names = ['input_tokens','output_tokens','total_tokens','llm_calls','retrieval_calls']
    for row in raw:
        rows.append(dict(task_id=row['task_id'], condition=row['condition'], repetition=row['repetition'], run_id=row['run_id'],
                         use_case=row['UC'],task_type=metadata[row['task_id']]['task_type'],
                         **{k:row[k] for k in metric_names},seconds=row['end_to_end_ms']/1000,
                         recovered=int(row['status']=='completed_after_recovery'),abstained=row['final_abstention'],
                         selected_action=row['selected_action'] or 'NONE'))
    task_rows = []
    for task in sorted(metadata):
        for condition in common.CONDITIONS:
            rr=[r for r in rows if r['task_id']==task and r['condition']==condition]
            task_rows.append(dict(task_id=task,condition=condition,use_case=rr[0]['use_case'],task_type=rr[0]['task_type'],
                                 **{k:statistics.mean(r[k] for r in rr) for k in metric_names+['seconds']},
                                 recovered=rr[0]['recovered'],abstained=rr[0]['abstained'],selected_action=rr[0]['selected_action']))
    lookup={(r['task_id'],r['condition']):r for r in task_rows}
    differences=[dict(task_id=t,**{k:lookup[t,'G1'][k]-lookup[t,'B1'][k] for k in metric_names+['seconds']}) for t in sorted(metadata)]
    types=['direct_retrieval','within_document_reasoning','cross_document_reasoning','insufficient_evidence']
    joint=[]
    for task_type in types:
        for condition in ['B1','G1']:
            rr=[r for r in task_rows if r['task_type']==task_type and r['condition']==condition]
            for recovered,abstained in [(0,0),(1,0),(1,1),(0,1)]:
                count=sum(r['recovered']==recovered and r['abstained']==abstained for r in rr)
                joint.append(dict(task_type=task_type,condition=condition,recovered=recovered,abstained=abstained,tasks=count,task_denominator=len(rr),runs=count*3,run_denominator=len(rr)*3))
    thesis_out=output/'thesis';thesis_out.mkdir()
    for name,table in [('validated_execution_metrics.csv',sorted(rows,key=lambda r:(r['task_id'],r['condition'],r['repetition']))),('task_resource_means.csv',task_rows),('paired_task_differences.csv',differences),('recovery_abstention_by_type.csv',joint)]:
        target=thesis_out/'data'/name;write_csv(target,table);compare_csv(target,PACKAGE/'reference/thesis/data'/name);compared.append('reference/thesis/data/'+name)
    # Exact already-reported paired bootstrap; this reproduces an existing
    # analysis, not an additional uncertainty design or task selection.
    rng=random.Random(20260912)
    metrics=['total_tokens','llm_calls','retrieval_calls','seconds']
    values=np.array([[r[k] for k in metrics] for r in differences])
    indices=np.array([rng.choices(range(30),k=30) for _ in range(10000)])
    intervals=np.quantile(values[indices].mean(axis=1),[.025,.975],axis=0)
    paired_stats=[dict(metric=k,mean=float(values[:,i].mean()),median=float(np.median(values[:,i])),lower=float(intervals[0,i]),upper=float(intervals[1,i])) for i,k in enumerate(metrics)]
    write_csv(thesis_out/'data/reconstructed_paired_statistics.csv',paired_stats)
    historical = json.loads((PACKAGE/'reference/thesis/validation_report.json').read_text())
    bounds = historical['existing_interval_reproduction']['bounds']
    for i, row in enumerate(paired_stats):
        assert math.isclose(row['lower'], bounds[0][i], abs_tol=1e-12)
        assert math.isclose(row['upper'], bounds[1][i], abs_tol=1e-12)
    # Recompute the LLM annotation matrix from released numeric annotations.
    pairs=read_csv(PACKAGE/'evaluation/paired_judge_scores.csv')
    slots=read_csv(PACKAGE/'evaluation/slot_provenance.csv')
    assert len(pairs)==270 and len(slots)==540
    matrix=np.zeros((3,3),dtype=int);original=np.zeros((3,3),dtype=int)
    slot_lookup={(r['task_id'],r['condition'],int(r['repetition']),r['judge']):r for r in slots}
    for r in pairs:
        keys=(r['task_id'],r['condition'],int(r['repetition']))
        first,second=[slot_lookup[(*keys,j)] for j in ['J1','J2']]
        assert int(first['score'])==int(r['J1_score']) and int(second['score'])==int(r['J2_score'])
        matrix[int(r['J1_score']),int(r['J2_score'])]+=1
        if first['original_valid']==second['original_valid']=='1':original[int(r['J1_score']),int(r['J2_score'])]+=1
    thesis=load_module('generate_benchmark_figures',PACKAGE/'originals/thesis/generate_benchmark_figures.py')
    evaluation=load_module('provisional_agreement_plot',PACKAGE/'adapters/provisional_agreement_plot.py')
    metrics=evaluation.agreement(matrix);original_metrics=evaluation.agreement(original)
    expected=json.loads((PACKAGE/'evaluation/validation_report.public.json').read_text())
    assert matrix.tolist()==expected['matrix']
    for actual,key in [(metrics,'composite_agreement'),(original_metrics,'original_agreement')]:
        for k,v in actual.items():assert math.isclose(v,expected[key][k],rel_tol=1e-12)
    composition=dict(collections.Counter(r['composite_provenance'] for r in slots))
    assert composition==expected['composition']
    eval_out=output/'evaluation';eval_out.mkdir()
    write_csv(eval_out/'correctness_matrix.csv',[dict(J1_score=i,J2_score=j,count=int(matrix[i,j])) for i in range(3) for j in range(3)])
    compare_csv(eval_out/'correctness_matrix.csv',PACKAGE/'evaluation/correctness_matrix.csv')
    varied=[];slot_groups=collections.defaultdict(list)
    for r in slots:slot_groups[r['task_id'],r['condition'],r['judge']].append(r)
    assert sum(len({r['score'] for r in rr})>1 for rr in slot_groups.values())==len(read_csv(PACKAGE/'evaluation/repeated_group_variation.csv'))==21
    mismatch_count=sum(slot_lookup[(t,'B1',r,j)]['score']!=slot_lookup[(t,'G1',r,j)]['score'] for t in metadata for r in [1,2,3] for j in ['J1','J2'])
    assert mismatch_count==len(read_csv(PACKAGE/'evaluation/matched_score_disagreements.csv'))==14
    figure_note='not requested'
    if args.figures:
        for folder in ['figures/pdf','figures/png','figures/svg','previews','validation']:(common.OUT/folder).mkdir(parents=True,exist_ok=True)
        figures=load_module('resource_figures',PACKAGE/'originals/resource_v1/figures.py')
        # Replace the original raw-source location in the generated manifest.
        figures.manifest['authoritative_sources']['raw_records']='released projection: data/execution_telemetry_270.jsonl; original records withheld'
        figures.main()
        thesis.OUT=thesis_out
        thesis.style();thesis.resources(task_rows);thesis.paired_differences(differences);thesis.recovery_abstention(joint)
        evaluation.OUT=eval_out;evaluation.plot(matrix,metrics)
        ieee_source=(PACKAGE/'reference/ieee_figure01/figure01_execution_resource_profile_ieee.py').read_text()
        original_base='BASE = Path(\n    "/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1"\n)'
        assert original_base in ieee_source
        ieee_source=ieee_source.replace(original_base,'BASE = Path('+repr(str(output))+')')
        for name in ['data','figures']:(output/'execution_figures_v2'/name).mkdir(parents=True,exist_ok=True)
        exec(compile(ieee_source,'<relocated original IEEE figure01>','exec'),{'__name__':'__main__','__file__':str(PACKAGE/'reference/ieee_figure01/figure01_execution_resource_profile_ieee.py')})
        for name in ['figure01_source_data.csv','figure01_summary.csv']:
            compare_csv(output/'execution_figures_v2/data'/name,PACKAGE/'reference/ieee_figure01'/name)
        figure_note='14 resource-v1 layouts, three thesis execution figures, provisional LLM matrix, and frozen IEEE resource Figure 1 rendered; numeric companions checked. Font/library differences can change bytes.'
    report=dict(status='PASS',scope='Released telemetry and numeric annotation reconstruction; no inference or independent semantic/human evaluation.',
                raw_records_released=False,projected_records=270,original_hash_match_is_not_raw_access=True,
                existing_table_files_compared=len(compared)+1,compared_tables=compared,
                numeric_tolerance=dict(relative=1e-12,absolute=1e-9),composition=composition,
                composite_agreement=metrics,original_valid_pair_agreement=original_metrics,
                paired_statistics=paired_stats,figures=figure_note,
                withheld='answer text; retrieval query text; rights-held source originals; original processed retrieval passages; human/expert data; full judge reasons/responses; model weights and vectors')
    (output/'RECONSTRUCTION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
