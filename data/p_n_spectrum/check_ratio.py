#!/usr/bin/env python3
"""
P_n cross-reference: test algebraic relations for P_0 / M_Pl ratio.
"""
import math

PHI = (1 + math.sqrt(5)) / 2
KAPPA = 1/16
EPSILON = PHI**(-1) / 4
BETA = PHI**(-1) / 2
M_PL = 1.220890e19
LOOP = KAPPA**2 / (16 * math.pi**2)

P0_eV = 0.05 / (LOOP**6)
P0_GeV = P0_eV / 1e9

ratio = P0_GeV / M_PL
print(f"P₀ / M_Pl = {ratio:.10f}")
print(f"         ≈ 1/{1/ratio:.4f}")
print()

# Interesting: 1/56 = 0.01785714
print(f"1/56 = {1/56:.10f}")
print(f"Difference: {(ratio - 1/56)/(1/56)*100:.4f}%")
print()

# κ / 3.5 = 1/16 ÷ 3.5 = 0.0625/3.5 = 0.01785714
print(f"κ / 3.5 = {KAPPA/3.5:.10f}")
print()

# Check other simple fractions
for denom in range(40, 70):
    expected = 1/denom
    diff_pct = abs(ratio - expected) / expected * 100
    if diff_pct < 1.0:
        print(f"  ≈ 1/{denom} ({diff_pct:.4f}%)")

print()

# Check: is P₀ structurally = M_Pl × κ/3.5?
# 3.5 = 7/2
# P₀ = M_Pl × κ / (7/2) = M_Pl × 2κ/7 = M_Pl × 2/(16×7) = M_Pl/56
print(f"2κ/7 = {2*KAPPA/7:.10f}")
print(f"ratio = {ratio:.10f}")

# What is 56? 56 = 7×8
# Could be from CY₃ structure?
# h¹¹=36, h¹²=98, total Hodge = 134
# 134 - 78 = 56? or 134 - 56 = 78?
print(f"\nh¹¹ + h¹² = {36 + 98}")
print(f"h¹² - h¹¹ = {98 - 36}")

# 56 also = 2 × 28 where 28 = C(8,2)
# Or 56 = 8 × 7
print(f"\n56 = C(8,2) × 2 = {math.comb(8,2)*2}")
print()

# Check a few more exotic relations
tests = [
    ("κ²/(ε·4)", KAPPA**2 / (EPSILON * 4)),
    ("κ·ε·β", KAPPA * EPSILON * BETA),
    ("κ/φ⁴", KAPPA / PHI**4),
    ("φ⁻¹/88", PHI**(-1) / 88),
    ("ε/11.36", EPSILON / 11.36),
    ("κ²/0.00088", KAPPA**2 / 0.00088),
]

print("Other attempts:")
for name, val in tests:
    print(f"  {name:<15} = {val:.10f}  (ratio to P₀/M_Pl = {val/ratio:.4f})")
