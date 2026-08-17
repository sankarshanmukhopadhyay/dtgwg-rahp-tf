import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "build" / "site"


class TestGeneratedAssuranceSite(unittest.TestCase):
    def test_portable_catalogue_is_generated(self):
        text = (SITE / "portable-catalogue.html").read_text()
        for token in ("HRM-AUT-01", "RKP-AUTH-01", "CTP-AUTH-01", "GRP-AUTH-01", "ATP-AUTH-01", "EVP-AUTH-01"):
            self.assertIn(token, text)
        self.assertIn("Portable method layer", text)

    def test_assurance_graph_contains_coverage_and_head_evidence(self):
        text = (SITE / "assurance-graph.html").read_text()
        self.assertIn("Portable assurance chain", text)
        self.assertIn("Coverage diagnostics", text)
        self.assertIn("HQ-2026-08-17-v1.1.0", text)
        self.assertIn("11 live repos", text)

    def test_legacy_catalogue_is_explicitly_deployment_scoped(self):
        text = (SITE / "catalogue.html").read_text()
        self.assertIn("DTG deployment catalogue", text)
        self.assertIn("portable assurance catalogue", text)
        self.assertNotIn("Canonical RAHP reference catalogue", text)

    def test_operational_assurance_is_deployment_scoped(self):
        text = (SITE / "assurance.html").read_text()
        self.assertIn("DTG operational assurance", text)
        self.assertIn("v1.1 portable ATP/EVP model", text)

    def test_glossary_and_guardrail_closure_are_generated(self):
        glossary = (SITE / "glossary.html").read_text()
        self.assertIn("RAHP terms explained in simple English", glossary)
        graph = (SITE / "assurance-graph.html").read_text()
        self.assertIn("Required guardrails missing", graph)
        self.assertIn("Conditional guardrail risks", graph)

    def test_standalone_toolkit_links_to_site_only_views(self):
        text = (ROOT / "build" / "rahp-toolkit.html").read_text()
        self.assertIn('href="site/portable-catalogue.html"', text)
        self.assertIn('href="site/assurance-graph.html"', text)
        self.assertNotIn('href="portable-catalogue.html"', text)
        self.assertNotIn('href="assurance-graph.html"', text)


if __name__ == "__main__":
    unittest.main()
