# Alert Funnel - 2026-06-23

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 82
- NEAR_MISS: 106
- REJECT: 175
- SINGLE_APP_WATCH: 24
- WATCH: 190

## Alert Stage Counts
- COOLDOWN_BLOCKED: 37
- NONE: 495
- QUALIFIED_CANDIDATE_ONLY: 44
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 37
- duplicate_market_signals_suppressed: 107
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 307
- below_data_quality_score: 307
- below_mvp_feasibility: 199
- below_opportunity_score: 491
- below_sendable_alert_score: 577
- below_team_fit_score: 370
- below_trend_confidence_score: 387
- blocked_risk_tag: 73
- complex_full_product: 276
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 37
- duplicate_market_signal: 107
- giant_developer_competition: 27
- giant_developer_penalty: 20
- giant_share_too_high: 15
- growth_by_one_app_too_high: 275
- high_mvp_complexity: 129
- high_production_complexity: 56
- leader_dominated_market: 210
- low_classification_confidence: 177
- low_developer_diversity: 134
- low_mvp_feasibility: 199
- low_total_daily_installs: 136
- low_total_daily_installs_for_trend_confidence: 136
- market_signal_duplicate: 7
- not_alert_status: 495
- one_app_growth_penalty: 303
- organic_confidence_low: 212
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 70
- single_app_breakout_not_regular_alert: 134
- single_developer_dominance: 189
- single_developer_penalty: 225
- single_developer_share_too_high: 210
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 134
- too_few_successful_new_apps_for_trend_confidence: 134
- too_few_unique_developers: 134
- top3_too_dominant: 332
- top_app_concentration_penalty: 240
- top_app_too_dominant: 240
- unknown_pattern_blocker_active: 75

## Top Qualified But Not Sent
- ALERT block_puzzle score=88.01 sendable=78.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.46 installs=1108868 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=88.16 sendable=77.2 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=513807 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.47 sendable=77.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=80.03 installs=670977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.11 sendable=76.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.53 installs=116144 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.87 sendable=76.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.59 installs=1275295 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=83.93 sendable=75.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=75350 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=78.97 sendable=75.21 stage=COOLDOWN_BLOCKED quality=87.62 mvp=77.64 installs=23912 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.32 sendable=73.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=188775 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.68 sendable=73.05 stage=QUALIFIED_CANDIDATE_ONLY quality=91.7 mvp=65.0 installs=116935 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=85.64 sendable=72.42 stage=QUALIFIED_CANDIDATE_ONLY quality=94.55 mvp=65.0 installs=155905 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=80.2 sendable=71.9 stage=COOLDOWN_BLOCKED quality=86.79 mvp=85.0 installs=21804 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=85.46 sendable=70.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.62 installs=1019508 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.38 sendable=69.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=156352 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.48 sendable=69.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.75 installs=39733 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.75 sendable=69.33 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=1595839 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=83.58 sendable=69.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.1 installs=143210 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=83.76 sendable=68.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.82 installs=608752 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT other score=82.88 sendable=68.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=62.72 installs=570169 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT idle_tycoon score=81.36 sendable=67.91 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.65 installs=130845 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sandbox score=80.78 sendable=67.82 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.84 installs=286539 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
