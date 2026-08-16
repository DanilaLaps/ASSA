# Alert Funnel - 2026-08-16

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 95
- NEAR_MISS: 113
- REJECT: 199
- SINGLE_APP_WATCH: 14
- WATCH: 153

## Alert Stage Counts
- COOLDOWN_BLOCKED: 63
- NONE: 479
- QUALIFIED_CANDIDATE_ONLY: 31
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 63
- duplicate_market_signals_suppressed: 132
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 298
- below_data_quality_score: 298
- below_mvp_feasibility: 191
- below_opportunity_score: 458
- below_sendable_alert_score: 572
- below_team_fit_score: 348
- below_trend_confidence_score: 328
- blocked_risk_tag: 122
- complex_full_product: 259
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 63
- duplicate_market_signal: 132
- giant_developer_competition: 29
- giant_developer_penalty: 25
- giant_share_too_high: 20
- growth_by_one_app_too_high: 264
- high_mvp_complexity: 122
- high_production_complexity: 62
- leader_dominated_market: 221
- low_classification_confidence: 177
- low_developer_diversity: 152
- low_mvp_feasibility: 191
- low_total_daily_installs: 151
- low_total_daily_installs_for_trend_confidence: 151
- market_signal_duplicate: 9
- no_growth_history: 1
- not_alert_status: 479
- one_app_growth_penalty: 298
- organic_confidence_low: 226
- other_niche_low_confidence: 58
- severe_paid_spike_penalty: 119
- single_app_breakout_not_regular_alert: 151
- single_developer_dominance: 204
- single_developer_penalty: 251
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 224
- too_few_apps_for_trend_confidence: 224
- too_few_successful_new_apps: 151
- too_few_successful_new_apps_for_trend_confidence: 151
- too_few_unique_developers: 152
- top3_too_dominant: 335
- top_app_concentration_penalty: 277
- top_app_too_dominant: 277
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT block_puzzle score=89.44 sendable=80.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=877122 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.64 sendable=80.23 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=133218 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.34 sendable=79.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=270246 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.58 sendable=78.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.62 installs=126567 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.55 sendable=78.82 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.81 installs=1143848 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.92 sendable=78.67 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=72779 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=89.12 sendable=78.44 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=929124 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.64 sendable=78.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=351750 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.45 sendable=77.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.46 installs=910064 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.04 sendable=77.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.96 installs=926648 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.01 sendable=77.71 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.61 installs=176951 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=78.82 sendable=77.15 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.0 installs=58252 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.73 sendable=76.95 stage=COOLDOWN_BLOCKED quality=94.63 mvp=65.0 installs=35219 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=77.16 sendable=76.76 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=11049 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=82.68 sendable=76.52 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.59 installs=271498 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.87 sendable=76.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1229374 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=83.9 sendable=76.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.08 installs=287096 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.2 sendable=75.54 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=27761 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=80.17 sendable=75.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.33 installs=156168 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=77.71 sendable=74.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.67 installs=211690 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
