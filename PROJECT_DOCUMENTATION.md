# AppStoreSpy Niche Monitor - Project Documentation

This document is a human and AI oriented map of the project. It explains what the system does, the invariants that must not be broken, the runtime pipeline, the data contracts, and where to make safe changes.

## 1. Executive Summary

The project is an automated niche monitor for mobile games on Google Play. It collects one AppStoreSpy `/play/apps/query` response, normalizes and classifies apps, aggregates them into explainable niche clusters, scores those clusters deterministically, builds an internal alert longlist, ranks a strict sendable shortlist, optionally asks OpenAI for analysis of the sendable alerts, and delivers Telegram notifications.

The system is intentionally conservative:

- AppStoreSpy collection is limited to one production API request per run.
- The AppStoreSpy query must not use country, language, active country, or pagination axes.
- Scoring and alert selection are deterministic Python logic.
- LLM analysis is commentary and validation support, not the primary selector.
- `ALERT` is an internal qualified candidate longlist; `SENDABLE_ALERT` is the strict Telegram shortlist stage.
- Telegram should never send more than `alert_limits.max_alerts_per_run` regular alerts.
- The first run without compatible history must not send regular alerts.
- Unknown/new-pattern handling is ratio-based at cluster level and must remain discriminative.
- App-level unknown classification must not mark the whole market unknown because of one weak secondary dimension or an unlisted combo.

## 2. Primary Users and Use Cases

Primary users:

- A solo or small mobile-game team looking for fresh Google Play niche opportunities.
- A maintainer tuning deterministic rules, thresholds, and feedback loops.
- An AI coding agent that needs to modify the project without breaking safety constraints.

Main use cases:

- Production monitoring with AppStoreSpy, OpenAI analysis, Telegram alerts, and stored history.
- Dry-run monitoring against `data/sample/sample_apps.json`.
- Weekly digest generation from stored history and manual feedback.
- Feedback ingestion and one-time legacy feedback migration.
- Regression testing of classifier, scorer, trend, alert, LLM, Telegram, feedback, and collection behavior.

## 3. Non-Negotiable Invariants

These rules come from `AGENTS.md` and the current codebase. Treat them as hard constraints.

### Collection

- Production collection must make exactly one AppStoreSpy `/play/apps/query` request per run.
- Production collection must not add `country`, `language`, `active_countries`, or pagination.
- The production payload must use `page=1`, `sort=-release_date`, `published=true`, `category_type=GAME`, recent releases, and `downloads_daily >= 500`.
- Do not retry with a different query shape if AppStoreSpy rejects fields or limits. Fix config instead.

### Secrets

- Never commit real API keys or tokens.
- Read secrets only from environment variables.
- Important env vars:
  - `APPSTORESPY_API_KEY`
  - `OPENAI_API_KEY`
  - `OPENAI_MODEL` optional, controlled by config
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_CHAT_ID`

### Scoring and Alerts

- Keep scoring deterministic and explainable.
- Every alert must include:
  - `reason_codes`
  - `score_components`
  - `data_quality_score`
  - classification dimensions: `market_category`, `core_mechanic`, `theme`, `meta`, `audience`, `production_complexity`
- Never send more than `alert_limits.max_alerts_per_run` regular alerts.
- Only candidates with `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT` may be regular Telegram alerts.
- Every candidate should expose sendable funnel fields: `alert_stage`, `sendable_alert_score`, `sendable_alert_reasons`, and `sendable_alert_failures`.
- First run without compatible history must not send regular alerts.
- Store manual feedback labels and use them to improve scoring.

### LLM and Messaging

- LLM analysis must receive sendable alert candidates only, not raw full datasets.
- Current LLM pack is intentionally limited to `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT`.
- LLM and Telegram text must describe the data as one AppStoreSpy query without country/language filters.
- LLM analysis does not choose which alerts are sent. Python scoring and filtering choose them first.
- A LLM recommendation of `TEST` is commentary only and must not create a separate Telegram message.
- If there are zero final sendable alerts, OpenAI must be skipped and the run should report `fallback_reason=no_sendable_alerts`.

## 4. Repository Layout

```text
src/appstorespy_niche_monitor/
  appstorespy_client.py   HTTP client for AppStoreSpy.
  collector.py            Builds and validates the single AppStoreSpy query.
  cleaner.py              Normalizes raw AppStoreSpy app rows.
  niche_classifier.py     Rule-based niche and dimension classification.
  aggregator.py           Groups apps into niche summaries.
  trend_detector.py       Compares current summaries to history.
  data_quality.py         Computes data-quality score and reasons.
  scorer.py               Computes opportunity score, reason codes, risk tags.
  alert_ranker.py         Computes sendable alert score, hard filters, organic confidence.
  candidate_generator.py  Converts scored summaries into candidates.
  alert_filter.py         Sendable ranking, cooldown, send limits, sent-alert marking.
  llm_report.py           OpenAI/fallback analysis and alert markdown.
  telegram_notify.py      Telegram message formatting and delivery.
  report_writer.py        Daily and baseline markdown reports.
  storage.py              JSON/CSV/history/report persistence.
  feedback.py             Feedback JSONL, legacy migration, adjustments.
  weekly_digest.py        Weekly calibration digest.
  first_run_handler.py    First-run baseline rules.
  coverage.py             API response coverage metadata.
  config.py               JSON/YAML config loader.
  dedupe.py               Stable hashes and alert IDs.
  utils.py                Dates, parsing, math, text normalization.
  main.py                 CLI and pipeline orchestration.
```

Other important files:

- `config.yaml`: JSON-compatible YAML configuration.
- `README.md`: concise user-facing overview and commands.
- `AGENTS.md`: hard development and review rules.
- `tests/`: standard-library `unittest` test suite.
- `data/sample/sample_apps.json`: dry-run input.
- `data/raw/`, `data/processed/`, `data/history/`: runtime artifacts.
- `reports/alerts/`, `reports/daily/`, `reports/weekly/`: generated reports.

## 5. Runtime Pipeline

Main orchestration lives in `src/appstorespy_niche_monitor/main.py`, function `run_pipeline`.

Pipeline order:

```text
load config
ensure storage paths
migrate/load feedback
collect raw AppStoreSpy records or sample data
save raw snapshot
clean raw app rows
classify apps
save processed apps
aggregate apps into summaries
load compatible history
detect trends
enrich data quality
score summaries
save clusters and summaries
load sent_alerts
generate candidates
apply first-run baseline rules
rank sendable alerts, apply market-signal dedupe, hard filters, cooldown, and max-alert limits
build history summary
run LLM/fallback analysis for final sendable alerts
attach analysis to candidates
split candidates by status
write daily and alert reports
save processed candidates/status files
send Telegram alerts if notify enabled
mark sent alerts after successful send
send first-run baseline digest if applicable
save history summaries
send completion summary if notify enabled
return run result JSON
```

Important ordering notes:

- `save_raw` happens immediately after collection, before normalization.
- `save_history_summaries` happens after candidate processing and notifications.
- `sent_alerts.json` is updated only after `send_alerts` returns sent items.
- Daily reports and processed candidate files are written before Telegram sending.
- `alert_candidates` means all `status == ALERT`, not only sent alerts.
- `urgent_alerts` means `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT`.
- `sent_alerts.json` must only be updated for successfully sent `SENDABLE_ALERT` candidates.

Run result highlights:

- `alerts_count` / `alert_candidates_count`: all `status == ALERT` candidates.
- `sendable_alerts_count`: final regular-alert shortlist before Telegram delivery.
- `telegram_regular_alerts_sent`: successfully sent regular Telegram alert messages.
- `llm_candidates_sent`: candidates included in the LLM pack.
- `llm_test_recommendations`: `TEST` recommendations among final sendable alerts.
- `separate_test_messages_sent`: always `0` for production regular-alert flow.
- `duplicate_market_signals_suppressed`, `cooldown_blocked_count`, `limit_blocked_count`: funnel diagnostics.

## 6. Collection Contract

Collection code:

- `collector.build_single_query_payload`
- `collector.validate_single_query_payload`
- `collector.collect_apps`
- `appstorespy_client.AppStoreSpyClient.query_play_apps`

External API reference:

- AppStoreSpy API documentation/entry page: https://appstorespy.com/app-store-api
- If AppStoreSpy provides a private authenticated documentation URL inside the API dashboard, treat that account-specific URL as the source of truth and update this reference.

Production query shape:

```json
{
  "limit": 10000,
  "page": 1,
  "sort": "-release_date",
  "fields": ["id", "name", "..."],
  "filter": {
    "published": true,
    "category_type": "GAME",
    "release_date": {"gte": "<snapshot_date - release_date_days_back>"},
    "downloads_daily": {"gte": 500}
  }
}
```

Forbidden in payload, filter, and fields:

- `country`
- `language`
- `active_countries`

Dry-run behavior:

- `mode=dry-run` reads `data/sample/sample_apps.json`.
- Dry-run still builds the same payload metadata, but records `collection_mode=single_query_dry_run` and `api_requests_count=0`.

AppStoreSpy client behavior:

- Uses `APPSTORESPY_API_KEY` from environment unless explicitly passed.
- Does not retry `/play/apps/query`; `query_play_apps` calls `_request` with `max_attempts=1`.
- Redacts API key from error details.
- Converts 204 query response into `{"apps": []}`.

## 7. Normalized App Schema

`cleaner.normalize_app` maps raw AppStoreSpy rows to a stable app dict. Important fields:

- identity: `app_id`, `bundle`, `name`
- developer: `developer_name`, `developer_id`, `website`
- taxonomy: `platform`, `category`, `category_type`
- descriptions: `description`, `description_short`, `description_full`
- metrics: `downloads_daily`, `downloads_month`, `downloads_exact`, `downloads_mark`, `revenue_month`
- store quality: `rating_avg`, `rating_count`, `review_count`
- dates: `release_date`, `update_date`
- monetization/acquisition: `iap`, `ads`, `advertised`
- assets and links: `icon`, `screenshots`, `url_appstorespy`, `url`
- metadata: `source_query`, `coverage`
- raw copy: `raw_source_fields_json`

The normalized app retains `response_country` and `response_language` if AppStoreSpy returns them, but country/language are not query axes and are not grouping dimensions.

Deduplication:

- `clean_apps` dedupes by `(platform, bundle or app_id)`.
- If duplicate rows appear, the one with higher `downloads_daily` wins.

## 8. Classification

Classifier code:

- `niche_classifier.classify_app`
- `niche_classifier.match_niche`
- `niche_classifier.infer_dimension_with_confidence`
- `niche_classifier.infer_mvp_fields`

Classification is rule-based and uses:

- app name
- developer name
- category
- short and full descriptions
- configured `niche_rules`
- configured `dimension_rules`

Output dimensions:

- `niche`
- `normalized_niche`
- `market_category`
- `core_mechanic`
- `theme`
- `meta`
- `audience`
- `production_complexity`
- `full_product_complexity`
- `mvp_complexity`
- `mvp_feasibility_score`
- `simplifiable`
- `simplification_idea`
- confidence fields
- `is_unknown_or_new_pattern`

Important confidence fields:

- `niche_confidence`
- `mechanic_confidence`
- `theme_confidence`
- `audience_confidence`
- `complexity_confidence`

`confidence_from_match` is intentionally simple:

- no keyword match: `0.35`
- keyword match: `0.45 + keyword_length / 30`, clamped to `0.95`

This means short but valid keywords such as `run`, `tile`, `match`, `arrow`, or `level` can have confidence below `classification.min_confidence_for_hard_label`. Do not treat every short-match dimension as an unknown market signal.

Production complexity is inferred from `production_scores`. Higher production score means easier production:

- score `>= 12`: `low`
- score `>= 7`: `medium`
- otherwise: `high`

### App-Level Unknown/New-Pattern Detection

App-level `is_unknown_or_new_pattern` is computed in `niche_classifier.is_unknown_or_new_pattern`.

Current semantics:

- The feature is controlled by `classification.unknown_pattern_enabled`.
- The app is marked unknown only when both the primary `niche` and primary `core_mechanic` are unclassified or below `classification.min_primary_confidence_for_unknown_pattern`.
- Default `min_primary_confidence_for_unknown_pattern` is `0.5`.
- `theme`, `meta`, and `audience` uncertainty does not by itself make an app unknown.
- A recognized niche with a recognized mechanic is not unknown just because a dimension keyword is short.
- A recognized mechanic with `niche=other` is not automatically unknown; it may still be useful as a coarse mechanic signal.

The old dangerous behavior was to mark an app unknown when:

- any dimension was `other`
- any confidence value was below the hard-label threshold
- or `(core_mechanic, theme, meta)` was not in a tiny hardcoded whitelist

That behavior was non-discriminative for real AppStoreSpy slices because nearly every fresh game can have at least one weak dimension or a combination not in a small whitelist.

Optional combo detection:

- `classification.detect_unlisted_pattern_combos` defaults to `false`.
- If enabled, `known_pattern_combos` may be configured under `classification`.
- This mode should be treated as experimental because a small whitelist can easily make the whole market look suspicious.

Practical interpretation:

- App-level unknown means "the classifier could not identify the primary game niche and primary mechanic."
- It does not mean "this is a new opportunity."
- Cluster-level ratios decide whether unknown apps dominate a market signal.

## 9. Aggregation

Aggregator code:

- `aggregator.aggregate_apps`
- `aggregator.aggregate_group`
- `aggregator.compact_app`
- `aggregator.calculate_unknown_pattern_diagnostics`
- `aggregator.finalize_unknown_pattern_diagnostics`

Current group definitions:

- `normalized_niche`
- `core_mechanic`
- `core_mechanic_theme`
- `core_mechanic_theme_meta`
- `market_category_core_mechanic`

Configured group keys live in `config.yaml` under `aggregation.group_keys`.

Country and language are not grouping dimensions. Audience is summarized and retained, but not used as a hard group key.

Aggregated summary includes:

- grouping fields and dimensions
- `source_scope=single_appstorespy_query_no_country_language`
- query metadata and coverage
- app counts and app IDs
- total/average/median daily installs
- monthly downloads and revenue
- ratings
- new app counts
- developer diversity and fresh-success metrics:
  - `unique_developer_count`
  - `developer_diversity_score`
  - `fresh_success_ratio`
  - `cluster_diversity_score`
- concentration metrics:
  - `top_app_share`
  - `top3_app_share`
  - `growth_by_one_app_share`
  - `advertised_top_app_share`
  - `giant_developer_share`
  - `single_developer_share`
- `classification_confidence_avg`
- top apps

Unknown/new-pattern summary fields:

- `unknown_app_count`: number of apps in the cluster with app-level `is_unknown_or_new_pattern=true`.
- `unknown_app_share`: `unknown_app_count / app_count`.
- `unknown_installs_share`: daily installs from app-level unknown apps divided by total cluster daily installs.
- `top_app_unknown`: whether the highest-install app is app-level unknown.
- `top3_unknown_app_share`: share of top 3 apps that are app-level unknown.
- `mixed_unknown_cluster`: true when `unknown_app_count > 0`.
- `unknown_dominant_cluster`: true when unknown apps dominate the cluster.
- `unknown_pattern_blocker_active`: true when the cluster is unknown-dominant and classifier confidence is low.
- `cluster_pattern_status`: one of `known`, `mixed_unknown`, `unknown_dominant`, or `unknown_blocker_active`.
- `unknown_or_new_pattern_cluster`: backward-compatible alias for `unknown_dominant_cluster`.

Current formulas:

```text
mixed_unknown_cluster =
  unknown_app_count > 0

unknown_dominant_cluster =
  unknown_app_share >= 0.50
  OR unknown_installs_share >= 0.60
  OR (top_app_unknown AND top_app_share >= 0.55)

unknown_pattern_blocker_active =
  unknown_dominant_cluster
  AND classification_confidence_avg < 0.70
```

Important semantics:

- `mixed_unknown_cluster` is a soft diagnostic and risk tag.
- `unknown_dominant_cluster` is a stronger warning, not automatically a Telegram-send blocker.
- `unknown_pattern_blocker_active` is the hard/near-hard blocker used by candidate generation and sendable filters.
- `unknown_or_new_pattern_cluster` is preserved for backward compatibility but now means `unknown_dominant_cluster`, not "any app in this cluster is unknown."

Acceptance expectation:

- It should not be possible for all summaries to become unknown merely because every cluster has one unknown app.
- If all summaries become unknown-dominant, debug app-level classifier rules before changing aggregation thresholds.

Top apps:

- Sorted by `downloads_daily` descending.
- Stored up to 5.
- Include AppStoreSpy link, store link, monetization fields, rating fields, descriptions, icon, and first 3 screenshots.
- Top 3 are treated as top products/competitors for LLM and Telegram.

## 10. History and Trends

Trend code:

- `trend_detector.detect_trends`
- `trend_detector.nearest_before`
- `trend_detector.growth_by_one_app_share`

History source:

- `data/history/*_summaries.json`
- Loaded by `storage.load_history_summaries`
- Filtered in `main.run_pipeline` to matching `score_version`

Trend fields:

- `has_history`
- `history_depth_days`
- `weekly_growth_percent`
- `monthly_growth_percent`
- `growth_by_one_app_share`
- `previous_total_daily_installs`

If no compatible prior history exists:

- growth fields are zeroed
- first-run behavior may block alerts

## 11. Data Quality

Data-quality code:

- `data_quality.enrich_data_quality`
- `data_quality.calculate_data_quality`
- `alert_ranker.calculate_organic_confidence`

Data quality is a confidence score, not a standalone selector for the broad candidate list. It is used in opportunity scoring, candidate status, and sendable-alert hard filters.

Components:

- required field completeness
- history depth
- sample size
- signal diversity
- monetization reliability
- fresh-success reliability
- penalties

Common data-quality reasons:

- `no_history`
- `low_sample_size`
- `top_app_dominance`
- `weak_revenue_signal`
- `weak_monetization_signal`
- `no_successful_new_apps`
- `missing_required_fields`
- `one_app_growth`
- `paid_spike_risk`
- `classifier_low_confidence`
- `sample_truncated`
- `unknown_coverage`

Coverage risk comes from `coverage.coverage_risk_tags`.

Organic confidence fields:

- `organic_confidence`: `LOW`, `MEDIUM`, or `HIGH`
- `organic_confidence_score`: 0-100 confidence score
- `organic_confidence_reasons`: reason codes such as `organic_confidence_high_multi_developer`, `organic_confidence_low_paid_spike`, and `organic_confidence_low_top_app_dominance`

`organic_confidence == LOW` blocks a regular sendable alert, but the candidate may still appear in reports for manual review.

## 12. Scoring

Scoring code:

- `scorer.score_summaries`
- `scorer.score_summary`
- `alert_ranker.calculate_trend_confidence_score`
- `alert_ranker.calculate_team_fit_score`
- `alert_ranker.calculate_sendable_alert_score`
- `alert_ranker.passes_sendable_hard_filters`
- `alert_ranker.enrich_sendable_alert_fields`

Opportunity score is deterministic and explainable. It combines:

- demand
- freshness
- revenue/monetization
- rating
- MVP feasibility
- data quality
- competition penalty
- giant developer penalty
- paid-spike penalty

`score_components` stores each piece. `opportunity_score` is the clamped final score.

Sendable alert score is a second deterministic score for Telegram budget decisions. It answers a stricter question: is this candidate strong enough to send as a standalone regular Telegram alert today?

Sendable scoring combines:

- `opportunity_score`
- `trend_confidence_score`
- `team_fit_score`
- `data_quality_score`
- concentration penalty
- paid-spike penalty
- classifier-confidence penalty
- soft risk-tag penalty

`sendable_score_components` stores each piece and a `final` value. `sendable_alert_score` is clamped to 0-100.

Trend confidence considers:

- multi-app validation
- successful fresh apps
- developer diversity
- install volume
- weekly/monthly growth and history depth
- top-app and one-app-growth concentration
- paid acquisition exposure
- data quality and classification confidence
- severe/possible paid-spike risk

Team fit considers:

- MVP feasibility
- production and MVP complexity
- simplifiability
- giant-developer and leader dominance
- single-developer dominance
- high content or complex meta-loop risk tags

Demand scoring:

- If history is mature enough, uses percentile demand.
- Otherwise uses absolute total daily installs thresholds.

Reason codes are positive explanations such as:

- `multi_app_cluster`
- `strong_daily_installs`
- `fresh_traction`
- `low_mvp_complexity`
- `simplifiable_high_complexity`
- `low_giant_share`
- `diversified_apps`
- `monetization_signal_present`
- `good_rating_confidence`
- `new_pattern_detected`
- `single_app_breakout`
- `growing_vs_previous_snapshot`
- `historical_growth`
- `small_team_fit`

`new_pattern_detected` is intentionally conservative. It may be added only when the signal is broad enough:

- `app_count >= 3`
- `successful_new_apps_count >= 2`
- `unique_developer_count >= 2`

This prevents a single unclear app or a one-developer cluster from being described as a new market pattern.

Risk tags are caution flags such as:

- `leader_dominated`
- `severe_paid_spike`
- `possible_paid_spike`
- `growth_by_one_app`
- `giant_developer_risk`
- `single_developer_cluster`
- `weak_rating_signal`
- `weak_revenue_signal`
- `weak_monetization_signal`
- `low_data_quality`
- `classifier_low_confidence`
- `sample_truncated`
- `unknown_coverage`
- `high_full_complexity`
- `audience_uncertain`
- `mixed_unknown_cluster`
- `unknown_dominant_cluster`

Unknown risk-tag semantics:

- `mixed_unknown_cluster` is a soft penalty in sendable scoring.
- `unknown_dominant_cluster` is a stronger diagnostic and appears when unknown apps dominate the cluster.
- `unknown_pattern_blocker_active` is not just a tag; it is a boolean field that can block or heavily penalize sendable alerts.

## 13. Candidate Generation

Candidate code:

- `candidate_generator.generate_candidates`
- `candidate_generator.build_candidate`
- `candidate_generator.determine_status`
- `candidate_generator.dedupe_candidates`

Statuses:

- `ALERT`: passed configured alert thresholds and is part of the internal qualified longlist.
- `WATCH`: worth tracking but not a sendable alert.
- `SINGLE_APP_WATCH`: one app breakout that needs manual validation.
- `NEAR_MISS`: close to alert but failed limited conditions.
- `REJECT`: not worth acting on.

Alert failure conditions:

- `low_score`
- `low_demand`
- `too_few_apps`
- `no_successful_new_apps`
- `weak_data_quality`
- `low_mvp_feasibility`
- `giant_dominated`
- `severe_paid_spike`
- strict alert blockers such as `top_app_too_dominant`, `growth_by_one_app_too_high`, `classifier_low_confidence`, `unknown_pattern_blocker_active`

Important status rules:

- Single-app breakouts should not become ordinary `ALERT` candidates.
- Severe paid spike blocks `ALERT`.
- Strong top-app dominance or one-app-growth dominance blocks `ALERT`.
- Low classification confidence or weak data quality blocks `ALERT`.
- Mixed unknown clusters do not automatically block `ALERT`.
- Unknown-dominant clusters carry risk tags and diagnostics.
- `unknown_pattern_blocker_active` applies elevated unknown/new-pattern thresholds.
- `other` or unknown-pattern clusters need stronger app count, fresh-success, data-quality, and classification-confidence signals before becoming `ALERT` only when the unknown blocker is active.

Candidate IDs:

- `candidate_id`: `<snapshot_date>:<dedupe_key>:<group_key_type>`
- `dedupe_key`: stable 16-char hash of normalized niche, top 3 app IDs, and release window
- `alert_instance_id`: `<snapshot_date>:<dedupe_key>` for `ALERT` candidates

Candidate dedupe:

- Keeps the highest ranked candidate per dedupe key.
- Ranking favors status, group specificity, score, and app count.

Broad new-pattern reason code:

- `candidate_reason_codes` removes `new_pattern_detected` when the signal is not broad enough.
- `new_pattern_detected` requires at least 3 apps, 2 successful fresh apps, and 2 unique developers.
- This keeps reason codes from overstating isolated or single-developer events.

Candidate sendable funnel fields:

- `alert_stage`: one of `QUALIFIED_CANDIDATE`, `QUALIFIED_CANDIDATE_ONLY`, `SENDABLE_ALERT`, `COOLDOWN_BLOCKED`, `INITIAL_BASELINE_DIGEST`, `EXCLUDED_FROM_COOLDOWN`, or `NONE`
- `send_regular_alert`: true only for final regular Telegram alerts
- `telegram_delivery_channel`: `regular_alert`, `daily_digest_only`, `initial_baseline_digest`, or `none`
- `sendable_alert_score`
- `sendable_alert_rank`
- `trend_confidence_score`
- `team_fit_score`
- `sendable_score_components`
- `sendable_threshold_margins`
- `sendable_alert_reasons`
- `sendable_alert_failures`
- `first_blocking_failure`
- `market_signal_key`
- `market_signal_label`
- `duplicate_of_candidate_id`
- `duplicate_reason`

`sendable_threshold_margins` stores signed distance from each hard threshold. Positive values mean the candidate cleared a minimum threshold or stayed below a maximum concentration threshold. Negative values show by how much it missed.

`first_blocking_failure` is set for blocked candidates to make the first practical blocker visible in reports without scanning the full failure list.

## 14. Alert Filtering, Cooldown, and Sending

Alert filtering code:

- `alert_filter.apply_cooldown_and_alert_limits`
- `alert_filter.split_candidates`
- `alert_filter.mark_sent`
- `dedupe.build_market_signal_key`
- `dedupe.top_app_overlap`
- `dedupe.dedupe_market_signals`

Filtering rules:

- Enrich all candidates with sendable scores and funnel fields.
- Build and apply market-signal dedupe before final send selection.
- Rank `ALERT` candidates by descending `sendable_alert_score`, then `opportunity_score`.
- Apply sendable hard filters from `sendable_alert_rules`.
- Apply cooldown checks for exact dedupe key and normalized niche.
- Apply per-normalized-niche, per-core-mechanic, and per-market-signal limits.
- Apply `alert_limits.max_alerts_per_run`.
- Only `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT` can be regular Telegram alerts.
- Non-alert statuses never become regular Telegram alerts.

Sendable hard filters include:

- minimum sendable alert score
- minimum opportunity score
- minimum trend confidence and team fit
- minimum data quality, classification confidence, and MVP feasibility
- minimum app count, successful fresh apps, unique developers, and total daily installs
- maximum top-app, top-3, one-app-growth, advertised-top-app, giant-developer, and single-developer concentration
- blocked risk tags, including `severe_paid_spike`
- `organic_confidence != LOW`
- `unknown_pattern_blocker_active` when unknown/new-pattern low-confidence blocking is enabled

Common sendable failure codes:

- `below_sendable_alert_score`
- `below_trend_confidence_score`
- `below_team_fit_score`
- `below_data_quality_score`
- `too_few_apps_for_sendable`
- `too_few_successful_new_apps`
- `too_few_unique_developers`
- `top_app_too_dominant`
- `growth_by_one_app_too_high`
- `blocked_risk_tag`
- `organic_confidence_low`
- `unknown_pattern_blocker_active`
- `other_niche_low_confidence`
- `duplicate_market_signal`
- `cooldown_exact_dedupe_key`
- `cooldown_normalized_niche`
- `per_niche_limit_blocked`
- `per_core_mechanic_limit_blocked`
- `max_alerts_per_run_blocked`
- `telegram_budget_blocked`

Market-signal dedupe:

- Uses `market_signal_key` plus top-app overlap.
- Candidates with overlapping top apps at or above the configured threshold are treated as the same market signal.
- The best ranked candidate remains primary.
- Duplicates keep their status for reporting, but receive `duplicate_of_candidate_id`, `duplicate_reason=market_signal_duplicate`, and sendable failure codes.

Market-signal primary ranking prefers:

- higher `sendable_alert_score`
- higher `opportunity_score`
- more specific `group_key_type`
- lower `unknown_app_share`
- lower `unknown_installs_share`
- higher `classification_confidence_avg`
- higher `data_quality_score`

A candidate with `unknown_pattern_blocker_active=true` receives an additional rank penalty and should not suppress a cleaner duplicate unless it is clearly stronger.

Blocked sendable diagnostics:

- Every enriched candidate has `sendable_score_components`.
- Every enriched candidate has `sendable_threshold_margins`.
- Blocked candidates should expose `first_blocking_failure`.
- Reports should make the first blocker and unknown shares visible, because a candidate can fail many thresholds at once.

Output sets:

- `urgent_alerts`: `ALERT`, `send_regular_alert=True`, and `alert_stage=SENDABLE_ALERT`
- `alert_candidates`: all `ALERT`
- `watch`: `WATCH` and `SINGLE_APP_WATCH`
- `near_misses`: `NEAR_MISS`
- `rejected`: `REJECT`

Sent-alert state:

- Stored in `data/sent_alerts.json`.
- Updated only after Telegram alert send succeeds.
- Only successfully sent `SENDABLE_ALERT` candidates are written.
- Includes normalized niche, last sent timestamp, last alert instance ID, top app IDs, status, and score.

## 15. First-Run Behavior

First-run code:

- `first_run_handler.detect_history_state`
- `first_run_handler.apply_initial_baseline_rules`

History states:

- `FIRST_RUN_NO_HISTORY`
- `HISTORY_AVAILABLE`
- `WEEKLY_HISTORY_AVAILABLE`

If there is no compatible historical summary for the current `score_version`:

- Regular alerts are blocked.
- `send_regular_alert=False`.
- Candidates may be marked for initial baseline digest.
- Digest candidates use `alert_stage=INITIAL_BASELINE_DIGEST` and `telegram_delivery_channel=initial_baseline_digest`.
- Confidence is capped at configured maximum, usually `MEDIUM`.
- `INITIAL_BASELINE_NO_HISTORY` is added to reason codes for digest items.
- Digest items are not written to `sent_alerts` and do not start cooldown.

## 16. LLM Analysis

LLM code:

- `llm_report.analyze_candidate_pack`
- `llm_report.build_candidate_pack_input`
- `llm_report.generate_openai_pack_analysis`
- `llm_report.generate_fallback_pack_analysis`

Current LLM scope:

- OpenAI receives only candidates in `alerts`.
- `alerts` contains only `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT`.
- `watch`, `near_misses`, and `initial_baseline_digest` arrays are currently empty in the LLM pack.
- This is deliberate to ensure the LLM gives complete analysis for the Telegram alerts that will actually be sent.
- If there are zero sendable alerts, OpenAI is not called.
- Zero sendable alerts produces deterministic fallback status with `fallback_reason=no_sendable_alerts`.

LLM does not rank candidates. It analyzes already selected sendable alerts.

LLM recommendation semantics:

- `TEST`, `WATCH`, and `AVOID` are analytical recommendations only.
- `TEST` must not create additional Telegram messages.
- Python deterministic filtering has already selected the sendable candidates before OpenAI is called.

LLM compact candidate includes:

- candidate IDs and status
- source scope and query metadata
- classification dimensions
- demand, revenue, rating, freshness, concentration, and quality metrics
- score components
- sendable alert score, trend confidence, team fit, alert stage, and sendable score components
- sendable threshold margins and first blocking failure
- organic confidence
- market signal key and label
- reason codes and risk tags
- sendable reasons and failures
- unknown diagnostics:
  - `unknown_app_count`
  - `unknown_app_share`
  - `unknown_installs_share`
  - `top_app_unknown`
  - `top3_unknown_app_share`
  - `mixed_unknown_cluster`
  - `unknown_dominant_cluster`
  - `unknown_pattern_blocker_active`
  - `cluster_pattern_status`
- top apps, top products, top competitors

Top product context:

- `top_apps`: up to 5 apps
- `top_products`: first 3 top apps
- `top_competitors`: first 3 top apps
- Each includes names, developer, installs, revenue, ratings, dates, descriptions, AppStoreSpy URL, store URL, icon, and first 3 screenshots.

OpenAI response contract:

```json
{
  "candidate_analyses": {
    "<candidate_id>": {
      "recommendation": "TEST|WATCH|AVOID",
      "confidence": "low|medium|high",
      "why_interesting": [],
      "why_might_be_false_positive": [],
      "mvp_hypothesis": "",
      "simplified_mvp_scope": "",
      "competitor_takeaways": [],
      "entry_angle": "",
      "differentiation_idea": "",
      "why_top_products_validate_or_weaken_signal": "",
      "validation_steps": [],
      "risk_notes": [],
      "missing_data": [],
      "manual_review_needed": false
    }
  }
}
```

Fallback behavior:

- If LLM is disabled, missing API key, disabled in config, or API call fails, fallback analysis is generated deterministically.
- If there are zero sendable alerts, fallback is returned without making an OpenAI request.
- The expected fallback reason for this case is `no_sendable_alerts`.
- If OpenAI returns no usable candidate analyses, the call raises and falls back.
- If OpenAI returns only some expected candidate IDs, missing candidates receive `fallback_missing_from_openai`.

Important operational note:

- If Telegram shows `AI review: source=fallback_missing_from_openai`, OpenAI responded but omitted that candidate ID or used a non-matching key.
- The current pack restriction to sendable alerts only is intended to reduce this risk.

## 17. Telegram Notifications

Telegram code:

- `telegram_notify.format_alert_message`
- `telegram_notify.send_alerts`
- `telegram_notify.format_initial_baseline_digest_message`
- `telegram_notify.send_run_summary`

Regular alert message includes:

- niche name
- platform
- source/scope disclaimer
- release window and query sort
- coverage
- opportunity score
- sendable alert score
- trend confidence
- team fit
- organic confidence
- alert stage
- data quality
- MVP feasibility
- app count
- total daily installs
- top app share
- risk tags
- AI review source/confidence/fallback reason
- why interesting
- why sent now
- MVP hypothesis
- top 3 competitors with AppStoreSpy links
- risks
- why this can be false positive
- recommendation
- alert ID

Telegram send behavior:

- Requires `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
- Sends only candidates with `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT`.
- Asserts the `ALERT` status and `SENDABLE_ALERT` stage before sending each regular alert.
- Chunks long messages using `telegram.max_message_chars`.
- Sends completion summary if `telegram.notify_on_completion=true`.
- Completion summary reports `SENDABLE alerts`, `LLM TEST recommendations among sendable alerts`, and `Separate TEST messages sent: 0`.
- Completion summary also reports unknown diagnostics:
  - `Mixed unknown clusters`
  - `Unknown-dominant clusters`
  - `Unknown blocker active`
  - `Candidates blocked by unknown_pattern_blocker_active`
- If `SENDABLE alerts` is `0`, completion summary should show LLM fallback with `fallback_reason=no_sendable_alerts`.

## 18. Reports and Storage

Storage code:

- `storage.ensure_storage`
- `storage.save_raw`
- `storage.save_processed`
- `storage.save_history_summaries`
- `storage.write_alert_report`
- `report_writer.write_daily_reports`

Generated artifacts:

```text
data/raw/<date>_raw.json
data/processed/<date>_apps.json
data/processed/<date>_apps.csv
data/processed/<date>_clusters.json
data/processed/<date>_summaries.json
data/processed/<date>_candidates.json
data/processed/<date>_alerts.json
data/processed/<date>_sendable_alerts.json
data/processed/<date>_alert_funnel.json
data/processed/<date>_watch.json
data/processed/<date>_near_misses.json
data/processed/<date>_rejected.json
data/history/<date>_summaries.json
reports/daily/<date>_candidates.json
reports/daily/<date>_candidates.md
reports/daily/<date>_sendable_alerts.md
reports/daily/<date>_alert_funnel.md
reports/daily/<date>_unknown_diagnostics.md
reports/daily/<date>_watch.md
reports/daily/<date>_near_misses.md
reports/daily/<date>_rejected_summary.md
reports/alerts/<alert_id>.md
reports/weekly/<date>_weekly_digest.md
```

CSV caveat:

- `storage.write_csv` excludes `top_apps` because nested structures are not CSV friendly.
- JSON artifacts preserve nested top app data.

Processed alert artifacts:

- `<date>_alerts.json` contains all `status == ALERT` candidates, including qualified-but-not-sent candidates.
- `<date>_sendable_alerts.json` contains only `status == ALERT`, `send_regular_alert == true`, and `alert_stage == SENDABLE_ALERT`.
- `<date>_alert_funnel.json` summarizes total candidates, alert candidates, sendable alerts, watch/near-miss/reject counts, duplicate market signals suppressed, cooldown blocks, limit blocks, and sendable failure distributions.
- `<date>_unknown_diagnostics.md` summarizes mixed unknown clusters, unknown-dominant clusters, active unknown blockers, and top blocked candidates by `unknown_app_share` and `unknown_installs_share`.

Daily markdown reports include:

- status counts
- alert-stage counts
- coverage warnings
- unknown diagnostics
- candidate rows with unknown app/install shares
- candidate rows with `first_blocking_failure`
- sendable failure distributions

Use the markdown reports for human scanning and JSON artifacts for precise debugging.

## 19. Feedback Loop

Feedback code:

- `feedback.load_feedback`
- `feedback.append_feedback`
- `feedback.add_feedback`
- `feedback.feedback_adjustments`
- `feedback.migrate_legacy_feedback_to_jsonl_once`

Canonical feedback format:

- `data/feedback.jsonl`

Legacy format:

- `data/feedback.json`
- Used only for one-time migration.
- Normal runtime should read JSONL only.

Allowed verdicts:

- `good`
- `maybe`
- `false_positive`
- `already_known`
- `too_complex`
- `too_competitive`
- `paid_spike`

Feedback adjustments currently influence:

- paid-spike penalty multiplier
- competition penalty multiplier
- watch threshold delta
- MVP feasibility delta

Adjustments are bounded by `feedback.max_weight_adjustment_abs`.

## 20. Weekly Digest

Weekly digest code:

- `weekly_digest.generate_weekly_digest`

Digest includes:

- feedback summary
- false-positive reasons
- top WATCH-like candidates
- niches classified as `other`
- suspicious paid spike or concentration risks
- calibration recommendations

CLI:

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --weekly-digest
```

## 21. CLI Commands

Entrypoint:

- `python -m appstorespy_niche_monitor`
- package script: `appstorespy-monitor`

Common commands:

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode dry-run --snapshot-date 2026-06-04 --no-llm
```

```powershell
$env:APPSTORESPY_API_KEY="..."
$env:OPENAI_API_KEY="..."
$env:TELEGRAM_BOT_TOKEN="..."
$env:TELEGRAM_CHAT_ID="..."
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --mode production --notify
```

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --weekly-digest
```

```powershell
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --migrate-feedback
```

```powershell
$env:TELEGRAM_BOT_TOKEN="..."
$env:TELEGRAM_CHAT_ID="..."
$env:PYTHONPATH="src"
python -m appstorespy_niche_monitor --test-telegram
```

On this machine, `python` may not be in PATH. The bundled Codex runtime path used during development is:

```powershell
& "C:\Users\Danila\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
```

## 22. Configuration Map

Important `config.yaml` sections:

- `app`: app metadata, mode, score version, sample data path.
- `collection`: AppStoreSpy query constraints and fields.
- `filters`: AppStoreSpy filter values.
- `coverage`: coverage handling flags.
- `classification`: classifier behavior, unknown-pattern controls, and aliases.
- `aggregation`: group keys and grouping strategy.
- `scoring`: scoring behavior and neutral monetization score.
- `candidate_generation`: status thresholds.
- `thresholds`: freshness and dominance thresholds.
- `alert_rules`: legacy/compatibility alert thresholds used by tests and helper functions.
- `sendable_alert_rules`: strict shortlist thresholds, sendable hard filters, per-niche/mechanic/market-signal limits, and duplicate-overlap threshold.
- `giant_developers`: aliases for large developers.
- `production_scores`: small-team feasibility by niche.
- `niche_rules`: keyword-to-niche mapping.
- `dimension_rules`: keyword-to-dimension mapping.
- `classification_dimensions`: allowed values.
- `data_quality`: required fields and data-quality thresholds.
- `feedback`: feedback format, migration, allowed labels, adjustment settings.
- `alert_limits`: send limit, digest limits, cooldown days.
- `first_run_behavior`: baseline-only behavior.
- `llm`: OpenAI enablement, model env, default model, output tokens, timeout.
- `telegram`: Telegram env var names and message limit.
- `storage`: paths for data and reports.

Important `classification` keys:

- `use_rule_based_classifier`: current classifier mode.
- `use_llm_for_uncertain_apps`: currently disabled; LLM should not classify raw apps in production.
- `min_confidence_for_hard_label`: hard-label confidence reference used by older logic and diagnostics.
- `min_primary_confidence_for_unknown_pattern`: app-level unknown threshold for primary niche/mechanic confidence.
- `unknown_pattern_enabled`: master switch for app-level unknown marking.
- `detect_unlisted_pattern_combos`: optional experimental combo-whitelist mode; defaults to false.
- `known_pattern_combos`: optional list of known `(core_mechanic, theme, meta)` combos if combo detection is enabled.
- `aliases`: niche alias configuration.

Important `sendable_alert_rules` keys:

- `min_sendable_alert_score`: final sendable score floor.
- `min_opportunity_score`, `min_trend_confidence_score`, `min_team_fit_score`: core sendable floors.
- `min_data_quality_score`, `min_classification_confidence_avg`, `min_mvp_feasibility_score`: quality and feasibility floors.
- `min_app_count`, `min_successful_new_apps`, `min_unique_developers`, `min_total_daily_installs`: breadth floors.
- `max_top_app_share`, `max_top3_app_share`, `max_growth_by_one_app_share`: concentration ceilings.
- `max_advertised_top_app_share`: paid acquisition concentration ceiling.
- `max_giant_developer_share`, `max_single_developer_share`: competition/developer concentration ceilings.
- `blocked_risk_tags`: hard risk tags.
- `soft_penalty_risk_tags`: risk tags that reduce score but do not directly block.
- `max_sendable_per_normalized_niche`, `max_sendable_per_core_mechanic`, `max_sendable_per_market_signal_key`: send budget diversity caps.
- `market_signal_overlap_threshold`: top-app overlap threshold for duplicate market signals.
- `unknown_pattern_alert_min_classification_confidence`, `unknown_pattern_alert_min_app_count`, `unknown_pattern_alert_min_successful_new_apps`, `unknown_pattern_alert_min_data_quality_score`: elevated requirements used only when `unknown_pattern_blocker_active=true`.

Config file format:

- The file is JSON-compatible YAML.
- Runtime can load it with PyYAML if installed, otherwise with Python `json`.

## 23. Testing

Tests use `unittest` and can be run without pytest:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests
```

Bundled Python example:

```powershell
& "C:\Users\Danila\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -c "import sys, unittest; sys.path.insert(0, r'C:\Users\Danila\Documents\AppstoreSpy_analyze\src'); suite = unittest.defaultTestLoader.discover('tests'); result = unittest.TextTestRunner(verbosity=2).run(suite); raise SystemExit(0 if result.wasSuccessful() else 1)"
```

Test coverage by file:

- `test_collector.py`: single-query payload and one-request production contract.
- `test_appstorespy_client.py`: HTTP handling, no retries, redaction.
- `test_cleaner.py`: normalization and dedupe.
- `test_classifier.py`: niche/dimension classification and app-level unknown-pattern semantics.
- `test_aggregator.py`: aggregation without country, top app compact data, and ratio-based unknown diagnostics.
- `test_trend_detector.py`: growth metrics.
- `test_data_quality.py`: quality scoring and reasons.
- `test_scorer.py`: opportunity scoring, components, reason codes.
- `test_alert_ranker.py`: sendable score, components, hard filters, threshold margins, unknown blocker behavior, deterministic behavior.
- `test_candidate_generator.py`: status generation, candidate preservation, mixed/dominant unknown tags, broad new-pattern reason logic.
- `test_alert_filter.py`: alert rules, sendable limits, IDs.
- `test_alert_dedupe.py`: cooldown and dedupe stability.
- `test_sendable_alert_filter.py`: strict Telegram budget and non-alert status blocking.
- `test_market_signal_dedupe.py`: duplicate market signal suppression and cleaner duplicate preference over unknown-heavy duplicates.
- `test_first_run_behavior.py`: baseline-only logic.
- `test_llm_input.py`: LLM pack restrictions and raw-data exclusion.
- `test_llm_report.py`: OpenAI/fallback parsing, prompt contract, and no-LLM-call behavior when sendable alert count is zero.
- `test_telegram_notify.py`: Telegram formatting and chunking.
- `test_report_writer.py`: daily/baseline report content.
- `test_feedback.py`: feedback round trip.
- `test_feedback_migration.py`: legacy migration.
- `test_feedback_migration_cli.py`: migration CLI exits without pipeline.
- `test_weekly_digest.py`: weekly digest content.
- `test_workflow.py`: GitHub workflow expectations.

When changing classifier, scorer, trend detector, data quality, feedback, or alert filter behavior, add or update tests.

Unknown/new-pattern regression tests should cover:

- one unknown app in a mostly known cluster does not activate the blocker
- majority-unknown clusters become unknown-dominant
- unknown top app with high top-app share becomes unknown-dominant
- mixed unknown clusters do not automatically block sendable alerts
- active unknown blocker blocks or heavily penalizes sendable alerts
- cleaner duplicate beats unknown-heavy duplicate in market-signal dedupe
- valid short classifier keywords do not make an app unknown
- OpenAI is skipped when there are zero sendable alerts

## 24. Safe Change Guide for Humans and AI Agents

Before editing:

- Read `AGENTS.md`.
- Check `git status --short`.
- Identify whether the change touches collection, scoring, alert sending, storage, or secrets.
- Do not remove or rewrite unrelated user changes.

Collection changes:

- Must preserve exactly one production `/play/apps/query` request.
- Must keep forbidden query axes out of payload and fields.
- Must update `tests/test_collector.py`.

Scoring changes:

- Must preserve deterministic behavior.
- Must keep `score_components` explainable.
- Must update scorer and candidate tests.

Alert filter changes:

- Must not increase Telegram spam risk.
- Must preserve `max_alerts_per_run`.
- Must preserve the requirement that only `SENDABLE_ALERT` candidates can be regular Telegram alerts.
- Must update alert ranker, alert filter, dedupe, LLM input, Telegram, and first-run tests when relevant.

LLM changes:

- Must not send raw full datasets.
- Must keep source scope wording: one AppStoreSpy query, no country/language filters.
- Must maintain fallback behavior when OpenAI is unavailable.
- Must update LLM input/report tests.

Telegram changes:

- Must not send non-alert statuses as regular alerts.
- Must include data quality, reason codes, and score context.
- Must keep completion summary behavior explicit.

Storage/history changes:

- Must avoid silent data loss.
- Use atomic JSON writes where possible.
- Preserve history summaries needed for trend detection.

## 25. Debugging Playbook

### No alerts sent

Check:

- `result["baseline_only"]`
- `data/processed/<date>_alerts.json`
- `data/processed/<date>_sendable_alerts.json`
- `data/processed/<date>_alert_funnel.json`
- `send_regular_alert` fields
- `alert_stage`
- `sendable_alert_score`
- `sendable_alert_failures`
- `alert_filter_reasons`
- `data/sent_alerts.json`
- `first_run_without_history`

Common reasons:

- first run without history
- cooldown
- Telegram budget already reached
- no candidates passed base alert thresholds
- no `ALERT` candidates passed sendable hard filters
- weak data quality, classification confidence, trend confidence, or MVP feasibility
- duplicate market signal suppression
- top-app, top-3, one-app-growth, advertised-top-app, giant-developer, or single-developer concentration

### Telegram says fallback or no AI review

Check:

- `llm_status`
- `llm_analysis_source`
- `llm_fallback_reason`
- `OPENAI_API_KEY`
- `llm.enabled`
- `--no-llm`
- whether candidate was included in LLM pack
- whether candidate has `alert_stage=SENDABLE_ALERT`

Meaning of sources:

- `openai`: OpenAI supplied usable analysis.
- `fallback`: deterministic fallback was used.
- `fallback_missing_from_openai`: OpenAI response omitted that candidate ID.

### Data quality is low

Check:

- `data_quality_reasons`
- required fields in config
- AppStoreSpy response field coverage
- `coverage.sample_truncated`
- sample size and top app dominance

### Candidate classified as `other`

Check:

- app `name`, `description_short`, `description_full`, `category`
- `niche_rules`
- `dimension_rules`
- `classification_confidence_avg`
- `unknown_or_new_pattern_cluster`, which is now an alias for `unknown_dominant_cluster`
- whether `unknown_pattern_blocker_active` is true

Important distinction:

- `niche=other` means the niche keyword rules did not find a configured niche.
- `is_unknown_or_new_pattern=true` means app-level primary niche and primary mechanic are both unclassified or very weak.
- `unknown_or_new_pattern_cluster=true` means the cluster is unknown-dominant, not merely that one app is unknown.

### All or most clusters are unknown

Check:

- `data/processed/<date>_apps.json`
- app-level `is_unknown_or_new_pattern`
- app-level `niche`, `core_mechanic`, `theme`, and confidence fields
- `classification.min_primary_confidence_for_unknown_pattern`
- `classification.detect_unlisted_pattern_combos`
- `reports/daily/<date>_unknown_diagnostics.md`
- `data/processed/<date>_alert_funnel.json`

Expected diagnosis flow:

- If almost every app has `is_unknown_or_new_pattern=true`, fix `niche_classifier.is_unknown_or_new_pattern` or classifier rules first.
- If app-level unknown is reasonable but every summary is unknown-dominant, inspect aggregation grouping and top-app concentration.
- If only mixed unknown clusters are high, that is not automatically bad; mixed unknown is a soft diagnostic.
- If `unknown_pattern_blocker_active` is high, inspect whether unknown apps dominate by app count, installs, or top-app share and whether `classification_confidence_avg < 0.70`.

Do not fix this by changing the AppStoreSpy query, adding country/language filters, enabling pagination, or letting the LLM select alerts. The issue is classifier/aggregation semantics, not collection scope.

Useful quick checks:

```powershell
$apps = Get-Content -Raw data\processed\<date>_apps.json | ConvertFrom-Json
($apps | Where-Object { $_.is_unknown_or_new_pattern -eq $true }).Count
$apps | Group-Object niche,core_mechanic,theme,meta,is_unknown_or_new_pattern | Sort-Object Count -Descending | Select-Object -First 20 Name,Count
```

### Suspicious paid spike

Check:

- `advertised_top_app_share`
- `growth_by_one_app_share`
- `top_app_share`
- `top3_app_share`
- `organic_confidence`
- `sendable_alert_failures`
- `rating_confidence`
- `severe_paid_spike_risk`
- top app `advertised` flag

### History seems ignored

Check:

- `data/history/*_summaries.json`
- `score_version`
- `snapshot_date`
- `history_state`
- `history_depth_days`

## 26. Current Known Design Choices

- Runtime dependencies are standard library only.
- `pytest` is optional; tests are `unittest` compatible.
- Config is JSON-compatible YAML for environments without PyYAML.
- LLM analysis is done through the OpenAI Responses API endpoint.
- Telegram uses simple text messages, not Markdown parse mode.
- Top competitors are derived from the same one AppStoreSpy query, not fetched separately.
- Raw AppStoreSpy data is stored locally, but LLM receives compact final sendable alert candidates only.
- Weekly digest is offline and uses stored history plus feedback.

## 27. Glossary

- AppStoreSpy query: The single `/play/apps/query` call made in production.
- App: A normalized Google Play product row.
- Niche: A rule-derived label such as `sort puzzle`, `merge`, or `runner`.
- Dimension: One of market category, mechanic, theme, meta, audience, complexity.
- Summary: Aggregated metrics for a grouped niche.
- Candidate: A scored summary converted into an actionable status.
- ALERT: Candidate passed base alert thresholds and belongs to the internal qualified longlist.
- Sendable alert: An `ALERT` with `send_regular_alert=True` and `alert_stage=SENDABLE_ALERT`.
- Alert stage: Funnel stage explaining whether an alert is a qualified candidate, sendable alert, cooldown block, baseline digest, or non-sendable item.
- Sendable alert score: Deterministic shortlist score used for Telegram budget selection.
- Market signal key: Stable key used to suppress duplicate opportunities across grouping strategies.
- WATCH: Candidate worth tracking but not sent as regular alert.
- NEAR_MISS: Candidate close to alert thresholds.
- REJECT: Candidate filtered out.
- Dedupe key: Stable hash used for cooldown.
- Alert instance ID: Date-specific alert identifier.
- Data quality score: Confidence in the source signal.
- Reason code: Positive/explanatory signal for why the candidate matters.
- Risk tag: Caution signal for false positives or poor fit.
- App-level unknown pattern: `is_unknown_or_new_pattern=true` on an app when primary niche and primary mechanic are both unclassified or very low confidence.
- Mixed unknown cluster: A cluster with at least one app-level unknown app.
- Unknown-dominant cluster: A cluster where unknown apps dominate by count, installs, or top-app leadership.
- Unknown pattern blocker active: A cluster-level hard/near-hard blocker active when the cluster is unknown-dominant and classification confidence is below 0.70.
- Cluster pattern status: Human-readable status for unknown diagnostics: `known`, `mixed_unknown`, `unknown_dominant`, or `unknown_blocker_active`.
- Top competitors: Top 3 apps from a niche by `downloads_daily` in the same query slice.
- LLM pack: Compact JSON sent to OpenAI for final `SENDABLE_ALERT` candidates.

## 28. Quick AI-Agent Checklist

Before finalizing any change, verify:

- No secrets were added.
- Production collection still uses exactly one request.
- No country/language/active country/pagination was introduced.
- Alert sending still respects cooldown and `max_alerts_per_run`.
- Regular Telegram alerts require `status == ALERT`, `send_regular_alert == True`, and `alert_stage == SENDABLE_ALERT`.
- LLM TEST recommendations do not create separate Telegram messages.
- First-run baseline still blocks regular alerts.
- LLM input still excludes raw full datasets.
- LLM input includes only final sendable alerts.
- LLM is skipped when there are zero final sendable alerts.
- LLM and Telegram wording still says one AppStoreSpy query without country/language filters.
- Alerts still include reason codes, score components, data quality, and classification dimensions.
- Candidates still include sendable funnel fields and explainable sendable failures.
- Unknown diagnostics are ratio-based and app-level unknown is not triggered by one weak secondary dimension or a tiny combo whitelist.
- Relevant tests were updated and run.
