# Alert Funnel - 2026-07-16

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 117
- NEAR_MISS: 115
- REJECT: 203
- SINGLE_APP_WATCH: 4
- WATCH: 170

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 492
- QUALIFIED_CANDIDATE_ONLY: 108
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 8
- duplicate_market_signals_suppressed: 127
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 203
- below_data_quality_for_trend_confidence: 288
- below_data_quality_score: 288
- below_mvp_feasibility: 208
- below_opportunity_score: 486
- below_sendable_alert_score: 598
- below_team_fit_score: 387
- below_trend_confidence_score: 285
- blocked_risk_tag: 158
- complex_full_product: 286
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 8
- duplicate_market_signal: 127
- giant_developer_competition: 33
- giant_developer_penalty: 30
- giant_share_too_high: 23
- growth_by_one_app_too_high: 273
- high_mvp_complexity: 131
- high_production_complexity: 58
- leader_dominated_market: 234
- low_classification_confidence: 203
- low_developer_diversity: 136
- low_mvp_feasibility: 208
- low_total_daily_installs: 109
- low_total_daily_installs_for_trend_confidence: 109
- market_signal_duplicate: 11
- not_alert_status: 492
- one_app_growth_penalty: 317
- organic_confidence_low: 228
- other_niche_low_confidence: 65
- severe_paid_spike_penalty: 156
- single_app_breakout_not_regular_alert: 136
- single_developer_dominance: 220
- single_developer_penalty: 262
- single_developer_share_too_high: 235
- too_few_apps_for_sendable: 219
- too_few_apps_for_trend_confidence: 219
- too_few_successful_new_apps: 136
- too_few_successful_new_apps_for_trend_confidence: 136
- too_few_unique_developers: 136
- top3_too_dominant: 358
- top_app_concentration_penalty: 288
- top_app_too_dominant: 288
- unknown_pattern_blocker_active: 70

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.34 sendable=82.82 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=40554 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.34 sendable=82.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1371852 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.52 sendable=82.16 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=488215 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.24 sendable=82.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=553328 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=90.13 sendable=81.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1208114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.3 sendable=80.94 stage=QUALIFIED_CANDIDATE_ONLY quality=93.11 mvp=85.0 installs=29190 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT other score=87.32 sendable=80.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.02 installs=5752150 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.13 sendable=80.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=190953 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.64 sendable=80.31 stage=COOLDOWN_BLOCKED quality=94.64 mvp=65.0 installs=181704 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=87.22 sendable=80.16 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.91 installs=2421509 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.17 sendable=79.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.49 installs=2555514 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.06 sendable=78.97 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=466531 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=86.42 sendable=78.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.42 installs=1424553 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.18 sendable=78.84 stage=QUALIFIED_CANDIDATE_ONLY quality=94.06 mvp=65.0 installs=57858 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=84.35 sendable=78.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.42 installs=503633 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.21 sendable=78.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1662218 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=70.04 sendable=78.03 stage=QUALIFIED_CANDIDATE_ONLY quality=93.45 mvp=85.0 installs=11364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=73.22 sendable=77.99 stage=QUALIFIED_CANDIDATE_ONLY quality=93.43 mvp=65.0 installs=57135 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.74 sendable=76.98 stage=QUALIFIED_CANDIDATE_ONLY quality=85.35 mvp=85.0 installs=135957 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.05 sendable=76.85 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.9 installs=1699093 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
