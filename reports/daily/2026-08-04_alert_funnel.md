# Alert Funnel - 2026-08-04

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 87
- NEAR_MISS: 114
- REJECT: 200
- SINGLE_APP_WATCH: 16
- WATCH: 158

## Alert Stage Counts
- COOLDOWN_BLOCKED: 2
- NONE: 488
- QUALIFIED_CANDIDATE_ONLY: 84
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 2
- duplicate_market_signals_suppressed: 122
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 63
- unknown_pattern_blocker_active: 63

## Sendable Failure Distribution
- below_classification_confidence: 174
- below_data_quality_for_trend_confidence: 299
- below_data_quality_score: 299
- below_mvp_feasibility: 180
- below_opportunity_score: 470
- below_sendable_alert_score: 572
- below_team_fit_score: 352
- below_trend_confidence_score: 355
- blocked_risk_tag: 96
- complex_full_product: 250
- cooldown_normalized_niche: 2
- duplicate_market_signal: 122
- giant_developer_competition: 32
- giant_developer_penalty: 28
- giant_share_too_high: 22
- growth_by_one_app_too_high: 259
- high_mvp_complexity: 122
- high_production_complexity: 61
- leader_dominated_market: 230
- low_classification_confidence: 174
- low_developer_diversity: 149
- low_mvp_feasibility: 180
- low_total_daily_installs: 150
- low_total_daily_installs_for_trend_confidence: 150
- market_signal_duplicate: 10
- no_growth_history: 1
- not_alert_status: 488
- one_app_growth_penalty: 284
- organic_confidence_low: 227
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 94
- single_app_breakout_not_regular_alert: 149
- single_developer_dominance: 209
- single_developer_penalty: 245
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 227
- too_few_apps_for_trend_confidence: 227
- too_few_successful_new_apps: 149
- too_few_successful_new_apps_for_trend_confidence: 149
- too_few_unique_developers: 149
- top3_too_dominant: 337
- top_app_concentration_penalty: 269
- top_app_too_dominant: 269
- unknown_pattern_blocker_active: 61

## Top Qualified But Not Sent
- ALERT coloring score=90.29 sendable=83.81 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=777637 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=86.19 sendable=80.37 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=158648 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=83.31 sendable=79.21 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=84901 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.65 sendable=79.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.27 installs=1088839 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.59 sendable=78.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.26 installs=709012 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.93 sendable=78.34 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.51 installs=2524331 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.08 sendable=77.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.87 installs=959675 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.51 sendable=77.59 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.21 installs=863924 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=87.07 sendable=77.26 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=148979 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=78.85 sendable=76.55 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=118243 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.7 sendable=76.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.6 installs=186872 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.63 sendable=75.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1120006 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=85.19 sendable=74.34 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=363656 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.56 sendable=74.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=43411 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.89 sendable=73.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.03 installs=1234184 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.13 sendable=73.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=771121 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=73.77 sendable=72.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=15599 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.19 sendable=72.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.55 installs=79427 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=87.54 sendable=71.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.64 installs=1011818 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT sort_puzzle score=87.37 sendable=71.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=301868 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
