#!/usr/bin/env python3
"""
CYTools compute_AA at J* — Exact CKM from CY₃(36,98)
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json, math, sys

PHI = (1 + 5**0.5) / 2
BASE = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search"

print("="*60)
print("CKM EXACT — CYTools compute_AA at J*")
print("="*60)

# Load J*
with open(f"{BASE}/data/Jstar_36D.json") as f:
    jdata = json.load(f)
Jstar = np.array(jdata["Jstar_36D"])
print(f"J* loaded: {len(Jstar)}D")

# Build CY
poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate(backend="qhull")
cy = tri.get_cy()
print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}, χ={cy.chi()}")

# Try compute_kappa_vector at J*
print("\n--- compute_kappa_vector at J* ---")
try:
    kv = cy.compute_kappa_vector(Jstar.tolist())
    kv_arr = np.array(kv)
    print(f"kappa_vector shape: {kv_arr.shape}")
    print(f"kappa_vector (first 10): {kv_arr[:10]}")
    # Top magnitudes
    top = sorted(np.abs(kv_arr.flatten()))[::-1][:10]
    print(f"Top 10: {top}")
    for i in range(min(10, len(top))):
        if top[i] > 0:
            exp = -math.log(top[i]/top[0], PHI) if top[i] > 1e-100 else float('inf')
            print(f"  λ_{i} = {top[i]:.6e}  →  φ^{exp:.3f}")
except Exception as e:
    print(f"kappa_vector error: {e}")

# Try compute_AA at J*
print("\n--- compute_AA at J* ---")
try:
    aa = cy.compute_AA(Jstar.tolist())
    aa_arr = np.array(aa)
    print(f"AA shape: {aa_arr.shape}")
    if aa_arr.ndim == 3:
        # 3-tensor: Yukawa couplings
        flat = aa_arr.flatten()
        top = sorted(np.abs(flat))[::-1][:10]
        print(f"Top 10 AA: {top}")
        for i in range(min(10, len(top))):
            if abs(top[i]) > 1e-100:
                exp = -math.log(abs(top[i])/abs(top[0]), PHI) if abs(top[0]) > 1e-100 else float('inf')
                print(f"  AA_{i} = {top[i]:.6e}  →  φ^{exp:.3f}")
    elif aa_arr.ndim == 2:
        print(f"AA (5x5):\n{aa_arr[:5,:5]}")
    else:
        print(f"AA flat (first 10): {aa_arr[:10]}")
except Exception as e:
    print(f"compute_AA error: {e}")
    import traceback
    traceback.print_exc()

# Try compute_cy_volume at J*
print("\n--- CY volume ---")
try:
    vol = cy.compute_cy_volume(Jstar.tolist())
    print(f"Vol(CY) @ J* = {vol}")
except Exception as e:
    print(f"volume error: {e}")

# Try kappa_matrix
print("\n--- kappa_matrix ---")
try:
    km = cy.compute_kappa_matrix(Jstar.tolist())
    km_arr = np.array(km)
    print(f"kappa_matrix shape: {km_arr.shape}")
except Exception as e:
    print(f"kappa_matrix error: {e}")

print("\n✅ Done")
