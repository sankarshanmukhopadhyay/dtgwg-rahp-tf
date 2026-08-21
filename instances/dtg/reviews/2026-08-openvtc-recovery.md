---
title: "DTG review: OpenVTC authoritative-state and recovery change window"
parent: DTG RAHP review record
nav_order: 40
layout: default
nav_exclude: true
---

# DTG review: OpenVTC authoritative-state and recovery change window

**Assessment ID:** `DTG-AR-2026-004`  
**Assessment key:** `dtg:repository:OpenVTC/openvtc`  
**Mode:** combined RAHP + security  
**Status:** dispositioned  
**Disposition:** findings-raised  
**Reviewed revision:** `4fc64d711724cdbd23f94507b4e3743f99f00dcd`

## Scope

This assessment reviews the material change window
`df623ec303a90e83ed60a2f84e63db3efb3f0cc1` →
`4fc64d711724cdbd23f94507b4e3743f99f00dcd` and dispositions RAHP toolkit
issue **#26**.

The window materially changes recovery, local-state reconstruction and the
relationship between OpenVTC and its VTA. It adds durable secret handling,
context-occupancy protection, account reconstruction, recovery application,
device-presence handling and a design record for VTA-authoritative state.

## Material assurance observations

1. **Recovery is re-authorisation, not identity recovery.** The design explicitly
   treats the administrator credential as an authorisation grant and keeps persona
   identity and private-key authority at the VTA.
2. **Existing context state is protected from accidental overwrite.** Setup probes
   an occupied context and offers recovery rather than silently treating it as a new
   account.
3. **Rebuild evidence is verified.** Recovery reconstructs state from VTA-held DIDs,
   credentials and context data instead of trusting a local backup as authoritative.
4. **Destructive recovery semantics are narrowed.** Starting fresh is separated from
   deletion, and the design records revocation of superseded authorisations as a
   recovery obligation.
5. **Local secret handling is materially strengthened.** The change window includes
   durable Linux secret storage and fail-closed, diagnosable startup failures.
6. **Authority remains externally governed.** Reprovisioning an existing context
   requires an authorised operator or an explicitly configured consent/approver path;
   knowledge of a context identifier is not sufficient authority.

## Residual findings

### F-001 — recovery authority requires pre-established governance evidence

**Residual state:** `assurance-gap`

A recovery approver or equivalent authority must be established before loss of the
original client. A recovery ceremony created only after loss does not independently
prove legitimate continuity of authority.

**Owner:** deployment / VTA governance profile.  
**Retest condition:** a profile demonstrates pre-registered recovery authority,
revocation of superseded grants, and evidence linking approval to the exact recovery
payload.

### F-002 — VTA-authoritative reconstruction expands confidentiality exposure

**Residual state:** `review-required`

The architecture intentionally places membership, relationship and contact state at
the VTA so that it can be reconstructed. This is a recoverability gain and a privacy
trade-off: compromise or operator access at the VTA can expose the relationship graph.

**Owner:** deployment privacy/governance profile.  
**Retest condition:** deployed profiles document data minimisation, operator-access
controls, retention and incident-response obligations for reconstructed account state.

### F-003 — application-state concurrency remains a cross-repository dependency

**Residual state:** `assurance-gap`

The design identifies versioned application state and conflict detection as a required
primitive. Safe multi-client recovery therefore depends on the VTA/VTI application-state
contract providing version/precondition semantics rather than last-writer-wins mutation.

**Owner:** OpenVTC + VTI integration boundary.  
**Retest condition:** executable tests demonstrate versioned writes, conflict surfacing,
and recovery without silent overwrite under concurrent clients.

## Assurance disposition

The reviewed revision is a **net material strengthening** of recoverability,
authorisation separation, context protection and evidence preservation. No new
repository-level blocking security defect is identified.

The three residuals are intentionally classified as cross-boundary assurance obligations.
They do not prevent closure of the generated assessment trigger because they have named
owners and retest conditions.

This record closes RAHP toolkit issue **#26** for revision
`4fc64d711724cdbd23f94507b4e3743f99f00dcd`.

## Sources

- <https://github.com/OpenVTC/openvtc/compare/df623ec303a90e83ed60a2f84e63db3efb3f0cc1...4fc64d711724cdbd23f94507b4e3743f99f00dcd>
- <https://github.com/OpenVTC/openvtc/blob/4fc64d711724cdbd23f94507b4e3743f99f00dcd/docs/design/vta-authoritative-state.md>
