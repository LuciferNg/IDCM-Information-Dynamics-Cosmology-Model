#!/usr/bin/env python3
"""
Full 3×3 CKM from up/down VEV optimization.
Find v_u (up-type Higgs VEV) and v_d (down-type Higgs VEV)
separately, compute Y_u and Y_d, diagonalize → CKM = V_u† · V_d
"""

import json, math, numpy as np
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1 + 5**0.5) / 2
PHI_INV = PHI - 1

with open(DATA / "Jstar_36D.json") as f:   jstar = json.load(f)
with open(DATA / "cy36_98_final.json") as f: final = json.load(f)
with open(DATA / "kappa_36d_raw.json") as f: kappa_raw = json.load(f)

Jstar = np.array(jstar["Jstar_36D"])
glsm = np.array(final["glsm_coord3"])
kappa_entries = [(i,j,k,float(v)) for kk,v in kappa_raw["kappa"].items() 
                 for (i,j,k) in [tuple(map(int, kk.split(",")))]]

charges = np.zeros(36, dtype=int)
charges[:32] = glsm.astype(int)

def build_Y(v):
    Y = np.zeros((36,36))
    for i,j,k,val in kappa_entries:
        Y[i,j] += val * v[k]
    return Y

def charge_group_matrix(Y, q1, q2):
    i1 = [i for i in range(36) if charges[i]==q1]
    i2 = [i for i in range(36) if charges[i]==q2]
    return Y[np.ix_(i1,i2)]

print("="*72)
print("  FULL 3×3 CKM FROM UP/DOWN VEV OPTIMIZATION")
print("="*72)

# UP sector: dominated by q=10 (Top). 
# The 3 up generations come from mixing of q=10 (Top), q=6÷9 (Charm), q=1÷5 (Up)
# Build Y_u by contracting κ with J* on the up-Higgs direction

# For up-type: the relevant charge groups are the higher-charge divisors
# For down-type: the relevant charge groups include q=8 (Bottom)

# Strategy: find the optimal VEV for each sector by minimizing
# φ-exponent error against IDCM predictions

# Target φ-exponents:
# Up sector:   t=0, c=5.10, u=10.20
# Down sector: b=0, s=3.95, d=7.89  
# Lepton:      τ=0, μ=2.94, e=5.87

target_up = np.array([0.0, 5.10, 10.20])
target_down = np.array([0.0, 3.95, 7.89])

# Selective charge groups for each sector
up_charges = [12, 10, 9, 8, 7, 6, 5]   # high charges → up-type
down_charges = [8, 7, 6, 5, 4, 3, 2]   # mid charges → down-type

def eval_sector(v, charge_list, target_exp):
    """Score how well v produces the target φ-exponents"""
    Y = build_Y(v)
    # Collect all divisor pairs within the charge groups
    indices = [i for i in range(36) if charges[i] in charge_list]
    sub = Y[np.ix_(indices, indices)]
    S = np.linalg.svd(sub, compute_uv=False)
    S = np.sort(S)[::-1]
    # Take top 3 eigenvalues
    S3 = np.maximum(S[:3], 1e-30)
    exps = np.array([-math.log(s/S3[0], PHI) if s>0 else 99 for s in S3])
    err = np.sum((exps[:len(target_exp)] - target_exp[:len(exps)])**2)
    return err, exps, S3

# Random optimization over VEV directions
print("\n  Optimizing UP sector VEV...")
best_up_v, best_up_err = Jstar.copy(), 1e10
for t in range(10000):
    noise = np.random.normal(0, 0.02, 36)
    v = np.abs(Jstar + noise)
    v = v / np.sum(v) * np.sum(Jstar)
    err, exps, _ = eval_sector(v, up_charges, target_up)
    if err < best_up_err:
        best_up_err, best_up_v = err, v.copy()
        best_up_exps = exps
    if t % 5000 == 0:
        print(f"    Trial {t}: best_up_err = {best_up_err:.6e}")

print(f"  UP sector result: loss={best_up_err:.6e}")
print(f"    φ-exponents: {best_up_exps}")
print(f"    Target:      {target_up}")

print("\n  Optimizing DOWN sector VEV...")
best_down_v, best_down_err = Jstar.copy(), 1e10
for t in range(10000):
    if err < best_down_err:
        best_down_err, best_down_v = err, v.copy()
        best_down_exps = exps
    if t % 10000 == 0:
        print(f"    Trial {t}: best_down_err = {best_down_err:.6e}")

print(f"  DOWN sector result: loss={best_down_err:.6e}")
print(f"    φ-exponents: {best_down_exps}")
print(f"    Target:      {target_down}")

# ─── Compute CKM ───────────────────────────────────────
print("\n## Computing CKM from optimized VEVs...")

Y_u = build_Y(best_up_v)
Y_d = build_Y(best_down_v)

# Use shared charge groups for CKM computation
# Balance the index sets
shared_charges = sorted(set(up_charges) & set(down_charges))
up_idx_shared = [i for i in range(36) if charges[i] in shared_charges]
down_idx_shared = [i for i in range(36) if charges[i] in shared_charges]

Y_u_3 = Y_u[np.ix_(up_idx_shared, up_idx_shared)]
Y_d_3 = Y_d[np.ix_(down_idx_shared, down_idx_shared)]

# SVD
Uu, Su, Vhu = np.linalg.svd(Y_u_3)
Ud, Sd, Vhd = np.linalg.svd(Y_d_3)

# Top 3 singular vectors
Uu3 = Uu[:, :3]
Ud3 = Ud[:, :3]

# CKM = Uu† · Ud
CKM = np.abs(Uu3.T @ Ud3)

print(f"\n  CKM matrix (|V_ij|):")
print(f"  {'':>8} {'d(1st)':>10} {'s(2nd)':>10} {'b(3rd)':>10}")
for i, label in enumerate(['u(1st)', 'c(2nd)', 't(3rd)']):
    print(f"  {label:>8} {CKM[i,0]:>10.6f} {CKM[i,1]:>10.6f} {CKM[i,2]:>10.6f}")

# Compare with PDG
print(f"\n  Comparison with PDG:")
print(f"    |V_us| = {CKM[0,1]:.6f}  PDG: 0.224  Δ={abs(CKM[0,1]-0.224)/0.224*100:.1f}%")
print(f"    |V_cb| = {CKM[1,2]:.6f}  PDG: 0.042  Δ={abs(CKM[1,2]-0.042)/0.042*100:.1f}%")
print(f"    |V_ub| = {CKM[0,2]:.6f}  PDG: 0.004  Δ={abs(CKM[0,2]-0.004)/0.004*100:.1f}%")
print(f"    |V_ud| = {CKM[0,0]:.6f}  PDG: 0.974")
print(f"    |V_cs| = {CKM[1,1]:.6f}  PDG: 0.974")
print(f"    |V_tb| = {CKM[2,2]:.6f}  PDG: ~1.0")

# φ-exponent form
print(f"\n  CKM in φ-exponent form:")
for i in range(3):
    for j in range(3):
        if CKM[i,j] > 1e-6:
            n = -math.log(CKM[i,j], PHI)
            print(f"    V_[{i},{j}] = φ^{-n:.2f} = {CKM[i,j]:.6f}")

print(f"\n{'='*72}")
print(f"  STATUS")
print(f"{'='*72}")

v_us_err = abs(CKM[0,1]-0.224)/0.224*100
v_cb_err = abs(CKM[1,2]-0.042)/0.042*100
v_ub_err = abs(CKM[0,2]-0.004)/0.004*100

all_good = v_us_err < 10 and v_cb_err < 10 and v_ub_err < 10
if all_good:
    print(f"  ✅ All CKM elements within 10% of PDG")
    print(f"  🟡 V_us = {CKM[0,1]:.4f} ({v_us_err:.1f}%) — converges with full 3×3 mixing")
else:
    print(f"  🟡 Some deviations remain — VEV optimization needs refinement")
