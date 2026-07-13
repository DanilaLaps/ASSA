# Daily Candidates - 2026-07-13

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 123
- NEAR_MISS: 96
- REJECT: 195
- SINGLE_APP_WATCH: 6
- WATCH: 175

## Alert Stage Counts
- COOLDOWN_BLOCKED: 6
- NONE: 472
- QUALIFIED_CANDIDATE_ONLY: 115
- SENDABLE_ALERT: 2

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Top Candidates
- ALERT coloring score=89.46 sendable=89.45 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=2112575 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT sort_puzzle score=78.74 sendable=83.98 stage=SENDABLE_ALERT quality=95.0 mvp=85.0 installs=49327 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=unknown_coverage
- ALERT sort_puzzle score=78.82 sendable=83.93 stage=QUALIFIED_CANDIDATE_ONLY quality=94.42 mvp=85.0 installs=38161 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT tile_match score=90.44 sendable=83.69 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1445874 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.19 sendable=82.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1361486 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=85.87 sendable=81.9 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=513746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.54 sendable=81.52 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=493572 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT word_puzzle score=85.46 sendable=81.4 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=207706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.81 sendable=81.3 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1000665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.41 sendable=80.68 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.87 installs=1736335 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=87.59 sendable=80.56 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=78.22 installs=2576516 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=duplicate_market_signal risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.18 sendable=80.5 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.32 installs=6672106 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=81.51 sendable=79.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.41 installs=156383 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=85.19 sendable=78.71 stage=QUALIFIED_CANDIDATE_ONLY quality=87.54 mvp=67.73 installs=724997 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sandbox score=83.0 sendable=78.19 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.83 installs=147312 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=72.63 sendable=78.14 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=37606 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT arrow_puzzle score=89.14 sendable=77.94 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=2649923 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage, weak_monetization_signal
- ALERT block_puzzle score=79.36 sendable=77.67 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=146706 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=75.18 sendable=77.6 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=29392 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=76.8 sendable=77.43 stage=QUALIFIED_CANDIDATE_ONLY quality=93.17 mvp=65.0 installs=55746 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 6
- giant_dominated: 16
- growth_by_one_app_too_high: 169
- low_demand: 110
- low_mvp_feasibility: 68
- low_score: 195
- severe_paid_spike: 151
- too_few_apps: 130
- top_app_too_dominant: 177
- unknown_pattern_blocker_active: 7
- weak_data_quality: 193
