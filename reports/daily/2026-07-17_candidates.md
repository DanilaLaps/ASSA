# Daily Candidates - 2026-07-17

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 113
- NEAR_MISS: 115
- REJECT: 203
- SINGLE_APP_WATCH: 13
- WATCH: 159

## Alert Stage Counts
- COOLDOWN_BLOCKED: 61
- NONE: 490
- QUALIFIED_CANDIDATE_ONLY: 51
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 70
- unknown_pattern_blocker_active: 70

## Top Candidates
- ALERT coloring score=88.72 sendable=88.78 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1726441 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=81.52 sendable=84.81 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=49748 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=89.41 sendable=83.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1411572 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.24 sendable=82.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=464294 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.39 sendable=82.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1330722 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=73.41 sendable=82.69 stage=COOLDOWN_BLOCKED quality=94.02 mvp=85.0 installs=16409 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_opportunity_score risks=unknown_coverage
- ALERT sort_puzzle score=86.74 sendable=82.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=524194 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.17 sendable=81.91 stage=COOLDOWN_BLOCKED quality=92.73 mvp=85.0 installs=33339 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=83.0 sendable=80.7 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=188281 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.75 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1074893 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.33 sendable=79.82 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=78088 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT tile_match score=83.51 sendable=79.4 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.09 installs=171069 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.5 sendable=79.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1708182 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT arrow_puzzle score=86.54 sendable=79.31 stage=SENDABLE_ALERT quality=88.0 mvp=79.74 installs=1361543 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.62 sendable=78.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.28 installs=2388779 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=84.57 sendable=78.37 stage=COOLDOWN_BLOCKED quality=88.0 mvp=64.13 installs=512595 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=73.5 sendable=78.22 stage=COOLDOWN_BLOCKED quality=94.32 mvp=65.0 installs=59378 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=80.88 sendable=76.95 stage=COOLDOWN_BLOCKED quality=91.53 mvp=65.0 installs=191659 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=81.27 sendable=76.94 stage=COOLDOWN_BLOCKED quality=85.13 mvp=85.0 installs=133198 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.18 sendable=76.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.15 installs=2314704 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal

## Rejected Reason Distribution
- classifier_low_confidence: 5
- giant_dominated: 9
- growth_by_one_app_too_high: 167
- low_demand: 121
- low_mvp_feasibility: 79
- low_score: 203
- severe_paid_spike: 143
- too_few_apps: 123
- top_app_too_dominant: 172
- unknown_pattern_blocker_active: 8
- weak_data_quality: 200
