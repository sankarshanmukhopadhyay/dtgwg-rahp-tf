# Identity × Governance/TRQP composition pressure test

> **v0.8 revalidation:** this curated review has been mechanically revalidated against `rahp-engine-contract-v1` and the current RAHP catalogues on 2026-08-16. The target commit and original substantive review date remain unchanged; this does not claim a new upstream-target reassessment.

This is a RAHP Toolkit v0.7.0 external assurance review. It is not an upstream conformance or governance decision.

<!-- BEGIN GENERATED PRESSURE TEST -->

## Generated pressure-test record

> This section is generated from [`pressure-test.yaml`](pressure-test.yaml). Do not edit it by hand. The YAML is the canonical review record; run `python3 tools/render_pressure_tests.py` after changing it.

### Review metadata

| Field | Value |
|---|---|
| Review ID | `CAWG-COMP-001` |
| Status | complete |
| Title | Identity × Governance/TRQP composition pressure test |
| Reviewed on | 2026-08-14 |
| Target repository | `decentralized-identity/cawg-identity-assertion` |
| Target document | https://cawg.io/identity/1.3-draft+governance/ |
| Target version | 1.3 governance experiment |
| Target commit | `5f1908d4f5bf6c89d02d671ae5051f893df92dc9` |
| Target source paths | — |
| RAHP repository | `sankarshanmukhopadhyay/rahp-toolkit` |
| RAHP version | `v0.8.0` |
| Engine contract | `rahp-engine-contract-v1` |
| RAHP corpus date | 2026-08-16 |
| Engine/method revalidated on | 2026-08-16 |
| Original RAHP version | `v0.7.0` |
| Revalidation scope | method-and-engine-only; target revision and substantive findings unchanged |

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
| Primary disposition: Implementation Guidance | 1 |

**Overall assessment**

Cross-specification RAHP review: individually valid components are tested for unsafe composed conclusions and downgrade behaviour.

### Finding index

| ID | Finding | Severity | Status | Primary disposition | RAHP risks |
|---|---|---|---|---|---|
| `F-001` | Identity-valid plus registry-authorized can still be wrong at time T | High | open | Governance | [CRK-16 — Trust-framework policy drift](/rahp-toolkit/docs/cawg-risk-register.html#crk-16) |
| `F-002` | Registry outage must not silently downgrade to identity-only trust | High | open | Implementation Guidance | [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |

### Detailed findings

#### F-001 — Identity-valid plus registry-authorized can still be wrong at time T

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Governance |
| Secondary dispositions | — |
| Scenarios | `CAWG-003`, `CAWG-011` |
| Scenario patterns | `SP-GOV-02`, `SP-COMP-01` |
| Personas | [P1 — Principal / Rights-Bearing Party](../../../../build/site/catalogue.html#P1), [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../../build/site/catalogue.html#P6) |
| Risks | [CRK-16 — Trust-framework policy drift](/rahp-toolkit/docs/cawg-risk-register.html#crk-16) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/274` | TRQP introduces current authorization over an identity whose credential lifecycle is independently validated. |

**Potential harm**

Policy drift can turn the same tuple into a different authorization outcome over time.

**Recommended treatment**

Bind authorization decisions to policy/version/time evidence and test historical replay.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

#### F-002 — Registry outage must not silently downgrade to identity-only trust

| Field | Value |
|---|---|
| Severity | High |
| Status | open |
| Primary disposition | Implementation Guidance |
| Secondary dispositions | — |
| Scenarios | `CAWG-009` |
| Scenario patterns | `SP-OPS-01`, `SP-COMP-01` |
| Personas | [P3 — Relying Party / Verifier](../../../../build/site/catalogue.html#P3), [P6 — Registry / Discovery / Trust-Service Operator](../../../../build/site/catalogue.html#P6) |
| Risks | [CRK-15 — Registry and governing-authority availability dependency](/rahp-toolkit/docs/cawg-risk-register.html#crk-15) |
| Controls | — |
| Guardrails | — |
| Assurance tests | — |

**Evidence**

| Source | Observation |
|---|---|
| `https://github.com/decentralized-identity/cawg-identity-assertion/issues/275` | TRQP adds a network-resolved authority decision after identity verification. |

**Potential harm**

A validator may accept identity while dropping the higher-layer authorization check during degraded operation.

**Recommended treatment**

Define fail-closed/fail-indeterminate profiles and expose authorization-unavailable separately from identity-valid.

**Retest when**

- Normative semantics and interoperable test vectors close this failure path.

<!-- END GENERATED PRESSURE TEST -->

