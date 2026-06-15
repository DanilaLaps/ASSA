# Alert Funnel - 2026-06-15

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 59
- NEAR_MISS: 74
- REJECT: 165
- SINGLE_APP_WATCH: 17
- WATCH: 274

## Alert Stage Counts
- NONE: 530
- QUALIFIED_CANDIDATE_ONLY: 58
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 105
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 190
- below_data_quality_for_trend_confidence: 313
- below_data_quality_score: 313
- below_mvp_feasibility: 204
- below_opportunity_score: 551
- below_sendable_alert_score: 589
- below_team_fit_score: 374
- below_trend_confidence_score: 397
- blocked_risk_tag: 90
- complex_full_product: 278
- duplicate_market_signal: 105
- giant_developer_competition: 28
- giant_developer_penalty: 25
- giant_share_too_high: 11
- growth_by_one_app_too_high: 304
- high_mvp_complexity: 126
- high_production_complexity: 53
- leader_dominated_market: 192
- low_classification_confidence: 190
- low_developer_diversity: 120
- low_mvp_feasibility: 204
- low_total_daily_installs: 119
- low_total_daily_installs_for_trend_confidence: 119
- market_signal_duplicate: 7
- no_growth_history: 2
- not_alert_status: 530
- one_app_growth_penalty: 326
- organic_confidence_low: 190
- other_niche_low_confidence: 66
- severe_paid_spike_penalty: 86
- single_app_breakout_not_regular_alert: 119
- single_developer_dominance: 172
- single_developer_penalty: 213
- single_developer_share_too_high: 194
- too_few_apps_for_sendable: 198
- too_few_apps_for_trend_confidence: 198
- too_few_successful_new_apps: 119
- too_few_successful_new_apps_for_trend_confidence: 119
- too_few_unique_developers: 120
- top3_too_dominant: 326
- top_app_concentration_penalty: 232
- top_app_too_dominant: 232
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT sort_puzzle score=71.24 sendable=78.14 stage=QUALIFIED_CANDIDATE_ONLY quality=92.61 mvp=85.0 installs=23067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.62 sendable=75.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=741245 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.51 sendable=74.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=290590 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT coloring score=79.29 sendable=73.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=453254 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.97 sendable=73.59 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=879335 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.22 sendable=73.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.71 installs=2304376 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.05 sendable=73.24 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.59 installs=3936582 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=74.18 sendable=73.16 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=287163 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.26 sendable=72.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.46 installs=101478 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.31 sendable=72.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=768753 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=75.08 sendable=72.2 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=338305 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.26 sendable=71.51 stage=QUALIFIED_CANDIDATE_ONLY quality=93.71 mvp=85.0 installs=40787 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.46 sendable=70.83 stage=QUALIFIED_CANDIDATE_ONLY quality=94.83 mvp=85.0 installs=56689 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.52 sendable=70.62 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.56 installs=172551 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.73 sendable=68.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=117607 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.08 sendable=67.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.43 installs=839735 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=75.91 sendable=66.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.76 installs=307805 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT merge score=77.02 sendable=65.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.31 installs=403619 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=73.74 sendable=65.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.28 installs=460280 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=76.15 sendable=65.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=368627 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
