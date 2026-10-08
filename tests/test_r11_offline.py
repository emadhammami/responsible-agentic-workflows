"""Offline transport simulations; never call provider APIs."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
import urllib.error
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "r11_hosted_qualification.py"
spec = importlib.util.spec_from_file_location("r11_runner", SCRIPT)
r11 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r11)
MATERIALS = ROOT / "evidence" / "engineering" / "r11_qualification_v1"


def judgment(gold, cid, invalid=False):
    return {
        "evaluation_id": cid,
        "correctness_score": gold[cid][0],
        "correctness_reason": "Expected semantics match reference and evidence.",
        "abstention_outcome": gold[cid][1],
        "claim_judgments": [
            {"claim_text": "Single asserted claim", "label": lab,
             "reason": "Evidence supports the assigned label."} for lab in gold[cid][2]
        ],
        "evaluator_notes": [] if invalid else "",
    }


class R11OfflineIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        self.cases, self.gold, self.prompt, self.valid = r11.material_check(MATERIALS)
        self.capsule_patch = patch.object(r11, "CAPSULE", self.path)
        self.capsule_patch.start()
        self.addCleanup(self.capsule_patch.stop)
        self.verify_patch = patch.object(r11, "verify", return_value=(self.cases, self.gold, self.prompt, self.valid))
        self.verify_patch.start()
        self.addCleanup(self.verify_patch.stop)
        self.env_patch = patch.dict(os.environ, {
            "R11_FREE_TIER_CONFIRMED": "YES",
            "COHERE_API_KEY": "mock-cohere",
            "GEMINI_API_KEY": "mock-gemini",
        })
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)
        self._send_count = 0

    def fake_response(self, url, payload, provider, key):
        self._send_count += 1
        if provider == "cohere":
            case = json.loads(payload["messages"][1]["content"])
        else:
            case = json.loads(payload["contents"][0]["parts"][0]["text"])
        cid = case["evaluation_id"]
        j = judgment(self.gold, cid)
        if provider == "cohere":
            return {"finish_reason": "COMPLETE", "usage": {"tokens": 42},
                    "message": {"content": [{"type": "thinking", "thinking": "mock"},
                                            {"type": "text", "text": json.dumps(j)}]}}
        return {"usageMetadata": {"totalTokenCount": 42},
                "candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": json.dumps(j)}]}}]}

    def run_silent(self, resume=False):
        with redirect_stdout(StringIO()):
            return r11.execute(resume=resume)

    def test_capsule_prepare_and_verify_without_network(self):
        # Patch Git checks only because this ZIP is tested outside the user repo.
        old_cwd = os.getcwd()
        os.chdir(ROOT)
        self.addCleanup(os.chdir, old_cwd)
        capsule = self.path / "fresh_capsule"
        contract = ROOT / r11.PROTOCOL_PATH
        if not contract.is_file():
            contract = ROOT / "reference" / "r11_contract.md"
        self.assertEqual(r11.sha(contract.read_bytes()), r11.PROTOCOL_SHA256)
        with patch.object(r11, "repo_guard"), patch.object(r11, "git", return_value="offline-test-commit"), patch.object(r11, "CAPSULE", capsule), patch.object(r11, "PROTOCOL_PATH", str(contract)):
            with redirect_stdout(StringIO()):
                r11.prepare()
            self.assertTrue((capsule / "harness_freeze.json").is_file())
            verified_cases, verified_gold, _, _ = r11.verify()
            self.assertEqual(verified_cases, self.cases)
            self.assertEqual(verified_gold, self.gold)
            self.assertEqual(json.loads((capsule / "harness_freeze.json").read_text())["inference_requests"], 0)

    def test_all_36_slots_success_and_no_replay(self):
        with patch.object(r11, "send_one", side_effect=self.fake_response):
            self.assertEqual(self.run_silent(), 0)
            self.assertEqual(self._send_count, 36)
            result = json.loads((self.path / "results.json").read_text())
            self.assertEqual(result["pair_status"], "PASS")
            self.assertEqual(len(r11.read_jsonl(self.path / "completed.jsonl")), 36)
            self.assertTrue(all(m["qualified"] for m in result["models"]))
            with self.assertRaises(RuntimeError):
                self.run_silent()
            self.assertEqual(self._send_count, 36)

    def test_429_pause_manual_resume_without_replaying_completions(self):
        def with_429_first(*args):
            if self._send_count == 0:
                self._send_count += 1
                raise urllib.error.HTTPError("https://example.invalid", 429, "rate limit", None, None)
            return self.fake_response(*args)
        with patch.object(r11, "send_one", side_effect=with_429_first):
            self.assertEqual(self.run_silent(), 2)
            self.assertEqual(len(r11.read_jsonl(self.path / "completed.jsonl")), 0)
            state = json.loads((self.path / "run_status.json").read_text())
            self.assertEqual(state["reason"], "HTTP_429")
            with self.assertRaises(RuntimeError):
                self.run_silent()
            self.assertEqual(self.run_silent(resume=True), 0)
        self.assertEqual(len(r11.read_jsonl(self.path / "completed.jsonl")), 36)
        attempts = r11.read_jsonl(self.path / "requests.jsonl")
        self.assertEqual(len(attempts), 37)
        self.assertEqual(sum(x["slot_index"] == 0 for x in attempts), 2)
        self.assertEqual(self._send_count, 37)

    def test_503_stops_with_no_resume(self):
        def fail_503(*_):
            self._send_count += 1
            raise urllib.error.HTTPError("https://example.invalid", 503, "unavailable", None, None)
        with patch.object(r11, "send_one", side_effect=fail_503):
            self.assertEqual(self.run_silent(), 2)
            with self.assertRaises(RuntimeError):
                self.run_silent(resume=True)
        self.assertEqual(self._send_count, 1)
        self.assertFalse((self.path / "results.json").exists())

    def test_schema_failure_invalidates_pair(self):
        def fake_invalid_once(url, payload, provider, key):
            raw = self.fake_response(url, payload, provider, key)
            if self._send_count == 1:
                j = judgment(self.gold, "Q01", invalid=True)
                raw["message"]["content"][-1]["text"] = json.dumps(j)
            return raw
        with patch.object(r11, "send_one", side_effect=fake_invalid_once):
            self.assertEqual(self.run_silent(), 0)
        result = json.loads((self.path / "results.json").read_text())
        self.assertEqual(result["models"][0]["schema"], 17)
        self.assertEqual(result["pair_status"], "NO_QUALIFIED_PAIR")
        self.assertEqual(self._send_count, 18)
        self.assertEqual(result["j2_status"], "NOT_RUN_J1_FAILED")
        self.assertEqual(len(r11.read_jsonl(self.path / "completed.jsonl")), 18)

    def test_gold_failure_stops_before_j2(self):
        def wrong_gold(url, payload, provider, key):
            raw = self.fake_response(url, payload, provider, key)
            if provider == "cohere":
                case = json.loads(payload["messages"][1]["content"])
                if case["evaluation_id"] in ("Q01", "Q03", "Q04", "Q05"):
                    j = judgment(self.gold, case["evaluation_id"])
                    j["correctness_score"] = (j["correctness_score"] + 1) % 3
                    raw["message"]["content"][-1]["text"] = json.dumps(j)
            return raw
        with patch.object(r11, "send_one", side_effect=wrong_gold):
            self.assertEqual(self.run_silent(), 0)
        self.assertEqual(self._send_count, 18)
        result = json.loads((self.path / "results.json").read_text())
        self.assertEqual(result["models"][0]["gold"], 10)
        self.assertEqual(result["j2_status"], "NOT_RUN_J1_FAILED")
        self.assertEqual(result["pair_status"], "NO_QUALIFIED_PAIR")


    def test_j2_invalid_schema_cannot_qualify_pair(self):
        def j2_bad_once(url, payload, provider, key):
            raw = self.fake_response(url, payload, provider, key)
            if provider == "gemini" and self._send_count == 19:
                case = json.loads(payload["contents"][0]["parts"][0]["text"])
                bad = judgment(self.gold, case["evaluation_id"], invalid=True)
                raw["candidates"][0]["content"]["parts"][0]["text"] = json.dumps(bad)
            return raw
        with patch.object(r11, "send_one", side_effect=j2_bad_once):
            self.assertEqual(self.run_silent(), 0)
        self.assertEqual(self._send_count, 36)
        result = json.loads((self.path / "results.json").read_text())
        self.assertTrue(result["models"][0]["qualified"])
        self.assertFalse(result["models"][1]["qualified"])
        self.assertEqual(result["pair_status"], "NO_QUALIFIED_PAIR")

    def test_missing_free_tier_confirmation_blocks_before_journaling(self):
        with patch.dict(os.environ, {"R11_FREE_TIER_CONFIRMED": "NO"}):
            with patch.object(r11, "send_one", side_effect=AssertionError("No API expected")):
                with self.assertRaises(RuntimeError):
                    self.run_silent()
        self.assertFalse((self.path / "run_status.json").exists())
        self.assertFalse((self.path / "requests.jsonl").exists())
        self.assertEqual(self._send_count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
