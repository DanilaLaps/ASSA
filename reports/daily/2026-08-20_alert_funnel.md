# Alert Funnel - 2026-08-20

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 92
- NEAR_MISS: 116
- REJECT: 212
- SINGLE_APP_WATCH: 18
- WATCH: 178

## Alert Stage Counts
- COOLDOWN_BLOCKED: 31
- NONE: 524
- QUALIFIED_CANDIDATE_ONLY: 60
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 31
- duplicate_market_signals_suppressed: 118
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 325
- below_data_quality_score: 325
- below_mvp_feasibility: 198
- below_opportunity_score: 502
- below_sendable_alert_score: 614
- below_team_fit_score: 370
- below_trend_confidence_score: 367
- blocked_risk_tag: 124
- complex_full_product: 273
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 31
- duplicate_market_signal: 118
- giant_developer_competition: 33
- giant_developer_penalty: 30
- giant_share_too_high: 23
- growth_by_one_app_too_high: 317
- high_mvp_complexity: 122
- high_production_complexity: 62
- leader_dominated_market: 247
- low_classification_confidence: 193
- low_developer_diversity: 159
- low_mvp_feasibility: 198
- low_total_daily_installs: 132
- low_total_daily_installs_for_trend_confidence: 132
- market_signal_duplicate: 3
- no_growth_history: 1
- not_alert_status: 524
- one_app_growth_penalty: 344
- organic_confidence_low: 235
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 123
- single_app_breakout_not_regular_alert: 158
- single_developer_dominance: 224
- single_developer_penalty: 270
- single_developer_share_too_high: 249
- too_few_apps_for_sendable: 231
- too_few_apps_for_trend_confidence: 231
- too_few_successful_new_apps: 158
- too_few_successful_new_apps_for_trend_confidence: 158
- too_few_unique_developers: 159
- top3_too_dominant: 353
- top_app_concentration_penalty: 290
- top_app_too_dominant: 290
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=77.32 sendable=82.5 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=19254 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.67 sendable=81.94 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.34 installs=2501313 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.03 sendable=79.78 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=246200 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=86.86 sendable=79.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1087614 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.0 sendable=78.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.8 installs=1572126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.05 sendable=78.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1591720 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.97 sendable=78.21 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=63044 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.76 sendable=78.06 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.88 installs=5267768 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.72 sendable=78.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=207184 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.57 sendable=77.91 stage=COOLDOWN_BLOCKED quality=95.0 mvp=84.8 installs=731470 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.06 sendable=77.78 stage=COOLDOWN_BLOCKED quality=94.25 mvp=65.0 installs=59493 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=84.32 sendable=76.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.33 installs=187251 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=72.13 sendable=74.88 stage=COOLDOWN_BLOCKED quality=86.46 mvp=85.0 installs=7385 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.26 sendable=74.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=2023841 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.36 sendable=74.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=118655 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT coloring score=77.22 sendable=74.53 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=39220 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.74 sendable=74.46 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=59203 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=85.68 sendable=74.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=527942 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.2 sendable=73.46 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=63765 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sandbox score=79.22 sendable=73.08 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.9 installs=98792 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
