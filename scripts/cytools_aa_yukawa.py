#!/usr/bin/env python3
"""
Path C: CYTools compute_AA() — A-model correlation functions
Directly computes the physical Yukawa couplings from the CY₃.
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np

print("="*72)
print("CYTools A-MODEL — Direct Yukawa from compute_AA()")
print("="*72)

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate()
cy = tri.get_cy()

print(f"CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}")
print(f"Smooth: {cy.is_smooth()}")

# Try compute_AA — A-model correlation functions
print("\nTrying compute_AA()...")
try:
    aa = cy.compute_AA()
    print(f"compute_AA result type: {type(aa)}")
    if isinstance(aa, dict):
        print(f"Keys: {list(aa.keys())[:10]}")
        for k in list(aa.keys())[:5]:
            print(f"  {k}: shape {np.array(aa[k]).shape if hasattr(aa[k], '__len__') else aa[k]}")
    else:
        print(f"compute_AA returned: {aa}")
except Exception as e:
    print(f"compute_AA error: {e}")

# Try compute_gv — Gopakumar-Vafa invariants (indirectly gives Yukawa)
print("\nTrying compute_gv()...")
try:
    gv = cy.compute_gv()
    print(f"compute_gv result type: {type(gv)}")
    if isinstance(gv, dict):
        print(f"Keys: {list(gv.keys())[:10]}")
    else:
        print(f"compute_gv returned shape: {np.array(gv).shape if hasattr(gv, '__len__') else gv}")
except Exception as e:
    print(f"compute_gv error: {e}")

# Try compute_gws — Gromov-Witten invariants (three-point functions)
print("\nTrying compute_gws()...")
try:
    gws = cy.compute_gws()
    print(f"compute_gws result type: {type(gws)}")
except Exception as e:
    print(f"compute_gws error: {e}")

# Try compute_kappa_matrix — the Yukawa matrix in special geometry
print("\nTrying compute_kappa_matrix()...")
try:
    km = cy.compute_kappa_matrix()
    print(f"kappa_matrix type: {type(km)}")
    if isinstance(km, (list, np.ndarray)):
        km_arr = np.array(km)
        print(f"kappa_matrix shape: {km_arr.shape}")
        print(f"kappa_matrix (first 3×3):")
        if km_arr.ndim >= 2:
            print(km_arr[:3, :3])
        else:
            print(km_arr[:10])
except Exception as e:
    print(f"compute_kappa_matrix error: {e}")

# Try compute_kappa_vector — Yukawa couplings in special coordinates
print("\nTrying compute_kappa_vector()...")
try:
    kv = cy.compute_kappa_vector()
    print(f"kappa_vector type: {type(kv)}")
    if isinstance(kv, (list, np.ndarray)):
        kv_arr = np.array(kv)
        print(f"kappa_vector shape: {kv_arr.shape}")
        print(f"kappa_vector (first 10): {kv_arr[:10]}")
except Exception as e:
    print(f"compute_kappa_vector error: {e}")

# Most promising: compute_inverse_kahler_metric
# The special geometry Yukawa is K_{ijk} = ∂³K/∂t_i∂t_j∂t_k
print("\nTrying compute_inverse_kahler_metric()...")
try:
    ikm = cy.compute_inverse_kahler_metric(Jstar=None)
    print(f"inverse_kahler_metric type: {type(ikm)}")
except Exception as e:
    print(f"compute_inverse_kahler_metric error: {e}")

# Try compute_cy_volume at J*
print("\nTrying compute_cy_volume()...")
try:
    vol = cy.compute_cy_volume([0.1]*cy.h11())
    print(f"CY volume at t=0.1: {vol}")
except Exception as e:
    print(f"compute_cy_volume error: {e}")

# Check what's available by listing all compute_* methods
compute_methods = [m for m in dir(cy) if m.startswith('compute_')]
print(f"\nAll compute_* methods: {compute_methods}")
