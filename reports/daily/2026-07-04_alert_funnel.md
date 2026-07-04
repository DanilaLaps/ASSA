# Alert Funnel - 2026-07-04

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 117
- NEAR_MISS: 106
- REJECT: 193
- SINGLE_APP_WATCH: 5
- WATCH: 155

## Alert Stage Counts
- COOLDOWN_BLOCKED: 35
- NONE: 459
- QUALIFIED_CANDIDATE_ONLY: 81
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 35
- duplicate_market_signals_suppressed: 108
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 180
- below_data_quality_for_trend_confidence: 265
- below_data_quality_score: 265
- below_mvp_feasibility: 194
- below_opportunity_score: 459
- below_sendable_alert_score: 569
- below_team_fit_score: 357
- below_trend_confidence_score: 250
- blocked_risk_tag: 148
- complex_full_product: 254
- cooldown_normalized_niche: 35
- duplicate_market_signal: 108
- giant_developer_competition: 32
- giant_developer_penalty: 25
- giant_share_too_high: 22
- growth_by_one_app_too_high: 263
- high_mvp_complexity: 115
- high_production_complexity: 57
- leader_dominated_market: 220
- low_classification_confidence: 180
- low_developer_diversity: 135
- low_mvp_feasibility: 194
- low_total_daily_installs: 122
- low_total_daily_installs_for_trend_confidence: 122
- market_signal_duplicate: 9
- not_alert_status: 459
- one_app_growth_penalty: 294
- organic_confidence_low: 225
- other_niche_low_confidence: 61
- severe_paid_spike_penalty: 145
- single_app_breakout_not_regular_alert: 134
- single_developer_dominance: 205
- single_developer_penalty: 241
- single_developer_share_too_high: 222
- too_few_apps_for_sendable: 208
- too_few_apps_for_trend_confidence: 208
- too_few_successful_new_apps: 134
- too_few_successful_new_apps_for_trend_confidence: 134
- too_few_unique_developers: 135
- top3_too_dominant: 342
- top_app_concentration_penalty: 269
- top_app_too_dominant: 269
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT coloring score=89.83 sendable=83.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1107300 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.9 sendable=83.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1141743 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.91 sendable=80.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=254753 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.78 sendable=80.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=297655 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.76 sendable=80.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.19 installs=1230672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.88 sendable=80.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.94 installs=1906170 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.76 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=103559 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.35 sendable=79.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.88 installs=1225587 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.96 sendable=79.31 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=271425 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=90.15 sendable=78.96 stage=COOLDOWN_BLOCKED quality=94.84 mvp=85.0 installs=567514 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=82.75 sendable=78.26 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.05 installs=138227 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=72.94 sendable=77.89 stage=COOLDOWN_BLOCKED quality=93.54 mvp=65.0 installs=21396 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.48 sendable=77.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1038738 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=77.22 sendable=77.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.88 installs=72173 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=75.74 sendable=77.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.79 installs=56915 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.44 sendable=76.54 stage=COOLDOWN_BLOCKED quality=86.27 mvp=85.0 installs=52865 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.48 sendable=76.39 stage=COOLDOWN_BLOCKED quality=94.53 mvp=65.0 installs=23935 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.2 sendable=76.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.95 installs=1331753 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=76.3 sendable=75.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.5 installs=28083 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.7 sendable=74.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.49 installs=907821 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
