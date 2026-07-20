# Alert Funnel - 2026-07-20

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 92
- NEAR_MISS: 105
- REJECT: 167
- SINGLE_APP_WATCH: 23
- WATCH: 196

## Alert Stage Counts
- NONE: 491
- QUALIFIED_CANDIDATE_ONLY: 91
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 117
- limit_blocked: 3

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 198
- below_opportunity_score: 482
- below_sendable_alert_score: 579
- below_team_fit_score: 370
- below_trend_confidence_score: 349
- blocked_risk_tag: 87
- complex_full_product: 285
- duplicate_market_signal: 117
- giant_developer_competition: 34
- giant_developer_penalty: 29
- giant_share_too_high: 24
- growth_by_one_app_too_high: 286
- high_mvp_complexity: 131
- high_production_complexity: 56
- leader_dominated_market: 212
- low_classification_confidence: 193
- low_developer_diversity: 125
- low_mvp_feasibility: 198
- low_total_daily_installs: 116
- low_total_daily_installs_for_trend_confidence: 116
- market_signal_duplicate: 6
- no_growth_history: 1
- not_alert_status: 491
- one_app_growth_penalty: 308
- organic_confidence_low: 210
- other_niche_low_confidence: 65
- per_niche_limit_blocked: 3
- severe_paid_spike_penalty: 84
- single_app_breakout_not_regular_alert: 125
- single_developer_dominance: 198
- single_developer_penalty: 242
- single_developer_share_too_high: 212
- too_few_apps_for_sendable: 199
- too_few_apps_for_trend_confidence: 199
- too_few_successful_new_apps: 125
- too_few_successful_new_apps_for_trend_confidence: 125
- too_few_unique_developers: 125
- top3_too_dominant: 339
- top_app_concentration_penalty: 271
- top_app_too_dominant: 271
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT sort_puzzle score=78.05 sendable=81.9 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=23132 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=75.03 sendable=80.77 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=12024 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=87.31 sendable=80.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=347354 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.37 sendable=77.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=60.0 installs=429584 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.83 sendable=77.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=679853 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.97 sendable=76.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1166454 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=84.55 sendable=76.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=292207 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.58 sendable=74.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.88 installs=516072 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.15 sendable=74.0 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=11602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sandbox score=76.81 sendable=73.8 stage=QUALIFIED_CANDIDATE_ONLY quality=87.37 mvp=69.5 installs=56127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=79.17 sendable=73.33 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.18 installs=56513 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.51 sendable=71.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.22 installs=4006273 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT block_puzzle score=86.68 sendable=71.06 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.03 installs=1159332 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT merge score=85.23 sendable=70.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=527305 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=88.44 sendable=70.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.46 installs=1713253 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=84.62 sendable=70.41 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.72 installs=232660 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=80.77 sendable=70.28 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.85 installs=250516 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=73.75 sendable=69.87 stage=QUALIFIED_CANDIDATE_ONLY quality=84.0 mvp=65.0 installs=245843 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_revenue_signal
- ALERT arrow_puzzle score=86.73 sendable=69.27 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.84 installs=610683 unknown_app_share=0.3137 unknown_installs_share=0.2474 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT sort_puzzle score=72.84 sendable=69.16 stage=QUALIFIED_CANDIDATE_ONLY quality=84.0 mvp=85.0 installs=40579 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_revenue_signal
