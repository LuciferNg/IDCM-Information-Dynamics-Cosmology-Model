#!/usr/bin/env python3
"""
Detailed cross-checks for each P_n level.
"""
import math

PHI = (1 + math.sqrt(5)) / 2
KAPPA = 1/16
EPSILON = PHI**(-1) / 4
BETA = PHI**(-1) / 2
M_PL = 1.220890e19
LOOP = KAPPA**2 / (16 * math.pi**2)
LOOP_FACTOR = LOOP

# P_n energies in GeV
P0_GeV = (0.05 / 1e9) / (LOOP_FACTOR**6)
Pn_GeV = {n: P0_GeV * (LOOP_FACTOR**n) for n in range(7)}

# Known masses (GeV)
masses = {
    "m_e": 0.000511,
    "m_μ": 0.105658,
    "m_τ": 1.77686,
    "m_u": 0.0022,
    "m_d": 0.0047,
    "m_s": 0.093,
    "m_c": 1.27,
    "m_b": 4.18,
    "m_t": 172.76,
    "m_π0": 0.134977,
    "m_π±": 0.139570,
    "m_K0": 0.497614,
    "m_K±": 0.493677,
    "m_η": 0.547862,
    "m_η'": 0.95778,
    "m_p": 0.938272,
    "m_n": 0.939565,
    "Λ_QCD": 0.200,
    "M_Z": 91.1876,
    "M_W": 80.379,
    "M_H": 125.10,
    "M_GUT": 1.24e16,
}

# n=3: 3.3 TeV — compare
print("=" * 60)
print(f"n=3: {Pn_GeV[3]:.6e} GeV = {Pn_GeV[3]*1000:.4f} GeV")
print("=" * 60)
print(f"{'Expression':<25} {'Value (GeV)':<16} {'Ratio':<12} {'Note'}")
print("-" * 55)
for name, m in sorted(masses.items(), key=lambda x: abs(x[1]/Pn_GeV[3] - 1)):
    if m < 1000:  # Only show sub-TeV for context
        continue
    ratio_val = m / Pn_GeV[3]
    note = "✅" if 0.1 < ratio_val < 10 else ""
    print(f"{name:<25} {m:<16.6e} {ratio_val:<12.4f} {note}")
print()

# Also check some IDCM expressions at TeV scale
print(f"{'Epsilon expressions at n=3':^55}")
tests = [
    ("M_GUT × κ²", masses["M_GUT"] * KAPPA**2),
    ("M_GUT × ε", masses["M_GUT"] * EPSILON),
    ("M_Pl × κ³", M_PL * KAPPA**3),
    ("M_Pl × ε²", M_PL * EPSILON**2),
    ("M_Pl × κεβ", M_PL * KAPPA * EPSILON * BETA),
]
for name, val in tests:
    ratio = val / Pn_GeV[3]
    print(f"  {name:<20} {val:<16.6e}  /P₃={ratio:.4f}")

print()

# n=4: 81.7 MeV — compare with hadrons
print("=" * 60)
print(f"n=4: {Pn_GeV[4]:.6e} GeV = {Pn_GeV[4]*1000:.4f} MeV")
print("=" * 60)
print(f"{'Expression':<25} {'Value (MeV)':<16} {'Ratio':<12} {'Note'}")
print("-" * 55)

# Find closest known masses to n=4
for name, m in sorted(masses.items(), key=lambda x: abs(x[1] - Pn_GeV[4])):
    if m > 5:  # Only sub-5 GeV
        continue
    m_MeV = m * 1000
    P4_MeV = Pn_GeV[4] * 1000
    ratio_val = m_MeV / P4_MeV
    diff_pct = (m_MeV - P4_MeV) / P4_MeV * 100
    note = ""
    if abs(diff_pct) < 10:
        note = "🟡"
    if abs(diff_pct) < 3:
        note = "✅"
    print(f"{name:<25} {m_MeV:<16.4f} {ratio_val:<12.4f} {note} ({diff_pct:+.2f}%)")

print()

# IDCM expressions for n=4
print(f"{'IDCM expressions at n=4':^55}")
P4_MeV = Pn_GeV[4] * 1000
expressions = [
    ("m_π × φ⁻¹", masses["m_π0"]*1000 * PHI**(-1)),
    ("m_μ × φ", masses["m_μ"]*1000 * PHI),
    ("m_τ × εβ", masses["m_τ"]*1000 * EPSILON * BETA),
    ("m_τ × κ", masses["m_τ"]*1000 * KAPPA),
    ("m_p × φ⁻⁴", masses["m_p"]*1000 * PHI**(-4)),
    ("m_p × ε²", masses["m_p"]*1000 * EPSILON**2),
    ("m_n × φ⁻³", masses["m_n"]*1000 * PHI**(-3)),
    ("Λ_QCD × φ⁻¹", masses["Λ_QCD"]*1000 * PHI**(-1)),
    ("m_π × ε", masses["m_π0"]*1000 * EPSILON),
    ("m_K × φ⁻²", masses["m_K0"]*1000 * PHI**(-2)),
]

for name, val in expressions:
    diff_pct = (val - P4_MeV) / P4_MeV * 100
    print(f"  {name:<20} {val:<16.4f} MeV  diff={diff_pct:+.2f}%")

print()

# n=5: 2.02 keV
print("=" * 60)
print(f"n=5: {Pn_GeV[5]:.6e} GeV = {Pn_GeV[5]*1e6:.4f} eV")
print("=" * 60)

# Check: sterile neutrino? Axion?
P5_eV = Pn_GeV[5] * 1e9
P5_keV = P5_eV / 1000
print(f"  = {P5_keV:.4f} keV")
print(f"  Sterile neutrino DM at keV?  ✅ possible")
print(f"  Axion-like particle? ✅ possible")
print(f"  W-field coherence scale? 🟡 plausible")
print()

# Check if each level relates to known IDCM constants
print("=" * 60)
print("Global check: P_n vs IDCM constants")
print("=" * 60)
for n in range(1, 6):
    En = Pn_GeV[n]
    check = En / (EPSILON * BETA * M_PL * LOOP_FACTOR**n)
    check2 = En / (KAPPA**2 * M_PL * LOOP_FACTOR**n)
    print(f"  n={n}: E/(εβ·M_Pl·loopⁿ) = {check:.6f}")
    print(f"       E/(κ²·M_Pl·loopⁿ)  = {check2:.6f}")

print()
print("Done.")
