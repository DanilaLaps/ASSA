# Alert Funnel - 2026-09-01

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 114
- NEAR_MISS: 104
- REJECT: 208
- SINGLE_APP_WATCH: 10
- WATCH: 149

## Alert Stage Counts
- COOLDOWN_BLOCKED: 11
- NONE: 471
- QUALIFIED_CANDIDATE_ONLY: 102
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 11
- duplicate_market_signals_suppressed: 113
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 71
- unknown_pattern_blocker_active: 71

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 285
- below_data_quality_score: 285
- below_mvp_feasibility: 188
- below_opportunity_score: 463
- below_sendable_alert_score: 573
- below_team_fit_score: 357
- below_trend_confidence_score: 298
- blocked_risk_tag: 163
- complex_full_product: 256
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 11
- duplicate_market_signal: 113
- giant_developer_competition: 25
- giant_developer_penalty: 24
- giant_share_too_high: 15
- growth_by_one_app_too_high: 285
- high_mvp_complexity: 129
- high_production_complexity: 62
- leader_dominated_market: 236
- low_classification_confidence: 185
- low_developer_diversity: 145
- low_mvp_feasibility: 188
- low_total_daily_installs: 132
- low_total_daily_installs_for_trend_confidence: 132
- market_signal_duplicate: 11
- not_alert_status: 471
- one_app_growth_penalty: 310
- organic_confidence_low: 236
- other_niche_low_confidence: 66
- severe_paid_spike_penalty: 163
- single_app_breakout_not_regular_alert: 145
- single_developer_dominance: 210
- single_developer_penalty: 263
- single_developer_share_too_high: 237
- too_few_apps_for_sendable: 231
- too_few_apps_for_trend_confidence: 231
- too_few_successful_new_apps: 145
- too_few_successful_new_apps_for_trend_confidence: 145
- too_few_unique_developers: 145
- top3_too_dominant: 346
- top_app_concentration_penalty: 282
- top_app_too_dominant: 282
- unknown_pattern_blocker_active: 70

## Top Qualified But Not Sent
- ALERT coloring score=90.16 sendable=84.35 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=798373 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=80.13 sendable=84.16 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=38133 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=78.09 sendable=83.66 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=17059 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.92 sendable=82.78 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=46003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.42 sendable=82.74 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=862488 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.88 sendable=80.71 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.34 installs=1461269 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.64 sendable=80.71 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=86813 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.9 sendable=80.56 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=296346 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.66 sendable=80.45 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.92 installs=1212876 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.89 sendable=80.39 stage=COOLDOWN_BLOCKED quality=94.47 mvp=65.0 installs=49153 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=84.14 sendable=80.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.0 installs=167238 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.98 sendable=79.65 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=153627 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=85.14 sendable=79.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=352773 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.11 sendable=78.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.66 installs=244672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.72 sendable=78.4 stage=QUALIFIED_CANDIDATE_ONLY quality=87.67 mvp=69.17 installs=310734 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=81.6 sendable=78.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=182017 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=80.62 sendable=78.33 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.03 installs=452535 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.09 sendable=78.1 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.85 installs=1577795 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=82.95 sendable=77.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.0 installs=185494 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.46 sendable=77.53 stage=QUALIFIED_CANDIDATE_ONLY quality=85.68 mvp=85.0 installs=33888 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
