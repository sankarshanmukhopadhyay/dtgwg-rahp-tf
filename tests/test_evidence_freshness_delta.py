import unittest

from tools.assurance_state import conclusion_transition, freshness_from_basis


class EvidenceFreshnessDeltaTests(unittest.TestCase):
    def test_requires_retest_dominates_potential(self):
        status, retest = freshness_from_basis([
            {"effect": "potential"},
            {"effect": "requires-retest"},
        ])
        self.assertEqual(status, "retest-required")
        self.assertTrue(retest)

    def test_invalidating_is_stale(self):
        status, retest = freshness_from_basis([{"effect": "invalidating"}])
        self.assertEqual(status, "stale")
        self.assertTrue(retest)

    def test_unknown_preserves_uncertainty(self):
        status, retest = freshness_from_basis([{"effect": "unknown"}])
        self.assertEqual(status, "indeterminate")
        self.assertTrue(retest)

    def test_resolution_transition(self):
        self.assertEqual(conclusion_transition("finding", "controlled"), "resolved")

    def test_regression_transition(self):
        self.assertEqual(conclusion_transition("assured", "finding"), "regressed")

    def test_unchanged_transition(self):
        self.assertEqual(conclusion_transition("controlled", "controlled"), "unchanged")


if __name__ == "__main__":
    unittest.main()
