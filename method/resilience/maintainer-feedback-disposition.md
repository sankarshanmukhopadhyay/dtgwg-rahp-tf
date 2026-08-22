# Maintainer feedback and DRARM finding disposition

RAHP treats detector output as **evidence for disposition**, not as an authority that overrides repository-specific facts.

This policy applies when a target maintainer responds to a DRARM signal with architectural rationale, implementation evidence, runtime measurements, or ownership information.

## Disposition sequence

1. **Detect the signal.** Preserve the original detector evidence and target revision.
2. **Identify the control claim.** Record the maintainer's explanation in falsifiable terms. A statement such as "this queue is safe" is insufficient; the claim must identify why growth, loss, duplication, or amplification is bounded or preferable to the alternative.
3. **Check scope and topology.** Re-evaluate severity against deployment topology, shared fate, producer cardinality, consumer rate, payload size, authority boundary and blast radius.
4. **Require corroborating evidence.** A documented rationale may weaken a finding to `review-required`; it does not by itself produce `controlled` or `assured`.
5. **Retest the claim.** Prefer executable tests, measurements, fault injection, durable logs, or machine-verifiable policy evidence.
6. **Record lineage.** Use an explicit transition such as `unchanged`, `strengthened`, `weakened`, `resolved`, `split`, `merged`, `superseded`, or `not-retested`.

## Queue-specific rule

An unbounded channel is a resource-risk signal, but bounding it is not automatically the safe remediation. Review acknowledgement and handoff ordering before prescribing a bound.

For a consequential queue, record at least:

- whether the upstream copy still exists when the local queue accepts work;
- what happens when a bounded queue is full;
- whether blocking propagates pressure into another lossy or bounded layer;
- producer cardinality and maximum credible burst rate;
- consumer service rate and failure/stall behaviour;
- payload size or other memory-growth bound;
- queue depth/high-water/lag observability;
- slow-consumer and producer-faster-than-consumer measurements.

A documented loss-avoidance rationale can justify `review-required` rather than an asserted finding. Moving to `controlled` requires evidence that the claimed operating bound holds under induced load or failure.

## Severity calibration

Severity is a property of the failure in its deployment context, not of the syntax that triggered a detector. A construct in a single-user local application can have a different blast radius from the same construct in a multi-tenant service, while still requiring evidence.

Do not use topology to erase a real failure mode. Use it to calibrate consequence, affected principals, shared fate and recovery cost.

## Ownership

A finding may be valid while remediation belongs in another repository or layer. Record:

- the target where the effect is observed;
- the authority/control plane that can actually enforce the fix;
- any downstream adoption/conformance requirement;
- the evidence needed to show that the downstream target consumes the upstream fix.

## Reference exemplar

`examples/resilience/openvtc-cypress/` demonstrates this lifecycle. The original queue-growth signal was challenged with a concrete acknowledgement/loss argument, weakened to `review-required`, and converted into explicit runtime evidence obligations rather than either being defended mechanically or dismissed by maintainer assertion.
