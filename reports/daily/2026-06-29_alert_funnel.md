# Alert Funnel - 2026-06-29

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 75
- NEAR_MISS: 75
- REJECT: 180
- SINGLE_APP_WATCH: 14
- WATCH: 136

## Alert Stage Counts
- NONE: 405
- QUALIFIED_CANDIDATE_ONLY: 73
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 132
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 67
- unknown_dominant_cluster: 61
- unknown_pattern_blocker_active: 61

## Sendable Failure Distribution
- below_classification_confidence: 159
- below_data_quality_for_trend_confidence: 273
- below_data_quality_score: 273
- below_mvp_feasibility: 183
- below_opportunity_score: 399
- below_sendable_alert_score: 478
- below_team_fit_score: 315
- below_trend_confidence_score: 303
- blocked_risk_tag: 106
- complex_full_product: 229
- duplicate_market_signal: 132
- giant_developer_competition: 26
- giant_developer_penalty: 21
- giant_share_too_high: 17
- growth_by_one_app_too_high: 219
- high_mvp_complexity: 111
- high_production_complexity: 60
- leader_dominated_market: 213
- low_classification_confidence: 159
- low_developer_diversity: 132
- low_mvp_feasibility: 183
- low_total_daily_installs: 113
- low_total_daily_installs_for_trend_confidence: 113
- market_signal_duplicate: 7
- no_growth_history: 3
- not_alert_status: 405
- one_app_growth_penalty: 242
- organic_confidence_low: 208
- other_niche_low_confidence: 55
- severe_paid_spike_penalty: 104
- single_app_breakout_not_regular_alert: 132
- single_developer_dominance: 196
- single_developer_penalty: 235
- single_developer_share_too_high: 213
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 132
- too_few_successful_new_apps_for_trend_confidence: 132
- too_few_unique_developers: 132
- top3_too_dominant: 307
- top_app_concentration_penalty: 257
- top_app_too_dominant: 257
- unknown_pattern_blocker_active: 59

## Top Qualified But Not Sent
- ALERT sort_puzzle score=88.19 sendable=79.82 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=389187 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=85.92 sendable=78.69 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=424608 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.01 sendable=77.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.68 installs=2643198 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.4 sendable=74.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.88 installs=1196244 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=77.7 sendable=74.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.5 installs=171190 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.14 sendable=74.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=402695 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.71 sendable=73.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.78 installs=806962 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.29 sendable=73.77 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.68 installs=525561 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.04 sendable=73.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.21 installs=487542 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=81.75 sendable=73.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.75 installs=489894 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=71.37 sendable=72.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=23055 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.03 sendable=72.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.75 installs=338280 unknown_app_share=0.275 unknown_installs_share=0.1833 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT hidden_object score=73.59 sendable=72.49 stage=QUALIFIED_CANDIDATE_ONLY quality=92.86 mvp=65.0 installs=23847 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.2 sendable=72.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=100357 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.1 sendable=71.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.47 installs=466222 unknown_app_share=0.3472 unknown_installs_share=0.202 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT other score=86.88 sendable=71.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.83 installs=674594 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT merge score=79.35 sendable=71.15 stage=QUALIFIED_CANDIDATE_ONLY quality=86.3 mvp=66.62 installs=28348 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.87 sendable=70.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.71 installs=119872 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.28 sendable=70.46 stage=QUALIFIED_CANDIDATE_ONLY quality=90.64 mvp=65.0 installs=40056 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=78.46 sendable=70.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.46 installs=63502 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
