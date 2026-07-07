# Alert Funnel - 2026-07-07

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 92
- NEAR_MISS: 101
- REJECT: 185
- SINGLE_APP_WATCH: 14
- WATCH: 143

## Alert Stage Counts
- COOLDOWN_BLOCKED: 42
- NONE: 443
- QUALIFIED_CANDIDATE_ONLY: 49
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 42
- duplicate_market_signals_suppressed: 129
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 70
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 176
- below_data_quality_for_trend_confidence: 260
- below_data_quality_score: 260
- below_mvp_feasibility: 182
- below_opportunity_score: 436
- below_sendable_alert_score: 533
- below_team_fit_score: 322
- below_trend_confidence_score: 303
- blocked_risk_tag: 93
- complex_full_product: 234
- cooldown_normalized_niche: 42
- duplicate_market_signal: 129
- giant_developer_competition: 30
- giant_developer_penalty: 28
- giant_share_too_high: 20
- growth_by_one_app_too_high: 211
- high_mvp_complexity: 112
- high_production_complexity: 59
- leader_dominated_market: 185
- low_classification_confidence: 176
- low_developer_diversity: 131
- low_mvp_feasibility: 182
- low_total_daily_installs: 174
- low_total_daily_installs_for_trend_confidence: 174
- market_signal_duplicate: 5
- not_alert_status: 443
- one_app_growth_penalty: 234
- organic_confidence_low: 193
- other_niche_low_confidence: 59
- severe_paid_spike_penalty: 90
- single_app_breakout_not_regular_alert: 131
- single_developer_dominance: 174
- single_developer_penalty: 204
- single_developer_share_too_high: 187
- too_few_apps_for_sendable: 205
- too_few_apps_for_trend_confidence: 205
- too_few_successful_new_apps: 131
- too_few_successful_new_apps_for_trend_confidence: 131
- too_few_unique_developers: 131
- top3_too_dominant: 295
- top_app_concentration_penalty: 231
- top_app_too_dominant: 231
- unknown_pattern_blocker_active: 65

## Top Qualified But Not Sent
- ALERT sort_puzzle score=88.97 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=164066 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.77 sendable=80.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=260456 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.18 sendable=79.81 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=253609 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.47 sendable=79.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=91271 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.89 sendable=77.23 stage=COOLDOWN_BLOCKED quality=93.89 mvp=85.0 installs=19086 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=77.69 sendable=76.98 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=11871 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sandbox score=82.76 sendable=76.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.88 installs=49837 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.35 sendable=75.82 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=403445 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=78.95 sendable=75.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.69 installs=18379 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.82 sendable=74.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.74 installs=498893 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=72.47 sendable=74.32 stage=COOLDOWN_BLOCKED quality=91.0 mvp=85.0 installs=23336 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT arrow_puzzle score=79.01 sendable=73.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.03 installs=58442 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=83.34 sendable=73.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=38738 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.6 sendable=73.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.78 installs=316784 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.57 sendable=73.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=350047 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=75.31 sendable=73.45 stage=QUALIFIED_CANDIDATE_ONLY quality=86.9 mvp=75.82 installs=21046 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.45 sendable=73.13 stage=COOLDOWN_BLOCKED quality=94.91 mvp=65.0 installs=71379 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT coloring score=75.23 sendable=72.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.46 installs=18405 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.62 sendable=72.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.84 installs=580393 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=85.95 sendable=72.57 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=382141 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
