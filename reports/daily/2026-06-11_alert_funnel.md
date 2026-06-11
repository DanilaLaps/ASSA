# Alert Funnel - 2026-06-11

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 64
- NEAR_MISS: 78
- REJECT: 183
- SINGLE_APP_WATCH: 13
- WATCH: 252

## Alert Stage Counts
- NONE: 526
- QUALIFIED_CANDIDATE_ONLY: 63
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 102
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 74
- unknown_pattern_blocker_active: 74

## Sendable Failure Distribution
- below_classification_confidence: 191
- below_data_quality_for_trend_confidence: 292
- below_data_quality_score: 292
- below_mvp_feasibility: 211
- below_opportunity_score: 557
- below_sendable_alert_score: 588
- below_team_fit_score: 372
- below_trend_confidence_score: 376
- blocked_risk_tag: 108
- complex_full_product: 286
- duplicate_market_signal: 102
- giant_developer_competition: 27
- giant_developer_penalty: 21
- giant_share_too_high: 16
- growth_by_one_app_too_high: 303
- high_mvp_complexity: 140
- high_production_complexity: 60
- leader_dominated_market: 207
- low_classification_confidence: 191
- low_developer_diversity: 126
- low_mvp_feasibility: 211
- low_total_daily_installs: 111
- low_total_daily_installs_for_trend_confidence: 111
- market_signal_duplicate: 6
- no_growth_history: 1
- not_alert_status: 526
- one_app_growth_penalty: 329
- organic_confidence_low: 199
- other_niche_low_confidence: 70
- severe_paid_spike_penalty: 104
- single_app_breakout_not_regular_alert: 125
- single_developer_dominance: 184
- single_developer_penalty: 231
- single_developer_share_too_high: 209
- too_few_apps_for_sendable: 198
- too_few_apps_for_trend_confidence: 198
- too_few_successful_new_apps: 125
- too_few_successful_new_apps_for_trend_confidence: 125
- too_few_unique_developers: 126
- top3_too_dominant: 324
- top_app_concentration_penalty: 249
- top_app_too_dominant: 249
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT sort_puzzle score=72.25 sendable=81.83 stage=QUALIFIED_CANDIDATE_ONLY quality=94.97 mvp=85.0 installs=62229 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.02 sendable=76.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=855141 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.7 sendable=75.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.61 installs=204814 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.67 sendable=75.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=866378 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.58 sendable=75.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=574750 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.66 sendable=75.28 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=320495 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.12 sendable=75.17 stage=QUALIFIED_CANDIDATE_ONLY quality=86.3 mvp=80.03 installs=1799136 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.52 sendable=74.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.83 installs=2582492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=73.41 sendable=74.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.91 installs=89365 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.75 sendable=73.83 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=85531 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.56 sendable=72.68 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.8 installs=118199 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=76.37 sendable=72.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.43 installs=440279 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=77.58 sendable=71.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.06 installs=905199 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.25 sendable=70.03 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.69 installs=4386556 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=70.8 sendable=69.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.94 installs=42500 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.87 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.07 installs=64498 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=70.84 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=48827 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=75.84 sendable=69.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=228013 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=75.25 sendable=68.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.75 installs=534744 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=70.55 sendable=68.01 stage=QUALIFIED_CANDIDATE_ONLY quality=87.25 mvp=85.0 installs=36078 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
