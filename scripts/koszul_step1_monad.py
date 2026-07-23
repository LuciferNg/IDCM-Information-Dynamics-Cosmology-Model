#!/usr/bin/env python3
"""
Phase Koszul Step 1: Extract Monad Definition Data from CY₃(36,98)
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json

BASE = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search"

print("="*72)
print("KOSZUL STEP 1 — Monad Definition from GLSM")
print("="*72)

# Load CY
poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate(backend="qhull")
cy = tri.get_cy()
print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}, dim_ambient={cy.ambient_dim()}")

# GLSM charge matrix
glsm = np.array(cy.glsm_charge_matrix())
print(f"GLSM: {glsm.shape} — {glsm.shape[0]} divisor basis × {glsm.shape[1]} charges")

# Divisor basis → ray mapping
basis_rays = cy.divisor_basis()
print(f"Divisor basis: {len(basis_rays)} rays → indices {basis_rays}")

# Fan information
print(f"Ambient variety: {cy.ambient_dim()}D, {len(cy.rays()) if hasattr(cy, 'rays') else '?'} rays")

# ============================================================
# GLSM charge structure analysis
# ============================================================
print("\n=== GLSM Charge Structure ===")

# Statistics per charge column
charge_cols = glsm.T  # (37, 32)
print(f"Charge columns (37 rays × 32 charges):")
for ray_idx in range(min(10, charge_cols.shape[0])):
    row = charge_cols[ray_idx]
    print(f"  Ray {ray_idx:>2}: min={row.min():>3}, max={row.max():>3}, nonzero={np.count_nonzero(row)}, pos={np.sum(row>0)}, neg={np.sum(row<0)}")

# Identify monad defining line bundles
# Standard Monad: 0 → V → ⊕_i O(a_i) → ⊕_j O(b_j) → 0
# where a_i = positive GLSM charges for "matter" fields
#       b_j = negative GLSM charges for "constraint" fields

# Method: Decompose the GLSM into positive bundles (a_i) and negative bundles (b_j)
# Exclude the "gauged" charges (those corresponding to the CFT)

# Extract the monad data: 
# For each ray, the GLSM charge vector determines which line bundle O(a) contributes
# The "dual" rays (negative charge under most U(1)s) define the constraint bundle

# Group rays by charge pattern
pos_mask = np.all(charge_cols >= 0, axis=1)
neg_mask = np.all(charge_cols <= 0, axis=1)
mixed_mask = ~(pos_mask | neg_mask)

print(f"\nRay charge patterns:")
print(f"  All non-negative (positive bundle O(a_i)): {np.sum(pos_mask)} rays")
print(f"  All non-positive (constraint bundle O(b_j)): {np.sum(neg_mask)} rays")
print(f"  Mixed signs: {np.sum(mixed_mask)} rays")

# The positive bundle B = ⊕ O(a_i) where a_i are the charge vectors of pos rays
# For the monad, B has rank = number of positive rays
# The constraint bundle C = ⊕ O(c_j) where c_j are charge vectors of mixed/neg rays

# List the positive rays
print(f"\nPositive rays (candidate B generators):")
for ray_idx in np.where(pos_mask)[0][:10]:
    print(f"  Ray {ray_idx:>2}: charges = {list(charge_cols[ray_idx][:8])}...")

# Extract charge vectors as divisor class integers
# Each 32-entry charge vector defines O(a) where a = Σ q_i D_i

print(f"\n=== Monad Data Export ===")

# The monad is 0 → V → B → C → 0
# B = ⊕ O(a_i) where a_i are 32D divisor class vectors (positive rays)
# C = ⊕ O(b_j) where b_j are 32D divisor class vectors (negative/mixed rays)

B_charges = [charge_cols[i].tolist() for i in np.where(pos_mask)[0]]
C_charges = [charge_cols[i].tolist() for i in np.where(~pos_mask)[0]]

print(f"B (positive bundle): rank = {len(B_charges)}")
print(f"  Examples: {B_charges[:3]}")
print(f"C (constraint bundle): rank = {len(C_charges)}")
print(f"  Examples: {C_charges[:3]}")

# The monad rank is: rk(V) = rk(B) - rk(C)
monad_rank = len(B_charges) - len(C_charges)
print(f"Monad rank: rk(V) = rk(B) - rk(C) = {len(B_charges)} - {len(C_charges)} = {monad_rank}")

# For a heterotic model, we need rk(V) = 4 or 5
# Expected: this should give rk(V) = 4 (the visible E₆ or SO(10) bundle)

# ============================================================
# Fan data export for SageMath
# ============================================================
print(f"\n=== Fan Export for SageMath ===")

# Get all rays (vertices of the polytope)
rays_list = cy.rays().tolist() if hasattr(cy, 'rays') else []
print(f"Number of rays: {len(rays_list)}")

# SR ideal from existing file
sr_pairs = []
with open(f"{BASE}/data/cy36_98_chomcalg_sr.in") as f:
    for line in f:
        if 'srideal' in line:
            # Parse [vX*vY]
            import re
            matches = re.findall(r'\[v(\d+)\*v(\d+)\]', line)
            for m in matches:
                sr_pairs.append([int(m[0]), int(m[1])])
print(f"SR ideal pairs: {len(sr_pairs)}")

# Export everything to JSON for SageMath
monad_data = {
    "glsm_shape": list(glsm.shape),
    "basis_rays": basis_rays,
    "num_rays_in_fan": len(rays_list),
    "B_charges": B_charges,
    "C_charges": C_charges,
    "monad_rank": monad_rank,
    "sr_ideal_pairs": sr_pairs[:10],  # truncated for readability
    "sr_ideal_count": len(sr_pairs),
}

# Save
output_path = f"{BASE}/data/monad_definition.json"
with open(output_path, "w") as f:
    json.dump(monad_data, f, indent=2)
print(f"\nMonad data saved to {output_path}")

# ============================================================
# Key Divsor Classes for Yukawa
# ============================================================
print(f"\n=== Physical Sector Divisors ===")
# Load κ-vector and AA for sector identification
kv = np.load(f"{BASE}/data/kappa_vector_jstar.npy")
aa = np.load(f"{BASE}/data/AA_jstar.npy")
Jstar = np.array(json.load(open(f"{BASE}/data/Jstar_36D.json"))["Jstar_36D"])[:32]

# For each B-ray, compute its Kähler pairing at J*
print(f"B-ray divisor classes at J*:")
for i, ray_idx in enumerate(np.where(pos_mask)[0][:5]):
    charge_vec = charge_cols[ray_idx]
    # The divisor class is D = Σ charge_q * D_q
    # Evaluate D · J* = Σ charge_q * (J*)_q
    dj = sum(charge_vec[q] * Jstar[q] for q in range(min(32, len(charge_vec))))
    print(f"  Ray {ray_idx:>2}: Σq·J* = {dj:.4f}, charges = {list(charge_vec[:8])}...")

print("\n✅ Koszul Step 1 — Complete")
print(f"Monad rank = {monad_rank}")
print(f"Next: Step 2 — Build SageMath monad bundle and compute Koszul LES")
