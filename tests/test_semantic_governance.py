import json, pathlib, unittest, yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
class TestSemanticGovernance(unittest.TestCase):
    def test_glossary_is_substantial_and_simple_english(self):
        terms=[]
        for p in (ROOT/'method/glossary/terms').glob('*.yaml'):
            terms.append(yaml.safe_load(p.read_text()))
        self.assertGreaterEqual(len(terms),50)
        for t in terms:
            self.assertLessEqual(len(t['definition'].split()),45)
            self.assertIn('source',t)
    def test_required_guardrail_gaps_are_zero(self):
        cov=json.loads((ROOT/'build/derived/portable-catalogue-coverage.json').read_text())
        self.assertEqual(cov['required_guardrails_missing'],[])
        self.assertIn('RKP-PE-02',cov['conditional_guardrail_risks'])
    def test_generated_glossary_is_published(self):
        self.assertTrue((ROOT/'build/glossary.json').exists())
        text=(ROOT/'build/site/glossary.html').read_text()
        for term in ('Guardrail','Authority','Evidence','Cross-spec composition'):
            self.assertIn(term,text)
if __name__=='__main__': unittest.main()
