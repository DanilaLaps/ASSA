# Alert Funnel - 2026-06-27

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 95
- NEAR_MISS: 72
- REJECT: 179
- SINGLE_APP_WATCH: 14
- WATCH: 148

## Alert Stage Counts
- COOLDOWN_BLOCKED: 29
- NONE: 413
- QUALIFIED_CANDIDATE_ONLY: 65
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 29
- duplicate_market_signals_suppressed: 132
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 168
- below_data_quality_for_trend_confidence: 238
- below_data_quality_score: 238
- below_mvp_feasibility: 185
- below_opportunity_score: 406
- below_sendable_alert_score: 506
- below_team_fit_score: 326
- below_trend_confidence_score: 297
- blocked_risk_tag: 64
- complex_full_product: 248
- cooldown_normalized_niche: 29
- duplicate_market_signal: 132
- giant_developer_competition: 24
- giant_developer_penalty: 23
- giant_share_too_high: 14
- growth_by_one_app_too_high: 145
- high_mvp_complexity: 116
- high_production_complexity: 66
- leader_dominated_market: 203
- low_classification_confidence: 168
- low_developer_diversity: 133
- low_mvp_feasibility: 185
- low_total_daily_installs: 167
- low_total_daily_installs_for_trend_confidence: 167
- market_signal_duplicate: 10
- no_growth_history: 1
- not_alert_status: 413
- one_app_growth_penalty: 157
- organic_confidence_low: 190
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 62
- single_app_breakout_not_regular_alert: 133
- single_developer_dominance: 186
- single_developer_penalty: 224
- single_developer_share_too_high: 204
- too_few_apps_for_sendable: 215
- too_few_apps_for_trend_confidence: 215
- too_few_successful_new_apps: 133
- too_few_successful_new_apps_for_trend_confidence: 133
- too_few_unique_developers: 133
- top3_too_dominant: 315
- top_app_concentration_penalty: 242
- top_app_too_dominant: 242
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT sort_puzzle score=89.28 sendable=86.39 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=125442 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.98 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=204081 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.31 sendable=79.39 stage=COOLDOWN_BLOCKED quality=94.77 mvp=85.0 installs=8586 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=89.08 sendable=79.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.11 installs=650958 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.56 sendable=78.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=506535 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.81 sendable=78.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=54651 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.54 sendable=78.1 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=29981 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=82.02 sendable=77.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=27712 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.14 sendable=76.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=94168 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=81.66 sendable=75.81 stage=COOLDOWN_BLOCKED quality=86.68 mvp=74.5 installs=28793 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.21 sendable=75.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=240550 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=77.9 sendable=74.68 stage=COOLDOWN_BLOCKED quality=87.59 mvp=76.9 installs=10282 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=90.13 sendable=74.41 stage=COOLDOWN_BLOCKED quality=86.5 mvp=85.0 installs=507748 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.54 sendable=73.7 stage=COOLDOWN_BLOCKED quality=86.25 mvp=79.46 installs=494668 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.37 sendable=72.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.13 installs=41012 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT merge score=80.67 sendable=72.5 stage=QUALIFIED_CANDIDATE_ONLY quality=87.18 mvp=73.0 installs=20000 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.74 sendable=71.56 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=82683 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=82.92 sendable=71.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.15 installs=143057 unknown_app_share=0.2683 unknown_installs_share=0.2457 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT block_puzzle score=74.75 sendable=71.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.57 installs=16931 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=78.43 sendable=70.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.92 installs=13852 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
