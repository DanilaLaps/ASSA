# Alert Funnel - 2026-08-12

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 134
- NEAR_MISS: 109
- REJECT: 213
- SINGLE_APP_WATCH: 3
- WATCH: 168

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 493
- QUALIFIED_CANDIDATE_ONLY: 125
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 8
- duplicate_market_signals_suppressed: 121
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 196
- below_data_quality_for_trend_confidence: 287
- below_data_quality_score: 287
- below_mvp_feasibility: 197
- below_opportunity_score: 481
- below_sendable_alert_score: 615
- below_team_fit_score: 386
- below_trend_confidence_score: 267
- blocked_risk_tag: 179
- complex_full_product: 278
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 8
- duplicate_market_signal: 121
- giant_developer_competition: 35
- giant_developer_penalty: 30
- giant_share_too_high: 20
- growth_by_one_app_too_high: 278
- high_mvp_complexity: 129
- high_production_complexity: 55
- leader_dominated_market: 251
- low_classification_confidence: 196
- low_developer_diversity: 161
- low_mvp_feasibility: 197
- low_total_daily_installs: 130
- low_total_daily_installs_for_trend_confidence: 130
- market_signal_duplicate: 12
- no_growth_history: 1
- not_alert_status: 493
- one_app_growth_penalty: 301
- organic_confidence_low: 247
- other_niche_low_confidence: 62
- severe_paid_spike_penalty: 173
- single_app_breakout_not_regular_alert: 160
- single_developer_dominance: 234
- single_developer_penalty: 270
- single_developer_share_too_high: 254
- too_few_apps_for_sendable: 244
- too_few_apps_for_trend_confidence: 244
- too_few_successful_new_apps: 160
- too_few_successful_new_apps_for_trend_confidence: 160
- too_few_unique_developers: 161
- top3_too_dominant: 369
- top_app_concentration_penalty: 294
- top_app_too_dominant: 294
- unknown_pattern_blocker_active: 65

## Top Qualified But Not Sent
- ALERT sort_puzzle score=79.51 sendable=85.33 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=66716 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT block_puzzle score=90.2 sendable=83.26 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1751810 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.28 sendable=82.07 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1409882 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.02 sendable=82.03 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=269113 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.47 sendable=81.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=446824 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.75 sendable=81.2 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=146440 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT block_puzzle score=88.95 sendable=81.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.36 installs=2164920 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.97 sendable=80.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.26 installs=1376032 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.19 sendable=80.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=562349 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.89 sendable=80.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.8 installs=1887400 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.04 sendable=80.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.38 installs=4965465 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.6 sendable=79.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.57 installs=1898421 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.39 sendable=79.86 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=45057 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=76.7 sendable=79.78 stage=QUALIFIED_CANDIDATE_ONLY quality=91.1 mvp=85.0 installs=21095 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.08 sendable=79.71 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=87951 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.04 sendable=79.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1527489 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.74 sendable=79.43 stage=QUALIFIED_CANDIDATE_ONLY quality=87.96 mvp=85.0 installs=67828 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.78 sendable=79.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.66 installs=309249 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.64 sendable=79.0 stage=QUALIFIED_CANDIDATE_ONLY quality=94.1 mvp=65.0 installs=21874 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=79.03 sendable=78.55 stage=QUALIFIED_CANDIDATE_ONLY quality=92.44 mvp=65.0 installs=83079 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
