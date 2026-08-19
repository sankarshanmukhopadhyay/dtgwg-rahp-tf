import importlib.util
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('cross_spec_review', ROOT/'tools/cross_spec_review.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
REG=ROOT/'profiles/dtg/cross-spec-tests.yaml'

class CrossSpecReviewTests(unittest.TestCase):
    def test_runnable_composition_renders_upstream_section(self):
        registry=mod.load_yaml(REG)
        item=mod.composition(registry,'trust-tasks--credential-spec')
        item['_profile_id']='dtg'; item['_issue_labels']=['assessment-required','dtg-instance','cross-specification']
        assessment=mod.load_yaml(ROOT/item['assessment'])
        body=mod.render_issue(item,assessment,'https://github.example/run/1')
        self.assertIn('## Upstream issue candidates',body)
        self.assertIn('## WG review and disposition',body)
        self.assertIn('trustoverip/dtgwg-trust-tasks-tf',body)
        self.assertIn('[Cross-spec][F-001]',body)
        self.assertIn('Profile: `dtg`',body)
    def test_all_dtg_compositions_are_runnable(self):
        registry=mod.load_yaml(REG)
        self.assertEqual(8, len(registry['compositions']))
        for entry in registry['compositions']:
            self.assertTrue(entry['runnable'], entry['id'])
            item=mod.composition(registry,entry['id'])
            self.assertTrue((ROOT/item['assessment']).exists())
    def test_unknown_composition_fails(self):
        registry=mod.load_yaml(REG)
        with self.assertRaises(ValueError): mod.composition(registry,'does-not-exist')
    def test_event_key_is_profile_scoped(self):
        registry=mod.load_yaml(REG); item=mod.composition(registry,'credential-spec--zkp')
        item['_profile_id']='dtg'; item['_issue_labels']=['assessment-required','cross-specification']
        ev=mod.event_for(item,'body')
        self.assertEqual('dtg:cross-spec:credential-spec--zkp',ev['assessment_key'])
if __name__=='__main__': unittest.main()
