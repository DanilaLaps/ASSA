# Alert Funnel - 2026-06-18

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 70
- NEAR_MISS: 76
- REJECT: 192
- SINGLE_APP_WATCH: 18
- WATCH: 235

## Alert Stage Counts
- COOLDOWN_BLOCKED: 13
- NONE: 521
- QUALIFIED_CANDIDATE_ONLY: 56
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 13
- duplicate_market_signals_suppressed: 98
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 74
- unknown_pattern_blocker_active: 74

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 293
- below_data_quality_score: 293
- below_mvp_feasibility: 199
- below_opportunity_score: 550
- below_sendable_alert_score: 590
- below_team_fit_score: 375
- below_trend_confidence_score: 333
- blocked_risk_tag: 112
- complex_full_product: 279
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 13
- duplicate_market_signal: 98
- giant_developer_competition: 35
- giant_developer_penalty: 33
- giant_share_too_high: 16
- growth_by_one_app_too_high: 282
- high_mvp_complexity: 131
- high_production_complexity: 54
- leader_dominated_market: 214
- low_classification_confidence: 193
- low_developer_diversity: 120
- low_mvp_feasibility: 199
- low_total_daily_installs: 118
- low_total_daily_installs_for_trend_confidence: 118
- market_signal_duplicate: 4
- no_growth_history: 2
- not_alert_status: 521
- one_app_growth_penalty: 310
- organic_confidence_low: 220
- other_niche_low_confidence: 68
- severe_paid_spike_penalty: 108
- single_app_breakout_not_regular_alert: 120
- single_developer_dominance: 191
- single_developer_penalty: 237
- single_developer_share_too_high: 215
- too_few_apps_for_sendable: 209
- too_few_apps_for_trend_confidence: 209
- too_few_successful_new_apps: 120
- too_few_successful_new_apps_for_trend_confidence: 120
- too_few_unique_developers: 120
- top3_too_dominant: 339
- top_app_concentration_penalty: 261
- top_app_too_dominant: 261
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT sort_puzzle score=75.39 sendable=80.71 stage=COOLDOWN_BLOCKED quality=93.96 mvp=85.0 installs=67477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.36 sendable=79.76 stage=COOLDOWN_BLOCKED quality=92.63 mvp=85.0 installs=29902 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=73.77 sendable=75.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.0 installs=89331 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.27 sendable=74.96 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=283404 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.83 sendable=74.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=172272 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.36 sendable=74.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=792005 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT coloring score=79.41 sendable=74.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=566682 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=77.77 sendable=73.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.29 installs=1885678 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.04 sendable=73.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.92 installs=66813 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.19 sendable=73.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.51 installs=113040 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.67 sendable=72.62 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.22 installs=1005037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=77.17 sendable=71.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=980711 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=76.33 sendable=70.72 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=227234 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=73.11 sendable=70.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.43 installs=672503 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=75.3 sendable=69.84 stage=QUALIFIED_CANDIDATE_ONLY quality=94.93 mvp=65.0 installs=167810 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT other score=77.19 sendable=68.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.61 installs=982351 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.38 sendable=68.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=133732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=77.98 sendable=67.1 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2794462 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sandbox score=73.29 sendable=66.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=60.08 installs=271483 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT sandbox score=75.47 sendable=66.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.35 installs=980339 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
