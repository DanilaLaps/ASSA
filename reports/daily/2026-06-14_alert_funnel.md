# Alert Funnel - 2026-06-14

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 77
- NEAR_MISS: 80
- REJECT: 181
- SINGLE_APP_WATCH: 14
- WATCH: 243

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 518
- QUALIFIED_CANDIDATE_ONLY: 75
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 105
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 74
- unknown_pattern_blocker_active: 74

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 302
- below_data_quality_score: 302
- below_mvp_feasibility: 202
- below_opportunity_score: 544
- below_sendable_alert_score: 594
- below_team_fit_score: 380
- below_trend_confidence_score: 343
- blocked_risk_tag: 100
- complex_full_product: 288
- cooldown_normalized_niche: 1
- duplicate_market_signal: 105
- giant_developer_competition: 23
- giant_developer_penalty: 22
- giant_share_too_high: 12
- growth_by_one_app_too_high: 289
- high_mvp_complexity: 132
- high_production_complexity: 54
- leader_dominated_market: 193
- low_classification_confidence: 193
- low_developer_diversity: 117
- low_mvp_feasibility: 202
- low_total_daily_installs: 111
- low_total_daily_installs_for_trend_confidence: 111
- market_signal_duplicate: 11
- no_growth_history: 1
- not_alert_status: 518
- one_app_growth_penalty: 318
- organic_confidence_low: 200
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 96
- single_app_breakout_not_regular_alert: 116
- single_developer_dominance: 174
- single_developer_penalty: 218
- single_developer_share_too_high: 194
- too_few_apps_for_sendable: 197
- too_few_apps_for_trend_confidence: 197
- too_few_successful_new_apps: 116
- too_few_successful_new_apps_for_trend_confidence: 116
- too_few_unique_developers: 117
- top3_too_dominant: 330
- top_app_concentration_penalty: 235
- top_app_too_dominant: 235
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.79 sendable=82.39 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=538844 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.67 sendable=78.94 stage=QUALIFIED_CANDIDATE_ONLY quality=94.45 mvp=85.0 installs=51681 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=74.22 sendable=77.54 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=374125 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=75.07 sendable=76.95 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=442250 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=80.22 sendable=76.36 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1137447 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.41 sendable=75.71 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=822950 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.3 sendable=75.61 stage=QUALIFIED_CANDIDATE_ONLY quality=93.27 mvp=85.0 installs=67866 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.07 sendable=75.5 stage=QUALIFIED_CANDIDATE_ONLY quality=86.47 mvp=79.82 installs=1780873 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.23 sendable=75.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.82 installs=2667743 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.36 sendable=74.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.58 installs=193468 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=73.61 sendable=74.82 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=63049 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.9 sendable=74.71 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=298871 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.73 sendable=73.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=82.92 installs=60326 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.62 sendable=72.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.95 installs=127416 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=73.39 sendable=72.55 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.46 installs=94442 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=81.06 sendable=71.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=2145013 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.74 sendable=71.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=139366 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=75.81 sendable=70.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=240027 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.1 sendable=70.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.71 installs=4514137 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=77.96 sendable=69.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.19 installs=941915 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
