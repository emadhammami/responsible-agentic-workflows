#!/usr/bin/env python3
"""Reconstruct boundary summary from distributed integrity rows and reported totals."""
import csv,json,argparse
from pathlib import Path
from collections import Counter

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    root=Path(__file__).resolve().parent
    rows=list(csv.DictReader((root/'data/execution_integrity.csv').open(newline='',encoding='utf-8')))
    meta=json.loads((root/'data/reported_metrics.json').read_text(encoding='utf-8'))
    assert len(rows)==36
    assert len(set((r['family_id'],r['condition'],r['repetition']) for r in rows))==36
    assert len(set(r['family_id'] for r in rows))==6
    assert Counter(r['condition'] for r in rows)=={'B1':18,'G1':18}
    for f in set(r['family_id'] for r in rows):
        assert {(r['condition'],r['repetition']) for r in rows if r['family_id']==f}=={(c,str(i)) for c in ('B1','G1') for i in range(1,4)}
    assert all(r['recorded_status']=='resource_stopped' for r in rows)
    for r in rows:
        assert all(r[k]=='true' for k in r if k.startswith('recorded_') and k!='recorded_status' or k in ('model_capture_counts','retrieval_capture_counts','model_settings_and_wire_responses','usage_reconciles','source_exposure_and_provenance','initial_critic_matches_policy_event','final_state_matches_record','call_cap','identity','drafts_and_raw_critic_retained'))
        assert len(r['native_record_sha256'])==64
    rs=meta['resources_reported']
    pct=round(100*(1-rs['G1_tokens_total']/rs['B1_tokens_total']),2)
    assert abs(pct-30.67)<0.01
    assert (rs['G1_actual_reservation_gate_events'],rs['B1_supported_unreleased_revisions'])==(18,18)
    assert meta['task_completions_reported']=={'B1':0,'G1':0}
    result={'study':'Resource boundary','basis':'verified published integrity rows + arithmetically checked *reported* totals',
            'integrity_rows':len(rows),'families':6,'policy_counts':dict(Counter(r['condition'] for r in rows)),
            'recorded_status_counts':dict(Counter(r['recorded_status'] for r in rows)),
            'recorded_integrity_flags_all_true':True,'reported_completed_task_outcomes':meta['task_completions_reported'],
            'reported_model_tokens':{'B1':rs['B1_tokens_total'],'G1':rs['G1_tokens_total']},
            'recalculated_reduction_pct_from_reported_totals':pct,
            'reported_G1_reservation_events':rs['G1_actual_reservation_gate_events'],
            'limitations':'No native raw executions published; reserve-event details and token totals are source-reported, not independently remeasured.'}
    a.output.mkdir(parents=True,exist_ok=False)
    (a.output/'resource-boundary-summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
