# Alert Funnel - 2026-07-24

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 90
- NEAR_MISS: 120
- REJECT: 180
- SINGLE_APP_WATCH: 15
- WATCH: 182

## Alert Stage Counts
- COOLDOWN_BLOCKED: 61
- NONE: 497
- QUALIFIED_CANDIDATE_ONLY: 28
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 61
- duplicate_market_signals_suppressed: 122
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 186
- below_data_quality_for_trend_confidence: 300
- below_data_quality_score: 300
- below_mvp_feasibility: 197
- below_opportunity_score: 481
- below_sendable_alert_score: 581
- below_team_fit_score: 359
- below_trend_confidence_score: 341
- blocked_risk_tag: 105
- complex_full_product: 276
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 61
- duplicate_market_signal: 122
- giant_developer_competition: 28
- giant_developer_penalty: 27
- giant_share_too_high: 12
- growth_by_one_app_too_high: 299
- high_mvp_complexity: 128
- high_production_complexity: 53
- leader_dominated_market: 219
- low_classification_confidence: 186
- low_developer_diversity: 122
- low_mvp_feasibility: 197
- low_total_daily_installs: 116
- low_total_daily_installs_for_trend_confidence: 116
- market_signal_duplicate: 5
- no_growth_history: 4
- not_alert_status: 497
- one_app_growth_penalty: 325
- organic_confidence_low: 220
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 100
- single_app_breakout_not_regular_alert: 122
- single_developer_dominance: 201
- single_developer_penalty: 236
- single_developer_share_too_high: 219
- too_few_apps_for_sendable: 203
- too_few_apps_for_trend_confidence: 203
- too_few_successful_new_apps: 122
- too_few_successful_new_apps_for_trend_confidence: 122
- too_few_unique_developers: 122
- top3_too_dominant: 330
- top_app_concentration_penalty: 255
- top_app_too_dominant: 255
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT sort_puzzle score=82.52 sendable=83.5 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49837 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.22 sendable=83.18 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=33370 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.12 sendable=81.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=939529 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.94 sendable=81.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.87 installs=992642 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.69 sendable=81.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=650788 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.98 sendable=80.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1287788 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.07 sendable=79.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.67 installs=318602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.0 sendable=79.53 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=13643 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=88.15 sendable=79.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.33 installs=1596725 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.03 sendable=79.02 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1190435 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.74 sendable=78.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.37 installs=1113348 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.84 sendable=77.42 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=32703 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.4 sendable=77.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.08 installs=1449658 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.71 sendable=76.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=215815 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=83.37 sendable=76.11 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=45969 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.05 sendable=75.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=410330 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.69 sendable=74.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.4 installs=3970609 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.39 sendable=74.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=2010301 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT hidden_object score=80.88 sendable=73.88 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=109359 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT merge score=80.54 sendable=73.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.83 installs=95037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
