import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "validate_persona_quality", ROOT / "tools" / "validate_persona_quality.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PersonaQualityTests(unittest.TestCase):
    def test_repository_personas_satisfy_quality_profiles(self):
        self.assertEqual([], MODULE.validate(ROOT))

    def test_thin_portable_persona_fails(self):
        # Validate the rules themselves by reproducing the relevant minimums against
        # a deliberately anaemic record rather than relying only on repository state.
        config = MODULE.load_yaml(ROOT / "method" / "persona-quality.yaml")
        profile = config["profiles"]["portable_role"]
        thin = {"type": "portable_role", "context": {}, "goals": ["one"]}
        self.assertGreater(profile["minimum_items"]["goals"], len(thin["goals"]))
        self.assertIn("power_and_decisions", profile["required_fields"])
        self.assertIn("harms_and_externalities", profile["required_fields"])
        self.assertIn("pressure_test_situations", profile["required_fields"])


if __name__ == "__main__":
    unittest.main()
