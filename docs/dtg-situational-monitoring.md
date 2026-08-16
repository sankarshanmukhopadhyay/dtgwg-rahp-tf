---
layout: default
title: "DTG situational monitoring"
nav_order: 5
has_toc: true
parent: Deployments & examples
---
# DTG situational monitoring

> **v0.8 note:** monitoring events feed the language-neutral observation/trigger/assessment lifecycle. Repeated events should coalesce into stable assessment work items; they are not themselves findings or durable review records.
The DTG deployment uses **three complementary signals** to decide when existing RAHP evidence may need review. None of them automatically turns upstream discussion or source movement into a finding.

## 1. Portfolio membership

`tools/dtg_portfolio.py` resolves the current repository perimeter from the DTG Portfolio Monitor and relevant forks. This answers **which repositories belong in the DTG assurance perimeter?**

## 2. Repository source drift

For each resolved target, the DTG monitor records the observed revision and compares material-path changes. A material source change can create an `assessment-required` queue issue. This answers **what normative, draft, schema, workflow or materially relevant documentation changed?**

## 3. Selected upstream issue drift

`instances/dtg/watch/issues.yaml` is a deliberately small allow-list of upstream issues whose discussion can materially change assumptions in existing RAHP reviews before specification text is merged.

The curated DTG issue-watch set currently focuses on:

- Trust Tasks identity/proof versus authorization;
- cancellation, suspension, supersession and other corrigibility semantics;
- execution-time validity and revocable authority;
- duplicate-execution/replay protection;
- transport-security conditions for omitting in-band proof;
- Trust Tasks × Credential Specification `taskContext` composition;
- Credential Specification ZKP identity linkages;
- W3C Data Integrity/multibase alignment; and
- unresolved credential graph semantics.

`tools/issue_watch.py` is deployment-neutral. Each selected issue declares its repository, issue number, theme and affected RAHP reviews. The first observation establishes a baseline silently. A later update emits an `assessment-required` event labelled `dtg-instance`.

{: .warning }
A GitHub issue is **situational evidence, not normative authority**. Reviewers inspect the discussion and any resulting source changes before changing a RAHP finding, risk or conclusion.

## Why DTG should watch issues

DTG specification work is distributed across multiple task-force repositories and much of the architecture is negotiated before text lands. Repository monitoring alone therefore tells RAHP when the *document* changed but can miss when an unresolved cross-specification decision has changed the assumptions behind an assessment.

Watching every issue would create noise and make RAHP track project management rather than assurance. The DTG policy is therefore:

> **Watch only issues whose resolution could change normative semantics, authority, lifecycle, privacy/security posture, cross-specification composition or the interpretation of an existing RAHP finding.**

Routine editorial issues, implementation chores and ordinary backlog items remain outside the watch list.

## Discussions

Some DTG work, particularly ZKP task-force design, also happens in GitHub Discussions. Current issue monitoring does not yet treat Discussions as a monitored source type. They should be added selectively if a discussion is carrying architecture or governance decisions that would otherwise escape the repository and issue channels; the same early-warning/non-normative rule should apply.
