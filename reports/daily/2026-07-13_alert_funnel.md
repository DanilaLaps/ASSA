# Alert Funnel - 2026-07-13

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 123
- NEAR_MISS: 96
- REJECT: 195
- SINGLE_APP_WATCH: 6
- WATCH: 175

## Alert Stage Counts
- COOLDOWN_BLOCKED: 6
- NONE: 472
- QUALIFIED_CANDIDATE_ONLY: 115
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 6
- duplicate_market_signals_suppressed: 131
- limit_blocked: 3

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 198
- below_data_quality_for_trend_confidence: 257
- below_data_quality_score: 257
- below_mvp_feasibility: 204
- below_opportunity_score: 481
- below_sendable_alert_score: 583
- below_team_fit_score: 382
- below_trend_confidence_score: 258
- blocked_risk_tag: 160
- complex_full_product: 275
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 6
- duplicate_market_signal: 131
- giant_developer_competition: 40
- giant_developer_penalty: 39
- giant_share_too_high: 30
- growth_by_one_app_too_high: 245
- high_mvp_complexity: 129
- high_production_complexity: 61
- leader_dominated_market: 233
- low_classification_confidence: 198
- low_developer_diversity: 137
- low_mvp_feasibility: 204
- low_total_daily_installs: 110
- low_total_daily_installs_for_trend_confidence: 110
- market_signal_duplicate: 11
- no_growth_history: 8
- not_alert_status: 472
- one_app_growth_penalty: 275
- organic_confidence_low: 223
- other_niche_low_confidence: 66
- per_niche_limit_blocked: 3
- severe_paid_spike_penalty: 151
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 215
- single_developer_penalty: 252
- single_developer_share_too_high: 233
- too_few_apps_for_sendable: 224
- too_few_apps_for_trend_confidence: 224
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 137
- top3_too_dominant: 365
- top_app_concentration_penalty: 281
- top_app_too_dominant: 281
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT coloring score=89.46 sendable=89.45 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=2112575 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=78.82 sendable=83.93 stage=QUALIFIED_CANDIDATE_ONLY quality=94.42 mvp=85.0 installs=38161 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT tile_match score=90.44 sendable=83.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1445874 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.19 sendable=82.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1361486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.87 sendable=81.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=513746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.54 sendable=81.52 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=493572 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=86.81 sendable=81.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1000665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.41 sendable=80.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.87 installs=1736335 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.59 sendable=80.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.22 installs=2576516 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.18 sendable=80.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.32 installs=6672106 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.51 sendable=79.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.41 installs=156383 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.19 sendable=78.71 stage=QUALIFIED_CANDIDATE_ONLY quality=87.54 mvp=67.73 installs=724997 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sandbox score=83.0 sendable=78.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.83 installs=147312 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=72.63 sendable=78.14 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=37606 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=89.14 sendable=77.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=2649923 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=79.36 sendable=77.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=146706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.18 sendable=77.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=29392 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.8 sendable=77.43 stage=QUALIFIED_CANDIDATE_ONLY quality=93.17 mvp=65.0 installs=55746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=75.19 sendable=76.93 stage=QUALIFIED_CANDIDATE_ONLY quality=92.14 mvp=65.0 installs=48690 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=76.85 sendable=76.61 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.71 installs=73027 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
