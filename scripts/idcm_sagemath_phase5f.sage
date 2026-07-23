"""
Phase 5f: J* NUMERICAL OPTIMIZATION
=====================================
Using triple intersection numbers from Phase 5e,
find J* fixed point (Vol = κ³) and compute FN charges.
"""
import os, json, math, sys, numpy as np
from scipy.optimize import minimize

from sage.all import *
from sage.schemes.toric.all import *
from sage.geometry.cone import *

DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

print("="*70)
print("PHASE 5f: J* NUMERICAL OPTIMIZATION")
print("="*70)

with open(os.path.join(DATA_DIR, "cy36_98_sage_export.json")) as f:
    data = json.load(f)
glsm = matrix(ZZ, data["glsm_matrix"])

PHI = (1 + math.sqrt(5))/2; PHI_INV = PHI - 1
BETA = PHI_INV/2; KAPPA3 = (1/16)**3

# Build simplicial fan + cohomology ring
pts = data["points"]; simps = data["simplices"]
fan_pts = [vector(ZZ, pts[i]) for i in range(37)]
cones = [[i for i in s if i != 0] for s in simps if len([i for i in s if i != 0]) == 4]
F = Fan(cones, fan_pts, lattice=ToricLattice(4), check=True)
X = ToricVariety(F)
H = X.cohomology_ring()
D = [H(d) for d in X.toric_divisor_group().gens()]
antiK = H(-X.K())

glsm_c3 = [int(glsm[i,3]) for i in range(glsm.nrows())]
charge_rays = {c: [i for i in range(len(glsm_c3)) if glsm_c3[i]==c] for c in [12,10,9,8,7,6]}
all_key_rays = sorted(set(sum([charge_rays[c] for c in [12,10,9,8,7,6]], [])))
print(f"\n1. {len(all_key_rays)} key divisors: {all_key_rays}")

# Compute triple intersections
print(f"\n2. Triple intersection tensor...")
kappa = {}
for i in all_key_rays:
    for j in all_key_rays:
        if i > j: continue
        for k in all_key_rays:
            if j > k: continue
            try:
                val = float(X.integrate(D[i] * D[j] * D[k] * antiK))
                if val != 0:
                    kappa[(i,j,k)] = val
            except:
                pass

print(f"   {len(kappa)} non-zero entries")

# Volume functional
key_idx = {r: n for n, r in enumerate(all_key_rays)}
n_key = len(all_key_rays)
kappa_mat = np.zeros((n_key, n_key, n_key))
for (i,j,k), val in kappa.items():
    ni, nj, nk = key_idx[i], key_idx[j], key_idx[k]
    for (a,b,c) in [(ni,nj,nk), (ni,nk,nj), (nj,ni,nk), (nj,nk,ni), (nk,ni,nj), (nk,nj,ni)]:
        kappa_mat[a,b,c] = val

def vol_fun(t):
    return float((1.0/6.0) * np.einsum('ijk,i,j,k', kappa_mat, t, t, t))

# Find J*: bounded optimization using brute-force scan + refinement
print(f"\n3. Optimizing J*...")

# Start from 32D uniform scaling
t = np.array([0.1] * n_key)
best_t = t.copy()
best_err = abs(vol_fun(t) - KAPPA3)

# Simple grid search annealing
for phase in range(5):
    scale = 0.5 ** phase  # shrinking step size
    for step in range(200):
        t_try = best_t + np.random.uniform(-scale, scale, n_key)
        t_try = np.maximum(t_try, 1e-10)  # Kähler cone: t > 0
        err = abs(vol_fun(t_try) - KAPPA3)
        if err < best_err:
            best_err = err
            best_t = t_try.copy()

t_opt = best_t
print(f"   Best Vol(J*) = {vol_fun(t_opt):.10e} (target {float(KAPPA3):.10e})"
)
print(f"   t_opt = {[f'{v:.4f}' for v in t_opt[:8]]}...")

# FN charges at J*
print(f"\n4. FN charges at J*:")
for charge in [12,10,9,8,7,6]:
    rays = charge_rays.get(charge, [])
    for r in rays:
        if r in all_key_rays:
            ti = t_opt[key_idx[r]]
            k = -math.log(ti) / math.log(PHI) if ti > 0 else float('nan')
            print(f"   charge {charge:2d} ray {r:2d}: t={ti:.4f}, k={k:.4f}")

# IDCM predictions
print(f"\n5. IDCM:")
print(f"   k_u = {33*BETA:.4f}")
print(f"   k_d = {26*BETA - PHI_INV**4:.4f}")
print(f"   k_l = {19*BETA:.4f}")
print(f"   φ⁻⁴ = {PHI_INV**4:.6f}")
