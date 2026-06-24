# Alert Funnel - 2026-06-24

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 71
- NEAR_MISS: 98
- REJECT: 153
- SINGLE_APP_WATCH: 27
- WATCH: 221

## Alert Stage Counts
- COOLDOWN_BLOCKED: 36
- NONE: 499
- QUALIFIED_CANDIDATE_ONLY: 34
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 36
- duplicate_market_signals_suppressed: 111
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 175
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 195
- below_opportunity_score: 484
- below_sendable_alert_score: 570
- below_team_fit_score: 369
- below_trend_confidence_score: 387
- blocked_risk_tag: 48
- complex_full_product: 278
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 36
- duplicate_market_signal: 111
- giant_developer_competition: 29
- giant_developer_penalty: 25
- giant_share_too_high: 15
- growth_by_one_app_too_high: 233
- high_mvp_complexity: 127
- high_production_complexity: 58
- leader_dominated_market: 211
- low_classification_confidence: 175
- low_developer_diversity: 137
- low_mvp_feasibility: 195
- low_total_daily_installs: 133
- low_total_daily_installs_for_trend_confidence: 133
- market_signal_duplicate: 4
- no_growth_history: 1
- not_alert_status: 499
- one_app_growth_penalty: 251
- organic_confidence_low: 192
- other_niche_low_confidence: 67
- severe_paid_spike_penalty: 44
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 192
- single_developer_penalty: 225
- single_developer_share_too_high: 210
- too_few_apps_for_sendable: 208
- too_few_apps_for_trend_confidence: 208
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 137
- top3_too_dominant: 328
- top_app_concentration_penalty: 247
- top_app_too_dominant: 247
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT block_puzzle score=88.08 sendable=78.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.43 installs=1159705 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.46 sendable=78.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=68861 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.62 sendable=77.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.99 installs=690701 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.8 sendable=77.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=38891 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.07 sendable=77.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=500206 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=87.9 sendable=77.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=487756 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.94 sendable=76.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.48 installs=106546 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.52 sendable=75.53 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=625765 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=79.2 sendable=75.14 stage=QUALIFIED_CANDIDATE_ONLY quality=86.35 mvp=77.64 installs=27820 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.21 sendable=74.28 stage=COOLDOWN_BLOCKED quality=85.84 mvp=79.94 installs=56445 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.62 sendable=74.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.62 installs=1286557 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=73.67 sendable=71.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.75 installs=43823 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.33 sendable=71.03 stage=COOLDOWN_BLOCKED quality=90.24 mvp=85.0 installs=23814 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT sort_puzzle score=79.91 sendable=70.9 stage=COOLDOWN_BLOCKED quality=86.06 mvp=85.0 installs=22971 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.47 sendable=70.48 stage=QUALIFIED_CANDIDATE_ONLY quality=94.72 mvp=65.0 installs=159137 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT mahjong score=86.9 sendable=69.43 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=165649 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=83.35 sendable=69.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.89 installs=131193 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=84.42 sendable=69.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.81 installs=605079 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=82.8 sendable=68.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=63.06 installs=549640 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT idle_tycoon score=82.12 sendable=68.21 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.64 installs=123170 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
