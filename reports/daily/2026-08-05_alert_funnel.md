# Alert Funnel - 2026-08-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 83
- NEAR_MISS: 112
- REJECT: 187
- SINGLE_APP_WATCH: 20
- WATCH: 157

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 476
- QUALIFIED_CANDIDATE_ONLY: 81
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 124
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 71
- unknown_dominant_cluster: 62
- unknown_pattern_blocker_active: 62

## Sendable Failure Distribution
- below_classification_confidence: 174
- below_data_quality_for_trend_confidence: 287
- below_data_quality_score: 287
- below_mvp_feasibility: 175
- below_opportunity_score: 465
- below_sendable_alert_score: 557
- below_team_fit_score: 344
- below_trend_confidence_score: 346
- blocked_risk_tag: 79
- complex_full_product: 251
- cooldown_normalized_niche: 1
- duplicate_market_signal: 124
- giant_developer_competition: 28
- giant_developer_penalty: 24
- giant_share_too_high: 17
- growth_by_one_app_too_high: 231
- high_mvp_complexity: 124
- high_production_complexity: 60
- leader_dominated_market: 212
- low_classification_confidence: 174
- low_developer_diversity: 147
- low_mvp_feasibility: 175
- low_total_daily_installs: 154
- low_total_daily_installs_for_trend_confidence: 154
- market_signal_duplicate: 10
- not_alert_status: 476
- one_app_growth_penalty: 251
- organic_confidence_low: 211
- other_niche_low_confidence: 58
- severe_paid_spike_penalty: 78
- single_app_breakout_not_regular_alert: 147
- single_developer_dominance: 195
- single_developer_penalty: 229
- single_developer_share_too_high: 213
- too_few_apps_for_sendable: 221
- too_few_apps_for_trend_confidence: 221
- too_few_successful_new_apps: 147
- too_few_successful_new_apps_for_trend_confidence: 147
- too_few_unique_developers: 147
- top3_too_dominant: 330
- top_app_concentration_penalty: 259
- top_app_too_dominant: 259
- unknown_pattern_blocker_active: 60

## Top Qualified But Not Sent
- ALERT block_puzzle score=88.76 sendable=80.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.18 installs=935277 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.32 sendable=79.56 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=73706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=88.66 sendable=79.11 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=688668 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.22 sendable=77.8 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=836660 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.46 sendable=76.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=922141 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=88.13 sendable=76.71 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.51 installs=2172691 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.49 sendable=76.3 stage=QUALIFIED_CANDIDATE_ONLY quality=93.66 mvp=65.0 installs=7117 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=79.2 sendable=76.27 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=84781 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.35 sendable=76.02 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=111983 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=83.69 sendable=75.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.57 installs=165210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.17 sendable=75.26 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=70187 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.11 sendable=74.83 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=28513 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT mahjong score=86.76 sendable=74.63 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=124355 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.48 sendable=74.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.3 installs=605065 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.97 sendable=73.78 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=37552 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.93 sendable=71.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.68 installs=878210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT sort_puzzle score=72.95 sendable=71.92 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=12559 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.87 sendable=71.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=15773 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=71.61 sendable=70.82 stage=QUALIFIED_CANDIDATE_ONLY quality=91.0 mvp=85.0 installs=13958 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT runner score=83.13 sendable=70.37 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.32 installs=162185 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
