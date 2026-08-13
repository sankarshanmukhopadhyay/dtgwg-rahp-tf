#!/usr/bin/env python3
"""
tf_actions.py — derive the Task Force Action Register from canonical RAHP state.

The register is intentionally derived rather than hand-maintained. A canonical
record remains the source of truth; this tool turns unresolved governance states
into stable, itemized work items so decisions cannot disappear into roadmap prose.

Current action sources:
- controls / guardrails whose standards_status is unassigned
- proposed rule profiles
- proposed governance precedents
- pending risk acceptances
- proposed operational-monitoring contracts

Usage:
  python3 tools/tf_actions.py
  python3 tools/tf_actions.py --json
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("tf_actions.py requires PyYAML: pip install -r requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load(path: pathlib.Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_records(data_dir: pathlib.Path):
    instance = load(data_dir / "instance.yaml")
    records = {}
    for _, spec in (instance.get("namespaces") or {}).items():
        doc = load(data_dir / spec["file"]) if (data_dir / spec["file"]).exists() else {}
        recs = doc.get("records") or []
        records[spec["record_type"]] = recs
    return records


def _priority_for_normative(item):
    relevance = item.get("standards_relevance")
    return "high" if relevance == "High" else "medium" if relevance == "Medium" else "normal"


def load_manual_actions(data_dir: pathlib.Path):
    """Load non-derivable Task Force decisions.

    These are reserved for governance questions that do not already have a
    canonical record state. Never duplicate CT/GR/RP/GP/RA/M actions here.
    """
    path = data_dir / "task-force-actions.yaml"
    if not path.exists():
        return []
    doc = load(path)
    return doc.get("actions") or []


def derive_tf_actions(records, manual_actions=None):
    actions = []

    for kind in ("control", "guardrail"):
        source_file = "data/controls.yaml" if kind == "control" else "data/guardrails.yaml"
        for item in records.get(kind, []):
            if item.get("standards_status") not in (None, "unassigned"):
                continue
            sid = item["id"]
            actions.append({
                "action_key": f"TF-NORM-{sid}",
                "subject_id": sid,
                "category": "normative_triage",
                "priority": _priority_for_normative(item),
                "status": "waiting_on_tf",
                "current_state": "standards_status=unassigned",
                "requested_decision": (
                    "Assign canonical standards status, normative language where applicable, "
                    "target control plane, and rationale."
                ),
                "source": source_file,
                "title": item.get("name") or sid,
            })

    for item in records.get("rule_profile", []):
        if item.get("status") != "proposed":
            continue
        sid = item["id"]
        actions.append({
            "action_key": f"TF-{sid}",
            "subject_id": sid,
            "category": "rule_profile",
            "priority": "high",
            "status": "waiting_on_tf",
            "current_state": "status=proposed",
            "requested_decision": "Ratify, revise, defer, or reject the proposed governance rule profile.",
            "source": "data/rule-profiles.yaml",
            "title": item.get("name") or sid,
        })

    for item in records.get("governance_precedent", []):
        if item.get("status") != "proposed":
            continue
        sid = item["id"]
        actions.append({
            "action_key": f"TF-{sid}",
            "subject_id": sid,
            "category": "governance_precedent",
            "priority": "medium",
            "status": "waiting_on_tf",
            "current_state": "status=proposed",
            "requested_decision": "Ratify, revise, supersede, or reject this proposed governance precedent.",
            "source": "data/governance-precedents.yaml",
            "title": item.get("title") or sid,
        })

    for item in records.get("risk_acceptance", []):
        if item.get("decision") != "pending":
            continue
        sid = item["id"]
        actions.append({
            "action_key": f"TF-{sid}",
            "subject_id": sid,
            "category": "risk_acceptance",
            "priority": "high",
            "status": "waiting_on_tf",
            "current_state": "decision=pending",
            "requested_decision": (
                "Resolve the pending acceptance only after the applicable rule profile and "
                "authority model have been ratified."
            ),
            "blocked_by": ["TF-RP-001"] if any(
                p.get("id") == "RP-001" and p.get("status") == "proposed"
                for p in records.get("rule_profile", [])
            ) else [],
            "source": "data/risk-acceptances.yaml",
            "title": f"Risk acceptance for {item.get('risk_id', sid)}",
        })

    for item in records.get("metric", []):
        mon = item.get("monitoring")
        if not isinstance(mon, dict) or mon.get("status") != "pilot_proposed":
            continue
        sid = item["id"]
        actions.append({
            "action_key": f"TF-MON-{sid}",
            "subject_id": sid,
            "category": "monitoring_activation",
            "priority": "high",
            "status": "waiting_on_tf",
            "current_state": "monitoring.status=pilot_proposed",
            "requested_decision": (
                "Activate, revise, defer, or reject the proposed monitoring contract, "
                "including threshold/SLA/accountability assumptions."
            ),
            "source": "data/metrics.yaml",
            "title": item.get("name") or sid,
        })

    for item in manual_actions or []:
        if item.get("status") != "waiting_on_tf":
            continue
        actions.append({
            "action_key": item["action_key"],
            "subject_id": item.get("subject_id") or item["action_key"],
            "category": item.get("category", "governance_question"),
            "priority": item.get("priority", "medium"),
            "status": "waiting_on_tf",
            "current_state": item.get("current_state", "open"),
            "requested_decision": item["requested_decision"],
            "source": "data/task-force-actions.yaml",
            "title": item.get("title") or item["action_key"],
            "blocked_by": item.get("blocked_by") or [],
        })

    category_order = {
        "governance_question": 0,
        "rule_profile": 1,
        "risk_acceptance": 2,
        "monitoring_activation": 3,
        "governance_precedent": 4,
        "normative_triage": 5,
    }
    priority_order = {"high": 0, "medium": 1, "normal": 2}
    actions.sort(key=lambda a: (
        category_order.get(a["category"], 99),
        priority_order.get(a["priority"], 99),
        a["subject_id"],
    ))
    return actions


def summary(actions):
    by_category = {}
    by_priority = {}
    for action in actions:
        by_category[action["category"]] = by_category.get(action["category"], 0) + 1
        by_priority[action["priority"]] = by_priority.get(action["priority"], 0) + 1
    return {
        "waiting_on_tf": len(actions),
        "by_category": by_category,
        "by_priority": by_priority,
    }


def render_markdown(actions):
    s = summary(actions)
    lines = [
        "# Task Force Action Register",
        "",
        "> **Generated work queue. Do not edit this file by hand.**",
        "> The source of truth is the unresolved state on each canonical RAHP record.",
        "> Run `python3 tools/build.py` after a Task Force decision is recorded.",
        "",
        f"Open Task Force decisions: **{s['waiting_on_tf']}**.",
        "",
        "| Category | Open items |",
        "|---|---:|",
    ]
    labels = {
        "governance_question": "Open governance questions",
        "normative_triage": "Normative status / language",
        "rule_profile": "Rule profiles",
        "governance_precedent": "Governance precedents",
        "risk_acceptance": "Risk acceptances",
        "monitoring_activation": "Monitoring activation",
    }
    for key, count in sorted(s["by_category"].items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {labels.get(key, key)} | {count} |")

    lines += [
        "",
        "## Itemized decisions",
        "",
        "| Action | Subject | Priority | Current state | Decision required | Source |",
        "|---|---|---|---|---|---|",
    ]
    for a in actions:
        decision = a["requested_decision"].replace("|", "\\|")
        title = a["title"].replace("|", "\\|")
        state = a["current_state"].replace("|", "\\|")
        source = f"`{a['source']}`"
        blocked = ""
        if a.get("blocked_by"):
            blocked = f" Blocked by {', '.join(a['blocked_by'])}."
        lines.append(
            f"| `{a['action_key']}` | `{a['subject_id']}` — {title} | {a['priority']} | "
            f"{state} | {decision}{blocked} | {source} |"
        )
    lines += [
        "",
        "## Closure rule",
        "",
        "An item disappears from this register only when its canonical state is changed through",
        "an accountable Task Force decision. The register itself is never the decision record.",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "data"))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    data_dir = pathlib.Path(args.data)
    actions = derive_tf_actions(load_records(data_dir), load_manual_actions(data_dir))
    if args.json:
        print(json.dumps({"summary": summary(actions), "actions": actions}, indent=2))
    else:
        print(render_markdown(actions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
