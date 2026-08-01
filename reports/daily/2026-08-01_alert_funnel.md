# Alert Funnel - 2026-08-01

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 98
- NEAR_MISS: 113
- REJECT: 204
- SINGLE_APP_WATCH: 14
- WATCH: 165

## Alert Stage Counts
- COOLDOWN_BLOCKED: 43
- NONE: 496
- QUALIFIED_CANDIDATE_ONLY: 54
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 43
- duplicate_market_signals_suppressed: 122
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 179
- below_data_quality_for_trend_confidence: 308
- below_data_quality_score: 308
- below_mvp_feasibility: 194
- below_opportunity_score: 478
- below_sendable_alert_score: 592
- below_team_fit_score: 364
- below_trend_confidence_score: 353
- blocked_risk_tag: 119
- complex_full_product: 261
- cooldown_normalized_niche: 43
- duplicate_market_signal: 122
- giant_developer_competition: 31
- giant_developer_penalty: 26
- giant_share_too_high: 20
- growth_by_one_app_too_high: 273
- high_mvp_complexity: 127
- high_production_complexity: 60
- leader_dominated_market: 232
- low_classification_confidence: 179
- low_developer_diversity: 143
- low_mvp_feasibility: 194
- low_total_daily_installs: 138
- low_total_daily_installs_for_trend_confidence: 138
- market_signal_duplicate: 7
- not_alert_status: 496
- one_app_growth_penalty: 294
- organic_confidence_low: 230
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 118
- single_app_breakout_not_regular_alert: 143
- single_developer_dominance: 206
- single_developer_penalty: 259
- single_developer_share_too_high: 233
- too_few_apps_for_sendable: 232
- too_few_apps_for_trend_confidence: 232
- too_few_successful_new_apps: 143
- too_few_successful_new_apps_for_trend_confidence: 143
- too_few_unique_developers: 143
- top3_too_dominant: 341
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT coloring score=91.17 sendable=84.81 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=844896 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.27 sendable=80.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=926729 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.61 sendable=79.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=355231 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=87.53 sendable=79.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=182500 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.71 sendable=79.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=420000 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.77 sendable=79.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.64 installs=1255134 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.78 sendable=78.66 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=183575 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=86.21 sendable=78.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.68 installs=861337 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.16 sendable=78.03 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=36133 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.07 sendable=77.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.3 installs=1068761 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.16 sendable=76.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=145175 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.88 sendable=76.58 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=979756 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.15 sendable=76.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.68 installs=231044 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.5 sendable=76.45 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=50532 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.83 sendable=76.39 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=90218 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=88.48 sendable=75.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.24 installs=1142478 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=83.04 sendable=74.94 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=69.15 installs=214680 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.21 sendable=74.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.14 installs=950270 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.92 sendable=73.44 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.38 installs=2842099 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.38 sendable=71.96 stage=COOLDOWN_BLOCKED quality=85.11 mvp=85.0 installs=66459 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
