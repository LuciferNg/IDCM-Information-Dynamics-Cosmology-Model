#!/usr/bin/env python3
"""
Instanton Geometric Weight — Fast version using cached data.
"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()
import numpy as np, json, math, sys
from pathlib import Path

DATA = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
PHI = (1+5**0.5)/2; TWOPI = 2*math.pi

print("="*72)
print("  INSTANTON GEOMETRIC WEIGHT — H·L·N COUPLING")
print("  Target: δ_inst = Σ n_β·β_H·β_L·β_N·q/(1-q) ≈ 6.74")
print("="*72)

with open(DATA/"Jstar_36D.json") as f: jd = json.load(f)
Jstar = np.array(jd["Jstar_36D"])

# Load previously cached GLSM + kappa data
with open(DATA/"cy36_98_final.json") as f: fn = json.load(f)
with open(DATA/"kappa_36d_raw.json") as f: kr = json.load(f)
K = kr["kappa"]
glsm3 = np.array(fn["glsm_coord3"], dtype=int)  # 1D: charge per divisor
n_glsm = len(glsm3)
charges = np.zeros(36, dtype=int); charges[:n_glsm] = glsm3

# Get full GLSM charge matrix from CYTools
poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
cy = poly.triangulate().get_cy()
glsm_mat = np.array(cy.glsm_charge_matrix())  # (n_charges, n_coords)
print(f"  GLSM matrix shape: {glsm_mat.shape}")

# ════════════════════════════════════════════════════════════
# 1. GLSM coordinate analysis (fast, no cone computation)
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  1. GLSM COORDINATE SCAN — β·J AND GEOMETRIC WEIGHT")
print(f"{'='*72}")

# The GLSM charge matrix gives the Mori cone generators' intersection
# In toric geometry, each coordinate c corresponds to a curve class β_c
# whose intersection with divisor a is Q_{a,c} (the GLSM charge)
# The Kähler volume of the curve is: β_c·J = Σ_a |Q_{a,c}| · J*_a
# This is the standard toric formula

print(f"\n  {'Coord':>5} {'Div':>4} {'Charge':>6} {'β·J':>10} {'β_H':>5} {'β_L':>5} {'β_N':>5} {'Geom':>8} {'q':>12} {'q/(1-q)':>10} {'Weighted':>10}")
print(f"  {'─'*5} {'─'*4} {'─'*6} {'─'*10} {'─'*5} {'─'*5} {'─'*5} {'─'*8} {'─'*12} {'─'*10} {'─'*10}")

# For each GLSM coordinate, compute β·J using the correct toric formula
# The coordinate index maps to a divisor. The GLSM gives charge per U(1).
# β·J = Σ_a |Q_ac| · t_a where t is the Kähler parameter

all_coords = []
for coord in range(glsm_mat.shape[1]):
    # β·J = Σ_a |Q_ac| · J*_a  (sum over all U(1) charges × Kähler moduli)
    bj = 0.0
    for a in range(min(glsm_mat.shape[0], len(Jstar))):
        bj += abs(glsm_mat[a, coord]) * Jstar[a]
    
    if bj < 1e-10: continue
    
    # Charges for H·L·N: H=D₂(index 2 in divisor basis), L=N=D₇(index 7)
    # The GLSM coordinates map to divisors. For the first 32 coordinates,
    # coordinate c = divisor c. Our J* is 36D, first 32 are divisor basis.
    # The charge of a divisor is glsm3[div_idx]
    
    # For the H·L·N coupling, the relevant GLSM charges are those
    # of divisors D₂ (H), D₇ (L/N)
    # The instanton weight uses the multiplicities:
    # β_H = number of times the curve intersects D₂ = Σ_a Q_a2 · ... 
    # Actually in the GLSM, the charge of coordinate c under U(1)_a is Q_ac
    # The intersection of curve β_c with divisor D_a is Q_ac
    
    # For the three fields:
    # H field → divisor D₂ → GLSM coordinate 2
    # L field → divisor D₇ → GLSM coordinate 7
    # N field → divisor D₇ → GLSM coordinate 7
    qH = abs(glsm_mat[2, coord]) if glsm_mat.shape[0] > 2 else 0
    qL = abs(glsm_mat[7, coord]) if glsm_mat.shape[0] > 7 else 0
    qN = qL  # ν_R on same divisor as L
    
    geom = qH * qL * qN
    q = math.exp(-TWOPI * bj)
    q1q = q / (1 - q) if q < 0.9999 else 999.9
    w = geom * q1q
    
    div_idx = coord if coord < len(charges) else -1
    ch = charges[div_idx] if div_idx >= 0 else -1
    all_coords.append((coord, bj, qH, qL, geom, q, q1q, w, ch))

# Sort by weighted contribution descending
all_coords.sort(key=lambda x: -x[7])

for coord, bj, qH, qL, geom, q_, q1q, w, ch in all_coords:
    print(f"  {coord:>5} {coord:>4} {ch:>6} {bj:>10.4f} {qH:>5} {qL:>5} {qL:>5} {geom:>8} {q_:>12.6e} {q1q:>10.4f} {w:>10.4f}")

total_w = sum(c[7] for c in all_coords)
print(f"\n  Total geometric weighted sum (n_β=1): {total_w:.4f}")
print(f"  Target δ_inst = 6.74")
print(f"  Required avg GV invariant = {6.74/total_w:.2f}" if total_w > 0 else "")

# ════════════════════════════════════════════════════════════
# 2. Top candidates with GV estimates
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  2. CLOSURE WITH ESTIMATED GV INVARIANTS")
print(f"{'='*72}")

print(f"\n  Taking top contributors with n_β ~ degree²:")
closure = 0.0
for i in range(min(10, len(all_coords))):
    coord, bj, qH, qL, geom, q_, q1q, w, ch = all_coords[i]
    degree = qH + 2*qL  # total degree
    n_beta = max(1, degree)  # conservative lower bound
    contrib = n_beta * w
    closure += contrib
    
    # If this curve class dominates the sum, n_β_alone:
    n_alone = 6.74 / w if w > 0 else float('inf')
    
    print(f"  Coord {coord}: deg={degree}, geom={geom}, w={w:.2f}, n_β={n_beta}, contrib={contrib:.2f}, n_if_alone={n_alone:.0f}")

print(f"\n  δ_inst(estimated) = {closure:.4f}")
print(f"  ℐ_inst = 1 + {closure:.2f} = {1+closure:.2f}")
print(f"  Target ℐ_inst = 7.7")
print(f"  Match: {(1+closure)/7.7*100:.1f}%")

# ════════════════════════════════════════════════════════════
# 3. Find the single curve that can close the gap
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  3. SINGLE-CURVE CLOSURE ANALYSIS")
print(f"{'='*72}")

print(f"\n  Can a single curve class provide δ_inst ≈ 6.74?")
for i in range(min(5, len(all_coords))):
    coord, bj, qH, qL, geom, q_, q1q, w, ch = all_coords[i]
    if w > 0:
        n_needed = 6.74 / w
        category = "✅ trivial" if n_needed < 10 else ("✅ reasonable" if n_needed < 100 else "🟡 high" if n_needed < 1000 else "🔴 extreme")
        print(f"  Coord {coord}: n_β = {n_needed:.0f} → {category}")
        print(f"    (qH={qH}, qL={qL}, β·J={bj:.4f}, q={q_:.4e})")

# ════════════════════════════════════════════════════════════
# 4. Summary for document
# ════════════════════════════════════════════════════════════
print(f"\n{'='*72}")
print("  4. SUMMARY FOR NEUTRINO_INSTANTON_CORRECTION")
print(f"{'='*72}")

# The coordinate with the best combination of small β·J + large geometric weight
# is the one that maximizes w = geom × q/(1-q)
best = all_coords[0]
coord, bj, qH, qL, geom, q_, q1q, w, ch = best

print(f"\n  Primary instanton candidate: coordinate {coord}")
print(f"  Divisor index: {coord}, charge: {ch}")
print(f"  β·J = {bj:.4f}")
print(f"  β_H × β_L × β_N = {qH} × {qL} × {qL} = {geom}")
print(f"  q/(1-q) = {q1q:.4f}")
print(f"  Weighted contribution (n_β=1): {w:.4f}")
print(f"  GV invariant needed: n_β ≈ {6.74/w:.0f}")
print(f"  → This n_β is ", end="")
if 6.74/w < 10: print("trivially achievable ✅")
elif 6.74/w < 100: print("well within CY₃ range ✅")
elif 6.74/w < 1000: print("plausible for CY₃ 🟡")
else: print("extreme but possible 🔴")

# Multiple curves
print(f"\n  Multiple-curve scenario (top 5 with n_β=degree):")
mult = sum(max(1, c[3]+2*c[4]) * c[7] for c in all_coords[:5])
print(f"  δ_inst = {mult:.2f}")
print(f"  ℐ_inst = {1+mult:.2f}")
print(f"  vs target 7.7: ratio = {(1+mult)/7.7:.3f}")

print(f"\n{'='*72}")
sys.stdout.flush()
