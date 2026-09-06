# Alert Funnel - 2026-09-06

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 88
- NEAR_MISS: 100
- REJECT: 208
- SINGLE_APP_WATCH: 19
- WATCH: 161

## Alert Stage Counts
- COOLDOWN_BLOCKED: 34
- NONE: 488
- QUALIFIED_CANDIDATE_ONLY: 53
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 34
- duplicate_market_signals_suppressed: 121
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 184
- below_data_quality_for_trend_confidence: 296
- below_data_quality_score: 296
- below_mvp_feasibility: 207
- below_opportunity_score: 475
- below_sendable_alert_score: 574
- below_team_fit_score: 354
- below_trend_confidence_score: 355
- blocked_risk_tag: 103
- complex_full_product: 253
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 34
- duplicate_market_signal: 121
- giant_developer_competition: 27
- giant_developer_penalty: 21
- giant_share_too_high: 16
- growth_by_one_app_too_high: 251
- high_mvp_complexity: 129
- high_production_complexity: 60
- leader_dominated_market: 238
- low_classification_confidence: 184
- low_developer_diversity: 155
- low_mvp_feasibility: 207
- low_total_daily_installs: 144
- low_total_daily_installs_for_trend_confidence: 144
- market_signal_duplicate: 5
- not_alert_status: 488
- one_app_growth_penalty: 278
- organic_confidence_low: 240
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 98
- single_app_breakout_not_regular_alert: 155
- single_developer_dominance: 221
- single_developer_penalty: 260
- single_developer_share_too_high: 239
- too_few_apps_for_sendable: 245
- too_few_apps_for_trend_confidence: 245
- too_few_successful_new_apps: 155
- too_few_successful_new_apps_for_trend_confidence: 155
- too_few_unique_developers: 155
- top3_too_dominant: 348
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT sort_puzzle score=88.71 sendable=80.45 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=248676 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.93 sendable=80.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1134620 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.38 sendable=79.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.12 installs=1122437 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.58 sendable=79.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=988396 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.13 sendable=78.93 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=14048 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.57 sendable=78.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.23 installs=185210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.68 sendable=78.28 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=23191 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=86.48 sendable=78.24 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=296302 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=82.37 sendable=77.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.97 installs=308705 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=82.37 sendable=77.01 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=174544 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=81.58 sendable=76.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.93 installs=154817 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.09 sendable=76.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.95 installs=730206 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.74 sendable=76.34 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=38082 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=81.33 sendable=74.99 stage=COOLDOWN_BLOCKED quality=87.19 mvp=72.9 installs=166047 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.73 sendable=74.2 stage=COOLDOWN_BLOCKED quality=89.55 mvp=85.0 installs=24064 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT coloring score=84.89 sendable=74.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.12 installs=93360 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT coloring score=74.77 sendable=73.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.2 installs=26269 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.52 sendable=73.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.77 installs=1140329 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT arrow_puzzle score=80.83 sendable=72.95 stage=COOLDOWN_BLOCKED quality=83.76 mvp=81.4 installs=119755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=81.32 sendable=72.54 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.26 installs=118472 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
