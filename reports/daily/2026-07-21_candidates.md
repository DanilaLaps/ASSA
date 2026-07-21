# Daily Candidates - 2026-07-21

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 92
- NEAR_MISS: 113
- REJECT: 182
- SINGLE_APP_WATCH: 24
- WATCH: 178

## Alert Stage Counts
- COOLDOWN_BLOCKED: 3
- NONE: 497
- QUALIFIED_CANDIDATE_ONLY: 88
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 73
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Top Candidates
- ALERT sort_puzzle score=80.31 sendable=82.81 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=41986 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=78.89 sendable=82.24 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=24264 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=90.29 sendable=81.58 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=1261111 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.01 sendable=80.44 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=354240 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.0 sendable=78.5 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=940348 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.58 sendable=77.97 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=14685 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=89.13 sendable=77.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.75 installs=721505 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=85.19 sendable=76.72 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=68.81 installs=544692 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.2 sendable=76.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.86 installs=1028242 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.52 sendable=76.26 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=62.21 installs=410107 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=89.2 sendable=76.16 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=2020908 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT sort_puzzle score=84.35 sendable=75.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=279627 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.73 sendable=74.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.06 installs=1196597 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=86.95 sendable=74.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=73.48 installs=1250693 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.68 sendable=73.63 stage=QUALIFIED_CANDIDATE_ONLY quality=93.66 mvp=65.0 installs=116238 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=88.33 sendable=73.14 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.37 installs=1774538 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.21 sendable=71.7 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=152190 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.91 sendable=70.65 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=60.93 installs=468140 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, high_full_complexity, unknown_coverage
- ALERT runner score=81.29 sendable=69.61 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=203178 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=84.86 sendable=69.2 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=2394396 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 6
- giant_dominated: 10
- growth_by_one_app_too_high: 106
- low_demand: 124
- low_mvp_feasibility: 80
- low_score: 182
- severe_paid_spike: 87
- too_few_apps: 103
- top_app_too_dominant: 139
- unknown_pattern_blocker_active: 8
- weak_data_quality: 180
