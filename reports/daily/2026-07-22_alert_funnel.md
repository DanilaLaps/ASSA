# Alert Funnel - 2026-07-22

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 86
- NEAR_MISS: 125
- REJECT: 181
- SINGLE_APP_WATCH: 18
- WATCH: 181

## Alert Stage Counts
- COOLDOWN_BLOCKED: 48
- NONE: 505
- QUALIFIED_CANDIDATE_ONLY: 37
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 48
- duplicate_market_signals_suppressed: 114
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 186
- below_data_quality_for_trend_confidence: 295
- below_data_quality_score: 295
- below_mvp_feasibility: 196
- below_opportunity_score: 499
- below_sendable_alert_score: 588
- below_team_fit_score: 373
- below_trend_confidence_score: 360
- blocked_risk_tag: 93
- complex_full_product: 284
- cooldown_normalized_niche: 48
- duplicate_market_signal: 114
- giant_developer_competition: 37
- giant_developer_penalty: 34
- giant_share_too_high: 20
- growth_by_one_app_too_high: 295
- high_mvp_complexity: 127
- high_production_complexity: 56
- leader_dominated_market: 220
- low_classification_confidence: 186
- low_developer_diversity: 125
- low_mvp_feasibility: 196
- low_total_daily_installs: 121
- low_total_daily_installs_for_trend_confidence: 121
- market_signal_duplicate: 12
- no_growth_history: 1
- not_alert_status: 505
- one_app_growth_penalty: 320
- organic_confidence_low: 213
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 91
- single_app_breakout_not_regular_alert: 125
- single_developer_dominance: 197
- single_developer_penalty: 249
- single_developer_share_too_high: 221
- too_few_apps_for_sendable: 199
- too_few_apps_for_trend_confidence: 199
- too_few_successful_new_apps: 125
- too_few_successful_new_apps_for_trend_confidence: 125
- too_few_unique_developers: 125
- top3_too_dominant: 339
- top_app_concentration_penalty: 269
- top_app_too_dominant: 269
- unknown_pattern_blocker_active: 62

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.47 sendable=83.34 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=43937 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.31 sendable=82.41 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=28390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT sort_puzzle score=88.94 sendable=81.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1016129 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.55 sendable=79.56 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=13581 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.11 sendable=79.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.09 installs=1451484 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.06 sendable=78.6 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.37 installs=1558070 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.65 sendable=78.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.42 installs=874962 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.79 sendable=78.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=701996 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.51 sendable=77.7 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=116102 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=89.26 sendable=77.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=992099 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.37 sendable=77.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.23 installs=1142623 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.47 sendable=76.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=2019627 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT coloring score=89.32 sendable=76.26 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1052160 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.66 sendable=75.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=34705 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.91 sendable=75.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=361710 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.15 sendable=73.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=47056 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.47 sendable=73.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=61.77 installs=418681 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.86 sendable=72.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=286951 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.13 sendable=70.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=137080 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=84.8 sendable=70.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=554372 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
