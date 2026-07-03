# Alert Funnel - 2026-07-03

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 119
- NEAR_MISS: 107
- REJECT: 194
- SINGLE_APP_WATCH: 1
- WATCH: 169

## Alert Stage Counts
- COOLDOWN_BLOCKED: 7
- NONE: 471
- QUALIFIED_CANDIDATE_ONLY: 111
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 7
- duplicate_market_signals_suppressed: 122
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 70
- unknown_pattern_blocker_active: 70

## Sendable Failure Distribution
- below_classification_confidence: 187
- below_data_quality_for_trend_confidence: 248
- below_data_quality_score: 248
- below_mvp_feasibility: 199
- below_opportunity_score: 472
- below_sendable_alert_score: 582
- below_team_fit_score: 374
- below_trend_confidence_score: 244
- blocked_risk_tag: 152
- complex_full_product: 262
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 7
- duplicate_market_signal: 122
- giant_developer_competition: 36
- giant_developer_penalty: 34
- giant_share_too_high: 23
- growth_by_one_app_too_high: 248
- high_mvp_complexity: 118
- high_production_complexity: 57
- leader_dominated_market: 228
- low_classification_confidence: 187
- low_developer_diversity: 138
- low_mvp_feasibility: 199
- low_total_daily_installs: 98
- low_total_daily_installs_for_trend_confidence: 98
- market_signal_duplicate: 8
- no_growth_history: 2
- not_alert_status: 471
- one_app_growth_penalty: 281
- organic_confidence_low: 219
- other_niche_low_confidence: 62
- severe_paid_spike_penalty: 146
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 212
- single_developer_penalty: 254
- single_developer_share_too_high: 229
- too_few_apps_for_sendable: 214
- too_few_apps_for_trend_confidence: 214
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 138
- top3_too_dominant: 358
- top_app_concentration_penalty: 280
- top_app_too_dominant: 280
- unknown_pattern_blocker_active: 69

## Top Qualified But Not Sent
- ALERT coloring score=89.28 sendable=83.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1386266 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.82 sendable=82.64 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1432680 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.6 sendable=82.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=543242 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT hidden_object score=79.22 sendable=80.57 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=77506 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=84.35 sendable=80.43 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=346258 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.42 sendable=80.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=159183 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.84 sendable=80.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.92 installs=2639944 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.83 sendable=79.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.47 installs=6000271 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.44 sendable=79.82 stage=QUALIFIED_CANDIDATE_ONLY quality=87.66 mvp=82.92 installs=114920 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.29 sendable=79.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.52 installs=200500 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=79.92 sendable=78.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.62 installs=157332 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.36 sendable=77.93 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1514722 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=82.05 sendable=77.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.34 installs=182367 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.54 sendable=77.75 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.05 installs=122656 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.57 sendable=76.68 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.08 installs=1867689 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.26 sendable=76.66 stage=QUALIFIED_CANDIDATE_ONLY quality=92.02 mvp=65.0 installs=36446 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=78.51 sendable=76.59 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.38 installs=632721 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=80.23 sendable=76.56 stage=QUALIFIED_CANDIDATE_ONLY quality=86.95 mvp=80.5 installs=83535 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=75.67 sendable=75.93 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.27 installs=77370 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=78.34 sendable=75.71 stage=QUALIFIED_CANDIDATE_ONLY quality=87.56 mvp=60.56 installs=111535 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
