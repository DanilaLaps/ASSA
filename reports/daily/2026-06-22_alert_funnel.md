# Alert Funnel - 2026-06-22

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 89
- NEAR_MISS: 118
- REJECT: 176
- SINGLE_APP_WATCH: 19
- WATCH: 192

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 505
- QUALIFIED_CANDIDATE_ONLY: 86
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 110
- limit_blocked: 2

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 181
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 201
- below_opportunity_score: 489
- below_sendable_alert_score: 589
- below_team_fit_score: 372
- below_trend_confidence_score: 344
- blocked_risk_tag: 97
- complex_full_product: 282
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 1
- duplicate_market_signal: 110
- giant_developer_competition: 28
- giant_developer_penalty: 21
- giant_share_too_high: 16
- growth_by_one_app_too_high: 271
- high_mvp_complexity: 127
- high_production_complexity: 58
- leader_dominated_market: 209
- low_classification_confidence: 181
- low_developer_diversity: 133
- low_mvp_feasibility: 201
- low_total_daily_installs: 135
- low_total_daily_installs_for_trend_confidence: 135
- market_signal_duplicate: 11
- no_growth_history: 2
- not_alert_status: 505
- one_app_growth_penalty: 297
- organic_confidence_low: 209
- other_niche_low_confidence: 66
- per_niche_limit_blocked: 2
- severe_paid_spike_penalty: 92
- single_app_breakout_not_regular_alert: 133
- single_developer_dominance: 190
- single_developer_penalty: 232
- single_developer_share_too_high: 210
- too_few_apps_for_sendable: 206
- too_few_apps_for_trend_confidence: 206
- too_few_successful_new_apps: 133
- too_few_successful_new_apps_for_trend_confidence: 133
- too_few_unique_developers: 133
- top3_too_dominant: 336
- top_app_concentration_penalty: 257
- top_app_too_dominant: 257
- unknown_pattern_blocker_active: 73

## Top Qualified But Not Sent
- ALERT sort_puzzle score=83.09 sendable=85.56 stage=QUALIFIED_CANDIDATE_ONLY quality=94.68 mvp=85.0 installs=62280 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=84.85 sendable=84.62 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=54529 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT tile_match score=87.31 sendable=80.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=849067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.04 sendable=79.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.67 installs=823383 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.46 sendable=79.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=794089 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.36 sendable=79.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=237304 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.45 sendable=79.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=640602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.64 sendable=79.15 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.55 installs=155577 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.22 sendable=78.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.97 installs=1394965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.8 sendable=78.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.07 installs=1634983 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.73 sendable=78.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=101913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.54 sendable=77.86 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=47280 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=85.74 sendable=77.6 stage=QUALIFIED_CANDIDATE_ONLY quality=94.8 mvp=65.0 installs=192085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=72.62 sendable=77.56 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=13152 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=84.93 sendable=77.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.0 installs=99041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.69 sendable=77.11 stage=QUALIFIED_CANDIDATE_ONLY quality=87.8 mvp=82.92 installs=52989 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=82.62 sendable=76.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.05 installs=92114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.61 sendable=74.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.23 mvp=85.0 installs=48195 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT sort_puzzle score=80.42 sendable=73.43 stage=QUALIFIED_CANDIDATE_ONLY quality=86.4 mvp=85.0 installs=27514 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.14 sendable=72.96 stage=QUALIFIED_CANDIDATE_ONLY quality=91.39 mvp=65.0 installs=36486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
