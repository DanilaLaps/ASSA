# Build MVP prompt

Implement or improve the AppStoreSpy Niche Monitor without changing secret handling.

Requirements:

- Keep the first run baseline-only.
- Keep scoring deterministic and explainable.
- Include `data_quality_score`, `reason_codes`, and `score_components` in every alert candidate.
- Keep Telegram anti-spam limits and cooldowns intact.
- Add tests for classifier, scorer, trend detector, data quality, feedback, and alert filter changes.
