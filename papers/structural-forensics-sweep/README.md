# R-006 -- Structural Forensics Sweep

**Author:** Jay Carpenter
**Date:** 2026-03-01
**Instrument:** SECS Structural Scanner v1.0.0 + Hypothesis Engine v1.0
**Campaign:** C-006
**Study:** 200 GitHub repositories (100 historical, 100 recent) -- cross-era cohort comparison

## Key Findings

First large-scale structural comparison of pre-AI and AI-era repositories. 10 hypotheses tested, CSDI = 0.674 (CI [0.613, 0.705]).

- **3 SUPPORTED:** AI-era repos show lower max depth, lower orphan-dir ratio, and higher file-to-dir ratio
- **5 FALSIFIED:** No significant difference in naming entropy, root file ratio, mean depth, root config count, or duplicate purpose
- **1 DIRECTIONAL ONLY:** Sub-tree CV difference present but below statistical threshold
- **1 NOT SUPPORTED:** Template fingerprint shows no era effect

AI-era repos are **structurally simpler and flatter**, not more complex. 3 enforcement candidates extracted for v1.9 design phase (subsequently tested in R-006b maturity control).

## Files

- `R-006-structural-forensics-sweep.pdf` -- Full report (PDF)
- `R-006-structural-forensics-sweep.md` -- Full report (Markdown)
