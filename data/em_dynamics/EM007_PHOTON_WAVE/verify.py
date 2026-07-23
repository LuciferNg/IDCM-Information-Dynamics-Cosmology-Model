#!/usr/bin/env python3
"""EM007: Photon Wave — Verification Script

Key claims:
1. ω² = c²k² + ω_p² with ω_p² = c²(κ+ε)
2. m_γ = ℏ√(κ+ε) ≈ 1.5×10⁻³³ eV
3. Photon mass below experimental bound
4. g_eff ∼ ε/f_a for axion-like coupling
"""

import numpy as np
import sys

φ = (1 + np.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16

# Physical constants
c = 299792458  # m/s
hbar = 1.054571817e-34  # J·s
eV_J = 1.602176634e-19  # J/eV

print("="*60)
print("EM007: Photon Wave — Verification")
print("="*60)

# ─── 1. Photon dispersion ───
print("\n1. Photon dispersion relation")
print("   ω² = c²k² + ω_p²")
ω_p2 = c**2 * (κ + ε)
ω_p = np.sqrt(ω_p2)
print(f"   ω_p² = c²(κ+ε) = c² × ({κ} + {ε:.6f})")
print(f"   ω_p² = {ω_p2:.4e} (m²/s²)")
print(f"   ω_p = {ω_p:.4e} rad/s")
print(f"   f_p = {ω_p/(2*np.pi):.4e} Hz")
print("   Status: ✅ Algebraically consistent")

# ─── 2. Photon mass ───
print("\n2. Effective photon mass")
m_γ = hbar * np.sqrt(κ + ε)  # in J
m_γ_eV = m_γ / eV_J
print(f"   m_γ = ℏ√(κ+ε)")
print(f"   ℏ = {hbar:.4e} J·s")
print(f"   √(κ+ε) = {np.sqrt(κ+ε):.6f}")
print(f"   m_γ = {m_γ:.4e} J")
print(f"   m_γ = {m_γ_eV:.4e} eV")
print(f"   Claimed: 1.5×10⁻³³ eV")

# Check: ℏ in eV·s = 6.582119569e-16 eV·s
# √(κ+ε) in s⁻¹ = √(0.217) × c ??? No, ω_p is in rad/s
# Let me redo in natural units
hbar_eVs = 6.582119569e-16  # eV·s
m_γ_eV_direct = hbar_eVs * np.sqrt(κ + ε) * c  # Wait, this is wrong
# m_γ = ℏω_p/c² in natural units? No...
# In natural units c=1, m_γ = ℏ·√(κ+ε) (since ω_p = √(c²(κ+ε)) = √(κ+ε) in c=1)
# In SI: m_γ = ℏ·ω_p/c² = ℏ·√(c²(κ+ε))/c² = ℏ·√(κ+ε)/c
m_γ_SI = hbar * np.sqrt(κ + ε) / c
m_γ_SI_eV = m_γ_SI / eV_J
print(f"   m_γ (corrected) = ℏ√(κ+ε)/c = {m_γ_SI_eV:.4e} eV")
print(f"   Claimed: 1.5×10⁻³³ eV")
print(f"   Status: {'✅' if abs(m_γ_SI_eV/1.5e-33 - 1) < 0.2 else '🟡'}")

# ─── 3. Experimental bound ───
print("\n3. Comparison with experimental bound")
m_γ_bound = 1e-18  # eV (from Coulomb's law tests)
print(f"   m_γ (IDCM) = {m_γ_SI_eV:.2e} eV")
print(f"   Experimental bound: {m_γ_bound} eV")
print(f"   Ratio: {m_γ_SI_eV/m_γ_bound:.2e}")
print(f"   Status: ✅ (far below bound)")

# ─── 4. Photon in condensate ───
print("\n4. Photon inside W-field condensate")
m_γ_cond = hbar_eVs * np.sqrt(κ) / c  # Wait, same issue
# m_γ_cond = ℏ√κ/c
m_γ_cond_eV = hbar_eVs * np.sqrt(κ) / c  # No, let me be careful
# Actually: m_γ = ℏ·ω_p/c², and ω_p² = c²(κ+ε·Φ)
# For condensate Φ<1, so m_γ_cond = ℏ√(κ)/c (if Φ→0)
m_γ_cond_eV = hbar_eVs * np.sqrt(κ)  # In natural units this is correct
# hbar_eVs gives eV·s, √κ gives s⁻¹, product gives eV...
# Actually in natural units: m_γ = √(κ+ε) in eV when ℏ=c=1
# To convert to SI: m_γ(SI) = √(κ+ε) × (ℏ·c) in eV
# Since ℏc = 197.327 MeV·fm = 1.97327e-7 eV·m
# No wait, that's not right either.
# Let me just use the simpler approach:
# m_γ(eV) = √(κ+ε) in natural units × (ℏc) → convert to eV
# In natural units, mass has dimension of energy
# √(κ+ε) is dimensionless, so m_γ = √(κ+ε) eV? No.
# κ+ε is dimensionless, √(κ+ε) is dimensionless
# m_γ = ℏ√(c²(κ+ε))/c² = ℏ√(κ+ε)/c
# In SI: m_γ(kg) = ℏ√(κ+ε)/c³... no
# Let me just use the formula from the doc directly
# m_γ² = ℏ²(κ+ε) (in natural units ℏ=1, c=1)
# To convert: m_γ(eV) = √(κ+ε) × 1 (in natural units)

# Actually in natural units ℏ=c=1, everything is in eV
# But κ+ε is dimensionless. So m_γ² = κ+ε (in natural units ℏ=c=1)?
# That would give m_γ ~ 0.5, which is clearly wrong (photon mass ~0)
# 
# I think the formula ω_p² = c²(κ+ε) is in SI units where κ has
# dimension 1/m². But κ is defined as 1/16 (dimensionless).
# 
# This is the same dimensional issue as EM001. The W-field PDE
# ∇²A = κA has κ with dimension 1/length², but κ is given as 1/16
# (dimensionless). So the whole dispersion relation is dimensionally
# inconsistent.

print("\n   ⚠️ DIMENSIONAL NOTE: The claim m_γ = ℏ√(κ+ε) ≈ 1.5×10⁻³³ eV")
print("   assumes κ has dimension 1/length², but κ = 1/16 is dimensionless.")
print("   The dimensional analysis is inconsistent.")

# Let me compute what the doc actually says
# m_γ² = ℏ²/c² · ω_p² = ℏ²/c² · c²(κ+ε) = ℏ²(κ+ε)
# m_γ = ℏ√(κ+ε)
# ℏ = 6.582e-16 eV·s
# √(κ+ε) = √(0.217) = 0.466 s⁻¹? No, that's not right.
# κ+ε = 0.217, but κ has dimension 1/s² in the PDE
# The PDE ∇²A = κA in SI: κ has dimension 1/m²
# But the doc says κ = 1/16 (dimensionless) — this is the issue

print(f"\n   κ+ε = {κ+ε:.6f}")
print(f"   ℏ√(κ+ε) = {hbar_eVs*np.sqrt(κ+ε):.4e} eV   (using ℏ in eV·s)")
print(f"   This gives {hbar_eVs*np.sqrt(κ+ε):.4e} eV, not 1.5e-33 eV")
print("   🔴 The claimed value 1.5×10⁻³³ eV cannot be reproduced")
print("   without additional dimensionful conversion factors")

# ─── 5. Axion-like coupling ───
print("\n5. Axion-like coupling")
print("   g_eff ∼ ε/f_a, f_a ∼ M_P/√𝒩")
print("   For 𝒩 ∼ 10¹⁰: g_eff ∼ 10⁻¹² GeV⁻¹")
print("   Status: 🔲 Scaling argument — no numerical verification")
print("   The 𝒩 value is not derived from first principles")

# ─── Summary ───
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print("🟡  ω² = c²k² + ω_p² is algebraically consistent")
print("🔴  m_γ = ℏ√(κ+ε) ≈ 1.5×10⁻³³ eV cannot be reproduced")
print("    (dimensional inconsistency in κ)")
print("✅  If correct, m_γ is far below experimental bound")
print("🔲  Axion-like coupling — scaling argument")
print("")
print("FINAL VERDICT: 🔴 Photon mass claim has same dimensional issue")
print("as EM001. κ is dimensionless (1/16) but used as dimensionful.")
print("="*60)
sys.exit(0)