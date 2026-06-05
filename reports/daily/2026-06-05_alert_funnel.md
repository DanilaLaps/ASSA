# Alert Funnel - 2026-06-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 95
- NEAR_MISS: 131
- REJECT: 215
- SINGLE_APP_WATCH: 12
- WATCH: 167

## Alert Stage Counts
- NONE: 525
- QUALIFIED_CANDIDATE_ONLY: 94
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 121
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 81
- unknown_dominant_cluster: 77
- unknown_pattern_blocker_active: 77

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 405
- below_data_quality_score: 405
- below_mvp_feasibility: 200
- below_opportunity_score: 539
- below_sendable_alert_score: 620
- below_team_fit_score: 375
- below_trend_confidence_score: 458
- blocked_risk_tag: 160
- complex_full_product: 279
- duplicate_market_signal: 121
- giant_developer_competition: 30
- giant_developer_penalty: 30
- giant_share_too_high: 19
- growth_by_one_app_too_high: 355
- high_mvp_complexity: 134
- high_production_complexity: 56
- leader_dominated_market: 227
- low_classification_confidence: 193
- low_developer_diversity: 138
- low_mvp_feasibility: 200
- low_total_daily_installs: 127
- low_total_daily_installs_for_trend_confidence: 127
- market_signal_duplicate: 3
- no_growth_history: 10
- not_alert_status: 525
- one_app_growth_penalty: 399
- organic_confidence_low: 220
- other_niche_low_confidence: 71
- severe_paid_spike_penalty: 126
- single_app_breakout_not_regular_alert: 138
- single_developer_dominance: 204
- single_developer_penalty: 243
- single_developer_share_too_high: 229
- too_few_apps_for_sendable: 211
- too_few_apps_for_trend_confidence: 211
- too_few_successful_new_apps: 138
- too_few_successful_new_apps_for_trend_confidence: 138
- too_few_unique_developers: 138
- top3_too_dominant: 361
- top_app_concentration_penalty: 274
- top_app_too_dominant: 274
- unknown_pattern_blocker_active: 76

## Top Qualified But Not Sent
- ALERT coloring score=80.92 sendable=72.59 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=682368 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.98 sendable=72.22 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=337284 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=74.86 sendable=72.15 stage=QUALIFIED_CANDIDATE_ONLY quality=81.76 mvp=80.5 installs=35717 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.57 sendable=70.72 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.11 installs=84881 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.4 sendable=70.07 stage=QUALIFIED_CANDIDATE_ONLY quality=82.22 mvp=85.0 installs=2753754 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.92 sendable=69.99 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=847821 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=80.9 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=184923 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.53 sendable=68.68 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.9 installs=71786 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=77.17 sendable=68.68 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.95 installs=54937 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.68 sendable=68.41 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=82.92 installs=80105 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.24 sendable=67.75 stage=QUALIFIED_CANDIDATE_ONLY quality=82.86 mvp=75.9 installs=2968117 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.04 sendable=66.6 stage=QUALIFIED_CANDIDATE_ONLY quality=82.72 mvp=85.0 installs=15646 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=78.87 sendable=66.29 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=69.59 installs=167846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=78.8 sendable=66.03 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=308925 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=78.65 sendable=66.0 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=70.12 installs=1371189 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=70.74 sendable=65.92 stage=QUALIFIED_CANDIDATE_ONLY quality=84.93 mvp=65.0 installs=29477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
- ALERT block_puzzle score=80.37 sendable=65.8 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=1298854 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal, weak_rating_signal
- ALERT match_3 score=78.38 sendable=65.72 stage=QUALIFIED_CANDIDATE_ONLY quality=80.69 mvp=68.29 installs=69263 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT merge score=70.81 sendable=65.72 stage=QUALIFIED_CANDIDATE_ONLY quality=82.38 mvp=69.0 installs=5417 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=78.86 sendable=65.17 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.0 installs=76547 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
