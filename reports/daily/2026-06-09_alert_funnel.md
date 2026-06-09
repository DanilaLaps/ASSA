# Alert Funnel - 2026-06-09

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 72
- NEAR_MISS: 141
- REJECT: 196
- SINGLE_APP_WATCH: 16
- WATCH: 186

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 539
- QUALIFIED_CANDIDATE_ONLY: 70
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 1
- duplicate_market_signals_suppressed: 121
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Sendable Failure Distribution
- below_classification_confidence: 198
- below_data_quality_for_trend_confidence: 409
- below_data_quality_score: 409
- below_mvp_feasibility: 214
- below_opportunity_score: 548
- below_sendable_alert_score: 610
- below_team_fit_score: 386
- below_trend_confidence_score: 453
- blocked_risk_tag: 135
- complex_full_product: 294
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 1
- duplicate_market_signal: 121
- giant_developer_competition: 29
- giant_developer_penalty: 27
- giant_share_too_high: 18
- growth_by_one_app_too_high: 336
- high_mvp_complexity: 140
- high_production_complexity: 60
- leader_dominated_market: 214
- low_classification_confidence: 198
- low_developer_diversity: 143
- low_mvp_feasibility: 214
- low_total_daily_installs: 115
- low_total_daily_installs_for_trend_confidence: 115
- market_signal_duplicate: 5
- no_growth_history: 4
- not_alert_status: 539
- one_app_growth_penalty: 359
- organic_confidence_low: 204
- other_niche_low_confidence: 70
- severe_paid_spike_penalty: 104
- single_app_breakout_not_regular_alert: 142
- single_developer_dominance: 195
- single_developer_penalty: 242
- single_developer_share_too_high: 217
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 142
- too_few_successful_new_apps_for_trend_confidence: 142
- too_few_unique_developers: 143
- top3_too_dominant: 350
- top_app_concentration_penalty: 258
- top_app_too_dominant: 258
- unknown_pattern_blocker_active: 74

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.04 sendable=81.41 stage=COOLDOWN_BLOCKED quality=90.0 mvp=85.0 installs=74438 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.79 sendable=74.65 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=85.0 installs=60846 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.04 sendable=73.13 stage=QUALIFIED_CANDIDATE_ONLY quality=81.93 mvp=85.0 installs=41713 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=78.41 sendable=72.23 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.21 installs=1063492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.12 sendable=71.77 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=903666 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.51 sendable=71.63 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=77.95 installs=2748109 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=76.34 sendable=70.79 stage=QUALIFIED_CANDIDATE_ONLY quality=89.9 mvp=65.0 installs=307908 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT mahjong score=74.48 sendable=70.56 stage=QUALIFIED_CANDIDATE_ONLY quality=82.5 mvp=78.77 installs=37773 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.17 sendable=70.38 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=74.95 installs=133602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=71.81 sendable=70.16 stage=QUALIFIED_CANDIDATE_ONLY quality=84.51 mvp=85.0 installs=22111 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal, weak_revenue_signal
- ALERT tile_match score=78.8 sendable=69.06 stage=QUALIFIED_CANDIDATE_ONLY quality=82.49 mvp=74.88 installs=56224 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.72 sendable=68.77 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=325582 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT other score=71.19 sendable=68.77 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=74.2 installs=46378 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.23 sendable=68.76 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=77.5 installs=43522 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=77.68 sendable=68.41 stage=QUALIFIED_CANDIDATE_ONLY quality=75.0 mvp=85.0 installs=103067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT mahjong score=78.92 sendable=68.04 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=250492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=77.07 sendable=67.95 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=388891 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=76.26 sendable=67.59 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=65.49 installs=530001 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.96 sendable=67.3 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.26 installs=1097464 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=72.1 sendable=66.44 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.0 installs=11324 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
