# Alert Funnel - 2026-07-18

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 103
- NEAR_MISS: 109
- REJECT: 211
- SINGLE_APP_WATCH: 16
- WATCH: 160

## Alert Stage Counts
- COOLDOWN_BLOCKED: 5
- NONE: 496
- QUALIFIED_CANDIDATE_ONLY: 97
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 5
- duplicate_market_signals_suppressed: 126
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 194
- below_data_quality_for_trend_confidence: 308
- below_data_quality_score: 308
- below_mvp_feasibility: 203
- below_opportunity_score: 488
- below_sendable_alert_score: 592
- below_team_fit_score: 390
- below_trend_confidence_score: 318
- blocked_risk_tag: 128
- complex_full_product: 284
- cooldown_normalized_niche: 5
- duplicate_market_signal: 126
- giant_developer_competition: 33
- giant_developer_penalty: 27
- giant_share_too_high: 21
- growth_by_one_app_too_high: 282
- high_mvp_complexity: 130
- high_production_complexity: 54
- leader_dominated_market: 249
- low_classification_confidence: 194
- low_developer_diversity: 145
- low_mvp_feasibility: 203
- low_total_daily_installs: 118
- low_total_daily_installs_for_trend_confidence: 118
- market_signal_duplicate: 9
- no_growth_history: 2
- not_alert_status: 496
- one_app_growth_penalty: 309
- organic_confidence_low: 243
- other_niche_low_confidence: 62
- severe_paid_spike_penalty: 125
- single_app_breakout_not_regular_alert: 145
- single_developer_dominance: 228
- single_developer_penalty: 268
- single_developer_share_too_high: 250
- too_few_apps_for_sendable: 223
- too_few_apps_for_trend_confidence: 223
- too_few_successful_new_apps: 145
- too_few_successful_new_apps_for_trend_confidence: 145
- too_few_unique_developers: 145
- top3_too_dominant: 355
- top_app_concentration_penalty: 286
- top_app_too_dominant: 286
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT coloring score=89.45 sendable=84.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1335099 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=81.05 sendable=83.59 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=45650 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.21 sendable=83.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1293568 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.17 sendable=82.72 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1229497 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.25 sendable=81.12 stage=COOLDOWN_BLOCKED quality=87.11 mvp=85.0 installs=171655 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.65 sendable=80.45 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1005127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.02 sendable=79.53 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1673666 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT arrow_puzzle score=86.47 sendable=79.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.56 installs=1307166 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.53 sendable=79.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.8 installs=2150842 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=83.46 sendable=79.08 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=151617 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.62 sendable=79.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=469328 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.9 sendable=78.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=184113 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=80.9 sendable=78.31 stage=QUALIFIED_CANDIDATE_ONLY quality=87.97 mvp=72.21 installs=76870 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.3 sendable=77.89 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=431371 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=73.11 sendable=77.89 stage=QUALIFIED_CANDIDATE_ONLY quality=93.13 mvp=65.0 installs=14750 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=77.05 sendable=77.8 stage=QUALIFIED_CANDIDATE_ONLY quality=91.6 mvp=85.0 installs=30038 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=74.15 sendable=77.77 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=15612 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=83.85 sendable=77.53 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=372024 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.6 sendable=76.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.19 installs=497200 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.96 sendable=76.21 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.04 installs=2221185 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
