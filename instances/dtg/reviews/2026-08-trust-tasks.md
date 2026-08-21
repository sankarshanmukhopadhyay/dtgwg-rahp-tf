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
7. **HTTPS endpoint ownership is clarified.** Binding 0.2 defines the advertised endpoint as
   the Trust Task base, defines `TrustTaskHTTPS` DID service discovery, and prevents endpoint
   interpretation from being left to incompatible client assumptions.
8. **Generated bindings and CI guardrails accompany the normative additions.** TypeScript and
   Rust bindings plus validation workflows materially improve evidence that schemas and generated
   interfaces remain synchronized.

## Residual-state classification

| Proposition | Residual state | Assessment |
|---|---|---|
| Proof identifies the caller independently of transport | `controlled` | Normatively required for consequential VTA tasks and bound into audit evidence. |
| Role/scope authorization is evaluated separately from proof | `controlled` | Explicit authorization sections define the distinction and target scope. |
| Context/service/DID lifecycle operations expose distinguishable semantics | `controlled` | Dedicated task families and schemas make the state transitions reviewable and testable. |
| Destructive deletion produces attributable evidence and explicit destructive intent | `controlled` | Mandatory proof, non-empty refusal, and `force` semantics provide enforceable controls. |
| Cross-system delegated authority can be verified at action time | `assurance-gap` | Trust Tasks correctly leaves broader mandate/delegation evidence to local policy or companion profiles. |
| Duplicate consequential execution is prevented across task + credential composition | `assurance-gap` | Component semantics improve replay handling, but cross-spec freshness/idempotency binding remains external. |
| Credential/status/policy lifecycle is synchronized with Trust Task lifecycle | `assurance-gap` | The task lifecycle is explicit; composed status-as-of and safe-degradation rules remain undefined. |
| Cross-context privacy impact is bounded across task, credential, transport and error evidence | `review-required` | New VTA and endpoint surfaces increase the number of observable artifacts; composition analysis remains necessary. |
| Adverse outcomes have an accountable cross-boundary contestability path | `review-required` | Component audit evidence improves explainability, but responsibility allocation remains a governance/profile concern. |

## Findings and follow-up

### F-001 — retained outcome evidence remains a cross-specification dependency

Trust Task context and outcome evidence can be retained and consumed outside the original
exchange. The Credential Specification now strengthens edge binding by requiring a VWC digest,
but the broader contract between authorization, task completion, retained outcome evidence and
credential interpretation remains a composition responsibility.

**Residual state:** `assurance-gap`  
**Disposition:** retain as a cross-specification watch; addressed in the refreshed #15 assessment.

### F-002 — generic task-control and lifecycle observability are materially strengthened

The earlier framework-level corrigibility gap remains closed. The new VTA lifecycle families
further improve explicitness around destructive operations, rollback boundaries, disable/drain
states and object ownership.

**Residual state:** `controlled`  
**Disposition:** no new Trust Tasks defect raised.

### F-005 — supervising-principal and delegated authority remain profile/governance dependencies

The specification consistently separates proof from authorization and defines role checks, which
is the correct architectural boundary. Interoperability still depends on deployments being able
to evidence the current mandate, scope and revocation state of a supervising principal or agent.

**Residual state:** `assurance-gap`  
**Disposition:** retain as a deployment/cross-specification dependency; do not require Trust Tasks
to define a universal delegation model.

## Security review disposition

No new blocking security defect is raised against `2a40f6bd3b13c85c49123174fdbe4354b3c48d81`.
The most security-relevant additions strengthen attribution, scope checks, destructive-operation
explicitness, endpoint ownership and schema/binding validation. The residual risks arise when
Trust Tasks is composed with credentials, delegation evidence, cached status, privacy-sensitive
proofs or external governance systems.

## Assurance disposition

The revision is a **net material assurance strengthening** and is suitable to become the reviewed
Trust Tasks baseline for downstream composition reviews.

RAHP toolkit issue **#20** is therefore eligible for closure. Its closure does not assert that all
Trust Tasks compositions are safe; it records that the queued repository revision has been reviewed
and that its residual risks are explicitly classified.

The downstream Trust Tasks × Credential Specification review in **#15** must use this reviewed SHA
rather than the older `fbe196a8` baseline.

## Retest triggers

Retest this assessment when any of the following occurs:

- a material Trust Tasks repository change affecting authority, lifecycle, replay or privacy;
- a generic delegation/supervisory-authority profile is introduced;
- retained outcome evidence semantics change;
- cross-task idempotency/freshness semantics become normative;
- VTA lifecycle tasks move maturity level or materially alter destructive/rollback semantics.

## Sources

- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/compare/7e0d755f5b815498c861cacecee5cae49b3f14eb...2a40f6bd3b13c85c49123174fdbe4354b3c48d81>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/blob/2a40f6bd3b13c85c49123174fdbe4354b3c48d81/specs/vta/contexts/create/1.0/spec.md>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/blob/2a40f6bd3b13c85c49123174fdbe4354b3c48d81/specs/vta/contexts/delete/1.0/spec.md>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/blob/2a40f6bd3b13c85c49123174fdbe4354b3c48d81/bindings/https/0.2/spec.md>
