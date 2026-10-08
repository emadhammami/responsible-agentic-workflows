#!/usr/bin/env python3
"""USN Option-C V3 evidence-preserving HTTP 503 continuation, provisional ratings.

No HTTP calls except the explicitly authorized `sentinel`, `bulk`, `resume` modes.
Does not edit source records, frozen R1-R11, or Git. Python stdlib only.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import tempfile
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError

SOURCE = Path.home() / 'primary-benchmark-results/PRIMARY-BENCHMARK-V1/scoring/scoring_package_v1/evaluator_A_blinded_270.jsonl'
EXPECTED_SHA = '3c2021037eeb39cec5ff90e212edf077fc17b3183e11ba2af44395b57ce26dec'
CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V3'
V2_CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V2'
V1_CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V1'
OUTPUT_TOKEN_LIMIT = 16384
R11_PATH = Path('scripts/r11_hosted_qualification.py')
R11_PROMPT = Path('evidence/engineering/r11_qualification_v1/prompt.txt')
R11_VALIDATOR = Path('evidence/engineering/r11_qualification_v1/frozen_validator.py')
PROTOCOL = Path('evidence/engineering/option_c_primary_503_continuation_v3_2026-10-08.md')
V2_RUNNER = Path('scripts/usn_option_c_primary_runner_v2.py')
V2_PROTOCOL = Path('evidence/engineering/option_c_primary_output_budget_v2_2026-10-08.md')
V2_EVIDENCE_FILES = ('freeze.json', 'status.json', 'requests.jsonl', 'attempt_results.jsonl',
                     'raw_responses.jsonl', 'completed.jsonl', 'private_id_map.json')
V2_COMPLETED_SLOTS = 5
V2_STOPPED_SLOT = 5
HTTP_503_ATTEMPT_LIMIT = 2
HTTP_503_RETRY_DELAY_SECS = 30
JUDGES = (('J1', 'cohere', 'command-a-plus-05-2026', 'COHERE_API_KEY'),
          ('J2', 'gemini', 'gemini-3.5-flash-lite', 'GEMINI_API_KEY'))
SEND_FIELDS = ('question', 'generated_output', 'reference_answer', 'reference_evidence', 'retrieved_evidence')
EXPECTED_ROWS = 270
TOTAL_SLOTS = EXPECTED_ROWS * len(JUDGES)
MIN_GAP_SECS = {'cohere': 3.2, 'gemini': 5.0}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(x):
    return json.dumps(x, ensure_ascii=True, sort_keys=True, separators=(',', ':'))


def now():
    return datetime.now(timezone.utc).isoformat()


def repo(*args):
    return subprocess.check_output(['git', *args], text=True, stderr=subprocess.DEVNULL).strip()


def load_r11():
    if not R11_PATH.is_file():
        raise RuntimeError('R11_TRANSPORT_NOT_FOUND')
    spec = importlib.util.spec_from_file_location('frozen_r11_readonly', R11_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_validator():
    spec = importlib.util.spec_from_file_location('frozen_r11_validator_readonly', R11_VALIDATOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def records():
    if not SOURCE.is_file() or digest(SOURCE.read_bytes()) != EXPECTED_SHA:
        raise RuntimeError('PRIMARY_SOURCE_SHA_MISMATCH')
    data = []
    for n, line in enumerate(SOURCE.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            raise RuntimeError(f'EMPTY_SOURCE_LINE_{n}')
        row = json.loads(line)
        if not isinstance(row, dict) or not all(k in row for k in SEND_FIELDS + ('evaluation_id',)):
            raise RuntimeError(f'BAD_SOURCE_SCHEMA_{n}')
        if not isinstance(row['evaluation_id'], str) or not row['evaluation_id']:
            raise RuntimeError(f'BAD_SOURCE_ID_{n}')
        if not isinstance(row['question'], str) or not isinstance(row['reference_answer'], str):
            raise RuntimeError(f'BAD_PRIMARY_QUESTION_OR_REFERENCE_{n}')
        if not isinstance(row['generated_output'], dict) or row['generated_output'].get('kind') not in ('answer', 'abstention'):
            raise RuntimeError(f'BAD_OUTPUT_KIND_{n}')
        if not isinstance(row['reference_evidence'], list) or not isinstance(row['retrieved_evidence'], list):
            raise RuntimeError(f'BAD_EVIDENCE_SCHEMA_{n}')
        if row['generated_output']['kind'] == 'abstention' and row['generated_output'].get('answer') is not None:
            raise RuntimeError(f'INVALID_PURE_ABSTENTION_{n}')
        if not set(row.get('judgment', {})).issuperset({'correctness_score', 'claim_judgments'}):
            raise RuntimeError(f'BAD_EMPTY_JUDGMENT_{n}')
        j = row['judgment']
        if any(j.get(k) is not None for k in ('correctness_score', 'correctness_reason', 'abstention_outcome')) or j.get('claim_judgments'):
            raise RuntimeError(f'PREEXISTING_JUDGMENTS_STOP_{n}')
        data.append(row)
    if len(data) != EXPECTED_ROWS or len({x['evaluation_id'] for x in data}) != EXPECTED_ROWS:
        raise RuntimeError('EXPECTED_270_UNIQUE_ROWS')
    return data


def mapped_payload(data, idx):
    row = data[idx]
    # Retain an opaque, position-based judge ID: never disclose source ID/task/condition.
    return {'evaluation_id': f'I{idx + 1:03d}', **{k: row[k] for k in SEND_FIELDS}}


def structure_report(data):
    p = [mapped_payload(data, i) for i in range(len(data))]
    if any(set(x) != set(SEND_FIELDS) | {'evaluation_id'} for x in p):
        raise RuntimeError('UNEXPECTED_SEND_FIELDS')
    # Detect explicit treatment-arm keys in nested payloads; inspect sources separately if found.
    def secret_key(x):
        if isinstance(x, dict):
            if any(str(k).casefold() in {'condition', 'arm', 'workflow', 'system_variant', 'baseline'} for k in x):
                return True
            return any(secret_key(v) for v in x.values())
        if isinstance(x, list):
            return any(secret_key(v) for v in x)
        return False
    if any(secret_key(x) for x in p):
        raise RuntimeError('POSSIBLE_ARM_METADATA_IN_SEND_PAYLOAD')
    print('INPUT_SHA256=' + EXPECTED_SHA)
    print(f'BLINDED_ITEMS={len(data)}')
    print('JUDGMENT_SOURCE_FIELDS_EXCLUDED=YES')
    print('ORIGINAL_EVALUATION_IDS_NOT_SENT=YES')
    print('TASK_IDS_AND_CONDITION_NOT_SENT=YES')
    print('OPAQUE_IDS=' + p[0]['evaluation_id'] + '..' + p[-1]['evaluation_id'])
    print('BOTH_JUDGES_SEE_SAME_BLINDED_ITEM=YES')
    print('MODEL_RESULTS_PROVISIONAL=YES')
    print('SOURCE_MUTATION=NO')
    print('API_REQUESTS=0')
    return p


def check_repo():
    if repo('branch', '--show-current') != 'research/b1-g1-real-execution-wiring':
        raise RuntimeError('WRONG_BRANCH')
    if repo('status', '--porcelain', '--untracked-files=all'):
        raise RuntimeError('DIRTY_WORKTREE_STOP')
    if not repo('ls-files', '--error-unmatch', 'scripts/usn_option_c_primary_runner_v3.py'):
        raise RuntimeError('RUNNER_NOT_COMMITTED')
    if not PROTOCOL.is_file() or not repo('ls-files', '--error-unmatch', str(PROTOCOL)):
        raise RuntimeError('PROTOCOL_NOT_COMMITTED')


def secure_new(p, obj):
    with p.open('x', encoding='utf-8') as f:
        f.write(canonical(obj) + '\n')
        f.flush()
        os.fsync(f.fileno())
    p.chmod(0o600)


def append(p, obj):
    with p.open('a', encoding='utf-8') as f:
        f.write(canonical(obj) + '\n')
        f.flush()
        os.fsync(f.fileno())
    p.chmod(0o600)


def read_lines(p):
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.is_file() else []


def replace_status(obj):
    dst = CAPSULE / 'status.json'
    tmp = CAPSULE / 'status.new'
    secure_new(tmp, obj)
    os.replace(tmp, dst)


def v2_evidence_snapshot():
    """Read-only qualification of the exact stopped V2 history before cloning it."""
    if not V2_CAPSULE.is_dir():
        raise RuntimeError('V2_CAPSULE_MISSING')
    if any(not (V2_CAPSULE / f).is_file() or (V2_CAPSULE / f).is_symlink()
           for f in V2_EVIDENCE_FILES):
        raise RuntimeError('V2_EVIDENCE_MISSING_OR_SYMLINK')
    frozen = json.loads((V2_CAPSULE / 'freeze.json').read_text())
    if frozen.get('input_sha256') != EXPECTED_SHA or frozen.get('output_token_limit') != OUTPUT_TOKEN_LIMIT:
        raise RuntimeError('V2_INPUT_OR_OUTPUT_BUDGET_MISMATCH')
    if not str(frozen.get('git_head','')).startswith('160bfd8'):
        raise RuntimeError('V2_ORIGIN_COMMIT_MISMATCH')
    paths = {'runner': V2_RUNNER, 'r11_transport': R11_PATH, 'prompt': R11_PROMPT,
             'validator': R11_VALIDATOR, 'protocol': V2_PROTOCOL}
    for key, path in paths.items():
        if not path.is_file() or digest(path.read_bytes()) != frozen['hashes'][key]:
            raise RuntimeError('V2_FROZEN_SOURCE_MISMATCH_' + key)
    if frozen.get('v1_failure_sha256') != v1_failure_snapshot():
        raise RuntimeError('V1_PROVENANCE_CHANGED')
    st = json.loads((V2_CAPSULE / 'status.json').read_text())
    if (st.get('state'), st.get('reason'), st.get('next_slot')) != ('STOPPED', 'HTTP_503', V2_STOPPED_SLOT):
        raise RuntimeError('V2_NOT_EXPECTED_STOPPED_503')
    req = read_lines(V2_CAPSULE / 'requests.jsonl')
    att = read_lines(V2_CAPSULE / 'attempt_results.jsonl')
    raw = read_lines(V2_CAPSULE / 'raw_responses.jsonl')
    done = read_lines(V2_CAPSULE / 'completed.jsonl')
    if not (len(req) == len(att) == 6 and len(raw) == len(done) == V2_COMPLETED_SLOTS):
        raise RuntimeError('V2_JOURNAL_COUNTS_MISMATCH')
    if ([r.get('slot') for r in req] != list(range(6)) or
            [r.get('slot') for r in att] != list(range(6)) or
            [r.get('slot') for r in raw] != list(range(5)) or
            [r.get('slot') for r in done] != list(range(5))):
        raise RuntimeError('V2_JOURNAL_ORDER_MISMATCH')
    if any(a.get('status') != 'HTTP_200' for a in att[:5]) or att[5].get('status') != 'HTTP_503':
        raise RuntimeError('V2_JOURNAL_HTTP_MISMATCH')
    if any(d.get('schema_ok') is not True or d.get('judgment') is None for d in done):
        raise RuntimeError('V2_COMPLETED_JUDGMENT_INVALID')
    if any(req[n].get('judge') != slot(n)[1][0] or
           raw[n].get('judge') != slot(n)[1][0] or
           done[n].get('judge') != slot(n)[1][0] for n in range(5)):
        raise RuntimeError('V2_COMPLETED_JUDGE_MISMATCH')
    if req[5].get('judge') != 'J2' or req[5].get('item') != 'I003':
        raise RuntimeError('V2_PENDING_JUDGE_OR_ITEM_MISMATCH')
    # Reject attempts with missing recorded outcome; never replay an ambiguous call.
    if any(a.get('status') is None or r.get('attempt') != 1 for r, a in zip(req, att)):
        raise RuntimeError('V2_AMBIGUOUS_ATTEMPT')
    return {f: digest((V2_CAPSULE / f).read_bytes()) for f in V2_EVIDENCE_FILES}


def check_prefix(snapshot):
    for name in ('requests.jsonl', 'attempt_results.jsonl', 'raw_responses.jsonl', 'completed.jsonl'):
        original = (V2_CAPSULE / name).read_bytes()
        newer = (CAPSULE / name).read_bytes()
        if digest(original) != snapshot[name] or not newer.startswith(original):
            raise RuntimeError('V2_JOURNAL_PREFIX_CHANGED_' + name)
    if digest((CAPSULE / 'private_id_map.json').read_bytes()) != snapshot['private_id_map.json']:
        raise RuntimeError('PRIVATE_ID_MAP_CHANGED')


def assert_freeze():
    manifest = json.loads((CAPSULE / 'freeze.json').read_text())
    paths = {'runner': Path(__file__), 'v2_runner': V2_RUNNER, 'v2_protocol': V2_PROTOCOL,
             'r11_transport': R11_PATH, 'prompt': R11_PROMPT,
             'validator': R11_VALIDATOR, 'protocol': PROTOCOL}
    for name, path in paths.items():
        if digest(path.read_bytes()) != manifest['hashes'][name]:
            raise RuntimeError('FROZEN_HASH_MISMATCH_' + name)
    if repo('rev-parse', 'HEAD') != manifest['git_head']:
        raise RuntimeError('FROZEN_GIT_HEAD_CHANGED')
    if manifest.get('v2_snapshot_sha256') != v2_evidence_snapshot():
        raise RuntimeError('V2_EVIDENCE_CHANGED')
    if manifest.get('input_sha256') != EXPECTED_SHA or manifest.get('output_token_limit') != OUTPUT_TOKEN_LIMIT:
        raise RuntimeError('V3_INPUT_OR_BUDGET_CHANGED')
    check_repo()
    data = records()
    check_prefix(manifest['v2_snapshot_sha256'])
    return data


def prepare():
    check_repo()
    data = records()
    structure_report(data)
    evidence = v2_evidence_snapshot()
    if CAPSULE.exists():
        raise RuntimeError('V3_CAPSULE_ALREADY_EXISTS_STOP')
    parent = CAPSULE.parent
    tempdir = Path(tempfile.mkdtemp(prefix='.OPTION-C-PRIMARY-V3-PREPARE-', dir=parent))
    tempdir.chmod(0o700)
    try:
        for name in V2_EVIDENCE_FILES:
            src = V2_CAPSULE / name
            dst = tempdir / name
            with dst.open('xb') as writer:
                writer.write(src.read_bytes())
                writer.flush()
                os.fsync(writer.fileno())
            dst.chmod(0o600)
            if digest(dst.read_bytes()) != evidence[name]:
                raise RuntimeError('COPY_HASH_MISMATCH_' + name)
        # Do not transport the V2 mutable state file into V3.
        (tempdir / 'status.json').unlink()
        paths = {'runner': Path(__file__), 'v2_runner': V2_RUNNER, 'v2_protocol': V2_PROTOCOL,
                 'r11_transport': R11_PATH, 'prompt': R11_PROMPT,
                 'validator': R11_VALIDATOR, 'protocol': PROTOCOL}
        secure_new(tempdir / 'freeze.json.v3', {
            'created_utc': now(), 'git_head': repo('rev-parse', 'HEAD'),
            'input_sha256': EXPECTED_SHA, 'items': EXPECTED_ROWS, 'slots': TOTAL_SLOTS,
            'method_status': 'PROVISIONAL_UNQUALIFIED_OPTION_C_V3_503_CONTINUATION',
            'output_token_limit': OUTPUT_TOKEN_LIMIT,
            'v2_snapshot_sha256': evidence, 'prior_completed_slots': V2_COMPLETED_SLOTS,
            'prior_failed_slot': V2_STOPPED_SLOT,
            'http_503_attempt_limit': HTTP_503_ATTEMPT_LIMIT,
            'judge_models': [{'code': x[0], 'provider': x[1], 'model': x[2]} for x in JUDGES],
            'hashes': {k: digest(v.read_bytes()) for k, v in paths.items()}
        })
        (tempdir / 'freeze.json').unlink()
        (tempdir / 'freeze.json.v3').rename(tempdir / 'freeze.json')
        secure_new(tempdir / 'status.json', {'state': 'READY_CONTINUE_503',
                   'next_slot': V2_STOPPED_SLOT, 'reason': 'HTTP_503', 'updated_utc': now()})
        if evidence != v2_evidence_snapshot():
            raise RuntimeError('V2_CHANGED_DURING_PREPARE')
        if CAPSULE.exists():
            raise RuntimeError('V3_TARGET_RACE_STOP')
        tempdir.rename(CAPSULE)
    finally:
        if tempdir.exists():
            shutil.rmtree(tempdir)
    print('V3_CAPSULE_PREPARED=PASS')
    print('INHERITED_VALID_JUDGMENTS=5')
    print('INHERITED_HTTP_503_ATTEMPTS=1')
    print('API_REQUESTS=0')


def status():
    p = CAPSULE / 'status.json'
    if not p.is_file():
        print('PRIMARY_STATUS=NOT_PREPARED')
    else:
        x = json.loads(p.read_text())
        print('PRIMARY_STATUS=' + x['state'])
        print('COMPLETED_SLOTS=' + str(len(read_lines(CAPSULE / 'completed.jsonl'))))
        print('NEXT_SLOT=' + str(x['next_slot']))
        if x.get('reason'):
            print('STOP_REASON=' + x['reason'])


def slot(n):
    idx, who = divmod(n, 2)
    return idx, JUDGES[who]


def assert_journal(next_slot, state):
    completed = read_lines(CAPSULE / 'completed.jsonl')
    intents = read_lines(CAPSULE / 'requests.jsonl')
    outcomes = read_lines(CAPSULE / 'attempt_results.jsonl')
    raw = read_lines(CAPSULE / 'raw_responses.jsonl')
    if len(completed) != next_slot or [x.get('slot') for x in completed] != list(range(next_slot)):
        raise RuntimeError('JOURNAL_COMPLETED_MISMATCH_STOP')
    if len(raw) != len(completed) or [x.get('slot') for x in raw] != list(range(next_slot)):
        raise RuntimeError('JOURNAL_RAW_MISMATCH_STOP')
    if any(x.get('schema_ok') is not True or x.get('judgment') is None for x in completed):
        raise RuntimeError('INVALID_PAST_JUDGMENT_STOP')
    if len(outcomes) != len(intents):
        raise RuntimeError('INFLIGHT_OR_AMBIGUOUS_REQUEST_STOP')
    if [x.get('slot') for x in intents] != [x.get('slot') for x in outcomes]:
        raise RuntimeError('REQUEST_OUTCOME_ORDER_MISMATCH')
    if any(not isinstance(x.get('slot'), int) or not 0 <= x['slot'] < TOTAL_SLOTS for x in intents):
        raise RuntimeError('BAD_REQUEST_JOURNAL_STOP')
    if any(intents[i]['slot'] > intents[i+1]['slot'] for i in range(len(intents)-1)):
        raise RuntimeError('NONMONOTONIC_SLOT_JOURNAL_STOP')
    for n in range(next_slot):
        ins = [x for x in intents if x['slot'] == n]
        outs = [x for x in outcomes if x['slot'] == n]
        if (not ins or len(ins) != len(outs) or
            any(x['status'] not in ('HTTP_429', 'HTTP_503') for x in outs[:-1]) or
            outs[-1].get('status') != 'HTTP_200'):
            raise RuntimeError('INCOMPLETE_PRIOR_SLOT_STOP')
        if sum(x['status'] == 'HTTP_503' for x in outs) > HTTP_503_ATTEMPT_LIMIT - 1:
            raise RuntimeError('EXCESS_503_RETRIES_STOP')
    pending = [x for x in intents if x['slot'] == next_slot]
    statuses = [x.get('status') for x in outcomes if x['slot'] == next_slot]
    if pending:
        if len(pending) != len(statuses) or any(s not in ('HTTP_429', 'HTTP_503') for s in statuses):
            raise RuntimeError('UNSAFE_PENDING_ATTEMPT_STOP')
        if state == 'READY_CONTINUE_503' and statuses != ['HTTP_503']:
            raise RuntimeError('INITIAL_V3_PENDING_STATE_MISMATCH')
        if state == 'PAUSED_429' and statuses[-1] != 'HTTP_429':
            raise RuntimeError('PAUSED_429_STATUS_MISMATCH')
        if state not in ('READY_CONTINUE_503', 'PAUSED_429', 'STOPPED'):
            raise RuntimeError('PENDING_SLOT_NOT_RESUMABLE')
    elif state in ('READY_CONTINUE_503', 'PAUSED_429'):
        raise RuntimeError('MISSING_EXPECTED_PENDING_ATTEMPT')
    if any(x['slot'] > next_slot for x in intents):
        raise RuntimeError('FUTURE_JOURNAL_SLOT_STOP')
    return intents, outcomes


def v1_failure_snapshot():
    # V2 is legal only after the single primary sentinel was truncated; V1 remains immutable.
    required = ('freeze.json', 'status.json', 'requests.jsonl',
                'attempt_results.jsonl', 'raw_responses.jsonl', 'completed.jsonl')
    if not V1_CAPSULE.is_dir() or any(not (V1_CAPSULE / n).is_file() for n in required):
        raise RuntimeError('V1_FAILURE_EVIDENCE_MISSING_STOP')
    status = json.loads((V1_CAPSULE / 'status.json').read_text())
    old_freeze = json.loads((V1_CAPSULE / 'freeze.json').read_text())
    if (status.get('state'), status.get('reason'), status.get('next_slot')) != (
            'STOPPED', 'INVALID_JUDGMENT_SCHEMA', 1):
        raise RuntimeError('V1_NOT_EXPECTED_STOPPED_STATE')
    if old_freeze.get('input_sha256') != EXPECTED_SHA:
        raise RuntimeError('V1_INPUT_IDENTITY_MISMATCH')
    req = read_lines(V1_CAPSULE / 'requests.jsonl')
    att = read_lines(V1_CAPSULE / 'attempt_results.jsonl')
    raw = read_lines(V1_CAPSULE / 'raw_responses.jsonl')
    done = read_lines(V1_CAPSULE / 'completed.jsonl')
    if not (len(req) == len(att) == len(raw) == len(done) == 1):
        raise RuntimeError('V1_JOURNAL_COUNTS_MISMATCH')
    if not (req[0].get('slot') == att[0].get('slot') == raw[0].get('slot') == done[0].get('slot') == 0
            and req[0].get('judge') == raw[0].get('judge') == done[0].get('judge') == 'J1'
            and att[0].get('status') == 'HTTP_200'
            and raw[0].get('raw', {}).get('finish_reason') == 'MAX_TOKENS'
            and done[0].get('schema_ok') is False and done[0].get('judgment') is None):
        raise RuntimeError('V1_FAILURE_NOT_MAX_TOKENS_STOP')
    return {n: digest((V1_CAPSULE / n).read_bytes()) for n in required}


def request_for_v2(transport, provider, model, prompt, case):
    # Frozen R11 serializer, model, prompt, temperature and response format unchanged.
    url, payload = transport.request_for(provider, model, prompt, case)
    if provider == 'cohere':
        if payload.get('max_tokens') != 4096:
            raise RuntimeError('V1_OUTPUT_LIMIT_UNEXPECTED')
        payload['max_tokens'] = OUTPUT_TOKEN_LIMIT
    elif provider == 'gemini':
        config = payload.get('generationConfig', {})
        if config.get('maxOutputTokens') != 4096:
            raise RuntimeError('V1_OUTPUT_LIMIT_UNEXPECTED')
        config['maxOutputTokens'] = OUTPUT_TOKEN_LIMIT
    else:
        raise RuntimeError('UNKNOWN_PROVIDER')
    return url, payload


def usage(provider, raw):
    if provider == 'cohere':
        v = raw.get('usage') or raw.get('meta', {}).get('billed_units', {})
        return v if isinstance(v, dict) else {}
    x = raw.get('usageMetadata', {})
    return x if isinstance(x, dict) else {}


def run(kind):
    data = assert_freeze()
    stat = json.loads((CAPSULE / 'status.json').read_text())
    allowed = {'continue': ('READY_CONTINUE_503',), 'resume': ('PAUSED_429',)}
    if stat['state'] not in allowed[kind]:
        raise RuntimeError('INVALID_STAGE_' + kind)
    if os.environ.get('USN_PRIMARY_FREE_CONFIRMED') != 'YES':
        raise RuntimeError('FREE_TIER_NOT_CONFIRMED_STOP')
    if os.environ.get('USN_PRIMARY_DATA_SHARING_AUTHORIZED') != 'YES':
        raise RuntimeError('EXTERNAL_DATA_SHARING_NOT_AUTHORIZED_STOP')
    if any(not os.environ.get(x[3]) for x in JUDGES):
        raise RuntimeError('MISSING_API_KEY_STOP')
    if kind == 'continue' and os.environ.get('USN_EXPLICIT_V3_503_CONTINUATION') != 'YES':
        raise RuntimeError('V3_503_CONTINUATION_NOT_AUTHORIZED')
    if kind == 'resume' and os.environ.get('USN_EXPLICIT_429_RESUME') != 'YES':
        raise RuntimeError('429_RESUME_NOT_AUTHORIZED')
    transport = load_r11()
    validator = load_validator()
    prompt = R11_PROMPT.read_text()
    start = stat['next_slot']
    intents, outcomes = assert_journal(start, stat['state'])
    sent_last = {}
    for n in range(start, TOTAL_SLOTS):
        idx, (code, provider, model, env) = slot(n)
        case = mapped_payload(data, idx)
        url, payload = request_for_v2(transport, provider, model, prompt, case)
        payload_hash = digest(transport.encode(payload).encode('utf-8'))
        prior = [x for x in intents if x['slot'] == n]
        prior_outcomes = [x for x in outcomes if x['slot'] == n]
        if prior and any(x.get('payload_sha256') != payload_hash for x in prior):
            raise RuntimeError('CHANGED_RETRY_PAYLOAD_STOP')
        if prior and (len(prior) != len(prior_outcomes) or
            any(x.get('status') not in ('HTTP_429', 'HTTP_503') for x in prior_outcomes)):
            raise RuntimeError('AMBIGUOUS_OR_SUCCESSFUL_SLOT_REPLAY_STOP')
        while True:
            # One extra attempt only for any journaled 503; never retry timeouts/ambiguous failures.
            if sum(x['status'] == 'HTTP_503' for x in prior_outcomes) >= HTTP_503_ATTEMPT_LIMIT:
                raise RuntimeError('HTTP_503_ATTEMPT_BUDGET_EXHAUSTED')
            if provider in sent_last:
                wait = MIN_GAP_SECS[provider] - (time.monotonic() - sent_last[provider])
                if wait > 0:
                    time.sleep(wait)
            append(CAPSULE / 'requests.jsonl', {
                'slot': n, 'judge': code, 'item': case['evaluation_id'],
                'payload_sha256': payload_hash, 'requested_utc': now(),
                'attempt': len(prior) + 1})
            tic = time.monotonic()
            try:
                raw = transport.send_one(url, payload, provider, os.environ[env])
            except HTTPError as err:
                code_http = err.code
                err.close()
                result = {'slot': n, 'status': 'HTTP_' + str(code_http),
                          'elapsed_seconds': round(time.monotonic() - tic, 4),
                          'finished_utc': now()}
                append(CAPSULE / 'attempt_results.jsonl', result)
                sent_last[provider] = time.monotonic()
                outcomes.append(result)
                prior_outcomes.append(result)
                prior.append({'slot': n, 'payload_sha256': payload_hash})
                if code_http == 503 and sum(x['status'] == 'HTTP_503' for x in prior_outcomes) < HTTP_503_ATTEMPT_LIMIT:
                    print(f'PRIMARY_V3_503_RETRY={code}|SLOT={n}|WAIT_SEC={HTTP_503_RETRY_DELAY_SECS}', flush=True)
                    time.sleep(HTTP_503_RETRY_DELAY_SECS)
                    continue
                replace_status({'state': 'PAUSED_429' if code_http == 429 else 'STOPPED',
                                'next_slot': n, 'reason': 'HTTP_' + str(code_http),
                                'updated_utc': now()})
                print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|HTTP_{code_http}', flush=True)
                return 2
            except Exception as err:
                result = {'slot': n, 'status': 'TRANSPORT_' + type(err).__name__,
                          'elapsed_seconds': round(time.monotonic() - tic, 4),
                          'finished_utc': now()}
                append(CAPSULE / 'attempt_results.jsonl', result)
                replace_status({'state': 'STOPPED', 'next_slot': n,
                                'reason': 'TRANSPORT_' + type(err).__name__, 'updated_utc': now()})
                print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|TRANSPORT_{type(err).__name__}', flush=True)
                return 2
            break
        elapsed = round(time.monotonic() - tic, 4)
        sent_last[provider] = time.monotonic()
        append(CAPSULE / 'attempt_results.jsonl', {
            'slot': n, 'status': 'HTTP_200', 'elapsed_seconds': elapsed,
            'finished_utc': now()})
        append(CAPSULE / 'raw_responses.jsonl', {
            'slot': n, 'judge': code, 'item': case['evaluation_id'],
            'payload_sha256': payload_hash, 'raw': raw,
            'response_sha256': digest(transport.encode(raw).encode()),
            'usage': usage(provider, raw), 'elapsed_seconds': elapsed})
        try:
            judgment = transport.strict_json(transport.final_text(provider, raw))
            valid = validator.valid(judgment, case['evaluation_id'])
            if case['generated_output']['kind'] == 'abstention' and valid:
                valid = judgment['claim_judgments'] == []
            if case['generated_output']['kind'] == 'answer' and valid and case['generated_output'].get('answer'):
                valid = len(judgment['claim_judgments']) >= 1
        except Exception:
            judgment = None
            valid = False
        append(CAPSULE / 'completed.jsonl', {
            'slot': n, 'judge': code, 'item': case['evaluation_id'],
            'schema_ok': valid, 'judgment': judgment,
            'response_sha256': digest(transport.encode(raw).encode()),
            'elapsed_seconds': elapsed})
        state = 'RUNNING' if n + 1 < TOTAL_SLOTS else 'COMPLETE'
        replace_status({'state': state, 'next_slot': n + 1, 'updated_utc': now()})
        print(f'PRIMARY_RESULT={code}|SLOT={n+1}/{TOTAL_SLOTS}|SCHEMA={int(valid)}|SECONDS={elapsed:.2f}', flush=True)
        if not valid:
            replace_status({'state': 'STOPPED', 'next_slot': n + 1,
                            'reason': 'INVALID_JUDGMENT_SCHEMA', 'updated_utc': now()})
            print('PRIMARY_STOP=INVALID_JUDGMENT_SCHEMA', flush=True)
            return 2
    print('PRIMARY_STAGE=COMPLETE')
    return 0


def mock_test():
    # No real data, credential access, files written, or network calls.
    example = {'evaluation_id': 'I001', 'question': 'What is the policy?',
               'generated_output': {'kind': 'answer', 'answer': 'The limit is 10.'},
               'reference_answer': 'The limit is ten.',
               'reference_evidence': [{'text': 'The limit is ten.'}],
               'retrieved_evidence': [{'text': 'The limit is ten.'}]}
    transport = load_r11()
    validator = load_validator()
    assert validator.valid({'evaluation_id': 'I001', 'correctness_score': 2,
                            'correctness_reason': 'match', 'abstention_outcome': 'not_applicable',
                            'claim_judgments': [{'claim_text': 'The limit is 10',
                                                 'label': 'SUPPORTED', 'reason': 'match'}],
                            'evaluator_notes': ''}, 'I001')
    for _, provider, model, _ in JUDGES:
        url, payload = request_for_v2(transport, provider, model, R11_PROMPT.read_text(), example)
        assert url.startswith('https://') and example['evaluation_id'] in transport.encode(payload)
        assert (payload['max_tokens'] if provider == 'cohere' else payload['generationConfig']['maxOutputTokens']) == OUTPUT_TOKEN_LIMIT
        assert 'COHERE_API_KEY' not in transport.encode(payload)
        assert 'GEMINI_API_KEY' not in transport.encode(payload)
    assert [slot(n)[1][0] for n in range(4)] == ['J1', 'J2', 'J1', 'J2']
    print('V3_OFFLINE_MOCK_TEST=PASS')
    print('NETWORK_REQUESTS=0')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('audit', 'mock-test', 'prepare', 'verify', 'status', 'continue', 'resume'))
    a = parser.parse_args()
    if a.mode == 'audit':
        structure_report(records())
    elif a.mode == 'mock-test':
        mock_test()
    elif a.mode == 'prepare':
        prepare()
    elif a.mode == 'verify':
        assert_freeze()
        state = json.loads((CAPSULE / 'status.json').read_text())
        assert_journal(state['next_slot'], state['state'])
        print('PRIMARY_FROZEN_VERIFY=PASS')
        print('API_REQUESTS_BY_THIS_VERIFY=0')
    elif a.mode == 'status':
        status()
    else:
        return run(a.mode)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        # Never echo source text, response bodies, API keys, or provider error payloads.
        print('PRIMARY_ERROR=' + type(exc).__name__ + ':' + str(exc)[:100])
        sys.exit(1)
