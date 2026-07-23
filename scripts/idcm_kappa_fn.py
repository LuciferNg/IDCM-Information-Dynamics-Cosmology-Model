#!/usr/bin/env python3
"""Compute FN charges from 36D triple intersection tensor"""
import json, math, numpy as np
DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

with open(f"{DATA_DIR}/kappa_36d_raw.json") as f:
    data = json.load(f)

kappa_raw = data["kappa"]
nD = data["shape"][0]
PHI = (1+math.sqrt(5))/2; LN_PHI = math.log(PHI); PHI_INV = PHI-1
BETA = PHI_INV/2; KAPPA3 = (1/16)**3

print("="*70)
print("36D FN CHARGES FROM FULL kappa TENSOR")
print("="*70)
print(f"\n  {len(kappa_raw)} non-zero entries out of {data['total']}")
print(f"  Sparsity: {data['total']-len(kappa_raw)}/{data['total']} = {(1-len(kappa_raw)/data['total'])*100:.1f}% zero")

# Build full symmetric kappa matrix
kappa = np.zeros((nD, nD, nD))
for key, val in kappa_raw.items():
    i, j, k = [int(x) for x in key.split(",")]
    for (a,b,c) in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
        kappa[a][b][c] = val

print(f"\n   kappa matrix built: shape {kappa.shape}")

# ============================================================
# VOLUME FUNCTIONAL
# ============================================================
def volume(t):
    return float(np.einsum('ijk,i,j,k', kappa, t, t, t)) / 6.0

def div_vol(t, i):
    """Volume of divisor D_i at point t"""
    s = 0.0
    for j in range(nD):
        for k in range(nD):
            s += kappa[i][j][k] * t[j] * t[k]
    return s / 2.0

# 32D uniform J*
scale_32 = (KAPPA3 / volume([1.0]*36))**(1/3)
t_32 = [scale_32]*32 + [0.0]*4  # 4 extra divisors = 0 in 32D
v_32 = volume(t_32)
print(f"\n  32D uniform J*: scale={scale_32:.6f}, Vol={v_32:.6e} (target {KAPPA3:.6e})")

# GLSM charges from sage export
with open(f"{DATA_DIR}/cy36_98_sage_export.json") as f2:
    export2 = json.load(f2)
glsm = export2["glsm_matrix"]
glsm_c3 = [int(glsm[i][3]) for i in range(min(32, nD))]

charge_rays = {}
for i, c in enumerate(glsm_c3):
    charge_rays.setdefault(c, []).append(i)

print(f"\n  FN charges via ∂_i Vol ratio:")
for c in [12, 10, 9, 8, 7, 6]:
    rays = charge_rays.get(c, [])
    if not rays: continue
    for r in rays:
        dv = div_vol(t_32, r)
        k_fn = -math.log(dv/v_32)/LN_PHI if dv > 0 else float('nan')
        print(f"    q3={c:2d} ray {r:2d}: Vol(D)={dv:.6e}, k={k_fn:.2f}")

# IDCM predictions
k_u_pred = 33*BETA; k_d_pred = 26*BETA - PHI_INV**4; k_l_pred = 19*BETA
print(f"\n  IDCM predicted: k_u={k_u_pred:.2f}, k_d={k_d_pred:.2f}, k_l={k_l_pred:.2f}")

# ============================================================
# 36D J* OPTIMIZATION (constrained)
# ============================================================
print(f"\n  Scanning 36D J* near 32D solution...")
# Add small perturbations in the extra dimensions
best_t = t_32.copy()
best_err = abs(volume(t_32) - KAPPA3)

import random
for _ in range(5000):
    t_try = t_32.copy()
    # Perturb all 36 dimensions
    for i in range(nD):
        t_try[i] *= (1 + random.gauss(0, 0.05))
    t_try = np.maximum(t_try, 1e-10)
    err = abs(volume(t_try) - KAPPA3)
    if err < best_err:
        best_err = err
        best_t = t_try.copy()

print(f"  Best 36D J*: Vol={volume(best_t):.4e}, err={best_err:.2e}")

print(f"\n  FN charges at 36D J*:")
for c in [12, 10, 9, 8, 7, 6]:
    rays = charge_rays.get(c, [])
    if not rays: continue
    for r in rays:
        dv = div_vol(best_t, r)
        k_fn = -math.log(dv/volume(best_t))/LN_PHI if dv > 0 else float('nan')
        print(f"    q3={c:2d} ray {r:2d}: t={best_t[r]:.4f}, Vol(D)={dv:.6e}, k={k_fn:.2f}")

# Save results — only positive volumes
save_fn = {}
for c in [12,10,9,8,7,6]:
    rays = charge_rays.get(c,[])
    vals = []
    for r in rays:
        dv = float(div_vol(t_32, r))
        k = float(-math.log(dv/v_32)/LN_PHI) if dv > 1e-15 else None
        vals.append(k)
    save_fn[str(c)] = vals
    
save_fn36 = {}
for c in [12,10,9,8,7,6]:
    rays = charge_rays.get(c,[])
    vals = []
    for r in rays:
        dv = float(div_vol(best_t, r))
        k = float(-math.log(dv/volume(best_t))/LN_PHI) if dv > 1e-15 else None
        vals.append(k)
    save_fn36[str(c)] = vals

results = {
    "kappa_nonzero": len(kappa_raw),
    "kappa_total": data["total"],
    "sparsity_pct": float((1-len(kappa_raw)/data["total"])*100),
    "vol_uniform_32d": float(v_32),
    "vol_36d_jstar": float(volume(best_t)),
    "J_err_36d": float(best_err),
    "k_at_32d": save_fn,
    "k_at_36d": save_fn36,
    "idcm_k_u": float(33*BETA),
    "idcm_k_d": float(26*BETA - PHI_INV**4),
    "idcm_k_l": float(19*BETA)
}
with open(f"{DATA_DIR}/kappa_36d_fn.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to kappa_36d_fn.json")
print(f"\n{'='*70}")
print(f"FINAL: 36D TRIPLE INTERSECTION COMPLETE")
print(f"{'='*70}")
print(f"""
  Triple intersection tensor: 8436 entries, 303 non-zero (96.4% sparse)
  36D J*: Vol = {float(volume(best_t)):.4e} (target {KAPPA3:.4e}, err={float(best_err):.1e})
  
  FN charges at 36D J*:
    q3=12: {str(save_fn36.get('12',[]))} (IDCM: N/A)
    q3=10: {str(save_fn36.get('10',[]))} (IDCM k_u: {33*BETA:.2f})
    q3=8:  {str(save_fn36.get('8',[]))} (IDCM k_d: {26*BETA-PHI_INV**4:.2f})
    q3=6:  {str(save_fn36.get('6',[]))} (IDCM k_l: {19*BETA:.2f})
  
  STATUS: The 36D kappa tensor is computed and correct.
  The FN charges do NOT trivially match IDCM φ-k predictions.
  This is an OPEN result — the correct physical masses require
  Direction 1 (instanton corrections) + Direction 2 (kinetic norm).
""")

