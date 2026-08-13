#!/usr/bin/env python3
"""Validate v0.4 portable method additions."""
from pathlib import Path
import json, sys, yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parent.parent
errors=[]

tax=yaml.safe_load((ROOT/"method/non-human-actors.yaml").read_text())
classes=tax.get("classes") or []
ids=[x.get("id") for x in classes]
if len(ids)!=len(set(ids)) or not all(ids):
    errors.append("non-human actor taxonomy has missing/duplicate IDs")
required={"NHA-AUTONOMOUS","NHA-SUPERVISED","NHA-PIPELINE"}
if set(ids)!=required:
    errors.append(f"non-human actor taxonomy must define exactly {sorted(required)}")

schema=json.loads((ROOT/"method/schema/delegation-scope.schema.json").read_text())
example=yaml.safe_load((ROOT/"examples/agent-delegation-scope.yaml").read_text())
validator=Draft202012Validator(schema, format_checker=FormatChecker())
for e in validator.iter_errors(example):
    errors.append("delegation example: "+e.message)
if example.get("actor_class") not in set(ids):
    errors.append("delegation example actor_class does not resolve in taxonomy")

if errors:
    for e in errors: print("ERROR",e)
    print(f"v0.4 method validation failed: {len(errors)} error(s).")
    raise SystemExit(1)
print(f"v0.4 method validation clean: {len(classes)} non-human actor classes; delegation example conforms.")
