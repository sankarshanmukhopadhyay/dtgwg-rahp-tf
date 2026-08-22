import copy
import json
import unittest
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class V15ReleaseQualificationTests(unittest.TestCase):
    def test_assessment_reconstructs_without_work_item_state(self):
        doc = yaml.safe_load((ROOT / "examples/assurance-lineage/generic-specification.yaml").read_text())
        reconstructed = copy.deepcopy(doc)
        reconstructed.pop("work_items", None)
        schema = json.loads((ROOT / "method/schema/assessment-lineage.schema.json").read_text())
        errors = list(Draft202012Validator(schema).iter_errors(reconstructed))
        self.assertEqual(errors, [])
        current = reconstructed["current_run_id"]
        self.assertIn(current, {run["run_id"] for run in reconstructed["runs"]})

    def test_portable_qualification_paths_do_not_name_maintained_deployments(self):
        manifest = yaml.safe_load((ROOT / "method/v1.5-release-qualification.yaml").read_text())
        forbidden = [token.lower() for token in manifest["forbidden_core_dependencies"]]
        for rel in manifest["portable_paths"]:
            text = (ROOT / rel).read_text().lower()
            for token in forbidden:
                self.assertNotIn(token, text, f"{rel} unexpectedly depends on {token}")

    def test_stable_compatibility_contracts_are_unchanged(self):
        status = yaml.safe_load((ROOT / "PROJECT-STATUS.yaml").read_text())
        self.assertEqual(status["compatibility"]["engine_contract"], "rahp-engine-contract-v1")
        self.assertEqual(status["compatibility"]["normalized_result_schema"], 1)
        self.assertEqual(status["compatibility"]["evidence_retention_contract"], "rahp-evidence-retention-v1")

    def test_butterfly_name_is_deferred_until_release_cut(self):
        status = yaml.safe_load((ROOT / "PROJECT-STATUS.yaml").read_text())
        self.assertEqual(status["release_naming"]["selection"], "random-at-release-time")
        self.assertEqual(status["stable_release"], "1.2.0")
        self.assertEqual(status["release_status"], "unreleased")


if __name__ == "__main__":
    unittest.main()
