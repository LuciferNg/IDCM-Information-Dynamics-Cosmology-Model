#!/usr/bin/env python3
"""Find the 37D J* that satisfies Vol=κ³ AND Mori cone quantization"""
import sys, os, json, math, itertools, time
import numpy as np
from scipy.optimize import minimize

PHI = (1+math.sqrt(5))/2; PHI_INV = PHI-1; LN_PHI = math.log(PHI)
BETA = PHI_INV/2; KAPPA3 = (1/16)**3

DATA = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

# Load κ_ijk
with open(f"{DATA}/kappa_36d_raw.json") as f:
    kd = json.load(f)
K = np.zeros((37,37,37))
for key, val in kd["kappa"].items():
    i,j,k = [int(x) for x in key.split(",")]
    v = float(val)
    for a,b,c in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
        K[a,b,c] = v

# Load Mori cone generators from CYTools
import warnings
import cytools.config; cytools.config.enable_experimental_features()
warnings.filterwarnings('ignore')
from cytools import fetch_polytopes, calabiyau
P = list(fetch_polytopes(h11=36, h21=98, limit=1))[0]
cy = calabiyau.CalabiYau(P.triangulate(make_star=True, verbosity=0).get_toric_variety())
mc = cy.toric_mori_cone()
mori_gen = np.array(mc.rays())  # (185, 37)

print(f"κ_ijk: {np.count_nonzero(K)} / 37^3 non-zero")
print(f"Mori cone: {mori_gen.shape[0]} generators × {mori_gen.shape[1]} D")

# Key generators (by charge content)
gen_data = {}
# #56: q10↔q6 connector
gen56 = mori_gen[56]
# #74: q6↔q6  
gen74 = mori_gen[74]
# #174: q10↔q6 (smaller)
gen174 = mori_gen[174]
# #24: q12 + extra v32
gen24 = mori_gen[24]
# #32: q12↔q8
gen32 = mori_gen[32]

def volume(t):
    return (1/6) * np.einsum('ijk,i,j,k', K, t, t, t)

def objective_and_grad(t):
    """Find J* that gives specific Mori cone volumes while keeping Vol=κ³
    
    Targets:
      gen56 · t = 12 · ln(φ) = 5.77  (for q₃=10→k_u)
      gen74 · t = 13 · ln(φ) = 6.25  (for q₃=8→k_d)  
      Vol = κ³
    
    Also keep t_i relatively uniform (entropy regularization).
    """
    vol_t = float(volume(t))
    
    # Mori cone volumes
    v56 = float(abs(gen56 @ t))
    v74 = float(abs(gen74 @ t))
    
    # Targets
    target56 = 12 * LN_PHI  # 5.77 for φ⁻¹²
    target74 = 10 * LN_PHI  # 4.81 for φ⁻¹⁰ (slightly smaller for q₃=8)
    
    # Errors
    err_vol = ((vol_t - KAPPA3) / KAPPA3) ** 2
    err56 = ((v56 - target56) / target56) ** 2
    err74 = ((v74 - target74) / target74) ** 2
    
    # Entropy regularization (keep t_i large enough)
    eps = 1e-12
    entropy = -np.sum(np.log(np.maximum(t, eps)))
    
    # Weights — Mori cone MUST dominate
    w_vol = 1e8
    w_mori = 1e6  # 強制瞬子體積
    w_ent = 1e-4  # 微量 regularizer
    
    return w_vol * err_vol + w_mori * (err56 + err74) + w_ent * entropy

# Initial: near-uniform
t0 = np.ones(37) * 0.09
bounds = [(1e-8, None)] * 37

print("\nOptimizing J* for Mori cone quantization...")
t_start = time.time()
res = minimize(objective_and_grad, t0, method='L-BFGS-B', bounds=bounds,
               options={'maxiter': 5000, 'ftol': 1e-15})
t_opt = res.x
dt = time.time() - t_start

vol_opt = float(volume(t_opt))
v56_opt = float(abs(gen56 @ t_opt))
v74_opt = float(abs(gen74 @ t_opt))
q56 = math.exp(-v56_opt)
q74 = math.exp(-v74_opt)

print(f"\nOptimizer: {res.success}, {res.nit} iter, {dt:.1f}s")
print(f"Vol(J*) = {vol_opt:.6e} (target {KAPPA3:.6e})")
print(f"gen56·J = {v56_opt:.4f} (target {12*LN_PHI:.4f}) → q={q56:.4f} = φ^{-v56_opt/LN_PHI:.2f}")
print(f"gen74·J = {v74_opt:.4f} (target {10*LN_PHI:.4f}) → q={q74:.4f} = φ^{-v74_opt/LN_PHI:.2f}")
print(f"t range: [{t_opt.min():.6f}, {t_opt.max():.6f}], ||t||={np.linalg.norm(t_opt):.4f}")

# Compute FN charges
kappa_ij = np.einsum('ijk,k->ij', K, t_opt)
div_vols = 0.5 * np.einsum('ij,j->i', kappa_ij, t_opt)
k_i = np.zeros(37)
for i in range(37):
    if div_vols[i] > 1e-15:
        k_i[i] = -math.log(div_vols[i] / vol_opt) / LN_PHI
    else:
        k_i[i] = float('nan')

# Charge mapping
with open(f"{DATA}/phase5c_jstar_fn.json") as f:
    fn32 = json.load(f)
charge_rays = {12:[2],10:[4],8:[6],7:[19,20],6:[7,8,9,21]}

print(f"\nFN charges at quantized J*:")
print(f"{'Chg':>4s} {'Ray':>4s} {'t_i':>10s} {'Vol(D)':>12s} {'k':>8s} {'IDCM':>8s} {'δ':>6s}")
print("-"*58)
idcm_preds = {10: 33*BETA, 8: 26*BETA-PHI_INV**4, 6: 19*BETA}
for c in sorted(charge_rays, reverse=True):
    for r in charge_rays[c]:
        kv = k_i[r]
        idcm = idcm_preds.get(c)
        if not math.isnan(kv):
            delta = abs(kv - idcm) if idcm else 0
            sym = "✅" if (idcm and delta < 0.5) else ("🟡" if idcm and delta < 2.0 else "❌" if idcm else "—")
            idcm_s = f"{idcm:.2f}" if idcm else "—"
            delta_s = f"{delta:.2f}" if idcm else "—"
            print(f"  {c:3d}  r={r:2d}  {t_opt[r]:8.4f}  {div_vols[r]:10.3e}  {kv:6.2f}  {idcm_s:>8s}  {delta_s:>6s}  {sym}")

# All other generators at this J*
print(f"\nAll 185 Mori cone generators at quantized J*:")
all_vols = np.array([abs(g @ t_opt) for g in mori_gen])
order = np.argsort(-all_vols)
print(f"{'#':>4s} {'Vol':>8s} {'n':>6s} {'q':>8s} {'φ⁻ⁿ':>6s}")
for rank in range(min(20, len(order))):
    idx = order[rank]
    v = all_vols[idx]
    n = v / LN_PHI
    q = math.exp(-v)
    nr = round(n)
    print(f"{idx:4d} {v:8.4f} {n:6.2f} {q:8.4f} φ⁻{nr:2d}")

# Save results
res_out = {
    "t_i": [float(t) for t in t_opt],
    "vol": float(vol_opt),
    "gen56_vol": float(v56_opt), "gen56_q": float(q56),
    "gen74_vol": float(v74_opt), "gen74_q": float(q74),
    "k_i": [float(k) if not math.isnan(k) else None for k in k_i],
}
with open(f"{DATA}/jstar_quantized.json", "w") as f:
    json.dump(res_out, f, indent=2)
print(f"\nSaved: {DATA}/jstar_quantized.json")
print("DONE")
