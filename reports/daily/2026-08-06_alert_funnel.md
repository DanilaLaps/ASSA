# Alert Funnel - 2026-08-06

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 70
- NEAR_MISS: 109
- REJECT: 183
- SINGLE_APP_WATCH: 19
- WATCH: 162

## Alert Stage Counts
- COOLDOWN_BLOCKED: 17
- NONE: 473
- QUALIFIED_CANDIDATE_ONLY: 52
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 17
- duplicate_market_signals_suppressed: 120
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 70
- unknown_dominant_cluster: 60
- unknown_pattern_blocker_active: 60

## Sendable Failure Distribution
- below_classification_confidence: 166
- below_data_quality_for_trend_confidence: 290
- below_data_quality_score: 290
- below_mvp_feasibility: 174
- below_opportunity_score: 456
- below_sendable_alert_score: 541
- below_team_fit_score: 333
- below_trend_confidence_score: 364
- blocked_risk_tag: 77
- complex_full_product: 242
- cooldown_normalized_niche: 17
- duplicate_market_signal: 120
- giant_developer_competition: 28
- giant_developer_penalty: 22
- giant_share_too_high: 17
- growth_by_one_app_too_high: 240
- high_mvp_complexity: 119
- high_production_complexity: 61
- leader_dominated_market: 216
- low_classification_confidence: 166
- low_developer_diversity: 148
- low_mvp_feasibility: 174
- low_total_daily_installs: 157
- low_total_daily_installs_for_trend_confidence: 157
- market_signal_duplicate: 6
- not_alert_status: 473
- one_app_growth_penalty: 257
- organic_confidence_low: 207
- other_niche_low_confidence: 54
- severe_paid_spike_penalty: 76
- single_app_breakout_not_regular_alert: 148
- single_developer_dominance: 200
- single_developer_penalty: 236
- single_developer_share_too_high: 218
- too_few_apps_for_sendable: 222
- too_few_apps_for_trend_confidence: 222
- too_few_successful_new_apps: 148
- too_few_successful_new_apps_for_trend_confidence: 148
- too_few_unique_developers: 148
- top3_too_dominant: 320
- top_app_concentration_penalty: 254
- top_app_too_dominant: 254
- unknown_pattern_blocker_active: 55

## Top Qualified But Not Sent
- ALERT hidden_object score=85.46 sendable=81.28 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=112648 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT hidden_object score=83.17 sendable=80.35 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=69635 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.47 sendable=79.81 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.96 installs=767629 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.5 sendable=77.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.03 installs=828323 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.83 sendable=77.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.39 installs=59650 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=86.29 sendable=77.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=101173 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.76 sendable=76.35 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.54 installs=118342 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.65 sendable=76.33 stage=COOLDOWN_BLOCKED quality=93.4 mvp=65.0 installs=6925 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=77.6 sendable=74.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=24335 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=78.47 sendable=74.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=80885 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.96 sendable=73.47 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=738643 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=88.0 sendable=72.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.12 installs=884046 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT arrow_puzzle score=80.24 sendable=72.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.19 installs=105152 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.47 sendable=71.06 stage=COOLDOWN_BLOCKED quality=87.44 mvp=67.3 installs=296215 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT idle_tycoon score=77.29 sendable=70.87 stage=QUALIFIED_CANDIDATE_ONLY quality=86.17 mvp=66.08 installs=21434 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.69 sendable=70.75 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.53 installs=785497 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT arrow_puzzle score=86.43 sendable=69.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.23 installs=293702 unknown_app_share=0.2319 unknown_installs_share=0.2349 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT coloring score=86.41 sendable=69.16 stage=QUALIFIED_CANDIDATE_ONLY quality=87.0 mvp=64.82 installs=628001 unknown_app_share=0.3578 unknown_installs_share=0.1875 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, mixed_unknown_cluster, unknown_coverage
- ALERT sandbox score=80.96 sendable=68.61 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=67.16 installs=335245 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT sort_puzzle score=81.26 sendable=68.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=37737 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
