# Documentation Era Shift — Hypothesis Test Report v2.0

**Author:** Jay Carpenter  
**Date:** 2026-03-01  
**Instrument:** SECS MD Scanner v2.1.0 + Hypothesis Testing Engine v2.0  
**License:** CC BY 4.0

---

## Abstract

A large-scale observational study of Markdown documentation across 200 GitHub repositories (100 historical, 100 recent) reveals a statistically significant and practically large shift in documentation structure, style, and content between the pre-LLM era and the 2024–2026 period. 29,419 Markdown files were scanned. 17 hypotheses were tested using Mann-Whitney U tests with Benjamini-Hochberg FDR correction. 16 of 17 hypotheses were supported; 0 were falsified. The composite era shift index is 0.764.

---

## 1. Introduction

Documentation is a key artefact in software engineering. The emergence of large language model (LLM) tooling in 2022–2024 is hypothesised to have materially altered documentation patterns — in structure, density, style, and signal composition. This report operationalises that hypothesis into 17 measurable sub-hypotheses and tests each against a corpus of public GitHub repositories.

The study is observational. No causal claims are made. The goal is to characterise the shift, not to attribute it.

---

## 2. Corpus

| Property | Value |
|---|---|
| Total repositories | 200 |
| Historical repos (pre-2024) | 100 |
| Recent repos (Jan–Mar 2026) | 100 |
| Total MD files scanned | 29,419 |
| Instrument | SECS MD Scanner v2.1.0 |

---

## 3. Hypotheses

| ID | Hypothesis | Supported | p (BH-FDR) | Cohen's d | Cliff's δ |
|---|---|---|---|---|---|
| H1 | AI signal mean is higher in recent repos | Yes | < 0.001 | 1.593 | 0.712 |
| H2 | Heading uniformity is higher in recent repos | Yes | < 0.001 | 1.081 | 0.634 |
| H3 | Prose ratio is lower in recent repos | Yes | < 0.001 | −1.000 | −0.598 |
| H4 | Template score is higher in recent repos | Yes | < 0.001 | 0.969 | 0.621 |
| H5 | Table ratio is higher in recent repos | Yes | < 0.001 | 0.888 | 0.589 |
| H6 | Badge count is higher in recent repos | Yes | 0.003 | 0.741 | 0.511 |
| H7 | Code block ratio is higher in recent repos | Yes | 0.004 | 0.698 | 0.487 |
| H8 | Link density is higher in recent repos | Yes | 0.006 | 0.671 | 0.469 |
| H9 | Section count is higher in recent repos | Yes | 0.008 | 0.643 | 0.452 |
| H10 | Word count per section is lower in recent repos | Yes | 0.012 | −0.612 | −0.431 |
| H11 | List density is higher in recent repos | Yes | 0.014 | 0.589 | 0.418 |
| H12 | Emoji frequency is higher in recent repos | Yes | 0.018 | 0.561 | 0.401 |
| H13 | Readability score differs between eras | Yes | 0.022 | 0.534 | 0.383 |
| H14 | Header depth variance is lower in recent repos | Yes | 0.031 | −0.498 | −0.358 |
| H15 | Frontmatter presence is higher in recent repos | Yes | 0.038 | 0.471 | 0.341 |
| H16 | Sentence length variance is lower in recent repos | Yes | 0.044 | −0.443 | −0.321 |
| E2 | Governance density is unchanged between eras (control) | Control | 0.412 | 0.089 | 0.063 |

---

## 4. Key Findings

### 4.1 Top Effect Sizes

1. **aiSignalMean** d=1.593 — the strongest signal; AI-characteristic phrasing and structure is markedly more prevalent in recent documentation.
2. **headingUniformity** d=1.081 — recent repos show significantly more uniform heading hierarchies.
3. **proseRatio** d=−1.000 — prose as a fraction of total content has declined sharply; structured elements (lists, tables, code) have displaced running text.
4. **templateScore** d=0.969 — recent documentation more closely matches template-driven scaffolding patterns.
5. **tableRatio** d=0.888 — tabular presentation of information has increased substantially.

### 4.2 Internal Control

**E2 (governance density)** was included as an internal control. Governance artefacts (CODEOWNERS, CONTRIBUTING.md policy sections, security policies) are primarily human-authored and process-driven. The hypothesis was that governance density should *not* shift with LLM tooling adoption. The result confirms this: p=0.412, d=0.089. This validates the discriminant validity of the instrument.

### 4.3 Composite Era Shift Index

The composite era shift index aggregates the per-hypothesis effect magnitudes into a single summary statistic (0 = no shift, 1 = complete separation). The index for this study is **0.764**, indicating a large and practically significant era shift.

---

## 5. Methodology

### 5.1 Repository Selection

Repositories were selected from GitHub using the SECS MD Scanner's corpus construction pipeline. Historical repos were last updated before 2024-01-01. Recent repos were last updated between 2026-01-01 and 2026-03-01. Minimum 10 Markdown files per repository. No forks.

### 5.2 Statistical Tests

- **Primary test:** Mann-Whitney U (non-parametric, two-sided, α=0.05)
- **Multiple comparison correction (primary):** Benjamini-Hochberg FDR
- **Comparison corrections:** Holm-Bonferroni, Bonferroni
- **Effect sizes:** Cohen's d (standardised mean difference), Cliff's δ (non-parametric)

### 5.3 Instrument

SECS MD Scanner v2.1.0 extracts 40+ features from each Markdown file. Hypothesis Testing Engine v2.0 applies the statistical pipeline described above.

---

## 6. Conclusion

The documentation era shift is real, large, and consistent across 16 of 17 tested dimensions. The single non-significant result (governance density) is theoretically predicted and validates the instrument. The composite era shift index of 0.764 places this shift in the "large" category by conventional thresholds.

All findings are observational. The study does not claim that LLM tooling *caused* these changes; it characterises what changed and when.

---

## Disclaimer

All tests are observational — no causal claims are made.

---

## Citation

```bibtex
@techreport{carpenter2026docera,
  author      = {Jay Carpenter},
  title       = {Documentation Era Shift --- Hypothesis Test Report v2.0},
  institution = {SECS Research},
  year        = {2026},
  month       = {March},
  url         = {https://github.com/JustNothingJay/SECS_Research/tree/main/papers/documentation-era-shift},
  note        = {Produced by SECS MD Scanner v2.1.0 + Hypothesis Testing Engine v2.0.
                 29,419 MD files, 200 GitHub repositories, 17 hypotheses.
                 Licensed under CC BY 4.0.}
}
```
