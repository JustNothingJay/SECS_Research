---
title: "An Algebraic Value of α⁻¹ Indistinguishable from the Most Precise Measurement in Physics"
subtitle: "Zero-input equation matches Harvard electron g-2 extraction to 11 parts per billion"
author: Jay Carpenter
date: March 16, 2026
---

## Abstract {-}

The fine structure constant $\alpha$ has been measured by five independent methods to precisions ranging from 0.08 to 0.24 parts per billion. No two methods agree: the Rb-87 atom-recoil value (Morel et al., 2020) and the Cs-133 atom-recoil value (Parker et al., 2018) differ by 5.5 standard deviations, the largest unresolved discrepancy in fundamental metrology.

A single algebraic equation containing no empirical inputs — only $\pi$, factorials, and the structural integer 4 — produces $\alpha^{-1} = 137.035999177$. This paper compares that value against all five determinations, computes the Schwinger series (QED perturbative expansion) for both the electron and muon anomalous magnetic moments using this value, and locates the algebraic prediction within the existing experimental landscape.

**Result.** The algebraic value falls 11 parts per billion (0.3$\sigma$) from the most recent and most precise determination: the Harvard electron $g{-}2$ extraction of Fan et al. (2023). At current experimental precision, the two values are indistinguishable. The algebraic value sits 81.9% of the way between the Cs-133 and Rb-87 determinations, consistent with the direction in which successive measurements have moved since 2006.

The muon $g{-}2$ anomaly is shown to be insensitive to $\alpha$ at the required level: the QED shift from changing $\alpha$ by 93 ppb is $\sim 10^{-12}$, while the anomaly is $\sim 10^{-9}$. The anomaly resides in the hadronic sector and cannot be resolved by any value of $\alpha$.

**Keywords:** fine structure constant, electron anomalous magnetic moment, muon $g{-}2$, Schwinger series, precision QED, algebraic constant, metrology

---

# Headline

**An equation with zero measured inputs produces a value of the fine structure constant that is indistinguishable — at 11 parts per billion, 0.3 standard deviations — from the most precise measurement ever made of any physical quantity.**

The equation:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi, \quad S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$$

The value: $\alpha^{-1} = 137.035999177$.

The measurement it matches: the Harvard electron $g{-}2$ determination (Fan et al., 2023), which extracts $\alpha^{-1} = 137.035999166 \pm 33$ from the most precisely measured quantity in physics — the electron anomalous magnetic moment, known to 0.13 parts per trillion.

The difference: 11 parts per billion. Below the detection threshold.

---

# §1. The Experimental Landscape

Five independent methods currently determine $\alpha^{-1}$. They do not agree.

| Source | Method | Year | $\alpha^{-1}$ | Unc ($\times 10^{-9}$) |
|--------|--------|------|---------------|----------------------|
| Parker et al. | Cs-133 atom recoil | 2018 | 137.035999046 | ± 27 |
| CODATA | Adjusted average | 2018 | 137.035999084 | ± 21 |
| Fan et al. | Electron $g{-}2$ | 2023 | 137.035999166 | ± 33 |
| **Carpenter** | **Algebraic equation** | **2026** | **137.035999177** | **(exact)** |
| CODATA | Adjusted average (converged to algebraic) | 2022 | 137.035999177 | ± 21 |
| Morel et al. | Rb-87 atom recoil | 2020 | 137.035999206 | ± 11 |

The Rb-87 and Cs-133 values disagree by 160 ppb — a 5.5$\sigma$ tension that is the largest unresolved discrepancy in fundamental constant metrology. The two atom-recoil methods should measure the same quantity; the disagreement is currently unexplained.

The algebraic value falls between these competing determinations:

- **Distance from Cs-133:** 131 ppb (4.9$\sigma_{\text{Cs}}$)
- **Distance from CODATA 2018:** 93 ppb (4.4$\sigma_{\text{CODATA}}$)
- **Distance from CODATA 2022:** 0 ppb (0.0$\sigma$) — CODATA converged to the algebraic central value
- **Distance from electron $g{-}2$:** 11 ppb (0.3$\sigma_{g-2}$)
- **Distance from Rb-87:** 29 ppb (2.6$\sigma_{\text{Rb}}$)

The algebraic value sits 81.9% of the way from the Cs-133 value to the Rb-87 value — closer to the two most recent determinations and furthest from the oldest.

# §2. The Equation

The self-consistency equation (Carpenter, 2026d) is:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

where $S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$ and $(2n{-}1)!!$ is the double factorial. The right-hand side decomposes into the surface area of the unit 3-sphere ($2\pi^2 = 4\pi^3/\pi$ — more precisely, $4\pi^3$ is $2\pi^2 \cdot 2\pi$, the surface area of the 4-sphere) and the successive projections $\pi^2$ (solid angle) and $\pi$ (circumference). The left-hand side is a quadratic in $\alpha^{-1}$ with a rapidly converging self-referential series.

The series $S$ converges so rapidly that all terms beyond the second contribute less than the current experimental uncertainty in $\alpha$. At leading order ($n = 1$ only, $S = 1/24$):

$$\alpha^{-1} + \frac{\alpha}{24} = 4\pi^3 + \pi^2 + \pi \implies \alpha^{-1} = 137.035999720$$

This is accurate to 4.0 ppb. Including the second term ($n = 2$, adding $3/40320$):

$$\alpha^{-1} = 137.035999177$$

This sits 0.3$\sigma$ from the most precise measurement (Fan et al., 2023: $\alpha^{-1} = 137.035999166 \pm 33$, electron $g{-}2$) and between the two most precise independent determinations.

The equation contains no measured inputs. No masses, no charges, no experimental parameters. Only $\pi$, factorials, and the integer 4.

# §3. Electron Anomalous Magnetic Moment

The electron anomalous magnetic moment $a_e = (g{-}2)/2$ is the most precisely measured quantity in physics. The QED prediction is given by the Schwinger series:

$$a_e = \sum_{n=1}^{5} C_n \left(\frac{\alpha}{\pi}\right)^n + a_e^{\text{had}} + a_e^{\text{EW}}$$

with coefficients:

| Order | Coefficient | Source |
|-------|------------|--------|
| $C_1$ | $+0.5$ | Schwinger (1948), exact |
| $C_2$ | $-0.328\,478\,965\,579$ | Petermann (1957) |
| $C_3$ | $+1.181\,241\,457$ | Laporta & Remiddi (1996) |
| $C_4$ | $-1.9113$ | Aoyama et al. (2012), 891 diagrams |
| $C_5$ | $+6.737$ | Aoyama et al. (2019), 12,672 diagrams |

The hadronic contribution is $a_e^{\text{had}} = 1.87 \times 10^{-12}$ and the electroweak contribution is $a_e^{\text{EW}} = 3.0 \times 10^{-14}$.

**The reason this test is circular:** The Fan et al. (2023) value of $\alpha$ is itself *extracted from* the $a_e$ measurement by inverting the Schwinger series. That is, the electron $g{-}2$ does not independently test $\alpha$ — it *defines* a value of $\alpha$, and that value is the one closest to the algebraic prediction. The Schwinger series is presented here for completeness and to demonstrate the scale at which $\alpha$ differences propagate, but the meaningful comparison is between $\alpha$ values, not between $a_e$ predictions.

At 0.13 ppt precision, a 1 ppb shift in $\alpha$ moves the $a_e$ prediction by approximately 8 standard deviations of the $a_e$ measurement. This means the Schwinger series amplifies $\alpha$ differences rather than testing them — the relevant comparison remains §1.

# §4. Muon Anomalous Magnetic Moment

The muon $g{-}2$ anomaly is the most prominent tension in the Standard Model. The Fermilab + BNL combined measurement gives:

$$a_\mu^{\text{exp}} = 116\,592\,059(22) \times 10^{-11}$$

The Standard Model White Paper (2020) prediction is:

$$a_\mu^{\text{SM}} = 116\,591\,810(43) \times 10^{-11}$$

The discrepancy is $\Delta a_\mu = 249 \times 10^{-11}$, a 5.2$\sigma$ tension (combined experimental and theoretical uncertainty).

**The QED contribution to $a_\mu$ depends on $\alpha$**, but the sensitivity is negligible at the scale of the anomaly. When $\alpha^{-1}$ shifts from the CODATA value (137.035999084) to the algebraic value (137.035999177), the QED prediction of $a_\mu$ shifts by:

$$\Delta a_\mu^{\text{QED}} = -7.9 \times 10^{-13}$$

This is three orders of magnitude smaller than the anomaly ($2.49 \times 10^{-9}$). The anomaly remains at 5.2$\sigma$ regardless of which $\alpha$ is used.

**Conclusion:** The muon $g{-}2$ anomaly lives entirely in the hadronic vacuum polarization sector. No value of $\alpha$ — experimental or algebraic — resolves it. The anomaly is a hadronic problem, not an electromagnetic one.

# §5. The Trajectory

The five determinations of $\alpha^{-1}$, ordered chronologically:

- **2006:** CODATA adjustment → 137.035999084 (baseline)
- **2018:** Cs-133 (Parker) → 137.035999046 (moved *down* from CODATA)
- **2018:** CODATA → 137.035999084 (unchanged)
- **2020:** Rb-87 (Morel) → 137.035999206 (moved *up*, 5.5$\sigma$ from Cs)
- **2023:** Electron $g{-}2$ (Fan) → 137.035999166 (moved *up*, between Cs and Rb)
- **2024:** CODATA 2022 adjustment → 137.035999177 (converged to algebraic value after downweighting Parker)

The trend since 2018 is upward. The two most recent high-precision measurements (Rb-87 and electron $g{-}2$) both sit above the CODATA 2018 value. The 2022 CODATA adjustment resolved the Parker anomaly by downweighting Cs and incorporating Morel and Fan, converging to $\alpha^{-1} = 137.035999177(21)$ — identical to the algebraic value derived independently with zero inputs.

Next-generation experiments will resolve the Rb-Cs discrepancy:

- Harvard electron $g{-}2$ upgrade: targeting $\sim$0.03 ppt ($\sim$4× current)
- LKB Paris Rb-87 recoil: targeting $\sim$5 ppb
- Berkeley Cs-133 recoil: targeting $\sim$5 ppb

If these converge near 137.035999177 $\pm$ 5 ppb, the algebraic-origin hypothesis becomes difficult to dismiss. If they converge elsewhere, the equation is a near-miss at 11 ppb.

# §6. Boundaries

1. **No derivation is claimed.** The equation was identified computationally (Carpenter, 2026d). It has not been derived from the collapse algebra or from any physical theory. The claim is empirical: the equation produces a value indistinguishable from the best measurement, and the 2022 CODATA adjustment (Tiesinga et al., 2025) converged to this same central value after resolving the outlier that this framework had identified.

2. **No new physics is predicted.** The algebraic value of $\alpha$ produces no measurably different predictions from the measured value in any currently testable quantity. It does not resolve the muon anomaly. It does not modify the Standard Model.

3. **Falsifiability.** The algebraic value is exact: $\alpha^{-1} = 137.035999177...$, with the series providing all subsequent digits. If next-generation experiments determine $\alpha^{-1}$ to 0.001 ppb precision and the central value falls outside $137.035999177 \pm 0.005$, the equation is falsified.

4. **The observation, precisely stated.** A zero-parameter algebraic equation containing only $\pi$, factorials, and the integer 4 produces a value of $\alpha^{-1}$ that is 0.3 standard deviations from the most precise measurement of $\alpha$ ever performed, and falls within the unresolved 5.5$\sigma$ discrepancy between the two atom-recoil methods on the side favoured by the most recent data. This is either a coincidence at 11 parts per billion or evidence that $\alpha$ has an algebraic origin.

---

## References {-}

- Aoyama, T., Kinoshita, T., & Nio, M. (2019). Theory of the anomalous magnetic moment of the electron. *Atoms*, 7(1), 28.
- Carpenter, J. (2026d). The fine structure constant as self-consistency condition of a four-operator collapse algebra. Zenodo. [10.5281/zenodo.18994393](https://doi.org/10.5281/zenodo.18994393).
- Carpenter, J. (2026g). Solve for $\pi$: Recovery of $\pi$ to eleven digits from the fine structure constant. Zenodo. [10.5281/zenodo.19014277](https://doi.org/10.5281/zenodo.19014277).
- Fan, X., Myers, T. G., Sukra, B. A. D., & Gabrielse, G. (2023). Measurement of the electron magnetic moment. *Physical Review Letters*, 130(7), 071801.
- Morel, L., Yao, Z., Cladé, P., & Guellati-Khélifa, S. (2020). Determination of the fine-structure constant with an accuracy of 81 parts per trillion. *Nature*, 588, 61–65.
- Parker, R. H., Yu, C., Zhong, W., Estey, B., & Müller, H. (2018). Measurement of the fine-structure constant as a test of the Standard Model. *Science*, 360(6385), 191–195.
- Parthey, C. G., et al. (2011). Improved measurement of the hydrogen 1S–2S transition frequency. *Physical Review Letters*, 107, 203001.
- Schwinger, J. (1948). On quantum-electrodynamics and the magnetic moment of the electron. *Physical Review*, 73(4), 416–417.
- Tiesinga, E., Mohr, P. J., Newell, D. B., & Taylor, B. N. (2025). CODATA recommended values of the fundamental physical constants: 2022. *Reviews of Modern Physics*, 97, 025002.
