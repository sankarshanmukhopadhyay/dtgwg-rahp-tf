import importlib.util
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, relpath):
    spec = importlib.util.spec_from_file_location(name, ROOT / relpath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class MonitorHeadResolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dtg = load_module("dtg_portfolio_test", "tools/dtg_portfolio.py")
        cls.generic = load_module("instance_monitor_test", "tools/instance_monitor.py")

    @staticmethod
    def http_error(code):
        return urllib.error.HTTPError(
            url="https://api.github.test/repos/example/empty/commits/main",
            code=code,
            msg="test",
            hdrs=None,
            fp=None,
        )

    def test_dtg_empty_repository_is_not_fatal(self):
        with patch.object(self.dtg, "api_json", side_effect=self.http_error(409)):
            self.assertIsNone(self.dtg.head_sha("example/empty", "main"))

    def test_generic_empty_repository_is_not_fatal(self):
        with patch.object(self.generic, "api_json", side_effect=self.http_error(409)):
            self.assertIsNone(self.generic.head_sha("example/empty", "main"))

    def test_dtg_other_http_errors_are_not_suppressed(self):
        with patch.object(self.dtg, "api_json", side_effect=self.http_error(403)):
            with self.assertRaises(urllib.error.HTTPError):
                self.dtg.head_sha("example/private", "main")

    def test_generic_other_http_errors_are_not_suppressed(self):
        with patch.object(self.generic, "api_json", side_effect=self.http_error(500)):
            with self.assertRaises(urllib.error.HTTPError):
                self.generic.head_sha("example/down", "main")


if __name__ == "__main__":
    unittest.main()
