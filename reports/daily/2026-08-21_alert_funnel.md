# Alert Funnel - 2026-08-21

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 102
- NEAR_MISS: 115
- REJECT: 209
- SINGLE_APP_WATCH: 11
- WATCH: 177

## Alert Stage Counts
- COOLDOWN_BLOCKED: 7
- NONE: 512
- QUALIFIED_CANDIDATE_ONLY: 93
- SENDABLE_ALERT: 2

## Blocked Counts
- cooldown_blocked: 7
- duplicate_market_signals_suppressed: 112
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 188
- below_data_quality_for_trend_confidence: 315
- below_data_quality_score: 315
- below_mvp_feasibility: 196
- below_opportunity_score: 489
- below_sendable_alert_score: 605
- below_team_fit_score: 365
- below_trend_confidence_score: 332
- blocked_risk_tag: 131
- complex_full_product: 265
- cooldown_normalized_niche: 7
- duplicate_market_signal: 112
- giant_developer_competition: 33
- giant_developer_penalty: 31
- giant_share_too_high: 23
- growth_by_one_app_too_high: 295
- high_mvp_complexity: 122
- high_production_complexity: 62
- leader_dominated_market: 244
- low_classification_confidence: 188
- low_developer_diversity: 152
- low_mvp_feasibility: 196
- low_total_daily_installs: 133
- low_total_daily_installs_for_trend_confidence: 133
- market_signal_duplicate: 3
- not_alert_status: 512
- one_app_growth_penalty: 334
- organic_confidence_low: 237
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 131
- single_app_breakout_not_regular_alert: 151
- single_developer_dominance: 226
- single_developer_penalty: 267
- single_developer_share_too_high: 246
- too_few_apps_for_sendable: 230
- too_few_apps_for_trend_confidence: 230
- too_few_successful_new_apps: 151
- too_few_successful_new_apps_for_trend_confidence: 151
- too_few_unique_developers: 152
- top3_too_dominant: 356
- top_app_concentration_penalty: 293
- top_app_too_dominant: 293
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.75 sendable=85.16 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=56950 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.73 sendable=82.38 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=25481 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=76.8 sendable=82.02 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=16766 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.47 sendable=81.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.25 installs=2322463 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.44 sendable=80.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1946546 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.97 sendable=80.28 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=229616 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=83.18 sendable=80.18 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=112873 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=79.81 sendable=79.54 stage=QUALIFIED_CANDIDATE_ONLY quality=94.37 mvp=65.0 installs=53779 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.8 sendable=79.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.73 installs=327286 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.63 sendable=79.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.83 installs=647170 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.07 sendable=79.08 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.82 installs=1464154 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.82 sendable=79.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.85 installs=4999682 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=81.02 sendable=78.37 stage=QUALIFIED_CANDIDATE_ONLY quality=87.06 mvp=76.0 installs=134576 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.23 sendable=77.91 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=57336 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=89.14 sendable=77.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1594210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.11 sendable=76.92 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=527514 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.57 sendable=76.34 stage=QUALIFIED_CANDIDATE_ONLY quality=84.88 mvp=85.0 installs=54831 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.08 sendable=75.53 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.97 installs=1606046 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.4 sendable=75.4 stage=QUALIFIED_CANDIDATE_ONLY quality=87.73 mvp=85.0 installs=54309 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.35 sendable=74.95 stage=QUALIFIED_CANDIDATE_ONLY quality=94.77 mvp=65.0 installs=15153 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
