# R-007 — Structural Age Regression

> **Report ID:** R-007
> **Campaign:** C-007
> **Author:** Jay Carpenter
> **Date:** 2026-03-03
> **Status:** FINAL
> **Type:** OUTWARD-FACING STRUCTURAL MEASUREMENT — continuous-variable age regression with breakpoint detection
> **Disposition:** 0/3 primary AI-breakpoint hypotheses supported. 3/3 FALSIFIED.
>                  1/2 null (maturity-monotonic) hypotheses confirmed. 1/2 FALSIFIED.
>                  At 10,000-repo scale, no structural breakpoint at the AI transition survives BH-FDR correction for the three C-006b AI-effect metrics.
>                  Maturity is the dominant structural driver. No enforcement candidates emerge.
> **System Under Test:** 9,925 GitHub repositories (10,000 target, 75 failures) across 16 inception-year strata (2010–2026)
> **Suite:** Structural Scanner v1.1 + Continuous Comparison Engine v1.0
> **Campaign Result:** 5 directional hypotheses tested + 4 exploratory. 3 BH-significant breakpoints found — all in exploratory metrics, none in primary AI-effect metrics.
> **Constitutional Source:** D-66, D-68, D-74, D-76 (translations 0011, 0012)
> **Version Arc:** v1.8 — measurement only, no enforcement
> **Parent Campaigns:** C-006 (structural forensics), C-006b (maturity control)

---

## §0 — Executive Summary

C-007 asked: **"How does structural complexity change with repository age, and does the relationship change at the AI transition?"**

The answer: **Complexity changes with age, but the relationship does NOT change at the AI transition** — at least not for the three metrics that C-006b identified as potential AI effects.

### Population

| Parameter | Value |
|-----------|-------|
| Target repos | 10,000 |
| Successfully scanned | 9,925 (99.25%) |
| Failed | 75 (0.75%) |
| Strata | 16 (2010–2024 individual + 2025–2026 combined) |
| Per-stratum target | 625 |
| Age range | 5 – 5,903 days (median 2,984) |
| Stars range | 10 – 572,668 (median 18,605) |
| Language families | 129 → 9 analysis groups |
| Min stars | 10 |
| Exclusions | Forks, archived repos, repos with <5 files |

### Verdict Summary

| Hypothesis | Metric | Type | Breakpoint BH q | Verdict |
|-----------|--------|------|-----------------|---------|
| H7-1 | m1_maxDepth | Primary (AI effect) | 0.065 | **FALSIFIED** |
| H7-2 | m3_namingEntropy | Primary (AI effect) | 0.081 | **FALSIFIED** |
| H7-3 | m4_duplicatePurpose | Primary (AI effect) | 0.188 | **FALSIFIED** |
| H7-4 | m2_rootFileRatio | Null (monotonic) | 0.072 | **SUPPORTED** |
| H7-5 | m7_fileToDirRatio | Null (monotonic) | 0.039 | **FALSIFIED** |

### Exploratory Breakpoints (BH-significant)

| Metric | τ (inception ≈) | BH q | CUSUM | Notes |
|--------|-----------------|------|-------|-------|
| m5_templateFingerprint | 2023-04 | 0.024 | ⚠ UNSTABLE | Not hypothesised as AI effect |
| m7_fileToDirRatio | 2023-11 | 0.039 | ✓ stable | Late-window maturity dynamics |
| rootConfigCount | 2023-02 | 0.037 | ⚠ UNSTABLE | Config accumulation shift |

### Campaign Outcome

This maps to **Outcome #2** from the C-007 specification:

> *No breakpoints for the primary AI-effect metrics → At 10K scale, maturity is the complete explanation for C-006b's AI signals. D-74 is strengthened. v1.9 enforcement remains blocked.*

### Bug Discovery & Correction

During atlas review, a unit-space mismatch was discovered in the breakpoint candidate generation. The engine was using epoch-days (days since 2010-01-01) as split points on the ageDays axis (days since repo creation). This caused the breakpoint search to scan the 11–14 year range instead of the intended 2–5 year AI-transition window. The bug was fixed and the engine re-run. All results in this report reflect the corrected analysis. The correction is documented in §7.

---

## §1 — Methodology

### Instrument: Scanner v1.1

SECS Structural Scanner v1.1 uses the GitHub Trees API to retrieve the complete file tree for each repository in a single API call. No repository content is cloned or read — only tree topology is analysed.

**12-field metadata block:** `ageDays`, `inceptionYear`, `aiEra`, `languageFamily`, `stars`, `forks`, `watchers`, `createdAt`, `updatedAt`, `defaultBranch`, `archived`, `size`.

**Filtering:** Entries under vendor directories (`node_modules`, `.git`, `vendor`, `dist`, `build`, etc.) are excluded.

### Instrument: Continuous Comparison Engine v1.0

Four analysis families, each applied to all 10 metrics:

| Family | Method | Purpose |
|--------|--------|---------|
| 1 — Correlation | Spearman $r_s$ + paired bootstrap CI (5,000 iterations) | Monotonic association strength |
| 2 — Regression | OLS simple + multiple (log(stars) + language dummies) | Effect size, confound control |
| 3 — Breakpoint | Segmented regression + Chow test + CUSUM | Structural break detection |
| 4 — Smoothing | LOESS (bandwidth 0.3) | Non-linear shape diagnostics |

### Multiple Comparison Correction

- **Within-family:** BH-FDR at $\alpha = 0.05$ across $k = 10$ metrics per family
- **Cross-family:** Bonferroni across 3 families ($\alpha/3 = 0.0167$)
- All three families are significant at the cross-family level

### Breakpoint Search Window

Monthly candidates from 2021-01-01 to 2023-12-01 (36 candidates), converted to ageDays relative to the scan date (2026-03-03). This corresponds to repos aged 823–1,887 days, targeting inception dates within the AI transition period (Copilot launch June 2021 through post-ChatGPT stabilisation December 2023).

### Metrics

| # | Metric | Key | C-006b Verdict |
|---|--------|-----|---------------|
| 1 | Max Folder Depth | `m1_maxDepth` | AI EFFECT (borderline) |
| 2 | Mean Folder Depth | `m1_meanDepth` | — (supplementary) |
| 3 | Root File Ratio | `m2_rootFileRatio` | MATURITY EFFECT |
| 4 | Naming Entropy | `m3_namingEntropy` | AI EFFECT |
| 5 | Duplicate-Purpose Dirs | `m4_duplicatePurpose` | AI EFFECT |
| 6 | Template Fingerprint | `m5_templateFingerprint` | Not tested |
| 7 | Orphan Dir Ratio | `m6_orphanDirRatio` | Not tested |
| 8 | File-to-Dir Ratio | `m7_fileToDirRatio` | MATURITY EFFECT |
| 9 | Root Config Count | `rootConfigCount` | Not tested |
| 10 | Sub-tree CV | `subTreeCV` | MIXED |

---

## §2 — Correlation Analysis

All 10 metrics show statistically significant Spearman rank correlations with repo age (all BH $q < 0.05$). However, effect sizes are uniformly small — no $|r_s| > 0.15$.

| Metric | Spearman $r_s$ | Bootstrap 95% CI | BH $q$ | Direction |
|--------|---------------|------------------|--------|-----------|
| m1_maxDepth | −0.032 | [−0.051, −0.014] | 0.002 | Older → deeper |
| m1_meanDepth | −0.056 | [−0.075, −0.037] | < 0.001 | Older → deeper |
| m2_rootFileRatio | +0.035 | [+0.016, +0.055] | < 0.001 | Older → more root files |
| m3_namingEntropy | −0.064 | [−0.084, −0.044] | < 0.001 | Older → lower entropy |
| m4_duplicatePurpose | −0.114 | [−0.134, −0.095] | < 0.001 | Older → fewer duplicates |
| m5_templateFingerprint | −0.023 | [−0.043, −0.004] | 0.025 | Older → less templated |
| m6_orphanDirRatio | +0.022 | [+0.003, +0.042] | 0.029 | Older → more orphans |
| m7_fileToDirRatio | +0.130 | [+0.111, +0.149] | < 0.001 | Older → higher density |
| rootConfigCount | +0.030 | [+0.011, +0.049] | 0.005 | Older → more configs |
| subTreeCV | −0.022 | [−0.041, −0.002] | 0.032 | Older → more uniform |

**Strongest correlation:** m4_duplicatePurpose ($r_s = -0.114$) and m7_fileToDirRatio ($r_s = +0.130$). Both consistent with maturity effects — older repos accumulate files and clean up duplicate-purpose directories over time.

**Key finding:** All correlations are significant by statistical power alone ($n = 9{,}925$). The practical significance is negligible — age explains less than 2% of variance in any single metric.

---

## §3 — Regression Analysis

### Simple OLS

Simple regression of each metric on ageDays confirms the correlation picture: statistically significant but near-zero $R^2$.

| Metric | Slope per 1000d | $R^2$ | $p$ |
|--------|----------------|-------|-----|
| m1_maxDepth | −0.032 | 0.0003 | 0.104 |
| m1_meanDepth | −0.021 | 0.0004 | 0.035 |
| m2_rootFileRatio | +0.007 | 0.0027 | < 0.001 |
| m3_namingEntropy | −0.050 | 0.0023 | < 0.001 |
| m4_duplicatePurpose | −0.291 | 0.0086 | < 0.001 |
| m5_templateFingerprint | −0.006 | 0.0005 | 0.024 |
| m6_orphanDirRatio | +0.004 | 0.0010 | 0.002 |
| m7_fileToDirRatio | −0.877 | 0.0002 | 0.192 |
| rootConfigCount | +0.019 | < 0.001 | 0.512 |
| subTreeCV | −0.004 | < 0.001 | 0.389 |

**Maximum $R^2$:** 0.0086 (m4_duplicatePurpose). Age alone explains less than 1% of variance.

### Multiple Regression (age + log(stars) + language family)

Adding log(stars) and language-family dummies dramatically increases explained variance:

| Metric | Simple $R^2$ | Multiple $R^2$ | Δ $R^2$ | ageDays $\beta$ (per 1000d) | ageDays $p$ |
|--------|-------------|---------------|---------|---------------------------|------------|
| m1_maxDepth | 0.0003 | **0.2971** | +0.297 | −0.182 | < 0.001 |
| m1_meanDepth | 0.0004 | **0.3750** | +0.375 | −0.107 | < 0.001 |
| m2_rootFileRatio | 0.0027 | **0.1360** | +0.133 | +0.010 | < 0.001 |
| m3_namingEntropy | 0.0023 | **0.1694** | +0.167 | −0.078 | < 0.001 |
| m4_duplicatePurpose | 0.0086 | **0.1171** | +0.109 | −0.444 | < 0.001 |
| m5_templateFingerprint | 0.0005 | **0.1626** | +0.162 | −0.013 | < 0.001 |
| m6_orphanDirRatio | 0.0010 | **0.0368** | +0.036 | −0.002 | 0.281 |
| m7_fileToDirRatio | 0.0002 | **0.0026** | +0.002 | −1.060 | 0.139 |
| rootConfigCount | < 0.001 | **0.2200** | +0.220 | +0.065 | 0.019 |
| subTreeCV | < 0.001 | **0.1284** | +0.128 | −0.019 | < 0.001 |

**Key finding:** Language family and project scale (stars) explain 10–38% of structural variance. Once these confounds are controlled, ageDays remains significant for 8/10 metrics — but the effect sizes are small. The structural landscape is shaped primarily by **what kind of project it is**, not when it was created.

---

## §4 — Breakpoint Analysis (Primary Hypotheses)

### H7-1: m1_maxDepth — Structural break at AI transition

**Claim:** Repos created after the AI transition show a different slope in max folder depth vs. age.

| Parameter | Value |
|-----------|-------|
| Optimal τ | 1,583 days (inception ≈ 2021-11-01) |
| Slope below τ (younger repos) | +0.00033 |
| Slope above τ (older repos) | −0.000059 |
| Chow F | 3.262 |
| Chow $p$ (raw) | 0.0392 |
| Chow $q$ (BH) | **0.065** |
| CUSUM | ⚠ UNSTABLE (max dev = 2.676) |
| Segment sizes | $n_{\leq\tau} = 2{,}570$, $n_{>\tau} = 7{,}355$ |

**Verdict: FALSIFIED.** The Chow test $p$-value (0.039) does not survive BH-FDR correction ($q = 0.065 > 0.05$). The CUSUM diagnostic is unstable, further indicating no clean structural break. At 10K scale, there is no significant breakpoint in max folder depth at the AI transition.

The C-006b borderline AI effect ($d = 0.208$, CI crossing zero) does not replicate.

---

### H7-2: m3_namingEntropy — Structural break at AI transition

**Claim:** Repos created after the AI transition show a different slope in naming entropy vs. age.

| Parameter | Value |
|-----------|-------|
| Optimal τ | 1,856 days (inception ≈ 2021-02-01) |
| Slope below τ (younger repos) | +0.000085 |
| Slope above τ (older repos) | −0.000043 |
| Chow F | 2.733 |
| Chow $p$ (raw) | 0.0652 |
| Chow $q$ (BH) | **0.081** |
| CUSUM | ⚠ UNSTABLE (max dev = 2.451) |
| Segment sizes | $n_{\leq\tau} = 3{,}023$, $n_{>\tau} = 6{,}902$ |

**Verdict: FALSIFIED.** Raw $p = 0.065$ is not even nominally significant. BH $q = 0.081$. CUSUM unstable. The C-006b AI effect ($d = 0.420$) does not produce a detectable breakpoint at 10K scale.

---

### H7-3: m4_duplicatePurpose — Structural break at AI transition

**Claim:** Repos created after the AI transition show a different slope in duplicate-purpose directories vs. age.

| Parameter | Value |
|-----------|-------|
| Optimal τ | 1,856 days (inception ≈ 2021-02-01) |
| Slope below τ (younger repos) | +0.000045 |
| Slope above τ (older repos) | −0.000281 |
| Chow F | 1.781 |
| Chow $p$ (raw) | 0.169 |
| Chow $q$ (BH) | **0.188** |
| CUSUM | ✓ stable (max dev = 1.977) |
| Segment sizes | $n_{\leq\tau} = 3{,}023$, $n_{>\tau} = 6{,}902$ |

**Verdict: FALSIFIED.** Raw $p = 0.169$ — clearly not significant. CUSUM is stable, which is consistent with a monotonic decline (older repos have fewer duplicate-purpose directories). The C-006b AI effect ($d = 0.356$) reflects maturity dynamics at 10K scale: m4 shows the strongest Spearman correlation ($r_s = -0.114$) of any metric, and the relationship is smooth and monotonic. There is no transition, just a continuous maturity gradient.

---

## §5 — Breakpoint Analysis (Null Hypotheses)

### H7-4: m2_rootFileRatio — Monotonic (no breakpoint)

**Claim:** The age–root-file-ratio relationship is monotonic — there is no structural break at the AI transition.

| Parameter | Value |
|-----------|-------|
| Optimal τ | 1,856 days (inception ≈ 2021-02-01) |
| Chow $p$ (raw) | 0.036 |
| Chow $q$ (BH) | **0.072** |
| CUSUM | ✓ stable (max dev = 1.970) |

**Verdict: SUPPORTED.** BH $q = 0.072 > 0.05$ — the breakpoint is not significant after correction. CUSUM stable. The C-006b maturity verdict holds at 10K scale. Root-file ratio changes monotonically with age.

---

### H7-5: m7_fileToDirRatio — Monotonic (no breakpoint)

**Claim:** The age–file-to-directory-ratio relationship is monotonic — there is no structural break at the AI transition.

| Parameter | Value |
|-----------|-------|
| Optimal τ | 853 days (inception ≈ **2023-11-01**) |
| Slope below τ (younger repos) | +0.04185 |
| Slope above τ (older repos) | −0.000523 |
| Chow F | 5.649 |
| Chow $p$ (raw) | 0.0039 |
| Chow $q$ (BH) | **0.039** |
| CUSUM | ✓ stable (max dev = 1.109) |
| Segment sizes | $n_{\leq\tau} = 1{,}320$, $n_{>\tau} = 8{,}605$ |

**Verdict: FALSIFIED.** A significant breakpoint is found ($q = 0.039 < 0.05$), rejecting the monotonic null. However, interpretation requires caution:

1. **The breakpoint is at inception ≈ November 2023** — 12 months after ChatGPT. This is at the late edge of the search window, not at the AI transition proper.
2. **The slope change is a growth-curve effect.** Repos younger than ~2.3 years show a steep positive slope (file-to-dir ratio increases rapidly as young repos grow). Repos older than 2.3 years have a near-zero slope (the ratio stabilises). This is consistent with early-life structural dynamics, not AI influence.
3. **C-006b correctly identified m7 as a MATURITY EFFECT.** The breakpoint found here is a maturity-curve inflection point — the transition from rapid structural growth to stability — not an era effect.
4. **CUSUM is stable**, supporting a clean (not noisy) transition.

The formal hypothesis is falsified (a breakpoint exists), but the breakpoint's location and character confirm the maturity-effect interpretation.

---

## §6 — Exploratory Hypotheses

### H7-6: subTreeCV — Non-linear relationship?

| Result | Value |
|--------|-------|
| Spearman $r_s$ | −0.022 (BH $q = 0.032$) |
| Breakpoint BH $q$ | 0.234 (not significant) |
| LOESS range | 1.337 – 1.368 (essentially flat) |
| CUSUM | ✓ stable |

**Finding: Linear/flat model adequate.** Sub-tree CV is essentially constant across all repo ages. Neither non-linear nor breakpoint models are needed. The weak correlation is statistically significant only by power ($n = 9{,}925$); the practical effect is nil.

---

### H7-7: m5_templateFingerprint — Age correlation

| Result | Value |
|--------|-------|
| Spearman $r_s$ | −0.023 (BH $q = 0.025$) |
| Breakpoint τ | 1,067 days (inception ≈ **2023-04-01**) |
| Breakpoint BH $q$ | **0.024** (significant) |
| CUSUM | ⚠ UNSTABLE |
| Slope below τ | −0.000123 |
| Slope above τ | −0.000004 |

**Finding: Weak negative correlation with a significant breakpoint at April 2023.** Younger repos (created after Apr 2023) show a near-zero slope; older repos show a weak declining trend. The CUSUM instability suggests the breakpoint is noisy. Template fingerprint scores are low across the board (median ~0.45) — the practical significance is minimal.

This metric was not hypothesised as an AI effect by C-006b. The breakpoint may reflect changes in scaffolding tool defaults (e.g., Vite replacing CRA in the JS ecosystem).

---

### H7-8: m6_orphanDirRatio — Maturity scaling

| Result | Value |
|--------|-------|
| Spearman $r_s$ | +0.022 (BH $q = 0.029$) |
| Breakpoint BH $q$ | 0.077 (not significant) |
| CUSUM | ⚠ UNSTABLE |

**Finding: Very weak positive correlation, no significant breakpoint.** Orphan directories accumulate slightly with age but the effect is negligible ($R^2 < 0.001$).

---

### H7-9: rootConfigCount — Maturity scaling

| Result | Value |
|--------|-------|
| Spearman $r_s$ | +0.030 (BH $q = 0.005$) |
| Breakpoint τ | 1,126 days (inception ≈ **2023-02-01**) |
| Breakpoint BH $q$ | **0.037** (significant) |
| CUSUM | ⚠ UNSTABLE |
| Slope below τ | +0.001089 |
| Slope above τ | −0.000002 |

**Finding: Significant breakpoint at February 2023 — repos created before this date show a near-zero age slope for config count, while repos created after show a steep positive slope.** This suggests that newer repos accumulate root configs faster, possibly reflecting the proliferation of tooling configs (ESLint, Prettier, Biome, Tailwind, etc.) in recent ecosystems.

However, CUSUM is unstable, and the multiple regression shows that log(stars) is the dominant predictor ($R^2_{multiple} = 0.220$). Config count tracks project scale more than project age.

---

## §7 — Bug Discovery: Breakpoint Candidate Unit Mismatch

During atlas review prior to report generation, a critical unit-space mismatch was discovered in the Continuous Comparison Engine v1.0.

### The Bug

The `generateBreakpointCandidates()` function generated candidate τ values as **epoch-days** (days since 2010-01-01), but the segmented regression's $x$-axis uses **ageDays** (days since repo creation to scan date). These are different units with an inverse relationship:

$$\mathrm{ageDays} = \mathrm{scanEpochDays} - \mathrm{epochDays}$$

Epoch-day candidates ranged from 4,018 to 5,082 — which, when interpreted as ageDays, tested breakpoints at repos aged 11–14 years (inception ≈ 2012–2015). The intended search window was repos aged 823–1,887 days (inception ≈ 2021–2023).

### Impact

The initial engine output reported 6/10 significant breakpoints, all clustering around ageDays 4,138–4,595 (inception ≈ 2013–2014). These results were mathematically valid — there IS a structural change between 11-year-old repos and 14-year-old repos — but they were testing the wrong question. They measured decade-boundary maturity effects, not AI-transition effects.

### Fix

The function was corrected to convert inception dates to ageDays:

```javascript
function generateBreakpointCandidates(scanDateStr) {
  const scanMs = new Date(scanDateStr).getTime();
  const candidates = [];
  for (let year = 2021; year <= 2023; year++) {
    for (let month = 1; month <= 12; month++) {
      const dateMs = new Date(`${year}-${String(month).padStart(2, '0')}-01`).getTime();
      const ageDays = Math.floor((scanMs - dateMs) / 86400000);
      candidates.push(ageDays);
    }
  }
  candidates.sort((a, b) => b - a);
  return candidates;
}
```

The engine was re-run. All results in this report use the corrected analysis.

### Constitutional Note

This bug was caught by the Analyst during systematic atlas review. No external reviewer flagged it. It demonstrates why measurement infrastructure must be re-verified before report generation (D-68) and why the SECS methodology separates implementation (PE) from interpretation (Analyst). The bug was in the PE's implementation; it was caught during Analyst verification.

---

## §8 — Synthesis

### The Master Finding

**Structural complexity varies with repo age, but the relationship is dominated by project type (language, scale), not temporal era.**

| Factor | Typical $R^2$ explained | Evidence |
|--------|------------------------|----------|
| Language family + log(stars) | 0.03 – 0.37 | Multiple regression $\Delta R^2$ |
| Repo age (ageDays) | < 0.01 | Simple regression $R^2$ |
| AI-era breakpoint | Not detected | 0/3 primary breakpoints survive BH |

### What happened to C-006b's AI effects?

C-006b identified three metrics with potential AI effects:

| Metric | C-006b $d$ | C-006b Status | C-007 Breakpoint BH $q$ | C-007 Verdict |
|--------|-----------|---------------|------------------------|---------------|
| m1_maxDepth | 0.208 (borderline) | AI EFFECT | 0.065 | No breakpoint |
| m3_namingEntropy | 0.420 (small) | AI EFFECT | 0.081 | No breakpoint |
| m4_duplicatePurpose | 0.356 (small) | AI EFFECT | 0.188 | No breakpoint |

At 300 repos, categorical era labels (pre-AI vs AI-era) detected small but statistically significant differences. At 9,925 repos, continuous age regression with a 36-candidate breakpoint search in the AI-transition window detects **no significant structural break** in any of these metrics.

**Interpretation:** The C-006b AI effects were real statistical signals in a 300-repo sample. But they reflected the tail end of a smooth maturity gradient, not a discrete technological transition. When the sample grows 33×, the gradient resolves into a continuous age function with no inflection point at the AI boundary.

### Maturity Confirmation

D-74 (maturity dominance) is overwhelmingly supported:

1. **All 10 Spearman correlations are significant** — structural metrics DO change with age.
2. **All are weak** ($|r_s| < 0.15$) — the change is gradual, not dramatic.
3. **No primary AI-effect metric shows a breakpoint** — the change is monotonic.
4. **Language and scale explain 10–38× more variance** than age alone.
5. **m4_duplicatePurpose shows the strongest monotonic trend** ($r_s = -0.114$, CUSUM stable) — this was C-006b's strongest AI effect, but it's actually the poster child for maturity.

### The Three Exploratory Breakpoints

Three BH-significant breakpoints were found in non-primary metrics:

1. **m5_templateFingerprint** (τ ≈ April 2023): Possibly reflects ecosystem tooling shifts (CRA → Vite transition). CUSUM unstable.
2. **m7_fileToDirRatio** (τ ≈ November 2023): Early-life growth dynamics. CUSUM stable — the cleanest breakpoint in the entire analysis. But it's a maturity inflection, not an AI effect.
3. **rootConfigCount** (τ ≈ February 2023): Config proliferation shift. CUSUM unstable.

None of these were hypothesised as AI effects. None represent enforcement candidates.

---

## §9 — Enforcement Implications

| Question | Answer |
|----------|--------|
| Do AI-era repos have structurally distinct breakpoints? | **No** (0/3 primary hypotheses supported) |
| Should v1.9 introduce structural enforcement rules? | **No** — no metric shows a reliable AI-specific structural pattern |
| Are any metrics candidates for enforcement? | **No** — all significant breakpoints are in exploratory metrics with CUSUM instability or maturity-curve explanations |
| Is D-74 (maturity dominance) upheld? | **Yes** — overwhelmingly |
| Is D-76 (no enforcement without evidence) satisfied? | **Yes** — evidence does not support enforcement |

**Enforcement status: BLOCKED.** v1.9 cannot introduce structural enforcement rules based on C-007 results. The substrate remains measurement-only.

---

## §10 — Limitations

1. **Cross-sectional, not longitudinal.** Each repo is scanned once. We measure age-at-scan, not structural evolution over time. The "structural age reset" hypothesis cannot be tested without longitudinal data.

2. **Selection bias.** Stars-sorted sampling biases toward visible projects. The structural population may not represent the full GitHub ecosystem. Repos with 0–9 stars are excluded.

3. **Survivorship bias.** Repos created in 2010 and still active today are survivors. Abandoned/deleted repos cannot be measured. This inflates structural quality estimates for older repos.

4. **Language confounds.** Multiple regression controls for 9 language families but not framework-specific effects. The m5_templateFingerprint breakpoint may reflect framework transitions (e.g., CRA → Vite).

5. **AI transition is gradual, not binary.** The breakpoint search window (2021–2023) captures the range from Copilot launch through ChatGPT stabilisation. But the transition is a gradient, and a single breakpoint test may not capture diffuse adoption.

6. **Small effect sizes throughout.** Even significant correlations explain < 2% of variance. Structural complexity is dominated by factors not captured in this analysis (project domain, team size, architecture philosophy).

---

## §11 — Artefacts

| Artefact | Path | Size |
|---------|------|------|
| Regression atlas (Markdown) | `auditor/structural-reports/hypothesis/structural-regression-atlas-C-007.md` | 16 KB |
| Regression atlas (JSON) | `auditor/structural-reports/hypothesis/structural-regression-atlas-C-007.json` | 3 MB |
| Per-repo scans | `auditor/structural-reports/C-007/{owner}__{repo}.json` | 9,925 files |
| Population summary | `auditor/structural-reports/C-007/summary.json` | 10.3 MB |
| Per-metric CSV | `auditor/structural-reports/C-007/metric-*.csv` | 10 files |
| Campaign specification | `analyst/campaigns/C-007-structural-age-regression.md` | — |
| Scanner v1.1 | `auditor/structural-scan-v1.1.mjs` | — |
| Continuous Comparison Engine | `auditor/continuous-comparison-engine.mjs` | — |

---

## §12 — Constitutional Record

| Item | Value |
|------|-------|
| Campaign | C-007 Structural Age Regression |
| Constitutional source | D-66, D-68, D-74, D-76 |
| Version arc position | v1.8 (measurement only) |
| Scale | 9,925 repos (33× C-006/C-006b combined) |
| Independent variable | `ageDays` (continuous) |
| Hypotheses tested | 5 directional + 4 exploratory |
| Starting evidence | 3 AI effects from C-006b (m1 borderline, m3, m4) |
| Primary result | 0/3 AI-effect breakpoints survive BH-FDR |
| Null hypotheses | 1/2 confirmed (m2 monotonic), 1/2 falsified (m7 growth-curve inflection) |
| Enforcement candidates | **None** |
| D-74 status | **STRENGTHENED** |
| D-76 compliance | **SATISFIED** — no enforcement proposed |
| Substrate modifications | Zero (D-68 compliance) |
| Bug discovered | Breakpoint candidate unit mismatch — fixed and re-run |
| Cross-campaign validation | C-006/C-006b repos flagged with `metadata.c006Cohort` |

---

*C-006 asked "are they different?" (Yes, CSDI = 0.674.) C-006b asked "is it maturity?" (Mostly, 0/2 enforcement candidates survived.) C-007 asked "how does the relationship actually work?" (Smooth age gradient, no AI-transition breakpoint, language and scale dominate.) Three campaigns, 10,425 repos, one answer: structural complexity is a function of what you build and how long you build it, not when the tools changed.*
