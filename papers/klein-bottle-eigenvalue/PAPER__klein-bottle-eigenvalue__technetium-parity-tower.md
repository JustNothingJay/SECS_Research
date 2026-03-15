---
title: "The Klein Bottle Eigenvalue: Technetium, Parity Violation, and the Tower Inside $\\alpha$"
author: Jay Carpenter
date: March 15, 2026
---

## Abstract {-}

The fine structure constant identity $\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi$ factors as $\pi(4\pi^2 + \pi + 1)$. The inner polynomial $4\pi^2 + \pi + 1 \approx 43.620$ serves as the right-hand side of a second-level equation with the same structure: $\beta^{-1} + S\beta = 4\pi^2 + \pi + 1$, yielding $\beta^{-1} = 43.619\,053$. Dividing again by $\pi$ produces a third level: $\gamma^{-1} + S\gamma = 4\pi + 1 + 1/\pi$, yielding $\gamma^{-1} = 13.882$.

The identity contains a tower. Each level is the previous level divided by $\pi$, exactly. The eigenvalue ratios are not exactly $\pi$ --- they differ by the overshoot constant $\mathcal{O} = S/\text{RHS}^2$, which grows by a factor of $\pi^2$ at each level.

The floor of the Level 1 eigenvalue is 43 --- the atomic number of technetium, the lightest element with no stable isotopes. Technetium's instability is entirely weak-force mediated: every isotope decays by $\beta^{\pm}$ or electron capture. The weak force is the only fundamental interaction that violates parity. Parity violation is the physical signature of non-orientability. The Level 1 surface --- the Klein bottle, formed by closing the Möbius strip's boundary --- is non-orientable and requires embedding in four dimensions.

The chain is: Möbius (half-twist, Level 0) $\to$ electromagnetic coupling $\to$ $\alpha$. Klein bottle (non-orientable closure, Level 1) $\to$ weak-force shadow $\to$ $\beta^{-1} \approx 43.6$. The tower was always inside the polynomial. The periodic table was always inside $\alpha$.

**Keywords:** fine structure constant, Klein bottle, technetium, parity violation, weak force, eigenvalue tower, non-orientable topology, Möbius strip, beta decay, self-consistency

**DOI:** 10.5281/zenodo.19021507

---

## What This Paper Says, In Plain Language {-}

The formula for the fine structure constant --- the number $1/137$ that sets the size of every atom --- has a hidden structure. Its right-hand side, $4\pi^3 + \pi^2 + \pi$, is not a single number. It factors into $\pi$ times a smaller expression: $4\pi^2 + \pi + 1 \approx 43.6$.

You can feed that smaller expression back into the same formula and solve again. You get a new number: $43.619...$

That number is 43 and a fraction. Element 43 is technetium --- the only element below bismuth with no stable isotopes. Every technetium atom ever made eventually decays. No exception. And every decay channel is the weak nuclear force: the same force responsible for radioactivity.

The weak force has a unique property among the four fundamental forces: it violates parity. Left and right are not the same to the weak force. In mathematics, a surface where left and right are not globally defined is called non-orientable. The Möbius strip is non-orientable. The Klein bottle --- formed by closing the Möbius strip's open boundary --- is non-orientable too, but it requires a fourth dimension to exist without self-intersection.

The companion paper identified the constraint surface of existence as a Möbius strip, with $\alpha$ as its friction coefficient. This paper shows that the same equation, applied one level deeper, produces the Klein bottle eigenvalue --- and that eigenvalue points directly at the hole in the periodic table that the weak force makes.

The formula did not need to know about technetium. It was not built to explain nuclear stability. It is a self-consistency equation for $\alpha$, built from $\pi$ and factorials. But when you factor the polynomial and solve the next level, element 43 is sitting there. The algebra knew where the weak force tears the periodic table. The fourth dimension was always inside $\pi$.

---

## 1. The Tower

### 1.1 The Equation

The self-consistency equation for the fine structure constant (Carpenter, 2026d):

$$\alpha^{-1} + S \cdot \alpha = 4\pi^3 + \pi^2 + \pi$$

where:

$$S = \sum_{n=1}^{\infty} \frac{(2n-1)!!}{(4n)!} = \frac{1}{24} + \frac{3}{40320} + \frac{15}{479001600} + \cdots \approx 0.04174110$$

This is a quadratic in $x = \alpha^{-1}$:

$$x^2 - \text{RHS} \cdot x + S = 0$$

with solutions:

$$x = \frac{\text{RHS} \pm \sqrt{\text{RHS}^2 - 4S}}{2}$$

The large root is $\alpha^{-1}$. The small root is $S \cdot \alpha$. Their product is $S$ (Vieta's formula). Their sum is the RHS.

### 1.2 The Factorisation

The right-hand side factors:

$$4\pi^3 + \pi^2 + \pi = \pi(4\pi^2 + \pi + 1) = \pi^2\!\left(4\pi + 1 + \frac{1}{\pi}\right)$$

This is not an approximation. It is a polynomial identity. The RHS is a cubic in $\pi$ with coefficients $(4, 1, 1, 0)$, and $\pi$ divides it exactly.

### 1.3 Three Levels

Define:

$$\text{RHS}_0 = 4\pi^3 + \pi^2 + \pi = 137.036\,303\,776$$

$$\text{RHS}_1 = 4\pi^2 + \pi + 1 = 43.620\,010\,258$$

$$\text{RHS}_2 = 4\pi + 1 + \frac{1}{\pi} = 13.884\,681$$

Then $\text{RHS}_0 = \pi \cdot \text{RHS}_1 = \pi^2 \cdot \text{RHS}_2$, exactly.

At each level, solve the same quadratic $x^2 - \text{RHS}_k \cdot x + S = 0$:

| Level | Topology | RHS | Eigenvalue ($x^{-1}_{\text{large}}$) | Floor |
|---|---|---|---|---|
| 0 | Möbius strip | $4\pi^3 + \pi^2 + \pi$ | $\alpha^{-1} = 137.035\,999\,176$ | 137 |
| 1 | Klein bottle | $4\pi^2 + \pi + 1$ | $\beta^{-1} = 43.619\,053\,311$ | 43 |
| 2 | — | $4\pi + 1 + 1/\pi$ | $\gamma^{-1} = 13.881\,674$ | 13 |

The series $S$ is the same at every level. The polynomial changes; the self-referential correction does not. The equation is universal. The levels are distinguished by how many factors of $\pi$ have been peeled off.

### 1.4 Eigenvalue Ratios

The RHS ratios are exactly $\pi$: $\text{RHS}_0 / \text{RHS}_1 = \pi$ (verified to float64 precision: difference $< 10^{-15}$).

The eigenvalue ratios are *not* exactly $\pi$:

$$\frac{\alpha^{-1}}{\beta^{-1}} = 3.14165... \neq \pi = 3.14159...$$

The difference is $6.19 \times 10^{-5}$. This is the **overshoot constant** --- the self-coupling correction identified in (Carpenter, 2026g):

$$\mathcal{O}_k = \frac{S}{\text{RHS}_k^2}$$

At Level 0: $\mathcal{O}_0 = 2.22 \times 10^{-6}$. At Level 1: $\mathcal{O}_1 = 2.19 \times 10^{-5}$. The overshoot grows by $\pi^2$ per level because the RHS shrinks by $\pi$. The eigenvalue ratio differs from $\pi$ by a correction of order $\mathcal{O}_1 - \mathcal{O}_0 \sim 10^{-5}$.

The eigenvalues are not geometric ($\alpha^{-1} / \beta^{-1} \neq \pi$). They *would* be geometric if $S = 0$ (no self-referential correction). The overshoot is the price of self-reference.

### 1.5 The Product Rule

At every level, the product of the two roots equals $S$:

$$\alpha^{-1} \cdot (S \cdot \alpha) = S$$

$$\beta^{-1} \cdot (S \cdot \beta) = S$$

This is Vieta's formula for the quadratic. It confirms that the same $S$ governs every level. The self-referential correction is a constant of the tower, not a constant of the level.

---

## 2. Technetium

### 2.1 The Number

$$\beta^{-1} = 43.619\,053\,311$$

The floor is 43. Element 43 is technetium.

Technetium is the lightest element with no stable isotopes. It was the first element to be produced artificially (Perrier & Segrè, 1937). Its absence from the Earth's crust was a mystery for decades after Mendeleev predicted its existence in 1871.

### 2.2 Why No Stable Isotopes

The explanation has three interlocking components, all established nuclear physics.

**The Mattauch isobar rule.** Two adjacent isobars (same mass number $A$, differing by one in atomic number $Z$) cannot both be stable. For every mass number where technetium might be stable, either molybdenum ($Z = 42$) or ruthenium ($Z = 44$) already occupies the stable slot. Molybdenum has 7 stable isotopes (92, 94, 95, 96, 97, 98, 100). Ruthenium has 7 stable isotopes (96, 98, 99, 100, 101, 102, 104). Together, they block every available mass number. There is no gap for Tc to fill (Mattauch, 1934).

**The odd-$Z$ pairing penalty.** Technetium has $Z = 43$, an odd number of protons. The nuclear binding energy includes a pairing term $\delta$ in the semi-empirical mass formula (Bethe--Weizsäcker). For even-even nuclei, $\delta > 0$ (extra stability). For odd-$Z$ nuclei, this bonus is absent. The even-$Z$ neighbours Mo and Ru have systematically higher binding energy for their isobars, displacing Tc from the energy minimum at every mass number (Weizsäcker, 1935).

**No shell closure.** In the nuclear shell model, magic numbers (2, 8, 20, 28, 50, 82, 126) correspond to closed shells with extra stability. $Z = 43$ sits between the $Z = 28$ and $Z = 50$ closures, in a region with no special stabilisation. The 43rd proton occupies the $g_{9/2}$ orbital --- no closed-shell reinforcement (Mayer, 1949).

### 2.3 The Weak Force Makes Every Decay Channel

The crucial fact: **every technetium isotope is unstable specifically because weak-force decay channels are energetically available.**

- $^{99}$Tc $\to$ $^{99}$Ru by $\beta^{-}$ decay ($t_{1/2} = 2.11 \times 10^5$ yr)
- $^{95}$Tc $\to$ $^{95}$Mo by electron capture
- $^{98}$Tc $\to$ $^{98}$Ru by $\beta^{-}$ decay ($t_{1/2} = 4.2 \times 10^6$ yr)

If the weak force did not exist, technetium would be stable. The strong nuclear force binds it. The electromagnetic force does not provide enough energy to eject protons. It is *exclusively* the weak interaction --- beta decay --- that opens the channel.

The longest-lived isotope, $^{98}$Tc, has a half-life of 4.2 million years. This is geologically long but cosmically short. The small Q-values (energy releases) show how close technetium comes to stability. But "close" is not enough. Beta decay always finds the channel.

### 2.4 Promethium: The Same Mechanism at $Z = 61$

The only other element below bismuth with no stable isotopes is promethium ($Z = 61$, odd). The mechanism is identical: odd-$Z$ pairing penalty, isobar exclusion by neodymium ($Z = 60$) and samarium ($Z = 62$), and no shell closure between $Z = 50$ and $Z = 82$. Every promethium isotope decays by weak-force channels ($\beta^{-}$ or EC). Longest-lived: $^{145}$Pm, $t_{1/2} = 17.7$ yr.

If the tower extends, promethium sits at $Z = 61 \approx 4\pi^2 + \pi + 1 + 17.4$. The formula does not predict promethium --- but it predicts the mechanism: odd-$Z$ elements flanked by even-$Z$ neighbours with full isobar coverage, where the weak force is the sole agent of instability.

---

## 3. Parity Violation and Non-Orientability

### 3.1 The Weak Force Violates Parity

The weak interaction is the only fundamental force that distinguishes left from right. Lee and Yang (1956) proposed this; Wu et al. (1957) confirmed it experimentally: $^{60}$Co $\beta$-decay emits electrons preferentially in one direction relative to the nuclear spin. The effect is maximal --- the V$-$A structure of the weak current couples exclusively to left-handed particles.

Electromagnetism, the strong force, and gravity are parity-symmetric. The weak force is not. This is established physics, confirmed by sixty-nine years of high-precision experiments.

### 3.2 Non-Orientability Is the Mathematical Expression of Parity Violation

On an **orientable** surface, you can define "left" and "right" consistently everywhere. The surface has two sides. A clockwise loop remains clockwise under parallel transport.

On a **non-orientable** surface, there is no globally consistent definition of handedness. A clockwise loop, transported around the surface, returns as a counterclockwise loop. The Möbius strip has this property. The Klein bottle has this property.

If the constraint surface on which a force operates is non-orientable, then that force cannot distinguish left from right globally. Parity violation is a geometric consequence of non-orientability.

Hadley (1997, 2000) published this argument in *Classical and Quantum Gravity*: if spacetime contains non-orientable structures at small scales, P-violation follows as a geometric consequence, without additional postulates. The proposal is not mainstream but has not been refuted.

### 3.3 The Topology of Each Level

The companion paper (Carpenter, 2026f) identified the Level 0 constraint surface as a **Möbius strip** --- a non-orientable surface with one side, one edge, and a half twist. The fine structure constant $\alpha$ is its friction coefficient.

The **Klein bottle** is formed by closing the Möbius strip's boundary. Take the single edge of a Möbius strip and glue it to itself. The result has no boundary, no edge, one side --- and requires embedding in four dimensions to avoid self-intersection. It is the non-orientable analogue of the torus (which is formed by closing a cylinder's two boundaries). In three dimensions, the Klein bottle must intersect itself. In four dimensions, it is a smooth, closed, non-orientable 2-manifold.

| Surface | Orientable | Boundary | Embedding | Level |
|---|---|---|---|---|
| Cylinder | Yes | 2 edges | $\mathbb{R}^3$ | — |
| Möbius strip | No | 1 edge | $\mathbb{R}^3$ | 0 |
| Torus | Yes | None | $\mathbb{R}^3$ | — |
| Klein bottle | No | None | $\mathbb{R}^4$ | 1 |

Level 0 (Möbius) governs the electromagnetic force --- parity-symmetric at the force level, non-orientable at the surface level. The half-twist produces self-reference ($S \cdot \alpha$) without parity violation.

Level 1 (Klein) governs the weak-force shadow --- parity-violating. The closure of the boundary, requiring a fourth dimension, produces the full non-orientable topology. The weak force is the only force that "sees" the non-orientability. The Klein bottle's non-orientability without boundary is the topological structure of maximal parity violation.

### 3.4 The Fourth Dimension

The Klein bottle cannot exist in three dimensions without self-intersection. It requires $\mathbb{R}^4$.

The RHS at Level 0 encodes three-sphere and circle surface areas: $4\pi^3 + \pi^2 + \pi = (2S_3 \cdot S_1 + S_3 + S_1)/2$, where $S_3 = 2\pi^2$ (3-sphere surface) and $S_1 = 2\pi$ (circle circumference).

At Level 1, the $\pi$ factor has been peeled off. What remains is the **interior**: the constraint that operates one dimension deeper. The Klein bottle requires the fourth dimension because the Level 1 eigenvalue exists one factor of $\pi$ below the Level 0 surface.

Each factor of $\pi$ stripped from the RHS corresponds to one full oscillation cycle ($S_1 = 2\pi$) removed from the constraint surface. The Level 1 surface has lost one cycle of closure --- it can no longer close in three dimensions. It must embed in four.

---

## 4. The Overshoot Tower

### 4.1 The Self-Coupling at Each Level

The overshoot constant $\mathcal{O}_k = S / \text{RHS}_k^2$ measures the self-coupling strength at level $k$:

| Level | $\text{RHS}_k$ | $\mathcal{O}_k$ | Interpretation |
|---|---|---|---|
| 0 | $137.036$ | $2.22 \times 10^{-6}$ | Electromagnetic self-coupling |
| 1 | $43.620$ | $2.19 \times 10^{-5}$ | Weak-force self-coupling |
| 2 | $13.885$ | $2.17 \times 10^{-4}$ | Level 2 self-coupling |

The overshoot grows by $\pi^2$ per level because $\text{RHS}_{k+1} = \text{RHS}_k / \pi$.

At Level 0, the self-coupling is 2 ppm --- invisible in single-direction computation, visible only in the error-propagation ratio (Carpenter, 2026g). At Level 1, the self-coupling is 22 ppm --- ten times larger. The Klein eigenvalue departs from the inner polynomial ($43.620$) by $9.57 \times 10^{-4}$, which is $\mathcal{O}_1 \cdot \text{RHS}_1 \approx 10^{-3}$.

The tower amplifies self-reference. Each level deeper, the self-coupling grows. The further from the surface, the more the eigenvalue "knows about itself."

### 4.2 Convergence

The tower terminates when $\text{RHS}_k^2 < 4S$, because the discriminant $\text{RHS}_k^2 - 4S$ goes negative and the roots become complex.

$$\text{RHS}_k^2 = 4S \implies \text{RHS}_k = 2\sqrt{S} = 2\sqrt{0.04174} = 0.4087$$

Since $\text{RHS}_2 = 13.885 \gg 0.409$, and each level divides by $\pi \approx 3.14$, the tower remains real for:

$$\text{RHS}_k = \frac{\text{RHS}_0}{\pi^k} > 0.409 \implies \pi^k < 335 \implies k < 5.3$$

The tower has at most 5 real levels. Beyond Level 5, the eigenvalues become complex. The tower is finite.

| Level | $\text{RHS}_k$ | $\mathcal{O}_k$ | Real? |
|---|---|---|---|
| 0 | 137.036 | $2.2 \times 10^{-6}$ | Yes |
| 1 | 43.620 | $2.2 \times 10^{-5}$ | Yes |
| 2 | 13.885 | $2.2 \times 10^{-4}$ | Yes |
| 3 | 4.419 | $2.1 \times 10^{-3}$ | Yes |
| 4 | 1.407 | $2.1 \times 10^{-2}$ | Yes |
| 5 | 0.448 | $2.1 \times 10^{-1}$ | Marginal ($0.448^2 = 0.201 > 0.167$) |
| 6 | 0.143 | — | No ($0.143^2 = 0.020 < 0.167$) |

Five real levels. Then the tower collapses to complex eigenvalues.

---

## 5. What the Tower Predicts

### 5.1 Structural Predictions

| Prediction | Type | Testable? |
|---|---|---|
| The Level 1 eigenvalue floor is 43 (technetium) | Structural | Yes --- it is |
| Technetium's instability is entirely weak-force mediated | Established physics | Already confirmed |
| The weak force is the only parity-violating force | Established physics | Already confirmed |
| The Klein bottle (non-orientable, closed, 4D) is the Level 1 topology | Structural | Consistent but not directly testable |
| The overshoot grows by $\pi^2$ per level | Mathematical | Follows from the factorisation |
| The tower has at most 5 real levels | Mathematical | Follows from $\text{RHS}_k^2 > 4S$ |

### 5.2 What the Tower Does Not Predict

The tower does not predict the weak mixing angle $\sin^2\theta_W \approx 0.231$ from the Klein eigenvalue. The Level 1 eigenvalue $\beta^{-1} = 43.619$ does not appear to relate to $\sin^2\theta_W$ by any simple function. GUT theory derives $\sin^2\theta_W$ from the algebraic structure of the unification group SU(5), not from topology (Georgi & Glashow, 1974). No topological derivation of $\sin^2\theta_W$ exists.

The tower does not explain *why* $Z = 43$ specifically has no stable isotopes. The nuclear physics explanation (Mattauch rule + odd-$Z$ penalty + no shell closure) is complete. What the tower provides is a *structural coincidence* that may or may not be physically meaningful: the same equation that produces $\alpha$ from self-consistency produces 43 from the next level of the same polynomial.

The tower does not derive the number of fundamental forces (four), nor does it explain why Level 2 ($\gamma^{-1} = 13.882$) should correspond to a physical force. If it does, the most natural candidate is the strong force at some scale ($\alpha_s^{-1}$ runs from $\sim 8.5$ at $M_Z$ to larger values at lower energy). This is noted as a question, not a claim.

---

## 6. The Chain

Summarising the logical chain, with the status of each link:

$$\boxed{\alpha^{-1} + S\alpha = 4\pi^3 + \pi^2 + \pi}$$

$$\downarrow \text{factor out } \pi \text{ (exact polynomial identity)}$$

$$\boxed{\beta^{-1} + S\beta = 4\pi^2 + \pi + 1 = 43.620...}$$

$$\downarrow \text{floor}$$

$$\boxed{Z = 43 \text{ (technetium)}}$$

$$\downarrow \text{nuclear physics: no stable isotopes}$$

$$\boxed{\text{Every Tc isotope: } \beta^{\pm} \text{ decay (weak force only)}}$$

$$\downarrow \text{Wu (1957): only parity-violating force}$$

$$\boxed{\text{Parity violation} = \text{non-orientability}}$$

$$\downarrow \text{topology}$$

$$\boxed{\text{Klein bottle: non-orientable, closed, requires } \mathbb{R}^4}$$

Each link is either:
- A polynomial identity (exact)
- Established nuclear physics (Mattauch, Weizsäcker, Mayer)
- Established particle physics (Wu, Lee--Yang)
- A published topological proposal (Hadley, 1997)
- Or a structural identification (this paper)

The weakest link is Hadley's proposal connecting non-orientability to parity violation. It is published and unrefuted, but not mainstream. If that link is rejected, the chain still holds from $\alpha$ to 43 to technetium to weak force. Only the final step to Klein bottle topology is conditional.

---

## Boundaries {-}

1. **The floor operation is not a derivation.** $\beta^{-1} = 43.619...$ has floor 43, but 43.619 is not 43. The fractional part ($0.619...$, close to $\phi - 1 = 0.618...$ but different by $2 \times 10^{-3}$) is unexplained. The coincidence with $Z = 43$ is numerically striking but not algebraically derived.

2. **Two elements have no stable isotopes below bismuth.** Technetium ($Z = 43$) and promethium ($Z = 61$). The tower predicts 43 but not 61. A complete theory would need to account for both. The mechanism is the same (odd-$Z$ + weak force), but the formula singles out 43 specifically.

3. **The topological identification is interpretive.** Calling Level 0 "Möbius" and Level 1 "Klein bottle" is motivated by the properties (non-orientability, boundary structure, dimension of embedding) but is not derived from the quadratic. The quadratic knows only RHS and $S$. The topological names are imposed by the physicist, not demanded by the algebra.

4. **The overshoot tower is a mathematical consequence, not a physical theory.** The growth of $\mathcal{O}_k$ by $\pi^2$ per level follows from dividing RHS by $\pi$ at each level. Whether this mathematical structure maps onto physical forces is an open question.

5. **Hadley's non-orientability proposal is not mainstream.** The connection between Klein bottle topology and parity violation rests on Hadley (1997, 2000), which has not been incorporated into the Standard Model or any GUT. This paper uses it as a structural motivation, not as established physics.

---

# The Thesis in One Line

The fire burns at Level 0. The hole in the periodic table is at Level 1. They are the same equation divided by $\pi$.

---

## References {-}

**External**

- Bethe, H. & Bacher, R. (1936). "Nuclear physics. A. Stationary states of nuclei." *Reviews of Modern Physics*, 8: 82--229.
- Christenson, J.H., Cronin, J.W., Fitch, V.L. & Turlay, R.E. (1964). "Evidence for the $2\pi$ decay of the $K_2^0$ meson." *Physical Review Letters*, 13: 138--140.
- Georgi, H. & Glashow, S.L. (1974). "Unity of all elementary-particle forces." *Physical Review Letters*, 32: 438--441.
- Hadley, M.J. (1997). "Spin half in classical general relativity." *Classical and Quantum Gravity*, 14: A83--A93.
- Hadley, M.J. (2000). "The orientability of spacetime." *Classical and Quantum Gravity*, 19: 4565--4571.
- Lee, T.D. & Yang, C.N. (1956). "Question of parity conservation in weak interactions." *Physical Review*, 104: 254--258.
- Mattauch, J. (1934). "Zur Systematik der Isotopen." *Zeitschrift für Physik*, 91: 361--371.
- Mayer, M.G. (1949). "On closed shells in nuclei. II." *Physical Review*, 75: 1969--1970.
- Perrier, C. & Segrè, E. (1937). "Some chemical properties of element 43." *Journal of Chemical Physics*, 5: 712--716.
- Weizsäcker, C.F. von (1935). "Zur Theorie der Kernmassen." *Zeitschrift für Physik*, 96: 431--458.
- Wu, C.S., Ambler, E., Hayward, R.W., Hoppes, D.D. & Hudson, R.P. (1957). "Experimental test of parity conservation in beta decay." *Physical Review*, 105: 1413--1415.

**This Research Programme**

- Carpenter, J. (2026a). *A Formal Algebra of Collapse-Based Computation.* Zenodo. DOI: 10.5281/zenodo.18906064.
- Carpenter, J. (2026b). *Existence as Fixed Point: A Meta-Theory of Deterministic Collapse.* Zenodo. DOI: 10.5281/zenodo.18932890.
- Carpenter, J. (2026c). *The Constitutional Constant: Algebraic Foundations for $c = E/m$ and the Eigenvalue Structure of the Unit Sphere.* Zenodo. DOI: 10.5281/zenodo.18995286.
- Carpenter, J. (2026d). *The Fine Structure Constant as Self-Consistency Condition of a Four-Operator Collapse Algebra.* Zenodo. DOI: 10.5281/zenodo.18994393.
- Carpenter, J. (2026e). *Osmotic Selectivity as a Deterministic Function of the Fine Structure Constant.* Zenodo. DOI: 10.5281/zenodo.19000474.
- Carpenter, J. (2026f). *The Möbius Strip as Fixed Point of Existence: Cradle to the Grave.* Zenodo. DOI: 10.5281/zenodo.19020526.
- Carpenter, J. (2026g). *Solving for $\pi$: Recovering Geometry from Physics.* Zenodo. DOI: 10.5281/zenodo.19014277.
- Carpenter, J. (2026h). *Oxygen as Fixed Point: Wind, Blood, and the Constraint Surface of Existence.* Zenodo. DOI: 10.5281/zenodo.19020287.
