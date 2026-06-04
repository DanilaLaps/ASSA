# AGENTS.md

## Project goal

Build an automated AppStoreSpy niche monitor for mobile games.

## Development rules

- Never commit real API keys or tokens.
- Read secrets only from environment variables.
- Production collection must make exactly one AppStoreSpy `/play/apps/query` request per run.
- Do not add `country`, `language`, `active_countries`, or pagination to the production AppStoreSpy query.
- Keep scoring deterministic and explainable.
- LLM analysis must receive alert candidates only, not raw full datasets.
- LLM and Telegram text must describe the data as one AppStoreSpy query without country/language filters.
- First run without history must not send alerts.
- Every alert must include `reason_codes` and `score_components`.
- Every alert must include `data_quality_score`.
- Every alert must include classification dimensions: `market_category`, `core_mechanic`, `theme`, `meta`, `audience`, `production_complexity`.
- Never send more than `max_alerts_per_run` alerts.
- Store manual feedback labels and use them to improve scoring.
- Add or update tests for classifier, scorer, trend detector, data quality, feedback, and alert filter changes.

## Review guidelines

- Flag any secret leakage as P0.
- Flag workflows with excessive permissions as P1.
- Flag changes that can spam Telegram as P1.
- Flag silent data loss in history or snapshots as P1.
- Flag scoring changes without tests as P1.
