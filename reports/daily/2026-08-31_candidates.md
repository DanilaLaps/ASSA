# Daily Candidates - 2026-08-31

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 114
- NEAR_MISS: 100
- REJECT: 218
- SINGLE_APP_WATCH: 11
- WATCH: 151

## Alert Stage Counts
- COOLDOWN_BLOCKED: 10
- NONE: 480
- QUALIFIED_CANDIDATE_ONLY: 103
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 78
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Top Candidates
- ALERT sort_puzzle score=80.05 sendable=83.34 stage=SENDABLE_ALERT quality=95.0 mvp=85.0 installs=37099 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=unknown_coverage
- ALERT sort_puzzle score=79.84 sendable=83.16 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=45695 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT sort_puzzle score=78.51 sendable=82.62 stage=QUALIFIED_CANDIDATE_ONLY quality=95.0 mvp=85.0 installs=16807 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=per_niche_limit_blocked risks=unknown_coverage
- ALERT tile_match score=89.32 sendable=82.55 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=940067 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=88.35 sendable=81.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=76.97 installs=1588437 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=83.21 sendable=81.2 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=97048 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=88.24 sendable=80.59 stage=COOLDOWN_BLOCKED quality=88.0 mvp=77.96 installs=1755026 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=89.75 sendable=80.56 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=877965 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=one_app_growth_penalty risks=unknown_coverage
- ALERT hidden_object score=86.02 sendable=80.44 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=162119 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT arrow_puzzle score=86.86 sendable=80.39 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1513260 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.04 sendable=80.28 stage=COOLDOWN_BLOCKED quality=88.0 mvp=73.9 installs=3833068 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=81.39 sendable=80.26 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=46664 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT block_puzzle score=86.97 sendable=80.04 stage=COOLDOWN_BLOCKED quality=88.0 mvp=71.99 installs=1230114 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.48 sendable=79.87 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=680058 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=89.94 sendable=79.73 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=1469003 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=88.54 sendable=79.44 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=302445 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=86.77 sendable=78.36 stage=QUALIFIED_CANDIDATE_ONLY quality=87.92 mvp=69.12 installs=322055 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT coloring score=82.78 sendable=77.7 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=69.85 installs=197607 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=77.3 sendable=77.64 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=40441 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=82.6 sendable=77.55 stage=QUALIFIED_CANDIDATE_ONLY quality=86.17 mvp=85.0 installs=36126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 10
- giant_dominated: 8
- growth_by_one_app_too_high: 177
- low_demand: 153
- low_mvp_feasibility: 74
- low_score: 218
- severe_paid_spike: 156
- too_few_apps: 133
- top_app_too_dominant: 176
- unknown_pattern_blocker_active: 12
- weak_data_quality: 216
