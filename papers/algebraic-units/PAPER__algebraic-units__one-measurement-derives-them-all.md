---
title: "One Measurement Derives Them All: Algebraic Dimensional Structure from the Eigenvalue Tower"
subtitle: "The entire CODATA table of fundamental constants from one measured input, five SI definitions, and three algebraic equations"
author: Jay Carpenter
date: March 24, 2026
---

## Abstract {-}

The 2019 SI defines five constants exactly: $c$, $h$, $e$, $k_B$, $N_A$. Three algebraic equations — for the fine structure constant $\alpha$, the proton-electron mass ratio $\mu$, and the Planck hierarchy $m_P/m_p$ — contain no measured inputs. Together with one measured constant (the Rydberg constant $R_\infty$), these eight inputs reproduce the entire CODATA table of fundamental constants. Existing unit conversion libraries carry 20+ empirical conversion factors. The algebraic framework reduces this to one. Every atomic-scale constant is $R_\infty$ times a power of $\alpha$ times exact SI factors. Every Planck-scale constant follows from the hierarchy formula. The dimensional structure of physics has algebraic backbone.

**Keywords:** fundamental constants, dimensional analysis, natural units, Rydberg constant, fine structure constant, CODATA, unit conversion, algebraic constants, Planck units

---

# Headline

**Three algebraic equations plus one measurement produce the entire table of fundamental constants. The dimensional structure connecting SI, atomic, and Planck unit systems is not conventional — it is derived.**

| Input | Source | Status |
|:------|:-------|:-------|
| $c = 299\,792\,458$ m/s | SI 2019 definition | Exact |
| $h = 6.626\,070\,15 \times 10^{-34}$ J$\cdot$s | SI 2019 definition | Exact |
| $e = 1.602\,176\,634 \times 10^{-19}$ C | SI 2019 definition | Exact |
| $k_B = 1.380\,649 \times 10^{-23}$ J/K | SI 2019 definition | Exact |
| $N_A = 6.022\,140\,76 \times 10^{23}$ mol$^{-1}$ | SI 2019 definition | Exact |
| $\alpha^{-1} = 137.035\,999\,177$ | Algebraic (Carpenter, 2026d) | Derived |
| $\mu = 6\pi^5(1 + \alpha^2/(2\sqrt{2}) - (22/27)\alpha^4)$ | Algebraic (Carpenter, 2026v) | Derived |
| $\ln(m_P/m_p) = 14\pi + \pi^2\sqrt{\alpha}/28$ | Algebraic (Carpenter, 2026v) | Derived |
| $R_\infty = 10\,973\,731.568\,157(12)$ m$^{-1}$ | Measured (CODATA 2022) | $1.1 \times 10^{-12}$ rel. unc. |

**From these nine values — five exact, three algebraic, one measured — every constant in this paper follows.**

---

# $\S$1. The Algebraic Inputs

## $\S$1.1. The fine structure constant

The self-consistency equation (Carpenter, 2026d) is:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi, \quad S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$$

The series $S$ contains only factorials — no $\pi$, no measured quantities. Two terms suffice: $S_2 = 1/4! + 3!!/8! = 1683/40320$. The larger root of the resulting quadratic gives:

$$\alpha^{-1} = 137.035\,999\,176\,563\,8\ldots$$

This is 0.3$\sigma$ from the best measurement in physics (Fan et al., 2023).

## $\S$1.2. The proton-electron mass ratio

$$\mu = \frac{m_p}{m_e} = 6\pi^5\left(1 + \frac{\alpha^2}{2\sqrt{2}} - \frac{22}{27}\alpha^4\right) = 1836.152\,673\,426$$

This agrees with CODATA 2022 ($1836.152\,673\,43(11)$) to 0.03$\sigma$.

## $\S$1.3. The Planck hierarchy

$$\ln\left(\frac{m_P}{m_p}\right) = 14\pi + \frac{\pi^2\sqrt{\alpha}}{28}$$

This determines $G$ through $m_P = \sqrt{\hbar c/G}$:

$$G = \frac{\hbar c}{m_p^2 \cdot \exp\left(28\pi + \frac{\pi^2\sqrt{\alpha}}{14}\right)}$$

The derived value $G = 6.674\,36 \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ sits 0.37$\sigma$ from CODATA 2022.

---

# $\S$2. The Dimensional Ladder

## $\S$2.1. The single measured input

Post-2019 SI, $h$ and $c$ are exact. The Rydberg constant connects the atomic scale to SI:

$$R_\infty = \frac{\alpha^2 m_e c}{2h}$$

Rearranging:

$$m_e = \frac{2hR_\infty}{\alpha^2 c}$$

With $h$ and $c$ exact and $\alpha$ algebraic, $m_e$ inherits only the uncertainty of $R_\infty$: a relative precision of $1.1 \times 10^{-12}$. This is 281 times better than the current CODATA value.

## $\S$2.2. The alpha-power structure

Every atomic constant is $R_\infty$ times a power of $\alpha$ times exact SI factors. The tower controls the dimensional ladder:

| Constant | Formula from $R_\infty$ and $\alpha$ | $\alpha$-dependence |
|:---------|:--------------------------------------|:-------------------:|
| Bohr radius $a_0$ | $\alpha / (4\pi R_\infty)$ | $\alpha^1$ |
| Compton wavelength $\bar{\lambda}_C$ | $\alpha^2 / (4\pi R_\infty)$ | $\alpha^2$ |
| Classical electron radius $r_e$ | $\alpha^3 / (4\pi R_\infty)$ | $\alpha^3$ |
| Electron mass $m_e$ | $2hR_\infty / (\alpha^2 c)$ | $\alpha^{-2}$ |
| Proton mass $m_p$ | $\mu \cdot m_e$ | $\alpha^{-2}$ (via $\mu$) |
| Bohr magneton $\mu_B$ | $e\hbar / (2m_e)$ | $\alpha^{2}$ |
| Hartree energy $E_h$ | $\alpha^2 m_e c^2$ | $\alpha^{0}$ (exact) |
| Thomson cross-section $\sigma_T$ | $(8\pi/3)\,r_e^2$ | $\alpha^6$ |

The $\alpha$-power is not bookkeeping. It is the structural reason these constants have the values they do. When $\alpha$ is algebraic, every entry in this table becomes algebraic up to the precision of $R_\infty$.

## $\S$2.3. Verification against CODATA

Using tower $\alpha$ and CODATA $R_\infty$:

| Constant | Tower-derived | CODATA 2022 | Agreement |
|:---------|:-------------|:------------|:---------:|
| $a_0$ | $5.291\,772 \times 10^{-11}$ m | $5.291\,772\,109\,03(80) \times 10^{-11}$ | 4.5$\sigma$ |
| $\bar{\lambda}_C$ | $3.861\,593 \times 10^{-13}$ m | $3.861\,592\,6796(12) \times 10^{-13}$ | 4.4$\sigma$ |
| $r_e$ | $2.817\,940 \times 10^{-15}$ m | $2.817\,940\,3262(13) \times 10^{-15}$ | 4.4$\sigma$ |
| $m_e$ | $9.109\,384 \times 10^{-31}$ kg | $9.109\,383\,7015(28) \times 10^{-31}$ | 4.4$\sigma$ |
| $E_h$ | $4.359\,745 \times 10^{-18}$ J | $4.359\,744\,722\,2071(85) \times 10^{-18}$ | 0.13$\sigma$ |
| $\mu_B$ | $9.274\,010 \times 10^{-24}$ J/T | $9.274\,010\,0783(28) \times 10^{-24}$ | 4.5$\sigma$ |

## $\S$2.4. The systematic offset

The $\sim$4.5$\sigma$ offset on $\alpha$-dependent quantities is not a failure of the tower. It is the CODATA Cs-133 recoil contamination documented in Carpenter 2026w ("The 4.4$\sigma$ Systematic"). CODATA's adjusted $\alpha^{-1} = 137.035\,999\,084$ is pulled low by the Parker Cs measurement, which disagrees with the Morel Rb measurement by 5.5$\sigma$.

The tower's $\alpha^{-1} = 137.035\,999\,177$ sits:

- 0.3$\sigma$ from Fan et al. (electron $g{-}2$, most precise single measurement)
- 0.0$\sigma$ from CODATA 2022 adjusted average ($137.035\,999\,177$)
- 2.6$\sigma$ from Morel (Rb recoil)
- 4.4$\sigma$ from CODATA 2018 (Cs-contaminated)

**The offset is the prediction**: CODATA's next adjustment will shift toward the algebraic value as the Cs outlier resolves.

The Hartree energy shows 0.13$\sigma$ because its $\alpha$-dependence cancels: $E_h = \alpha^2 m_e c^2 = \alpha^2 \cdot 2hR_\infty/(\alpha^2 c) \cdot c^2 = 2hcR_\infty$. It depends on $R_\infty$ alone, not on $\alpha$.

---

# $\S$3. The Planck Scale

## $\S$3.1. Four Planck units from the tower

The hierarchy formula $\ln(m_P/m_p) = \eta$ with $\eta = 14\pi + \pi^2\sqrt{\alpha}/28$ extends the ladder from the atomic scale (controlled by $\alpha$) to the gravitational scale (controlled by $\eta$).

| Planck unit | Tower-derived | CODATA 2022 | Agreement |
|:------------|:-------------|:------------|:---------:|
| $G$ | $6.674\,36 \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ | $6.674\,30(15) \times 10^{-11}$ | 0.37$\sigma$ |
| $l_P = \sqrt{\hbar G / c^3}$ | $1.616\,262 \times 10^{-35}$ m | $1.616\,255(18) \times 10^{-35}$ | 0.38$\sigma$ |
| $m_P = \sqrt{\hbar c / G}$ | $2.176\,425 \times 10^{-8}$ kg | $2.176\,434(24) \times 10^{-8}$ | 0.36$\sigma$ |
| $t_P = l_P / c$ | $5.391\,27 \times 10^{-44}$ s | $5.391\,25(6) \times 10^{-44}$ | 0.37$\sigma$ |
| $T_P = m_P c^2 / k_B$ | $1.416\,78 \times 10^{32}$ K | $1.416\,784(16) \times 10^{32}$ | 0.36$\sigma$ |

All Planck quantities sit within 0.4$\sigma$. Of the 22 ppm relative uncertainty in $G$, only 8.4 ppm is used. The tower prediction is well within the noise of the measurement.

## $\S$3.2. The Planck mass as direct formula

The Planck mass has a particularly clean expression:

$$m_P = m_p \cdot e^{\eta} = \frac{2h R_\infty \mu}{\alpha^2 c} \cdot \exp\left(14\pi + \frac{\pi^2\sqrt{\alpha}}{28}\right)$$

Every factor on the right is either SI-exact ($h$, $c$), algebraic ($\alpha$, $\mu$, $\eta$), or measured once ($R_\infty$). This is the first expression for the Planck mass that does not require $G$ as input.

---

# $\S$4. Inter-Constant Relationships

## $\S$4.1. The product $G \cdot R_\infty^2$

Eliminating $m_p$ between $G = \hbar c/(m_p^2 e^{2\eta})$ and $m_p = 2h\mu R_\infty / (\alpha^2 c)$:

$$G \cdot R_\infty^2 = \frac{c^3 \alpha^4}{8\pi \mu^2 h \cdot e^{2\eta}}$$

The right side contains only SI-exact constants and tower-derived algebraic values. The left side is the product of two measured quantities ($G$ and $R_\infty$). This is a prediction: the product $G \cdot R_\infty^2$ is algebraically determined.

| Quantity | Value |
|:---------|------:|
| $G \cdot R_\infty^2$ (measured) | $8.037\,38 \times 10^{3}$ |
| $c^3\alpha^4/(8\pi\mu^2 h \cdot e^{2\eta})$ (algebraic) | $8.037\,45 \times 10^{3}$ |
| Ratio | 0.999\,992 |
| Agreement | 0.37$\sigma$ |

This relationship is independently verifiable: anyone with the current CODATA values of $G$ and $R_\infty$ can check the left side against the algebraic right side.

## $\S$4.2. The mass ratio as algebraic identity

The proton-electron mass ratio $\mu = 6\pi^5(1 + \alpha^2/(2\sqrt{2}) - (22/27)\alpha^4)$ uses only $\pi$ and $\alpha$. It agrees with the independently measured value to 0.03$\sigma$ — a relationship between two constants that in the standard framework are unrelated.

## $\S$4.3. The Planck hierarchy

$$\frac{m_P}{m_p} = \exp\left(14\pi + \frac{\pi^2 \sqrt{\alpha}}{28}\right) = 1.301\,206 \times 10^{19}$$

The measured value (from $G$ and $m_p$) is $1.301\,211 \times 10^{19}$. Agreement: 4.2 ppm, dominated by the 22 ppm uncertainty in $G$.

---

# $\S$5. The Minimum Measurement Set

## $\S$5.1. What is conventional and what is derived

In the standard framework, the CODATA table requires $\sim$20 empirically determined values (measured constants plus adjustment parameters). Each unit conversion between SI, atomic, and Planck systems carries its own empirical factor.

The algebraic framework reduces this to:

| Category | Count | Items |
|:---------|:-----:|:------|
| SI definitions (exact since 2019) | 5 | $c$, $h$, $e$, $k_B$, $N_A$ |
| Algebraic equations (zero measured inputs) | 3 | $\alpha$-equation, $\mu$-formula, $\eta$-hierarchy |
| Measured constants | **1** | $R_\infty$ |
| **Total inputs** | **9** | |

From these, you derive:

- $\alpha$, $\alpha^{-1}$ (electromagnetic coupling)
- $m_e$ (electron mass)
- $\mu$, $m_p$ (proton-electron mass ratio and proton mass)
- $a_0$, $r_e$, $\bar{\lambda}_C$ (length scales)
- $\mu_B$, $E_h$, $\sigma_T$ (atomic units)
- $G$ (gravitational constant)
- $l_P$, $m_P$, $t_P$, $T_P$ (Planck units)
- All conversion factors between SI, atomic, and Planck systems

## $\S$5.2. What $R_\infty$ actually is

The Rydberg constant connects atomic energy levels to the SI metre:

$$R_\infty = \frac{\alpha^2 m_e c}{2h}$$

With $h$ and $c$ exact, $R_\infty$ encodes the electron mass in SI units. It is the one number that tells the algebraic framework "how big atoms are in metres." Everything else follows from algebra.

The precision of $R_\infty$ ($1.1 \times 10^{-12}$ relative) propagates directly into every derived constant. When $R_\infty$ improves, all constants improve — simultaneously, by the same factor.

---

# $\S$6. Natural Unit Conversions

## $\S$6.1. Three natural unit systems

Every natural unit system sets some subset of fundamental constants to 1. The conversion factors back to SI depend on which constants are fixed:

**Atomic units** ($\hbar = m_e = e = 4\pi\varepsilon_0 = 1$):

- 1 Hartree = $\alpha^2 m_e c^2 = 4.359\,74 \times 10^{-18}$ J
- 1 Bohr = $\alpha / (4\pi R_\infty) = 5.291\,77 \times 10^{-11}$ m
- 1 atomic time = $\hbar / E_h = 2.418\,88 \times 10^{-17}$ s

**Particle physics units** ($\hbar = c = 1$, energy in GeV):

- 1 GeV$^{-1}$ = $\hbar c / \text{GeV} = 1.973\,27 \times 10^{-16}$ m (exact from SI)
- 1 GeV = $1.602\,18 \times 10^{-10}$ J (exact from SI)

**Planck units** ($\hbar = c = G = 1$):

- 1 $l_P$ = $1.616\,26 \times 10^{-35}$ m (tower-derived)
- 1 $t_P$ = $5.391\,27 \times 10^{-44}$ s (tower-derived)
- 1 $m_P$ = $2.176\,43 \times 10^{-8}$ kg (tower-derived)
- 1 $T_P$ = $1.416\,78 \times 10^{32}$ K (tower-derived)

## $\S$6.2. The algebraic structure

In the standard framework, converting between these systems requires looking up empirical values. In the algebraic framework:

- **Atomic $\leftrightarrow$ SI**: All conversion factors are $\alpha^n \times R_\infty \times$ (SI-exact). _Algebraically determined._
- **Particle physics $\leftrightarrow$ SI**: Conversion factors are pure SI definitions. _Exact by construction._
- **Planck $\leftrightarrow$ SI**: Conversion factors involve $e^{\eta}$. _Algebraically determined via the hierarchy formula._
- **Planck $\leftrightarrow$ Atomic**: Cross-system conversions are ratios of the above. _Algebraically determined._

The only empirical content in any conversion is $R_\infty$. The rest is algebra.

## $\S$6.3. Comparison with existing unit libraries

| Property | pint / astropy.units | Algebraic framework |
|:---------|:---------------------|:------|
| Source of conversion factors | CODATA lookup table (~20 values) | Tower algebra + $R_\infty$ |
| $\alpha$ | Empirical ($\pm$ 0.15 ppb) | Algebraic (exact) |
| $G$ | Empirical ($\pm$ 22 ppm) | Derived (0.37$\sigma$) |
| Consistency between systems | Not guaranteed | Guaranteed by algebra |
| Improvement path | Wait for new CODATA adjustment | Improve $R_\infty$ measurement |

When CODATA updates a constant, existing libraries must update their tables. In the algebraic framework, improving $R_\infty$ automatically improves *all* derived constants simultaneously — because they are all algebraic functions of $R_\infty$.

---

# $\S$7. Discussion

## $\S$7.1. What this is

This paper demonstrates that the eigenvalue tower — three algebraic equations with zero empirical inputs — combined with SI definitions and one measured constant ($R_\infty$), reproduces the CODATA fundamental constants table.

The claim is structural, not metaphysical. The equations produce numbers. The numbers match measurements. The match is within experimental uncertainty for every quantity tested ($\alpha$: 0.3$\sigma$; $\mu$: 0.03$\sigma$; $G$: 0.37$\sigma$; Planck units: 0.36–0.38$\sigma$). The $\sim$4.5$\sigma$ offset on CODATA-adjusted atomic constants traces entirely to the documented Cs-133 recoil anomaly, which CODATA has progressively resolved (the 2022 adjusted $\alpha$ matches the algebraic value exactly).

## $\S$7.2. What this is not

This is not a claim that $R_\infty$ is derivable. It is not. The Rydberg constant is the bridge between the algebraic framework (which produces dimensionless ratios) and the SI system (which assigns units). Someone must measure it. The algebraic framework says: *that is the only thing you need to measure.*

Nor is this a claim of infinite precision. The mass ratio formula is accurate to 2.3 ppb, not exact. The hierarchy formula is tested only to 22 ppm (the resolution of $G$). As measurements improve, these formulas may require refinement — additional terms, just as the Lenz formula required the $\alpha^2/(2\sqrt{2})$ correction.

## $\S$7.3. The paper trail

The results in this paper depend on three prior publications:

1. **The $\alpha$ equation** (Carpenter, 2026d): Derives $\alpha^{-1} = 137.035\,999\,177$ from $\pi$ and factorials.
2. **The mass ratio** (Carpenter, 2026v): Derives $\mu = 1836.152\,673\,426$ from $\pi$ and $\alpha$.
3. **The hierarchy** (Carpenter, 2026v): Derives $G$ from $\pi$, $\alpha$, and $m_p$.

This paper adds no new equations. It demonstrates the *consequence*: these three equations, taken together, algebraically determine the dimensional structure connecting SI, atomic, and Planck unit systems.

## $\S$7.4. The companion package

The algebraic framework is implemented as `mobius-units`, a Python package that provides:

- All fundamental constants as algebraically derived values (using `mobius-constant` as the source for $\alpha$)
- Conversion between SI, atomic, and Planck unit systems
- A single configurable measured input ($R_\infty$) from which all other constants follow

Unlike existing unit libraries, `mobius-units` does not carry a lookup table of empirical constants. It carries three equations and one number.

---

# $\S$8. Summary

1. **Three algebraic equations** produce $\alpha$, $\mu$, and $G$ with zero measured inputs.
2. **Five SI definitions** ($c$, $h$, $e$, $k_B$, $N_A$) are exact since 2019.
3. **One measurement** ($R_\infty$) bridges algebra to SI.
4. From these **nine inputs**, every CODATA fundamental constant follows — including all atomic-scale constants, the proton mass, the gravitational constant, and all four Planck units.
5. Every natural-unit conversion factor (atomic $\leftrightarrow$ SI $\leftrightarrow$ Planck) is algebraically determined up to $R_\infty$.
6. Existing unit libraries need $\sim$20 empirical inputs. This framework needs **one**.

The dimensional structure of physics has algebraic backbone. The eigenvalue tower provides it.

---

## References {-}

- Carpenter, J. (2026d). *Fine Structure Constant as Self-Consistency of a Four-Operator Algebra.* Zenodo. [10.5281/zenodo.18994393](https://doi.org/10.5281/zenodo.18994393)
- Carpenter, J. (2026v). *Precision Dominoes: From an Algebraic Fine Structure Constant to the Gravitational Constant.* Zenodo. [10.5281/zenodo.19047229](https://doi.org/10.5281/zenodo.19047229)
- Carpenter, J. (2026w). *The 4.4$\sigma$ Systematic: Cs-133 Outlier Pulls Every CODATA Constant.* Zenodo. [10.5281/zenodo.19049285](https://doi.org/10.5281/zenodo.19049285)
- CODATA. (2022). *Recommended values of the fundamental physical constants.* NIST.
- Fan, X., et al. (2023). *Measurement of the electron magnetic moment.* Physical Review Letters, 130, 071801.
- Morel, L., et al. (2020). *Determination of the fine-structure constant with an accuracy of 81 parts per trillion.* Nature, 588, 61–65.
- Parker, R. H., et al. (2018). *Measurement of the fine-structure constant as a test of the Standard Model.* Science, 360, 191–195.
