# Alert Funnel - 2026-08-14

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 119
- NEAR_MISS: 111
- REJECT: 214
- SINGLE_APP_WATCH: 3
- WATCH: 158

## Alert Stage Counts
- COOLDOWN_BLOCKED: 74
- NONE: 486
- QUALIFIED_CANDIDATE_ONLY: 44
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 74
- duplicate_market_signals_suppressed: 118
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 66
- unknown_pattern_blocker_active: 66

## Sendable Failure Distribution
- below_classification_confidence: 187
- below_data_quality_for_trend_confidence: 285
- below_data_quality_score: 285
- below_mvp_feasibility: 197
- below_opportunity_score: 476
- below_sendable_alert_score: 593
- below_team_fit_score: 379
- below_trend_confidence_score: 270
- blocked_risk_tag: 178
- complex_full_product: 268
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 74
- duplicate_market_signal: 118
- giant_developer_competition: 33
- giant_developer_penalty: 33
- giant_share_too_high: 20
- growth_by_one_app_too_high: 277
- high_mvp_complexity: 119
- high_production_complexity: 53
- leader_dominated_market: 239
- low_classification_confidence: 187
- low_developer_diversity: 159
- low_mvp_feasibility: 197
- low_total_daily_installs: 143
- low_total_daily_installs_for_trend_confidence: 143
- market_signal_duplicate: 7
- no_growth_history: 3
- not_alert_status: 486
- one_app_growth_penalty: 298
- organic_confidence_low: 242
- other_niche_low_confidence: 60
- severe_paid_spike_penalty: 171
- single_app_breakout_not_regular_alert: 158
- single_developer_dominance: 224
- single_developer_penalty: 260
- single_developer_share_too_high: 241
- too_few_apps_for_sendable: 237
- too_few_apps_for_trend_confidence: 237
- too_few_successful_new_apps: 158
- too_few_successful_new_apps_for_trend_confidence: 158
- too_few_unique_developers: 159
- top3_too_dominant: 363
- top_app_concentration_penalty: 279
- top_app_too_dominant: 279
- unknown_pattern_blocker_active: 64

## Top Qualified But Not Sent
- ALERT coloring score=88.9 sendable=88.03 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1117056 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.86 sendable=84.26 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=46824 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=76.48 sendable=83.07 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=23135 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.23 sendable=82.09 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1214582 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.8 sendable=81.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=954192 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.69 sendable=81.83 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=401454 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.56 sendable=81.57 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1298569 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.0 sendable=81.15 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.4 installs=1503341 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.58 sendable=80.99 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=485226 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.97 sendable=80.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.27 installs=990755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.86 sendable=80.46 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.46 installs=1417243 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.72 sendable=80.27 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.78 installs=897886 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.0 sendable=79.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.68 installs=3788875 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.99 sendable=79.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.25 installs=1377054 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.85 sendable=79.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=63.75 installs=584669 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.37 sendable=79.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.62 installs=232131 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.78 sendable=79.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.97 installs=143810 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.09 sendable=79.03 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=199149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=77.94 sendable=78.66 stage=COOLDOWN_BLOCKED quality=93.28 mvp=65.0 installs=42334 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=82.76 sendable=78.58 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=96614 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
