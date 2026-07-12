# Alert Funnel - 2026-07-12

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 104
- NEAR_MISS: 103
- REJECT: 192
- SINGLE_APP_WATCH: 8
- WATCH: 147

## Alert Stage Counts
- COOLDOWN_BLOCKED: 34
- NONE: 450
- QUALIFIED_CANDIDATE_ONLY: 69
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 34
- duplicate_market_signals_suppressed: 116
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 71
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 187
- below_data_quality_for_trend_confidence: 259
- below_data_quality_score: 259
- below_mvp_feasibility: 182
- below_opportunity_score: 448
- below_sendable_alert_score: 545
- below_team_fit_score: 345
- below_trend_confidence_score: 266
- blocked_risk_tag: 135
- complex_full_product: 243
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 34
- duplicate_market_signal: 116
- giant_developer_competition: 35
- giant_developer_penalty: 33
- giant_share_too_high: 30
- growth_by_one_app_too_high: 235
- high_mvp_complexity: 121
- high_production_complexity: 56
- leader_dominated_market: 217
- low_classification_confidence: 187
- low_developer_diversity: 127
- low_mvp_feasibility: 182
- low_total_daily_installs: 104
- low_total_daily_installs_for_trend_confidence: 104
- market_signal_duplicate: 8
- no_growth_history: 4
- not_alert_status: 450
- one_app_growth_penalty: 260
- organic_confidence_low: 215
- other_niche_low_confidence: 57
- severe_paid_spike_penalty: 129
- single_app_breakout_not_regular_alert: 127
- single_developer_dominance: 201
- single_developer_penalty: 237
- single_developer_share_too_high: 216
- too_few_apps_for_sendable: 210
- too_few_apps_for_trend_confidence: 210
- too_few_successful_new_apps: 127
- too_few_successful_new_apps_for_trend_confidence: 127
- too_few_unique_developers: 127
- top3_too_dominant: 350
- top_app_concentration_penalty: 267
- top_app_too_dominant: 267
- unknown_pattern_blocker_active: 62

## Top Qualified But Not Sent
- ALERT tile_match score=89.64 sendable=83.26 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1226633 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=87.82 sendable=82.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1649342 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.86 sendable=82.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=463438 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.5 sendable=81.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1075931 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.12 sendable=81.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=868409 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.34 sendable=80.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.21 installs=2011632 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.98 sendable=80.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.17 installs=2475827 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.38 sendable=80.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.02 installs=1428012 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.16 sendable=80.03 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=798865 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=83.07 sendable=79.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=147999 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.36 sendable=79.42 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=354034 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=87.11 sendable=79.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=471209 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=85.01 sendable=78.53 stage=QUALIFIED_CANDIDATE_ONLY quality=86.79 mvp=85.0 installs=356176 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.74 sendable=78.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=116457 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=82.05 sendable=77.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.67 installs=448321 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.36 sendable=77.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.62 installs=119010 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.47 sendable=77.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=2384330 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=84.49 sendable=76.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=101196 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=71.41 sendable=76.46 stage=COOLDOWN_BLOCKED quality=90.24 mvp=85.0 installs=22203 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT other score=77.15 sendable=76.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=64386 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
