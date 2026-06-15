# Alert Funnel - 2026-06-15

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 59
- NEAR_MISS: 74
- REJECT: 167
- SINGLE_APP_WATCH: 17
- WATCH: 271

## Alert Stage Counts
- COOLDOWN_BLOCKED: 7
- NONE: 529
- QUALIFIED_CANDIDATE_ONLY: 51
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 7
- duplicate_market_signals_suppressed: 105
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 189
- below_data_quality_for_trend_confidence: 315
- below_data_quality_score: 315
- below_mvp_feasibility: 204
- below_opportunity_score: 549
- below_sendable_alert_score: 588
- below_team_fit_score: 373
- below_trend_confidence_score: 398
- blocked_risk_tag: 89
- complex_full_product: 277
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 7
- duplicate_market_signal: 105
- giant_developer_competition: 27
- giant_developer_penalty: 24
- giant_share_too_high: 11
- growth_by_one_app_too_high: 305
- high_mvp_complexity: 126
- high_production_complexity: 53
- leader_dominated_market: 194
- low_classification_confidence: 189
- low_developer_diversity: 122
- low_mvp_feasibility: 204
- low_total_daily_installs: 119
- low_total_daily_installs_for_trend_confidence: 119
- market_signal_duplicate: 7
- no_growth_history: 2
- not_alert_status: 529
- one_app_growth_penalty: 327
- organic_confidence_low: 191
- other_niche_low_confidence: 67
- severe_paid_spike_penalty: 85
- single_app_breakout_not_regular_alert: 121
- single_developer_dominance: 174
- single_developer_penalty: 215
- single_developer_share_too_high: 196
- too_few_apps_for_sendable: 197
- too_few_apps_for_trend_confidence: 197
- too_few_successful_new_apps: 121
- too_few_successful_new_apps_for_trend_confidence: 121
- too_few_unique_developers: 122
- top3_too_dominant: 327
- top_app_concentration_penalty: 234
- top_app_too_dominant: 234
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT sort_puzzle score=73.14 sendable=79.33 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49552 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.22 sendable=78.13 stage=COOLDOWN_BLOCKED quality=92.61 mvp=85.0 installs=23067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.62 sendable=75.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=742295 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.56 sendable=74.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=290590 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.97 sendable=73.59 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=881091 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.98 sendable=73.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.62 installs=3948560 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.1 sendable=73.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.71 installs=2316298 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=74.22 sendable=73.18 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=287163 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.25 sendable=72.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.46 installs=101478 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.3 sendable=72.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=767068 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=75.11 sendable=72.21 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=338305 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.25 sendable=71.5 stage=COOLDOWN_BLOCKED quality=93.71 mvp=85.0 installs=40787 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.55 sendable=70.88 stage=COOLDOWN_BLOCKED quality=94.97 mvp=85.0 installs=57688 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.52 sendable=70.62 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=172551 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.72 sendable=68.06 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=117607 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.08 sendable=67.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.43 installs=839952 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=75.91 sendable=66.61 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.84 installs=307236 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT merge score=76.99 sendable=65.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.12 installs=402663 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=73.71 sendable=65.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.4 installs=459498 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=76.15 sendable=65.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=368627 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
