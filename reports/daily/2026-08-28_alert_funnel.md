# Alert Funnel - 2026-08-28

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 89
- NEAR_MISS: 105
- REJECT: 190
- SINGLE_APP_WATCH: 15
- WATCH: 190

## Alert Stage Counts
- COOLDOWN_BLOCKED: 2
- NONE: 500
- QUALIFIED_CANDIDATE_ONLY: 86
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 2
- duplicate_market_signals_suppressed: 118
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 309
- below_data_quality_score: 309
- below_mvp_feasibility: 187
- below_opportunity_score: 489
- below_sendable_alert_score: 586
- below_team_fit_score: 348
- below_trend_confidence_score: 368
- blocked_risk_tag: 98
- complex_full_product: 251
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 2
- duplicate_market_signal: 118
- giant_developer_competition: 31
- giant_developer_penalty: 29
- giant_share_too_high: 19
- growth_by_one_app_too_high: 284
- high_mvp_complexity: 122
- high_production_complexity: 60
- leader_dominated_market: 228
- low_classification_confidence: 185
- low_developer_diversity: 147
- low_mvp_feasibility: 187
- low_total_daily_installs: 130
- low_total_daily_installs_for_trend_confidence: 130
- market_signal_duplicate: 7
- not_alert_status: 500
- one_app_growth_penalty: 308
- organic_confidence_low: 222
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 96
- single_app_breakout_not_regular_alert: 147
- single_developer_dominance: 213
- single_developer_penalty: 254
- single_developer_share_too_high: 229
- too_few_apps_for_sendable: 222
- too_few_apps_for_trend_confidence: 222
- too_few_successful_new_apps: 147
- too_few_successful_new_apps_for_trend_confidence: 147
- too_few_unique_developers: 147
- top3_too_dominant: 345
- top_app_concentration_penalty: 276
- top_app_too_dominant: 276
- unknown_pattern_blocker_active: 69

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.68 sendable=81.04 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=59594 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.56 sendable=80.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1463897 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.14 sendable=78.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1481095 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.78 sendable=78.39 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=15311 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.21 sendable=77.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.7 installs=1668912 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.42 sendable=77.23 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=709920 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.07 sendable=77.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=384230 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.22 sendable=77.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.86 installs=732927 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.82 sendable=77.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=468522 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.74 sendable=76.82 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=36442 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.64 sendable=76.69 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.88 installs=1376666 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.86 sendable=76.21 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.83 installs=3948968 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.21 sendable=75.77 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.12 installs=1294474 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT other score=86.93 sendable=75.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.8 installs=334493 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.86 sendable=75.14 stage=QUALIFIED_CANDIDATE_ONLY quality=87.06 mvp=85.0 installs=37582 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=82.21 sendable=73.88 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.85 installs=179511 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.5 sendable=73.03 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.52 installs=476761 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.89 sendable=72.99 stage=QUALIFIED_CANDIDATE_ONLY quality=94.25 mvp=65.0 installs=50867 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=80.37 sendable=72.92 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=147492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=78.65 sendable=71.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.32 installs=44963 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
