# Alert Funnel - 2026-07-01

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 115
- NEAR_MISS: 110
- REJECT: 193
- WATCH: 161

## Alert Stage Counts
- COOLDOWN_BLOCKED: 5
- NONE: 464
- QUALIFIED_CANDIDATE_ONLY: 109
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 5
- duplicate_market_signals_suppressed: 115
- limit_blocked: 1

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Sendable Failure Distribution
- below_classification_confidence: 177
- below_data_quality_for_trend_confidence: 247
- below_data_quality_score: 247
- below_mvp_feasibility: 194
- below_opportunity_score: 470
- below_sendable_alert_score: 571
- below_team_fit_score: 361
- below_trend_confidence_score: 236
- blocked_risk_tag: 160
- complex_full_product: 254
- cooldown_normalized_niche: 5
- duplicate_market_signal: 115
- giant_developer_competition: 36
- giant_developer_penalty: 33
- giant_share_too_high: 27
- growth_by_one_app_too_high: 262
- high_mvp_complexity: 113
- high_production_complexity: 55
- leader_dominated_market: 220
- low_classification_confidence: 177
- low_developer_diversity: 136
- low_mvp_feasibility: 194
- low_total_daily_installs: 85
- low_total_daily_installs_for_trend_confidence: 85
- market_signal_duplicate: 11
- not_alert_status: 464
- one_app_growth_penalty: 290
- organic_confidence_low: 217
- other_niche_low_confidence: 61
- per_niche_limit_blocked: 1
- severe_paid_spike_penalty: 159
- single_app_breakout_not_regular_alert: 135
- single_developer_dominance: 210
- single_developer_penalty: 247
- single_developer_share_too_high: 220
- too_few_apps_for_sendable: 210
- too_few_apps_for_trend_confidence: 210
- too_few_successful_new_apps: 135
- too_few_successful_new_apps_for_trend_confidence: 135
- too_few_unique_developers: 136
- top3_too_dominant: 351
- top_app_concentration_penalty: 274
- top_app_too_dominant: 274
- unknown_pattern_blocker_active: 67

## Top Qualified But Not Sent
- ALERT coloring score=89.47 sendable=83.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1339362 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.94 sendable=80.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.94 installs=2885646 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.14 sendable=80.33 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=343584 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.88 sendable=80.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.98 installs=2743451 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.87 sendable=80.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=138281 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.69 sendable=80.06 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.39 installs=6277052 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.98 sendable=80.03 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.08 installs=1748444 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=84.08 sendable=79.66 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.59 installs=1572697 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.05 sendable=79.14 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=663362 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.06 sendable=78.95 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.49 installs=194667 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=90.53 sendable=78.49 stage=QUALIFIED_CANDIDATE_ONLY quality=91.95 mvp=85.0 installs=1031031 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.29 sendable=78.42 stage=QUALIFIED_CANDIDATE_ONLY quality=86.63 mvp=82.75 installs=144333 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=80.0 sendable=78.0 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.05 installs=154336 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.12 sendable=77.85 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1517893 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=78.58 sendable=76.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.81 installs=683956 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.71 sendable=76.77 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.42 installs=1945424 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=74.63 sendable=76.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.25 installs=76578 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=72.6 sendable=76.47 stage=QUALIFIED_CANDIDATE_ONLY quality=92.06 mvp=65.0 installs=36586 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=82.22 sendable=76.23 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.0 installs=185359 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=78.56 sendable=76.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=60.62 installs=119055 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
