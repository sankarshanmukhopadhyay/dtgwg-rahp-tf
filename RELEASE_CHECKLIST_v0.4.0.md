---
layout: default
title: "RAHP v0.4.0 Release Checklist"
nav_order: 23
---
# RAHP Toolkit v0.4.0 release checklist

## Before tagging

- [ ] Confirm the GitHub Actions `validate` workflow is green on `main`.
- [ ] Confirm the GitHub Pages workflow builds and deploys successfully.
- [ ] Confirm Corpus Source Status may show review-required warnings but no operational failure.
- [ ] Review [`docs/releases/v0.4.0.md`](docs/releases/v0.4.0.md).
- [ ] Confirm `data/instance.yaml` reports `toolkit_version: v0.4.0`.
- [ ] Confirm `RP-001` is still `proposed` unless the Task Force has explicitly ratified it.
- [ ] Confirm the five monitoring contracts are still `pilot_proposed` unless a practitioner trial has activated them.
- [ ] Do not rewrite historical review records from `v0.3-dev`; their recorded version is provenance.

## Local validation

```bash
pip install -r requirements.txt
python3 tools/validate_v04_method.py
python3 tools/validate.py
python3 tools/validate_scenario_corpora.py
python3 tools/corpus_status.py --offline
python3 tools/validate_pressure_tests.py
python3 tools/validate_security_reviews.py
python3 tools/validate_combined_reviews.py
python3 tools/build.py
python3 tools/validate_reference_links.py
```

## Git tag and GitHub release

Recommended tag:

```text
v0.4.0
```

Recommended release title:

```text
RAHP Toolkit v0.4.0 — Governed and Observable Assurance
```

Use `docs/releases/v0.4.0.md` as the substantive GitHub Release description.

## After tagging

- [ ] Verify the tag resolves to the intended `main` commit.
- [ ] Verify GitHub Pages displays the v0.4 release notes, operational assurance guide,
      rule profile, evidence artefacts, non-human actor taxonomy, and delegation schema.
- [ ] Open/track Task Force decisions for `RP-001`, the five pilot monitoring contracts,
      and the 87 canonical standards-status assignments.
- [ ] Begin a practitioner trial that can populate real evidence artefact URI/hash/time fields.
- [ ] Begin the v0.5 portability proof with a second RAHP instance.
