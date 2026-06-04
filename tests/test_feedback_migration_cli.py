import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.main import main


class FeedbackMigrationCliTests(unittest.TestCase):
    def test_migrate_feedback_cli_exits_without_pipeline(self):
        config, _ = load_config("config.yaml")
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "data").mkdir()
            (root / "data" / "feedback.json").write_text(
                json.dumps(
                    [
                        {
                            "created_at": "2026-06-04T12:00:00Z",
                            "dedupe_key": "abc",
                            "normalized_niche": "sort_puzzle",
                            "verdict": "good",
                            "reason": "manual validation",
                        }
                    ]
                ),
                encoding="utf-8",
            )
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = main(["--config", str(config_path), "--migrate-feedback"])

            self.assertEqual(exit_code, 0)
            self.assertTrue((root / "data" / "feedback.jsonl").exists())
            self.assertFalse((root / "data" / "raw").exists())
            self.assertIn("migrated_count", output.getvalue())


if __name__ == "__main__":
    unittest.main()
