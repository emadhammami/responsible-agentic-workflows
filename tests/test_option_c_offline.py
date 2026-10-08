"""Synthetic-only tests for the USN Option C primary runner; zero network."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/usn_option_c_primary_runner.py'
spec = importlib.util.spec_from_file_location('primary', SCRIPT)
primary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(primary)
BASE = Path(__file__).resolve().parents[1]


class PrimaryOffline(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.cap = root / 'cap'
        src = root / 'items.jsonl'
        rows = []
        for i in range(2):
            rows.append({
                'evaluation_id': f'PRIMARY_SOURCE_PRIVATE_{i}',
                'question': 'What is the maximum?',
                'generated_output': {'kind': 'answer', 'answer': 'Maximum 10.'},
                'reference_answer': 'Maximum 10.',
                'reference_evidence': [{'text': 'Maximum 10.'}],
                'retrieved_evidence': [{'text': 'Maximum 10.'}],
                'judgment': {'correctness_score': None, 'correctness_reason': None,
                             'abstention_outcome': None, 'claim_judgments': []}
            })
        src.write_text(''.join(json.dumps(x) + '\n' for x in rows))
        self.hooks = []
        patches = dict(CAPSULE=self.cap, SOURCE=src,
                       EXPECTED_SHA=primary.digest(src.read_bytes()),
                       EXPECTED_ROWS=2, TOTAL_SLOTS=4,
                       R11_PATH=BASE / 'scripts/r11_hosted_qualification.py',
                       R11_PROMPT=BASE / 'evidence/engineering/r11_qualification_v1/prompt.txt',
                       R11_VALIDATOR=BASE / 'evidence/engineering/r11_qualification_v1/frozen_validator.py',
                       PROTOCOL=BASE / 'evidence/engineering/option_c_primary_amendment_2026-10-08.md')
        for k, v in patches.items():
            hook = patch.object(primary, k, v)
            hook.start()
            self.hooks.append(hook)
        self.hooks.append(patch.object(primary, 'check_repo', lambda: None))
        self.hooks[-1].start()
        self.hooks.append(patch.object(primary, 'repo', lambda *x: 'MOCK_HEAD'))
        self.hooks[-1].start()
        self.hooks.append(patch.object(primary.time, 'sleep', lambda sec: None))
        self.hooks[-1].start()
        self.addCleanup(lambda: [h.stop() for h in reversed(self.hooks)])
        self.env = patch.dict(os.environ, {'COHERE_API_KEY': 'DUMMY', 'GEMINI_API_KEY': 'DUMMY',
                                          'USN_PRIMARY_FREE_CONFIRMED': 'YES',
                                          'USN_PRIMARY_DATA_SHARING_AUTHORIZED': 'YES',
                                          'USN_EXPLICIT_429_RESUME': 'YES'})
        self.env.start()
        self.addCleanup(self.env.stop)
        primary.prepare()

    def provider_response(self, provider):
        answer = json.dumps({
            'evaluation_id': 'I001', 'correctness_score': 2,
            'correctness_reason': 'Correct', 'abstention_outcome': 'not_applicable',
            'claim_judgments': [{'claim_text': 'Maximum 10', 'label': 'SUPPORTED', 'reason': 'Source'}],
            'evaluator_notes': ''})
        # Infer current slot directly from request intents to return correct opaque ID.
        n = primary.read_lines(self.cap / 'requests.jsonl')[-1]['slot']
        obj = json.loads(answer)
        obj['evaluation_id'] = f'I{n//2 + 1:03d}'
        answer = json.dumps(obj)
        if provider == 'cohere':
            return {'finish_reason': 'COMPLETE', 'message': {'content': [{'type': 'text', 'text': answer}]},
                    'usage': {'billed_units': {'input_tokens': 100, 'output_tokens': 30}}}
        return {'candidates': [{'finishReason': 'STOP', 'content': {'parts': [{'text': answer}]}}],
                'usageMetadata': {'promptTokenCount': 100, 'candidatesTokenCount': 30}}

    def test_all_4_slots(self):
        transport = primary.load_r11()
        with patch.object(transport, 'send_one', side_effect=lambda url, payload, provider, key: self.provider_response(provider)):
            with patch.object(primary, 'load_r11', return_value=transport):
                self.assertEqual(primary.run('sentinel'), 0)
                self.assertEqual(primary.run('bulk'), 0)
                self.assertEqual(primary.read_lines(self.cap / 'completed.jsonl').__len__(), 4)
                self.assertEqual(json.loads((self.cap/'status.json').read_text())['state'], 'COMPLETE')
                self.assertEqual(len(primary.read_lines(self.cap/'requests.jsonl')), 4)
                self.assertEqual(len(primary.read_lines(self.cap/'attempt_results.jsonl')), 4)
                self.assertEqual(len(primary.read_lines(self.cap/'raw_responses.jsonl')), 4)
                self.assertNotIn('PRIMARY_SOURCE_PRIVATE_', (self.cap/'requests.jsonl').read_text())
                self.assertEqual((self.cap/'private_id_map.json').stat().st_mode & 0o077, 0)
                self.assertEqual(primary.assert_journal(4, False)[0][-1]['slot'], 3)

    def test_explicit_429_resume_does_not_replay_completion(self):
        from urllib.error import HTTPError
        transport = primary.load_r11()
        once = [False]
        def send(url, payload, provider, key):
            if provider == 'gemini' and not once[0]:
                once[0] = True
                raise HTTPError(url, 429, 'rate limit', None, None)
            return self.provider_response(provider)
        with patch.object(transport, 'send_one', side_effect=send):
            with patch.object(primary, 'load_r11', return_value=transport):
                self.assertEqual(primary.run('sentinel'), 2)
                self.assertEqual(len(primary.read_lines(self.cap / 'completed.jsonl')), 1)
                self.assertEqual(primary.run('resume'), 0)
                self.assertEqual(primary.run('bulk'), 0)
                ints, outs = primary.assert_journal(4, False)
                self.assertEqual(len(ints), 5)
                self.assertEqual([x['status'] for x in outs],
                                 ['HTTP_200', 'HTTP_429', 'HTTP_200', 'HTTP_200', 'HTTP_200'])

    def test_missing_privacy_authorization_makes_no_requests(self):
        os.environ.pop('USN_PRIMARY_DATA_SHARING_AUTHORIZED', None)
        with self.assertRaisesRegex(RuntimeError, 'EXTERNAL_DATA_SHARING_NOT_AUTHORIZED'):
            primary.run('sentinel')
        self.assertFalse((self.cap/'requests.jsonl').exists())

    def test_original_ids_not_sent(self):
        payload = primary.mapped_payload(primary.records(), 0)
        self.assertEqual(set(payload), set(primary.SEND_FIELDS) | {'evaluation_id'})
        self.assertEqual(payload['evaluation_id'], 'I001')
        self.assertNotIn('PRIMARY_SOURCE_PRIVATE_', json.dumps(payload))


if __name__ == '__main__':
    unittest.main()
