---
title: "DTG review: Verifiable Trust Infrastructure August 2026 change window"
parent: DTG RAHP review record
nav_order: 20
layout: default
nav_exclude: true
---

# DTG review: Verifiable Trust Infrastructure August 2026 change window

**Assessment ID:** `DTG-AR-2026-002`  
**Assessment key:** `dtg:repository:OpenVTC/verifiable-trust-infrastructure`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** findings-raised  
**Reviewed revision:** `187ad9cde4cf5c5f8add3732a661816a650d631c`

## Scope

This assessment extends the existing VTI review through
`1c20e3157597952d174fa2e884609f5b938923be` →
`187ad9cde4cf5c5f8add3732a661816a650d631c` and dispositions RAHP toolkit
issue **#8**.

The review intentionally includes implementation code that the previous generic
materiality filter did not classify as material. The role-aware monitoring change in this
repository now treats source and test surfaces of a reference implementation as assurance
evidence.

## Material assurance changes

The revision adds or materially changes:

- ISO mdoc ingestion, verification, storage and presentation;
- configured IACA trust anchors for mdoc issuer validation;
- holder/device-key binding for mdoc credentials;
- presentation over OID4VP;
- non-extractable internal signing keys;
- key-management and credential-exchange service paths; and
- Trust Tasks integration and related conformance behaviour.

The mdoc trust implementation fails closed when no anchors are configured, verifies the
Document Signer against a configured CA anchor, checks certificate validity and signing
usage, and deliberately keeps the X.509 trust-store decision explicit at the VTA boundary.
Internal signing keys are intentionally non-exportable, excluded from mnemonic recovery
and backup export, and prohibited for `did:webvh` update signing where irreversible key
loss would strand the identity.

## Findings and follow-up

### F-003 — attested configuration verification remains required

The prior TEE finding remains applicable: production trust requires the consuming workflow
to verify nonce-bound attestation, approved measurements and expected tenant KMS material.
Exposure of evidence is not equivalent to policy consumption.

**Status:** watch.

### F-004 — parent availability/routing influence remains outside attestation

A parent can still delay or disrupt configuration/routing even when it cannot forge an
approved attested configuration.

**Status:** residual operational risk.

### F-006 — IACA trust-anchor lifecycle is now a first-class authority dependency

mdoc verification depends on a configured set of IACA roots. The implementation correctly
fails closed for an empty set and validates the leaf against an accepted root, but the
assurance proposition "this issuer is currently trusted for this relying purpose" depends
on how anchors are sourced, approved, updated, withdrawn and audited.

**Disposition:** require deployment evidence identifying trust-anchor provenance, approving
authority, effective period and change history. Do not infer issuer authority merely from a
cryptographically valid chain.

### F-007 — certificate revocation is deliberately not checked

The mdoc trust module explicitly does not perform CRL/OCSP checking. Short certificate
validity mitigates but does not eliminate compromise/revocation risk.

**Disposition:** document this as an assurance limitation. Profiles requiring current
revocation knowledge must supply an external status mechanism and explicit fail-open/
fail-closed policy.

### F-008 — non-extractable keys trade recoverability for stronger custody

Internal keys strengthen custody by refusing export even to administrators, but loss of the
KMS key or sealed storage permanently destroys signing capability. In non-TEE deployments,
operator disk access remains inside the protection boundary.

**Disposition:** require key-origin and recoverability classification in deployment policy,
with explicit prohibition on using unrecoverable keys where loss would permanently strand
an identity/control chain.

## Assurance disposition

The reviewed revision is **conditionally acceptable with explicit residual operational and
lifecycle dependencies**. The implementation adds strong fail-closed and non-exportability
controls and makes important trust decisions visible rather than implicit. No blocking defect
is raised against the reviewed SHA.

This record closes RAHP toolkit issue **#8** for revision
`187ad9cde4cf5c5f8add3732a661816a650d631c` and establishes that SHA as the
new DTG RAHP baseline.

## Sources

- <https://github.com/OpenVTC/verifiable-trust-infrastructure/compare/1c20e3157597952d174fa2e884609f5b938923be...187ad9cde4cf5c5f8add3732a661816a650d631c>
- <https://github.com/OpenVTC/verifiable-trust-infrastructure/blob/187ad9cde4cf5c5f8add3732a661816a650d631c/docs/02-vta/internal-keys.md>
- <https://github.com/OpenVTC/verifiable-trust-infrastructure/blob/187ad9cde4cf5c5f8add3732a661816a650d631c/vta-vault/src/mdoc_trust.rs>
