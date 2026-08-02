# Alert Funnel - 2026-08-02

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 105
- NEAR_MISS: 110
- REJECT: 203
- SINGLE_APP_WATCH: 14
- WATCH: 163

## Alert Stage Counts
- COOLDOWN_BLOCKED: 23
- NONE: 490
- QUALIFIED_CANDIDATE_ONLY: 81
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 23
- duplicate_market_signals_suppressed: 123
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 174
- below_data_quality_for_trend_confidence: 304
- below_data_quality_score: 304
- below_mvp_feasibility: 189
- below_opportunity_score: 475
- below_sendable_alert_score: 593
- below_team_fit_score: 361
- below_trend_confidence_score: 362
- blocked_risk_tag: 116
- complex_full_product: 259
- cooldown_normalized_niche: 23
- duplicate_market_signal: 123
- giant_developer_competition: 32
- giant_developer_penalty: 28
- giant_share_too_high: 19
- growth_by_one_app_too_high: 264
- high_mvp_complexity: 127
- high_production_complexity: 62
- leader_dominated_market: 234
- low_classification_confidence: 174
- low_developer_diversity: 147
- low_mvp_feasibility: 189
- low_total_daily_installs: 151
- low_total_daily_installs_for_trend_confidence: 151
- market_signal_duplicate: 12
- no_growth_history: 1
- not_alert_status: 490
- one_app_growth_penalty: 283
- organic_confidence_low: 227
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 114
- single_app_breakout_not_regular_alert: 146
- single_developer_dominance: 209
- single_developer_penalty: 261
- single_developer_share_too_high: 236
- too_few_apps_for_sendable: 231
- too_few_apps_for_trend_confidence: 231
- too_few_successful_new_apps: 146
- too_few_successful_new_apps_for_trend_confidence: 146
- too_few_unique_developers: 147
- top3_too_dominant: 349
- top_app_concentration_penalty: 282
- top_app_too_dominant: 282
- unknown_pattern_blocker_active: 65

## Top Qualified But Not Sent
- ALERT coloring score=90.95 sendable=87.06 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=842221 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.75 sendable=81.51 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=30050 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.81 sendable=79.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.41 installs=1218684 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.66 sendable=78.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=356869 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.67 sendable=78.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.48 installs=813832 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.08 sendable=78.15 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=176674 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.19 sendable=78.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.31 installs=1060673 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.74 sendable=77.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=170222 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.24 sendable=77.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1012693 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.36 sendable=76.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=145835 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.99 sendable=76.15 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=81522 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=88.85 sendable=75.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1610133 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=84.5 sendable=75.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=93268 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.16 sendable=75.54 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=418267 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.89 sendable=75.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=52199 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.89 sendable=74.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=883346 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.99 sendable=74.57 stage=COOLDOWN_BLOCKED quality=86.94 mvp=70.5 installs=32258 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=76.58 sendable=73.78 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.08 installs=21908 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.93 sendable=73.75 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.31 installs=2786250 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=82.22 sendable=71.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.6 installs=47494 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
