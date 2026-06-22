# Daily Candidates - 2026-06-22

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 89
- NEAR_MISS: 118
- REJECT: 176
- SINGLE_APP_WATCH: 19
- WATCH: 192

## Alert Stage Counts
- COOLDOWN_BLOCKED: 1
- NONE: 505
- QUALIFIED_CANDIDATE_ONLY: 86
- SENDABLE_ALERT: 2

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 79
- unknown_dominant_cluster: 75
- unknown_pattern_blocker_active: 75

## Top Candidates
- ALERT sort_puzzle score=90.32 sendable=85.75 stage=SENDABLE_ALERT quality=95.0 mvp=85.0 installs=429763 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=unknown_coverage
- ALERT sort_puzzle score=83.09 sendable=85.56 stage=QUALIFIED_CANDIDATE_ONLY quality=94.68 mvp=85.0 installs=62280 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=84.85 sendable=84.62 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=54529 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT coloring score=88.61 sendable=80.97 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=596221 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.31 sendable=80.32 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=849067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.04 sendable=79.52 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.67 installs=823383 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=87.46 sendable=79.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=794089 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.36 sendable=79.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=237304 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.45 sendable=79.31 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=640602 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.64 sendable=79.15 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.55 installs=155577 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.22 sendable=78.99 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=77.97 installs=1394965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.8 sendable=78.58 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=76.07 installs=1634983 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT word_puzzle score=84.73 sendable=78.32 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=101913 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.54 sendable=77.86 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=47280 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=85.74 sendable=77.6 stage=QUALIFIED_CANDIDATE_ONLY quality=94.8 mvp=65.0 installs=192085 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=72.62 sendable=77.56 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=13152 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT block_puzzle score=84.93 sendable=77.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.0 installs=99041 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.69 sendable=77.11 stage=QUALIFIED_CANDIDATE_ONLY quality=87.8 mvp=82.92 installs=52989 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=82.62 sendable=76.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=74.05 installs=92114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.61 sendable=74.29 stage=QUALIFIED_CANDIDATE_ONLY quality=88.23 mvp=85.0 installs=48195 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage, weak_revenue_signal

## Rejected Reason Distribution
- classifier_low_confidence: 5
- giant_dominated: 9
- growth_by_one_app_too_high: 110
- low_demand: 134
- low_mvp_feasibility: 68
- low_score: 176
- severe_paid_spike: 92
- too_few_apps: 114
- top_app_too_dominant: 141
- unknown_pattern_blocker_active: 7
- weak_data_quality: 171
