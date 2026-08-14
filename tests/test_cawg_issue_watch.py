import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("cawg_issue_watch", ROOT / "tools" / "cawg_issue_watch.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestCawgIssueWatch(unittest.TestCase):
    def test_baseline_then_change_emits_publisher_compatible_event(self):
        with tempfile.TemporaryDirectory() as td:
            td = pathlib.Path(td)
            reg = td / "issues.yaml"
            state = td / "issues.json"
            events = td / "events.json"
            reg.write_text("""version: 1\ninstance: cawg\nrepository: example/cawg\nissues:\n  - number: 1\n    theme: governance\n    title: Example\n    affected_reviews: [identity-governance]\n""")
            state.write_text('{"version":1,"observed":{}}\n')
            MOD.REG, MOD.STATE, MOD.EVENTS = reg, state, events
            snapshots = [
                {"updated_at":"2026-08-14T00:00:00Z","state":"open","title":"Example","comments":1},
                {"updated_at":"2026-08-14T01:00:00Z","state":"open","title":"Example","comments":2},
            ]
            MOD.get_issue = lambda repo, n, token=None: snapshots.pop(0)
            old_argv = sys.argv
            try:
                sys.argv = ["cawg_issue_watch.py"]
                self.assertEqual(MOD.main(), 0)
                self.assertEqual(json.loads(events.read_text()), [])
                self.assertEqual(MOD.main(), 0)
            finally:
                sys.argv = old_argv
            out = json.loads(events.read_text())
            self.assertEqual(len(out), 1)
            self.assertIn("title", out[0])
            self.assertIn("body", out[0])
            self.assertEqual(out[0]["labels"], ["assessment-required", "cawg-instance"])


if __name__ == "__main__":
    unittest.main()
