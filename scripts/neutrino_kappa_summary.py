#!/usr/bin/env python3
"""
Neutrino κ Summary — key numbers only
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json, math, sys
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1+5**0.5)/2; PHII = PHI-1; EPS = PHII/4; KAP = 1/16
V_EW = 174.0; MP = 1.22e19
def phi_exp(x): return -math.log(abs(x))/math.log(PHI) if abs(x) > 1e-300 else float('inf')
def kappa_get(d, i, j, k):
    for perm in [(i,j,k),(i,k,j),(j,i,k),(j,k,i),(k,i,j),(k,j,i)]:
        key = f"{perm[0]},{perm[1]},{perm[2]}"
        if key in d: return d[key]
    return 0

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
cy = poly.triangulate().get_cy()
with open(DATA/"Jstar_36D.json") as f: jd = json.load(f)
with open(DATA/"kappa_36d_raw.json") as f: kr = json.load(f)
with open(DATA/"cy36_98_final.json") as f: fn = json.load(f)

Jstar = np.array(jd["Jstar_36D"])
glsm = np.array(fn["glsm_coord3"], dtype=int)
charges = np.zeros(36, dtype=int); charges[:len(glsm)] = glsm
K = kr["kappa"]

# κ_vector @ J*
tloc = Jstar[:32].tolist()
kv = np.array(cy.compute_kappa_vector(tloc))

# ─── Div 7 (ν_R₁) N·N·φ contributions ───
print("="*70)
print("  1. ν_R₁ (D_7, q=6) — N·N·φ terms")
print("="*70)
total_MR1 = 0
for k in range(36):
    v = kappa_get(K, 7, 7, k)
    if v != 0:
        contrib = v * 64 * Jstar[7]**2 * Jstar[k] * MP
        total_MR1 += contrib
        print(f"    κ[7,7,{k}]={v:>+4.0f} J*_k={Jstar[k]:.4e} → M_R+= {contrib:.4e} GeV")
print(f"    Σ M_R = {total_MR1:.4e} GeV")

# ─── κ[2,7,7] Dirac Yukawa ───
print(f"\n{'='*70}")
print("  2. Dirac Yukawa Y_ν from κ[2,7,7]")
print("="*70)
y_nu = kappa_get(K, 2, 7, 7)
kinetic = 64 * math.sqrt(Jstar[2] * Jstar[7]**2)
Y_nu = y_nu * kinetic
print(f"    κ[2,7,7] = {y_nu}")
print(f"    kinetic = 64 × √(J*_2 × J*_7²) = {kinetic:.4f}")
print(f"    Y_ν = κ[2,7,7] × kinetic = {Y_nu:.4f}")

# ─── Seesaw deep-dive ───
print(f"\n{'='*70}")
print("  3. TYPE I SEESAW — all terms")
print("="*70)

# Full seesaw from κ[N,N,φ] summed over all φ_k
eK2 = 64
for a, na in enumerate([7, 9, 20]):
    MR_diag = 0
    for k in range(36):
        v = kappa_get(K, na, na, k)
        if v != 0:
            MR_diag += v * eK2 * Jstar[na]**2 * Jstar[k]
    MR_diag *= MP
    
    # Dirac
    yv = kappa_get(K, 2, na, na)
    Y = yv * eK2 * math.sqrt(Jstar[2] * Jstar[na]**2)
    
    # Seesaw
    m_nu_GeV = Y**2 * V_EW**2 / abs(MR_diag)
    print(f"\n  ν_R at D_{na} (q={charges[na]}):")
    print(f"    M_R = {MR_diag:.4e} GeV")
    print(f"    Y_ν = {Y:.4f}")
    print(f"    Seesaw m_ν = {m_nu_GeV*1e9:.6e} eV  (obs ~0.05)")
    print(f"    IDCM κ·ε^14·v = {KAP*EPS**14*V_EW*1e9:.4f} eV")
    print(f"    Ratio CY/IDCM = {m_nu_GeV*1e9/(KAP*EPS**14*V_EW*1e9):.4f}")

# ─── κ_vector hierarchy for lepton sector ───
print(f"\n{'='*70}")
print("  4. κ_VECTOR LEPTON HIERARCHY @ J*")
print("="*70)

kv_max = max(abs(kv))
q6 = [7, 8, 9, 21]
print(f"\n  Top λ: κ_vector = {max(kv):.4f} at D_28 (q=3)")
print(f"  κ_vector range: [{kv.min():.4f}, {kv.max():.4f}]")
print(f"\n  Lepton (q=6) hierarchy from κ_vector:")
print(f"  {'Div':>4} {'J*_i':>10} {'κ_vec':>10} {'φ-exp':>8} {'IDCM label':>12}")
print(f"  {'─'*4} {'─'*10} {'─'*10} {'─'*8} {'─'*12}")
for d in q6:
    y = kv[d]
    rel = y/kv_max
    exp = -math.log(abs(rel))/math.log(PHI) if rel != 0 else float('inf')
    label = {7: "τ(ν₃)", 9: "μ(ν₂)", 8: "e(ν₁)", 21: "?"}.get(d, "?")
    print(f"  {d:>4} {Jstar[d]:>10.4e} {y:>+10.4f} {exp:>8.3f} {label:>12}")

# ─── Check: κ[0,2,2] = +6 is H·H·Φ₀, NOT N·N·Φ₀ ───
print(f"\n{'='*70}")
print("  5. κ[0,2,2]=+6 IS NOT NEUTRINO MAJORANA")
print("="*70)
print(f"\n  κ[0,2,2] involves divisors (0,2,2):")
print(f"    ν_R lives on D_7, D_9, D_20, NOT D_2")
print(f"    κ[0,2,2] = H·H·Φ₀ (Higgs-Higgs-φ coupling)")
print(f"    → κ[0,2,2] is Higgs MASS term, NOT N·N·φ")
print(f"\n  κ[0,2,2] = +6 gives tree-level µ-term in superpotential:")
print(f"    W = µ·H_u·H_d where µ = κ[0,2,2] × ⟨Φ₀⟩")
print(f"    µ ∼ 6 × 64 × J*_0 × MP = 6 × 64 × {Jstar[0]:.4e} × {MP:.2e}")
print(f"    µ ∼ {6 * eK2 * Jstar[0] * MP:.4e} GeV  → too large!")
print(f"    → SUSY µ-problem — µ must be ∼ 100-1000 GeV")
print(f"    → This means Φ₀ VEV is NOT at J* for µ-term")
print(f"    → Similarly, N·N·φ VEVs may NOT be at J* either")

# ─── Final comparison ───
print(f"\n{'='*70}")
print("  6. FINAL: κ VECTOR vs φ-EXPONENT MATCH")
print("="*70)

kv_norm = kv / max(abs(kv))
print(f"\n  IDCM k-values for lepton:")
# From v2.2 neutrino doc: k_1=106.2, k_2=101.2, k_3=97.6
# These are in the φ^-k hierarchy of M_P
# But κ_vector eigenvalues are relative Yukawa strengths
# Need to compare: κ_vector Y_eff ratios → φ-exponent differences

for d, label, k_pred, m_pred_eV in [(7, "ν₃(τ)", 97.55, 0.048),
                                       (9, "ν₂(μ)", 101.21, 0.0074),
                                       (8, "ν₁(e)", 106.21, 0.0011)]:
    y_kv = kv[d]
    y_rel = abs(y_kv/kv_max)
    kv_exp = phi_exp(y_rel) if y_rel > 0 else None
    
    # m_ν from κ_vector: map Y_eff to m_ν via some relation
    # The Y_eff ~ kv[d] is the κ·J contraction → Yukawa eigenvalue
    # The m_ν IDCM formula: m_ν = κ·ε^k·v
    # Map: kv_exp roughly corresponds to the log of the mass ratio
    
    print(f"\n  {label} (D_{d}):")
    print(f"    κ_vector Y_eff = {y_kv:+.4f} (rel={y_rel:.4f})")
    print(f"    κ_vector φ-exp = {kv_exp:.2f}" if kv_exp else "")
    print(f"    IDCM k = {k_pred:.2f}, m = {m_pred_eV:.4f} eV")
    print(f"    IDCM ε^k: κ·ε^{k_pred}·v = {KAP*EPS**k_pred*V_EW*1e9:.6f} (mismatch because ε^k != φ^-k)")

print(f"\n{'='*70}")
print(f"  VERDICT: κ tensor confirms structure, seesaw needs moduli tuning")
print(f"  The tree-level M_R from κ[N,N,φ] at J* is ~10¹⁸ GeV")
print(f"  → ~10³× too large for observed m_ν via seesaw")
print(f"  → But consistent with IDCM claim that ν sector needs instantons")
print(f"  → κ_vector hierarchy: D_7(τ) > D_9(μ) > D_21/D_8(e)")
print(f"  → κ[0,2,2]=+6 identified as µ-term, NOT N·N·φ")
print(f"{'='*70}")
sys.stdout.flush()
