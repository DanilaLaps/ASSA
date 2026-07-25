# Alert Funnel - 2026-07-25

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 93
- NEAR_MISS: 109
- REJECT: 189
- SINGLE_APP_WATCH: 14
- WATCH: 184

## Alert Stage Counts
- COOLDOWN_BLOCKED: 64
- NONE: 496
- QUALIFIED_CANDIDATE_ONLY: 28
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 64
- duplicate_market_signals_suppressed: 120
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 307
- below_data_quality_score: 307
- below_mvp_feasibility: 200
- below_opportunity_score: 479
- below_sendable_alert_score: 583
- below_team_fit_score: 371
- below_trend_confidence_score: 335
- blocked_risk_tag: 114
- complex_full_product: 279
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 64
- duplicate_market_signal: 120
- giant_developer_competition: 30
- giant_developer_penalty: 26
- giant_share_too_high: 17
- growth_by_one_app_too_high: 292
- high_mvp_complexity: 129
- high_production_complexity: 51
- leader_dominated_market: 223
- low_classification_confidence: 185
- low_developer_diversity: 127
- low_mvp_feasibility: 200
- low_total_daily_installs: 120
- low_total_daily_installs_for_trend_confidence: 120
- market_signal_duplicate: 10
- no_growth_history: 2
- not_alert_status: 496
- one_app_growth_penalty: 318
- organic_confidence_low: 224
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 110
- single_app_breakout_not_regular_alert: 127
- single_developer_dominance: 204
- single_developer_penalty: 239
- single_developer_share_too_high: 224
- too_few_apps_for_sendable: 203
- too_few_apps_for_trend_confidence: 203
- too_few_successful_new_apps: 127
- too_few_successful_new_apps_for_trend_confidence: 127
- too_few_unique_developers: 127
- top3_too_dominant: 328
- top_app_concentration_penalty: 259
- top_app_too_dominant: 259
- unknown_pattern_blocker_active: 65

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.84 sendable=84.72 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49439 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.4 sendable=84.32 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=33509 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=90.19 sendable=81.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1370050 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.9 sendable=81.3 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=974486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.78 sendable=81.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=683342 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.91 sendable=80.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=434076 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.36 sendable=79.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.58 installs=1481271 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.8 sendable=79.58 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.88 installs=1035215 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.23 sendable=79.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.52 installs=1619535 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.91 sendable=79.07 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.52 installs=1189380 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=85.82 sendable=79.01 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=182708 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.47 sendable=77.66 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=36109 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=85.03 sendable=77.65 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.7 installs=327549 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.09 sendable=77.27 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=12220 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=83.81 sendable=76.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=52515 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.81 sendable=76.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=40828 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.89 sendable=75.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1163425 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.25 sendable=75.69 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=113223 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=77.36 sendable=75.48 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=144214 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=70.49 sendable=75.34 stage=COOLDOWN_BLOCKED quality=87.78 mvp=85.0 installs=15687 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
