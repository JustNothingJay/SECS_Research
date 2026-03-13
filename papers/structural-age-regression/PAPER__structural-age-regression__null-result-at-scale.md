---
title: "The Null Result at Scale: Structural Entropy in 9,925 Repositories Is Driven by Age, Not AI"
author: "Jay Carpenter"
date: "March 2026"
abstract: |
  Three successive measurement campaigns — covering 200, 300, and 9,925 GitHub repositories — tested whether AI-assisted development has changed the structural topology of codebases. The first campaign (C-006) found large structural differences between pre-AI and AI-era repositories (CSDI = 0.674). The second (C-006b) introduced a maturity-matched control cohort and showed that most differences were age effects; three metrics survived as potential AI signals. The third (C-007) scaled to 9,925 repositories and treated age as a continuous variable with breakpoint detection across a 36-month AI-transition window. All three AI-effect hypotheses were falsified. No structural breakpoint at the AI transition survives multiple-comparison correction. Structural complexity is a monotonic function of project age, modulated by language family and project scale. AI tooling — including Copilot, ChatGPT, and subsequent models — has produced no detectable structural signature at the macro level. The implications for code-quality measurement and drift detection are discussed.
---

# 1. Introduction

The rapid adoption of AI-assisted coding tools — GitHub Copilot (June 2021), ChatGPT (November 2022), and subsequent model generations — has prompted urgent questions about their effect on software quality. Does AI-generated code increase structural complexity? Does it introduce new patterns of drift? Does it degrade or improve the topological organisation of codebases?

These questions are typically addressed through code-level analysis: syntax patterns, bug density, test coverage. This paper takes a different approach. We measure **structural topology** — the shape of the file tree itself — across 9,925 repositories spanning 16 years of inception dates (2010–2026). The question is not whether AI changes *code*, but whether AI changes the *structure that holds code*.

The answer, at the scale we measured, is no.

This paper reports the arc of three campaigns that progressively refined that answer:

- **C-006** (200 repos): Found large structural divergence between eras (CSDI = 0.674). Identified enforcement candidates.
- **C-006b** (300 repos): Introduced maturity-matched controls. Most divergence explained by project age. Three metrics survived as potential AI effects.
- **C-007** (9,925 repos): Continuous age regression with breakpoint detection. All three AI-effect hypotheses falsified. Maturity is the complete structural driver.

# 2. Instruments

## 2.1 SECS Structural Scanner

All three campaigns used the SECS Structural Scanner (v1.0 for C-006/C-006b, v1.1 for C-007), which retrieves the complete file tree for each repository via GitHub's Trees API in a single call. No repository content is cloned or read — only tree topology is analysed.

Vendor directories (`node_modules`, `.git`, `vendor`, `dist`, `build`, etc.) are excluded from all metrics to measure authored structure, not dependency artefacts.

### Metrics

| # | Metric | Definition |
|---|--------|-----------|
| 1 | Max Folder Depth | Maximum nesting depth of any file/directory |
| 2 | Root File Ratio | Files at root ÷ total files |
| 3 | Naming Entropy | Shannon entropy of name tokens (split on separators + camelCase) |
| 4 | Duplicate-Purpose Dirs | Directories with semantically overlapping roles |
| 5 | Template Fingerprint | Best match against 15 scaffolding signatures (0–1) |
| 6 | Orphan Dir Ratio | Leaf directories with ≤1 file ÷ total leaf directories |
| 7 | File-to-Dir Ratio | Total files ÷ total directories |
| — | Root Config Count | Config/dotfiles at root |
| — | Sub-tree CV | CV of top-level subdirectory file counts |

## 2.2 Hypothesis Engine (C-006, C-006b)

Mann-Whitney U (two-tailed), Cohen's $d$ (pooled SD), Cliff's $\delta$ (dominance probability), bootstrap 95% CI (10,000 iterations). Multiple comparison correction via Benjamini-Hochberg FDR at $\alpha = 0.05$.

## 2.3 Continuous Comparison Engine (C-007)

Four analysis families applied to all 10 metrics:

| Family | Method | Purpose |
|--------|--------|---------|
| Correlation | Spearman $r_s$ + paired bootstrap CI (5,000 iterations) | Monotonic association strength |
| Regression | OLS simple + multiple (log(stars) + language dummies) | Effect size, confound control |
| Breakpoint | Segmented regression + Chow test + CUSUM | Structural break detection |
| Smoothing | LOESS (bandwidth 0.3) | Non-linear shape diagnostics |

Breakpoint candidates: 36 monthly split points from 2021-01 to 2023-12, converted to `ageDays` relative to scan date. BH-FDR correction across 10 metrics per family. Cross-family Bonferroni ($\alpha/3 = 0.0167$).

# 3. Campaign 1 — Structural Forensics (C-006)

## 3.1 Design

200 repositories: 100 historical (created pre-2015, 1,000+ stars), 100 recent (created 2025–2026, 50+ stars). Binary era comparison.

## 3.2 Results

**Composite Structural Drift Index (CSDI): 0.674** (bootstrap 95% CI: [0.613, 0.705]).

Large structural divergence. AI-era repositories are structurally simpler and flatter — not more complex.

| Metric | Cohen's $d$ | Direction |
|--------|------------|-----------|
| Max Folder Depth | −1.416 | Recent repos are shallower |
| Naming Entropy | −1.385 | Recent repos have lower entropy |
| Duplicate-Purpose | −0.994 | Recent repos have fewer duplicates |
| Sub-tree CV | −0.946 | Recent repos are more homogeneous |
| Root Config Count | −0.858 | Recent repos have fewer root configs |
| Root File Ratio | +0.829 | Recent repos have higher root ratio |
| File-to-Dir Ratio | −0.265 | Recent repos have lower density |

Three enforcement candidates were extracted for further investigation: naming entropy ($d = -1.385$), duplicate-purpose directories ($d = -0.994$), and sub-tree CV ($d = -0.946$).

## 3.3 Limitation

The design compares 10+-year-old repositories against weeks-old repositories. Any structural difference could be a maturity effect — older projects accumulate complexity over time — rather than an AI effect.

# 4. Campaign 2 — Maturity Control (C-006b)

## 4.1 Design

100 additional repositories (created 2018–2019, 50–2,000 stars, pre-Copilot/ChatGPT) scanned with the same instrument. This cohort was created in the pre-AI era but has had 6–7 years to mature. It resolves the primary confound:

- If pre-AI early ≈ historical → maturity drives structure
- If pre-AI early ≈ recent → era drives structure
- If pre-AI early is intermediate → both effects present

## 4.2 Results

| Metric | C-006 $d$ | Pre-AI vs Recent $d$ | Verdict |
|--------|-----------|---------------------|---------|
| Max Folder Depth | −1.416 | 0.208 | **AI EFFECT** (borderline) |
| Root File Ratio | +0.829 | −0.256 | **MATURITY EFFECT** |
| Naming Entropy | −1.385 | 0.420 | **AI EFFECT** |
| Duplicate-Purpose | −0.994 | 0.356 | **AI EFFECT** |
| File-to-Dir Ratio | −0.265 | −0.263 | **MATURITY EFFECT** |
| Sub-tree CV | −0.946 | 0.403 | **MIXED** |

The C-006 enforcement candidates (file-to-dir ratio, sub-tree CV) did not survive maturity control. Three metrics retained small AI-effect signals: max depth ($d = 0.208$, borderline), naming entropy ($d = 0.420$), and duplicate-purpose directories ($d = 0.356$).

## 4.3 Remaining Question

At 300 repos with categorical era labels, small AI effects are detectable. But are they real structural transitions, or the tail end of a continuous maturity gradient that happens to be sampled at different points?

# 5. Campaign 3 — Continuous Age Regression (C-007)

## 5.1 Design

9,925 repositories (10,000 target, 75 scan failures, 99.25% success rate). 16 inception-year strata (2010–2026), 625 repos per stratum. Stars ≥ 10. Age range: 5–5,903 days (median 2,984).

Age treated as a continuous independent variable. No categorical era labels in the primary analysis. Breakpoint detection via segmented regression + Chow test across 36 monthly candidates in the AI-transition window (2021-01 to 2023-12).

## 5.2 Correlation Analysis

All 10 metrics show statistically significant Spearman correlations with repo age ($n = 9{,}925$, all BH $q < 0.05$). All are weak — no $|r_s| > 0.15$.

| Metric | Spearman $r_s$ | Direction |
|--------|---------------|-----------|
| Naming Entropy | −0.064 | Older → lower entropy |
| Duplicate-Purpose | −0.114 | Older → fewer duplicates |
| Max Folder Depth | −0.032 | Older → deeper |
| File-to-Dir Ratio | +0.130 | Older → higher density |
| Root File Ratio | +0.035 | Older → more root files |

Strongest correlation: $r_s = +0.130$ (file-to-dir ratio). Age explains less than 2% of variance in any single metric.

## 5.3 Multiple Regression

Adding log(stars) and language-family dummies dramatically increases explained variance:

| Metric | Age-only $R^2$ | Full model $R^2$ | $\Delta R^2$ |
|--------|---------------|-----------------|-------------|
| Mean Depth | 0.0004 | **0.3750** | +0.375 |
| Max Depth | 0.0003 | **0.2971** | +0.297 |
| Root Config Count | < 0.001 | **0.2200** | +0.220 |
| Naming Entropy | 0.0023 | **0.1694** | +0.167 |
| Template Fingerprint | 0.0005 | **0.1626** | +0.162 |

Language family and project scale explain 10–38% of structural variance. Age contributes less than 1%. The structural landscape is shaped by **what you build**, not when you built it.

## 5.4 Breakpoint Analysis — Primary Hypotheses

The three C-006b AI-effect metrics were tested for structural breaks in the AI-transition window:

| Metric | C-006b $d$ | Optimal $\tau$ | Chow $p$ (raw) | BH $q$ | CUSUM | Verdict |
|--------|-----------|---------------|----------------|--------|-------|---------|
| Max Depth | 0.208 | 2021-11 | 0.039 | 0.065 | Unstable | **FALSIFIED** |
| Naming Entropy | 0.420 | 2021-02 | 0.065 | 0.081 | Unstable | **FALSIFIED** |
| Duplicate-Purpose | 0.356 | 2021-02 | 0.169 | 0.188 | Stable | **FALSIFIED** |

**All three AI-effect hypotheses are falsified.** No structural breakpoint at the AI transition survives BH-FDR correction. CUSUM diagnostics are unstable for two of three, indicating no clean structural break.

## 5.5 Exploratory Breakpoints

Three BH-significant breakpoints were found in non-primary metrics:

| Metric | $\tau$ (inception) | BH $q$ | CUSUM | Interpretation |
|--------|-------------------|--------|-------|----------------|
| Template Fingerprint | 2023-04 | 0.024 | Unstable | Ecosystem tooling shift (CRA → Vite) |
| File-to-Dir Ratio | 2023-11 | 0.039 | Stable | Early-life growth inflection |
| Root Config Count | 2023-02 | 0.037 | Unstable | Config proliferation shift |

None were hypothesised as AI effects. None represent structural transitions attributable to AI tooling. The cleanest breakpoint (file-to-dir ratio, CUSUM stable) reflects a maturity inflection — repos younger than ~2.3 years grow rapidly, then stabilise.

## 5.6 Bug Discovery

During atlas review, a unit-space mismatch was discovered in the breakpoint candidate generation. The engine was generating epoch-days (days since 2010-01-01) but the regression axis uses ageDays (days since repo creation). This caused the initial search to scan the 11–14-year range instead of the 2–5-year AI-transition window. The bug was caught during analyst verification, corrected, and the engine re-run. All results in this paper use the corrected analysis.

This is documented because measurement integrity requires it, and because the bug itself is instructive: the initial (incorrect) analysis found 6/10 significant breakpoints clustering around 2013–2014. These were real effects — there IS structural change between decade-old repos — but they answered the wrong question.

# 6. Synthesis

## 6.1 The Arc

| Campaign | Repos | Finding |
|----------|-------|---------|
| C-006 | 200 | Large structural divergence (CSDI = 0.674). AI-era repos are simpler. |
| C-006b | 300 | Most divergence is maturity. 3 small AI effects survive ($d$ = 0.2–0.4). |
| C-007 | 9,925 | AI effects vanish. No breakpoint at the AI transition. Maturity is the full explanation. |

The C-006b AI effects were real statistical signals in a 300-repo sample. They reflected the tail end of a smooth maturity gradient, not a discrete technological transition. When the sample grew 33×, the gradient resolved into a continuous age function with no inflection at the AI boundary.

## 6.2 What Drives Structural Complexity

| Factor | Variance explained | Evidence |
|--------|-------------------|----------|
| Language family + scale | 10–38% | Multiple regression $\Delta R^2$ |
| Repo age | < 1% | Simple regression $R^2$ |
| AI-era transition | Not detected | 0/3 breakpoints survive BH-FDR |

Structure is determined by what you build (language, framework, ecosystem norms) and to a lesser extent by how long you've been building it. The tools used to write the code — human or AI — leave no detectable structural signature at this measurement scale.

## 6.3 Maturity as Mechanism

Structural complexity correlates with age, but weakly ($|r_s| < 0.15$, $R^2 < 0.01$). The correlation is real but explains almost nothing. This is consistent with a model where:

- Young repositories start with a scaffolded template (low depth, low entropy, high template fingerprint).
- Over years, they accumulate depth, naming variation, configuration files, and orphan directories.
- This accumulation is gradual and monotonic — there are no abrupt transitions, no era-specific inflections.

The effect is small because maturity itself is a proxy. The actual drivers are likely the decisions made *during* ageing — scope expansion, team changes, technology migrations, process shifts — none of which are captured by tree topology alone.

# 7. Limitations

1. **Cross-sectional, not longitudinal.** Each repo is scanned once. We measure age-at-scan, not structural evolution over time.

2. **Selection bias.** Stars-sorted sampling biases toward visible, maintained projects. The structural population may not represent the full GitHub ecosystem.

3. **Survivorship bias.** Repos from 2010 still active today are survivors. Abandoned repos cannot be measured. This inflates structural quality estimates for older repos.

4. **Metric scope.** All metrics measure tree topology: depth, density, naming patterns, directory structure. They do not measure code semantics, implementation patterns, dependency graphs, or runtime behaviour. Structural metrics are a useful but narrow lens.

5. **AI transition is a gradient.** The breakpoint search tests for a single structural break across a 36-month window. A diffuse, gradual adoption pattern would not produce a detectable breakpoint even if cumulative effects exist.

6. **Small effect sizes throughout.** Even significant correlations explain < 2% of variance. Structural complexity is dominated by factors not captured in this analysis.

# 8. Implications

The null result has practical consequences.

**For AI governance:** structural topology — file depth, naming entropy, directory organisation — is not a reliable signal for detecting AI involvement in a codebase. Tools that rely on structural metrics to flag AI-generated code will produce false negatives at scale.

**For code quality measurement:** structural entropy increases with age, but the increase is small, monotonic, and indistinguishable between human-maintained and AI-assisted projects. Age is the driver, not the tool.

**For drift detection:** if structural drift is not the layer where AI's effect manifests, the question becomes: where does it manifest? Structural metrics measure the skeleton. They do not measure the tissue — implementation idioms, API usage patterns, dependency coupling, semantic consistency. The absence of structural signal does not imply the absence of signal. It implies that the instrument measured the wrong layer.

# References

1. J. Carpenter, "R-006 — Structural Forensics Sweep," SECS Sovereign, March 2026. 200 repositories, CSDI = 0.674.
2. J. Carpenter, "R-006b — Maturity-Controlled Structural Forensics," SECS Sovereign, March 2026. 300 repositories, maturity control.
3. J. Carpenter, "R-007 — Structural Age Regression," SECS Sovereign, March 2026. 9,925 repositories, continuous age regression.
4. GitHub, "Trees API," GitHub REST API Documentation. https://docs.github.com/en/rest/git/trees
5. Y. Benjamini and Y. Hochberg, "Controlling the false discovery rate: a practical and powerful approach to multiple testing," *JRSS-B*, 57(1), pp. 289–300, 1995.
