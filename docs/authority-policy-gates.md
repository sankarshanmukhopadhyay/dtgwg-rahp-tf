---
layout: default
title: "Authority and policy gates"
nav_order: 11
has_toc: true
parent: Operate assurance
---
# Executable authority and policy gates

RAHP v1.5 development treats authority as explicit machine-readable governance input. Repository permissions, successful automation, detector output and policy evaluation are not substitutes for delegated authority.

The portable authority contract is `method/schema/authority.schema.json`. It identifies an issuer, subject, lifecycle status, validity window and one or more grants. Each grant binds an action to a scope. Portable actions are `observe`, `assess`, `disposition`, `remediate`, `publish`, `accept-risk`, `close` and `reopen`.

## Authority is scoped and revocable

An authority decision is valid only when the declared subject, action, scope and lifecycle state match. Suspended, revoked or expired authority cannot authorize a transition. A grant for one assessment does not silently become authority over another assessment, portfolio or remediation.

```bash
python3 tools/authority.py \
  --authority examples/assurance-lineage/generic-authority.yaml \
  --subject example:assurance-operator \
  --action publish \
  --scope-kind assessment \
  --scope-id example:specification:payments-api \
  --at 2026-08-22T00:00:00Z \
  --json
```

The evaluator reports `AUTHORIZED` or `DENIED` with reasons and matched grants. It does not create a delegation, modify upstream governance state or infer authority from GitHub access.

## Policy gates

The portable policy contract is `method/schema/gate-policy.schema.json`. A policy contains `require` and `deny` rules evaluated against a machine-readable context. Conditions support explicit paths and the operators `equals`, `not-equals`, `in`, `not-in`, `exists` and `not-exists`.

```bash
python3 tools/policy_gate.py \
  --policy examples/assurance-lineage/generic-release-gate.yaml \
  --context examples/assurance-lineage/generic-release-context-pass.yaml \
  --json
```

Gate outcomes are deliberately three-valued:

- `PASS` — all required rules are satisfied and no deny rule is triggered;
- `FAIL` — a required rule is false or a deny rule is triggered;
- `INDETERMINATE` — required inputs are absent or cannot be evaluated without inventing evidence.

A definite failure dominates an unrelated indeterminate condition. Otherwise missing required evidence is preserved as `INDETERMINATE`, never converted into `PASS`.

## Separation between gate result and governance authority

A policy can declare an `authority_required` action and scope. This means the policy expects an independent authority decision before the governed action is legitimate. The gate engine does not satisfy that requirement merely by returning `PASS`.

For example, a release policy can require current assurance, zero critical residual findings, verified evidence integrity and separately established publication authority. Passing those tests does not confer `accept-risk` or `close` authority.

This preserves the v1.5 lifecycle distinction:

```text
assurance evidence
    → policy evaluation
    → PASS | FAIL | INDETERMINATE
    → independent authority check
    → governed action, if authorized
```

## Portability

Authority subjects and scopes are opaque identifiers. The portable contract does not assume DTG, OpenVTC, ARPA, CAWG/C2PA, GitHub teams, repository maintainers or any particular standards body. A deployment may define stronger role, quorum, signature or delegation requirements without changing the core contract.

## Documentation synchronization

The v1.5 capability registry at `method/capability-documentation.yaml` binds each implemented capability to its schemas/tools/tests and primary documentation. `tools/validate_capability_documentation.py` checks those mappings in CI, including semantic terms that must remain present in the documentation.

This is an assurance guard, not an assertion that documentation can never contain errors. It makes drift detectable when a capability is added, renamed or loses its required documentation surface.
