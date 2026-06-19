# Alert Funnel - 2026-06-19

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 85
- NEAR_MISS: 112
- REJECT: 191
- SINGLE_APP_WATCH: 18
- WATCH: 200

## Alert Stage Counts
- COOLDOWN_BLOCKED: 40
- NONE: 521
- QUALIFIED_CANDIDATE_ONLY: 44
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 40
- duplicate_market_signals_suppressed: 96
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 73
- unknown_pattern_blocker_active: 73

## Sendable Failure Distribution
- below_classification_confidence: 188
- below_data_quality_for_trend_confidence: 313
- below_data_quality_score: 313
- below_mvp_feasibility: 201
- below_opportunity_score: 496
- below_sendable_alert_score: 605
- below_team_fit_score: 384
- below_trend_confidence_score: 371
- blocked_risk_tag: 106
- complex_full_product: 283
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 40
- duplicate_market_signal: 96
- giant_developer_competition: 37
- giant_developer_penalty: 29
- giant_share_too_high: 19
- growth_by_one_app_too_high: 298
- high_mvp_complexity: 134
- high_production_complexity: 56
- leader_dominated_market: 231
- low_classification_confidence: 188
- low_developer_diversity: 131
- low_mvp_feasibility: 201
- low_total_daily_installs: 120
- low_total_daily_installs_for_trend_confidence: 120
- market_signal_duplicate: 5
- no_growth_history: 6
- not_alert_status: 521
- one_app_growth_penalty: 327
- organic_confidence_low: 224
- other_niche_low_confidence: 69
- severe_paid_spike_penalty: 99
- single_app_breakout_not_regular_alert: 131
- single_developer_dominance: 201
- single_developer_penalty: 254
- single_developer_share_too_high: 232
- too_few_apps_for_sendable: 219
- too_few_apps_for_trend_confidence: 219
- too_few_successful_new_apps: 131
- too_few_successful_new_apps_for_trend_confidence: 131
- too_few_unique_developers: 131
- top3_too_dominant: 352
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 73

## Top Qualified But Not Sent
- ALERT sort_puzzle score=84.35 sendable=82.12 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=60965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=83.39 sendable=79.88 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.47 installs=100812 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.71 sendable=78.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.58 installs=188200 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.22 sendable=78.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.7 installs=681933 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.52 sendable=78.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.43 installs=1919033 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.83 sendable=77.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.33 installs=4086390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.25 sendable=77.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1094605 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=71.89 sendable=77.35 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=15176 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=84.31 sendable=77.22 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.24 installs=118198 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.16 sendable=75.3 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=985412 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=85.65 sendable=73.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.11 installs=1068022 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=85.02 sendable=73.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.73 installs=980300 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.88 sendable=71.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.85 installs=1826201 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=72.35 sendable=71.17 stage=QUALIFIED_CANDIDATE_ONLY quality=87.86 mvp=64.0 installs=19715 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=86.01 sendable=69.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=147129 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=84.73 sendable=69.34 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=416126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=86.74 sendable=69.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.53 installs=1228437 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=84.49 sendable=69.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2580569 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=84.74 sendable=68.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.15 installs=537309 unknown_app_share=0.3043 unknown_installs_share=0.2516 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT match_3 score=84.96 sendable=67.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.43 installs=930471 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
