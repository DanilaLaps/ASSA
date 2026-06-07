# Alert Funnel - 2026-06-07

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 65
- NEAR_MISS: 141
- REJECT: 195
- SINGLE_APP_WATCH: 21
- WATCH: 187

## Alert Stage Counts
- NONE: 544
- QUALIFIED_CANDIDATE_ONLY: 64
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 74
- unknown_pattern_blocker_active: 74

## Sendable Failure Distribution
- below_classification_confidence: 199
- below_data_quality_for_trend_confidence: 432
- below_data_quality_score: 432
- below_mvp_feasibility: 205
- below_opportunity_score: 552
- below_sendable_alert_score: 609
- below_team_fit_score: 381
- below_trend_confidence_score: 477
- blocked_risk_tag: 135
- complex_full_product: 285
- duplicate_market_signal: 119
- giant_developer_competition: 29
- giant_developer_penalty: 28
- giant_share_too_high: 17
- growth_by_one_app_too_high: 351
- high_mvp_complexity: 138
- high_production_complexity: 58
- leader_dominated_market: 219
- low_classification_confidence: 199
- low_developer_diversity: 135
- low_mvp_feasibility: 205
- low_total_daily_installs: 120
- low_total_daily_installs_for_trend_confidence: 120
- market_signal_duplicate: 4
- no_growth_history: 2
- not_alert_status: 544
- one_app_growth_penalty: 378
- organic_confidence_low: 213
- other_niche_low_confidence: 70
- severe_paid_spike_penalty: 101
- single_app_breakout_not_regular_alert: 134
- single_developer_dominance: 197
- single_developer_penalty: 236
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 134
- too_few_successful_new_apps_for_trend_confidence: 134
- too_few_unique_developers: 135
- top3_too_dominant: 349
- top_app_concentration_penalty: 257
- top_app_too_dominant: 257
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT arrow_puzzle score=80.46 sendable=74.49 stage=QUALIFIED_CANDIDATE_ONLY quality=82.84 mvp=85.0 installs=2047150 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.55 sendable=74.45 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=79.0 installs=43769 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=79.05 sendable=72.64 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.43 installs=134906 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.55 sendable=70.94 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=77.95 installs=2466408 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.34 sendable=70.57 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=71.62 installs=53846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.64 sendable=70.05 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.58 installs=79900 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT match_3 score=78.73 sendable=69.36 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.18 installs=1060021 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=78.2 sendable=67.36 stage=QUALIFIED_CANDIDATE_ONLY quality=75.0 mvp=85.0 installs=88949 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=78.04 sendable=66.95 stage=QUALIFIED_CANDIDATE_ONLY quality=86.62 mvp=65.0 installs=196676 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=77.56 sendable=66.76 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=360167 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT merge score=72.25 sendable=66.66 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.12 installs=12186 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=74.61 sendable=66.58 stage=QUALIFIED_CANDIDATE_ONLY quality=80.55 mvp=65.0 installs=29402 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.38 sendable=66.19 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=71.86 installs=79783 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.69 sendable=65.82 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.08 installs=987975 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.0 sendable=65.17 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=302660 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=78.26 sendable=64.65 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=65.81 installs=71576 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=75.01 sendable=64.45 stage=QUALIFIED_CANDIDATE_ONLY quality=82.15 mvp=60.0 installs=11845 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT idle_tycoon score=78.24 sendable=64.4 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.85 installs=172969 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=78.31 sendable=64.32 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.75 installs=34425 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT runner score=76.79 sendable=63.82 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=63.66 installs=1958415 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
