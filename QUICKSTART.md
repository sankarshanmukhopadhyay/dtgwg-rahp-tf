# RAHP Quickstart

Use this path when you want useful output before learning every artefact type.

1. **Choose a target.** Record the specification/system, version or commit, and review scope.
2. **Choose 3–6 personas.** Start with who has decision power, who bears harm, and edge cases.
3. **Reuse existing risks.** Search `data/risks.yaml` before inventing new hypotheses.
4. **Pressure-test 5–15 hypotheses.** Ask what fails, who is harmed, what harmful inference remains possible, and what can remain technically valid while governance-invalid.
5. **Map controls only where needed.** Use guardrails for hard stops and assurance tests for evidence.
6. **Route each finding.** Decide the correct control plane using `docs/governance-boundaries.md`.
7. **Publish recommendations.** Make each action traceable to evidence and status.
8. **Validate and repeat.** Re-run the review when the target specification changes.

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/build.py
```

For the complete process, see [ADOPTION.md](ADOPTION.md) and [docs/pressure-testing-a-spec.md](docs/pressure-testing-a-spec.md).
