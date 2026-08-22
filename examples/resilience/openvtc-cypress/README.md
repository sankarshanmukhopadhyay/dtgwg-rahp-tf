# OpenVTC Cypress DRARM reference profile

This directory demonstrates how an ecosystem-specific target maps into RAHP's generic Distributed Resilience and Amplification Risk Model without changing portable DRARM semantics.

It is now also a **maintainer-feedback exemplar**: the original Cypress assessment produced findings and review gaps, the maintainer supplied counter-evidence and sharper implementation evidence, and RAHP records the resulting transitions rather than treating the detector output as immutable truth.

## Run the profile

Use the **Run distributed resilience assessment** workflow with:

```text
target_repository = OpenVTC/openvtc
target_ref = Cypress
target_type = mixed
profile_path = examples/resilience/openvtc-cypress/profile.yaml
upstream_repository = OpenVTC/openvtc
```

The profile uses `findings-and-review-gaps` because a tagged-release review benefits from surfacing unresolved assurance evidence as well as directly observed hazardous constructs. Upstream filing remains `recommend-only`; ownership and remediation are governed follow-on actions.

## Why the queue finding is intentionally not a clean acceptance

The original review detected production `unbounded_channel` use and treated the signal as a Critical queue-growth finding. Maintainer review established a material architectural counter-claim for the DIDComm handoff: the upstream mediator copy has already been acknowledged and deleted before local handoff, so a bounded queue that drops on overflow can destroy consequential credentials and verdicts, while blocking can simply move loss to an upstream lag boundary.

RAHP therefore does **not** convert that counter-claim directly into `controlled` or `assured`. In this profile the `unbounded-channel` detector is overridden to `review-only`, and the disposition remains `review-required` until executable evidence demonstrates the claimed operating bound.

Required evidence includes queue depth/high-water telemetry, producer-faster-than-consumer stress, stalled-consumer memory measurements, and explicit overload/recoverability semantics.

This is the intended review lifecycle:

```text
static detector signal
        ↓
initial finding hypothesis
        ↓
maintainer counter-evidence / architecture rationale
        ↓
weakened to review-required
        ↓
executable evidence
     /        \
  fails      passes
    ↓           ↓
 finding    controlled
```

## Finding transitions

`maintainer-disposition.yaml` is the machine-readable record of the feedback loop:

- `OVTC-RAHP-01` — **weakened** and narrowed to the material WebVH AutoAssign/idempotency seam; severity Medium.
- `OVTC-RAHP-02` — **weakened** from Critical finding to `review-required` pending runtime evidence.
- `OVTC-RAHP-03` — **strengthened** because decision evidence is present on the wire and discarded by the client.
- `OVTC-RAHP-04` — **strengthened** because the stable fallback is a resolvable `did:webvh`, making correlation a direct lookup.
- `RLA-016` — promoted into the current multi-instance reconnect-loop finding.
- `RLA-030` — remains separately `review-required`; noisy-neighbour capacity is not the same failure as mutual websocket eviction.

The historical assessment remains available in `rahp-toolkit#18`; the current v1.5 reassessment is `rahp-toolkit#46`.

## Portable method lesson

A detector identifies evidence that deserves disposition. It does not own the final disposition. Maintainer rationale is valid assurance evidence, but it must itself be testable. Deployment topology and blast radius can change severity without making the underlying signal disappear.
