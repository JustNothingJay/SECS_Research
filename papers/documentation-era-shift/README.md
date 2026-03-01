# Documentation Era Shift — Hypothesis Test Report v2.0

**Author:** Jay Carpenter
**Date:** 2026-03-01
**Instrument:** SECS MD Scanner v2.1.0 + Hypothesis Testing Engine v2.0
**Study:** 100 historical repos (pre-LLM, established) vs 100 recent repos (Jan–Mar 2026)
**Total files analysed:** 29,419 markdown files

## Key Findings

**Documentation Era Shift Index: 0.764 (medium)**
**Claims supported: 16/17 (94%) | Falsified: 0/17**

### Strongest Effects

| Rank | Metric | Cohen's d | Δ% | Direction |
|---|---|---|---|---|
| 1 | AI Signal (aiSignalMean) | 1.593 (very large) | +97.8% | higher in recent |
| 2 | Heading Uniformity | 1.081 (large) | +40.2% | higher in recent |
| 3 | Prose Ratio | -1.000 (large) | -50.2% | lower in recent |
| 4 | Template Score | 0.969 (large) | +114.2% | higher in recent |
| 5 | Table Ratio | 0.888 (large) | +229.9% | higher in recent |

### Internal Control

E2 (governance density) was the only claim that did not reach statistical significance (p=0.1128, d=0.111). This serves as an internal control: governance documentation is constrained by institutional and legal norms, not authorial style, and its resistance to LLM influence validates that the study measures genuine generative-behavioural differences rather than a blanket "everything is different" artefact.

### Methodology

- Non-parametric: Mann-Whitney U test (two-tailed)
- Effect sizes: Cohen's d (parametric) + Cliff's δ (non-parametric)
- Robustness: Bootstrap 95% CI (10,000 iterations), 20% trimmed means
- Multiple comparisons: Benjamini-Hochberg FDR (primary), Holm-Bonferroni and Bonferroni (comparison)
- All tests are observational — no causal claims are made.

## Files

| File | Description |
|---|---|
| hypothesis-test-report-v2.0.pdf | Full report (PDF) |
| hypothesis-test-report-v2.0.md | Full report (Markdown) |
| hypothesis-test-report-v2.0.json | Structured data (JSON) |

## Citation

```bibtex
@techreport{carpenter2026docshift,
  title   = {Documentation Era Shift: Hypothesis Test Report v2.0},
  author  = {Carpenter, Jay},
  year    = {2026},
  month   = {March},
  institution = {SECS Sovereign},
  type    = {Technical Report},
  url     = {https://github.com/JustNothingJay/SECS_Research/tree/main/papers/documentation-era-shift}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
