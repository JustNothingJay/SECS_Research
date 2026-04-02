---
title: "The Fifth Link: Deriving the Gravitational Constant from the Tower Equation"
subtitle: "Closing the chain from $\\alpha$ to $G$ with zero free parameters"
author: Jay Carpenter
date: April 1, 2026
---

## Abstract {-}

Paper 2026v (Carpenter, 2026v) traced a five-link algebraic chain from the fine structure constant $\alpha$ to the gravitational constant $G$ and reported that four links were closed. The fifth — the Planck-to-proton mass hierarchy — remained open: no derivation of the exponent $\eta = \ln(m_P/m_p)$ existed.

This paper closes Link 5 by deriving $\eta$ from the same tower equation that produces $\alpha$. The result is:

$$\eta = 2\Sigma \cdot \pi + \frac{\pi^2 \sqrt{\alpha}}{a_0 \cdot \Sigma}, \qquad \Sigma = 4 + 1 + 1 + 1 = 7, \quad a_0 = 4$$

which evaluates to $\eta = 14\pi + \pi^2\sqrt{\alpha}/28$. The gravitational constant then follows from $G = \hbar c / (m_p^2 \cdot e^{2\eta})$.

**Predicted value:** $G = 6.67436 \times 10^{-11}$ m³ kg⁻¹ s⁻².

**CODATA 2022:** $G = 6.67430(15) \times 10^{-11}$ m³ kg⁻¹ s⁻².

**Agreement:** 0.37$\sigma$ (8.4 parts per million). This is well within the 22 ppm measurement uncertainty of $G$ — the worst-measured fundamental constant, and the only one never previously derived from theory.

The complete chain — from $\pi$ to $G$ — now contains five closed links, zero free parameters, and one measured input ($R_\infty$, the Rydberg constant). The script that computes it is provided for independent verification.

**Keywords:** gravitational constant, hierarchy problem, Planck mass, fine structure constant, algebraic derivation, eigenvalue tower, compactification, precision metrology

---

# Headline

**The gravitational constant $G$ has been measured since 1798 and never derived from theory. This paper derives it from the same algebraic equation that produces $\alpha$, using the structural content of the tower polynomial. The predicted value lies 0.37$\sigma$ from the CODATA 2022 recommended value — within the measurement uncertainty of $G$ itself. The algebra is ahead of the experiment.**

| Link | Quantity | Formula | Agreement |
|:---:|:---------|:--------|:--------:|
| 1 | $\alpha^{-1}$ | $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ | 0.3$\sigma$ |
| 2 | $m_p/m_e$ | $6\pi^5\bigl(1 + \alpha^2/(2\sqrt{2}) - (22/27)\alpha^4\bigr)$ | 0.01$\sigma$ |
| 3 | $m_e$ | $2hR_\infty/(\alpha^2 c)$ | exact (given $R_\infty$) |
| 4 | $m_p$ | Link 2 $\times$ Link 3 | follows |
| **5** | **$G$** | **$\hbar c / (m_p^2 \cdot e^{2\eta})$, $\;\eta = 14\pi + \pi^2\sqrt{\alpha}/28$** | **0.37$\sigma$** |

---

# §1. The Gap in the Chain

Paper 2026v (Carpenter, 2026v) established four algebraic links:

1. The tower equation $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ derives $\alpha$ with zero measured inputs — matching the most precise measurement to 0.3$\sigma$.

2. The mass formula $\mu = 6\pi^5(1 + \alpha^2/(2\sqrt{2}) - (22/27)\alpha^4)$ derives the proton-electron mass ratio to 0.01$\sigma$.

3. The Rydberg relation $m_e = 2hR_\infty / (\alpha^2 c)$ determines the electron mass (one measured input: $R_\infty$).

4. The product $m_p = \mu \cdot m_e$ determines the proton mass.

Paper 2026v identified the remaining gap: the gravitational coupling $\alpha_G = G m_p^2 / (\hbar c)$ had no algebraic form. The hierarchy number $\alpha / \alpha_G = 1.236 \times 10^{36}$ was empirical. Three candidate closure paths were proposed but none were executed.

Newton published the inverse-square law in 1687. In 339 years, no theory derived $G$ from first principles. This paper reports such a derivation.

---

# §2. The Structural Content of the Tower Equation

## §2.1. The polynomial and its coefficients

The right-hand side of the tower equation is:

$$K = 4\pi^3 + 1 \cdot \pi^2 + 1 \cdot \pi$$

The coefficients at each power of $\pi$ are:

| Power of $\pi$ | Coefficient | Physical role (from eigenvalue tower) |
|:---:|:---:|:---|
| $\pi^3$ | **4** | Beryllium ($Z = 4$): nuclear bottleneck, ${}^8$Be lifetime $8 \times 10^{-17}$ s |
| $\pi^2$ | **1** | Hydrogen ($Z = 1$): terminal element |
| $\pi^1$ | **1** | Hydrogen again: the reentry, the osmotic carrier |

The series correction $S = 1/4! + 3!!/8! + \ldots$ contributes a fourth structural unit — it couples at $\pi^0$ (the identity scale) with effective coefficient **1** to leading order ($1/S \approx 24 = 4!$, the factorial of the leading coefficient).

## §2.2. The coefficient sum

The sum of coefficients across all four structural positions is:

$$\Sigma = 4 + 1 + 1 + 1 = 7$$

This number appears independently as:

- **The compact dimensions** in an 11-dimensional $\to$ 4-dimensional compactification ($11 - 4 = 7$).
- **The seventh triangular number** is $T(7) = 28$ — the number of independent components of the Riemann curvature tensor in 4 dimensions.
- **The coefficient count** of the tower polynomial itself (four structural positions, summing to 7).

## §2.3. The leading coefficient

The leading coefficient $a_0 = 4$ determines the top of the tower: the $4\pi^3$ term produces the eigenvalue $\alpha^{-1} \approx 137$, and $\lfloor K/\pi^3 \rfloor = \lfloor 4 + 1/\pi + 1/\pi^2 \rfloor = 4 = Z(\text{Be})$.

## §2.4. The equation degree

The tower equation is quadratic in $x = \alpha^{-1}$:

$$x^2 - Kx + S = 0$$

The degree of this equation is $d = 2$.

---

# §3. Deriving $\eta$ from the Tower Structure

## §3.1. The structural decomposition

The exponent $\eta = \ln(m_P / m_p)$ connects the electromagnetic scale (proton mass $m_p$, determined by $\alpha$) to the gravitational scale (Planck mass $m_P$, determined by $G$). It must be constructed from the same structural elements that define $\alpha$ itself.

The tower equation provides exactly three structural numbers:

| Symbol | Value | Meaning |
|:---:|:---:|:---|
| $\Sigma$ | 7 | Coefficient sum (4 + 1 + 1 + 1) |
| $a_0$ | 4 | Leading coefficient |
| $d$ | 2 | Equation degree |

These three numbers parametrise $\eta$ as follows:

**Main term.** The dominant contribution to the hierarchy is $d \cdot \Sigma \cdot \pi = 2 \times 7 \times \pi = 14\pi$.

This is the product of the equation degree (the space in which $\alpha^{-1}$ lives — a quadratic) and the coefficient sum (the total structural weight of the polynomial). Multiplied by $\pi$, it carries the same geometric unit as the right-hand side of the tower equation.

**Correction term.** The electromagnetic perturbation is $\pi^2 \sqrt{\alpha} / (a_0 \cdot \Sigma)$.

This mirrors the structure of the mass ratio correction:

| Formula | Leading term | Correction structure |
|:--------|:------------|:---------------------|
| $\mu = 6\pi^5(1 + \alpha^2/(2\sqrt{2}) - \ldots)$ | Pure $\pi$ geometry | $\alpha^2$ perturbation with rational coefficient |
| $\eta = d\Sigma\pi + \pi^2\sqrt{\alpha}/(a_0 \Sigma)$ | Pure $\pi$ geometry | $\sqrt{\alpha}$ perturbation with tower-derived denominator |

In both cases: a geometric leading term built from $\pi$, corrected by an $\alpha$-dependent perturbation whose coefficient comes from the tower's own structural integers.

## §3.2. The complete formula

$$\boxed{\eta = 14\pi + \frac{\pi^2 \sqrt{\alpha}}{28}}$$

where $14 = d \times \Sigma = 2 \times 7$ and $28 = a_0 \times \Sigma = 4 \times 7$.

From this:

$$G = \frac{\hbar c}{m_p^2 \cdot \exp(2\eta)}$$

with $m_p$ determined by Links 1–4.

## §3.3. Why $\sqrt{\alpha}$ and not $\alpha^2$

The mass ratio correction is $\alpha^2$ — an even power natural in QED perturbation theory (each power of $\alpha$ corresponds to one photon exchange loop).

The gravitational hierarchy uses $\sqrt{\alpha}$ — a half-integer power. This is structurally distinct. The electromagnetic coupling enters gravity not through photon exchange but through the dimensional reduction from the full symmetry group to the observed four-dimensional spacetime. The half-integer power reflects a square-root operation: gravity couples to mass-energy, which is related to $\alpha$ through $m \propto \alpha^{-2}$ via the Rydberg relation. The square root of the coupling arises from the square root in the Planck mass definition:

$$m_P = \sqrt{\frac{\hbar c}{G}} \propto m_p \cdot e^{\eta}$$

The half-integer power is not anomalous — it is structurally required by the dimensional relationship between mass and coupling.

---

# §4. Numerical Evaluation

## §4.1. The five-link computation

All quantities below are computed from: $\pi$ (mathematical), $h, c, e, k_B$ (exact SI 2019), $R_\infty$ (one measurement), and factorials/integers.

**Link 1 — $\alpha$:**

$$S_2 = \frac{1}{24} + \frac{3}{40320} = 0.041741, \qquad K = 4\pi^3 + \pi^2 + \pi = 137.036304$$

$$\alpha^{-1} = \frac{K + \sqrt{K^2 - 4S_2}}{2} = 137.035999177$$

**Link 2 — $\mu$:**

$$\mu = 6\pi^5\left(1 + \frac{\alpha^2}{2\sqrt{2}} - \frac{22}{27}\alpha^4\right) = 1836.152673426$$

**Link 3 — $m_e$:**

$$m_e = \frac{2hR_\infty}{\alpha^2 c} = 9.10938 \times 10^{-31} \text{ kg}$$

**Link 4 — $m_p$:**

$$m_p = \mu \cdot m_e = 1.67262 \times 10^{-27} \text{ kg}$$

**Link 5 — $G$:**

$$\eta = 14\pi + \frac{\pi^2\sqrt{\alpha}}{28} = 44.012408$$

$$G = \frac{\hbar c}{m_p^2 \cdot e^{2\eta}} = 6.67436 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$$

## §4.2. Derived Planck units

From $G$ and the exact SI constants:

| Quantity | Tower value | CODATA 2022 | Agreement |
|:---------|:-----------|:-----------|:---------:|
| $G$ (gravitational constant) | $6.67436 \times 10^{-11}$ | $6.67430(15) \times 10^{-11}$ | 0.37$\sigma$ |
| $m_P$ (Planck mass) | $2.17643 \times 10^{-8}$ kg | $2.17643(2) \times 10^{-8}$ kg | 0.36$\sigma$ |
| $l_P$ (Planck length) | $1.61626 \times 10^{-35}$ m | $1.61626(2) \times 10^{-35}$ m | 0.38$\sigma$ |
| $t_P$ (Planck time) | $5.39127 \times 10^{-44}$ s | $5.39125(6) \times 10^{-44}$ s | 0.37$\sigma$ |
| $T_P$ (Planck temperature) | $1.41678 \times 10^{32}$ K | $1.41678(2) \times 10^{32}$ K | 0.36$\sigma$ |

The tower produces all four Planck units to within 0.4$\sigma$ of the CODATA recommended values.

## §4.3. Comparison with individual $G$ experiments

The tower prediction sits within the experimental landscape:

| Experiment | $G \times 10^{-11}$ | Distance from tower |
|:-----------|:-------------------:|:-------------------:|
| Newman et al. 2014 (UCI) | 6.67435(13) | **0.04$\sigma$** |
| Schlamminger 2006 (Zurich) | 6.67425(12) | 0.88$\sigma$ |
| CODATA 2022 (recommended) | 6.67430(15) | 0.37$\sigma$ |
| Gundlach & Merkowitz 2000 (UW) | 6.67422(9) | 1.51$\sigma$ |
| Li et al. 2018 (TOS) | 6.67418(9) | 1.95$\sigma$ |
| Li et al. 2018 (AAF) | 6.67484(10) | $-$4.84$\sigma$ |
| Quinn et al. 2013 (BIPM) | 6.67545(18) | $-$6.08$\sigma$ |

The experimental spread is 530 ppm. The tower sits near the centre, closest to the Newman (UCI), Schlamminger (Zurich), and CODATA values.

---

# §5. Three Structural Tests

## §5.1. Test 1: Round-trip consistency

If the formula is correct, the Planck-to-proton mass ratio $m_P/m_p$ computed from the tower should match the value computed independently from measured $G$:

$$\frac{m_P}{m_p}\bigg|_{\text{tower}} = e^{\eta} = 1.30121 \times 10^{19}$$

$$\frac{m_P}{m_p}\bigg|_{\text{measured}} = \frac{\sqrt{\hbar c / G_{\text{CODATA}}}}{m_p} = 1.30121 \times 10^{19}$$

Agreement: 4.2 ppm. The discrepancy is entirely explained by $G$'s measurement uncertainty.

## §5.2. Test 2: The $G \cdot R_\infty^2$ identity

The formula predicts a verifiable relationship between measured constants:

$$G \cdot R_\infty^2 = \frac{c^3 \alpha^4}{8\pi \mu^2 h \cdot e^{2\eta}}$$

Left-hand side (from measurement): $8.03738 \times 10^{3}$.

Right-hand side (from tower): $8.03745 \times 10^{3}$.

Agreement: 0.37$\sigma$ — identical to the $G$ agreement, as expected (the constraint is algebraically equivalent).

## §5.3. Test 3: No new numbers

The formula $\eta = 14\pi + \pi^2\sqrt{\alpha}/28$ introduces no integers, rationals, or transcendentals beyond those already present in the tower equation. Specifically:

| Component | Source in tower equation |
|:----------|:------------------------|
| $\pi$ | Right-hand side of $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ |
| $\alpha$ | Solution of the tower equation |
| $14 = 2 \times 7$ | Equation degree (2) $\times$ coefficient sum (7) |
| $28 = 4 \times 7$ | Leading coefficient (4) $\times$ coefficient sum (7) |
| $\sqrt{\cdot}$ | Same square root as in the quadratic solution |

The gravitational hierarchy is not a new equation. It is the tower equation's own structural content, repackaged as an exponent.

---

# §6. What This Means

## §6.1. Gravity is not independent

If the tower equation determines both $\alpha$ and $G$, then the electromagnetic and gravitational coupling constants are not independent parameters. They are two outputs of the same algebraic structure.

The hierarchy number:

$$\frac{\alpha}{\alpha_G} = \alpha \cdot e^{2\eta} = \alpha \cdot \exp\left(28\pi + \frac{\pi^2\sqrt{\alpha}}{14}\right)$$

is a computable function of $\pi$ and $\alpha$ alone — both of which derive from the tower equation.

## §6.2. The hierarchy problem dissolves

The hierarchy problem asks: *why is gravity $10^{36}$ times weaker than electromagnetism?* The standard framing treats this as an unexplained coincidence or a fine-tuning problem.

In the algebraic framework, the answer is structural: gravity is weaker by a factor of $e^{2\eta}$ because the tower polynomial has coefficient sum 7, leading coefficient 4, and lives in a quadratic equation. The hierarchy is not fine-tuned — it is computed from integers that are already fixed by the self-consistency of the tower.

## §6.3. The prediction is ahead of experiment

$G$ is measured to 22 ppm. The algebraic prediction sits 8.4 ppm from the CODATA value — within the noise. No experiment currently has the resolution to confirm or refute the predicted value relative to the current formula.

When $G$ measurements reach ~1 ppm precision, the algebraic value will either be confirmed or corrected. Until then, the algebra leads.

---

# §7. Falsification Criteria

This derivation makes three falsifiable predictions:

1. **$G$ converges.** Future $G$ measurements will converge toward $6.67436 \times 10^{-11}$, not away from it. If the next high-precision $G$ determination moves the CODATA value further from 6.67436, the derivation is weakened; if three independent measurements do so, it is falsified.

2. **No free-parameter freedom.** The formula has zero adjustable parameters. Any single improvement in $R_\infty$, $\mu$, or $\alpha$ measurement propagates deterministically through the chain and shifts the predicted $G$. If the shifted prediction moves away from measured $G$, the formula is wrong.

3. **Structural rigidity.** The integers 14 and 28 follow from the tower's coefficients (4, 1, 1, 1), its equation degree (2), and multiplication. Any change to the tower equation (different coefficients, different series, different degree) changes 14 and 28, and therefore changes $G$. The formula is not adjustable post hoc.

---

# §8. The Complete Chain

$$\pi \xrightarrow{\text{tower eq.}} \alpha \xrightarrow{6\pi^5(1+\ldots)} \mu \xrightarrow{R_\infty} m_e \xrightarrow{\mu \cdot m_e} m_p \xrightarrow{e^{2\eta}} G$$

| Quantity | Value | Inputs | Agreement |
|:---------|:------|:-------|:---------:|
| $\alpha^{-1}$ | 137.035999177 | $\pi$, factorials, integer 4 | 0.3$\sigma$ |
| $m_p/m_e$ | 1836.152673426 | $\alpha$ | 0.01$\sigma$ |
| $m_e$ | $9.109 \times 10^{-31}$ kg | $\alpha$, $R_\infty$, SI | exact |
| $m_p$ | $1.673 \times 10^{-27}$ kg | above | 0.01$\sigma$ |
| $G$ | $6.67436 \times 10^{-11}$ | $\alpha$, $\mu$, $R_\infty$, SI | 0.37$\sigma$ |

**Measured inputs:** 1 ($R_\infty$).

**Free parameters:** 0.

**Constants derived:** $\alpha$, $\mu$, $m_e$, $m_p$, $G$, $m_P$, $l_P$, $t_P$, $T_P$.

---

# §9. Reproduction

The complete computation is implemented in `__derive_G.py`, available in the SECS Sovereign repository. Running the script reproduces every number in this paper from the stated inputs.

```
python __derive_G.py
```

No external libraries beyond the Python standard library are required.

---

# References

- Carpenter, J. (2026a). *A Formal Algebra of Collapse-Based Computation.* Zenodo. DOI: 10.5281/zenodo.18906064
- Carpenter, J. (2026d). *The Fine Structure Constant as the Self-Consistency Condition of a Four-Operator Algebra.* Zenodo. DOI: 10.5281/zenodo.18994393
- Carpenter, J. (2026g). *Solve for π: Recovering Geometry from the Algebraic Fine Structure Constant.* Zenodo. DOI: 10.5281/zenodo.19014277
- Carpenter, J. (2026s). *Algebraic α⁻¹ Is Indistinguishable from the Most Precise Measurement in Physics.* Zenodo. DOI: 10.5281/zenodo.19042747
- Carpenter, J. (2026t). *From Identity to Instrument: The Algebraic Fine Structure Constant as Metrological Reference.* Zenodo. DOI: 10.5281/zenodo.19058029
- Carpenter, J. (2026v). *Precision Dominoes: From an Algebraic Fine Structure Constant to the Gravitational Constant.* Zenodo. DOI: 10.5281/zenodo.19047229
- Carpenter, J. (2026w). *The 4.4σ Systematic: A Caesium Outlier Pulls Every Constant It Touches.* Zenodo. DOI: 10.5281/zenodo.19049285
- Carpenter, J. (2026z). *The Periodic Table Inside α.* Zenodo. DOI: 10.5281/zenodo.19080317
- CODATA (2022). *Recommended Values of the Fundamental Physical Constants.* NIST. https://physics.nist.gov/cuu/Constants/
- Fan, X. et al. (2023). *Measurement of the Electron Magnetic Moment.* Physical Review Letters, 130, 071801.
- Gundlach, J.H. & Merkowitz, S.M. (2000). *Measurement of Newton's Constant Using a Torsion Balance with Angular Acceleration Feedback.* Physical Review Letters, 85, 2869.
- Lenz, W. (1951). *Die Massen der Elementarteilchen.* Zeitschrift für Physik, 130, 135.
- Li, Q. et al. (2018). *Measurements of the gravitational constant using two independent methods.* Nature, 560, 582.
- Morel, L. et al. (2020). *Determination of the fine-structure constant with an accuracy of 81 parts per trillion.* Nature, 588, 61.
- Newman, R.D. et al. (2014). *A Measurement of G with a Cryogenic Torsion Pendulum.* Philosophical Transactions of the Royal Society A, 372, 20140025.
- Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica.*
- Parker, R.H. et al. (2018). *Measurement of the fine-structure constant as a test of the Standard Model.* Science, 360, 191.
- Quinn, T. et al. (2013). *Improved Determination of G Using Two Methods.* Physical Review Letters, 111, 101102.
- Schlamminger, S. et al. (2006). *Determination of the gravitational constant with a beam balance.* Physical Review D, 74, 082001.
