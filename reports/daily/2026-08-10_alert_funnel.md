# Alert Funnel - 2026-08-10

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 124
- NEAR_MISS: 106
- REJECT: 223
- SINGLE_APP_WATCH: 2
- WATCH: 154

## Alert Stage Counts
- COOLDOWN_BLOCKED: 6
- NONE: 485
- QUALIFIED_CANDIDATE_ONLY: 116
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 6
- duplicate_market_signals_suppressed: 133
- limit_blocked: 4

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 191
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 204
- below_opportunity_score: 475
- below_sendable_alert_score: 595
- below_team_fit_score: 381
- below_trend_confidence_score: 282
- blocked_risk_tag: 181
- complex_full_product: 274
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 6
- duplicate_market_signal: 133
- giant_developer_competition: 32
- giant_developer_penalty: 30
- giant_share_too_high: 23
- growth_by_one_app_too_high: 289
- high_mvp_complexity: 128
- high_production_complexity: 57
- leader_dominated_market: 244
- low_classification_confidence: 191
- low_developer_diversity: 153
- low_mvp_feasibility: 204
- low_total_daily_installs: 141
- low_total_daily_installs_for_trend_confidence: 141
- market_signal_duplicate: 12
- no_growth_history: 6
- not_alert_status: 485
- one_app_growth_penalty: 317
- organic_confidence_low: 240
- other_niche_low_confidence: 62
- per_niche_limit_blocked: 4
- severe_paid_spike_penalty: 173
- single_app_breakout_not_regular_alert: 153
- single_developer_dominance: 225
- single_developer_penalty: 266
- single_developer_share_too_high: 245
- too_few_apps_for_sendable: 235
- too_few_apps_for_trend_confidence: 235
- too_few_successful_new_apps: 153
- too_few_successful_new_apps_for_trend_confidence: 153
- too_few_unique_developers: 153
- top3_too_dominant: 359
- top_app_concentration_penalty: 290
- top_app_too_dominant: 290
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT block_puzzle score=89.94 sendable=83.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1423161 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.82 sendable=83.01 stage=QUALIFIED_CANDIDATE_ONLY quality=87.94 mvp=84.77 installs=962814 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.42 sendable=82.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1259333 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.01 sendable=82.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.74 installs=1283731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.66 sendable=82.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1090353 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=87.55 sendable=81.6 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=257556 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.82 sendable=81.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.47 installs=1745808 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.92 sendable=81.01 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=29431 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT arrow_puzzle score=87.93 sendable=80.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.58 installs=1127699 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.91 sendable=80.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.9 installs=1548778 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.57 sendable=80.12 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=185149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=84.31 sendable=80.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=91553 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.29 sendable=79.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=412125 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.3 sendable=79.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.08 installs=1638382 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.84 sendable=79.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=495131 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.08 sendable=79.56 stage=QUALIFIED_CANDIDATE_ONLY quality=93.79 mvp=65.0 installs=16566 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.07 sendable=79.27 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.65 installs=290309 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=79.4 sendable=79.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=180557 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.99 sendable=78.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.68 installs=128668 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.05 sendable=78.65 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=51947 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
