"""V3 continuation tests: synthetic fixtures only, zero network and zero primary data."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

BASE = Path(__file__).resolve().parents[1]
SCRIPT = BASE / 'scripts/usn_option_c_primary_runner_v3.py'
spec = importlib.util.spec_from_file_location('primary_v3', SCRIPT)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class ContinuationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        source = base / 'source.jsonl'
        rows = []
        for k in range(4):
            rows.append({
                'evaluation_id': f'SOURCE_PRIVATE_{k}',
                'question': 'What is required?',
                'generated_output': {'kind': 'answer', 'answer': 'A signed form.'},
                'reference_answer': 'A signed form is required.',
                'reference_evidence': [{'text': 'A signed form is required.'}],
                'retrieved_evidence': [{'text': 'A signed form is required.'}],
                'judgment': {'correctness_score': None, 'correctness_reason': None,
                             'abstention_outcome': None, 'claim_judgments': []}
            })
        source.write_text(''.join(json.dumps(x) + '\n' for x in rows))
        self.v2 = base / 'v2'
        self.v2.mkdir()
        self.v3 = base / 'v3'
        self.saved = []
        for attr, obj in dict(CAPSULE=self.v3, V2_CAPSULE=self.v2, SOURCE=source,
                              EXPECTED_SHA=p.digest(source.read_bytes()),
                              EXPECTED_ROWS=4, TOTAL_SLOTS=8,
                              R11_PATH=BASE/'scripts/r11_hosted_qualification.py',
                              R11_PROMPT=BASE/'evidence/engineering/r11_qualification_v1/prompt.txt',
                              R11_VALIDATOR=BASE/'evidence/engineering/r11_qualification_v1/frozen_validator.py',
                              V2_RUNNER=BASE/'scripts/usn_option_c_primary_runner_v2.py',
                              V2_PROTOCOL=BASE/'evidence/engineering/option_c_primary_output_budget_v2_2026-10-08.md',
                              PROTOCOL=BASE/'evidence/engineering/option_c_primary_503_continuation_v3_2026-10-08.md').items():
            h = patch.object(p, attr, obj)
            h.start(); self.saved.append(h)
        for attr, obj in [('v1_failure_snapshot', lambda: {'test': 'unchanged'}),
                          ('check_repo', lambda: None),
                          ('repo', lambda *args: 'V3_MOCK_HEAD')]:
            h=patch.object(p,attr,obj); h.start(); self.saved.append(h)
        h=patch.object(p.time,'sleep',lambda _: None); h.start(); self.saved.append(h)
        self.addCleanup(lambda: [h.stop() for h in reversed(self.saved)])
        h=patch.dict(os.environ,{'COHERE_API_KEY':'DUMMY','GEMINI_API_KEY':'DUMMY',
            'USN_PRIMARY_FREE_CONFIRMED':'YES','USN_PRIMARY_DATA_SHARING_AUTHORIZED':'YES',
            'USN_EXPLICIT_V3_503_CONTINUATION':'YES','USN_EXPLICIT_429_RESUME':'YES'})
        h.start(); self.addCleanup(h.stop)
        self.make_v2_fixture()

    @staticmethod
    def write_lines(path, rows):
        path.write_text(''.join(p.canonical(x) + '\n' for x in rows))

    def j(self,n):
        return {'evaluation_id': f'I{n//2+1:03d}', 'correctness_score': 2,
                'correctness_reason': 'Matches', 'abstention_outcome': 'not_applicable',
                'claim_judgments': [{'claim_text':'Signed form', 'label':'SUPPORTED','reason':'Evidence'}],
                'evaluator_notes': ''}

    def response(self, provider):
        n=p.read_lines(self.v3/'requests.jsonl')[-1]['slot']
        txt=json.dumps(self.j(n))
        if provider=='cohere':
            return {'finish_reason':'COMPLETE','message':{'content':[{'type':'text','text':txt}]},
                    'usage':{'input_tokens':100,'output_tokens':80}}
        return {'candidates':[{'finishReason':'STOP','content':{'parts':[{'text':txt}]}}],
                'usageMetadata':{'promptTokenCount':100,'candidatesTokenCount':80}}

    def make_v2_fixture(self):
        req=[]; att=[]; raw=[]; done=[]
        for n in range(6):
            judge=p.slot(n)[1][0]
            r={'slot':n,'judge':judge,'item':f'I{n//2+1:03d}',
               'payload_sha256': 'will_replace', 'attempt':1}
            transport=p.load_r11()
            row=p.mapped_payload(p.records(),n//2)
            url,payload=p.request_for_v2(transport,p.slot(n)[1][1],p.slot(n)[1][2],p.R11_PROMPT.read_text(),row)
            r['payload_sha256']=p.digest(transport.encode(payload).encode('utf-8'))
            req.append(r)
            att.append({'slot':n,'status':'HTTP_200' if n<5 else 'HTTP_503'})
            if n<5:
                body={'mock':'NO_REAL_DOCUMENTS','slot':n}
                raw.append({'slot':n,'judge':judge,'item':r['item'],'raw':body})
                done.append({'slot':n,'judge':judge,'item':r['item'],
                             'schema_ok':True, 'judgment':self.j(n)})
        for filename, rows in [('requests.jsonl',req),('attempt_results.jsonl',att),
                               ('raw_responses.jsonl',raw),('completed.jsonl',done)]:
            self.write_lines(self.v2/filename,rows)
        (self.v2/'private_id_map.json').write_text(p.canonical({f'I{i+1:03d}':f'SOURCE_PRIVATE_{i}' for i in range(4)}))
        (self.v2/'status.json').write_text(p.canonical({'state':'STOPPED','reason':'HTTP_503','next_slot':5}))
        hashes={'runner':p.digest(p.V2_RUNNER.read_bytes()), 'protocol':p.digest(p.V2_PROTOCOL.read_bytes()),
            'prompt':p.digest(p.R11_PROMPT.read_bytes()), 'r11_transport':p.digest(p.R11_PATH.read_bytes()),
            'validator':p.digest(p.R11_VALIDATOR.read_bytes())}
        (self.v2/'freeze.json').write_text(p.canonical({'git_head':'160bfd8MOCK','hashes':hashes,
                    'v1_failure_sha256': {'test':'unchanged'},
                    'input_sha256':p.EXPECTED_SHA,'output_token_limit':p.OUTPUT_TOKEN_LIMIT}))

    def test_preserves_five_and_continues_from_sixth(self):
        p.prepare()
        for name in ('completed.jsonl','requests.jsonl','attempt_results.jsonl','raw_responses.jsonl'):
            self.assertEqual((self.v3/name).read_bytes(),(self.v2/name).read_bytes())
        transport=p.load_r11()
        calls=[]
        def fake(url,payload,provider,key):
            n=p.read_lines(self.v3/'requests.jsonl')[-1]['slot']
            calls.append(n)
            return self.response(provider)
        with patch.object(transport,'send_one',side_effect=fake), patch.object(p,'load_r11',return_value=transport):
            self.assertEqual(p.run('continue'),0)
        self.assertEqual(calls,[5,6,7])
        self.assertEqual(len(p.read_lines(self.v3/'completed.jsonl')),8)
        self.assertEqual(len(p.read_lines(self.v3/'requests.jsonl')),9)
        self.assertEqual(json.loads((self.v3/'status.json').read_text())['state'],'COMPLETE')
        self.assertEqual(p.assert_journal(8,'COMPLETE')[0][-1]['slot'],7)
        self.assertEqual(p.v2_evidence_snapshot(),json.loads((self.v3/'freeze.json').read_text())['v2_snapshot_sha256'])

    def test_historical_503_second_failure_stops(self):
        p.prepare()
        transport=p.load_r11()
        calls=[]
        def failure(url,payload,provider,key):
            calls.append(p.read_lines(self.v3/'requests.jsonl')[-1]['slot'])
            raise HTTPError(url,503,'unavailable',None,None)
        with patch.object(transport,'send_one',side_effect=failure), patch.object(p,'load_r11',return_value=transport):
            self.assertEqual(p.run('continue'),2)
        self.assertEqual(calls,[5])
        self.assertEqual(len(p.read_lines(self.v3/'completed.jsonl')),5)
        self.assertEqual([a['status'] for a in p.read_lines(self.v3/'attempt_results.jsonl')][-2:],['HTTP_503','HTTP_503'])
        self.assertEqual(json.loads((self.v3/'status.json').read_text())['state'],'STOPPED')

    def test_future_503_single_automatic_retry(self):
        p.prepare()
        transport=p.load_r11()
        calls=[]
        def fake(url,payload,provider,key):
            n=p.read_lines(self.v3/'requests.jsonl')[-1]['slot']
            calls.append(n)
            if n==6 and calls.count(6)==1:
                raise HTTPError(url,503,'unavailable',None,None)
            return self.response(provider)
        with patch.object(transport,'send_one',side_effect=fake), patch.object(p,'load_r11',return_value=transport):
            self.assertEqual(p.run('continue'),0)
        self.assertEqual(calls,[5,6,6,7])
        self.assertEqual([a['status'] for a in p.read_lines(self.v3/'attempt_results.jsonl')][-4:],
                         ['HTTP_200','HTTP_503','HTTP_200','HTTP_200'])

    def test_429_requires_manual_resume_and_does_not_replay_prior(self):
        p.prepare(); transport=p.load_r11(); calls=[]
        def fake(url,payload,provider,key):
            n=p.read_lines(self.v3/'requests.jsonl')[-1]['slot']; calls.append(n)
            if n==6 and calls.count(6)==1:
                raise HTTPError(url,429,'rate limit',None,None)
            return self.response(provider)
        with patch.object(transport,'send_one',side_effect=fake), patch.object(p,'load_r11',return_value=transport):
            self.assertEqual(p.run('continue'),2)
            self.assertEqual(json.loads((self.v3/'status.json').read_text())['state'],'PAUSED_429')
            self.assertEqual(p.run('resume'),0)
        self.assertEqual(calls,[5,6,6,7])

    def test_tampered_v2_history_blocks_before_send(self):
        p.prepare()
        with (self.v2/'attempt_results.jsonl').open('a') as f: f.write('{}\n')
        with self.assertRaisesRegex(RuntimeError,'V2_JOURNAL_COUNTS_MISMATCH'):
            p.assert_freeze()

    def test_inflight_request_blocks(self):
        p.prepare()
        with (self.v3/'requests.jsonl').open('a') as f: f.write(p.canonical({'slot':5,'attempt':2})+'\n')
        with self.assertRaisesRegex(RuntimeError,'INFLIGHT_OR_AMBIGUOUS_REQUEST_STOP'):
            p.assert_journal(5,'READY_CONTINUE_503')

    def test_future_double_503_stops_without_third_attempt(self):
        p.prepare(); t=p.load_r11(); calls=[]
        def fake(url,payload,provider,key):
            n=p.read_lines(self.v3/'requests.jsonl')[-1]['slot']
            calls.append(n)
            if n==6:
                raise HTTPError(url,503,'unavailable',None,None)
            return self.response(provider)
        with patch.object(t,'send_one',side_effect=fake), patch.object(p,'load_r11',return_value=t):
            self.assertEqual(p.run('continue'),2)
        self.assertEqual(calls,[5,6,6])
        self.assertEqual(len(p.read_lines(self.v3/'completed.jsonl')),6)
        self.assertEqual(json.loads((self.v3/'status.json').read_text())['reason'],'HTTP_503')

    def test_unknown_transport_failure_never_retried(self):
        p.prepare(); t=p.load_r11(); calls=[]
        def fake(url,payload,provider,key):
            calls.append(1)
            raise TimeoutError('ambiguous')
        with patch.object(t,'send_one',side_effect=fake), patch.object(p,'load_r11',return_value=t):
            self.assertEqual(p.run('continue'),2)
        self.assertEqual(len(calls),1)
        self.assertEqual(json.loads((self.v3/'status.json').read_text())['reason'],'TRANSPORT_TimeoutError')
        with self.assertRaisesRegex(RuntimeError,'INFLIGHT|UNSAFE_PENDING'):
            p.assert_journal(5,'STOPPED')

    def test_completed_slots_cannot_be_replayed(self):
        p.prepare(); t=p.load_r11()
        with patch.object(t,'send_one',side_effect=lambda url,payload,provider,key:self.response(provider)), \
             patch.object(p,'load_r11',return_value=t):
            self.assertEqual(p.run('continue'),0)
            with self.assertRaisesRegex(RuntimeError,'INVALID_STAGE_continue'):
                p.run('continue')

    def test_gates_require_explicit_authorization(self):
        p.prepare()
        os.environ.pop('USN_PRIMARY_FREE_CONFIRMED',None)
        with self.assertRaisesRegex(RuntimeError,'FREE_TIER_NOT_CONFIRMED'):
            p.run('continue')
        self.assertEqual(len(p.read_lines(self.v3/'requests.jsonl')),6)

    def test_pin_output_limit_and_model_transports(self):
        t=p.load_r11()
        data=p.records()
        for _,provider,model,_ in p.JUDGES:
            _,body=p.request_for_v2(t,provider,model,p.R11_PROMPT.read_text(),p.mapped_payload(data,0))
            self.assertEqual(body['max_tokens'] if provider=='cohere' else body['generationConfig']['maxOutputTokens'],16384)

if __name__=='__main__': unittest.main()
