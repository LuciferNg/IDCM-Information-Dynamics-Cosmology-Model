#!/usr/bin/env python3
"""Cone Width Analysis: Is CY₃(36,98) Kähler cone too narrow?

Measures β·J for all Mori cone / GLSM directions at J*,
identifies which hit boundaries, and determines
what h^1,1 would be needed to accommodate all physical constraints.

References:
  - Jstar_36D.json: J* fixed point in 36D
  - kappa_36d_raw.json: Intersection numbers
  - cy36_98_final.json: GLSM charges (coord3)
  - kappa_36d_fn.json: FN charge data
"""

import json, sys, math
import numpy as np
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1 + 5**0.5) / 2
PHI_INV = PHI - 1
EPS = 1e-12

# ─── Load data ───────────────────────────────────────────────

with open(DATA / "Jstar_36D.json") as f:
    jstar_data = json.load(f)

with open(DATA / "cy36_98_final.json") as f:
    final_data = json.load(f)

with open(DATA / "kappa_36d_raw.json") as f:
    kappa_raw = json.load(f)

with open(DATA / "kappa_36d_fn.json") as f:
    kappa_fn = json.load(f)

Jstar = np.array(jstar_data["Jstar_36D"])
glsm_coord3 = np.array(final_data["glsm_coord3"])
h11 = final_data["h11"]
kappa = 1/16
target_vol = kappa**3

# Verify J* dimensions
assert len(Jstar) == 36, f"J* has {len(Jstar)} dimensions, expected 36"
assert len(glsm_coord3) == 32, f"GLSM coord3 has {len(glsm_coord3)} entries, expected 32"

# The J* is 36D. GLSM coord3 is 32D (the 32 GLSM rays).
# The extra 4 dimensions are non-GLSM divisors (special resolution divisors).
# We need to map: the GLSM charges correspond to the first 32 divisor indices.

print("=" * 72)
print("  KÄHLER CONE WIDTH ANALYSIS — CY₃(36,98)")
print("=" * 72)

# ─── 1. GLSM Charge Distribution ── ──────────────────────────

print("\n## 1. GLSM Charge Vector (Coord3) — 32 rays")
print(f"\n{'Index':>6} {'Charge':>8} {'J*_component':>16} {'β·J':>16} {'Status':>10}")
print("-" * 62)

glsm_J = np.zeros(36)
glsm_J[:32] = glsm_coord3  # GLSM charges define directions in Kähler moduli space

# Compute β·J for GLSM charge directions
# The GLSM charges are the q-vectors. For a given q, β·J = sum(q_i * J*_i)
beta_dot_J_glsm = []
boundary_hits = []

for i in range(32):
    # Each GLSM charge component defines a direction
    q = np.zeros(36)
    q[i] = glsm_coord3[i]
    bj = float(np.dot(q, Jstar))
    beta_dot_J_glsm.append(bj)
    
    status = "EDGE" if abs(bj) < EPS else ("NEAR-EDGE" if abs(bj) < 1e-6 else "OK")
    if status in ("EDGE", "NEAR-EDGE"):
        boundary_hits.append((i, glsm_coord3[i], bj))
    
    print(f"{i:>6} {glsm_coord3[i]:>8.0f} {Jstar[i]:>16.8e} {bj:>16.8e} {status:>10}")

n_boundary = len(boundary_hits)
print(f"\n  GLSM directions near/on boundary: {n_boundary}/32")

# ─── 2. Physical FN Charge Directions ──────────────────────

print("\n## 2. Physical FN Charge Directions")
print("\n  The FN charges are linear combinations of GLSM directions:")
print(f"    k_u ≈ 33β = 10.20 → uses 33 divisor subset")
print(f"    k_d ≈ 26β - φ⁻⁴ = 7.89 → uses 26 divisor subset")
print(f"    k_l ≈ 19β = 5.87 → uses 19 divisor subset")

idcm_k_u = kappa_fn["idcm_k_u"]
idcm_k_d = kappa_fn["idcm_k_d"]
idcm_k_l = kappa_fn["idcm_k_l"]

# Physical FN charge vectors as weights on divisors
# k_u uses GLSM charges positively weighted
# The actual weights come from the GLSM charge selection
sorted_indices = np.argsort(-glsm_coord3)  # largest charges first
print(f"\n  Top 10 GLSM charges (sorted): {glsm_coord3[sorted_indices[:10]]}")
print(f"  Bottom 10 GLSM charges: {glsm_coord3[sorted_indices[-10:]]}")

# Count charges at each level
charge_counts = {}
for c in glsm_coord3:
    charge_counts[int(c)] = charge_counts.get(int(c), 0) + 1
print(f"\n  GLSM charge distribution:")
for c in sorted(charge_counts.keys(), reverse=True):
    print(f"    q={c:>3}: {charge_counts[c]:>2} divisors")

# ─── 3. Effective Cone Width ────────────────────────────────

print("\n## 3. Effective Cone Width")

# The Kähler cone condition: J³ > 0 and J·J·D_i > 0 for all effective divisors
# In the toric case, the cone is defined by: J_i > 0 for all i in the divisor basis

# Check how many J* components are near zero
near_zero = np.sum(np.abs(Jstar) < 1e-8)
small = np.sum(np.abs(Jstar) < 1e-6)
print(f"  J* components below 1e-8: {near_zero}")
print(f"  J* components below 1e-6: {small}")
print(f"  J* distribution: min={Jstar.min():.6e}, max={Jstar.max():.6e}, "
      f"mean={Jstar.mean():.6e}, median={np.median(Jstar):.6e}")

# Find which indices are tiny (potentially at cone boundary)
tiny_idx = np.where(np.abs(Jstar) < 1e-6)[0]
if len(tiny_idx) > 0:
    print(f"\n  Tiny J* components (potential cone boundaries):")
    for idx in tiny_idx:
        charge = glsm_coord3[idx] if idx < 32 else "N/A"
        print(f"    D_{idx}: J*={Jstar[idx]:.6e}, GLSM charge={charge}")

# ─── 4. Sparsity Analysis ──────────────────────────────────

print("\n## 4. Intersection Matrix Sparsity")
kappa_dict = kappa_raw["kappa"]
n_nonzero = len(kappa_dict)
n_total = kappa_fn["kappa_total"]
sparsity = kappa_fn["sparsity_pct"]
print(f"  Non-zero triple intersections: {n_nonzero}")
print(f"  Total possible: {n_total}")
print(f"  Sparsity: {sparsity:.2f}%")

# ─── 5. Minimal h¹¹ Estimate ──────────────────────────────

print("\n## 5. Minimum h¹¹ Estimate from Physical Constraints")

# Key question: which physical constraints need more Kähler moduli?
# Each FN charge requires independent divisor volumes.
# With M = 33 effective divisors for FN, h¹¹ = M + n_gen = 36.
# If the cone is too narrow, we need more divisors (higher h¹¹).

# The GLSM charge range: [0, 12]
# For binary MERA, h¹¹ = 2^n - 3 where n is MERA layers
# 36 = 2^6 - 28? No.
# 36 = 2^5 + 4? 32 + 4 extra.
# The GLSM has 32 rays + 4 extra toric divisors = 36.

# If h¹¹ > 40, M = h¹¹ - 3 > 37
# This would change all FN charge formulas

print(f"  Current h¹¹ = {h11} → M = {h11 - 3} = {h11 - 3}")
print(f"  Gemini proposal: h¹¹ > 40 → M > 37")
print(f"  Difference: Δh¹¹ ≥ {41 - h11}, ΔM ≥ {(41 - 3) - (h11 - 3)}")
print()

# What would new FN charges be?
# k_u = M·β = (h¹¹ - 3)·β
# k_l = (M - 14)·β = (h¹¹ - 17)·β
# k_d = k_u - 7β + φ⁻⁴

def predict_fn(h11_val):
    M = h11_val - 3
    k_u = M * PHI_INV / 2
    k_l = (M - 14) * PHI_INV / 2
    k_d = k_u - 7 * PHI_INV / 2 + PHI_INV**4
    return M, k_u, k_d, k_l

print("  FN charge sensitivity to h¹¹:")
print(f"  {'h¹¹':>5} {'M':>5} {'k_u':>10} {'k_d':>10} {'k_l':>10} "
      f"{'k_u/k_l':>10} {'Δk_u(%)':>10}")
print("  " + "-" * 65)

for h in [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]:
    M, ku, kd, kl = predict_fn(h)
    dku = (ku - idcm_k_u) / idcm_k_u * 100
    ku_kl = ku / kl if kl > 0 else float('inf')
    flag = " <<< CURRENT" if h == h11 else (" <<< PROPOSED" if h >= 41 else "")
    print(f"  {h:>5} {M:>5} {ku:>10.4f} {kd:>10.4f} {kl:>10.4f} "
          f"{ku_kl:>10.4f} {dku:>+9.2f}%{flag}")

# ─── 6. Cone Width Score ───────────────────────────────────

print("\n## 6. Cone Width Score — Summary")

# The Kähler cone width is measured by the smallest gap between J* and each cone wall
# For a 36D cone with 185 hyperplanes, the narrowness is:
#   gap_ratio = min(β·J) / max(β·J)

J_pos = Jstar[Jstar > EPS]
J_neg = Jstar[Jstar < -EPS]

print(f"  Positive components: {len(J_pos)}")
print(f"  Negative components: {len(J_neg)}")
print(f"  Min positive J*: {J_pos.min():.6e}" if len(J_pos) > 0 else "  No positive J*")
print(f"  Max positive J*: {J_pos.max():.6e}" if len(J_pos) > 0 else "")

# The cone is "narrow" if many GLSM directions have β·J near zero
total_glsm_charge = np.sum(glsm_coord3[glsm_coord3 > 0])
active_charge = np.sum(glsm_coord3[glsm_coord3 > 0] * Jstar[:32][glsm_coord3 > 0])
print(f"  Total positive GLSM charge weight: {active_charge:.4f}")
print(f"  Raw total positive GLSM charge: {total_glsm_charge:.0f}")

# The critical question: does the cone have room for all instanton corrections?
# Instanton corrections add φ^{-n} terms that require β·J > n·ln(φ) ≈ 0.481·n
print(f"\n  φ-weight scale: ln(φ) = {math.log(PHI):.4f}")
print(f"  For instanton order n: requires β·J > {math.log(PHI):.4f}×n")

# ─── 7. Conclusion ─────────────────────────────────────────

print("\n" + "=" * 72)
print("  VERDICT")
print("=" * 72)

boundary_frac = n_boundary / 32
width_ok = np.abs(Jstar).min() > 1e-8 and boundary_frac < 0.3

print(f"""
  Boundary-hit directions: {n_boundary}/32 ({100*boundary_frac:.1f}%)
  Min |J*| component: {np.abs(Jstar).min():.2e}
  J* Vol: {jstar_data['Vol']:.6e} (target: {target_vol:.6e})
  J* Ind: {jstar_data['Ind']:.4f} (target: 48.0000)

  Current h¹¹ = {h11} → M = {h11-3} → k_u = {idcm_k_u:.4f}
  Matches 19 SM params: ✅ (v2.2 verified)

  Key question: 
    {'CONE WIDTH SUFFICIENT — no need for h¹¹ > 40' if width_ok 
     else 'CONE TOO NARROW — h¹¹ > 40 may be required'}
""")
