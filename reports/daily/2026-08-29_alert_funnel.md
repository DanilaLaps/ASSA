# Alert Funnel - 2026-08-29

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 96
- NEAR_MISS: 93
- REJECT: 203
- SINGLE_APP_WATCH: 13
- WATCH: 181

## Alert Stage Counts
- COOLDOWN_BLOCKED: 28
- NONE: 490
- QUALIFIED_CANDIDATE_ONLY: 67
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 28
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 183
- below_data_quality_for_trend_confidence: 325
- below_data_quality_score: 325
- below_mvp_feasibility: 189
- below_opportunity_score: 481
- below_sendable_alert_score: 583
- below_team_fit_score: 346
- below_trend_confidence_score: 367
- blocked_risk_tag: 119
- complex_full_product: 249
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 28
- duplicate_market_signal: 119
- giant_developer_competition: 29
- giant_developer_penalty: 28
- giant_share_too_high: 19
- growth_by_one_app_too_high: 309
- high_mvp_complexity: 123
- high_production_complexity: 62
- leader_dominated_market: 227
- low_classification_confidence: 183
- low_developer_diversity: 144
- low_mvp_feasibility: 189
- low_total_daily_installs: 123
- low_total_daily_installs_for_trend_confidence: 123
- market_signal_duplicate: 6
- not_alert_status: 490
- one_app_growth_penalty: 330
- organic_confidence_low: 229
- other_niche_low_confidence: 65
- severe_paid_spike_penalty: 118
- single_app_breakout_not_regular_alert: 144
- single_developer_dominance: 213
- single_developer_penalty: 250
- single_developer_share_too_high: 228
- too_few_apps_for_sendable: 217
- too_few_apps_for_trend_confidence: 217
- too_few_successful_new_apps: 144
- too_few_successful_new_apps_for_trend_confidence: 144
- too_few_unique_developers: 144
- top3_too_dominant: 343
- top_app_concentration_penalty: 277
- top_app_too_dominant: 277
- unknown_pattern_blocker_active: 69

## Top Qualified But Not Sent
- ALERT coloring score=89.98 sendable=86.56 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=996080 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=79.37 sendable=82.42 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=38390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.99 sendable=81.8 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=484996 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=86.13 sendable=78.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1556583 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.87 sendable=78.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=394043 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.0 sendable=78.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.9 installs=4211282 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.71 sendable=78.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1591271 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.2 sendable=77.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.42 installs=358268 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.97 sendable=77.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.86 installs=765709 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=82.51 sendable=76.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=197493 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.73 sendable=76.58 stage=COOLDOWN_BLOCKED quality=87.74 mvp=85.0 installs=43956 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.4 sendable=76.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.39 installs=1323718 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.59 sendable=75.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.05 installs=176757 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.97 sendable=75.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.05 installs=1481671 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.14 sendable=75.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.7 installs=1743103 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.47 sendable=75.57 stage=COOLDOWN_BLOCKED quality=85.15 mvp=85.0 installs=42640 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.55 sendable=75.56 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=49211 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=81.4 sendable=75.51 stage=QUALIFIED_CANDIDATE_ONLY quality=94.86 mvp=65.0 installs=54640 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=82.34 sendable=75.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.71 installs=194037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.19 sendable=75.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=744261 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
