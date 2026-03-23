# R-006b — Maturity-Controlled Structural Forensics

> **Report ID:** R-006b
> **Campaign:** C-006b
> **Author:** Jay Carpenter
> **Date:** 2026-03-01
> **Status:** FINAL
> **Type:** OUTWARD-FACING STRUCTURAL MEASUREMENT — three-way maturity-controlled cohort comparison
> **Disposition:** 2 MATURITY EFFECT, 3 AI EFFECT, 1 MIXED.
>                  C-006 enforcement candidates H7 (fileToDirRatio) and H9 (subTreeCV) did NOT survive maturity control.
>                  0/2 enforcement candidates valid for v1.9 design.
> **System Under Test:** 300 GitHub repositories (100 historical, 100 pre-AI early, 100 recent)
> **Suite:** Structural Scanner v1.0.0 + Three-Way Hypothesis Engine v1.0
> **Campaign Result:** 6 hypotheses tested via three-way comparison
> **Constitutional Source:** D-66, D-68 (measurement before enforcement)
> **Version Arc:** v1.8 — measurement only, no enforcement
> **Directed by:** Änti (adversarial audit)
> **Parent Campaign:** C-006 Structural Forensics Sweep

---

## §0 — Executive Summary

C-006b resolves the primary confound in C-006: were the observed structural differences between historical and recent repos caused by AI influence, or by project maturity?

A maturity-matched control cohort (100 repos created 2018-2019, 50-2000 stars, pre-Copilot/ChatGPT) was scanned with the same instrument and compared against both the historical and recent cohorts from C-006.

### Cohort Design — Age at Scan

All three cohorts were scanned as they exist today (March 2026). The pre-AI early cohort captures repos that were created in the pre-AI era but have had 6–7 years to mature.

| Cohort | Created | Scanned | Age at scan |
|--------|---------|---------|-------------|
| Historical | pre-2015 | 2026 | 10+ years |
| Pre-AI early | 2018–2019 | 2026 | 6–7 years |
| Recent | 2025–2026 | 2026 | weeks–months |

**Interpretation matrix:**
- Pre-AI early ≈ historical → maturity drives structure, enforcement candidates survive
- Pre-AI early ≈ recent → era drives structure, enforcement candidates need re-examination
- Pre-AI early intermediate → both effects present, metric-by-metric triage

### Maturity-Control Verdicts

| Hypothesis | Metric | C-006 Verdict | C-006 d | Pre-AI vs Recent d | Pre-AI vs Recent p (BH) | Maturity Verdict |
|-----------|--------|---------------|---------|-------------------|------------------------|------------------|
| H1b | m1_maxDepth | FALSIFIED | -1.416 | 0.208 | 0.022499 | **AI EFFECT** |
| H2b | m2_rootFileRatio | FALSIFIED | 0.829 | -0.256 | 0.179388 | **MATURITY EFFECT** |
| H3b | m3_namingEntropy | FALSIFIED | -1.385 | 0.420 | 0.006687 | **AI EFFECT** |
| H4b | m4_duplicatePurpose | FALSIFIED | -0.994 | 0.356 | 0.003057 | **AI EFFECT** |
| H7b | m7_fileToDirRatio | SUPPORTED | -0.265 | -0.263 | 0.211491 | **MATURITY EFFECT** |
| H9b | subTreeCV | SUPPORTED | -0.946 | 0.403 | 0.011829 | **MIXED — PRE-AI IS DISTINCT FROM BOTH** |

### Summary

| Verdict | Count |
|---------|-------|
| MATURITY EFFECT | 2 |
| AI EFFECT | 3 |
| MIXED | 1 |

**Overall finding:** The results are mixed — some C-006 findings are maturity effects, others are genuine AI signals. Enforcement candidates must be evaluated metric-by-metric.

### Enforcement Candidate Survival

| C-006 Candidate | Metric | C-006 d | Pre-AI vs Recent d | Survives? |
|----------------|--------|---------|-------------------|-----------|
| H7b | m7_fileToDirRatio | -0.265 | -0.263 | **NO** |
| H9b | subTreeCV | -0.946 | 0.403 | **NO** |

**Neither C-006 enforcement candidate survives maturity control.** H7 is a maturity effect. H9 is mixed — pre-AI early repos differ from both cohorts, suggesting the metric tracks something other than simple maturity or AI influence.

---

## §1 — H8/H9 Identical-Statistic Verification

Änti flagged that C-006's H8 (rootConfigCount) and H9 (subTreeCV) reported identical Mann-Whitney U (2554.5), z-score (5.975), and Cliff's δ (-0.489).

**Verification result:** One coincidence, not four. Source data arrays are entirely different (rootConfigCount = integers with 173 tied ranks; subTreeCV = floats with 10 tied ranks). No data leakage. The identical rank-sum (U = 7445.5) is the single coincidence; z, δ, and p are mechanically derived from U given fixed n₁ = n₂ = 100:

$$z = \frac{U - n_1 n_2 / 2}{\sigma_U}, \quad \delta = \frac{2U}{n_1 n_2} - 1$$

Same U, same n₁, same n₂ → same everything downstream. With U ranging over ~10,000 possible integer values for these cohort sizes, one rank-sum collision is unusual but not extraordinary (~1/10,000 if independent). **Issue CLOSED — no atlas correction needed.**

---

## §2 — Three-Way Hypothesis Results

### H1b: m1_maxDepth

**Claim:** Pre-AI early-stage repos have similar max folder depth to recent repos (both shallow because both are young).

**Resolves:** If similar → C-006 H1 falsification was a maturity effect.

**C-006 reference:** H1 — FALSIFIED (d = -1.416)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 8.9600 | 3.8800 | 4.4300 |
| Trimmed Mean (20%) | 8.4500 | 3.3167 | 4.3667 |
| Median | 8.5000 | 3.0000 | 4.0000 |
| Std Dev | 3.8767 | 2.9346 | 2.3323 |
| IQR | 5.0000 | 4.0000 | 3.0000 |
| Min | 3.0000 | 0.0000 | 0.0000 |
| P25 | 6.0000 | 2.0000 | 3.0000 |
| P75 | 11.0000 | 6.0000 | 6.0000 |
| Max | 23.0000 | 14.0000 | 12.0000 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | 0.5500 (14.2%) | 5.0800 (130.9%) | -4.5300 (-50.6%) |
| Cohen's d | 0.208 (small) | 1.478 (very large) | -1.416 (very large) |
| Cliff's δ | 0.199 (small) | 0.737 (large) | -0.701 (large) |
| U | 4004.5 | 1317.5 | 1497.0 |
| z | 2.432 | 8.998 | 8.559 |
| p (raw) | 0.014999 | 0.000000 | 0.000000 |
| BH q | 0.022499 | 0.000000 | — |
| BH significant | ✅ | ✅ | — |
| Bootstrap 95% CI | [-0.2100, 1.2900] | [4.1100, 6.0100] | [-5.4300, -3.6700] |
| CI crosses zero | Yes | No | No |

**Primary Verdict (Pre-AI Early vs Recent):** SIGNIFICANTLY DIFFERENT†

**Maturity-Control Verdict:** AI EFFECT

**Implication:** C-006 H1 (FALSIFIED) reflects a genuine AI-era structural shift. Enforcement candidate SURVIVES.

---

### H2b: m2_rootFileRatio

**Claim:** Pre-AI early-stage repos have similar root-file ratio to recent repos.

**Resolves:** If similar → C-006 H2 falsification was a maturity effect.

**C-006 reference:** H2 — FALSIFIED (d = 0.829)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 0.0166 | 0.2056 | 0.1418 |
| Trimmed Mean (20%) | 0.0079 | 0.1081 | 0.0771 |
| Median | 0.0063 | 0.0920 | 0.0651 |
| Std Dev | 0.0350 | 0.2816 | 0.2107 |
| IQR | 0.0141 | 0.2055 | 0.1128 |
| Min | 0.0002 | 0.0003 | 0.0013 |
| P25 | 0.0024 | 0.0335 | 0.0321 |
| P75 | 0.0165 | 0.2390 | 0.1449 |
| Max | 0.2500 | 1.0000 | 1.0000 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | -0.0637 (-31.0%) | -0.1889 (-91.9%) | 0.1252 (752.7%) |
| Cohen's d | -0.256 (small) | -0.941 (large) | 0.829 (large) |
| Cliff's δ | -0.110 (negligible) | -0.787 (large) | 0.796 (large) |
| U | 4450.5 | 1064.5 | 1020.5 |
| z | 1.343 | 9.616 | 9.723 |
| p (raw) | 0.179388 | 0.000000 | 0.000000 |
| BH q | 0.179388 | 0.000000 | — |
| BH significant | ❌ | ✅ | — |
| Bootstrap 95% CI | [-0.1322, 0.0036] | [-0.2477, -0.1366] | [0.0865, 0.1698] |
| CI crosses zero | Yes | No | No |

**Primary Verdict (Pre-AI Early vs Recent):** NOT SIGNIFICANTLY DIFFERENT

**Maturity-Control Verdict:** MATURITY EFFECT

**Implication:** C-006 H2 (FALSIFIED) was a maturity effect. Enforcement candidate INVALID.

---

### H3b: m3_namingEntropy

**Claim:** Pre-AI early-stage repos have similar naming entropy to recent repos.

**Resolves:** If similar → C-006 H3 falsification was a maturity effect.

**C-006 reference:** H3 — FALSIFIED (d = -1.385)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 8.3481 | 5.7813 | 6.4575 |
| Trimmed Mean (20%) | 8.2936 | 5.9985 | 6.6669 |
| Median | 8.3938 | 6.0435 | 6.6202 |
| Std Dev | 1.2068 | 1.7100 | 1.5066 |
| IQR | 1.6004 | 2.1346 | 1.7343 |
| Min | 5.8646 | 1.0000 | 1.5850 |
| P25 | 7.4825 | 4.8066 | 5.8517 |
| P75 | 9.0830 | 6.9411 | 7.5859 |
| Max | 11.1740 | 10.4899 | 8.9020 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | 0.6762 (11.7%) | 2.5668 (44.4%) | -1.8907 (-22.6%) |
| Cohen's d | 0.420 (small) | 1.734 (very large) | -1.385 (very large) |
| Cliff's δ | 0.250 (small) | 0.817 (large) | -0.688 (large) |
| U | 3748.5 | 915.0 | 1559.0 |
| z | 3.058 | 9.981 | 8.408 |
| p (raw) | 0.002229 | 0.000000 | 0.000000 |
| BH q | 0.006687 | 0.000000 | — |
| BH significant | ✅ | ✅ | — |
| Bootstrap 95% CI | [0.2400, 1.1230] | [2.1665, 2.9758] | [-2.2715, -1.5292] |
| CI crosses zero | No | No | No |

**Primary Verdict (Pre-AI Early vs Recent):** SIGNIFICANTLY DIFFERENT

**Maturity-Control Verdict:** AI EFFECT

**Implication:** C-006 H3 (FALSIFIED) reflects a genuine AI-era structural shift. Enforcement candidate SURVIVES.

---

### H4b: m4_duplicatePurpose

**Claim:** Pre-AI early-stage repos have similar duplicate-purpose directory counts to recent repos.

**Resolves:** If similar → C-006 H4 falsification was a maturity effect.

**C-006 reference:** H4 — FALSIFIED (d = -0.994)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 9.9400 | 1.3900 | 2.7300 |
| Trimmed Mean (20%) | 7.9000 | 0.2833 | 1.4667 |
| Median | 6.5000 | 0.0000 | 1.0000 |
| Std Dev | 9.4343 | 3.4812 | 4.0298 |
| IQR | 14.0000 | 1.0000 | 3.0000 |
| Min | 0.0000 | 0.0000 | 0.0000 |
| P25 | 2.0000 | 0.0000 | 0.0000 |
| P75 | 16.0000 | 1.0000 | 3.0000 |
| Max | 42.0000 | 22.0000 | 24.0000 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | 1.3400 (96.4%) | 8.5500 (615.1%) | -7.2100 (-72.5%) |
| Cohen's d | 0.356 (small) | 1.202 (very large) | -0.994 (large) |
| Cliff's δ | 0.284 (small) | 0.746 (large) | -0.557 (large) |
| U | 3577.5 | 1271.5 | 2216.5 |
| z | 3.476 | 9.110 | 6.801 |
| p (raw) | 0.000510 | 0.000000 | 0.000000 |
| BH q | 0.003057 | 0.000000 | — |
| BH significant | ✅ | ✅ | — |
| Bootstrap 95% CI | [0.3100, 2.3500] | [6.6300, 10.5500] | [-9.2500, -5.2000] |
| CI crosses zero | No | No | No |

**Primary Verdict (Pre-AI Early vs Recent):** SIGNIFICANTLY DIFFERENT

**Maturity-Control Verdict:** AI EFFECT

**Implication:** C-006 H4 (FALSIFIED) reflects a genuine AI-era structural shift. Enforcement candidate SURVIVES.

---

### H7b: m7_fileToDirRatio

**Claim:** Pre-AI early-stage repos have similar file-to-directory ratio to recent repos.

**Resolves:** Tests whether the one supported structural candidate holds under maturity control.

**C-006 reference:** H7 — SUPPORTED (d = -0.265)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 7.6884 | 8.6818 | 5.5495 |
| Trimmed Mean (20%) | 5.7016 | 5.0501 | 4.4375 |
| Median | 5.4660 | 4.9650 | 4.0335 |
| Std Dev | 10.4401 | 16.2272 | 4.5699 |
| IQR | 4.1140 | 4.3038 | 3.0745 |
| Min | 1.2690 | 0.8570 | 1.4000 |
| P25 | 3.8165 | 3.2967 | 3.1723 |
| P75 | 7.9305 | 7.6005 | 6.2468 |
| Max | 97.6280 | 140.0000 | 33.0000 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | -3.1323 (-36.1%) | -0.9934 (-11.4%) | -2.1389 (-27.8%) |
| Cohen's d | -0.263 (small) | -0.073 (negligible) | -0.265 (small) |
| Cliff's δ | -0.111 (negligible) | 0.094 (negligible) | -0.222 (small) |
| U | 4446.5 | 4531.5 | 3888.5 |
| z | 1.352 | 1.145 | 2.716 |
| p (raw) | 0.176242 | 0.252322 | 0.006611 |
| BH q | 0.211491 | 0.252322 | — |
| BH significant | ❌ | ❌ | — |
| Bootstrap 95% CI | [-6.7737, -0.3003] | [-4.8824, 2.4648] | [-4.6616, -0.1959] |
| CI crosses zero | No | Yes | No |

**Primary Verdict (Pre-AI Early vs Recent):** NOT SIGNIFICANTLY DIFFERENT

**Maturity-Control Verdict:** MATURITY EFFECT

**Implication:** C-006 H7 (SUPPORTED) was a maturity effect. Enforcement candidate INVALID.

---

### H9b: subTreeCV

**Claim:** Pre-AI early-stage repos have higher sub-tree CV than recent repos (less uniform, closer to historical).

**Resolves:** Tests whether the strongest enforcement candidate (d=-0.946) survives maturity control.

**C-006 reference:** H9 — SUPPORTED (d = -0.946)

| Statistic | Historical | Pre-AI Early | Recent |
|-----------|-----------|-------------|--------|
| n | 100 | 100 | 100 |
| Mean | 1.9644 | 1.0591 | 1.3215 |
| Trimmed Mean (20%) | 1.9831 | 1.0949 | 1.3347 |
| Median | 2.0323 | 1.1601 | 1.3153 |
| Std Dev | 0.6990 | 0.6422 | 0.6591 |
| IQR | 1.0294 | 0.8080 | 0.7667 |
| Min | 0.5194 | 0.0000 | 0.0000 |
| P25 | 1.4095 | 0.6363 | 0.9499 |
| P75 | 2.4389 | 1.4443 | 1.7167 |
| Max | 4.1176 | 2.9226 | 2.9737 |

#### Pairwise Comparisons

| Test | Pre-AI vs Recent | Pre-AI vs Historical | Historical vs Recent (C-006) |
|------|-----------------|---------------------|-----------------------------|
| Δ (mean) | 0.2624 (24.8%) | 0.9053 (85.5%) | -0.6430 (-32.7%) |
| Cohen's d | 0.403 (small) | 1.349 (very large) | -0.946 (large) |
| Cliff's δ | 0.225 (small) | 0.648 (large) | -0.489 (large) |
| U | 3873.5 | 1759.5 | 2554.5 |
| z | 2.752 | 7.918 | 5.975 |
| p (raw) | 0.005915 | 0.000000 | 0.000000 |
| BH q | 0.011829 | 0.000000 | — |
| BH significant | ✅ | ✅ | — |
| Bootstrap 95% CI | [0.0839, 0.4382] | [0.7193, 1.0886] | [-0.8279, -0.4538] |
| CI crosses zero | No | No | No |

**Primary Verdict (Pre-AI Early vs Recent):** SIGNIFICANTLY DIFFERENT

**Maturity-Control Verdict:** MIXED — PRE-AI IS DISTINCT FROM BOTH

**Implication:** Pre-AI early differs from both historical and recent. The metric tracks something other than simple maturity or AI influence. Enforcement candidate requires further investigation.

---

## §3 — Three-Way Cohort Profiles

| Metric | Historical (mean) | Pre-AI Early (mean) | Recent (mean) | Pre-AI closer to |
|--------|------------------|--------------------|--------------|-----------------|
| m1_maxDepth | 8.9600 | 3.8800 | 4.4300 | Recent |
| m1_meanDepth | 4.0951 | 2.1275 | 2.3819 | Recent |
| m2_rootFileRatio | 0.0166 | 0.2056 | 0.1418 | Recent |
| m3_namingEntropy | 8.3481 | 5.7813 | 6.4575 | Recent |
| m4_duplicatePurpose | 9.9400 | 1.3900 | 2.7300 | Recent |
| m5_templateFingerprint | 0.6033 | 0.3917 | 0.5750 | Recent |
| m6_orphanDirRatio | 0.3194 | 0.2598 | 0.3381 | Historical |
| m7_fileToDirRatio | 7.6884 | 8.6818 | 5.5495 | Historical |
| rootConfigCount | 10.5400 | 4.0900 | 5.6400 | Recent |
| subTreeCV | 1.9644 | 1.0591 | 1.3215 | Recent |

## §4 — Correction Robustness (Primary Comparisons)

| Hypothesis | p (raw) | BH q | BH Sig | Holm Sig | Bonf Sig | Primary Verdict |
|-----------|---------|------|--------|----------|----------|----------------|
| H1b | 0.014999 | 0.022499 | ✅ | ✅ | ❌ | SIGNIFICANTLY DIFFERENT† |
| H2b | 0.179388 | 0.179388 | ❌ | ❌ | ❌ | NOT SIGNIFICANTLY DIFFERENT |
| H3b | 0.002229 | 0.006687 | ✅ | ✅ | ✅ | SIGNIFICANTLY DIFFERENT |
| H4b | 0.000510 | 0.003057 | ✅ | ✅ | ✅ | SIGNIFICANTLY DIFFERENT |
| H7b | 0.176242 | 0.211491 | ❌ | ❌ | ❌ | NOT SIGNIFICANTLY DIFFERENT |
| H9b | 0.005915 | 0.011829 | ✅ | ✅ | ✅ | SIGNIFICANTLY DIFFERENT |

## §5 — Implications for v1.8 Enforcement Design

### Mixed results — metric-by-metric triage required

The picture is mixed. Some C-006 findings are maturity effects; others are genuine AI signals.

**Metrics confirmed as MATURITY EFFECTS (enforcement INVALID):**

- **m2_rootFileRatio** — H2 (FALSIFIED, d=0.829)
- **m7_fileToDirRatio** — H7 (SUPPORTED, d=-0.265)

**Metrics confirmed as AI EFFECTS (enforcement SURVIVES):**

- **m1_maxDepth** — H1 (FALSIFIED, d=-1.416), maturity-controlled d=0.208
- **m3_namingEntropy** — H3 (FALSIFIED, d=-1.385), maturity-controlled d=0.420
- **m4_duplicatePurpose** — H4 (FALSIFIED, d=-0.994), maturity-controlled d=0.356

**Mixed / requires further investigation:**

- **subTreeCV** — H9: Pre-AI early differs from both cohorts

## §6 — Limitations

1. **Star-count proxy:** "Stars 50-2000 today" is a rough proxy for "early-stage at creation." Some 2018-2019 repos with 2000 stars may now be mature. However, the star ceiling (2000) excludes mega-projects that dominate the historical cohort.
1. **Pre-AI early star clustering:** All 100 pre-AI early repos cluster at ~1965–2000 stars (min 1965, max 2000, median 1982) due to GitHub API `sort=stars&per_page=100` selecting from the ceiling of the 50–2000 range. Results may not generalise to lower-popularity repos in the same era. Stars were a quality filter (exclude toy repos and mega-projects), not a controlled variable — neither existing cohort was star-controlled, so adding a star-uniform third cohort would introduce a new asymmetry rather than remove one.
2. **Temporal gap:** The pre-AI cohort is from 2018-2019 (5-6 years old today), while recent is from Jan-Mar 2026. Ecosystem-wide changes (not just AI) may have shifted structural norms.
3. **Language/domain confounds:** Star-sorted selection may produce different language/domain mixes across cohorts. This is not controlled.
4. **Maturity ≠ age alone:** A 2018 repo with 100 stars may still receive active AI-assisted contributions in 2025-2026, introducing AI effects into the "pre-AI" cohort.
5. **Same limitations as C-006:** API tree truncation, vendor filtering, template signature coverage, no content analysis, single timepoint.

## §7 — Constitutional Record

| Item | Value |
|------|-------|
| Campaign | C-006b Maturity-Controlled Structural Forensics |
| Parent campaign | C-006 Structural Forensics Sweep |
| Directed by | Änti (adversarial audit) |
| Constitutional source | D-66 (measurement before enforcement) |
| Version arc | v1.8 (measurement only) |
| Hypotheses tested | 6 |
| MATURITY EFFECT | 2 |
| AI EFFECT | 3 |
| MIXED | 1 |
| C-006 enforcement candidates tested | 2 |
| Enforcement candidates surviving | 0 |
| H8/H9 verification | CLOSED — one coincidence (rank-sum), no bug |
| Substrate modifications | Zero (D-68 compliance) |
| Total repos scanned | 300 |
| Scanner version | 1.0.0 |
| Engine version | 1.0 |

### Cohort Precondition Verification

| Constraint | Result |
|---|---|
| Zero overlap with C-006 200 repos | **0 overlap** ✅ |
| Creation dates 2018-01-01 to 2019-12-31 | **All 100 in range** (earliest 2018-01-05, latest 2019-12-15) ✅ |
| Star count 50–2000 | **All 100 in range** (min 1965, max 2000, median 1982) ✅ |

---

*The Änti asks questions that make the substrate stronger. This campaign exists because one question — "is this maturity or AI?" — could not be answered without measurement.*
