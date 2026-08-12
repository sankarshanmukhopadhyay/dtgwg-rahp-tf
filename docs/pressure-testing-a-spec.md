# Pressure-testing a specification

Specification pressure testing is a first-class RAHP workflow. The goal is to produce reproducible, traceable findings that can be re-run after a specification changes.

```mermaid
flowchart LR
  A[1. Select specification or change] --> B[2. Establish affected personas]
  B --> C[3. Test against existing risk hypotheses]
  C --> D[4. Identify new or changed harms]
  D --> E[5. Map controls, guardrails and evidence]
  E --> F[6. Determine specification vs other control plane]
  F --> G[7. Produce actionable recommendations]
  G --> H[8. Feed decisions back into RAHP]
  H -. new evidence .-> C
```

## 1. Select the target

Record repository/document, version, commit or date, review scope and the authority expected to act on findings.

## 2. Establish affected personas and scenarios

Select the participants who exercise power, receive decisions, bear harms, or represent edge cases. Trace their likely scenarios before reviewing individual clauses in isolation.

## 3. Reuse existing risks first

Search `data/risks.yaml` and linked scenarios/controls. Add a new risk only when the existing corpus cannot represent the failure mechanism without distorting its meaning.

## 4. Look for harmful inference and governance-invalid states

Ask what an implementation may infer beyond what was intended, what can remain cryptographically valid while authority is absent/revoked, and what assumptions collapse in adversarial or exceptional conditions.

## 5. Map controls and evidence

Connect each finding to relevant controls, guardrails, assurance tests and metrics. A recommendation with no plausible evidence path is difficult to assure.

## 6. Determine the control plane

Use the disposition model in [Governance boundaries](governance-boundaries.md). Do not force governance or runtime obligations into a technical specification merely because a risk is real.

## 7. Record the finding

Use this minimum record shape. The reusable starter file is `examples/pressure-test-template.yaml`:

```yaml
review:
  id: SR-001
  status: complete
  reviewed_on: YYYY-MM-DD
  target:
    repository: trustoverip/dtgwg-cred-spec
    version: Working Draft 01
    commit: <full-40-character-commit-sha>
  reviewed_against:
    rahp_version: v0.3-dev
  findings:
    - id: F-001
      title: Concise finding
      status: open
      severity: High
      primary_disposition: specification
      risks: [RK-SC02]
      controls: [CT-18]
      guardrails: [GR-01]
      assurance_tests: [AT-01]
      evidence:
        - source: spec/body.md#relevant-section
          observation: What the reviewed text permits, omits or contradicts.
      harm: Who can be harmed and how.
      recommendation: Action at the selected control plane.
      retest_when:
        - Observable condition that should trigger re-review.
```

A completed review is expected to pin the target to a full commit SHA and preserve enough evidence to explain why each canonical RAHP risk was triggered. Validate worked records with:

```bash
python3 tools/validate_pressure_tests.py
```

The validator checks target pinning, required finding metadata, controlled dispositions, summary counts, and that every referenced risk, control, guardrail and assurance test resolves in the canonical corpus.

## 8. Re-run after change

A review is not complete when findings are published. Preserve the target version/commit and resolution references so a future revision can determine which findings are closed, reopened or made obsolete.

## Evidence produced

A pressure test should leave behind enough evidence to answer: what was reviewed, against which RAHP version, which risks were triggered, which target version was assessed, what remains open, what change resolved a finding, and when retesting is required.
