# Alert Funnel - 2026-09-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 90
- NEAR_MISS: 113
- REJECT: 210
- SINGLE_APP_WATCH: 20
- WATCH: 165

## Alert Stage Counts
- COOLDOWN_BLOCKED: 53
- NONE: 508
- QUALIFIED_CANDIDATE_ONLY: 36
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 53
- duplicate_market_signals_suppressed: 120
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 187
- below_data_quality_for_trend_confidence: 307
- below_data_quality_score: 307
- below_mvp_feasibility: 197
- below_opportunity_score: 496
- below_sendable_alert_score: 591
- below_team_fit_score: 372
- below_trend_confidence_score: 353
- blocked_risk_tag: 121
- complex_full_product: 263
- cooldown_exact_dedupe_key: 3
- cooldown_normalized_niche: 53
- duplicate_market_signal: 120
- giant_developer_competition: 29
- giant_developer_penalty: 26
- giant_share_too_high: 13
- growth_by_one_app_too_high: 279
- high_mvp_complexity: 133
- high_production_complexity: 59
- leader_dominated_market: 251
- low_classification_confidence: 187
- low_developer_diversity: 156
- low_mvp_feasibility: 197
- low_total_daily_installs: 132
- low_total_daily_installs_for_trend_confidence: 132
- market_signal_duplicate: 6
- no_growth_history: 1
- not_alert_status: 508
- one_app_growth_penalty: 308
- organic_confidence_low: 245
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 116
- single_app_breakout_not_regular_alert: 156
- single_developer_dominance: 225
- single_developer_penalty: 272
- single_developer_share_too_high: 252
- too_few_apps_for_sendable: 247
- too_few_apps_for_trend_confidence: 247
- too_few_successful_new_apps: 156
- too_few_successful_new_apps_for_trend_confidence: 156
- too_few_unique_developers: 156
- top3_too_dominant: 361
- top_app_concentration_penalty: 292
- top_app_too_dominant: 292
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.1 sendable=84.68 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=68845 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.73 sendable=83.95 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=52582 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT sort_puzzle score=77.12 sendable=81.97 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=14910 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.63 sendable=81.35 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=26949 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.39 sendable=81.11 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=309865 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.59 sendable=80.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1451127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.97 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=376089 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.42 sendable=79.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.42 installs=1491740 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.79 sendable=78.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1394665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.34 sendable=78.41 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=437599 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=83.06 sendable=78.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.33 installs=248260 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.11 sendable=78.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=771913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.03 sendable=77.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.01 installs=479026 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=83.18 sendable=76.88 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=194624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=80.88 sendable=76.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.33 installs=183846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=85.03 sendable=75.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.35 installs=116972 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.83 sendable=73.94 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.3 installs=45105 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.81 sendable=73.75 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=38219 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=80.43 sendable=73.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=65.39 installs=186067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.17 sendable=72.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.74 installs=707847 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
