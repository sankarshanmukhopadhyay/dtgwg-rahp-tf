---
layout: default
title: "Review modes"
nav_order: 7
has_toc: true
---
# Review modes

RAHP exposes three coordinated review modes through `tools/review.py`.

## 1. RAHP pressure test

Use the RAHP lens when the primary question is:

> What harms, governance failures, assurance gaps, affected-party consequences, or trust-system weaknesses remain?

```bash
python3 tools/review.py init \
  --mode rahp \
  --slug example-spec \
  --title "Example Specification" \
  --repository owner/repo \
  --version "Draft 0.1" \
  --commit <40-character-sha>
```

The canonical record is `examples/<slug>/pressure-test.yaml`. Its human-readable projection is the sibling `README.md`.

## 2. Security-hardening review

Use the security lens when the primary question is:

> How can an adversary, compromised component, malicious participant, or unsafe implementation violate a security property?

```bash
python3 tools/review.py init \
  --mode security \
  --slug example-spec \
  --title "Example Specification" \
  --repository owner/repo \
  --version "Draft 0.1" \
  --commit <40-character-sha>
```

The canonical record is `examples/security-hardening/<slug>/findings.yaml`. Its Markdown report is `SECURITY_REVIEW.md`.

## 3. Combined review

Combined mode scaffolds both canonical records and a third linkage record:

```bash
python3 tools/review.py init \
  --mode combined \
  --slug example-spec \
  --title "Example Specification" \
  --repository owner/repo \
  --version "Draft 0.1" \
  --commit <40-character-sha>
```

This produces:

```text
examples/example-spec/
  pressure-test.yaml
  README.md

examples/security-hardening/example-spec/
  findings.yaml
  SECURITY_REVIEW.md

examples/combined/example-spec/
  combined-review.yaml
  COMBINED_REVIEW.md
```

The combined report is **not a third independent test**. It synthesizes the two lenses, showing where RAHP and security findings share canonical risks, controls, guardrails, or assurance tests, and which findings remain specific to one lens.

## Analysis is reviewer work

`tools/review.py` scaffolds, renders, validates, and synthesizes. It does not claim to statically scan a specification and discover defensible findings by itself. A human or AI-assisted reviewer must inspect the target and populate the canonical YAML records with evidence.

An `in-progress` scaffold may contain zero findings without breaking CI. Once the review status moves beyond `in-progress`, findings are required and the ordinary validators enforce their structure and references.

## Orchestration commands

Render the selected review mode:

```bash
python3 tools/review.py render --mode combined
```

Validate it:

```bash
python3 tools/review.py validate --mode combined
```

Render and validate in one command:

```bash
python3 tools/review.py run --mode combined
```

Inspect discovered review records:

```bash
python3 tools/review.py status
```

The lower-level renderer and validator scripts remain available for automation and CI.
