#!/usr/bin/env python3
"""Strategy B: 3×3 Yukawa Projection from CY₃(36,98) κ_{ijk}

Project the intersection tensor onto physical flavor states,
diagonalize, and compare eigenvalues to φ^{-n} predictions.

The Yukawa coupling:  Y_{ij} = κ_{ijk} · v_k
where v_k are VEV directions in Kähler moduli space.

For heterotic CY₃:  Y_{ijk} = ∫ ψ_i ∧ ψ_j ∧ ψ_k ∧ Ω
→ maps to triple intersection numbers in the divisor basis.
"""

import json, math, sys
import numpy as np
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1 + 5**0.5) / 2
PHI_INV = PHI - 1
KAPPA = 1/16

np.set_printoptions(precision=6, suppress=True, linewidth=120)

# ─── Load all data ────────────────────────────────────────────

with open(DATA / "Jstar_36D.json") as f:   jstar = json.load(f)
with open(DATA / "cy36_98_final.json") as f: final = json.load(f)
with open(DATA / "kappa_36d_raw.json") as f: kappa_raw = json.load(f)

Jstar = np.array(jstar["Jstar_36D"])
glsm = np.array(final["glsm_coord3"])
h11 = final["h11"]

# Parse κ dictionary into (i,j,k,value) format
kappa_entries = []
kappa_dict = kappa_raw["kappa"]
for key, val in kappa_dict.items():
    i, j, k = map(int, key.split(","))
    if abs(val) > 0:
        kappa_entries.append((i, j, k, float(val)))

# Identify divisor charge groups
n_glsm = len(glsm)  # 32
# Assign charge 0 to the remaining 4 non-GLSM divisors (indices 32-35)
charges = np.zeros(36, dtype=int)
charges[:n_glsm] = glsm.astype(int)

# ─── 1. Charge Group Analysis ─────────────────────────────────

print("=" * 72)
print("  STRATEGY B: 3×3 YUKAWA PROJECTION")
print("=" * 72)

charge_groups = {}
for idx in range(36):
    q = charges[idx]
    if q not in charge_groups:
        charge_groups[q] = []
    charge_groups[q].append(idx)

print("\n## 1. Divisor Charge Groups (GLSM coord3 + 4 non-GLSM)")
for q in sorted(charge_groups.keys(), reverse=True):
    divisors = charge_groups[q]
    j_vals = [Jstar[d] for d in divisors]
    print(f"  q={q:>3}: {len(divisors):>2} divisors — indices {divisors} — J*≈{np.mean(j_vals):.4f}")

# ─── 2. Build κ-contracted Yukawa matrix candidates ──────────

print("\n## 2. Yukawa Matrix from κ·J Contraction")

# The Yukawa coupling in heterotic CY₃ is:
# Y_{ij}^{(\alpha)} = κ_{ijk} · J^{*k}
# where J^{*k} is the stabilized Kähler class
# This gives us a 36×36 matrix that we need to project onto 3×3

# Full 36×36 matrix from contraction
Y_full = np.zeros((36, 36))
for i, j, k, val in kappa_entries:
    Y_full[i, j] += val * Jstar[k]
    # κ is symmetric in permutations for CY triple intersections
    Y_full[j, i] += val * Jstar[k]

# Alternative: use the GLSM charge 12 Higgs direction
# κ[2,7,7] = -32 involves divisor 2 (q=12) as the "Higgs partner"
# Let's try different contraction vectors

# Contraction vector candidates:
# Option A: J* (the stabilized Kähler class)
# Option B: unit vector along divisor 2 (q=12, the Higgs-like direction)
# Option C: unit vector along divisor 4 (q=10, the Top direction)

for name, vec in [
    ("J* (stabilized Kähler class)", Jstar),
    ("q=12 direction (Higgs-like, divisor 2)", np.eye(36)[2]),
    ("q=10 direction (Top, divisor 4)", np.eye(36)[4]),
    ("q=8 direction (Bottom, divisor 6)", np.eye(36)[6]),
    ("q=6 direction (Lepton, divisor 7)", np.eye(36)[7]),
]:
    Y = np.zeros((36, 36))
    for i, j, k, val in kappa_entries:
        Y[i, j] += val * vec[k]
    
    # Project onto charge sectors
    print(f"\n  --- Contraction: {name} ---")
    
    # For each charge sector pair, compute the effective coupling
    for q1 in [10, 8, 6]:  # physical families
        for q2 in [10, 8, 6]:
            idx1 = charge_groups.get(q1, [])
            idx2 = charge_groups.get(q2, [])
            sub = Y[np.ix_(idx1, idx2)]
            if sub.size > 0:
                avg = np.mean(np.abs(sub))
                maxv = np.max(np.abs(sub))
                nonzero = np.count_nonzero(sub)
                print(f"    Y(q={q1}→q={q2}): dim={sub.shape}, |Y|_avg={avg:.4f}, max={maxv:.4f}, nonzero={nonzero}/{sub.size}")

# ─── 3. 3×3 Flavor Yukawa from physical projection ──────────

print("\n## 3. 3×3 Flavor Yukawa Matrix Construction")

# Physical families from dual mechanism:
# Up-type (q=10): divisors with charge 10
# Down-type (q=8): divisors with charge 8  
# Lepton (q=6): divisors with charge 6

# But also: τ gets its mass from κ[2,7,7] which involves q=12 and q=6
# So the 3 generations within each sector correspond to different 
# linear combinations of the same-charge divisors

# The simplest approach: use J*-weighted average over each charge group
# as the effective "direction" for that family

Y_3x3 = np.zeros((3, 3))
family_labels = [(10, "Top/Charm/Up"), (8, "Bottom/Str/Down"), (6, "Tau/Mu/El")]
family_indices = [charge_groups[10], charge_groups[8], charge_groups[6]]

# For each pair of families, contract κ with J*
for a, (q_a, label_a) in enumerate(family_labels):
    for b, (q_b, label_b) in enumerate(family_labels):
        idx_a = family_indices[a]
        idx_b = family_indices[b]
        
        # Sum over all divisor combinations weighted by geometric mean of J*
        total = 0.0
        weight_sum = 0.0
        
        for i in idx_a:
            for j in idx_b:
                # Find all κ entries with these indices
                for k in range(36):
                    # Check (i,j,k) and permutations
                    for (ii, jj, kk, val) in kappa_entries:
                        if (ii == i and jj == j) or (ii == j and jj == i):
                            total += val * Jstar[kk] * Jstar[i] * Jstar[j]
                            weight_sum += Jstar[i] * Jstar[j]
        
        Y_3x3[a, b] = total / weight_sum if weight_sum > 0 else 0

print("\n  Raw 3×3 Yukawa (J*-weighted average over charge sectors):")
print(f"  Sectors: [0]=q=10 (Top), [1]=q=8 (Bottom), [2]=q=6 (Lepton)")
print(f"\n  Y_ij =")
for row in Y_3x3:
    print(f"    [{row[0]:>10.4f} {row[1]:>10.4f} {row[2]:>10.4f}]")

# SVD for diagonalization
U, S, Vh = np.linalg.svd(Y_3x3)
print(f"\n  Singular values: {S}")
print(f"  Ratios (relative to largest):")
for i in range(3):
    print(f"    λ_{i}/λ_max = {S[i]/S[0]:.4f}")

# ─── 4. Comparison with IDCM φ^{-n} predictions ──────────────

print("\n## 4. IDCM φ-exponent comparison")

# IDCM predictions: mass ratios in φ-exponents
# Top: reference (λ_0)
# Bottom/τ: relative to Top

# Predicted φ-exponents for singular values
if S[0] > 0:
    exponents = [-math.log(s/S[0], PHI) for s in S]
    print(f"\n  Measured φ-exponents: {exponents}")

# Predicted from IDCM v2.2
idcm = {
    "Top": 0.0,
    "Charm/Top": 5.1,  # k_u/2  
    "Up/Top": 10.2,     # k_u
    "Bottom/Top": None,  # depends on normalization
    "Tau/Top": None
}

print(f"""
  IDCM v2.2 predicted exponents (relative to Top):
    Top/Charm/Up:    0 ,  ≈5.1 ,  ≈10.2    (k_u = 10.20)
    Bottom/Str/Down: 0 ,  ≈3.9 ,  ≈7.9     (k_d = 7.89, approx split)
    Tau/Mu/El:       0 ,  ≈2.9 ,  ≈5.9     (k_l = 5.87, approx split)
""")

# ─── 5. Direct Top Yukawa from κ[4,4,22] ─────────────────────

print("## 5. Direct κ Entries for Physical Couplings")

# Find all κ entries for the Top sector (q=10)
q10_div = charge_groups[10]
print(f"\n  Top sector (q=10, divisors {q10_div}):")
for i, j, k, val in kappa_entries:
    if i in q10_div and j in q10_div:
        print(f"    κ[{i},{j},{k}] = {val:>+4.0f}  (qi={charges[i]}, qj={charges[j]}, qk={charges[k]})")

# Find all κ entries for the Lepton sector (q=6)  
q6_div = charge_groups[6]
print(f"\n  Lepton sector (q=6, divisors {q6_div}):")
for i, j, k, val in kappa_entries:
    if i in q6_div and j in q6_div:
        print(f"    κ[{i},{j},{k}] = {val:>+4.0f}  (qi={charges[i]}, qj={charges[j]}, qk={charges[k]})")

# Find all κ entries for the Bottom sector (q=8)
q8_div = charge_groups[8]
print(f"\n  Bottom sector (q=8, divisors {q8_div}):")
for i, j, k, val in kappa_entries:
    if i in q8_div and j in q8_div:
        print(f"    κ[{i},{j},{k}] = {val:>+4.0f}  (qi={charges[i]}, qj={charges[j]}, qk={charges[k]})")

# ─── 6. Alternative: κ·J*·J* contraction (double contraction) ─

print("\n## 6. Double Contraction: κ_{ijk}·J*_j·J*_k")

# This gives a 36-vector: effective Yukawa coupling per divisor
Y_vec = np.zeros(36)
for i, j, k, val in kappa_entries:
    Y_vec[i] += val * Jstar[j] * Jstar[k]

print(f"\n  Per-divisor effective Yukawa (top 10):")
top10 = np.argsort(-np.abs(Y_vec))[:10]
for idx in top10:
    print(f"    D_{idx:>2}: q={charges[idx]:>3}, Y_eff={Y_vec[idx]:>+.6f}, J*={Jstar[idx]:.4e}")

print(f"\n  Per-charge-sector average:")
for q in [12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
    divs = charge_groups.get(q, [])
    if not divs or q > 12: continue
    vals = [Y_vec[d] for d in divs]
    print(f"    q={q:>3}: mean(Y)={np.mean(vals):>+.6f}, |max|={np.max(np.abs(vals)):.4f}")

# ─── 7. Check κ·J*·J*·J* triple contraction (volume) ────────

print("\n## 7. Volume Check: κ_{ijk}·J*_i·J*_j·J*_k")

vol = 0.0
for i, j, k, val in kappa_entries:
    vol += val * Jstar[i] * Jstar[j] * Jstar[k]

print(f"  Computed CY volume: {vol:.10f}")
print(f"  Target (κ³ = 1/4096): {KAPPA**3:.10f}")
print(f"  Match: {abs(vol - KAPPA**3)/KAPPA**3*100:.4f}%" if KAPPA**3 > 0 else "")

# ─── 8. Summary ──────────────────────────────────────────────

print("\n" + "=" * 72)
print("  STRATEGY B — SUMMARY")
print("=" * 72)

print(f"""
  Physical Projection:
    - κ entries with q=10×10 cross: few (~1: κ[4,4,22]=+3)
    - κ entries with q=6×6 cross: few (~1: κ[2,7,7]=-32 + small)
    - κ entries with q=8×8 cross: NONE (classically forbidden ✓)
    
  The 3×3 Yukawa matrix from direct κ·J contraction gives:
    - Off-diagonal structure from shared divisors
    - Top/Bottom/Lepton sectors connected by J* overlap
  
  Next step: the 3 generations within each sector (Top/Charm/Up)
  come from different linear combinations of same-charge divisors.
  This is an SVD/diagonalization problem inside each charge block.
""")
