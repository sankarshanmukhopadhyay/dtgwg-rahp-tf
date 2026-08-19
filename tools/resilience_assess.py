#!/usr/bin/env python3
"""Run the RAHP Distributed Resilience and Amplification Risk Model (DRARM).

This adapter performs conservative static evidence discovery against a repository,
specification checkout, architecture bundle or mixed target. Detector matches are
signals, not proof by themselves. Hazardous constructs may produce high-confidence
findings; missing corroborating controls produce review-required evidence gaps.

Outputs:
- normalized JSON result for machine processing;
- Markdown assessment record for review and GitHub issue use;
- RAHP assessment-event JSON consumable by publish_assessment_issues.py.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Any

try:
    import yaml
    import jsonschema
except ImportError:
    sys.exit("resilience_assess.py requires PyYAML and jsonschema: pip install -r requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "method/resilience/catalogue.yaml"
DETECTORS = ROOT / "method/resilience/detectors.yaml"
PROFILE_SCHEMA = ROOT / "method/schema/resilience-profile.schema.json"
RESULT_SCHEMA = ROOT / "method/schema/resilience-result.schema.json"
TEXT_EXTS = {
    ".rs", ".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".java", ".kt", ".kts", ".swift",
    ".c", ".cc", ".cpp", ".h", ".hpp", ".cs", ".rb", ".php", ".scala", ".sh", ".bash",
    ".md", ".mdx", ".txt", ".rst", ".adoc", ".yaml", ".yml", ".json", ".jsonld", ".toml",
    ".xml", ".html", ".htm", ".proto", ".graphql", ".gql", ".tf", ".hcl", ".ini", ".cfg",
}


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value = yaml.safe_load(fh) or {}
    if not isinstance(value, dict):
        raise SystemExit(f"YAML root must be a mapping: {path}")
    return value


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_profile(profile: dict[str, Any]) -> None:
    jsonschema.Draft202012Validator(load_json(PROFILE_SCHEMA)).validate(profile)


def git_revision(target: pathlib.Path) -> str | None:
    if not (target / ".git").exists():
        return None
    run = subprocess.run(["git", "-C", str(target), "rev-parse", "HEAD"], capture_output=True, text=True)
    return run.stdout.strip() if run.returncode == 0 else None


def normalize_patterns(items: list[str] | None, default: list[str]) -> list[str]:
    return list(items or default)


def glob_match(path: str, pattern: str) -> bool:
    # fnmatch treats ** as ordinary *, so **/*.md misses a top-level spec.md.
    # Also test the pattern with a leading **/ removed to keep profile semantics
    # consistent for repository roots and nested paths.
    if fnmatch.fnmatch(path, pattern):
        return True
    if pattern.startswith("**/") and fnmatch.fnmatch(path, pattern[3:]):
        return True
    return False

def selected(path: str, includes: list[str], excludes: list[str]) -> bool:
    inc = any(glob_match(path, p) for p in includes)
    exc = any(glob_match(path, p) for p in excludes)
    return inc and not exc


def iter_files(target: pathlib.Path, profile: dict[str, Any]) -> list[pathlib.Path]:
    cfg = profile.get("target") or {}
    thresholds = profile.get("thresholds") or {}
    includes = normalize_patterns(cfg.get("include"), ["**/*"])
    excludes = normalize_patterns(cfg.get("exclude"), [".git/**", "node_modules/**", "vendor/**", "target/**", "build/**"])
    max_files = int(thresholds.get("max_files", 20000))
    max_bytes = int(thresholds.get("max_file_bytes", 1048576))
    out: list[pathlib.Path] = []
    for p in target.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(target).as_posix()
        if not selected(rel, includes, excludes):
            continue
        if p.suffix.lower() not in TEXT_EXTS and p.name not in {"Dockerfile", "Makefile"}:
            continue
        try:
            if p.stat().st_size > max_bytes:
                continue
        except OSError:
            continue
        out.append(p)
        if len(out) >= max_files:
            break
    return sorted(out)


def read_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def line_for(text: str, needle: str) -> int:
    idx = text.lower().find(needle.lower())
    return text[:max(0, idx)].count("\n") + 1 if idx >= 0 else 1


def first_context(text: str, needle: str, radius: int = 180) -> str:
    low = text.lower()
    idx = low.find(needle.lower())
    if idx < 0:
        return ""
    start, end = max(0, idx-radius), min(len(text), idx+len(needle)+radius)
    return " ".join(text[start:end].split())[:500]


def has_any(text_low: str, values: list[str]) -> tuple[bool, str | None]:
    for item in values:
        if item.lower() in text_low:
            return True, item
    return False, None


def is_production_evidence(rel: str) -> bool:
    parts = rel.lower().split('/')
    nonprod = {'test', 'tests', 'fixtures', 'fixture', 'examples', 'example', 'docs', 'doc', 'archive', 'bench', 'benches'}
    return not any(part in nonprod for part in parts[:-1])

def match_detector(files: list[pathlib.Path], target: pathlib.Path, detector: dict[str, Any]) -> dict[str, Any] | None:
    globs = detector.get("globs") or ["**/*"]
    any_terms = detector.get("any") or []
    context_terms = detector.get("context_any") or []
    control_terms = detector.get("control_any") or []
    matched_files: list[dict[str, Any]] = []
    control_seen = False
    control_evidence: list[dict[str, Any]] = []

    for p in files:
        rel = p.relative_to(target).as_posix()
        if not any(glob_match(rel, g) for g in globs):
            continue
        text = read_text(p)
        low = text.lower()
        matched, needle = False, None
        # For detectors with context terms, require the context close to the
        # triggering occurrence rather than merely somewhere else in the file.
        for term in any_terms:
            start = 0
            while True:
                idx = low.find(term.lower(), start)
                if idx < 0:
                    break
                if not context_terms:
                    matched, needle = True, term
                    break
                window = low[max(0, idx-800):min(len(low), idx+len(term)+800)]
                if any(c.lower() in window for c in context_terms):
                    matched, needle = True, term
                    break
                start = idx + max(1, len(term))
            if matched:
                break
        if not matched:
            # control evidence is still useful globally for this detector.
            c, cneedle = has_any(low, control_terms)
            if c:
                control_seen = True
                if len(control_evidence) < 3:
                    control_evidence.append({"path": rel, "line": line_for(text, cneedle or ""), "signal": cneedle})
            continue
        if control_terms:
            c, cneedle = has_any(low, control_terms)
            if c:
                control_seen = True
                if len(control_evidence) < 3:
                    control_evidence.append({"path": rel, "line": line_for(text, cneedle or ""), "signal": cneedle})
        if len(matched_files) < 8:
            matched_files.append({
                "path": rel,
                "line": line_for(text, needle or ""),
                "signal": needle,
                "excerpt": first_context(text, needle or ""),
            })

    if not matched_files:
        return None
    return {
        "matches": matched_files,
        "control_seen": control_seen,
        "control_evidence": control_evidence,
        "production_match": any(is_production_evidence(e["path"]) for e in matched_files),
    }


def applicability(risk: dict[str, Any], target_type: str) -> bool:
    apps = set(risk.get("applies_to") or [])
    if target_type == "mixed":
        return True
    return target_type in apps


def rule_selection(profile: dict[str, Any], catalogue: dict[str, Any]) -> list[dict[str, Any]]:
    rules = profile.get("rules") or {}
    include = set(rules.get("include") or [])
    exclude = set(rules.get("exclude") or [])
    items = []
    for r in catalogue.get("risks") or []:
        if include and r["id"] not in include:
            continue
        if r["id"] in exclude:
            continue
        items.append(r)
    return items


def filing_for(risk: dict[str, Any], finding_status: str, profile: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
    upstream = profile.get("upstream") or {}
    title = f"[{risk['id']}] {risk['title']}: define and verify amplification bounds"
    evidence_lines = "; ".join(f"{e.get('path')}:{e.get('line')} ({e.get('signal')})" for e in evidence[:4]) or "RAHP evidence gap"
    body = (
        f"## Problem\n\nRAHP DRARM identified **{risk['title']}** (`{risk['id']}`) as {finding_status}. "
        f"Trigger: {risk.get('trigger')}\n\n"
        f"## Observed evidence\n\n{evidence_lines}\n\n"
        f"## Required control outcome\n\n" + "\n".join(f"- `{c}`" for c in risk.get("required_controls") or []) + "\n\n"
        f"## Required assurance evidence\n\n" + "\n".join(f"- `{e}`" for e in risk.get("evidence_required") or []) + "\n\n"
        f"## Retest condition\n\n{risk.get('retest_when','Relevant implementation or specification changes.')}\n"
    )
    return {
        "repository": upstream.get("repository"),
        "policy": upstream.get("filing_policy", "recommend-only"),
        "labels": upstream.get("issue_labels") or [],
        "control_plane": risk.get("upstream_control_plane"),
        "title": title,
        "body": body,
    }


def assess(target: pathlib.Path, profile: dict[str, Any], repository: str | None, revision: str | None) -> dict[str, Any]:
    catalogue = load_yaml(CATALOGUE)
    detectors = (load_yaml(DETECTORS).get("detectors") or {})
    files = iter_files(target, profile)
    target_type = (profile.get("target") or {}).get("type", "mixed")
    overrides = ((profile.get("rules") or {}).get("detector_overrides") or {})

    findings: list[dict[str, Any]] = []
    pass_count = 0
    review_count = 0
    finding_count = 0

    for risk in rule_selection(profile, catalogue):
        if not applicability(risk, target_type):
            continue
        detector_results = []
        for detector_id in risk.get("detectors") or []:
            if overrides.get(detector_id) == "disabled":
                continue
            detector = detectors.get(detector_id)
            if not detector:
                continue
            result = match_detector(files, target, detector)
            if result:
                detector_results.append((detector_id, detector, result))
        if not detector_results:
            pass_count += 1
            continue

        evidence: list[dict[str, Any]] = []
        statuses: list[str] = []
        prompts: list[str] = []
        for detector_id, detector, result in detector_results:
            mode = detector.get("mode", "review_on_match")
            if overrides.get(detector_id) == "review-only":
                mode = "review_on_match"
            control_seen = bool(result.get("control_seen"))
            if mode == "finding_on_match":
                # High-confidence static findings require production-path evidence.
                # Matches confined to tests/examples/docs are retained as review evidence
                # so the detector does not turn its own fixtures into asserted defects.
                statuses.append("finding" if result.get("production_match") else "review-required")
            elif mode in {"review_on_match", "evidence_gap"}:
                statuses.append("pass" if control_seen and mode == "review_on_match" else "review-required")
            prompts.append(detector.get("prompt") or "Review the detected construct against the risk controls.")
            for ev in result.get("matches") or []:
                evidence.append({**ev, "detector": detector_id, "kind": "risk-signal"})
            for ev in result.get("control_evidence") or []:
                evidence.append({**ev, "detector": detector_id, "kind": "control-signal"})

        if "finding" in statuses:
            status, confidence = "finding", "high"
            finding_count += 1
        elif "review-required" in statuses:
            status, confidence = "review-required", "medium"
            review_count += 1
        else:
            pass_count += 1
            continue
        unique_prompts = list(dict.fromkeys(prompts))
        recommendation = " ".join(unique_prompts) + " Required controls: " + ", ".join(risk.get("required_controls") or []) + "."
        item = {
            "id": f"DR-{len(findings)+1:03d}",
            "risk_id": risk["id"],
            "title": risk["title"],
            "status": status,
            "severity": risk.get("severity", "Medium"),
            "confidence": confidence,
            "category": risk.get("category"),
            "trigger": risk.get("trigger"),
            "failure": risk.get("failure"),
            "required_controls": risk.get("required_controls") or [],
            "evidence_required": risk.get("evidence_required") or [],
            "evidence": evidence[:16],
            "recommendation": recommendation,
        }
        item["upstream_filing"] = filing_for(risk, status, profile, item["evidence"])
        findings.append(item)

    result = {
        "version": 1,
        "model": "distributed-resilience-amplification",
        "target": {
            "path": str(target),
            "type": target_type,
            "repository": repository,
            "revision": revision or git_revision(target),
        },
        "summary": {
            "rules_evaluated": finding_count + review_count + pass_count,
            "finding_count": finding_count,
            "review_gap_count": review_count,
            "pass_count": pass_count,
            "files_scanned": len(files),
        },
        "findings": findings,
        "evidence_manifest": [
            {"id": "source-tree", "class": "referenced", "description": "Static source/specification evidence scanned by DRARM", "revision": revision or git_revision(target)},
            {"id": "drarm-catalogue", "class": "durable", "description": "RAHP DRARM catalogue", "sha256": hashlib.sha256(CATALOGUE.read_bytes()).hexdigest()},
        ],
    }
    jsonschema.Draft202012Validator(load_json(RESULT_SCHEMA)).validate(result)
    return result


def render_markdown(result: dict[str, Any], profile: dict[str, Any]) -> str:
    s = result["summary"]
    lines = [
        "# Distributed Resilience and Amplification Assessment",
        "",
        f"- Model: `DRARM` / `{result['model']}`",
        f"- Profile: `{profile['profile']['id']}` — {profile['profile']['title']}",
        f"- Target: `{result['target'].get('repository') or result['target']['path']}`",
        f"- Target type: `{result['target']['type']}`",
        f"- Revision: `{result['target'].get('revision') or 'unavailable'}`",
        f"- Files scanned: **{s['files_scanned']}**",
        f"- Findings: **{s['finding_count']}**; review-required gaps: **{s['review_gap_count']}**; rules without detected signals: **{s['pass_count']}**",
        "",
        "> Detector output is evidence triage, not proof by keyword absence. High-confidence findings identify hazardous constructs directly; review-required items identify constructs whose governing control/evidence needs confirmation.",
        "",
    ]
    if not result["findings"]:
        lines += ["## Result", "", "No DRARM detector produced a finding or review-required gap in the selected target scope.", ""]
        return "\n".join(lines)
    for f in result["findings"]:
        lines += [
            f"## {f['risk_id']} — {f['title']}", "",
            f"**Status:** `{f['status']}` · **Severity:** `{f['severity']}` · **Confidence:** `{f['confidence']}`", "",
            f"**Failure model:** {f.get('failure','')}", "",
            "### Evidence", "",
        ]
        for e in f.get("evidence") or []:
            lines.append(f"- `{e.get('path')}:{e.get('line')}` — `{e.get('detector')}` / {e.get('kind')}: `{e.get('signal')}`")
        lines += ["", "### Required controls", ""]
        for c in f.get("required_controls") or []:
            lines.append(f"- `{c}`")
        lines += ["", "### Assurance evidence to produce", ""]
        for e in f.get("evidence_required") or []:
            lines.append(f"- `{e}`")
        up = f["upstream_filing"]
        lines += [
            "", "### Recommended disposition", "", f["recommendation"], "",
            "### What to file upstream", "",
            f"- Repository: `{up.get('repository') or 'set in the assessment profile'}`",
            f"- Control plane: `{up.get('control_plane')}`",
            f"- Filing policy: `{up.get('policy')}`",
            f"- Suggested title: **{up.get('title')}**", "",
            "<details><summary>Ready-to-file upstream issue body</summary>", "", up.get("body", ""), "", "</details>", "",
        ]
    return "\n".join(lines)


def event_body(result: dict[str, Any], profile: dict[str, Any], report_path: str | None = None) -> str:
    s = result["summary"]
    lines = [
        "## RAHP distributed resilience assessment",
        "",
        f"Target: `{result['target'].get('repository') or result['target']['path']}` @ `{result['target'].get('revision') or 'unavailable'}`",
        f"Profile: `{profile['profile']['id']}`",
        f"DRARM result: **{s['finding_count']} finding(s)** and **{s['review_gap_count']} review-required gap(s)** across **{s['rules_evaluated']}** evaluated rules.",
        "",
        "This issue is the durable RAHP work item. It does **not** automatically assert every review-required signal as an upstream defect. Confirm evidence and disposition here; each item below contains an upstream-ready filing recommendation.",
        "",
    ]
    if report_path:
        lines += [f"Assessment artifact: `{report_path}`", ""]
    for f in result["findings"]:
        up = f["upstream_filing"]
        lines += [
            f"### {f['risk_id']} — {f['title']}", "",
            f"- Status: `{f['status']}`; severity `{f['severity']}`; confidence `{f['confidence']}`",
            f"- Upstream repository: `{up.get('repository') or 'not configured'}`",
            f"- Upstream title: **{up['title']}**",
            f"- Required controls: {', '.join('`'+c+'`' for c in f.get('required_controls') or [])}",
            "", "<details><summary>Upstream-ready issue body</summary>", "", up["body"], "", "</details>", "",
        ]
    return "\n".join(lines)


def make_events(result: dict[str, Any], profile: dict[str, Any], report_path: str | None, run_url: str | None) -> list[dict[str, Any]]:
    threshold = (profile.get("thresholds") or {}).get("publish", "high-confidence")
    candidates = result["findings"]
    if threshold == "high-confidence":
        candidates = [f for f in candidates if f["status"] == "finding" and f["confidence"] == "high"]
    elif threshold == "all-findings":
        candidates = [f for f in candidates if f["status"] == "finding"]
    if not candidates:
        return []
    repo = result["target"].get("repository") or pathlib.Path(result["target"]["path"]).name
    rev = result["target"].get("revision") or "unversioned"
    key = f"resilience:{repo}:{rev}"
    body = event_body(result, profile, report_path)
    if run_url:
        body += f"\n\nWorkflow evidence: {run_url}\n"
    return [{
        "assessment_key": key,
        "source": "distributed-resilience-assessment",
        "title": f"RAHP resilience assessment: {repo} @ {rev[:12]}",
        "repository": repo,
        "observed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "labels": ["assessment-required", "distributed-resilience", "load-amplification"],
        "body": body,
    }]


def write(path: pathlib.Path | None, text: str) -> None:
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", type=pathlib.Path, required=True, help="checked-out repository or extracted specification bundle")
    ap.add_argument("--profile", type=pathlib.Path, default=ROOT / "profiles/resilience/default.yaml")
    ap.add_argument("--repository", help="owner/repository identity for provenance and upstream filing")
    ap.add_argument("--revision", help="tag/commit/revision when target is not a Git checkout")
    ap.add_argument("--json", dest="json_path", type=pathlib.Path, default=ROOT / "build/resilience/result.json")
    ap.add_argument("--markdown", type=pathlib.Path, default=ROOT / "build/resilience/report.md")
    ap.add_argument("--events", type=pathlib.Path, default=ROOT / "build/resilience/issue-events.json")
    ap.add_argument("--run-url")
    args = ap.parse_args()
    if not args.target.exists() or not args.target.is_dir():
        raise SystemExit(f"target directory not found: {args.target}")
    profile = load_yaml(args.profile)
    validate_profile(profile)
    result = assess(args.target.resolve(), profile, args.repository, args.revision)
    write(args.json_path, json.dumps(result, indent=2) + "\n")
    write(args.markdown, render_markdown(result, profile) + "\n")
    events = make_events(result, profile, str(args.markdown) if args.markdown else None, args.run_url)
    write(args.events, json.dumps(events, indent=2) + "\n")
    s = result["summary"]
    print(f"DRARM assessed {s['rules_evaluated']} rules across {s['files_scanned']} files: {s['finding_count']} finding(s), {s['review_gap_count']} review gap(s)")
    print(f"Issue publication events: {len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
