# Alert Funnel - 2026-06-12

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 61
- NEAR_MISS: 91
- REJECT: 179
- SINGLE_APP_WATCH: 16
- WATCH: 251

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 537
- QUALIFIED_CANDIDATE_ONLY: 59
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 103
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 74
- unknown_pattern_blocker_active: 74

## Sendable Failure Distribution
- below_classification_confidence: 195
- below_data_quality_for_trend_confidence: 295
- below_data_quality_score: 295
- below_mvp_feasibility: 209
- below_opportunity_score: 566
- below_sendable_alert_score: 594
- below_team_fit_score: 373
- below_trend_confidence_score: 376
- blocked_risk_tag: 106
- complex_full_product: 284
- cooldown_normalized_niche: 1
- duplicate_market_signal: 103
- giant_developer_competition: 28
- giant_developer_penalty: 22
- giant_share_too_high: 18
- growth_by_one_app_too_high: 298
- high_mvp_complexity: 135
- high_production_complexity: 56
- leader_dominated_market: 197
- low_classification_confidence: 195
- low_developer_diversity: 128
- low_mvp_feasibility: 209
- low_total_daily_installs: 106
- low_total_daily_installs_for_trend_confidence: 106
- market_signal_duplicate: 7
- no_growth_history: 4
- not_alert_status: 537
- one_app_growth_penalty: 343
- organic_confidence_low: 205
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 101
- single_app_breakout_not_regular_alert: 126
- single_developer_dominance: 184
- single_developer_penalty: 225
- single_developer_share_too_high: 199
- too_few_apps_for_sendable: 205
- too_few_apps_for_trend_confidence: 205
- too_few_successful_new_apps: 126
- too_few_successful_new_apps_for_trend_confidence: 126
- too_few_unique_developers: 128
- top3_too_dominant: 338
- top_app_concentration_penalty: 250
- top_app_too_dominant: 250
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT sort_puzzle score=75.64 sendable=80.52 stage=COOLDOWN_BLOCKED quality=94.29 mvp=85.0 installs=75729 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=73.91 sendable=80.36 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=73584 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.2 sendable=80.02 stage=QUALIFIED_CANDIDATE_ONLY quality=94.74 mvp=85.0 installs=59938 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.67 sendable=75.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=919308 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=73.41 sendable=75.79 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=333790 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.73 sendable=75.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=347454 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.66 sendable=75.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.61 installs=224458 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.27 sendable=75.17 stage=QUALIFIED_CANDIDATE_ONLY quality=87.55 mvp=78.16 installs=2909206 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=72.01 sendable=74.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.89 installs=62706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=77.09 sendable=74.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=156285 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=73.45 sendable=74.65 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.96 installs=99993 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.65 sendable=73.81 stage=QUALIFIED_CANDIDATE_ONLY quality=87.84 mvp=75.63 installs=3008966 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.03 sendable=73.42 stage=QUALIFIED_CANDIDATE_ONLY quality=84.81 mvp=80.13 installs=2200325 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=76.47 sendable=73.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.57 installs=480149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.81 sendable=72.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.96 installs=520318 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.68 sendable=72.7 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.61 installs=132465 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.3 sendable=72.65 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.68 installs=5054192 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.3 sendable=72.65 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.07 installs=75059 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=70.81 sendable=72.2 stage=QUALIFIED_CANDIDATE_ONLY quality=85.58 mvp=85.0 installs=44441 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.89 sendable=70.23 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=898853 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
