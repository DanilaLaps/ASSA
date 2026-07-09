# Alert Funnel - 2026-07-09

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 85
- NEAR_MISS: 101
- REJECT: 185
- SINGLE_APP_WATCH: 19
- WATCH: 162

## Alert Stage Counts
- COOLDOWN_BLOCKED: 3
- NONE: 467
- QUALIFIED_CANDIDATE_ONLY: 81
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 3
- duplicate_market_signals_suppressed: 125
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 71
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 178
- below_data_quality_for_trend_confidence: 284
- below_data_quality_score: 284
- below_mvp_feasibility: 189
- below_opportunity_score: 464
- below_sendable_alert_score: 547
- below_team_fit_score: 359
- below_trend_confidence_score: 336
- blocked_risk_tag: 113
- complex_full_product: 254
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 3
- duplicate_market_signal: 125
- giant_developer_competition: 32
- giant_developer_penalty: 30
- giant_share_too_high: 21
- growth_by_one_app_too_high: 266
- high_mvp_complexity: 121
- high_production_complexity: 59
- leader_dominated_market: 227
- low_classification_confidence: 178
- low_developer_diversity: 121
- low_mvp_feasibility: 189
- low_total_daily_installs: 98
- low_total_daily_installs_for_trend_confidence: 98
- market_signal_duplicate: 9
- no_growth_history: 3
- not_alert_status: 467
- one_app_growth_penalty: 294
- organic_confidence_low: 212
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 109
- single_app_breakout_not_regular_alert: 121
- single_developer_dominance: 200
- single_developer_penalty: 248
- single_developer_share_too_high: 228
- too_few_apps_for_sendable: 208
- too_few_apps_for_trend_confidence: 208
- too_few_successful_new_apps: 121
- too_few_successful_new_apps_for_trend_confidence: 121
- too_few_unique_developers: 121
- top3_too_dominant: 340
- top_app_concentration_penalty: 264
- top_app_too_dominant: 264
- unknown_pattern_blocker_active: 65

## Top Qualified But Not Sent
- ALERT sort_puzzle score=89.52 sendable=81.79 stage=COOLDOWN_BLOCKED quality=92.86 mvp=85.0 installs=637955 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=90.39 sendable=81.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1177544 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.83 sendable=80.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=170217 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.67 sendable=80.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=879962 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.57 sendable=79.35 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.84 installs=1204082 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.42 sendable=79.21 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=334864 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.1 sendable=77.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=61662 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.1 sendable=77.53 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.27 installs=4331143 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.3 sendable=77.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.16 installs=1916950 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.32 sendable=77.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=47270 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.69 sendable=76.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.23 installs=2107350 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.26 sendable=76.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1659510 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=82.29 sendable=74.72 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.26 installs=144843 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.07 sendable=73.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.5 installs=1241901 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT coloring score=85.67 sendable=73.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.8 installs=1017095 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=83.42 sendable=72.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.33 installs=292717 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.55 sendable=71.84 stage=QUALIFIED_CANDIDATE_ONLY quality=92.9 mvp=65.0 installs=107455 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=74.67 sendable=71.0 stage=QUALIFIED_CANDIDATE_ONLY quality=84.0 mvp=85.0 installs=228941 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_revenue_signal
- ALERT block_puzzle score=77.53 sendable=70.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.89 installs=83071 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.47 sendable=70.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.25 installs=2209118 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
