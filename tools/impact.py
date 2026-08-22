#!/usr/bin/env python3
"""Portable RAHP assurance-graph impact analysis."""
from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path
from typing import Any

import yaml


def load_document(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    value = json.loads(text) if path.suffix.lower() == ".json" else yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError(f"expected object: {path}")
    return value


def adjacency(graph: dict[str, Any]) -> dict[str, list[tuple[str, str]]]:
    out: dict[str, list[tuple[str, str]]] = {}
    for edge in graph.get("edges") or []:
        source = edge["source"]
        target = edge["target"]
        edge_id = edge.get("id") or f"{source}->{target}"
        mode = edge["impact_propagation"]
        if mode in {"source-to-target", "both"}:
            out.setdefault(source, []).append((target, edge_id))
        if mode in {"target-to-source", "both"}:
            out.setdefault(target, []).append((source, edge_id))
    return out


def analyze(graph: dict[str, Any], changed_nodes: list[str]) -> dict[str, Any]:
    nodes = {item["id"]: item for item in graph.get("nodes") or []}
    links = adjacency(graph)
    unresolved = sorted({node for node in changed_nodes if node not in nodes})
    resolved = sorted({node for node in changed_nodes if node in nodes})

    distance: dict[str, int] = {}
    path: dict[str, list[str]] = {}
    queue: deque[str] = deque()
    for node in resolved:
        distance[node] = 0
        path[node] = []
        queue.append(node)

    while queue:
        current = queue.popleft()
        for nxt, edge_id in links.get(current, []):
            candidate = distance[current] + 1
            if nxt not in distance or candidate < distance[nxt]:
                distance[nxt] = candidate
                path[nxt] = [*path[current], edge_id]
                queue.append(nxt)

    affected = []
    assessments: list[str] = []
    for node_id in sorted(distance, key=lambda item: (distance[item], item)):
        node = nodes[node_id]
        affected.append({
            "id": node_id,
            "type": node["type"],
            "distance": distance[node_id],
            "via": path[node_id],
        })
        if node["type"] == "assessment":
            assessments.append(node.get("assessment_id") or node_id)

    assessments = sorted(set(assessments))
    return {
        "version": 1,
        "graph_id": graph["graph_id"],
        "changed_nodes": sorted(set(changed_nodes)),
        "affected_nodes": affected,
        "affected_assessments": assessments,
        "retest_required": assessments,
        "unresolved_changed_nodes": unresolved,
        "notes": [
            "Impact is graph-reachability evidence, not an assurance conclusion.",
            "Retest-required identifies candidate assessments; disposition remains governed."
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="RAHP portable assurance graph impact analysis")
    parser.add_argument("--graph", type=Path, required=True)
    parser.add_argument("--changed-node", action="append", dest="changed_nodes", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = analyze(load_document(args.graph), args.changed_nodes)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"graph: {result['graph_id']}")
        print(f"affected assessments: {len(result['affected_assessments'])}")
        for assessment in result["affected_assessments"]:
            print(f"  retest-required: {assessment}")
        if result["unresolved_changed_nodes"]:
            for node in result["unresolved_changed_nodes"]:
                print(f"  unresolved changed node: {node}")
    return 0 if not result["unresolved_changed_nodes"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
