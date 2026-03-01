# R-005 — E/I Balance Sweep Exploration

**Author:** Jay Carpenter
**Date:** 2026-02-28
**Instrument:** SECS Sovereign Substrate (Analyst Campaign C-005)
**Protocol:** P-004
**Type:** Computational Exploration — not a biological or clinical claim
**Study:** 18-value sweep of `targetEntropy` ∈ [0.05, 0.90], 1,000 cycles per run, 3 seeds (42, 137, 2026), 54 configurations, 10,800 trajectory samples

## Key Findings

**Disposition: ALL PASS (10/10) — 5 hypotheses, 10 test cases**

1. **Single attractor basin** — The controller has one attractor covering the entire research envelope [0.05, 0.90]. No bifurcations, no multi-modal attractors, no divergent regimes. Every initial condition converges to the same steady state (~0.75, the observation distribution mean).
2. **Convergence speed is monotonic** — Configurations at 0.65–0.75 converge in 1 cycle; low targets (0.05–0.35) require 22–29 cycles (~3% of total run)
3. **Asymmetric transient** — Controller corrects more rapidly from above the attractor (0.90 → 4 cycles) than below (0.05 → 29 cycles)
4. **Zero vetoes** — Entire research envelope is unconditionally safe. No configurations triggered envelope vetoes, warnings, or boundary contacts
5. **Oscillation amplitude uniform** — Steady-state oscillation (0.4–0.5) is driven by stochastic observations, not initial target
6. **Deterministic replay byte-identical** — Per-seed; different seeds produce different observation sequences → different transients to the same attractor
7. **Cross-seed consistency** — Mean spread 0.056 < 0.15 threshold at both probed targets

## Files

| File | Description |
|---|---|
| R-005-ei-balance-sweep-exploration.pdf | Full report (PDF) |
| R-005-ei-balance-sweep-exploration.md | Full report (Markdown) |

## Citation

```bibtex
@techreport{carpenter2026r005,
  title   = {R-005: E/I Balance Sweep Exploration},
  author  = {Carpenter, Jay},
  year    = {2026},
  month   = {February},
  institution = {SECS Sovereign},
  type    = {Technical Report},
  url     = {https://github.com/JustNothingJay/SECS_Research/tree/main/papers/ei-balance-sweep-exploration}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
