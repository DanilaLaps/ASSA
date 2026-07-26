# Alert Funnel - 2026-07-26

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 91
- NEAR_MISS: 116
- REJECT: 182
- SINGLE_APP_WATCH: 14
- WATCH: 179

## Alert Stage Counts
- COOLDOWN_BLOCKED: 40
- NONE: 491
- QUALIFIED_CANDIDATE_ONLY: 50
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 40
- duplicate_market_signals_suppressed: 116
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 191
- below_data_quality_for_trend_confidence: 293
- below_data_quality_score: 293
- below_mvp_feasibility: 195
- below_opportunity_score: 475
- below_sendable_alert_score: 578
- below_team_fit_score: 359
- below_trend_confidence_score: 319
- blocked_risk_tag: 104
- complex_full_product: 272
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 40
- duplicate_market_signal: 116
- giant_developer_competition: 29
- giant_developer_penalty: 26
- giant_share_too_high: 16
- growth_by_one_app_too_high: 293
- high_mvp_complexity: 128
- high_production_complexity: 52
- leader_dominated_market: 213
- low_classification_confidence: 191
- low_developer_diversity: 119
- low_mvp_feasibility: 195
- low_total_daily_installs: 119
- low_total_daily_installs_for_trend_confidence: 119
- market_signal_duplicate: 9
- not_alert_status: 491
- one_app_growth_penalty: 322
- organic_confidence_low: 215
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 101
- single_app_breakout_not_regular_alert: 119
- single_developer_dominance: 195
- single_developer_penalty: 232
- single_developer_share_too_high: 214
- too_few_apps_for_sendable: 201
- too_few_apps_for_trend_confidence: 201
- too_few_successful_new_apps: 119
- too_few_successful_new_apps_for_trend_confidence: 119
- too_few_unique_developers: 119
- top3_too_dominant: 325
- top_app_concentration_penalty: 257
- top_app_too_dominant: 257
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.99 sendable=85.16 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=47432 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.89 sendable=84.78 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=33683 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT sort_puzzle score=86.99 sendable=80.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=386611 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.0 sendable=80.15 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=439773 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.2 sendable=79.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.69 installs=325136 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.82 sendable=79.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=51801 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.1 sendable=79.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.1 installs=1137419 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.43 sendable=79.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=62.5 installs=520060 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.61 sendable=78.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=39933 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=85.72 sendable=78.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=185966 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.63 sendable=78.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.7 installs=841080 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.6 sendable=77.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=594617 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.25 sendable=77.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1182542 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.79 sendable=77.39 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=235362 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.87 sendable=77.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=113746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=78.45 sendable=77.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=137609 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.17 sendable=76.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1286722 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=70.89 sendable=75.67 stage=COOLDOWN_BLOCKED quality=86.53 mvp=85.0 installs=13626 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.19 sendable=75.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.4 installs=1375017 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=88.77 sendable=74.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.87 installs=943273 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
