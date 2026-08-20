---
layout: default
title: "Assurance evaluation"
nav_order: 7
has_toc: true
parent: Run assessments
---
# Evidence-driven assurance evaluation

RAHP v1.2 separates **signals** from **assurance conclusions**. A detector, reviewer, static analyser, scenario corpus, or resilience rule may identify a risk signal, but that signal does not become a finding until relevant control evidence, assurance evidence, contradictory evidence, and target context have been evaluated.

The canonical residual states are `assured`, `controlled`, `finding`, `assurance-gap`, `review-required`, `not-assessed`, and `not-applicable`. These states are intentionally richer than pass/fail. In particular, **zero findings is not a pass** when assurance gaps, review-required propositions, or unassessed propositions remain.

`method/schema/assurance-evaluation.schema.json` defines the portable object. Each evaluation contains a proposition, detector/reviewer signals, credited control evidence, assurance-test evidence, and a residual conclusion with reasoning and any missing evidence obligations.

Evidence references are typed by context (`normative-spec`, `implementation`, `test`, `deployment`, `governance`, `operational-evidence`, `build-infrastructure`, `documentation`, `example`, `historical`) and authority (`normative`, `authoritative`, `supporting`, `informative`, `incidental`). This prevents incidental repository text from being treated as equivalent to normative or implementation evidence.

## Conservative reference inference

The Python and TypeScript references expose a conservative inference helper. It is not a universal risk-scoring algorithm. It demonstrates the invariant that uncertainty must not be converted into assurance:

- risk + absent control or failed assurance evidence → `finding`;
- risk + present control + passing assurance evidence → `controlled`;
- risk + present control + incomplete assurance evidence → `assurance-gap`;
- risk without enough control evidence → `review-required`;
- evidenced control + passing test without a risk signal → `assured`;
- otherwise → `not-assessed`.

```bash
python3 tools/assurance_cli.py validate-evaluation evaluation.json
python3 tools/assurance_cli.py summarize result.json
```
