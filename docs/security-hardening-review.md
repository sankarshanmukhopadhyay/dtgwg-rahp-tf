# Security and hardening review workflow

RAHP pressure testing asks whether a specification leaves people, governance or system integrity exposed to harm. A **security and hardening review** is a narrower adversarial companion: it asks how an attacker, compromised participant, stale authority, ambiguous verifier or failing dependency could exploit the specification as written.

The two review types should be read together. A pressure-test finding may be a policy or inclusion gap with no practical exploit path; a security-hardening finding must describe a concrete failure mode, the preconditions under which it becomes reachable, the security property affected, the existing mitigations, and the narrowest control plane that should close the gap.

## Review unit

Every review is pinned to a full upstream commit. Each finding records:

- an attack surface and preconditions;
- a credible exploit or failure path;
- the security property affected;
- existing mitigations already present in the target;
- the residual gap;
- severity plus exploitability, impact, detectability and propagation;
- a primary control plane (`SPEC`, `PROFILE`, `GOV`, `IMPL`, `OPS`, or `TEST`);
- a recommended hardening action and verification condition; and
- links back to canonical RAHP risks, controls, guardrails and assurance tests where applicable; and
- structured external standards alignment where an authoritative or widely used security source materially reinforces the finding.

## Severity dimensions

| Dimension | Question |
|---|---|
| Severity | What is the worst credible consequence? |
| Exploitability | How difficult is it to reach the failure mode? |
| Impact | What happens if exploitation succeeds? |
| Detectability | How likely is normal monitoring or verification to notice? |
| Propagation | Does compromise remain local, cross parties, contaminate a community, or become systemic? |

These dimensions are deliberately not collapsed into a single numeric score. A difficult-to-exploit flaw with systemic propagation may deserve more standards attention than an easy but contained failure.

## Control planes

| Code | Destination | Use when |
|---|---|---|
| `SPEC` | Core specification | Interoperability or safety requires every conforming implementation to behave consistently. |
| `PROFILE` | Companion profile/specification | The core architecture is correctly generic, but a security, delegation, proof, status or deployment profile must make a narrower choice. |
| `GOV` | Governance | Legitimacy, authorization, due process or human approval depends on governing policy rather than wire syntax. |
| `IMPL` | Implementation hardening | Safe limits, constant-time handling, secure storage, key management or equivalent implementation practice is required. |
| `OPS` | Operational control | Availability, monitoring, registry operations, caching, incident response or key/status operations are the primary mitigation. |
| `TEST` | Conformance/adversarial test | The normative rule exists but should be converted into executable negative/abuse-case evidence. |

A finding gets one primary control plane. Secondary work may span several layers, but the primary destination keeps issue filing actionable.

## Workflow

1. Pin the target commit and enumerate trust boundaries.
2. Record safeguards that already exist before looking for gaps.
3. Attack authentication, authorization, freshness, replay, integrity, confidentiality, privacy, availability, evidence and recovery separately.
4. For protocol families, inspect composition boundaries, not only individual messages or credentials.
5. Prefer an existing RAHP risk/control mapping. Do not create a new canonical RAHP artefact merely because a security review uses different terminology.
6. Write a finding only when the exploit/failure path can be stated and the residual gap survives the target's existing mitigations.
7. Route the recommendation to the narrowest effective control plane.
8. Define a verification condition so a later review can close the finding objectively.

## Canonical and rendered records

`findings.yaml` is canonical. `tools/render_security_reviews.py` renders the human-readable review beside it. `tools/validate_security_reviews.py` validates structure, controlled vocabularies, commit pinning, RAHP references and generated Markdown freshness.


## External standards alignment

Security findings may be cross-referenced to authoritative standards and widely used security guidance. The canonical source registry is [`data/external-standards.yaml`](../data/external-standards.yaml). The initial corpus deliberately stays small and high-confidence: NIST CSF 2.0, NIST SP 800-53 Rev. 5, the current SP 800-63 Revision 4 family, NIST SP 800-207/207A, W3C Verifiable Credentials Data Model 2.0, W3C Verifiable Credential Data Integrity 1.0, W3C Bitstring Status List 1.0, OWASP API Security Top 10 2023, and OWASP Agentic AI threat guidance.

An external mapping is **not** an assertion that the cited organization reviewed, endorsed, or intended its material to govern DTG. Every mapping therefore declares one relationship:

| Relationship | Meaning |
|---|---|
| `direct` | The external source explicitly addresses substantially the same requirement or mechanism. |
| `supports` | The source provides a control, principle, or assurance objective supporting the proposed hardening. |
| `analogous` | The source describes a closely analogous attack/control class but was written for a different technical context. |
| `contextual` | The source provides relevant background but is not independent evidence for the finding. |

A mapping must include a short rationale. Prefer a clause, control identifier, or named section where one can be cited defensibly. Do not force a cross-reference merely to increase standards coverage, and do not convert informative OWASP guidance into a purported normative requirement.

The rendered security reviews expose these mappings as hyperlinks so specification authors can move directly from a RAHP finding to the relevant external source.
