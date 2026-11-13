"""Execution-only constants and filesystem guards; no benchmark execution."""
from pathlib import Path
import csv, hashlib, json, subprocess, math

ROOT = Path('/home/emadh/primary-benchmark-results/PRIMARY-BENCHMARK-V1')
REPO = Path('/home/emadh/projects/responsible-agentic-workflows')
OUT = ROOT / 'execution_figures_v1'
CONDITIONS = ['B0', 'B1', 'G1']
UCS = ['UC1', 'UC2', 'UC3']
CORE = ['total_tokens', 'llm_calls', 'retrieval_calls', 'end_to_end_ms']
CORE_LABELS = ['Total tokens', 'Model calls', 'Retrieval calls', 'Latency (ms)']
CONTROL = ['recovery_trigger_count', 'recovery_attempt_count', 'recovery_retrieval_count',
           'revision_completed_count', 'post_recovery_verification_count', 'verification_calls',
           'abstention_event_count', 'policy_decision_count', 'pre_recovery_abstention',
           'recovery_finalized']
METRICS = {
 'input_tokens': ('tokens', 'usage.input_tokens; verified sum of model.calls[].input_tokens', 'all'),
 'output_tokens': ('tokens', 'usage.output_tokens; verified sum of model.calls[].output_tokens', 'all'),
 'total_tokens': ('tokens', 'usage.total_tokens; input_tokens + output_tokens', 'all'),
 'llm_calls': ('calls', 'usage.llm_calls; verified len(model.calls)', 'all'),
 'retrieval_calls': ('calls', 'usage.retrieval_calls; verified len(retrieval.calls)', 'all'),
 'tool_calls': ('calls', 'usage.tool_calls; separate from retrieval_calls, always 0', 'all'),
 'retries': ('recovery cycles', 'usage.retries; frozen AgenticRunner supplies recovery_iteration, not transport retries', 'all'),
 'end_to_end_ms': ('ms', 'timing.end_to_end_ms; recorder elapsed monotonic milliseconds', 'all'),
 'llm_ms': ('ms', 'timing.llm_ms; verified sum of model-call latency_ms', 'all'),
 'retrieval_ms': ('ms', 'timing.retrieval_ms; verified sum of retrieval-call latency_ms', 'all'),
 'error_count': ('errors', 'len(errors); not an outcome score', 'all'),
 'completed_execution': ('0/1 per run', 'status in {completed, completed_after_recovery}', 'all'),
 'resource_stop': ('0/1 per run', 'status == resource_stopped', 'all'),
 'final_abstention': ('0/1 per run', 'final_output.abstained; logged action, not correct/incorrect abstention', 'all'),
 'recovery_trigger_count': ('triggers', 'policy_decision.details.selected_action in {REVISE_ONLY, RERETRIEVE_REVISE}', 'B1/G1'),
 'recovery_attempt_count': ('starts', 'count(events[].event_type == recovery_started)', 'B1/G1'),
 'recovery_retrieval_count': ('completed stages', 'count(recovery_retrieval_completed events)', 'B1/G1'),
 'revision_completed_count': ('completed stages', 'count(revision_completed events)', 'B1/G1'),
 'post_recovery_verification_count': ('completed calls', 'count(post_recovery_critic_completed events); frozen node executes one model call', 'B1/G1'),
 'verification_calls': ('completed calls', 'count(initial_critic_completed) + count(post_recovery_critic_completed); no critic assessment labels used', 'B1/G1'),
 'abstention_event_count': ('events', 'count(abstained events)', 'B1/G1'),
 'policy_decision_count': ('decisions', 'count(policy_decision events)', 'B1/G1'),
 'pre_recovery_abstention': ('0/1 per run', 'selected_action == ABSTAIN at the logged policy decision', 'B1/G1'),
 'recovery_finalized': ('0/1 per run', 'status == completed_after_recovery; also checked revision and post-recovery verification events', 'B1/G1'),
}
for name, unit in [('input_tokens', 'tokens'), ('output_tokens', 'tokens'), ('total_tokens', 'tokens'),
                   ('llm_calls', 'calls'), ('retrieval_calls', 'calls'), ('retries', 'recovery cycles')]:
 METRICS['prepolicy_'+name] = (unit, 'policy_decision.details.'+name+'_used; direct pre-decision usage snapshot', 'B1/G1')

def hash_file(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for part in iter(lambda:f.read(1024*1024),b''): h.update(part)
 return h.hexdigest()

def json_hash(value):
 return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def tree_hash(root, exclude=()):
 files={str(p.relative_to(root)):hash_file(p) for p in sorted(Path(root).rglob('*'))
        if p.is_file() and not any(part in exclude for part in p.relative_to(root).parts)}
 return {'sha256':json_hash(files), 'files':len(files)}

def guard_snapshot():
 # Scoring and expert files are hashed only for mutation detection. Their
 # contents are never parsed, joined, exported, or used to select metrics.
 return {
  'raw_source':tree_hash(ROOT/'run_records'),
  'root_control_files':{p.name:hash_file(p) for p in sorted(ROOT.iterdir()) if p.is_file()},
  'existing_analysis':tree_hash(ROOT/'analysis', exclude=('__pycache__',)),
  'scoring_and_expert_artifacts':tree_hash(ROOT/'scoring', exclude=('node_modules','.netlify','__pycache__')),
  'corpus':tree_hash(REPO/'corpus', exclude=('__pycache__',)),
  'repo_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),
  'repo_status':subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=REPO,text=True),
 }

def write_csv(name, rows, fields=None):
 path=OUT/'data'/name
 path.parent.mkdir(parents=True,exist_ok=True)
 fields=fields or list(rows[0])
 with path.open('w',encoding='utf-8',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader(); writer.writerows(rows)

def read_csv(name):
 with (OUT/'data'/name).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))

def mean(values): return math.fsum(values)/len(values)

def metrics_rows(row):
 return {m:(float(row[m]) if row[m] not in [None,''] else None) for m in METRICS}
