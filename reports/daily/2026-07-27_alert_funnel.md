# Alert Funnel - 2026-07-27

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 98
- NEAR_MISS: 111
- REJECT: 187
- SINGLE_APP_WATCH: 9
- WATCH: 185

## Alert Stage Counts
- COOLDOWN_BLOCKED: 2
- NONE: 492
- QUALIFIED_CANDIDATE_ONLY: 95
- SENDABLE_ALERT: 1

## Blocked Counts
- cooldown_blocked: 2
- duplicate_market_signals_suppressed: 104
- limit_blocked: 6

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 67
- unknown_pattern_blocker_active: 67

## Sendable Failure Distribution
- below_classification_confidence: 193
- below_data_quality_for_trend_confidence: 295
- below_data_quality_score: 295
- below_mvp_feasibility: 199
- below_opportunity_score: 479
- below_sendable_alert_score: 578
- below_team_fit_score: 359
- below_trend_confidence_score: 330
- blocked_risk_tag: 111
- complex_full_product: 274
- cooldown_exact_dedupe_key: 1
- cooldown_normalized_niche: 2
- duplicate_market_signal: 104
- giant_developer_competition: 29
- giant_developer_penalty: 27
- giant_share_too_high: 18
- growth_by_one_app_too_high: 294
- high_mvp_complexity: 130
- high_production_complexity: 52
- leader_dominated_market: 215
- low_classification_confidence: 193
- low_developer_diversity: 118
- low_mvp_feasibility: 199
- low_total_daily_installs: 119
- low_total_daily_installs_for_trend_confidence: 119
- market_signal_duplicate: 11
- no_growth_history: 2
- not_alert_status: 492
- one_app_growth_penalty: 324
- organic_confidence_low: 217
- other_niche_low_confidence: 64
- per_niche_limit_blocked: 6
- severe_paid_spike_penalty: 108
- single_app_breakout_not_regular_alert: 118
- single_developer_dominance: 203
- single_developer_penalty: 241
- single_developer_share_too_high: 217
- too_few_apps_for_sendable: 212
- too_few_apps_for_trend_confidence: 212
- too_few_successful_new_apps: 118
- too_few_successful_new_apps_for_trend_confidence: 118
- too_few_unique_developers: 118
- top3_too_dominant: 329
- top_app_concentration_penalty: 264
- top_app_too_dominant: 264
- unknown_pattern_blocker_active: 66

## Top Qualified But Not Sent
- ALERT sort_puzzle score=80.5 sendable=83.93 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=37153 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT coloring score=91.61 sendable=83.89 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1061303 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=84.93 sendable=81.51 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=62149 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.41 sendable=81.46 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=390142 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.76 sendable=81.13 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=927896 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.73 sendable=81.12 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=459904 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=83.8 sendable=81.05 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=50689 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.71 sendable=80.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.75 installs=976372 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.16 sendable=80.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.69 installs=331456 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.04 sendable=80.27 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.78 installs=626412 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT mahjong score=85.7 sendable=80.02 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=198232 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.02 sendable=79.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.42 installs=1415755 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.27 sendable=79.59 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=185611 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=85.69 sendable=79.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.16 installs=851919 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.22 sendable=79.18 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.37 installs=1120558 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.42 sendable=78.86 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=61.03 installs=465372 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.72 sendable=78.48 stage=QUALIFIED_CANDIDATE_ONLY quality=94.16 mvp=65.0 installs=41379 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.08 sendable=77.79 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=92844 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT word_puzzle score=79.48 sendable=77.42 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=142374 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=75.61 sendable=77.34 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=30084 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
