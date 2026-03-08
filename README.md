# SECS Research

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18896103.svg)](https://doi.org/10.5281/zenodo.18896103)

Public research outputs from the SECS project.

**Author:** Jay Andrew Carpenter — Independent Researcher, Sydney, Australia  
**Contact:** jay.andrew.carpenter@gmail.com  
**License:** CC-BY 4.0 International  

---

## Repository Structure

This repository contains two distinct content types with separate governance.

### `papers/` — Publications

#### Substrate Measurement Reports

Measurement reports from the SECS computational substrate. These are transferred from the private source repository via a manifest-controlled publication script with SHA-256 hash verification. They are read-only mirrors — edits happen at source.

| Paper | Description |
|-------|-------------|
| [`convergence-under-stochastic-load`](papers/convergence-under-stochastic-load/) | Convergence behaviour under stochastic input conditions |
| [`neurotrophic-capability-baseline`](papers/neurotrophic-capability-baseline/) | Baseline neurotrophic capability measurement |
| [`extended-convergence-mapping`](papers/extended-convergence-mapping/) | Extended convergence mapping across parameter space |
| [`biological-fidelity-assessment`](papers/biological-fidelity-assessment/) | Biological fidelity assessment of the substrate |
| [`ei-balance-sweep-exploration`](papers/ei-balance-sweep-exploration/) | Excitatory-inhibitory balance sweep exploration |
| [`documentation-era-shift`](papers/documentation-era-shift/) | Documentation era shift analysis |

#### Mathematical Theory

| Paper | Description | DOI |
|-------|-------------|-----|
| [`collapse-never-happens-grothendieck`](papers/collapse-never-happens-grothendieck/) | Generative fixed points and the open problems of Grothendieck — connects SECS Collapse Algebra to seven open mathematical frontiers | [10.5281/zenodo.18905785](https://doi.org/10.5281/zenodo.18905785) |

The following paper is published on Zenodo as a standalone deposit:

| Paper | Description | DOI |
|-------|-------------|-----|
| A Formal Algebra of Collapse-Based Computation | Complete algebraic framework: collapse operator, admissibility, veto partition, identity extinction, governance filtration, and the Collapse Completeness Theorem | [10.5281/zenodo.18906064](https://doi.org/10.5281/zenodo.18906064) |

### `biological-research/` — Perinatal Oxygen-Timing Research

A **41-document** biological research corpus investigating gestational oxygen-demand timing, HIF-1α counter-regulation, and developmental vulnerability windows. Includes:

- **11 synthesis papers** — 10 published on [Zenodo](https://doi.org/10.5281/zenodo.18896103) (DOI: 10.5281/zenodo.18896103), March 2026. Paper 10 (NR3C1/HPA convergence) is repo-only.
- **22 foundational research documents** covering molecular pathways, clinical evidence, neurodevelopmental mapping, and epidemiology
- **7 post-publication extension tracks** covering paternal epigenetics, colostrum as personalised repair, environmental exposures, immune activation, neonatal oxygen management, cascade trigger mechanisms, and PE as paternal compatibility signal
- **2 narrative documents** tracing the research programme origins

See [`biological-research/README.md`](biological-research/README.md) for the full description, file index, and testable predictions.

---

## Content Governance

| Directory | Content | Governance | Transfer |
|-----------|---------|------------|----------|
| `papers/` | Substrate measurement reports + mathematical theory | Publication mirror protocol (manifest, hash-verified) / Author-managed | Automated script / Direct |
| `biological-research/` | Perinatal biology / HIF / OPC research | Author-managed (direct commit) | Direct |

These two content types are independent. The publication script does not touch `biological-research/`. The biological research is not derived from the substrate.

---

## Citation

> Carpenter, J. A. (2026). *Gestational Oxygen-Timing Theory: Synthesis Papers on HIF-1α-Mediated Developmental Injury, Myelination, and Multi-System Outcomes* (1.2). Zenodo. https://doi.org/10.5281/zenodo.18896103

---

*This repository is part of the SECS project.*
