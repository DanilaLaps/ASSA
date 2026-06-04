import json
import tempfile
import unittest
from pathlib import Path

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.feedback import load_feedback, migrate_legacy_feedback_to_jsonl_once


class FeedbackMigrationTests(unittest.TestCase):
    def test_migrates_legacy_json_to_jsonl_once(self):
        config, _ = load_config("config.yaml")
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir)
            (config_dir / "data").mkdir()
            legacy = config_dir / "data" / "feedback.json"
            legacy.write_text(
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

            result = migrate_legacy_feedback_to_jsonl_once(config, config_dir)
            second = migrate_legacy_feedback_to_jsonl_once(config, config_dir)
            records = load_feedback(config, config_dir)

            self.assertEqual(result["migrated_count"], 1)
            self.assertEqual(second["migrated_count"], 0)
            self.assertEqual(second["skipped_duplicates_count"], 1)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["source_format"], "legacy_json")
            self.assertTrue((config_dir / "data" / "feedback_migration_state.json").exists())
            self.assertTrue(list((config_dir / "data").glob("feedback.migrated.*.json")))

    def test_invalid_legacy_json_does_not_fail_when_configured(self):
        config, _ = load_config("config.yaml")
        with tempfile.TemporaryDirectory() as tmpdir:
            config_dir = Path(tmpdir)
            (config_dir / "data").mkdir()
            (config_dir / "data" / "feedback.json").write_text("{bad", encoding="utf-8")

            result = migrate_legacy_feedback_to_jsonl_once(config, config_dir)

            self.assertEqual(result["migration"], "skipped")
            self.assertIn("warning", result)


if __name__ == "__main__":
    unittest.main()
