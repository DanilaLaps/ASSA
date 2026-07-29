# Alert Funnel - 2026-07-29

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 95
- NEAR_MISS: 110
- REJECT: 209
- SINGLE_APP_WATCH: 5
- WATCH: 172

## Alert Stage Counts
- COOLDOWN_BLOCKED: 54
- NONE: 496
- QUALIFIED_CANDIDATE_ONLY: 40
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 54
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 192
- below_data_quality_for_trend_confidence: 309
- below_data_quality_score: 309
- below_mvp_feasibility: 200
- below_opportunity_score: 480
- below_sendable_alert_score: 583
- below_team_fit_score: 362
- below_trend_confidence_score: 335
- blocked_risk_tag: 128
- complex_full_product: 274
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 54
- duplicate_market_signal: 119
- giant_developer_competition: 34
- giant_developer_penalty: 29
- giant_share_too_high: 21
- growth_by_one_app_too_high: 301
- high_mvp_complexity: 129
- high_production_complexity: 54
- leader_dominated_market: 221
- low_classification_confidence: 192
- low_developer_diversity: 128
- low_mvp_feasibility: 200
- low_total_daily_installs: 122
- low_total_daily_installs_for_trend_confidence: 122
- market_signal_duplicate: 8
- no_growth_history: 1
- not_alert_status: 496
- one_app_growth_penalty: 322
- organic_confidence_low: 220
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 125
- single_app_breakout_not_regular_alert: 128
- single_developer_dominance: 202
- single_developer_penalty: 246
- single_developer_share_too_high: 222
- too_few_apps_for_sendable: 210
- too_few_apps_for_trend_confidence: 210
- too_few_successful_new_apps: 128
- too_few_successful_new_apps_for_trend_confidence: 128
- too_few_unique_developers: 128
- top3_too_dominant: 338
- top_app_concentration_penalty: 270
- top_app_too_dominant: 270
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT coloring score=90.77 sendable=88.18 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=941842 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=85.39 sendable=84.63 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=87238 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=84.01 sendable=81.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=53780 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.34 sendable=80.83 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=227732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.25 sendable=80.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=790727 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.88 sendable=80.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=448212 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.08 sendable=80.66 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=40490 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=86.94 sendable=80.62 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=392438 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.23 sendable=79.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=747810 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.55 sendable=79.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.69 installs=314888 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.14 sendable=79.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.46 installs=1145503 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.77 sendable=79.16 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.77 installs=3496295 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.96 sendable=79.08 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=107112 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=89.29 sendable=78.92 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.88 installs=1086852 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.43 sendable=78.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.2 installs=1449006 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.23 sendable=78.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.55 installs=1440741 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.86 sendable=78.43 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=13789 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=76.78 sendable=77.82 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=34347 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=90.16 sendable=76.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1262363 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.48 sendable=76.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=114595 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
