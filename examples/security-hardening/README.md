# DTG coordinated security-hardening reviews

This example set applies the RAHP security-hardening workflow to two adjacent DTG specifications and then reviews their composition as a separate attack surface.

| Review | Target | Purpose |
|---|---|---|
| [Trust Tasks](trust-tasks/SECURITY_REVIEW.md) | `trustoverip/dtgwg-trust-tasks-tf` | Adversarial review of task documents, transports, registry resolution, ceremonies and delegated execution. |
| [DTG Core Credentials](credential-spec/SECURITY_REVIEW.md) | `trustoverip/dtgwg-cred-spec` | Adversarial review of credential types, status, proof, privacy and governance-dependent semantics. |
| [Cross-spec composition](cross-spec/COMPOSITION_THREAT_MODEL.md) | Trust Tasks + DTG Credentials | Failure modes that remain reachable even when both component specifications are individually followed. |

The central rule is that **successful component verification is not the same as authorized end-to-end action**. The composition review therefore treats intent, execution, ceremony completion, durable credentials and registry state as distinct trust boundaries.

The canonical records are the sibling `findings.yaml` files. Generated Markdown should be refreshed with:

```bash
python3 tools/render_security_reviews.py
python3 tools/validate_security_reviews.py
```
