#!/usr/bin/env python3
"""Watch selected upstream CAWG architecture issues for assessment-relevant change.

This tool intentionally watches only an allow-listed issue registry. It does not treat
GitHub issue text as normative specification content; it creates a review trigger when
an architecture/governance discussion changes materially enough to merit reassessment.
"""
from __future__ import annotations
import argparse,json,os,pathlib,sys,urllib.request,urllib.error
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
REG=ROOT/'instances/cawg/watch/issues.yaml'
STATE=ROOT/'instances/cawg/state/issues.json'
EVENTS=ROOT/'instances/cawg/state/issue-events.json'

def get_issue(repo,n,token=None):
    req=urllib.request.Request(f'https://api.github.com/repos/{repo}/issues/{n}',headers={'Accept':'application/vnd.github+json','User-Agent':'rahp-toolkit'})
    if token:req.add_header('Authorization',f'Bearer {token}')
    with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args()
    reg=yaml.safe_load(REG.read_text()); state=json.loads(STATE.read_text()) if STATE.exists() else {'version':1,'observed':{}}
    token=os.getenv('GITHUB_TOKEN'); events=[]
    for item in reg['issues']:
        key=f"{reg['repository']}#{item['number']}"
        try: issue=get_issue(reg['repository'],item['number'],token)
        except urllib.error.HTTPError as e:
            if e.code in (403,429) or 500<=e.code<600: raise
            print(f'warning: unable to resolve {key}: HTTP {e.code}',file=sys.stderr); continue
        snap={'updated_at':issue.get('updated_at'),'state':issue.get('state'),'title':issue.get('title'),'comments':issue.get('comments',0)}
        old=state['observed'].get(key)
        if old and old!=snap:
            issue_title=issue.get('title') or item['title']
            revision=(snap.get('updated_at') or 'unknown').replace(':','-')
            event_title=f"[CAWG assessment] upstream issue #{item['number']} changed @ {revision}"
            body=(f"## Why this needs RAHP review\n\nA selected upstream CAWG architecture/governance issue changed after the last observed state. Issue discussion is not normative input, but this change may alter assumptions used by the affected RAHP reviews.\n\n"
                  f"- Upstream: `{reg['repository']}#{item['number']}`\n- Theme: `{item['theme']}`\n- Affected reviews: {', '.join(item.get('affected_reviews',[])) or 'unspecified'}\n- Previous observed state: `{old}`\n- Current observed state: `{snap}`\n\nReview the discussion and any resulting branch/spec changes before re-baselining the affected assessment.")
            events.append({'title':event_title,'body':body,'labels':['assessment-required','cawg-instance'],'source':'upstream-issue','upstream_issue':item['number'],'theme':item['theme'],'affected_reviews':item.get('affected_reviews',[])})
        state['observed'][key]=snap
    if not a.check:
        STATE.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n')
        EVENTS.write_text(json.dumps(events,indent=2,sort_keys=True)+'\n')
    print(f'CAWG issue watch: {len(reg["issues"])} selected issue(s), {len(events)} assessment event(s).')
    return 0
if __name__=='__main__': raise SystemExit(main())
