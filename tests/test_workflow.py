import unittest
from pathlib import Path


class WorkflowTests(unittest.TestCase):
    def test_production_monitor_requires_openai_key_before_collector(self):
        workflow = Path(".github/workflows/monitor.yml").read_text(encoding="utf-8")

        self.assertIn('if [ "$MODE" = "production" ] && [ -z "$OPENAI_API_KEY" ]; then', workflow)
        self.assertIn("OPENAI_API_KEY secret is required for production AI baseline review.", workflow)
        self.assertLess(
            workflow.index("OPENAI_API_KEY secret is required for production AI baseline review."),
            workflow.index('python -m appstorespy_niche_monitor "${ARGS[@]}"'),
        )


if __name__ == "__main__":
    unittest.main()
