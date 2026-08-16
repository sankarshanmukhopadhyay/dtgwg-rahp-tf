---
title: DTG RAHP review record
nav_order: 70
---

# DTG RAHP review record

This directory is the durable review record for the **DTG Working Group instance** of RAHP.

Each material repository change detected by the DTG portfolio workflow can create an
`assessment-required` issue in this repository. Review artefacts produced in response
belong here, grouped by target repository and assessment identifier.

The portable RAHP engine does **not** depend on this directory. Another adopter may
clone the repository, supply its own YAML configuration, and ignore `instances/dtg/`
entirely.


## Assessment cycles

A source observation is not automatically a new review. v0.7.1 assigns a stable
`assessment_key` to repository work and allows issue-watch observations affecting the
same repository to become triggers on an existing open assessment. Each durable review
records an assessment ID, reviewed revision, findings and disposition. Deployment queue
state under `instances/dtg/state/assessment-queue.json` links generated GitHub work items
to those records.

Closing a generated queue issue means the named revision was reviewed and dispositioned;
it does **not** mean every upstream design discussion is finished. Later material source
changes start a new assessment cycle after the reviewed baseline.
