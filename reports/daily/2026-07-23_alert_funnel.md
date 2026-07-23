# Alert Funnel - 2026-07-23

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 86
- NEAR_MISS: 113
- REJECT: 167
- SINGLE_APP_WATCH: 17
- WATCH: 195

## Alert Stage Counts
- COOLDOWN_BLOCKED: 4
- NONE: 492
- QUALIFIED_CANDIDATE_ONLY: 80
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 4
- duplicate_market_signals_suppressed: 112
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 72
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 284
- below_data_quality_score: 284
- below_mvp_feasibility: 186
- below_opportunity_score: 485
- below_sendable_alert_score: 572
- below_team_fit_score: 353
- below_trend_confidence_score: 355
- blocked_risk_tag: 78
- complex_full_product: 272
- cooldown_normalized_niche: 4
- duplicate_market_signal: 112
- giant_developer_competition: 28
- giant_developer_penalty: 24
- giant_share_too_high: 12
- growth_by_one_app_too_high: 282
- high_mvp_complexity: 124
- high_production_complexity: 52
- leader_dominated_market: 213
- low_classification_confidence: 185
- low_developer_diversity: 119
- low_mvp_feasibility: 186
- low_total_daily_installs: 115
- low_total_daily_installs_for_trend_confidence: 115
- market_signal_duplicate: 7
- not_alert_status: 492
- one_app_growth_penalty: 313
- organic_confidence_low: 199
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 77
- single_app_breakout_not_regular_alert: 119
- single_developer_dominance: 192
- single_developer_penalty: 236
- single_developer_share_too_high: 213
- too_few_apps_for_sendable: 198
- too_few_apps_for_trend_confidence: 198
- too_few_successful_new_apps: 119
- too_few_successful_new_apps_for_trend_confidence: 119
- too_few_unique_developers: 119
- top3_too_dominant: 320
- top_app_concentration_penalty: 258
- top_app_too_dominant: 258
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT sort_puzzle score=89.16 sendable=81.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=900915 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.95 sendable=81.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=929994 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.73 sendable=81.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=29008 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.8 sendable=80.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1178649 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.97 sendable=79.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.96 installs=1372585 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.58 sendable=78.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=150909 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.78 sendable=78.0 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=633643 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.43 sendable=77.78 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=121364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=88.04 sendable=77.69 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.33 installs=1392200 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.51 sendable=76.77 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.41 installs=848522 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.58 sendable=76.7 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=38423 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.26 sendable=76.66 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=42888 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=85.15 sendable=76.23 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.03 installs=390376 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.85 sendable=76.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.22 installs=1122139 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.67 sendable=75.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=273038 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.56 sendable=74.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=50359 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.42 sendable=74.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.95 installs=1266666 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=70.39 sendable=71.87 stage=QUALIFIED_CANDIDATE_ONLY quality=91.03 mvp=65.0 installs=24284 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.37 sendable=71.8 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.23 installs=3529835 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT block_puzzle score=86.86 sendable=71.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.45 installs=1194589 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
