---
title: "DTG review: Verifiable Trust Infrastructure August 2026 change window"
parent: DTG RAHP review record
nav_order: 20
---

# DTG review: Verifiable Trust Infrastructure August 2026 change window

**Assessment ID:** `DTG-AR-2026-002`  
**Assessment key:** `dtg:repository:OpenVTC/verifiable-trust-infrastructure`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** findings-raised  
**Reviewed revision:** `1c20e3157597952d174fa2e884609f5b938923be`

## Scope

This review dispositions RAHP toolkit issue #2 and covers
`a879926704382c72cec24f8b1367194f7fb087fa` through
`1c20e3157597952d174fa2e884609f5b938923be` in
`OpenVTC/verifiable-trust-infrastructure`.

The material change is the Nitro/TEE configuration and attestation work: fleet
instances can use a common enclave image while receiving a constrained tenant-specific
configuration overlay at runtime. That changes the trust boundary around who supplies
configuration, what the enclave can accept, and what evidence a tenant or relying party
must verify before treating the instance as correctly configured.

## Material assurance changes

The reviewed implementation includes several safeguards that materially constrain the
new runtime-configuration risk:

1. a typed tenant overlay with unknown-field rejection rather than unrestricted
   whole-configuration injection;
2. fail-closed behavior for missing or malformed fleet configuration;
3. restrictions around KMS account/key selection and configuration provenance;
4. attestation evidence binding the effective secret-free configuration view to the
   enclave report;
5. required image/PCR and tenant KMS-key pinning before obtaining the stronger verified
   attestation result;
6. explicit separation between authenticated configuration evidence and policy-approved
   configuration evidence; and
7. additional tests for envelope parsing, timeout behavior, routing changes and fleet
   build paths.

These are substantial mitigations. The design does not make the parent environment
trusted; instead it narrows what parent-controlled configuration can express and gives
an external verifier evidence with which to reject an unacceptable configuration.

## Findings and follow-up

### F-003 — onboarding depends on verification of the attested configuration

The architecture is safe only if the tenant or relying workflow actually verifies the
nonce-bound attestation, approved image/PCR and expected tenant KMS key before granting
trust or onboarding authority. Merely exposing an attestation endpoint is not the same
as consuming it as a gate.

**Disposition:** treat the verification step as required assurance evidence for a
production deployment and retain it in deployment documentation/conformance tests.

### F-004 — the parent retains availability and routing influence

Attestation prevents a malicious parent from silently presenting an unapproved
configuration as approved, but it does not prevent the parent from withholding,
delaying or disrupting configuration delivery or related routing. Those are
availability/corrigibility concerns rather than configuration-integrity failures.

**Disposition:** document the residual availability boundary and ensure operators do
not interpret successful attestation as evidence of availability or liveness.

## Assurance disposition

The reviewed delta changes the TEE trust boundary materially but also contains
purpose-built controls for the major configuration-integrity and tenant-isolation
risks introduced by that change. The assessment therefore raises the two operational
assurance findings above rather than a blocking defect.

`1c20e3157597952d174fa2e884609f5b938923be` becomes the reviewed DTG RAHP baseline for
this target.

## Sources

- <https://github.com/OpenVTC/verifiable-trust-infrastructure/compare/a879926704382c72cec24f8b1367194f7fb087fa...1c20e3157597952d174fa2e884609f5b938923be>
- <https://github.com/OpenVTC/verifiable-trust-infrastructure/commit/277b926f7e4a90d77ca4975c4280abd96fd62edb>
