#!/usr/bin/env python3
"""USN Option-C output-budget-only V2 primary scoring, provisional ratings.

No HTTP calls except the explicitly authorized `sentinel`, `bulk`, `resume` modes.
Does not edit source records, frozen R1-R11, or Git. Python stdlib only.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone
from urllib.error import HTTPError

SOURCE = Path.home() / 'primary-benchmark-results/PRIMARY-BENCHMARK-V1/scoring/scoring_package_v1/evaluator_A_blinded_270.jsonl'
EXPECTED_SHA = '3c2021037eeb39cec5ff90e212edf077fc17b3183e11ba2af44395b57ce26dec'
CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V2'
V1_CAPSULE = Path.home() / 'primary-benchmark-results/OPTION-C-PRIMARY-PROVISIONAL-V1'
OUTPUT_TOKEN_LIMIT = 16384
R11_PATH = Path('scripts/r11_hosted_qualification.py')
R11_PROMPT = Path('evidence/engineering/r11_qualification_v1/prompt.txt')
R11_VALIDATOR = Path('evidence/engineering/r11_qualification_v1/frozen_validator.py')
PROTOCOL = Path('evidence/engineering/option_c_primary_output_budget_v2_2026-10-08.md')
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
    if not repo('ls-files', '--error-unmatch', 'scripts/usn_option_c_primary_runner_v2.py'):
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


def assert_freeze():
    manifest = json.loads((CAPSULE / 'freeze.json').read_text())
    paths = {'runner': Path(__file__), 'r11_transport': R11_PATH,
             'prompt': R11_PROMPT, 'validator': R11_VALIDATOR, 'protocol': PROTOCOL}
    for name, path in paths.items():
        if digest(path.read_bytes()) != manifest['hashes'][name]:
            raise RuntimeError('FROZEN_HASH_MISMATCH_' + name)
    if repo('rev-parse', 'HEAD') != manifest['git_head']:
        raise RuntimeError('FROZEN_GIT_HEAD_CHANGED')
    if manifest.get('v1_failure_sha256') != v1_failure_snapshot():
        raise RuntimeError('V1_FAILURE_EVIDENCE_CHANGED')
    if manifest.get('output_token_limit') != OUTPUT_TOKEN_LIMIT:
        raise RuntimeError('V2_OUTPUT_LIMIT_CHANGED')
    check_repo()
    data = records()
    if len(data) != EXPECTED_ROWS:
        raise RuntimeError('PRIMARY_COUNT_CHANGED')
    return data


def prepare():
    check_repo()
    data = records()
    structure_report(data)
    v1_evidence = v1_failure_snapshot()
    if CAPSULE.exists():
        raise RuntimeError('CAPSULE_ALREADY_EXISTS_STOP')
    # All content remains local to the user's private benchmark-results tree.
    CAPSULE.mkdir(mode=0o700)
    secure_new(CAPSULE / 'freeze.json', {
        'created_utc': now(), 'git_head': repo('rev-parse', 'HEAD'),
        'input_sha256': EXPECTED_SHA, 'items': EXPECTED_ROWS, 'slots': TOTAL_SLOTS,
        'method_status': 'PROVISIONAL_UNQUALIFIED_OPTION_C_V2',
        'output_token_limit': OUTPUT_TOKEN_LIMIT,
        'v1_failure_sha256': v1_evidence,
        'judge_models': [{'code': x[0], 'provider': x[1], 'model': x[2]} for x in JUDGES],
        'hashes': {'runner': digest(Path(__file__).read_bytes()),
                   'r11_transport': digest(R11_PATH.read_bytes()),
                   'prompt': digest(R11_PROMPT.read_bytes()),
                   'validator': digest(R11_VALIDATOR.read_bytes()),
                   'protocol': digest(PROTOCOL.read_bytes())}
    })
    secure_new(CAPSULE / 'private_id_map.json', {
        f'I{i+1:03d}': row['evaluation_id'] for i, row in enumerate(data)})
    replace_status({'state': 'READY_SENTINEL', 'next_slot': 0, 'updated_utc': now()})
    print('CAPSULE_PREPARED=PASS')
    print('PRIMARY_API_REQUESTS=0')


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


def assert_journal(next_slot, resume):
    completed = read_lines(CAPSULE / 'completed.jsonl')
    intents = read_lines(CAPSULE / 'requests.jsonl')
    outcomes = read_lines(CAPSULE / 'attempt_results.jsonl')
    if len(completed) != next_slot or [x['slot'] for x in completed] != list(range(next_slot)):
        raise RuntimeError('JOURNAL_COMPLETED_MISMATCH_STOP')
    if len(outcomes) != len(intents):
        raise RuntimeError('INFLIGHT_OR_AMBIGUOUS_REQUEST_STOP')
    if any(x['slot'] < 0 or x['slot'] >= TOTAL_SLOTS for x in intents):
        raise RuntimeError('BAD_REQUEST_JOURNAL_STOP')
    if [x['slot'] for x in intents] != [x['slot'] for x in outcomes]:
        raise RuntimeError('REQUEST_OUTCOME_ORDER_MISMATCH')
    for n in range(next_slot):
        ins = [x for x in intents if x['slot'] == n]
        outs = [x for x in outcomes if x['slot'] == n]
        if not ins or len(ins) != len(outs) or any(x['status'] != 'HTTP_429' for x in outs[:-1]) or outs[-1]['status'] != 'HTTP_200':
            raise RuntimeError('INCOMPLETE_PRIOR_SLOT_STOP')
    pending = [x for x in intents if x['slot'] == next_slot]
    if pending:
        if not resume or any(x['status'] != 'HTTP_429' for x in outcomes if x['slot'] == next_slot) or len(pending) != len([x for x in outcomes if x['slot'] == next_slot]):
            raise RuntimeError('PENDING_SLOT_REQUIRES_EXPLICIT_429_RESUME')
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
    allowed = {'sentinel': ('READY_SENTINEL',),
               'bulk': ('READY_BULK',),
               'resume': ('PAUSED_429',)}
    if stat['state'] not in allowed[kind]:
        raise RuntimeError('INVALID_STAGE_' + kind)
    if os.environ.get('USN_PRIMARY_FREE_CONFIRMED') != 'YES':
        raise RuntimeError('FREE_TIER_NOT_CONFIRMED_STOP')
    if os.environ.get('USN_PRIMARY_DATA_SHARING_AUTHORIZED') != 'YES':
        raise RuntimeError('EXTERNAL_DATA_SHARING_NOT_AUTHORIZED_STOP')
    if any(not os.environ.get(x[3]) for x in JUDGES):
        raise RuntimeError('MISSING_API_KEY_STOP')
    if kind == 'resume' and os.environ.get('USN_EXPLICIT_429_RESUME') != 'YES':
        raise RuntimeError('RESUME_NOT_AUTHORIZED_STOP')
    mod = load_r11()
    val = load_validator()
    prompt = R11_PROMPT.read_text()
    start = stat['next_slot']
    intents, outcomes = assert_journal(start, kind == 'resume')
    finish = 2 if kind == 'sentinel' else TOTAL_SLOTS
    if kind == 'resume' and start < 2:
        finish = 2  # Resume only the interrupted sentinel, then require bulk authorization.
    sent_last = {}
    for n in range(start, finish):
        idx, (code, provider, model, env) = slot(n)
        case = mapped_payload(data, idx)
        url, payload = request_for_v2(mod, provider, model, prompt, case)
        payload_hash = digest(mod.encode(payload).encode('utf-8'))
        prior = [x for x in intents if x['slot'] == n]
        if prior and any(x['payload_sha256'] != payload_hash for x in prior):
            raise RuntimeError('CHANGED_RETRY_PAYLOAD_STOP')
        # Conservative per-provider pacing, including manual resumes.
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
            raw = mod.send_one(url, payload, provider, os.environ[env])
        except HTTPError as err:
            code_http = err.code
            err.close()
            append(CAPSULE / 'attempt_results.jsonl', {
                'slot': n, 'status': 'HTTP_' + str(code_http),
                'elapsed_seconds': round(time.monotonic() - tic, 4),
                'finished_utc': now()})
            replace_status({'state': 'PAUSED_429' if code_http == 429 else 'STOPPED',
                            'next_slot': n, 'reason': 'HTTP_' + str(code_http),
                            'updated_utc': now()})
            print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|HTTP_{code_http}')
            return 2
        except Exception as err:
            append(CAPSULE / 'attempt_results.jsonl', {
                'slot': n, 'status': 'TRANSPORT_' + type(err).__name__,
                'elapsed_seconds': round(time.monotonic() - tic, 4),
                'finished_utc': now()})
            replace_status({'state': 'STOPPED', 'next_slot': n,
                            'reason': 'TRANSPORT_' + type(err).__name__, 'updated_utc': now()})
            print(f'PRIMARY_TRANSPORT_STOP={code}|SLOT={n}|TRANSPORT_{type(err).__name__}')
            return 2
        elapsed = round(time.monotonic() - tic, 4)
        sent_last[provider] = time.monotonic()
        append(CAPSULE / 'attempt_results.jsonl', {
            'slot': n, 'status': 'HTTP_200', 'elapsed_seconds': elapsed,
            'finished_utc': now()})
        append(CAPSULE / 'raw_responses.jsonl', {
            'slot': n, 'judge': code, 'item': case['evaluation_id'],
            'payload_sha256': payload_hash, 'raw': raw,
            'response_sha256': digest(mod.encode(raw).encode()),
            'usage': usage(provider, raw), 'elapsed_seconds': elapsed})
        try:
            judgment = mod.strict_json(mod.final_text(provider, raw))
            valid = val.valid(judgment, case['evaluation_id'])
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
            'response_sha256': digest(mod.encode(raw).encode()),
            'elapsed_seconds': elapsed})
        next_state = 'RUNNING' if n + 1 < finish else ('READY_BULK' if finish == 2 else 'COMPLETE')
        replace_status({'state': next_state, 'next_slot': n + 1, 'updated_utc': now()})
        print(f'PRIMARY_RESULT={code}|SLOT={n+1}/{TOTAL_SLOTS}|SCHEMA={int(valid)}|SECONDS={elapsed:.2f}', flush=True)
        if not valid:
            replace_status({'state': 'STOPPED', 'next_slot': n + 1,
                            'reason': 'INVALID_JUDGMENT_SCHEMA', 'updated_utc': now()})
            print('PRIMARY_STOP=INVALID_JUDGMENT_SCHEMA')
            return 2
    print('PRIMARY_STAGE=' + ('SENTINEL_PASS' if finish == 2 else 'COMPLETE'))
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
    print('OFFLINE_MOCK_TEST=PASS')
    print('NETWORK_REQUESTS=0')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('audit', 'mock-test', 'prepare', 'verify', 'status', 'sentinel', 'bulk', 'resume'))
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
        assert_journal(state['next_slot'], state['state'] == 'PAUSED_429')
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
