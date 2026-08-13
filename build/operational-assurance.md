# Operational assurance pilot

RAHP v0.4 introduces five **proposed pilot monitoring contracts**. They are implementation
scaffolds, not claims that any DTG deployment is currently collecting this evidence.

| Metric | Status | Signal | Threshold rule | Evidence | Responsible role |
|---|---|---|---|---|---|
| M-02 Time to Revocation Notice (SLA) | pilot_proposed | Elapsed hours from revocation decision timestamp to formal notification timestamp. | Instance target must be defined before activation; any breach of the adopted revocation-notification SLA enters triage. | EV-001 | VTC governance operations |
| M-04 IDVC Issuer Verification Rate | pilot_proposed | Percentage of Phase 4 admissions with IDVP DID and authority verified before VMC issuance. | Target is 100%; any unverified admission is a triage event. | EV-002 | VTC admission authority |
| M-06 Registry Write Authorisation Failure Rate | pilot_proposed | Percentage of unauthorised single-party registry write attempts rejected by policy enforcement. | Target is 100% rejection; any successful unauthorised write is a critical triage event. | EV-003 | registry operations and governance |
| M-08 Agent Credential Scope Violation Rate | pilot_proposed | Rate of agent actions attempted or executed outside the delegated credential scope. | Target is zero successful out-of-scope actions; attempted violations are retained for trend review. | EV-004 | delegation policy operator |
| M-27 Agent Liveness Check Interval Compliance Rate | pilot_proposed | Percentage of required operator/agent liveness checks completed within the adopted interval. | Target is 100% interval compliance; missed liveness checks suspend reliance until re-established. | EV-005 | agent operator |

Rule profiles and evidence contracts remain canonical under `data/`.
