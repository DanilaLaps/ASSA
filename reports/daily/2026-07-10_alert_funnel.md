# Alert Funnel - 2026-07-10

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 88
- NEAR_MISS: 92
- REJECT: 191
- SINGLE_APP_WATCH: 23
- WATCH: 165

## Alert Stage Counts
- COOLDOWN_BLOCKED: 43
- NONE: 471
- QUALIFIED_CANDIDATE_ONLY: 44
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 43
- duplicate_market_signals_suppressed: 142
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 70
- unknown_dominant_cluster: 64
- unknown_pattern_blocker_active: 64

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 297
- below_data_quality_score: 297
- below_mvp_feasibility: 187
- below_opportunity_score: 469
- below_sendable_alert_score: 555
- below_team_fit_score: 362
- below_trend_confidence_score: 341
- blocked_risk_tag: 105
- complex_full_product: 256
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 43
- duplicate_market_signal: 142
- giant_developer_competition: 31
- giant_developer_penalty: 28
- giant_share_too_high: 21
- growth_by_one_app_too_high: 266
- high_mvp_complexity: 119
- high_production_complexity: 59
- leader_dominated_market: 231
- low_classification_confidence: 185
- low_developer_diversity: 129
- low_mvp_feasibility: 187
- low_total_daily_installs: 102
- low_total_daily_installs_for_trend_confidence: 102
- market_signal_duplicate: 7
- no_growth_history: 3
- not_alert_status: 471
- one_app_growth_penalty: 294
- organic_confidence_low: 225
- other_niche_low_confidence: 57
- severe_paid_spike_penalty: 99
- single_app_breakout_not_regular_alert: 129
- single_developer_dominance: 205
- single_developer_penalty: 257
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 129
- too_few_successful_new_apps_for_trend_confidence: 129
- too_few_unique_developers: 129
- top3_too_dominant: 347
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT sort_puzzle score=85.11 sendable=84.71 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=72281 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=90.35 sendable=81.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1177119 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.26 sendable=80.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=378348 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.93 sendable=80.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1395435 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.75 sendable=78.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.27 installs=1295898 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.11 sendable=77.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=155124 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=82.94 sendable=77.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=269117 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.24 sendable=77.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.12 installs=4367773 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.87 sendable=77.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=54598 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.5 sendable=77.46 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=904402 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.27 sendable=76.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1707472 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=78.59 sendable=75.94 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.71 installs=89219 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.02 sendable=74.26 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.83 installs=1208534 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=75.41 sendable=74.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.75 installs=42488 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.6 sendable=73.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.77 installs=2042850 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=84.77 sendable=73.42 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.2 installs=1011089 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.66 sendable=72.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=876021 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=81.61 sendable=72.46 stage=COOLDOWN_BLOCKED quality=86.07 mvp=67.69 installs=185489 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=85.47 sendable=71.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.27 installs=2251349 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.58 sendable=71.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.58 installs=1495395 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
