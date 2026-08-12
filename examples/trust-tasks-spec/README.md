# Trust Tasks Framework pressure-test example

This directory records a **substantive RAHP pressure test of the Trust Tasks Framework**, using the same review-record model as the DTG Credential Specification example.

The purpose is not to argue that every safety concern belongs in `SPEC.md`. Trust Tasks intentionally separates document authenticity, authorization, transport, ceremony evidence, deployment policy and task-specific semantics. The pressure test preserves that architecture by routing each finding to the narrowest effective control plane.

## Review target

| Field | Value |
|---|---|
| Framework | Trust Tasks |
| Repository | `trustoverip/dtgwg-trust-tasks-tf` |
| Document | `SPEC.md` |
| Version | Editor's Draft 0.3, dated 2026-08-07 |
| Reviewed commit | `fbe196a8a17ba3f99d0657a64be5ac58621023a1` |
| Review date | 2026-08-12 |
| RAHP baseline | `v0.3-dev` corpus in this repository |
| Machine-readable record | [`pressure-test.yaml`](pressure-test.yaml) |

The attached source archive was checked against the current upstream editor's-draft state and the review is pinned to the full commit so that later changes can be re-tested rather than silently changing the target.

## Result at a glance

The review records **8 open findings**.

| Finding | Primary disposition | Severity | Core issue |
|---|---|---:|---|
| F-001 | Specification | Critical | State-changing tasks do not have mandatory same-recipient replay suppression |
| F-002 | Specification | High | Destructive/authority-bearing tasks can lack a bounded freshness window |
| F-003 | Companion specification | Critical | Authenticated issuer identity is not portable evidence of mandate/delegation |
| F-004 | Specification | High | Mutable draft semantics weaken reproducibility of retained evidence |
| F-005 | Operational policy | High | Runtime registry resolution can become an availability/integrity dependency |
| F-006 | Companion specification | High | Discovery does not negotiate a mutually executable security profile |
| F-007 | Governance | Critical | High-impact delegated execution has no minimum human-approval floor |
| F-008 | Specification | High | Supported decision-making/legal representation lacks a common binding point |

## What the pressure test found

### 1. Unique IDs are not enough when execution has side effects

The framework correctly requires every document to have a globally unique `id`, but same-recipient duplicate suppression is only a `SHOULD`. That is too weak for a framework that already classifies tasks as `mutating`, `destructive`, or `actsAsSubject`.

The RAHP recommendation is narrow: make replay suppression mandatory for those classes, define the lifetime of the replay record, and permit task-specific operation-level idempotency where a document identifier alone is not sufficient.

### 2. High-impact instructions need freshness, not only authenticity

`issuedAt` is recommended and `expiresAt` is optional. As a result, a cryptographically valid destructive instruction can remain actionable after the human intent, mandate or policy state that produced it has expired.

The pressure test does not recommend making every read-only query short-lived. It recommends coupling a bounded freshness rule to the task classes that can destroy state or exercise the subject's authority.

### 3. Identity and authority are correctly separated, but portable delegation is still missing

One of the strongest properties of Trust Tasks is that ceremony membership explicitly **does not confer authority**. The same separation needs a portable positive path: when a producer is an agent, representative or delegated executor, what evidence proves that it is allowed to ask for this particular action?

That belongs primarily in a companion authorization/delegation profile rather than in the generic envelope. The profile should cover principal, delegate, task scope, constraints, validity, revocation and onward delegation.

### 4. Draft mutability conflicts with long-lived evidentiary use

The framework allows producers to emit against `draft` task specifications while also allowing draft schema/prose to change without notice and some changes to occur in place. A retained task can therefore outlive the exact semantics under which it was produced.

The proposed fix is not to eliminate drafts. It is to make emitted draft documents able to pin the exact revision — by content digest, immutable revision URI or equivalent registry snapshot — so later verification is reproducible.

### 5. The registry needs an offline and failure-mode profile

The consumer algorithm is described in terms of resolving framework and payload schemas by content negotiation. The security section already recognizes the difference between dynamically resolved and build-pinned schemas.

RAHP turns that observation into an operational requirement: define authenticated caching, immutable digest pinning, offline verification and fail-closed behavior when a required artifact cannot be authenticated.

### 6. “We support the same task” does not yet mean “we can execute it together”

Discovery advertises Type URIs. It does not advertise the VID methods, proof suites, transport bindings or named authorization/freshness profiles that make the task executable.

A companion capability profile can close this gap without making Trust Tasks transport-specific. Its purpose is anti-downgrade interoperability, not another mandatory envelope field.

### 7. Safety classifications do not create a human-consent baseline

The distinction between `sideEffects` and `exposure` is excellent: a signing operation may mutate no local state while still exercising the subject's authority. But the classifications are intentionally descriptive, and the delegated-execution design confirms that policy enforcement is opt-in.

That means a destructive or `actsAsSubject` task can be conformingly automated with no human approval unless deployment governance says otherwise. RAHP routes this primarily to a **governance/safety profile**, including fail-safe treatment where effects cannot be rendered.

### 8. Supported decision-making needs a reusable representation path

The bilateral document model works for protocol transport, but it does not provide shared semantics for a guardian, attorney, supporter, co-decision-maker or secondary notification person. Leaving every task specification to invent this independently will create incompatible representations and exclusion.

The recommendation is a common companion representation/delegation profile plus a framework non-inference rule: issuer identity must not be treated as proof that no legally authorized or supported representative exists.

## Positive controls observed

A pressure test should record safeguards that already work, not only gaps. The reviewed draft has several important strengths:

- a proof binds document content to the issuer and, for non-bearer use, cryptographically binds the intended recipient;
- in-band and transport-derived identities are cross-checked rather than silently overridden;
- ceremony membership explicitly confers no authority;
- destructive side effects and `actsAsSubject` exposure are modeled as separate dimensions;
- dynamically obtained schemas are recognized as a security boundary;
- discovery is advisory rather than an authorization commitment;
- the delegated-execution design binds human approval to the exact payload and state being executed.

These controls are why several findings are routed outside the core framework rather than expressed as requests for additional envelope fields.

## Reproducing the review

```bash
pip install -r requirements.txt
python3 tools/validate.py
python3 tools/validate_pressure_tests.py
```

The pressure-test validator checks this record and the credential-spec review together. It verifies commit pinning, required finding metadata, dispositions, summary counts, and every RAHP risk/control/guardrail/assurance-test reference.

## Re-testing

Re-run SR-002 when the Trust Tasks framework changes any of the following:

- replay/idempotency requirements;
- freshness or expiry requirements;
- delegation/authorization profiles;
- draft version immutability rules;
- registry caching/pinning guidance;
- discovery/capability negotiation;
- delegated-execution consent policy; or
- supported representation semantics.

Do not overwrite the target commit while leaving the findings unchanged. Update each finding's state against the newly reviewed commit and retain the old commit as historical review evidence.

## Interpretation boundary

This review does **not** assert that the Trust Tasks core document format should absorb all governance, delegation, legal-capacity or consent semantics. In several places the current architecture is stronger precisely because it separates those concerns. RAHP's role is to make the remaining dependency explicit, assign it to a control plane, and give the project a testable condition for knowing when the risk has actually been addressed.
