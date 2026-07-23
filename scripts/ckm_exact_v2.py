#!/usr/bin/env python3
"""
CKM EXACT v2 — Proper divisor basis projection
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json, math

PHI = (1 + 5**0.5) / 2
BASE = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search"

print("="*60)
print("CKM EXACT v2 — Divisor basis Yukawa")
print("="*60)

# Load J* and project to divisor basis
with open(f"{BASE}/data/Jstar_36D.json") as f:
    Jstar = np.array(json.load(f)["Jstar_36D"])
Jstar_32 = Jstar[:32]  # Divisor basis is first 32 components

# Build CY
poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate(backend="qhull")
cy = tri.get_cy()

# Get GLSM charges for 32 basis divisors
glsm = cy.glsm_charge_matrix()
print(f"GLSM matrix: {glsm.shape}")

# coord3 charges for physical sector identification
coord3 = [glsm[i][2] if len(glsm[i]) > 2 else glsm[i][0] for i in range(min(32, len(glsm)))]
print(f"coord3 charges (first 10): {coord3[:10]}")

# Group divisors by charge
charge_groups = {}
for i, q in enumerate(coord3):
    charge_groups.setdefault(q, []).append(i)
for q in sorted(charge_groups.keys()):
    print(f"  q={q:>3}: divisors {charge_groups[q]}")

# compute_kappa_vector at J*[:32]
print("\n--- kappa_vector at J*32 ---")
kv = cy.compute_kappa_vector(Jstar_32.tolist())
kv_arr = np.array(kv)
print(f"kappa_vector shape: {kv_arr.shape}")

# φ-exponent hierarchy
flat = np.abs(kv_arr.flatten())
top_kv = sorted(flat)[::-1][:20]
print(f"Top 20 kappa magnitudes:")
for i in range(min(20, len(top_kv))):
    if top_kv[i] > 1e-100:
        exp = -math.log(top_kv[i]/top_kv[0], PHI) if top_kv[0] > 1e-100 else float('inf')
        print(f"  λ_{i}: {top_kv[i]:.8e}  φ^{exp:.3f}")

# compute_AA at J*32
print("\n--- compute_AA at J*32 ---")
aa = cy.compute_AA(Jstar_32.tolist())
aa_arr = np.array(aa)
print(f"AA shape: {aa_arr.shape}")
flat_aa = np.abs(aa_arr.flatten())
top_aa = sorted(flat_aa)[::-1][:20]
for i in range(min(20, len(top_aa))):
    if top_aa[i] > 1e-100:
        exp = -math.log(top_aa[i]/top_aa[0], PHI) if top_aa[0] > 1e-100 else float('inf')
        print(f"  AA_{i}: {top_aa[i]:.8e}  φ^{exp:.3f}")

# Project AA onto charge sectors: 
# The AA is a 32×32 matrix. The physical Yukawa is the projection
# onto the 3 generation sectors determined by GLSM charges.
# q=12 → top/up (1 divisor)
# q=10 → charm (1 divisor)
# q=9  → strange/bottom (2 divisors)  
# q=8  → bottom (1 divisor)
# q=6  → lepton (4 divisors)
# q=5,7,4 → mixing

# For the CKM, we only need the up and down quark Yukawa eigenvalues.
# The up Yukawa comes from q=12 (D₂) and q=10 (D₄) sectors.
# The down Yukawa comes from q=9 (D₅, D₁₈) and q=8 (D₆) sectors.

print("\n--- CKM from AA eigenvalues ---")
# AA is a 32×32 matrix in the divisor basis
# The eigenvalues correspond to physical Yukawa scales at J*
eigvals = sorted(np.abs(np.linalg.eigvalsh(aa_arr)))[::-1]

print(f"Top 10 AA eigenvalues:")
for i in range(min(10, len(eigvals))):
    if eigvals[i] > 1e-100:
        exp = -math.log(eigvals[i]/eigvals[0], PHI) if eigvals[0] > 1e-100 else float('inf')
        print(f"  λ_{i}: {eigvals[i]:.8e}  φ^{exp:.3f}")

# CKM mixing: identify mixing between charge sectors
# Look at off-diagonal AA entries connecting charge groups
print("\n--- Charge sector mixing (CKM-like) ---")
# For each charge group pair, compute effective mixing strength
glsm_charges_with_indices = list(zip(range(32), coord3))

# Compute block norms
for q1 in sorted(charge_groups.keys()):
    for q2 in sorted(charge_groups.keys()):
        if q1 >= q2: continue
        indices1 = charge_groups[q1]
        indices2 = charge_groups[q2]
        block = aa_arr[np.ix_(indices1, indices2)]
        # Frobenius norm of the mixing block
        norm = np.linalg.norm(block, 'fro')
        if norm > 1e-6:
            # Normalize by sector sizes
            n1, n2 = len(indices1), len(indices2)
            print(f"  q={q1:>3}↔q={q2:>3}: ||·||_F = {norm:.6e}  (size: {n1}×{n2})")

# Key CKM ratio from mixing  
print("\n--- CKM elements from AA ---")
# V_cb-like: mixing between q=8 (bottom) and q=10 (charm)
# V_us-like: mixing between q=12 (top/up generator) and q=7 (down generator)
d12_idxs = charge_groups.get(12, [])
d10_idxs = charge_groups.get(10, [])
d8_idxs = charge_groups.get(8, [])
d7_idxs = charge_groups.get(7, [])
d6_idxs = charge_groups.get(6, [])

# V_cb proxy: mixing between q=8 and q=10 sectors
if d8_idxs and d10_idxs:
    vcb_block = aa_arr[np.ix_(d8_idxs, d10_idxs)]
    vcb_norm = np.linalg.norm(vcb_block, 'fro')
    print(f"\n  V_cb (q=8↔q=10 block norm): {vcb_norm:.6e}")
    print(f"  IDCM formula: φ^(-{33/5:.1f}) = {PHI**(-33/5):.6f}")
    print(f"  PDG V_cb: ~0.0418")

# V_us proxy: mixing between q=12 and appropriate down sectors
if d12_idxs and d7_idxs:
    vus_block = aa_arr[np.ix_(d12_idxs, d7_idxs)]
    vus_norm = np.linalg.norm(vus_block, 'fro')
    print(f"\n  V_us (q=12↔q=7 block norm): {vus_norm:.6e}")
    print(f"  IDCM formula: φ^(-{33/11:.1f}) = {PHI**(-33/11):.6f}")
    print(f"  PDG V_us: ~0.2243")

# Save results
output = {
    "aa_shape": list(aa_arr.shape),
    "aa_eigenvalues_top10": [float(x) for x in eigvals[:10]],
    "kappa_top10": [float(x) for x in top_kv[:10]],
    "charge_groups": {str(k): v for k, v in charge_groups.items()},
    "cy_volume": float(cy.compute_cy_volume(Jstar_32.tolist()))
}
with open(f"{BASE}/data/ckm_exact_results.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to ckm_exact_results.json")

print("\n✅ CKM EXACT v2 — Complete")
