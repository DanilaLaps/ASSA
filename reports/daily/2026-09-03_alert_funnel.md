# Alert Funnel - 2026-09-03

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 118
- NEAR_MISS: 99
- REJECT: 216
- SINGLE_APP_WATCH: 17
- WATCH: 151

## Alert Stage Counts
- COOLDOWN_BLOCKED: 12
- NONE: 483
- QUALIFIED_CANDIDATE_ONLY: 105
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 12
- duplicate_market_signals_suppressed: 123
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 186
- below_data_quality_for_trend_confidence: 305
- below_data_quality_score: 305
- below_mvp_feasibility: 192
- below_opportunity_score: 472
- below_sendable_alert_score: 587
- below_team_fit_score: 357
- below_trend_confidence_score: 311
- blocked_risk_tag: 143
- complex_full_product: 254
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 12
- duplicate_market_signal: 123
- giant_developer_competition: 27
- giant_developer_penalty: 21
- giant_share_too_high: 14
- growth_by_one_app_too_high: 283
- high_mvp_complexity: 129
- high_production_complexity: 58
- leader_dominated_market: 242
- low_classification_confidence: 186
- low_developer_diversity: 156
- low_mvp_feasibility: 192
- low_total_daily_installs: 128
- low_total_daily_installs_for_trend_confidence: 128
- market_signal_duplicate: 10
- no_growth_history: 3
- not_alert_status: 483
- one_app_growth_penalty: 308
- organic_confidence_low: 244
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 139
- single_app_breakout_not_regular_alert: 156
- single_developer_dominance: 221
- single_developer_penalty: 270
- single_developer_share_too_high: 243
- too_few_apps_for_sendable: 235
- too_few_apps_for_trend_confidence: 235
- too_few_successful_new_apps: 156
- too_few_successful_new_apps_for_trend_confidence: 156
- too_few_unique_developers: 156
- top3_too_dominant: 359
- top_app_concentration_penalty: 299
- top_app_too_dominant: 299
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=78.65 sendable=85.14 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=55493 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT coloring score=90.66 sendable=84.01 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1015755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=86.23 sendable=83.07 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=205051 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=84.3 sendable=82.62 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=119325 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=87.18 sendable=82.18 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1694846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.23 sendable=81.97 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=35041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=87.59 sendable=81.8 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=509760 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.58 sendable=81.72 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=16815 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.52 sendable=81.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=354475 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.04 sendable=80.89 stage=COOLDOWN_BLOCKED quality=94.8 mvp=65.0 installs=68645 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=90.02 sendable=80.72 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1523384 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.03 sendable=80.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=424102 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.55 sendable=80.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.41 installs=1606446 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.51 sendable=79.98 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=59986 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=86.87 sendable=79.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.8 installs=1288126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.84 sendable=79.64 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=41810 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=82.7 sendable=79.36 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.69 installs=180239 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.12 sendable=79.12 stage=QUALIFIED_CANDIDATE_ONLY quality=92.79 mvp=65.0 installs=34675 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=87.95 sendable=79.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.52 installs=1517451 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.69 sendable=78.97 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.13 installs=1766202 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
