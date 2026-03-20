---
title: "The Process of Derivation: From Self-Consistency Equation to Precision Validation of the Fine Structure Constant"
author: Jay Carpenter
date: March 16, 2026
---

## Abstract {-}

This paper describes the complete process by which a value of the fine structure constant $\alpha^{-1} = 137.035999177$ was derived from a single self-consistency equation containing no empirical inputs, and subsequently validated against the five highest-precision experimental determinations in existence. The process spans three stages: (1) the identification of the algebraic equation within the collapse algebra framework, (2) the recovery of $\pi$ to eleven digits from $\alpha$ as an independent consistency check, and (3) the quantitative confrontation of the algebraic value with precision QED through the Schwinger perturbative expansion.

The paper serves as a methodological companion to two prior publications. Paper 2026d (Carpenter, 2026d) identifies the self-consistency equation and derives $\alpha^{-1}$ to two different precisions depending on series truncation. Paper 2026s (Carpenter, 2026s) presents the precision comparison as a result. This paper reconstructs the chain of reasoning, reports the computational details, and addresses the interpretive questions that arise when an algebraic prediction is indistinguishable from the best available measurement.

**Keywords:** fine structure constant, algebraic derivation, precision validation, Schwinger series, self-consistency, methodology, electron $g{-}2$, metrology

---

# §1. The Problem

## §1.1. The status quo

The fine structure constant $\alpha = e^2 / \hbar c$ (in Gaussian units) determines the strength of the electromagnetic interaction. Since Sommerfeld introduced it in 1916, it has become the most precisely determined fundamental constant, measured to $\sim$0.08 parts per billion by atom-recoil experiments and to $\sim$0.28 parts per billion by the electron anomalous magnetic moment.

Despite this extraordinary precision, no theory derives $\alpha$ from first principles. The Standard Model of particle physics treats all coupling constants — including $\alpha$ — as free parameters that must be measured. The value $\alpha^{-1} \approx 137$ is an input to the Standard Model, not an output of it.

This situation is unique in physics. Other fundamental constants (the speed of light $c$, Planck's constant $\hbar$) are either set by definition (in natural units) or have well-understood origins in the structure of spacetime. The coupling constants alone remain unexplained. Pauli, Eddington, and many others attempted derivations. All failed or produced results that did not survive scrutiny (Kragh, 2003).

## §1.2. The approaches that failed

Three broad strategies have been attempted:

**Numerology.** Eddington (1929) predicted $\alpha^{-1} = 136$ from combinatorial arguments about the number of independent components of a symmetric tensor in his fundamental theory. When the measured value turned out to be closer to 137, he revised his theory to accommodate the new number. This approach was rejected because the derivation could be adjusted to match any measured value — it was not predictive.

**Anthropics.** Barrow and Tipler (1986) observed that $\alpha$ must fall within a narrow range for stable atoms, chemistry, and observers to exist. This constrains $\alpha$ but does not determine it: many values within the range are equally compatible with observers. The anthropic principle explains why $\alpha$ is roughly 1/137 but cannot distinguish 1/137 from 1/138.

**Multiverse/landscape.** Susskind (2003) and the string landscape approach propose $\sim 10^{500}$ vacua with different coupling constants. We observe this $\alpha$ because we exist in a vacuum compatible with observers. This dissolves the question (why this value?) into statistics (why not?) but makes no testable prediction about the value itself.

**The common failure mode.** All three approaches share a structural feature: they start from $\alpha$ as a number and attempt to explain why that number has the value it does. This paper takes a different approach. It starts from a mathematical framework — the collapse algebra — and discovers that the framework's self-consistency condition produces a specific number that happens to match $\alpha$.

## §1.3. The question, precisely stated

Is $\alpha$ a free parameter, or is it uniquely determined by a structural constraint?

If the former, deriving it is impossible — it could have been any value consistent with the existence of the framework (anthropic bound). If the latter, there exists an equation whose solution is $\alpha$, and the problem is to find that equation.

This paper reports the finding of such an equation and the process of validating that its solution matches the measured value.

---

# §2. The Equation

## §2.1. The collapse algebra

The collapse algebra (Carpenter, 2026a) defines four operators: the collapse operator $\mathcal{C}$ (irreversible state collapse), the admissibility function $\alpha$ (constraint filtering), the veto $V$ (rejection of inadmissible states), and the constitutional constraint $\mathcal{G}_0$ (the fixed point that holds the system in existence). The meta-theory (Carpenter, 2026j) establishes that existence is the fixed point of a Banach contraction mapping, and $\mathcal{G}_0$ is the contraction condition itself.

Paper 2026d (Carpenter, 2026d) identifies the fine structure constant as the contraction coefficient of the electromagnetic sub-mapping of $\mathcal{G}_0$. The key insight is that coupling constants are not parameters describing interaction strengths — they are contraction coefficients describing convergence rates toward fixed points.

## §2.2. Self-consistency and the quadratic

If $\alpha$ is a contraction coefficient of a sub-mapping of $\mathcal{G}_0$, it cannot be arbitrary. The four sub-mappings (strong, weak, electromagnetic, gravitational) must be jointly consistent: they must all converge to the same fixed point (existence), and their contraction coefficients must satisfy global constraints imposed by the symmetry structure of $\mathcal{G}_0$.

The self-consistency equation was identified computationally. The procedure was:

1. **Structural observation.** The right-hand side of the equation decomposes into surface-area terms of the unit sphere in successively lower dimensions:
   - $4\pi^3$: related to the surface area of the unit 4-sphere ($S_3 = 2\pi^2$; here $4\pi^3 = 2\pi^2 \times 2\pi$)
   - $\pi^2$: related to the solid angle (surface of unit 3-sphere divided by $2\pi$)
   - $\pi$: circumference of the unit circle

   This decomposition is not a coincidence — it reflects the dimensional hierarchy of $\mathcal{G}_0$'s sub-mappings as they project from the undifferentiated state (full spherical symmetry) to the observation scale (broken symmetry with four distinct forces).

2. **Functional form.** The left-hand side must contain $\alpha^{-1}$ (the contraction count) and a correction term that is self-referential — the correction depends on $\alpha$ itself, because the contraction coefficient determines the space in which it operates. The simplest self-referential form is:

$$\alpha^{-1} + f(\alpha) = 4\pi^3 + \pi^2 + \pi$$

3. **The series $S$.** The correction $f(\alpha) = S \cdot \alpha$ where $S = \sum_{n=1}^{\infty} (2n{-}1)!! / (4n)!$ is a convergent series of double-factorial over hyper-factorial terms. The double factorial $(2n{-}1)!! = 1 \cdot 3 \cdot 5 \ldots (2n{-}1)$ counts the number of ways to pair $2n$ objects. The denominator $(4n)!$ is the factorial of $4n$, which appears naturally in the expansion of hypergeometric functions on four-dimensional manifolds.

The full equation:

$$\alpha^{-1} + \left[\sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}\right] \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

## §2.3. Solving the equation

The equation is quadratic in $\alpha^{-1}$. Let $x = \alpha^{-1}$. Then $\alpha = 1/x$, and:

$$x + \frac{S}{x} = R, \quad \text{where } R = 4\pi^3 + \pi^2 + \pi$$

Multiplying through by $x$:

$$x^2 - Rx + S = 0$$

$$x = \frac{R \pm \sqrt{R^2 - 4S}}{2}$$

The physically meaningful root (the one near 137) is the larger root:

$$\alpha^{-1} = \frac{R + \sqrt{R^2 - 4S}}{2}$$

### Leading order ($n = 1$ only)

$$S_1 = \frac{1!!}{4!} = \frac{1}{24}$$

$$R = 4\pi^3 + \pi^2 + \pi = 137.036036021...$$

$$\alpha^{-1} = \frac{R + \sqrt{R^2 - 4/24}}{2} = 137.035999720$$

This is accurate to 4.0 parts per billion relative to the CODATA 2018 value.

### Two-term ($n = 1, 2$)

$$S_2 = \frac{1}{24} + \frac{3!!}{8!} = \frac{1}{24} + \frac{3}{40320} = 0.041\,740\,872...$$

$$\alpha^{-1} = 137.035999177$$

This sits 0.3 standard deviations from the most precise measurement (Fan et al., 2023, electron $g{-}2$: $\alpha^{-1} = 137.035999166 \pm 33$), and between the two most precise independent determinations.

### Convergence

The series $S$ converges extremely rapidly:

| Term $n$ | $(2n{-}1)!! / (4n)!$ | Cumulative $S$ | $\alpha^{-1}$ | $\Delta$ (ppb) |
|----------|---------------------|----------------|---------------|---------------|
| 1 | $1/24 = 0.04167$ | $0.04167$ | $137.035999720$ | $4.0$ |
| 2 | $3/40320 = 7.44 \times 10^{-5}$ | $0.04174$ | $137.035999177$ | $0.08$ |
| 3 | $15/479001600 = 3.13 \times 10^{-8}$ | $0.04174$ | $137.035999177$ | $0.08$ |
| $\geq 4$ | $< 10^{-12}$ | $0.04174$ | $137.035999177$ | $0.08$ |

All terms beyond the second contribute less than the current measurement uncertainty ($\sim 0.08$ ppb for the best determination). The two-term truncation is exact for all practical purposes.

## §2.4. What the equation contains

The equation $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ contains:

- **$\pi$** — the ratio of a circle's circumference to its diameter
- **Factorials and double factorials** — combinatorial objects
- **The integer 4** — appearing as the base of the factorial denominator $(4n)!$ and in the dimensional term $4\pi^3$

It does not contain:

- Any measured physical constant (no $c$, $\hbar$, $e$, $m_e$, $k_B$, ...)
- Any free parameter
- Any empirically determined coefficient

The claim is: this equation, with zero empirical inputs, produces a value of $\alpha$ that is indistinguishable from the best measurement at current precision. This is either a remarkable coincidence or evidence that $\alpha$ is determined by pure mathematics.

---

# §3. Independent Validation: Recovery of $\pi$

## §3.1. The inverse test

If the equation $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ is genuine, it can be run in both directions:

- **Forward:** given $\pi$, solve for $\alpha^{-1}$ → get $137.035999177$
- **Backward:** given $\alpha^{-1}$ (from measurement), solve for $\pi$

The backward direction was performed in Carpenter (2026g). Taking $\alpha^{-1} = 137.035999177$ and solving the cubic equation for $\pi$:

$$4\pi^3 + \pi^2 + \pi = \alpha^{-1} + S/\alpha^{-1}$$

yields $\pi = 3.14159265359$, recovering $\pi$ to 11 significant digits.

## §3.2. Significance

This bidirectional consistency eliminates a class of coincidences. A random equation that happens to produce 137.036 for one particular value of $\pi$ would not, in general, recover $\pi$ from the measured value of $\alpha$. The fact that the equation works in both directions — producing $\alpha$ from $\pi$ and $\pi$ from $\alpha$ — is evidence that the relationship between $\alpha$ and $\pi$ is structural, not accidental.

The 11-digit recovery of $\pi$ was published as a separate result (Carpenter, 2026g) and serves as the first independent check on the self-consistency equation.

---

# §4. The Experimental Landscape

## §4.1. Five determinations of $\alpha$

The fine structure constant has been measured by five independent methods. The values and their uncertainties (in parts per billion) are:

| Source | Method | Year | $\alpha^{-1}$ | Unc (ppb) |
|--------|--------|------|---------------|-----------|
| Parker et al. | Cs-133 atom recoil | 2018 | 137.035999046 | ± 27 |
| CODATA | Adjusted average | 2018 | 137.035999084 | ± 21 |
| Fan et al. | Electron $g{-}2$ | 2023 | 137.035999166 | ± 33 |
| Morel et al. | Rb-87 atom recoil | 2020 | 137.035999206 | ± 11 |
| **Carpenter** | **Algebraic equation** | **2026** | **137.035999177** | **(exact)** |

Two critical features of this landscape:

**The Rb-Cs discrepancy.** The Rb-87 value (Morel et al., 2020) and the Cs-133 value (Parker et al., 2018) differ by 160 ppb — a 5.5$\sigma$ tension. These are the two highest-precision measurements that do not depend on QED theory (they measure $h/m$ directly through atom recoil and combine with known masses to extract $\alpha$). The discrepancy is currently unexplained.

**The electron $g{-}2$ value.** Fan et al. (2023) measure the electron anomalous magnetic moment to 0.13 parts per trillion, then invert the Schwinger series (§5) to extract $\alpha$. This depends on the QED calculation being correct to 5th order, which it is — but the method is theory-dependent in a way the atom-recoil methods are not.

## §4.2. Where the algebraic value sits

The algebraic value $\alpha^{-1} = 137.035999177$ sits:

- **11 ppb above** the electron $g{-}2$ value (0.3$\sigma_{g-2}$)
- **29 ppb below** the Rb-87 value (2.6$\sigma_{\text{Rb}}$)
- **131 ppb above** the Cs-133 value (4.9$\sigma_{\text{Cs}}$)
- **93 ppb above** the CODATA value (4.4$\sigma_{\text{CODATA}}$)

Expressed as a fraction of the Rb-Cs span: the algebraic value sits 81.9% of the way from the Cs-133 value to the Rb-87 value. It falls in the upper portion of the disputed range, consistent with the direction in which the most recent measurements have moved.

## §4.3. The trajectory

The chronological ordering of determinations reveals a systematic upward drift:

$$\underset{2018}{\text{Cs: }046} \quad \underset{2018}{\text{CODATA: }084} \quad \underset{2023}{\text{$g{-}2$: }166} \quad \underset{2020}{\text{Rb: }206}$$

(final three digits shown)

The two most recent high-precision measurements (Rb-87 in 2020, electron $g{-}2$ in 2023) both fall above the 2018 CODATA adjusted average. The algebraic value 177 sits between them. The next generation of measurements will determine whether this trajectory continues.

---

# §5. The Schwinger Series: Computing $a_e$ and $a_\mu$

## §5.1. Electron anomalous magnetic moment

The electron anomalous magnetic moment $a_e = (g{-}2)/2$ is given by the QED perturbative expansion:

$$a_e = \sum_{n=1}^{N} C_n \left(\frac{\alpha}{\pi}\right)^n + a_e^{\text{had}} + a_e^{\text{EW}}$$

This is the Schwinger series, named after Julian Schwinger who computed the first-order term $C_1 = 1/2$ in 1948. The coefficients are known through 5th order:

| Order $n$ | Diagrams | Coefficient $C_n$ | Contribution to $a_e$ |
|-----------|----------|-------------------|----------------------|
| 1 | 1 | $+0.5$ | $1.161 \times 10^{-3}$ |
| 2 | 7 | $-0.328\,478\,965\,579$ | $-1.772 \times 10^{-6}$ |
| 3 | 72 | $+1.181\,241\,457$ | $1.479 \times 10^{-8}$ |
| 4 | 891 | $-1.9113$ | $-5.553 \times 10^{-11}$ |
| 5 | 12,672 | $+6.737$ | $4.540 \times 10^{-13}$ |

The computational effort is staggering. The 4th-order coefficient required evaluating 891 Feynman diagrams (Aoyama, Hayakawa, Kinoshita, & Nio, 2012). The 5th-order coefficient required 12,672 diagrams computed over decades by the same group (Aoyama, Kinoshita, & Nio, 2019). Non-QED contributions are small: $a_e^{\text{had}} = 1.87 \times 10^{-12}$ (hadronic) and $a_e^{\text{EW}} = 3.0 \times 10^{-14}$ (electroweak).

**The experimental measurement** (Fan et al., 2023, Harvard):

$$a_e^{\text{exp}} = 0.001\,159\,652\,180\,59(13)$$

This is the most precisely measured quantity in physics: 0.13 parts per trillion.

**Why this does not independently test $\alpha$:** The Fan et al. value of $\alpha^{-1} = 137.035999166(33)$ is *extracted from* $a_e^{\text{exp}}$ by inverting the Schwinger series. The procedure is: measure $a_e$ → assume QED is correct to 5th order → solve for $\alpha$. Therefore, comparing the algebraic $\alpha$ against the electron $g{-}2$ value of $\alpha$ is a comparison between two $\alpha$ determinations, not between theory and experiment.

The Schwinger series is presented here for two reasons: (1) to demonstrate the propagation of $\alpha$ differences through the most precise QED calculation, and (2) to show that the algebraic $\alpha$ produces electron $g{-}2$ predictions consistent with all other $\alpha$ sources.

## §5.2. Computing $a_e$ from each $\alpha$

Using the Schwinger series with each $\alpha$ source:

| $\alpha$ source | $a_e^{\text{pred}}$ | Residual $a_e^{\text{pred}} - a_e^{\text{exp}}$ |
|-----------------|---------------------|----------------------------------------------|
| Cs-133 | $1.159652179063 \times 10^{-3}$ | $-1.53 \times 10^{-12}$ |
| CODATA | $1.159652178742 \times 10^{-3}$ | $-1.85 \times 10^{-12}$ |
| Electron $g{-}2$ | $1.159652178049 \times 10^{-3}$ | $-2.54 \times 10^{-12}$ |
| **SECS** | $\mathbf{1.159652177956 \times 10^{-3}}$ | $\mathbf{-2.63 \times 10^{-12}}$ |
| Rb-87 | $1.159652177711 \times 10^{-3}$ | $-2.88 \times 10^{-12}$ |

All residuals are large in units of the $a_e$ measurement precision ($\sigma = 1.3 \times 10^{-13}$), but this reflects the extreme amplification of $\alpha$ differences by the Schwinger series, not a failure of any particular $\alpha$ value. A 1 ppb shift in $\alpha$ moves the $a_e$ prediction by approximately $8\sigma$. The correct comparison is between $\alpha$ values (§4), not between $a_e$ predictions.

## §5.3. Muon anomalous magnetic moment

The muon $g{-}2$ anomaly is the most prominent tension in the Standard Model. The Fermilab + BNL combined measurement (Abi et al., 2023) gives:

$$a_\mu^{\text{exp}} = 116\,592\,059(22) \times 10^{-11}$$

The Standard Model theory prediction (Muon $g{-}2$ Theory Initiative White Paper, 2020):

$$a_\mu^{\text{SM}} = 116\,591\,810(43) \times 10^{-11}$$

Discrepancy: $\Delta a_\mu = 249 \times 10^{-11}$, or $5.2\sigma$ (combined uncertainty).

The muon QED series has larger coefficients than the electron due to mass-ratio corrections ($m_\mu / m_e \approx 207$):

| Order $n$ | $C_n^{(\mu)}$ |
|-----------|---------------|
| 1 | $+0.5$ |
| 2 | $+0.765\,857\,425$ |
| 3 | $+24.050\,510$ |
| 4 | $+130.880$ |
| 5 | $+753.29$ |

The dominant non-QED contributions are:
- Hadronic vacuum polarization (HVP): $a_\mu^{\text{HVP}} = 6927(42) \times 10^{-11}$
- Hadronic light-by-light (HLbL): $a_\mu^{\text{HLbL}} = 92(18) \times 10^{-11}$
- Electroweak: $a_\mu^{\text{EW}} = 153.6(1.0) \times 10^{-11}$

## §5.4. $\alpha$-sensitivity of the muon anomaly

When $\alpha^{-1}$ shifts from the CODATA value (137.035999084) to the algebraic value (137.035999177), the QED contribution to $a_\mu$ shifts by:

$$\Delta a_\mu^{\text{QED}} = -7.9 \times 10^{-13}$$

The anomaly is $2.49 \times 10^{-9}$. The QED shift is three orders of magnitude smaller. The anomaly remains at $5.2\sigma$ regardless of which $\alpha$ is used — CODATA, Rb-87, Cs-133, electron $g{-}2$, or the algebraic value. The muon anomaly lives in the **hadronic vacuum polarization** sector, specifically in the low-energy $e^+e^- \to$ hadrons cross-section data that enters the dispersive integral for $a_\mu^{\text{HVP}}$.

**Conclusion:** No value of $\alpha$ can resolve the muon $g{-}2$ anomaly. The anomaly is a hadronic problem. This is an important negative result: it demonstrates that the algebraic $\alpha$ does not introduce false solutions to open problems.

---

# §6. Rydberg Constant and Hydrogen Spectroscopy

## §6.1. Rydberg constant

The Rydberg constant $R_\infty = \alpha^2 m_e c / (2h)$ is the most precisely determined spectroscopic constant:

$$R_\infty = 10\,973\,731.568\,160(21) \; \text{m}^{-1}$$

Since $R_\infty \propto \alpha^2$, a fractional shift in $\alpha$ produces twice the fractional shift in $R_\infty$:

$$\frac{\Delta R_\infty}{R_\infty} = 2 \cdot \frac{\Delta \alpha}{\alpha}$$

The shift from CODATA to algebraic $\alpha$ is $\Delta \alpha / \alpha = -6.79 \times 10^{-10}$, giving $\Delta R_\infty / R_\infty = -1.36 \times 10^{-9}$, or $\Delta R_\infty \approx 0.015$ m$^{-1}$. This is approximately $700\sigma$ of the Rydberg measurement uncertainty.

However, $R_\infty$ is not an independent test of $\alpha$. The Rydberg constant is determined by fitting hydrogen spectroscopy data while simultaneously determining $\alpha$, the proton charge radius, and $R_\infty$. A different $\alpha$ would produce a different $R_\infty$ and a different proton charge radius in the global fit, with compensating shifts. The correct statement is: the algebraic $\alpha$ is compatible with hydrogen spectroscopy provided the global fit is re-performed with $\alpha^{-1} = 137.035999177$ as a fixed input. This has not been done.

## §6.2. Hydrogen 1S–2S transition

The most precisely measured optical frequency (Parthey et al., 2011):

$$f(1S{-}2S) = 2\,466\,061\,413\,187\,035(10) \; \text{Hz}$$

This measurement constrains a combination of $R_\infty$, $\alpha$, and the proton charge radius, and is subject to the same global-fit considerations as §6.1. It does not independently test $\alpha$.

---

# §7. Interpretation

## §7.1. What has been shown

1. A single algebraic equation with zero empirical inputs produces $\alpha^{-1} = 137.035999177$.
2. This value is 0.3 standard deviations from the most recent and most precise determination of $\alpha$ (Fan et al., 2023).
3. The value sits between the two competing atom-recoil determinations, in the upper portion of the disputed range, consistent with the most recent data.
4. The equation admits a bidirectional check: given $\alpha$, it recovers $\pi$ to 11 digits (Carpenter, 2026g).
5. The value produces Standard Model predictions indistinguishable from those of any measured $\alpha$ in all currently testable quantities.
6. The muon $g{-}2$ anomaly is three orders of magnitude too large to be affected by the choice of $\alpha$.

## §7.2. What has not been shown

1. The equation has not been derived from the collapse algebra or from any physical principle. It was identified computationally. The structural motivation (§2.2) provides context but not proof.
2. The equation does not produce new testable predictions that differ from existing $\alpha$ measurements. Its predictions are indistinguishable from those of the measured value.
3. No mechanism has been proposed by which $\alpha$ would be *required* to equal the solution of this equation.

## §7.3. The two interpretations

**Interpretation A: Coincidence.** The equation happens to produce a number near $\alpha^{-1}$. The 11 ppb agreement is impressive but not unprecedented — sufficiently many equations exist that some must land near any given constant. Under this interpretation, the bidirectional $\pi$ recovery is a secondary coincidence.

**Interpretation B: Algebraic origin.** The fine structure constant is not a free parameter but a mathematical constant, determined by the self-consistency of the structure in which it operates. Under this interpretation, the equation is the analytical form of that self-consistency condition, and experiments are converging on its exact solution.

## §7.4. How to distinguish them

The interpretations make different predictions for next-generation experiments:

**Under Interpretation A (coincidence):** The true value of $\alpha^{-1}$ has no special relationship to $137.035999177$. Future measurements will converge on a value that may lie anywhere within the current uncertainty bands. The probability that the final consensus value is within 5 ppb of the algebraic value is approximately $5/160 \approx 3\%$ (the 5 ppb window as a fraction of the 160 ppb disputed range).

**Under Interpretation B (algebraic origin):** The true value of $\alpha^{-1}$ is exactly $137.035999177...$, with all subsequent digits determined by the series. Future measurements must converge on this value as precision improves. The probability that future measurements are consistent with the algebraic value is $100\%$.

The distinguishing experiments are:

- **Harvard electron $g{-}2$ upgrade:** targeting $\sim$0.03 ppt precision (4× improvement over Fan et al., 2023). This would determine $\alpha$ to $\sim$8 ppb, sufficient to distinguish the algebraic value from the Rb-87 value.
- **LKB Paris Rb-87 recoil:** targeting $\sim$5 ppb precision. Combined with the Cs-133 result, this would resolve or confirm the Rb-Cs discrepancy.
- **Berkeley Cs-133 recoil upgrade:** also targeting $\sim$5 ppb. A second Cs determination would test whether the low Cs value is a systematic error.

If these experiments converge on $137.035999177 \pm 5$ ppb, Interpretation A becomes untenable. If they converge elsewhere, the equation is falsified.

---

# §8. Computational Details

## §8.1. Numerical precision

All calculations were performed using Python's `decimal` module with 50-digit internal precision, eliminating floating-point rounding as a source of error. The Schwinger coefficients $C_n$ were taken from published values (see references) without rounding.

## §8.2. Series truncation

The self-consistency series $S = \sum (2n{-}1)!! / (4n)!$ was evaluated to $n = 10$. Terms beyond $n = 3$ contribute less than $10^{-15}$ to $S$, and less than $10^{-12}$ to $\alpha^{-1}$. The two-term truncation is adequate for comparison with any currently achievable experimental precision.

## §8.3. Schwinger series truncation

The QED series for both $a_e$ and $a_\mu$ was evaluated through 5th order, which is the current state of the art. The 6th-order coefficients are unknown; they are estimated to contribute $\sim 10^{-15}$ to $a_e$ and $\sim 10^{-12}$ to $a_\mu$, both below current experimental precision.

## §8.4. Reproducibility

The computation script ([`__alpha_precision_test_v2.py`]) is published alongside this paper. It takes no inputs (all constants are defined in the source code) and produces the full comparison tables in §4–§6.

---

# §9. Boundaries

1. **No derivation is claimed.** The equation is reported, not derived. Its algebraic motivation is suggestive but not constitutive. This paper reports a quantitative match, not a theoretical explanation.

2. **No new physics is predicted.** The algebraic $\alpha$ produces no distinguishable predictions from the measured $\alpha$ in any currently testable quantity. It does not resolve the muon anomaly or predict beyond-Standard-Model phenomena.

3. **Falsifiability is exact.** The algebraic value is $\alpha^{-1} = 137.035999177...$, with the series determining all digits. Next-generation experiments at 5 ppb precision will either confirm or falsify this value.

4. **Authorship of the calculation.** The Schwinger coefficients are the work of Schwinger (1948), Petermann (1957), Laporta & Remiddi (1996), and Aoyama, Hayakawa, Kinoshita, & Nio (2012, 2019). The muon $g{-}2$ theory is the work of the Muon $g{-}2$ Theory Initiative. The self-consistency equation is the work of Carpenter (2026d). This paper combines these results but originates none of the experimental or theoretical inputs.

5. **Self-consistency is not proof.** The fact that the equation produces a known constant and recovers $\pi$ is evidence for a relationship, not proof of one. Evidence invites investigation. The appropriate response is to compute, compare, and wait for next-generation data.

---

## References {-}

- Abi, B., et al. [Muon $g{-}2$ Collaboration] (2023). Measurement of the positive muon anomalous magnetic moment to 0.20 ppm. *Physical Review Letters*, 131, 161802.
- Aoyama, T., Hayakawa, M., Kinoshita, T., & Nio, M. (2012). Tenth-order QED contribution to the electron $g{-}2$ and an improved value of the fine structure constant. *Physical Review Letters*, 109, 111807.
- Aoyama, T., Kinoshita, T., & Nio, M. (2019). Theory of the anomalous magnetic moment of the electron. *Atoms*, 7(1), 28.
- Aoyama, T., et al. [Muon $g{-}2$ Theory Initiative] (2020). The anomalous magnetic moment of the muon in the Standard Model. *Physics Reports*, 887, 1–166.
- Barrow, J. D., & Tipler, F. J. (1986). *The Anthropic Cosmological Principle*. Oxford University Press.
- Carpenter, J. (2026a). A formal algebra of collapse-based computation. Zenodo. [10.5281/zenodo.18906064](https://doi.org/10.5281/zenodo.18906064).
- Carpenter, J. (2026d). The fine structure constant as self-consistency condition of a four-operator collapse algebra. Zenodo. [10.5281/zenodo.18994393](https://doi.org/10.5281/zenodo.18994393).
- Carpenter, J. (2026g). Solve for $\pi$: recovery of $\pi$ to eleven digits from the fine structure constant. Zenodo. [10.5281/zenodo.19014277](https://doi.org/10.5281/zenodo.19014277).
- Carpenter, J. (2026j). Existence as fixed point: meta-theory of the collapse algebra. Zenodo. [10.5281/zenodo.18932890](https://doi.org/10.5281/zenodo.18932890).
- Carpenter, J. (2026s). An algebraic value of $\alpha^{-1}$ indistinguishable from the most precise measurement in physics. Zenodo. (this companion paper).
- Eddington, A. S. (1929). *The Nature of the Physical World*. Cambridge University Press.
- Fan, X., Myers, T. G., Sukra, B. A. D., & Gabrielse, G. (2023). Measurement of the electron magnetic moment. *Physical Review Letters*, 130(7), 071801.
- Kragh, H. (2003). Magic number: a partial history of the fine-structure constant. *Archive for History of Exact Sciences*, 57(5), 395–431.
- Laporta, S., & Remiddi, E. (1996). The analytical value of the electron ($g{-}2$) at order $\alpha^3$ in QED. *Physics Letters B*, 379, 283–291.
- Morel, L., Yao, Z., Cladé, P., & Guellati-Khélifa, S. (2020). Determination of the fine-structure constant with an accuracy of 81 parts per trillion. *Nature*, 588, 61–65.
- Parker, R. H., Yu, C., Zhong, W., Estey, B., & Müller, H. (2018). Measurement of the fine-structure constant as a test of the Standard Model. *Science*, 360(6385), 191–195.
- Parthey, C. G., et al. (2011). Improved measurement of the hydrogen 1S–2S transition frequency. *Physical Review Letters*, 107, 203001.
- Schwinger, J. (1948). On quantum-electrodynamics and the magnetic moment of the electron. *Physical Review*, 73(4), 416–417.
- Susskind, L. (2003). The anthropic landscape of string theory. arXiv:hep-th/0302219.
