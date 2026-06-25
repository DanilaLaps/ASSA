# Alert Funnel - 2026-06-25

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 69
- NEAR_MISS: 105
- REJECT: 160
- SINGLE_APP_WATCH: 26
- WATCH: 208

## Alert Stage Counts
- COOLDOWN_BLOCKED: 19
- NONE: 499
- QUALIFIED_CANDIDATE_ONLY: 49
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 19
- duplicate_market_signals_suppressed: 105
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 176
- below_data_quality_for_trend_confidence: 288
- below_data_quality_score: 288
- below_mvp_feasibility: 196
- below_opportunity_score: 481
- below_sendable_alert_score: 568
- below_team_fit_score: 371
- below_trend_confidence_score: 387
- blocked_risk_tag: 56
- complex_full_product: 280
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 19
- duplicate_market_signal: 105
- giant_developer_competition: 29
- giant_developer_penalty: 26
- giant_share_too_high: 17
- growth_by_one_app_too_high: 236
- high_mvp_complexity: 128
- high_production_complexity: 59
- leader_dominated_market: 211
- low_classification_confidence: 176
- low_developer_diversity: 136
- low_mvp_feasibility: 196
- low_total_daily_installs: 131
- low_total_daily_installs_for_trend_confidence: 131
- market_signal_duplicate: 5
- no_growth_history: 2
- not_alert_status: 499
- one_app_growth_penalty: 251
- organic_confidence_low: 198
- other_niche_low_confidence: 67
- severe_paid_spike_penalty: 52
- single_app_breakout_not_regular_alert: 136
- single_developer_dominance: 196
- single_developer_penalty: 228
- single_developer_share_too_high: 211
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 136
- too_few_successful_new_apps_for_trend_confidence: 136
- too_few_unique_developers: 136
- top3_too_dominant: 326
- top_app_concentration_penalty: 250
- top_app_too_dominant: 250
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT block_puzzle score=88.0 sendable=78.93 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.25 installs=1176929 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.95 sendable=78.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=517041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.57 sendable=77.58 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=37085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.53 sendable=77.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=67265 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=88.68 sendable=76.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=395245 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.37 sendable=76.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.03 installs=74831 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=80.92 sendable=75.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.07 installs=297459 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.48 sendable=75.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=627426 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=87.7 sendable=75.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.54 installs=1251292 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.49 sendable=72.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.8 installs=334828 unknown_app_share=0.2817 unknown_installs_share=0.2857 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT block_puzzle score=74.3 sendable=71.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.75 installs=46603 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=79.06 sendable=71.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.56 installs=34670 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.21 sendable=71.4 stage=COOLDOWN_BLOCKED quality=86.25 mvp=85.0 installs=23411 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.66 sendable=70.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.95 installs=715088 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.79 sendable=69.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.75 installs=40369 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.52 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.8 installs=560743 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=83.29 sendable=68.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=255842 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=82.25 sendable=68.26 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.63 installs=126684 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=81.19 sendable=67.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.43 installs=80504 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.3 sendable=67.35 stage=COOLDOWN_BLOCKED quality=84.83 mvp=79.6 installs=60406 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
