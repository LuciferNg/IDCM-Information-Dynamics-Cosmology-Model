#!/usr/bin/env python3
"""
Brute force monomial search for monad map entries.

Each entry f_{pq} has degree deg_{pq} = charge(B_p) - charge(C_q).
We need to find monomials in 37 coordinates matching that degree.
"""
import json, numpy as np, itertools, sys
from pathlib import Path

BASE = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
OUT = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/monad_map_search")

# ── Load data ──
with open(BASE / "monad_definition.json") as f:
    md = json.load(f)
with open(OUT / "bc_assignment.json") as f:
    bc = json.load(f)

glsm = np.array(md["glsm_charge_matrix"], dtype=int)  # (37, 32)

B_rays = bc["best_B"]
C_rays = bc["best_C"]
zeros_needed = bc["zeros_needed"]

# Build full B/C lists with O(0) fill
full_B = B_rays + ["O0"] * zeros_needed
full_C = C_rays

print("=" * 70)
print("MONAD MAP — BRUTE FORCE MONOMIAL SEARCH")
print("=" * 70)

print(f"\nB ({len(full_B)} summands): {[f'Ray{r}' if isinstance(r,int) else r for r in full_B]}")
print(f"C ({len(full_C)} summands): {[f'Ray{r}' for r in full_C]}")

# ── Degree matrix ──
print(f"\n{'─'*70}")
print(f"{'Entry':<12} {'Deg nnz':<10} {'Charge range':<30} {'Possible monomials?'}")
print(f"{'─'*70}")

for p in range(len(full_B)):
    if isinstance(full_B[p], int):
        bp = glsm[full_B[p]]
        bp_label = f"R{full_B[p]}"
    else:
        bp = np.zeros(32, dtype=int)
        bp_label = "O(0)"
    
    for q in range(len(full_C)):
        cq = glsm[full_C[q]]
        deg = bp - cq
        nnz = np.count_nonzero(deg)
        deg_min, deg_max = int(deg.min()), int(deg.max())
        
        # Quick check: is this monomial realizable?
        # A monomial in 37 variables: deg = Σ a_i * charge(ray_i)
        # So we need a non-negative integer solution a_i >= 0
        # For a single entry: deg must be in the cone spanned by all rays
        
        label = f"f_{{{p}{q}}}"
        rng = f"[{deg_min}, {deg_max}]"
        
        possible = "🟡" if deg_min <= 0 <= deg_max else "🔴"
        if nnz == 0:
            possible = "✅ constant"
        
        print(f"{label:<12} {nnz:<10} {rng:<30} {possible}")

# ── For each entry, try to find monomials (limited search) ──
print(f"\n{'='*70}")
print("DETAILED MONOMIAL SEARCH (sample)")
print(f"{'='*70}")

# For simplicity: focus on one entry at a time
# The monomial is x_0^a_0 ... x_36^a_36 where degree = Σ a_i * charge(ray_i)
# This is a linear Diophantine system in 37 variables

# Strategy: use the fact that coord rays are unit vectors
# Any monomial x_i has degree = charge(ray_i)
# Complex monomial = product of x_i^a_i → degree = Σ a_i * charge(ray_i)

# For a given degree vector d (32-dim), we need a_i >= 0 integer s.t.
# Σ a_i * glsm[i] = d

# Since 32 of the 37 rays are unit vectors e_j,
# we can always match ANY d by choosing a_i = max(d_j, 0) for some ...
# Actually the coord rays have charge = unit vectors with entry +1 at one position
# So for any d, the lowest-degree monomial is: x_{j+offset}^{d_j} for positive d_j

# But the deg might have negative entries — need negative charge rays
# Negative_noncoord rays supply negative charges

# Let's try for a couple sample entries:
sample_entries = [(0,0), (0,1), (1,0), (1,1), (2,0)]
for p, q in sample_entries:
    if p >= len(full_B) or q >= len(full_C):
        continue
    
    if isinstance(full_B[p], int):
        bp = glsm[full_B[p]]
    else:
        bp = np.zeros(32, dtype=int)
    
    cq = glsm[full_C[q]]
    deg = bp - cq
    
    print(f"\n  f_{{{p}{q}}}: deg = {deg[:8].tolist()}... (showing first 8/32)")
    
    # Positive part: use coord rays
    pos_mask = deg > 0
    pos_charges = deg[pos_mask]
    pos_indices = np.where(pos_mask)[0]
    
    # Proposed monomial: Π x_{coord_j}^{deg_j} for deg_j > 0
    monomial_parts = []
    for j, charge in zip(pos_indices[:10], pos_charges[:10]):
        # coord ray for U(1)_j is... need to find which ray has charge e_j
        coord_rays = [i for i in range(37) if np.count_nonzero(glsm[i]) == 1 
                      and glsm[i].sum() == 1 and glsm[i].max() == 1]
        # coord ray for j is the ray with glsm[ray][j] = 1
        coord_ray_j = None
        for ray in coord_rays:
            if glsm[ray][j] == 1:
                coord_ray_j = ray
                break
        if coord_ray_j is not None and charge > 0:
            monomial_parts.append(f"x_{coord_ray_j}^{charge}")
    
    if monomial_parts:
        print(f"  → Tentative monomial: {' · '.join(monomial_parts[:5])}")
        if len(pos_charges) > 5:
            print(f"    ... + {len(pos_charges)-5} more terms")
    else:
        print(f"  → All deg ≤ 0, only negative rays contribute")

print(f"\n{'='*70}")
print("NEXT STEP: Full monomial enumeration + SR ideal check")
print(f"{'='*70}")
print("""
The monad map f is a matrix of monomials. Each entry must:
1. Have the correct degree vector (U(1) charges)
2. Use only coordinates NOT in the SR ideal at that position
3. Be injective at J* (the Kähler stabilization point)

The SR ideal for CY₃(36,98) has 450+ pairs — need to filter monomials.
See 04_SR_IDEAL.md for details.
""")