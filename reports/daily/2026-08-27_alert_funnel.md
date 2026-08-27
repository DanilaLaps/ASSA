# Alert Funnel - 2026-08-27

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 72
- NEAR_MISS: 122
- REJECT: 187
- SINGLE_APP_WATCH: 17
- WATCH: 191

## Alert Stage Counts
- COOLDOWN_BLOCKED: 45
- NONE: 517
- QUALIFIED_CANDIDATE_ONLY: 26
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 45
- duplicate_market_signals_suppressed: 121
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 185
- below_data_quality_for_trend_confidence: 313
- below_data_quality_score: 313
- below_mvp_feasibility: 189
- below_opportunity_score: 503
- below_sendable_alert_score: 587
- below_team_fit_score: 354
- below_trend_confidence_score: 386
- blocked_risk_tag: 99
- complex_full_product: 257
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 45
- duplicate_market_signal: 121
- giant_developer_competition: 29
- giant_developer_penalty: 26
- giant_share_too_high: 16
- growth_by_one_app_too_high: 296
- high_mvp_complexity: 122
- high_production_complexity: 61
- leader_dominated_market: 232
- low_classification_confidence: 185
- low_developer_diversity: 143
- low_mvp_feasibility: 189
- low_total_daily_installs: 137
- low_total_daily_installs_for_trend_confidence: 137
- market_signal_duplicate: 7
- no_growth_history: 1
- not_alert_status: 517
- one_app_growth_penalty: 319
- organic_confidence_low: 217
- other_niche_low_confidence: 63
- severe_paid_spike_penalty: 98
- single_app_breakout_not_regular_alert: 143
- single_developer_dominance: 203
- single_developer_penalty: 252
- single_developer_share_too_high: 233
- too_few_apps_for_sendable: 222
- too_few_apps_for_trend_confidence: 222
- too_few_successful_new_apps: 143
- too_few_successful_new_apps_for_trend_confidence: 143
- too_few_unique_developers: 143
- top3_too_dominant: 340
- top_app_concentration_penalty: 267
- top_app_too_dominant: 267
- unknown_pattern_blocker_active: 68

## Top Qualified But Not Sent
- ALERT coloring score=89.85 sendable=84.68 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=906344 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.7 sendable=80.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1361357 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.93 sendable=79.63 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.93 installs=1231986 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.26 sendable=79.05 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.45 installs=1526396 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.04 sendable=78.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1334700 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.96 sendable=78.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=295479 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=82.86 sendable=77.63 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=81653 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=76.86 sendable=77.26 stage=COOLDOWN_BLOCKED quality=92.85 mvp=65.0 installs=14732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=81.92 sendable=75.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=69.71 installs=157609 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.81 sendable=74.79 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.59 installs=3673326 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.5 sendable=73.03 stage=COOLDOWN_BLOCKED quality=88.0 mvp=66.52 installs=424937 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.81 sendable=72.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.55 installs=1106927 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=79.45 sendable=72.08 stage=COOLDOWN_BLOCKED quality=94.83 mvp=65.0 installs=43301 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=74.76 sendable=71.87 stage=COOLDOWN_BLOCKED quality=85.0 mvp=76.62 installs=13909 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.73 sendable=71.5 stage=COOLDOWN_BLOCKED quality=87.15 mvp=85.0 installs=68090 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.23 sendable=71.22 stage=COOLDOWN_BLOCKED quality=88.0 mvp=67.57 installs=2202124 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=81.02 sendable=70.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.95 installs=174315 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=70.69 sendable=69.91 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.92 installs=98317 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT runner score=84.75 sendable=69.37 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.58 installs=855904 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=84.56 sendable=69.22 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=64.89 installs=1324874 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
