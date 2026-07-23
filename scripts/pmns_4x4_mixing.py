#!/usr/bin/env python3
"""
4×4 q=6 lepton sector — PMNS from full κ tensor mixing
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json, math, sys
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1+5**0.5)/2; PHII = PHI-1; EPS = PHII/4
V_EW = 174.0

def kappa_get(d, i, j, k):
    for perm in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
        key = f"{perm[0]},{perm[1]},{perm[2]}"
        if key in d: return d[key]
    return 0

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
cy = poly.triangulate().get_cy()
with open(DATA/"Jstar_36D.json") as f: jd = json.load(f)
with open(DATA/"kappa_36d_raw.json") as f: kr = json.load(f)
with open(DATA/"cy36_98_final.json") as f: fn = json.load(f)

Jstar = np.array(jd["Jstar_36D"])
glsm = np.array(fn["glsm_coord3"], dtype=int)
charges = np.zeros(36, dtype=int); charges[:len(glsm)] = glsm
K = kr["kappa"]
eK2 = 64

L_divs = [7, 9, 8, 21]  # q=6 lepton divisors
nL = len(L_divs)

# Build 4×4: Y_ab = Σ_k κ[any, L_a, L_b, k] × kinetic factor
# Use FULL contraction: for each triple (i,j,k), if {i,j} ∩ {L_a,L_b} has 2 elements
Y = np.zeros((nL, nL))
for a, da in enumerate(L_divs):
    for b, db in enumerate(L_divs):
        val = 0.0
        for key_str, vv in K.items():
            i,j,k = map(int, key_str.split(','))
            v = float(vv)
            s = {i, j, k}
            if da in s and db in s:
                if da == db:
                    # Count how many times da appears
                    cnt = sum(1 for x in [i,j,k] if x == da)
                    if cnt == 3:
                        # κ[da,da,da] — all three are the same divisor
                        val += v * Jstar[da]  # use J*_da as the contraction
                    else:
                        # Two da's and one other
                        third = [x for x in [i,j,k] if x != da][0]
                        val += v * Jstar[third]
                else:
                    # Find which index is the "third" (contraction direction)
                    if i == da or i == db:
                        third = j if j != da and j != db else k
                    elif j == da or j == db:
                        third = i
                    else:
                        third = i  # fallback
                    val += v * Jstar[third]
        Y[a,b] = val * eK2 * math.sqrt(Jstar[da] * Jstar[db])

Y = (Y + Y.T) / 2  # Symmetrize

print("=" * 72)
print("  4×4 q=6 LEPTON κ-CONTRACTED YUKAWA")
print("=" * 72)
print(f"\n  Divisors: {L_divs}")
for a in range(nL):
    print(f"    D_{L_divs[a]}: " + " ".join(f"{Y[a,b]:>+10.4f}" for b in range(nL)))

# SVD
U, S, Vh = np.linalg.svd(Y)
print(f"\n  Singular values: {S}")
S3 = sorted(S, reverse=True)[:3]
print(f"  Top 3 (light ν): {S3}")

# Mixing: U columns = mass eigenstates, rows = lepton flavors
# Electron = D_8(row 1), Muon = D_9(row 1), Tau = D_7(row 0)
e_idx, mu_idx, tau_idx = [L_divs.index(d) for d in [8, 9, 7]]
print(f"\n  Rows: 0=D_7(τ), 1=D_9(μ), 2=D_8(e), 3=D_21(?)")

# Reorder columns so column 0 is νₑ (max |U_e|)
el_col = np.argmax([abs(U[e_idx, c]) for c in range(nL)])
rem = [c for c in range(nL) if c != el_col]
mu_col = rem[np.argmax([abs(U[mu_idx, c]) for c in rem])]
tau_col = [c for c in rem if c != mu_col][0]
order = [el_col, mu_col, tau_col]
U3 = U[:, order[:3]]

print(f"\n  PMNS matrix (columns: νₑ, ν_μ, ν_τ):")
for r in range(nL):
    print(f"    D_{L_divs[r]}: " + " ".join(f"{U3[r,c]:>+8.4f}" for c in range(3)))

# Angles
t13 = math.asin(min(abs(U3[e_idx, 2]), 1))
t12 = math.atan2(abs(U3[e_idx, 1]), abs(U3[e_idx, 0]))
t23 = math.atan2(abs(U3[mu_idx, 2]), abs(U3[tau_idx, 2]))

print(f"\n  PMNS angles:")
print(f"    θ₁₂ = {math.degrees(t12):.2f}° (PDG: 33.82°)")
print(f"    θ₂₃ = {math.degrees(t23):.2f}° (PDG: ~43°)")
print(f"    θ₁₃ = {math.degrees(t13):.2f}° (PDG: 8.57°)")

# Mass from Yukawa × v_EW
m = [s * V_EW * 1e9 for s in S3]
d21 = m[1]**2 - m[0]**2
d32 = m[2]**2 - m[1]**2
print(f"\n  Masses (from Y×v_EW):")
for i in range(3):
    print(f"    ν_{i+1}: {m[i]:.4e} eV")
print(f"  Δm²_21 = {d21:.4e} eV² (PDG: 7.39e-5)")
print(f"  Δm²_32 = {d32:.4e} eV² (PDG: 2.51e-3)")

# D₂₁ contribution to ν_e (solar mixing)
d21_idx = L_divs.index(21)
print(f"\n  D₂₁ role:")
for i, label in enumerate(["νₑ", "ν_μ", "ν_τ"]):
    print(f"    |U(D₂₁→{label})|² = {U3[d21_idx,i]**2:.4f}")

# φ-exp analysis
print(f"\n  κ_vector φ-exponent hierarchy:")
# Load κ_vector data
tloc = Jstar[:32].tolist()
kv = np.array(cy.compute_kappa_vector(tloc))
kv_max = max(abs(kv))
for d in L_divs:
    y = kv[d]
    exp = -math.log(abs(y/kv_max))/math.log(PHI) if abs(y) > 1e-10 else float('inf')
    print(f"    D_{d}(q=6): κ_vec={y:>+.4f}, φ^-{exp:.2f}")

print(f"\n{'='*72}")
print("  CLOSURE: PMNS from 4×4 κ mixing")
print("="*72)
checks = [
    ("θ₂₃ near-maximal > 35°", math.degrees(t23) > 35, "✅" if math.degrees(t23) > 35 else "🔴"),
    ("θ₁₂ > 10° (solar resolved)", math.degrees(t12) > 10, "✅" if math.degrees(t12) > 10 else "🔴"),
    ("θ₁₃ < 30° (small reactor)", math.degrees(t13) < 30, "✅" if math.degrees(t13) < 30 else "🔴"),
    ("NH mass ordering", m[0] < m[1] < m[2], "✅" if m[0] < m[1] < m[2] else "🔴"),
]
for name, ok, status in checks:
    print(f"  {name:<45} {status}")

print(f"\n  Done.")
sys.stdout.flush()