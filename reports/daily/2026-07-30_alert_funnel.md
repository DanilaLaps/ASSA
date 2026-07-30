# Alert Funnel - 2026-07-30

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 111
- NEAR_MISS: 105
- REJECT: 209
- SINGLE_APP_WATCH: 6
- WATCH: 168

## Alert Stage Counts
- COOLDOWN_BLOCKED: 62
- NONE: 488
- QUALIFIED_CANDIDATE_ONLY: 48
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 62
- duplicate_market_signals_suppressed: 124
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 192
- below_data_quality_for_trend_confidence: 310
- below_data_quality_score: 310
- below_mvp_feasibility: 202
- below_opportunity_score: 479
- below_sendable_alert_score: 593
- below_team_fit_score: 363
- below_trend_confidence_score: 331
- blocked_risk_tag: 124
- complex_full_product: 274
- cooldown_normalized_niche: 62
- duplicate_market_signal: 124
- giant_developer_competition: 24
- giant_developer_penalty: 23
- giant_share_too_high: 16
- growth_by_one_app_too_high: 279
- high_mvp_complexity: 132
- high_production_complexity: 59
- leader_dominated_market: 224
- low_classification_confidence: 192
- low_developer_diversity: 129
- low_mvp_feasibility: 202
- low_total_daily_installs: 132
- low_total_daily_installs_for_trend_confidence: 132
- market_signal_duplicate: 11
- no_growth_history: 1
- not_alert_status: 488
- one_app_growth_penalty: 307
- organic_confidence_low: 227
- other_niche_low_confidence: 64
- severe_paid_spike_penalty: 120
- single_app_breakout_not_regular_alert: 129
- single_developer_dominance: 204
- single_developer_penalty: 248
- single_developer_share_too_high: 224
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 129
- too_few_successful_new_apps_for_trend_confidence: 129
- too_few_unique_developers: 129
- top3_too_dominant: 342
- top_app_concentration_penalty: 275
- top_app_too_dominant: 275
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT sort_puzzle score=83.12 sendable=84.83 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=56416 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.31 sendable=81.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=390149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.86 sendable=80.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=454108 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=90.17 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1172626 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.75 sendable=80.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.88 installs=944726 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.46 sendable=80.08 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=207623 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=85.28 sendable=79.97 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=61386 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.34 sendable=79.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=48672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.48 sendable=79.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=185433 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=80.39 sendable=79.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=208197 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=74.37 sendable=78.63 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=14134 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=81.71 sendable=78.58 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=99416 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.89 sendable=78.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.63 installs=1169092 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.63 sendable=78.13 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.74 installs=3051412 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.41 sendable=78.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=601551 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.33 sendable=77.8 stage=COOLDOWN_BLOCKED quality=87.34 mvp=85.0 installs=75193 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.38 sendable=77.76 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=39109 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=84.49 sendable=76.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.91 installs=391652 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.44 sendable=75.91 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=22741 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=88.73 sendable=75.53 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=923726 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
