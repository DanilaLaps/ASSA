# Alert Funnel - 2026-06-28

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 66
- NEAR_MISS: 84
- REJECT: 149
- SINGLE_APP_WATCH: 18
- WATCH: 128

## Alert Stage Counts
- COOLDOWN_BLOCKED: 38
- NONE: 379
- QUALIFIED_CANDIDATE_ONLY: 27
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 38
- duplicate_market_signals_suppressed: 107
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 68
- unknown_dominant_cluster: 64
- unknown_pattern_blocker_active: 64

## Sendable Failure Distribution
- below_classification_confidence: 155
- below_data_quality_for_trend_confidence: 224
- below_data_quality_score: 224
- below_mvp_feasibility: 163
- below_opportunity_score: 372
- below_sendable_alert_score: 445
- below_team_fit_score: 298
- below_trend_confidence_score: 277
- blocked_risk_tag: 61
- complex_full_product: 223
- cooldown_normalized_niche: 38
- duplicate_market_signal: 107
- giant_developer_competition: 21
- giant_developer_penalty: 21
- giant_share_too_high: 14
- growth_by_one_app_too_high: 150
- high_mvp_complexity: 103
- high_production_complexity: 58
- leader_dominated_market: 192
- low_classification_confidence: 155
- low_developer_diversity: 130
- low_mvp_feasibility: 163
- low_total_daily_installs: 149
- low_total_daily_installs_for_trend_confidence: 149
- market_signal_duplicate: 4
- no_growth_history: 1
- not_alert_status: 379
- one_app_growth_penalty: 171
- organic_confidence_low: 184
- other_niche_low_confidence: 56
- severe_paid_spike_penalty: 58
- single_app_breakout_not_regular_alert: 130
- single_developer_dominance: 182
- single_developer_penalty: 207
- single_developer_share_too_high: 192
- too_few_apps_for_sendable: 197
- too_few_apps_for_trend_confidence: 197
- too_few_successful_new_apps: 130
- too_few_successful_new_apps_for_trend_confidence: 130
- too_few_unique_developers: 130
- top3_too_dominant: 280
- top_app_concentration_penalty: 219
- top_app_too_dominant: 219
- unknown_pattern_blocker_active: 62

## Top Qualified But Not Sent
- ALERT sort_puzzle score=82.16 sendable=79.69 stage=COOLDOWN_BLOCKED quality=90.77 mvp=85.0 installs=17346 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=87.85 sendable=78.62 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.29 installs=431943 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.2 sendable=77.57 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=30341 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT coloring score=83.66 sendable=76.14 stage=COOLDOWN_BLOCKED quality=87.88 mvp=68.77 installs=45356 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.61 sendable=76.07 stage=COOLDOWN_BLOCKED quality=86.06 mvp=85.0 installs=726670 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=87.0 sendable=75.11 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=182113 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.78 sendable=73.54 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=150223 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.12 sendable=72.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.8 installs=394397 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=78.92 sendable=71.65 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.71 installs=9646 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.52 sendable=71.53 stage=COOLDOWN_BLOCKED quality=88.0 mvp=83.58 installs=27007 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.0 sendable=71.15 stage=COOLDOWN_BLOCKED quality=90.05 mvp=85.0 installs=16390 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=86.63 sendable=71.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.03 installs=291895 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT tile_match score=86.97 sendable=70.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=252083 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=82.31 sendable=69.95 stage=COOLDOWN_BLOCKED quality=86.53 mvp=63.3 installs=66116 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=84.74 sendable=69.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=408661 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=74.61 sendable=69.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.46 installs=14222 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=74.96 sendable=68.42 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=8948 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT runner score=82.25 sendable=68.34 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.16 installs=161583 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=83.31 sendable=68.24 stage=COOLDOWN_BLOCKED quality=84.13 mvp=64.35 installs=608916 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT mahjong score=76.17 sendable=67.9 stage=QUALIFIED_CANDIDATE_ONLY quality=84.0 mvp=85.0 installs=84364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_revenue_signal
