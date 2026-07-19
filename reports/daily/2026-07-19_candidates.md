# Daily Candidates - 2026-07-19

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 105
- NEAR_MISS: 102
- REJECT: 198
- SINGLE_APP_WATCH: 16
- WATCH: 172

## Alert Stage Counts
- COOLDOWN_BLOCKED: 29
- NONE: 488
- QUALIFIED_CANDIDATE_ONLY: 75
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 74
- unknown_dominant_cluster: 69
- unknown_pattern_blocker_active: 69

## Top Candidates
- ALERT sort_puzzle score=75.5 sendable=82.89 stage=COOLDOWN_BLOCKED quality=94.34 mvp=85.0 installs=16601 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=77.15 sendable=81.55 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=20664 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT coloring score=87.84 sendable=80.89 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1055057 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=79.21 sendable=80.73 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=39504 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=84.38 sendable=80.52 stage=COOLDOWN_BLOCKED quality=85.82 mvp=85.0 installs=149953 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.77 sendable=80.31 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=466693 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=90.19 sendable=80.25 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=806262 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.56 sendable=79.6 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=413047 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.01 sendable=79.34 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1062042 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=86.43 sendable=79.24 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.46 installs=1249980 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=85.72 sendable=79.21 stage=SENDABLE_ALERT quality=88.0 mvp=62.03 installs=458609 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.96 sendable=78.84 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1362456 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=86.87 sendable=78.71 stage=COOLDOWN_BLOCKED quality=88.0 mvp=78.21 installs=1968027 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.86 sendable=78.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=318797 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=80.44 sendable=78.07 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=99205 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT hidden_object score=73.64 sendable=77.83 stage=COOLDOWN_BLOCKED quality=92.57 mvp=65.0 installs=14732 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT other score=85.41 sendable=77.38 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=63.51 installs=401955 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.39 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.15 installs=1840445 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=89.08 sendable=75.61 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=997645 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.53 sendable=75.06 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=290443 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 3
- giant_dominated: 12
- growth_by_one_app_too_high: 147
- low_demand: 125
- low_mvp_feasibility: 76
- low_score: 198
- severe_paid_spike: 126
- too_few_apps: 116
- top_app_too_dominant: 153
- unknown_pattern_blocker_active: 7
- weak_data_quality: 195
