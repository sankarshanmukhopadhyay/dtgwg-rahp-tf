import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reconcile", ROOT / "tools" / "reconcile_assessment_issues.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class AssessmentReconciliationTests(unittest.TestCase):
    def test_issue_requires_every_referencing_assessment_to_be_eligible(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as td:
            base = pathlib.Path(td)
            review1 = base / "one.md"
            review2 = base / "two.md"
            review1.write_text("one")
            review2.write_text("two")
            review1.with_suffix(".result.json").write_text(json.dumps({
                "status": "dispositioned", "target": {"reviewed_revision": "aaa"},
                "closure": {"eligible_issues": [12]}
            }))
            review2.with_suffix(".result.json").write_text(json.dumps({
                "status": "dispositioned", "target": {"reviewed_revision": "bbb"},
                "closure": {"eligible_issues": []}
            }))
            q = {"dispositions": [
                {"assessment_id": "A1", "assessment_key": "k1", "review": str(review1.relative_to(ROOT)), "rahp_issues": [12]},
                {"assessment_id": "A2", "assessment_key": "k2", "review": str(review2.relative_to(ROOT)), "rahp_issues": [12]},
            ]}
            self.assertEqual(MOD.closure_candidates(q), [])
            data = json.loads(review2.with_suffix(".result.json").read_text())
            data["closure"]["eligible_issues"] = [12]
            review2.with_suffix(".result.json").write_text(json.dumps(data))
            out = MOD.closure_candidates(q)
            self.assertEqual([x["issue"] for x in out], [12])
            self.assertEqual(len(out[0]["evidence"]), 2)


if __name__ == "__main__":
    unittest.main()

class AssessmentQueueLegacyCoalescingTests(unittest.TestCase):
    def test_legacy_coalesced_issue_requires_explicit_marker(self):
        from tools.validate_assessment_queue import validate
        import tempfile
        from pathlib import Path
        import json

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            # Review path validation is intentionally bypassed here by checking the
            # duplicate issue diagnostic only against the real CAWG queue contract.
            data = json.loads((ROOT / "instances/cawg/state/assessment-queue.json").read_text())
            data["dispositions"][0].pop("legacy_coalesced_issue", None)
            q = root / "assessment-queue.json"
            q.write_text(json.dumps(data))
            errors = validate(q)
            self.assertTrue(any("legacy_coalesced_issue=true" in error for error in errors))
