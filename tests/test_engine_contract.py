import json, pathlib, sys, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from engine_contract import validate_result, load_result, retention_plan

class EngineContractTests(unittest.TestCase):
    def test_valid_fixture(self):
        self.assertTrue(validate_result(ROOT/'tests/conformance/engine/valid-minimal/result.json',quiet=True))
    def test_missing_revision_invalid(self):
        self.assertFalse(validate_result(ROOT/'tests/conformance/engine/invalid-missing-revision/result.json',quiet=True))
    def test_referenced_evidence_requires_integrity_metadata(self):
        self.assertFalse(validate_result(ROOT/'tests/conformance/engine/invalid-referenced-evidence-no-hash/result.json',quiet=True))
    def test_durable_is_committed_ephemeral_is_not(self):
        result=load_result(ROOT/'tests/conformance/engine/valid-minimal/result.json')
        result['evidence'].append({'id':'LOG-1','class':'ephemeral','description':'run log'})
        plan=retention_plan(result)
        actions={a['id']:a['action'] for a in plan['actions']}
        self.assertEqual(actions['EV-1'],'commit')
        self.assertEqual(actions['LOG-1'],'do-not-commit')
if __name__=='__main__': unittest.main()
