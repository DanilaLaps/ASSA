# Alert Funnel - 2026-06-08

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 59
- NEAR_MISS: 133
- REJECT: 187
- SINGLE_APP_WATCH: 22
- WATCH: 201

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 543
- QUALIFIED_CANDIDATE_ONLY: 57
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 112
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 73
- unknown_pattern_blocker_active: 73

## Sendable Failure Distribution
- below_classification_confidence: 189
- below_data_quality_for_trend_confidence: 430
- below_data_quality_score: 430
- below_mvp_feasibility: 208
- below_opportunity_score: 546
- below_sendable_alert_score: 601
- below_team_fit_score: 380
- below_trend_confidence_score: 480
- blocked_risk_tag: 120
- complex_full_product: 287
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 1
- duplicate_market_signal: 112
- giant_developer_competition: 32
- giant_developer_penalty: 27
- giant_share_too_high: 15
- growth_by_one_app_too_high: 329
- high_mvp_complexity: 138
- high_production_complexity: 59
- leader_dominated_market: 219
- low_classification_confidence: 189
- low_developer_diversity: 138
- low_mvp_feasibility: 208
- low_total_daily_installs: 112
- low_total_daily_installs_for_trend_confidence: 112
- market_signal_duplicate: 1
- no_growth_history: 4
- not_alert_status: 543
- one_app_growth_penalty: 348
- organic_confidence_low: 207
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 80
- single_app_breakout_not_regular_alert: 137
- single_developer_dominance: 195
- single_developer_penalty: 240
- single_developer_share_too_high: 223
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 137
- too_few_successful_new_apps_for_trend_confidence: 137
- too_few_unique_developers: 138
- top3_too_dominant: 343
- top_app_concentration_penalty: 261
- top_app_too_dominant: 261
- unknown_pattern_blocker_active: 72

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.04 sendable=82.22 stage=COOLDOWN_BLOCKED quality=90.0 mvp=85.0 installs=67728 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.29 sendable=74.51 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=883644 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.41 sendable=73.72 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.04 installs=77092 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT match_3 score=78.51 sendable=72.24 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=71.94 installs=993817 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=79.23 sendable=70.97 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=74.2 installs=123273 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.41 sendable=70.52 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.07 installs=54913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.69 sendable=69.86 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.43 installs=47991 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.34 sendable=69.34 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=77.89 installs=41359 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=78.34 sendable=68.67 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=76.17 installs=543370 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal, weak_rating_signal
- ALERT block_puzzle score=77.91 sendable=68.08 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.29 installs=966025 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=76.82 sendable=68.02 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=65.0 installs=200775 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=78.94 sendable=67.81 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=245707 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.46 sendable=67.74 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=800964 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=78.17 sendable=67.22 stage=QUALIFIED_CANDIDATE_ONLY quality=75.0 mvp=85.0 installs=92761 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT runner score=74.61 sendable=66.63 stage=QUALIFIED_CANDIDATE_ONLY quality=80.57 mvp=65.0 installs=29475 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.39 sendable=66.6 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=71.92 installs=74577 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.96 sendable=66.29 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=75.73 installs=2417653 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=72.41 sendable=65.39 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.0 installs=11146 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT idle_tycoon score=78.3 sendable=64.52 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.69 installs=155619 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=78.75 sendable=64.28 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=70.34 installs=1160075 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
