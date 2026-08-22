# Alert Funnel - 2026-08-22

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 107
- NEAR_MISS: 110
- REJECT: 217
- SINGLE_APP_WATCH: 4
- WATCH: 166

## Alert Stage Counts
- COOLDOWN_BLOCKED: 12
- NONE: 497
- QUALIFIED_CANDIDATE_ONLY: 94
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 12
- duplicate_market_signals_suppressed: 103
- limit_blocked: 1

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 181
- below_data_quality_for_trend_confidence: 297
- below_data_quality_score: 297
- below_mvp_feasibility: 194
- below_opportunity_score: 480
- below_sendable_alert_score: 590
- below_team_fit_score: 361
- below_trend_confidence_score: 304
- blocked_risk_tag: 151
- complex_full_product: 262
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 12
- duplicate_market_signal: 103
- giant_developer_competition: 34
- giant_developer_penalty: 32
- giant_share_too_high: 22
- growth_by_one_app_too_high: 273
- high_mvp_complexity: 121
- high_production_complexity: 59
- leader_dominated_market: 242
- low_classification_confidence: 181
- low_developer_diversity: 156
- low_mvp_feasibility: 194
- low_total_daily_installs: 143
- low_total_daily_installs_for_trend_confidence: 143
- market_signal_duplicate: 3
- no_growth_history: 3
- not_alert_status: 497
- one_app_growth_penalty: 300
- organic_confidence_low: 241
- other_niche_low_confidence: 62
- per_niche_limit_blocked: 1
- severe_paid_spike_penalty: 149
- single_app_breakout_not_regular_alert: 155
- single_developer_dominance: 228
- single_developer_penalty: 260
- single_developer_share_too_high: 244
- too_few_apps_for_sendable: 228
- too_few_apps_for_trend_confidence: 228
- too_few_successful_new_apps: 155
- too_few_successful_new_apps_for_trend_confidence: 155
- too_few_unique_developers: 156
- top3_too_dominant: 350
- top_app_concentration_penalty: 289
- top_app_too_dominant: 289
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT tile_match score=89.57 sendable=83.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1396399 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=90.1 sendable=83.24 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1341260 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=one_app_growth_penalty risks=unknown_coverage
- ALERT block_puzzle score=89.31 sendable=82.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1516282 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.45 sendable=82.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.27 installs=2197889 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.27 sendable=82.03 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=369476 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.87 sendable=81.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.84 installs=4956338 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.04 sendable=81.3 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49993 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=85.13 sendable=81.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=481944 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.67 sendable=81.2 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.25 installs=2008554 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.45 sendable=81.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1790045 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.73 sendable=80.51 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=105663 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=77.05 sendable=80.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=16127 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=87.32 sendable=80.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.76 installs=1393318 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.83 sendable=79.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.8 installs=366587 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.62 sendable=79.39 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.51 installs=628405 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.83 sendable=79.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=913064 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.6 sendable=79.31 stage=QUALIFIED_CANDIDATE_ONLY quality=94.74 mvp=65.0 installs=15542 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=86.46 sendable=79.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.8 installs=621947 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.16 sendable=79.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.72 installs=297567 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.15 sendable=78.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=96913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
