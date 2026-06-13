# Alert Funnel - 2026-06-13

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 70
- NEAR_MISS: 87
- REJECT: 187
- SINGLE_APP_WATCH: 13
- WATCH: 246

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 533
- QUALIFIED_CANDIDATE_ONLY: 68
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
- below_classification_confidence: 196
- below_data_quality_for_trend_confidence: 302
- below_data_quality_score: 302
- below_mvp_feasibility: 205
- below_opportunity_score: 569
- below_sendable_alert_score: 600
- below_team_fit_score: 384
- below_trend_confidence_score: 356
- blocked_risk_tag: 118
- complex_full_product: 290
- cooldown_normalized_niche: 1
- duplicate_market_signal: 103
- giant_developer_competition: 26
- giant_developer_penalty: 25
- giant_share_too_high: 16
- growth_by_one_app_too_high: 297
- high_mvp_complexity: 135
- high_production_complexity: 56
- leader_dominated_market: 201
- low_classification_confidence: 196
- low_developer_diversity: 128
- low_mvp_feasibility: 205
- low_total_daily_installs: 110
- low_total_daily_installs_for_trend_confidence: 110
- market_signal_duplicate: 7
- no_growth_history: 4
- not_alert_status: 533
- one_app_growth_penalty: 325
- organic_confidence_low: 212
- other_niche_low_confidence: 69
- severe_paid_spike_penalty: 113
- single_app_breakout_not_regular_alert: 127
- single_developer_dominance: 186
- single_developer_penalty: 222
- single_developer_share_too_high: 202
- too_few_apps_for_sendable: 206
- too_few_apps_for_trend_confidence: 206
- too_few_successful_new_apps: 127
- too_few_successful_new_apps_for_trend_confidence: 127
- too_few_unique_developers: 128
- top3_too_dominant: 344
- top_app_concentration_penalty: 247
- top_app_too_dominant: 247
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT sort_puzzle score=72.12 sendable=80.24 stage=QUALIFIED_CANDIDATE_ONLY quality=94.89 mvp=85.0 installs=61019 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.14 sendable=80.07 stage=COOLDOWN_BLOCKED quality=93.76 mvp=85.0 installs=71414 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=73.98 sendable=76.85 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=363793 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.57 sendable=76.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.61 installs=224539 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.49 sendable=75.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=927088 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.17 sendable=75.61 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=350452 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=74.75 sendable=75.61 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=434802 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=71.84 sendable=74.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.25 installs=62790 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.88 sendable=74.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=156527 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=73.22 sendable=74.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.46 installs=95602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=76.19 sendable=74.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=268025 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.16 sendable=74.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.61 installs=5270222 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.97 sendable=74.02 stage=QUALIFIED_CANDIDATE_ONLY quality=85.03 mvp=79.86 installs=2245891 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.41 sendable=73.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=984711 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=80.19 sendable=73.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1279114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=70.8 sendable=73.32 stage=QUALIFIED_CANDIDATE_ONLY quality=85.65 mvp=85.0 installs=44718 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.31 sendable=72.85 stage=QUALIFIED_CANDIDATE_ONLY quality=91.89 mvp=85.0 installs=31390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.64 sendable=72.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.4 installs=137786 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.47 sendable=71.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.07 installs=78815 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.87 sendable=69.42 stage=QUALIFIED_CANDIDATE_ONLY quality=86.84 mvp=85.0 installs=2684961 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
