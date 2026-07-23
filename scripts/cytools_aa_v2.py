#!/usr/bin/env python3
"""
Path C v2: compute divisor volumes at J*, then compute kappa_matrix
The Yukawa in special geometry: K_{ijk}(t) = compute_kappa_matrix(tloc)
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np
import json, math

PHI = (1 + 5**0.5) / 2

print("="*72)
print("CYTools A-MODEL v2 — Yukawa from kappa_matrix(tloc)")
print("="*72)

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate()
cy = tri.get_cy()
h11 = cy.h11()
print(f"CY₃: h¹¹={h11}")

# Load J* from our data
with open("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data/Jstar_36D.json") as f:
    jstar_data = json.load(f)
Jstar = np.array(jstar_data["Jstar_36D"])
print(f"J* loaded, dim={len(Jstar)}")

# Divisor basis: 32 elements from CYTools
# J* is 36D. The first 32 components correspond to the divisor basis.
# The extra 4 are non-GLSM resolution divisors not in the divisor basis.
tloc_32d = Jstar[:32]  # Project to divisor basis
print(f"tloc (32D): first 5 = {tloc_32d[:5]}")

# Step 1: compute divisor volumes at J* (as 32D tloc)
print("\nComputing divisor volumes at tloc=J*[:32]...")
try:
    # set_divisor_basis first
    div_vols = cy.compute_divisor_volumes(tloc_32d.tolist())
    print(f"Divisor volumes type: {type(div_vols)}")
    dv_arr = np.array(div_vols)
    print(f"Divisor volumes shape: {dv_arr.shape}")
    print(f"Divisor volumes (first 10): {dv_arr[:10]}")
    
    # Use original tloc for kappa_matrix (expects 32D divisor basis)
    print("\nComputing kappa_matrix at tloc = J*[:32] (divisor basis)...")
    km = cy.compute_kappa_matrix(tloc_32d.tolist())
    print(f"kappa_matrix type: {type(km)}")
    km_arr = np.array(km)
    print(f"kappa_matrix shape: {km_arr.shape}")
    
    # kappa_matrix: the special geometry Kähler metric (32×32)
    # For physical Yukawa, we need kappa_vector or AA
    
    print("\nComputing kappa_vector (Yukawa couplings)...")
    try:
        kv = cy.compute_kappa_vector(tloc_32d.tolist())
        kv_arr = np.array(kv)
        print(f"kappa_vector shape: {kv_arr.shape}")
        print(f"kappa_vector (first 10): {kv_arr[:10]}")
        
        # The kappa_vector is the contracted Yukawa coupling
        # For physical 3×3 Yukawa, project onto charge sectors
        phys_yukawa = kv_arr[:32]  # Full 32D Yukawa vector
        
        # Top 10 eigenvalues
        S = np.sort(np.abs(phys_yukawa))[::-1][:10]
        print(f"\nTop 10 magnitudes: {S}")
        print(f"φ-exponents (relative to largest):")
        for i in range(min(10, len(S))):
            if S[i] > 0:
                exp = -math.log(S[i]/S[0], PHI)
                print(f"  λ_{i} = {S[i]:.6f} → φ^{exp:.3f}")
    except Exception as e:
        print(f"compute_kappa_vector error: {e}")
    
    # Also try AA computation
    print("\nComputing AA (A-model three-point functions)...")
    try:
        aa = cy.compute_AA(tloc_32d.tolist())
        aa_arr = np.array(aa)
        print(f"AA shape: {aa_arr.shape}")
        print(f"AA (first 5×5):")
        print(aa_arr[:5, :5] if aa_arr.ndim >=2 else aa_arr[:10])
    except Exception as e:
        print(f"compute_AA error: {e}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
