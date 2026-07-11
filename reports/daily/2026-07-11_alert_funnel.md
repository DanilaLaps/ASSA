# Alert Funnel - 2026-07-11

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 98
- NEAR_MISS: 98
- REJECT: 189
- SINGLE_APP_WATCH: 13
- WATCH: 157

## Alert Stage Counts
- COOLDOWN_BLOCKED: 5
- NONE: 457
- QUALIFIED_CANDIDATE_ONLY: 92
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 5
- duplicate_market_signals_suppressed: 126
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 184
- below_data_quality_for_trend_confidence: 275
- below_data_quality_score: 275
- below_mvp_feasibility: 186
- below_opportunity_score: 452
- below_sendable_alert_score: 548
- below_team_fit_score: 345
- below_trend_confidence_score: 275
- blocked_risk_tag: 134
- complex_full_product: 254
- cooldown_normalized_niche: 5
- duplicate_market_signal: 126
- giant_developer_competition: 31
- giant_developer_penalty: 28
- giant_share_too_high: 24
- growth_by_one_app_too_high: 247
- high_mvp_complexity: 122
- high_production_complexity: 61
- leader_dominated_market: 216
- low_classification_confidence: 184
- low_developer_diversity: 118
- low_mvp_feasibility: 186
- low_total_daily_installs: 100
- low_total_daily_installs_for_trend_confidence: 100
- market_signal_duplicate: 13
- no_growth_history: 7
- not_alert_status: 457
- one_app_growth_penalty: 276
- organic_confidence_low: 216
- other_niche_low_confidence: 57
- severe_paid_spike_penalty: 125
- single_app_breakout_not_regular_alert: 118
- single_developer_dominance: 199
- single_developer_penalty: 243
- single_developer_share_too_high: 217
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 118
- too_few_successful_new_apps_for_trend_confidence: 118
- too_few_unique_developers: 118
- top3_too_dominant: 345
- top_app_concentration_penalty: 273
- top_app_too_dominant: 273
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT sort_puzzle score=89.27 sendable=82.82 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1018740 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=90.12 sendable=82.37 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1258125 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.94 sendable=81.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=373716 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=87.85 sendable=81.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1429785 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.64 sendable=81.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=956269 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.32 sendable=80.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.08 installs=1368707 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.26 sendable=79.85 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=83656 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.83 sendable=79.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.35 installs=5328037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.28 sendable=78.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=56622 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.14 sendable=78.1 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=131292 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.33 sendable=77.78 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.01 installs=2273451 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=82.0 sendable=77.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=238732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.28 sendable=77.36 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.62 installs=133879 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=70.91 sendable=76.36 stage=QUALIFIED_CANDIDATE_ONLY quality=91.0 mvp=85.0 installs=19546 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT other score=76.58 sendable=76.0 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=50001 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=79.17 sendable=75.69 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.5 installs=470277 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=87.25 sendable=75.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.03 installs=1585517 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.02 sendable=75.5 stage=QUALIFIED_CANDIDATE_ONLY quality=87.51 mvp=85.0 installs=106263 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.01 sendable=75.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1885560 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=88.52 sendable=75.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=972865 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
