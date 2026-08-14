import ast
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_jtd_site.py"


def literal_assignment(name):
    tree = ast.parse(VALIDATOR.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return ast.literal_eval(node.value)
    raise AssertionError(f"{name} not found")


class TestJtdBaseUrlRegression(unittest.TestCase):
    def test_rahp_toolkit_baseurl_links_resolve_from_site_root(self):
        with tempfile.TemporaryDirectory() as td:
            site = pathlib.Path(td)
            html = "<!doctype html><html><body>ok</body></html>"
            for rel in literal_assignment("REQUIRED_DOCS") + literal_assignment("REQUIRED_PROJECTIONS"):
                p = site / rel
                # Mirror validate_jtd_site's acceptable Jekyll materializations.
                if rel.endswith((".yaml", ".yml", ".json", ".jsonld")):
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(html, encoding="utf-8")
                elif pathlib.Path(rel).suffix in {".md"}:
                    p = p.with_suffix(".md.html")
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(html, encoding="utf-8")
                else:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(html, encoding="utf-8")
            target = site / "docs" / "baseurl-target.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
            source = site / "docs" / "baseurl-source.html"
            source.write_text('<!doctype html><html><body><a href="/rahp-toolkit/docs/baseurl-target.html">target</a></body></html>', encoding="utf-8")
            run = subprocess.run([sys.executable, str(VALIDATOR), str(site)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
