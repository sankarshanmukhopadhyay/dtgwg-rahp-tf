import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("instance_monitor", ROOT / "tools" / "instance_monitor.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class InstanceMonitorTests(unittest.TestCase):
    def test_main_branch_key_is_backward_compatible(self):
        target = {"repository": "example/spec", "branch": "main"}
        self.assertEqual(MOD.assessment_key("cawg", target), "cawg:repository:example/spec")

    def test_non_main_branch_has_distinct_assessment_key(self):
        target = {"repository": "example/spec", "branch": "governance"}
        self.assertEqual(
            MOD.assessment_key("cawg", target),
            "cawg:repository:example/spec@governance",
        )

    def test_root_file_matches_double_star_pattern(self):
        self.assertTrue(MOD.path_matches("SPEC.md", "**/SPEC.md"))

    def test_role_profile_expands_materiality(self):
        target = {
            "repository": "example/implementation",
            "context": {"type": "reference-implementation"},
            "scope": {"include": ["docs/**"]},
        }
        cfg = {
            "assessment": {
                "materiality": {
                    "always_material_paths": [".github/workflows/**"],
                    "role_profiles": {"reference-implementation": ["**/src/**", "**/tests/**"]},
                }
            }
        }
        classification, matched = MOD.classify(
            target,
            [{"filename": "vta-vault/src/receive.rs"}, {"filename": "Cargo.lock"}],
            cfg,
        )
        self.assertEqual(classification, "assessment")
        self.assertEqual(matched, ["vta-vault/src/receive.rs"])

    def test_documentation_only_change_can_be_triaged_for_configured_role(self):
        target = {
            "repository": "example/task-force",
            "context": {"type": "task-force-workspace"},
            "scope": {"include": ["README.md", "docs/**", "specs/**"]},
        }
        cfg = {
            "assessment": {
                "materiality": {
                    "documentation_paths": ["README.md", "docs/**"],
                    "documentation_triage_roles": ["task-force-workspace"],
                }
            }
        }
        classification, matched = MOD.classify(
            target,
            [{"filename": "README.md"}],
            cfg,
        )
        self.assertEqual(classification, "triage")
        self.assertEqual(matched, ["README.md"])

    def test_normative_change_still_requires_assessment(self):
        target = {
            "repository": "example/task-force",
            "context": {"type": "task-force-workspace"},
            "scope": {"include": ["README.md", "specs/**"]},
        }
        cfg = {
            "assessment": {
                "materiality": {
                    "documentation_paths": ["README.md", "docs/**"],
                    "documentation_triage_roles": ["task-force-workspace"],
                }
            }
        }
        classification, matched = MOD.classify(
            target,
            [{"filename": "README.md"}, {"filename": "specs/protocol.md"}],
            cfg,
        )
        self.assertEqual(classification, "assessment")
        self.assertEqual(matched, ["README.md", "specs/protocol.md"])


if __name__ == "__main__":
    unittest.main()
