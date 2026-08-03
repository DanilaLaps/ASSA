# Alert Funnel - 2026-08-03

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 112
- NEAR_MISS: 105
- REJECT: 203
- SINGLE_APP_WATCH: 12
- WATCH: 157

## Alert Stage Counts
- COOLDOWN_BLOCKED: 3
- NONE: 477
- QUALIFIED_CANDIDATE_ONLY: 108
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 3
- duplicate_market_signals_suppressed: 128
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 65
- unknown_pattern_blocker_active: 65

## Sendable Failure Distribution
- below_classification_confidence: 174
- below_data_quality_for_trend_confidence: 279
- below_data_quality_score: 279
- below_mvp_feasibility: 190
- below_opportunity_score: 463
- below_sendable_alert_score: 585
- below_team_fit_score: 370
- below_trend_confidence_score: 323
- blocked_risk_tag: 131
- complex_full_product: 264
- cooldown_normalized_niche: 3
- duplicate_market_signal: 128
- giant_developer_competition: 31
- giant_developer_penalty: 28
- giant_share_too_high: 20
- growth_by_one_app_too_high: 249
- high_mvp_complexity: 129
- high_production_complexity: 61
- leader_dominated_market: 235
- low_classification_confidence: 174
- low_developer_diversity: 148
- low_mvp_feasibility: 190
- low_total_daily_installs: 148
- low_total_daily_installs_for_trend_confidence: 148
- market_signal_duplicate: 15
- no_growth_history: 1
- not_alert_status: 477
- one_app_growth_penalty: 271
- organic_confidence_low: 234
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 129
- single_app_breakout_not_regular_alert: 147
- single_developer_dominance: 211
- single_developer_penalty: 252
- single_developer_share_too_high: 236
- too_few_apps_for_sendable: 227
- too_few_apps_for_trend_confidence: 227
- too_few_successful_new_apps: 147
- too_few_successful_new_apps_for_trend_confidence: 147
- too_few_unique_developers: 148
- top3_too_dominant: 351
- top_app_concentration_penalty: 276
- top_app_too_dominant: 276
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT coloring score=90.54 sendable=82.23 stage=COOLDOWN_BLOCKED quality=94.8 mvp=85.0 installs=890135 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=86.44 sendable=80.77 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=194901 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=90.35 sendable=80.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1036977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.25 sendable=79.19 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=92904 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=88.53 sendable=79.15 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.27 installs=1217184 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.15 sendable=78.71 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=1084003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.07 sendable=78.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.2 installs=807695 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.06 sendable=78.38 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=47507 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.9 sendable=78.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.36 installs=2868657 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.3 sendable=78.06 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.76 installs=908712 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.03 sendable=77.59 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=420210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.77 sendable=77.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.64 installs=217924 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.39 sendable=77.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=158786 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.88 sendable=77.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=54414 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.26 sendable=76.38 stage=QUALIFIED_CANDIDATE_ONLY quality=86.12 mvp=85.0 installs=52300 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.16 sendable=76.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1611009 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=84.42 sendable=76.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=77333 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.19 sendable=75.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=17591 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.58 sendable=75.41 stage=QUALIFIED_CANDIDATE_ONLY quality=91.63 mvp=65.0 installs=43765 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=71.55 sendable=74.89 stage=QUALIFIED_CANDIDATE_ONLY quality=91.0 mvp=85.0 installs=15731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
