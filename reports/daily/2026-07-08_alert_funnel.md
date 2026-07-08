# Alert Funnel - 2026-07-08

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 84
- NEAR_MISS: 100
- REJECT: 183
- SINGLE_APP_WATCH: 20
- WATCH: 152

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 455
- QUALIFIED_CANDIDATE_ONLY: 82
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 137
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 70
- unknown_dominant_cluster: 64
- unknown_pattern_blocker_active: 64

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 285
- below_data_quality_score: 285
- below_mvp_feasibility: 194
- below_opportunity_score: 447
- below_sendable_alert_score: 537
- below_team_fit_score: 346
- below_trend_confidence_score: 325
- blocked_risk_tag: 95
- complex_full_product: 245
- cooldown_normalized_niche: 1
- duplicate_market_signal: 137
- giant_developer_competition: 25
- giant_developer_penalty: 24
- giant_share_too_high: 21
- growth_by_one_app_too_high: 239
- high_mvp_complexity: 123
- high_production_complexity: 63
- leader_dominated_market: 224
- low_classification_confidence: 177
- low_developer_diversity: 126
- low_mvp_feasibility: 194
- low_total_daily_installs: 107
- low_total_daily_installs_for_trend_confidence: 107
- market_signal_duplicate: 9
- no_growth_history: 2
- not_alert_status: 455
- one_app_growth_penalty: 264
- organic_confidence_low: 208
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 91
- single_app_breakout_not_regular_alert: 126
- single_developer_dominance: 202
- single_developer_penalty: 243
- single_developer_share_too_high: 224
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 126
- too_few_successful_new_apps_for_trend_confidence: 126
- too_few_unique_developers: 126
- top3_too_dominant: 332
- top_app_concentration_penalty: 270
- top_app_too_dominant: 270
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT arrow_puzzle score=88.83 sendable=80.01 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1124499 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.62 sendable=79.58 stage=QUALIFIED_CANDIDATE_ONLY quality=86.34 mvp=85.0 installs=837149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.24 sendable=79.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=234041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.31 sendable=79.08 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=289163 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.86 sendable=79.06 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.58 installs=2045018 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.33 sendable=78.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.8 installs=1648094 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.95 sendable=78.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=80.64 installs=993945 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.22 sendable=78.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1095127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.71 sendable=76.44 stage=QUALIFIED_CANDIDATE_ONLY quality=84.13 mvp=85.0 installs=682817 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.11 sendable=75.18 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=196453 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=77.01 sendable=74.68 stage=QUALIFIED_CANDIDATE_ONLY quality=94.14 mvp=65.0 installs=19624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=72.02 sendable=74.52 stage=QUALIFIED_CANDIDATE_ONLY quality=93.83 mvp=65.0 installs=12679 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=81.24 sendable=74.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.04 installs=80032 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.93 sendable=73.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.79 installs=1545602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.5 sendable=72.93 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.65 installs=1017146 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=83.57 sendable=72.89 stage=QUALIFIED_CANDIDATE_ONLY quality=86.61 mvp=66.33 installs=204906 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.69 sendable=72.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=148755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.91 sendable=71.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.57 installs=1027288 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.24 sendable=71.37 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.39 installs=1069199 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT other score=81.67 sendable=70.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.47 installs=228724 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
