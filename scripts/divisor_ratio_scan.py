#!/usr/bin/env python3
"""
Systematic divisor ratio scan for V_cb, V_ub, V_us
"""
import numpy as np, json, math

PHI = (1+5**0.5)/2
BASE = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

kv = np.load(f"{BASE}/kappa_vector_jstar.npy")
aa = np.load(f"{BASE}/AA_jstar.npy")
with open(f"{BASE}/monad_definition.json") as f:
    mdata = json.load(f)
glsm = np.array(mdata["glsm_charge_matrix"])

# Targets
T = {"V_us": 0.2243, "V_cb": 0.04178, "V_ub": 0.003630, "V_td": 0.0086, "V_ts": 0.0400, "V_tb": 0.9991}

# Diag κ info
print("Divisor |κ| rank (top 10):")
idx_rank = np.argsort(-np.abs(kv))
for rank in range(10):
    i = idx_rank[rank]
    pe = -math.log(abs(kv[i]/kv[idx_rank[0]]), PHI) if abs(kv[i])>1e-100 and abs(kv[idx_rank[0]])>1e-100 else 0
    print(f"  D_{i:>2}: |κ|={abs(kv[i]):.4e}  φ^{pe:.3f}  κ={kv[i]:.4e}")

# Systematic scan
for target, pdg in T.items():
    print(f"\n=== Best {target} (PDG={pdg}) ratios ===")
    best = []
    for i in range(32):
        for j in range(32):
            if i == j or abs(kv[j]) < 1e-100: continue
            ratio = abs(kv[i]/kv[j])
            err = abs(ratio - pdg)/pdg
            pe_i = -math.log(abs(kv[i]/kv[28]), PHI) if abs(kv[i])>1e-100 and abs(kv[28])>1e-100 else 0
            pe_j = -math.log(abs(kv[j]/kv[28]), PHI) if abs(kv[j])>1e-100 and abs(kv[28])>1e-100 else 0
            best.append((err, i, j, ratio, pe_i, pe_j))
    best.sort(key=lambda x: x[0])
    for err, i, j, ratio, pe_i, pe_j in best[:8]:
        print(f"  |κ[D_{i:>2}]/κ[D_{j:>2}]| = {ratio:.6f}  err={err*100:.2f}%  [φ^{pe_i:.2f}/φ^{pe_j:.2f}]")

# Also check IDCM formula denominators
print(f"\n=== IDCM formula check ===")
print(f"V_us = φ^(-3) = {PHI**(-3):.6f} vs PDG 0.2243")
print(f"V_cb = φ^(-6.6) = {PHI**(-6.6):.6f} vs PDG 0.04178")

# Which divisor φ-exponent gives the IDCM formula numbers?
for p_exp in [3.0, 6.6, 8.8, 10.6, 7.6, 11.6]:
    val = PHI**(-p_exp)
    print(f"  φ^(-{p_exp:.1f}) = {val:.6f}")

# AA eigenvalue ratios
aa_eigs = sorted(np.abs(np.linalg.eigvalsh(aa)))[::-1]
print(f"\n=== AA eigenvalue ratios ===")
for target, pdg in T.items():
    for k in range(1, min(15, len(aa_eigs))):
        ratio = aa_eigs[k]/aa_eigs[0]
        err = abs(ratio - pdg)/pdg
        if err < 2.0:
            print(f"  AA λ_{k}/λ_0 = {ratio:.6f}  → {target}: err={err*100:.1f}%")
            break
