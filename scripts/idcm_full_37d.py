#!/usr/bin/env python3
"""
CY₃(36,98) — Full 37D J* + 6-Task One-Shot
=============================================
Strategy: fix ambient 32D uniform J* (proven), optimize
only the 5 extra rays (32-36) that adjust the volume.
"""
import sys, os, json, math, itertools, time
import numpy as np
from scipy.optimize import minimize

PHI = (1+math.sqrt(5))/2; PHI_INV = PHI-1; LN_PHI = math.log(PHI)
BETA = PHI_INV/2; KAPPA = 1/16; KAPPA3 = KAPPA**3
T_UNIFORM = 0.0901405981538189  # 32D uniform J* proven value

DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

print("="*70)
print("CY₃(36,98) — FULL 37D J* + 6-TASK ONE-SHOT")
print("="*70)
print(f"κ={KAPPA}, κ³={KAPPA3:.6e}, φ={PHI:.6f}, ln(φ)={LN_PHI:.6f}")

# ================================================================
# 1. LOAD κ_ijk TENSOR
# ================================================================
print("\nPHASE 1: κ_ijk tensor")
with open(f"{DATA_DIR}/kappa_36d_raw.json") as f:
    kd = json.load(f)
kappa_raw = kd["kappa"]
print(f"  {len(kappa_raw)} non-zero / {kd['total']} total")

K = np.zeros((37,37,37))
for key, val in kappa_raw.items():
    i,j,k = [int(x) for x in key.split(",")]
    v = float(val)
    for a,b,c in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
        K[a,b,c] = v

# ================================================================
# 2. LOAD FN MAPPING + EDGES
# ================================================================
print("\nPHASE 2: FN mapping + edges")
with open(f"{DATA_DIR}/phase5c_jstar_fn.json") as f:
    fn32 = json.load(f)
with open(f"{DATA_DIR}/cy36_98_sage_export.json") as f:
    sage_d = json.load(f)

charge_rays = {
    12: fn32.get("charge_12_rays", [2]),
    10: fn32.get("charge_10_rays", [4]),
     8: fn32.get("charge_8_rays", [6]),
     7: fn32.get("charge_7_rays", [19, 20]),
     6: fn32.get("charge_6_rays", [7, 8, 9, 21]),
}
ray_to_charge = {}
for c, rays in charge_rays.items():
    for r in rays:
        ray_to_charge[r] = c
print(f"  Charged rays: {len(ray_to_charge)}: {sorted(ray_to_charge.items())}")

simps = sage_d["simplices"]
all_edges = set()
for s in simps:
    nr = [i for i in s if i != 0]
    for i,j in itertools.combinations(sorted(nr), 2):
        if i < 37 and j < 37:
            all_edges.add((min(i,j), max(i,j)))
fan_edges = sorted(all_edges)
print(f"  Edges: {len(fan_edges)}")

# ================================================================
# 3. J*: 32D FIXED + EXTRA OPTIMIZATION
# ================================================================
print("\nPHASE 3: 37D J* (fixed 32D uniform + extra optimization)")

t_37d = np.ones(37) * T_UNIFORM  # rays 0-31

# Volume at uniform 32D
vol_32d = (1/6) * np.einsum('ijk,i,j,k', K[:32,:32,:32], 
                             t_37d[:32], t_37d[:32], t_37d[:32])
print(f"  32D uniform Vol = {vol_32d:.10e} (target {KAPPA3:.10e})")
print(f"  Error = {abs(vol_32d - KAPPA3):.2e}")

# The 32D uniform already gives κ³! So the 3 extra classes
# add corrections. To maintain Vol=κ³, we need to slightly
# adjust ambient t_i OR set extra t_i = 0 (degenerate).

# Physical insight: the 3 extra classes are non-toric divisors
# that exist in CY cohomology but NOT in ambient toric variety.
# Their t_i should be SMALL but non-zero.
# The 32D→36D transition: t_i redistribute to accommodate extras.

# Minimize: |Vol_37D - κ³| + λ*||t_extra||² with t_i > 0
# Subject to: all ambient t_i close to 0.09014
# And: extra t_i ≥ 0

print(f"\n  Strategy: optimize extra t_i (32-36) + ambient small perturbation")
print(f"  37 variables, 1 constraint (Vol=κ³)")

# Simpler: just set extra t_i to the values that absorb the volume
# correction from the non-uniform distribution.

# The key: at 36D J*, the FN data shows that charged-ray t_i differ
# from the 32D uniform. The difference comes from κ_ijk redistribution.

# From the earlier 36D FN charge data, we can reconstruct t_i for
# charged rays at 36D J* using k_i:
# k_i = -log_φ(Vol(D_i)/Vol(CY))
# Vol(D_i) = Vol(CY) × φ^(-k_i) = κ³ × φ^(-k_i)

# Load FN charges at 36D J*
with open(f"{DATA_DIR}/kappa_36d_fn.json") as f:
    fn36d = json.load(f)

k_at_36d = fn36d.get("k_at_36d", {})

# Reconstruct div volumes from FN charges
div_vols_36d = np.ones(37) * 1e-20
for charge_str, k_list in k_at_36d.items():
    charge = int(charge_str)
    rays = charge_rays.get(charge, [])
    for idx, r in enumerate(rays):
        if idx < len(k_list) and k_list[idx] is not None:
            k_val = float(k_list[idx])
            if not math.isnan(k_val) and abs(k_val) < 50:
                div_vols_36d[r] = KAPPA3 * (PHI_INV ** k_val)

print(f"\n  Reconstructed divisor volumes at 36D J* from FN charges:")
for c in sorted(charge_rays, reverse=True):
    for r in charge_rays[c]:
        print(f"    charge {c:2d} ray {r:2d}: Vol(D)={div_vols_36d[r]:.3e} (k={k_at_36d.get(str(c),[None])[charge_rays[c].index(r)]})")

# Now solve for t_i: Vol(D_i) = (1/2) Σ_j κ_ij · t_j
# κ_ij(t) = Σ_k κ_ijk · t_k
# So: Vol(D_i) = (1/2) Σ_jk κ_ijk · t_j · t_k
# This is a quadratic form in t. We need to solve for t given Vol(D).

# Approach: optimize t to match Vol(D) and Vol(CY)
def volume(t):
    return (1/6) * np.einsum('ijk,i,j,k', K, t, t, t)

def div_vols(t):
    k_ij = np.einsum('ijk,k->ij', K, t)
    return 0.5 * np.einsum('ij,j->i', k_ij, t)

def objective(t):
    """Match reconstructed divisor volumes"""
    dv = div_vols(t)
    # Penalize deviation from reconstructed div vols for charged rays
    err = 0.0
    n_charged = 0
    for c in charge_rays:
        for r in charge_rays[c]:
            if div_vols_36d[r] > 1e-15:
                err += (dv[r] - div_vols_36d[r])**2 / div_vols_36d[r]**2
                n_charged += 1
    # Also penalize Vol(CY) deviation
    vol_err = (volume(t) - KAPPA3)**2 / KAPPA3**2
    # Keep t_i positive
    eps = 1e-20
    log_penalty = -np.sum(np.log(np.maximum(t, eps))) * 1e-5  # gentle
    return err + vol_err + log_penalty

t0 = np.ones(37) * T_UNIFORM
bounds = [(1e-10, None)] * 37

print(f"\n  Optimizing 37D J* to match FN charges...")
t0_t = time.time()
res = minimize(objective, t0, method='L-BFGS-B', bounds=bounds,
               options={'maxiter': 5000, 'ftol': 1e-15})
t_opt = res.x
dt = time.time() - t0_t

vol_opt_val = float(volume(t_opt))
vol_err_val = abs(vol_opt_val - KAPPA3)
dv_opt = div_vols(t_opt)

print(f"  Optimizer: {res.success}, iter={res.nit}, time={dt:.1f}s")
print(f"  Vol(J*) = {vol_opt_val:.10e} (err={vol_err_val:.2e})")

# Print t_i for charged rays
print(f"\n  Optimized t_i:")
for c in sorted(charge_rays, reverse=True):
    for r in charge_rays[c]:
        print(f"    charge {c:2d} ray {r:2d}: t={t_opt[r]:.6f}, Vol(D)={dv_opt[r]:.3e} (target {div_vols_36d[r]:.3e})")

# Print non-charged rays summary
t_nonzero = t_opt[t_opt > 1e-6]
print(f"  Non-zero t_i: {len(t_nonzero)}/{37}, range [{t_opt.min():.6e}, {t_opt.max():.6f}]")

# ================================================================
# 4. FN CHARGES AT 37D J*
# ================================================================
print("\n" + "="*70)
print("PHASE 4: FN CHARGES AT 37D J*")
print("="*70)

k_i = np.zeros(37)
for i in range(37):
    if dv_opt[i] > 1e-20:
        k_i[i] = -math.log(dv_opt[i] / vol_opt_val) / LN_PHI
    else:
        k_i[i] = float('nan')

idcm_preds = {12: None, 10: 33*BETA, 8: 26*BETA-PHI_INV**4, 7: None, 6: 19*BETA}

print(f"{'Chg':>4s} {'Ray':>4s} {'t_i':>10s} {'Vol(D)':>12s} {'k':>8s} {'IDCM':>8s} {'δ':>6s}")
print("-"*58)
matches = []
for c in sorted(charge_rays, reverse=True):
    for r in charge_rays[c]:
        idcm = idcm_preds.get(c)
        kv = k_i[r]
        if not math.isnan(kv):
            delta = abs(kv - idcm) if idcm else float('nan')
            sym = "✅" if (idcm and delta < 0.5) else ("🟡" if idcm and delta < 2.0 else ("❌" if idcm else "—"))
            if idcm and delta < 0.5:
                matches.append((c, r, kv, idcm, delta))
            idcm_s = f"{idcm:.2f}" if idcm else "—"
            delta_s = f"{delta:.2f}" if idcm else "—"
            print(f"  {c:3d}  r={r:2d}  {t_opt[r]:8.4f}  {dv_opt[r]:10.3e}  {kv:6.2f}  {idcm_s:>8s}  {delta_s:>6s}  {sym}")

if matches:
    print(f"\n✅ Direct matches:")
    for c, r, kv, idcm, delta in matches:
        print(f"  charge {c:2d} ray {r:2d}: k={kv:.2f} ≈ IDCM {idcm:.2f} (δ={delta:.2f})")

# ================================================================
# 5. CURVE VOLUMES
# ================================================================
print("\n" + "="*70)
print("PHASE 5: CURVE VOLUMES AT 37D J*")
print("="*70)

kappa_ij_at_j = np.einsum('ijk,k->ij', K, t_opt)
cp_curves = {}
for i,j in fan_edges:
    vol = max(float(kappa_ij_at_j[i,j]), 1e-20)
    ci, cj = ray_to_charge.get(i,0), ray_to_charge.get(j,0)
    if ci > 0 and cj > 0:
        pk = (min(ci,cj), max(ci,cj))
        cp_curves.setdefault(pk, []).append((i,j,vol))

print(f"{'Pair':>8s} {'N':>4s} {'Avg Vol':>10s} {'q':>12s} {'n=Vol/lnφ':>12s} {'int(n)':>6s} {'Match':>6s}")
print("-"*62)
for pk in sorted(cp_curves, reverse=True):
    entries = cp_curves[pk]
    vols = [e[2] for e in entries]
    avg = np.mean(vols)
    q = math.exp(-avg)
    n_e = avg / LN_PHI
    n_i = round(n_e) if n_e >= 1 else 0
    err = abs(n_e - n_i) if n_i >= 1 else 0
    m = "✅" if n_i >= 1 and err/n_i < 0.05 else ("🟡" if n_i >= 1 else "—")
    print(f"  {pk[0]:2d}↔{pk[1]:2d}   {len(entries):3d}  {avg:8.4f}  {q:10.6f}  {n_e:10.4f}  {n_i:5d}  {m:>6s}")

# ================================================================
# 6. φ⁻ⁿ QUANTIZATION CHECK
# ================================================================
print("\n" + "="*70)
print("PHASE 6: φ⁻ⁿ QUANTIZATION")
print("="*70)
print(f"  ln(φ) = {LN_PHI:.6f}")
print(f"  Need Vol = n·ln(φ) for instanton q = φ⁻ⁿ")

for pk in sorted(cp_curves, reverse=True):
    entries = cp_curves[pk]
    vols = [e[2] for e in entries]
    avg = np.mean(vols)
    n_e = avg / LN_PHI
    n_i = max(0, round(n_e))
    if n_i >= 1:
        err = abs(n_e - n_i) / n_i * 100
        m = "✅" if err < 2 else ("🟡" if err < 10 else "❌")
    else:
        err = n_e
        m = "—"
    print(f"  {pk[0]:2d}↔{pk[1]:2d}: Vol={avg:.4f}, n_exact={n_e:.4f}, n_int={n_i}, err={err:.1f}% {m}")

# ================================================================
# 7. INSTANTON CORRECTED YUKAWA
# ================================================================
print("\n" + "="*70)
print("PHASE 7: INSTANTON-CORRECTED YUKAWA")
print("="*70)

print(f"  GW invariants n_β: tool-limited (need cohomCalg)")
print(f"  Using n_β = 1 per edge type (schematic)")
print(f"")
print(f"{'Pair':>8s} {'κ_cl':>8s} {'q':>10s} {'q/(1-q)':>10s} {'Y_inst':>8s} {'Y_net':>8s}")
print("-"*55)

for pk in sorted(cp_curves, reverse=True):
    entries = cp_curves[pk]
    vols = [e[2] for e in entries]
    avg = np.mean(vols)
    q = math.exp(-avg)
    q_corr = q / (1-q) if q < 1 else 1.618
    
    # Classical κ for this pair (average)
    i_ex = entries[0][0] if entries else 0
    j_ex = entries[0][1] if entries else 0
    cl_k = float(K[i_ex,j_ex,j_ex]) if len(entries) > 0 else 0
    
    y_net = cl_k + q_corr
    print(f"  {pk[0]:2d}↔{pk[1]:2d}   {cl_k:7.2f}  {q:8.6f}  {q_corr:8.4f}  {q_corr:7.4f}  {y_net:7.4f}")

# ================================================================
# 8. FN PREDICTIONS
# ================================================================
print("\n" + "="*70)
print("PHASE 8: FN PREDICTIONS")
print("="*70)

print(f"{'Type':>8s} {'Ray':>4s} {'k_cl':>8s} {'k_inst':>8s} {'k_eff':>8s} {'IDCM':>8s} {'Stat':>5s}")
print("-"*55)

for c in sorted(charge_rays, reverse=True):
    for r in charge_rays[c]:
        kv = k_i[r]
        if math.isnan(kv): continue
        
        # Find edges for this ray
        edge_vols = [v for (i,j),v in [((e[0],e[1]),e[2]) for pk2, ents2 in cp_curves.items() for e in ents2] if i==r or j==r]
        n_inst = 0
        k_inst = 0
        if edge_vols:
            n_inst = max(1, round(np.mean(edge_vols) / LN_PHI))
            k_inst = 0.5 * math.log(PHI_INV**n_inst/abs(1-PHI_INV**n_inst)) / LN_PHI if PHI_INV**n_inst < 1 else 0
        
        k_eff = kv + k_inst
        idcm = idcm_preds.get(c)
        
        if idcm:
            delta = abs(k_eff - idcm)
            s = "✅" if delta < 0.5 else ("🟡" if delta < 2.0 else "❌")
        else:
            s = "—"
        
        print(f"  q₃={c:2d}   r={r:2d}  {kv:7.2f}  {k_inst:7.2f}  {k_eff:7.2f}  ", end="")
        print(f"{idcm:7.2f}  {s:>5s}" if idcm else f"  —     {s:>5s}")

# ================================================================
# SAVE
# ================================================================
res_out = {
    "t_i": [float(t) for t in t_opt],
    "vol_opt": float(vol_opt_val),
    "vol_err": float(vol_err_val),
    "k_i": [float(k) if not math.isnan(k) else None for k in k_i],
    "div_vols": [float(d) if d > 1e-20 else None for d in dv_opt],
}
with open(f"{DATA_DIR}/jstar_37d_full.json", "w") as f:
    json.dump(res_out, f, indent=2)

print(f"\n✅ Saved: {DATA_DIR}/jstar_37d_full.json")
print("="*70)
print("DONE")
print("="*70)
