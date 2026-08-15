# Alert Funnel - 2026-08-15

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 122
- NEAR_MISS: 98
- REJECT: 217
- SINGLE_APP_WATCH: 5
- WATCH: 147

## Alert Stage Counts
- COOLDOWN_BLOCKED: 68
- NONE: 467
- QUALIFIED_CANDIDATE_ONLY: 53
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 68
- duplicate_market_signals_suppressed: 132
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 182
- below_data_quality_for_trend_confidence: 285
- below_data_quality_score: 285
- below_mvp_feasibility: 193
- below_opportunity_score: 456
- below_sendable_alert_score: 579
- below_team_fit_score: 362
- below_trend_confidence_score: 280
- blocked_risk_tag: 170
- complex_full_product: 264
- cooldown_exact_dedupe_key: 4
- cooldown_normalized_niche: 68
- duplicate_market_signal: 132
- giant_developer_competition: 29
- giant_developer_penalty: 27
- giant_share_too_high: 22
- growth_by_one_app_too_high: 266
- high_mvp_complexity: 121
- high_production_complexity: 61
- leader_dominated_market: 230
- low_classification_confidence: 182
- low_developer_diversity: 162
- low_mvp_feasibility: 193
- low_total_daily_installs: 145
- low_total_daily_installs_for_trend_confidence: 145
- market_signal_duplicate: 8
- no_growth_history: 1
- not_alert_status: 467
- one_app_growth_penalty: 294
- organic_confidence_low: 241
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 165
- single_app_breakout_not_regular_alert: 161
- single_developer_dominance: 218
- single_developer_penalty: 254
- single_developer_share_too_high: 232
- too_few_apps_for_sendable: 229
- too_few_apps_for_trend_confidence: 229
- too_few_successful_new_apps: 161
- too_few_successful_new_apps_for_trend_confidence: 161
- too_few_unique_developers: 162
- top3_too_dominant: 347
- top_app_concentration_penalty: 271
- top_app_too_dominant: 271
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT coloring score=89.41 sendable=87.74 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=919460 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=79.98 sendable=84.54 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=41477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.13 sendable=83.33 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=20755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.17 sendable=81.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=839497 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.12 sendable=81.58 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.77 installs=698829 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.88 sendable=81.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=279569 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.77 sendable=81.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1003939 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.77 sendable=81.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.25 installs=1290624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.69 sendable=80.24 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=357891 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.05 sendable=80.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.69 installs=3224341 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.95 sendable=79.56 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.59 installs=1216905 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.59 sendable=79.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.5 installs=139528 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.54 sendable=78.92 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.59 installs=190138 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.95 sendable=78.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.2 installs=1065149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.97 sendable=78.69 stage=QUALIFIED_CANDIDATE_ONLY quality=93.41 mvp=65.0 installs=42924 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=86.96 sendable=78.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.96 installs=1131721 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=82.93 sendable=78.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.41 installs=305826 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.84 sendable=78.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=41989 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=80.49 sendable=78.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.5 installs=67909 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=79.68 sendable=78.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=129938 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
