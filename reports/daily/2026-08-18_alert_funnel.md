# Alert Funnel - 2026-08-18

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 77
- NEAR_MISS: 118
- REJECT: 192
- SINGLE_APP_WATCH: 21
- WATCH: 192

## Alert Stage Counts
- COOLDOWN_BLOCKED: 50
- NONE: 523
- QUALIFIED_CANDIDATE_ONLY: 26
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 50
- duplicate_market_signals_suppressed: 106
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 75
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 320
- below_data_quality_score: 320
- below_mvp_feasibility: 196
- below_opportunity_score: 495
- below_sendable_alert_score: 599
- below_team_fit_score: 353
- below_trend_confidence_score: 389
- blocked_risk_tag: 97
- complex_full_product: 262
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 50
- duplicate_market_signal: 106
- giant_developer_competition: 32
- giant_developer_penalty: 29
- giant_share_too_high: 22
- growth_by_one_app_too_high: 284
- high_mvp_complexity: 120
- high_production_complexity: 59
- leader_dominated_market: 232
- low_classification_confidence: 185
- low_developer_diversity: 152
- low_mvp_feasibility: 196
- low_total_daily_installs: 127
- low_total_daily_installs_for_trend_confidence: 127
- market_signal_duplicate: 3
- no_growth_history: 1
- not_alert_status: 523
- one_app_growth_penalty: 318
- organic_confidence_low: 229
- other_niche_low_confidence: 58
- severe_paid_spike_penalty: 95
- single_app_breakout_not_regular_alert: 151
- single_developer_dominance: 212
- single_developer_penalty: 258
- single_developer_share_too_high: 233
- too_few_apps_for_sendable: 230
- too_few_apps_for_trend_confidence: 230
- too_few_successful_new_apps: 151
- too_few_successful_new_apps_for_trend_confidence: 151
- too_few_unique_developers: 152
- top3_too_dominant: 349
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 63

## Top Qualified But Not Sent
- ALERT hidden_object score=86.03 sendable=80.32 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=205461 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.85 sendable=79.4 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=50862 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=88.65 sendable=78.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.98 installs=2278439 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.5 sendable=77.51 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.69 installs=261513 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.06 sendable=76.24 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1276370 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.94 sendable=75.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.85 installs=1291501 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=76.21 sendable=75.72 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.18 installs=35625 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.56 sendable=75.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=310794 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=80.33 sendable=74.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.43 installs=178649 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.95 sendable=74.24 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=102792 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.54 sendable=74.08 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=48927 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=87.77 sendable=73.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.56 installs=4377153 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.82 sendable=73.65 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.39 installs=348806 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=79.84 sendable=72.29 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=159691 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=83.63 sendable=71.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.68 installs=450315 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT tile_match score=83.16 sendable=70.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.53 installs=155629 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.6 sendable=70.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1071207 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.27 sendable=70.54 stage=COOLDOWN_BLOCKED quality=84.61 mvp=85.0 installs=40573 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=79.7 sendable=70.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.83 installs=98821 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT hidden_object score=80.32 sendable=69.94 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=67696 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
