---
layout: default
title: "Adoption"
nav_order: 20
has_toc: true
---
# Adopting RAHP

RAHP can be adopted incrementally. You do **not** need to populate the entire model before it produces useful assurance evidence.

## Step 1 — Establish context

Identify the target specification or system, expected participants, decision points, trust assumptions, power asymmetries, known governance constraints, and the authority able to act on findings.

## Step 2 — Reuse before inventing

Search existing personas, scenarios, risks and controls before creating records. Reuse preserves comparability and prevents the corpus from fragmenting into near-duplicates.

## Step 3 — Pressure-test

Ask what can go wrong, who is harmed, what harmful inference an implementation can make, what remains cryptographically valid but governance-invalid, and what assumptions fail under adversarial or exceptional conditions.

## Step 4 — Determine the correct control layer

A valid risk is not automatically a requirement for the core specification. Route remediation to the narrowest layer with legitimate authority and effective enforcement: specification, companion specification, governance, implementation guidance, runtime control, operational policy, or formal risk acceptance.

## Step 5 — Publish actionable findings

Each finding should capture the finding and harm, affected persona, relevant RAHP risks, linked controls/guardrails, proposed resolution, disposition, status, target version/commit, and evidence or issue/PR reference.

## Minimum viable assessment

A practical first pass can be limited to:

```text
1 specification scope
3–6 relevant personas
5–15 risk hypotheses
controls only where necessary
guardrails only for hard-stop conditions
recommendations as the primary output
```

See `examples/minimal-instance/` for a compact pattern and `examples/dtg-credential-spec/` for a worked specification-review structure.

## Forking for another Working Group

Keep `method/`, `tools/`, `context/`, and the documentation scaffolding. Replace the contents of `data/` with a new `instance.yaml` and records for the target domain. Preserve identifiers once published, record provenance, and run the validator as a conformance gate.


## v0.5 portability contract

RAHP now distinguishes **target-repository portability** from **independent-instance
portability**. The engine already operates across multiple configured repositories.
An independent adopter must go further: it owns its own `data/` root, governance
profile, personas, risks, controls and evidence decisions.

A synthetic portability fixture lives under `examples/portable-instance/` and is
validated in CI:

```bash
python3 tools/validate_portability.py
```

The fixture proves that the validator can operate against a separate instance without
coupling to DTG data or the root DTG README. It is not evidence of external adoption.

For assessment reporting, use `method/conformance-claim-template.yaml` to state that
a target was **assessed using RAHP** without implying that the target conforms to
DTG-specific instance content.
