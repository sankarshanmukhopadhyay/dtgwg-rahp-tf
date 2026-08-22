import unittest
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from impact import analyze  # noqa: E402


class AssuranceGraphImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = yaml.safe_load((ROOT / "examples" / "assurance-lineage" / "generic-assurance-graph.yaml").read_text())

    def test_target_change_selects_assessment(self):
        result = analyze(self.graph, ["target:payments-api"])
        self.assertIn("example:specification:payments-api", result["retest_required"])

    def test_control_change_propagates_to_test_evidence_and_assessment(self):
        result = analyze(self.graph, ["control:authorization-check"])
        ids = {item["id"] for item in result["affected_nodes"]}
        self.assertIn("test:authorization-revoked", ids)
        self.assertIn("evidence:test-run", ids)
        self.assertIn("assessment:payments-auth", ids)

    def test_unknown_node_is_reported_without_false_impact(self):
        result = analyze(self.graph, ["unknown:thing"])
        self.assertEqual([], result["affected_nodes"])
        self.assertEqual(["unknown:thing"], result["unresolved_changed_nodes"])
        self.assertEqual([], result["retest_required"])

    def test_impact_is_deterministic(self):
        first = analyze(self.graph, ["target:payments-api"])
        second = analyze(self.graph, ["target:payments-api"])
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
