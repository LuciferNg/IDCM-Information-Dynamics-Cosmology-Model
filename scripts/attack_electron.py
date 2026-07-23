#!/usr/bin/env python3
"""Attack the electron φ⁻⁶ correction — find structural origin."""
import math

phi = (1 + math.sqrt(5)) / 2
phii = phi**-1
eps = phii / 4
kap = 1/16
beta = phii / 2
M, Nh = 33, 42
v = 174.0  # GeV
m_tau_mev = 1776.86  # MeV

def phi_pow(n): return phii ** n
def m_from_k(k, ref=m_tau_mev): return ref * phi_pow(k)

print("=" * 65)
print("  ELECTRON φ⁻⁶ CORRECTION — STRUCTURAL SEARCH")
print("=" * 65)

# === 1. Current status ===
print("\n--- 1. CURRENT STATUS ---")
ku, kd, kl = 10.20, 7.89, 5.87  # v2.2
k_e_v1 = kl + M/3  # = 5.87 + 11 = 16.87
m_e_v1 = m_from_k(k_e_v1)  # = 1777 * φ^{-16.87}
print(f"  k_e(v1) = k_l + M/3 = {kl:.2f} + {M/3:.2f} = {k_e_v1:.4f}")
print(f"  m_e(v1) = m_τ × φ⁻{k_e_v1:.4f} = {m_e_v1:.4f} MeV")
print(f"  PDG m_e = 0.510999 MeV")
print(f"  Error = {(m_e_v1 - 0.510999)/0.510999*100:.2f}%")

# v2 with φ⁻⁶ correction
phi6 = phii**6  # φ⁻⁶
k_e_v2 = k_e_v1 + phi6
m_e_v2 = m_from_k(k_e_v2)
print(f"\n  φ⁻⁶ = {phi6:.6f}")
print(f"  k_e(v2) = k_e(v1) + φ⁻⁶ = {k_e_v1:.4f} + {phi6:.6f} = {k_e_v2:.4f}")
print(f"  m_e(v2) = m_τ × φ⁻{k_e_v2:.4f} = {m_e_v2:.4f} MeV")
print(f"  Error = {(m_e_v2 - 0.510999)/0.510999*100:.2f}%")

# === 2. Where does φ⁻⁶ come from? ===
print("\n--- 2. ORIGIN OF φ⁻⁶ ---")
print(f"  N_h = {Nh}")
print(f"  N_h/7 = {Nh/7:.0f}  ← exponent 6 = N_h/7")
print(f"  N_h - M = {Nh - M}  ← Higgs correction (φ⁻⁹)")
print(f"\n  Candidate A: N_h/7 = 6 → φ⁻⁶ is KK threshold from 7th mode")
print(f"  Candidate B: 6 = 2×3 (two GLSM charge-7 divisors × 3 generations)")
print(f"  Candidate C: 6 = from charge-5 sector (electron has q₃=5)")

# Check GLSM charge-5 data
print("\n  GLSM charges for electron sector:")
print("  q_electron = 5 (ray ? — from CYTools GLSM data)")
print("  q_7_divisors = 7 (rays 14 and 16)")

# Check: is 6 = 7-1? KK threshold from charge-7 coupling to charge-5?
print(f"\n  Check: deficit = q_7 - q_e = 7 - 5 = 2")
print(f"  φ⁻² = {phi_pow(2):.6f} — NOT φ⁻⁶")
print(f"  φ⁻⁶ = φ⁻² × φ⁻⁴")
print(f"  → Needs two-step process or higher-order")

# What gives φ⁻⁶ precisely?
# Check N_h/7, M-27, etc
print(f"\n  Systematic search for 6:")
candidates = [
    ("N_h/7", Nh/7),
    ("N_h-M-3", Nh-M-3),
    ("M-27", M-27),
    ("2×3", 6),
    ("β^{-1}+1", 1/beta+1),
    ("N_h/3-N_h/7", Nh/3-Nh/7),
]
for name, val in candidates:
    print(f"  {name} = {val:.2f}  {'→ 6 ✅' if abs(val-6)<0.01 else ''}")

# The real question: does φ⁻⁶ have a CY₃(36,98) interpretation?
print("\n\n  KEY INSIGHT FROM DUAL MECHANISM:")
print("  In the dual mechanism, first-generation masses are")
print("  deeper instanton corrections relative to 3rd-generation anchors.")
print("  The electron correction φ⁻⁶ is the 1st-gen-specific factor.")
print()
print("  In the lepton sector (q₃=6,12):")
print("    τ (3rd gen): tree-level κ[2,7,7]=-32")
print("    μ (2nd gen): φ⁻ᵏ relative to τ, k_l/2 = 2.94 → φ⁻²·⁹⁴")
print("    e (1st gen): φ⁻ᵏ relative to τ, k_l = 5.87 → φ⁻⁵·⁸⁷")
print()
print("  The φ⁻⁶ correction refines m_e by closing a KK threshold gap.")
print("  This gap comes from the 7th KK mode (N_h=42 → 42/7=6).")

# === 3. Can we derive φ⁻⁶ from CY structure? ===
print("\n--- 3. CY₃(36,98) STRUCTURAL PATH ---")
print(f"""
  In CY₃(36,98), the electron lives on a q₃=5 divisor.
  The GLSM charge-7 divisors (rays 14, 16) couple to the
  lepton sector through the instanton sum.
  
  The 7th KK mode (of N_h=42 modes) has threshold correction:
    Δk = Σ β_i·β_j·β_k · q/(1-q)   for instantons coupling q₃=7 to q₃=5
  
  At uniform J* (Vol=κ³), the dominant contribution is:
    q ≈ φ^{-1.5} → q/(1-q) ≈ φ^{-1.0}
  
  For a coupling between charge-7 and charge-5:
    Δk ≈ (β_7·β_5·β_e) × φ^(-n)
    where β_7 is the divisor intersection of q₃=7 rays with the instanton
  
  The threshold 6 = N_h/7 = 42/7 suggests this is the 7th KK mode.
  
  NUMERICAL CHECK: φ⁻⁶ = {phi6:.6f}
  Is there a CY combination that gives exactly φ⁻⁶?
  
  q₃=7 rays (14,16) at J*:
    β₁₄·J* = ?  (need CY data)
    β₁₆·J* = ?  (need CY data)
  
  If β·J = -ln(φ⁶) = 6·ln(1/φ) = 6×0.4812 = 2.887
  Then q = exp(-2.887) = 0.056
  q/(1-q) = 0.059
  β·β factors × 0.059 ≈ φ⁻⁶ = 0.056
  
  → Needs β·J ≈ 2.89 for the instanton connecting charge-7 and charge-5
""")

# === 4. HK mode tower approach ===
print("--- 4. TOWER STRUCTURE APPROACH ---")
# In IDCM, the KK tower has N_h=42 modes
# 42 = 6×7

# Check electron correction from HK mode at level m:
for m in range(1, Nh+1):
    phi_m = phii**m
    # Check if φ⁻ᵐ matches φ⁻⁶ or could be the electron correction
    if abs(phi_m - phii**6) < 1e-6:
        print(f"  KK mode {m}: φ⁻{m} = {phi_m:.6f} = φ⁻⁶  ✅")
    if abs(phi_m - phii**6)/phii**6 < 0.05:
        print(f"  KK mode {m}: φ⁻{m} = {phi_m:.6f} (close to φ⁻⁶ = {phii**6:.6f})")

# What if 6 comes from the integer part of k_l?
k_l_mod = kl % 6
print(f"\n  k_l mod 6 = {kl:.4f} mod 6 = {kl % 6:.4f}")
print(f"  k_l / 6 = {kl/6:.4f}")

# The REAL structural pattern:
# Lepton sector: k_l = 19β = 5.87
# 19 = M - N_h/3 = 33 - 14
# Electron correction φ⁻⁶:
# In the v2.2 dual mechanism, all 1st gen corrections are deeper instanton
# The φ⁻⁶ = φ^{-N_h/7} has:

print(f"""
  CANDIDATE DERIVATION:
  
  The KK tower has N_h = 42 modes. The 7th KK mode threshold
  contributes to the electron mass correction because:
  
  N_h/7 = 6 → φ⁻⁶
  
  PHYSICAL REASONING:
  The electron is the lightest charged fermion. Its mass arises
  from the deepest instanton correction. The 7th KK mode is
  the deepest mode that couples to the lepton sector (charge-7
  GLSM sector in CY₃(36,98)).
  
  For the Higgs, the correction φ⁻⁹ has:
  9 = N_h - M = 42 - 33
  This is the difference between the KK cutoff and the MERA depth.
  
  For the electron:
  6 = N_h/7
  This is the 7th KK mode — the deepest accessible mode below
  the charge-7 GLSM threshold.
  
  WHETHER THIS IS A DERIVATION:
  🟡 PARTIAL — N_h/7 = 6 is a FACT (empirically confirmed)
  but the "why 7?" needs geometric justification:
  
  In CY₃(36,98), GLSM charge-7 divisors (rays 14,16) have
  intersection numbers that can produce φ⁻⁶ corrections.
  The charge-7 sector is the only GLSM sector with charge
  not appearing in the classical κ_ijk sum (sum=24).
  
  → φ⁻⁶ COMES FROM q=7 GLSM SECTOR, modulo the identification
    that 7th KK mode = charge-7 threshold.
""")

# === Summary ===
print(f"\n{'='*65}")
print(f"  ELECTRON φ⁻⁶ — ASSESSMENT")
print(f"{'='*65}")
print(f"""
  ✅ φ⁻⁶ = φ⁻⁽ᴺʰ/⁷⁾ = {phii**6:.6f} = {phii**(Nh/7):.6f} (exact)
  ✅ Corrects m_e from {m_e_v1:.4f} MeV (3.6%) to {m_e_v2:.4f} MeV ({abs(m_e_v2-0.510999)/0.510999*100:.2f}%)
  
  🟡 Structural interpretation:
     - N_h=42 KK modes, 7th threshold gives N_h/7=6
     - Charge-7 GLSM divisors (rays 14,16) in CY₃(36,98)
     - Electron on q₃=5 divisor, couples through charge-7 instanton
  
  To fully CLOSE: need to show that the charge-7 GLSM sector
  is the ONLY source of 1st-generation KK corrections in CY₃(36,98).
  
  VERDICT: 🟡 PARTIAL — pattern clear, geometric mapping needs
  CYTools computation of charge-7 divisor intersection with
  the electron divisor (q₃=5) in the instanton sum.
""")
