# Alert Funnel - 2026-06-26

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 86
- NEAR_MISS: 89
- REJECT: 169
- SINGLE_APP_WATCH: 22
- WATCH: 189

## Alert Stage Counts
- COOLDOWN_BLOCKED: 22
- NONE: 469
- QUALIFIED_CANDIDATE_ONLY: 63
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 22
- duplicate_market_signals_suppressed: 114
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 181
- below_data_quality_for_trend_confidence: 280
- below_data_quality_score: 280
- below_mvp_feasibility: 200
- below_opportunity_score: 458
- below_sendable_alert_score: 555
- below_team_fit_score: 361
- below_trend_confidence_score: 354
- blocked_risk_tag: 64
- complex_full_product: 274
- cooldown_normalized_niche: 22
- duplicate_market_signal: 114
- giant_developer_competition: 33
- giant_developer_penalty: 27
- giant_share_too_high: 15
- growth_by_one_app_too_high: 210
- high_mvp_complexity: 134
- high_production_complexity: 69
- leader_dominated_market: 211
- low_classification_confidence: 181
- low_developer_diversity: 129
- low_mvp_feasibility: 200
- low_total_daily_installs: 133
- low_total_daily_installs_for_trend_confidence: 133
- market_signal_duplicate: 7
- not_alert_status: 469
- one_app_growth_penalty: 231
- organic_confidence_low: 204
- other_niche_low_confidence: 70
- severe_paid_spike_penalty: 62
- single_app_breakout_not_regular_alert: 129
- single_developer_dominance: 196
- single_developer_penalty: 229
- single_developer_share_too_high: 211
- too_few_apps_for_sendable: 217
- too_few_apps_for_trend_confidence: 217
- too_few_successful_new_apps: 129
- too_few_successful_new_apps_for_trend_confidence: 129
- too_few_unique_developers: 129
- top3_too_dominant: 327
- top_app_concentration_penalty: 250
- top_app_too_dominant: 250
- unknown_pattern_blocker_active: 75

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.31 sendable=79.89 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=20513 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=85.52 sendable=79.82 stage=COOLDOWN_BLOCKED quality=92.85 mvp=65.0 installs=127401 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=85.03 sendable=78.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.39 installs=83913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.46 sendable=78.21 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=50394 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.15 sendable=75.38 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=566486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT arrow_puzzle score=83.67 sendable=74.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.39 installs=71364 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=90.8 sendable=73.44 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=645579 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=74.7 sendable=72.85 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=20433 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=74.8 sendable=72.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.5 installs=12608 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT merge score=79.4 sendable=71.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.81 installs=31735 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=88.82 sendable=71.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=328933 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.67 sendable=70.94 stage=COOLDOWN_BLOCKED quality=88.91 mvp=65.0 installs=92003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=73.2 sendable=70.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.75 installs=41878 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=79.55 sendable=70.41 stage=COOLDOWN_BLOCKED quality=85.45 mvp=76.9 installs=25461 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=85.12 sendable=69.49 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.24 installs=416275 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=84.92 sendable=69.4 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=1144654 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT mahjong score=74.51 sendable=69.3 stage=QUALIFIED_CANDIDATE_ONLY quality=86.37 mvp=75.75 installs=15640 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.32 sendable=69.2 stage=COOLDOWN_BLOCKED quality=85.5 mvp=85.0 installs=24267 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=83.93 sendable=69.01 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.76 installs=543102 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT coloring score=78.58 sendable=68.73 stage=COOLDOWN_BLOCKED quality=88.0 mvp=63.96 installs=107930 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
