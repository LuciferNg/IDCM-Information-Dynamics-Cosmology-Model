#!/usr/bin/env python3
"""
CYTools compute_AA — using QHull backend instead of CGAL
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
config.use_backend("qhull")  # Use QHull instead of CGAL
import numpy as np

print("="*72)
print("CYTools A-MODEL — QHull backend")
print("="*72)

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate()
cy = tri.get_cy()

print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}")
print(f"Smooth: {cy.is_smooth()}")

# Try compute_AA
print("\nTrying compute_AA()...")
try:
    aa = cy.compute_AA()
    print(f"compute_AA result type: {type(aa)}")
    if isinstance(aa, dict):
        print(f"Keys: {list(aa.keys())[:10]}")
        for k in list(aa.keys())[:5]:
            v = aa[k]
            print(f"  {k}: shape {np.array(v).shape if hasattr(v, '__len__') else v}")
    else:
        print(f"compute_AA returned: {aa}")
except Exception as e:
    print(f"compute_AA error: {e}")
    import traceback
    traceback.print_exc()

# Also try compute_kappa_vector
print("\nTrying compute_kappa_vector()...")
try:
    kv = cy.compute_kappa_vector()
    print(f"kappa_vector type: {type(kv)}")
    kv_arr = np.array(kv)
    print(f"kappa_vector shape: {kv_arr.shape}")
    print(f"kappa_vector (first 10): {kv_arr[:10]}")
except Exception as e:
    print(f"compute_kappa_vector error: {e}")

# List available methods
compute_methods = [m for m in dir(cy) if m.startswith('compute_')]
print(f"\nAll compute_* methods: {compute_methods}")
