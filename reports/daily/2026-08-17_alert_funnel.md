# Alert Funnel - 2026-08-17

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 78
- NEAR_MISS: 127
- REJECT: 189
- SINGLE_APP_WATCH: 18
- WATCH: 176

## Alert Stage Counts
- COOLDOWN_BLOCKED: 51
- NONE: 510
- QUALIFIED_CANDIDATE_ONLY: 26
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 51
- duplicate_market_signals_suppressed: 99
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 297
- below_data_quality_score: 297
- below_mvp_feasibility: 192
- below_opportunity_score: 492
- below_sendable_alert_score: 586
- below_team_fit_score: 353
- below_trend_confidence_score: 365
- blocked_risk_tag: 101
- complex_full_product: 260
- cooldown_normalized_niche: 51
- duplicate_market_signal: 99
- giant_developer_competition: 33
- giant_developer_penalty: 31
- giant_share_too_high: 20
- growth_by_one_app_too_high: 279
- high_mvp_complexity: 123
- high_production_complexity: 62
- leader_dominated_market: 226
- low_classification_confidence: 177
- low_developer_diversity: 143
- low_mvp_feasibility: 192
- low_total_daily_installs: 138
- low_total_daily_installs_for_trend_confidence: 138
- market_signal_duplicate: 3
- no_growth_history: 1
- not_alert_status: 510
- one_app_growth_penalty: 304
- organic_confidence_low: 225
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 98
- single_app_breakout_not_regular_alert: 142
- single_developer_dominance: 205
- single_developer_penalty: 246
- single_developer_share_too_high: 228
- too_few_apps_for_sendable: 228
- too_few_apps_for_trend_confidence: 228
- too_few_successful_new_apps: 142
- too_few_successful_new_apps_for_trend_confidence: 142
- too_few_unique_developers: 143
- top3_too_dominant: 337
- top_app_concentration_penalty: 269
- top_app_too_dominant: 269
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT hidden_object score=86.16 sendable=80.37 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=162489 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.47 sendable=80.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1051107 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.02 sendable=79.3 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1288332 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.98 sendable=78.1 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.64 installs=203209 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.3 sendable=77.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.2 installs=147394 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.38 sendable=75.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=47503 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=84.02 sendable=74.56 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.4 installs=404103 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.87 sendable=74.31 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=79266 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.18 sendable=73.96 stage=COOLDOWN_BLOCKED quality=94.15 mvp=65.0 installs=40753 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=84.92 sendable=73.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=365930 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=73.92 sendable=73.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.2 installs=24185 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.99 sendable=72.82 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.09 installs=2406084 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.86 sendable=71.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.29 installs=81413 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.85 sendable=69.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.11 installs=454922 unknown_app_share=0.2447 unknown_installs_share=0.1533 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT runner score=84.07 sendable=69.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=1649286 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=83.84 sendable=69.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=64.01 installs=706792 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT block_puzzle score=86.98 sendable=68.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=65.65 installs=438718 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.07 sendable=68.48 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=36467 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=82.87 sendable=68.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.18 installs=259874 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=82.63 sendable=68.23 stage=COOLDOWN_BLOCKED quality=88.0 mvp=63.86 installs=340681 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
