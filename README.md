# SECS Research

Public research outputs from the SECS project.

**Author:** Jay Andrew Carpenter — Independent Researcher, Sydney, Australia  
**Contact:** jay.andrew.carpenter@gmail.com  
**License:** CC-BY 4.0 International  

---

## Repository Structure

This repository contains two distinct content types with separate governance.

### `papers/` — Substrate Publications

Measurement reports from the SECS computational substrate. These are transferred from the private source repository via a manifest-controlled publication script with SHA-256 hash verification. They are read-only mirrors — edits happen at source.

| Paper | Description |
|-------|-------------|
| [`convergence-under-stochastic-load`](papers/convergence-under-stochastic-load/) | Convergence behaviour under stochastic input conditions |
| [`neurotrophic-capability-baseline`](papers/neurotrophic-capability-baseline/) | Baseline neurotrophic capability measurement |
| [`extended-convergence-mapping`](papers/extended-convergence-mapping/) | Extended convergence mapping across parameter space |
| [`biological-fidelity-assessment`](papers/biological-fidelity-assessment/) | Biological fidelity assessment of the substrate |
| [`ei-balance-sweep-exploration`](papers/ei-balance-sweep-exploration/) | Excitatory-inhibitory balance sweep exploration |
| [`documentation-era-shift`](papers/documentation-era-shift/) | Documentation era shift analysis |

### `biological-research/` — Perinatal Oxygen-Timing Research

A **37-document** biological research corpus investigating gestational oxygen-demand timing, HIF-1α counter-regulation, and developmental vulnerability windows. Includes:

- **9 synthesis papers** (Papers 1–8 submitted to medRxiv March 2026, rejected as out of scope; Paper 9 completed March 2026)
- **22 foundational research documents** covering molecular pathways, clinical evidence, neurodevelopmental mapping, and epidemiology
- **5 post-publication extension tracks** covering paternal epigenetics, environmental exposures, immune activation, neonatal oxygen management, and cascade trigger mechanisms
- **2 narrative documents** tracing the research programme origins

See [`biological-research/README.md`](biological-research/README.md) for the full description, file index, and testable predictions.

---

## Content Governance

| Directory | Content | Governance | Transfer |
|-----------|---------|------------|----------|
| `papers/` | Substrate measurement reports | Publication mirror protocol (manifest, hash-verified) | Automated script |
| `biological-research/` | Perinatal biology / HIF / OPC research | Author-managed (direct commit) | Direct |

These two content types are independent. The publication script does not touch `biological-research/`. The biological research is not derived from the substrate.

---

## Citation

> Carpenter, J. A. (2026). *Gestational Oxygen-Timing Alignment: A Theoretical Framework Linking Placental Hypoxia Timing to OPC Maturation Arrest and Region-Specific Myelination Deficits in Autism Spectrum Disorder.* medRxiv preprint. GitHub repository: https://github.com/JustNothingJay/SECS_Research

---

*This repository is part of the SECS project.*
