# Alert Funnel - 2026-08-30

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 109
- NEAR_MISS: 104
- REJECT: 197
- SINGLE_APP_WATCH: 14
- WATCH: 169

## Alert Stage Counts
- COOLDOWN_BLOCKED: 45
- NONE: 484
- QUALIFIED_CANDIDATE_ONLY: 63
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 45
- duplicate_market_signals_suppressed: 120
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 70
- unknown_pattern_blocker_active: 70

## Sendable Failure Distribution
- below_classification_confidence: 184
- below_data_quality_for_trend_confidence: 305
- below_data_quality_score: 305
- below_mvp_feasibility: 191
- below_opportunity_score: 482
- below_sendable_alert_score: 588
- below_team_fit_score: 354
- below_trend_confidence_score: 329
- blocked_risk_tag: 130
- complex_full_product: 254
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 45
- duplicate_market_signal: 120
- giant_developer_competition: 29
- giant_developer_penalty: 28
- giant_share_too_high: 18
- growth_by_one_app_too_high: 281
- high_mvp_complexity: 126
- high_production_complexity: 63
- leader_dominated_market: 229
- low_classification_confidence: 184
- low_developer_diversity: 143
- low_mvp_feasibility: 191
- low_total_daily_installs: 130
- low_total_daily_installs_for_trend_confidence: 130
- market_signal_duplicate: 7
- no_growth_history: 1
- not_alert_status: 484
- one_app_growth_penalty: 309
- organic_confidence_low: 226
- other_niche_low_confidence: 65
- severe_paid_spike_penalty: 129
- single_app_breakout_not_regular_alert: 143
- single_developer_dominance: 208
- single_developer_penalty: 259
- single_developer_share_too_high: 231
- too_few_apps_for_sendable: 229
- too_few_apps_for_trend_confidence: 229
- too_few_successful_new_apps: 143
- too_few_successful_new_apps_for_trend_confidence: 143
- too_few_unique_developers: 143
- top3_too_dominant: 344
- top_app_concentration_penalty: 282
- top_app_too_dominant: 282
- unknown_pattern_blocker_active: 70

## Top Qualified But Not Sent
- ALERT coloring score=89.66 sendable=86.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=923918 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.86 sendable=82.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1528179 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=78.41 sendable=82.05 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=16973 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=89.5 sendable=81.53 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=939274 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.97 sendable=80.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=44066 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=83.3 sendable=79.56 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=95191 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=86.73 sendable=79.2 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1487648 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.78 sendable=78.44 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=63863 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.3 sendable=78.24 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.99 installs=1586601 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.03 sendable=77.98 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.72 installs=355830 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.08 sendable=77.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.95 installs=1394299 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.29 sendable=77.28 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=36922 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=80.85 sendable=77.22 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=58230 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=82.26 sendable=77.2 stage=COOLDOWN_BLOCKED quality=85.99 mvp=85.0 installs=34937 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.25 sendable=77.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.66 installs=246792 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.88 sendable=77.07 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.91 installs=1239710 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=82.37 sendable=76.81 stage=COOLDOWN_BLOCKED quality=88.0 mvp=70.14 installs=195756 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.22 sendable=76.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.66 installs=1201796 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=74.39 sendable=75.32 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=35520 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=81.01 sendable=75.02 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=45675 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
