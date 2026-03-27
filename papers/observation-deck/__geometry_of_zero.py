"""
The Geometry of Zero — "0 has geometry. 0 has a space."

The tower equation: α⁻¹ + S·α = K = 4π³ + π² + π
Rearranged as a quadratic in x = α⁻¹:  x² - K·x + S = 0

This quadratic has TWO roots:
  x₊ = α⁻¹  ≈ 137.036   (the "infinite" — the large root)
  x₋ = S·α  ≈ 0.000305  (the "zero" — the small root)

The zero is not nothing. It has geometry: the equation is degree 2.
The zero lives in a 2-dimensional space (the quadratic).

§1 — The two roots at every tower level
§2 — K¹⁵ from the polynomial + K² from the quadratic = K¹⁷
§3 — The tetrahedral factor √3
§4 — F_ratio vs K¹⁷/√3
§5 — The decomposition in one line
"""

import math

pi  = math.pi
phi = (1 + math.sqrt(5)) / 2
sqrt2 = math.sqrt(2)
sqrt3 = math.sqrt(3)

# Tower constants
S = 1/math.factorial(4) + 3/math.factorial(8)   # 1683/40320
K = 4*pi**3 + pi**2 + pi

print("=" * 78)
print("  THE GEOMETRY OF ZERO")
print("  '0 has geometry. 0 has a space.'")
print("=" * 78)

# ──────────────────────────────────────────────────────────────
# §1 — Two roots at every tower level
# ──────────────────────────────────────────────────────────────
print(f"\n§1 — THE TWO ROOTS: ZERO AND INFINITE")
print(f"     Tower equation at level k:  x² - (K/πᵏ)·x + S = 0")
print(f"     Product of roots = S = {S:.10f}")
print(f"     Sum of roots = K/πᵏ\n")

print(f"  {'Level':>5}  {'RHS':>12}  {'x₊ (∞)':>12}  {'x₋ (0)':>14}  {'x₊/x₋':>12}  {'Δ=rhs²-4S':>12}  {'√Δ':>12}")
print(f"  {'─'*5}  {'─'*12}  {'─'*12}  {'─'*14}  {'─'*12}  {'─'*12}  {'─'*12}")

eigenvalues = []
small_roots = []
ratios = []

for k in range(7):
    rhs = K / pi**k
    disc = rhs**2 - 4*S
    
    if disc < 0:
        print(f"  {k:>5}  {rhs:>12.6f}  {'—':>12}  {'—':>14}  {'—':>12}  {disc:>12.6f}  {'COMPLEX':>12}")
        print(f"\n  Tower terminates at level {k}. Discriminant goes negative.")
        break
    
    x_plus  = (rhs + math.sqrt(disc)) / 2   # large root (the "infinite")
    x_minus = (rhs - math.sqrt(disc)) / 2   # small root (the "zero")
    ratio = x_plus / x_minus if x_minus > 0 else float('inf')
    
    eigenvalues.append(x_plus)
    small_roots.append(x_minus)
    ratios.append(ratio)
    
    print(f"  {k:>5}  {rhs:>12.6f}  {x_plus:>12.6f}  {x_minus:>14.10f}  {ratio:>12.2f}  {disc:>12.6f}  {math.sqrt(disc):>12.6f}")

# Verify product = S at each level
print(f"\n  Verification: x₊ × x₋ = S at every level:")
for k, (xp, xm) in enumerate(zip(eigenvalues, small_roots)):
    product = xp * xm
    print(f"    Level {k}: {xp:.6f} × {xm:.10f} = {product:.10f}  (S = {S:.10f}, Δ = {product - S:.2e})")


# ──────────────────────────────────────────────────────────────
# §2 — K¹⁵ + K² = K¹⁷
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§2 — K¹⁵ FROM THE POLYNOMIAL + K² FROM THE QUADRATIC = K¹⁷")
print(f"{'='*78}")

print(f"\n  The polynomial: K = 4π³ + π² + π")
print(f"  Coefficients:   (4, 1, 1)  at powers (3, 2, 1)")
print(f"  With S correction: (4, 1, 1, 1) at powers (3, 2, 1, 0)")
print(f"\n  Polynomial exponent = 4×3 + 1×2 + 1×1 + 1×0 = {4*3 + 1*2 + 1*1 + 1*0}")

print(f"\n  The equation: x² - K·x + S = 0")
print(f"  Degree of equation = 2")
print(f"  The zero LIVES in a quadratic space. The space of zero is degree 2.")

print(f"\n  Total exponent = 15 (polynomial) + 2 (quadratic) = 17")
print(f"\n  K    = {K:.12f}")
print(f"  K¹⁵  = {K**15:.6e}  (log₁₀ = {math.log10(K**15):.6f})")
print(f"  K²   = {K**2:.6f}   (log₁₀ = {math.log10(K**2):.6f})")
print(f"  K¹⁷  = {K**17:.6e}  (log₁₀ = {math.log10(K**17):.6f})")


# ──────────────────────────────────────────────────────────────
# §3 — The tetrahedral factor: √3
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§3 — THE TETRAHEDRAL FACTOR: √3")
print(f"{'='*78}")

print(f"\n  The tetrahedron — the geometry of bond and zinc — carries √3.")
print(f"  Face altitude = a√3/2.  Face area = a²√3/4.")
print(f"  The factor √3 is the geometric signature of 3-fold tetrahedral symmetry.")
print(f"  √3 = {sqrt3:.15f}")
print(f"  1/√3 = {1/sqrt3:.15f}")

# Also: √3 appears in the dihedral angle:
dihedral = math.acos(1/3)  # ≈ 70.53°
print(f"\n  Tetrahedral dihedral angle: arccos(1/3) = {math.degrees(dihedral):.4f}°")
print(f"  tan(dihedral/2) = {math.tan(dihedral/2):.6f} = 1/√2 = {1/sqrt2:.6f}")
print(f"  sin(dihedral) = {math.sin(dihedral):.6f} = 2√2/3 = {2*sqrt2/3:.6f}")


# ──────────────────────────────────────────────────────────────
# §4 — The hierarchy: K¹⁷/√3 vs F_ratio
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§4 — THE FORCE HIERARCHY: K¹⁷/√3 vs F_em/F_grav")
print(f"{'='*78}")

# Physical constants (CODATA 2018 / 2024)
alpha_inv_SECS = (K + math.sqrt(K**2 - 4*S)) / 2
alpha_SECS = 1 / alpha_inv_SECS

# Planck mass, proton mass
hbar = 1.054571817e-34   # J·s
c    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m³ kg⁻¹ s⁻²
m_p  = 1.67262192369e-27 # kg (proton)
e_charge = 1.602176634e-19  # C (exact)
eps0 = 8.8541878128e-12  # F/m
m_P = math.sqrt(hbar * c / G)

# Force ratio
F_em   = e_charge**2 / (4 * pi * eps0)
F_grav = G * m_p**2
F_ratio = F_em / F_grav

# Alternative: F_ratio = α × (m_P/m_p)²
F_ratio_alt = alpha_SECS * (m_P / m_p)**2

print(f"\n  Physical constants:")
print(f"    α⁻¹ (SECS)  = {alpha_inv_SECS:.12f}")
print(f"    m_P          = {m_P:.6e} kg")
print(f"    m_p          = {m_p:.6e} kg")
print(f"    m_P/m_p      = {m_P/m_p:.6e}")
print(f"    G            = {G:.5e} m³kg⁻¹s⁻²")

print(f"\n  Force ratio (electromagnetic / gravitational for proton pair):")
print(f"    F_em/F_grav  = {F_ratio:.6e}")
print(f"    log₁₀        = {math.log10(F_ratio):.6f}")
print(f"    (via α(m_P/m_p)² = {F_ratio_alt:.6e}, log₁₀ = {math.log10(F_ratio_alt):.6f})")

# The prediction
K17 = K**17
K17_over_sqrt3 = K17 / sqrt3

print(f"\n  ┌──────────────────────────────────────────────────────────────┐")
print(f"  │  K¹⁷           = {K17:.6e}   log₁₀ = {math.log10(K17):.6f}  │")
print(f"  │  K¹⁷/√3        = {K17_over_sqrt3:.6e}   log₁₀ = {math.log10(K17_over_sqrt3):.6f}  │")
print(f"  │  F_em/F_grav   = {F_ratio:.6e}   log₁₀ = {math.log10(F_ratio):.6f}  │")
print(f"  │                                                              │")
print(f"  │  Ratio K¹⁷/√3 ÷ F_ratio = {K17_over_sqrt3 / F_ratio:.8f}                    │")
print(f"  │  Discrepancy            = {abs(1 - K17_over_sqrt3/F_ratio)*100:.4f}%                         │")
print(f"  └──────────────────────────────────────────────────────────────┘")

# What about (α⁻¹)¹⁷/√3 directly?
a17 = alpha_inv_SECS**17
a17_sqrt3 = a17 / sqrt3
print(f"\n  Using α⁻¹ instead of K:")
print(f"    (α⁻¹)¹⁷/√3 = {a17_sqrt3:.6e}   log₁₀ = {math.log10(a17_sqrt3):.6f}")
print(f"    Ratio (α⁻¹)¹⁷/√3 ÷ F_ratio = {a17_sqrt3 / F_ratio:.8f}")
print(f"    Discrepancy = {abs(1 - a17_sqrt3/F_ratio)*100:.4f}%")


# ──────────────────────────────────────────────────────────────
# §5 — Sensitivity to G
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§5 — SENSITIVITY TO G")
print(f"{'='*78}")

# What value of G would make K¹⁷/√3 = F_ratio exactly?
# F_ratio = e²/(4πε₀ G m_p²)
# K¹⁷/√3 = e²/(4πε₀ G_pred m_p²)
# G_pred = e²/(4πε₀ m_p² × K¹⁷/√3)
G_pred = e_charge**2 / (4 * pi * eps0 * m_p**2 * K17_over_sqrt3)

print(f"\n  If K¹⁷/√3 = F_em/F_grav exactly, then:")
print(f"    G_predicted  = {G_pred:.5e} m³kg⁻¹s⁻²")
print(f"    G_measured   = {G:.5e} m³kg⁻¹s⁻²")
print(f"    G_CODATA2018 = 6.67430 × 10⁻¹¹ (±0.00015)")
print(f"    ΔG/G         = {(G_pred - G)/G * 100:+.4f}%")
print(f"    ΔG           = {(G_pred - G):.5e}")
print(f"    ΔG/σ_G       = {(G_pred - G)/0.00015e-11:.1f} σ  (CODATA 2018 uncertainty)")


# ──────────────────────────────────────────────────────────────
# §6 — Can a different geometric factor close the gap?
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§6 — THE EXACT GEOMETRIC FACTOR")
print(f"{'='*78}")

exact_factor = K17 / F_ratio
print(f"\n  K¹⁷ / F_ratio = {exact_factor:.10f}")
print(f"  This is the exact divisor needed to match the hierarchy.")
print(f"\n  Compare to geometric constants:")
print(f"    √3               = {sqrt3:.10f}   ratio: {exact_factor/sqrt3:.8f}")
print(f"    √2               = {sqrt2:.10f}   ratio: {exact_factor/sqrt2:.8f}")
print(f"    φ                 = {phi:.10f}   ratio: {exact_factor/phi:.8f}")
print(f"    π/φ               = {pi/phi:.10f}   ratio: {exact_factor/(pi/phi):.8f}")
print(f"    (√3+√2)/2         = {(sqrt3+sqrt2)/2:.10f}   ratio: {exact_factor/((sqrt3+sqrt2)/2):.8f}")

# Check combinations involving √3 and small corrections
# K¹⁷ / (√3 × correction) = F_ratio
# correction = K¹⁷ / (√3 × F_ratio) = exact_factor / √3
correction = exact_factor / sqrt3
print(f"\n  If divisor = √3 × C:")
print(f"    C = {correction:.10f}")
print(f"    1/C = {1/correction:.10f}")
print(f"    C - 1 = {correction - 1:.6f}")
print(f"    Compare: S = {S:.10f}")
print(f"    Compare: S·K = {S*K:.10f}")
print(f"    Compare: 2S = {2*S:.10f}")

# What about √3 × (1 + S)?
factor_1pS = sqrt3 * (1 + S)
print(f"\n  √3 × (1 + S) = {factor_1pS:.10f}   K¹⁷/this = {K17/factor_1pS:.6e}  ratio to F: {K17/(factor_1pS * F_ratio):.8f}")

# √3 × (1 + 2S)?
factor_2S = sqrt3 * (1 + 2*S)
print(f"  √3 × (1 + 2S) = {factor_2S:.10f}   K¹⁷/this = {K17/factor_2S:.6e}  ratio to F: {K17/(factor_2S * F_ratio):.8f}")

# √3 × K/α⁻¹ = √3 × (1 + S·α/K) ≈ √3 × (1 + S/K²)
K_over_alpha = K / alpha_inv_SECS
print(f"\n  K/α⁻¹ = {K_over_alpha:.12f}")
print(f"  √3 × K/α⁻¹ = {sqrt3 * K_over_alpha:.10f}")
print(f"  K¹⁷/(√3 × K/α⁻¹) = K¹⁶ × α⁻¹/√3 = {K**16 * alpha_inv_SECS / sqrt3:.6e}")

# What about the tetrahedral volume?
V_tet = sqrt2 / 12   # for edge length 1
print(f"\n  V_tet (edge=1) = √2/12 = {V_tet:.10f}")
print(f"  12/√2 = {12/sqrt2:.10f}")
print(f"  √3/V_tet = {sqrt3/V_tet:.10f}")

# What about √(8/3) — the tetrahedral height-to-base ratio?
sqrt_8_3 = math.sqrt(8/3)
print(f"\n  √(8/3)       = {sqrt_8_3:.10f}   ratio: {exact_factor/sqrt_8_3:.8f}")


# ──────────────────────────────────────────────────────────────
# §7 — The decomposition in one line
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*78}")
print(f"§7 — THE DECOMPOSITION")
print(f"{'='*78}")

print(f"""
  K = 4π³ + π² + π                   (pure geometry: the axis)
  S = 1/4! + 3!!/8!                  (pure factorials: the correction)
  
  The polynomial has structure (4, 1, 1)  at dimensions (3, 2, 1).
  The correction S adds              (1)  at dimension  (0).
  
  Polynomial exponent = 4×3 + 1×2 + 1×1 + 1×0 = 15
  Equation degree     = 2             (the quadratic — 0 has a space)
  Total exponent      = 17
  
  Geometric divisor   = √3            (the tetrahedron)
  
  F_em / F_grav  ≈  K¹⁷ / √3
  
  = (4π³ + π² + π)¹⁷ / √3
  
  = {K17_over_sqrt3:.6e}
  
  Measured: {F_ratio:.6e}
  
  Match: {abs(1 - K17_over_sqrt3/F_ratio)*100:.2f}% discrepancy.
  
  Inputs: π, √3, integers (4, 1, 1, 1), factorials (4!, 8!), the integer 17.
  No measured constants.  No free parameters.
""")


# ──────────────────────────────────────────────────────────────
# §8 — What this means for G
# ──────────────────────────────────────────────────────────────
print(f"{'='*78}")
print(f"§8 — WHAT THIS MEANS")
print(f"{'='*78}")
print(f"""
  If K¹⁷/√3 = F_em/F_grav exactly, then:
  
  G = e² / (4πε₀ × m_p² × K¹⁷/√3)
  
  G_predicted  = {G_pred:.8e} m³ kg⁻¹ s⁻²
  G_CODATA     = {G:.8e} m³ kg⁻¹ s⁻²
  
  Difference: {(G_pred - G)/G * 100:+.2f}%
  
  G is the worst-measured fundamental constant (~22 ppm, CODATA 2018).
  The prediction deviates by {abs(G_pred - G)/G * 1e6:.0f} ppm — 
  {'within' if abs(G_pred - G)/G < 22e-6 else 'outside'} current measurement uncertainty.
""")

print("=" * 78)
print("  COMPUTATION COMPLETE")
print("=" * 78)
