#!/usr/bin/env python3
"""
CYTools compute_AA — QHull triangulation backend
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np

print("="*72)
print("CYTools A-MODEL — QHull triangulation backend")
print("="*72)

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
print(f"Polytope dim={poly.dim()}")

# Force PPL backend for polytope (already default for dim<=4)
# Use QHull for triangulation instead of CGAL
print("Using QHull for triangulation...")
tri = poly.triangulate(backend="qhull")
print(f"Triangulation: {len(tri.simplices())} simplices")

cy = tri.get_cy()
print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}")
print(f"Smooth: {cy.is_smooth()}")

# List methods
compute_methods = sorted(m for m in dir(cy) if m.startswith('compute_'))
print(f"\nAvailable compute methods ({len(compute_methods)}):")
for m in compute_methods:
    print(f"  - {m}")

# compute_kappa_vector (works without CGAL)
print("\nTrying compute_kappa_vector()...")
try:
    kv = cy.compute_kappa_vector()
    kv_arr = np.array(kv)
    print(f"kappa_vector shape: {kv_arr.shape}")
    print(f"kappa_vector (first 10): {kv_arr[:10]}")
    # φ-exponent ratio
    phi = (1+5**0.5)/2
    top_vals = sorted(np.abs(kv_arr.flatten()))[::-1][:10]
    print(f"Top magnitudes: {top_vals}")
    for i in range(min(10, len(top_vals))):
        if top_vals[i] > 0:
            exp = -np.log(top_vals[i]/top_vals[0])/np.log(phi)
            print(f"  λ_{i} = {top_vals[i]:.6e} → φ^{exp:.3f}")
except Exception as e:
    print(f"compute_kappa_vector error: {e}")

# compute_AA
print("\nTrying compute_AA()...")
try:
    aa = cy.compute_AA()
    if isinstance(aa, dict):
        print(f"Keys (first 10): {list(aa.keys())[:10]}")
    elif isinstance(aa, list):
        aa_arr = np.array(aa)
        print(f"AA shape: {aa_arr.shape}")
    else:
        print(f"AA type: {type(aa)}, value: {str(aa)[:200]}")
except Exception as e:
    print(f"compute_AA error: {e}")
