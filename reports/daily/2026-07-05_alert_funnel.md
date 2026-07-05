# Alert Funnel - 2026-07-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 118
- NEAR_MISS: 113
- REJECT: 201
- SINGLE_APP_WATCH: 4
- WATCH: 141

## Alert Stage Counts
- COOLDOWN_BLOCKED: 60
- NONE: 459
- QUALIFIED_CANDIDATE_ONLY: 57
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 60
- duplicate_market_signals_suppressed: 129
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 176
- below_data_quality_for_trend_confidence: 252
- below_data_quality_score: 252
- below_mvp_feasibility: 189
- below_opportunity_score: 455
- below_sendable_alert_score: 569
- below_team_fit_score: 363
- below_trend_confidence_score: 247
- blocked_risk_tag: 145
- complex_full_product: 258
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 60
- duplicate_market_signal: 129
- giant_developer_competition: 32
- giant_developer_penalty: 27
- giant_share_too_high: 20
- growth_by_one_app_too_high: 226
- high_mvp_complexity: 119
- high_production_complexity: 59
- leader_dominated_market: 220
- low_classification_confidence: 176
- low_developer_diversity: 140
- low_mvp_feasibility: 189
- low_total_daily_installs: 134
- low_total_daily_installs_for_trend_confidence: 134
- market_signal_duplicate: 11
- no_growth_history: 1
- not_alert_status: 459
- one_app_growth_penalty: 247
- organic_confidence_low: 220
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 141
- single_app_breakout_not_regular_alert: 139
- single_developer_dominance: 203
- single_developer_penalty: 237
- single_developer_share_too_high: 221
- too_few_apps_for_sendable: 217
- too_few_apps_for_trend_confidence: 217
- too_few_successful_new_apps: 139
- too_few_successful_new_apps_for_trend_confidence: 139
- too_few_unique_developers: 140
- top3_too_dominant: 331
- top_app_concentration_penalty: 264
- top_app_too_dominant: 264
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT coloring score=89.42 sendable=82.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=736450 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.85 sendable=82.22 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1200536 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.83 sendable=81.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=777624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.99 sendable=80.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.39 installs=1299952 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.48 sendable=80.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.23 installs=1285809 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.82 sendable=80.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=194392 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.58 sendable=80.18 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=234665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.7 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.09 installs=857898 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.01 sendable=79.65 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.44 installs=3344360 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.04 sendable=79.62 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.05 installs=1117061 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.03 sendable=78.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.55 installs=117117 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.67 sendable=78.12 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=228966 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.6 sendable=77.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=750645 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=76.18 sendable=77.11 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.23 installs=52213 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.59 sendable=75.58 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.95 installs=986778 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=76.32 sendable=75.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.2 installs=49178 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.31 sendable=75.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.95 installs=772768 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sandbox score=86.31 sendable=75.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.58 installs=921408 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.96 sendable=75.34 stage=COOLDOWN_BLOCKED quality=84.67 mvp=85.0 installs=34257 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=81.3 sendable=75.0 stage=COOLDOWN_BLOCKED quality=84.35 mvp=80.85 installs=60003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
