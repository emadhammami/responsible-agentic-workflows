#!/usr/bin/env python3
"""Option C V4: journal-preserving continuation after a schema-invalid judgment.

V3 and all older benchmark/qualification evidence remain read-only. This
continuation records schema-invalid outputs as missing judgments, never valid
quality scores, and never replays a completed HTTP 200 slot.
"""
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError

BASE = Path('scripts/usn_option_c_primary_runner_v3.py')
V3_PROTOCOL = Path('evidence/engineering/option_c_primary_503_continuation_v3_2026-10-08.md')
PROTOCOL = Path('evidence/engineering/option_c_primary_missing_judgment_v4_2026-10-08.md')
V3_CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V3'
CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V4'
COPY_FILES = ('freeze.json', 'status.json', 'requests.jsonl', 'attempt_results.jsonl',
              'raw_responses.jsonl', 'completed.jsonl', 'private_id_map.json')
V3_PRIOR_SLOTS = 18
LAST_INVALID_SLOT = 17
V3_HEAD_PREFIX = 'de6fb0b'


def v3():
    spec = importlib.util.spec_from_file_location('option_c_v3_readonly', BASE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(b):
    return hashlib.sha256(b).hexdigest()


def canonical(x):
    return json.dumps(x, ensure_ascii=True, sort_keys=True, separators=(',', ':'))


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    return subprocess.check_output(['git', *args], text=True, stderr=subprocess.DEVNULL).strip()


def check_git():
    if git('branch', '--show-current') != 'research/b1-g1-real-execution-wiring':
        raise RuntimeError('WRONG_BRANCH')
    if git('status', '--porcelain', '--untracked-files=all'):
        raise RuntimeError('DIRTY_WORKTREE_STOP')
    for name in ('scripts/usn_option_c_primary_runner_v4.py', str(PROTOCOL)):
        git('ls-files', '--error-unmatch', name)


def rows(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()] if p.is_file() else []


def newfile(path, obj):
    with path.open('x', encoding='utf-8') as f:
        f.write(canonical(obj) + '\n')
        f.flush(); os.fsync(f.fileno())
    path.chmod(0o600)


def append(path, obj):
    with path.open('a', encoding='utf-8') as f:
        f.write(canonical(obj) + '\n')
        f.flush(); os.fsync(f.fileno())
    path.chmod(0o600)


def status_write(obj):
    dest = CAPSULE / 'status.json'
    temp = CAPSULE / 'status.tmp.v4'
    newfile(temp, obj)
    os.replace(temp, dest)


def schema_check(j, case, validator):
    if not validator.valid(j, case['evaluation_id']):
        return False, 'FROZEN_VALIDATOR_REJECTED'
    claims = j['claim_judgments']
    if case['generated_output']['kind'] == 'abstention' and claims:
        return False, 'ABSTENTION_WITH_CLAIMS'
    if case['generated_output']['kind'] == 'answer' and case['generated_output'].get('answer') and not claims:
        return False, 'ANSWER_WITHOUT_CLAIMS'
    return True, None


def v3_snapshot():
    """Prove exact stopped V3 provenance; do not execute V3.verify after V4 HEAD."""
    b = v3()
    if not V3_CAPSULE.is_dir() or any(not (V3_CAPSULE / n).is_file() or
                                     (V3_CAPSULE / n).is_symlink() for n in COPY_FILES):
        raise RuntimeError('V3_EVIDENCE_MISSING')
    f = json.loads((V3_CAPSULE / 'freeze.json').read_text())
    if not str(f.get('git_head', '')).startswith(V3_HEAD_PREFIX):
        raise RuntimeError('V3_HEAD_MISMATCH')
    subprocess.run(['git', 'merge-base', '--is-ancestor', f['git_head'], 'HEAD'], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    files = {'runner': BASE, 'v2_runner': b.V2_RUNNER, 'v2_protocol': b.V2_PROTOCOL,
             'r11_transport': b.R11_PATH, 'prompt': b.R11_PROMPT,
             'validator': b.R11_VALIDATOR, 'protocol': V3_PROTOCOL}
    for key, p in files.items():
        if not p.is_file() or sha(p.read_bytes()) != f['hashes'].get(key):
            raise RuntimeError('V3_FROZEN_FILE_CHANGED_' + key)
    if f.get('input_sha256') != b.EXPECTED_SHA or f.get('output_token_limit') != b.OUTPUT_TOKEN_LIMIT:
        raise RuntimeError('V3_FROZEN_INPUT_CHANGED')
    if b.v2_evidence_snapshot() != f.get('v2_snapshot_sha256'):
        raise RuntimeError('V2_PROVENANCE_CHANGED')
    b.check_prefix(f['v2_snapshot_sha256'])
    st = json.loads((V3_CAPSULE / 'status.json').read_text())
    if (st.get('state'), st.get('reason'), st.get('next_slot')) != ('STOPPED', 'INVALID_JUDGMENT_SCHEMA', V3_PRIOR_SLOTS):
        raise RuntimeError('V3_NOT_EXPECTED_STOP')
    req = rows(V3_CAPSULE / 'requests.jsonl')
    att = rows(V3_CAPSULE / 'attempt_results.jsonl')
    raw = rows(V3_CAPSULE / 'raw_responses.jsonl')
    done = rows(V3_CAPSULE / 'completed.jsonl')
    if not (len(req) == len(att) == V3_PRIOR_SLOTS + 1 and
            len(raw) == len(done) == V3_PRIOR_SLOTS):
        raise RuntimeError('V3_JOURNAL_COUNTS_MISMATCH')
    expected_requests = list(range(6)) + list(range(5, V3_PRIOR_SLOTS))
    if [x.get('slot') for x in req] != expected_requests or [x.get('slot') for x in att] != expected_requests:
        raise RuntimeError('V3_REQUEST_ORDER_MISMATCH')
    if [x.get('slot') for x in raw] != list(range(V3_PRIOR_SLOTS)) or \
       [x.get('slot') for x in done] != list(range(V3_PRIOR_SLOTS)):
        raise RuntimeError('V3_COMPLETED_ORDER_MISMATCH')
    if [x.get('status') for x in att] != ['HTTP_200']*5 + ['HTTP_503'] + ['HTTP_200']*(V3_PRIOR_SLOTS-5):
        raise RuntimeError('V3_HTTP_HISTORY_MISMATCH')
    if any(x.get('schema_ok') is not True for x in done[:LAST_INVALID_SLOT]):
        raise RuntimeError('V3_PREFIX_INVALID')
    if done[-1].get('schema_ok') is not False or done[-1].get('judge') != 'J2' or done[-1].get('item') != 'I009':
        raise RuntimeError('V3_INVALID_SLOT_MISMATCH')
    data = b.records()
    case = b.mapped_payload(data, LAST_INVALID_SLOT // 2)
    valid, reason = schema_check(done[-1].get('judgment'), case, b.load_validator())
    if valid or reason != 'ANSWER_WITHOUT_CLAIMS':
        raise RuntimeError('V3_ROOT_CAUSE_NOT_MATCHED')
    if any(x.get('judge') != b.slot(n)[1][0] for n,x in enumerate(done)):
        raise RuntimeError('V3_JUDGE_ORDER_MISMATCH')
    if any(raw[n].get('response_sha256') != done[n].get('response_sha256') for n in range(len(done))):
        raise RuntimeError('V3_RESPONSE_HASH_MISMATCH')
    return {name: sha((V3_CAPSULE / name).read_bytes()) for name in COPY_FILES}


def check_v3_prefix(snap):
    for n in ('requests.jsonl', 'attempt_results.jsonl', 'raw_responses.jsonl', 'completed.jsonl'):
        original = (V3_CAPSULE / n).read_bytes()
        if sha(original) != snap[n] or not (CAPSULE / n).read_bytes().startswith(original):
            raise RuntimeError('V3_JOURNAL_PREFIX_CHANGED_' + n)
    if sha((CAPSULE / 'private_id_map.json').read_bytes()) != snap['private_id_map.json']:
        raise RuntimeError('V3_ID_MAP_CHANGED')


def prepare():
    check_git()
    b = v3(); data = b.records(); b.structure_report(data)
    snap = v3_snapshot()
    if CAPSULE.exists():
        raise RuntimeError('V4_CAPSULE_ALREADY_EXISTS')
    t = Path(tempfile.mkdtemp(prefix='.OPTION-C-V4-PREPARE-', dir=CAPSULE.parent))
    t.chmod(0o700)
    try:
        for n in COPY_FILES:
            dst = t / n
            with dst.open('xb') as f:
                f.write((V3_CAPSULE / n).read_bytes()); f.flush(); os.fsync(f.fileno())
            dst.chmod(0o600)
            if sha(dst.read_bytes()) != snap[n]:
                raise RuntimeError('V3_COPY_MISMATCH_' + n)
        (t / 'freeze.json').unlink(); (t / 'status.json').unlink()
        hashes = {'runner': sha(Path(__file__).read_bytes()), 'protocol': sha(PROTOCOL.read_bytes()),
                  'v3_runner': sha(BASE.read_bytes()), 'v3_protocol': sha(V3_PROTOCOL.read_bytes())}
        newfile(t / 'freeze.json', {'created_utc':now(), 'git_head':git('rev-parse','HEAD'),
            'input_sha256':b.EXPECTED_SHA, 'judges':b.JUDGES, 'output_limit':b.OUTPUT_TOKEN_LIMIT,
            'v3_snapshot_sha256':snap, 'hashes':hashes,
            'method_status':'PROVISIONAL_WITH_INVALID_MISSING_V4', 'prior_attempted_slots':V3_PRIOR_SLOTS,
            'prior_valid_slots':V3_PRIOR_SLOTS-1, 'prior_invalid_slot':LAST_INVALID_SLOT})
        newfile(t / 'status.json', {'state':'READY_CONTINUE_INVALID','next_slot':V3_PRIOR_SLOTS,
                                  'reason':'ANSWER_WITHOUT_CLAIMS','updated_utc':now()})
        if snap != v3_snapshot():
            raise RuntimeError('V3_CHANGED_DURING_PREPARE')
        t.rename(CAPSULE)
    finally:
        if t.exists():
            shutil.rmtree(t)
    print('V4_CAPSULE_PREPARED=PASS')
    print('INHERITED_COMPLETED_SLOTS=18')
    print('INHERITED_SCHEMA_VALID=17')
    print('INHERITED_SCHEMA_INVALID=1')
    print('API_REQUESTS=0')


def assert_freeze():
    check_git(); b = v3()
    f = json.loads((CAPSULE / 'freeze.json').read_text())
    if git('rev-parse', 'HEAD') != f.get('git_head'):
        raise RuntimeError('V4_GIT_HEAD_CHANGED')
    files = {'runner':Path(__file__), 'protocol':PROTOCOL, 'v3_runner':BASE, 'v3_protocol':V3_PROTOCOL}
    if any(not p.is_file() or sha(p.read_bytes()) != f['hashes'].get(key) for key, p in files.items()):
        raise RuntimeError('V4_FROZEN_FILES_CHANGED')
    if f.get('input_sha256') != b.EXPECTED_SHA or f.get('output_limit') != b.OUTPUT_TOKEN_LIMIT:
        raise RuntimeError('V4_INPUT_CHANGED')
    if v3_snapshot() != f.get('v3_snapshot_sha256'):
        raise RuntimeError('V3_EVIDENCE_CHANGED')
    check_v3_prefix(f['v3_snapshot_sha256'])
    return b, b.records()


def check_journal(b, data, next_slot, state):
    req = rows(CAPSULE / 'requests.jsonl'); att = rows(CAPSULE / 'attempt_results.jsonl')
    raw = rows(CAPSULE / 'raw_responses.jsonl'); done = rows(CAPSULE / 'completed.jsonl')
    if not (len(req) == len(att) and len(raw) == len(done) == next_slot):
        raise RuntimeError('V4_JOURNAL_COUNTS_MISMATCH')
    if any(x.get('slot') != n for n,x in enumerate(raw)) or any(x.get('slot') != n for n,x in enumerate(done)):
        raise RuntimeError('V4_COMPLETION_ORDER_MISMATCH')
    if [x.get('slot') for x in req] != [x.get('slot') for x in att]:
        raise RuntimeError('V4_REQUEST_RESULT_ORDER_MISMATCH')
    if any(req[i]['slot'] > req[i+1]['slot'] for i in range(len(req)-1)):
        raise RuntimeError('V4_NONMONOTONIC_INTENTS')
    validator = b.load_validator()
    for n in range(next_slot):
        earlier = [x for x in req if x['slot'] == n]
        results = [x for x in att if x['slot'] == n]
        if (not earlier or len(earlier) != len(results) or results[-1].get('status') != 'HTTP_200'
            or any(x.get('status') not in ('HTTP_429','HTTP_503') for x in results[:-1])):
            raise RuntimeError('V4_UNEXPECTED_COMPLETED_HISTORY')
        if sum(x.get('status') == 'HTTP_503' for x in results) > 1:
            raise RuntimeError('V4_503_LIMIT_BREACH')
        case = b.mapped_payload(data, n//2)
        if (done[n].get('judge') != b.slot(n)[1][0] or raw[n].get('judge') != b.slot(n)[1][0]
            or done[n].get('item') != case['evaluation_id'] or raw[n].get('item') != case['evaluation_id']
            or raw[n].get('response_sha256') != done[n].get('response_sha256')):
            raise RuntimeError('V4_COMPLETED_CONTENT_MISMATCH')
        valid, _ = schema_check(done[n].get('judgment'), case, validator)
        if valid is not done[n].get('schema_ok'):
            raise RuntimeError('V4_JUDGMENT_VALIDITY_CHANGED')
    pending_req = [x for x in req if x['slot'] == next_slot]
    pending_att = [x for x in att if x['slot'] == next_slot]
    if any(x['slot'] > next_slot for x in req):
        raise RuntimeError('V4_FUTURE_REQUESTS')
    if pending_req:
        if len(pending_req) != len(pending_att) or any(x.get('status') not in ('HTTP_429','HTTP_503') for x in pending_att):
            raise RuntimeError('V4_UNSAFE_PENDING')
        if state != 'PAUSED_429' or pending_att[-1]['status'] != 'HTTP_429':
            raise RuntimeError('V4_PENDING_NOT_RESUMABLE')
    elif state == 'PAUSED_429':
        raise RuntimeError('V4_MISSING_PENDING_429')
    return req, att, done


def status():
    p = CAPSULE / 'status.json'
    if not p.is_file():
        print('PRIMARY_STATUS=NOT_PREPARED'); return
    s = json.loads(p.read_text())
    done = rows(CAPSULE / 'completed.jsonl')
    print('PRIMARY_STATUS=' + s['state'])
    print('COMPLETED_SLOTS=' + str(len(done)))
    print('VALID_JUDGMENTS=' + str(sum(x.get('schema_ok') is True for x in done)))
    print('INVALID_JUDGMENTS=' + str(sum(x.get('schema_ok') is False for x in done)))
    print('NEXT_SLOT=' + str(s['next_slot']))
    if s.get('reason'):
        print('STOP_REASON=' + s['reason'])


def run(kind):
    b, data = assert_freeze()
    st = json.loads((CAPSULE / 'status.json').read_text())
    if st['state'] not in {'continue': ('READY_CONTINUE_INVALID',), 'resume':('PAUSED_429',)}[kind]:
        raise RuntimeError('V4_INVALID_STAGE')
    for gate in ('USN_PRIMARY_FREE_CONFIRMED','USN_PRIMARY_DATA_SHARING_AUTHORIZED'):
        if os.environ.get(gate) != 'YES':
            raise RuntimeError('NOT_AUTHORIZED_' + gate)
    if os.environ.get('USN_EXPLICIT_V4_INVALID_CONTINUATION') != 'YES' and kind == 'continue':
        raise RuntimeError('V4_NOT_EXPLICITLY_AUTHORIZED')
    if os.environ.get('USN_EXPLICIT_429_RESUME') != 'YES' and kind == 'resume':
        raise RuntimeError('429_NOT_EXPLICITLY_AUTHORIZED')
    if any(not os.environ.get(j[3]) for j in b.JUDGES):
        raise RuntimeError('MISSING_API_KEY')
    req, att, done = check_journal(b, data, st['next_slot'], st['state'])
    transport = b.load_r11(); validator = b.load_validator()
    prompt = b.R11_PROMPT.read_text()
    sent_last = {}
    for n in range(st['next_slot'], b.TOTAL_SLOTS):
        idx, (code, provider, model, env) = b.slot(n)
        case = b.mapped_payload(data, idx)
        url, payload = b.request_for_v2(transport, provider, model, prompt, case)
        payload_hash = sha(transport.encode(payload).encode('utf-8'))
        prior_req = [x for x in req if x['slot'] == n]
        prior_att = [x for x in att if x['slot'] == n]
        if prior_req and any(x.get('payload_sha256') != payload_hash for x in prior_req):
            raise RuntimeError('CHANGED_RETRY_PAYLOAD')
        if prior_req and (len(prior_req) != len(prior_att) or
                          any(x.get('status') not in ('HTTP_429','HTTP_503') for x in prior_att)):
            raise RuntimeError('UNSAFE_RETRY')
        while True:
            if sum(a.get('status') == 'HTTP_503' for a in prior_att) >= b.HTTP_503_ATTEMPT_LIMIT:
                raise RuntimeError('HTTP_503_BUDGET_EXHAUSTED')
            if provider in sent_last:
                wait = b.MIN_GAP_SECS[provider] - (time.monotonic() - sent_last[provider])
                if wait > 0:
                    time.sleep(wait)
            attempt = {'slot':n,'judge':code,'item':case['evaluation_id'],
                       'payload_sha256':payload_hash,'requested_utc':now(),'attempt':len(prior_req)+1}
            append(CAPSULE / 'requests.jsonl', attempt)
            req.append(attempt)
            tic = time.monotonic()
            try:
                response = transport.send_one(url, payload, provider, os.environ[env])
            except HTTPError as err:
                http = err.code; err.close()
                res = {'slot':n,'status':'HTTP_'+str(http),
                       'elapsed_seconds':round(time.monotonic()-tic,4),'finished_utc':now()}
                append(CAPSULE / 'attempt_results.jsonl', res); att.append(res)
                prior_req.append(attempt); prior_att.append(res)
                sent_last[provider] = time.monotonic()
                if http == 503 and sum(x['status']=='HTTP_503' for x in prior_att) < b.HTTP_503_ATTEMPT_LIMIT:
                    print(f'PRIMARY_V4_503_RETRY={code}|SLOT={n}|WAIT_SEC={b.HTTP_503_RETRY_DELAY_SECS}',flush=True)
                    time.sleep(b.HTTP_503_RETRY_DELAY_SECS)
                    continue
                status_write({'state':'PAUSED_429' if http==429 else 'STOPPED',
                              'next_slot':n,'reason':'HTTP_'+str(http),'updated_utc':now()})
                print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|HTTP_{http}',flush=True)
                return 2
            except Exception as err:
                res = {'slot':n,'status':'TRANSPORT_'+type(err).__name__,
                       'elapsed_seconds':round(time.monotonic()-tic,4),'finished_utc':now()}
                append(CAPSULE / 'attempt_results.jsonl',res); att.append(res)
                status_write({'state':'STOPPED','next_slot':n,
                              'reason':'TRANSPORT_'+type(err).__name__,'updated_utc':now()})
                print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|TRANSPORT_{type(err).__name__}',flush=True)
                return 2
            break
        elapsed = round(time.monotonic()-tic,4)
        sent_last[provider] = time.monotonic()
        res = {'slot':n,'status':'HTTP_200','elapsed_seconds':elapsed,'finished_utc':now()}
        append(CAPSULE / 'attempt_results.jsonl',res); att.append(res)
        raw = {'slot':n,'judge':code,'item':case['evaluation_id'],
               'payload_sha256':payload_hash,'raw':response,
               'response_sha256':sha(transport.encode(response).encode()),
               'usage':b.usage(provider,response),'elapsed_seconds':elapsed}
        append(CAPSULE / 'raw_responses.jsonl',raw)
        try:
            judgment = transport.strict_json(transport.final_text(provider,response))
            good, reason = schema_check(judgment,case,validator)
        except Exception:
            judgment = None; good = False; reason = 'RESPONSE_EXTRACTION_OR_JSON_FAILED'
        completion = {'slot':n,'judge':code,'item':case['evaluation_id'],
                      'schema_ok':good,'judgment':judgment,'response_sha256':raw['response_sha256'],
                      'elapsed_seconds':elapsed,'invalid_reason':reason}
        append(CAPSULE / 'completed.jsonl',completion)
        done.append(completion)
        final = n + 1 == b.TOTAL_SLOTS
        new_state = ('COMPLETE_WITH_INVALID' if any(x.get('schema_ok') is False for x in done)
                     else 'COMPLETE') if final else 'RUNNING'
        status_write({'state':new_state,'next_slot':n+1,'updated_utc':now()})
        print(f'PRIMARY_RESULT={code}|SLOT={n+1}/{b.TOTAL_SLOTS}|SCHEMA={int(good)}|SECONDS={elapsed:.2f}',flush=True)
        if not good:
            print(f'PRIMARY_JUDGMENT_MISSING={code}|SLOT={n+1}|REASON={reason}',flush=True)
    print('PRIMARY_STAGE=COMPLETE_WITH_INVALID')
    return 0


def mock_test():
    b = v3()
    assert b.OUTPUT_TOKEN_LIMIT == 16384
    assert b.JUDGES[0][2] == 'command-a-plus-05-2026'
    assert b.JUDGES[1][2] == 'gemini-3.5-flash-lite'
    print('V4_OFFLINE_MOCK_TEST=PASS')
    print('NETWORK_REQUESTS=0')


def main():
    import argparse
    a = argparse.ArgumentParser()
    a.add_argument('mode',choices=('mock-test','prepare','verify','status','continue','resume'))
    mode = a.parse_args().mode
    if mode == 'mock-test': mock_test()
    elif mode == 'prepare': prepare()
    elif mode == 'status': status()
    elif mode == 'verify':
        b,data=assert_freeze(); state=json.loads((CAPSULE/'status.json').read_text())
        check_journal(b,data,state['next_slot'],state['state'])
        print('PRIMARY_FROZEN_VERIFY=PASS'); print('API_REQUESTS_BY_THIS_VERIFY=0')
    else: return run(mode)
    return 0

if __name__ == '__main__':
    try: sys.exit(main())
    except Exception as e:
        print('PRIMARY_ERROR='+type(e).__name__+':'+str(e)[:100]); sys.exit(1)
