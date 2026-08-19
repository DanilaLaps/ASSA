# Alert Funnel - 2026-08-19

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 84
- NEAR_MISS: 120
- REJECT: 198
- SINGLE_APP_WATCH: 20
- WATCH: 185

## Alert Stage Counts
- COOLDOWN_BLOCKED: 2
- NONE: 523
- QUALIFIED_CANDIDATE_ONLY: 81
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 2
- duplicate_market_signals_suppressed: 108
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Sendable Failure Distribution
- below_classification_confidence: 192
- below_data_quality_for_trend_confidence: 323
- below_data_quality_score: 323
- below_mvp_feasibility: 197
- below_opportunity_score: 501
- below_sendable_alert_score: 604
- below_team_fit_score: 361
- below_trend_confidence_score: 369
- blocked_risk_tag: 103
- complex_full_product: 267
- cooldown_normalized_niche: 2
- duplicate_market_signal: 108
- giant_developer_competition: 31
- giant_developer_penalty: 28
- giant_share_too_high: 23
- growth_by_one_app_too_high: 283
- high_mvp_complexity: 123
- high_production_complexity: 59
- leader_dominated_market: 240
- low_classification_confidence: 192
- low_developer_diversity: 155
- low_mvp_feasibility: 197
- low_total_daily_installs: 130
- low_total_daily_installs_for_trend_confidence: 130
- market_signal_duplicate: 3
- not_alert_status: 523
- one_app_growth_penalty: 309
- organic_confidence_low: 231
- other_niche_low_confidence: 62
- severe_paid_spike_penalty: 101
- single_app_breakout_not_regular_alert: 154
- single_developer_dominance: 219
- single_developer_penalty: 272
- single_developer_share_too_high: 242
- too_few_apps_for_sendable: 228
- too_few_apps_for_trend_confidence: 228
- too_few_successful_new_apps: 154
- too_few_successful_new_apps_for_trend_confidence: 154
- too_few_unique_developers: 155
- top3_too_dominant: 352
- top_app_concentration_penalty: 290
- top_app_too_dominant: 290
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=79.93 sendable=83.84 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=50081 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=86.23 sendable=80.4 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=242453 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=88.53 sendable=79.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.26 installs=2580798 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.54 sendable=78.19 stage=QUALIFIED_CANDIDATE_ONLY quality=94.08 mvp=65.0 installs=58310 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=77.13 sendable=77.04 stage=QUALIFIED_CANDIDATE_ONLY quality=94.56 mvp=85.0 installs=19457 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT coloring score=76.15 sendable=76.82 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=37002 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.14 sendable=75.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1074564 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.14 sendable=75.48 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=59556 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=80.01 sendable=75.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=186012 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.46 sendable=74.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1911939 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.18 sendable=74.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.74 installs=526817 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.45 sendable=74.06 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=117707 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=81.15 sendable=73.91 stage=QUALIFIED_CANDIDATE_ONLY quality=87.69 mvp=76.0 installs=131083 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=71.83 sendable=73.87 stage=QUALIFIED_CANDIDATE_ONLY quality=85.53 mvp=85.0 installs=6731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.64 sendable=73.72 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.83 installs=5067282 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.63 sendable=73.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.72 installs=328813 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=79.84 sendable=73.26 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.64 installs=94453 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.85 sendable=71.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.02 installs=1697822 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=79.97 sendable=71.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.2 installs=114691 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT block_puzzle score=86.93 sendable=70.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.62 installs=1607480 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
