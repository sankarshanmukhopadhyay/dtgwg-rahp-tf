import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("dtg_portfolio", ROOT / "tools" / "dtg_portfolio.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class DtgPortfolioClassificationTests(unittest.TestCase):
    def cfg(self):
        return {
            "assessment": {
                "materiality": {
                    "review_weights": ["critical", "high"],
                    "include_transitional": True,
                    "always_material_paths": ["schemas/**", "specs/**", "**/*spec*.md"],
                    "documentation_paths": ["README.md", "docs/**"],
                    "documentation_triage_roles": ["task-force-workspace", "legacy-or-transition"],
                }
            }
        }

    def test_issue_16_shape_is_triage_not_assessment(self):
        target = {
            "role": "task-force-workspace",
            "reporting_weight": "high",
            "lifecycle": "active",
            "material_paths": ["README.md", "docs/**", "specs/**", "schemas/**", "**/*spec*.md"],
        }
        files = [
            {"filename": "README.md"},
            {"filename": "dtg.md"},
        ]
        classification, matched, reasons = MOD.classify(target, files, self.cfg())
        self.assertEqual(classification, "triage")
        self.assertEqual(matched, ["README.md"])
        self.assertTrue(any("triage-enabled" in r for r in reasons))

    def test_spec_change_remains_assessment(self):
        target = {
            "role": "task-force-workspace",
            "reporting_weight": "high",
            "lifecycle": "active",
            "material_paths": ["README.md", "specs/**"],
        }
        files = [{"filename": "README.md"}, {"filename": "specs/credential-spec.md"}]
        classification, matched, _ = MOD.classify(target, files, self.cfg())
        self.assertEqual(classification, "assessment")
        self.assertEqual(matched, ["README.md", "specs/credential-spec.md"])


if __name__ == "__main__":
    unittest.main()
