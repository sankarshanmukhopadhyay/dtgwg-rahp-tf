# DTG Credential Specification pressure-test example

This directory contains a **substantive RAHP pressure test**, not an illustrative placeholder. It demonstrates how a standards review can be pinned to a precise target revision, mapped to the canonical RAHP corpus, routed to the correct control plane, and retained for later re-testing.

## Review target

| Field | Value |
|---|---|
| Specification | DTG Core Credential Specification |
| Repository | `trustoverip/dtgwg-cred-spec` |
| Version | Working Draft 01 |
| Reviewed commit | `d19f7c9cac364fab8e50cf434513ef53fef80e37` |
| Review date | 2026-08-12 |
| RAHP baseline | `v0.3-dev` corpus in this repository |
| Machine-readable record | [`pressure-test.yaml`](pressure-test.yaml) |

The commit is intentionally recorded in full. A rendered specification URL can move; a commit gives a later reviewer a stable answer to **what was actually pressure-tested**.

## Result at a glance

The review records **8 open findings**. They do not all belong in the credential specification. RAHP's control-plane discipline is used to separate schema/semantic defects from companion-protocol and governance obligations.

| Finding | Primary disposition | RAHP risks | Core issue |
|---|---|---|---|
| F-001 | Specification | RK-SC02 | Reverse VMC required for membership-edge completion is not constructible from WD-01 schema |
| F-002 | Specification | RK-AI01, RK-AI02, RK-G05 | Agent membership can be over-read as authority/capability/accountability |
| F-003 | Specification | RK-ID03, RK-CR01/02/03, RK-AI02 | Revocation/status/lifecycle semantics are not interoperable enough |
| F-004 | Specification | RK-SC04, RK-ID05 | M-DID bootstrap exception can become a permanent correlation path |
| F-005 | Companion specification | RK-CY01 | ZKP-by-default guidance lacks a proof interoperability profile |
| F-006 | Governance | RK-G05, RK-SC02 | Technical conformance is not sharply separated from governance legitimacy |
| F-007 | Companion specification | RK-HX05, RK-SC05 | Supported decision-making/LPA/guardianship is not representable |
| F-008 | Specification | RK-EX05 | Ordinary organisational entity semantics are not explicit |

## What the pressure test found

### 1. Membership-edge directionality is a real schema contradiction

WD-01 says that a complete membership edge consists of two VMCs, one in each direction, while its normative VMC schema only defines the community-issued direction. This is not merely editorial because different implementations can make different choices about consent and edge completeness. The open upstream PR `trustoverip/dtgwg-cred-spec#12` proposes a direction-qualified member acknowledgement and therefore becomes evidence attached to F-001, not a reason to mark the finding resolved.

### 2. Membership must not silently become authority

The specification explicitly allows an agent to be the subject of a VMC. RAHP therefore tests the harmful inference that a verifier may treat that VMC as evidence of the agent's mandate. The pressure-test record recommends a semantic boundary: membership can recognize an agent node, but operator identity, accountability, delegation, autonomy, capabilities and current authority remain separately verifiable facts.

### 3. Lifecycle semantics need a technical contract even when due process remains governance

The draft has validity periods and tells verifiers to check applicable revocation through a trust registry, but it does not define a mandatory status discovery/profile contract or consistent failure semantics. RAHP separates two questions: **how a verifier determines status** belongs in interoperable technical semantics; **whether revocation was legitimate and what consequence follows** remains a governance question.

### 4. Privacy-by-default requires bounding the bootstrap exception

R-DIDs are the privacy-preserving relationship identifier, but M-DIDs remain allowed for bootstrapping and post-bootstrap migration is only recommended. Without a defined end condition or migration state, the exception can become permanent and cross-relationship correlation can become normal implementation behavior.

### 5. ZKP guidance needs a companion interoperability profile

The credential spec is right to remain proof-format agnostic, but `SHOULD`-style ZKP-by-default expectations cannot become interoperable behavior without a profile covering proof constructions, predicates, freshness/replay, status checks and test vectors. F-005 therefore routes primarily to a companion specification rather than forcing a specific cryptographic suite into the core credential schema.

### 6. Conformance should distinguish cryptographic/schema validity from governance legitimacy

The specification correctly says a cryptographically valid credential is not necessarily an authorized one. The remaining gap is claim language: an implementation should not be able to collapse "valid DTG-shaped credential" into "governance-qualified DTG trust assertion." F-006 recommends explicit conformance levels or terminology.

### 7. Legal representation and supported consent need an assigned architecture

The current issuer/subject model does not represent supported decision-making, guardianship or power-of-attorney relationships. That does not mean all legal-capacity semantics belong in this credential specification. It does mean the gap should have an explicit companion-specification route and the core model should avoid implying that subject identity proves exclusive capacity or control.

### 8. Organisational entity semantics should be explicit

The VMC text names person, device and agent members, while C-DID represents communities. An ordinary organisation is therefore easy to model inconsistently. F-008 asks the specification either to define the organisational entity path or to state that it is intentionally outside this layer and name the required companion architecture.

## Reproducing the review

Run the repository integrity validator and the pressure-test validator:

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/validate_pressure_tests.py
```

The second command validates every `examples/**/pressure-test.yaml` against the canonical RAHP identifiers and the controlled finding-disposition vocabulary. It fails if a finding cites a risk/control/guardrail/assurance test that does not exist, if a target is not pinned to a commit, or if required review metadata is missing.

## Re-testing after the specification changes

Do **not** overwrite the reviewed commit and silently keep the old findings. Re-run the review against the new target revision, then update each finding as `resolved`, `open`, `superseded` or `monitoring`, preserving upstream issue/PR references as evidence. This turns the example into a longitudinal assurance record rather than a static critique.

## Interpretation boundary

This is a RAHP pressure test, not a claim that every listed control must become normative text in `dtgwg-cred-spec`. Each finding records a primary disposition and, where necessary, secondary control planes. That is intentional: the purpose of RAHP is to expose harm pathways **and** put remediation where legitimate authority and effective enforcement actually exist.
