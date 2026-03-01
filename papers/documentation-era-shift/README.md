# Documentation Era Shift — Hypothesis Test Report v2.0

**Author:** Jay Carpenter  
**Date:** 2026-03-01  
**Instrument:** SECS MD Scanner v2.1.0 + Hypothesis Testing Engine v2.0

---

## Key Findings

Top 5 effect sizes (Cohen's d):

| Metric | Cohen's d | Direction |
|---|---|---|
| aiSignalMean | 1.593 | ↑ Recent |
| headingUniformity | 1.081 | ↑ Recent |
| proseRatio | −1.000 | ↓ Recent |
| templateScore | 0.969 | ↑ Recent |
| tableRatio | 0.888 | ↑ Recent |

**Internal control — E2 (governance density):** This metric was designed to resist LLM influence (governance artefacts are human-authored and process-driven). It was the one metric that did not shift significantly between eras, confirming the instrument's discriminant validity.

**Overall result:** 16/17 hypotheses supported, 0 falsified. Composite era shift index: **0.764**.

---

## Methodology

- **Corpus:** 100 historical repositories (pre-2024) + 100 recent repositories (Jan–Mar 2026)
- **Files scanned:** 29,419 Markdown files
- **Statistical tests:** Mann-Whitney U (non-parametric, two-sided)
- **Multiple comparison corrections:**
  - Primary: Benjamini-Hochberg FDR (BH-FDR)
  - Comparison: Holm-Bonferroni and Bonferroni
- **Effect size measures:** Cohen's d and Cliff's δ
- All tests are observational — no causal claims are made.

---

## Files

| File | Format | Description |
|---|---|---|
| hypothesis-test-report-v2.0.pdf | PDF | Full report (typeset) — *to be added once generated* |
| [hypothesis-test-report-v2.0.md](hypothesis-test-report-v2.0.md) | Markdown | Full report (plain text) |
| [hypothesis-test-report-v2.0.json](hypothesis-test-report-v2.0.json) | JSON | Machine-readable results |

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
