# Alert Funnel - 2026-08-09

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 94
- NEAR_MISS: 120
- REJECT: 215
- SINGLE_APP_WATCH: 9
- WATCH: 147

## Alert Stage Counts
- COOLDOWN_BLOCKED: 67
- NONE: 491
- QUALIFIED_CANDIDATE_ONLY: 26
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 67
- duplicate_market_signals_suppressed: 133
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 310
- below_data_quality_score: 310
- below_mvp_feasibility: 197
- below_opportunity_score: 470
- below_sendable_alert_score: 583
- below_team_fit_score: 360
- below_trend_confidence_score: 341
- blocked_risk_tag: 148
- complex_full_product: 268
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 67
- duplicate_market_signal: 133
- giant_developer_competition: 29
- giant_developer_penalty: 28
- giant_share_too_high: 18
- growth_by_one_app_too_high: 309
- high_mvp_complexity: 132
- high_production_complexity: 66
- leader_dominated_market: 228
- low_classification_confidence: 177
- low_developer_diversity: 155
- low_mvp_feasibility: 197
- low_total_daily_installs: 145
- low_total_daily_installs_for_trend_confidence: 145
- market_signal_duplicate: 6
- no_growth_history: 2
- not_alert_status: 491
- one_app_growth_penalty: 346
- organic_confidence_low: 240
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 144
- single_app_breakout_not_regular_alert: 155
- single_developer_dominance: 216
- single_developer_penalty: 249
- single_developer_share_too_high: 229
- too_few_apps_for_sendable: 232
- too_few_apps_for_trend_confidence: 232
- too_few_successful_new_apps: 155
- too_few_successful_new_apps_for_trend_confidence: 155
- too_few_unique_developers: 155
- top3_too_dominant: 346
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.47 sendable=83.09 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=42624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.96 sendable=81.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1058916 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.8 sendable=79.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=833562 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.98 sendable=78.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=52164 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.43 sendable=77.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=356226 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.38 sendable=77.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.71 installs=1173700 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.58 sendable=77.64 stage=COOLDOWN_BLOCKED quality=92.88 mvp=65.0 installs=40985 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=85.31 sendable=77.59 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=117567 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=89.45 sendable=76.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=678657 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=71.12 sendable=76.24 stage=COOLDOWN_BLOCKED quality=90.73 mvp=85.0 installs=13107 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=83.05 sendable=75.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.36 installs=78197 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.92 sendable=75.6 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=300298 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.52 sendable=75.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.69 installs=891340 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.6 sendable=75.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.74 installs=682789 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.55 sendable=75.18 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=21077 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=86.63 sendable=74.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1093274 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.21 sendable=74.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=186412 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.54 sendable=74.06 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=23188 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=72.72 sendable=73.83 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=20464 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=77.32 sendable=73.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.0 installs=55494 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
