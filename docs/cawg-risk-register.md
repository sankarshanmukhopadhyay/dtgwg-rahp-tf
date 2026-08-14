---
title: CAWG/C2PA assessment risk register
nav_order: 71
---
# CAWG/C2PA assessment risk register

This register belongs to the **external CAWG/C2PA RAHP instance**. The `CRK-*` records are assessment
vocabulary, not CAWG, DIF or C2PA normative terms. Keeping them under `instances/cawg/data/` prevents
an external deployment from silently inheriting the DTG instance's `RK-*` catalogue.

| ID | Risk | Assessment meaning |
|---|---|---|
| <a id="crk-01"></a>`CRK-01` | Identity-validity and authority conflation | Valid identity/credential evidence is over-read as authority for a role, right, claim or decision. |
| <a id="crk-02"></a>`CRK-02` | Historical verification continuity loss | Later lifecycle or infrastructure change prevents reliable as-of verification. |
| <a id="crk-03"></a>`CRK-03` | Integrity and factual truth conflation | Tamper evidence is mistaken for factual correctness or authority. |
| <a id="crk-04"></a>`CRK-04` | Conflicting authoritative assertions | Multiple valid claims disagree without deterministic conflict handling. |
| <a id="crk-05"></a>`CRK-05` | Rights signal and legal-effect ambiguity | Machine-readable use signals are over- or under-interpreted as legal authorization. |
| <a id="crk-06"></a>`CRK-06` | Permission precedence and lifecycle conflict | Embedded/external or old/new permission states disagree. |
| <a id="crk-07"></a>`CRK-07` | Consent authority and representation ambiguity | Consent is accepted without establishing rights, capacity or representative authority. |
| <a id="crk-08"></a>`CRK-08` | Endorsement or delegation scope creep | Bounded approval becomes broader, transitive or indefinite authority. |
| <a id="crk-09"></a>`CRK-09` | Stale delegated or organizational authority | Role/credential/mandate changes do not terminate apparent authority consistently. |
| <a id="crk-10"></a>`CRK-10` | Trust-anchor concentration and participation exclusion | Mandates turn a narrow issuer/root/registry set into gatekeepers without adequate alternatives or appeal. |
| <a id="crk-11"></a>`CRK-11` | Verification UX overclaim | UI causes users to infer truth, legitimacy or safety from narrower verification results. |
| <a id="crk-12"></a>`CRK-12` | Required-evidence downgrade ambiguity | Missing or stripped higher-layer evidence is accepted because policy cannot identify what was required. |
| <a id="crk-13"></a>`CRK-13` | Accessibility and failure-state exclusion | Mandatory UX or ambiguous error/unknown states deny equivalent understanding or choice. |

The worked reviews at [`examples/cawg-c2pa/`](../examples/cawg-c2pa/README.md) provide the evidence,
harm path, treatment and retest trigger for each use of these risks.
