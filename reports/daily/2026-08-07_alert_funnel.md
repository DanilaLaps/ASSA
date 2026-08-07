# Alert Funnel - 2026-08-07

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 65
- NEAR_MISS: 114
- REJECT: 174
- SINGLE_APP_WATCH: 16
- WATCH: 179

## Alert Stage Counts
- COOLDOWN_BLOCKED: 36
- NONE: 483
- QUALIFIED_CANDIDATE_ONLY: 28
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 36
- duplicate_market_signals_suppressed: 123
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 70
- unknown_dominant_cluster: 61
- unknown_pattern_blocker_active: 61

## Sendable Failure Distribution
- below_classification_confidence: 166
- below_data_quality_for_trend_confidence: 285
- below_data_quality_score: 285
- below_mvp_feasibility: 176
- below_opportunity_score: 463
- below_sendable_alert_score: 547
- below_team_fit_score: 337
- below_trend_confidence_score: 384
- blocked_risk_tag: 63
- complex_full_product: 246
- cooldown_normalized_niche: 36
- duplicate_market_signal: 123
- giant_developer_competition: 28
- giant_developer_penalty: 23
- giant_share_too_high: 17
- growth_by_one_app_too_high: 238
- high_mvp_complexity: 120
- high_production_complexity: 63
- leader_dominated_market: 224
- low_classification_confidence: 166
- low_developer_diversity: 150
- low_mvp_feasibility: 176
- low_total_daily_installs: 154
- low_total_daily_installs_for_trend_confidence: 154
- market_signal_duplicate: 2
- not_alert_status: 483
- one_app_growth_penalty: 252
- organic_confidence_low: 205
- other_niche_low_confidence: 55
- severe_paid_spike_penalty: 62
- single_app_breakout_not_regular_alert: 150
- single_developer_dominance: 211
- single_developer_penalty: 238
- single_developer_share_too_high: 225
- too_few_apps_for_sendable: 220
- too_few_apps_for_trend_confidence: 220
- too_few_successful_new_apps: 150
- too_few_successful_new_apps_for_trend_confidence: 150
- too_few_unique_developers: 150
- top3_too_dominant: 323
- top_app_concentration_penalty: 257
- top_app_too_dominant: 257
- unknown_pattern_blocker_active: 57

## Top Qualified But Not Sent
- ALERT sort_puzzle score=79.16 sendable=80.89 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=24752 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=85.16 sendable=78.55 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=107253 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.63 sendable=75.94 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.17 installs=792270 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.17 sendable=75.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=12140 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.56 sendable=74.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.07 installs=819511 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.17 sendable=74.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.0 installs=763023 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.99 sendable=73.75 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.53 installs=1955751 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.82 sendable=73.71 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.65 installs=61276 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.94 sendable=73.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=721286 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.63 sendable=73.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.48 installs=126782 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=80.39 sendable=73.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.77 installs=108024 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.01 sendable=72.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=763734 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=86.79 sendable=70.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=62.27 installs=307906 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT arrow_puzzle score=82.98 sendable=69.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=60.49 installs=346295 unknown_app_share=0.4216 unknown_installs_share=0.3839 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT runner score=84.81 sendable=69.45 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.04 installs=828095 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=73.95 sendable=69.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=12560 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.38 sendable=69.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=1081615 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=83.23 sendable=69.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.84 installs=147955 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=81.67 sendable=68.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=120064 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sandbox score=80.87 sendable=68.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.25 installs=70688 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
