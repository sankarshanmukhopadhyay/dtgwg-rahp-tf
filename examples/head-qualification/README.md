# v1.1.0 HEAD qualification

This directory records the 2026-08-17 qualification of the maintained RAHP v1.1.0 example estate against the **current default-branch HEAD** of every live target repository represented by those examples.

The qualification is deliberately additive. Existing worked examples remain pinned to the revision they actually assessed; this run records whether current HEAD changes that evidence and classifies the delta. Experimental CAWG branches/drafts remain pinned to their experiment revision rather than being rewritten as default-branch evidence.

## Result

- 11 live repositories checked.
- 8 canonical baselines were already at current HEAD.
- 3 repositories advanced: A2A, DTG Credential Spec and Trust Tasks.
- A2A advanced by one non-material documentation-link commit outside assessed source paths.
- Credential Spec advanced by one material-positive commit requiring the VWC edge digest; `SEC-CR-009` is resolved.
- Trust Tasks advanced by 27 commits and materially strengthened duplicate-execution prevention, authorization semantics, authority re-evaluation, task control/corrigibility, transport proof profiles, citation integrity and payload validation.
- No new open finding or portable-catalogue pattern was required.

The machine-readable record is [`qualification.yaml`](qualification.yaml). The human-readable interpretation is published in [`docs/head-qualification.md`](../../docs/head-qualification.md).

## Interpretation rule

A `resolved` classification means the cited HEAD change closes the **specific finding as written**. It does not imply the broader risk family is impossible. `weakened` means the risk still exists but the new source state materially narrows it. `unchanged` means no source change was found that materially changes the finding.
