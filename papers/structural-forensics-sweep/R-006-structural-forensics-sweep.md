# R-006 — Structural Forensics Sweep

> **Report ID:** R-006
> **Campaign:** C-006
> **Author:** Jay Carpenter
> **Date:** 2026-03-01
> **Status:** FINAL
> **Type:** OUTWARD-FACING STRUCTURAL MEASUREMENT — cross-era cohort comparison
> **Disposition:** CSDI = 0.674 (large). 3 SUPPORTED, 5 FALSIFIED, 1 DIRECTIONAL ONLY, 1 NOT SUPPORTED.
>                  AI-era repos are structurally simpler and flatter, not more complex.
>                  3 enforcement candidates extracted for v1.9 design phase.
> **System Under Test:** 200 GitHub repositories (100 historical, 100 recent)
> **Suite:** Structural Scanner v1.0.0 + Hypothesis Engine v1.0
> **Campaign Result:** 10 hypotheses tested, CSDI = 0.674 (CI [0.613, 0.705])
> **Constitutional Source:** D-68, D-69 (translation_0011)
> **Version Arc:** v1.8 — measurement only, no enforcement

---

## §0 — Executive Summary

The C-006 Structural Forensics Sweep measured 7 structural metrics + 2 supplementary metrics across 200 repositories, testing 10 falsifiable hypotheses about structural divergence between pre-AI-era (historical) and AI-era (recent) codebases.

**Composite Structural Drift Index (CSDI): 0.674** (large)
Bootstrap 95% CI: [0.613, 0.705]

Moderate structural divergence between eras.

### Verdict Summary (BH-FDR corrected, α = 0.05)

| Verdict | Count |
|---------|-------|
| SUPPORTED | 3 |
| DIRECTIONAL ONLY | 1 |
| FALSIFIED | 5 |
| NOT SUPPORTED | 1 |

### Top Effects by |Cohen's d|

| Rank | Hypothesis | Metric | Cohen's d | Cliff's δ | BH Verdict |
|------|-----------|--------|-----------|-----------|------------|
| 1 | H1 | m1_maxDepth | -1.416 (very large) | -0.701 (large) | FALSIFIED |
| 2 | H3 | m3_namingEntropy | -1.385 (very large) | -0.688 (large) | FALSIFIED |
| 3 | H4 | m4_duplicatePurpose | -0.994 (large) | -0.557 (large) | FALSIFIED |
| 4 | H9 | subTreeCV | -0.946 (large) | -0.489 (large) | SUPPORTED |
| 5 | H8 | rootConfigCount | -0.858 (large) | -0.489 (large) | FALSIFIED |

---

## §1 — Methodology

### Instrument

SECS Structural Scanner v1.0.0 uses the GitHub Trees API (`GET /repos/{owner}/{repo}/git/trees/{branch}?recursive=1`) to retrieve the complete file tree for each repository in a single API call. No repository content is cloned or read — only tree topology (file paths, directory structure, entry types) is analysed.

**Filtering:** Entries under vendor directories (`node_modules`, `.git`, `vendor`, `dist`, `build`, etc.) are excluded from all metrics to measure authored structure, not dependency artifacts.

### Metrics

| # | Metric | Definition | Drift Pattern |
|---|--------|-----------|---------------|
| M1 | Max Folder Depth | Maximum nesting depth of any file/directory | Structural sprawl |
| M2 | Root File Ratio | Files at root ÷ total files | Config accumulation |
| M3 | Naming Entropy | Shannon entropy of name tokens (split on separators + camelCase) | Naming inconsistency |
| M4 | Duplicate-Purpose Dirs | Count of directories with semantically overlapping roles | Role confusion |
| M5 | Template Fingerprint | Best match against 15 scaffolding directory signatures (0–1) | Template masquerade |
| M6 | Orphan Dir Ratio | Leaf directories with ≤1 file ÷ total leaf directories | Dead weight |
| M7 | File-to-Dir Ratio | Total files ÷ total directories | Structural density |
| — | Root Config Count | Count of config/dotfiles at root | Config proliferation |
| — | Sub-tree CV | Coefficient of variation of top-level subdirectory file counts | Structural homogeneity |

### Statistical Tests

All hypotheses tested with:
- **Mann-Whitney U** (two-tailed, normal approximation) — non-parametric rank-sum test
- **Cohen's d** (pooled SD) — parametric effect size
- **Cliff's δ** (dominance probability) — non-parametric effect size, robust to skew
- **Bootstrap 95% CI** (10,000 iterations) — confidence interval for mean difference
- **BH-FDR** (Benjamini-Hochberg) — primary significance criterion (α = 0.05)
- **Holm-Bonferroni** — step-down FWER control (comparison)
- **Bonferroni** — conservative FWER control (comparison)

### Verdict Criteria

| Verdict | Requirements |
|---------|-------------|
| SUPPORTED | Direction matches + BH-significant + |d| ≥ 0.2 + CI excludes zero |
| SUPPORTED† | As SUPPORTED but bootstrap CI crosses zero |
| WEAKLY SUPPORTED | Direction matches + BH-significant + |d| < 0.2 |
| DIRECTIONAL ONLY | Direction matches but not BH-significant |
| FALSIFIED | Opposite direction + BH-significant |
| NOT SUPPORTED | No significant directional match |

---

## §2 — Hypothesis Results

### H1: m1_maxDepth

**Claim:** Recent repos have deeper maximum directory nesting than historical repos (structural sprawl).

**Drift Pattern:** Structural sprawl — AI tendency to create deep, sparse hierarchies

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 8.9600 | 4.4300 |
| Trimmed Mean (20%) | 8.4500 | 4.3667 |
| Median | 8.5000 | 4.0000 |
| Std Dev | 3.8767 | 2.3323 |
| IQR | 5.0000 | 3.0000 |
| Skewness | 0.8408 | 0.4975 |
| Min | 3.0000 | 0.0000 |
| P25 | 6.0000 | 3.0000 |
| P75 | 11.0000 | 6.0000 |
| P95 | 15.0500 | 8.0000 |
| Max | 23.0000 | 12.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | lower |
| Δ (mean) | -4.5300 (-50.6%) |
| Δ (trimmed) | -4.0833 |
| Mann-Whitney U | 1497.0 |
| z-score | 8.559 |
| p (raw) | 0.000000 |
| Cohen's d | -1.416 (very large) |
| Cliff's δ | -0.701 (large) |
| Rank-biserial r | 0.701 |
| Bootstrap 95% CI | [-5.4300, -3.6700] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): FALSIFIED**

**Substrate Implication:** Directory depth limits become candidate enforcement constraints in v1.9.

---

### H2: m2_rootFileRatio

**Claim:** Recent repos have a lower root-level file ratio (files pushed into nested directories).

**Drift Pattern:** Configuration accumulation — AI tendency to over-organise into sub-directories

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 0.0166 | 0.1418 |
| Trimmed Mean (20%) | 0.0079 | 0.0771 |
| Median | 0.0063 | 0.0651 |
| Std Dev | 0.0350 | 0.2107 |
| IQR | 0.0141 | 0.1128 |
| Skewness | 4.8599 | 2.8837 |
| Min | 0.0002 | 0.0013 |
| P25 | 0.0024 | 0.0321 |
| P75 | 0.0165 | 0.1449 |
| P95 | 0.0575 | 0.5125 |
| Max | 0.2500 | 1.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | lower |
| Actual Direction | higher |
| Δ (mean) | 0.1252 (752.7%) |
| Δ (trimmed) | 0.0692 |
| Mann-Whitney U | 1020.5 |
| z-score | 9.723 |
| p (raw) | 0.000000 |
| Cohen's d | 0.829 (large) |
| Cliff's δ | 0.796 (large) |
| Rank-biserial r | 0.796 |
| Bootstrap 95% CI | [0.0863, 0.1685] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): FALSIFIED**

**Substrate Implication:** Root-level ratio thresholds inform envelope defaults.

---

### H3: m3_namingEntropy

**Claim:** Recent repos exhibit higher naming entropy (more diverse, less conventionalised token vocabulary).

**Drift Pattern:** Naming inconsistency — AI tendency toward high-entropy, low-convention naming

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 8.3481 | 6.4575 |
| Trimmed Mean (20%) | 8.2936 | 6.6669 |
| Median | 8.3938 | 6.6202 |
| Std Dev | 1.2068 | 1.5066 |
| IQR | 1.6004 | 1.7343 |
| Skewness | 0.2195 | -1.1026 |
| Min | 5.8646 | 1.5850 |
| P25 | 7.4825 | 5.8517 |
| P75 | 9.0830 | 7.5859 |
| P95 | 10.5220 | 8.5198 |
| Max | 11.1740 | 8.9020 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | lower |
| Δ (mean) | -1.8907 (-22.6%) |
| Δ (trimmed) | -1.6267 |
| Mann-Whitney U | 1559.0 |
| z-score | 8.408 |
| p (raw) | 0.000000 |
| Cohen's d | -1.385 (very large) |
| Cliff's δ | -0.688 (large) |
| Rank-biserial r | 0.688 |
| Bootstrap 95% CI | [-2.2817, -1.5168] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): FALSIFIED**

**Substrate Implication:** Naming entropy thresholds become naming invariant candidates.

---

### H4: m4_duplicatePurpose

**Claim:** Recent repos contain more duplicate-purpose directories (overlapping functional roles).

**Drift Pattern:** Role confusion — AI tendency to create overlapping structural categories

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 9.9400 | 2.7300 |
| Trimmed Mean (20%) | 7.9000 | 1.4667 |
| Median | 6.5000 | 1.0000 |
| Std Dev | 9.4343 | 4.0298 |
| IQR | 14.0000 | 3.0000 |
| Skewness | 1.0775 | 2.4720 |
| Min | 0.0000 | 0.0000 |
| P25 | 2.0000 | 0.0000 |
| P75 | 16.0000 | 3.0000 |
| P95 | 27.0000 | 11.0500 |
| Max | 42.0000 | 24.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | lower |
| Δ (mean) | -7.2100 (-72.5%) |
| Δ (trimmed) | -6.4333 |
| Mann-Whitney U | 2216.5 |
| z-score | 6.801 |
| p (raw) | 0.000000 |
| Cohen's d | -0.994 (large) |
| Cliff's δ | -0.557 (large) |
| Rank-biserial r | 0.557 |
| Bootstrap 95% CI | [-9.2300, -5.3000] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): FALSIFIED**

**Substrate Implication:** Directory role uniqueness becomes an enforcement constraint.

---

### H5: m5_templateFingerprint

**Claim:** Recent repos have higher template fingerprint scores (more scaffold-derived structure).

**Drift Pattern:** Template masquerade — scaffolding structure masquerading as authored architecture

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 0.6033 | 0.5750 |
| Trimmed Mean (20%) | 0.6722 | 0.6250 |
| Median | 1.0000 | 0.5000 |
| Std Dev | 0.4405 | 0.4441 |
| IQR | 1.0000 | 1.0000 |
| Skewness | -0.4154 | -0.2882 |
| Min | 0.0000 | 0.0000 |
| P25 | 0.0000 | 0.0000 |
| P75 | 1.0000 | 1.0000 |
| P95 | 1.0000 | 1.0000 |
| Max | 1.0000 | 1.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | lower |
| Δ (mean) | -0.0283 (-4.7%) |
| Δ (trimmed) | -0.0472 |
| Mann-Whitney U | 4827.5 |
| z-score | 0.421 |
| p (raw) | 0.673401 |
| Cohen's d | -0.064 (negligible) |
| Cliff's δ | -0.035 (negligible) |
| Rank-biserial r | 0.034 |
| Bootstrap 95% CI | [-0.1517, 0.0950] |
| CI crosses zero | Yes |
| BH q-value | 0.757576 |
| BH significant | No |
| Holm significant | No |
| Bonferroni significant | No |

**Verdict (BH-FDR): NOT SUPPORTED**

**Substrate Implication:** Template detection fingerprints feed into Layer 2 semantic enforcement.

---

### H6: m6_orphanDirRatio

**Claim:** Recent repos have more orphan directories (leaf dirs with 0-1 files, sparse hierarchy).

**Drift Pattern:** Dead weight — AI tendency to generate directories that exist but serve no purpose

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 0.3194 | 0.3381 |
| Trimmed Mean (20%) | 0.3002 | 0.3214 |
| Median | 0.3047 | 0.2982 |
| Std Dev | 0.1752 | 0.2360 |
| IQR | 0.2405 | 0.3182 |
| Skewness | 0.6987 | 0.4296 |
| Min | 0.0000 | 0.0000 |
| P25 | 0.1793 | 0.1818 |
| P75 | 0.4198 | 0.5000 |
| P95 | 0.6463 | 0.7479 |
| Max | 0.8381 | 0.9128 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | higher |
| Δ (mean) | 0.0187 (5.9%) |
| Δ (trimmed) | 0.0212 |
| Mann-Whitney U | 4858.5 |
| z-score | 0.346 |
| p (raw) | 0.729538 |
| Cohen's d | 0.090 (negligible) |
| Cliff's δ | 0.028 (negligible) |
| Rank-biserial r | 0.028 |
| Bootstrap 95% CI | [-0.0386, 0.0775] |
| CI crosses zero | Yes |
| BH q-value | 0.729538 |
| BH significant | No |
| Holm significant | No |
| Bonferroni significant | No |

**Verdict (BH-FDR): DIRECTIONAL ONLY**

**Substrate Implication:** Minimum directory density becomes a structural constraint.

---

### H7: m7_fileToDirRatio

**Claim:** Recent repos have lower file-to-directory ratios (more directories per file, structural sprawl).

**Drift Pattern:** Structural sprawl — low-density directory trees

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 7.6884 | 5.5495 |
| Trimmed Mean (20%) | 5.7016 | 4.4375 |
| Median | 5.4660 | 4.0335 |
| Std Dev | 10.4401 | 4.5699 |
| IQR | 4.1140 | 3.0745 |
| Skewness | 6.8834 | 3.5029 |
| Min | 1.2690 | 1.4000 |
| P25 | 3.8165 | 3.1723 |
| P75 | 7.9305 | 6.2468 |
| P95 | 18.1691 | 13.0333 |
| Max | 97.6280 | 33.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | lower |
| Actual Direction | lower |
| Δ (mean) | -2.1389 (-27.8%) |
| Δ (trimmed) | -1.2641 |
| Mann-Whitney U | 3888.5 |
| z-score | 2.716 |
| p (raw) | 0.006611 |
| Cohen's d | -0.265 (small) |
| Cliff's δ | -0.222 (small) |
| Rank-biserial r | 0.222 |
| Bootstrap 95% CI | [-4.5716, -0.1879] |
| CI crosses zero | No |
| BH q-value | 0.008500 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | No |

**Verdict (BH-FDR): SUPPORTED**

**Substrate Implication:** Minimum density thresholds inform structural enforcement.

---

### H8: rootConfigCount

**Claim:** Recent repos have more configuration files at root level (config proliferation).

**Drift Pattern:** Configuration accumulation — AI tendency to proliferate root-level config

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 10.5400 | 5.6400 |
| Trimmed Mean (20%) | 9.1500 | 5.2000 |
| Median | 8.5000 | 5.0000 |
| Std Dev | 6.8526 | 4.2723 |
| IQR | 6.0000 | 6.0000 |
| Skewness | 1.9238 | 0.7931 |
| Min | 0.0000 | 0.0000 |
| P25 | 6.0000 | 2.0000 |
| P75 | 12.0000 | 8.0000 |
| P95 | 23.3000 | 14.0000 |
| Max | 40.0000 | 20.0000 |

| Test | Value |
|------|-------|
| Predicted Direction | higher |
| Actual Direction | lower |
| Δ (mean) | -4.9000 (-46.5%) |
| Δ (trimmed) | -3.9500 |
| Mann-Whitney U | 2554.5 |
| z-score | 5.975 |
| p (raw) | 0.000000 |
| Cohen's d | -0.858 (large) |
| Cliff's δ | -0.489 (large) |
| Rank-biserial r | 0.489 |
| Bootstrap 95% CI | [-6.5400, -3.3400] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): FALSIFIED**

**Substrate Implication:** Config proliferation becomes a drift signature for Layer 3 behavioural enforcement.

---

### H9: subTreeCV

**Claim:** Recent repos have lower sub-tree size variance (AI produces more uniform directory structures).

**Drift Pattern:** Template uniformity — AI tendency to replicate directory patterns

| Statistic | Historical | Recent |
|-----------|-----------|--------|
| n | 100 | 100 |
| Mean | 1.9644 | 1.3215 |
| Trimmed Mean (20%) | 1.9831 | 1.3347 |
| Median | 2.0323 | 1.3153 |
| Std Dev | 0.6990 | 0.6591 |
| IQR | 1.0294 | 0.7667 |
| Skewness | 0.1178 | -0.1150 |
| Min | 0.5194 | 0.0000 |
| P25 | 1.4095 | 0.9499 |
| P75 | 2.4389 | 1.7167 |
| P95 | 2.9505 | 2.3898 |
| Max | 4.1176 | 2.9737 |

| Test | Value |
|------|-------|
| Predicted Direction | lower |
| Actual Direction | lower |
| Δ (mean) | -0.6430 (-32.7%) |
| Δ (trimmed) | -0.6485 |
| Mann-Whitney U | 2554.5 |
| z-score | 5.975 |
| p (raw) | 0.000000 |
| Cohen's d | -0.946 (large) |
| Cliff's δ | -0.489 (large) |
| Rank-biserial r | 0.489 |
| Bootstrap 95% CI | [-0.8307, -0.4552] |
| CI crosses zero | No |
| BH q-value | 0.000000 |
| BH significant | Yes |
| Holm significant | Yes |
| Bonferroni significant | Yes |

**Verdict (BH-FDR): SUPPORTED**

**Substrate Implication:** Structural repetition detection feeds into Layer 3 behavioural enforcement.

---

### H10: Composite Structural Drift Index

**Claim:** A composite of all structural metrics produces a discriminative index (CSDI > 0.5) separating AI-era from pre-AI-era repos.

**CSDI = 0.674** (raw: 0.818, large)

Bootstrap 95% CI: [0.613, 0.705]

**Verdict: SUPPORTED**

| Category | RMS Effect | Weight | Weighted |
|----------|-----------|--------|----------|
| Topology | 0.949 | 0.30 | 0.2846 |
| Naming | 1.385 | 0.15 | 0.2078 |
| Role Structure | 0.994 | 0.10 | 0.0994 |
| Templates | 0.064 | 0.10 | 0.0064 |
| Density | 0.265 | 0.15 | 0.0398 |
| Configuration | 0.858 | 0.10 | 0.0858 |
| Homogeneity | 0.946 | 0.10 | 0.0946 |

**Interpretation:** Moderate structural divergence between eras.

**Substrate Implication:** CSDI becomes the structural analogue of the DESI for enforcement priority ranking.

---

## §3 — Drift Vectors

| Category | RMS Effect | Magnitude | Direction | Significant Fraction |
|----------|-----------|-----------|-----------|---------------------|
| Topology | 0.949 | large | increasing | 67% |
| Naming | 1.385 | very large | decreasing | 100% |
| Role Structure | 0.994 | large | decreasing | 100% |
| Templates | 0.064 | negligible | decreasing | 0% |
| Density | 0.265 | small | decreasing | 100% |
| Configuration | 0.858 | large | decreasing | 100% |
| Homogeneity | 0.946 | large | decreasing | 100% |

## §4 — Correction Robustness

| Hypothesis | p (raw) | BH q | BH Sig | Holm Sig | Bonf Sig | BH Verdict |
|-----------|---------|------|--------|----------|----------|------------|
| H1 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | FALSIFIED |
| H2 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | FALSIFIED |
| H3 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | FALSIFIED |
| H4 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | FALSIFIED |
| H5 | 0.673401 | 0.757576 | ❌ | ❌ | ❌ | NOT SUPPORTED |
| H6 | 0.729538 | 0.729538 | ❌ | ❌ | ❌ | DIRECTIONAL ONLY |
| H7 | 0.006611 | 0.008500 | ✅ | ✅ | ❌ | SUPPORTED |
| H8 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | FALSIFIED |
| H9 | 0.000000 | 0.000000 | ✅ | ✅ | ✅ | SUPPORTED |
| H10 | — | — | — | — | — | SUPPORTED |

## §5 — Enforcement Candidates for v1.9

The following metrics showed statistically significant structural divergence (BH-FDR) with meaningful effect sizes. These are candidate enforcement constraints for the v1.9 design phase.

> **D-66 compliance:** Each candidate below has an empirical basis derived from this governed, reproducible measurement campaign. No enforcement rule has been encoded.

| Hypothesis | Metric | Effect Size | Historical Baseline | Enforcement Layer |
|-----------|--------|-------------|--------------------|-----------------|
| H7 | m7_fileToDirRatio | d=-0.265 | median=5.466, IQR=[3.817, 7.931] | Layer 1 (Structural) |
| H9 | subTreeCV | d=-0.946 | median=2.032, IQR=[1.409, 2.439] | Layer 3 (Behavioural) |
| H10 | CSDI | d=N/A | median=N/A, IQR=[N/A, N/A] | Layer 1 (Structural) |

### Candidate Constraint Specifications

#### H7: m7_fileToDirRatio

- **Drift pattern:** Structural sprawl — low-density directory trees
- **Substrate implication:** Minimum density thresholds inform structural enforcement.
- **Historical baseline:** mean=7.688, median=5.466
- **Recent observed:** mean=5.549, median=4.034
- **Candidate threshold:** Historical p75: 7.931
- **Enforcement layer:** Layer 1 (Structural)

#### H9: subTreeCV

- **Drift pattern:** Template uniformity — AI tendency to replicate directory patterns
- **Substrate implication:** Structural repetition detection feeds into Layer 3 behavioural enforcement.
- **Historical baseline:** mean=1.964, median=2.032
- **Recent observed:** mean=1.321, median=1.315
- **Candidate threshold:** Historical p75: 2.439
- **Enforcement layer:** Layer 3 (Behavioural)

#### H10: CSDI

- **Drift pattern:** Multi-dimensional structural divergence
- **Substrate implication:** CSDI becomes the structural analogue of the DESI for enforcement priority ranking.
- **Historical baseline:** mean=N/A, median=N/A
- **Recent observed:** mean=N/A, median=N/A
- **Candidate threshold:** N/A
- **Enforcement layer:** Layer 1 (Structural)

## §6 — Cohort Structural Profiles

### Historical Cohort

| Metric | Mean | Median | Std Dev | Min | Max |
|--------|------|--------|---------|-----|-----|
| m1_maxDepth | 8.9600 | 8.5000 | 3.8767 | 3.0000 | 23.0000 |
| m1_meanDepth | 4.0951 | 3.7185 | 1.7811 | 1.4320 | 9.3550 |
| m2_rootFileRatio | 0.0166 | 0.0064 | 0.0350 | 0.0002 | 0.2500 |
| m3_namingEntropy | 8.3481 | 8.3938 | 1.2068 | 5.8646 | 11.1740 |
| m4_duplicatePurpose | 9.9400 | 6.5000 | 9.4343 | 0.0000 | 42.0000 |
| m5_templateFingerprint | 0.6033 | 1.0000 | 0.4405 | 0.0000 | 1.0000 |
| m6_orphanDirRatio | 0.3194 | 0.3047 | 0.1752 | 0.0000 | 0.8381 |
| m7_fileToDirRatio | 7.6884 | 5.4660 | 10.4401 | 1.2690 | 97.6280 |
| rootConfigCount | 10.5400 | 8.5000 | 6.8526 | 0.0000 | 40.0000 |
| subTreeCV | 1.9644 | 2.0323 | 0.6990 | 0.5194 | 4.1176 |

### Recent Cohort

| Metric | Mean | Median | Std Dev | Min | Max |
|--------|------|--------|---------|-----|-----|
| m1_maxDepth | 4.4300 | 4.0000 | 2.3323 | 0.0000 | 12.0000 |
| m1_meanDepth | 2.3819 | 2.2340 | 1.2581 | 0.0000 | 6.7180 |
| m2_rootFileRatio | 0.1418 | 0.0652 | 0.2107 | 0.0013 | 1.0000 |
| m3_namingEntropy | 6.4575 | 6.6202 | 1.5066 | 1.5850 | 8.9020 |
| m4_duplicatePurpose | 2.7300 | 1.0000 | 4.0298 | 0.0000 | 24.0000 |
| m5_templateFingerprint | 0.5750 | 0.5000 | 0.4441 | 0.0000 | 1.0000 |
| m6_orphanDirRatio | 0.3381 | 0.2982 | 0.2360 | 0.0000 | 0.9128 |
| m7_fileToDirRatio | 5.5495 | 4.0335 | 4.5699 | 1.4000 | 33.0000 |
| rootConfigCount | 5.6400 | 5.0000 | 4.2723 | 0.0000 | 20.0000 |
| subTreeCV | 1.3215 | 1.3153 | 0.6591 | 0.0000 | 2.9737 |

## §7 — Limitations

1. **Cohort asymmetry:** Historical repos are mature, large-scale projects; recent repos are early-stage, trending projects. Structural differences may reflect maturity, not AI influence.
2. **API tree truncation:** GitHub truncates trees above ~100,000 entries. Large monorepos may have incomplete data (flagged per-repo as `treeTruncated`).
3. **Vendor filtering:** Excluding `node_modules`, `vendor`, etc. may miss interesting divergence in dependency management patterns.
4. **Template fingerprinting:** The 15 template signatures are a curated subset. Novel frameworks or domain-specific scaffolds may go undetected.
5. **No content analysis:** This scanner measures tree topology only. Semantic divergence (file *content*, code quality, documentation accuracy) is measured by the companion MD Scanner, not this instrument.
6. **Selection bias:** Historical cohort selected for community adoption; recent cohort selected by stars. GitHub trending dynamics may bias recent repos toward AI/ML tooling.
7. **Single timepoint:** This is a cross-sectional observation, not a longitudinal study. Causal claims about AI influence on structure cannot be made from this design alone.

## §8 — Constitutional Record

| Item | Value |
|------|-------|
| Campaign | C-006 Structural Forensics Sweep |
| Constitutional source | D-68, D-69 (translation_0011) |
| Version arc | v1.8 (measurement only) |
| Hypotheses tested | 10 |
| SUPPORTED | 3 |
| DIRECTIONAL ONLY | 1 |
| FALSIFIED | 5 |
| NOT SUPPORTED | 1 |
| CSDI | 0.674 (large) |
| Enforcement candidates | 3 |
| Substrate modifications | Zero (D-68 compliance) |
| Repos scanned | 200 |
| Scanner version | 1.0.0 |
| Engine version | 1.0 |

---

*Measurement is not delay. It is the foundation that makes enforcement constitutional rather than arbitrary.*
