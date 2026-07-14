# Alert Funnel - 2026-07-14

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 123
- NEAR_MISS: 98
- REJECT: 199
- SINGLE_APP_WATCH: 7
- WATCH: 179

## Alert Stage Counts
- COOLDOWN_BLOCKED: 10
- NONE: 483
- QUALIFIED_CANDIDATE_ONLY: 112
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 10
- duplicate_market_signals_suppressed: 141
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Sendable Failure Distribution
- below_classification_confidence: 203
- below_data_quality_for_trend_confidence: 282
- below_data_quality_score: 282
- below_mvp_feasibility: 206
- below_opportunity_score: 487
- below_sendable_alert_score: 595
- below_team_fit_score: 392
- below_trend_confidence_score: 264
- blocked_risk_tag: 153
- complex_full_product: 288
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 10
- duplicate_market_signal: 141
- giant_developer_competition: 34
- giant_developer_penalty: 32
- giant_share_too_high: 27
- growth_by_one_app_too_high: 260
- high_mvp_complexity: 133
- high_production_complexity: 58
- leader_dominated_market: 251
- low_classification_confidence: 203
- low_developer_diversity: 141
- low_mvp_feasibility: 206
- low_total_daily_installs: 112
- low_total_daily_installs_for_trend_confidence: 112
- market_signal_duplicate: 14
- no_growth_history: 4
- not_alert_status: 483
- one_app_growth_penalty: 291
- organic_confidence_low: 232
- other_niche_low_confidence: 66
- severe_paid_spike_penalty: 148
- single_app_breakout_not_regular_alert: 141
- single_developer_dominance: 227
- single_developer_penalty: 266
- single_developer_share_too_high: 251
- too_few_apps_for_sendable: 223
- too_few_apps_for_trend_confidence: 223
- too_few_successful_new_apps: 141
- too_few_successful_new_apps_for_trend_confidence: 141
- too_few_unique_developers: 141
- top3_too_dominant: 367
- top_app_concentration_penalty: 291
- top_app_too_dominant: 291
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT coloring score=89.55 sendable=89.49 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1784778 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.77 sendable=83.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=47490 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT tile_match score=89.85 sendable=82.43 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1179238 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.37 sendable=82.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=540216 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.29 sendable=81.95 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=520492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT word_puzzle score=85.87 sendable=81.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=194584 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.41 sendable=80.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.38 installs=5836477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.74 sendable=80.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.2 installs=2675318 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.0 sendable=80.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.56 installs=1469337 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.83 sendable=80.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1264870 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.13 sendable=79.64 stage=QUALIFIED_CANDIDATE_ONLY quality=94.26 mvp=65.0 installs=62677 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.74 sendable=79.28 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.65 installs=147855 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.36 sendable=78.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.62 installs=151665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.32 sendable=77.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=134126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.32 sendable=77.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=23743 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=82.58 sendable=77.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=451463 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.15 sendable=76.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.53 installs=1712520 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=85.64 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.39 installs=2869592 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.7 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=86.43 mvp=85.0 installs=34247 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.36 sendable=76.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.14 installs=55918 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
