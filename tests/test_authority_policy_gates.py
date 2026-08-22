import unittest
from datetime import datetime, timezone

from tools.authority import evaluate_authority
from tools.policy_gate import evaluate_policy


AUTHORITY = {
    "authority_id": "A1",
    "subject": "actor",
    "status": "active",
    "grants": [
        {"action": "assess", "scope": {"kind": "assessment", "id": "alpha"}},
        {"action": "observe", "scope": {"kind": "global", "id": "*"}},
    ],
}


class AuthorityTests(unittest.TestCase):
    def test_declared_scope_authorizes(self):
        result = evaluate_authority(AUTHORITY, subject="actor", action="assess", scope_kind="assessment", scope_id="alpha")
        self.assertTrue(result["authorized"])

    def test_undeclared_action_denied(self):
        result = evaluate_authority(AUTHORITY, subject="actor", action="accept-risk", scope_kind="assessment", scope_id="alpha")
        self.assertFalse(result["authorized"])

    def test_revoked_authority_denied(self):
        grant = dict(AUTHORITY, status="revoked")
        result = evaluate_authority(grant, subject="actor", action="assess", scope_kind="assessment", scope_id="alpha")
        self.assertFalse(result["authorized"])

    def test_global_scope_matches(self):
        result = evaluate_authority(AUTHORITY, subject="actor", action="observe", scope_kind="target", scope_id="anything")
        self.assertTrue(result["authorized"])

    def test_expired_time_denied(self):
        grant = dict(AUTHORITY, valid_until="2026-01-01T00:00:00Z")
        result = evaluate_authority(
            grant,
            subject="actor",
            action="assess",
            scope_kind="assessment",
            scope_id="alpha",
            at=datetime(2026, 8, 22, tzinfo=timezone.utc),
        )
        self.assertFalse(result["authorized"])


class PolicyGateTests(unittest.TestCase):
    def setUp(self):
        self.policy = {
            "policy_id": "P1",
            "rules": [
                {"id": "r1", "effect": "require", "conditions": [{"path": "freshness", "operator": "equals", "value": "current"}]},
                {"id": "r2", "effect": "deny", "conditions": [{"path": "critical", "operator": "not-equals", "value": 0}]},
            ],
        }

    def test_pass(self):
        self.assertEqual(evaluate_policy(self.policy, {"freshness": "current", "critical": 0})["outcome"], "PASS")

    def test_fail(self):
        self.assertEqual(evaluate_policy(self.policy, {"freshness": "current", "critical": 1})["outcome"], "FAIL")

    def test_missing_input_is_indeterminate(self):
        self.assertEqual(evaluate_policy(self.policy, {"critical": 0})["outcome"], "INDETERMINATE")

    def test_fail_dominates_indeterminate(self):
        self.assertEqual(evaluate_policy(self.policy, {"critical": 1})["outcome"], "FAIL")


if __name__ == "__main__":
    unittest.main()
