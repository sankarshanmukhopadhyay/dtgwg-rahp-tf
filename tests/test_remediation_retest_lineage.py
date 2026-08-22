from copy import deepcopy
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_remediation_retest_lineage import semantic_errors  # noqa: E402


class RemediationRetestLineageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = ROOT / "examples" / "assurance-lineage"
        cls.remediation = yaml.safe_load((base / "generic-remediation.yaml").read_text(encoding="utf-8"))
        cls.retest = yaml.safe_load((base / "generic-retest.yaml").read_text(encoding="utf-8"))

    def test_generic_fixture_is_semantically_valid(self):
        self.assertEqual([], semantic_errors(self.remediation, self.retest))

    def test_resolved_requires_passing_closure_evidence(self):
        retest = deepcopy(self.retest)
        retest["closure_evidence"][0]["result"] = "fail"
        errors = semantic_errors(self.remediation, retest)
        self.assertTrue(any("lacks passing evidence" in error for error in errors))
        self.assertTrue(any("non-passing closure evidence" in error for error in errors))

    def test_indeterminate_cannot_be_closed(self):
        retest = deepcopy(self.retest)
        retest["outcome"] = "indeterminate"
        retest["disposition"]["status"] = "closed"
        errors = semantic_errors(self.remediation, retest)
        self.assertIn("inconclusive or indeterminate retest cannot be closed", errors)

    def test_retest_must_resolve_remediation_identity(self):
        retest = deepcopy(self.retest)
        retest["remediation_id"] = "REM-other"
        self.assertIn("retest remediation_id does not resolve to the remediation", semantic_errors(self.remediation, retest))


if __name__ == "__main__":
    unittest.main()
