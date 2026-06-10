# Alert Funnel - 2026-06-10

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 81
- NEAR_MISS: 141
- REJECT: 189
- SINGLE_APP_WATCH: 18
- WATCH: 173

## Alert Stage Counts
- COOLDOWN_BLOCKED: 2
- NONE: 521
- QUALIFIED_CANDIDATE_ONLY: 78
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 2
- duplicate_market_signals_suppressed: 100
- limit_blocked: 0

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 76
- unknown_pattern_blocker_active: 76

## Sendable Failure Distribution
- below_classification_confidence: 196
- below_data_quality_for_trend_confidence: 386
- below_data_quality_score: 386
- below_mvp_feasibility: 213
- below_opportunity_score: 535
- below_sendable_alert_score: 600
- below_team_fit_score: 384
- below_trend_confidence_score: 416
- blocked_risk_tag: 140
- complex_full_product: 292
- cooldown_exact_dedupe_key: 2
- cooldown_normalized_niche: 2
- duplicate_market_signal: 100
- giant_developer_competition: 30
- giant_developer_penalty: 25
- giant_share_too_high: 17
- growth_by_one_app_too_high: 318
- high_mvp_complexity: 141
- high_production_complexity: 61
- leader_dominated_market: 212
- low_classification_confidence: 196
- low_developer_diversity: 134
- low_mvp_feasibility: 213
- low_total_daily_installs: 114
- low_total_daily_installs_for_trend_confidence: 114
- market_signal_duplicate: 2
- no_growth_history: 2
- not_alert_status: 521
- one_app_growth_penalty: 343
- organic_confidence_low: 210
- other_niche_low_confidence: 71
- severe_paid_spike_penalty: 111
- single_app_breakout_not_regular_alert: 133
- single_developer_dominance: 194
- single_developer_penalty: 239
- single_developer_share_too_high: 215
- too_few_apps_for_sendable: 207
- too_few_apps_for_trend_confidence: 207
- too_few_successful_new_apps: 133
- too_few_successful_new_apps_for_trend_confidence: 133
- too_few_unique_developers: 134
- top3_too_dominant: 340
- top_app_concentration_penalty: 255
- top_app_too_dominant: 255
- unknown_pattern_blocker_active: 76

## Top Qualified But Not Sent
- ALERT sort_puzzle score=81.04 sendable=83.9 stage=COOLDOWN_BLOCKED quality=90.0 mvp=85.0 installs=82245 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.79 sendable=82.98 stage=COOLDOWN_BLOCKED quality=90.0 mvp=85.0 installs=68287 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage, weak_rating_signal
- ALERT hidden_object score=76.51 sendable=75.38 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=332706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.02 sendable=73.96 stage=QUALIFIED_CANDIDATE_ONLY quality=81.83 mvp=85.0 installs=41472 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.31 sendable=73.64 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=83.07 installs=71483 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.24 sendable=72.92 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=75.12 installs=124225 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT arrow_puzzle score=79.63 sendable=72.62 stage=QUALIFIED_CANDIDATE_ONLY quality=80.6 mvp=80.24 installs=1999262 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT hidden_object score=77.2 sendable=71.98 stage=QUALIFIED_CANDIDATE_ONLY quality=90.0 mvp=65.0 installs=422567 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT mahjong score=74.63 sendable=71.85 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=78.77 installs=35101 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT tile_match score=79.26 sendable=71.46 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=887925 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=79.31 sendable=71.35 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=78.65 installs=42085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.78 sendable=70.36 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=74.93 installs=481619 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=80.1 sendable=69.9 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=1160922 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=80.06 sendable=69.61 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=910650 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT mahjong score=78.94 sendable=69.61 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=85.0 installs=247709 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT merge score=71.98 sendable=68.91 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=64.12 installs=13022 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=70.85 sendable=68.68 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=75.36 installs=50672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT sort_puzzle score=79.6 sendable=68.61 stage=QUALIFIED_CANDIDATE_ONLY quality=74.23 mvp=85.0 installs=98437 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_rating_signal
- ALERT tile_match score=76.17 sendable=68.14 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=66.08 installs=557693 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
- ALERT block_puzzle score=77.98 sendable=68.12 stage=QUALIFIED_CANDIDATE_ONLY quality=83.0 mvp=72.35 installs=1092517 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage, weak_rating_signal
