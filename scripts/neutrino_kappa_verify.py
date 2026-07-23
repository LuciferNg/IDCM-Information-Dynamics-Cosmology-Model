#!/usr/bin/env python3
"""
Neutrino Sector κ Tensor Verification — CYTools based
=====================================================
1. κ_vector extraction for neutrino-sector effective Yukawa eigenvalues
2. Seesaw mechanism verification: m_ν ~ (Y_ν·v)² / M_R
3. Off-diagonal κ terms for PMNS mixing structure
4. Comparison with v2.2 neutrino predictions
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np
import json, math, sys
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1 + 5**0.5) / 2
PHII = PHI - 1
EPS = PHII / 4
KAP = 1/16
BETA = PHII / 2
V_EW = 174.0  # GeV
MP = 1.22e19  # GeV

np.set_printoptions(precision=6, suppress=True, linewidth=120)

def phi_pow(n):
    return PHII ** n

def phi_exp(x):
    if x <= 0: return float('inf')
    return math.log(x, PHI)

# ─── Load CY₃(36,98) ────────────────────────────────────────
print("="*72)
print("  NEUTRINO SECTOR κ TENSOR VERIFICATION")
print("  CY₃(36,98) — CYTools compute_kappa_vector @ J*")
print("="*72)

print("\nLoading CY₃(36,98)...")
poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate()
cy = tri.get_cy()
h11 = cy.h11()
print(f"  h¹¹ = {h11}, Smooth: {cy.is_smooth()}")

# ─── Load local data ─────────────────────────────────────────
with open(DATA / "Jstar_36D.json") as f: jdata = json.load(f)
with open(DATA / "kappa_36d_raw.json") as f: kappa_raw = json.load(f)
with open(DATA / "cy36_98_final.json") as f: final = json.load(f)

Jstar = np.array(jdata["Jstar_36D"])
glsm_charges = np.array(final["glsm_coord3"], dtype=int)
kappa_dict = kappa_raw["kappa"]

# Parse κ entries
kappa_entries = []
for key, val in kappa_dict.items():
    i, j, k = map(int, key.split(","))
    kappa_entries.append((i, j, k, float(val)))

# Map charge groups (32 GLSM + 4 extra)
n_glsm = len(glsm_charges)
charges = np.zeros(36, dtype=int)
charges[:n_glsm] = glsm_charges

charge_groups = {}
for idx in range(36):
    q = charges[idx]
    if q not in charge_groups: charge_groups[q] = []
    charge_groups[q].append(idx)

print(f"\nGLSM charges (32 entries): {dict(sorted(charge_groups.items()))}")

# 32D tloc for CYTools (divisor basis)
tloc_32d = Jstar[:32].tolist()
print(f"\nJ*[:32] min={min(tloc_32d):.6e}, max={max(tloc_32d):.6e}")

# ════════════════════════════════════════════════════════════
# 1. CYTools compute_kappa_vector @ J*
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  1. κ_VECTOR FROM CYTools @ J*")
print(f"{'='*72}")

kv = cy.compute_kappa_vector(tloc_32d)
kv_arr = np.array(kv)
print(f"  kappa_vector shape: {kv_arr.shape}")
print(f"  kappa_vector[:10]: {kv_arr[:10]}")

# The kappa_vector in special geometry outputs the Yukawa couplings.
# For a CY with h¹¹=32 divisor classes, the vector has 32 components
# corresponding to the Yukawa couplings contracted with the Kähler class.
print(f"  kappa_vector stats: min={kv_arr.min():.4f}, max={kv_arr.max():.4f}")

# ─── Effective Yukawa per charge sector ──────────────────────
print(f"\n  Per-charge-sector average κ_vector:")
for q in sorted(charge_groups.keys(), reverse=True):
    divs = charge_groups[q]
    vals = [kv_arr[d] for d in divs if d < len(kv_arr)]
    if not vals: continue
    mean_val = np.mean(vals)
    std_val = np.std(vals)
    print(f"    q={q:>3}: mean={mean_val:>+.6f}, std={std_val:.6f}, n={len(vals)}")

# ════════════════════════════════════════════════════════════
# 2. MAJORANA MASS MATRIX FROM κ[2,2,i]
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  2. MAJORANA MASS MATRIX — N·N·φ couplings")
print(f"{'='*72}")

# Right-handed neutrino: divisor 2 (q=12)
# N·N·φ terms: κ[2,2,0]=+6, κ[2,2,3]=+3, κ[2,2,20]=+3
majorana_terms = [
    (2, 2, 0, "κ[2,2,0]"),
    (2, 2, 3, "κ[2,2,3]"),
    (2, 2, 20, "κ[2,2,20]"),
]
# Majorana couplings (N·N·φ) — κ is symmetric, check all permutations
print(f"\n  Majorana couplings (N·N·φ):")
for i, j, k, label in majorana_terms:
    val = kappa_dict.get(f"{i},{j},{k}", 0)
    if val == 0: val = kappa_dict.get(f"{j},{i},{k}", 0)
    if val == 0: val = kappa_dict.get(f"{j},{k},{i}", 0)
    if val == 0: val = kappa_dict.get(f"{i},{k},{j}", 0)
    qi, qj, qk = charges[i], charges[j], charges[k]
    print(f"    {label} = {val:>+3.0f}  (qi={qi}, qj={qj}, qk={qk})")

# The three different κ[2,2,φ_k] terms give different φ VEV directions
# → 3×3 Majorana mass matrix for 3 right-handed neutrinos
# In the flavor basis where each N has the same divisor 2,
# the different φ_k directions give the mixing structure.

# Build 3×3 Majorana mass matrix
# The 3 right-handed neutrinos are associated with divisors (7, 9, 20) 
# from the κ[2,7,7], κ[2,9,9], κ[2,20,20] pattern
N_divisors = [7, 9, 20]  # Three ν_R generations
N_charges = [charges[d] for d in N_divisors]

print(f"\n  Right-handed neutrino divisors: {N_divisors}")
print(f"  N charges: {N_charges}")
print(f"  GLSM charges: q_N = {[charges[d] for d in N_divisors]}")
print(f"  q_N = {charges[7]} -> H·L·N charge sum = {charges[2]}+{charges[7]}+{charges[7]}", 
      f"= {charges[2]+charges[7]*2} {'✅' if charges[2]+charges[7]*2==24 else '❌≠24'}")

# Build 3×3 Majorana matrix
M_R_matrix = np.zeros((3, 3))
# Diagonal: κ[2,N_a,N_a] 
for a, d in enumerate(N_divisors):
    key = f"2,{d},{d}"
    val = kappa_dict.get(key, 0)
    print(f"    κ[2,{d},{d}] = {val}")
    # Full strength: κ_val × e^{K/2} × t_2 × t_d² × M_P
    # t_2 and t_d are Kähler parameters
    kinetic = 64 * Jstar[2] * Jstar[d]**2  # e^{K/2} = 64 from Vol=κ³
    M_R_matrix[a, a] = val * kinetic * MP

# Off-diagonal: κ[2,N_a,N_b]
for a, da in enumerate(N_divisors):
    for b, db in enumerate(N_divisors):
        if a >= b: continue
        key = f"2,{da},{db}"
        if key not in kappa_dict:
            key = f"2,{db},{da}"
            if key not in kappa_dict:
                key = f"{da},{db},2" if f"{da},{db},2" in kappa_dict else None
        if key is None:
            # Check all permutations
            for pi, pj, pk, pv in kappa_entries:
                if pi == 2 and set([pj,pk]) == set([da,db]):
                    key = f"{pi},{pj},{pk}"
                    val = pv
                    break
        else:
            val = kappa_dict.get(key, 0)
        if key is None:
            val = 0

        if val != 0:
            kinetic = 64 * Jstar[2] * Jstar[da] * Jstar[db] * MP
            M_R_matrix[a, b] = val * kinetic
            M_R_matrix[b, a] = val * kinetic

# κ[2,7,7] = -32 → τ Yukawa 
# κ[2,9,9] = -2 
# κ[2,20,20] = -5

# Rebuild diagonal from κ[2,7,7], κ[2,9,9], κ[2,20,20]
for a, d in enumerate(N_divisors):
    key = f"2,{d},{d}"
    val = kappa_dict.get(key, 0)
    kinetic = 64 * Jstar[2] * Jstar[d]**2
    M_R_full = val * kinetic * MP
    M_R_matrix[a, a] = M_R_full
    print(f"  M_R[{a},{a}] = κ[2,{d},{d}] × 64 × J*_2 × J*_{d}² × M_P")
    print(f"         = {val} × 64 × {Jstar[2]:.4e} × {Jstar[d]:.4e}² × {MP:.2e}")
    print(f"         = {M_R_full:.4e} GeV")

print(f"\n  3×3 Majorana mass matrix (GeV):")
for row in M_R_matrix:
    print(f"    [{row[0]:>12.4e}  {row[1]:>12.4e}  {row[2]:>12.4e}]")

# Diagonalize
M_R_eigvals, M_R_eigvecs = np.linalg.eigh(M_R_matrix)
print(f"\n  Eigenvalues (GeV): {M_R_eigvals}")
print(f"  φ-exponents of M_R: {[phi_exp(abs(e)/MP) if e != 0 else float('inf') for e in M_R_eigvals]}")

# The seesaw scale (dominant eigenmass)
M_R_dom = np.max(np.abs(M_R_eigvals))
print(f"\n  Dominant M_R = {M_R_dom:.4e} GeV")
print(f"  (cf. GUT scale ~10¹⁵-10¹⁶ GeV)")

# ════════════════════════════════════════════════════════════
# 3. DIRAC YUKAWA FROM κ[2,7,7] & κ_VECTOR
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  3. DIRAC YUKAWA — H·L·N couplings")
print(f"{'='*72}")

# Higgs = divisor 2 (charge 12), Lepton = divisor 7 (charge 6)
# The Dirac Yukawa Y_ν comes from κ[2,7,7] and κ[2,9,9]
# κ[2,7,7] = -32, κ[2,9,9] = -2

# The three generations come from three different lepton divisors
# all with charge 6: divisors 7, 9, 20 (and 8 from neutrino doc)
# Actually let me check which divisors are charge 6
q6_divs = charge_groups.get(6, [])
print(f"  Divisor group q=6 (lepton): {q6_divs}")
print(f"  Divisor group q=12 (Higgs/ν_R): {charge_groups.get(12, [])}")

# Build 3×3 Dirac Yukawa from κ[H, L_i, L_j]
# Y_ν = κ[2, L_i, L_j] × (kinetic factors) @ J*
Y_D = np.zeros((3, 3))

for a, d_a in enumerate(N_divisors):
    for b, d_b in enumerate(N_divisors):
        # Direct κ[2, d_a, d_b]
        key = f"2,{d_a},{d_b}"
        val = kappa_dict.get(key, 0)
        if val == 0:
            key = f"2,{d_b},{d_a}"
            val = kappa_dict.get(key, 0)
        if val == 0:
            key = f"{d_a},{d_b},2"
            val = kappa_dict.get(key, 0)
        if val == 0:
            # Check all permutations
            for pi, pj, pk, pv in kappa_entries:
                if pi == 2:
                    if set([pj,pk]) == set([d_a,d_b]):
                        val = pv
                        break
        
        # Kinetic factor: K_ν = e^{K/2} / sqrt(G_HH·G_LL·G_NN)
        # Approximate: kinetic ~ 64 × J*_2^{1/2} × J*_{d_a}^{1/2} × J*_{d_b}^{1/2}
        kinetic = 64 * math.sqrt(Jstar[2] * Jstar[d_a] * Jstar[d_b])
        Y_D[a, b] = val * kinetic
        if val != 0:
            print(f"  Y_D[{a},{b}] = κ[2,{d_a},{d_b}] = {val} × K ≈ {val} × {kinetic:.4e} = {Y_D[a,b]:.6e}")

print(f"\n  3×3 Dirac Yukawa matrix (Y_ν):")
for row in Y_D:
    print(f"    [{row[0]:>+10.4e}  {row[1]:>+10.4e}  {row[2]:>+10.4e}]")

# κ_vector contains the Yukawa eigenvalues directly
print(f"\n  κ_VECTOR projection onto lepton sector (q=6):")
for d in q6_divs:
    y_kv = kv_arr[d] if d < len(kv_arr) else 0
    print(f"    D_{d}: q={charges[d]}, Y_eff(kv) = {y_kv:+.6f}")

# ════════════════════════════════════════════════════════════
# 4. TYPE I SEESAW
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  4. TYPE I SEESAW — m_ν = Y_ν² · v² / M_R")
print(f"{'='*72}")

# Full seesaw: m_ν = Y_D · M_R^{-1} · Y_D^T · v²
# M_R has large GUT-scale eigenvalues → invert carefully
M_R_inv = np.linalg.inv(M_R_matrix)
m_nu_matrix = Y_D @ M_R_inv @ Y_D.T * V_EW**2

print(f"\n  Light neutrino mass matrix (eV):")
m_nu_eV = m_nu_matrix * 1e9  # Convert GeV to eV
for row in m_nu_eV:
    print(f"    [{row[0]:>+10.4e}  {row[1]:>+10.4e}  {row[2]:>+10.4e}]")

# Diagonalize
m_nu_eigvals, m_nu_eigvecs = np.linalg.eigh(m_nu_eV)
# Sort: lightest first for NH
idx = np.argsort(np.abs(m_nu_eigvals))
m_nu_eigvals = m_nu_eigvals[idx]
m_nu_eigvecs = m_nu_eigvecs[:, idx]

print(f"\n  Neutrino mass eigenvalues (eV):")
for i, val in enumerate(m_nu_eigvals):
    abv = abs(val)
    print(f"    ν_{i+1}: m = {val:+.6e} eV  (|m| = {abv:.6e})")

abs_masses = np.sort(np.abs(m_nu_eigvals))
if len(abs_masses) >= 3:
    dmsq_21 = abs_masses[1]**2 - abs_masses[0]**2
    dmsq_32 = abs_masses[2]**2 - abs_masses[1]**2
    print(f"\n  Δm²_21 = {dmsq_21:.6e} eV²")
    print(f"  Δm²_32 = {dmsq_32:.6e} eV²")
    print(f"  (PDG: Δm²_21 = 7.39×10⁻⁵ eV², Δm²_32 = 2.51×10⁻³ eV²)")

# ════════════════════════════════════════════════════════════
# 5. OFF-DIAGONAL κ — PMNS MIXING STRUCTURE
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  5. OFF-DIAGONAL κ TERMS — PMNS mixing structure")
print(f"{'='*72}")

# Off-diagonal N·N·φ couplings drive PMNS mixing
# κ[2,2,3] and κ[2,2,20] break N generation degeneracy
print(f"\n  Off-diagonal Majorana couplings:")
for i, j, k, val in kappa_entries:
    if i == 2 and j == 2 and k not in [0, 2, 3, 20]:
        print(f"    κ[2,2,{k}] = {val} (extra)")
    if i == 2 and j != 2 and k != 2:
        # Mixing between different N generators
        if charges[j] == 6 and charges[k] == 6:
            print(f"    κ[2,{j},{k}] = {val} → lepton mixing (H·L_a·L_b)")

# Check off-diagonal among lepton sector
print(f"\n  All κ entries involving q=6 lepton divisors:")
q6_set = set(q6_divs)
for i, j, k, val in kappa_entries:
    divs_set = {i, j, k}
    if len(divs_set & q6_set) >= 2:
        labels = f"D_{i}(q={charges[i]}),D_{j}(q={charges[j]}),D_{k}(q={charges[k]})"
        print(f"    κ[{i},{j},{k}] = {val:>+4.0f}  → {labels}")

# PMNS mixing angles from M_R off-diagonal structure
print(f"\n  PMNS mixing from M_R matrix structure:")
for a in range(3):
    for b in range(a+1, 3):
        ratio_off_diag = abs(M_R_matrix[a,b]) / max(abs(M_R_matrix[a,a]), abs(M_R_matrix[b,b]))
        angle = np.arctan(ratio_off_diag)
        print(f"    M_R[{a},{b}]/max_diag = {ratio_off_diag:.4f} → θ ≈ {angle*180/math.pi:.1f}°")
        print(f"      cf. PMNS: θ₁₂≈33.4°, θ₂₃≈43°, θ₁₃≈8.6°")

# ════════════════════════════════════════════════════════════
# 6. COMPARISON WITH v2.2 PREDICTIONS
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  6. v2.2 NEUTRINO PREDICTION COMPARISON")
print(f"{'='*72}")

# Load neutrino predictions
with open(DATA / "neutrino_predictions_clean.json") as f: pred = json.load(f)

# IDCM formula: m_ν(k) = κ·ε^k·v
print(f"\n  IDCM formula m_ν = κ·ε^k·v:")
for k, label, target in [(14, "ν₃ (atm)", 0.048), (15, "ν₂ (solar)", 0.0074), (16, "ν₁ (NH)", 0.0011)]:
    m_pred = KAP * (EPS**k) * V_EW * 1e9  # eV
    print(f"    κ·ε^{k}·v = {m_pred:.4e} eV  ← {label} (target {target} eV)")

# Compare seesaw result
if len(abs_masses) >= 3:
    print(f"\n  {'='*72}")
    print(f"  {'Quantity':<20} {'Predicted':>15} {'v2.2 doc':>15} {'PDG':>15} {'Status':>10}")
    print(f"  {'─'*20} {'─'*15} {'─'*15} {'─'*15} {'─'*10}")
    
    # m_ν eigenvalues
    results = [
        ("m_ν₃", abs_masses[2], 0.05, 0.048),
        ("m_ν₂", abs_masses[1], 0.0086, 0.0074),
        ("m_ν₁", abs_masses[0], 0.0003, 0.0011),
    ]
    if len(abs_masses) >= 3:
        results += [
            ("Δm²₂₁", dmsq_21, 7.4e-5, 7.39e-5),
            ("Δm²₃₂", dmsq_32, 2.5e-3, 2.51e-3),
        ]
    
    for name, val, v22, pdg in results:
        ratio = val/pdg if pdg > 0 else float('inf')
        status = "✅" if abs(ratio-1) < 0.5 else ("🟡" if abs(ratio-1) < 2 else "🔴")
        print(f"  {name:<20} {val:>15.4e} {v22:>15.4e} {pdg:>15.4e} {status:>10}")

# ════════════════════════════════════════════════════════════
# 7. κ_VECTOR EIGENVALUE HIERARCHY
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  7. κ_VECTOR EIGENVALUE HIERARCHY")
print(f"{'='*72}")

# The kappa_vector at J* projects the Yukawa tensor onto the
# physical Kähler moduli direction.
# Top singular values give the Yukawa eigenvalue hierarchy.
kv_norm = kv_arr / np.max(np.abs(kv_arr))
top_indices = np.argsort(-np.abs(kv_arr))[:20]

print(f"\n  Top 20 κ_vector components:")
print(f"  {'Rank':>5} {'Div':>4} {'Charge':>8} {'Y_eff':>12} {'φ-exp':>10} {'Desc':>15}")
print(f"  {'─'*5} {'─'*4} {'─'*8} {'─'*12} {'─'*10} {'─'*15}")
for rank, idx in enumerate(top_indices):
    y_eff = kv_arr[idx]
    q = charges[idx] if idx < len(charges) else -1
    y_rel = y_eff / max(abs(kv_arr))
    exp = phi_exp(abs(y_rel)) if y_rel != 0 else float('inf')
    desc = f"q={q}" if q > 0 else "non-GLSM"
    print(f"  {rank:>5} {idx:>4} {q:>8} {y_eff:>+12.6f} {exp:>10.3f} {desc:>15}")

# ════════════════════════════════════════════════════════════
# 8. SUMMARY
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  8. VERDICT SUMMARY")
print(f"{'='*72}")

# Count how many κ entries are relevant per charge sector
print(f"\n  κ tensor statistics:")
print(f"    Total non-zero entries: {len(kappa_entries)}")
print(f"    Involving q=6 lepton group: ", end="")
lepton_count = sum(1 for i,j,k,v in kappa_entries if charges[i]==6 or charges[j]==6 or charges[k]==6)
print(f"{lepton_count}")

neutrino_count = sum(1 for i,j,k,v in kappa_entries if charges[i]==12 or charges[j]==12 or charges[k]==12)
print(f"    Involving q=12 (ν_R/Higgs) group: {neutrino_count}")

majorana_count = sum(1 for i,j,k,v in kappa_entries if charges[i]==12 and charges[j]==12 and charges[k]<=3)
print(f"    N·N·φ (Majorana) candidates: {majorana_count}")

print(f"\n  Seesaw consistency:")
print(f"    M_R scale: {M_R_dom:.4e} GeV (GUT-scale ✓)" if M_R_dom > 1e14 else f"    M_R scale: {M_R_dom:.4e} GeV (low!)")

print(f"\n{'='*72}")
sys.stdout.flush()
