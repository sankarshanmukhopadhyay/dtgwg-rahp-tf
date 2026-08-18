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
**Disposition:** findings-raised  
**Reviewed revision:** `7e0d755f5b815498c861cacecee5cae49b3f14eb`

## Scope and trigger consolidation

This assessment extends the earlier review through the material change window
`8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3` →
`7e0d755f5b815498c861cacecee5cae49b3f14eb` and consolidates RAHP toolkit
issues **#7** and **#9** into the existing durable assessment record.

Issue #9 observed closure of upstream Trust Tasks issue #204. That observation is
not treated as normative evidence on its own. The resulting repository changes are
inside the #7 revision window and are the evidence used for this disposition.

## Material assurance changes

The new delta completes a major portion of the previously open corrigibility surface:

1. **Semantic task control is now specified.** `trust-task-control/0.1` defines
   `cancel`, `suspend`, and `resume` as protocol-level operations rather than
   transport cancellation.
2. **Proof remains separate from authority.** The control specification explicitly
   states that proof establishes who asked, not whether the caller may control the
   task. The initiator is the default authority floor; broader supervisory authority
   remains local policy/governance.
3. **Control is evaluated at effect time.** Consumers must re-evaluate valid control
   operations before irreversible or externally visible effects, making race handling
   part of the execution pipeline rather than an advisory note.
4. **Cancellation does not pretend to roll back history.** Responses distinguish
   `applied`, `appliedWithEffects`, `alreadyCompleted`, and `unknownTask`, and must
   describe prior externally visible effects when cancellation arrives too late.
5. **Cancelled work remains replay-resistant.** Consumers retain the cancellation
   record through the acceptance window so redelivery of the original task is absorbed.
6. **Out-of-order control is recognized.** A consumer is advised to record a control
   operation that arrives before the target task and reject the later-arriving task.
7. **Authorization evidence was propagated to consequential specifications.** The
   revision also adds explicit authorization statements across multiple task types and
   tightens consumer conformance behaviour.
8. **Task identity is strengthened for retained evidence.** Citations now bind a task
   digest rather than an identifier alone, reducing ambiguity when evidence is reused.

## Findings and follow-up

### F-001 — retained outcome evidence remains a cross-specification dependency

Trust Tasks issue #173 still demonstrates that a DTG credential verifier may rely on a
retained outcome document outside the original bilateral exchange. Error provenance,
terminal-state semantics and proof requirements must remain aligned between Trust Tasks
and the Credential Specification.

**Disposition:** retain the cross-specification watch. This is not a defect introduced by
this revision.

### F-002 — semantic task control is substantially closed; compensation remains domain-specific

The previous finding that task control itself was not normatively closed is resolved by
this revision. A remaining boundary is intentionally outside the generic framework:
rollback/compensation for irreversible effects is domain-specific. The protocol now makes
that boundary observable by requiring effect reporting rather than implying rollback.

**Disposition:** close the generic corrigibility gap. Retest compensation semantics only
where a consequential task/profile claims reversibility or automated remediation.

### F-005 — supervising-principal control depends on local policy evidence

The specification allows a consumer to recognize a mandate holder, supervising principal,
or organization as authorized to control a task initiated by its agent. This is the right
architecture, but cross-system interoperability still depends on the relying deployment
being able to evidence that supervisory authority and its current scope.

**Disposition:** watch as a deployment/cross-specification assurance dependency; do not
require Trust Tasks itself to define a universal delegation model.

## Assurance disposition

The revision is a **net material strengthening** of authority separation, corrigibility,
replay handling, retained evidence and action-time control. No blocking RAHP or security
defect is raised against the reviewed SHA.

This record closes the generated assessment cycle represented by RAHP toolkit issues
**#7 and #9** and advances the reviewed baseline to
`7e0d755f5b815498c861cacecee5cae49b3f14eb`.

## Sources

- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/compare/8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3...7e0d755f5b815498c861cacecee5cae49b3f14eb>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/blob/7e0d755f5b815498c861cacecee5cae49b3f14eb/specs/trust-task-control/0.1/spec.md>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/204>
