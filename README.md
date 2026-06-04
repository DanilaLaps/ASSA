# AppStoreSpy Niche Monitor

Automated monitor for mobile-game niches using AppStoreSpy data, deterministic Python scoring, optional OpenAI analysis, and Telegram alerts.

The first run stores a baseline and does not send regular alerts. If candidates are found, it writes an Initial Baseline Discovery Report; with `--notify` in production and Telegram credentials present, that report can be sent as a digest that does not start cooldown.

## What it does

- Collects AppStoreSpy `/play/apps/query` results with exactly one production API request per run.
- Uses a single Google Play query with `limit=10000`: `page=1`, `sort=-release_date`, `published=true`, `category_type=GAME`, recent releases, and `downloads_daily >= 500`.
- Does not send `country`, `language`, or `active_countries` in the AppStoreSpy payload.
- Stores raw responses so snapshots can be reprocessed later.
- Normalizes app records into a consistent schema.
- Classifies each app into a niche plus dimensions: market category, core mechanic, theme, meta, audience, and production complexity.
- Aggregates micro-niches by platform, niche, and dimensions; country is not a grouping dimension.
- Calculates growth, data quality, opportunity score, score components, and reason codes.
- Preserves `ALERT`, `WATCH`, `SINGLE_APP_WATCH`, `NEAR_MISS`, and `REJECT` candidates before applying cooldown and max-alert send limits.
- Saves markdown reports and can send Telegram alerts.
- Sends a Telegram completion summary when notifications are enabled, even if no regular ALERT messages were sent.
- Generates structured candidate-pack analysis with `TEST`, `WATCH`, or `AVOID` recommendations.
- Generates weekly feedback and calibration digests from history and manual labels.
- Supports a dry-run mode with sample data and no API keys.

## Repository layout

```text
src/appstorespy_niche_monitor/
  appstorespy_client.py   AppStoreSpy HTTP client with retries
  collector.py            Single-query AppStoreSpy collection
  cleaner.py              Raw app normalization
  niche_classifier.py     Rule-based niche and dimension classifier
  aggregator.py           Micro-niche aggregation
  trend_detector.py       Previous snapshot comparison
  data_quality.py         Trust score and quality reasons
  scorer.py               Opportunity score and score components
  alert_filter.py         Alert rules, cooldown, anti-spam
  feedback.py             Manual feedback labels
  weekly_digest.py        Weekly calibration report
  llm_report.py           Structured OpenAI/fallback analysis and markdown reports
  telegram_notify.py      Telegram delivery
  storage.py              Raw, processed, history, reports
  main.py                 CLI and pipeline orchestration
```

## Local dry-run

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode dry-run --snapshot-date 2026-06-04 --no-llm
```

On this machine, use the bundled Python executable if `python` is not on PATH:

```powershell
$env:PYTHONPATH="src"
& "C:\Users\Danila\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m appstorespy_niche_monitor --mode dry-run --snapshot-date 2026-06-04 --no-llm
```

## Tests

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests
```

## Weekly digest

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --weekly-digest
```

The digest summarizes feedback labels, false-positive reasons, top WATCH candidates, `other` niches, and suspicious concentration or paid-spike risks.

## Production secrets

Add these as GitHub Actions secrets:

- `APPSTORESPY_API_KEY`
- `OPENAI_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Do not commit real secret values. `.env.example` only documents variable names.

## Production run

```powershell
$env:APPSTORESPY_API_KEY="..."
$env:OPENAI_API_KEY="..."
$env:TELEGRAM_BOT_TOKEN="..."
$env:TELEGRAM_CHAT_ID="..."
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode production --notify
```

Production mode performs one AppStoreSpy request and asks for up to 10000 apps. If the API rejects a field or limit, update `config.yaml` and rerun; the collector does not retry with a different field list because v1.2 requires one query per run.
With `--notify`, Telegram receives a completion summary for every finished run. If regular ALERT candidates pass cooldown and send limits, alert messages are sent separately before the completion summary.

## Feedback migration

Canonical feedback storage is `data/feedback.jsonl`. Legacy `data/feedback.json` is used only for one-time migration and is not read during normal scoring after migration.

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --migrate-feedback
```

The migration command imports missing legacy records into JSONL, creates backup/state files, and exits without running collector, scoring, LLM, or Telegram.

## Feedback loop

Manual feedback is stored in `data/feedback.jsonl`. Valid verdicts are:

- `good`
- `maybe`
- `false_positive`
- `already_known`
- `too_complex`
- `too_competitive`
- `paid_spike`

Valid reasons are configured in `config.yaml`. Use this data weekly to tune thresholds, `niche_rules`, dimension rules, and anti-spam checks.

## Operational notes

- `config.yaml` is JSON-compatible YAML so the project can run without PyYAML.
- Runtime code uses only the Python standard library.
- OpenAI and Telegram calls are skipped unless env vars are present and the CLI enables notifications/reporting.
- Generated raw, processed, history, and report files are ignored by git except placeholder `.gitkeep` files.
