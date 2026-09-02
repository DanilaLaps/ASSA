# Alert Funnel - 2026-09-02

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 110
- NEAR_MISS: 100
- REJECT: 217
- SINGLE_APP_WATCH: 16
- WATCH: 138

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 471
- QUALIFIED_CANDIDATE_ONLY: 101
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 8
- duplicate_market_signals_suppressed: 109
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 180
- below_data_quality_for_trend_confidence: 296
- below_data_quality_score: 296
- below_mvp_feasibility: 190
- below_opportunity_score: 461
- below_sendable_alert_score: 572
- below_team_fit_score: 352
- below_trend_confidence_score: 304
- blocked_risk_tag: 159
- complex_full_product: 254
- cooldown_normalized_niche: 8
- duplicate_market_signal: 109
- giant_developer_competition: 23
- giant_developer_penalty: 22
- giant_share_too_high: 14
- growth_by_one_app_too_high: 269
- high_mvp_complexity: 131
- high_production_complexity: 60
- leader_dominated_market: 240
- low_classification_confidence: 180
- low_developer_diversity: 152
- low_mvp_feasibility: 190
- low_total_daily_installs: 131
- low_total_daily_installs_for_trend_confidence: 131
- market_signal_duplicate: 6
- no_growth_history: 2
- not_alert_status: 471
- one_app_growth_penalty: 296
- organic_confidence_low: 242
- other_niche_low_confidence: 65
- severe_paid_spike_penalty: 157
- single_app_breakout_not_regular_alert: 152
- single_developer_dominance: 214
- single_developer_penalty: 263
- single_developer_share_too_high: 240
- too_few_apps_for_sendable: 237
- too_few_apps_for_trend_confidence: 237
- too_few_successful_new_apps: 152
- too_few_successful_new_apps_for_trend_confidence: 152
- too_few_unique_developers: 152
- top3_too_dominant: 351
- top_app_concentration_penalty: 286
- top_app_too_dominant: 286
- unknown_pattern_blocker_active: 70

## Top Qualified But Not Sent
- ALERT coloring score=90.99 sendable=88.19 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=834189 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.66 sendable=82.76 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=14069 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.13 sendable=82.34 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=30125 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.1 sendable=81.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=43698 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.27 sendable=81.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=834200 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.03 sendable=80.92 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=296315 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.03 sendable=80.91 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=86258 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=84.1 sendable=80.07 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.82 installs=149939 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.54 sendable=79.92 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.87 installs=1549765 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.54 sendable=79.79 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=43081 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.91 sendable=79.78 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.79 installs=3444121 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.51 sendable=79.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.69 installs=677733 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.82 sendable=79.51 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=146477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=88.18 sendable=79.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.49 installs=1218541 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.82 sendable=78.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1313467 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=81.39 sendable=78.7 stage=QUALIFIED_CANDIDATE_ONLY quality=86.58 mvp=81.62 installs=109382 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.08 sendable=78.63 stage=QUALIFIED_CANDIDATE_ONLY quality=87.63 mvp=85.0 installs=60344 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.85 sendable=77.93 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.29 installs=238036 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=82.88 sendable=77.77 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.19 installs=190366 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.26 sendable=77.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=362617 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
