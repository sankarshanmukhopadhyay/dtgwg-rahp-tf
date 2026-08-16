---
title: CAWG/C2PA assessment risk register
parent: Deployments & examples
nav_order: 7
---
# CAWG/C2PA assessment risk register

This register belongs to the **external CAWG/C2PA RAHP instance**. The `CRK-*` records are RAHP assessment vocabulary, not CAWG, DIF or C2PA normative terms. Keeping them under `instances/cawg/data/` prevents an external deployment from silently inheriting the DTG instance's `RK-*` catalogue.

| ID | Risk | Assessment meaning |
|---|---|---|
| <a id="crk-01"></a>`CRK-01` | Identity-validity and authority conflation | A relying party treats successful identity or credential validation as proof that the actor is authoritative for the role, claim, right, or decision at issue. |
| <a id="crk-02"></a>`CRK-02` | Historical verification continuity loss | Later revocation, issuer/key rotation, registry loss, or policy change makes it impossible to determine whether evidence was valid at the time an action occurred. |
| <a id="crk-03"></a>`CRK-03` | Integrity and factual truth conflation | Tamper-evident or authenticated metadata is interpreted as factually correct or authoritative merely because its integrity can be verified. |
| <a id="crk-04"></a>`CRK-04` | Conflicting authoritative assertions | Multiple valid actors, namespaces, registries, or assertions provide incompatible claims and relying parties lack deterministic conflict handling. |
| <a id="crk-05"></a>`CRK-05` | Rights signal and legal-effect ambiguity | A machine-readable permission or prohibition signal is treated either as universally enforceable authorization or as legally irrelevant without a deployment-specific rights/governance interpretation. |
| <a id="crk-06"></a>`CRK-06` | Permission precedence and lifecycle conflict | Embedded, external, older, newer, withdrawn, or superseding permission signals disagree and consumers choose inconsistent effective states. |
| <a id="crk-07"></a>`CRK-07` | Consent authority and representation ambiguity | A consent assertion is accepted from an actor whose rights, legal capacity, representative authority, or relationship to other affected parties has not been established. |
| <a id="crk-08"></a>`CRK-08` | Endorsement or delegation scope creep | Approval for bounded actions is interpreted as broader, transitive, onward-delegable, or indefinite authority. |
| <a id="crk-09"></a>`CRK-09` | Stale delegated or organizational authority | An endorsement, role, credential, or organizational signing relationship remains apparently valid after employment, role, key-control, or mandate changes. |
| <a id="crk-10"></a>`CRK-10` | Trust-anchor concentration and participation exclusion | A mandate makes a narrow set of credential issuers, certificate roots, or trust registries effective gatekeepers for participation without adequate alternatives, appeal, or portability. |
| <a id="crk-11"></a>`CRK-11` | Verification UX overclaim | Human-facing presentation causes users to infer truth, safety, legitimacy, or endorsement from a narrower cryptographic, provenance, or identity verification result. |
| <a id="crk-12"></a>`CRK-12` | Required-evidence downgrade ambiguity | A relying party accepts content after expected higher-layer assertions are absent, removed, unsupported, or unavailable because policy cannot distinguish missing evidence from acceptable evidence. |
| <a id="crk-13"></a>`CRK-13` | Accessibility and failure-state exclusion | Mandatory provenance/identity interfaces or ambiguous unknown/error states prevent people using assistive technology or constrained contexts from understanding or exercising equivalent choices. |
| <a id="crk-14"></a>`CRK-14` | Trust-registry identity binding failure | A trust-registry entity identifier is incorrectly bound, ambiguously rebound, or insufficiently linked to the credential subject used by a relying party. |
| <a id="crk-15"></a>`CRK-15` | Registry and governing-authority availability dependency | A relying party cannot complete authorization because a trust registry, governing-authority endpoint, or registry-of-registries is unavailable or operationally degraded. |
| <a id="crk-16"></a>`CRK-16` | Trust-framework policy drift | A credential or assertion remains cryptographically valid while the governance framework, membership criteria, assurance rules, or relying-party policy that gave it meaning changes. |
| <a id="crk-17"></a>`CRK-17` | Credential restatement and transitive trust amplification | A restating issuer or intermediary transforms upstream credentials into a stronger or broader downstream trust signal than the original evidence supports. |
| <a id="crk-18"></a>`CRK-18` | Holder and custodian authority ambiguity | A custodian, wallet, claims aggregator, or service can exercise signing capability without sufficiently proving that the named actor authorized the specific content-binding act. |
| <a id="crk-19"></a>`CRK-19` | Selective-disclosure correlation leakage | Credential presentation or repeated stable identifiers enable cross-context correlation, deanonymization, or linkage beyond the holder’s intended disclosure. |
| <a id="crk-20"></a>`CRK-20` | Alternative trust-method inconsistency | Different signature, DID, PKI, DNSSEC, KERI, or credential mechanisms produce materially different security and lifecycle guarantees while appearing equivalent to consumers. |
| <a id="crk-21"></a>`CRK-21` | Timestamp or status evidence insufficiency | A timestamp, status token, or archival bundle fails to establish the historical validity state needed for durable verification. |
| <a id="crk-22"></a>`CRK-22` | Unsafe external-resource resolution | A validator follows attacker-controlled or insufficiently constrained URIs, redirects, schemas, logos, status endpoints, or registry references during verification. |
| <a id="crk-23"></a>`CRK-23` | Assertion stripping and downgrade | An intermediary removes an optional higher-layer assertion and a downstream verifier cannot distinguish intentional absence from unsupported or stripped evidence. |
| <a id="crk-24"></a>`CRK-24` | Autonomous-agent attribution ambiguity | A software or AI actor is presented as creator, signer, delegate, or named actor without a clear boundary between machine operation and human or organizational accountability. |
| <a id="crk-25"></a>`CRK-25` | Onward delegation and sub-agent escalation | Delegated authority is passed to another actor or agent without an explicit, bounded, verifiable right to sub-delegate. |
| <a id="crk-26"></a>`CRK-26` | Assurance-level miscomparison | Relying parties compare or map identity assurance levels from different schemes as if they were directly equivalent or sufficient for the same decision. |
| <a id="crk-27"></a>`CRK-27` | Rights-holder and affected-party conflict | Creator, rights holder, subject, performer, employer, licensee, or other affected parties have conflicting authority or consent states and the system lacks deterministic resolution. |
| <a id="crk-28"></a>`CRK-28` | Implementation/specification semantic collapse | SDKs, validators, products, or UX collapse distinct specification states such as signature-valid, identity-valid, authorized, current, truthful, or trusted into a single result. |

The worked reviews at [`examples/cawg-c2pa/`](../examples/cawg-c2pa/README.md) provide the evidence, harm path, treatment and retest trigger for each use of these risks.
