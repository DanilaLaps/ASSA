# Alert Funnel - 2026-06-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 2
- NEAR_MISS: 167
- REJECT: 165
- SINGLE_APP_WATCH: 13
- WATCH: 274

## Alert Stage Counts
- NONE: 619
- QUALIFIED_CANDIDATE_ONLY: 2

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 117
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 653
- unknown_dominant_cluster: 653
- unknown_pattern_blocker_active: 586

## Sendable Failure Distribution
- below_classification_confidence: 194
- below_data_quality_for_trend_confidence: 415
- below_data_quality_score: 415
- below_mvp_feasibility: 201
- below_opportunity_score: 544
- below_sendable_alert_score: 621
- below_team_fit_score: 378
- below_trend_confidence_score: 465
- blocked_risk_tag: 158
- complex_full_product: 280
- duplicate_market_signal: 117
- giant_developer_competition: 31
- giant_developer_penalty: 30
- giant_share_too_high: 19
- growth_by_one_app_too_high: 362
- high_mvp_complexity: 135
- high_production_complexity: 56
- leader_dominated_market: 229
- low_classification_confidence: 194
- low_developer_diversity: 139
- low_mvp_feasibility: 201
- low_total_daily_installs: 128
- low_total_daily_installs_for_trend_confidence: 128
- no_growth_history: 10
- not_alert_status: 619
- one_app_growth_penalty: 407
- organic_confidence_low: 221
- other_niche_low_confidence: 201
- severe_paid_spike_penalty: 124
- single_app_breakout_not_regular_alert: 139
- single_developer_dominance: 205
- single_developer_penalty: 245
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 212
- too_few_apps_for_trend_confidence: 212
- too_few_successful_new_apps: 139
- too_few_successful_new_apps_for_trend_confidence: 139
- too_few_unique_developers: 139
- top3_too_dominant: 360
- top_app_concentration_penalty: 275
- top_app_too_dominant: 275
- unknown_pattern_blocker_active: 557

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.43 sendable=73.18 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=85.0 installs=74010 unknown_app_share=1.0 unknown_installs_share=1.0 first_blocking=below_sendable_alert_score risks=mixed_unknown_cluster, unknown_coverage, unknown_dominant_cluster, weak_rating_signal
- ALERT hidden_object score=70.74 sendable=61.92 stage=QUALIFIED_CANDIDATE_ONLY quality=84.93 mvp=65.0 installs=29477 unknown_app_share=1.0 unknown_installs_share=1.0 first_blocking=below_sendable_alert_score risks=mixed_unknown_cluster, unknown_coverage, unknown_dominant_cluster, weak_rating_signal, weak_revenue_signal
