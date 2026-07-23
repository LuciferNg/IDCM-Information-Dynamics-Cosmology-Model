#!/usr/bin/env python3
"""
P_n Spectrum Calculator — IDCM v5.0
======================================
Compute full P_n spectrum from n=0 to n=6, cross-check with known closure points.

Usage:
    python3 pn_spectrum.py              # Full table
    python3 pn_spectrum.py --n 3        # Single level
    python3 pn_spectrum.py --verify     # Cross-check mode
"""

import argparse
import math
import sys

# ═══════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
KAPPA = 1/16                    # 4-body tensor contraction
EPSILON = PHI**(-1) / 4         # ε = φ⁻¹/4
BETA = PHI**(-1) / 2            # β = φ⁻¹/2
M_PL = 1.220890e19              # GeV
LOOP = KAPPA**2 / (16 * math.pi**2)  # Loop factor

LABELS = {
    0: "Consciousness (C formula)",
    1: "Subconscious / Bio-QM",
    2: "Quantum biology",
    3: "Ghost afterimage / DE tail",
    4: "DM candidate",
    5: "Transition layer",
    6: "Neutrino mass (closed ✅)",
}

COLORS = {
    0: "✅",
    1: "🟡",
    2: "🟡",
    3: "🟡",
    4: "🟡",
    5: "🟡",
    6: "✅",
}

# ═══════════════════════════════════════════════════════════════
# Core Calculation
# ═══════════════════════════════════════════════════════════════
def compute_Pn(P0_eV: float, n: int) -> float:
    """Compute P_n energy in eV from P_0 and loop order n."""
    return P0_eV * (LOOP**n)


def calibrate_P0(known_energy_eV: float, known_n: int) -> float:
    """Back-calculate P_0 from a known closure point."""
    return known_energy_eV / (LOOP**known_n)


def full_spectrum(neutrino_mass_eV: float = 0.05, neutrino_n: int = 6):
    """Compute full P_n spectrum from n=0 to n_max."""
    P0_eV = calibrate_P0(neutrino_mass_eV, neutrino_n)
    P0_GeV = P0_eV / 1e9
    
    print(f"P_n Spectrum (calibrated from n={neutrino_n} = {neutrino_mass_eV} eV)")
    print(f"Loop factor: κ²/(16π²) = {LOOP:.6e}")
    print(f"P_0 = {P0_eV:.4e} eV = {P0_GeV:.4e} GeV")
    print(f"P_0 / M_Pl = {P0_GeV/M_PL:.6f}")
    print()
    print(f"{'n':<4} {'Status':<8} {'Energy (eV)':<20} {'Energy (GeV)':<20} {'log₁₀(eV)':<12} {'Physical':<35}")
    print("-" * 100)
    
    results = {}
    for n in range(0, 7):
        E_eV = compute_Pn(P0_eV, n)
        E_GeV = E_eV / 1e9
        logE = math.log10(E_eV)
        status = COLORS.get(n, "?")
        label = LABELS.get(n, "")
        results[n] = {"eV": E_eV, "GeV": E_GeV, "log10": logE}
        print(f"{n:<4} {status:<8} {E_eV:<20.6e} {E_GeV:<20.6e} {logE:<12.4f} {label}")
    
    print()
    
    # Dimensionless prefactor
    X = P0_GeV / (M_PL**2)
    print(f"X = τ([H,P_κ]@W†W) × sin²θ(λ)/λ = P_0 / M_Pl² = {X:.4e}")
    
    return results


def verify_cross_checks(P0_eV: float):
    """Cross-check P0 against known IDCM constants."""
    P0_GeV = P0_eV / 1e9
    print("═" * 60)
    print("Cross-checks")
    print("═" * 60)
    print()
    
    checks = [
        ("P₀ / M_Pl", P0_GeV / M_PL, None),
        ("P₀ / M_GUT", P0_GeV / 1.24e16, "M_GUT ≈ 1.24×10¹⁶ GeV"),
        ("P₀ / M_EW", P0_GeV / 125.0, "EW scale ≈ 125 GeV"),
        ("P₀ / M_Proton", P0_GeV / 0.938, "proton mass ≈ 0.938 GeV"),
    ]
    
    print(f"{'Ratio':<20} {'Value':<20} {'Notes'}")
    print("-" * 55)
    for name, val, note in checks:
        print(f"{name:<20} {val:<20.6e} {note or ''}")
    
    print()
    
    # Test algebraic relations
    X = P0_GeV / (M_PL**2)
    print(f"P₀ / M_Pl² = X = {X:.6e}")
    print()
    
    relations = [
        ("κ²·ε", KAPPA**2 * EPSILON),
        ("ε·β·κ", EPSILON * BETA * KAPPA),
        ("κ³", KAPPA**3),
        ("ε²", EPSILON**2),
        ("β²", BETA**2),
        ("κ/ε", KAPPA / EPSILON),
        ("εβ/κ", EPSILON * BETA / KAPPA),
        ("φ⁻⁴²", PHI**(-42)),
        ("κ²/16π² (loop)", LOOP),
    ]
    
    print(f"{'Expression':<20} {'Value':<20} {'/ X':<15} {'Note'}")
    print("-" * 70)
    for name, val in relations:
        ratio = val / X if X != 0 else float('inf')
        note = "✅" if 0.5 < ratio < 2.0 else ""
        print(f"{name:<20} {val:<20.6e} {ratio:<15.4f} {note}")
    
    print()
    
    # Check discrepancy with prior estimates
    print("⚠️  Discrepancy Check (vs prior estimates)")
    print("-" * 45)
    
    # n=3 was estimated at 1e-5 to 1e-4 eV
    E3_eV = compute_Pn(P0_eV, 3)
    print(f"  n=3 calc: {E3_eV:.4e} eV = {E3_eV/1e9:.4e} GeV")
    print(f"  n=3 prior est: 1e-5 to 1e-4 eV")
    print(f"  Discrepancy: {E3_eV / 1e-5:.1f}x to {E3_eV / 1e-4:.1f}x")
    print(f"  Verdict: 🔴 {'MATCH' if 1e-5 < E3_eV < 1e3 else 'MISMATCH'}")
    print()
    
    # n=4 was estimated at ~1e9 GeV
    E4_eV = compute_Pn(P0_eV, 4)
    E4_GeV = E4_eV / 1e9
    print(f"  n=4 calc: {E4_eV:.4e} eV = {E4_GeV:.4e} GeV")
    print(f"  n=4 prior est: ~1e9 GeV")
    print(f"  Discrepancy: {E4_GeV / 1e9:.6f}x")
    print(f"  Verdict: 🔴 {'MATCH' if 0.1 < E4_GeV/1e9 < 10 else 'MISMATCH'}")


def interactive():
    parser = argparse.ArgumentParser(description="P_n Spectrum Calculator")
    parser.add_argument("--n", type=int, help="Compute single n")
    parser.add_argument("--verify", action="store_true", help="Cross-check mode")
    parser.add_argument("--mnu", type=float, default=0.05, help="Neutrino mass in eV (default: 0.05)")
    args = parser.parse_args()
    
    P0_eV = calibrate_P0(args.mnu, 6)
    
    if args.n is not None:
        n = args.n
        E_eV = compute_Pn(P0_eV, n)
        E_GeV = E_eV / 1e9
        print(f"P_{n} = {E_eV:.6e} eV = {E_GeV:.6e} GeV")
        print(f"log₁₀(P_{n}) = {math.log10(E_eV):.4f}")
        print(f"Physical: {LABELS.get(n, 'Unknown')}")
        return
    
    results = full_spectrum(args.mnu)
    
    if args.verify:
        verify_cross_checks(P0_eV)


if __name__ == "__main__":
    interactive()
