# Alert Funnel - 2026-07-28

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 100
- NEAR_MISS: 115
- REJECT: 197
- SINGLE_APP_WATCH: 9
- WATCH: 174

## Alert Stage Counts
- COOLDOWN_BLOCKED: 7
- NONE: 495
- QUALIFIED_CANDIDATE_ONLY: 92
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 7
- duplicate_market_signals_suppressed: 123
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 194
- below_data_quality_for_trend_confidence: 298
- below_data_quality_score: 298
- below_mvp_feasibility: 201
- below_opportunity_score: 476
- below_sendable_alert_score: 585
- below_team_fit_score: 366
- below_trend_confidence_score: 323
- blocked_risk_tag: 124
- complex_full_product: 277
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 7
- duplicate_market_signal: 123
- giant_developer_competition: 35
- giant_developer_penalty: 31
- giant_share_too_high: 22
- growth_by_one_app_too_high: 301
- high_mvp_complexity: 131
- high_production_complexity: 55
- leader_dominated_market: 221
- low_classification_confidence: 194
- low_developer_diversity: 125
- low_mvp_feasibility: 201
- low_total_daily_installs: 120
- low_total_daily_installs_for_trend_confidence: 120
- market_signal_duplicate: 15
- not_alert_status: 495
- one_app_growth_penalty: 319
- organic_confidence_low: 223
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 121
- single_app_breakout_not_regular_alert: 125
- single_developer_dominance: 209
- single_developer_penalty: 249
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 212
- too_few_apps_for_trend_confidence: 212
- too_few_successful_new_apps: 125
- too_few_successful_new_apps_for_trend_confidence: 125
- too_few_unique_developers: 125
- top3_too_dominant: 332
- top_app_concentration_penalty: 270
- top_app_too_dominant: 270
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT sort_puzzle score=82.09 sendable=86.45 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=54091 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=80.17 sendable=83.74 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=35488 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.15 sendable=82.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1055944 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.26 sendable=81.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=393311 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.19 sendable=81.22 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=63052 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.99 sendable=80.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=50519 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.63 sendable=80.55 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=213809 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=85.73 sendable=80.33 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=459718 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.54 sendable=80.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.69 installs=310523 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.02 sendable=79.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1022692 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.24 sendable=79.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.5 installs=1415965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.85 sendable=79.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.38 installs=913059 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.03 sendable=79.1 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.34 installs=1119305 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.04 sendable=78.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.75 installs=1071749 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.03 sendable=77.95 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=12698 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=76.66 sendable=77.77 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=25938 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=88.65 sendable=76.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.78 installs=740702 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=72.99 sendable=76.06 stage=QUALIFIED_CANDIDATE_ONLY quality=93.34 mvp=65.0 installs=11303 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT mahjong score=85.7 sendable=76.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=214092 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=87.49 sendable=75.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.49 installs=3638133 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
