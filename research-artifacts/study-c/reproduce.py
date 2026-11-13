#!/usr/bin/env python3
"""Reconstruct Study C's secondary ordinal scores from published task rows."""
import csv,json,argparse
from pathlib import Path
from collections import Counter

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    root=Path(__file__).resolve().parent
    rows=list(csv.DictReader((root/'data/secondary_task_scores.csv').open(newline='',encoding='utf-8')))
    meta=json.loads((root/'data/reported_metrics.json').read_text(encoding='utf-8'))
    assert len(rows)==18 and len({x['task_id'] for x in rows})==18
    assert Counter(r['use_case'] for r in rows)=={'UC1':6,'UC2':6,'UC3':6}
    assert Counter(r['stratum'] for r in rows)=={'sufficient':6,'missing':6,'grounding':6}
    assert Counter(r['expected_answerability'] for r in rows)=={'answerable':12,'withhold':6}
    assert all(r['technical_abstained'] in ('true','false') and r['trailing_incomplete_observed'] in ('true','false') for r in rows)
    grades=[int(r['grade_0_2']) for r in rows]
    assert set(grades)<={0,1,2}
    c=Counter(grades);pts=sum(grades)
    assert c=={2:15,1:2,0:1} and pts==32
    assert [r['task_id'] for r in rows if int(r['grade_0_2'])==0]==['T21008']
    actual_withhold_stops=sum(r['technical_abstained']=='true' for r in rows if r['expected_answerability']=='withhold')
    assert actual_withhold_stops==3
    assert meta['reported_usable_outcomes']==108 and meta['reported_paired_runs']==54
    assert meta['paired_final_output_identity_reported']==54
    ci=meta['latency_reported']['task_paired_95pct_interval_ms']
    assert ci[0]<0<ci[1]
    b1=meta['means_reported']['B1'];g1=meta['means_reported']['G1']
    assert all(b1[k]==g1[k] for k in ['total_tokens','input_tokens','output_tokens','llm_calls','retrieval_calls'])
    result={'study':'Study C','basis':'derived directly from distributed 18 task-level secondary ratings; operational metrics reported',
            'scoring_units':len(rows),'scoring_policy':'Same 18 distinct task response texts under B1 and G1; do not multiply by repetitions',
            'grade_counts':{str(k):c[k] for k in (0,1,2)},'total_points_per_policy':pts,'maximum_points_per_policy':2*len(rows),
            'percent_of_possible_points_per_policy':round(100*pts/(2*len(rows)),2),
            'full_grade2_tasks':c[2],'technical_abstentions_on_withhold_tasks':actual_withhold_stops,
            'reported_workflows':meta['reported_usable_outcomes'], 'reported_identical_final_pairs':meta['paired_final_output_identity_reported'],
            'reported_paired_token_difference':meta['paired_structural_differences_reported']['paired_token_difference'],
            'reported_latency_mean_difference_ms':meta['latency_reported']['G1_minus_B1_ms'],
            'reported_latency_task_paired_ci_ms':ci,
            'limitations':'AI-assisted post-hoc semantic ratings, not independent expert judgments; response/source text and original run logs are not distributed.'}
    a.output.mkdir(parents=True,exist_ok=False)
    (a.output/'study-c-summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
