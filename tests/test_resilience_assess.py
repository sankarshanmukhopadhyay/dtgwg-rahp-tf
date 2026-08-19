import json, pathlib, subprocess, sys, tempfile, unittest
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
TOOL=ROOT/'tools/resilience_assess.py'

class ResilienceAssessTests(unittest.TestCase):
    def run_target(self, files):
        with tempfile.TemporaryDirectory() as td:
            t=pathlib.Path(td)/'target'; t.mkdir()
            for name,content in files.items():
                p=t/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content)
            result=pathlib.Path(td)/'result.json'; report=pathlib.Path(td)/'report.md'; events=pathlib.Path(td)/'events.json'
            subprocess.run([sys.executable,str(TOOL),'--target',str(t),'--profile',str(ROOT/'profiles/resilience/default.yaml'),'--repository','example/test','--revision','abc123','--json',str(result),'--markdown',str(report),'--events',str(events)],check=True,capture_output=True,text=True)
            return json.loads(result.read_text()), report.read_text(), json.loads(events.read_text())

    def test_unbounded_channel_is_high_confidence_finding(self):
        result, report, events=self.run_target({'src/main.rs':'let (tx, rx) = tokio::sync::mpsc::unbounded_channel();'})
        rows=[x for x in result['findings'] if x['risk_id']=='RLA-005']
        self.assertTrue(rows)
        self.assertEqual(rows[0]['status'],'finding')
        self.assertEqual(rows[0]['confidence'],'high')
        self.assertIn('What to file upstream', report)
        self.assertEqual(len(events),1)

    def test_retry_backoff_with_jitter_reduces_review_signals(self):
        src='''fn retry(){ let max_retries=4; let backoff=2; let jitter=rand::random::<u64>(); let idempotency_key="x"; }'''
        result,_,_=self.run_target({'src/main.rs':src})
        retry=[x for x in result['findings'] if x['risk_id']=='RLA-001']
        self.assertFalse(retry)

    def test_review_gap_contains_upstream_payload(self):
        result,_,_=self.run_target({'spec.md':'The client retries delivery when the transport fails.'})
        row=next(x for x in result['findings'] if x['risk_id']=='RLA-001')
        self.assertEqual(row['status'],'review-required')
        self.assertIn('Required control outcome',row['upstream_filing']['body'])

if __name__=='__main__': unittest.main()
