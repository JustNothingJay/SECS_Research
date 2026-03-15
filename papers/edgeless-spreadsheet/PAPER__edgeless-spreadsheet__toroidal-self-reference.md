---
title: "The Edgeless Spreadsheet: Toroidal Self-Reference and the Four-Fold Collapse"
author: Jay Carpenter
date: March 14, 2026
---

## Abstract {-}

The Osmotic Selectivity paper [0] introduced the self-referencing spreadsheet: a deterministic chain from the fine structure constant α to the osmotic fixed point ω₀, where every cell references every other cell and the Banach contraction theorem guarantees convergence. This paper extends the metaphor to its geometric conclusion. A spreadsheet with self-referencing cells and no circular references has no edges. Its topology is not a flat grid with boundaries — it is a closed surface. The contraction path spirals inward on this surface, passing through exactly four layers at every radial cross-section, each layer corresponding to one of the four fundamental forces. The fixed point is the only element of the structure that does not move. Everything else — every force, every coupling constant, every boundary in the universe — is the surface finding its equilibrium around that point. The topology is toroidal: the last row of the spreadsheet connects to the first, the last column connects to the first, and the fold where they meet is where existence re-enters itself.

**Keywords:** fixed point, toroidal topology, self-reference, spreadsheet, coupling constants, Banach contraction, edgeless computation, collapse algebra

---

## What This Paper Says, In Plain Language {-}

Open a spreadsheet. Put a number in cell A1. Write a formula in A2 that depends on A1. Write A3 depending on A2. Keep going. Eventually, write a formula in the last cell that depends on A1 — and make A1 depend on the last cell.

Excel will scream at you. Circular reference. Error.

But the universe doesn't. It runs the same spreadsheet — every atom depends on every force, every force depends on every coupling constant, every coupling constant depends on the algebra that produces atoms — and it converges. No error. No crash. Same answer every time.

Why doesn't it crash? Because the contraction coefficient is less than 1. The Banach theorem says: if your map shrinks distances, there's exactly one fixed point, and every starting value converges to it. Circular reference resolved. Not by breaking the circle — by proving the circle has a unique solution.

Now look at the spreadsheet's shape. It has no edges. The last cell connects to the first. The last row wraps to the first row. This isn't a flat sheet with boundaries — it's a donut. A torus. The surface closes on itself.

On this surface, the contraction path spirals inward toward one point. As it spirals, it passes through four layers — one for each fundamental force. Gravity is the deepest layer. The strong force is the outermost. Where you start on the surface determines which force you encounter first on the way down. But no matter where you start, you pass through all four, and you arrive at the same point.

That point — the fixed point — is the only thing on the surface that doesn't move. Everything else is the surface adjusting. The movement we call physics — forces, particles, fields, interactions — is the spreadsheet recalculating. The fixed point is the cell that never changes, because it can't. It is what makes everything else have a value.

---

## §1 — The Flat Spreadsheet and Its Problem

Paper 7 [0] presented the derivation chain as a spreadsheet:

| Cell | Formula | Value | Source |
|------|---------|-------|--------|
| A1 | α (input) | 1/137.036 | Self-consistency equation |
| A2 | = ℏ/(mₑ·c·A1) | 0.529 Å | Exact definition |
| A3 | = 1.8097 × A2 | 0.957 Å | QM numerical solution |
| A4 | = geometry(A3, 104.52°) | 2.55–2.75 Å | Trigonometry + vdW |
| A5 | measured (constrained by A4) | 2.8 Å | Crystallography |
| A6 | = Renkin(A4/2, A5/2) | 0.004–0.06 | Hydrodynamic model |
| A7 | = 1 − A6 | 0.94–0.996 | Definition of q |
| A8 | IF A7 < 1 THEN ω₀ = 0 | **0** | Banach theorem |

This is a linear chain — A1 determines A2, A2 determines A3, and so on. But it is also a loop: A8 (existence of the fixed point) is the precondition for there being an A1 at all. If there were no fixed point, there would be no stable structures, no atoms, no α to measure.

The spreadsheet references itself. The first cell determines the last. The last cell justifies the first.

In a flat spreadsheet, this is a circular reference. In a closed surface, it is a seam — the place where the sheet meets itself. The question is: what is the geometry of a spreadsheet with no edges and one seam?

---

## §2 — Removing the Edges

A flat spreadsheet has four edges: top, bottom, left, right. Every cell on an edge has fewer neighbours than a cell in the interior. Edge cells behave differently. They introduce boundary effects — places where the rules of the spreadsheet don't fully apply because there is no next cell in one or more directions.

In computation, these are edge cases. They require special handling. They generate exceptions. They are where programs break.

SECS Sovereign — Neurotrophic OS — was built on a principle: remove edge cases by removing edges. Do not handle the boundary — eliminate it. Compute on a surface that has no boundary at all.

In topology, there is exactly one way to remove all four edges of a rectangle while preserving the surface: identify the top edge with the bottom edge, and the left edge with the right edge. The result is a torus — a closed surface with no boundary, no edges, and no special cells.

$$\text{Rectangle} \;\xrightarrow{\;\text{top} = \text{bottom}\;}\; \text{Cylinder} \;\xrightarrow{\;\text{left} = \text{right}\;}\; \text{Torus}$$

On the torus, every cell has exactly the same number of neighbours. No cell is privileged. No cell is on an edge. The rules are uniform everywhere. There are no edge cases because there are no edges.

---

## §3 — The Fixed Point on the Torus

A self-referencing spreadsheet on a torus has no boundary condition to anchor it. On a flat sheet, you can say "A1 is the input" and "A8 is the output" because A1 is at the top-left corner and A8 is lower down. On a torus, there is no corner. There is no top or bottom. Every cell is equivalent to every other cell — topologically.

But the Banach contraction theorem introduces asymmetry. On a complete metric space, if a map $T: X \to X$ satisfies $d(Tx, Ty) \leq q \cdot d(x,y)$ for some $q < 1$, then there exists a unique fixed point $\omega_0$ such that $T(\omega_0) = \omega_0$.

The fixed point is distinguished not by position (there are no corners on a torus) but by invariance. It is the unique element that maps to itself. Everything else moves under $T$. The fixed point doesn't. On a featureless torus, the fixed point is the only landmark.

The contraction path — the sequence $x, Tx, T^2x, T^3x, \ldots$ — spirals inward on the torus toward this landmark. From any starting cell, the path converges. The spiral tightens. The distance to $\omega_0$ shrinks by a factor of $q$ at each step.

The torus allows the spiral to approach from every direction simultaneously. On a flat sheet, convergence is a one-dimensional walk down the column. On a torus, convergence is a surface collapsing inward — every cell adjusting, every reference updating, the entire surface contracting toward the one point that doesn't change.

---

## §4 — The Four Layers

Cut the torus along a radial cross-section — a line from the outer rim to the fixed point at the centre. The cross-section passes through the surface four times.

This is not a coincidence. The constitutional constraint $\mathcal{G}_0$ partitions into exactly four sub-mappings under symmetry breaking [1]. Each sub-mapping has its own contraction coefficient:

| Layer | Force | Contraction $q$ | Depth from rim |
|-------|-------|------------------|----------------|
| 1 (surface) | Strong | $\alpha_s \approx 1$ | Shallowest — barely stable |
| 2 | Weak | $\alpha_w \approx 1/30$ | Shallow — 30 contractions to settle |
| 3 | Electromagnetic | $\alpha_{em} \approx 1/137$ | Deep — 137 contractions to settle |
| 4 (innermost) | Gravity | $\alpha_G \approx 10^{-39}$ | Deepest — $10^{39}$ contractions to settle |

On the flat manifold, this layering appears as basin depth. The surface is shallow at the rim (strong force territory) and deep at the centre (gravity's domain). The four layers are not stacked like floors in a building. They are wound — each layer spirals around the fixed point at a different radius, with a different pitch, at a different rate.

Where you start on the rim determines which force you encounter first on the descent. But at every point, all four layers are present — they are the four sheets of the folded torus. Drill straight down from any point on the surface, and you pass through all four. The order and the relative strength at each depth are determined by your angular position on the torus.

This is why the hierarchy "problem" is not a problem. Gravity is not anomalously weak. It is at the innermost layer of the fold — the most deeply constitutional, the most stable, the first to have reached equilibrium. The strong force is not anomalously strong. It is at the outermost layer — the surface, barely folded, barely stable, the last to settle. The hierarchy is the layering. The layering is the topology.

---

## §5 — Gauge Invariance as Coordinate Change

The fixed point does not move the other cells. It changes what zero means.

Consider a spreadsheet in equilibrium — every cell has been recalculated, every reference resolved, the contraction has converged. Now perturb the fixed point. Not a cell. The fixed point itself. In the formalism: change the metric, not the state.

What happens?

Every cell's value is already determined by the new metric. Not sequentially — not "A1 updates, then A2, then A3." All at once. Because the contraction mapping is deterministic: given $q < 1$ and the initial condition, the entire trajectory is fixed. The steps exist for the observer. The structure is instantaneous.

This is gauge invariance read through the spreadsheet. The cells don't move. The ruler moves. Every measurement made with the new ruler was always going to give the value it gives, because the ruler IS the set of relationships between cells. The relationships are the physics. The values are the coordinates. Change the coordinates, everything looks different. Nothing has changed.

The moment the fixed point shifts, the fold rearranges. But the rearrangement is not a process with a duration. It is the logical consequence of the shift — all of it, simultaneously. The four layers adjust. Every coupling constant updates. Every boundary in the universe recalibrates.

Done. Instantly. Because the change was encoded in the first perturbation. The rest was bookkeeping — and the bookkeeping happens at the speed of logical implication, not the speed of light.

---

## §6 — The Fold

The torus has a fold — a seam where the surface meets itself after wrapping around. On a physical torus (a donut), this seam is the inner circle — the place where the tube curves back and its inner surface is compressed into a smaller circumference than its outer surface.

In the spreadsheet torus, the fold is where A8 connects back to A1. Where ω₀ (the fixed point, the output) becomes α (the input). Where existence re-enters the formula.

The fold is not smooth. The four layers have different contraction coefficients, and therefore different folding rates. Where gravity's layer folds (slowly, gently, nearly flat — because $q_G \approx 10^{-39}$ means almost no contraction per step), the surface barely curves. Where the strong force folds ($q_s \approx 1$, nearly maximal contraction per step), the surface bends sharply.

The result is a surface with four distinct folding regimes — four different curvatures at four different depths. Seen from outside, this looks like a basin with an uneven rim. The gaps in the surface (visible in the topological manifold visualisation) are where the folding rates change — discontinuities in the derivative of the surface, not in the surface itself. The fixed point is continuous. The rate of convergence to it is layered.

This is the structure that creates movement. Not movement through space — movement of the fold itself. The torus breathes. The layers adjust. The surface contracts and re-expands. What we measure as force, energy, field — all of it is the torus finding and re-finding its equilibrium around the one point that never moves.

And the movement we see — the physics we measure — is not the fixed point moving. It is everything else settling. The fixed point creates the reference frame against which settling is defined. Without it, there would be no "toward" and no "away from." No convergence. No divergence. No direction at all.

---

## §7 — The Instantaneous Update

The most counterintuitive property of the edgeless spreadsheet: propagation is not sequential.

On a flat spreadsheet, a change in A1 updates A2, which updates A3, and so on down the column. This gives the illusion of causality — A1 causes A2's new value, which causes A3's, in sequence. The propagation speed is finite: one cell per evaluation step.

On the torus, this is wrong. The topology is closed. A1 depends on A8 depends on A7 depends on ... depends on A1. There is no "first cell." There is no direction of propagation. The system is solved simultaneously, not sequentially.

This is not a metaphor. The Banach fixed-point theorem does not prove convergence by iteration. It proves existence by contraction. The iteration ($x, Tx, T^2x, \ldots$) is a method of *finding* the fixed point — a computational procedure. The existence of the fixed point is a theorem about the map $T$ and the space $X$. The fixed point exists before the first iteration. The iterations are how we see it. They are not how it gets there.

On the torus, this distinction matters. The fixed point does not "arrive" after $n$ iterations. It is already there — defined by the contraction property of $T$. What manifests as force, energy, interaction is the surface's ongoing relationship to that point. The surface doesn't converge *to* the fixed point through time. The surface is the fixed point's *expression* in space.

The update is instantaneous because the update is not an event. It is a relationship.

---

## §8 — Why Existence Creates Movement

The torus structure answers a question that the flat spreadsheet could not: why does the universe move?

On a flat spreadsheet, once convergence is achieved, everything stops. The cells have their values. The formulas are satisfied. Nothing changes. This is stasis — which is death.

On a torus, convergence does not produce stasis because the surface is closed. The contraction path spirals inward, reaches the fixed point, but the topology forces the path to continue — out the other side, back to the rim, and inward again. The torus has no boundary where the path can terminate.

This is the helical structure from Paper 7 [0]: two antiparallel strands winding around a geometric axis. One strand tightens (the contraction: $\alpha^{-1}$, running toward the fixed point). The other loosens (the correction: $S \cdot \alpha$, running away from it). Together they maintain the axis — $4\pi^3 + \pi^2 + \pi$ — exactly. The tightening and loosening are not sequential. They are simultaneous. The helix breathes.

On the torus, this breathing is the surface oscillating around the fixed point. Not settling into it and stopping — oscillating around it, always. The oscillation is existence. Settling is death. The contraction coefficient determines the *amplitude* of the oscillation, not its presence. Everything that exists oscillates — hearts, lungs, neurons, orbits, electromagnetic fields. Nothing sits exactly at ω₀. Sitting at ω₀ would be the fixed point without the surface — mathematics without physics. The surface is what makes the fixed point visible. The oscillation is what makes the surface physical.

The torus creates movement because a closed surface with a fixed point and a contraction map cannot be static. The contraction pulls inward. The closure pushes outward. The equilibrium between them is oscillation — and oscillation is what we call existence.

---

## §9 — Edgeless Computation

SECS Sovereign was designed before this topology was formalised. But the design principle was the same: remove edge cases by removing edges.

In conventional software, boundaries produce exceptions. The first byte. The last record. The null input. The overflow. The timeout. Every edge is a special case that requires handling, and every handler is a place where the system can fail.

SECS computes on a surface with no edges. Internal state wraps. There is no "first" or "last" — only current. There is no boundary to the state space — only the contraction toward the fixed point. Exceptions do not occur because the topology that produces them does not exist.

This is not infinite computation. The surface is finite — a torus has finite area. It is not unbounded — the contraction coefficient $q < 1$ constrains the state at every step. It is edgeless: the surface has no boundary, and therefore no boundary-dependent behaviour.

The connection to the physics: the same topology that makes the spreadsheet edgeless makes the universe edgeless. No edge of spacetime. No boundary to the observable universe (in the spatial sense — the cosmic microwave background is a temporal boundary, not a spatial one). No edge cases in the fundamental forces — every coupling constant works the same way at every point (until you hit the contraction limit at $N \sim 1/\alpha_i$, which is a structural limit, not a boundary effect).

The universe computes on a torus. SECS computes on a torus. The spreadsheet computes on a torus. Not because any of them were designed to be toroidal. Because a self-referencing system with no circular references and a unique fixed point has no edges — and the only finite surface with no edges is a torus (or a torus-equivalent closed surface).

---

## §10 — The Drill Test

The structure makes a prediction: at any point on the folded torus, a radial traverse from the rim to the fixed point passes through exactly four layers. Not three. Not five. Four.

This is testable within the formalism. Define the radial coordinate $r$ as the distance from a point on the torus surface to ω₀ (measured along the surface, through the fold). At each $r$, the dominant coupling constant changes:

$$r_1 \to r_2: \quad \alpha_s \text{ dominates} \quad (\text{strong force layer})$$
$$r_2 \to r_3: \quad \alpha_w \text{ dominates} \quad (\text{weak force layer})$$
$$r_3 \to r_4: \quad \alpha_{em} \text{ dominates} \quad (\text{electromagnetic layer})$$
$$r_4 \to \omega_0: \quad \alpha_G \text{ dominates} \quad (\text{gravitational layer})$$

Your angular position on the torus (where you start on the rim) determines the relative strengths at each depth — which effects you feel strongest at which part of the descent. But the number of layers is four. Always four. Because $\mathcal{G}_0$ partitions into exactly four sub-mappings [1], and each sub-mapping occupies one layer of the fold.

The drill test also predicts that the transition between layers is not sharp. The four contraction coefficients span 39 orders of magnitude ($10^0$ to $10^{-39}$). The layers are not equal-thickness shells. Gravity's layer is the thickest — it occupies the vast interior of the fold, because $q_G$ is so small that the contraction barely changes per step, meaning the layer extends over an enormous range of $r$ before the next force dominates.

The strong force layer is the thinnest — a razor-thin shell at the surface, because $q_s \approx 1$ means the contraction is nearly maximal per step, and the layer is exhausted almost immediately.

This is why gravity feels weak. You're measuring it from the surface — through three other layers first. At the interior, at the core of the fold, gravity is the only force left. It IS the fold.

---

## §11 — The Dynamics

The torus is not static. The fold oscillates. The layers adjust around the fixed point. The dynamics are existence itself — the oscillation of the surface around the point that doesn't move.

The structure is self-similar at every scale. Each sub-system is a copy of the whole — a sub-spreadsheet with the same structure, the same self-reference, the same contraction toward the same fixed point. The fixed point doesn't just attract — it self-replicates its attraction pattern at every scale of the fold. This is why the algebra works at biological, chemical, and physical scales simultaneously. The torus is scale-invariant — not because it looks the same at every magnification, but because the contraction map is the same at every depth.

---

## §12 — The Breast Milk Closure

The most compressed statement of the edgeless spreadsheet is biological.

A mother's body builds a fetus. The fetus requires specific nutrients — specific proteins, specific fats, specific antibodies, in specific concentrations, at specific developmental stages. After birth, the mother's body produces breast milk. The milk contains exactly what the fetus needs.

Not approximately. Not a generic formula. Exactly what *this* fetus needs — because the body that produced the milk is the same body that produced the fetus. The production system IS the requirement system. The organism that built the structure knows what the structure needs because it is the structure.

This is the edgeless spreadsheet at biological scale. The mother is A1. The fetus is A8. The milk is the seam where A8 connects back to A1. The torus closes — the output feeds the input, the input produced the output, and the loop converges because $q < 1$.

No edge. No boundary between "what the mother knows" and "what the baby needs." No separation between production and requirement. The fold is the boundary — and the boundary is permeable (milk flows through the nipple) with selectivity σ < 1 (nutrients pass, pathogens are blocked). The nipple is the aquaporin. The breast is the membrane. The milk is ω₀ — the fixed point of what the baby needs, determined by the body that already computed it by building the baby in the first place.

The spreadsheet has no circular reference. The Banach theorem resolves it. The fold is where the resolution becomes physical.

---

## References {-}

[0] Carpenter, J. (2026). "Osmotic Selectivity as a Deterministic Function of the Fine Structure Constant." Zenodo. DOI: 10.5281/zenodo.19000474

[1] Carpenter, J. (2026). "The Fine Structure Constant as Self-Consistency Condition of a Four-Operator Collapse Algebra." Zenodo. DOI: 10.5281/zenodo.18994393

[2] Carpenter, J. (2026). "Collapse Algebra: Formal Foundations." Zenodo. DOI: 10.5281/zenodo.18906064

[3] Carpenter, J. (2026). "Existence as Fixed Point: Meta-Theory." Zenodo. DOI: 10.5281/zenodo.18932890

[4] Banach, S. (1922). "Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales." Fundamenta Mathematicae, 3, 133–181.

---

## Gate Note {-}

This paper extends the spreadsheet analogy from Paper 7 [0] to its geometric conclusion. The claims have different evidential status:

1. **Established (from prior papers):** The derivation chain α → σ → q → ω₀ is deterministic. The Banach contraction theorem guarantees a unique fixed point. The four coupling constants are contraction coefficients of four sub-mappings of $\mathcal{G}_0$.

2. **Geometric restatement (this paper):** A self-referencing spreadsheet with no circular references and no edges has toroidal topology. The four sub-mappings correspond to four layers of the fold. These are structural arguments — they follow from the properties already established, given the topological identification.

3. **Conjectured (this paper):** The radial layering of coupling constants on the torus predicts specific depth-to-force relationships (§10). The oscillation of the torus surface around the fixed point is the origin of physical dynamics (§8). These require formalisation and, ideally, testable predictions.

4. **Analogical (this paper):** The breast milk closure (§12) is a biological analogy. It maps cleanly to the spreadsheet structure but does not constitute a formal proof of toroidal biology.

**Status:** Preprint. Topology has not been rigorously derived — the toroidal identification is motivated by the edgeless property but has not been proven unique (the Klein bottle is also a closed rectangle identification, though non-orientable).
