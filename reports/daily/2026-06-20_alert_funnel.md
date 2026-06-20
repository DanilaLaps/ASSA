# Alert Funnel - 2026-06-20

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 72
- NEAR_MISS: 119
- REJECT: 184
- SINGLE_APP_WATCH: 20
- WATCH: 205

## Alert Stage Counts
- COOLDOWN_BLOCKED: 36
- NONE: 528
- QUALIFIED_CANDIDATE_ONLY: 35
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 36
- duplicate_market_signals_suppressed: 107
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 73
- unknown_pattern_blocker_active: 73

## Sendable Failure Distribution
- below_classification_confidence: 188
- below_data_quality_for_trend_confidence: 322
- below_data_quality_score: 322
- below_mvp_feasibility: 202
- below_opportunity_score: 508
- below_sendable_alert_score: 599
- below_team_fit_score: 380
- below_trend_confidence_score: 390
- blocked_risk_tag: 92
- complex_full_product: 280
- cooldown_exact_dedupe_key: 3
- cooldown_normalized_niche: 36
- duplicate_market_signal: 107
- giant_developer_competition: 35
- giant_developer_penalty: 29
- giant_share_too_high: 20
- growth_by_one_app_too_high: 306
- high_mvp_complexity: 132
- high_production_complexity: 57
- leader_dominated_market: 227
- low_classification_confidence: 188
- low_developer_diversity: 132
- low_mvp_feasibility: 202
- low_total_daily_installs: 129
- low_total_daily_installs_for_trend_confidence: 129
- market_signal_duplicate: 3
- no_growth_history: 1
- not_alert_status: 528
- one_app_growth_penalty: 326
- organic_confidence_low: 215
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 86
- single_app_breakout_not_regular_alert: 132
- single_developer_dominance: 200
- single_developer_penalty: 250
- single_developer_share_too_high: 227
- too_few_apps_for_sendable: 217
- too_few_apps_for_trend_confidence: 217
- too_few_successful_new_apps: 132
- too_few_successful_new_apps_for_trend_confidence: 132
- too_few_unique_developers: 132
- top3_too_dominant: 353
- top_app_concentration_penalty: 268
- top_app_too_dominant: 268
- unknown_pattern_blocker_active: 73

## Top Qualified But Not Sent
- ALERT sort_puzzle score=84.75 sendable=82.33 stage=COOLDOWN_BLOCKED quality=94.66 mvp=85.0 installs=63739 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=72.38 sendable=79.23 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=14847 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=83.97 sendable=78.95 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.5 installs=103825 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=82.81 sendable=78.71 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.35 installs=770246 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.43 sendable=78.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=174721 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.84 sendable=77.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.37 installs=3988846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.7 sendable=77.32 stage=COOLDOWN_BLOCKED quality=92.84 mvp=85.0 installs=33499 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=83.87 sendable=76.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.76 installs=101187 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.41 sendable=76.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.48 installs=1992010 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.83 sendable=74.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.53 installs=961293 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=86.39 sendable=74.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1081332 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.14 sendable=74.16 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.08 installs=1720734 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.68 sendable=73.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=659631 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=85.53 sendable=73.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.9 installs=1051460 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=84.98 sendable=73.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.57 installs=969728 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.36 sendable=71.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=137500 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.93 sendable=71.12 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=266140 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT merge score=72.17 sendable=71.06 stage=QUALIFIED_CANDIDATE_ONLY quality=87.53 mvp=64.0 installs=18908 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.68 sendable=71.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.5 installs=1230624 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=84.49 sendable=69.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2460231 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
