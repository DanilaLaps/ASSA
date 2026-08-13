# Daily Candidates - 2026-08-13

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 129
- NEAR_MISS: 105
- REJECT: 207
- SINGLE_APP_WATCH: 3
- WATCH: 166

## Alert Stage Counts
- COOLDOWN_BLOCKED: 12
- NONE: 481
- QUALIFIED_CANDIDATE_ONLY: 116
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Top Candidates
- ALERT coloring score=89.1 sendable=88.11 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1277737 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=79.2 sendable=84.92 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=59605 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.36 sendable=83.42 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=30768 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=89.9 sendable=83.0 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1632277 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=88.92 sendable=81.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1138293 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=86.17 sendable=81.71 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=240980 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.12 sendable=81.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=462000 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.91 sendable=81.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.41 installs=1994389 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.35 sendable=81.04 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=125565 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=86.65 sendable=81.02 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=554486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.09 sendable=80.89 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.28 installs=1289654 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.16 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.55 installs=1720896 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.13 sendable=80.23 stage=SENDABLE_ALERT quality=88.0 mvp=73.61 installs=4510669 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.55 sendable=80.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=119772 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.03 sendable=80.12 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1336941 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.65 sendable=79.96 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=65.0 installs=44671 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=87.3 sendable=79.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.46 installs=1804827 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.0 sendable=79.37 stage=QUALIFIED_CANDIDATE_ONLY quality=94.4 mvp=65.0 installs=22614 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.07 sendable=79.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.66 installs=270174 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.43 sendable=78.89 stage=QUALIFIED_CANDIDATE_ONLY quality=86.21 mvp=85.0 installs=66783 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 7
- giant_dominated: 14
- growth_by_one_app_too_high: 184
- low_demand: 143
- low_mvp_feasibility: 77
- low_score: 207
- severe_paid_spike: 170
- too_few_apps: 153
- top_app_too_dominant: 184
- unknown_pattern_blocker_active: 12
- weak_data_quality: 206
