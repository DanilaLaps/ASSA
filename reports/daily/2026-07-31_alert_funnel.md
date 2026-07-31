# Alert Funnel - 2026-07-31

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 111
- NEAR_MISS: 107
- REJECT: 207
- SINGLE_APP_WATCH: 10
- WATCH: 160

## Alert Stage Counts
- COOLDOWN_BLOCKED: 62
- NONE: 484
- QUALIFIED_CANDIDATE_ONLY: 48
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 62
- duplicate_market_signals_suppressed: 115
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 187
- below_data_quality_for_trend_confidence: 286
- below_data_quality_score: 286
- below_mvp_feasibility: 193
- below_opportunity_score: 476
- below_sendable_alert_score: 588
- below_team_fit_score: 362
- below_trend_confidence_score: 327
- blocked_risk_tag: 128
- complex_full_product: 266
- cooldown_normalized_niche: 62
- duplicate_market_signal: 115
- giant_developer_competition: 28
- giant_developer_penalty: 25
- giant_share_too_high: 16
- growth_by_one_app_too_high: 265
- high_mvp_complexity: 131
- high_production_complexity: 58
- leader_dominated_market: 221
- low_classification_confidence: 187
- low_developer_diversity: 133
- low_mvp_feasibility: 193
- low_total_daily_installs: 122
- low_total_daily_installs_for_trend_confidence: 122
- market_signal_duplicate: 10
- no_growth_history: 1
- not_alert_status: 484
- one_app_growth_penalty: 296
- organic_confidence_low: 222
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 126
- single_app_breakout_not_regular_alert: 133
- single_developer_dominance: 204
- single_developer_penalty: 245
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 215
- too_few_apps_for_trend_confidence: 215
- too_few_successful_new_apps: 133
- too_few_successful_new_apps_for_trend_confidence: 133
- too_few_unique_developers: 133
- top3_too_dominant: 335
- top_app_concentration_penalty: 270
- top_app_too_dominant: 270
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT coloring score=91.22 sendable=86.27 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=903390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=80.79 sendable=84.4 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=43347 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.49 sendable=80.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=392841 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.04 sendable=80.52 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=995885 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.14 sendable=80.45 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=466995 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.67 sendable=80.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=681629 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.9 sendable=80.15 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.88 installs=1001060 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.75 sendable=79.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=55760 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.31 sendable=79.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=43668 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.61 sendable=79.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=207834 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.3 sendable=78.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.14 installs=1181307 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.8 sendable=78.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=97676 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=74.28 sendable=78.59 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=13320 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.86 sendable=78.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.15 installs=3100560 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.33 sendable=78.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.51 installs=1010213 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.12 sendable=77.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.06 installs=1213334 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.63 sendable=77.1 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=204967 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.65 sendable=76.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.5 installs=1364631 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.24 sendable=76.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.48 installs=930346 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.2 sendable=75.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1142837 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
