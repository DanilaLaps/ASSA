# Alert Funnel - 2026-07-06

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 113
- NEAR_MISS: 106
- REJECT: 206
- SINGLE_APP_WATCH: 10
- WATCH: 133

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 455
- QUALIFIED_CANDIDATE_ONLY: 111
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 138
- limit_blocked: 1

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 179
- below_data_quality_for_trend_confidence: 264
- below_data_quality_score: 264
- below_mvp_feasibility: 194
- below_opportunity_score: 449
- below_sendable_alert_score: 565
- below_team_fit_score: 346
- below_trend_confidence_score: 274
- blocked_risk_tag: 133
- complex_full_product: 248
- cooldown_normalized_niche: 1
- duplicate_market_signal: 138
- giant_developer_competition: 31
- giant_developer_penalty: 30
- giant_share_too_high: 23
- growth_by_one_app_too_high: 231
- high_mvp_complexity: 116
- high_production_complexity: 61
- leader_dominated_market: 207
- low_classification_confidence: 179
- low_developer_diversity: 139
- low_mvp_feasibility: 194
- low_total_daily_installs: 151
- low_total_daily_installs_for_trend_confidence: 151
- market_signal_duplicate: 14
- no_growth_history: 1
- not_alert_status: 455
- one_app_growth_penalty: 263
- organic_confidence_low: 221
- other_niche_low_confidence: 60
- per_niche_limit_blocked: 1
- severe_paid_spike_penalty: 129
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 193
- single_developer_penalty: 232
- single_developer_share_too_high: 210
- too_few_apps_for_sendable: 213
- too_few_apps_for_trend_confidence: 213
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 139
- top3_too_dominant: 314
- top_app_concentration_penalty: 247
- top_app_too_dominant: 247
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT tile_match score=88.79 sendable=80.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=465889 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.38 sendable=80.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=139115 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=82.93 sendable=79.41 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=80576 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.46 sendable=78.6 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=23734 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=87.67 sendable=78.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.4 installs=787436 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.6 sendable=78.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.81 installs=351054 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=87.53 sendable=77.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=127114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=82.47 sendable=77.37 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=58427 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.77 sendable=76.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=672292 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=87.5 sendable=76.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=471823 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=79.78 sendable=75.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.21 installs=24592 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=72.65 sendable=75.74 stage=QUALIFIED_CANDIDATE_ONLY quality=92.48 mvp=65.0 installs=7782 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=88.21 sendable=75.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=357309 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.2 sendable=75.42 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=113833 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.1 sendable=74.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.63 installs=669329 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.3 sendable=74.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.07 installs=40588 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.61 sendable=74.43 stage=QUALIFIED_CANDIDATE_ONLY quality=91.0 mvp=85.0 installs=38302 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT sandbox score=86.97 sendable=73.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.2 installs=626734 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.45 sendable=73.71 stage=QUALIFIED_CANDIDATE_ONLY quality=87.73 mvp=85.0 installs=705867 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=80.54 sendable=73.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.62 installs=119087 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
