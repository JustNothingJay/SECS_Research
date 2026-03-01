# R-003 — Extended Convergence Mapping

**Author:** Jay Carpenter
**Date:** 2026-02-27
**Instrument:** SECS Sovereign Substrate (Analyst Campaign C-003)
**Protocol:** P-002 (Neurotrophic Capability Portrait) — extended cycle mode
**Study:** 12 tests, ~2,221 trajectory data points across 3 seeds. Extended C-002 baseline to mappable convergence data across all four SECS adaptation phases.

## Key Findings

**Disposition: ALL PASS (12/12)**

1. **STDP exponential decay confirmed** — 21-point Δt sweep matches δw = A·exp(−|Δt|/τ) with R² > 0.9
2. **Homeostatic convergence mapped** — 2,000 cycles × 3 seeds; set-point converges to ~0.75 (centre-of-mass of input distribution)
3. **Pruning convergence monotonic** — Node count strictly decreases when growth disabled, reaching steady-state within 200 cycles
4. **Full pipeline bounded** — 500 cycles of A+B+D integration: all weights [0,1], topology constant, homeostatic target stable
5. **Determinism confirmed** — Byte-identical replays across two 500-cycle runs

### Design Observation

O(n²) topology blowup discovered: `StructuralPlasticityController` with growth enabled adds one node per cycle when active ratio exceeds threshold. Over 1,000+ cycles this causes linear topology growth and O(n²) learning operations. Real deployment would cap topology via envelope bounds.

## Files

| File | Description |
|---|---|
| R-003-extended-convergence-mapping.pdf | Full report (PDF) |
| R-003-extended-convergence-mapping.md | Full report (Markdown) |

## Citation

```bibtex
@techreport{carpenter2026r003,
  title   = {R-003: Extended Convergence Mapping},
  author  = {Carpenter, Jay},
  year    = {2026},
  month   = {February},
  institution = {SECS Sovereign},
  type    = {Technical Report},
  url     = {https://github.com/JustNothingJay/SECS_Research/tree/main/papers/extended-convergence-mapping}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
