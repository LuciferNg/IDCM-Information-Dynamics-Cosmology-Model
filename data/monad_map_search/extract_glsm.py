#!/usr/bin/env python3
"""
Extract GLSM charge matrix from monad_definition.json and compute monad map degrees.
"""
import json, numpy as np, itertools, os, sys
from pathlib import Path

BASE = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
OUT = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/monad_map_search")

# ── Load data ──
with open(BASE / "monad_definition.json") as f:
    md = json.load(f)

glsm_raw = md["glsm_charge_matrix"]  # 37 lists of 32 ints
glsm = np.array(glsm_raw, dtype=int)  # shape (37, 32)

print(f"GLSM charge matrix: {glsm.shape}")
print(f"  Rows (rays): {glsm.shape[0]}")
print(f"  Cols (U(1)): {glsm.shape[1]}")

# ── Ray classification ──
coord_rays = []
noncoord_rays = []
pos_rays = []
neg_rays = []
zero_rays = []
mixed_rays = []

for i in range(37):
    row = glsm[i]
    nnz = np.count_nonzero(row)
    total = row.sum()
    is_coord = (nnz == 1 and total == 1 and row.max() == 1)
    
    if is_coord:
        coord_rays.append(i)
    else:
        noncoord_rays.append(i)
        if np.all(row >= 0) and np.any(row > 0):
            pos_rays.append(i)
        elif np.all(row <= 0) and np.any(row < 0):
            neg_rays.append(i)
        elif np.all(row == 0):
            zero_rays.append(i)
        else:
            mixed_rays.append(i)

print(f"\nCoordinate rays (32 total):")
print(f"  Indices: {sorted(coord_rays)}")

print(f"\nNon-coordinate rays (5 total):")
for i in sorted(noncoord_rays):
    row = glsm[i]
    print(f"  Ray {i:>2}: sum={int(row.sum()):>4}  min={int(row.min()):>4}  max={int(row.max()):>4}  nnz={np.count_nonzero(row)}")

print(f"\n  Positive: {sorted(pos_rays)}")
print(f"  Negative: {sorted(neg_rays)}")
print(f"  Mixed:    {sorted(mixed_rays)}")

# ── Brute force B/C assignment ──
print(f"\n{'='*60}")
print(f"B/C ASSIGNMENT SEARCH")
print(f"{'='*60}")

best_err = 1e18
best_soln = None
best_mask = None

for mask in range(1 << len(noncoord_rays)):
    B_list = []
    C_list = []
    for j, ray in enumerate(noncoord_rays):
        if (mask >> j) & 1:
            B_list.append(ray)
        else:
            C_list.append(ray)
    
    B_sum = sum(glsm[i] for i in B_list) if B_list else np.zeros(32, dtype=int)
    C_sum = sum(glsm[i] for i in C_list) if C_list else np.zeros(32, dtype=int)
    
    c1 = B_sum - C_sum
    err = int(np.sum(np.abs(c1)))
    
    rk = len(B_list) - len(C_list)
    
    if rk <= 4:
        zeros_needed = 4 - rk
        total_B = len(B_list) + zeros_needed
        total_C = len(C_list)
        
        if err < best_err:
            best_err = err
            best_soln = (B_list, C_list, zeros_needed, c1)
            best_mask = mask

B_list, C_list, zeros_needed, c1 = best_soln
print(f"\nBest assignment (err={best_err}):")
print(f"  B rays: {sorted(B_list)}")
print(f"  C rays: {sorted(C_list)}")
print(f"  O(0) fill in B: {zeros_needed}")
print(f"  rk(V) = {len(B_list) + zeros_needed} - {len(C_list)} = {len(B_list) + zeros_needed - len(C_list)}")

c1_nz = np.where(np.abs(c1) > 0)[0]
print(f"\n  c₁(V) non-zero entries: {len(c1_nz)}")
if len(c1_nz) > 0:
    print(f"  c₁(V) non-zero indices (first 10): {c1_nz[:10].tolist()}")
    print(f"  c₁(V) values at those: {c1[c1_nz[:10]].tolist()}")
    print(f"\n  ❌ c₁(V) ≠ 0 — need coordinate ray shift")
    print(f"  Each O(-e_j) in C cancels c₁ entry at U(1)_j")
else:
    print(f"  ✅ c₁(V) = 0")

# ── Compute degree matrix ──
print(f"\n{'='*60}")
print(f"MONAD MAP DEGREE MATRIX")
print(f"{'='*60}")

# Full B and C with zeros
full_B = B_list[:]
full_C = C_list[:]
# Add O(0) summands to B (zero charge vectors)
for _ in range(zeros_needed):
    full_B.append("O(0)")

# Degree matrix: deg(f_{pq}) = charge(B_p) - charge(C_q)
print(f"\nB summands: {[f'Ray{r}' for r in B_list]} + O(0)×{zeros_needed}")
print(f"C summands: {[f'Ray{r}' for r in C_list]}")
print(f"\nEntries need to be monomials in 37 homogeneous coordinates")
print(f"Each monomial's degree vector must match the charge difference.")

# Print degree matrix (compact)
print(f"\nDegree matrix (U(1) charge differences):")
nB = len(full_B)
nC = len(full_C)
for p in range(nB):
    if isinstance(full_B[p], int):
        bp = glsm[full_B[p]]
    else:
        bp = np.zeros(32, dtype=int)
    print(f"\n  B[{p}] {'Ray'+str(full_B[p]) if isinstance(full_B[p],int) else 'O(0)'}:")
    for q in range(nC):
        cq = glsm[full_C[q]]
        deg = bp - cq
        nnz = np.count_nonzero(deg)
        rng = f"[{int(deg.min())},{int(deg.max())}]"
        print(f"    → C[{q}] Ray{full_C[q]}: deg nnz={nnz:>2} range={rng:>10}")

# ── Save results ──
result = {
    "coord_rays": sorted(coord_rays),
    "noncoord_rays": sorted(noncoord_rays),
    "pos_rays": sorted(pos_rays),
    "neg_rays": sorted(neg_rays),
    "mixed_rays": sorted(mixed_rays),
    "best_B": sorted(B_list),
    "best_C": sorted(C_list),
    "zeros_needed": zeros_needed,
    "c1_nz_count": int(len(c1_nz)),
    "c1_nz_indices": c1_nz.tolist() if len(c1_nz) > 0 else [],
    "c1_nz_values": c1[c1_nz].tolist() if len(c1_nz) > 0 else [],
}

with open(OUT / "bc_assignment.json", "w") as f:
    json.dump(result, f, indent=2)

print(f"\n✅ Results saved to {OUT / 'bc_assignment.json'}")