# Daily Candidates - 2026-08-11

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 128
- NEAR_MISS: 117
- REJECT: 219
- SINGLE_APP_WATCH: 2
- WATCH: 158

## Alert Stage Counts
- COOLDOWN_BLOCKED: 8
- NONE: 496
- QUALIFIED_CANDIDATE_ONLY: 118
- SENDABLE_ALERT: 2

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 77
- unknown_dominant_cluster: 68
- unknown_pattern_blocker_active: 68

## Top Candidates
- ALERT coloring score=90.95 sendable=84.67 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1460809 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=79.89 sendable=83.61 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=64483 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT block_puzzle score=90.06 sendable=83.55 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=1651464 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.43 sendable=82.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1223226 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=85.86 sendable=82.04 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=225657 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=88.44 sendable=81.49 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1433145 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.93 sendable=81.46 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=1954757 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.83 sendable=81.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.33 installs=2089739 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=88.02 sendable=80.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=79.36 installs=1330255 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.66 sendable=80.78 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=487561 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.52 sendable=80.47 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=577532 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.02 sendable=80.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.81 installs=1746204 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.36 sendable=80.23 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=22184 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=87.35 sendable=80.17 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.34 installs=1848197 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=84.55 sendable=80.17 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=106572 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.84 sendable=79.98 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.75 installs=1421646 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.56 sendable=79.83 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=94543 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.73 sendable=79.81 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=84.79 installs=1039507 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=84.76 sendable=79.74 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=75.05 installs=168062 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=78.94 sendable=79.01 stage=QUALIFIED_CANDIDATE_ONLY quality=92.89 mvp=65.0 installs=64865 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 9
- giant_dominated: 16
- growth_by_one_app_too_high: 187
- low_demand: 149
- low_mvp_feasibility: 78
- low_score: 219
- severe_paid_spike: 174
- too_few_apps: 161
- top_app_too_dominant: 196
- unknown_pattern_blocker_active: 11
- weak_data_quality: 218
