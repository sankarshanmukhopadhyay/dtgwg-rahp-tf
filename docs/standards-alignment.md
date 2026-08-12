# External standards alignment

RAHP uses external standards alignment to show where a security-hardening finding is reinforced by established security controls, credential standards, or threat models.

## Canonical registry

[`data/external-standards.yaml`](../data/external-standards.yaml) is the source of truth for external references. Review YAML stores the registry ID rather than duplicating publication URLs.

The initial baseline contains:

- NIST Cybersecurity Framework 2.0;
- NIST SP 800-53 Rev. 5;
- NIST SP 800-63 Revision 4 and its authentication/federation volumes;
- NIST SP 800-207 and SP 800-207A;
- W3C Verifiable Credentials Data Model v2.0;
- W3C Verifiable Credential Data Integrity 1.0;
- W3C Bitstring Status List v1.0;
- OWASP API Security Top 10 2023; and
- OWASP Agentic AI — Threats and Mitigations.

This corpus should expand only when a new source materially improves a finding or supplies a missing assurance dimension.

## Mapping model

A security finding uses:

```yaml
external_alignment:
  - ref: W3C-BSL-1.0
    clause: "7.2 Validity Periods"
    relationship: direct
    rationale: >
      Credential status validity directly informs the finding about stale
      or ambiguous status information.
```

`relationship` is controlled as `direct`, `supports`, `analogous`, or `contextual`.

The rationale is mandatory. It should state *why* the reference matters to this finding and avoid claiming endorsement or applicability beyond the source's stated scope.

## Interpretation

External alignment serves three purposes:

1. **Defensibility** — show that a recommendation is grounded in recognized security principles rather than only local preference.
2. **Translation** — let implementers and SDO participants relate RAHP terminology to frameworks they already use.
3. **Coverage analysis** — reveal where a DTG-specific threat has no close external analogue and therefore needs original standards work.

External alignment does not replace RAHP's own risk/control analysis, and the absence of a mapping does not make a finding invalid.
