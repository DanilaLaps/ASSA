# Alert Funnel - 2026-08-26

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 70
- NEAR_MISS: 118
- REJECT: 182
- SINGLE_APP_WATCH: 19
- WATCH: 186

## Alert Stage Counts
- NONE: 505
- QUALIFIED_CANDIDATE_ONLY: 69
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 180
- below_data_quality_for_trend_confidence: 308
- below_data_quality_score: 308
- below_mvp_feasibility: 190
- below_opportunity_score: 491
- below_sendable_alert_score: 574
- below_team_fit_score: 341
- below_trend_confidence_score: 397
- blocked_risk_tag: 75
- complex_full_product: 253
- duplicate_market_signal: 119
- giant_developer_competition: 30
- giant_developer_penalty: 23
- giant_share_too_high: 18
- growth_by_one_app_too_high: 269
- high_mvp_complexity: 118
- high_production_complexity: 64
- leader_dominated_market: 226
- low_classification_confidence: 180
- low_developer_diversity: 143
- low_mvp_feasibility: 190
- low_total_daily_installs: 156
- low_total_daily_installs_for_trend_confidence: 156
- market_signal_duplicate: 5
- no_growth_history: 2
- not_alert_status: 505
- one_app_growth_penalty: 280
- organic_confidence_low: 219
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 73
- single_app_breakout_not_regular_alert: 143
- single_developer_dominance: 208
- single_developer_penalty: 253
- single_developer_share_too_high: 227
- too_few_apps_for_sendable: 223
- too_few_apps_for_trend_confidence: 223
- too_few_successful_new_apps: 143
- too_few_successful_new_apps_for_trend_confidence: 143
- too_few_unique_developers: 143
- top3_too_dominant: 329
- top_app_concentration_penalty: 270
- top_app_too_dominant: 270
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT block_puzzle score=86.9 sendable=79.09 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.18 installs=990464 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.04 sendable=78.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1128699 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.24 sendable=78.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.65 installs=1256398 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.5 sendable=78.1 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=32429 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=77.22 sendable=77.82 stage=QUALIFIED_CANDIDATE_ONLY quality=93.82 mvp=65.0 installs=12193 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.35 sendable=77.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.86 installs=940308 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.47 sendable=77.07 stage=QUALIFIED_CANDIDATE_ONLY quality=87.49 mvp=85.0 installs=27549 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.42 sendable=76.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=55726 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.52 sendable=76.1 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=21268 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.7 sendable=75.48 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.91 installs=1565805 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.36 sendable=74.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.64 installs=184401 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.41 sendable=74.0 stage=QUALIFIED_CANDIDATE_ONLY quality=87.56 mvp=69.57 installs=78387 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=80.39 sendable=73.84 stage=QUALIFIED_CANDIDATE_ONLY quality=87.19 mvp=77.89 installs=82477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.54 sendable=73.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.63 installs=921218 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT tile_match score=76.79 sendable=71.41 stage=QUALIFIED_CANDIDATE_ONLY quality=87.59 mvp=73.75 installs=35786 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.36 sendable=70.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.44 installs=1735494 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT idle_tycoon score=84.91 sendable=69.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=380823 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=77.16 sendable=69.24 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=106663 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=80.86 sendable=69.03 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.18 installs=138673 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=83.43 sendable=68.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.89 installs=210450 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
