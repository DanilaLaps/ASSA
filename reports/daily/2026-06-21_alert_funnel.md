# Alert Funnel - 2026-06-21

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 86
- NEAR_MISS: 120
- REJECT: 201
- SINGLE_APP_WATCH: 15
- WATCH: 181

## Alert Stage Counts
- COOLDOWN_BLOCKED: 50
- NONE: 517
- QUALIFIED_CANDIDATE_ONLY: 35
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 50
- duplicate_market_signals_suppressed: 105
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 192
- below_data_quality_for_trend_confidence: 308
- below_data_quality_score: 308
- below_mvp_feasibility: 204
- below_opportunity_score: 502
- below_sendable_alert_score: 597
- below_team_fit_score: 373
- below_trend_confidence_score: 366
- blocked_risk_tag: 105
- complex_full_product: 278
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 50
- duplicate_market_signal: 105
- giant_developer_competition: 32
- giant_developer_penalty: 29
- giant_share_too_high: 20
- growth_by_one_app_too_high: 297
- high_mvp_complexity: 131
- high_production_complexity: 60
- leader_dominated_market: 219
- low_classification_confidence: 192
- low_developer_diversity: 132
- low_mvp_feasibility: 204
- low_total_daily_installs: 139
- low_total_daily_installs_for_trend_confidence: 139
- market_signal_duplicate: 7
- no_growth_history: 3
- not_alert_status: 517
- one_app_growth_penalty: 325
- organic_confidence_low: 220
- other_niche_low_confidence: 69
- severe_paid_spike_penalty: 97
- single_app_breakout_not_regular_alert: 132
- single_developer_dominance: 195
- single_developer_penalty: 251
- single_developer_share_too_high: 219
- too_few_apps_for_sendable: 215
- too_few_apps_for_trend_confidence: 215
- too_few_successful_new_apps: 132
- too_few_successful_new_apps_for_trend_confidence: 132
- too_few_unique_developers: 132
- top3_too_dominant: 353
- top_app_concentration_penalty: 276
- top_app_too_dominant: 276
- unknown_pattern_blocker_active: 75

## Top Qualified But Not Sent
- ALERT sort_puzzle score=90.25 sendable=86.58 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=516420 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=83.11 sendable=84.06 stage=COOLDOWN_BLOCKED quality=94.76 mvp=85.0 installs=62839 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=86.4 sendable=80.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1022785 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.89 sendable=80.87 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=64621 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.66 sendable=80.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=745873 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.1 sendable=80.25 stage=COOLDOWN_BLOCKED quality=92.41 mvp=85.0 installs=34731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=top3_too_dominant risks=unknown_coverage
- ALERT tile_match score=83.66 sendable=79.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.68 installs=882351 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=88.59 sendable=78.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=614637 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.88 sendable=78.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=179211 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.7 sendable=78.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.37 installs=902672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.9 sendable=77.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.42 installs=3850278 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.29 sendable=77.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=959358 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.38 sendable=77.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.96 installs=1601804 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.14 sendable=77.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.88 installs=105425 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=84.23 sendable=76.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.89 installs=102165 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.87 sendable=76.64 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.75 installs=57449 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.4 sendable=76.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.91 installs=1919179 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.44 sendable=75.22 stage=COOLDOWN_BLOCKED quality=88.38 mvp=85.0 installs=48896 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT tile_match score=78.93 sendable=74.64 stage=COOLDOWN_BLOCKED quality=85.79 mvp=74.88 installs=43977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.25 sendable=74.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=260017 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
