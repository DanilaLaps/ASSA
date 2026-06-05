# Alert Funnel - 2026-06-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 6
- NEAR_MISS: 149
- REJECT: 160
- SINGLE_APP_WATCH: 17
- WATCH: 287

## Alert Stage Counts
- NONE: 613
- QUALIFIED_CANDIDATE_ONLY: 6

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 115
- limit_blocked: 0

## Sendable Failure Distribution
- below_classification_confidence: 194
- below_data_quality_for_trend_confidence: 429
- below_data_quality_score: 429
- below_mvp_feasibility: 200
- below_opportunity_score: 549
- below_sendable_alert_score: 619
- below_team_fit_score: 377
- below_trend_confidence_score: 472
- blocked_risk_tag: 155
- complex_full_product: 280
- duplicate_market_signal: 115
- giant_developer_competition: 32
- giant_developer_penalty: 31
- giant_share_too_high: 19
- growth_by_one_app_too_high: 363
- high_mvp_complexity: 135
- high_production_complexity: 56
- leader_dominated_market: 228
- low_classification_confidence: 194
- low_developer_diversity: 139
- low_mvp_feasibility: 200
- low_total_daily_installs: 127
- low_total_daily_installs_for_trend_confidence: 127
- no_growth_history: 9
- not_alert_status: 613
- one_app_growth_penalty: 402
- organic_confidence_low: 218
- other_niche_low_confidence: 200
- severe_paid_spike_penalty: 120
- single_app_breakout_not_regular_alert: 139
- single_developer_dominance: 205
- single_developer_penalty: 244
- single_developer_share_too_high: 230
- too_few_apps_for_sendable: 212
- too_few_apps_for_trend_confidence: 212
- too_few_successful_new_apps: 139
- too_few_successful_new_apps_for_trend_confidence: 139
- too_few_unique_developers: 139
- top3_too_dominant: 358
- top_app_concentration_penalty: 273
- top_app_too_dominant: 273
- unknown_pattern_low_confidence: 555

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.43 sendable=77.18 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=85.0 installs=74010 risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=76.69 sendable=74.42 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=402600 risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=75.57 sendable=73.96 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=295221 risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=70.74 sendable=65.92 stage=QUALIFIED_CANDIDATE_ONLY quality=84.93 mvp=65.0 installs=29477 risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
- ALERT hidden_object score=70.57 sendable=63.22 stage=QUALIFIED_CANDIDATE_ONLY quality=81.58 mvp=65.0 installs=172404 risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
- ALERT hidden_object score=70.74 sendable=50.63 stage=QUALIFIED_CANDIDATE_ONLY quality=79.97 mvp=65.0 installs=75982 risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
