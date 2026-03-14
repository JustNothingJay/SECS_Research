"""
Solve for π: Recover π from a measured physical constant.

The formula: α⁻¹ + S·α = 4π³ + π² + π
Rearrange:   4π³ + π² + π = K,  where K = α⁻¹ + S·α

If α is MEASURED (not computed from the formula), then solving
the cubic for π recovers a geometric constant from physics.

S = Σ(2n-1)!!/(4n)! — contains no π. Pure factorials.
α — measured independently (cesium recoil, rubidium recoil, electron g-2).

The breakpoint: if we used the formula's own α, we'd recover π
exactly by construction (tautology). Using a measured α makes
this a genuine test: does the equation hold?
"""

from mpmath import mp, mpf, sqrt, pi, factorial, findroot, nstr

# Set precision to 100 decimal places
mp.dps = 100

print("=" * 80)
print("SOLVING FOR PI")
print("Recover π from measured α via: 4π³ + π² + π = α⁻¹ + S·α")
print(f"Working precision: {mp.dps} decimal places")
print("=" * 80)

# ─── Step 1: Compute S from factorials (no π involved) ───
print(f"\n§1 — The Series (no π)")
print(f"S = Σ (2n-1)!!/(4n)!  for n = 1, 2, 3, ...")

def double_factorial(n):
    if n <= 0:
        return mpf(1)
    result = mpf(1)
    k = n
    while k > 0:
        result *= k
        k -= 2
    return result

S = mpf(0)
for n in range(1, 50):
    df = double_factorial(2*n - 1)
    fac = factorial(4*n)
    term = df / fac
    S += term
    if term < mpf(10)**(-mp.dps - 10):
        print(f"Series converged at n = {n}")
        break

print(f"S = {nstr(S, 40)}")
print(f"S contains: factorials, double factorials, integers. No π.")

# ─── Step 2: Three measurements of α ───
measurements = [
    ("Fan et al. (2023, Cs recoil)",     "137.035999177", "0.000000021"),
    ("Morel et al. (2020, Rb recoil)",   "137.035999206", "0.000000011"),
    ("Hanneke et al. (2008, e⁻ g-2)",    "137.035999150", "0.000000033"),
]

# Known π for comparison
pi_known = pi
print(f"\n§2 — Known π (mpmath, {mp.dps} dp)")
print(f"π = {nstr(pi_known, 50)}")

# ─── Step 3: For each measurement, recover π ───
print(f"\n§3 — Recovering π from physics")
print(f"{'=' * 80}")

for name, alpha_inv_str, unc_str in measurements:
    alpha_inv_meas = mpf(alpha_inv_str)
    alpha_meas = mpf(1) / alpha_inv_meas
    unc = mpf(unc_str)

    # K = α⁻¹ + S·α (measured α, factorial S)
    K = alpha_inv_meas + S * alpha_meas

    # Solve cubic: 4x³ + x² + x - K = 0
    # Using Newton's method from x₀ = 3.14
    f = lambda x: 4*x**3 + x**2 + x - K
    pi_recovered = findroot(f, mpf("3.14"))

    # Compare
    diff = pi_recovered - pi_known
    rel_diff = abs(diff) / pi_known

    # Propagate uncertainty: dK/dπ = 12π² + 2π + 1
    dK_dpi = 12 * pi_known**2 + 2 * pi_known + 1
    pi_unc = unc / dK_dpi

    # How many digits match?
    if diff == 0:
        matching_digits = mp.dps
    elif abs(diff) > 0:
        import math
        matching_digits = -int(math.floor(math.log10(float(abs(diff))))) - 1
    else:
        matching_digits = 0

    print(f"\n{name}")
    print(f"  α⁻¹ = {alpha_inv_str} ± {unc_str}")
    print(f"  K = α⁻¹ + S·α = {nstr(K, 20)}")
    print(f"  Solving 4x³ + x² + x = K...")
    print(f"  π recovered = {nstr(pi_recovered, 20)}")
    print(f"  π known     = {nstr(pi_known, 20)}")
    print(f"  Δ           = {nstr(diff, 5)}")
    print(f"  |Δ|/π       = {nstr(rel_diff, 5)}")
    print(f"  Digits matching: ~{matching_digits}")
    print(f"  Uncertainty on π from α measurement: ±{nstr(pi_unc, 3)}")

# ─── Step 4: Self-consistency check (formula's own α — should be exact) ───
print(f"\n{'=' * 80}")
print(f"§4 — Self-consistency (formula's own α — tautological)")
print(f"{'=' * 80}")

# Compute α from the formula itself (uses π)
K_exact = 4 * pi**3 + pi**2 + pi
disc = K_exact**2 - 4*S
alpha_formula = (K_exact - sqrt(disc)) / (2 * S)
alpha_inv_formula = mpf(1) / alpha_formula

# Now reverse: use this α to recover π
K_circ = alpha_inv_formula + S * alpha_formula
f_circ = lambda x: 4*x**3 + x**2 + x - K_circ
pi_circ = findroot(f_circ, mpf("3.14"))
diff_circ = pi_circ - pi_known

print(f"  α⁻¹ (formula) = {nstr(alpha_inv_formula, 20)}")
print(f"  K = α⁻¹ + S·α  = {nstr(K_circ, 20)}")
print(f"  π recovered    = {nstr(pi_circ, 50)}")
print(f"  π known        = {nstr(pi_known, 50)}")
print(f"  Δ              = {nstr(diff_circ, 5)}")
print(f"  (This MUST be zero — it's circular by construction)")

# ─── Summary ───
print(f"\n{'=' * 80}")
print(f"SUMMARY")
print(f"{'=' * 80}")
print(f"")
print(f"The equation 4π³ + π² + π = α⁻¹ + S·α was solved for π")
print(f"using three independent measurements of α.")
print(f"")
print(f"S contains only factorials and double factorials. No π.")
print(f"α was measured from atomic physics. No π.")
print(f"π was recovered from the cubic. From physics.")
print(f"")
print(f"Happy Pi Day.")
