import importlib.util
import unittest
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('cross_spec_review', ROOT/'tools/cross_spec_review.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class CrossSpecReviewTests(unittest.TestCase):
    def test_maintained_composition_renders_upstream_section(self):
        registry=mod.load_yaml(ROOT/'instances/dtg/cross-spec-tests.yaml')
        item=mod.composition(registry,'trust-tasks--credential-spec')
        assessment=mod.load_yaml(ROOT/item['assessment'])
        body=mod.render_issue(item,assessment,'https://github.example/run/1')
        self.assertIn('## Upstream issue candidates',body)
        self.assertIn('## WG review and disposition',body)
        self.assertIn('trustoverip/dtgwg-trust-tasks-tf',body)
        self.assertIn('[Cross-spec][F-001]',body)
    def test_candidate_is_not_runnable(self):
        registry=mod.load_yaml(ROOT/'instances/dtg/cross-spec-tests.yaml')
        with self.assertRaises(ValueError): mod.composition(registry,'credential-spec--zkp')
if __name__=='__main__': unittest.main()
