#!/usr/bin/env python3
"""
IDCM CY₃(36,98) — J* KÄHLER CONE OPTIMIZATION
================================================
Find J* fixed point within 36D Kähler cone.
J* is defined by stable fixed point condition:
  Vol(CY₃) = κ³ = (1/16)³ = 1/4096
  under the SYNC dynamics.
"""
import sys, os, json, math, warnings, numpy as np
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)

import cytools.config
cytools.config.enable_experimental_features()
warnings.filterwarnings("ignore")
from cytools import fetch_polytopes, calabiyau

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)

PHI = (1 + math.sqrt(5))/2; PHI_INV = PHI - 1; BETA = PHI_INV/2; KAPPA = 1/16

print("="*70)
print("IDCM — J* KÄHLER CONE OPTIMIZATION")
print("="*70)

# 1. Build CY
polys = list(fetch_polytopes(h11=36, h21=98, limit=5))
P = polys[0]
tri = P.triangulate(make_star=True, verbosity=0)
tv = tri.get_toric_variety()
cy = calabiyau.CalabiYau(tv)
print(f"\n1. CY₃({cy.h11()},{cy.h21()}), n_divisors={len(cy.prime_toric_divisors())}")

# 2. Divisor basis
print(f"\n2. Computing divisor basis...")
try:
    cy.set_divisor_basis()
    print(f"   Divisor basis set")
except Exception as e:
    print(f"   set_divisor_basis: {e}")
    # Try with basis
    try:
        cy.set_divisor_basis(range(cy.h11()))
        print(f"   Divisor basis set with range")
    except Exception as e2:
        print(f"   Also failed: {e2}")

# 3. Get the Kähler cone
print(f"\n3. Kähler cone structure...")
try:
    kc = cy.toric_kahler_cone()
    print(f"   Kähler cone: {kc}")
    print(f"   rays: {kc.rays() if hasattr(kc, 'rays') else 'N/A'}")
except Exception as e:
    print(f"   {e}")

# 4. Kappa matrix (Kähler metric)
print(f"\n4. Kappa matrix (Kähler metric on moduli space)...")
try:
    kappa = cy.compute_kappa_matrix()
    print(f"   Kappa matrix shape: {kappa.shape}")
    print(f"   Kappa diagonal (first 5): {kappa.diagonal()[:5] if hasattr(kappa, 'diagonal') else kappa[:5,:5]}")
except Exception as e:
    print(f"   {e}")

# 5. Kappa vector
print(f"\n5. Kappa vector...")
try:
    kvec = cy.compute_kappa_vector()
    print(f"   Kappa vector shape: {kvec.shape if hasattr(kvec, 'shape') else len(kvec)}")
    print(f"   First 5 entries: {kvec[:5] if hasattr(kvec, '__getitem__') else kvec}")
except Exception as e:
    print(f"   {e}")

# 6. Divisor volumes - try different approaches
print(f"\n6. Divisor volumes...")
vols = None
if hasattr(cy, 'compute_divisor_volumes'):
    try:
        vols = cy.compute_divisor_volumes(stretched_tip=True)
        print(f"   Stretched tip: {len(vols)} volumes computed")
    except Exception as e:
        print(f"   stretched_tip: {e}")
        try:
            vols = cy.compute_divisor_volumes()
            print(f"   Default: {len(vols)} volumes computed")
        except Exception as e2:
            print(f"   default: {e2}")

if vols is not None and len(vols) > 0:
    sorted_idx = np.argsort(vols)[::-1]
    print(f"\n   Top 20 divisor volumes (sorted descending):")
    for rank, idx in enumerate(sorted_idx[:20]):
        k_phi = math.log(vols[idx]) / math.log(PHI) if vols[idx] > 0 else float('-inf')
        print(f"   #{rank:2d}: D_{idx:2d} Vol={vols[idx]:.6f}, k={k_phi:.4f}")
    
    # Check which divisors match k_u, k_d, k_l
    k_u = 33 * BETA; k_d = 26 * BETA - PHI_INV**4; k_l = 19 * BETA
    print(f"\n   Matching IDCM FN charges:")
    for k_name, k_target in [("k_u", k_u), ("k_d", k_d), ("k_l", k_l)]:
        best = min(range(len(vols)), key=lambda i: abs(math.log(vols[i])/math.log(PHI) - k_target))
        best_k = math.log(vols[best]) / math.log(PHI)
        print(f"   {k_name}={k_target:.4f}: best D_{best} k={best_k:.4f} Δ={abs(best_k-k_target):.4f}")

# 7. CY volume
print(f"\n7. CY volume:")
try:
    cy_vol = cy.compute_cy_volume(tloc='default')
    print(f"   Vol(CY) = {cy_vol:.6f}")
    target_vol = KAPPA**3
    print(f"   Vol(κ³) = {target_vol:.10f}")
    ratio = cy_vol / target_vol if target_vol > 0 else 0
    print(f"   Ratio = {ratio:.4f}")
except Exception as e:
    print(f"   {e}")

# 8. Kähler metric
print(f"\n8. Kähler metric...")
try:
    km = cy.compute_kahler_metric()
    print(f"   Kähler metric shape: {km.shape if hasattr(km, 'shape') else '?'}")
except Exception as e:
    print(f"   {e}")

# 9. Save intermediate results
print(f"\n9. Optimizing toward J* (Vol = κ³)...")
# The J* fixed point requires Vol(CY) = κ³ = 1/4096
# Currently at stretched cone tip; need to scale t-modes
# to reach target volume

results = {
    "kappa_matrix_shape": None,
    "divisor_volumes_stretched": vols.tolist() if vols is not None else None,
    "target_vol": KAPPA**3,
}

print(f"\n{'='*70}")
print(f"J* OPTIMIZATION — INTERMEDIATE RESULTS")
print(f"{'='*70}")
print(f"""
Status: Stretched cone tip computed
Next step: Scale Kähler parameters to reach Vol = κ³
  Requires iterative optimization in 36D Kähler cone

Current ratio (stretched/κ³) ≈ {ratio:.2f} if computed
Target: Vol(CY) = 1/4096 = 0.000244140625

The J* search is a convex optimization problem:
  minimize |Vol(t) - κ³|  subject to t ∈ Kähler cone
  Vol(t) = (1/6) · kappa_ijk · t_i · t_j · t_k
""")
