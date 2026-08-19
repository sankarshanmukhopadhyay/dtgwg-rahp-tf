#!/usr/bin/env python3
"""DTG RAHP instance portfolio discovery and material-change assessment queue.

This module is instance-specific. The portable RAHP engine in tools/rahp.py does not
import or depend on it.
"""
from __future__ import annotations
import argparse, fnmatch, json, os, pathlib, re, sys, urllib.error, urllib.request
from datetime import datetime, timezone
from typing import Any
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_CFG = ROOT / "instances/dtg/instance.yaml"

def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def api_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "dtg-rahp-instance/0.5",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def raw_text(repo: str, branch: str, path: str) -> str:
    url=f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
    req=urllib.request.Request(url, headers={"User-Agent":"dtg-rahp-instance/0.5"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode()

def slug(repo: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", repo.lower()).strip("-")

def discover(cfg: dict[str,Any]) -> list[dict[str,Any]]:
    p=cfg["portfolio"]
    registry=yaml.safe_load(raw_text(p["registry_repository"], p.get("registry_branch","main"), p["registry_path"]))
    base=[]
    for r in registry.get("repositories", []):
        base.append({
            "id": slug(r["repo"]), "repository": r["repo"],
            "branch": r.get("default_branch","main"),
            "source": "portfolio-monitor",
            "upstream": None,
            "workstream": r.get("workstream"),
            "role": r.get("role"),
            "lifecycle": r.get("lifecycle","active"),
            "reporting_weight": r.get("reporting_weight","medium"),
            "material_paths": r.get("material_paths", []),
            "reviews": ["rahp","security","combined"],
        })
    base_names={x["repository"] for x in base}
    owner=p.get("fork_owner")
    if owner:
        page=1
        while True:
            repos=api_json(f"https://api.github.com/users/{owner}/repos?per_page=100&page={page}&type=owner")
            if not repos: break
            for r in repos:
                if not r.get("fork"): continue
                detail=api_json(r["url"])
                parent=(detail.get("parent") or {}).get("full_name")
                if parent in base_names:
                    upstream=next(x for x in base if x["repository"]==parent)
                    base.append({
                        **upstream,
                        "id": slug(r["full_name"]),
                        "repository": r["full_name"],
                        "branch": r.get("default_branch","main"),
                        "source": "portfolio-fork",
                        "upstream": parent,
                    })
            if len(repos)<100: break
            page+=1
    # This RAHP repo is a deployment host, not a target for recursive review.
    review_repo=cfg["instance"].get("review_repository")
    for x in base:
        x["self_hosted_instance"] = x["repository"] == review_repo
    return base

def head_sha(repo: str, branch: str) -> str | None:
    """Resolve a branch head, tolerating repositories with no commit history.

    GitHub returns HTTP 409 for an empty/uninitialised Git repository. That is a
    repository state, not a monitor failure, so callers receive ``None`` and may
    record the target as not-yet-initialised. Other HTTP failures remain fatal so
    authentication, permission, or API outages are not silently hidden.
    """
    try:
        return api_json(f"https://api.github.com/repos/{repo}/commits/{branch}")["sha"]
    except urllib.error.HTTPError as exc:
        if exc.code == 409:
            return None
        raise

def compare(repo: str, base: str, head: str) -> dict[str,Any]:
    return api_json(f"https://api.github.com/repos/{repo}/compare/{base}...{head}")

def path_matches(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path,p) or pathlib.PurePosixPath(path).match(p) for p in patterns)

def classify(target: dict[str,Any], files: list[dict[str,Any]], cfg: dict[str,Any]) -> tuple[str,list[str],list[str]]:
    mc=cfg["assessment"]["materiality"]
    configured=target.get("material_paths",[])
    always=mc.get("always_material_paths",[])
    matched=[]
    reasons=[]
    for f in files:
        p=f["filename"]
        if path_matches(p, configured + always):
            matched.append(p)
    if matched:
        reasons.append(f"{len(matched)} changed file(s) match the target's material assessment scope")
    if target.get("reporting_weight") in mc.get("review_weights",[]) and files:
        reasons.append(f"portfolio reporting weight is {target.get('reporting_weight')}")
    if target.get("lifecycle")=="transitional" and not mc.get("include_transitional",True):
        return "ignore", matched, ["transitional repository excluded by DTG instance policy"]
    if not matched:
        return "ignore", matched, reasons

    # Some repository roles use README/docs as operational routing surfaces rather
    # than normative specification text. For those roles, documentation-only
    # movement is significant enough to record, but should be triaged before a
    # full RAHP/security assessment is opened. This prevents canonical-source
    # relocations and repository housekeeping from becoming false-positive
    # assurance work while preserving an auditable governance signal.
    documentation = mc.get("documentation_paths", [])
    triage_roles = set(mc.get("documentation_triage_roles", []))
    role = target.get("role")
    docs_only = bool(documentation) and all(path_matches(p, documentation) for p in matched)
    if role in triage_roles and docs_only:
        reasons.append("all material matches are documentation/routing paths for a triage-enabled repository role")
        return "triage", matched, reasons

    return "assessment", matched, reasons

def assessment_key(repo: str) -> str:
    return f"dtg:repository:{repo}"

def issue_mark(repo: str, sha: str) -> str:
    return f"<!-- rahp-assessment-key:{assessment_key(repo)} -->\n<!-- rahp-dtg-change:{repo}@{sha} -->"

def issue_body(target:dict[str,Any], old:str, new:str, comp:dict[str,Any], matched:list[str], reasons:list[str]) -> str:
    files=comp.get("files",[])
    commits=comp.get("commits",[])
    rows="\n".join(f"| `{f['filename']}` | {f.get('status','')} | +{f.get('additions',0)} / -{f.get('deletions',0)} | {'yes' if f['filename'] in matched else 'no'} |" for f in files[:100])
    commit_rows="\n".join(f"- `{c['sha'][:12]}` {c['commit']['message'].splitlines()[0]}" for c in commits[:50])
    why="\n".join(f"- {r}" for r in reasons) or "- Change intersects configured material paths."
    return f"""# DTG RAHP assessment required

{issue_mark(target['repository'],new)}

A change in a repository tracked by the DTG Portfolio Monitor has crossed the DTG
RAHP instance's configured materiality boundary. This issue is an **assessment queue
record**, not a finding and not evidence that the change is unsafe.

## Target

| Field | Value |
|---|---|
| Repository | `{target['repository']}` |
| Upstream | `{target.get('upstream') or 'n/a'}` |
| Portfolio source | `{target['source']}` |
| Workstream | `{target.get('workstream') or 'n/a'}` |
| Role | `{target.get('role') or 'n/a'}` |
| Lifecycle | `{target.get('lifecycle')}` |
| Reporting weight | `{target.get('reporting_weight')}` |
| Previous assessed/observed SHA | `{old}` |
| Current SHA | `{new}` |
| Compare | https://github.com/{target['repository']}/compare/{old}...{new} |

## Why review is required

{why}

The change is therefore queued for **combined RAHP + security review** by default.
A reviewer may narrow the mode if the evidence shows that only one lens is relevant.

## Material files

| File | Status | Delta | In material scope |
|---|---|---:|---|
{rows or '| _No file metadata returned_ | | | |'}

## Commits in the change window

{commit_rows or '- No commit metadata returned.'}

## Required review actions

1. Inspect the revision delta rather than reassessing unrelated repository content.
2. Determine whether changed requirements, schemas, workflows or implementation guidance
   alter existing risks, harms, controls, guardrails, threat assumptions or assurance evidence.
3. Run the appropriate RAHP, security or combined workflow using the target revision.
4. Store durable review artefacts under `instances/dtg/reviews/`.
5. Link findings to the affected specification text and existing RAHP catalogue entries.
6. Record the disposition: no material assurance impact, finding(s) raised, remediation
   requested, or risk accepted by the relevant governance authority.
7. Close this issue only when the assessment record identifies the reviewed SHA `{new}`.

## Reproduce the workspace

```bash
python3 tools/rahp.py review --config instances/dtg/generated/repositories.yaml --mode combined --target {target['id']}
```

For dynamically discovered DTG targets, use the repository and SHA above when creating
the canonical review record.

## Governance note

This issue was raised by the **DTG instance automation**. It is deliberately separate
from the portable RAHP toolkit. Other adopters do not inherit this portfolio, queue,
or DTG governance state.
"""

def triage_body(target:dict[str,Any], old:str, new:str, comp:dict[str,Any], matched:list[str], reasons:list[str]) -> str:
    files=comp.get("files",[])
    commits=comp.get("commits",[])
    rows="\n".join(f"| `{f['filename']}` | {f.get('status','')} | +{f.get('additions',0)} / -{f.get('deletions',0)} | {'yes' if f['filename'] in matched else 'no'} |" for f in files[:100])
    commit_rows="\n".join(f"- `{c['sha'][:12]}` {c['commit']['message'].splitlines()[0]}" for c in commits[:50])
    why="\n".join(f"- {r}" for r in reasons) or "- Documentation/routing change requires classification."
    return f"""# DTG change classification required

{issue_mark(target['repository'],new)}

A change in a repository tracked by the DTG Portfolio Monitor intersects configured
material paths, but the changed material is limited to documentation/routing surfaces
for a repository role configured for **triage before assessment**.

This is a **classification queue record**, not a RAHP finding and not an assessment
requirement. Its purpose is to distinguish substantive assurance changes from repository
topology, canonical-source relocation, editorial routing, or other operational changes.

## Target

| Field | Value |
|---|---|
| Repository | `{target['repository']}` |
| Workstream | `{target.get('workstream') or 'n/a'}` |
| Role | `{target.get('role') or 'n/a'}` |
| Lifecycle | `{target.get('lifecycle')}` |
| Previous observed SHA | `{old}` |
| Current SHA | `{new}` |
| Compare | https://github.com/{target['repository']}/compare/{old}...{new} |

## Why classification is required

{why}

## Changed files

| File | Status | Delta | In configured scope |
|---|---|---:|---|
{rows or '| _No file metadata returned_ | | | |'}

## Commits in the change window

{commit_rows or '- No commit metadata returned.'}

## Required classification

Choose one disposition:

- **assessment-required** — semantics, assurance assumptions, security properties, governance dependencies, or interoperability behaviour changed;
- **topology-change** — canonical source, repository ownership/location, or portfolio routing changed without changing the governed semantics;
- **editorial/no-assurance-impact** — the change does not alter assurance-relevant behaviour.

If `assessment-required`, open or promote an assessment work item for this revision.
For the other dispositions, record the classification evidence and update portfolio/canonical-source metadata where necessary without running a RAHP/security assessment.

## Governance note

Classification is intentionally separate from assessment. A material operational change
can require attention without implying that substantive RAHP review is warranted.
"""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("command", choices=["sync","check"])
    ap.add_argument("--config", type=pathlib.Path, default=DEFAULT_CFG)
    ap.add_argument("--initialize", action="store_true", help="record current heads without raising review events")
    args=ap.parse_args()
    cfg=load_yaml(args.config)
    targets=discover(cfg)
    manifest=ROOT/cfg["generated"]["manifest"]
    manifest.parent.mkdir(parents=True,exist_ok=True)
    portable_targets=[]
    for t in targets:
        portable_targets.append({
            "id": t["id"],
            "repository": t["repository"],
            "branch": t["branch"],
            **({"upstream": t["upstream"]} if t.get("upstream") else {}),
            "context": {
                "title": t["repository"],
                "type": t.get("role") or "repository",
                "description": f"DTG instance target discovered from {t['source']}; workstream={t.get('workstream') or 'n/a'}; lifecycle={t.get('lifecycle') or 'n/a'}; reporting_weight={t.get('reporting_weight') or 'n/a'}."
            },
            "scope": {"include": t.get("material_paths") or ["README.md","docs/**","specs/**","schemas/**","**/*spec*.md",".github/workflows/**"]},
            "reviews": ["rahp","security","combined"],
        })
    generated_profile={
        "version":1,
        "profile":{
            "id":"dtg-discovered",
            "title":"DTG RAHP discovered portfolio",
            "description":"Generated DTG Working Group RAHP deployment profile. Do not hand edit.",
            "owner":"DTG RAHP instance",
        },
        "assessment":{"default_mode":cfg["assessment"].get("default_mode","combined")},
        "repositories":portable_targets,
        "output":{"directory":"build/targets"},
        "governance":{"namespace":"dtg"},
        "extensions":{
            "generated_at":datetime.now(timezone.utc).isoformat(),
            "source_registry":cfg["portfolio"]["registry_repository"],
            "fork_owner":cfg["portfolio"].get("fork_owner"),
        },
    }
    manifest.write_text(yaml.safe_dump(generated_profile,sort_keys=False),encoding="utf-8")
    print(f"discovered {len(targets)} DTG instance target(s)")
    if args.command=="sync":
        return
    state_path=ROOT/cfg["state"]["file"]
    state_path.parent.mkdir(parents=True,exist_ok=True)
    state=json.loads(state_path.read_text()) if state_path.exists() else {"version":1,"repositories":{}}
    events=[]
    for t in targets:
        # avoid self-recursive assessment issue storms for this deployment host
        if t.get("self_hosted_instance"):
            continue
        repo=t["repository"]
        old_entry=state["repositories"].get(repo,{})
        old=old_entry.get("sha")
        print(f"checking {repo}@{t['branch']}")
        new=head_sha(repo,t["branch"])
        if new is None:
            # An empty repository is a valid discovered portfolio state. Keep any
            # last known SHA for provenance, mark the current source condition,
            # and continue assessing the rest of the portfolio.
            state["repositories"][repo]={
                **({"sha": old} if old else {}),
                "status":"no-commits",
                "observed_at":datetime.now(timezone.utc).isoformat(),
            }
            print(f"warning: {repo}@{t['branch']} has no commit history; skipped until a head revision exists")
            continue
        if not old or args.initialize:
            state["repositories"][repo]={"sha":new,"status":"active","observed_at":datetime.now(timezone.utc).isoformat()}
            continue
        if old==new: continue
        try:
            comp=compare(repo,old,new)
            classification,matched,reasons=classify(t,comp.get("files",[]),cfg)
        except Exception as exc:
            classification="assessment"; matched=[]; reasons=[f"unable to compare prior SHA cleanly; conservative review required ({exc})"]
            comp={"files":[],"commits":[]}
        if classification == "assessment":
            events.append({"target":t,"old":old,"new":new,"matched":matched,"reasons":reasons,
                           "assessment_key": assessment_key(repo),
                           "source": "repository-change",
                           "repository": repo,
                           "event_class": "assessment-required",
                           "title":f"[RAHP review required] {repo}: {old[:7]} → {new[:7]}",
                           "body":issue_body(t,old,new,comp,matched,reasons),
                           "labels": cfg.get("assessment",{}).get("issue",{}).get("labels",["assessment-required","dtg-instance"])})
        elif classification == "triage":
            events.append({"target":t,"old":old,"new":new,"matched":matched,"reasons":reasons,
                           "assessment_key": f"dtg:classification:{repo}",
                           "source": "repository-change",
                           "repository": repo,
                           "event_class": "change-triage",
                           "title":f"[Change triage] {repo}: {old[:7]} → {new[:7]}",
                           "body":triage_body(t,old,new,comp,matched,reasons),
                           "labels": ["change-triage","dtg-instance"]})
        state["repositories"][repo]={"sha":new,"status":"active","observed_at":datetime.now(timezone.utc).isoformat()}
    state_path.write_text(json.dumps(state,indent=2)+"\n")
    events_path=ROOT/"instances/dtg/generated/review-events.json"
    events_path.write_text(json.dumps(events,indent=2)+"\n")
    print(f"material review event(s): {len(events)}")
if __name__=="__main__":
    main()
