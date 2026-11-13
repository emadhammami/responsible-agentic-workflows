#!/usr/bin/env python3
"""Reconstruct Study B summaries from distributed integrity rows and reported aggregate inputs."""
import csv, json, argparse
from pathlib import Path
from collections import Counter

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    rows=list(csv.DictReader((root/'data/execution_integrity.csv').open(newline='',encoding='utf-8')))
    meta=json.loads((root/'data/reported_metrics.json').read_text(encoding='utf-8'))
    assert len(rows)==144, 'Study B: expected 144 execution-integrity rows'
    assert len(set((r['family_id'],r['condition'],r['repetition']) for r in rows))==144
    assert len(set(r['family_id'] for r in rows))==24
    assert Counter(r['condition'] for r in rows)=={'B1':72,'G1':72}
    assert set(r['repetition'] for r in rows)=={'1','2','3'}
    for f in set(r['family_id'] for r in rows):
        assert {(r['condition'],r['repetition']) for r in rows if r['family_id']==f}=={(c,str(i)) for c in ('B1','G1') for i in range(1,4)}
    for r in rows:
        assert r['recorded_status'] in ('completed','completed_after_recovery')
        assert all(r[k]=='true' for k in r if k.startswith('recorded_') and k!='recorded_status' or k in ('model_capture_counts','retrieval_capture_counts','model_settings_and_wire_responses','usage_reconciles','source_exposure_and_provenance','initial_critic_matches_policy_event','final_state_matches_record','call_cap','identity','drafts_and_raw_critic_retained'))
        assert len(r['native_record_sha256'])==64
    res=meta['resources_reported'];out=meta['outcomes_reported']
    assert res['B1_input_tokens_total']+res['B1_output_tokens_total']==res['B1_tokens_total']
    assert res['G1_input_tokens_total']+res['G1_output_tokens_total']==res['G1_tokens_total']
    assert (out['B1_success_families'],out['G1_success_families'],out['denominator_families'])==(21,21,24)
    assert meta['paired_final_output_identity_reported']==72
    pct=round(100*(1-res['G1_tokens_total']/res['B1_tokens_total']),2)
    assert abs(pct-res['token_savings_pct'])<0.01
    result={'study':'Study B','basis':'verified published integrity rows + arithmetically checked *reported* aggregates',
            'integrity_rows':len(rows),'families':24,'policies':dict(Counter(r['condition'] for r in rows)),
            'observed_record_status_counts':dict(Counter(r['recorded_status'] for r in rows)),
            'recorded_integrity_flags_all_true':True,
            'reported_success_per_policy':{'B1':21,'G1':21,'denominator':24},
            'reported_final_identity_pairs':72,
            'reported_model_tokens':{'B1':res['B1_tokens_total'],'G1':res['G1_tokens_total']},
            'reported_token_difference':res['G1_tokens_total']-res['B1_tokens_total'],
            'recalculated_reduction_pct_from_reported_totals':pct,
            'limitations':'Does not independently derive token totals, output identity, or semantic correctness from native raw workflow outputs.'}
    args.output.mkdir(parents=True,exist_ok=False)
    (args.output/'study-b-summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
