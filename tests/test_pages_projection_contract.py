import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class TestPagesProjectionContract(unittest.TestCase):
    def test_cawg_mandate_readiness_is_projected_from_instances(self):
        plugin = (ROOT / "_plugins" / "structured_data_pages.rb").read_text()
        validator = (ROOT / "tools" / "validate_jtd_site.py").read_text()
        self.assertIn("instances/cawg/mandate-readiness.yaml", plugin)
        self.assertIn("instances/cawg/mandate-readiness.yaml", validator)
        self.assertIn("instances/cawg/watch/issues.yaml", plugin)
        self.assertIn("instances/dtg/watch/issues.yaml", plugin)
        self.assertIn("instances/cawg/watch/issues.yaml", validator)
        self.assertIn("instances/dtg/watch/issues.yaml", validator)

    def test_cawg_docs_link_to_projected_readme_not_directory(self):
        for rel in ("docs/cawg-instance.md", "docs/cawg-mandate-readiness.md"):
            text = (ROOT / rel).read_text()
            self.assertNotIn("(../examples/cawg-c2pa/)", text)
            self.assertIn("../examples/cawg-c2pa/README.md", text)


if __name__ == "__main__":
    unittest.main()
