# Alert Funnel - 2026-06-16

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 70
- NEAR_MISS: 70
- REJECT: 177
- SINGLE_APP_WATCH: 25
- WATCH: 245

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 517
- QUALIFIED_CANDIDATE_ONLY: 61
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 8
- duplicate_market_signals_suppressed: 100
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 188
- below_data_quality_for_trend_confidence: 303
- below_data_quality_score: 303
- below_mvp_feasibility: 207
- below_opportunity_score: 551
- below_sendable_alert_score: 587
- below_team_fit_score: 369
- below_trend_confidence_score: 372
- blocked_risk_tag: 94
- complex_full_product: 277
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 8
- duplicate_market_signal: 100
- giant_developer_competition: 36
- giant_developer_penalty: 30
- giant_share_too_high: 17
- growth_by_one_app_too_high: 293
- high_mvp_complexity: 130
- high_production_complexity: 53
- leader_dominated_market: 201
- low_classification_confidence: 188
- low_developer_diversity: 123
- low_mvp_feasibility: 207
- low_total_daily_installs: 116
- low_total_daily_installs_for_trend_confidence: 116
- market_signal_duplicate: 5
- no_growth_history: 5
- not_alert_status: 517
- one_app_growth_penalty: 320
- organic_confidence_low: 203
- other_niche_low_confidence: 69
- severe_paid_spike_penalty: 88
- single_app_breakout_not_regular_alert: 123
- single_developer_dominance: 183
- single_developer_penalty: 224
- single_developer_share_too_high: 203
- too_few_apps_for_sendable: 196
- too_few_apps_for_trend_confidence: 196
- too_few_successful_new_apps: 123
- too_few_successful_new_apps_for_trend_confidence: 123
- too_few_unique_developers: 123
- top3_too_dominant: 324
- top_app_concentration_penalty: 248
- top_app_too_dominant: 248
- unknown_pattern_blocker_active: 75

## Top Qualified But Not Sent
- ALERT sort_puzzle score=79.5 sendable=75.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=840279 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.65 sendable=75.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=326560 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.61 sendable=74.9 stage=QUALIFIED_CANDIDATE_ONLY quality=86.67 mvp=85.0 installs=2256700 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.46 sendable=74.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.58 installs=186836 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT coloring score=79.3 sendable=74.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=528399 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.05 sendable=74.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=120457 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=77.11 sendable=73.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.61 installs=933819 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.85 sendable=73.07 stage=QUALIFIED_CANDIDATE_ONLY quality=84.82 mvp=79.81 installs=1885970 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.53 sendable=72.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.12 installs=118043 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=71.38 sendable=71.65 stage=QUALIFIED_CANDIDATE_ONLY quality=94.89 mvp=65.0 installs=183087 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=70.64 sendable=71.56 stage=COOLDOWN_BLOCKED quality=92.95 mvp=85.0 installs=28073 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT mahjong score=76.79 sendable=70.0 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=236115 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.18 sendable=67.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=64228 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=73.05 sendable=67.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.42 installs=193919 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.61 sendable=66.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1050554 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=73.05 sendable=66.39 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=232277 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.75 sendable=66.09 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.31 installs=4671370 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=78.14 sendable=65.37 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2743404 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.91 sendable=65.23 stage=COOLDOWN_BLOCKED quality=80.0 mvp=85.0 installs=59517 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.89 sendable=65.21 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.58 installs=2635190 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
