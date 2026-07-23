#!/usr/bin/env python3
"""
CYTools compute_AA — use TOPCOM or patched CGAL path
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
# Patch CGAL path to use conda-installed CGAL
config.cgal_path = "/home/wsl/miniconda/envs/sage37/bin/"
import numpy as np, os, subprocess, sys

print("="*72)
print("CYTools A-MODEL — Patched CGAL path")
print("="*72)

# Check if cgal-triangulate-4d exists now
import glob
potential = glob.glob("/home/wsl/miniconda/envs/sage37/bin/*cgal*")
print(f"CGAL binaries: {potential}")

# If still missing, try to build the symlink
cgal_bin = config.cgal_path + "cgal-triangulate-4d"
if not os.path.exists(cgal_bin):
    print(f"CGAL triangulator not found at {cgal_bin}, trying alternative...")
    # Try TOPCOM or PPL
    try:
        poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
        # Use PPL for triangulation (dim <= 4, PPL works)
        tri = poly.triangulate(backend="cgal")  # Will fail
        print("CGAL worked!")
    except Exception as e:
        print(f"CGAL failed: {e}")
        # Try with qhull backend for the convex hull
        print("Trying with PPL polytope backend...")
        from cytools.polytope import Polytope
        poly2 = Polytope(poly.points(), backend="qhull")
        try:
            tri2 = poly2.triangulate(backend="cgal")
            print("PPL+CGAL worked!")
        except Exception as e2:
            print(f"PPL+CGAL failed: {e2}")
            sys.exit(1)

# If we get here, continue with compute_AA
cy = tri.get_cy()
print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}")
print(f"Smooth: {cy.is_smooth()}")

# Compute AA
print("\nTrying compute_AA()...")
try:
    aa = cy.compute_AA()
    print(f"compute_AA result type: {type(aa)}")
    if isinstance(aa, dict):
        print(f"Keys: {list(aa.keys())[:10]}")
        for k, v in list(aa.items())[:5]:
            print(f"  {k}: shape {np.array(v).shape if hasattr(v, '__len__') else v}")
    elif isinstance(aa, np.ndarray):
        print(f"AA shape: {aa.shape}")
        print(f"AA (first 5): {aa[:5]}")
    else:
        print(f"compute_AA returned: {aa}")
except Exception as e:
    print(f"compute_AA error: {e}")
    import traceback
    traceback.print_exc()

# Try kappa_vector
print("\nTrying compute_kappa_vector()...")
try:
    kv = cy.compute_kappa_vector()
    kv_arr = np.array(kv)
    print(f"kappa_vector shape: {kv_arr.shape}")
    print(f"kappa_vector (first 10): {kv_arr[:10]}")
except Exception as e:
    print(f"compute_kappa_vector error: {e}")

compute_methods = [m for m in dir(cy) if m.startswith('compute_')]
print(f"\nAvailable compute methods: {compute_methods}")
