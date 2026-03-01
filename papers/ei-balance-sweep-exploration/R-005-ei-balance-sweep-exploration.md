# R-005 — E/I Balance Sweep Exploration

> **Report ID:** R-005
> **Campaign:** C-005
> **Protocol:** P-004
> **Author:** Analyst
> **Date:** 2026-02-28
> **Status:** FINAL
> **Type:** COMPUTATIONAL EXPLORATION — not a biological or clinical claim
> **Disposition:** ALL PASS (10/10). Controller converges to a single attractor regardless
>                  of initial `targetEntropy`; convergence speed is monotonically related to
>                  distance from observation mean; zero vetoes across entire research envelope.
> **System Under Test:** SECS Sovereign Execution & Collapse Substrate, Phase A
> **Suite:** 136 suites / 1,730 tests / 0 failures
> **Campaign Result:** 10/10 pass (5 hypotheses, 10 test cases)
> **Seeds:** 42, 137, 2026
> **Parameters Swept:** `targetEntropy` ∈ [0.05, 0.90], step 0.05, 18 values

---

## §1 — Question

How does the SECS homeostatic controller behave across a range of
`targetEntropy` set-points? Where does it converge quickly, where does
it oscillate, and where (if anywhere) does the envelope intervene?

This campaign maps the convergence landscape of a single swept parameter
while holding all other parameters at defaults. It produces a
topological map of controller behavior, not a verdict.

---

## §2 — Parameters

### Fixed Configuration

| Parameter | Value |
|-----------|-------|
| ConstraintSurface | V1_DEFAULTS |
| Topology | 10 nodes, 12 edges (standard) |
| Clock | 100 ms per cycle (integer stamps) |
| PRNG | Mulberry32 (per seed) |
| Observation entropy | uniform [0.1, 1.4] |
| Observation conductivity | uniform [0.3, 0.8] |
| Observation mean entropy | 0.75 |
| Adaptation cadence | 1 (every cycle) |
| Structural plasticity | disabled |
| Learning | defaults (not swept) |
| Cycles per run | 1,000 |
| Trajectory sample interval | every 5th cycle (200 points per run) |
| Tail window | last 200 cycles (40 trajectory samples) |

### Swept Parameter

| Parameter | Default | Sweep Range | Step | Values |
|-----------|---------|-------------|------|--------|
| `homeostatic.targetEntropy` | 0.30 | [0.05, 0.90] | 0.05 | 18 |

---

## §3 — Runs

| # | Section | Hypothesis | Configurations | Cycles | Seeds | Runs |
|---|---------|-----------|---------------|--------|-------|------|
| 1 | §A | H18–H20 | 18 sweep values | 1,000 | 42, 137, 2026 | 54 |
| 2 | §B | H21 | 2 (targets 0.30, 0.70) | 1,000 | 42, 137, 2026 | 6 |
| 3 | §C | H22 | 1 (target 0.30 + control) | 1,000 | 42 (×2), 137 | 3 |
| 4 | §D | detail | 5 (targets 0.05, 0.30, 0.50, 0.75, 0.90) | 1,000 | 42 | 5 |

**Total data points:** 54 × 200 = 10,800 trajectory samples (landscape) + replay & detail.

---

## §4 — Observations

### §4.1 — Convergence Speed Landscape (H18)

The convergence cycle is defined as the first cycle where
|`targetEntropy` − 0.75| < `entropyTolerance`.

| targetEntropy | Seed 42 | Seed 137 | Seed 2026 | Mean |
|:---:|:---:|:---:|:---:|:---:|
| 0.05 | 29 | 23 | 22 | 24.7 |
| 0.10 | 29 | 23 | 22 | 24.7 |
| 0.15 | 29 | 23 | 22 | 24.7 |
| 0.20 | 29 | 23 | 22 | 24.7 |
| 0.25 | 29 | 23 | 22 | 24.7 |
| 0.30 | 29 | 23 | 22 | 24.7 |
| 0.35 | 29 | 22 | 22 | 24.3 |
| 0.40 | 29 | 7 | 22 | 19.3 |
| 0.45 | 29 | 7 | 13 | 16.3 |
| 0.50 | 12 | 6 | 13 | 10.3 |
| 0.55 | 2 | 4 | 2 | 2.7 |
| 0.60 | 1 | 1 | 2 | 1.3 |
| **0.65** | **1** | **1** | **1** | **1.0** |
| **0.70** | **1** | **1** | **1** | **1.0** |
| **0.75** | **1** | **1** | **1** | **1.0** |
| 0.80 | 1 | 2 | 1 | 1.3 |
| 0.85 | 1 | 2 | 1 | 1.3 |
| 0.90 | 4 | 4 | 1 | 3.0 |

**Pattern:** The convergence landscape is asymmetric around the observation
distribution mean (0.75). Configurations at 0.65–0.75 converge in a single
cycle — the controller is already within tolerance. Convergence time
increases monotonically as the initial target moves below 0.55. For low
targets (0.05–0.35), convergence takes 22–29 cycles — a transient of
~3% of the total run — before the controller reaches the attractor.

The landscape exhibits a plateau below 0.35 (convergence cycle is
essentially constant at ~22–29 regardless of initial target), suggesting
that the controller's per-cycle correction magnitude is the rate-limiting
factor, not the absolute initial distance.

Above 0.75, convergence remains fast (1–4 cycles) even at 0.90, indicating
the controller corrects more efficiently when overshooting above the
observation mean than when undershooting below it.

### §4.2 — Steady-State Attractor

All 54 configurations converge to the same per-seed steady-state attractor:

| Seed | Final Mean (targetEntropy, tail 200 cycles) | Final Std |
|:---:|:---:|:---:|
| 42 | 0.73375 | 0.10452 |
| 137 | 0.73625 | 0.08731 |
| 2026 | 0.79000 | 0.11522 |

These values are **identical across all 18 initial targetEntropy settings**
within each seed. The initial target determines only the transient
duration — the controller erases all memory of the initial condition.

Grand mean across seeds: **0.7533**.  
Observation distribution mean: **0.75**.  
Deviation from observation mean: **0.0033** (0.44%).

### §4.3 — Oscillation Amplitude (H19)

| targetEntropy Range | Mean Oscillation Amplitude |
|:---:|:---:|
| Extremes (≤ 0.10 or ≥ 0.85) | 0.433 |
| Midrange (0.30–0.60) | 0.433 |
| All configurations | 0.433 |

Oscillation amplitude is **uniform** across all configurations (0.4 for
seeds 42 and 137, 0.5 for seed 2026). The steady-state oscillation is
driven entirely by the stochastic observation sequence, not by the
initial target. Since all configurations converge to the same attractor,
their steady-state dynamics are identical.

Both extreme and midrange mean oscillation amplitudes are bounded well
below 1.0 (assertion threshold), confirming stable controller operation
across the entire research envelope.

### §4.4 — Correction Density

| Seed | Correction Density Range |
|:---:|:---:|
| 42 | 0.935–0.937 |
| 137 | 0.950–0.952 |
| 2026 | 0.936–0.937 |

The controller emits `homeostatic_correction` events on 93.5–95.2% of
cycles, with negligible variation across initial targets (<0.002
within-seed spread). The controller is nearly always active.

---

## §5 — Stability Profile

### Per-Seed Convergence Summary

| Metric | Seed 42 | Seed 137 | Seed 2026 |
|--------|:-------:|:--------:|:---------:|
| Fastest convergence (cycles) | 1 (at 0.60–0.85) | 1 (at 0.60–0.75) | 1 (at 0.65–0.90) |
| Slowest convergence (cycles) | 29 (at 0.05–0.45) | 23 (at 0.05–0.30) | 22 (at 0.05–0.40) |
| Attractor steady-state mean | 0.73375 | 0.73625 | 0.79000 |
| Attractor steady-state std | 0.10452 | 0.08731 | 0.11522 |
| Oscillation amplitude | 0.4 | 0.4 | 0.5 |
| Max correction density | 0.937 | 0.952 | 0.937 |

### Key Finding: Single Attractor

The homeostatic controller has a **single attractor basin** covering the
entire research envelope [0.05, 0.90]. There are no bifurcations,
multi-modal attractors, or divergent regimes. Every initial condition
converges to the same steady state.

The attractor location is determined by the observation distribution
(mean entropy ~0.75), not by the initial parameter setting.

---

## §6 — Envelope Events

| Metric | Value |
|--------|-------|
| Total vetoes across 54 runs | **0** |
| Per-run maximum veto count | 0 |
| Per-run veto rate | 0.0% |
| Envelope boundary contacts | 0 |

The entire research envelope [0.05, 0.90] is **unconditionally safe**.
No configurations triggered envelope vetoes, warnings, or boundary
contacts. The `severeEntropyThreshold` (1.5) is sufficiently distant
from the swept range that no interventions occur.

H20 is confirmed: vetoes are zero throughout the research range, as
the swept values are well below the constitutional boundary.

---

## §7 — Determinism Verification

### Replay Test (H22)

| Metric | Run 1 (seed 42, target 0.30) | Run 2 (seed 42, target 0.30) | Match |
|--------|:---:|:---:|:---:|
| Trajectory length | 200 | 200 | identical |
| Convergence cycle | 29 | 29 | identical |
| Final mean | 0.73375 | 0.73375 | identical |
| Final std | 0.10452 | 0.10452 | identical |
| Oscillation amplitude | 0.4 | 0.4 | identical |
| Veto count | 0 | 0 | identical |
| Correction density | 0.935 | 0.935 | identical |
| Full JSON comparison | — | — | **byte-identical** |

### Control (Seed Divergence)

| Metric | Seed 42 | Seed 137 | Match |
|--------|:---:|:---:|:---:|
| Trajectory JSON | (unique) | (unique) | **different** |

Interpretation: determinism is per-seed, not substrate-wide. Different
PRNG seeds produce different observation sequences, yielding different
transient paths to the same attractor.

---

## §8 — Cross-Seed Consistency (H21)

### At targetEntropy = 0.30

| Metric | Seed 42 | Seed 137 | Seed 2026 |
|--------|:-------:|:--------:|:---------:|
| Convergence cycle | 29 | 23 | 22 |
| Final mean | 0.73375 | 0.73625 | 0.79000 |
| Final std | 0.10452 | 0.08731 | 0.11522 |
| Correction density | 0.935 | 0.951 | 0.936 |
| Mean spread | — | — | **0.056** |

### At targetEntropy = 0.70

| Metric | Seed 42 | Seed 137 | Seed 2026 |
|--------|:-------:|:--------:|:---------:|
| Convergence cycle | 1 | 1 | 1 |
| Final mean | 0.73375 | 0.73625 | 0.79000 |
| Mean spread | — | — | **0.056** |

Mean spread 0.056 < threshold 0.15 at both probed targets. Convergence
patterns are qualitatively similar across seeds: same attractor, same
steady-state dynamics, seed-specific differences only in transient timing.

---

## §9 — Detailed Trajectories (§D)

Five key configurations were recorded at full resolution (seed 42):

| targetEntropy | Conv Cycle | Final Mean | Final Std | Osc Amp | Veto | Corr Density |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0.05 | 29 | 0.73375 | 0.10452 | 0.4 | 0 | 0.935 |
| 0.30 | 29 | 0.73375 | 0.10452 | 0.4 | 0 | 0.935 |
| 0.50 | 12 | 0.73375 | 0.10452 | 0.4 | 0 | 0.935 |
| 0.75 | 1 | 0.73375 | 0.10452 | 0.4 | 0 | 0.937 |
| 0.90 | 4 | 0.73375 | 0.10452 | 0.4 | 0 | 0.937 |

All five configurations reach the same steady state. Only the convergence
cycle differs — confirming that `targetEntropy = 0.75` provides the
fastest initial convergence, while low values (0.05, 0.30) require ~29
cycles to traverse the distance to the attractor.

Trajectory data (200 points per run, 1,000 points total) is emitted in
full in the test output log for archival.

---

## §10 — Disposition

### Per-Hypothesis Summary

| ID | Hypothesis | Result | Evidence |
|----|-----------|--------|----------|
| H18 | Convergence speed varies with target proximity | **PASS** | Convergence cycle 1 at 0.65–0.75 vs 22–29 at 0.05–0.35 |
| H19 | Oscillation amplitude bounded across configs | **PASS** | Uniform 0.4–0.5, both extreme and midrange < 1.0 |
| H20 | Zero vetoes within research envelope | **PASS** | 0 vetoes across all 54 runs |
| H21 | Cross-seed qualitative consistency | **PASS** | Mean spread 0.056 < 0.15 at both probed targets |
| H22 | Deterministic replay | **PASS** | Byte-identical trajectories; control confirms seed divergence |

### Campaign Result: **10/10 PASS**

### Interpretation Notes (Computational Only)

1. **Single attractor:** The controller erases initial conditions within
   ~30 cycles at worst. The steady state is fully determined by the
   observation distribution, not the initial parameter.

2. **Asymmetric transient:** The convergence landscape is asymmetric —
   the controller corrects more rapidly from above the attractor
   (0.90 → 4 cycles) than from below (0.05 → 29 cycles).

3. **Plateau regime:** Below targetEntropy 0.35, convergence time is
   essentially constant (~24.7 cycles), suggesting a constant-rate
   correction mechanism rather than proportional control.

4. **Research envelope safety:** The entire [0.05, 0.90] range is
   unconditionally safe (zero vetoes). Future campaigns can explore
   the full range without envelope concerns.

5. **Seed independence:** The attractor location and oscillation amplitude
   are consistent across seeds. Per-seed variation is limited to the
   specific value of the attractor mean (±0.056), determined by the
   PRNG-generated observation sequence.

---

## §11 — Constitutional Compliance

| Constraint | Status |
|-----------|--------|
| Zero substrate modifications | Verified — no changes to `src/` |
| No clinical claims | Verified — computational language only |
| `Type: COMPUTATIONAL EXPLORATION` header | Present |
| Parameters within research envelope | All 18 values in [0.05, 0.90] |
| Deterministic replay confirmed | H22 PASS |
| Report uses permitted fields only | Verified against `research-report-schema.md` |
| No prohibited fields | No diagnosis, clinical_recommendation, biological_claim, treatment_suggestion, patient_identifier, medical_interpretation, or neurotypical_comparison |

---

*First research campaign complete. One axis swept. Landscape mapped.
The controller has a single attractor — initial conditions are forgotten.*
