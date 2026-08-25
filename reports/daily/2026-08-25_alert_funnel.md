# Alert Funnel - 2026-08-25

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 71
- NEAR_MISS: 117
- REJECT: 179
- SINGLE_APP_WATCH: 19
- WATCH: 193

## Alert Stage Counts
- COOLDOWN_BLOCKED: 40
- NONE: 508
- QUALIFIED_CANDIDATE_ONLY: 30
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 40
- duplicate_market_signals_suppressed: 116
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 173
- below_data_quality_for_trend_confidence: 295
- below_data_quality_score: 295
- below_mvp_feasibility: 183
- below_opportunity_score: 487
- below_sendable_alert_score: 577
- below_team_fit_score: 340
- below_trend_confidence_score: 388
- blocked_risk_tag: 75
- complex_full_product: 251
- cooldown_exact_dedupe_key: 3
- cooldown_normalized_niche: 40
- duplicate_market_signal: 116
- giant_developer_competition: 31
- giant_developer_penalty: 27
- giant_share_too_high: 21
- growth_by_one_app_too_high: 275
- high_mvp_complexity: 119
- high_production_complexity: 62
- leader_dominated_market: 226
- low_classification_confidence: 173
- low_developer_diversity: 141
- low_mvp_feasibility: 183
- low_total_daily_installs: 150
- low_total_daily_installs_for_trend_confidence: 150
- market_signal_duplicate: 6
- not_alert_status: 508
- one_app_growth_penalty: 296
- organic_confidence_low: 210
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 75
- single_app_breakout_not_regular_alert: 141
- single_developer_dominance: 202
- single_developer_penalty: 244
- single_developer_share_too_high: 226
- too_few_apps_for_sendable: 210
- too_few_apps_for_trend_confidence: 210
- too_few_successful_new_apps: 141
- too_few_successful_new_apps_for_trend_confidence: 141
- too_few_unique_developers: 141
- top3_too_dominant: 331
- top_app_concentration_penalty: 260
- top_app_too_dominant: 260
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT sort_puzzle score=88.02 sendable=84.1 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=411806 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=82.22 sendable=81.67 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=51993 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT block_puzzle score=86.83 sendable=79.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.08 installs=962544 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.24 sendable=77.92 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.77 installs=889457 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.42 sendable=77.67 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=41796 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.06 sendable=76.37 stage=COOLDOWN_BLOCKED quality=87.78 mvp=68.78 installs=264961 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.8 sendable=76.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1093952 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=80.15 sendable=75.68 stage=QUALIFIED_CANDIDATE_ONLY quality=87.56 mvp=77.89 installs=87355 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.24 sendable=75.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.03 installs=1219515 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.96 sendable=74.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.86 installs=633353 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.43 sendable=73.36 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.12 installs=20391 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.99 sendable=73.18 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.93 installs=1019922 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.76 sendable=73.07 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.71 installs=970551 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.06 sendable=72.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=322527 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=81.63 sendable=71.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.15 installs=147037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=77.14 sendable=69.16 stage=COOLDOWN_BLOCKED quality=87.91 mvp=69.42 installs=70987 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=83.84 sendable=68.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=1628879 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=83.53 sendable=68.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=64.15 installs=220338 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT word_puzzle score=82.2 sendable=68.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=109484 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.79 sendable=68.16 stage=COOLDOWN_BLOCKED quality=94.48 mvp=65.0 installs=32838 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
