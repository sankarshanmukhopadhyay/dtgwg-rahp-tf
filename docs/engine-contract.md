---
layout: default
title: "Engine contract"
nav_order: 1
has_toc: true
parent: Implement RAHP
---
# RAHP engine contract

v0.8 makes the execution boundary explicit so RAHP can support more than one
implementation language without making Python behaviour normative.

The portable contract is defined by:

- `method/engine-contract.yaml` — lifecycle, operations and invariants;
- `method/schema/rahp-result.schema.json` — normalized assessment result;
- `method/evidence-retention.yaml` — evidence/storage classes;
- `tests/conformance/engine/` — implementation-neutral fixtures.

The execution lifecycle is:

```text
source → observation → trigger → assessment → finding → disposition → baseline
```

An implementation may use Python, TypeScript, Rust, Java, Go or another language. A
conforming implementation must preserve these object boundaries and produce results
that validate against the common schema and fixtures.

## What is normative and what is not

The portable schemas, controlled method data, lifecycle invariants and conformance
fixtures define the contract. The current Python commands are a **reference adapter**
and operational implementation; their internal functions, filesystem layout and
libraries are not an API that another implementation must reproduce.

This distinction is deliberate. It enables a TypeScript SDK to arrive without
redefining RAHP, and later permits a Rust/WASM implementation to prove portability by
running the same conformance suite.

## Reference commands

```bash
python3 tools/engine_contract.py describe
python3 tools/engine_contract.py validate-result result.json
python3 tools/engine_contract.py retention-plan result.json
```

CI runs `tools/validate_engine_contract.py` to verify the contract, retention policy
and conformance fixtures together.

## Normalized result

A result records:

- stable assessment identity and triggers;
- repository/source and reviewed revision;
- review mode and lifecycle status;
- findings;
- disposition;
- evidence manifest entries; and
- observable retest triggers.

The normalized result is intentionally smaller than a run workspace. It is the
portable interchange object between an engine, CI, a future TypeScript SDK, reporting
systems and durable deployment assurance state.
