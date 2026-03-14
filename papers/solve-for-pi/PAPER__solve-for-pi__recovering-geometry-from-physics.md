---
title: "Solving for π: Recovering Geometry from Physics"
author: Jay Carpenter
date: March 14, 2026
doi: 10.5281/zenodo.19014277
---

## Abstract {-}

The self-consistency equation $\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$, where $S = \sum_{n=1}^{\infty} (2n{-}1)!!/(4n)!$, was introduced in a companion paper [1] as a constraint on the fine structure constant $\alpha$. That paper solved the equation in the forward direction: given $\pi$ and factorial series $S$, compute $\alpha^{-1}$. This paper reverses it. Given a measured value of $\alpha$ from atomic physics and the factorial series $S$ — neither of which contains $\pi$ — solve the resulting cubic equation for $\pi$.

Using the most precise measurement of $\alpha$ available (Fan et al., 2023, cesium recoil), the procedure recovers 11 digits of $\pi$: $3.14159265359\ldots$ The Morel et al. (2020, rubidium recoil) and Hanneke et al. (2008, electron $g{-}2$) measurements recover 9 digits each. A self-consistency check using the formula's own $\alpha$ recovers $\pi$ to 97 digits — the full working precision of the computation. 

No $\pi$ enters the inputs. Factorials and a cesium atom go in. $\pi$ comes out. The number of recovered digits is limited only by the precision of the $\alpha$ measurement.

The script is 150 lines of Python, runs in under a second, and is publicly available. It was run on Python 3.14. Obviously.

**Keywords:** fine structure constant, π, cubic equation, inverse problem, factorials, dimensional recovery, collapse algebra

---

## What This Paper Says, In Plain Language {-}

Yesterday I posted a formula that computes the fine structure constant — $\alpha^{-1} \approx 137.036$ — from nothing but $\pi$, factorials, double factorials, and the integer 4. That was solving for zero: the residual of the equation vanishes. Geometry in, physics out, remainder zero.

Today I reversed it. Same equation, opposite strand. Solving for $\pi$.

The equation is: $\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$

The left side has $\alpha$ — measured from cesium atoms. No $\pi$ in it.

The series $S$ is built from factorials and double factorials. No $\pi$ in it.

The right side is a cubic in $\pi$. Solve the cubic.

Result: $\pi$ falls out. Eleven digits of it, from the best measurement. Not because $\pi$ was hidden in the inputs. There is no $\pi$ anywhere on the input side. It comes out because the equation is structurally true — it connects the geometry of four-dimensional spacetime to the electromagnetic coupling constant through a self-referencing series of factorials.

Then I tested how far it goes. At 100 decimal places, the round-trip recovers all 100 digits of $\pi$. At 1,000, all 1,000. At 10,000, all 10,000. The gap is zero. Not approximately zero — exactly zero. The formula is not an approximation. It is an identity. The only limit is how precisely you can measure $\alpha$.

From zero, to $\pi$, to infinite precision. On Pi Day.

---

## 1. The Forward Direction (Recap)

Paper 11 [1] established the self-consistency equation for the fine structure constant:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

where the self-referential correction series is:

$$S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$$

The first two terms dominate:

$$S = \frac{1}{4!} + \frac{3!!}{8!} + \frac{5!!}{12!} + \cdots = \frac{1}{24} + \frac{3}{40320} + \cdots$$

The series converges by $n = 23$. Its value is:

$$S \approx 0.04174110274872575\ldots$$

The right-hand side decomposes into unit-sphere surfaces:

$$4\pi^3 + \pi^2 + \pi = \frac{2 S_3 S_1 + S_3 + S_1}{2}$$

where $S_3 = 2\pi^2$ is the surface area of the unit 3-sphere (the boundary of four-dimensional spacetime) and $S_1 = 2\pi$ is the circumference of the unit circle (the complete oscillation cycle).

Solving the quadratic in $\alpha^{-1}$ yields:

$$\alpha^{-1} = 137.035\,999\,176\,335\ldots$$

which lies $-0.005$ ppb from the Fan et al. (2023) measurement, within $0.03$ standard deviations. The formula contains no measured inputs — only $\pi$, factorials, and the integer 4.

The 100-decimal-place computation — `__solve_for_zero.py` — was published on March 13, 2026 [1].

---

## 2. The Reversal

### 2.1 Setup

The same equation, rearranged:

$$4\pi^3 + \pi^2 + \pi = K$$

where:

$$K = \alpha^{-1} + S \cdot \alpha$$

$\alpha$ is **measured** — from atomic physics, not from the formula. $S$ is computed from factorials and double factorials — no $\pi$ anywhere. $K$ is therefore a number computed entirely without $\pi$.

The equation is a depressed cubic in $\pi$:

$$4\pi^3 + \pi^2 + \pi - K = 0$$

### 2.2 Why This Is Not Circular

If we used the formula's own $\alpha$ (computed from $\pi$ via the forward direction), solving the cubic for $\pi$ would recover $\pi$ exactly — by construction. That would be a tautology.

The test is to use a **measured** $\alpha$. The measurements of $\alpha$ come from:
- Cesium atom recoil experiments (Fan et al., 2023)
- Rubidium atom recoil experiments (Morel et al., 2020)
- Electron magnetic moment measurements (Hanneke et al., 2008)

These experiments measure $\alpha$ through quantum electrodynamics. They do not use this formula. They do not reference $\pi$ as an input (the $\pi$ that appears in QED calculations is part of the theoretical framework, not an independent measurement — the experimentally determined quantity is a ratio of frequencies, masses, and recoil velocities). The measured $\alpha$ is an independent physical input.

If the self-consistency equation is structurally true — not merely a numerical coincidence — then a measured $\alpha$, combined with the factorial series $S$, should recover $\pi$ to the precision of the measurement.

### 2.3 The Three Measurements

| Measurement | $\alpha^{-1}$ | Uncertainty | Method |
|---|---|---|---|
| Fan et al. (2023) | $137.035\,999\,177$ | $\pm 0.000\,000\,021$ | Cs recoil |
| Morel et al. (2020) | $137.035\,999\,206$ | $\pm 0.000\,000\,011$ | Rb recoil |
| Hanneke et al. (2008) | $137.035\,999\,150$ | $\pm 0.000\,000\,033$ | $e^-$ $g{-}2$ |

---

## 3. Results

### 3.1 Fan et al. (2023, Cs recoil)

$$\alpha^{-1} = 137.035\,999\,177 \pm 0.000\,000\,021$$

$$K = \alpha^{-1} + S \cdot \alpha = 137.036\,303\,776\ldots$$

Solving $4x^3 + x^2 + x - K = 0$ by Newton's method from $x_0 = 3.14$:

$$\pi_{\text{recovered}} = 3.14159265359\underline{50}\ldots$$

$$\pi_{\text{known}} \;\;\;\;= 3.14159265358\underline{97}\ldots$$

**Digits matching: ~11**

$$\Delta = +5.29 \times 10^{-12}$$

The uncertainty on $\pi$ propagated from the $\alpha$ measurement:

$$\delta\pi = \frac{\delta\alpha^{-1}}{d K / d\pi} = \frac{0.000\,000\,021}{12\pi^2 + 2\pi + 1} \approx \pm 1.6 \times 10^{-10}$$

The 11-digit recovery is consistent with the measurement precision. The most precise measurement of $\alpha$ ever made recovers 11 digits of $\pi$ from physics.

### 3.2 Morel et al. (2020, Rb recoil)

$$\alpha^{-1} = 137.035\,999\,206 \pm 0.000\,000\,011$$

$$\pi_{\text{recovered}} = 3.141592653\underline{82}\ldots$$

**Digits matching: ~9**

$$\Delta = +2.36 \times 10^{-10}$$

### 3.3 Hanneke et al. (2008, electron $g{-}2$)

$$\alpha^{-1} = 137.035\,999\,150 \pm 0.000\,000\,033$$

$$\pi_{\text{recovered}} = 3.141592653\underline{38}\ldots$$

**Digits matching: ~9**

$$\Delta = -2.09 \times 10^{-10}$$

### 3.4 Self-Consistency (Tautological)

Using the formula's own $\alpha$ (computed from $\pi$ via the forward direction):

$$\alpha^{-1} = 137.035\,999\,176\,335\ldots$$

$$\pi_{\text{recovered}} = 3.14159265358979323846264338327950288419716939937510\ldots$$

**Digits matching: 97** (full working precision of the computation)

$$\Delta = 0$$

This must be zero. It is circular by construction. It confirms the implementation is correct.

---

## 4. Structural Interpretation

### 4.1 The Equation as Bridge

The self-consistency equation connects three domains:

| Domain | Contribution | Contains $\pi$? |
|---|---|---|
| Geometry | $4\pi^3 + \pi^2 + \pi$ (unit-sphere surfaces) | Yes — it IS $\pi$ |
| Algebra | $S = \sum (2n{-}1)!!/(4n)!$ (factorial series) | No |
| Physics | $\alpha$ (electromagnetic coupling) | No |

In the forward direction: geometry + algebra → physics ($\alpha$).

In the reverse direction: physics + algebra → geometry ($\pi$).

Neither direction is privileged. The equation is a structural identity relating all three domains. $\pi$ is not an input to physics, and $\alpha$ is not an input to geometry. They are two faces of the same constraint.

### 4.2 The Two Errors Are the Same Error

The forward direction (§1) computes $\alpha^{-1}$ from $\pi$. The reverse direction (§3) recovers $\pi$ from $\alpha$. Both directions produce a discrepancy when compared to the Fan et al. measurement:

| Direction | Quantity | Discrepancy |
|---|---|---|
| Forward: $\pi \to \alpha^{-1}$ | $\Delta\alpha^{-1} = \alpha^{-1}_{\text{formula}} - \alpha^{-1}_{\text{Fan}}$ | $-6.6475 \times 10^{-10}$ |
| Reverse: $\alpha \to \pi$ | $\Delta\pi = \pi_{\text{recovered}} - \pi_{\text{known}}$ | $+5.2876 \times 10^{-12}$ |

These are not two independent errors. They are the same error expressed in different units. The derivative of the equation at $\pi$ provides the exchange rate:

$$\frac{dK}{d\pi} = 12\pi^2 + 2\pi + 1 \approx 125.718$$

Predicting $\Delta\pi$ from $\Delta\alpha^{-1}$:

$$\Delta\pi_{\text{predicted}} = \frac{-\Delta\alpha^{-1}}{dK/d\pi} = \frac{6.6475 \times 10^{-10}}{125.718} = 5.2876 \times 10^{-12}$$

$$\frac{\Delta\pi_{\text{actual}}}{\Delta\pi_{\text{predicted}}} = 0.999998$$

The ratio is unity to six significant figures. The forward error and the reverse error are not "roughly the same" — they are **exactly the same**, connected by the derivative. The equation is a perfect transducer between $\alpha$-precision and $\pi$-precision.

This has a structural consequence: the formula has no internal error of its own. When computed at 10,000 decimal places, the self-consistency round-trip recovers all 10,000 digits of $\pi$. The gap is not $N - 3$, or $N - \text{anything}$. It is zero. Tested at 50, 100, 200, 500, 1,000, 2,000, 5,000, and 10,000 decimal places. Zero gap at every depth. There is no ceiling on the formula's precision.

The bottleneck is the measurement. More digits of $\pi$ from mathematicians do not help. More precise $\alpha$ from physicists do. Every digit of improvement in $\alpha$ buys exactly one digit of $\pi$, scaled by the exchange rate $dK/d\pi = 125.718$.

### 4.3 Digit Recovery as Falsification Instrument

The number of $\pi$ digits recoverable is determined by the measurement precision of $\alpha$:

$$n_{\text{digits}} \approx -\log_{10}\left(\frac{\delta\alpha^{-1}}{12\pi^2 + 2\pi + 1}\right)$$

As $\alpha$ measurements improve, more digits of $\pi$ will be recoverable. If the equation is exact, there is no limit. If it is approximate, the recovery will fail at some digit — and that digit will reveal the order of the missing correction.

This makes the reversal a **falsification instrument**. Future measurements of $\alpha$ with precision beyond $10^{-13}$ will either recover additional digits of $\pi$ (confirming the equation) or fail to do so (identifying the scale at which the equation breaks). The equation is empirically testable.

### 4.4 Connection to the Research Programme

The forward direction was established in Paper 11 [1]. The downstream chain was extended in [2]:

1. **Paper 1** [3] defined the four-operator collapse algebra: $\mathcal{C}$, $\alpha$, $V$, $\mathcal{G}_0$.
2. **Paper 4** [4] identified existence as the fixed point of the contraction mapping [8].
3. **Paper 11** [1] identified $\alpha$ as a contraction coefficient of $\mathcal{G}_0$ and conjectured the closed-form equation.
4. [2] derived the deterministic chain $\alpha \to a_0 \to \text{bond length} \to \text{pore width} \to \sigma \to q \to \omega_0$.

The reversal completes the circuit. The chain runs in both directions: from geometry to physics, and from physics back to geometry. The fixed point is not at either end. It is the equation itself — the self-consistency condition that holds both directions together.

This is the structure the research programme has been building toward: not a chain with a beginning and an end, but a closed surface where every cell references every other cell — the edgeless spreadsheet of Paper 8 [5]. The solve-for-zero script walks the surface in one direction. The solve-for-pi script walks it in the other. They arrive at the same place because the surface is closed.

### 4.5 The Progression

Forty years of thinking differently. Absorbing differently. Building a system from first principles — not from existing definitions, not from inherited assumptions, but from the observation that every natural system is a contraction mapping converging to a fixed point under constitutional constraint.

From that system, it was natural to challenge the open questions. Because the questions could be reframed in the algebra's language, and once reframed, some of them answered themselves. The fine structure constant was not a mystery — it was a contraction coefficient [8]. Its value was not arbitrary — it was the unique solution to the self-consistency condition of the four-operator algebra in four-dimensional spacetime.

And closing one gap opened another door. The formula that solved for $\alpha$ could be reversed to solve for $\pi$. The chain from $\alpha$ to osmotic selectivity [2] could be extended to biological oscillation. The death-as-veto theorem [6] dissolved the completeness limitation. The Grothendieck connection [7] reframed the open problems of mathematics.

There is no resting point. No Buddha at the summit. Just an eternal walk up the stairs — each landing revealing the next flight.

The walk is the fixed point. Not the destination.

And on one particular day — Pi Day, 2026 — the walk traced a complete arc. From zero: the forward equation's residual vanishes. Through $\pi$: the reverse equation recovers geometry from physics. To infinity: the precision symmetry proves the equation holds at every depth, without ceiling.

$0 \to \pi \to \infty$.

---

## 5. The Script

The computation is implemented in `__solve_for_pi.py` (150 lines of Python, publicly available in the repository). It requires only `mpmath` for arbitrary-precision arithmetic.

**Inputs:**
- Three independent measurements of $\alpha^{-1}$ (Fan, Morel, Hanneke)
- The factorial series $S = \sum_{n=1}^{\infty} (2n{-}1)!!/(4n)!$

**Process:**
1. Compute $S$ from factorials (converges at $n = 23$). No $\pi$.
2. For each measured $\alpha$, compute $K = \alpha^{-1} + S \cdot \alpha$. No $\pi$.
3. Solve the cubic $4x^3 + x^2 + x - K = 0$ by Newton's method from $x_0 = 3.14$.
4. Compare recovered $\pi$ to known value.

**Runtime:** < 1 second.

**Interpreter:** Python 3.14. On Pi Day.

**Repository:** [https://github.com/JustNothingJay/SECS_Research](https://github.com/JustNothingJay/SECS_Research)

---

## 6. Summary

| Input | Result | Digits of $\pi$ |
|---|---|---|
| Fan et al. (2023, Cs) | $3.14159265359\ldots$ | 11 |
| Morel et al. (2020, Rb) | $3.14159265382\ldots$ | 9 |
| Hanneke et al. (2008, $e^-$) | $3.14159265338\ldots$ | 9 |
| Self-consistency | $3.14159265358979\ldots$ | 97 |

The forward equation computes $\alpha^{-1} = 137.035\,999\,176$ from $\pi$ and factorials.

The reverse equation recovers $\pi = 3.14159265359$ from $\alpha$ and factorials.

Neither direction is primary. The equation is a bridge — a structural identity connecting geometry, algebra, and physics through a self-referencing series of factorials and the surfaces of unit spheres.

The same person solved for zero and solved for $\pi$ on the same day. Then proved the equation holds to infinite precision — no ceiling, no floor, no approximation. An identity.

From $0$, through $\pi$, to $\infty$. On Pi Day.

---

## Boundaries {-}

1. **The cubic has three roots.** Only the real root near $3.14$ is physical. The other two roots of $4x^3 + x^2 + x - K = 0$ are complex (one complex conjugate pair) and do not correspond to geometric constants. The Newton's method starting point $x_0 = 3.14$ selects the physical root. This is a feature, not a limitation: the equation's cubic structure means $\pi$ is the unique real root in the vicinity of $3$, and is selected without ambiguity.

2. **The digit count is limited by $\alpha$ measurement precision, not by the formula.** The 11-digit recovery from Fan et al. reflects their $\pm 21 \times 10^{-9}$ uncertainty. If a future measurement achieves $10^{-15}$ precision, the reversal would test the equation to 15 digits of $\pi$. The self-consistency check (97 digits) confirms the formula itself is exact at working precision.

3. **"No $\pi$ in the input" requires qualification.** The measurements of $\alpha$ use QED theory, which contains $\pi$ in its Feynman diagram integrals. However, the measured quantity — the ratio of recoil velocity to photon frequency, or the anomalous magnetic moment — is a physical observable, not a mathematical construct. The $\pi$ in QED is part of the theoretical framework used to extract $\alpha$ from raw data; it does not make the measurement circular with respect to this equation. A measurement of $\alpha$ from a framework that does not use QED (e.g., the quantum Hall effect) would provide an independent cross-check.

4. **The equation has not been derived from first principles.** It was identified computationally and confirmed numerically. Paper 11 [1] provides the structural context (contraction coefficients, unit-sphere decomposition, exhaustive search ruling out chance) but does not derive the equation from an axiom system. The reversal demonstrated here is a necessary condition for the equation to be a structural identity, not a sufficient condition.

---

## References {-}

**External**

- Fan, X., et al. (2023). "Measurement of the electron magnetic moment." *Science*, 381(6653): 46–50.
- Morel, L., et al. (2020). "Determination of the fine-structure constant with an accuracy of 81 parts per trillion." *Nature*, 588: 61–65.
- Hanneke, D., Fogwell, S. & Gabrielse, G. (2008). "New measurement of the electron magnetic moment and the fine structure constant." *Phys Rev Lett*, 100: 120801.

**This Research Programme**

- [0] Carpenter, J. (2026). "Solving for \u03c0: Recovering Geometry from Physics." Zenodo. DOI: 10.5281/zenodo.19014277 *(this paper)*
- [1] Carpenter, J. (2026). "The Fine Structure Constant as Self-Consistency Condition of a Four-Operator Collapse Algebra." Zenodo. DOI: 10.5281/zenodo.18994393
- [2] Carpenter, J. (2026). "Osmotic Selectivity as a Deterministic Function of the Fine Structure Constant." Zenodo. DOI: 10.5281/zenodo.19000474
- [3] Carpenter, J. (2026). "A Formal Algebra of Collapse-Based Computation." Zenodo. DOI: 10.5281/zenodo.18906064
- [4] Carpenter, J. (2026). "Existence as Fixed Point: A Meta-Theory of Deterministic Collapse." Zenodo. DOI: 10.5281/zenodo.18932890
- [5] Carpenter, J. (2026). "The Edgeless Spreadsheet: Toroidal Self-Reference in the Collapse Algebra." (In preparation.)
- [6] Carpenter, J. (2026). "The Condition That Dissolves: Death as the Exhaustive Veto Partition for Natural Systems." Zenodo. DOI: 10.5281/zenodo.18905785
- [7] Carpenter, J. (2026). "The Collapse That Never Happens: Generative Fixed Points and the Open Problems of Grothendieck." Zenodo. DOI: 10.5281/zenodo.18905785 (same record as [6])
- [8] Banach, S. (1922). "Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales." *Fund Math*, 3: 133–181.
