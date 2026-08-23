# Alert Funnel - 2026-08-23

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 110
- NEAR_MISS: 109
- REJECT: 207
- SINGLE_APP_WATCH: 7
- WATCH: 158

## Alert Stage Counts
- COOLDOWN_BLOCKED: 68
- NONE: 481
- QUALIFIED_CANDIDATE_ONLY: 41
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 68
- duplicate_market_signals_suppressed: 118
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 181
- below_data_quality_for_trend_confidence: 288
- below_data_quality_score: 288
- below_mvp_feasibility: 191
- below_opportunity_score: 471
- below_sendable_alert_score: 582
- below_team_fit_score: 357
- below_trend_confidence_score: 295
- blocked_risk_tag: 140
- complex_full_product: 262
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 68
- duplicate_market_signal: 118
- giant_developer_competition: 31
- giant_developer_penalty: 30
- giant_share_too_high: 21
- growth_by_one_app_too_high: 261
- high_mvp_complexity: 120
- high_production_complexity: 56
- leader_dominated_market: 230
- low_classification_confidence: 181
- low_developer_diversity: 145
- low_mvp_feasibility: 191
- low_total_daily_installs: 150
- low_total_daily_installs_for_trend_confidence: 150
- market_signal_duplicate: 9
- not_alert_status: 481
- one_app_growth_penalty: 291
- organic_confidence_low: 233
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 139
- single_app_breakout_not_regular_alert: 144
- single_developer_dominance: 215
- single_developer_penalty: 252
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 220
- too_few_apps_for_trend_confidence: 220
- too_few_successful_new_apps: 144
- too_few_successful_new_apps_for_trend_confidence: 144
- too_few_unique_developers: 145
- top3_too_dominant: 336
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT coloring score=90.35 sendable=88.66 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1207977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.82 sendable=84.45 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=42494 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.55 sendable=83.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1198117 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.32 sendable=82.84 stage=COOLDOWN_BLOCKED quality=95.0 mvp=84.78 installs=485329 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.32 sendable=82.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1305952 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.22 sendable=81.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.12 installs=1976898 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.09 sendable=80.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.83 installs=4383481 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.51 sendable=80.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.93 installs=1743432 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.19 sendable=80.2 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=90092 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=87.18 sendable=79.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.14 installs=1172205 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.4 sendable=79.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=753177 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.45 sendable=79.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.02 installs=1175462 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.37 sendable=79.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.79 installs=1630772 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.59 sendable=78.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.7 installs=243645 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.01 sendable=78.84 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=189291 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=85.74 sendable=77.8 stage=COOLDOWN_BLOCKED quality=87.91 mvp=72.05 installs=565620 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.7 sendable=77.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1482928 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.47 sendable=77.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=38008 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=78.21 sendable=76.1 stage=COOLDOWN_BLOCKED quality=87.17 mvp=74.2 installs=62521 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.79 sendable=76.03 stage=COOLDOWN_BLOCKED quality=94.1 mvp=65.0 installs=14439 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
