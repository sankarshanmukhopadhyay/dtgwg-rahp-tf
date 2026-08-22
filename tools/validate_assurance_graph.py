#!/usr/bin/env python3
"""Validate the portable assurance graph and deterministic impact analysis."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator

from impact import analyze

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "method" / "schema"
FIXTURE_DIR = ROOT / "examples" / "assurance-lineage"
GRAPH_FIXTURE = FIXTURE_DIR / "generic-assurance-graph.yaml"
EXPECTED_RESULT = FIXTURE_DIR / "generic-impact-result.json"


def validate_schema(document, schema_name: str) -> list[str]:
    schema = json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = []
    for err in sorted(validator.iter_errors(document), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in err.absolute_path) or "(record)"
        errors.append(f"{location}: {err.message}")
    return errors


def main() -> int:
    graph = yaml.safe_load(GRAPH_FIXTURE.read_text(encoding="utf-8"))
    expected = json.loads(EXPECTED_RESULT.read_text(encoding="utf-8"))
    errors = validate_schema(graph, "assurance-graph.schema.json")
    errors.extend(validate_schema(expected, "impact-analysis.schema.json"))

    node_ids = [node["id"] for node in graph.get("nodes") or []]
    if len(node_ids) != len(set(node_ids)):
        errors.append("graph contains duplicate node identifiers")
    known = set(node_ids)
    edge_ids = []
    for edge in graph.get("edges") or []:
        if edge.get("id"):
            edge_ids.append(edge["id"])
        if edge["source"] not in known:
            errors.append(f"edge source does not resolve: {edge['source']}")
        if edge["target"] not in known:
            errors.append(f"edge target does not resolve: {edge['target']}")
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("graph contains duplicate edge identifiers")

    result = analyze(graph, ["target:payments-api"])
    errors.extend(validate_schema(result, "impact-analysis.schema.json"))
    if result != expected:
        errors.append("target-change impact output differs from committed conformance fixture")

    expected_assessment = "example:specification:payments-api"
    if expected_assessment not in result["affected_assessments"]:
        errors.append("target change did not propagate to the expected assessment")
    if expected_assessment not in result["retest_required"]:
        errors.append("affected assessment was not selected for retest")

    isolated = analyze(graph, ["missing:node"])
    if isolated["affected_nodes"]:
        errors.append("unknown changed node unexpectedly produced affected nodes")
    if isolated["unresolved_changed_nodes"] != ["missing:node"]:
        errors.append("unknown changed node was not reported deterministically")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Portable assurance graph validation passed: schema, references and deterministic impact conformance satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
