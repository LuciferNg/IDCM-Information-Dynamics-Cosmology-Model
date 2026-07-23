#!/usr/bin/env python3
"""
Phase 5c: J* + FN charges via CYTools divisor volumes
======================================================
Uses the 32D ambient Kähler cone (CYTools-compatible).
Computes divisor volumes at J* for GLSM-charged rays.
"""
import sys, os, json, math, warnings
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)
import cytools.config
cytools.config.enable_experimental_features()
warnings.filterwarnings("ignore")
from cytools import fetch_polytopes, calabiyau
import numpy as np

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)

PHI = (1 + math.sqrt(5))/2; PHI_INV = PHI - 1; BETA = PHI_INV/2; KAPPA = 1/16; KAPPA3 = KAPPA**3

print("="*70)
print("PHASE 5c: J* FULL COMPUTATION")
print("="*70)

# Build CY
P = list(fetch_polytopes(h11=36, h21=98, limit=1))[0]
tri = P.triangulate(make_star=True, verbosity=0)
tv = tri.get_toric_variety()
cy = calabiyau.CalabiYau(tv)

# GLSM data
glsm = P.glsm_charge_matrix()
n_rays = glsm.shape[0]

# Compute J* scale (uniform scaling in 32D ambient)
t0 = [1.0] * n_rays
vol0 = cy.compute_cy_volume(t0)
scale = (KAPPA3 / vol0) ** (1/3)
tj = [t * scale for t in t0]
print(f"1. J* scale: {scale:.6f}")
vol_j = cy.compute_cy_volume(tj)
print(f"2. Vol(J*) = {vol_j:.10f} (target {KAPPA3:.10f})")

# Divisor volumes at J*
div_vols = cy.compute_divisor_volumes(tj)
print(f"3. {len(div_vols)} divisor volumes computed")

# GLSM charge-to-volume mapping
glsm_coord3 = glsm[:, 3].tolist()
results = {"scale": scale, "J": tj, "vol_CY": vol_j}
print(f"\n4. GLSM charge → divisor volume at J*:")
for charge in sorted(set(glsm_coord3), reverse=True)[:8]:
    rays_with_charge = [i for i, c in enumerate(glsm_coord3) if c == charge]
    vols_at_charge = [div_vols[i] for i in rays_with_charge if div_vols[i] > 0]
    if not vols_at_charge:
        continue
    v_mean = np.mean(vols_at_charge)
    k = math.log(v_mean / vol_j) / math.log(PHI)
    print(f"   charge {charge:2d}: rays={rays_with_charge}, mean Vol={v_mean:.6e}, k={k:.4f}")
    results[f"charge_{charge}_rays"] = rays_with_charge
    results[f"charge_{charge}_vols"] = [float(div_vols[i]) for i in rays_with_charge]
    results[f"charge_{charge}_k"] = float(k)

# IDCM predictions for comparison
k_u_pred = 33*BETA; k_d_pred = 26*BETA - PHI_INV**4; k_l_pred = 19*BETA
print(f"\n5. IDCM FN charge predictions:")
print(f"   k_u = {k_u_pred:.4f}")
print(f"   k_d = {k_d_pred:.4f}")
print(f"   k_l = {k_l_pred:.4f}")

# Volume ratios between charges
print(f"\n6. Volume ratios at J*:")
for c1 in [10]:
    for c2 in [8, 6, 12, 9, 7]:
        v1 = [div_vols[i] for i in range(n_rays) if glsm_coord3[i]==c1 and div_vols[i]>0]
        v2 = [div_vols[i] for i in range(n_rays) if glsm_coord3[i]==c2 and div_vols[i]>0]
        if not v1 or not v2:
            continue
        ratio = np.mean(v2)/np.mean(v1)
        k_diff = math.log(ratio)/math.log(PHI)
        print(f"   Vol(q3={c1})/Vol(q3={c2}): ratio={ratio:.4f}, k_diff={k_diff:.4f}")
        results[f"ratio_{c1}to{c2}"] = float(ratio)
        results[f"kdiff_{c1}to{c2}"] = float(k_diff)

# φ⁻⁴ check
print(f"\n7. φ⁻⁴ = {PHI_INV**4:.6f}")
print(f"   φ⁻⁶ = {PHI_INV**6:.6f}")

# Save
with open(os.path.join(OUTDIR, "phase5c_jstar_fn.json"), "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"\n{'='*70}")
print(f"✅ J* FN COMPUTATION COMPLETE")
print(f"{'='*70}")
print(f"""
Data saved to phase5c_jstar_fn.json

IDCM: k_u={k_u_pred:.4f}, k_d={k_d_pred:.4f}, k_l={k_l_pred:.4f}
Computed k values from divisor volumes at J*: see above
""")
