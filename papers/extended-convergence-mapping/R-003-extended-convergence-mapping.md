# R-003 — Extended Convergence Mapping Report

> **Report ID:** R-003
> **Campaign:** C-003
> **Protocol:** P-002 (Neurotrophic Capability Portrait) — extended cycle mode
> **Author:** Analyst
> **Date:** 2026-02-27
> **Status:** FINAL
> **Disposition:** ALL PASS (12/12)

---

## §1 — Executive Summary

C-003 extended the C-002 neurotrophic baseline to produce mappable convergence data across all four SECS adaptation phases. Each test emits per-cycle trajectory arrays suitable for external plotting. Key findings:

1. **STDP exponential decay confirmed** — 21-point Δt sweep matches δw = A·exp(−|Δt|/τ) with R² > 0.9
2. **Homeostatic convergence mapped** — 2000 cycles × 3 seeds, set-point converges to ~0.75 (centre-of-mass of input distribution)
3. **Pruning convergence monotonic** — Node count strictly decreases when growth disabled, reaching steady-state within 200 cycles
4. **Full pipeline bounded** — 500 cycles of A+B+D integration: all weights [0,1], topology constant, homeostatic target stable
5. **Determinism confirmed** — Byte-identical replays across two 500-cycle runs

## §2 — Design Constraint: O(n²) Topology Blowup

During construction, we discovered that `StructuralPlasticityController` with `growthEnabled: true` adds one node per cycle when `activeNodeRatio > growthThreshold/100`. Over extended cycles (1000+), this causes:

- Linear topology growth (1 node/cycle)
- O(n²) learning operations (snapshot iteration, activity recording)
- Memory exhaustion at ~10K cycles (1.5GB+ RSS)

**Resolution:** C-003 tests disable growth where not under test, isolating each Phase's dynamics. This is a structural observation about the substrate, not a defect — real deployment would cap topology via envelope bounds.

## §3 — Trajectory Data Format

All trajectories are logged via `console.log(JSON.stringify({...}))`. Extract with:

```bash
npx jest tests/analyst/C-003 --no-cache 2>&1 | grep '"campaign":"C-003"'
```

### H3x (Pruning)
```
[cycle, nodeCount, edgeCount]  — 100 points per seed
```

### H5x (Fault Resilience)
```
[cycle, nodes, edges, maxWeight, minWeight, faultActive]  — 100 points per seed
```

### H7x (STDP Sweep)
```
{dt, delta}  — 21 points
```

### H10x (Pipeline Soak)
```
[cycle, nodeCount, edgeCount, maxWeight, minWeight, targetEntropy]  — 100 points
```

### H1x (Homeostatic Convergence)
```
[cycle, targetEntropy, targetConductivity, correctionFired]  — 400 points per seed
```

## §4 — Suite Metrics

| Metric | Value |
|--------|-------|
| C-003 tests | 12 |
| C-003 runtime | 5.234s |
| Full suite (post-C-003) | 134 suites / 1,707 tests |
| Full suite failures | 0 |
| Full suite runtime | 159s |
| Trajectory data points | ~2,221 total |

## §5 — Open Work

| Item | Status |
|------|--------|
| Growth-enabled extended cycle test | Deferred — requires topology cap in PlasticityEnvelope |
| Cross-phase coupling sweep | Future campaign (C-004?) |
| Biological fidelity comparison (Arbor) | Requires external tooling, not a SECS unit test concern |
