# Alert Funnel - 2026-09-04

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 105
- NEAR_MISS: 105
- REJECT: 222
- SINGLE_APP_WATCH: 14
- WATCH: 156

## Alert Stage Counts
- COOLDOWN_BLOCKED: 5
- NONE: 497
- QUALIFIED_CANDIDATE_ONLY: 99
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 5
- duplicate_market_signals_suppressed: 128
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 186
- below_data_quality_for_trend_confidence: 310
- below_data_quality_score: 310
- below_mvp_feasibility: 192
- below_opportunity_score: 489
- below_sendable_alert_score: 595
- below_team_fit_score: 362
- below_trend_confidence_score: 332
- blocked_risk_tag: 144
- complex_full_product: 255
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 5
- duplicate_market_signal: 128
- giant_developer_competition: 28
- giant_developer_penalty: 24
- giant_share_too_high: 14
- growth_by_one_app_too_high: 287
- high_mvp_complexity: 130
- high_production_complexity: 60
- leader_dominated_market: 250
- low_classification_confidence: 186
- low_developer_diversity: 155
- low_mvp_feasibility: 192
- low_total_daily_installs: 133
- low_total_daily_installs_for_trend_confidence: 133
- market_signal_duplicate: 8
- no_growth_history: 2
- not_alert_status: 497
- one_app_growth_penalty: 312
- organic_confidence_low: 248
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 140
- single_app_breakout_not_regular_alert: 155
- single_developer_dominance: 222
- single_developer_penalty: 275
- single_developer_share_too_high: 250
- too_few_apps_for_sendable: 247
- too_few_apps_for_trend_confidence: 247
- too_few_successful_new_apps: 155
- too_few_successful_new_apps_for_trend_confidence: 155
- too_few_unique_developers: 155
- top3_too_dominant: 356
- top_app_concentration_penalty: 296
- top_app_too_dominant: 296
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.61 sendable=85.35 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=67746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.3 sendable=84.5 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=51742 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=unknown_coverage
- ALERT sort_puzzle score=78.98 sendable=82.53 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=30941 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=84.93 sendable=82.4 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=114299 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.1 sendable=81.86 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=16030 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=86.8 sendable=80.65 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1540484 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.94 sendable=79.62 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=867245 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.87 sendable=79.35 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.92 installs=1254458 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.99 sendable=78.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.35 installs=264880 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.56 sendable=77.88 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.46 installs=1512417 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.6 sendable=77.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=334804 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=82.5 sendable=77.76 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.75 installs=153372 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.35 sendable=77.66 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=201078 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=87.47 sendable=77.62 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=740177 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=81.25 sendable=76.34 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.0 installs=185385 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.06 sendable=75.97 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=39820 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=82.16 sendable=75.85 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=55127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=84.95 sendable=75.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=70.35 installs=122041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=71.4 sendable=75.58 stage=QUALIFIED_CANDIDATE_ONLY quality=92.04 mvp=81.0 installs=5929 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=85.73 sendable=75.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.41 installs=1267090 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
