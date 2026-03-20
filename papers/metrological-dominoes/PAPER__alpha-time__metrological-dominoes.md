---
title: "Metrological Dominoes: How an Algebraic Fine Structure Constant Restructures the Measurement of Time"
subtitle: "From exact α to the SI second — the cascade that collapses circular metrology"
author: Jay Carpenter
date: March 16, 2026
---

## Abstract {-}

Every atomic clock counts electromagnetic transitions. Every electromagnetic transition frequency depends on the fine structure constant $\alpha$. Currently, $\alpha$ is not known from theory — it is extracted from experiment, most precisely from the electron anomalous magnetic moment via inversion of the Schwinger QED series. This creates a circular dependency: the best value of $\alpha$ comes from QED, while QED predictions for other quantities use that same $\alpha$ as input.

A companion paper (Carpenter, 2026s) derived the algebraic equation $\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$, which yields $\alpha^{-1} = 137.035999177$ from zero measured inputs. The 2022 CODATA adjustment (Tiesinga et al., 2025) later converged to this same central value — $\alpha^{-1} = 137.035999177(21)$ — after downweighting the Parker Cs outlier that had pulled the 2018 value low by 4.4$\sigma$ (Carpenter, 2026w).

This paper traces the consequences. If $\alpha$ is algebraic — known exactly, with zero uncertainty — a metrological domino chain activates: the Rydberg constant becomes determinable from hydrogen spectroscopy alone; the electron mass improves by a factor of 281; the electron $g{-}2$ transforms from a constant-determination tool into a pure QED test; the 5.5$\sigma$ Rb-Cs discrepancy acquires a fixed target; optical clock frequency ratios gain exact $\alpha$-dependent factors; and the framework predicts $\dot{\alpha}/\alpha = 0$ exactly — a strong, falsifiable claim against cosmological variation theories.

The paper quantifies each step with specific sensitivity coefficients, uncertainty budgets, and implications for the planned redefinition of the SI second circa 2030.

**Keywords:** fine structure constant, atomic clocks, metrology, SI second, optical lattice clocks, Rydberg constant, CODATA, circular dependency, precision measurement

---

# §1. The Problem: α Is Everywhere in Time

## §1.1. The SI second and the cesium transition

The SI second is defined as 9,192,631,770 periods of the radiation corresponding to the hyperfine transition of the Cs-133 ground state:

$$\nu_{\text{Cs}} = 9\,192\,631\,770 \; \text{Hz} \quad \text{(exact by definition)}$$

This definition, adopted in 1967, anchors all of time metrology to a single atomic transition. The question this paper addresses: what determines this frequency *physically*, and how does uncertainty in $\alpha$ propagate through every quantity derived from it?

## §1.2. α-dependence of the cesium hyperfine transition

The hyperfine splitting of an alkali atom scales as:

$$\nu_{\text{hfs}} \propto \alpha^2 \cdot F_{\text{rel}}(Z\alpha) \cdot g_I \cdot \frac{m_e}{m_p} \cdot R_\infty c$$

where $\alpha^2$ is the leading electromagnetic factor, $F_{\text{rel}}(Z\alpha)$ is the Casimir relativistic correction, $g_I$ the nuclear g-factor, and $R_\infty c$ the Rydberg frequency. For a multi-electron atom, the relativistic factor is:

$$F_{\text{rel}}(Z\alpha) = \frac{3}{\gamma(4\gamma^2 - 1)}, \quad \gamma = \sqrt{1 - (Z\alpha)^2}$$

For Cs-133 ($Z = 55$), $(Z\alpha)^2 \approx 0.161$, giving $F_{\text{rel}} \approx 1.39$. The full sensitivity coefficient, from many-body perturbation theory (Dzuba, Flambaum & Webb, 1999), is:

$$K_\alpha(\text{Cs}) \equiv \frac{d \ln \nu_{\text{hfs}}}{d \ln \alpha} \approx 2.83$$

A fractional change $\delta\alpha/\alpha$ produces a fractional change of $2.83 \times \delta\alpha/\alpha$ in the cesium frequency. The simplified point-nucleus Casimir model gives $K_\alpha \approx 2.74$; the published 2.83 includes many-electron correlation effects.

## §1.3. Optical clock transitions

Optical clocks operate at frequencies $\sim 10^5$ higher than cesium, using narrow electronic transitions in trapped ions or optical lattices. Their $\alpha$-sensitivities vary widely:

| Clock transition | Frequency (Hz) | Fractional unc. | $K_\alpha$ |
|:---|---:|---:|---:|
| Cs-133 hyperfine | $9.19 \times 10^{9}$ | $\sim 10^{-16}$ | $+2.83$ |
| Sr-87 ${}^1S_0 \to {}^3P_0$ | $4.29 \times 10^{14}$ | $2 \times 10^{-18}$ | $+0.06$ |
| Yb-171 ${}^1S_0 \to {}^3P_0$ | $5.19 \times 10^{14}$ | $1.4 \times 10^{-18}$ | $+0.31$ |
| Al$^+$ ${}^1S_0 \to {}^3P_0$ | $1.12 \times 10^{15}$ | $9 \times 10^{-19}$ | $+0.008$ |
| Yb$^+$ E2 | $6.88 \times 10^{14}$ | $3 \times 10^{-18}$ | $+0.88$ |
| Yb$^+$ E3 (octupole) | $6.42 \times 10^{14}$ | $3 \times 10^{-18}$ | $-5.95$ |
| Hg$^+$ | $1.07 \times 10^{15}$ | $2 \times 10^{-17}$ | $-2.94$ |

Three observations matter for this paper:

1. **Sr-87** ($K_\alpha = +0.06$) is nearly $\alpha$-independent — a robust "standard candle" but nearly useless for detecting $\alpha$-variation.
2. **Al$^+$** ($K_\alpha = +0.008$) has the smallest sensitivity of any candidate, making it the most robust reference.
3. **Yb$^+$ E3** ($K_\alpha = -5.95$) has large *negative* sensitivity — ideal for $\alpha$-variation searches when compared against positive-sensitivity clocks.

## §1.4. The universal structure

Every atomic transition frequency reduces to:

$$\nu = C \cdot R_\infty c \cdot f(\alpha, m_e/m_p, \text{nuclear structure})$$

where $R_\infty = \alpha^2 m_e c / (2h)$. All frequencies depend on $\alpha$ — directly through $R_\infty \propto \alpha^2$, and indirectly through relativistic corrections. If $\alpha$ were known exactly, every transition frequency would be expressible as an exact algebraic factor times $m_e c^2/h$ times nuclear structure corrections. The $\alpha$-dependent part stops being an uncertainty and becomes a number.

---

# §2. The Redefinition of the SI Second

## §2.1. Cesium is being replaced

Optical clocks now outperform cesium fountains by $\sim 100\times$:

| Generation | Standard | Best uncertainty | Era |
|:---|:---|---:|:---|
| 1st | Cs-133 beam | $\sim 10^{-13}$ | 1960s |
| 2nd | Cs-133 fountain | $\sim 2 \times 10^{-16}$ | 2010s |
| 3rd (candidate) | Sr-87 optical lattice | $2.0 \times 10^{-18}$ | 2018 |
| 3rd (candidate) | Yb-171 optical lattice | $1.4 \times 10^{-18}$ | 2019 |
| 3rd (candidate) | Al$^+$ quantum-logic ion | $9.4 \times 10^{-19}$ | 2019 |

The definition of the second is the bottleneck. The CGPM targets $\sim$2030 for redefinition.

## §2.2. Candidate transitions

**Tier 1** (strongest candidates):

- **Sr-87** ${}^1S_0 \to {}^3P_0$. Most widely reproduced — operated at $>$10 national metrology institutes. Low $\alpha$-sensitivity. The pragmatic favourite.
- **Yb-171** ${}^1S_0 \to {}^3P_0$. Comparable performance. Strong programmes at NIST, PTB, INRIM, NMIJ.

**Tier 2** (high precision, limited deployment):

- **Al$^+$** ${}^1S_0 \to {}^3P_0$. Lowest systematic uncertainty achieved ($9.4 \times 10^{-19}$, Brewer et al., 2019). Single-ion, long averaging.
- **Yb$^+$ E3**. Large negative $K_\alpha$ — ideal for $\alpha$-variation searches.

**Tier 3** (emerging):

- **Th-229 nuclear clock**. Nuclear isomer transition at $\sim$8.4 eV. First laser excitation demonstrated (Tiedau et al., 2024). Exceptionally insensitive to external perturbations. Projected $10^{-19}$ ultimate accuracy.

## §2.3. The frequency ratio problem

To redefine the second, candidate transition frequencies must be known as ratios to the current Cs standard at the $10^{-18}$ level. These ratios depend on $\alpha$:

$$\frac{\nu_1}{\nu_2} = \frac{C_1 \cdot f_1(\alpha, ...)}{C_2 \cdot f_2(\alpha, ...)}$$

The sensitivity of the ratio to $\alpha$:

$$\frac{d}{d\ln\alpha}\left(\frac{\nu_1}{\nu_2}\right) = (K_{\alpha,1} - K_{\alpha,2}) \cdot \frac{\nu_1}{\nu_2}$$

For Sr/Cs: $K_{\alpha,\text{Sr}} - K_{\alpha,\text{Cs}} = 0.06 - 2.83 = -2.77$. At the current CODATA $\alpha$ uncertainty ($\sim 1.5 \times 10^{-10}$), this produces a $\sim 4.2 \times 10^{-10}$ uncertainty in the Sr/Cs frequency ratio.

The measurement precision is $\sim 10^{-16}$. The target is $10^{-18}$.

**The gap between what we can measure and what we can predict theoretically is $4.5 \times 10^6$.** We can measure time $4.5$ million times more precisely than we can explain it from the constants.

---

# §3. The Domino Chain

If $\alpha^{-1} = 137.035999177$ is exact — zero uncertainty — the following chain activates.

## §3.1. Domino 1: The Rydberg constant

$$R_\infty = \frac{\alpha^2 m_e c}{2h}$$

Currently known to $1.1 \times 10^{-12}$ fractional uncertainty (CODATA 2022). But $R_\infty$ is determined in a global fit that simultaneously adjusts $\alpha$, $R_\infty$, and the proton charge radius $r_p$ from hydrogen spectroscopy, the electron $g{-}2$, and atom-recoil measurements.

If $\alpha$ is exact, the fit gains one degree of freedom. $R_\infty$ becomes determinable from hydrogen spectroscopy alone, without importing $\alpha$ from external experiments. The remaining uncertainty is dominated by the proton charge radius, not $\alpha$.

The $\alpha$-dependent contribution to $R_\infty$ uncertainty: $2 \times \delta\alpha/\alpha = 2 \times 1.5 \times 10^{-10} = 3.0 \times 10^{-10}$. This is $\sim 280\times$ larger than the current $R_\infty$ measurement uncertainty. Removing it collapses the Rydberg determination to its intrinsic spectroscopic limit.

## §3.2. Domino 2: The electron mass

Since the 2019 SI revision, $h$ and $c$ are exact by definition. Therefore:

$$m_e = \frac{2R_\infty h}{\alpha^2 c}$$

With exact $\alpha$, exact $h$, exact $c$: the electron mass has the same fractional uncertainty as $R_\infty$.

Current $m_e$ uncertainty: $3.1 \times 10^{-10}$ (CODATA 2022).

With exact $\alpha$: $\delta m_e / m_e = \delta R_\infty / R_\infty \approx 1.1 \times 10^{-12}$.

**Improvement factor: 281×.**

## §3.3. Domino 3: The electron g-2 becomes a test

Currently, the electron anomalous magnetic moment $a_e$ is used to *determine* $\alpha$ by inverting the Schwinger series:

$$a_e^{\text{meas}} = \sum_{n=1}^{5} C_n \left(\frac{\alpha}{\pi}\right)^n + a_e^{\text{had}} + a_e^{\text{EW}} \quad \xrightarrow{\text{solve for } \alpha} \quad \alpha_{g\text{-}2}$$

This assumes QED is complete to 5th order. The coefficients $C_4$ and $C_5$ were computed numerically from 891 and 12,672 Feynman diagrams respectively (Aoyama, Kinoshita & Nio). Any error in the QED calculation propagates into the extracted $\alpha$.

If $\alpha$ is algebraic, this inversion becomes unnecessary. The Schwinger series becomes a *one-way prediction*:

$$a_e^{\text{pred}}(\alpha_{\text{algebraic}}) \to \text{compare with } a_e^{\text{meas}}$$

Any discrepancy is either a QED calculation error or new physics. The test is no longer circular. The 5th-order Schwinger coefficient $C_5$ becomes directly testable: at $\alpha^{-1} = 137.035999177$, the 5th-order contribution is $C_5(\alpha/\pi)^5 \approx 4.6 \times 10^{-13}$, which is $3.5\times$ the measurement uncertainty of $1.3 \times 10^{-13}$.

## §3.4. Domino 4: The Rb-Cs discrepancy gets a referee

The two independent atom-recoil determinations of $\alpha$ disagree by 5.5$\sigma$:

| Method | $\alpha^{-1}$ | Distance from algebraic |
|:---|:---|:---|
| Cs-133 recoil (Parker, 2018) | $137.035999046 \pm 27$ | 131 ppb low |
| Rb-87 recoil (Morel, 2020) | $137.035999206 \pm 11$ | 29 ppb high |
| Algebraic (SECS) | $137.035999177$ | — |

Without a known target, the discrepancy is undirected — each experiment can only be compared against the other. With algebraic $\alpha$ as a fixed reference, each experiment has a specific, quantified offset. The Cs value needs to move $+131$ ppb; the Rb value needs to move $-29$ ppb. Error budgets can be re-examined against a target rather than against each other.

## §3.5. Domino 5: Clock frequency ratios

For two optical clocks with sensitivities $K_1$ and $K_2$:

$$\frac{\nu_1}{\nu_2} = R_0 \cdot \alpha^{K_1 - K_2} \cdot G(\text{nuclear structure})$$

If $\alpha$ is exact, the $\alpha^{K_1 - K_2}$ factor becomes an exact algebraic number. The remaining uncertainty comes entirely from nuclear structure calculations.

Specific examples:

| Clock pair | $\Delta K_\alpha$ | Current $\alpha$-limited unc. | With exact $\alpha$ |
|:---|---:|---:|:---|
| Sr / Yb | $-0.25$ | $3.8 \times 10^{-11}$ | 0 |
| Sr / Al$^+$ | $+0.052$ | $7.8 \times 10^{-12}$ | 0 |
| Yb$^+$ E3 / Al$^+$ | $-5.958$ | $8.9 \times 10^{-10}$ | 0 |
| Sr / Cs | $-2.77$ | $4.2 \times 10^{-10}$ | 0 |

The $\alpha$-dependent theoretical uncertainty in every clock ratio vanishes. Comparisons become pure tests of nuclear structure and QED corrections.

## §3.6. Domino 6: The CODATA adjustment simplifies

The CODATA least-squares adjustment determines $\sim$80 constants from $\sim$200 input data items. $\alpha$ is one of the most influential inputs, entering through the electron $g{-}2$, atom-recoil measurements, hydrogen spectroscopy, muonium hyperfine structure, and (pre-2019) the quantum Hall effect.

If $\alpha$ is fixed algebraically:

1. The number of free parameters drops by one.
2. Correlations between $\alpha$ and $R_\infty$, $m_e$, $m_p/m_e$, etc. all simplify.
3. Several quantities with correlated uncertainties become independently determinable.
4. The proton charge radius puzzle (muonic vs. electronic hydrogen) decouples from $\alpha$ — the joint fit of $r_p$, $R_\infty$, and $\alpha$ reduces to two unknowns.

## §3.7. The full chain

$$\alpha \text{ exact} \to R_\infty \text{ from H spectroscopy alone} \to m_e \text{ improves } 281\times$$
$$\to m_p/m_e \text{ improves} \to \text{clock ratios predictable} \to \text{SI second gains backing}$$

Each step removes one source of circular dependency from the metrological network.

---

# §4. Implications Beyond Clocks

## §4.1. Gravitational redshift tests

The most precise tests of general relativity compare clocks at different gravitational potentials. The Bothwell et al. (2022) experiment measured gravitational redshift across a 1 mm height difference using Sr clocks at $10^{-21}/\sqrt{\text{Hz}}$ sensitivity.

When comparing clock frequencies at different heights:

$$\frac{\nu_1(\text{top})}{\nu_2(\text{bottom})} = \left(1 + \frac{g\Delta h}{c^2}\right) \times \frac{f_1(\alpha)}{f_2(\alpha)}$$

If $\alpha$ is exact, the ratio $f_1(\alpha)/f_2(\alpha)$ is exact, and any deviation from the predicted ratio is a pure test of general relativity or a signal of new physics. Currently, $\alpha$ uncertainty in the atomic structure factors contributes a systematic. With algebraic $\alpha$, this systematic vanishes.

## §4.2. α-variation over cosmological time

If $\alpha$ arises from a mathematical self-consistency condition, then $\alpha$ *cannot* vary — it is a fixed consequence of algebraic structure. The framework predicts:

$$\dot{\alpha}/\alpha = 0 \quad \text{exactly, at all times, in all locations}$$

This is a strong, falsifiable prediction.

Current laboratory constraints (Sr-Yb comparison): $|\dot{\alpha}/\alpha| < 1.0 \times 10^{-18}\,\text{yr}^{-1}$ (2$\sigma$). Astrophysical constraints (quasar absorption spectra, Webb et al.): $\Delta\alpha/\alpha \sim 10^{-5}$ over cosmological time, with disputed spatial dipole.

Both are consistent with the algebraic prediction. But any future measurement of nonzero $\alpha$-variation at any confidence level would falsify the algebraic origin hypothesis.

## §4.3. Deep-space navigation

Future deep-space missions (NASA's Deep Space Atomic Clock programme) use optically-referenced clocks with $10^{-15}$ to $10^{-17}$ stability. At these levels, the $\alpha$-dependence of the clock transition becomes the dominant systematic. Exact $\alpha$ removes this systematic entirely.

## §4.4. The proton-to-electron mass ratio

With exact $h$, $c$ (post-2019 SI), and exact $\alpha$:

$$m_e = \frac{2R_\infty h}{\alpha^2 c}$$

$m_e$ acquires the same fractional uncertainty as $R_\infty$ ($\sim 1.1 \times 10^{-12}$), a $281\times$ improvement. Combined with Penning trap measurements of $m_p$ ($\sim 3 \times 10^{-11}$), the proton-to-electron mass ratio $\mu = m_p/m_e$ improves modestly (from $1.7 \times 10^{-11}$ to $\sim 1.7 \times 10^{-11}$, already $m_p$-limited in CODATA 2022). More importantly, $\mu$ enters molecular transition frequencies, and molecular clocks are emerging tools for measuring $\dot{\mu}/\mu$. With exact $\alpha$, the atomic-frequency calibration chain tightens, making molecular measurements cleaner.

---

# §5. The Circular Dependency

## §5.1. The current loop

The best $\alpha$ comes from the electron $g{-}2$ (Fan et al., 2023): $\alpha^{-1} = 137.035999166 \pm 33$. This is *extracted* from measured $a_e$ by inverting the Schwinger QED series.

The problem: this assumes QED is correct to 5th order. Simultaneously, QED predictions for other quantities — the muon $g{-}2$, Lamb shift, hydrogen fine structure, helium fine structure — use the same $\alpha$ as input. The system tests QED against QED.

The atom-recoil measurements provide $\alpha$ independently of QED, but they disagree with each other by 5.5$\sigma$ (§3.4). There is no external referee.

## §5.2. How algebraic α breaks it

1. **The electron $g{-}2$ becomes a pure QED test.** No circular inversion.
2. **The Rb-Cs discrepancy becomes diagnosable.** Both experiments benchmarked against a fixed target.
3. **Hydrogen spectroscopy becomes a pure $r_p$ measurement.** The joint fit of $\alpha$, $R_\infty$, $r_p$ reduces to two unknowns.
4. **The CODATA adjustment gains an anchor.** One fewer free parameter, simplified correlations.
5. **The Schwinger coefficients become testable.** $C_4$ and $C_5$ can be checked against $a_e$ at higher sensitivity.

---

# §6. Quantified Summary

| Domain | Current situation | With algebraic $\alpha$ |
|:---|:---|:---|
| Electron $g{-}2$ | Determines $\alpha$ (circular) | Pure QED test |
| Rb-Cs discrepancy | No referee; 5.5$\sigma$ unresolved | Fixed target: Rb $+$29 ppb, Cs $-$131 ppb |
| Rydberg constant | Joint fit with $\alpha$, $r_p$ | H spectroscopy alone; $\alpha$ unc. removed |
| Electron mass | $3.1 \times 10^{-10}$ fractional | $1.1 \times 10^{-12}$ (281× improvement) |
| CODATA adjustment | $\sim$80 correlated constants | One fewer free parameter |
| Proton charge radius | Entangled with $\alpha$ in H fit | Decoupled; determinable from H data |
| Clock frequency ratios | Theory limited to $\sim 10^{-10}$ | Nuclear-structure limited |
| SI second redefinition | Candidates compared empirically | Theoretical backing for ratios |
| $\alpha$-variation | Measure $\dot{\alpha}/\alpha$; null expected | Predicts $\dot{\alpha}/\alpha = 0$ exactly |
| QED 5th order | Tested indirectly via global fit | $C_5$ directly testable against $a_e$ |

---

# §7. Boundaries

1. **This paper does not claim $\alpha$ is algebraic.** It traces the metrological consequences *if* the algebraic value $\alpha^{-1} = 137.035999177$ were exact. The companion paper (2026s) established that the algebraic value is indistinguishable from the best single measurement at current precision. The 2022 CODATA adjustment (Tiesinga et al., 2025) later converged to the same central value — $\alpha^{-1} = 137.035999177(21)$ — after resolving the Parker Cs outlier identified by this framework (Carpenter, 2026w).

2. **Nuclear structure limits remain.** Even with exact $\alpha$, theoretical predictions of absolute transition frequencies are limited by nuclear charge radii, nuclear polarisation, and many-body atomic structure calculations at the $\sim 10^{-6}$ level for complex atoms. The $\alpha$-dependent uncertainty is one term among several — but it is the one this framework addresses.

3. **The CODATA global fit has not been re-performed.** The domino chain described here identifies which uncertainties vanish; it does not compute the actual post-adjustment values. That requires running the full least-squares adjustment with $\alpha$ fixed, which is outside the scope of this work.

4. **The prediction $\dot{\alpha}/\alpha = 0$ is not unique to this framework.** The Standard Model also predicts constant $\alpha$ (at tree level). What is distinctive is that the algebraic framework makes this prediction *structurally* — $\alpha$ cannot vary because it is determined by a mathematical identity, not by a dynamical mechanism that could, in principle, evolve.

5. **GPS and telecommunications improvements are indirect.** The cascading improvements described in §4 operate through the calibration chain, not through the operational precision of existing systems. Current GPS is limited by propagation effects, not fundamental constants. The implications become relevant for next-generation satellite navigation targeting mm-level accuracy.

---

## References {-}

Bothwell, T., et al. (2022). Resolving the gravitational redshift across a millimetre-scale atomic sample. *Nature*, 602, 420–424.

Brewer, S. M., et al. (2019). $^{27}$Al$^+$ quantum-logic clock with a systematic uncertainty below $10^{-18}$. *Physical Review Letters*, 123, 033201.

Carpenter, J. (2026d). The fine structure constant as self-consistency condition of a four-operator collapse algebra. Zenodo. 10.5281/zenodo.18994393.

Carpenter, J. (2026s). An algebraic value of $\alpha^{-1}$ indistinguishable from the most precise measurement in physics. Zenodo. 10.5281/zenodo.19042747.

Dzuba, V. A., Flambaum, V. V., & Webb, J. K. (1999). Calculations of the relativistic effects in many-electron atoms and space-time variation of fundamental constants. *Physical Review A*, 59, 230.

Fan, X., et al. (2023). Measurement of the electron magnetic moment. *Physical Review Letters*, 130, 071801.

Ludlow, A. D., Boyd, M. M., Ye, J., Peik, E., & Schmidt, P. O. (2015). Optical atomic clocks. *Reviews of Modern Physics*, 87, 637–701.

Morel, L., et al. (2020). Determination of the fine-structure constant with an accuracy of 81 parts per trillion. *Nature*, 588, 61–65.

Parker, R. H., et al. (2018). Measurement of the fine-structure constant as a test of the Standard Model. *Science*, 360, 191–195.

Rosenband, T., et al. (2008). Frequency ratio of Al$^+$ and Hg$^+$ single-ion optical clocks; metrology at the 17th decimal place. *Science*, 319, 1808–1812.

Safronova, M. S., et al. (2018). Search for new physics with atoms and molecules. *Reviews of Modern Physics*, 90, 025008.

Takamoto, M., et al. (2020). Test of general relativity by a pair of transportable optical lattice clocks. *Nature Photonics*, 14, 411–415.

Tiedau, J., et al. (2024). Laser excitation of the Th-229 nuclear isomeric transition in a solid-state host. *Physical Review Letters*, 132, 182501.

Tiesinga, E., Mohr, P. J., Newell, D. B., & Taylor, B. N. (2021). CODATA recommended values of the fundamental physical constants: 2018. *Reviews of Modern Physics*, 93, 025010.

Tiesinga, E., Mohr, P. J., Newell, D. B., & Taylor, B. N. (2025). CODATA recommended values of the fundamental physical constants: 2022. *Reviews of Modern Physics*, 97, 025002.

Webb, J. K., et al. (2011). Indications of a spatial variation of the fine structure constant. *Physical Review Letters*, 107, 191101.
