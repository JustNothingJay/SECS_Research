# SECS MD Scanner — Hypothesis Test Report (v2.0)

> **Analyst:** Jay Carpenter
> **Date:** 2026-03-01
> **Instrument:** SECS MD Scanner v2.1.0
> **Engine:** Hypothesis Testing Engine v2.0
> **Study:** Documentation Era Shift — Hypothesis Testing
> **Cohorts:** Historical (100 repos, 20747 files) vs Recent (100 repos, 8672 files)
> **Statistical Methods:** Mann-Whitney U (non-parametric), Cohen's d, Cliff's δ, Bootstrap 95% CI, Bonferroni & Holm-Bonferroni corrections

---

## §0 — Methodology

### Cohort Selection

**Historical cohort (n=100):** Established, high-star-count open-source repositories spanning 15+ programming languages and diverse ecosystems. Original 88 repos from the SECS 9.1M-check study, extended with 12 additional repos covering Swift, Scala, Haskell, C++, Kotlin, Julia, Nix, and mobile ecosystems. Selection criteria: created before 2024, significant community adoption. No filtering by documentation quality — pure ecosystem coverage.

**Recent cohort (n=100):** Top 100 public repositories by star count created between 2026-01-01 and 2026-03-01 with >50 stars, discovered via GitHub Search API on 2026-03-01 (query: `created:2026-01-01..2026-03-01 stars:>50 is:public sort:stars-desc`). From 4,963 matching repos, top 100 selected by star ranking — no manual filtering to avoid selection bias.

**Limitations:** The cohorts differ in repo age/maturity, which confounds drift metrics (D1-D3). Historical repos may accumulate fossils naturally. Recent repos may be biased toward AI/ML domains due to current GitHub trending patterns. Star-based selection may under-represent enterprise or niche tooling. Both cohorts are public GitHub repos only — private/corporate documentation patterns are unobserved.

### Metric Definitions

| Metric | Definition | Source |
|---|---|---|
| `mdFiles` | Count of .md files in repo | Structural scan |
| `mdRatio` | MD files ÷ total files | Structural scan |
| `medianFileSize` | Median bytes per MD file | Size distribution |
| `headingUniformity` | Fraction of files with H1 headings | Content analysis |
| `tableRatio` | Table lines ÷ content lines | Content breakdown |
| `templateScore` | Score 0-1 measuring structural template conformance (headings, sections, patterns) | Semantic analysis |
| `govDensity` | Governance keywords per 100 words (policy, compliance, license terms) | Semantic analysis |
| `proseRatio` | Prose lines ÷ total content lines | Content breakdown |
| `codeRatio` | Code block lines ÷ total content lines | Content breakdown |
| `driftMean` | Mean drift composite (staleness, temporal references, version scatter) | Drift analysis |
| `totalFossils` | Count of outdated references (dead links, deprecated APIs, old dates) | Drift analysis |
| `personaLeakFiles` | Files showing persona voice inconsistency | Drift analysis |
| `aiSignalMean` | Composite AI-generation signal: weighted combination of template conformance, hallucination markers, persona uniformity, and structural regularity | AI surface |
| `aiHighCount` | Files with AI signal > 0.4 | AI surface |
| `promptStructures` | Count of prompt-like patterns (numbered lists with instructions, Q&A format, step markers) | AI-optimisation |
| `aiOptMean` | Composite AI-optimisation score: prompt structures, boilerplate, agent scaffolding, CoT leakage | AI-optimisation |
| `llmBoilerplate` | Count of LLM-characteristic phrases ("I'd be happy to", "Here's an example", etc.) | AI-optimisation |

### Statistical Methods

1. **Mann-Whitney U test** (two-tailed, normal approximation): Non-parametric rank-sum test suitable for non-normal distributions. Tests whether one cohort stochastically dominates the other. Selected over t-test due to high skewness in most metrics.
2. **Cohen's d** (pooled SD): Parametric effect size measuring standardised mean difference. Thresholds: |d| < 0.2 negligible, < 0.5 small, < 0.8 medium, < 1.2 large, ≥ 1.2 very large.
3. **Cliff's delta** (δ): Non-parametric effect size based on dominance probability. Robust to outliers and skew. Thresholds (Romano et al., 2006): |δ| < 0.147 negligible, < 0.33 small, < 0.474 medium, ≥ 0.474 large.
4. **Bootstrap 95% CI** (10,000 iterations): Non-parametric confidence interval for the mean difference via resampling.
5. **20% Trimmed means**: Robust central tendency removing the most extreme 20% from each tail, reducing outlier influence on skewed metrics.
6. **Bonferroni correction**: Conservative family-wise error rate control. Adjusted α = 0.05 / 17 = 0.0029.
7. **Holm-Bonferroni step-down**: Less conservative FWER control. Reported for comparison.
8. **Benjamini-Hochberg FDR**: Controls false discovery rate rather than family-wise error — appropriate for exploratory hypothesis testing where the goal is to identify real effects rather than eliminate all false positives. **Used as the primary corrected significance test.**

### Verdict Criteria

Verdicts use BH-FDR corrected significance as primary, with CI integrity check:
- **SUPPORTED:** Correct direction + BH-significant + |Cohen's d| ≥ 0.2 + CI excludes zero
- **SUPPORTED†:** Correct direction + BH-significant + |d| ≥ 0.2 but CI crosses zero (magnitude uncertain)
- **WEAKLY SUPPORTED:** Correct direction + BH-significant + |d| < 0.2
- **DIRECTIONAL ONLY:** Correct direction but not BH-significant
- **FALSIFIED:** Wrong direction + BH-significant
- **NOT SUPPORTED:** Wrong direction + not BH-significant

> **† CI Integrity Note:** When the bootstrap 95% CI crosses zero, the rank-based test confirms distributional separation but the magnitude of the mean difference is not robustly distinguishable from null. The claim's direction is reliable; its quantified effect size should be interpreted with caution.

---

## §1 — Core Hypothesis

> Documentation produced in the post-LLM era (Jan–Mar 2026) exhibits a distinct structural, semantic, and generative signature compared to pre-LLM documentation, characterised by: fewer but larger MD files, higher documentation-to-code ratios, greater template uniformity, higher AI-generation signals, lower drift and fossilisation, and reduced narrative prose in favour of code-heavy, example-driven content.

This hypothesis was decomposed into 17 testable claims across four categories (Structural, Semantic, Drift, AI-Generation) and tested against 200 repositories containing 29,419 MD files. See §0 for cohort selection methodology, metric definitions, and statistical methods.

---

## §2 — Documentation Era Shift Index

| Component | Value |
|---|---|
| Composite index | **0.764** |
| Magnitude | **medium** |
| Claims supported | 16 / 17 (94%) |
| Claims falsified | 0 / 17 (0%) |
| Interpretation | Moderate evidence of a documentation era shift. |

### Drift Vectors by Category

| Category | RMS Effect | Magnitude | Direction | Sig. Fraction |
|---|---|---|---|---|
| Structural | 0.790 | medium | increasing | 100% |
| Semantic | 0.762 | medium | increasing | 75% |
| Drift | 0.671 | medium | decreasing | 100% |
| AI-Generation | 0.804 | large | decreasing | 100% |

---

## §3 — Claim-by-Claim Results

| ID | Category | Verdict (BH-FDR) | Predicted | Actual | Δ% | Cohen's d | Cliff's δ | pₚₐₑ | qᴾᴴ | BH Sig. |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Structural | ✅ SUPPORTED | lower | lower | -58.2% | -0.355 (small) | -0.450 (medium) | 0.0000 | 0.0000 | Yes |
| S2 | Structural | ✅ SUPPORTED | higher | higher | +81.1% | 0.553 (medium) | 0.432 (medium) | 0.0000 | 0.0000 | Yes |
| S3 | Structural | ✅ SUPPORTED | higher | higher | +289.4% | 0.853 (large) | 0.563 (large) | 0.0000 | 0.0000 | Yes |
| S4 | Structural | ✅ SUPPORTED | higher | higher | +40.2% | 1.081 (large) | 0.649 (large) | 0.0000 | 0.0000 | Yes |
| S5 | Structural | ✅ SUPPORTED | higher | higher | +229.9% | 0.888 (large) | 0.578 (large) | 0.0000 | 0.0000 | Yes |
| E1 | Semantic | ✅ SUPPORTED | higher | higher | +114.2% | 0.969 (large) | 0.514 (large) | 0.0000 | 0.0000 | Yes |
| E2 | Semantic | ➡️ DIRECTIONAL ONLY | higher | higher | +11.0% | 0.111 (negligible) | 0.130 (negligible) | 0.1128 | 0.1128 | No |
| E3 | Semantic | ✅ SUPPORTED | lower | lower | -50.2% | -1.000 (large) | -0.603 (large) | 0.0000 | 0.0000 | Yes |
| E4 | Semantic | ✅ SUPPORTED | higher | higher | +44.4% | 0.609 (medium) | 0.369 (medium) | 0.0000 | 0.0000 | Yes |
| D1 | Drift | ✅ SUPPORTED | lower | lower | -44.1% | -0.621 (medium) | -0.454 (medium) | 0.0000 | 0.0000 | Yes |
| D2 | Drift | ✅ SUPPORTED | lower | lower | -86.3% | -0.490 (small) | -0.475 (large) | 0.0000 | 0.0000 | Yes |
| D3 | Drift | ✅ SUPPORTED | lower | lower | -94.9% | -0.850 (large) | -0.624 (large) | 0.0000 | 0.0000 | Yes |
| A1 | AI-Generation | ✅ SUPPORTED | higher | higher | +97.8% | 1.593 (very large) | 0.776 (large) | 0.0000 | 0.0000 | Yes |
| A2 | AI-Generation | ✅ SUPPORTED | higher | higher | +376.5% | 0.377 (small) | 0.165 (small) | 0.0441 | 0.0468 | Yes |
| A3 | AI-Generation | ✅ SUPPORTED | lower | lower | -82.9% | -0.576 (medium) | -0.649 (large) | 0.0000 | 0.0000 | Yes |
| A4 | AI-Generation | ✅ SUPPORTED† | lower | lower | -12.6% | -0.245 (small) | -0.168 (small) | 0.0404 | 0.0457 | Yes |
| A5 | AI-Generation | ✅ SUPPORTED | lower | lower | -67.1% | -0.399 (small) | -0.504 (large) | 0.0000 | 0.0000 | Yes |

### Multiple Comparisons Correction Summary

| ID | pₚₐₑ | qᴾᴴ | BH Sig. | Holm p | Holm Sig. | Bonf. p | Bonf. Sig. |
|---|---|---|---|---|---|---|---|
| S1 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| S2 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| S3 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| S4 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| S5 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| E1 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| E2 | 0.1128 | 0.1128 | No | 0.1128 | No | 1.0000 | No |
| E3 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| E4 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0001 | Yes |
| D1 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| D2 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| D3 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| A1 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| A2 | 0.0441 | 0.0468 | Yes | 0.0882 | No | 0.7493 | No |
| A3 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |
| A4 | 0.0404 | 0.0457 | Yes | 0.1211 | No | 0.6862 | No |
| A5 | 0.0000 | 0.0000 | Yes | 0.0000 | Yes | 0.0000 | Yes |

### Borderline Claims Under Correction

**A2** (pₚₐₑ=0.0441, qᴾᴴ=0.0468): Survives BH-FDR correction but fails Holm-Bonferroni (conservative FWER control).

**A4** (pₚₐₑ=0.0404, qᴾᴴ=0.0457): Survives BH-FDR correction but fails Holm-Bonferroni (conservative FWER control). Bootstrap 95% CI [-0.0205, 0.0012] **crosses zero** — the mean difference is not robustly distinguishable from null at the resampling level, even though the rank-order separation is real.

---

## §4 — Detailed Claim Analysis

### S1: Recent repos have significantly fewer MD files.

**Verdict:** ✅ SUPPORTED

**Metric:** `mdFiles`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 207.4700 | 86.7200 |
| Trimmed Mean (20%) | 99.0500 | 22.9833 |
| Median | 80.0000 | 18.0000 |
| Std Dev | 369.2071 | 307.5039 |
| Variance | 136313.8678 | 94558.6279 |
| Skewness | 3.871 | 8.174 |
| Kurtosis (excess) | 17.678 | 68.929 |
| Min | 2.0000 | 1.0000 |
| P5 | 6.0000 | 1.9500 |
| P25 | 27.5000 | 4.0000 |
| P75 | 209.2500 | 50.7500 |
| P95 | 915.1000 | 358.9000 |
| Max | 2597.0000 | 2916.0000 |
| IQR | 181.7500 | 46.7500 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -120.7500 |
| Trimmed Delta (20%) | -76.0667 |
| Delta % | -58.2% |
| Trimmed Delta % | -76.8% |
| Cohen's d | -0.355 (small) |
| Cliff's δ | -0.450 (medium) |
| Mann-Whitney U | 2750 |
| Mann-Whitney z | 5.499 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.450 |
| Bootstrap 95% CI | [-213.7400, -26.9600] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.355 (small), Cliff's δ: -0.450 (medium).

---

### S2: Recent repos have larger median file sizes.

**Verdict:** ✅ SUPPORTED

**Metric:** `medianFileSize`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 3003.9000 | 5439.5000 |
| Trimmed Mean (20%) | 2487.9833 | 4303.2500 |
| Median | 1977.0000 | 4354.0000 |
| Std Dev | 2704.9277 | 5607.3050 |
| Variance | 7316633.9091 | 31441869.1616 |
| Skewness | 1.681 | 5.260 |
| Kurtosis (excess) | 3.084 | 35.452 |
| Min | 170.0000 | 842.0000 |
| P5 | 260.7500 | 1447.1000 |
| P25 | 995.5000 | 2527.7500 |
| P75 | 4518.7500 | 6034.2500 |
| P95 | 8264.4500 | 14032.7000 |
| Max | 13284.0000 | 49402.0000 |
| IQR | 3523.2500 | 3506.5000 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 2435.6000 |
| Trimmed Delta (20%) | 1815.2667 |
| Delta % | +81.1% |
| Trimmed Delta % | +73.0% |
| Cohen's d | 0.553 (medium) |
| Cliff's δ | 0.432 (medium) |
| Mann-Whitney U | 2842 |
| Mann-Whitney z | 5.274 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.432 |
| Bootstrap 95% CI | [1348.9300, 3789.0000] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 0.553 (medium), Cliff's δ: 0.432 (medium).

---

### S3: MD ratio (documentation ÷ total files) is substantially higher in recent repos.

**Verdict:** ✅ SUPPORTED

**Metric:** `mdRatio`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.0605 | 0.2357 |
| Trimmed Mean (20%) | 0.0282 | 0.1454 |
| Median | 0.0237 | 0.1230 |
| Std Dev | 0.1007 | 0.2723 |
| Variance | 0.0101 | 0.0742 |
| Skewness | 3.052 | 1.388 |
| Kurtosis (excess) | 9.531 | 0.572 |
| Min | 0.0003 | 0.0023 |
| P5 | 0.0015 | 0.0089 |
| P25 | 0.0089 | 0.0444 |
| P75 | 0.0588 | 0.2728 |
| P95 | 0.2348 | 0.7867 |
| Max | 0.5614 | 1.0000 |
| IQR | 0.0500 | 0.2285 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.1751 |
| Trimmed Delta (20%) | 0.1171 |
| Delta % | +289.4% |
| Trimmed Delta % | +414.9% |
| Cohen's d | 0.853 (large) |
| Cliff's δ | 0.563 (large) |
| Mann-Whitney U | 2187 |
| Mann-Whitney z | 6.874 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.563 |
| Bootstrap 95% CI | [0.1203, 0.2335] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 0.853 (large), Cliff's δ: 0.563 (large).

---

### S4: Documentation shows greater structural uniformity (heading patterns).

**Verdict:** ✅ SUPPORTED

**Metric:** `headingUniformity`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.6247 | 0.8758 |
| Trimmed Mean (20%) | 0.6540 | 0.9385 |
| Median | 0.6521 | 0.9491 |
| Std Dev | 0.2607 | 0.2001 |
| Variance | 0.0680 | 0.0400 |
| Skewness | -0.454 | -2.715 |
| Kurtosis (excess) | -0.959 | 7.815 |
| Min | 0.0388 | 0.0000 |
| P5 | 0.1575 | 0.5000 |
| P25 | 0.4292 | 0.8197 |
| P75 | 0.8470 | 1.0000 |
| P95 | 0.9576 | 1.0000 |
| Max | 0.9967 | 1.0000 |
| IQR | 0.4178 | 0.1803 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.2511 |
| Trimmed Delta (20%) | 0.2845 |
| Delta % | +40.2% |
| Trimmed Delta % | +43.5% |
| Cohen's d | 1.081 (large) |
| Cliff's δ | 0.649 (large) |
| Mann-Whitney U | 1753 |
| Mann-Whitney z | 7.934 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.649 |
| Bootstrap 95% CI | [0.1861, 0.3163] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 1.081 (large), Cliff's δ: 0.649 (large).

---

### S5: Documentation shows greater table usage (structural layout).

**Verdict:** ✅ SUPPORTED

**Metric:** `tableRatio`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.0255 | 0.0841 |
| Trimmed Mean (20%) | 0.0128 | 0.0667 |
| Median | 0.0100 | 0.0597 |
| Std Dev | 0.0476 | 0.0802 |
| Variance | 0.0023 | 0.0064 |
| Skewness | 5.337 | 1.646 |
| Kurtosis (excess) | 35.824 | 2.767 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0000 | 0.0000 |
| P25 | 0.0008 | 0.0251 |
| P75 | 0.0304 | 0.1114 |
| P95 | 0.0838 | 0.2559 |
| Max | 0.3993 | 0.4094 |
| IQR | 0.0296 | 0.0863 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.0586 |
| Trimmed Delta (20%) | 0.0539 |
| Delta % | +229.9% |
| Trimmed Delta % | +421.3% |
| Cohen's d | 0.888 (large) |
| Cliff's δ | 0.578 (large) |
| Mann-Whitney U | 2108 |
| Mann-Whitney z | 7.066 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.578 |
| Bootstrap 95% CI | [0.0404, 0.0771] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 0.888 (large), Cliff's δ: 0.578 (large).

---

### E1: Recent repos show higher template match scores (uniform semantic patterns).

**Verdict:** ✅ SUPPORTED

**Metric:** `templateScore`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.0701 | 0.1503 |
| Trimmed Mean (20%) | 0.0633 | 0.1354 |
| Median | 0.0642 | 0.1353 |
| Std Dev | 0.0489 | 0.1062 |
| Variance | 0.0024 | 0.0113 |
| Skewness | 1.251 | 1.361 |
| Kurtosis (excess) | 2.270 | 2.696 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0106 | 0.0285 |
| P25 | 0.0367 | 0.0747 |
| P75 | 0.0937 | 0.2000 |
| P95 | 0.1597 | 0.3752 |
| Max | 0.2778 | 0.6111 |
| IQR | 0.0570 | 0.1253 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.0801 |
| Trimmed Delta (20%) | 0.0721 |
| Delta % | +114.2% |
| Trimmed Delta % | +113.8% |
| Cohen's d | 0.969 (large) |
| Cliff's δ | 0.514 (large) |
| Mann-Whitney U | 2429 |
| Mann-Whitney z | 6.282 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.514 |
| Bootstrap 95% CI | [0.0575, 0.1036] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 0.969 (large), Cliff's δ: 0.514 (large).

---

### E2: Governance density increases due to LLM over-structuring.

**Verdict:** ➡️ DIRECTIONAL ONLY

**Metric:** `govDensity`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.2409 | 0.2675 |
| Trimmed Mean (20%) | 0.1767 | 0.2354 |
| Median | 0.1622 | 0.2265 |
| Std Dev | 0.2545 | 0.2247 |
| Variance | 0.0648 | 0.0505 |
| Skewness | 3.313 | 2.025 |
| Kurtosis (excess) | 13.949 | 6.344 |
| Min | 0.0064 | 0.0000 |
| P5 | 0.0323 | 0.0000 |
| P25 | 0.0984 | 0.1085 |
| P75 | 0.2813 | 0.3692 |
| P95 | 0.7145 | 0.5876 |
| Max | 1.7828 | 1.3512 |
| IQR | 0.1829 | 0.2608 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.0266 |
| Trimmed Delta (20%) | 0.0587 |
| Delta % | +11.0% |
| Trimmed Delta % | +33.2% |
| Cohen's d | 0.111 (negligible) |
| Cliff's δ | 0.130 (negligible) |
| Mann-Whitney U | 4351 |
| Mann-Whitney z | 1.586 |
| pₚₐₑ (two-tailed) | 0.1128 |
| qᴾᴴ (BH-FDR) | 0.1128 |
| BH-FDR significant | No |
| Holm-Bonferroni significant | No |
| Rank-Biserial r | 0.130 |
| Bootstrap 95% CI | [-0.0391, 0.0912] |
| CI crosses zero | **Yes** — magnitude uncertain |

**Analysis:** DIRECTIONAL ONLY: Direction matches prediction (higher) but not statistically significant after BH-FDR correction (p_raw=0.1128, q_BH=0.1128). Cohen's d: 0.111 (negligible), Cliff's δ: 0.130 (negligible).

---

### E3: Prose density decreases, replaced by code-first documentation.

**Verdict:** ✅ SUPPORTED

**Metric:** `proseRatio`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.2595 | 0.1293 |
| Trimmed Mean (20%) | 0.2425 | 0.1035 |
| Median | 0.2497 | 0.1001 |
| Std Dev | 0.1420 | 0.1172 |
| Variance | 0.0202 | 0.0137 |
| Skewness | 0.513 | 3.097 |
| Kurtosis (excess) | -0.625 | 11.809 |
| Min | 0.0215 | -0.0368 |
| P5 | 0.0653 | 0.0301 |
| P25 | 0.1428 | 0.0706 |
| P75 | 0.3373 | 0.1507 |
| P95 | 0.4919 | 0.2893 |
| Max | 0.6056 | 0.7907 |
| IQR | 0.1945 | 0.0802 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -0.1301 |
| Trimmed Delta (20%) | -0.1389 |
| Delta % | -50.2% |
| Trimmed Delta % | -57.3% |
| Cohen's d | -1.000 (large) |
| Cliff's δ | -0.603 (large) |
| Mann-Whitney U | 1987 |
| Mann-Whitney z | 7.363 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.603 |
| Bootstrap 95% CI | [-0.1659, -0.0934] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -1.000 (large), Cliff's δ: -0.603 (large).

---

### E4: Code ratio increases in documentation content.

**Verdict:** ✅ SUPPORTED

**Metric:** `codeRatio`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.2166 | 0.3129 |
| Trimmed Mean (20%) | 0.1965 | 0.3121 |
| Median | 0.1821 | 0.3141 |
| Std Dev | 0.1673 | 0.1484 |
| Variance | 0.0280 | 0.0220 |
| Skewness | 0.815 | 0.152 |
| Kurtosis (excess) | 0.171 | -0.192 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0052 | 0.0600 |
| P25 | 0.0786 | 0.2165 |
| P75 | 0.3070 | 0.4130 |
| P95 | 0.5655 | 0.5432 |
| Max | 0.7005 | 0.7316 |
| IQR | 0.2284 | 0.1965 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.0963 |
| Trimmed Delta (20%) | 0.1156 |
| Delta % | +44.4% |
| Trimmed Delta % | +58.8% |
| Cohen's d | 0.609 (medium) |
| Cliff's δ | 0.369 (medium) |
| Mann-Whitney U | 3156 |
| Mann-Whitney z | 4.507 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.369 |
| Bootstrap 95% CI | [0.0532, 0.1387] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 0.609 (medium), Cliff's δ: 0.369 (medium).

---

### D1: Recent repos show lower drift composites.

**Verdict:** ✅ SUPPORTED

**Metric:** `driftMean`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.0583 | 0.0326 |
| Trimmed Mean (20%) | 0.0532 | 0.0216 |
| Median | 0.0530 | 0.0192 |
| Std Dev | 0.0423 | 0.0405 |
| Variance | 0.0018 | 0.0016 |
| Skewness | 1.288 | 2.572 |
| Kurtosis (excess) | 2.069 | 7.134 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0077 | 0.0000 |
| P25 | 0.0293 | 0.0088 |
| P75 | 0.0790 | 0.0406 |
| P95 | 0.1383 | 0.1070 |
| Max | 0.2025 | 0.2225 |
| IQR | 0.0498 | 0.0318 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -0.0257 |
| Trimmed Delta (20%) | -0.0316 |
| Delta % | -44.1% |
| Trimmed Delta % | -59.4% |
| Cohen's d | -0.621 (medium) |
| Cliff's δ | -0.454 (medium) |
| Mann-Whitney U | 2730 |
| Mann-Whitney z | 5.546 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.454 |
| Bootstrap 95% CI | [-0.0370, -0.0140] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.621 (medium), Cliff's δ: -0.454 (medium).

---

### D2: Recent repos have fewer fossils (outdated references).

**Verdict:** ✅ SUPPORTED

**Metric:** `totalFossils`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 9.1200 | 1.2500 |
| Trimmed Mean (20%) | 2.7500 | 0.0000 |
| Median | 1.0000 | 0.0000 |
| Std Dev | 21.5586 | 7.0816 |
| Variance | 464.7733 | 50.1490 |
| Skewness | 4.506 | 8.491 |
| Kurtosis (excess) | 21.274 | 71.940 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0000 | 0.0000 |
| P25 | 0.0000 | 0.0000 |
| P75 | 8.5000 | 0.0000 |
| P95 | 34.2000 | 3.0000 |
| Max | 136.0000 | 67.0000 |
| IQR | 8.5000 | 0.0000 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -7.8700 |
| Trimmed Delta (20%) | -2.7500 |
| Delta % | -86.3% |
| Trimmed Delta % | -100.0% |
| Cohen's d | -0.490 (small) |
| Cliff's δ | -0.475 (large) |
| Mann-Whitney U | 2626 |
| Mann-Whitney z | 5.802 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.475 |
| Bootstrap 95% CI | [-12.7800, -3.8000] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.490 (small), Cliff's δ: -0.475 (large).

---

### D3: Persona leakage is lower but more uniform in recent repos.

**Verdict:** ✅ SUPPORTED

**Metric:** `personaLeakFiles`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 6.0400 | 0.3100 |
| Trimmed Mean (20%) | 2.6167 | 0.0000 |
| Median | 2.0000 | 0.0000 |
| Std Dev | 9.4846 | 0.9502 |
| Variance | 89.9580 | 0.9029 |
| Skewness | 2.206 | 5.897 |
| Kurtosis (excess) | 4.566 | 40.885 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0000 | 0.0000 |
| P25 | 0.0000 | 0.0000 |
| P75 | 6.5000 | 0.0000 |
| P95 | 25.0000 | 1.0500 |
| Max | 48.0000 | 8.0000 |
| IQR | 6.5000 | 0.0000 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -5.7300 |
| Trimmed Delta (20%) | -2.6167 |
| Delta % | -94.9% |
| Trimmed Delta % | -100.0% |
| Cohen's d | -0.850 (large) |
| Cliff's δ | -0.624 (large) |
| Mann-Whitney U | 1883 |
| Mann-Whitney z | 7.617 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.623 |
| Bootstrap 95% CI | [-7.6300, -3.9500] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.850 (large), Cliff's δ: -0.624 (large).

---

### A1: AI-signal composites are significantly higher in recent repos.

**Verdict:** ✅ SUPPORTED

**Metric:** `aiSignalMean`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.1002 | 0.1982 |
| Trimmed Mean (20%) | 0.0924 | 0.1936 |
| Median | 0.0881 | 0.1916 |
| Std Dev | 0.0451 | 0.0743 |
| Variance | 0.0020 | 0.0055 |
| Skewness | 0.855 | 0.926 |
| Kurtosis (excess) | 0.093 | 3.234 |
| Min | 0.0297 | 0.0071 |
| P5 | 0.0441 | 0.1009 |
| P25 | 0.0654 | 0.1559 |
| P75 | 0.1193 | 0.2336 |
| P95 | 0.1854 | 0.3214 |
| Max | 0.2363 | 0.5264 |
| IQR | 0.0538 | 0.0777 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.0980 |
| Trimmed Delta (20%) | 0.1012 |
| Delta % | +97.8% |
| Trimmed Delta % | +109.6% |
| Cohen's d | 1.593 (very large) |
| Cliff's δ | 0.776 (large) |
| Mann-Whitney U | 1122 |
| Mann-Whitney z | 9.475 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.776 |
| Bootstrap 95% CI | [0.0814, 0.1147] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: 1.593 (very large), Cliff's δ: 0.776 (large).

---

### A2: High-AI files (>0.4) are more common in recent repos.

**Verdict:** ✅ SUPPORTED

**Metric:** `aiHighCount`  
**Predicted direction:** higher in recent  
**Observed direction:** higher in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.1700 | 0.8100 |
| Trimmed Mean (20%) | 0.0000 | 0.1167 |
| Median | 0.0000 | 0.0000 |
| Std Dev | 0.6039 | 2.3212 |
| Variance | 0.3647 | 5.3878 |
| Skewness | 5.806 | 6.165 |
| Kurtosis (excess) | 39.113 | 44.448 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0000 | 0.0000 |
| P25 | 0.0000 | 0.0000 |
| P75 | 0.0000 | 1.0000 |
| P95 | 1.0000 | 4.0000 |
| Max | 5.0000 | 20.0000 |
| IQR | 0.0000 | 1.0000 |

| Test | Value |
|---|---|
| Delta (recent − historical) | 0.6400 |
| Trimmed Delta (20%) | 0.1167 |
| Delta % | +376.5% |
| Trimmed Delta % | — |
| Cohen's d | 0.377 (small) |
| Cliff's δ | 0.165 (small) |
| Mann-Whitney U | 4176 |
| Mann-Whitney z | 2.013 |
| pₚₐₑ (two-tailed) | 0.0441 |
| qᴾᴴ (BH-FDR) | 0.0468 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | No |
| Rank-Biserial r | 0.165 |
| Bootstrap 95% CI | [0.2400, 1.1700] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0441, q_BH=0.0468), Cohen's d: 0.377 (small), Cliff's δ: 0.165 (small).

---

### A3: Prompt-like structures decrease as LLMs produce more polished documentation.

**Verdict:** ✅ SUPPORTED

**Metric:** `promptStructures`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 322.0900 | 55.0500 |
| Trimmed Mean (20%) | 151.9833 | 11.6667 |
| Median | 108.5000 | 8.5000 |
| Std Dev | 573.3032 | 317.3572 |
| Variance | 328676.5474 | 100715.5631 |
| Skewness | 4.036 | 9.784 |
| Kurtosis (excess) | 20.310 | 90.293 |
| Min | 0.0000 | 0.0000 |
| P5 | 2.0000 | 0.0000 |
| P25 | 32.2500 | 3.0000 |
| P75 | 355.5000 | 27.2500 |
| P95 | 1344.8000 | 81.5000 |
| Max | 4208.0000 | 3174.0000 |
| IQR | 323.2500 | 24.2500 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -267.0400 |
| Trimmed Delta (20%) | -140.3167 |
| Delta % | -82.9% |
| Trimmed Delta % | -92.3% |
| Cohen's d | -0.576 (medium) |
| Cliff's δ | -0.649 (large) |
| Mann-Whitney U | 1754 |
| Mann-Whitney z | 7.932 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.649 |
| Bootstrap 95% CI | [-398.3400, -144.7400] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.576 (medium), Cliff's δ: -0.649 (large).

---

### A4: AI-optimisation shifts from explicit scaffolding to implicit generative fingerprints.

**Verdict:** ✅ SUPPORTED†

**Metric:** `aiOptMean`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 0.0763 | 0.0667 |
| Trimmed Mean (20%) | 0.0733 | 0.0629 |
| Median | 0.0721 | 0.0619 |
| Std Dev | 0.0370 | 0.0415 |
| Variance | 0.0014 | 0.0017 |
| Skewness | 0.684 | 1.181 |
| Kurtosis (excess) | 0.399 | 2.367 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0292 | 0.0083 |
| P25 | 0.0516 | 0.0428 |
| P75 | 0.0983 | 0.0839 |
| P95 | 0.1413 | 0.1276 |
| Max | 0.1925 | 0.2200 |
| IQR | 0.0467 | 0.0411 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -0.0096 |
| Trimmed Delta (20%) | -0.0103 |
| Delta % | -12.6% |
| Trimmed Delta % | -14.1% |
| Cohen's d | -0.245 (small) |
| Cliff's δ | -0.168 (small) |
| Mann-Whitney U | 4161 |
| Mann-Whitney z | 2.050 |
| pₚₐₑ (two-tailed) | 0.0404 |
| qᴾᴴ (BH-FDR) | 0.0457 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | No |
| Rank-Biserial r | 0.168 |
| Bootstrap 95% CI | [-0.0205, 0.0012] |
| CI crosses zero | **Yes** — magnitude uncertain |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0404, q_BH=0.0457), Cohen's d: -0.245 (small), Cliff's δ: -0.168 (small). **†Note:** Bootstrap 95% CI [-0.0205, 0.0012] crosses zero, indicating the mean difference is not robustly distinguishable from null at the bootstrap level. The Mann-Whitney rank test confirms distributional separation, but the magnitude of the mean shift should be interpreted with caution.

---

### A5: LLM boilerplate decreases in better-trained model outputs.

**Verdict:** ✅ SUPPORTED

**Metric:** `llmBoilerplate`  
**Predicted direction:** lower in recent  
**Observed direction:** lower in recent  

| Statistic | Historical | Recent |
|---|---|---|
| n | 100 | 100 |
| Mean | 37.6800 | 12.3800 |
| Trimmed Mean (20%) | 17.5667 | 2.3333 |
| Median | 12.0000 | 2.0000 |
| Std Dev | 65.4473 | 61.2685 |
| Variance | 4283.3511 | 3753.8339 |
| Skewness | 3.321 | 9.476 |
| Kurtosis (excess) | 12.178 | 86.323 |
| Min | 0.0000 | 0.0000 |
| P5 | 0.0000 | 0.0000 |
| P25 | 3.0000 | 0.0000 |
| P75 | 43.0000 | 6.0000 |
| P95 | 181.8500 | 39.0500 |
| Max | 411.0000 | 608.0000 |
| IQR | 40.0000 | 6.0000 |

| Test | Value |
|---|---|
| Delta (recent − historical) | -25.3000 |
| Trimmed Delta (20%) | -15.2333 |
| Delta % | -67.1% |
| Trimmed Delta % | -86.7% |
| Cohen's d | -0.399 (small) |
| Cliff's δ | -0.504 (large) |
| Mann-Whitney U | 2480 |
| Mann-Whitney z | 6.157 |
| pₚₐₑ (two-tailed) | 0.0000 |
| qᴾᴴ (BH-FDR) | 0.0000 |
| BH-FDR significant | Yes |
| Holm-Bonferroni significant | Yes |
| Rank-Biserial r | 0.504 |
| Bootstrap 95% CI | [-42.2100, -7.0700] |

**Analysis:** SUPPORTED: Direction matches, statistically significant after BH-FDR correction (p_raw=0.0000, q_BH=0.0000), Cohen's d: -0.399 (small), Cliff's δ: -0.504 (large).

---

## §5 — Cohort Behavioural Signatures

The behavioural signature captures the characteristic shape of each cohort across all measured dimensions. The coefficient of variation (CV) indicates internal consistency — lower CV = more uniform behaviour within the cohort.

| Metric | Hist Mean | Hist CV | Recent Mean | Recent CV | Δ Mean% |
|---|---|---|---|---|---|
| mdFiles | 207.4700 | 1.780 | 86.7200 | 3.546 | -58.2 |
| mdRatio | 0.0605 | 1.664 | 0.2357 | 1.156 | 289.4 |
| medianFileSize | 3003.9000 | 0.900 | 5439.5000 | 1.031 | 81.1 |
| templateScore | 0.0701 | 0.698 | 0.1503 | 0.707 | 114.2 |
| govDensity | 0.2409 | 1.056 | 0.2675 | 0.840 | 11.0 |
| proseRatio | 0.2595 | 0.547 | 0.1293 | 0.906 | -50.2 |
| codeRatio | 0.2166 | 0.772 | 0.3129 | 0.474 | 44.4 |
| driftMean | 0.0583 | 0.725 | 0.0326 | 1.242 | -44.1 |
| totalFossils | 9.1200 | 2.364 | 1.2500 | 5.665 | -86.3 |
| aiSignalMean | 0.1002 | 0.450 | 0.1982 | 0.375 | 97.8 |
| aiOptMean | 0.0763 | 0.484 | 0.0667 | 0.623 | -12.6 |
| promptStructures | 322.0900 | 1.780 | 55.0500 | 5.765 | -82.9 |
| headingUniformity | 0.6247 | 0.417 | 0.8758 | 0.228 | 40.2 |
| tableRatio | 0.0255 | 1.867 | 0.0841 | 0.954 | 229.9 |
| llmBoilerplate | 37.6800 | 1.737 | 12.3800 | 4.949 | -67.1 |

### Signature Interpretation

- **Recent cohort is more internally uniform** on 6/15 metrics: mdRatio, govDensity, codeRatio, aiSignalMean, headingUniformity, tableRatio
- **Historical cohort is more internally uniform** on 9/15 metrics: mdFiles, medianFileSize, templateScore, proseRatio, driftMean, totalFossils, aiOptMean, promptStructures, llmBoilerplate

---

## §6 — Temporal Drift Vectors

Each drift vector captures the direction and magnitude of change from historical → recent for a signal category.

### Structural Drift Vector

- **RMS Effect Size:** 0.790 (medium)
- **Dominant Direction:** increasing
- **Significant Fraction:** 100%

| Component | Δ | Δ% | Cohen's d | Direction | Sig. |
|---|---|---|---|---|---|
| mdFiles | -120.7500 | -58.2% | -0.355 | lower | Yes |
| medianFileSize | 2435.6000 | +81.1% | 0.553 | higher | Yes |
| mdRatio | 0.1751 | +289.4% | 0.853 | higher | Yes |
| headingUniformity | 0.2511 | +40.2% | 1.081 | higher | Yes |
| tableRatio | 0.0586 | +229.9% | 0.888 | higher | Yes |

### Semantic Drift Vector

- **RMS Effect Size:** 0.762 (medium)
- **Dominant Direction:** increasing
- **Significant Fraction:** 75%

| Component | Δ | Δ% | Cohen's d | Direction | Sig. |
|---|---|---|---|---|---|
| templateScore | 0.0801 | +114.2% | 0.969 | higher | Yes |
| govDensity | 0.0266 | +11.0% | 0.111 | higher | No |
| proseRatio | -0.1301 | -50.2% | -1.000 | lower | Yes |
| codeRatio | 0.0963 | +44.4% | 0.609 | higher | Yes |

### Drift Drift Vector

- **RMS Effect Size:** 0.671 (medium)
- **Dominant Direction:** decreasing
- **Significant Fraction:** 100%

| Component | Δ | Δ% | Cohen's d | Direction | Sig. |
|---|---|---|---|---|---|
| driftMean | -0.0257 | -44.1% | -0.621 | lower | Yes |
| totalFossils | -7.8700 | -86.3% | -0.490 | lower | Yes |
| personaLeakFiles | -5.7300 | -94.9% | -0.850 | lower | Yes |

### AI-Generation Drift Vector

- **RMS Effect Size:** 0.804 (large)
- **Dominant Direction:** decreasing
- **Significant Fraction:** 100%

| Component | Δ | Δ% | Cohen's d | Direction | Sig. |
|---|---|---|---|---|---|
| aiSignalMean | 0.0980 | +97.8% | 1.593 | higher | Yes |
| aiHighCount | 0.6400 | +376.5% | 0.377 | higher | Yes |
| promptStructures | -267.0400 | -82.9% | -0.576 | lower | Yes |
| aiOptMean | -0.0096 | -12.6% | -0.245 | lower | Yes |
| llmBoilerplate | -25.3000 | -67.1% | -0.399 | lower | Yes |

---

## §7 — Falsification Summary

| Verdict | Count | Claims |
|---|---|---|
| ✅ SUPPORTED | 15 | S1, S2, S3, S4, S5, E1, E3, E4, D1, D2, D3, A1, A2, A3, A5 |
| ✅† SUPPORTED (CI caveat) | 1 | A4 |
| ⚠️ WEAKLY SUPPORTED | 0 | — |
| ➡️ DIRECTIONAL ONLY | 1 | E2 |
| ⬜ NOT SUPPORTED | 0 | — |
| ❌ FALSIFIED | 0 | — |

### † CI Caveat Claims

**A4: AI-optimisation shifts from explicit scaffolding to implicit generative fingerprints.**
The claim survives BH-FDR correction (q=0.0457) and shows the predicted directional effect, but the bootstrap 95% CI [-0.0205, 0.0012] crosses zero. The rank-based test detects real distributional separation; however, the mean difference is small enough that resampling cannot reliably exclude a null shift. **Interpretation:** The directional signal is real (confirmed by Mann-Whitney), but Δ=-12.6% should be treated as an upper-bound estimate rather than a precise measurement.

### E2 — Governance Density as a Meaningful Negative Finding

The failure of E2 (governance density increase, Δ=+11.0%, d=0.111, p=0.1128) is itself informative. While LLMs demonstrably reshape structural patterns (heading uniformity d=1.081), template conformance (d=0.969), and prose–code ratios, governance language density resists this transformation.

**Why this matters:** Governance documentation (license terms, compliance requirements, code-of-conduct language) is partly constrained by legal and institutional norms rather than authorial style, which limits LLM-driven variation. An alternative (or complementary) explanation is that governance keywords are simply rare and noisy in many repositories (historical IQR 0.18), making any shift hard to detect at this sample size. Either way, the result is consistent with the study measuring genuine generative-behavioural differences rather than a blanket “everything is different” artefact. A metric that *should* resist LLM influence *does* resist it, serving as a plausible internal control for the study.

The negligible effect size (d=0.111) with directional alignment (+11.0%) is consistent with mild LLM over-structuring (e.g., adding “License” sections to READMEs) without changing the underlying semantic density of governance language per unit of text.

---

## §8 — Conclusion

The Documentation Era Shift Index is **0.764** (medium), indicating **moderate evidence of a documentation era shift.**

Of 17 tested claims (after BH-FDR correction at α=0.05):
- 15 are fully supported with meaningful effect sizes and CIs excluding zero
- 1 is supported but with bootstrap CI crossing zero (direction reliable, magnitude uncertain)
- 0 are weakly supported (direction + significance, small effect)
- 1 show the predicted direction but lack statistical significance after correction
- 0 are not supported by the data
- 0 are contradicted by the data (falsified)

The E2 claim failing significance serves as a plausible internal control: governance density (E2) is partly constrained by institutional norms and partly limited by measurement noise (low base-rate, high IQR), and its resistance to LLM influence is consistent with the study measuring genuine generative-behavioural differences.

The A4 claim has CI caveats: the directional signal is confirmed by rank-based testing, but the mean difference is small enough that bootstrap resampling cannot exclude zero. The qualitative finding (direction) is robust; the quantitative magnitude should be treated as an upper-bound estimate.

The strongest signals of the documentation era shift are:
1. **aiSignalMean** — d=1.593 (very large), Δ+97.8%
2. **headingUniformity** — d=1.081 (large), Δ+40.2%
3. **proseRatio** — d=-1.000 (large), Δ-50.2%
4. **templateScore** — d=0.969 (large), Δ+114.2%
5. **tableRatio** — d=0.888 (large), Δ+229.9%

---

**Analysis executed by:** Jay Carpenter  
**SECS Sovereign — Documentation Era Shift Study**

*Generated by SECS Hypothesis Testing Engine v2.0. Statistical methods: Mann-Whitney U test (two-tailed, α=0.05), Cohen's d (pooled SD), Cliff's δ, Bootstrap 95% CI (10,000 iterations), Rank-Biserial correlation. Multiple comparisons: Benjamini-Hochberg FDR (primary), Holm-Bonferroni (comparison), Bonferroni (conservative). All tests are observational — no causal claims are made.*
