# Daily Candidates - 2026-07-14

Source: single AppStoreSpy query without country/language filters.

## Status Counts
- ALERT: 123
- NEAR_MISS: 98
- REJECT: 199
- SINGLE_APP_WATCH: 7
- WATCH: 179

## Alert Stage Counts
- COOLDOWN_BLOCKED: 10
- NONE: 483
- QUALIFIED_CANDIDATE_ONLY: 112
- SENDABLE_ALERT: 1

## Coverage
- unknown_coverage

## Unknown Diagnostics
- mixed_unknown_cluster: 76
- unknown_dominant_cluster: 72
- unknown_pattern_blocker_active: 72

## Top Candidates
- ALERT coloring score=89.55 sendable=89.49 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=1784778 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT sort_puzzle score=78.77 sendable=83.99 stage=COOLDOWN_BLOCKED quality=95.0 mvp=85.0 installs=47490 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=unknown_coverage
- ALERT block_puzzle score=89.13 sendable=82.45 stage=SENDABLE_ALERT quality=88.0 mvp=85.0 installs=1318275 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=none risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=89.85 sendable=82.43 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1179238 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=86.37 sendable=82.1 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=540216 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=84.29 sendable=81.95 stage=COOLDOWN_BLOCKED quality=95.0 mvp=65.0 installs=520492 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=unknown_coverage
- ALERT word_puzzle score=85.87 sendable=81.77 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=194584 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_exact_dedupe_key risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.41 sendable=80.67 stage=COOLDOWN_BLOCKED quality=88.0 mvp=72.38 installs=5836477 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT other score=88.74 sendable=80.66 stage=COOLDOWN_BLOCKED quality=88.0 mvp=75.2 installs=2675318 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT arrow_puzzle score=87.0 sendable=80.48 stage=COOLDOWN_BLOCKED quality=88.0 mvp=79.56 installs=1469337 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=87.83 sendable=80.19 stage=COOLDOWN_BLOCKED quality=88.0 mvp=85.0 installs=1264870 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=cooldown_normalized_niche risks=classifier_low_confidence, unknown_coverage
- ALERT hidden_object score=77.13 sendable=79.64 stage=QUALIFIED_CANDIDATE_ONLY quality=94.26 mvp=65.0 installs=62677 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=unknown_coverage
- ALERT sort_puzzle score=82.74 sendable=79.28 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=83.65 installs=147855 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT tile_match score=83.36 sendable=78.79 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.62 installs=151665 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT block_puzzle score=78.32 sendable=77.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=71.5 installs=134126 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=74.32 sendable=77.25 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=85.0 installs=23743 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=82.58 sendable=77.04 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=65.0 installs=451463 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT other score=87.15 sendable=76.96 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=72.53 installs=1712520 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=audience_uncertain, classifier_low_confidence, unknown_coverage
- ALERT runner score=85.64 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=88.0 mvp=66.39 installs=2869592 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage
- ALERT sort_puzzle score=76.7 sendable=76.84 stage=QUALIFIED_CANDIDATE_ONLY quality=86.43 mvp=85.0 installs=34247 unknown_app_share=0.0 unknown_installs_share=0.0 first_blocking=below_sendable_alert_score risks=classifier_low_confidence, unknown_coverage

## Rejected Reason Distribution
- classifier_low_confidence: 5
- giant_dominated: 16
- growth_by_one_app_too_high: 171
- low_demand: 106
- low_mvp_feasibility: 68
- low_score: 199
- severe_paid_spike: 148
- too_few_apps: 133
- top_app_too_dominant: 182
- unknown_pattern_blocker_active: 8
- weak_data_quality: 198
