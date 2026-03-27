#!/usr/bin/env python3
"""
Prediction 5 — 11-tetrahedron Möbius kaleidocycle compactification volume.

Calculates:
  1. Volume of a single regular tetrahedron at Planck scale
  2. Internal (cavity) volume of an 11-chain Möbius kaleidocycle
  3. Ratio of compactification volume to Planck volume
  4. Comparison to the electromagnetic/gravitational force hierarchy

Uses: mobius-units (Planck constants, α, G)
      mobius-constant (exact π, √2, √3)
"""

import math
from mobius_units import (
    alpha_inv, alpha, l_P, m_P, m_p, m_e, G, c, hbar, e_charge, E_h,
)
from mobius_constant import Pi, Sqrt2, Sqrt3

# ═══════════════════════════════════════════════════════════════════
# §1  Single regular tetrahedron, edge = Planck length
# ═══════════════════════════════════════════════════════════════════

a = l_P  # edge length = Planck length

V_tet = (a**3 * math.sqrt(2)) / 12  # volume of regular tetrahedron
V_tet_exact = (a**3 * float(Sqrt2)) / 12  # using Möbius exact √2

print("=" * 70)
print("§1  Single Tetrahedron (edge = Planck length)")
print("=" * 70)
print(f"  Edge length (l_P):          {a:.6e} m")
print(f"  Volume (std √2):            {V_tet:.6e} m³")
print(f"  Volume (Möbius √2):         {V_tet_exact:.6e} m³")
print(f"  Planck volume (l_P³):       {a**3:.6e} m³")
print(f"  V_tet / l_P³:               {V_tet / a**3:.10f}")
print(f"   = √2/12:                   {math.sqrt(2)/12:.10f}")
print()

# ═══════════════════════════════════════════════════════════════════
# §2  11-chain Möbius kaleidocycle geometry
# ═══════════════════════════════════════════════════════════════════
#
# A kaleidocycle of n tetrahedra forms a toroidal ring.
# Each tetrahedron is linked to the next by a shared edge.
# The centres of adjacent shared edges form a regular n-gon.
#
# Edge-midpoint to edge-midpoint distance for regular tetrahedra
# sharing an edge: d = a√2/2 (the distance between midpoints of
# opposite edges of a regular tetrahedron).
#
# The n shared-edge midpoints sit on a circle of circumradius:
#   R = d / (2 sin(π/n))
#
# For n=11:
#   R = (a√2/2) / (2 sin(π/11))
# ═══════════════════════════════════════════════════════════════════

n = 11  # number of tetrahedra in the Möbius kaleidocycle

# Distance between midpoints of opposite edges of regular tetrahedron
d = a * math.sqrt(2) / 2

# Circumradius of the n-gon formed by edge midpoints
R_ring = d / (2 * math.sin(math.pi / n))

# Inradius of regular tetrahedron (radius of inscribed sphere)
r_in = a / (2 * math.sqrt(6))

# The toroidal cavity has:
#   Major radius ≈ R_ring  
#   Minor radius ≈ r_in (the inscribed sphere radius, approximating the gap)
# Torus volume = 2π² R r²
V_cavity = 2 * math.pi**2 * R_ring * r_in**2

# Total solid volume of all 11 tetrahedra
V_solid = n * V_tet

# Total enclosed volume of the torus (major radius R, minor radius = outer extent)
# The circumradius of the tetrahedron (vertex to centre) = a√6/4
r_out = a * math.sqrt(6) / 4
V_torus_outer = 2 * math.pi**2 * R_ring * r_out**2

print("=" * 70)
print(f"§2  {n}-chain Möbius Kaleidocycle Geometry")
print("=" * 70)
print(f"  n (tetrahedra):             {n}")
print(f"  Edge-midpoint spacing (d):  {d:.6e} m")
print(f"  Ring circumradius (R):      {R_ring:.6e} m")
print(f"  Inradius (r_in):            {r_in:.6e} m")
print(f"  Circumradius (r_out):       {r_out:.6e} m")
print()
print(f"  Cavity volume (torus):      {V_cavity:.6e} m³")
print(f"  Solid volume (11 tets):     {V_solid:.6e} m³")
print(f"  Outer torus volume:         {V_torus_outer:.6e} m³")
print()
print(f"  Cavity / l_P³:              {V_cavity / a**3:.6f}")
print(f"  Solid / l_P³:               {V_solid / a**3:.6f}")
print(f"  Cavity / Solid:             {V_cavity / V_solid:.6f}")
print()

# ═══════════════════════════════════════════════════════════════════
# §3  The force hierarchy
# ═══════════════════════════════════════════════════════════════════
#
# The ratio of electromagnetic to gravitational force between two
# protons:
#   F_em / F_grav = e² / (4πε₀ G m_p²)
#                 = α ℏc / (G m_p²)
#
# This is the number the compactification volume should explain:
# why gravity is ~10³⁶ weaker than electromagnetism.
# ═══════════════════════════════════════════════════════════════════

# Electromagnetic coupling at proton scale
F_ratio = alpha * hbar * c / (G * m_p**2)

# Alternative: Planck mass / proton mass squared
hierarchy_planck = (m_P / m_p) ** 2

print("=" * 70)
print("§3  Force Hierarchy")
print("=" * 70)
print(f"  α (fine structure):         {alpha:.10e}")
print(f"  α⁻¹:                       {alpha_inv:.10f}")
print(f"  G:                          {G:.6e} m³ kg⁻¹ s⁻²")
print(f"  m_p:                        {m_p:.6e} kg")
print(f"  m_P:                        {m_P:.6e} kg")
print()
print(f"  F_em / F_grav (protons):    {F_ratio:.6e}")
print(f"  (m_P / m_p)²:              {hierarchy_planck:.6e}")
print(f"  log₁₀(F_ratio):            {math.log10(F_ratio):.4f}")
print(f"  log₁₀((m_P/m_p)²):        {math.log10(hierarchy_planck):.4f}")
print()

# ═══════════════════════════════════════════════════════════════════
# §4  The connection — volume ratios and the hierarchy
# ═══════════════════════════════════════════════════════════════════
#
# If compactification volume controls the dilution of gravity
# relative to forces confined to 3+1 dimensions, then:
#
#   F_em / F_grav ∝ V_compact / V_Planck
#
# or more precisely, the gravitational coupling in 3+1 dims is:
#   G_4d ∝ G_11d / V_compact
#
# So V_compact = G_11d / G_4d ∝ (m_P / m_p)² in Planck units.
#
# Let's compute the kaleidocycle volumes in Planck units and
# see what falls out.
# ═══════════════════════════════════════════════════════════════════

# In Planck units (l_P = 1), the volumes are just the numerical coefficients
V_cavity_planck = V_cavity / l_P**3
V_solid_planck = V_solid / l_P**3
V_outer_planck = V_torus_outer / l_P**3

# The void fraction of a tetrahedron (from 2026q)
void_frac = 1 - math.pi * math.sqrt(3) / 18  # ≈ 0.6977

# Total kaleidocycle volume (solid + cavity) in Planck units  
V_total_planck = V_outer_planck

print("=" * 70)
print("§4  Volume Ratios vs Force Hierarchy")
print("=" * 70)
print(f"  Cavity volume (Planck units):     {V_cavity_planck:.10f}")
print(f"  Solid volume (Planck units):      {V_solid_planck:.10f}")
print(f"  Outer torus volume (Planck):      {V_outer_planck:.10f}")
print(f"  Tetrahedral void fraction:        {void_frac:.10f}")
print()

# Key dimensionless numbers from the kaleidocycle
R_over_a = R_ring / a
print(f"  R_ring / l_P:                     {R_over_a:.10f}")
print(f"  R_ring / l_P × α⁻¹:              {R_over_a * alpha_inv:.6f}")
print()

# What power of α⁻¹ does the hierarchy equal?
log_hierarchy_alpha = math.log(F_ratio) / math.log(alpha_inv)
print(f"  log_α⁻¹(F_em/F_grav):            {log_hierarchy_alpha:.6f}")
print(f"    (hierarchy = (α⁻¹)^{log_hierarchy_alpha:.2f})")
print()

# The cavity volume raised to powers
print(f"  V_cavity_planck^(1):              {V_cavity_planck:.6e}")
print(f"  V_cavity_planck^(2):              {V_cavity_planck**2:.6e}")
print(f"  V_outer_planck^(1):               {V_outer_planck:.6e}")
print(f"  V_outer_planck^(2):               {V_outer_planck**2:.6e}")
print()

# ═══════════════════════════════════════════════════════════════════
# §5  Exploring the eigenvalue tower connection
# ═══════════════════════════════════════════════════════════════════
#
# From the eigenvalue tower (2026y):
#   Level 0: α⁻¹ ≈ 137.036  
#   Level 1: β⁻¹ ≈ 43.619
#   The tower polynomial: 4π³ + π² + π ≈ 137.073
#   Inner polynomial: 4π² + π + 1 ≈ 43.620
#
# Let's compute: does the kaleidocycle geometry × eigenvalue tower
# produce the hierarchy?
# ═══════════════════════════════════════════════════════════════════

pi_val = float(Pi)
tower_L0 = 4*pi_val**3 + pi_val**2 + pi_val  # RHS of α equation
tower_L1 = 4*pi_val**2 + pi_val + 1           # inner polynomial = β⁻¹ approx
beta_inv = tower_L1  # Level 1 eigenvalue

print("=" * 70)
print("§5  Eigenvalue Tower × Kaleidocycle")
print("=" * 70)
print(f"  Tower L0 (4π³+π²+π):       {tower_L0:.10f}")
print(f"  Tower L1 (4π²+π+1):        {tower_L1:.10f}")
print(f"  α⁻¹ (algebraic):           {alpha_inv:.10f}")
print(f"  β⁻¹ (Level 1):             {beta_inv:.10f}")
print()

# n=11 and the tower
print(f"  n = {n}")
print(f"  n × α⁻¹:                   {n * alpha_inv:.6f}")
print(f"  n × β⁻¹:                   {n * beta_inv:.6f}")
print(f"  n²:                         {n**2}")
print(f"  α⁻¹ × β⁻¹:                {alpha_inv * beta_inv:.6f}")
print(f"  (α⁻¹)²:                    {alpha_inv**2:.6f}")
print()

# The hierarchy should be ≈ (m_P/m_p)² ≈ 1.69e38
# Let's see what combinations of 11, α, β produce this order

combos = {
    "α⁻² × β⁻²":               alpha_inv**2 * beta_inv**2,
    "(α⁻¹ × β⁻¹)²":            (alpha_inv * beta_inv)**2,
    "α⁻¹ × (m_P/m_p)":         alpha_inv * (m_P / m_p),
    "11 × α⁻¹ × β⁻¹ × 4π³":   11 * alpha_inv * beta_inv * 4*pi_val**3,
    "α⁻⁴":                      alpha_inv**4,
    "(4π³)⁴":                    (4*pi_val**3)**4,
    "11² × α⁻⁴":               11**2 * alpha_inv**4,
    "n × α⁻¹ × β⁻¹ × R/l_P":  n * alpha_inv * beta_inv * R_over_a,
    "exp(4π × α⁻¹/n)":         math.exp(4 * pi_val * alpha_inv / n),
}

print("  Combination search (target ≈ {:.3e}):".format(F_ratio))
print()
for label, val in sorted(combos.items(), key=lambda x: abs(math.log10(x[1]) - math.log10(F_ratio))):
    ratio = val / F_ratio
    print(f"    {label:40s} = {val:.6e}  (ratio to target: {ratio:.4e})")

print()
print()

# ═══════════════════════════════════════════════════════════════════
# §6  Direct volume-based hierarchy
# ═══════════════════════════════════════════════════════════════════
#
# In Kaluza-Klein / M-theory compactification:
#   G₄ = G₁₁ / V₇
# where V₇ is the volume of the 7 compactified dimensions.
#
# In Planck units, G₄ ~ 1/m_P² and G₁₁ ~ l_P⁹ (11D Planck),
# so V₇ ~ (l_P)⁷ × (some dimensionless number).
#
# The dimensionless number controls the hierarchy.
# For the 11-kaleidocycle: the 7 "internal" dimensions are the
# 7 compactified edges (n=11 edges − 4 large = 7 internal).
# Each internal edge has length l_P.
# ═══════════════════════════════════════════════════════════════════

# Volume of 7 compactified dimensions if each is Planck-scale
V_7_planck = l_P**7   # if each dimension has extent l_P

# But the kaleidocycle geometry gives a different effective size.
# The ring circumradius R provides an amplification factor.
# Effective compactification radius per internal dimension:
r_eff = R_ring  # the ring radius sets the scale

# If 7 internal dimensions each have extent r_eff:
V_7_kaleidocycle = r_eff**7

# The hierarchy from KK:  m_P² = m_P_11² × V_7 / l_P^7
# So: (m_P/m_p)² ~ (r_eff/l_P)^7 × α-dependent factors

r_ratio = r_eff / l_P  # this is just R_over_a

print("=" * 70)
print("§6  Kaluza-Klein Volume Hierarchy")
print("=" * 70)
print(f"  Compactification radius (R_ring):  {R_ring:.6e} m")
print(f"  R_ring / l_P:                      {R_over_a:.10f}")
print(f"  (R_ring / l_P)^7:                  {R_over_a**7:.10f}")
print(f"  (R_ring / l_P)^11:                 {R_over_a**11:.10f}")
print()
print(f"  Target (m_P/m_p)²:                 {hierarchy_planck:.6e}")
print(f"  Target F_em/F_grav:                {F_ratio:.6e}")
print()

# What if the effective compactification radius is α⁻¹ × l_P?
R_alpha = alpha_inv * l_P
V_7_alpha = R_alpha**7 / l_P**7   # in Planck units = α⁻⁷

print(f"  If r_compact = α⁻¹ × l_P:")
print(f"    r_compact:                       {R_alpha:.6e} m")
print(f"    V₇ / l_P⁷ = (α⁻¹)⁷:            {alpha_inv**7:.6e}")
print(f"    log₁₀((α⁻¹)⁷):                 {math.log10(alpha_inv**7):.4f}")
print(f"    log₁₀(hierarchy):               {math.log10(F_ratio):.4f}")
print()

# What about n/2π correction (the kaleidocycle's angular factor)?
angular = n / (2 * pi_val)
print(f"  Kaleidocycle angular factor n/2π:   {angular:.10f}")
print(f"  (α⁻¹ × n/2π)^7:                   {(alpha_inv * angular)**7:.6e}")
print(f"  log₁₀:                             {math.log10((alpha_inv * angular)**7):.4f}")
print()

# And with the tower
R_tower = alpha_inv * beta_inv  # product of first two eigenvalues
print(f"  α⁻¹ × β⁻¹:                        {R_tower:.6f}")
print(f"  (α⁻¹ × β⁻¹)^(7/2):               {R_tower**3.5:.6e}")
print(f"  log₁₀:                             {math.log10(R_tower**3.5):.4f}")
print()

# ═══════════════════════════════════════════════════════════════════
# §7  Summary
# ═══════════════════════════════════════════════════════════════════

print("=" * 70)
print("§7  SUMMARY")
print("=" * 70)
print()
print(f"  Target hierarchy (F_em/F_grav):    {F_ratio:.6e}")
print(f"  log₁₀(target):                    {math.log10(F_ratio):.4f}")
print()
print(f"  Best algebraic match:")

# Find the closest
candidates = {
    "(α⁻¹)^7.19 [exact exponent]":  alpha_inv ** log_hierarchy_alpha,
    "(α⁻¹)^7":                       alpha_inv**7,
    "exp(4π × α⁻¹/11)":             math.exp(4 * pi_val * alpha_inv / 11),
    "(α⁻¹ × β⁻¹)^(7/2)":           R_tower**3.5,
    "α⁻⁴ (QED order)":              alpha_inv**4,
}

for label, val in sorted(candidates.items(), key=lambda x: abs(math.log10(x[1]) - math.log10(F_ratio))):
    log_val = math.log10(val)
    log_diff = log_val - math.log10(F_ratio)
    print(f"    {label:40s} = {val:.6e}  (log₁₀ diff: {log_diff:+.4f})")

print()
print("  Done.")
