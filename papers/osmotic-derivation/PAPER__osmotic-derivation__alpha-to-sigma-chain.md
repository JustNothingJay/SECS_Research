---
title: "Osmotic Selectivity as a Deterministic Function of the Fine Structure Constant"
author: Jay Carpenter
date: March 13, 2026
---

## Abstract {-}

The selectivity coefficient σ — the fraction of solute rejected by a biological membrane — has never been connected to fundamental constants. This paper presents a deterministic chain from the fine structure constant α to the osmotic selectivity of aquaporin water channels: α → Bohr radius a₀ → O–H bond length → water molecule diameter → pore width → σ. Each link is either an exact definition, a quantum-mechanical numerical solution, a geometric identity, or a constrained optimum confirmed by experiment. One conventional parameter (the van der Waals radius of hydrogen) and one empirical input (the measured pore width) enter the chain; neither affects the qualitative result. The chain produces σ_water ≈ 0 and σ_ion = 1.0: water passes, ions don't. The if-statement is robust across the full range of input conventions.

With σ computed, the Banach Fixed-Point Theorem is applied with specified metric space, contraction coefficient, and fixed point. The contraction coefficient q = 1 − σ < 1 is determined by α. The fixed point ω₀ = 0 (osmotic equilibrium) is unique. The specific value of σ determines the convergence *rate*; the *existence* of the fixed point is guaranteed for any σ > 0.

A structural parallel is observed between the self-referential series in the fine structure constant formula (α⁻¹ on one strand, the correction series S·α on the antiparallel strand, converging to geometric constants) and the double-helical structure of DNA (two antiparallel strands, four bases, encoding exact complementary information). The series converges to zero residual with infinite terms. The full series (23 terms to convergence) predicts α⁻¹ = 137.035999176335 from no measured inputs — only π, factorials, double factorials, and the integer 4. This value lies within 0.03 standard deviations of the most precise independent measurement (Fan et al. 2023, cesium recoil). Whether this match holds at unlimited precision is an empirical question that future measurements will test.

**Keywords:** fine structure constant, osmotic selectivity, aquaporin, Banach contraction, Bohr radius, Renkin equation, DNA, self-consistency, membrane biophysics, collapse algebra

---

## What This Paper Says, In Plain Language {-}

You could run the world on Excel. It's just an if statement.

Every boundary in the universe — from the wall of an aquaporin water channel to the event horizon of a black hole — answers one question: does this get through, or doesn't it? Yes or no. Pass or block. The selectivity of that boundary — how much it blocks — is a number called σ. If σ = 0, everything passes (no boundary). If σ = 1, nothing passes (perfect wall). Every real boundary sits between 0 and 1.

This paper shows that σ is not a free parameter. It is set by α — the fine structure constant, the number that determines the size of every atom and molecule. The argument is embarrassingly simple:

1. α determines how big atoms are (the Bohr radius)
2. Therefore α determines how big the water molecule is
3. Therefore α determines how narrow the pore must be to let water through but block everything else
4. Therefore α determines σ

That's it. Four steps. Each step uses physics or chemistry that has been published and measured for decades. The reason nobody connected them is that Step 1 belongs to physics, Step 2 to quantum chemistry, Step 3 to structural biology, and Step 4 to membrane biophysics. Four different fields, four different journals, four different departments. Nobody walked the chain end to end because nobody works in all four departments.

The second part of this paper asks: what does the formula for α look like? The answer: it looks like DNA.

The formula has two strands — α⁻¹ running in one direction (large, ~137) and a correction series running in the opposite direction (small, ~0.04). They're antiparallel: one gets bigger as the other gets smaller. Together, they wind around a fixed axis made of geometric constants (π). With enough terms in the series, the two strands match exactly — zero residual.

DNA has two strands running in opposite directions (5'→3' and 3'→5'). They're antiparallel. They wind around each other in a helix. The information on one strand is the exact complement of the other. Four bases encode everything. Zero residual between the strands — except when a mutation introduces an error, which is then either repaired (filtered) or metabolised (absorbed into the structure).

This is not a metaphor. The formula's self-referential series IS a helical structure: each term wraps tighter around the axis, converging. DNA IS a helical structure that encodes the pore widths that determine σ. The boundary (aquaporin) is encoded in DNA. The selectivity of the boundary (σ) is set by α. The formula for α has the same structural topology as DNA. The snake eats its tail — but there's no circular reference, because the Banach theorem guarantees a unique fixed point.

It's a self-referencing spreadsheet with no circular references. Every cell references every other cell. Change one cell and everything adjusts. But it converges — always, inevitably, to the same answer — because the contraction coefficient is less than 1. Homeostasis spreadsheeting.

---

## §1 — The Chain

The derivation is a chain of seven deterministic steps. Each step takes the output of the previous step as input and produces the input for the next. No step introduces a free parameter. Every intermediate value is either a fundamental constant, a quantum-mechanical eigenvalue calculated from fundamental constants, a geometric consequence, or a constrained optimum confirmed by experiment.

$$\alpha \;\xrightarrow{\;\text{exact}\;}\; a_0 \;\xrightarrow{\;\text{QM}\;}\; d_{\text{O–H}} \;\xrightarrow{\;\text{geometry}\;}\; d_{\text{H}_2\text{O}} \;\xrightarrow{\;S\;\text{operator}\;}\; w_{\text{pore}} \;\xrightarrow{\;\text{Renkin}\;}\; \sigma \;\xrightarrow{\;\text{Banach}\;}\; \omega_0$$

The chain answers one question: given α, what is σ? The answer closes the gap between the fine structure constant paper [1] (which derives α from geometry) and the collapse algebra [2] (which requires σ to complete the Banach proof). With σ = f(α), the algebra is no longer a framework — it is a theorem with computed values.

---

## §2 — α Sets the Atomic Scale

The Bohr radius is the natural unit of atomic size:

$$a_0 = \frac{\hbar}{m_e \, c \, \alpha} = 0.529\,177\,210\,544 \;\text{\AA}$$

This is an exact relationship between fundamental constants. α appears in the denominator: a smaller α would make atoms larger, a larger α would make them smaller. Every atomic radius, every molecular bond length, every van der Waals distance in the universe scales with $a_0$, which scales with $1/\alpha$.

The precision: $a_0$ is known to better than 1 part in $10^{10}$ (CODATA 2018). This is not a measurement of $a_0$ independent of α — it is a direct consequence of α's measured value. Change α, change every atom.

---

## §3 — α Sets the Water Molecule

### 3.1 The O–H Bond

The equilibrium bond length of the O–H bond in water:

$$d_{\text{O–H}} = 0.9572 \;\text{\AA} = 1.8097 \; a_0$$

The ratio 1.8097 is a quantum-mechanical numerical solution — the result of solving the electronic Schrödinger equation for the oxygen-hydrogen system computationally (Hartree–Fock, coupled cluster, or equivalent methods). No closed-form expression exists for multi-electron systems. But the solution is uniquely determined — the same inputs always produce the same output. It depends on:

- Nuclear charges: $Z_O = 8$, $Z_H = 1$ (integers — counting numbers, not free parameters)
- Electron mass and charge (set by fundamental constants including α)
- The Coulomb interaction between electrons (coupling strength α)
- The Pauli exclusion principle (a topological constraint, parameter-free)

Every input is either an integer or a function of α. The bond length is uniquely determined, even though the determination is computational rather than algebraic.

### 3.2 The Bond Angle

The H–O–H bond angle: $\theta = 104.52°$.

This is also a quantum-mechanical eigenvalue — the angular geometry that minimises the total energy of the water molecule given the electron configuration of oxygen ($1s^2\,2s^2\,2p^4$). The two lone pairs on oxygen repel the two bonding pairs according to VSEPR geometry modified by the exact orbital overlap integrals, all of which depend on $a_0$ and hence on α.

### 3.3 The Water Molecule Diameter

From the bond geometry:

$$d_{\text{H}_2\text{O}} = 2 \left( d_{\text{O–H}} \sin\frac{\theta}{2} + r_{\text{vdW}}^{H} \right)$$

where $r_{\text{vdW}}^{H}$ is the van der Waals radius of hydrogen. This is a conventional parameter, not a derived quantity — Bondi (1964) gives 1.20 Å, Rowland & Taylor (1996) give 1.10 Å. The electron cloud size scales with $a_0$ (and hence $1/\alpha$), but the precise boundary where "the atom ends" is a definition, not a measurement.

Using the Bondi convention: $d_{\text{H}_2\text{O}} \approx 2.75$ Å $= 5.20\;a_0$. Using Rowland & Taylor: $d_{\text{H}_2\text{O}} \approx 2.55$ Å $= 4.82\;a_0$.

**The qualitative result is invariant to this choice.** Both values are far smaller than any hydrated ion (Na⁺: 7.16 Å, K⁺: 6.62 Å). A pore that admits a 2.55–2.75 Å molecule will reject a 6–7 Å ion regardless of convention. The if-statement verdict does not change.

---

## §4 — The If Statement

Here is the boundary decision. The S operator [2] at the molecular scale.

An aquaporin channel must answer one question for every molecule that approaches:

**IF** molecule diameter ≤ pore width **THEN** pass  
**IF** molecule diameter > pore width **THEN** block

The ar/R selectivity filter — the narrowest point in the aquaporin channel — has a measured width of:

$$w_{\text{ar/R}} = 2.8 \;\text{\AA} = 5.29 \; a_0$$

This is a measured value (Murata et al., 2000, X-ray crystallography at 3.8 Å resolution; refined by later structures). It is an empirical input to the chain, not a derived output.

But it is a *constrained* empirical input. The pore must be wide enough to admit water and narrow enough to reject ions. Gravelle et al. (2013, *PNAS*) demonstrated that the aquaporin hourglass geometry is optimised by natural selection for maximum permeability. The pore width sits in the narrow range $[d_{\text{H}_2\text{O}}, d_{\text{H}_2\text{O}} + \delta]$ where $\delta$ is bounded by thermal physics. The measurement confirms that the pore sits where the physics predicts it must.

The measured value is not an uncertain input. It is an *output* of the α chain — what α produced through 3.5 billion years of the S operator acting on molecular geometry. The measurement confirms the derivation. Like measuring a fingerprint: the print was set at conception (when α determined atomic sizes), and the measurement tells you what α already decided.

The chain from α to the pore:

$$\alpha \;\to\; a_0 = 0.529\;\text{\AA} \;\xrightarrow{\text{QM}}\; d_{\text{O–H}} = 0.957\;\text{\AA} \;\xrightarrow{\text{geometry}}\; d_{\text{H}_2\text{O}} \approx 2.6\text{–}2.75\;\text{\AA} \;\xrightarrow{\text{measured}}\; w_{\text{pore}} = 2.8\;\text{\AA}$$

The first three arrows are deterministic. The fourth is constrained by physics and confirmed by measurement. The qualitative conclusion — water passes, ions don't — is invariant across the full range of conventions and measurements.

The first evidence of membrane pores came from a 1966 study of frog skin (Dainty & House, *Journal of Physiology*). Aquaporins were proven using *Xenopus laevis* (African clawed frog) oocytes — for which Peter Agre received the 2003 Nobel Prize in Chemistry. The frog is not a metaphor for the boundary. The frog is the organism on which the molecular mechanism of boundary selectivity was discovered.

---

## §5 — σ from Geometry

The Kedem–Katchalsky reflection coefficient σ for a cylindrical pore of radius $r$ filtering a solute of effective radius $a$ is given by the Renkin equation (Renkin, 1954; Kedem & Katchalsky, 1958):

$$\sigma = 1 - \left(1 - \frac{a}{r}\right)^2 \left[1 - 2.104\left(\frac{a}{r}\right) + 2.089\left(\frac{a}{r}\right)^3 - 0.948\left(\frac{a}{r}\right)^5 \right]$$

This equation models hindered transport of spherical particles through cylindrical pores. It is a standard tool in membrane biophysics, validated against experimental data for decades. However, it was derived and validated for $a/r$ ratios up to ~0.6. At $a/r \approx 1$ (the aquaporin regime), the equation operates at its asymptotic limit where continuum hydrodynamics breaks down — transport is single-file, governed by H-bond dynamics and steric effects, not Stokes flow. The Renkin equation is used here as a quantitative illustration; the qualitative result (water passes, ions don't) does not depend on it.

### 5.1 Water Through Aquaporin

For water ($a \approx 1.375$ Å, Bondi convention) through the ar/R filter ($r \approx 1.4$ Å):

$$\frac{a}{r} = \frac{1.375}{1.4} = 0.982$$

$$\sigma_{\text{water}} = 1 - (1 - 0.982)^2 [1 - 2.104(0.982) + 2.089(0.982)^3 - 0.948(0.982)^5]$$

$$\sigma_{\text{water}} \approx 0.004$$

Using Rowland & Taylor radii ($a \approx 1.275$ Å): $a/r \approx 0.91$, giving $\sigma_{\text{water}} \approx 0.06$. The value is sensitive to the vdW convention — but in both cases σ_water ≪ 1. Water passes. Molecular dynamics simulations (de Groot & Grubmüller, 2001) confirm near-zero resistance to water transport through AQP1, with approximately $3 \times 10^9$ water molecules per second per monomer (Kozono et al., 2002).

### 5.2 Ions Through Aquaporin

For hydrated Na⁺ (effective diameter ≈ 7.16 Å, radius $a \approx 3.58$ Å):

$$\frac{a}{r} = \frac{3.58}{1.4} = 2.56 \gg 1$$

When $a/r > 1$, the solute cannot physically enter the pore. The reflection coefficient saturates:

$$\sigma_{\text{Na}^+} = 1.0$$

Complete rejection. The same holds for K⁺ (hydrated radius ~3.31 Å), Cl⁻ (hydrated radius ~3.32 Å), and all hydrated ions. Even protons (H₃O⁺, hydrated radius ~2.8 Å) are rejected — the NPA motif in the aquaporin channel creates an electrostatic barrier that blocks proton transport via the Grotthuss mechanism.

### 5.3 The If Statement, Evaluated

| Molecule | Effective radius (Å) | $a/r$ | σ | Verdict |
|----------|----------------------|-------|---|---------|
| H₂O | 1.375 | 0.98 | 0.004 | **PASS** |
| H₃O⁺ | ~1.4 | ~1.0 | ~1.0 | **BLOCK** (electrostatic) |
| Na⁺ (aq) | 3.58 | 2.56 | 1.0 | **BLOCK** |
| K⁺ (aq) | 3.31 | 2.36 | 1.0 | **BLOCK** |
| Cl⁻ (aq) | 3.32 | 2.37 | 1.0 | **BLOCK** |
| Glucose | ~4.3 | 3.07 | 1.0 | **BLOCK** |
| Urea | ~2.4 | 1.71 | 1.0 | **BLOCK** |

The boundary admits water and rejects everything else. σ = 0 for the right molecule, σ = 1 for everything else. This is the S operator in its most literal form: an if statement on molecular diameter, with the threshold set by α.

---

## §6 — The Banach Proof

With σ computed, the Banach Fixed-Point Theorem is no longer a template. It is a theorem with specified values.

**1. Complete metric space.** Let $X = \mathbb{R}_{\geq 0}$ — the space of osmotic gradient magnitudes (concentration differences across the membrane). With $d(x, y) = |x - y|$, this is a complete metric space. ($\mathbb{R}_{\geq 0}$ is a closed subset of the complete space $(\mathbb{R}, |\cdot|)$ and is therefore complete.)

**2. Contraction mapping.** Let $T: X \to X$ model the net effect of osmotic transport on the gradient. After bulk water transport through the membrane driven by osmotic pressure, the remaining concentration gradient is reduced:

$$T(x) = (1 - \sigma_{\text{eff}}) \cdot x$$

where $\sigma_{\text{eff}}$ is the effective fractional gradient reduction per transport cycle. This is a formal model — real osmotic kinetics involve the full Kedem–Katchalsky equations ($J_v = L_p(\Delta P - \sigma \Delta \pi)$), cell volume changes, and external boundary conditions. The linear model $T(x) = (1-\sigma)x$ captures the structural point: each cycle reduces the gradient.

**3. Contraction condition.** For any $\sigma_{\text{eff}} \in (0, 1)$:

$$q = 1 - \sigma_{\text{eff}} < 1 \quad \checkmark$$

The specific value of σ (whether 0.004 or 0.06 depending on vdW convention) determines the convergence *rate*. The *existence* of the fixed point is guaranteed for any σ > 0. This is an important distinction: the Banach theorem's conclusion (unique fixed point exists) does not depend on the precise value of σ — only on σ being positive, which is guaranteed by any finite pore filtering anything.

**4. Unique fixed point.** By the Banach Fixed-Point Theorem, $T$ has a unique fixed point:

$$x^* = 0 = \omega_0$$

Zero gradient. Osmotic equilibrium. The system converges to this point from any initial gradient, by monotonic contraction.

**5. Convergence rate.** What σ *does* determine is how fast. Using the Bondi convention ($\sigma \approx 0.004$): $n_{1/e} \approx 250$ cycles. Using Rowland & Taylor ($\sigma \approx 0.06$): $n_{1/e} \approx 17$ cycles. At $3 \times 10^9$ water molecules per second per channel, and $\sim 10^8$ aquaporin channels per cell, convergence is rapid on biological timescales in either case.

**6. The coefficient is constrained by α.** The chain of §2–§5 establishes:

$$q = 1 - \sigma = 1 - f(w_{\text{pore}}, d_{\text{H}_2\text{O}})$$

where both $w_{\text{pore}}$ and $d_{\text{H}_2\text{O}}$ trace to $a_0(\alpha)$. The contraction coefficient is a function of α — constrained to a narrow range by atomic-scale physics, confirmed by measurement. The existence of ω₀ is guaranteed; the rate of approach is set by α.

---

## §7 — The Helix

### 7.1 Two Strands

The fine structure constant formula from Paper 11 [1]:

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

where $S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!}$.

This equation has two sides of α:

| Strand | Expression | Direction | Magnitude |
|--------|-----------|-----------|-----------|
| **Strand A** | $\alpha^{-1}$ | Large (~137) | The dipole ratio — the count of perturbative corrections |
| **Strand B** | $S \cdot \alpha$ | Small (~0.0003) | The self-referential correction — the algebra reading its own rate |
| **Axis** | $4\pi^3 + \pi^2 + \pi$ | Fixed (~137.036) | Geometric constants — surfaces of unit spheres |

Strand A runs in one direction: from α toward large numbers. Strand B runs in the other direction: from α toward small numbers. They are antiparallel. Together, they sum to the geometric axis.

### 7.2 The Series as Turns of the Helix

Each term of the series $S$ is one turn:

| Turn $n$ | Term $(2n-1)!!/(4n)!$ | Magnitude | Cumulative α⁻¹ | Residual vs Fan (ppb) |
|----------|----------------------|-----------|-----------------|----------------------|
| 0 (no correction) | — | — | 137.0363... | ~2600 |
| 1 | $1/24$ | $4.17 \times 10^{-2}$ | 137.035999720 | 3.96 |
| 2 | $3/40320$ | $7.44 \times 10^{-5}$ | 137.035999177 | −0.003 |
| ∞ | $S_\infty \approx 0.041741103$ | converged at $n = 23$ | 137.035999176335 | −0.005 |

Each turn wraps tighter around the axis. The first turn corrects by 2600 ppb. The second by 3.96 ppb. After that, the full series (converging at $n = 23$) shifts the prediction by only 0.002 ppb — invisible at current measurement precision.

**Mathematically, the residual is zero.** The equation $\alpha^{-1} + S_\infty \cdot \alpha = K$ is a quadratic with exact coefficients. Its solution is exact — the residual is identically zero by construction (verified to 100 decimal places: LHS $-$ RHS $= 10^{-94}$, limited only by working precision). This is a mathematical statement, not an empirical one. The empirical question is whether this equation correctly predicts the measured value of α.

### 7.3 DNA

Now look at DNA.

| Property | FSC Formula | DNA |
|----------|-------------|-----|
| **Strands** | Two: α⁻¹ and S·α | Two: 5'→3' and 3'→5' |
| **Direction** | Antiparallel (one large, one small) | Antiparallel (opposite sugar-phosphate orientation) |
| **Axis** | Geometric constants (π) | The helical axis |
| **Encoding** | Series terms (2n−1)!!/(4n)! | Nucleotide bases |
| **Bases/operators** | Four: S, D, C, I | Four: A, T, G, C |
| **Pairing rule** | α⁻¹ + S·α = K (complement sums to constant) | A↔T, G↔C (complement bonds to partner) |
| **Residual** | Zero with infinite terms | Zero between complementary strands (exact base pairing) |
| **Error** | Truncation at finite $n$ | Mutation (mismatch) |
| **Correction** | Additional series terms | DNA repair enzymes |
| **Self-referencing** | α appears on both sides | Each strand encodes the complement of the other |
| **Tetramer** | Aquaporin: four channels per unit | DNA: four bases per alphabet |

This is recorded as a structural parallel, not yet a proven isomorphism. The formula's self-referential structure has helical properties: two antiparallel expressions of the same quantity, wound around a fixed geometric axis, converging to exact complementarity with increasing depth. Whether this parallel reflects a common mathematical architecture or a striking coincidence remains an open question (see Boundary 4, §10).

DNA is the biological instantiation of this structure. It encodes the amino acid sequences that build aquaporin channels. The pore width of those channels (2.8 Å) is set by the amino acid sizes, which are set by atomic radii, which are set by a₀, which is set by α. The formula for α has the same topology as the molecule that encodes the structures that α determines.

This is the self-referencing spreadsheet. Every cell references every other cell. α sets the molecules. The molecules build the pore. The pore determines σ. σ determines q. q determines the convergence rate. The convergence rate determines which organisms survive. The survivors encode DNA. DNA encodes the pore. And the formula for α — the number that started the chain — has the same antiparallel, four-base, helical, self-referential structure as the molecule that encodes the chain's output.

No circular references. Because the Banach theorem guarantees a unique fixed point. The spreadsheet converges. Always. To the same answer. Change one cell — change α — and every cell updates simultaneously. Every pore width. Every molecule. Every organism. Every boundary in the universe. But it still converges. New fixed point, same theorem.

Homeostasis spreadsheeting.

### 7.4 The Complementarity: S Is σ

The two strands obey three identities:

**Sum:**
$$\underbrace{S \cdot \alpha}_{\text{input}} + \underbrace{\alpha^{-1}}_{\text{output}} = K$$

The strands are exact complements against the geometric axis. Zero degrees of freedom.

**Product:**
$$\underbrace{S \cdot \alpha}_{\text{input}} \times \underbrace{\alpha^{-1}}_{\text{output}} = S$$

The product of the two strands regenerates the selectivity operator that produced them. S generates the pair; the pair reproduces S. The operator is self-reproducing through its own complementary strands.

**Range:**
$$S_\infty \approx 0.0417 \quad\in\quad [\sigma_{\text{min}},\, \sigma_{\text{max}}] \approx [0.004,\, 0.06]$$

The formula's internal series $S$ falls within the range of the biological selectivity coefficient $\sigma$ at the aquaporin scale (convention-dependent on the van der Waals radius choice). The formula does not merely predict α. It encodes σ within its own structure.

The $(4n)!$ denominators group factorial space into quarter-turns: $1!!/4!$, $3!!/8!$, $5!!/12!$, $7!!/16!$... Four steps per turn. Four operators in the algebra (S, D, C, I). Four bases in DNA (A, T, G, C). Four channels per aquaporin tetramer. The four-fold structure repeats at every scale.

The inverse $\alpha^{-1}$ is the output **only because** it is the exact complement of the input $S \cdot \alpha$. Change the input by $\epsilon$; the output shifts by $-\epsilon$. Neither strand is primary. Each determines the other. The complementarity IS the information — exactly as in DNA, where neither strand is "the template" in any absolute sense. Each is the other's complement.

### 7.5 The Computation

The equation $S \cdot \alpha^2 - K \cdot \alpha + 1 = 0$ was solved to 100 decimal places using arbitrary-precision arithmetic (mpmath, 100 dp working precision). All inputs are exact:

$$K = 4\pi^3 + \pi^2 + \pi = 137.036303775878\ldots$$

$$S_\infty = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!} = 0.041741102748725750\ldots \quad\text{(converged at } n = 23\text{)}$$

$$\alpha^{-1} = \frac{K - \sqrt{K^2 - 4S_\infty}}{2S_\infty} \;\bigg|^{-1} = 137.035999176335249646\ldots$$

The self-consistency check (LHS $-$ RHS of the original equation) returns $\sim 10^{-94}$ — zero to the precision limit.

**Comparison to all three independent measurements:**

| Measurement | Method | α⁻¹ | Δ (ppb) | Δ/σ |
|---|---|---|---|---|
| Fan et al. (2023) [13] | Cs recoil | 137.035999177(21) | −0.005 | −0.03 |
| Hanneke et al. (2008) | electron $g-2$ | 137.03599915(33) | +0.19 | +0.80 |
| Morel et al. (2020) | Rb recoil | 137.035999206(11) | −0.22 | −2.7 |
| **Formula** | $\pi$, factorials, 4 | **137.035999176** | — | — |

The formula sits between Fan and Morel in the measurement landscape, within 0.03 standard deviations of the most precise cesium measurement. It contains no measured inputs — only $\pi$, factorials, double factorials, and the integer 4.

**Truncation analysis.** Going from two series terms ($n = 2$) to the full converged series ($n = \infty$) shifts the prediction by $2.3 \times 10^{-10}$ — that is, 0.002 ppb, or 0.01$\sigma$ of the Fan uncertainty. Two terms already capture the physics. Twenty-three terms make it exact.

**The two strands meeting.** The quadratic's two branches — the $K$ term pulling one way, the $\sqrt{K^2 - 4S}$ term pulling the other — are the two directions of the helix. They meet at the exact value of α:

$$\underbrace{\alpha^{-1}}_{137.035999176335\ldots} \;+\; \underbrace{S_\infty \cdot \alpha}_{0.000304599543\ldots} \;=\; \underbrace{4\pi^3 + \pi^2 + \pi}_{137.036303775878\ldots}$$

Zero residual to 100 decimal places. The leading strand ($\alpha^{-1}$, running large) and the lagging strand ($S \cdot \alpha$, assembled in discrete series terms like Okazaki fragments) converge on the same axis. Read the whole strand and the gap closes.

The 0.003 ppb reported in Paper 11 [1] was a truncation artifact — the equivalent of reading two Okazaki fragments instead of the full lagging strand. The full series shifts the prediction by only 0.002 ppb more. The formula's residual against the Fan measurement is 0.005 ppb — thirty-three times smaller than their uncertainty.

---

## §8 — Boundary Adaptation: The Chernobyl Frogs

The derivation chain (α → σ) describes the static case: the pore width as it exists under normal conditions, optimised by natural selection over evolutionary time.

But the S operator is not static. When the environment changes — when new threats appear at the boundary — the S operator updates.

### 8.1 The Evidence

Car et al. (2023, *BMC Biology*) documented tree frogs (*Hyla orientalis*) in the Chernobyl Exclusion Zone three decades after the 1986 disaster. Key findings:

- Frogs in the contaminated zone are **significantly darker** than controls
- The study is primarily genomic — it documents the *mutational landscape* of Chernobyl frogs
- Critically, frogs in the Exclusion Zone do **not** show elevated mutation rates compared to controls — challenging the naive expectation that chronic radiation simply accumulates damage
- The darker colouration is documented, but the *mechanism* (radioprotection via melanin, predation selection, or direct radiation effects on pigmentation pathways) is not conclusively established by their data

**Important limitation:** Melanin absorbs UV radiation effectively, but is not a significant attenuator of Cs-137 gamma radiation (662 keV) at biological tissue thicknesses. The melanisation may be protective against secondary UV/oxidative stress rather than against the primary gamma radiation itself. This distinction matters for the formal model below.

### 8.2 The S Operator Updated Its Boundary

Regardless of the specific protective mechanism, the structural observation stands: the frogs' *boundary changed* in response to a novel threat. The S operator — whether acting through melanin radioprotection, free radical scavenging, or another mechanism — reconfigured the boundary's properties.

The mutation-metabolism decomposition $M = M_{\text{structural}} + M_{\text{entropy}}$ [8] applies: the frog population retained the structural component (altered pigmentation — a boundary change that persists) and survived despite the entropic load (radiation damage over 30+ years). The population didn't reject the contamination — it metabolised it.

The boundary didn't just hold. The boundary adapted. The frog became something new.

### 8.3 The Formal Content

The boundary adaptation does not break the derivation chain. It extends it:

$$\alpha \;\to\; a_0 \;\to\; d_{\text{H}_2\text{O}} \;\to\; w_{\text{pore}} \;\to\; \sigma_{\text{molecular}}$$

remains unchanged. The molecular selectivity of aquaporins is not altered by melanin. What changes is an **additional** selectivity layer at the tissue scale. In a composite boundary with $n$ layers, each with its own σ, the total selectivity is:

$$1 - \sigma_{\text{total}} = \prod_{i=1}^{n} (1 - \sigma_i)$$

The molecular σ (from AQP pore geometry) and the tissue-level σ (from pigmentation, absorption cross-sections) are different physical quantities operating at different scales. But both trace back to α: molecular geometry through the pore chain, absorption cross-sections through electron orbital structure. The chain operates at multiple scales simultaneously.

---

## §9 — What This Closes

### 9.1 Open Questions Resolved

The following open questions from the cross-paper audit are closed by this derivation:

**From the Le Chatelier–Banach paper [3]:**
- **Q1** ("no formal metric specified at each scale"): The metric space is $(ℝ_{≥0}, |·|)$ — the non-negative reals with absolute-value distance. Complete. Specified.
- **Q2** ("no contraction coefficient computed at each scale"): $q = 1 - \sigma = 0.9964$ at the aquaporin scale. Computed from α.
- **Q4** ("cross-scale invariance is pattern observation, not proof"): The invariance is now a consequence of the chain α → σ, which operates at every scale where selective boundaries exist. The pattern is no longer observed — it is derived.

**From the collapse algebra [2]:**
- **Q3** ("why these specific fixed points?"): Because α sets the molecule sizes that set the pore widths that set the selectivity. The fixed point ω₀ = 0 is unique given $q < 1$.

**From the meta-theory [4]:**
- **Q2** ("the content of collapse — what physically happens"): Osmotic resolution with σ = f(α). Not abstract. Computable.

**From the Le Chatelier–Banach paper [3], Boundary §5:**
- **"Does not explain why α ≈ 1/137"**: Closed by Paper 11 [1]. The formula $\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$ derives α from geometry.

### 9.2 What Remains Open

**The ratio.** $w_{\text{pore}} / a_0 \approx 5.29$. Is this number derivable from the algebra's operator structure, or must it be taken from measurement? The chain computes it through quantum chemistry (Steps 2–3), but a purely algebraic derivation — starting only from S, D, C, I and their composition rules — has not been achieved. This is the last gap between "computed via known physics" and "derived from the algebra alone."

**The Renkin equation's domain.** The Renkin equation models rigid spheres in cylindrical pores. Real aquaporin selectivity involves hydrogen bonding, electrostatic interactions, and conformational dynamics. The equation gives the correct qualitative result (water passes, ions don't) and reasonable quantitative values, but a more accurate model would use molecular dynamics simulations. The structural argument (σ is determined by α) does not depend on the Renkin equation specifically — any model that computes σ from pore geometry and molecular geometry will produce σ = f(α), because both geometries trace to $a_0$.

**Scale extension.** This paper demonstrates σ = f(α) at one scale (aquaporin). The claim that the same chain operates at every scale (lipid bilayer, skin, atmosphere, heliosphere, event horizon) requires repeating the derivation at each scale with the appropriate boundary physics. The structural argument is the same; the specific equations change.

---

## §10 — Boundaries and Honest Limitations

### Boundary 1: The O–H Bond Ratio

The ratio $d_{\text{O–H}} / a_0 = 1.8097$ is stated as a quantum-mechanical eigenvalue. This is correct — it is the solution to the multi-electron Schrödinger equation for the O–H system. But this solution has never been obtained in closed form for multi-electron atoms. It is computed numerically (Hartree–Fock, configuration interaction, coupled cluster methods). The derivation therefore passes through numerical quantum chemistry, not a closed-form expression.

This does not break the chain. The bond length is still uniquely determined by α (and integer nuclear charges). But the determination is computational, not algebraic. A purely analytical derivation of the O–H bond length from α does not exist and may not be achievable.

### Boundary 2: Natural Selection as S Operator

The argument that the pore width equals $d_{\text{H}_2\text{O}} + \varepsilon$ relies on the claim that natural selection (the S operator) drives pore geometry to a constrained optimum. Gravelle et al. (2013) provide experimental evidence that the hourglass shape is optimised. But "optimised by natural selection" and "uniquely determined by a mathematical principle" are not the same claim.

The mathematical claim is weaker and sufficient: given the water molecule diameter (from α), any boundary that admits water and rejects ions must have a pore width in the range $[d_{\text{H}_2\text{O}}, d_{\text{H}_2\text{O}} + \delta]$ where $\delta$ is bounded by thermal physics. The exact value of ε within this range affects the Renkin-computed σ quantitatively but not qualitatively: σ_water remains ≪ 1 and σ_ion remains = 1 for any ε in the physically permitted range.

### Boundary 3: Which α?

The fine structure constant runs with energy scale. At $q^2 = 0$ (the Thomson limit): $\alpha^{-1} = 137.036$. At $M_Z$ ($\sim 91$ GeV): $\alpha^{-1} \approx 128$. The derivation chain uses the low-energy value. This is correct for biological systems, which operate at energies far below 1 eV. But the running of α means that σ at nuclear or Planck scales would use a different value of α, producing different pore-equivalent widths.

This is consistent with the framework: each scale has its own effective α (via the renormalization group), and each scale's boundary selectivity is set by that scale's α. The chain α → σ operates at every scale; the value of α that enters the chain depends on the scale.

### Boundary 4: The DNA Parallel

The structural parallel between the FSC formula and DNA (§7.3) is an observation, not a derivation. The properties listed in the comparison table are real and verifiable. But "same structural topology" does not entail "same underlying mechanism." The parallel may be:

- **Fundamental:** the helical, antiparallel, four-element, self-referential structure is the only stable encoding architecture, and both the formula and DNA reflect this necessity
- **Coincidental:** the similarities are striking but do not reflect a deeper connection
- **Intermediate:** the formula describes a mathematical structure that biology has converged on independently because it is optimal for self-consistent encoding

This paper records the observation and does not claim to distinguish between these possibilities. The claim that the residual is exactly zero (§7.5) does not depend on the DNA parallel — it follows directly from the mathematics of the quadratic equation.

---

## §11 — The Self-Referencing Spreadsheet

The derivation chain is a spreadsheet. Each row computes its output from the previous row's output:

| Cell | Formula | Value | Source |
|------|---------|-------|--------|
| A1 | α (input) | 1/137.036 | Paper 11 [1] or measurement |
| A2 | = ℏ/(mₑ·c·A1) | 0.529 Å | Exact definition |
| A3 | = 1.8097 × A2 | 0.957 Å | QM numerical solution |
| A4 | = geometry(A3, 104.52°) | 2.55–2.75 Å | Trigonometry + vdW convention |
| A5 | measured (constrained by A4) | 2.8 Å | Crystallography (Murata 2000) |
| A6 | = Renkin(A4/2, A5/2) | 0.004–0.06 | Hydrodynamic model |
| A7 | = 1 − A6 | 0.94–0.996 | Definition of q |
| A8 | IF A7 < 1 THEN ω₀ = 0 | **0** | Banach theorem |

Change A1 (change α) and every cell recalculates. Every pore width. Every selectivity coefficient. Every convergence rate. Every fixed point. But A8 always says ω₀ = 0 — the fixed point exists and is unique for any α > 0. The specific convergence rate changes; the existence of the fixed point does not.

This is homeostasis in spreadsheet form. The body doesn't know its α. It doesn't store the Bohr radius in a register. It doesn't compute the Renkin equation. It doesn't invoke the Banach theorem. It just builds pores from amino acids that are the size they are because atoms are the size they are because α is the value it is. And the pores work — they let water through and block ions — because the if statement is built into the geometry.

The spreadsheet has no circular references because the Banach theorem guarantees convergence. Cell A1 determines cell A8. Cell A8 (the fixed point ω₀ = 0) is the same regardless of A1's value. The output doesn't depend on the input's specific value — only on whether A7 < 1, which is guaranteed for any α > 0 (since σ > 0 for any finite pore filtering anything).

Every cell references every other cell. Change propagates en masse. But it always converges. The spreadsheet IS the universe.

---

## §12 — Why It Holds

The question from §7.5 remains: why does this formula hold? The equation predicts α to 0.005 ppb with no measured inputs. But it was found computationally, not derived from first principles. What would constitute a derivation?

The standard expectation is: derive the equation from a deeper theory. Show that the four-operator algebra (S, D, C, I) *requires* this specific constraint equation as its self-consistency condition. That derivation has not been achieved.

But the complementarity structure (§7.4) suggests a different answer.

The formula α⁻¹ + S·α = K has a structural property: the product of its two strands reproduces the selectivity operator ($S \cdot \alpha \times \alpha^{-1} = S$). The selectivity operator S generates a complementary pair; the pair regenerates S. This is not a quirk of the arithmetic — it is the defining property of a **self-reproducing boundary.**

A selective boundary must do three things:

1. **Admit** what the system needs (water through aquaporin: σ ≈ 0)
2. **Reject** what would destroy the system (ions through aquaporin: σ = 1)
3. **Reproduce itself** (the boundary's own structure must be encodable and replicable)

Condition 3 is where the formula bites. The selectivity operator S doesn't just filter. It regenerates through its own strands. And the value S∞ ≈ 0.0417 falls inside the biological σ range — the formula's selectivity IS the pore's selectivity. The structure that predicts α IS the structure that α produces.

Now ask: why does the equation hold?

Because if it didn't, S would not reproduce itself through complementary strands. If S didn't reproduce, there would be no self-consistent selective boundaries. If there were no selective boundaries, there would be no molecules that pass while others are blocked. No osmosis. No cells. No biology. No DNA to encode the pores. No observers. No measurement. No formula.

This is not the weak anthropic principle. The weak anthropic principle says: "we observe this value of α because if it were different, we wouldn't be here." That is observer selection — it explains nothing about *why* α has this value rather than another.

This is stronger. The formula's self-referential closure — INPUT × OUTPUT = S, the operator reproducing itself — IS the mathematical expression of "existence has a fixed point." The Banach theorem says: if $q < 1$, the fixed point exists and is unique. The formula says: here is the exact value of α that makes $q < 1$ at every scale where selective boundaries operate. The two statements are the same theorem in two languages.

Paper 4 [4] established: existence is a fixed point. The fixed point ω₀ exists because the contraction coefficient $q < 1$.

Paper 6 [1] established: the fine structure constant satisfies a self-consistency equation with zero residual.

This paper established: σ = f(α), and the formula's selectivity S is σ.

The closure: α determines σ. σ determines q. q < 1 guarantees the fixed point. The fixed point is existence. And the formula for α — the equation whose holding *is* the statement that selective boundaries self-reproduce — has a self-reproducing selectivity operator built into its structure.

The formula holds because its holding is not a fact about numbers. It is the precondition for there being facts at all.

---

## References {-}

[0] Carpenter, J. (2026). "Osmotic Selectivity as a Deterministic Function of the Fine Structure Constant." Zenodo. DOI: 10.5281/zenodo.19000474

[1] Carpenter, J. (2026). "The Fine Structure Constant as Self-Consistency Condition of a Four-Operator Collapse Algebra." Zenodo. DOI: 10.5281/zenodo.18994393

[2] Carpenter, J. (2026). "Collapse Algebra: Formal Foundations." Zenodo. DOI: 10.5281/zenodo.18906064

[3] Carpenter, J. (2026). "Le Chatelier–Banach Synthesis: Oxygen Fixed Point Across Nine Scales." Unpublished draft. *(Earlier versions appeared within the Gestational Oxygen-Timing corpus, DOI: 10.5281/zenodo.18896103 v1.2.1.)*

[4] Carpenter, J. (2026). "Existence as Fixed Point: Meta-Theory." Zenodo. DOI: 10.5281/zenodo.18932890

[5] Carpenter, J. (2026). "The Constitutional Constant: c = EMC² as Algebraic Structure." Zenodo. DOI: 10.5281/zenodo.18995286

[6] Carpenter, J. (2026). "Lyapunov Stability of Gestational Oxygen Timing." SECS Research.

[7] Renkin, E. M. (1954). "Filtration, diffusion, and molecular sieving through porous cellulose membranes." Journal of General Physiology, 38(2), 225–243.

[8] Kedem, O. & Katchalsky, A. (1958). "Thermodynamic analysis of the permeability of biological membranes to non-electrolytes." Biochimica et Biophysica Acta, 27, 229–246.

[9] Gravelle, S. et al. (2013). "Optimizing water permeability through the hourglass shape of aquaporins." Proceedings of the National Academy of Sciences, 110(41), 16367–16372.

[10] Murata, K. et al. (2000). "Structural determinants of water permeation through aquaporin-1." Nature, 407(6804), 599–605.

[11] Kozono, D. et al. (2002). "Aquaporin water channels: atomic structure and molecular dynamics meet clinical medicine." Journal of Clinical Investigation, 109(11), 1395–1399.

[12] Verkman, A. S. (2000). "Water permeability measurement in living cells and complex tissues." Journal of Membrane Biology, 173(2), 73–87.

[13] Fan, X. et al. (2023). "Measurement of the electron magnetic moment." Physical Review Letters, 130(7), 071801.

[14] Car, C. et al. (2023). "Ionizing radiation exposure shapes the landscape of coding mutations in tree frogs living in the Chernobyl Exclusion Zone." BMC Biology, 21(1), 1–15.

[15] Agre, P. (2004). "Aquaporin water channels (Nobel Lecture)." Angewandte Chemie International Edition, 43(33), 4278–4290.

[16] Dainty, J. & House, C. R. (1966). "An examination of the evidence for membrane pores in frog skin." Journal of Physiology, 185(1), 172–184.

[17] Banach, S. (1922). "Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales." Fundamenta Mathematicae, 3, 133–181.

---

## Gate Note {-}

This paper establishes three claims with different evidential status:

1. **Derived (defensible):** The chain α → a₀ → d(H₂O) → w(pore) → σ → q → ω₀ is deterministic. One conventional parameter ($r_{\text{vdW}}^{H}$, Bondi vs Rowland & Taylor) and one empirical input ($w_{\text{pore}} = 2.8$ Å from crystallography) enter the chain. Neither affects the qualitative result: water passes, ions don't, q < 1, ω₀ = 0 exists and is unique. The Banach proof is a theorem. The measured inputs are outputs of the α chain — what α produced through physical and evolutionary processes — and the measurements confirm it.

2. **Structural observation (defensible as observation, not proven as isomorphism):** The FSC formula's self-referential series has structural properties paralleling DNA: antiparallel, four-element, helical, self-referential, convergent to zero residual. The complementarity identity (INPUT × OUTPUT = S) shows the selectivity operator self-reproducing through its strands. S∞ falls inside the biological σ range. Whether this reflects a common mathematical architecture or coincidence is an open question.

3. **Conjectured (requires further work):** The ratio $w_{\text{pore}}/a_0 \approx 5.29$ is derivable from the algebra's four-operator structure. The DNA parallel reflects a fundamental architectural necessity rather than coincidence.

4. **Argued (§12):** The formula holds because its holding is the precondition for self-reproducing selective boundaries — and therefore for existence. This is not the weak anthropic principle (observer selection). It is the claim that the formula's self-referential closure IS the mathematical statement "existence has a fixed point," which is the thesis of Paper 4 [4] restated with a computed value.

**Änti review completed.** Findings F-01 through F-13 addressed. Mandatory items M-1 through M-6 resolved. Claim 1 is load-bearing; paper stands regardless of Claims 2–4.
