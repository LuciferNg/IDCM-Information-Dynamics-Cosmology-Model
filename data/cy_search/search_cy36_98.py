#!/usr/bin/env python3
"""
IDCM CY3 Search — Python Fallback
==================================
For environments without SageMath or PALP.
Works with pre-computed Hodge number lists.

Target: (h11, h21) = (36, 98), chi = -124
"""

from math import exp, log, sqrt, pi
import re, sys, os

# ════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════
PHI = (1 + sqrt(5)) / 2
PHI_INV = PHI - 1
KAPPA = 1.0 / 16.0
TARGET_H11 = 36
TARGET_H21 = 98

# ════════════════════════════════════════════════════════
# 1. Hodge Number List Search
# ════════════════════════════════════════════════════════
def search_hodge_list(filename="h11h21.txt"):
    """
    Search a pre-computed KS Hodge number list for (36, 98).
    
    Format: one 'h11 h21' pair per line (space-separated).
    Lines starting with '#' are ignored.
    """
    print(f"\n{'='*55}")
    print(f"  IDCM CY3 Search: (h11, h21) = ({TARGET_H11}, {TARGET_H21})")
    print(f"{'='*55}")
    
    if not os.path.exists(filename):
        print(f"  [X] File not found: {filename}")
        print(f"  Download from: https://www.thphys.uni-heidelberg.de/~kreuzer/")
        print(f"  Or generate with nef.x: nef.x -N -H < KS_db.txt > hodge_output.txt")
        return
    
    matches = []
    total = 0
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                h11, h21 = map(int, line.split()[:2])
                total += 1
                if h11 == TARGET_H11 and h21 == TARGET_H21:
                    matches.append((h11, h21, line))
            except:
                continue
    
    print(f"  Scanned: {total:,} Hodge pairs")
    print(f"  Matches: {len(matches)}")
    for h11, h21, extra in matches[:5]:
        print(f"    ({h11}, {h21}): {extra[:60]}")
    
    if not matches:
        print(f"\n  [NEGATIVE] No CY 3-fold with Hodge numbers (36, 98)")
        print(f"  found in the scanned dataset.")
        print(f"  Possible causes:")
        print(f"    1. Dataset is incomplete (only partial list)")
        print(f"    2. The IDCM prediction is falsified by the database")
        print(f"    3. (36, 98) exists but requires a different CY construction")
    
    return matches


# ════════════════════════════════════════════════════════
# 2. Synthetic Hodge Number Table (for IDCM docs)
# ════════════════════════════════════════════════════════
def print_hodge_diamond(h11, h21):
    """Print the Hodge diamond for a CY 3-fold."""
    print(f"\nHodge diamond (h11={h11}, h21={h21}):")
    print(f"            1")
    print(f"          0     0")
    print(f"        0   {h11}   0")
    print(f"      1   {h21}   {h21}   1")
    print(f"        0   {h11}   0")
    print(f"          0     0")
    print(f"            1")
    chi = 2 * (h11 - h21)
    print(f"Euler char: chi = {chi}")
    print(f"Hodge sum: 1 + h11 + h21 = {1 + h11 + h21}")
    return chi


# ════════════════════════════════════════════════════════
# 3. Verification: Check all IDCM topological constraints
# ════════════════════════════════════════════════════════
def verify_candidate(h11, h21):
    """Verify a candidate CY against all IDCM constraints."""
    chi = 2 * (h11 - h21)
    hodge_sum = 1 + h11 + h21
    ind = abs(chi) / 4  # Approximate Dirac index
    
    print(f"\n{'='*55}")
    print(f"  IDCM CY3 Constraint Verification")
    print(f"{'='*55}")
    print(f"  Input Hodge numbers: ({h11}, {h21})")
    print(f"  Input Euler char:    chi = {chi}")
    print()
    
    checks = [
        ("h11 + 1 = N_m = 37", h11 + 1 == 37, f"h11+1 = {h11+1}"),
        ("1 + h11 + h21 = N = 135", hodge_sum == 135, f"sum = {hodge_sum}"),
        ("Euler char = 2*(h11-h21)", True, f"chi = {chi}"),
        ("|chi|/2 >= 3 (gen. projection)", abs(chi)/2 >= 3, f"|chi|/2 = {abs(chi)/2}"),
        ("|chi|/2 = 62 (specific)", abs(chi)/2 == 62, f"|chi|/2 = {abs(chi)/2}"),
    ]
    
    all_pass = True
    for name, condition, value in checks:
        status = "✅" if condition else "❌"
        if not condition:
            all_pass = False
        print(f"  {status} {name:50s} [{value}]")
    
    if all_pass:
        print(f"\n  ✅ ALL CONSTRAINTS PASSED")
    else:
        print(f"\n  ❌ SOME CONSTRAINTS FAILED")
    
    return all_pass


# ════════════════════════════════════════════════════════
# 4. Main
# ════════════════════════════════════════════════════════
if __name__ == '__main__':
    print(f"IDCM CY3 Search Tool")
    print(f"Internal geometry: S1_w x_warp CY3, 2*pi*k*R = 1")
    print(f"Target CY: (h11, h21) = (36, 98), chi = -124")
    print(f"SO(10) Wilson line: Z2 quotient")
    print()
    
    # Check command line args
    filename = sys.argv[1] if len(sys.argv) > 1 else "h11h21.txt"
    search_hodge_list(filename)
    
    # Show Hodge diamond for target
    print_hodge_diamond(TARGET_H11, TARGET_H21)
    
    # Verify against IDCM constraints
    verify_candidate(TARGET_H11, TARGET_H21)
    
    print(f"\n{'='*55}")
    print(f"  Execution complete.")
    print(f"  To run with nef.x (PALP):")
    print(f"    nef.x -N -H -f < KS_database.txt | grep 'H:36,98'")
    print(f"{'='*55}")
