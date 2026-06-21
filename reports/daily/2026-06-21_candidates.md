# Daily Candidates - 2026-06-21

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 86
- NEAR_MISS: 120
- REJECT: 201
- SINGLE_APP_WATCH: 15
- WATCH: 181

## Alert Stage Counts
- COOLDOWN_BLOCKED: 50
- NONE: 517
- QUALIFIED_CANDIDATE_ONLY: 35
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 80
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Top Candidates
- ALERT sort_puzzle score=90.25 sendable=86.58 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=516420 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=83.11 sendable=84.06 stage=COOLDOWN_BLOCKED quality=94.76 mvp=85.0 installs=62839 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT tile_match score=86.4 sendable=80.9 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1022785 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.89 sendable=80.87 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=64621 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.66 sendable=80.41 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=745873 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.1 sendable=80.25 stage=COOLDOWN_BLOCKED quality=92.41 mvp=85.0 installs=34731 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=top3_too_dominant risks=unknown_coverage
- ALERT tile_match score=83.66 sendable=79.08 stage=COOLDOWN_BLOCKED quality=88.0 mvp=68.68 installs=882351 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=88.59 sendable=78.86 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=614637 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.88 sendable=78.85 stage=COOLDOWN_BLOCKED quality=88.0 mvp=84.56 installs=179211 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.7 sendable=78.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.37 installs=902672 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=85.36 sendable=78.57 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=130037 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.9 sendable=77.8 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.42 installs=3850278 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.29 sendable=77.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=959358 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.38 sendable=77.14 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.96 installs=1601804 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.14 sendable=77.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=74.88 installs=105425 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=84.23 sendable=76.76 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.89 installs=102165 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=80.87 sendable=76.64 stage=COOLDOWN_BLOCKED quality=88.0 mvp=82.75 installs=57449 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.4 sendable=76.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.91 installs=1919179 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.44 sendable=75.22 stage=COOLDOWN_BLOCKED quality=88.38 mvp=85.0 installs=48896 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal
- ALERT tile_match score=78.93 sendable=74.64 stage=COOLDOWN_BLOCKED quality=85.79 mvp=74.88 installs=43977 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 8
- giant_dominated: 13
- growth_by_one_app_too_high: 123
- low_demand: 137
- low_mvp_feasibility: 77
- low_score: 201
- severe_paid_spike: 97
- too_few_apps: 117
- top_app_too_dominant: 152
- unknown_pattern_blocker_active: 10
- weak_data_quality: 197
