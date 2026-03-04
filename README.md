# SECS Research

Public research outputs from the SECS project.

---

## Repository Structure

This repository contains two distinct content types with separate governance.

### `papers/` — Substrate Publications

Measurement reports from the SECS computational substrate. These are transferred from the private source repository via a manifest-controlled publication script with SHA-256 hash verification. They are read-only mirrors — edits happen at source.

### `biological-research/` — Perinatal Oxygen-Timing Research

A 22-file biological research corpus investigating gestational oxygen-demand timing, HIF-1α counter-regulation, and developmental vulnerability windows. This research is managed directly by the author and is not subject to the substrate's governance model.

See [`biological-research/README.md`](biological-research/README.md) for the full description, file index, and testable predictions.

---

## Content Governance

| Directory | Content | Governance | Transfer |
|-----------|---------|------------|----------|
| `papers/` | Substrate measurement reports | Publication mirror protocol (manifest, hash-verified) | Automated script |
| `biological-research/` | Perinatal biology / HIF / OPC research | Author-managed (direct commit) | Direct |

These two content types are independent. The publication script does not touch `biological-research/`. The biological research is not derived from the substrate.

---

*This repository is part of the SECS project.*
