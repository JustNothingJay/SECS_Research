#!/usr/bin/env python3
"""
Compactification Hierarchy — Tower-Weighted 7-Volume

The 11-tetrahedron Möbius kaleidocycle has equal edges throughout.
All compact radii are therefore equal.

The tower polynomial α⁻¹ + Sα = 4π³ + π² + π encodes the
dimensional structure. The coefficients (4, 1, 1) and the S
denominator (24 = 4!) are the numbers.

Does the hierarchy emerge from the polynomial structure
applied to the 7 compactified dimensions?
"""

import math
from itertools import combinations_with_replacement
from collections import Counter

from mobius_units import (
    alpha_inv, alpha, l_P, m_P, m_p, G, c, hbar, e_charge,
)
from mobius_constant import Pi, Sqrt2, Sqrt3

pi = float(Pi)

# ═══════════════════════════════════════════════════════════════
# Tower fundamentals
# ═══════════════════════════════════════════════════════════════

S = 1/math.factorial(4) + 3/math.factorial(8)
K = 4*pi**3 + pi**2 + pi

def tower_eigenvalue(level):
    rhs = K / (pi**level)
    d = rhs**2 - 4*S
    if d < 0:
        return None
    return (rhs + math.sqrt(d)) / 2

L = [tower_eigenvalue(k) for k in range(5)]

# Force hierarchy target
F_ratio = alpha * hbar * c / (G * m_p**2)
hierarchy_planck = (m_P / m_p) ** 2
target_log = math.log10(F_ratio)


# ═══════════════════════════════════════════════════════════════
# §1  The target
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§1  The Hierarchy Target")
print("=" * 70)
print(f"  F_em / F_grav (protons):     {F_ratio:.6e}")
print(f"  (m_P / m_p)²:               {hierarchy_planck:.6e}")
print(f"  log₁₀(F_em/F_grav):         {target_log:.6f}")
print(f"  log₁₀((m_P/m_p)²):         {math.log10(hierarchy_planck):.6f}")
print()
print(f"  Required equal radius (7 dims): r = {F_ratio**(1/7):.6f} l_P")
print(f"  log₁₀(r):                       {math.log10(F_ratio**(1/7)):.6f}")
print()


# ═══════════════════════════════════════════════════════════════
# §2  Tower eigenvalues and polynomial terms
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§2  Tower Structure")
print("=" * 70)
print(f"  K = 4π³ + π² + π = {K:.10f}")
print(f"  S = 1/4! + 3!!/8! = {S:.15f}")
print(f"  1/S = {1/S:.6f}")
print(f"  4! = 24")
print()

print(f"  Polynomial terms:")
print(f"    4π³  = {4*pi**3:.10f}")
print(f"    π²   = {pi**2:.10f}")
print(f"    π    = {pi:.10f}")
print(f"    1    = 1.0")
print(f"    1/24 = {1/24:.10f}")
print()

for k in range(5):
    rhs_k = K / pi**k
    print(f"  Level {k}: K/π^{k} = {rhs_k:.6f}  →  eigenvalue = {L[k]:.6f}")
print()


# ═══════════════════════════════════════════════════════════════
# §3  Equal-radius candidates (all 7 at same r)
# ═══════════════════════════════════════════════════════════════

r_needed = F_ratio**(1/7)

candidates = {
    "1 (Planck)":               1.0,
    "π":                         pi,
    "π²":                        pi**2,
    "4π³":                       4*pi**3,
    "K = 4π³+π²+π":             K,
    "α⁻¹ (L0)":                 L[0],
    "β⁻¹ (L1)":                 L[1],
    "γ⁻¹ (L2)":                 L[2],
    "δ⁻¹ (L3)":                 L[3],
    "ε⁻¹ (L4)":                 L[4],
    "24":                        24.0,
    "1/S":                       1/S,
    "α⁻¹ / π":                  L[0] / pi,
    "m_P / m_p":                 m_P / m_p,
    "√(m_P/m_p)":               math.sqrt(m_P / m_p),
    "R_ring/l_P (kaleidocycle)": (math.sqrt(2)/2) / (2*math.sin(pi/11)),
}

print("=" * 70)
print("§3  Equal-Radius Candidates: V₇ = r⁷")
print("=" * 70)
print(f"  Target log₁₀ = {target_log:.4f},  required r = {r_needed:.4f}")
print()
print(f"  {'Candidate':<30s} {'r':>12s} {'log₁₀(r⁷)':>12s} {'Δ':>10s}")
print(f"  {'-'*30} {'-'*12} {'-'*12} {'-'*10}")

for label, r in sorted(candidates.items(),
        key=lambda x: abs(7*math.log10(x[1]) - target_log) if x[1] > 0 else 999):
    if r > 0:
        log7 = 7 * math.log10(r)
        delta = log7 - target_log
        print(f"  {label:<30s} {r:>12.4f} {log7:>12.4f} {delta:>+10.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# §4  The (24, 1, 4, 1) structure
# ═══════════════════════════════════════════════════════════════
#
# The tower equation has two halves:
#   LHS:  α⁻¹  +  Sα        (eigenvalue  +  correction)
#   RHS:  4π³  +  π²  +  π   (polynomial)
#
# The full set of integers:  (4, 1, 1)  from the polynomial
#                            24 = 4!    from S = 1/24 + ...
#
# User: "24, 1, 4, 1" — the correction denominator first.
# "Only half the equation" — S is only the LHS correction.
# The other half IS the polynomial.
#
# 4 + 1 + 1 + 1 = 7.  Exactly the compact dimensions.
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§4  The (24, 1, 4, 1) Decomposition")
print("=" * 70)
print()
print("  Polynomial:  4·π³  +  1·π²  +  1·π")
print("  Correction:  S = 1/24 + 3!!/8!  (24 = 4!)")
print()
print("  Coefficients: (4, 1, 1) from polynomial + 1 from S = (4, 1, 1, 1)")
print("  Sum: 4 + 1 + 1 + 1 = 7  ← the compact dimensions")
print()

# Interpretation: the polynomial tells you HOW the 7 dimensions group.
# 4 dimensions share one scale.
# 1 dimension at a second scale.
# 1 dimension at a third scale.
# 1 dimension from the S correction at a fourth scale.
#
# The SCALES are the power of π associated with each coefficient:
#   4 dims at scale π³   (from 4π³ term)
#   1 dim  at scale π²   (from π² term)
#   1 dim  at scale π    (from π term)
#   1 dim  at scale 1/24 or 24 or S-related

# Group A: scales are the π-powers themselves as radii
print("  Group A: radii = π-powers")
print("    4 dims × π³, 1 dim × π², 1 dim × π, 1 dim × 1")
v7_A = (pi**3)**4 * (pi**2)**1 * (pi)**1 * (1)**1
print(f"    V₇ = (π³)⁴ × (π²)¹ × (π)¹ × (1)¹ = π^{4*3+2+1} = π^15")
print(f"    V₇ = {v7_A:.6e}")
print(f"    log₁₀ = {math.log10(v7_A):.4f},  Δ = {math.log10(v7_A) - target_log:+.4f}")
print()

# Group B: radii are coefficients × π-powers
print("  Group B: radii = coefficient × π^power")
print("    4 dims × 4π³, 1 dim × 1·π², 1 dim × 1·π, 1 dim × (1/24)")
v7_B = (4*pi**3)**4 * (pi**2)**1 * (pi)**1 * (1/24)**1
print(f"    V₇ = {v7_B:.6e}")
print(f"    log₁₀ = {math.log10(v7_B):.4f},  Δ = {math.log10(v7_B) - target_log:+.4f}")
print()

# Group C: like B but 7th dim at 24 (not 1/24)
print("  Group C: radii = coefficient × π^power, 7th dim at 24")
print("    4 dims × 4π³, 1 dim × π², 1 dim × π, 1 dim × 24")
v7_C = (4*pi**3)**4 * (pi**2)**1 * (pi)**1 * 24
print(f"    V₇ = {v7_C:.6e}")
print(f"    log₁₀ = {math.log10(v7_C):.4f},  Δ = {math.log10(v7_C) - target_log:+.4f}")
print()

# Group D: the terms themselves are not radii but CONTRIBUTE to V₇
# V₇ = (4π³ + π² + π) evaluated as a product decomposition
# K = 4π³ + π² + π ≈ α⁻¹
# The 7 radii are EQUAL (kaleidocycle), all = K^(1/1) = α⁻¹
# But wait — what if the exponents in K encode the volume?
# K = 4π³ + π² + π = π(4π² + π + 1)
# The product form: K = π × (4π² + π + 1) = π × L1_poly
print("  Group D: K as a product factorisation")
print(f"    K = π × (4π² + π + 1)")
print(f"    = {pi:.6f} × {4*pi**2 + pi + 1:.6f}")
print(f"    = {pi * (4*pi**2 + pi + 1):.6f}")
print()

# Group E: eigenvalue products
print("  Group E: All eigenvalue products for 7 dims")
eigenvalue_products = {
    "L0⁴ × L1 × L2 × L3":           L[0]**4 * L[1] * L[2] * L[3],
    "L0 × L1⁴ × L2 × L3":           L[0] * L[1]**4 * L[2] * L[3],
    "L0 × L1 × L2⁴ × L3":           L[0] * L[1] * L[2]**4 * L[3],
    "L0 × L1 × L2 × L3⁴":           L[0] * L[1] * L[2] * L[3]**4,
    "L0⁴ × L1 × L2 × L4":           L[0]**4 * L[1] * L[2] * L[4],
    "L0 × L1 × L2 × L3 × L4³":     L[0] * L[1] * L[2] * L[3] * L[4]**3,
    "∏(L0..L4) × L0 × L1":          L[0]*L[1]*L[2]*L[3]*L[4] * L[0]*L[1],
    "∏(L0..L4) × L2 × L3":          L[0]*L[1]*L[2]*L[3]*L[4] * L[2]*L[3],
    "L0⁵ × L1²":                     L[0]**5 * L[1]**2,
    "L0² × L1² × L2² × L3":         L[0]**2 * L[1]**2 * L[2]**2 * L[3],
    "(∏L0..L4)^(7/5)":              (L[0]*L[1]*L[2]*L[3]*L[4])**(7/5),
}

print(f"  {'Product':<35s} {'Value':>14s} {'log₁₀':>10s} {'Δ':>10s}")
print(f"  {'-'*35} {'-'*14} {'-'*10} {'-'*10}")
for label, val in sorted(eigenvalue_products.items(),
        key=lambda x: abs(math.log10(x[1]) - target_log)):
    log_val = math.log10(val)
    delta = log_val - target_log
    print(f"  {label:<35s} {val:>14.4e} {log_val:>10.4f} {delta:>+10.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# §5  Exhaustive search: 7 radii from tower levels
# ═══════════════════════════════════════════════════════════════
#
# Each of the 7 compact dimensions gets a radius = K/π^k
# where k ∈ {0, 1, 2, 3, 4} (the 5 tower levels).
# Which assignment of 7 levels best matches the hierarchy?
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§5  Exhaustive Search: 7 radii from {K/π⁰, K/π¹, ..., K/π⁴}")
print("=" * 70)
print()

rhs = [K / pi**k for k in range(5)]

best_delta = 999
best_combo = None
best_product = 0

for combo in combinations_with_replacement(range(5), 7):
    product = 1
    for k in combo:
        product *= rhs[k]
    log_p = math.log10(product)
    delta = abs(log_p - target_log)
    if delta < best_delta:
        best_delta = delta
        best_combo = combo
        best_product = product

counts = Counter(best_combo)
print(f"  Best partition: {best_combo}")
print(f"  Product = {best_product:.6e}")
print(f"  log₁₀  = {math.log10(best_product):.6f}")
print(f"  Target  = {target_log:.6f}")
print(f"  Δ       = {math.log10(best_product) - target_log:+.6f}")
print()
for k, n in sorted(counts.items()):
    print(f"    {n} dim(s) at Level {k}: K/π^{k} = {rhs[k]:.4f}")
print()

# Also check top-5 best
print("  Top 5 closest partitions:")
results = []
for combo in combinations_with_replacement(range(5), 7):
    product = 1
    for k in combo:
        product *= rhs[k]
    log_p = math.log10(product)
    delta = log_p - target_log
    results.append((abs(delta), combo, product, delta))
results.sort()
for _, combo, prod, delta in results[:5]:
    print(f"    {combo}  log₁₀ = {math.log10(prod):.4f}  Δ = {delta:+.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# §6  The polynomial exponent sum
# ═══════════════════════════════════════════════════════════════
#
# If the 7 radii decompose as (4, 1, 1, 1) with scales
# (π³, π², π, 1), then V₇ = π^(4×3 + 1×2 + 1×1 + 1×0)
#                           = π^(12 + 2 + 1 + 0) = π^15
#
# What if the scales aren't π-powers but eigenvalue-powers?
# The tower descends by factors of π:
#   L0 ≈ K,  L1 ≈ K/π,  L2 ≈ K/π²,  L3 ≈ K/π³,  L4 ≈ K/π⁴
#
# So (4, 1, 1, 1) dims at L3, L2, L1, L0 scales gives:
#   V₇ ≈ L3⁴ × L2 × L1 × L0
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§6  The Polynomial Exponent Sum")
print("=" * 70)
print()

# The polynomial is 4π³ + π² + π.
# Total π-power if we "multiply out" the structure:
# 4 copies of π³ × 1 copy of π² × 1 copy of π × 1 at π⁰
# ∏ = π^(3×4 + 2×1 + 1×1 + 0×1) = π^15

total_pi_power = 3*4 + 2*1 + 1*1 + 0*1  # = 15
print(f"  (4,1,1,1) decomposition: exponent sum = 3×4 + 2×1 + 1×1 + 0×1 = {total_pi_power}")
print(f"  V₇ = π^{total_pi_power} = {pi**total_pi_power:.6e}")
print(f"  log₁₀(π^{total_pi_power}) = {total_pi_power * math.log10(pi):.6f}")
print(f"  Target = {target_log:.6f}")
print(f"  Δ = {total_pi_power * math.log10(pi) - target_log:+.6f}")
print()

# What total exponent of π is needed?
p_needed = target_log / math.log10(pi)
print(f"  Required π-exponent: {p_needed:.6f}")
print(f"  (i.e., V₇ = π^{p_needed:.2f} to match hierarchy)")
print()

# If the (4,1,1,1) structure is correct but the BASE is K, not π:
# V₇ = K^(4×3 + 2 + 1 + 0) = K^15? No...
# Or: V₇ = (4π³)^4 × (π²)^1 × (π)^1 × (1/S)^1
# Let's compute all interpretations

print("  Systematic (4,1,1,1) interpretations:")
print()

interpretations = {
    "π-powers only: π^(4×3+2+1+0) = π^15": pi**15,
    "K-powers: K^(4×3+2+1+0) = K^15":      K**15,
    "Terms as radii: (4π³)⁴·(π²)¹·π¹·1¹":  (4*pi**3)**4 * pi**2 * pi * 1,
    "Terms: (4π³)⁴·(π²)¹·π¹·(1/24)¹":      (4*pi**3)**4 * pi**2 * pi * (1/24),
    "Terms: (4π³)⁴·(π²)¹·π¹·24¹":          (4*pi**3)**4 * pi**2 * pi * 24,
    "Terms: (4π³)⁴·(π²)¹·π¹·S¹":           (4*pi**3)**4 * pi**2 * pi * S,
    "Terms: (4π³)⁴·(π²)¹·π¹·(1/S)¹":       (4*pi**3)**4 * pi**2 * pi * (1/S),
    "L-vals: L3⁴ × L2 × L1 × L0":         L[3]**4 * L[2] * L[1] * L[0],
    "L-vals: L0⁴ × L1 × L2 × L3":         L[0]**4 * L[1] * L[2] * L[3],
    "L-vals: L1⁴ × L0 × L2 × L3":         L[1]**4 * L[0] * L[2] * L[3],
    "L-vals: L1⁴ × L2 × L3 × L4":         L[1]**4 * L[2] * L[3] * L[4],
    "Mixed: (4π³)⁴ × β⁻¹ × γ⁻¹ × δ⁻¹":   (4*pi**3)**4 * L[1] * L[2] * L[3],
    "Mixed: (4π³)⁴ × π² × π × (1/S)":     (4*pi**3)**4 * pi**2 * pi * (1/S),
    "All-K: K⁴ × (K/π) × (K/π²) × (K/π³)": K**4 * (K/pi) * (K/pi**2) * (K/pi**3),
}

sorted_interps = sorted(interpretations.items(),
    key=lambda x: abs(math.log10(x[1]) - target_log) if x[1] > 0 else 999)

for label, val in sorted_interps:
    if val > 0:
        log_v = math.log10(val)
        delta = log_v - target_log
        marker = " ◄◄◄" if abs(delta) < 1.0 else ""
        print(f"  {label}")
        print(f"    V₇ = {val:.6e},  log₁₀ = {log_v:.4f},  Δ = {delta:+.4f}{marker}")
        print()


# ═══════════════════════════════════════════════════════════════
# §7  The equal-edge identity
# ═══════════════════════════════════════════════════════════════
#
# The kaleidocycle enforces equal edges.
# HOWEVER: "equal edge length" in the compactification does NOT
# mean "equal radius." Each dimension's extent is the edge
# LENGTH PROJECTED onto that dimension's axis.
#
# For a regular tetrahedron with edge a, the projections onto
# orthogonal axes are NOT all equal — the tetrahedron has 6 edges
# projecting onto 3 directions in 3D. In 7D compactification,
# the 11 edges of the chain project onto 7 compact + 4 large axes.
#
# The projection of a regular tet's edge onto its principal axes
# involves the tetrahedral geometry: a_proj = a × direction cosines.
#
# For a chain of 11 tets, each new tet is rotated relative to the
# last by the kaleidocycle dihedral. The effective compactification
# radius per dimension is the PRODUCT of all edge projections
# onto that dimension across the full chain.
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§7  Equal-Edge Identity — But Not Equal Projections")
print("=" * 70)
print()
print("  In 11-tet chain: 11 shared edges, each = a (equal)")
print("  4 large dims, 7 compact dims")
print("  Each edge projects onto each dim with different weights")
print()

# The kaleidocycle ring angle between adjacent tets
theta = 2 * pi / 11  # angular step around the ring
print(f"  Ring angle θ = 2π/11 = {theta:.6f} rad = {math.degrees(theta):.4f}°")
print()

# For Möbius kaleidocycle with half-twist, the dihedral angle
# between successive tetrahedra alternates. The effective
# compactification radius comes from the circumradius and
# the twist geometry.

# The key insight: in KK, each dimension's "radius" is the
# circumference divided by 2π. For the kaleidocycle ring:
R_ring = (l_P * math.sqrt(2)/2) / (2 * math.sin(pi/11))
C_ring = 2 * pi * R_ring  # circumference
r_KK = R_ring  # the KK radius for the ring dimension

print(f"  Ring circumradius R = {R_ring/l_P:.6f} l_P")
print(f"  Ring circumference = {C_ring/l_P:.6f} l_P")
print()

# But the ring exists in 3D. It sweeps out only 1 compact dimension
# (the angular direction). The other 6 compact dimensions are
# transverse to the ring — they're the INTERNAL geometry of
# each tetrahedron.
#
# For a regular tetrahedron:
# - inradius r_in = a / (2√6) ≈ 0.204 a
# - midradius r_mid = a / (2√2) ≈ 0.354 a  (edge midpoint to centre)
# - circumradius r_out = a√6/4 ≈ 0.612 a

r_in = 1 / (2*math.sqrt(6))    # in units of edge length
r_mid = 1 / (2*math.sqrt(2))
r_out = math.sqrt(6) / 4

print(f"  Tetrahedral radii (in units of edge length a):")
print(f"    Inradius (insphere):    {r_in:.6f} a")
print(f"    Midradius (midsphere):  {r_mid:.6f} a")
print(f"    Circumradius:           {r_out:.6f} a")
print()

# If 1 compact dim has the ring radius and 6 have the tet internal radius:
print("  If 1 dim = ring radius, 6 dims = tet internal radius:")
for name, r_tet in [("inradius", r_in), ("midradius", r_mid), ("circumradius", r_out)]:
    v7 = R_ring/l_P * (r_tet)**6  # mixed: ring (1 dim) × tet (6 dims), in l_P units
    log_v = math.log10(abs(v7)) if v7 > 0 else 0
    print(f"    {name}: V₇ = {R_ring/l_P:.4f} × {r_tet:.4f}⁶ = {v7:.6e} l_P⁷, log₁₀ = {log_v:.4f}, Δ = {log_v - target_log:+.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# §8  K^7 / π^n — the polynomial descent
# ═══════════════════════════════════════════════════════════════
#
# The tower descends by factors of π at each level.
# If the 7 compact dims are at tower levels k₁...k₇:
#   V₇ = ∏ (K/π^kᵢ) = K⁷ / π^(Σkᵢ)
#
# So V₇ = K⁷ / π^n where n = sum of the 7 level indices.
# The hierarchy requires:  K⁷ / π^n ≈ 1.24 × 10³⁶
# So: n = (7 log₁₀ K - 36.09) / log₁₀ π
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§8  K⁷/π^n Descent — What n Closes the Gap?")
print("=" * 70)
print()

K7 = K**7
log_K7 = math.log10(K7)
n_needed = (log_K7 - target_log) / math.log10(pi)

print(f"  K⁷ = {K7:.6e}")
print(f"  log₁₀(K⁷) = {log_K7:.6f}")
print(f"  Target log₁₀ = {target_log:.6f}")
print(f"  Excess = {log_K7 - target_log:.6f}")
print()
print(f"  Need: K⁷ / π^n = hierarchy")
print(f"  So:   n = (log₁₀ K⁷ - log₁₀ hierarchy) / log₁₀ π")
print(f"        n = ({log_K7:.4f} - {target_log:.4f}) / {math.log10(pi):.4f}")
print(f"        n = {n_needed:.6f}")
print()

# Check n = integers near the solution
print(f"  Integer checks:")
for n_test in range(max(0, int(n_needed) - 3), int(n_needed) + 4):
    val = K7 / pi**n_test
    log_val = math.log10(val)
    delta = log_val - target_log
    marker = " ◄" if abs(delta) < 0.5 else ""
    print(f"    n = {n_test:2d}:  K⁷/π^{n_test:2d} = {val:.4e},  log₁₀ = {log_val:.4f},  Δ = {delta:+.4f}{marker}")
print()

# What partition gives n_needed (if integer)?
n_int = round(n_needed)
mean_level = n_int / 7
print(f"  Closest integer n = {n_int}")
print(f"  Mean level index = n/7 = {n_int}/7 = {n_int/7:.4f}")
print(f"  This corresponds to 7 dimensions each at ≈ Level {n_int/7:.1f}")
print()

# What partitions of n_int into 7 parts (each 0-4) exist?
print(f"  Partitions of {n_int} into 7 parts (each 0–4):")
count = 0
for combo in combinations_with_replacement(range(5), 7):
    if sum(combo) == n_int:
        product = 1
        for k in combo:
            product *= rhs[k]
        log_p = math.log10(product)
        delta = log_p - target_log
        counts_c = Counter(combo)
        desc = ", ".join(f"{n}×L{k}" for k, n in sorted(counts_c.items()))
        print(f"    {combo}  [{desc}]  log₁₀ = {log_p:.4f}  Δ = {delta:+.4f}")
        count += 1
        if count > 10:
            print(f"    ... (more partitions exist)")
            break
print()


# ═══════════════════════════════════════════════════════════════
# §9  The 11D ↔ 4D Planck relation
# ═══════════════════════════════════════════════════════════════
#
# The real KK relation is:
#   m_P² = M₁₁⁹ × V₇
# where M₁₁ is the 11D Planck mass and V₇ is in physical units.
#
# This means V₇ = m_P² / M₁₁⁹
# The hierarchy (m_P/m_p)² enters through m_P, not V₇ directly.
#
# If M₁₁ ≈ m_p (the proton mass — i.e. the fundamental scale
# IS the proton scale, not the Planck scale), then:
#   m_P² = m_p⁹ × V₇
#   V₇ = m_P² / m_p⁹ = (m_P/m_p)² × m_p⁷ / m_p⁹ × ...
#
# In Planck units (where m_P = 1):
#   1 = M₁₁⁹ × V₇(Planck)
#   V₇(Planck) = 1/M₁₁⁹
#
# But that makes V₇ huge if M₁₁ is small (in Planck units).
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§9  The 11D Planck Relation")
print("=" * 70)
print()

# Standard KK: G₄ = G₁₁ / V₇ (V₇ in physical length^7 units)
# In natural units: l_P² = l₁₁⁹ / V₇
# So V₇ / l₁₁⁷ = (l₁₁/l_P)² × l₁₁⁷ / l₁₁⁷ ... 

# More carefully:
# G₄ = G₁₁ / V₇
# l_P^(D-2) = G_D in D dims (in ℏ=c=1 units, with appropriate powers)
# 4D: G₄ ∝ l_P²
# 11D: G₁₁ ∝ l₁₁⁹  
# So: l_P² = l₁₁⁹ / V₇
# If V₇ = R⁷ (all radii equal):
#   l_P² = l₁₁⁹ / R⁷
#   (R/l₁₁)⁷ = l₁₁² / l_P² = (l₁₁/l_P)²

# If l₁₁ = l_P (the 11D Planck length equals 4D Planck length):
#   R⁷ = l_P⁹ / l_P² = l_P⁷ → R = l_P. Trivial. No hierarchy.
# So l₁₁ ≠ l_P.

# If l₁₁ = α × l_P (the 11D fundamental length is α times the 4D Planck):
# This is the ADD scenario (Arkani-Hamed, Dimopoulos, Dvali)
# where the fundamental scale is LOWER, not higher.

print("  KK relation: l_P² = l₁₁⁹ / V₇ = l₁₁⁹ / R⁷ (equal radii R)")
print("  → (R/l₁₁)⁷ = (l₁₁/l_P)²")
print()

# If the fundamental scale is the proton mass scale:
# m_fund = m_p, l_fund = ℏ/(m_p c)
l_proton = hbar / (m_p * c)
print(f"  Proton Compton wavelength: l_p = {l_proton:.6e} m")
print(f"  Planck length:             l_P = {l_P:.6e} m")
print(f"  l_proton / l_P = {l_proton/l_P:.6e}")
print(f"  (l_proton/l_P)² = {(l_proton/l_P)**2:.6e}")
print(f"  (l_proton/l_P)^(2/7) = {(l_proton/l_P)**(2/7):.6e}")
print()

# If l₁₁ = l_proton (fundamental scale = proton scale):
# (R/l₁₁)⁷ = (l₁₁/l_P)² = (l_proton/l_P)²
# R = l₁₁ × (l₁₁/l_P)^(2/7)
# R = l_proton × (l_proton/l_P)^(2/7)
R_compact = l_proton * (l_proton / l_P)**(2/7)
print(f"  If fundamental scale = proton mass:")
print(f"    R = l_proton × (l_proton/l_P)^(2/7)")
print(f"    R = {R_compact:.6e} m")
print(f"    R / l_P = {R_compact/l_P:.6e}")
print(f"    R / l_proton = {R_compact/l_proton:.6e}")
print()

# Alternatively, what if the TOWER sets the fundamental scale?
# The tower equation gives α⁻¹ ≈ K = 4π³ + π² + π
# l_tower = α⁻¹ × l_P = K × l_P
l_tower = K * l_P
print(f"  If fundamental scale = α⁻¹ × l_P:")
print(f"    l_tower = {l_tower:.6e} m")
print(f"    (l_tower/l_P)² = K² = {K**2:.6f}")
R_tower = l_tower * (l_tower/l_P)**(2/7)
print(f"    R = l_tower × K^(2/7) = {R_tower:.6e} m")
print(f"    R / l_P = {R_tower/l_P:.6f}")
print(f"    R⁷ / l_P⁷ = {(R_tower/l_P)**7:.6e}")
print(f"    log₁₀(R⁷/l_P⁷) = {math.log10((R_tower/l_P)**7):.4f}")
print(f"    Target = {target_log:.4f}")
print(f"    Δ = {math.log10((R_tower/l_P)**7) - target_log:+.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# §10  SUMMARY
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("§10  SUMMARY")
print("=" * 70)
print()
print(f"  Hierarchy target:  F_em/F_grav = {F_ratio:.4e}  (log₁₀ = {target_log:.4f})")
print(f"  3D cavity volume:  1.032 l_P³  (from __kaleidocycle_volume.py)")
print()
print(f"  Equal-radius (r⁷):")
print(f"    r = α⁻¹:  (α⁻¹)⁷ = {L[0]**7:.4e}  → log₁₀ = {7*math.log10(L[0]):.4f}  Δ = {7*math.log10(L[0]) - target_log:+.4f}")
print(f"    r = m_P/m_p: gives {(m_P/m_p)**7:.4e}  → log₁₀ = {7*math.log10(m_P/m_p):.4f}  Δ = {7*math.log10(m_P/m_p) - target_log:+.4f}")
print()
print(f"  Best tower partition (§5): levels {best_combo}")
print(f"    V₇ = {best_product:.4e}  log₁₀ = {math.log10(best_product):.4f}  Δ = {math.log10(best_product) - target_log:+.4f}")
print()
print(f"  K⁷/π^n descent (§8): n = {n_needed:.4f} ≈ {n_int}")
print(f"  Polynomial (4,1,1,1) decomposition (§6):")
print(f"    Pure π-powers: V₇ = π^15 = {pi**15:.4e}  (log₁₀ = {15*math.log10(pi):.4f}, Δ = {15*math.log10(pi) - target_log:+.4f})")

# Best from §6
print()
print(f"  Closest from §6:")
label0, val0 = sorted_interps[0]
print(f"    {label0}")
print(f"    V₇ = {val0:.4e}  log₁₀ = {math.log10(val0):.4f}  Δ = {math.log10(val0) - target_log:+.4f}")
