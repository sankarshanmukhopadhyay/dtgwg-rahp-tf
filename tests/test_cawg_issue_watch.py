import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("issue_watch", ROOT / "tools" / "issue_watch.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestIssueWatch(unittest.TestCase):
    def test_cawg_style_default_repository_baseline_then_change(self):
        with tempfile.TemporaryDirectory() as td:
            td = pathlib.Path(td)
            reg = td / "issues.yaml"
            state = td / "issues.json"
            events = td / "events.json"
            reg.write_text("""version: 1
instance: cawg
repository: example/cawg
issues:
  - number: 1
    theme: governance
    title: Example
    affected_reviews: [identity-governance]
""")
            state.write_text('{"version":1,"observed":{}}\n')
            snapshots = [
                {"updated_at":"2026-08-14T00:00:00Z","state":"open","title":"Example","comments":1},
                {"updated_at":"2026-08-14T01:00:00Z","state":"open","title":"Example","comments":2},
            ]
            original = MOD.get_issue
            MOD.get_issue = lambda repo, n, token=None: snapshots.pop(0)
            try:
                self.assertEqual(MOD.watch(reg, state, events), [])
                out = MOD.watch(reg, state, events)
            finally:
                MOD.get_issue = original
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0]["labels"], ["assessment-required", "cawg-instance"])
            self.assertEqual(out[0]["upstream_repository"], "example/cawg")
            self.assertEqual(out[0]["upstream_issue"], 1)

    def test_dtg_style_per_issue_repositories_and_labels(self):
        with tempfile.TemporaryDirectory() as td:
            td = pathlib.Path(td)
            reg = td / "issues.yaml"
            state = td / "issues.json"
            events = td / "events.json"
            reg.write_text("""version: 1
instance: dtg
labels: [assessment-required, dtg-instance]
issues:
  - repository: example/trust-tasks
    number: 205
    theme: authorization
    title: Authorization boundary
    affected_reviews: [trust-tasks-spec]
  - repository: example/cred-spec
    number: 17
    theme: standards-alignment
    title: W3C alignment
    affected_reviews: [dtg-credential-spec]
""")
            state.write_text('{"version":1,"observed":{}}\n')
            current = {
                ("example/trust-tasks",205): {"updated_at":"2026-08-14T00:00:00Z","state":"open","title":"Authorization boundary","comments":1},
                ("example/cred-spec",17): {"updated_at":"2026-08-14T00:00:00Z","state":"open","title":"W3C alignment","comments":1},
            }
            original = MOD.get_issue
            MOD.get_issue = lambda repo, n, token=None: dict(current[(repo,n)])
            try:
                self.assertEqual(MOD.watch(reg, state, events), [])
                current[("example/trust-tasks",205)]["updated_at"] = "2026-08-14T02:00:00Z"
                current[("example/trust-tasks",205)]["comments"] = 2
                out = MOD.watch(reg, state, events)
            finally:
                MOD.get_issue = original
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0]["labels"], ["assessment-required", "dtg-instance"])
            self.assertEqual(out[0]["upstream_repository"], "example/trust-tasks")
            self.assertIn("example/trust-tasks#205", out[0]["title"])

    def test_legacy_yaml_state_at_json_path_is_migrated(self):
        with tempfile.TemporaryDirectory() as td:
            td = pathlib.Path(td)
            reg = td / "issues.yaml"
            state = td / "issues.json"
            events = td / "events.json"
            reg.write_text("""version: 1
instance: cawg
repository: example/cawg
issues:
  - number: 1
    theme: governance
    title: Example
    affected_reviews: [identity-governance]
""")
            state.write_text("version: 1\nobserved: {}\n")
            original = MOD.get_issue
            MOD.get_issue = lambda repo, n, token=None: {"updated_at":"2026-08-14T00:00:00Z","state":"open","title":"Example","comments":1}
            try:
                self.assertEqual(MOD.watch(reg, state, events), [])
            finally:
                MOD.get_issue = original
            parsed = json.loads(state.read_text())
            self.assertEqual(parsed["version"], 1)
            self.assertIn("example/cawg#1", parsed["observed"])


if __name__ == "__main__":
    unittest.main()
