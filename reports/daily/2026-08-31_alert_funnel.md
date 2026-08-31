# Alert Funnel - 2026-08-31

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 114
- NEAR_MISS: 100
- REJECT: 218
- SINGLE_APP_WATCH: 11
- WATCH: 151

## Alert Stage Counts
- COOLDOWN_BLOCKED: 10
- NONE: 480
- QUALIFIED_CANDIDATE_ONLY: 103
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 10
- duplicate_market_signals_suppressed: 126
- limit_blocked: 2

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 184
- below_data_quality_for_trend_confidence: 314
- below_data_quality_score: 314
- below_mvp_feasibility: 188
- below_opportunity_score: 475
- below_sendable_alert_score: 581
- below_team_fit_score: 352
- below_trend_confidence_score: 322
- blocked_risk_tag: 156
- complex_full_product: 249
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 10
- duplicate_market_signal: 126
- giant_developer_competition: 26
- giant_developer_penalty: 25
- giant_share_too_high: 17
- growth_by_one_app_too_high: 297
- high_mvp_complexity: 128
- high_production_complexity: 63
- leader_dominated_market: 238
- low_classification_confidence: 184
- low_developer_diversity: 146
- low_mvp_feasibility: 188
- low_total_daily_installs: 136
- low_total_daily_installs_for_trend_confidence: 136
- market_signal_duplicate: 8
- not_alert_status: 480
- one_app_growth_penalty: 324
- organic_confidence_low: 241
- other_niche_low_confidence: 66
- per_niche_limit_blocked: 2
- severe_paid_spike_penalty: 156
- single_app_breakout_not_regular_alert: 145
- single_developer_dominance: 215
- single_developer_penalty: 260
- single_developer_share_too_high: 241
- too_few_apps_for_sendable: 234
- too_few_apps_for_trend_confidence: 234
- too_few_successful_new_apps: 145
- too_few_successful_new_apps_for_trend_confidence: 145
- too_few_unique_developers: 146
- top3_too_dominant: 345
- top_app_concentration_penalty: 288
- top_app_too_dominant: 288
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT sort_puzzle score=79.84 sendable=83.16 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=45695 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=78.51 sendable=82.62 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=16807 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT tile_match score=89.32 sendable=82.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=940067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.35 sendable=81.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.97 installs=1588437 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.21 sendable=81.2 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=97048 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.24 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.96 installs=1755026 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.75 sendable=80.56 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=877965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=one_app_growth_penalty risks=unknown_coverage
- ALERT hidden_object score=86.02 sendable=80.44 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=162119 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=86.86 sendable=80.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1513260 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.04 sendable=80.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.9 installs=3833068 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.39 sendable=80.26 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=46664 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=86.97 sendable=80.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.99 installs=1230114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.48 sendable=79.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=680058 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.94 sendable=79.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1469003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.54 sendable=79.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=302445 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.77 sendable=78.36 stage=QUALIFIED_CANDIDATE_ONLY quality=87.92 mvp=69.12 installs=322055 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=82.78 sendable=77.7 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.85 installs=197607 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.3 sendable=77.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=40441 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.6 sendable=77.55 stage=QUALIFIED_CANDIDATE_ONLY quality=86.17 mvp=85.0 installs=36126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=80.98 sendable=76.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.95 installs=495712 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
