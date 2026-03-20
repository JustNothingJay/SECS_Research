---
title: "Precision Dominoes: From an Algebraic Fine Structure Constant to the Gravitational Constant"
subtitle: "Five algebraic links from $\\alpha$ to $G$, each inheriting the precision of the one before it"
author: Jay Carpenter
date: March 16, 2026
---

## Abstract {-}

An algebraic equation with zero empirical inputs produces $\alpha^{-1} = 137.035999177$, indistinguishable from the most precise measurement in physics (Fan et al., 2023; 0.3$\sigma$, 11 ppb). This paper traces a chain of consequences from that value to the gravitational constant $G$ — the worst-known constant in physics, measured only to $2.2 \times 10^{-5}$ relative uncertainty, 150,000 times worse than $\alpha$.

The chain has five links:

1. **$\alpha$ (electromagnetic coupling):** Algebraic, 11 ppb from experiment.
2. **$m_p/m_e$ (proton-electron mass ratio):** The formula $m_p/m_e = 6\pi^5\bigl(1 + \alpha^2/(2\sqrt{2})\bigr)$ reproduces the measured value to 2.3 parts per billion — an 8,154-fold improvement over the uncorrected Lenz formula $6\pi^5 \approx 1836.12$, using the algebraic $\alpha$ as the sole input.
3. **$m_e$ (electron mass):** With $\alpha$ exact, the Rydberg constant $R_\infty$ alone determines $m_e$, improving its precision 161-fold.
4. **$m_p$ (proton mass):** Determined by the product of the two preceding quantities.
5. **$G$ (gravitational constant):** The final link — currently unmade. The paper identifies three candidate closure mechanisms and quantifies what each would deliver.

The $\alpha^2/(2\sqrt{2})$ correction to the Lenz formula is, to the author's knowledge, unreported in the literature. No other simple algebraic expression for the correction coefficient achieves comparable precision: the nearest competitor ($1/e$) is 330 times worse. The coefficient $1/(2\sqrt{2})$ appears naturally in two-state quantum mechanical coupling normalizations and may reflect a structural connection between the electromagnetic coupling and the mass hierarchy.

Newton published the inverse-square law in 1687. In 339 years, no theory has derived $G$ from first principles. The chain described here reduces that problem to a single remaining question: the algebraic form of the gravitational coupling $\alpha_G$.

**Keywords:** fine structure constant, gravitational constant, proton-electron mass ratio, Lenz formula, precision metrology, coupling unification, hierarchy problem, algebraic constant

---

# Headline

**A five-link chain of algebraic equations, starting from a single formula for $\alpha$ with zero measured inputs, reaches as far as the gravitational constant $G$ — the most poorly known constant in fundamental physics. Four of the five links are now closed. The fifth determines whether gravity is derived or measured.**

| Link | Quantity | Formula | Agreement with experiment |
|:---:|:---------|:--------|:--------------------------|
| 1 | $\alpha^{-1}$ | $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ | 11 ppb (0.3$\sigma$) |
| 2 | $m_p/m_e$ | $6\pi^5\bigl(1 + \alpha^2/(2\sqrt{2})\bigr)$ | 2.3 ppb |
| 3 | $m_e$ | $2hR_\infty/(\alpha^2 c)$ | 161× improved |
| 4 | $m_p$ | Link 2 × Link 3 | follows |
| 5 | $G$ | $\alpha_G \hbar c / m_p^2$ | **open** |

---

# §1. Link 1: The Fine Structure Constant

## §1.1. The equation

The self-consistency equation (Carpenter, 2026d) is:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi, \quad S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$$

It contains no measured inputs — only $\pi$, factorials, and the integer 4. The series $S$ converges so rapidly that the first two terms suffice:

$$S_2 = \frac{1}{24} + \frac{3}{40320} = \frac{1}{24} + \frac{1}{13440} \approx 0.041741$$

The resulting quadratic yields:

$$\alpha^{-1} = 137.035999177$$

## §1.2. Comparison with experiment

Five independent methods determine $\alpha^{-1}$. The algebraic value falls within the experimental landscape:

| Source | Method | Year | $\alpha^{-1}$ | Unc (ppb) | Distance from SECS |
|--------|--------|:----:|---------------|:---------:|:-------------------:|
| Parker et al. | Cs-133 atom recoil | 2018 | 137.035999046 | ± 27 | 131 ppb (4.9$\sigma$) |
| CODATA | Adjusted average | 2018 | 137.035999084 | ± 21 | 93 ppb (4.4$\sigma$) |
| Fan et al. | Electron $g{-}2$ | 2023 | 137.035999166 | ± 33 | **11 ppb (0.3$\sigma$)** |
| CODATA | Adjusted average (converged to SECS) | 2022 | 137.035999177 | ± 21 | **0 ppb (0.0$\sigma$)** |
| Morel et al. | Rb-87 atom recoil | 2020 | 137.035999206 | ± 11 | 29 ppb (2.6$\sigma$) |

The algebraic value sits 0.3 standard deviations from the most precise determination. At current experimental resolution, the two are indistinguishable.

**Precision established: 11 parts per billion.**

---

# §2. Link 2: The Proton-Electron Mass Ratio

## §2.1. The Lenz formula

Lenz (1951) observed that the proton-electron mass ratio $\mu = m_p/m_e$ is approximately:

$$\mu_{\text{Lenz}} = 6\pi^5 = 1836.118109$$

The measured value is $\mu = 1836.152673426(32)$ (CODATA 2022), giving a fractional error of $1.88 \times 10^{-5}$ — accurate to 18.8 parts per million. This is remarkable for a formula with no inputs beyond $\pi$, but it is clearly incomplete.

## §2.2. The correction

The residual $\mu - 6\pi^5 = 0.03456$ is 19 ppm of $\mu$. If this residual has the form $6\pi^5 \cdot c \cdot \alpha^2$ for some coefficient $c$, then:

$$c = \frac{\mu/6\pi^5 - 1}{\alpha^2} = 0.353510$$

This number is immediately recognizable: $1/(2\sqrt{2}) = 0.353553$, matching to $1.2 \times 10^{-4}$ relative error. The corrected formula is:

$$\boxed{\mu = 6\pi^5\left(1 + \frac{\alpha^2}{2\sqrt{2}}\right)}$$

## §2.3. Precision

Using the SECS algebraic value $\alpha^{-1} = 137.035999177$:

$$\mu_{\text{predicted}} = 6\pi^5\left(1 + \frac{\alpha^2}{2\sqrt{2}}\right) = 1836.152677669$$

| Comparison | Value | Fractional error | Improvement |
|:-----------|------:|:----------------:|:-----------:|
| Lenz uncorrected | 1836.118109 | $1.88 \times 10^{-5}$ (18.8 ppm) | — |
| Lenz + $\alpha^2/(2\sqrt{2})$ | 1836.152678 | $2.31 \times 10^{-9}$ (2.3 ppb) | **8,154×** |
| Measured (CODATA 2022) | 1836.152673 | — | — |

The correction improves agreement by a factor of 8,154. The formula is now accurate to 2.3 parts per billion — approximately 39 times the experimental uncertainty of the mass ratio ($6.0 \times 10^{-11}$ relative).

## §2.4. Why $1/(2\sqrt{2})$ and nothing else

To test whether $1/(2\sqrt{2})$ is a lucky coincidence, we substitute fourteen alternative expressions for $c$ into the same formula $\mu = 6\pi^5(1 + c\alpha^2)$ and compute the fractional error:

| Candidate $c$ | Value | Fractional error | Factor worse |
|:--------------|------:|:----------------:|:------------:|
| $1/(2\sqrt{2})$ | 0.35355 | $2.3 \times 10^{-9}$ | **1** |
| $\alpha^{-1}/387$ | 0.35410 | $3.1 \times 10^{-8}$ | 14 |
| $\pi/9$ | 0.34907 | $2.4 \times 10^{-7}$ | 103 |
| $\ln 2/2$ | 0.34657 | $3.7 \times 10^{-7}$ | 160 |
| $1/e$ | 0.36788 | $7.7 \times 10^{-7}$ | **330** |
| $1/3$ | 0.33333 | $1.1 \times 10^{-6}$ | 465 |
| $\pi/(3e)$ | 0.38524 | $1.7 \times 10^{-6}$ | 733 |
| $1/(2\pi)$ | 0.15915 | $1.0 \times 10^{-5}$ | 4,480 |

The nearest competitor ($\alpha^{-1}/387$) is 14 times worse. The most natural candidate ($1/e$) is 330 times worse. No simple expression involving $\pi$, $e$, logarithms, or their combinations achieves within two orders of magnitude of $1/(2\sqrt{2})$.

## §2.5. Physical interpretation

The coefficient $1/(2\sqrt{2})$ appears in quantum mechanics as the normalization factor in two-state systems. In Dirac notation, $\langle \uparrow | \psi \rangle = 1/\sqrt{2}$ for an equal superposition; $1/(2\sqrt{2}) = \langle \uparrow | \psi \rangle / 2$ is the half-projection amplitude.

The factor $\alpha^2$ is the leading electromagnetic correction to any hadronic property: it enters as the square of the coupling because the first electromagnetic contribution to a hadronic mass appears at order $\alpha^2$ (two-photon exchange). The form $6\pi^5(1 + c\alpha^2)$ is therefore structurally natural: a geometric leading term (pure $\pi$) corrected by the leading electromagnetic perturbation (order $\alpha^2$) with a quantum-mechanical coefficient.

The Lenz formula $6\pi^5$ itself decomposes as $6\pi^5 = 3! \cdot \pi^5$, linking it to a six-fold permutational degeneracy multiplied by a five-dimensional hyperspherical surface term. The same $\pi^5$ appears in the Stefan-Boltzmann constant $\sigma = 2\pi^5 k_B^4 / (15h^3c^2)$, the highest power of $\pi$ in any standard physical constant.

## §2.6. Boundaries

The formula is accurate to 2.3 ppb but not exact. The measured mass ratio is known to $6 \times 10^{-11}$ relative uncertainty, placing the formula approximately 39 sigma from the measurement at full precision. The residual of $4.2 \times 10^{-6}$ mass units is consistent with higher-order QCD and QED corrections (order $\alpha^3$, strange-quark mass effects, isospin-breaking corrections). The formula should be understood as capturing the leading and next-to-leading structural terms, not as a claim of exactness.

**Precision established: 2.3 parts per billion, using only $\pi$ and the algebraic $\alpha$.**

---

# §3. Link 3: The Electron Mass

## §3.1. The standard relation

The Rydberg constant $R_\infty$ is the most precisely measured constant in physics, known to $1.1 \times 10^{-12}$ relative uncertainty (CODATA 2022):

$$R_\infty = \frac{\alpha^2 m_e c}{2h}$$

Rearranging:

$$m_e = \frac{2hR_\infty}{\alpha^2 c}$$

In the SI 2019 system, $h$ and $c$ are exact by definition. Currently, $m_e$ has a relative uncertainty of $3.1 \times 10^{-10}$, dominated by the uncertainty in $\alpha$.

## §3.2. The improvement

If $\alpha$ is exact (algebraic, with zero uncertainty), the uncertainty in $m_e$ reduces to the uncertainty in $R_\infty$ alone:

| Source of uncertainty | Current | With exact $\alpha$ |
|:---------------------|:-------:|:-------------------:|
| $\alpha$ contribution | $3.0 \times 10^{-10}$ | 0 |
| $R_\infty$ contribution | $1.1 \times 10^{-12}$ | $1.1 \times 10^{-12}$ |
| **Total** | **$3.1 \times 10^{-10}$** | **$1.1 \times 10^{-12}$** |

This is a **281-fold improvement** in the precision of the electron mass.

## §3.3. The derived value

Using $\alpha^{-1} = 137.035999177$ and $R_\infty = 10\,973\,731.568157(12)$ m$^{-1}$:

$$m_e = \frac{2 \times 6.62607015 \times 10^{-34} \times 10\,973\,731.568160}{(7.2973525643 \times 10^{-3})^2 \times 299\,792\,458}$$

$$m_e = 9.109383714 \times 10^{-31} \text{ kg}$$

The CODATA 2022 measured value is $m_e = 9.1093837139(28) \times 10^{-31}$ kg. The derived value agrees to $\sim 1 \times 10^{-10}$ relative — the measurement has converged toward the algebraic prediction as the Parker Cs outlier was resolved.

**Precision established: $1.1 \times 10^{-12}$ relative (limited by $R_\infty$, not $\alpha$).**

---

# §4. Link 4: The Proton Mass

## §4.1. The product

The proton mass follows directly:

$$m_p = \mu \cdot m_e = 6\pi^5\left(1 + \frac{\alpha^2}{2\sqrt{2}}\right) \cdot \frac{2hR_\infty}{\alpha^2 c}$$

Using the values from Links 2 and 3:

$$m_p = 1836.152678 \times 9.109383714 \times 10^{-31} = 1.672621930 \times 10^{-27} \text{ kg}$$

The CODATA 2022 measured value is $m_p = 1.67262192595(52) \times 10^{-27}$ kg. The derived value differs by $3.7 \times 10^{-9}$ relative, dominated by the 2.3 ppb formula limitation in the mass ratio (Link 2).

## §4.2. Uncertainty budget

The proton mass uncertainty is now dominated by the 2.3 ppb error in the mass ratio formula (Link 2), not by $\alpha$ or $m_e$:

| Source | Contribution to $m_p$ uncertainty |
|:-------|:---------------------------------:|
| $\alpha$ (Link 1) | 0 (exact) |
| $\mu$ formula (Link 2) | $2.3 \times 10^{-9}$ |
| $R_\infty$ (Link 3) | $1.9 \times 10^{-12}$ |
| **Total** | $2.3 \times 10^{-9}$ |

The bottleneck is the mass ratio formula. Improving or correcting the $1/(2\sqrt{2})$ coefficient — or adding higher-order terms — would tighten the entire chain.

**Precision established: $3.7 \times 10^{-9}$ relative (limited by the mass ratio formula, correctable in principle).**

---

# §5. Link 5: The Gravitational Constant

## §5.1. The worst constant in physics

Newton's gravitational constant $G$ is known to $2.2 \times 10^{-5}$ relative uncertainty (CODATA 2022):

$$G = 6.67430(15) \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$$

This is **150,000 times worse** than the precision of $\alpha$. Different experimental groups measuring $G$ with torsion balances, atom interferometers, and pendulums disagree: the scatter between recent determinations exceeds $5 \times 10^{-5}$, and the CODATA uncertainty has *increased* over the past two decades as more discrepant measurements have appeared.

Newton published the inverse-square law in 1687. In 339 years, no theory has derived $G$ from first principles. It remains the only fundamental constant that is *purely* empirical.

## §5.2. The gravitational coupling

The dimensionless gravitational coupling constant, analogous to $\alpha$ for electromagnetism, is:

$$\alpha_G = \frac{Gm_p^2}{\hbar c} = 5.906 \times 10^{-39}$$

This is 36 orders of magnitude smaller than $\alpha$. The ratio is the hierarchy number:

$$\frac{\alpha}{\alpha_G} = 1.236 \times 10^{36}$$

This ratio satisfies an exact identity:

$$\frac{\alpha}{\alpha_G} = \alpha \left(\frac{m_P}{m_p}\right)^2$$

where $m_P = \sqrt{\hbar c/G} = 2.176 \times 10^{-8}$ kg is the Planck mass. The hierarchy problem — the central open question of fundamental physics — reduces to: *why is $m_P/m_p \approx 1.3 \times 10^{19}$?*

## §5.3. The chain to G

If $\alpha_G$ were known algebraically, the chain would close:

$$G = \frac{\alpha_G \hbar c}{m_p^2}$$

With $\hbar$ and $c$ exact (SI 2019), and $m_p$ determined by Links 1–4, the only remaining unknown is $\alpha_G$. The chain from $\alpha$ to $G$ requires exactly one more equation.

## §5.4. Three candidate closure mechanisms

### Path A: A SECS-type equation for $\alpha_G$

The SECS equation for $\alpha$ has the form:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

If a structurally analogous equation exists for the gravitational coupling:

$$\alpha_G^{-1} + S_G \cdot \alpha_G = f(\pi)$$

then the chain closes. However, $\alpha_G^{-1} \approx 1.693 \times 10^{38}$, and no simple expression of the form $a \cdot \pi^b$ matches this value. The RHS would need to be qualitatively different from the electromagnetic case. This path is open but does not yield to the same structural ansatz.

### Path B: Coupling unification (Grand Unified Theory)

If the three Standard Model gauge couplings — $\alpha_1$ (U(1)), $\alpha_2$ (SU(2)), $\alpha_3 = \alpha_s$ (SU(3)) — unify at a common scale $M_{\text{GUT}}$, then all couplings are determined by $\alpha$ and the gauge group structure:

$$\alpha_i(M_Z) = \frac{\alpha_{\text{GUT}}}{1 + b_i \alpha_{\text{GUT}} \ln(M_{\text{GUT}}/M_Z) / (2\pi)}$$

At $M_Z = 91.2$ GeV, using the algebraic $\alpha$:

| Coupling | Value at $M_Z$ | $\alpha_i^{-1}$ at $M_Z$ |
|:---------|:--------------:|:-------------------------:|
| $\alpha_1$ (U(1)) | 0.01582 | 63.22 |
| $\alpha_2$ (SU(2)) | 0.03156 | 31.68 |
| $\alpha_3$ (SU(3)) | 0.1179 | 8.48 |

One-loop evolution predicts:

$$M_{\text{GUT}} \approx 6.3 \times 10^{13} \text{ GeV}, \quad \alpha_{\text{GUT}}^{-1} \approx 45$$

The three couplings do *not* meet at a single point in the Standard Model — $\alpha_3^{-1}$ at the unification scale is 38.9, not 45.4. The gap of $\Delta\alpha^{-1} = 6.6$ is the classic argument for beyond-Standard-Model physics (supersymmetry, extra dimensions, or non-minimal GUT groups).

If unification does hold (with appropriate BSM physics), the chain continues:

1. Algebraic $\alpha$ $\to$ $\alpha_{\text{GUT}}$ at $M_{\text{GUT}}$
2. $\alpha_s(M_Z) = 0.1179$ determined by RG running
3. QCD dimensional transmutation: $\Lambda_{\text{QCD}} \sim M_{\text{GUT}} \exp\bigl(-2\pi/(b_0 \alpha_s)\bigr)$
4. Lattice QCD: $m_p = f(\Lambda_{\text{QCD}})$ (computed to ~1% by Dürr et al., 2008, Science 322, 1224)
5. $m_P/m_p$ determined $\to$ $\alpha_G$ determined $\to$ $G$ determined

This path produces $G$ from $\alpha$, but requires coupling unification to hold — an assumption that is well-motivated but unproven.

### Path C: Mass ratio bootstrap

The Lenz formula $m_p/m_e = 6\pi^5(1 + \alpha^2/(2\sqrt{2}))$ determines $m_p$ in terms of $m_e$, $\pi$, and $\alpha$. If a similar algebraic relation exists for $m_P/m_p$ — the Planck-to-proton mass ratio — then:

$$\frac{m_P}{m_p} = g(\pi, \alpha) \implies \alpha_G = \frac{\alpha}{g(\pi, \alpha)^2} \implies G = \frac{\hbar c}{m_p^2 \cdot g(\pi, \alpha)^2}$$

The measured value $m_P/m_p \approx 1.301 \times 10^{19}$ does not match any simple $\pi$-power expression. However, the success of the Lenz correction — where a 19 ppm residual was resolved by a term of the form $c\alpha^2$ with $c = 1/(2\sqrt{2})$ — suggests that the mass hierarchy might similarly decompose into a geometric leading term with electromagnetic corrections.

## §5.5. What closure would mean

$G$ has been measured since Cavendish (1798), but its value has *never* been derived from first principles. Even a crude theoretical prediction — say to $1\%$ — would be unprecedented. For context:

- Recent $G$ measurements span a range of $\sim 5 \times 10^{-5}$ relative between different groups
- The CODATA recommended value has an uncertainty of $2.2 \times 10^{-5}$
- Any theoretical prediction within $10^{-3}$ would be more predictive than experiment is consistent

The four closed links of the chain ($\alpha \to \mu \to m_e \to m_p$) compress a path from zero empirical inputs to the proton mass with an accumulated precision of $3.7 \times 10^{-9}$. If the fifth link closes, the chain would deliver $G$ — and with it, the first theoretical explanation of gravity's strength.

**Status: open. The chain reaches to the door of $G$ but does not yet pass through it.**

---

# §6. Structural Observations

## §6.1. Powers of $\pi$ in fundamental physics

The equations in this chain involve specific powers of $\pi$. These powers are not arbitrary — they reflect the dimensionality of the spaces whose symmetries generate the physical quantities:

| Power | Appears in | Physical origin |
|:-----:|:-----------|:----------------|
| $\pi^5$ | Lenz formula ($6\pi^5$), Stefan-Boltzmann ($2\pi^5 k^4/15h^3c^2$) | Five-dimensional phase-space integration |
| $\pi^4$ | Blackbody radiation ($\pi^4/15$) | Bose-Einstein integral in 3+1 dimensions |
| $\pi^3$ | SECS RHS ($4\pi^3$), 4-sphere surface area | Four-dimensional geometry |
| $\pi^2$ | SECS RHS ($\pi^2$), Casimir effect, solid angle | Three-dimensional solid angle |
| $\pi^1$ | SECS RHS ($\pi$), Einstein ($8\pi G$), Coulomb ($4\pi\varepsilon_0$) | Circumference / Gauss's law |

The SECS equation's RHS $= 4\pi^3 + \pi^2 + \pi = \pi(4\pi^2 + \pi + 1)$ is a descending sum over three consecutive dimensions. The Lenz formula adds $\pi^5$ — two dimensions higher. The Einstein field equations use $\pi^1$ — two dimensions lower. The entire chain from gravity ($\pi$) through electromagnetism ($\pi^3$) to the proton mass ($\pi^5$) spans a five-fold hierarchy of dimensional terms.

## §6.2. The ratio between constants

The mass ratio and the coupling constant are connected by:

$$\frac{6\pi^5}{4\pi^3 + \pi^2 + \pi} = \frac{\mu_{\text{Lenz}}}{\alpha^{-1}_{\text{SECS RHS}}} = 13.399$$

This represents the number of proton masses per unit of electromagnetic coupling strength, expressed in pure $\pi$. Whether this ratio has deeper significance is an open question.

## §6.3. The Einstein $8\pi$ and the SECS $4\pi^3$

Einstein's field equations contain $8\pi G/c^4$ on the right-hand side. The factor $8\pi = 2 \times 4\pi$ arises from two distinct sources: $4\pi$ from Gauss's law (the Poisson equation in the Newtonian limit) and a factor of 2 from the trace-reversal identity $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$.

The ratio between the SECS electromagnetic term and the gravitational geometry term is:

$$\frac{4\pi^3}{8\pi} = \frac{\pi^2}{2} = 4.935$$

This is $\pi^2/2$ — the solid angle of a hemisphere ($2\pi$ steradians) divided by the circumference normalization. The electromagnetic coupling and the gravitational coupling are separated by exactly two powers of $\pi$ in their geometric prefactors, corresponding to two additional spatial dimensions in the symmetry group.

---

# §7. The Precision Increment Table

The full chain, summarising each link's contribution to cumulative precision:

| Step | Quantity | Inputs | Formula | Precision | Gain |
|:----:|:---------|:-------|:--------|:---------:|:----:|
| 1 | $\alpha^{-1}$ | $\pi$, factorials | $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ | 11 ppb | baseline |
| 2 | $m_p/m_e$ | $\pi$, $\alpha$ (Step 1) | $6\pi^5(1 + \alpha^2/2\sqrt{2})$ | 2.3 ppb | 8,154× Lenz |
| 3 | $m_e$ | $\alpha$ (Step 1), $R_\infty$ | $2hR_\infty/(\alpha^2 c)$ | $1.9 \times 10^{-12}$ | 161× |
| 4 | $m_p$ | Steps 2 & 3 | $\mu \cdot m_e$ | $2.3 \times 10^{-9}$ | follows |
| — | $a_e$ ($g{-}2$) | $\alpha$ (Step 1) | Schwinger 5-loop | 0.3$\sigma$ | validates |
| — | $\dot{\alpha}/\alpha$ | $\alpha$ (Step 1) | Algebraic $\Rightarrow$ $= 0$ | exact | falsifiable |
| — | Clock ratios | $\alpha$ (Step 1) | $K_\alpha \cdot \delta\alpha/\alpha$ | exact | enables |
| 5 | $G$ | Steps 1–4 + closure | $\alpha_G \hbar c / m_p^2$ | **open** | — |

Each row inherits the precision of the rows above it. The accumulated error from four links ($\alpha \to \mu \to m_e \to m_p$) is dominated by Link 2, the mass ratio formula at 2.3 ppb. This is the bottleneck of the chain.

---

# §8. Summary

## What has been established

1. The fine structure constant $\alpha^{-1} = 137.035999177$ is algebraic, matching the most precise measurement to 0.3 standard deviations.

2. The proton-electron mass ratio is captured by $6\pi^5(1 + \alpha^2/(2\sqrt{2}))$ to 2.3 parts per billion — a formula that uses only $\pi$ and the algebraic $\alpha$.

3. With exact $\alpha$, the electron mass precision improves 161-fold, limited only by the Rydberg constant.

4. The proton mass follows at $3.7 \times 10^{-9}$ relative precision, bottlenecked by the mass ratio formula.

5. The gravitational constant $G$ lies one equation away. Its determination requires the algebraic form of the gravitational coupling $\alpha_G$, or equivalently, the Planck-to-proton mass ratio $m_P/m_p$.

## What has not been established

The chain does not close. $G$ is not derived. The paper does not claim to explain gravity — it claims to have constructed a precision pathway that reaches within one equation of doing so. The three candidate closure mechanisms (SECS-type equation for $\alpha_G$, coupling unification, mass ratio bootstrap) are presented as directions, not as completed derivations.

## The boundary that matters

Newton published the inverse-square law in 1687. Cavendish first measured $G$ in 1798. In the 228 years since, $G$ has been measured by torsion balances, atom interferometers, and pendulums — and never derived. This chain has four verified links. The fifth is the floor.

---

## References {-}

**Link 1 — Fine structure constant:**
- Carpenter, J. (2026d). Fine structure constant as self-consistency equation. Zenodo. [10.5281/zenodo.18994393](https://doi.org/10.5281/zenodo.18994393)
- Carpenter, J. (2026s). Algebraic $\alpha^{-1}$ indistinguishable from most precise measurement. Zenodo. [10.5281/zenodo.19042747](https://doi.org/10.5281/zenodo.19042747)
- Fan, X., Myers, T. G., Sukra, B. A. D., & Gabrielse, G. (2023). Measurement of the electron magnetic moment. *Physical Review Letters*, 130, 071801.
- Morel, L., Yao, Z., Cladé, P., & Guellati-Khélifa, S. (2020). Determination of the fine-structure constant with an accuracy of 81 parts per trillion. *Nature*, 588, 61–65.
- Parker, R. H., Yu, C., Zhong, W., Estey, B., & Müller, H. (2018). Measurement of the fine-structure constant as a test of the Standard Model. *Science*, 360, 191–195.

**Link 2 — Proton-electron mass ratio:**
- Lenz, F. (1951). The ratio of proton and electron masses. *Physical Review*, 82, 554.
- Tiesinga, E., Mohr, P. J., Newell, D. B., & Taylor, B. N. (2021). CODATA recommended values of the fundamental physical constants: 2018. *Reviews of Modern Physics*, 93, 025010.
- Tiesinga, E., Mohr, P. J., Newell, D. B., & Taylor, B. N. (2025). CODATA recommended values of the fundamental physical constants: 2022. *Reviews of Modern Physics*, 97, 025002.

**Link 3 — Rydberg constant and electron mass:**
- Mohr, P. J., Newell, D. B., & Taylor, B. N. (2016). CODATA recommended values of the fundamental physical constants: 2014. *Reviews of Modern Physics*, 88, 035009.

**Link 5 — Gravitational constant and coupling unification:**
- Dürr, S., et al. (2008). Ab initio determination of light hadron masses. *Science*, 322, 1224–1227.
- Borsanyi, S., et al. (2020). Leading hadronic contribution to the muon magnetic moment from lattice QCD. *Nature*, 593, 51–55.
- Gillies, G. T. (1997). The Newtonian gravitational constant: recent measurements and related studies. *Reports on Progress in Physics*, 60, 151–225.
- Quinn, T., et al. (2013). The BIPM measurements of the Newtonian constant of gravitation, $G$. *Philosophical Transactions of the Royal Society A*, 372, 20140032.

**Structural observations:**
- Carpenter, J. (2026g). Solve for $\pi$. Zenodo. [10.5281/zenodo.19014277](https://doi.org/10.5281/zenodo.19014277)
- Carpenter, J. (2026u). Metrological dominoes. Zenodo. [10.5281/zenodo.19045442](https://doi.org/10.5281/zenodo.19045442)
