---
title: "DTG review: Trust Tasks August 2026 change window"
parent: DTG RAHP review record
nav_order: 10
layout: default
nav_exclude: true
---

# DTG review: Trust Tasks August 2026 change window

**Assessment ID:** `DTG-AR-2026-001`  
**Assessment key:** `dtg:repository:trustoverip/dtgwg-trust-tasks-tf`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** assurance-strengthened-with-residual-cross-spec-gaps  
**Assessment queue disposition:** `findings-raised`  
**Reviewed revision:** `2a40f6bd3b13c85c49123174fdbe4354b3c48d81`

## Scope and trigger consolidation

This durable record now covers the Trust Tasks material change windows through
`2a40f6bd3b13c85c49123174fdbe4354b3c48d81` and closes the assessment queue
record in RAHP toolkit issue **#20**.

The immediately preceding reviewed baseline was
`7e0d755f5b815498c861cacecee5cae49b3f14eb`. The new window contains 13 commits,
including the VTA context, service and WebVH lifecycle task families plus HTTPS
binding 0.2.

Issue #20 initially observed `a8cc6f3373525716a19747b834460a225ff08516`.
The monitor subsequently advanced to `2a40f6bd3b13c85c49123174fdbe4354b3c48d81`;
this assessment intentionally reviews the later SHA because it is a direct descendant
and therefore subsumes the queued revision.

## Material assurance changes

The reviewed delta materially expands the normative surface, but it also makes several
important governance properties explicit and machine-testable:

1. **Authentication is explicitly separated from authorization.** VTA task specifications
   state that proof establishes who authored a request while role/scope checks determine
   whether it may execute.
2. **Authority is scoped to the affected object.** Context creation requires administrator
   authority over the VTA or parent scope; destructive context deletion requires administrator
   authority over the target context.
3. **Destructive operations preserve attributable evidence.** Proof is mandatory for deletion,
   with the audit record treated as the surviving evidence after keys, DIDs or scoped content
   are removed.
4. **Destructive semantics are explicit.** Context deletion is all-or-nothing by default,
   refuses non-empty deletion unless `force` is explicit, and distinguishes successful response
   transport from the semantic `deleted` result.
5. **Scope inheritance is explicit.** Nested contexts inherit parent reachability, making the
   authority consequence of hierarchy observable rather than implicit.
6. **Lifecycle task families are now first-class specification surfaces.** Context, service,
   WebVH DID and server operations expose distinct create/update/delete/disable/drain/rollback
   semantics instead of collapsing them into generic implementation behaviour.
7. **HTTPS endpoint ownership is explicit.** Binding 0.2 defines the advertised service endpoint
   as the base URL, the `/trust-tasks` operation path, the `TrustTaskHTTPS` DID service type and
   endpoint ownership/discovery semantics.
8. **Generated bindings and validation improve evidence quality.** The change window includes
   generated TypeScript/Rust bindings and CI guardrails that make schema drift observable.

## Residual assurance states

| Assurance proposition | State | Rationale |
|---|---|---|
| Proof identifies the request author | `controlled` | Task specifications require proof and distinguish it from authorization. |
| Role/scope authorization is separate from proof | `controlled` | Context and destructive operations define administrator checks independently of signature verification. |
| Lifecycle operations are semantically distinguishable | `controlled` | Create/update/delete/disable/drain/rollback families are explicit task surfaces. |
| Destructive deletion is attributable and explicit | `controlled` | Proof, force semantics, semantic result and surviving audit evidence are specified. |
| Cross-system delegated authority is verified at action time | `assurance-gap` | Core Trust Tasks cannot establish a universal delegation model for companion credentials or deployment governance. |
| Duplicate consequential execution is prevented across task + credential composition | `assurance-gap` | Trust Tasks can expose execution semantics, but cross-spec one-time/idempotent binding remains a companion-profile obligation. |
| Credential/status/policy lifecycle is synchronized | `assurance-gap` | No single cross-spec status-as-of and revocation contract exists. |
| Composed privacy is bounded | `review-required` | Task identifiers, endpoint metadata, errors and companion proofs require composition-level disclosure analysis. |
| Cross-boundary contestability is defined | `review-required` | Responsibility and evidence packaging span task, credential, registry and deployment governance layers. |

## Findings and disposition

### F-001 — Retained outcome dependency

**Residual state:** `assurance-gap`

Trust Tasks now makes execution and lifecycle semantics substantially clearer, but a relying
system must still keep task outcome evidence separate from credential validity. A credential
that refers to a task does not, by itself, prove that the task completed or that its effect
occurred exactly once.

**Owner:** cross-specification companion profile / relying implementation.  
**Retest condition:** adopted profile binds credential use to task instance, outcome evidence,
freshness and idempotent execution.

### F-002 — Generic task control and lifecycle observability

**Residual state:** `controlled`

The expanded VTA task families make authorization, destructive semantics and lifecycle
transitions explicit enough to remove the earlier generic-control ambiguity from this
review window. This does not grant assurance credit to downstream implementations unless
they demonstrate conformance to those semantics.

### F-005 — Supervising / delegated authority

**Residual state:** `assurance-gap`

Proof plus local administrator role establishes the authority model for individual VTA
operations, but cross-system supervisory or delegated authority remains outside the core
specification. A companion governance/delegation profile must define principal, delegate,
scope, purpose, validity, revocation and action-time evaluation.

**Owner:** companion profile / deployment governance authority.  
**Retest condition:** machine-verifiable delegation and lifecycle evidence is required and
negative tests reject validly signed but out-of-scope or revoked authority.

## Security disposition

No new blocking security defect was identified in the reviewed Trust Tasks delta. The changes
are net assurance-strengthening because authorization boundaries, destructive-operation
semantics, lifecycle transitions and evidence survival become more explicit. The residual
findings above are composition and governance gaps rather than a reason to treat the Trust
Tasks implementation surface as unsafe by default.

## Closure and downstream effects

This assessment dispositions issue **#20** and establishes
`2a40f6bd3b13c85c49123174fdbe4354b3c48d81` as the reviewed Trust Tasks baseline for
subsequent cross-specification reviews, including the refreshed Trust Tasks × Credential
Specification assessment tracked in issue **#15**.

Closing the queue issue does **not** accept the residual assurance gaps. It records that the
material change has been reviewed, classified and assigned explicit retest conditions.

## Retest triggers

- material Trust Tasks specification or VTA lifecycle change;
- adoption/change of a delegation or authority companion profile;
- Credential Specification changes affecting task/outcome binding or status semantics;
- implementation evidence showing different destructive-operation or lifecycle behaviour;
- new privacy or redress profile that changes the composition boundary.

## Sources

- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/compare/7e0d755f5b815498c861cacecee5cae49b3f14eb...2a40f6bd3b13c85c49123174fdbe4354b3c48d81>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/tree/2a40f6bd3b13c85c49123174fdbe4354b3c48d81/specs/vta>
