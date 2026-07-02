# Alert Funnel - 2026-07-02

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 116
- NEAR_MISS: 109
- REJECT: 202
- WATCH: 160

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 471
- QUALIFIED_CANDIDATE_ONLY: 107
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 8
- duplicate_market_signals_suppressed: 125
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 184
- below_data_quality_for_trend_confidence: 250
- below_data_quality_score: 250
- below_mvp_feasibility: 199
- below_opportunity_score: 469
- below_sendable_alert_score: 577
- below_team_fit_score: 371
- below_trend_confidence_score: 242
- blocked_risk_tag: 164
- complex_full_product: 258
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 8
- duplicate_market_signal: 125
- giant_developer_competition: 39
- giant_developer_penalty: 36
- giant_share_too_high: 30
- growth_by_one_app_too_high: 254
- high_mvp_complexity: 117
- high_production_complexity: 57
- leader_dominated_market: 232
- low_classification_confidence: 184
- low_developer_diversity: 141
- low_mvp_feasibility: 199
- low_total_daily_installs: 91
- low_total_daily_installs_for_trend_confidence: 91
- market_signal_duplicate: 11
- no_growth_history: 2
- not_alert_status: 471
- one_app_growth_penalty: 284
- organic_confidence_low: 226
- other_niche_low_confidence: 62
- severe_paid_spike_penalty: 161
- single_app_breakout_not_regular_alert: 140
- single_developer_dominance: 217
- single_developer_penalty: 255
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 219
- too_few_apps_for_trend_confidence: 219
- too_few_successful_new_apps: 140
- too_few_successful_new_apps_for_trend_confidence: 140
- too_few_unique_developers: 141
- top3_too_dominant: 360
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT coloring score=88.95 sendable=83.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1348947 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.98 sendable=82.96 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1547153 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=73.78 sendable=81.73 stage=QUALIFIED_CANDIDATE_ONLY quality=94.49 mvp=85.0 installs=24253 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage
- ALERT tile_match score=87.9 sendable=80.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.91 installs=2718085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.25 sendable=80.37 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=343324 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.28 sendable=80.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=140900 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.65 sendable=80.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.26 installs=1719084 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.17 sendable=80.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.46 installs=1595446 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.85 sendable=80.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.51 installs=6199168 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.64 sendable=79.92 stage=QUALIFIED_CANDIDATE_ONLY quality=87.83 mvp=82.75 installs=117311 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.51 sendable=79.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.53 installs=198094 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=80.26 sendable=78.23 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.26 installs=162573 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=79.03 sendable=77.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.05 installs=129143 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.18 sendable=77.85 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1507469 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=82.66 sendable=77.24 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.47 installs=196802 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.7 sendable=76.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.19 installs=661732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.85 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.57 installs=1827586 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=75.24 sendable=76.8 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.79 installs=76305 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.14 sendable=76.61 stage=QUALIFIED_CANDIDATE_ONLY quality=92.02 mvp=65.0 installs=36446 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=80.05 sendable=76.07 stage=QUALIFIED_CANDIDATE_ONLY quality=85.46 mvp=85.0 installs=69661 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
