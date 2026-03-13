---
title: "Vulnerability Windows as Lyapunov Stability Margins: A Dynamical Systems Model of Gestational Oxygen Sensitivity"
author: Jay Carpenter
date: March 12, 2026
---

## Abstract {-}

Each fetal organ system passes through a developmental period during which it is maximally sensitive to oxygen disruption. The General Theory of Latent Gestational Injury [5] identifies these vulnerability windows and maps them to clinical outcomes. This paper provides the dynamical systems formalisation of that mapping.

We model each developing organ system as a dynamical system with stable equilibrium trajectories corresponding to normal maturation. The system's Lyapunov stability margin — the maximum perturbation from which it can return to the normal trajectory — varies as a function of gestational age. During vulnerability windows, the stability margin narrows: the system can tolerate less perturbation before it is displaced to an alternative attractor (arrested development, reduced endowment, or abnormal structure).

Three results follow. First, the super-window of 23–36 weeks gestation corresponds to the period of minimum aggregate Lyapunov stability margin across all simultaneously developing systems. Second, Prigogine's dissipative structure framework (Prigogine, 1977) identifies the fetus as a far-from-equilibrium system maintained by continuous oxygen throughput — withdrawal of the throughput does not produce a graceful degradation but a phase transition to an alternative attractor. Third, the HIF-1α / PHD-VHL molecular oscillation under intermittent hypoxia can be modelled as a Lotka-Volterra predator-prey dynamic, with oscillation amplitude determining whether the system remains within or is expelled from the stability basin.

**Keywords:** Lyapunov stability, dynamical systems, vulnerability windows, dissipative structures, gestational programming, far-from-equilibrium, Lotka-Volterra, HIF-1α, preeclampsia, developmental attractor

---

## The Developmental Trajectory as Dynamical System

### Dynamical Systems Framework

A dynamical system is defined by a state space $\mathcal{X}$, a time parameter $t$, and an evolution rule $\dot{x} = f(x, t)$ that specifies how the state changes over time. An equilibrium point $x^*$ satisfies $f(x^*, t) = 0$; at equilibrium, the system remains stationary.

A trajectory is a path $x(t)$ through the state space as the system evolves. In developmental biology, the trajectory is not toward a fixed equilibrium but toward a time-parametrised target: the normal developmental programme. The system must track a moving target — a reference trajectory $x_{\text{ref}}(t)$ — rather than converge to a point.

This is a tracking problem in control theory. The state $x(t)$ represents the current developmental state of an organ system. The reference trajectory $x_{\text{ref}}(t)$ represents the normal developmental programme — the expected state at each gestational age. The deviation $e(t) = x(t) - x_{\text{ref}}(t)$ represents the developmental deficit at time $t$.

### The Organ System State Vector

For organ system $k$, the state vector $x^{(k)}(t)$ encodes:

- **Cell count**: $n(t)$ — number of functional cells (nephrons, cardiomyocytes, preOLs, etc.)
- **Maturation state**: $m(t)$ — degree of cellular differentiation (e.g., preOL → immature OL → mature OL)
- **Structural organisation**: $s(t)$ — tissue architecture (cortical folding, tubular organisation, vascular branching)
- **Functional capacity**: $\phi(t)$ — current functional level (glomerular filtration capacity, conduction velocity, contractility)

These are not independent. Cell count enables maturation, maturation enables structural organisation, structure enables function. The state variables form a partially ordered sequence, with each depending on its predecessors being within acceptable bounds.

### The Normal Trajectory

The normal developmental trajectory $x_{\text{ref}}^{(k)}(t)$ for organ system $k$ is defined by the genetically programmed developmental schedule, modulated by adequate oxygen supply. Under normal conditions:

$$\dot{x}_{\text{ref}}^{(k)} = g^{(k)}(x_{\text{ref}}^{(k)}, O_2(t))$$

where $O_2(t) \geq O_{2,\min}^{(k)}$ — the oxygen supply is sufficient for the programme to execute.

The normal trajectory is established empirically by histological studies of normal fetal development: nephron counts at each gestational age (Luyckx & Brenner, 2005; Sutherland et al., 2011), white matter maturation staging (Back et al., 2001; Kinney, 2006), cardiomyocyte proliferation curves (Botting et al., 2018), cortical folding patterns (Chi et al., 1977; Armstrong et al., 1995).

---

## Lyapunov Stability and the Vulnerability Window

### Lyapunov Stability — Definition

A trajectory $x^*(t)$ of a dynamical system is **Lyapunov stable** if, for every $\epsilon > 0$, there exists $\delta > 0$ such that:

$$\|x(t_0) - x^*(t_0)\| < \delta \implies \|x(t) - x^*(t)\| < \epsilon \quad \forall \, t \geq t_0$$

That is: if the system starts close to the reference trajectory, it stays close. The maximum $\delta$ for a given $\epsilon$ is the **stability margin** — how far the system can be perturbed and still return to (or remain near) the reference trajectory.

A stronger form — **asymptotic stability** — requires that the perturbed trajectory actually converges back to the reference:

$$\|x(t) - x^*(t)\| \to 0 \text{ as } t \to \infty$$

### The Time-Varying Stability Margin

In classical dynamical systems, the stability margin of an equilibrium is typically constant (for autonomous systems) or slowly varying. In fetal development, the stability margin is **strongly time-varying**:

$$\delta^{(k)}(t) = \text{max perturbation from which system } k \text{ can recover at time } t$$

During vulnerability windows, $\delta^{(k)}(t)$ reaches a minimum: the system is traversing a narrow passage in its stability landscape, and even small perturbations can displace it permanently.

The stability margin varies with gestational age because:

1. **Proliferative phases have narrow margins**: when cells are rapidly dividing, the timing is critical. A delay of even days can result in a permanently reduced cell count (nephrons: Sutherland et al., 2011).

2. **Differentiation transitions are irreversible**: the preOL → immature OL transition is a one-way state change. If oxygen disruption arrests a preOL before it transitions, it may never transition (Back, 2017). This is a saddle-node bifurcation: the normal state and the arrested state are separated by a saddle point, and perturbation beyond the saddle displaces the cell to the arrested attractor.

3. **Structural organisation has assembly constraints**: cortical gyration requires coordinated cell migration, axon guidance, and dendritic arborisation. These processes must occur in sequence, and each has a temporal window. A perturbation during gyration produces a structural abnormality that subsequent development builds upon rather than corrects (Armstrong et al., 1995).

### The Vulnerability Window as Minimum Stability Margin

The vulnerability window of organ system $k$ during gestational weeks $[t_1^{(k)}, t_2^{(k)}]$ is the period during which:

$$\delta^{(k)}(t) < \delta_{\text{crit}}$$

where $\delta_{\text{crit}}$ is the perturbation level that typical gestational complications (preeclampsia, placental insufficiency) actually produce. Outside the vulnerability window, $\delta^{(k)}(t) > \delta_{\text{crit}}$ — the system can absorb the perturbation and recover. During the window, the same perturbation exceeds the stability margin and displaces the trajectory.

This formalises the alignment model's core observation [5, §1–2]: the same hypoxic insult produces different outcomes depending on when it occurs. The oxygen disruption is the perturbation. The vulnerability window is the period of minimum stability margin. The outcome depends on whether the perturbation exceeds the margin.

### The Stability Landscape

The conceptual picture is a potential energy landscape that changes with gestational age:

- **Before vulnerability window**: deep basin around normal trajectory, high walls. Perturbation rocks the system within the basin but it returns.
- **During vulnerability window**: basin becomes shallow and narrow. An alternative basin (arrested development) becomes accessible. The same perturbation can push the system over the saddle into the alternative basin.
- **After vulnerability window**: the normal basin deepens again — but if the system is already in the alternative basin, it stays there. The window has closed.

This is Waddington's epigenetic landscape (Waddington, 1957) given mathematical content. Waddington's metaphor of a ball rolling down branching valleys is formalised here as a dynamical system with time-varying stability margins and irreversible bifurcations.

---

## The Super-Window as Aggregate Stability Minimum

### Aggregate Stability Margin

For $K$ organ systems developing simultaneously, the aggregate stability margin at time $t$ is:

$$\Delta(t) = \min_{k \in \{1, \ldots, K\}} \delta^{(k)}(t)$$

This is a min-of-minima metric: the aggregate system is only as robust as its least stable subsystem at any given time.

### The Super-Window Characterisation

The super-window of 23–36 weeks [5, §2.3] is the gestational period during which $\Delta(t)$ is minimised:

$$t^* = \arg\min_t \Delta(t) \qquad t^* \in [23 \text{ weeks}, 36 \text{ weeks}]$$

This is because the maximum number of organ systems are simultaneously in their vulnerability windows during this period. Even if each system's individual stability margin minimum occurs at a different gestational age (white matter peaks at ~28 weeks, nephrons peak at ~32 weeks, etc.), the aggregate minimum occurs when the greatest number of individual minima overlap.

The vulnerability windows from the alignment model [5]:

| Organ System | Vulnerability Window (weeks) | Critical Process |
|---|---|---|
| White matter (preOLs) | 23–32 | Pre-oligodendrocyte maturation |
| Kidneys (nephrons) | 20–36 | Nephrogenesis (closes ~36 weeks) |
| Heart (cardiomyocytes) | 20–38 | Cardiomyocyte proliferation |
| Lungs (alveoli) | 24–36 | Alveolar septation |
| Cortex (gyration) | 24–38 | Primary and secondary gyration |
| Cerebellum | 24–40 | Granule cell proliferation |
| Hippocampus | 22–36 | CA1/CA3 neuronal maturation |
| Retina | 24–36 | Retinal vascular development |
| Pancreas (β-cells) | 20–38 | Islet cell proliferation |

Between 24–32 weeks, **all nine systems** are simultaneously in their vulnerability windows. This 8-week period is the core of the super-window — the period of minimum aggregate stability margin.

### The Clinical Consequence

Preeclampsia most commonly presents after 20 weeks and peaks between 28–36 weeks (Steegers et al., 2010; ACOG Practice Bulletin 222, 2020). The timing of the pathology aligns with the vulnerability of the target:

- PE onset at 28 weeks → hits 9/9 systems at or near their individual minimum stability margins
- PE onset at 34 weeks → hits fewer systems, some already past their vulnerability windows (white matter closing, nephrons closing)
- PE onset at 37 weeks → most systems past vulnerability, damage is primarily acute rather than developmental

This explains the gestational-age-dependent severity gradient: early-onset PE (< 34 weeks) produces the most severe multi-system developmental injury because it strikes during the aggregate stability minimum.

---

## The Fetus as Dissipative Structure

### Prigogine's Framework

Ilya Prigogine's theory of dissipative structures (Prigogine, 1977; Prigogine & Stengers, 1984; Nobel Prize in Chemistry, 1977) identifies a class of systems that:

1. Exist far from thermodynamic equilibrium
2. Maintain their structure through continuous throughput of energy and matter
3. Exhibit spontaneous self-organisation through symmetry-breaking instabilities
4. Undergo **phase transitions** (not gradual degradation) when the throughput is disrupted

Classical examples include Bénard convection cells, the Belousov-Zhabotinsky reaction, and laser coherence. Each maintains complex structure only while energy throughput exceeds a critical threshold. Below the threshold, the structure collapses to a simpler state.

### The Fetus as Dissipative Structure

The developing fetus satisfies all four criteria:

1. **Far from equilibrium**: the fetus is among the most metabolically active biological entities per unit mass. Fetal O₂ consumption is ~6–8 mL/min/kg (Battaglia & Meschia, 1986), compared to adult resting consumption of ~3.5 mL/min/kg. The fetus is approximately twice as metabolically intense as the adult, per unit mass.

2. **Continuous throughput**: the oxygen, glucose, and nutrient supply through the placenta is continuous. There is no reserve — the fetus has essentially no glycogen stores before 36 weeks (Shelley, 1961) and minimal oxygen reserve (fetal blood oxygen content provides ~2 minutes of reserve at normal consumption rate — Giussani, 2016).

3. **Self-organisation**: the developmental programme is a cascade of symmetry-breaking events: cellular differentiation (one cell type → many), morphogenesis (uniform tissue → structured organ), lateralisation (bilateral symmetry → functional asymmetry). Each is an instability that produces a more complex, lower-symmetry state.

4. **Phase transition under disruption**: when oxygen throughput is reduced below a critical threshold, the system does not gracefully degrade. It transitions to an alternative state — developmental arrest. The preOL stops maturing. The nephron precursor stops dividing. The cardiomyocyte exits the cell cycle prematurely. These are phase transitions to alternative attractors, not proportional reductions in output.

### The Critical Threshold

Prigogine's framework predicts that the transition from ordered state to disordered state is **abrupt** and occurs at a critical throughput value (Prigogine, 1977, Chapter 8). Below this value, the dissipative structure cannot be maintained.

Applied to gestational development: there exists a critical oxygen delivery rate below which the developmental programme undergoes a phase transition from maturation to arrest. This is the capacity threshold $C_{\min}^{(k)}$ identified in the information-theoretic model [6] — but now understood not as a gradual threshold but as a phase boundary.

The clinical implication: developmental injury is not proportional to oxygen deficit. There is a threshold below which the injury escalates sharply. A fetus with $SpO_2$ just above the threshold may develop normally; a fetus with $SpO_2$ just below may sustain severe developmental arrest. The difference in oxygen level may be small, but the difference in outcome is categorical.

This is consistent with the epidemiological evidence: the distribution of outcomes in preeclampsia-exposed populations is bimodal (severe injury or near-normal), not normally distributed around a mean deficit (Backes et al., 2011; Odegård et al., 2000). The bimodality suggests a phase transition rather than a dose-response proportionality.

---

## The HIF Oscillation as Lotka-Volterra Dynamics

### Predator-Prey Formulation

The HIF-1α / PHD-VHL counter-regulatory system [5, §3.3] exhibits oscillatory dynamics that map onto the Lotka-Volterra predator-prey equations (Lotka, 1925; Volterra, 1926).

Define:
- $H(t)$ = HIF-1α concentration (the "prey" — flourishes when oxygen is low)
- $P(t)$ = PHD enzyme activity (the "predator" — requires oxygen; degrades HIF-1α)

Under stable oxygen conditions, the system reaches equilibrium. Under oscillating oxygen (intermittent hypoxia):

$$\dot{H} = \alpha H \left(1 - \frac{O_2(t)}{O_{2,\max}}\right) - \beta H P$$

$$\dot{P} = -\gamma P + \delta H P \cdot \frac{O_2(t)}{O_{2,\max}}$$

Where:
- $\alpha$: HIF-1α stabilisation rate under hypoxia
- $\beta$: PHD-mediated HIF-1α degradation rate
- $\gamma$: PHD decay rate in the absence of substrate
- $\delta$: PHD activation rate proportional to HIF-1α and oxygen
- $O_2(t)$: time-varying oxygen signal (oscillating under PE)

### Oscillation Under Intermittent Hypoxia

When $O_2(t)$ oscillates (as in preeclamptic vasospasm), the Lotka-Volterra system does not reach equilibrium. Instead, $H(t)$ and $P(t)$ oscillate with a phase relationship determined by the forcing frequency of $O_2(t)$:

- **Hypoxic phase**: $O_2 \downarrow$ → $H$ increases (prey flourishes), $P$ decreases (predator starved)
- **Reoxygenation phase**: $O_2 \uparrow$ → $P$ increases (predator feeds on accumulated prey), but also generates ROS during the predator-prey interaction
- **Repeat**: each cycle amplifies the oscillation if the forcing frequency resonates with the natural frequency of the $H$-$P$ system

The key prediction from the Lotka-Volterra model: **there exists a forcing frequency that maximises the oscillation amplitude**. If the vasospasm cycle frequency matches the natural frequency of the HIF/PHD system, the damage is maximised through resonance.

The natural period of the HIF-1α / PHD cycle is approximately 90–120 minutes based on in vitro measurements (Bagnall et al., 2014; Loenarz et al., 2011). If preeclamptic vasospasm episodes occur on a similar timescale (consistent with uterine artery Doppler patterns in severe PE — Papageorghiou et al., 2005), the resonance condition is approximately met.

### Stability Basin and Escape

The Lotka-Volterra system has a stability region in $(H, P)$ phase space. When the oscillation amplitude is small (mild hypoxic episodes), the system orbits within the stability basin — HIF-1α cycles but returns to near-baseline between episodes.

When the oscillation amplitude exceeds the stability margin (severe or frequent vasospasm), the system escapes the basin:

- HIF-1α accumulates to pathologically high levels → sustained activation of hypoxic response genes → permanent cell fate changes (maturation arrest)
- PHD overshoot during reoxygenation generates excess ROS → cumulative oxidative damage to DNA, lipid membranes, and mitochondria

This escape from the stability basin is the Lyapunov instability event described in §2: the perturbation (oscillating $O_2$) exceeds the stability margin ($\delta^{(k)}$), and the developmental trajectory is displaced to an alternative attractor (arrested development).

The molecular mechanism (Lotka-Volterra dynamics of HIF/PHD) and the system-level mechanism (Lyapunov stability margin of the developmental trajectory) are descriptions of the same event at different scales. The alignment model [5] identifies the clinical endpoint; this paper provides the dynamical systems formalism.

---

## Bifurcation Analysis

### The Developmental Bifurcation

The transition from normal development to arrested development is a **saddle-node bifurcation** (Strogatz, 2015, Chapter 3). The bifurcation parameter is the oxygen delivery rate $O_2(t)$.

For $O_2 > O_{2,\text{crit}}^{(k)}$: the normal developmental trajectory and the arrested state are separated by a saddle point. The system is in the basin of the normal attractor.

For $O_2 < O_{2,\text{crit}}^{(k)}$: the saddle point collides with the normal attractor and annihilates it. Only the arrested attractor remains. The system transitions abruptly.

This is the Prigogine phase transition (§4.3) described in bifurcation-theoretic terms. The critical oxygen level $O_{2,\text{crit}}^{(k)}$ is the bifurcation point — the parameter value at which the qualitative dynamics change.

### Hysteresis

Saddle-node bifurcations exhibit hysteresis: the forward transition (normal → arrested) occurs at a lower parameter value than the reverse transition (arrested → normal) would require (Strogatz, 2015, Chapter 3).

In developmental terms: **the oxygen level required to resume normal development after arrest is higher than the level at which arrest occurred.** Once a preOL has arrested, simply restoring oxygen to the pre-arrest level may not restart maturation — a higher oxygen level, or a different molecular intervention, may be required.

This is consistent with the clinical observation that delivery of the fetus from the hypoxic environment (removing from the degraded channel — see Shannon model [6]) does not reverse developmental injury already sustained. The system is in the arrested attractor. Restoring oxygen removes the perturbation but does not restore the original attractor, which was annihilated at the bifurcation.

### The Fixed Endowment as Irreversible Bifurcation

For systems with a fixed closure point (nephrons close at ~36 weeks, cardiomyocyte proliferation ceases perinatally), the bifurcation is not just hysteretic but **irreversible**:

$$\text{After } t_{\text{close}}^{(k)}: \text{ the arrested attractor becomes the only attractor, permanently}$$

The developmental window closes regardless of subsequent oxygen availability. The system can no longer return to the normal trajectory because the normal trajectory itself ceases to exist. There is no attractor to return to.

This is the dynamical systems formulation of the Fixed Endowment Principle [5, §2.4.1]: when the developmental programme closes, the current state becomes permanent. A reduced nephron count at 36 weeks is the final state. A reduced cardiomyocyte endowment at birth is the final state.

---

## Quantitative Framework

### The Lyapunov Function

For organ system $k$, define a Lyapunov function $V^{(k)}(e(t))$ where $e(t) = x(t) - x_{\text{ref}}(t)$ is the deviation from the normal trajectory:

$$V^{(k)}(e) = \frac{1}{2} e^T Q^{(k)}(t) \, e$$

where $Q^{(k)}(t)$ is a positive-definite matrix that reflects the relative importance and coupling of the state variables at gestational time $t$.

The stability condition requires:

$$\dot{V}^{(k)} = e^T Q^{(k)} \dot{e} + \frac{1}{2} e^T \dot{Q}^{(k)} e < 0$$

for all $e$ within the stability basin. The stability margin $\delta^{(k)}(t)$ is the maximum $\|e\|$ for which $\dot{V}^{(k)} < 0$ given the current perturbation level.

### The Perturbation Input

The oxygen perturbation enters the dynamics as:

$$\dot{e} = A^{(k)}(t) \, e + B^{(k)}(t) \, \Delta O_2(t)$$

where $A^{(k)}(t)$ is the (time-varying) system dynamics matrix and $\Delta O_2(t) = O_2(t) - O_{2,\text{ref}}(t)$ is the oxygen deviation from normal.

Under preeclamptic conditions:

$$\Delta O_2(t) = -\bar{d} + a(t) \sin(\omega t + \phi(t))$$

where $\bar{d}$ is the mean oxygen deficit (chronic placental insufficiency component), $a(t)$ is the vasospasm amplitude (non-stationary), $\omega$ is the vasospasm frequency, and $\phi(t)$ is a phase noise term.

The stability analysis reduces to: given the perturbation $\Delta O_2(t)$, does the deviation $e(t)$ remain within the stability basin defined by $V^{(k)}(e) < V_{\text{crit}}^{(k)}(t)$?

### What This Framework Requires

The quantitative framework is specified but not parameterised. Parameterisation requires:

1. **Normal trajectory data**: histological studies of normal fetal organ development at each gestational week, giving $x_{\text{ref}}^{(k)}(t)$ for each system
2. **Perturbation measurements**: continuous fetal $SpO_2$ monitoring in preeclamptic pregnancies, giving $O_2(t)$
3. **Outcome correlations**: linking measured $O_2(t)$ profiles with system-specific developmental outcomes, giving the relationship between perturbation and deviation

This data does not exist in unified form. The framework identifies what needs to be measured and how the measurements should be related. The measurement programme is described in [5, §7].

---

## Relationship to the Collapse Algebra

### Algebraic Mapping

| Algebraic Structure | Dynamical Systems Equivalent | Gestational Instance |
|---|---|---|
| $\omega_0$ (fixed point) | Normal developmental trajectory | Expected organ development |
| $\alpha$ (admissibility condition) | Lyapunov stability condition | $\dot{V}^{(k)} < 0$ within basin |
| Vulnerability window | Minimum stability margin period | $\delta^{(k)}(t) < \delta_{\text{crit}}$ |
| $V$ (veto) | Escape from stability basin | Development displaced to arrested attractor |
| $\mathcal{C}$ (collapse to reachable state) | Post-arrest fixed endowment | System locked at reduced state |
| $\mathcal{G}_0$ (constitution) | Saddle-node bifurcation threshold | $O_{2,\text{crit}}^{(k)}$ — cannot be negotiated |

### The Connection to the Meta-Theory

The meta-theory [4] establishes that existence is a fixed point of a contraction mapping. The fixed point is held in place by the admissibility surface $\alpha$, which defines the boundary between sustainable and unsustainable states. The veto $V$ is the process that enforces the boundary.

In the gestational model: the normal developmental trajectory is the fixed point. The Lyapunov stability margin is the admissibility surface. The saddle-node bifurcation is the veto. The same structure operates at every scale [4, §7]:

- Molecular: HIF/PHD stability basin (Lotka-Volterra)
- Cellular: cell fate bifurcation (differentiation vs arrest)
- Organ: developmental trajectory stability (Lyapunov margin)
- Organism: physiological viability (Prigogine dissipative threshold)

The theory predicts this scale-invariance. The dynamical systems framework confirms it.

---

## Boundaries and What This Paper Does Not Claim

1. **This paper does not derive the stability margins quantitatively.** The framework identifies what the stability margin is, how it varies, and what determines it — but the numerical values require empirical measurement that does not yet exist in sufficient resolution.

2. **The Lotka-Volterra model of HIF/PHD is simplified.** The actual molecular network involves dozens of interacting species (HIF-1α, HIF-2α, PHD1/2/3, VHL, FIH, p300/CBP, ARNT, etc.). The two-species model captures the qualitative dynamics — oscillation, escape, resonance — but not the full quantitative behaviour.

3. **The bifurcation analysis assumes a single bifurcation parameter ($O_2$).** In reality, glucose, inflammatory cytokines, and other metabolic factors also influence developmental trajectories. Oxygen is the dominant parameter in the preeclampsia model, but it is not the only one.

4. **Waddington's landscape is a metaphor given partial formalisation here.** A complete formalisation would require the full potential function of the developmental dynamics, which is not available for any organ system if viewed in full complexity.

5. **The resonance prediction (§5.2) is speculative.** While the natural period of HIF-1α cycling and the timescale of vasospasm episodes are both approximately 90–120 minutes, the resonance hypothesis has not been tested experimentally. This is a prediction of the model, not a confirmed result.

---

## References {-}

- ACOG Practice Bulletin No. 222. (2020). "Gestational Hypertension and Preeclampsia." *Obstet Gynecol*, 135(6): e237–e260.
- Armstrong, E., et al. (1995). "The ontogeny of human gyrification." *Cereb Cortex*, 5(1): 56–63.
- Back, S. A., et al. (2001). "Late oligodendrocyte progenitors coincide with the developmental window of vulnerability for human perinatal white matter injury." *J Neurosci*, 21(4): 1302–1312.
- Back, S. A. (2017). "White matter injury in the preterm infant: pathology and mechanisms." *Acta Neuropathol*, 134(3): 331–349.
- Backes, C. H., et al. (2011). "Maternal preeclampsia and neonatal outcomes." *J Pregnancy*, 2011: 214365.
- Bagnall, J., et al. (2014). "Quantitative analysis of competitive cytokine signalling predicts tissue thresholds for the propagation of macrophage activation." *Sci Signal*, 7(334): ra59.
- Battaglia, F. C. & Meschia, G. (1986). *An Introduction to Fetal Physiology*. Academic Press.
- Botting, K. J., et al. (2018). "Early origins of heart disease: Low birth weight and determinants of cardiomyocyte endowment." *Clin Exp Pharmacol Physiol*, 39(9): 814–823.
- Chi, J. G., et al. (1977). "Gyral development of the human brain." *Ann Neurol*, 1(1): 86–93.
- Giussani, D. A. (2016). "The fetal brain sparing response to hypoxia: physiological mechanisms." *J Physiol*, 594(5): 1215–1230.
- Kinney, H. C. (2006). "The near-term (late preterm) human brain and risk for periventricular leukomalacia: a review." *Semin Perinatol*, 30(2): 81–88.
- Loenarz, C., et al. (2011). "The hypoxia-inducible transcription factor pathway regulates oxygen sensing in the simplest animal, Trichoplax adhaerens." *EMBO Rep*, 12(1): 63–70.
- Lotka, A. J. (1925). *Elements of Physical Biology*. Williams & Wilkins.
- Luyckx, V. A. & Brenner, B. M. (2005). "Low birth weight, nephron number, and kidney disease." *Kidney Int Suppl*, 97: S68–77.
- Odegård, R. A., et al. (2000). "Preeclampsia and fetal growth." *Obstet Gynecol*, 96(6): 950–955.
- Papageorghiou, A. T., et al. (2005). "Uterine artery Doppler in the prediction of preeclampsia." *Ultrasound Obstet Gynecol*, 25(2): 160–167.
- Prigogine, I. (1977). "Time, structure, and fluctuations." Nobel Lecture, December 8, 1977.
- Prigogine, I. & Stengers, I. (1984). *Order Out of Chaos: Man's New Dialogue with Nature*. Flamingo.
- Shelley, H. J. (1961). "Glycogen reserves and their changes at birth and in anoxia." *Br Med Bull*, 17(2): 137–143.
- Steegers, E. A. P., et al. (2010). "Pre-eclampsia." *Lancet*, 376(9741): 631–644.
- Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos*, 2nd ed. Westview Press.
- Sutherland, M. R., et al. (2011). "Accelerated maturation and abnormal morphology in the preterm neonatal kidney." *J Am Soc Nephrol*, 22(7): 1365–1374.
- Volterra, V. (1926). "Fluctuations in the abundance of a species considered mathematically." *Nature*, 118: 558–560.
- Waddington, C. H. (1957). *The Strategy of the Genes*. George Allen & Unwin.

**This Research Programme**

- [1] Carpenter, J. (2026). "A Formal Algebra of Collapse-Based Computation." DOI: 10.5281/zenodo.18906064
- [2] Carpenter, J. (2026). "The Collapse That Never Happens: Generative Fixed Points and the Open Problems of Grothendieck." DOI: 10.5281/zenodo.18905785
- [3] Carpenter, J. (2026). "The Condition That Dissolves: Death as the Exhaustive Veto Partition for Natural Systems." DOI: 10.5281/zenodo.18905785
- [4] Carpenter, J. (2026). "Existence as Fixed Point: A Meta-Theory of Deterministic Collapse." DOI: 10.5281/zenodo.18932890
- [5] Carpenter, J. (2026). "Gestational Impact Zones: Oxygen Deprivation × Developmental Window Alignment — The General Theory of Latent Gestational Injury." Unpublished research document.
- [6] Carpenter, J. (2026). "The Umbilical Channel: An Information-Theoretic Model of Gestational Oxygen Delivery." Unpublished research document.
