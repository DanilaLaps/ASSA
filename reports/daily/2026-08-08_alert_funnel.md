# Alert Funnel - 2026-08-08

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 77
- NEAR_MISS: 103
- REJECT: 195
- SINGLE_APP_WATCH: 14
- WATCH: 166

## Alert Stage Counts
- COOLDOWN_BLOCKED: 59
- NONE: 478
- QUALIFIED_CANDIDATE_ONLY: 17
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 59
- duplicate_market_signals_suppressed: 123
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 63
- unknown_pattern_blocker_active: 63

## Sendable Failure Distribution
- below_classification_confidence: 168
- below_data_quality_for_trend_confidence: 299
- below_data_quality_score: 299
- below_mvp_feasibility: 184
- below_opportunity_score: 459
- below_sendable_alert_score: 554
- below_team_fit_score: 346
- below_trend_confidence_score: 376
- blocked_risk_tag: 89
- complex_full_product: 249
- cooldown_normalized_niche: 59
- duplicate_market_signal: 123
- giant_developer_competition: 30
- giant_developer_penalty: 25
- giant_share_too_high: 15
- growth_by_one_app_too_high: 271
- high_mvp_complexity: 121
- high_production_complexity: 60
- leader_dominated_market: 224
- low_classification_confidence: 168
- low_developer_diversity: 150
- low_mvp_feasibility: 184
- low_total_daily_installs: 146
- low_total_daily_installs_for_trend_confidence: 146
- market_signal_duplicate: 6
- no_growth_history: 2
- not_alert_status: 478
- one_app_growth_penalty: 292
- organic_confidence_low: 218
- other_niche_low_confidence: 56
- severe_paid_spike_penalty: 86
- single_app_breakout_not_regular_alert: 150
- single_developer_dominance: 206
- single_developer_penalty: 238
- single_developer_share_too_high: 225
- too_few_apps_for_sendable: 216
- too_few_apps_for_trend_confidence: 216
- too_few_successful_new_apps: 150
- too_few_successful_new_apps_for_trend_confidence: 150
- too_few_unique_developers: 150
- top3_too_dominant: 331
- top_app_concentration_penalty: 261
- top_app_too_dominant: 261
- unknown_pattern_blocker_active: 61

## Top Qualified But Not Sent
- ALERT sort_puzzle score=78.2 sendable=81.96 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=23730 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=87.95 sendable=79.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=848622 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.27 sendable=79.02 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.06 installs=878885 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.3 sendable=78.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.38 installs=595251 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.27 sendable=77.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=882604 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.25 sendable=74.93 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=99932 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.62 sendable=74.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.59 installs=757259 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.79 sendable=74.03 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.77 installs=1010070 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=80.61 sendable=73.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.25 installs=29336 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.48 sendable=73.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.0 installs=58447 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.39 sendable=72.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.44 installs=136704 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=77.35 sendable=72.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=79639 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=82.03 sendable=71.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.75 installs=72413 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.1 sendable=71.98 stage=COOLDOWN_BLOCKED quality=86.61 mvp=85.0 installs=12210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=80.99 sendable=71.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.38 installs=185710 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=86.31 sendable=70.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.36 installs=891509 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=84.74 sendable=69.3 stage=COOLDOWN_BLOCKED quality=88.0 mvp=65.8 installs=903018 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.81 sendable=68.92 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.92 installs=348979 unknown_app_share=0.2394 unknown_installs_share=0.2015 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT sandbox score=81.38 sendable=68.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.57 installs=74731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=84.55 sendable=68.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=65.0 installs=1201325 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
