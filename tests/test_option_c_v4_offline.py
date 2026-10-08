"""V4 synthetic-only journal and continuation tests. No network, no primary data."""
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.error import HTTPError

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('v4', BASE/'scripts/usn_option_c_primary_runner_v4.py')
v4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v4)
V3 = BASE/'scripts/usn_option_c_primary_runner_v3.py'
spec3 = importlib.util.spec_from_file_location('v3_for_mock', V3)
b = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(b)


class TestV4Continuation(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory(); self.addCleanup(t.cleanup)
        root = Path(t.name)
        self.v3 = root/'v3'; self.v3.mkdir()
        self.v4 = root/'v4'
        self.prompt = root/'prompt.txt'; self.prompt.write_text('Judge without condition metadata')
        self.data = [{
            'evaluation_id':f'SOURCE_{i}', 'question':'Who signs?',
            'generated_output':{'kind':'answer','answer':'A manager signs.'},
            'reference_answer':'A manager signs.',
            'reference_evidence':[{'text':'A manager signs.'}],
            'retrieved_evidence':[{'text':'A manager signs.'}],
            'judgment':{'correctness_score':None, 'claim_judgments':[]}
        } for i in range(10)]
        self.valid = SimpleNamespace(valid=lambda j, cid: isinstance(j,dict) and j.get('evaluation_id')==cid
           and type(j.get('correctness_score')) is int and isinstance(j.get('claim_judgments'),list))
        self.sent = []
        self.make_v3()
        self.transport = SimpleNamespace(
            request_for=self.request_for, encode=lambda x:json.dumps(x,sort_keys=True),
            strict_json=json.loads, final_text=self.final_text, send_one=self.send_one)
        patches = [
            patch.object(v4,'V3_CAPSULE',self.v3), patch.object(v4,'CAPSULE',self.v4),
            patch.object(v4,'v3',lambda:b), patch.object(v4,'check_git',lambda:None),
            patch.object(v4,'git',lambda *args:'MOCK_V4_HEAD'),
            patch.object(v4,'v3_snapshot',self.snapshot),
            patch.object(b,'records',lambda:self.data),
            patch.object(b,'EXPECTED_ROWS',10), patch.object(b,'TOTAL_SLOTS',20),
            patch.object(b,'R11_PROMPT',self.prompt),
            patch.object(b,'load_validator',lambda:self.valid),
            patch.object(b,'load_r11',lambda:self.transport),
            patch.object(v4.time,'sleep',lambda x:None),
            patch.dict(os.environ,{'COHERE_API_KEY':'SYNTHETIC','GEMINI_API_KEY':'SYNTHETIC',
               'USN_PRIMARY_FREE_CONFIRMED':'YES','USN_PRIMARY_DATA_SHARING_AUTHORIZED':'YES',
               'USN_EXPLICIT_V4_INVALID_CONTINUATION':'YES','USN_EXPLICIT_429_RESUME':'YES'})]
        for p in patches:
            p.start(); self.addCleanup(p.stop)
        v4.prepare()

    def judgment(self,n,empty=False):
        return {'evaluation_id':f'I{n//2+1:03d}','correctness_score':2,
                'correctness_reason':'Evidence matches','abstention_outcome':'not_applicable',
                'claim_judgments':[] if empty else [{'claim_text':'A manager signs','label':'SUPPORTED','reason':'Evidence'}],
                'evaluator_notes':''}

    def make_v3(self):
        req=[];att=[];raw=[];done=[]
        for n in range(18):
            for attempt in range(1,3 if n==5 else 2):
                req.append({'slot':n,'judge':'J1' if n%2==0 else 'J2','item':f'I{n//2+1:03d}',
                            'payload_sha256':'mock','attempt':attempt})
                att.append({'slot':n,'status':'HTTP_503' if n==5 and attempt==1 else 'HTTP_200'})
            judgment=self.judgment(n,empty=n==17)
            raw.append({'slot':n,'judge':'J1' if n%2==0 else 'J2',
                        'item':f'I{n//2+1:03d}','response_sha256':str(n)})
            done.append({'slot':n,'judge':'J1' if n%2==0 else 'J2','item':f'I{n//2+1:03d}',
                         'response_sha256':str(n),'schema_ok':n!=17,'judgment':judgment})
        for name,items in [('requests.jsonl',req),('attempt_results.jsonl',att),
                           ('raw_responses.jsonl',raw),('completed.jsonl',done)]:
            (self.v3/name).write_text(''.join(v4.canonical(x)+'\n' for x in items))
        (self.v3/'status.json').write_text(v4.canonical({'state':'STOPPED','reason':'INVALID_JUDGMENT_SCHEMA','next_slot':18}))
        (self.v3/'freeze.json').write_text(v4.canonical({'git_head':'de6fb0bMOCK'}))
        (self.v3/'private_id_map.json').write_text('{}')

    def snapshot(self):
        return {n:v4.sha((self.v3/n).read_bytes()) for n in v4.COPY_FILES}

    def request_for(self,provider,model,prompt,case):
        return 'https://example.invalid', (
            {'max_tokens':4096,'case':case} if provider=='cohere' else
            {'generationConfig':{'maxOutputTokens':4096},'case':case})

    def final_text(self,provider,raw):
        return raw['text']

    def send_one(self,url,payload,provider,key):
        n=v4.rows(self.v4/'requests.jsonl')[-1]['slot']
        self.sent.append(n)
        return {'text':json.dumps(self.judgment(n))}

    def test_copies_exact_journal_and_keeps_invalid(self):
        for name in ('requests.jsonl','attempt_results.jsonl','raw_responses.jsonl','completed.jsonl'):
            self.assertEqual((self.v4/name).read_bytes(),(self.v3/name).read_bytes())
        self.assertEqual(v4.rows(self.v4/'completed.jsonl')[-1]['schema_ok'],False)
        self.assertEqual(v4.rows(self.v4/'completed.jsonl')[-1]['judgment']['claim_judgments'],[])
        v4.assert_freeze()

    def test_continues_only_slots_18_19(self):
        self.assertEqual(v4.run('continue'),0)
        self.assertEqual(self.sent,[18,19]); v4.assert_freeze()
        done=v4.rows(self.v4/'completed.jsonl')
        self.assertEqual(len(done),20)
        self.assertEqual(sum(x['schema_ok'] is True for x in done),19)
        self.assertEqual(sum(x['schema_ok'] is False for x in done),1)
        self.assertEqual(json.loads((self.v4/'status.json').read_text())['state'], 'COMPLETE_WITH_INVALID')

    def test_second_invalid_remains_missing(self):
        def missing(url,payload,provider,key):
            n=v4.rows(self.v4/'requests.jsonl')[-1]['slot']; self.sent.append(n)
            return {'text':json.dumps(self.judgment(n,empty=n==19))}
        self.transport.send_one=missing
        self.assertEqual(v4.run('continue'),0)
        done=v4.rows(self.v4/'completed.jsonl')
        self.assertEqual(sum(x['schema_ok'] is False for x in done),2)
        self.assertEqual(done[-1]['invalid_reason'],'ANSWER_WITHOUT_CLAIMS')
        self.assertEqual(self.sent,[18,19])

    def test_paused_429_can_resume_slot18_only(self):
        first=[True]
        def throttle(url,payload,provider,key):
            n=v4.rows(self.v4/'requests.jsonl')[-1]['slot']
            self.sent.append(n)
            if first[0]:
                first[0]=False
                raise HTTPError('https://example.invalid',429,'rate limit',{},None)
            return {'text':json.dumps(self.judgment(n))}
        self.transport.send_one=throttle
        self.assertEqual(v4.run('continue'),2)
        self.assertEqual(json.loads((self.v4/'status.json').read_text())['state'],'PAUSED_429')
        self.assertEqual(v4.run('resume'),0)
        self.assertEqual(self.sent,[18,18,19])

    def test_http503_retries_at_most_once(self):
        first=[True]
        def transient(url,payload,provider,key):
            n=v4.rows(self.v4/'requests.jsonl')[-1]['slot']; self.sent.append(n)
            if first[0]:
                first[0]=False
                raise HTTPError('https://example.invalid',503,'unavailable',{},None)
            return {'text':json.dumps(self.judgment(n))}
        self.transport.send_one=transient
        self.assertEqual(v4.run('continue'),0)
        self.assertEqual(self.sent,[18,18,19])

    def test_persistent_503_stops_without_replay(self):
        def down(url,payload,provider,key):
            self.sent.append(v4.rows(self.v4/'requests.jsonl')[-1]['slot'])
            raise HTTPError('https://example.invalid',503,'unavailable',{},None)
        self.transport.send_one=down
        self.assertEqual(v4.run('continue'),2)
        self.assertEqual(self.sent,[18,18])
        self.assertEqual(json.loads((self.v4/'status.json').read_text())['reason'],'HTTP_503')
        self.assertRaises(RuntimeError,v4.run,'continue')

    def test_timeout_stops_ambiguously(self):
        def timeout(url,payload,provider,key):
            self.sent.append(v4.rows(self.v4/'requests.jsonl')[-1]['slot'])
            raise TimeoutError('synthetic timeout')
        self.transport.send_one=timeout
        self.assertEqual(v4.run('continue'),2)
        self.assertEqual(self.sent,[18])
        self.assertRaises(RuntimeError,v4.run,'continue')

    def test_tamper_v3_evidence_is_rejected(self):
        with (self.v3/'completed.jsonl').open('a') as f:
            f.write('{}\n')
        self.assertRaises(RuntimeError,v4.assert_freeze)

    def test_no_duplicate_completed_slot(self):
        stat={'state':'READY_CONTINUE_INVALID','next_slot':17}
        (self.v4/'status.json').write_text(v4.canonical(stat))
        self.assertRaises(RuntimeError,v4.run,'continue')

    def test_need_explicit_auth(self):
        with patch.dict(os.environ,{'USN_EXPLICIT_V4_INVALID_CONTINUATION':'NO'}):
            self.assertRaises(RuntimeError,v4.run,'continue')

    def test_unexpected_judgment_is_not_imputed(self):
        def malformed(url,payload,provider,key):
            n=v4.rows(self.v4/'requests.jsonl')[-1]['slot']; self.sent.append(n)
            return {'text':'not JSON' if n == 18 else json.dumps(self.judgment(n))}
        self.transport.send_one=malformed
        self.assertEqual(v4.run('continue'),0)
        done=v4.rows(self.v4/'completed.jsonl')
        self.assertIsNone(done[18]['judgment'])
        self.assertFalse(done[18]['schema_ok'])
        self.assertEqual(done[18]['invalid_reason'],'RESPONSE_EXTRACTION_OR_JSON_FAILED')

if __name__=='__main__': unittest.main()
