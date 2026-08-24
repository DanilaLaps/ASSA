# Alert Funnel - 2026-08-24

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 102
- NEAR_MISS: 100
- REJECT: 200
- SINGLE_APP_WATCH: 7
- WATCH: 175

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 482
- QUALIFIED_CANDIDATE_ONLY: 100
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 108
- limit_blocked: 1

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 179
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 184
- below_opportunity_score: 464
- below_sendable_alert_score: 580
- below_team_fit_score: 345
- below_trend_confidence_score: 331
- blocked_risk_tag: 115
- complex_full_product: 250
- cooldown_normalized_niche: 1
- duplicate_market_signal: 108
- giant_developer_competition: 29
- giant_developer_penalty: 26
- giant_share_too_high: 20
- growth_by_one_app_too_high: 276
- high_mvp_complexity: 118
- high_production_complexity: 58
- leader_dominated_market: 224
- low_classification_confidence: 179
- low_developer_diversity: 141
- low_mvp_feasibility: 184
- low_total_daily_installs: 151
- low_total_daily_installs_for_trend_confidence: 151
- market_signal_duplicate: 7
- not_alert_status: 482
- one_app_growth_penalty: 293
- organic_confidence_low: 215
- other_niche_low_confidence: 60
- per_niche_limit_blocked: 1
- severe_paid_spike_penalty: 114
- single_app_breakout_not_regular_alert: 141
- single_developer_dominance: 207
- single_developer_penalty: 243
- single_developer_share_too_high: 225
- too_few_apps_for_sendable: 213
- too_few_apps_for_trend_confidence: 213
- too_few_successful_new_apps: 141
- too_few_successful_new_apps_for_trend_confidence: 141
- too_few_unique_developers: 141
- top3_too_dominant: 330
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT coloring score=90.35 sendable=85.58 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1000068 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.38 sendable=82.52 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=36963 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT sort_puzzle score=88.07 sendable=81.28 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=442134 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=87.71 sendable=79.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=275364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.39 sendable=78.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.76 installs=1287933 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.22 sendable=78.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=343905 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.59 sendable=78.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.71 installs=405514 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.71 sendable=78.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.12 installs=1073809 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.25 sendable=78.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.01 installs=3384524 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.21 sendable=78.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=794903 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.66 sendable=77.63 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=74700 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.09 sendable=77.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.68 installs=210567 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.68 sendable=77.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1144465 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.37 sendable=76.82 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1269086 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.54 sendable=76.61 stage=QUALIFIED_CANDIDATE_ONLY quality=93.73 mvp=65.0 installs=11457 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=80.34 sendable=76.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=94484 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.91 sendable=76.15 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.62 installs=134864 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.19 sendable=75.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=643555 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=81.4 sendable=75.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.59 installs=143131 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sandbox score=78.47 sendable=75.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.25 installs=63197 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
