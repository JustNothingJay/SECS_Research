# R-002 — Neurotrophic Capability Baseline

**Author:** Jay Carpenter
**Date:** 2026-02-27
**Instrument:** SECS Sovereign Substrate (Analyst Campaign C-002)
**Protocol:** P-002 (Neurotrophic Capability Portrait)
**Study:** 10 hypotheses, 36 tests, ~12,850 adaptation cycles across 3 deterministic seeds (42, 137, 2026)

## Key Findings

All 36 tests pass across all four neurotrophic phases (A–D). **10/10 hypotheses confirmed.**

| ID | Hypothesis | Result | Confidence |
|---|---|---|---|
| H1 | Homeostatic convergence within 200 cycles | **PASS** | High |
| H2 | Deterministic replay at 1K and 5K | **PASS** | High |
| H3 | Activity-gated structural growth and pruning | **PASS** | Medium |
| H4 | Plasticity envelope caps enforced | **PASS** | High |
| H5 | Fault repair within cycle | **PASS** | Low |
| H6 | Hebbian learning proportional to co-activity | **PASS** | High |
| H7 | STDP asymmetric with correct signs | **PASS** | Medium |
| H8 | Learning envelope rejects excess | **PASS** | High |
| H9 | Proof tokens on all mutations | **PASS** (with B-001 boundary) | High |
| H10 | Full pipeline convergence (A+B+D, 500 cycles) | **PASS** | Medium |

### Boundaries Discovered

- **B-001:** Phase B plasticity events carry `proof: null` — mutations are authorized at the registry level but events don't carry proof attestation
- **B-002:** Meta-learning not implemented — `LearningParameters` are fixed; no self-adaptation of learning rules

## Files

| File | Description |
|---|---|
| R-002-neurotrophic-capability-baseline.pdf | Full report (PDF) |
| R-002-neurotrophic-capability-baseline.md | Full report (Markdown) |

## Citation

```bibtex
@techreport{carpenter2026r002,
  title   = {R-002: Neurotrophic Capability Baseline},
  author  = {Carpenter, Jay},
  year    = {2026},
  month   = {February},
  institution = {SECS Sovereign},
  type    = {Technical Report},
  url     = {https://github.com/JustNothingJay/SECS_Research/tree/main/papers/neurotrophic-capability-baseline}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
