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
**Reviewed revision:** `8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3`

## Scope and trigger consolidation

This review consolidates multiple observations into one assessment work item. The
review window starts at `fbe196a8a17ba3f99d0657a64be5ac58621023a1`, the prior
DTG RAHP baseline, and advances through `8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3`.
The latter supersedes the intermediate queued revision
`bcc75f5837bd92bbf81f7755aa5842de7bcd6f8b` rather than requiring a second review.

The following RAHP queue records are therefore dispositioned by this review:

- RAHP toolkit issue #1 — material Trust Tasks repository change;
- RAHP toolkit issue #3 — upstream Trust Tasks issue #173 changed;
- RAHP toolkit issue #4 — upstream Trust Tasks issue #205 changed and closed.

Watched upstream discussions are assessment triggers, not normative evidence. The
normative/editorial repository delta at the reviewed SHA remains the primary evidence.

## Material assurance changes

The reviewed change window materially strengthens several controls relevant to RAHP:

1. **Authorization is separated from identity and proof validation.** Framework and
   task-level material now makes the authorization decision explicit rather than
   allowing proof, identity, membership or successful validation to imply execution
   authority.
2. **Duplicate consequential execution becomes a normative concern.** The framework
   now requires duplicate-execution protection for consequential tasks and introduces
   explicit conflict handling for reuse of an identifier with different content.
3. **Authority is re-evaluated at consequential execution boundaries.** Long-running,
   resumed and agentic tasks must not rely indefinitely on authority that was valid
   only when the document was first accepted.
4. **Transport-dependent proof omission is more accountable.** Bindings that rely on
   transport security to permit omission of an in-band proof must describe the
   producer authentication, audience, intermediary, freshness, replay and key-status
   boundary on which that decision rests.
5. **Task-control/corrigibility is now an explicit design surface.** The repository
   records cancellation, suspension, resumption, partial execution and irreversible
   effect boundaries rather than treating transport cancellation as equivalent to
   semantic withdrawal.

These changes reduce risks already represented by RAHP around delegated authority,
replay, stale authorization, transport confusion and agentic execution. They do not
eliminate the need to test individual Trust Task specifications and implementations.

## Findings and follow-up

### F-001 — retained outcome evidence remains a cross-specification dependency

Trust Tasks issue #173 demonstrates that a DTG credential verifier may rely on a
retained outcome document outside the original bilateral exchange. Error provenance,
terminal-state semantics and proof requirements therefore need to remain aligned
between Trust Tasks and the Credential Specification. The discussion is useful
situational evidence but is not itself normative input.

**Disposition:** keep `trust-tasks-spec`, `dtg-credential-spec` and
`cross-spec-composition` linked in the issue-watch registry. Reassess when the
normative artifacts change.

### F-002 — semantic task control is not yet fully closed

Upstream issue #204 remains open. The design direction now distinguishes semantic
cancellation from transport cancellation and recognizes partial/irreversible effects,
but the complete portable control mechanism is still evolving.

**Disposition:** retain #204 as a watched dependency. A later normative repository
change is a new observation and should be coalesced into the next open Trust Tasks
assessment cycle rather than creating one issue per comment.

## Assurance disposition

The reviewed revision is a **net strengthening of the security and harms posture** for
consequential, delegated and agentic Trust Tasks. No additional blocking RAHP defect is
raised against the reviewed SHA. The two findings above are continuing
cross-specification/corrigibility dependencies and remain observable through the DTG
instance monitor.

This record closes the assessment cycle for the queued revision through
`8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3` and establishes that SHA as the DTG RAHP
repository baseline.

## Sources

- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/compare/fbe196a8a17ba3f99d0657a64be5ac58621023a1...8eb7509ffabf6cc095eec20cb7d8d0120ff59ef3>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/173>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/202>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/203>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/204>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/205>
- <https://github.com/trustoverip/dtgwg-trust-tasks-tf/issues/206>
