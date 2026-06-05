# Alert Funnel - 2026-06-05

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 93
- NEAR_MISS: 128
- REJECT: 215
- SINGLE_APP_WATCH: 13
- WATCH: 171

## Alert Stage Counts
- NONE: 527
- QUALIFIED_CANDIDATE_ONLY: 93

## Blocked Counts
- cooldown_blocked: 0
- duplicate_market_signals_suppressed: 119
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 81
- unknown_dominant_cluster: 77
- unknown_pattern_blocker_active: 77

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 414
- below_data_quality_score: 414
- below_mvp_feasibility: 200
- below_opportunity_score: 543
- below_sendable_alert_score: 620
- below_team_fit_score: 377
- below_trend_confidence_score: 463
- blocked_risk_tag: 158
- complex_full_product: 279
- duplicate_market_signal: 119
- giant_developer_competition: 31
- giant_developer_penalty: 30
- giant_share_too_high: 19
- growth_by_one_app_too_high: 361
- high_mvp_complexity: 134
- high_production_complexity: 56
- leader_dominated_market: 229
- low_classification_confidence: 193
- low_developer_diversity: 139
- low_mvp_feasibility: 200
- low_total_daily_installs: 128
- low_total_daily_installs_for_trend_confidence: 128
- market_signal_duplicate: 3
- no_growth_history: 10
- not_alert_status: 527
- one_app_growth_penalty: 406
- organic_confidence_low: 221
- other_niche_low_confidence: 71
- severe_paid_spike_penalty: 124
- single_app_breakout_not_regular_alert: 139
- single_developer_dominance: 205
- single_developer_penalty: 246
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 212
- too_few_apps_for_trend_confidence: 212
- too_few_successful_new_apps: 139
- too_few_successful_new_apps_for_trend_confidence: 139
- too_few_unique_developers: 139
- top3_too_dominant: 361
- top_app_concentration_penalty: 275
- top_app_too_dominant: 275
- unknown_pattern_blocker_active: 76

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.43 sendable=77.18 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=85.0 installs=74010 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT coloring score=80.88 sendable=72.59 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=683511 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=74.92 sendable=72.36 stage=QUALIFIED_CANDIDATE_ONLY quality=81.92 mvp=80.5 installs=36348 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.98 sendable=72.22 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=337284 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.57 sendable=70.72 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.11 installs=84881 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.4 sendable=70.08 stage=QUALIFIED_CANDIDATE_ONLY quality=82.23 mvp=85.0 installs=2756067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.88 sendable=69.98 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=849218 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=80.9 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=184977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.53 sendable=68.68 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.9 installs=71786 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=77.17 sendable=68.61 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=73.95 installs=54524 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.68 sendable=68.41 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=82.92 installs=80105 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.24 sendable=67.75 stage=QUALIFIED_CANDIDATE_ONLY quality=82.86 mvp=75.9 installs=2969320 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.04 sendable=66.6 stage=QUALIFIED_CANDIDATE_ONLY quality=82.72 mvp=85.0 installs=15646 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=78.87 sendable=66.29 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=69.59 installs=167758 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=78.81 sendable=66.03 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=309033 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=78.65 sendable=66.02 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=70.12 installs=1372837 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=70.74 sendable=65.92 stage=QUALIFIED_CANDIDATE_ONLY quality=84.93 mvp=65.0 installs=29477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
- ALERT block_puzzle score=80.38 sendable=65.83 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=1302444 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal, weak_rating_signal
- ALERT match_3 score=78.38 sendable=65.72 stage=QUALIFIED_CANDIDATE_ONLY quality=80.69 mvp=68.29 installs=69263 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT merge score=70.81 sendable=65.72 stage=QUALIFIED_CANDIDATE_ONLY quality=82.38 mvp=69.0 installs=5417 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
