# Alert Funnel - 2026-06-30

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 103
- NEAR_MISS: 114
- REJECT: 189
- SINGLE_APP_WATCH: 4
- WATCH: 148

## Alert Stage Counts
- COOLDOWN_BLOCKED: 50
- NONE: 455
- QUALIFIED_CANDIDATE_ONLY: 52
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 50
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 70
- unknown_pattern_blocker_active: 70

## Sendable Failure Distribution
- below_classification_confidence: 167
- below_data_quality_for_trend_confidence: 246
- below_data_quality_score: 246
- below_mvp_feasibility: 194
- below_opportunity_score: 452
- below_sendable_alert_score: 554
- below_team_fit_score: 354
- below_trend_confidence_score: 242
- blocked_risk_tag: 156
- complex_full_product: 252
- cooldown_normalized_niche: 50
- duplicate_market_signal: 119
- giant_developer_competition: 34
- giant_developer_penalty: 28
- giant_share_too_high: 18
- growth_by_one_app_too_high: 249
- high_mvp_complexity: 115
- high_production_complexity: 57
- leader_dominated_market: 222
- low_classification_confidence: 167
- low_developer_diversity: 139
- low_mvp_feasibility: 194
- low_total_daily_installs: 71
- low_total_daily_installs_for_trend_confidence: 71
- market_signal_duplicate: 6
- no_growth_history: 3
- not_alert_status: 455
- one_app_growth_penalty: 277
- organic_confidence_low: 212
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 154
- single_app_breakout_not_regular_alert: 138
- single_developer_dominance: 207
- single_developer_penalty: 243
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 213
- too_few_apps_for_trend_confidence: 213
- too_few_successful_new_apps: 138
- too_few_successful_new_apps_for_trend_confidence: 138
- too_few_unique_developers: 139
- top3_too_dominant: 343
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 69
- weak_monetization_signal: 1

## Top Qualified But Not Sent
- ALERT tile_match score=88.55 sendable=82.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1815598 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.51 sendable=82.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=2703230 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.87 sendable=81.04 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=343241 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT other score=86.57 sendable=80.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.25 installs=6515722 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.42 sendable=79.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.5 installs=1720034 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.34 sendable=79.62 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=99385 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=84.39 sendable=79.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=142132 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.49 sendable=79.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=335921 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.04 sendable=79.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1441126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=81.46 sendable=79.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.39 installs=212026 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.7 sendable=78.82 stage=COOLDOWN_BLOCKED quality=86.77 mvp=82.55 installs=146510 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=83.62 sendable=78.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.48 installs=1464497 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.58 sendable=78.33 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=120805 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.57 sendable=77.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.01 installs=2003389 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.2 sendable=77.0 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.76 installs=215448 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=77.32 sendable=75.92 stage=QUALIFIED_CANDIDATE_ONLY quality=86.5 mvp=77.64 installs=80364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=77.64 sendable=75.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.46 installs=43682 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=84.6 sendable=74.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.14 installs=850443 unknown_app_share=0.3 unknown_installs_share=0.1983 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT hidden_object score=70.59 sendable=74.69 stage=COOLDOWN_BLOCKED quality=91.62 mvp=65.0 installs=43361 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.28 sendable=74.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.72 installs=2658813 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
