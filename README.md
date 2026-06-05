# AppStoreSpy Niche Monitor

Automated monitor for fresh Google Play game niches using one AppStoreSpy query, deterministic Python scoring, optional OpenAI analysis, and Telegram reporting.

The project is intentionally conservative. It collects one production `/play/apps/query` response, turns apps into explainable niche clusters, builds an internal candidate funnel, and sends only strict `SENDABLE_ALERT` items to Telegram. The first run without compatible history stores a baseline and does not send regular alerts.

## Core Guarantees

- Production collection makes exactly one AppStoreSpy `/play/apps/query` request per run.
- Production collection does not add `country`, `language`, `active_countries`, or pagination.
- The source scope in reports and Telegram is always one AppStoreSpy query without country/language filters.
- Scoring, filtering, cooldown, dedupe, and sendable selection are deterministic Python logic.
- LLM analysis receives only final sendable alert candidates, never the raw full dataset.
- LLM recommendations are commentary only; they do not select or send alerts.
- Telegram regular alerts are limited by `alert_limits.max_alerts_per_run`.
- `ALERT` means an internal qualified candidate. `SENDABLE_ALERT` means it passed the stricter Telegram shortlist.
- Separate TEST Telegram messages are disabled.

## What It Does

- Collects fresh Google Play games from AppStoreSpy using `limit=10000`, `page=1`, `sort=-release_date`, recent releases, `published=true`, `category_type=GAME`, and `downloads_daily >= 500`.
- Stores raw, processed, history, and report artifacts for later debugging and reprocessing.
- Normalizes AppStoreSpy app rows into a stable schema.
- Classifies apps into `niche`, `market_category`, `core_mechanic`, `theme`, `meta`, `audience`, and `production_complexity`.
- Aggregates apps into multiple explainable market-signal groupings.
- Computes data quality, trend confidence, team fit, opportunity score, score components, reason codes, and risk tags.
- Produces `ALERT`, `WATCH`, `SINGLE_APP_WATCH`, `NEAR_MISS`, and `REJECT` candidates.
- Applies sendable hard filters, market-signal dedupe, cooldown, per-niche/per-mechanic/per-signal limits, and max-alert budget.
- Writes daily reports, alert funnel diagnostics, sendable reports, no-sendable diagnostics, rejected/watch/near-miss reports, and unknown-pattern diagnostics.
- Sends Telegram regular alerts only for final `SENDABLE_ALERT` candidates.
- Sends a Telegram completion summary for production notification runs, even when there are zero sendable alerts.
- Generates weekly feedback/calibration digests from history and manual labels.
- Supports dry-run mode with sample data and no API keys.

## Unknown/New-Pattern Semantics

There are two levels of unknown detection.

App-level `is_unknown_or_new_pattern` is intentionally narrow. An app is unknown only when both its primary niche and primary mechanic are unclassified or very low confidence. Valid short keyword matches such as `match`, `arrow`, `run`, or `level` must not mark an app unknown by themselves.

Cluster-level unknown diagnostics are ratio-based:

- `unknown_app_count`
- `unknown_app_share`
- `unknown_installs_share`
- `top_app_unknown`
- `top3_unknown_app_share`
- `mixed_unknown_cluster`
- `unknown_dominant_cluster`
- `unknown_pattern_blocker_active`
- `cluster_pattern_status`
- `unknown_or_new_pattern_cluster`

`mixed_unknown_cluster` means at least one app is unknown. It is a soft risk tag only.

`unknown_dominant_cluster` means unknown apps dominate the cluster by app count, installs, or top-app leadership. It is stronger, but it does not automatically block every candidate.

`unknown_pattern_blocker_active` is the hard/near-hard blocker. It is active only when the cluster is unknown-dominant and average classification confidence is below `0.70`.

If a run shows every summary as unknown-dominant, inspect app-level classification first. It usually means the classifier is over-marking apps before aggregation.

## Alert Funnel Terms

- `ALERT candidates`: all candidates that passed base alert thresholds.
- `SENDABLE alerts`: final regular Telegram shortlist after sendable score, hard filters, dedupe, cooldown, and alert limits.
- `WATCH candidates`: useful tracking items, not regular Telegram alerts.
- `NEAR_MISS candidates`: close to alert thresholds, useful for tuning.
- `Rejected candidates`: candidates that failed enough checks to be non-actionable.
- `Duplicate market signals suppressed`: candidates that overlapped another cleaner/stronger market signal.
- `Cooldown blocked`: otherwise sendable candidates blocked because the niche/signal was sent too recently.
- `Limit blocked`: otherwise sendable candidates blocked by per-run/per-niche/per-mechanic/per-signal caps.

If `SENDABLE alerts` is `0`, OpenAI is skipped and LLM status becomes `source=fallback, fallback_reason=no_sendable_alerts`. That is expected: there is no final alert pack for OpenAI to review.

## Sendable Calibration

The normal sendable gate remains strict. A candidate must pass deterministic scoring, hard filters, dedupe, cooldown, and send limits before it becomes a regular Telegram alert.

The optional calibration layer exists for the case where the base `ALERT` longlist has candidates but the strict shortlist is empty. When `sendable_alert_calibration.allow_promote_best_alert_if_no_sendable=true`, the pipeline may promote exactly one clean `ALERT` candidate if:

- this is not a baseline-only run
- normal sendable count is zero
- the candidate has `hard_blockers_count == 0`
- the candidate passes the configured `promote_*` thresholds
- the candidate is not a severe paid spike, duplicate market signal, cooldown block, unknown-pattern blocker, or low-organic-confidence signal
- promotion still respects `alert_limits.max_alerts_per_run`

Promoted alerts are marked with:

- `calibrated_promotion=true`
- `promoted_best_clean_alert_when_no_sendable`
- `no_hard_blockers`
- `closest_to_sendable_thresholds`

If promotion is disabled and `enable_manual_review_digest_when_no_sendable=true`, the run writes a manual-review digest instead. Manual-review items are not `SENDABLE_ALERT`, are not regular Telegram alerts, and are not written to `sent_alerts.json`.

## Diagnostics

Every candidate now carries:

- `alert_strength`: `WEAK_ALERT`, `MEDIUM_ALERT`, `STRONG_ALERT`, or `NONE`
- `hard_blockers`
- `soft_blockers`
- `hard_blockers_count`
- `soft_blockers_count`
- `first_blocking_failure`
- `sendable_threshold_margins`

When `baseline_only=false`, `ALERT candidates > 0`, and `SENDABLE alerts == 0`, the pipeline writes:

- `data/processed/<date>_no_sendable_diagnostics.json`
- `reports/daily/<date>_no_sendable_diagnostics.md`

The completion summary includes `SINGLE_APP_WATCH`, pre/post market-signal dedupe status counts, strong alert count, sendable hard-filter pass/fail counts, calibrated promotions, and top first blockers.

## Repository Layout

```text
src/appstorespy_niche_monitor/
  appstorespy_client.py   AppStoreSpy HTTP client
  collector.py            Single-query AppStoreSpy collection
  cleaner.py              Raw app normalization
  niche_classifier.py     Rule-based niche and dimension classifier
  aggregator.py           Multi-key cluster aggregation and unknown diagnostics
  trend_detector.py       Previous snapshot comparison
  data_quality.py         Trust score and quality reasons
  scorer.py               Opportunity score, components, reason codes, risk tags
  candidate_generator.py  Candidate statuses and broad new-pattern reason logic
  alert_ranker.py         Sendable score, hard filters, margins, organic confidence
  dedupe.py               Stable IDs and duplicate market-signal suppression
  alert_filter.py         Cooldown, send limits, final Telegram shortlist
  feedback.py             Manual feedback labels and migration
  weekly_digest.py        Weekly calibration report
  llm_report.py           OpenAI/fallback candidate-pack analysis
  telegram_notify.py      Telegram formatting and delivery
  report_writer.py        Daily markdown diagnostics
  storage.py              Raw, processed, history, report persistence
  main.py                 CLI and pipeline orchestration
```

Important project files:

- `config.yaml`: JSON-compatible YAML configuration.
- `PROJECT_DOCUMENTATION.md`: detailed human/AI project map.
- `AGENTS.md`: hard development and review rules.
- `tests/`: `unittest` regression suite.
- `data/processed/`: generated processed artifacts.
- `reports/daily/`: generated daily reports.

## Local Dry Run

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode dry-run --snapshot-date 2026-06-04 --no-llm
```

On this machine, `python` may not be on PATH. If available, use the bundled Codex runtime:

```powershell
$env:PYTHONPATH="src"
& "C:\Users\Danila\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m appstorespy_niche_monitor --mode dry-run --snapshot-date 2026-06-04 --no-llm
```

## Production Run

```powershell
$env:APPSTORESPY_API_KEY="..."
$env:OPENAI_API_KEY="..."
$env:TELEGRAM_BOT_TOKEN="..."
$env:TELEGRAM_CHAT_ID="..."
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode production --notify
```

Production mode performs one AppStoreSpy request. If AppStoreSpy rejects a field or limit, update `config.yaml`; the collector must not retry with pagination or country/language variants.

With `--notify`, Telegram sends regular alert messages only for final `SENDABLE_ALERT` candidates, then sends a completion summary.

## Tests

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests
```

The test suite covers collection invariants, classification, aggregation, trend detection, data quality, scoring, sendable ranking, dedupe, LLM input, Telegram formatting, feedback, first-run behavior, reports, and workflow checks.

## Weekly Digest

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --weekly-digest
```

The digest summarizes manual feedback labels, false-positive reasons, top WATCH candidates, `other` niches, suspicious concentration, paid-spike risks, and calibration recommendations.

## Feedback Migration

Canonical feedback storage is `data/feedback.jsonl`. Legacy `data/feedback.json` is used only for one-time migration and is not read during normal scoring after migration.

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --migrate-feedback
```

The migration command imports missing legacy records into JSONL, creates backup/state files, and exits without running collector, scoring, LLM, or Telegram.

## Feedback Loop

Manual feedback is stored in `data/feedback.jsonl`. Valid verdicts are:

- `good`
- `maybe`
- `false_positive`
- `already_known`
- `too_complex`
- `too_competitive`
- `paid_spike`

Valid reasons are configured in `config.yaml`. Use feedback weekly to tune thresholds, `niche_rules`, `dimension_rules`, risk penalties, and sendable hard filters.

## Production Secrets

Use environment variables or GitHub Actions secrets:

- `APPSTORESPY_API_KEY`
- `OPENAI_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Never commit real secret values.

## Operational Notes

- Runtime code uses only the Python standard library.
- `pytest` and `PyYAML` are optional development dependencies.
- `config.yaml` is JSON-compatible YAML so the project can run without PyYAML.
- Generated raw, processed, history, and report artifacts may be committed intentionally for snapshots, but secrets must never be committed.
- See `PROJECT_DOCUMENTATION.md` before changing collection, scoring, alert filtering, LLM, Telegram, storage, or feedback behavior.
