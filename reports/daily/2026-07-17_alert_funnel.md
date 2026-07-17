# Alert Funnel - 2026-07-17

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 113
- NEAR_MISS: 115
- REJECT: 203
- SINGLE_APP_WATCH: 13
- WATCH: 159

## Alert Stage Counts
- COOLDOWN_BLOCKED: 61
- NONE: 490
- QUALIFIED_CANDIDATE_ONLY: 51
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 61
- duplicate_market_signals_suppressed: 129
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 70
- unknown_pattern_blocker_active: 70

## Sendable Failure Distribution
- below_classification_confidence: 203
- below_data_quality_for_trend_confidence: 276
- below_data_quality_score: 276
- below_mvp_feasibility: 209
- below_opportunity_score: 487
- below_sendable_alert_score: 593
- below_team_fit_score: 389
- below_trend_confidence_score: 281
- blocked_risk_tag: 146
- complex_full_product: 288
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 61
- duplicate_market_signal: 129
- giant_developer_competition: 32
- giant_developer_penalty: 27
- giant_share_too_high: 20
- growth_by_one_app_too_high: 275
- high_mvp_complexity: 131
- high_production_complexity: 56
- leader_dominated_market: 238
- low_classification_confidence: 203
- low_developer_diversity: 137
- low_mvp_feasibility: 209
- low_total_daily_installs: 111
- low_total_daily_installs_for_trend_confidence: 111
- market_signal_duplicate: 9
- not_alert_status: 490
- one_app_growth_penalty: 306
- organic_confidence_low: 226
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 143
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 220
- single_developer_penalty: 259
- single_developer_share_too_high: 240
- too_few_apps_for_sendable: 218
- too_few_apps_for_trend_confidence: 218
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 137
- top3_too_dominant: 364
- top_app_concentration_penalty: 287
- top_app_too_dominant: 287
- unknown_pattern_blocker_active: 69

## Top Qualified But Not Sent
- ALERT coloring score=88.72 sendable=88.78 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1726441 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=81.52 sendable=84.81 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49748 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.41 sendable=83.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1411572 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.24 sendable=82.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=464294 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.39 sendable=82.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1330722 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=73.41 sendable=82.69 stage=COOLDOWN_BLOCKED quality=94.02 mvp=85.0 installs=16409 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage
- ALERT sort_puzzle score=86.74 sendable=82.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=524194 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.17 sendable=81.91 stage=COOLDOWN_BLOCKED quality=92.73 mvp=85.0 installs=33339 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=83.0 sendable=80.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=188281 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.75 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1074893 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.33 sendable=79.82 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=78088 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=83.51 sendable=79.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.09 installs=171069 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.5 sendable=79.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1708182 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=88.62 sendable=78.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.28 installs=2388779 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=84.57 sendable=78.37 stage=COOLDOWN_BLOCKED quality=88.0 mvp=64.13 installs=512595 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.5 sendable=78.22 stage=COOLDOWN_BLOCKED quality=94.32 mvp=65.0 installs=59378 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.88 sendable=76.95 stage=COOLDOWN_BLOCKED quality=91.53 mvp=65.0 installs=191659 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.27 sendable=76.94 stage=COOLDOWN_BLOCKED quality=85.13 mvp=85.0 installs=133198 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.18 sendable=76.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.15 installs=2314704 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=85.61 sendable=76.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.22 installs=2671368 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
