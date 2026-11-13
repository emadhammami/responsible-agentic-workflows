"""Audit frozen telemetry and derive all companion data before plotting."""
import json, math, statistics, collections, re, subprocess
from common import *

def load_source():
 freeze=json.loads((ROOT/'primary_benchmark_raw_freeze_manifest.json').read_text())
 assert freeze['status']=='frozen' and freeze['primary_execution_complete'] is True
 assert hash_file(ROOT/'RAW_RECORD_SHA256SUMS.txt')==freeze['record_hash_inventory']['sha256']
 inventory={name:digest for digest,name in (line.split(maxsplit=1) for line in (ROOT/'RAW_RECORD_SHA256SUMS.txt').read_text().splitlines())}
 assert len(inventory)==270
 actual={p.name:hash_file(p) for p in sorted((ROOT/'run_records').glob('*.json'))}
 assert actual==inventory, 'Frozen raw file inventory mismatch'
 bundle=hashlib.sha256(''.join(f'{name}\t{digest}\n' for name,digest in sorted(actual.items())).encode()).hexdigest()
 assert bundle==freeze['raw_record_bundle_sha256']
 order_path=REPO/'evidence/engineering/primary_execution_order_v1.json'
 assert hash_file(order_path)==freeze['execution_order']['sha256']
 assert hash_file(ROOT/'launch_manifest.json')==freeze['launch_manifest_sha256']
 assert hash_file(ROOT/'primary_benchmark_runner_v1.py')==freeze['runner_sha256']
 assert hash_file(ROOT/'PRIMARY_BENCHMARK_V1_LIVE.log')==freeze['execution_log_sha256']
 order=json.loads(order_path.read_text())['runs']
 assert len(order)==270 and [r['execution_sequence'] for r in order]==list(range(1,271))
 tasks=json.loads((REPO/'benchmark/tasks/primary_benchmark_freeze_manifest.json').read_text())
 uc_map={Path(name).stem:Path(name).parent.name for name in tasks['frozen_task_file_sha256']}
 assert len(uc_map)==30 and set(uc_map.values())==set(UCS)
 assert all(hash_file(REPO/name)==digest for name,digest in tasks['frozen_task_file_sha256'].items())
 raw=[]; traces={}
 for entry in order:
  path=ROOT/'run_records'/entry['output_relative_path']; d=json.loads(path.read_text())
  assert d['run_id']==entry['run_id'] and d['task_id']==entry['task_id'] and d['condition']==entry['condition']
  assert d['experiment_id']=='PRIMARY-BENCHMARK-V1' and d['execution_mode']=='benchmark'
  assert d['code_revision']==freeze['final_execution_code_revision']
  assert d['status'] in ['completed','completed_after_recovery']
  assert d['run_id']==f"primary-{d['task_id'].lower()}-{d['condition'].lower()}-r{entry['repetition']}"
  model=d['model']['calls']; retrieval=d['retrieval']['calls']; u=d['usage']; t=d['timing']
  assert all(c['status']=='completed' and all(isinstance(c[k],int) and c[k]>=0 for k in ['input_tokens','output_tokens','total_tokens']) for c in model)
  assert all(c['total_tokens']==c['input_tokens']+c['output_tokens'] for c in model)
  assert u['input_tokens']==sum(c['input_tokens'] for c in model)
  assert u['output_tokens']==sum(c['output_tokens'] for c in model)
  assert u['total_tokens']==u['input_tokens']+u['output_tokens']
  assert u['llm_calls']==len(model) and u['retrieval_calls']==len(retrieval)
  assert math.isclose(t['llm_ms'],sum(c['latency_ms'] for c in model),rel_tol=1e-12,abs_tol=1e-8)
  assert math.isclose(t['retrieval_ms'],sum(c['latency_ms'] for c in retrieval),rel_tol=1e-12,abs_tol=1e-8)
  assert t['end_to_end_ms']>0 and t['end_to_end_ms']>=t['llm_ms']+t['retrieval_ms']
  events=d['events']; counts=collections.Counter(e['event_type'] for e in events)
  policies=[e['details'] for e in events if e['event_type']=='policy_decision']
  assert len(policies)==(0 if d['condition']=='B0' else 1)
  row={'execution_sequence':entry['execution_sequence'],'run_id':d['run_id'],'task_id':d['task_id'],
       'UC':uc_map[d['task_id']],'condition':d['condition'],'repetition':entry['repetition'],
       'status':d['status'],'source_record_sha256':actual[path.name]}
  row.update({m:u[m] for m in ['input_tokens','output_tokens','total_tokens','llm_calls','retrieval_calls','tool_calls','retries']})
  row.update({m:t[m] for m in ['end_to_end_ms','llm_ms','retrieval_ms']})
  row.update(error_count=len(d['errors']),completed_execution=int(d['status'] in ['completed','completed_after_recovery']),
             resource_stop=int(d['status']=='resource_stopped'),final_abstention=int(d['final_output']['abstained']))
  row.update({m:None for m in CONTROL+[m for m in METRICS if m.startswith('prepolicy_')]})
  row.update(selected_action=None,selected_recovery_path=None,reason_code=None)
  if policies:
   p=policies[0]
   row.update(recovery_trigger_count=int(p['selected_action'] in ['REVISE_ONLY','RERETRIEVE_REVISE']),
      recovery_attempt_count=counts['recovery_started'],recovery_retrieval_count=counts['recovery_retrieval_completed'],
      revision_completed_count=counts['revision_completed'],post_recovery_verification_count=counts['post_recovery_critic_completed'],
      verification_calls=counts['initial_critic_completed']+counts['post_recovery_critic_completed'],
      abstention_event_count=counts['abstained'],policy_decision_count=counts['policy_decision'],
      pre_recovery_abstention=int(p['selected_action']=='ABSTAIN'),recovery_finalized=int(d['status']=='completed_after_recovery'),
      selected_action=p['selected_action'],selected_recovery_path=p['selected_recovery_path'],reason_code=p['reason_code'])
   for m in METRICS:
    if m.startswith('prepolicy_'): row[m]=p[m.removeprefix('prepolicy_')+'_used']
   assert counts['initial_critic_completed']==1
   assert row['llm_calls']==3+counts['revision_completed']+counts['post_recovery_critic_completed']
   assert row['retries']==row['recovery_attempt_count']==row['recovery_finalized']==row['revision_completed_count']==row['post_recovery_verification_count']
   assert row['retrieval_calls']==1+row['recovery_retrieval_count']
   assert row['final_abstention']==row['abstention_event_count']
  assert all(v is None or (math.isfinite(v) and v>=0) for m in METRICS for v in [row[m]])
  traces[d['run_id']]=[e['event_type'] for e in events]
  raw.append(row)
 assert len(raw)==len({r['run_id'] for r in raw})==270
 assert collections.Counter(r['condition'] for r in raw)=={'B0':90,'B1':90,'G1':90}
 assert collections.Counter(r['UC'] for r in raw)=={'UC1':90,'UC2':90,'UC3':90}
 assert len({r['task_id'] for r in raw})==30
 groups=collections.defaultdict(list)
 for row in raw: groups[row['task_id'],row['condition']].append(row)
 assert len(groups)==90 and all(sorted(r['repetition'] for r in rr)==[1,2,3] for rr in groups.values())
 return raw,groups,traces,freeze

def derive(raw,groups,traces):
 aggregated=[]; by_group={}
 for (task,condition),rr in sorted(groups.items()):
  row={'task_id':task,'UC':rr[0]['UC'],'condition':condition,'n_repetitions':3,'source_run_ids':';'.join(r['run_id'] for r in sorted(rr,key=lambda r:r['repetition']))}
  row.update({m:mean([r[m] for r in rr]) if rr[0][m] is not None else None for m in METRICS})
  aggregated.append(row); by_group[task,condition]=row
 paired=[]
 for task in sorted({r['task_id'] for r in raw}):
  b,g=by_group[task,'B1'],by_group[task,'G1']; assert b['UC']==g['UC']
  row={'task_id':task,'UC':b['UC'],'n_B1_repetitions':3,'n_G1_repetitions':3,'B1_run_ids':b['source_run_ids'],'G1_run_ids':g['source_run_ids']}
  for metric in METRICS:row.update({metric+'_B1':b[metric],metric+'_G1':g[metric],metric+'_difference':g[metric]-b[metric]})
  paired.append(row)
 assert len(paired)==30 and collections.Counter(r['UC'] for r in paired)=={'UC1':10,'UC2':10,'UC3':10}
 lookup={(r['task_id'],r['condition'],r['repetition']):r for r in raw}
 divergence=[]
 for task in sorted({r['task_id'] for r in raw}):
  for repetition in [1,2,3]:
   b,g=lookup[task,'B1',repetition],lookup[task,'G1',repetition]
   divergence.append({'task_id':task,'UC':b['UC'],'repetition':repetition,'B1_run_id':b['run_id'],'G1_run_id':g['run_id'],
    'B1_selected_action':b['selected_action'],'G1_selected_action':g['selected_action'],
    'action_diverged':int(b['selected_action']!=g['selected_action']),
    'event_trace_diverged':int(traces[b['run_id']]!=traces[g['run_id']])})
 return aggregated,paired,divergence

def descriptives(raw,paired):
 import numpy as np
 summary=[]
 groupings=[('overall','ALL','ALL',raw)]
 groupings += [('condition',c,'ALL',[r for r in raw if r['condition']==c]) for c in CONDITIONS]
 groupings += [('UC','ALL',uc,[r for r in raw if r['UC']==uc]) for uc in UCS]
 groupings += [('condition_x_UC',c,uc,[r for r in raw if r['condition']==c and r['UC']==uc]) for c in CONDITIONS for uc in UCS]
 for level,cond,uc,rr in groupings:
  for metric,(unit,definition,scope) in METRICS.items():
   v=[r[metric] for r in rr if r[metric] is not None];n=len(v)
   row={'grouping':level,'condition':cond,'UC':uc,'metric':metric,'unit':unit,'analysis_unit':'raw execution (descriptive only)',
     'n':n,'n_total_runs':len(rr),'n_structurally_not_applicable':len(rr)-n,'mean':None,'median':None,'std':None,'min':None,'max':None,'Q1':None,'Q3':None}
   if n:row.update(mean=mean(v),median=statistics.median(v),std=statistics.stdev(v) if n>1 else None,min=min(v),max=max(v),Q1=float(np.quantile(v,.25,method='linear')),Q3=float(np.quantile(v,.75,method='linear')))
   summary.append(row)
 pair_summary=[]
 for uc in ['ALL']+UCS:
  rows=[r for r in paired if uc=='ALL' or r['UC']==uc]
  for metric,(unit,definition,scope) in METRICS.items():
   v=[r[metric+'_difference'] for r in rows]
   pair_summary.append({'UC':uc,'metric':metric,'unit':unit,'analysis_unit':'paired task, mean of 3 repetitions per condition','difference':'G1 - B1','n_paired_tasks':len(v),
      'mean_difference':mean(v),'median_difference':statistics.median(v),'min_difference':min(v),'max_difference':max(v)})
 return summary,pair_summary

def audit_document(raw,groups,freeze):
 counts=collections.Counter(r['status'] for r in raw)
 lines=['# Frozen 270-run execution metric audit','','Status: PASS. Audit completed before plotting.','','## Authoritative sources','',
 f'- `{ROOT}/run_records/*.json`: exactly 270 raw records, authoritative usage, timing, event and terminal-status telemetry.',
 '- `RAW_RECORD_SHA256SUMS.txt` and `primary_benchmark_raw_freeze_manifest.json`: every raw record hash verified; raw bundle matches the frozen digest.',
 '- Repository `evidence/engineering/primary_execution_order_v1.json`: authoritative run/task/condition/repetition mapping, frozen hash verified.',
 '- Repository `benchmark/tasks/primary_benchmark_freeze_manifest.json`: use-case assignment comes from frozen task-file paths; task hashes verified without using reference answers or rubric content.',
 '- Existing `analysis/runtime_v1` is a derived projection and is not used as the numeric source. No scored/evaluated dataset is parsed or joined.',
 f'- Raw execution code revision: `{freeze["final_execution_code_revision"]}`. Instrumentation semantics checked read-only at that revision; no runner or workflow is executed.','',
 '## Design checks','',
 'TOTAL_RUNS=270; B0/B1/G1=90 each; UC1/UC2/UC3=90 each; UNIQUE_TASKS=30; exactly 3 repetitions for every task-condition.',
 f'Terminal telemetry: {dict(counts)}. All 270 raw observations are preserved; no run exclusion or task filtering.',
 'B1/G1 task identities align exactly: 30 paired tasks overall, 10 in each UC.','',
 '## Metric inventory','',
 '| Metric | Unit | Definition / authoritative field | Applicability | Valid values / missing |',
 '|---|---|---|---|---|']
 for metric,(unit,definition,scope) in METRICS.items():
  values=[r[metric] for r in raw if r[metric] is not None]
  lines.append(f'| {metric} | {unit} | {definition} | {scope} | n={len(values)}, range {min(values):g}–{max(values):g}; {270-len(values)} structural N/A |')
 lines+=['','All reported token totals are checked against individual model-call telemetry; no missing provider-token fields. Call counts and model/retrieval timing sums are cross-checked. The end-to-end unit is the logged millisecond throughout.','',
 '## Control semantics and unavailable measures','',
 '- `retries` is a bounded recovery-cycle counter, supplied by `recovery_iteration` in the frozen runner. Network/provider retry counts are not separately logged and are unavailable.',
 '- Recovery requested and recovery started are distinguished. In these records each requested path starts and reaches logged revision/post-recovery verification; resource-stop count is zero. B0 has no agentic event trace or policy decision, so event-derived control metrics are N/A for B0 rather than invented zeros.',
 '- Verification calls count completed initial/post-recovery critic invocations only. Critic assessment content, support/grounding labels, release flags and evidence-sufficiency labels are neither exported nor used.',
 '- `completed_after_recovery` is operational finalization, including runs that end in abstention. It does not establish answer correctness, support, reliability improvement, or successful recovery in a judged sense. No successful-recovery quality metric is available or constructed.',
 '- `final_abstention` is the raw final abstention flag. `abstention_event_count` and pre-recovery ABSTAIN are distinct operational events/actions; no correct/incorrect abstention labeling.',
 '- Action divergence compares logged selected actions; event-trace divergence compares ordered event_type lists, for the same task and repetition. This is a descriptive trace comparison, not a quality effect.',
 '- Tool calls are logged separately and are all zero. The core retrieval/tool panel therefore reports actual retrieval calls; it does not relabel a sum as a measured tool quantity.',
 '- Configuration limits, model identity, provider response IDs, retrieved text/scores, answer content/citations, critic judgments, references, rubric labels, scoring and expert results are outside this execution-analysis dataset.',
 '', '## Analysis and figure decisions','',
 '- Core metrics fixed by the requested design: total tokens, model calls, retrieval calls, end-to-end latency. All appear in Figures 1–3; no result-driven subset is selected.',
 '- For each task-condition compute the arithmetic mean of exactly three repetitions. Pair B1/G1 by task and compute G1 mean − B1 mean. Negative means less resource/time for G1. Repetitions are not independent tasks.',
 '- Figures 1 and 5 retain raw executions only as descriptive distributions (90 per condition; 30 per condition-UC). Figure 4 reports operational counts with denominators and task-mean verification-call distributions. B0 is supporting reference only.',
 '- Sample standard deviation uses n−1. Quartiles use linear interpolation (NumPy method="linear"). Box whiskers extend to the most extreme observation within 1.5 IQR; every observation is additionally shown, including outliers. Black diamonds mark arithmetic means; box center lines mark medians. No confidence intervals, significance tests or inferential claims.',
 '- Latency stays on a linear millisecond scale with all data included and zero visible. No silent transform; no log plot is needed for the observed range.',
 '- Supplement S1 separates input/output token resources. Supplement S2 shows within-task latency sample SD across three repetitions: replication variability is distinct from marginal latency distribution. Every within-task token SD is zero, documented numerically; a redundant all-zero token-variability chart is omitted.',
 '', '## Mutation and scoring boundaries','',
 'The regeneration pipeline hashes protected benchmark/corpus/scoring/expert artifacts before and after. Hashing is integrity checking only: no scoring or expert content is parsed, modeled, plotted or used for metric selection. Git HEAD/status are checked before and after; outputs are written only under execution_figures_v1.']
 (OUT/'source_metric_audit.md').write_text('\n'.join(lines)+'\n')

def main():
 OUT.mkdir(parents=True,exist_ok=True);(OUT/'data').mkdir(exist_ok=True)
 raw,groups,traces,freeze=load_source();aggregated,paired,divergence=derive(raw,groups,traces)
 audit_document(raw,groups,freeze)
 write_csv('raw_execution_metrics_270.csv',raw)
 write_csv('task_condition_means.csv',aggregated)
 write_csv('figure01_overall_resource_profile.csv',[{k:r[k] for k in ['run_id','task_id','UC','condition','repetition']+CORE} for r in raw])
 call_frequencies=[]
 for condition in CONDITIONS:
  for metric in ['llm_calls','retrieval_calls']:
   frequency=collections.Counter(r[metric] for r in raw if r['condition']==condition)
   for level,n in sorted(frequency.items()):call_frequencies.append({'condition':condition,'metric':metric,'call_count':level,'run_frequency':n,'denominator_runs':90})
 write_csv('figure01_call_frequency_counts.csv',call_frequencies)
 write_csv('figure02_b1_g1_paired_differences.csv',[{k:r[k] for k in ['task_id','UC','n_B1_repetitions','n_G1_repetitions','B1_run_ids','G1_run_ids']+[m+s for m in CORE for s in ['_B1','_G1','_difference']]} for r in paired])
 # Separate companions are intentional: each figure remains independently traceable.
 write_csv('figure03_use_case_resource.csv',[{k:r[k] for k in ['task_id','UC','n_B1_repetitions','n_G1_repetitions','B1_run_ids','G1_run_ids']+[m+s for m in CORE for s in ['_B1','_G1','_difference']]} for r in paired])
 agents=[r for r in raw if r['condition'] in ['B1','G1']]
 write_csv('figure04_control_behavior_runs.csv',[{k:r[k] for k in ['run_id','task_id','UC','condition','repetition','status','selected_action','selected_recovery_path','reason_code','retries','resource_stop','final_abstention']+CONTROL} for r in agents])
 control_plot=[]
 for cond in ['B1','G1']:
  selected=[r for r in agents if r['condition']==cond]
  for metric in ['recovery_attempt_count','recovery_retrieval_count','pre_recovery_abstention','final_abstention','resource_stop']:
   control_plot.append({'panel':'a','condition':cond,'metric':metric,'task_id':'','UC':'ALL','plotted_value':sum(r[metric] for r in selected),'unit':'runs','denominator_runs':90,'n_repetitions_per_task':'','analysis_unit':'raw execution incidence, descriptive'})
  for task in sorted({r['task_id'] for r in selected}):
   rr=[r for r in selected if r['task_id']==task]
   control_plot.append({'panel':'b','condition':cond,'metric':'verification_calls','task_id':task,'UC':rr[0]['UC'],'plotted_value':mean([r['verification_calls'] for r in rr]),'unit':'calls per run','denominator_runs':3,'n_repetitions_per_task':3,'analysis_unit':'task mean of 3 repetitions'})
  for action in ['ACCEPT','REVISE_ONLY','RERETRIEVE_REVISE','ABSTAIN']:
   control_plot.append({'panel':'c','condition':cond,'metric':action,'task_id':'','UC':'ALL','plotted_value':sum(r['selected_action']==action for r in selected),'unit':'runs','denominator_runs':90,'n_repetitions_per_task':'','analysis_unit':'raw execution policy actions, descriptive'})
 write_csv('figure04_control_behavior.csv',control_plot)
 latency=[{k:r[k] for k in ['run_id','task_id','UC','condition','repetition','end_to_end_ms']} for r in raw]
 for cond in CONDITIONS:
  selected=sorted((r for r in latency if r['condition']==cond),key=lambda r:(r['end_to_end_ms'],r['run_id']))
  for rank,r in enumerate(selected,1):r.update(overall_rank=rank,overall_n=90,overall_ecdf=rank/90)
  for uc in UCS:
   subset=sorted((r for r in selected if r['UC']==uc),key=lambda r:(r['end_to_end_ms'],r['run_id']))
   for rank,r in enumerate(subset,1):r.update(UC_rank=rank,UC_n=30,UC_ecdf=rank/30)
 write_csv('figure05_latency_distribution.csv',latency)
 write_csv('figureS01_token_decomposition.csv',[{k:r[k] for k in ['task_id','UC','condition','n_repetitions','source_run_ids','input_tokens','output_tokens','total_tokens']} for r in aggregated])
 variability=[]
 for (task,cond),rr in sorted(groups.items()):
  variability.append({'task_id':task,'UC':rr[0]['UC'],'condition':cond,'n_repetitions':3,'source_run_ids':';'.join(r['run_id'] for r in rr),
   'latency_mean_ms':mean([r['end_to_end_ms'] for r in rr]),'latency_sample_sd_ms':statistics.stdev([r['end_to_end_ms'] for r in rr]),
   'total_tokens_mean':mean([r['total_tokens'] for r in rr]),'total_tokens_sample_sd':statistics.stdev([r['total_tokens'] for r in rr])})
 assert all(r['total_tokens_sample_sd']==0 for r in variability)
 write_csv('figureS02_repetition_variability.csv',variability)
 summary,pair_summary=descriptives(raw,paired)
 write_csv('execution_summary.csv',summary);write_csv('paired_execution_summary.csv',pair_summary)
 write_csv('b1_g1_operational_divergence.csv',divergence)
 divergence_tasks=[]
 for task in sorted({r['task_id'] for r in divergence}):
  rr=[r for r in divergence if r['task_id']==task]
  divergence_tasks.append({'task_id':task,'UC':rr[0]['UC'],'n_paired_repetitions':3,
   'action_divergence_fraction':mean([r['action_diverged'] for r in rr]),
   'event_trace_divergence_fraction':mean([r['event_trace_diverged'] for r in rr])})
 write_csv('operational_divergence_task_means.csv',divergence_tasks)
 divergence_summary=[]
 for uc in ['ALL']+UCS:
  rr=[r for r in divergence_tasks if uc=='ALL' or r['UC']==uc]
  for metric in ['action_divergence_fraction','event_trace_divergence_fraction']:
   v=[r[metric] for r in rr]
   divergence_summary.append({'UC':uc,'metric':metric,'analysis_unit':'paired task; fraction of 3 paired repetitions','n_paired_tasks':len(v),
     'n_paired_repetitions':len(v)*3,'mean':mean(v),'median':statistics.median(v),'min':min(v),'max':max(v)})
 write_csv('operational_divergence_summary.csv',divergence_summary)
 categorical=[]
 for level,cond,uc,rr in [('condition',c,'ALL',[r for r in raw if r['condition']==c]) for c in CONDITIONS]+[('condition_x_UC',c,u,[r for r in raw if r['condition']==c and r['UC']==u]) for c in CONDITIONS for u in UCS]:
  for field in ['status','selected_action','selected_recovery_path','reason_code']:
   eligible=[r[field] for r in rr if r[field] is not None]
   for category,n in sorted(collections.Counter(eligible).items()):categorical.append({'grouping':level,'condition':cond,'UC':uc,'field':field,'category':category,'count':n,'denominator_runs':len(eligible),'fraction':n/len(eligible)})
 write_csv('operational_categorical_counts.csv',categorical)
 (OUT/'data/metric_definitions.json').write_text(json.dumps({m:{'unit':u,'definition':d,'scope':s} for m,(u,d,s) in METRICS.items()},indent=2)+'\n')
 print('SOURCE_270_RUNS_VERIFIED=PASS; paired tasks=30; no scoring/expert data used',flush=True)

if __name__=='__main__':main()
