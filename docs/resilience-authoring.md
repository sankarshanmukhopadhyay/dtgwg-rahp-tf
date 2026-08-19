---
layout: default
title: "Authoring resilience rules"
nav_order: 9
has_toc: true
parent: Implement RAHP
---
# Authoring DRARM rules and detectors

DRARM uses a strict separation between **risk semantics** and **evidence discovery**.

## Risk record

A risk in `method/resilience/catalogue.yaml` must remain implementation- and ecosystem-neutral. Required fields are:

```yaml
- id: RLA-XXX
  title: Reusable failure pattern
  category: amplification-class
  severity: High
  applies_to: [implementation, specification]
  trigger: Observable condition that activates the pattern.
  failure: What is amplified or lost.
  required_controls: [portable-control-name]
  evidence_required: [machine-or-human-verifiable-artifact]
  upstream_control_plane: implementation-and-specification
  retest_when: Observable change that invalidates the prior conclusion.
  detectors: [evidence-adapter-id]
```

A rule is not ready if it only says that a practice is "bad". It must state what can be tested and what evidence should exist.

## Detector record

A detector is a conservative static evidence adapter. It may use:

- `any`: one of these source/specification signals must appear;
- `context_any`: an additional context signal must appear in the same file;
- `control_any`: signals that can satisfy a preliminary control check;
- `globs`: optional file selection;
- `mode`: how RAHP treats the signal.

Detector modes are:

- `finding_on_match`: the matched construct is itself a hazardous state;
- `review_on_match`: the construct is legitimate only if a declared control is evidenced;
- `evidence_gap`: presence of the feature requires explicit assurance evidence that static inspection cannot establish.

Do not use `finding_on_match` merely because a preferred library or keyword is absent.

## Validation

```bash
python3 tools/validate_resilience.py
python3 -m unittest tests.test_resilience_assess
```

The repository-wide `validate` and Pages workflows run DRARM validation automatically.
