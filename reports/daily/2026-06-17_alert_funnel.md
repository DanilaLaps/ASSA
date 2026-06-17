# Alert Funnel - 2026-06-17

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 69
- NEAR_MISS: 85
- REJECT: 202
- SINGLE_APP_WATCH: 20
- WATCH: 223

## Alert Stage Counts
- COOLDOWN_BLOCKED: 10
- NONE: 530
- QUALIFIED_CANDIDATE_ONLY: 58
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 10
- duplicate_market_signals_suppressed: 104
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 76
- unknown_pattern_blocker_active: 76

## Sendable Failure Distribution
- below_classification_confidence: 194
- below_data_quality_for_trend_confidence: 309
- below_data_quality_score: 309
- below_mvp_feasibility: 204
- below_opportunity_score: 559
- below_sendable_alert_score: 599
- below_team_fit_score: 384
- below_trend_confidence_score: 365
- blocked_risk_tag: 110
- complex_full_product: 287
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 10
- duplicate_market_signal: 104
- giant_developer_competition: 35
- giant_developer_penalty: 33
- giant_share_too_high: 16
- growth_by_one_app_too_high: 295
- high_mvp_complexity: 132
- high_production_complexity: 56
- leader_dominated_market: 214
- low_classification_confidence: 194
- low_developer_diversity: 123
- low_mvp_feasibility: 204
- low_total_daily_installs: 114
- low_total_daily_installs_for_trend_confidence: 114
- market_signal_duplicate: 4
- no_growth_history: 3
- not_alert_status: 530
- one_app_growth_penalty: 316
- organic_confidence_low: 227
- other_niche_low_confidence: 70
- severe_paid_spike_penalty: 106
- single_app_breakout_not_regular_alert: 123
- single_developer_dominance: 195
- single_developer_penalty: 238
- single_developer_share_too_high: 216
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 123
- too_few_successful_new_apps_for_trend_confidence: 123
- too_few_unique_developers: 123
- top3_too_dominant: 340
- top_app_concentration_penalty: 264
- top_app_too_dominant: 264
- unknown_pattern_blocker_active: 76

## Top Qualified But Not Sent
- ALERT sort_puzzle score=71.18 sendable=78.74 stage=COOLDOWN_BLOCKED quality=94.55 mvp=85.0 installs=50085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.32 sendable=76.87 stage=COOLDOWN_BLOCKED quality=93.39 mvp=85.0 installs=29684 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=75.74 sendable=76.39 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=77953 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.29 sendable=74.87 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=311544 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=73.19 sendable=74.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.0 installs=81537 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.47 sendable=73.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=861129 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=72.39 sendable=72.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=83.07 installs=74104 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=80.09 sendable=72.64 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1183580 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=74.42 sendable=72.54 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.12 installs=122811 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=76.31 sendable=72.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.58 installs=197974 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=78.84 sendable=71.07 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.12 installs=5078670 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT word_puzzle score=76.03 sendable=70.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=130094 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=80.64 sendable=69.22 stage=QUALIFIED_CANDIDATE_ONLY quality=87.47 mvp=85.0 installs=2486100 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal, weak_rating_signal
- ALERT other score=77.12 sendable=67.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.07 installs=962491 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT coloring score=79.38 sendable=67.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=579121 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=76.77 sendable=67.41 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=261156 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sandbox score=75.89 sendable=66.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.15 installs=317446 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
- ALERT tile_match score=72.8 sendable=66.35 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.5 installs=634265 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT runner score=78.02 sendable=66.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2908129 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sandbox score=73.22 sendable=65.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=62.15 installs=218030 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage, weak_rating_signal
