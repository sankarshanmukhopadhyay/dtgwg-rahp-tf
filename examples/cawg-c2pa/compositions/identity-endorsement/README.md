# Identity × Endorsement / Delegation composition pressure test

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-COMP-004` |
| Status | complete |
| Title | Identity × Endorsement / Delegation composition pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-endorsement-assertion` |
| Target document | https://cawg.io/endorsement/1.0-draft/ |
| Target version | 1.0 draft |
| Target commit | `585c7fbe4ea49d89442ba1a8c04ab39927dbb47d` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.7.0` |
| RAHP corpus date | 2026-08-14 |

### Method

| Field | Value |
|---|---|
| Workflow | `docs/pressure-testing-a-spec.md` |
| Rule | Separate cryptographic validity, identity, authority, consent, lifecycle and relying-party trust; test both isolated and composed failure states. |

### Review scope

**Included**

- Normative and draft semantics relevant to the named composition or experiment.
- Cross-specification failure states that can remain hidden when each component is reviewed independently.

**Excluded**

- Legal opinion on enforceability in a particular jurisdiction.
- Claims that upstream CAWG, DIF, C2PA, GLEIF or W3C endorsed this RAHP assessment.

### Summary

| Measure | Value |
|---|---:|
| Findings | 2 |
| Open findings | 2 |
| Primary disposition: Governance | 1 |
| Primary disposition: Specification | 1 |

**Overall assessment**

Cross-specification RAHP review: individually valid components are tested for unsafe composed conclusions and downgrade behaviour.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Identity does not prove right to delegate | High | open | Governance | [CRK-08 — Endorsement or delegation scope creep](/rahp-toolkit/docs/cawg-risk-register.html#crk-08) |
| `F-002` | Onward agent delegation needs an explicit non-transitivity default | High | open | Specification | [CRK-25 — Onward delegation and sub-agent escalation](/rahp-toolkit/docs/cawg-risk-register.html#crk-25) |

### Detailed findings

#### F-001 — Identity does not prove right to delegate

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | `CAWG-019`, `CAWG-020`, `CAWG-021` |
| Scenario patterns | `SP-GOV-01`, `SP-AGENT-01` |
| Personas | — |
| Risks | [CRK-08 — Endorsement or delegation scope creep](/rahp-toolkit/docs/cawg-risk-register.html#crk-08) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-endorsement-assertion/issues/12` | The endorsement issue explicitly raises authority to assert and delegation of that authority. |

**Potential harm**

A verified actor can issue an endorsement beyond their underlying authority.

**Recommended treatment**

Require delegation provenance and authority-to-delegate checks that are independent of identity validation.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Onward agent delegation needs an explicit non-transitivity default

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Specification |
| Secondary dispositions | — |
| Scenarios | `CAWG-022`, `CAWG-023` |
| Scenario patterns | `SP-AGENT-02`, `SP-COMP-01` |
| Personas | — |
| Risks | [CRK-25 — Onward delegation and sub-agent escalation](/rahp-toolkit/docs/cawg-risk-register.html#crk-25) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/236` | CAWG is considering delegation for people, organizations and AI agents, but transitivity is a distinct authorization question. |

**Potential harm**

An endorsed service or agent can pass authority to a sub-agent beyond the principal’s intent.

**Recommended treatment**

Make sub-delegation prohibited by default unless explicitly authorized with bounded scope, audience, actions and expiry.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

