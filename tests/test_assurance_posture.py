import unittest
from tools.assurance_posture import build_posture


class AssurancePostureTests(unittest.TestCase):
    def test_actionable_counts_without_score(self):
        source = {
            "scope": {"id": "x", "kind": "project"},
            "records": [
                {"assessment_id":"a","conclusion":"controlled","freshness":"current","remediation":"resolved","gate":"PASS","authority":"authorized","evidence_gaps":0},
                {"assessment_id":"b","conclusion":"assurance-gap","freshness":"retest-required","remediation":"retest-pending","gate":"INDETERMINATE","authority":"not-evaluated","evidence_gaps":2},
            ],
        }
        result = build_posture(source, "2026-08-22T00:00:00Z")
        self.assertEqual(result["summary"]["total"], 2)
        self.assertEqual(result["summary"]["action_required"], 1)
        self.assertEqual(result["summary"]["stale_or_retest"], 1)
        self.assertEqual(result["summary"]["evidence_gaps"], 2)
        self.assertNotIn("score", result["summary"])

    def test_gate_and_authority_are_separate(self):
        source = {"scope":{"id":"x","kind":"project"},"records":[
            {"assessment_id":"a","conclusion":"assured","freshness":"current","remediation":"none","gate":"PASS","authority":"denied","evidence_gaps":0}
        ]}
        result = build_posture(source, "2026-08-22T00:00:00Z")
        self.assertEqual(result["summary"]["gate_blocked"], 0)
        self.assertEqual(result["summary"]["authority_blocked"], 1)


if __name__ == "__main__":
    unittest.main()
