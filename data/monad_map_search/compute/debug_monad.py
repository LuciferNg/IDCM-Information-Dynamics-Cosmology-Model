#!/usr/bin/env python3
"""Debug monad: pure numpy, no SageMath."""
import json, numpy as np
from pathlib import Path

BASE = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")
with open(BASE / "monad_definition.json") as f:
    md = json.load(f)

glsm_raw = np.array(md["glsm_charge_matrix"], dtype=int)
glsm = glsm_raw  # (37, 32): already rows = rays

coord_rays = [i for i in range(37) if np.count_nonzero(glsm[i])==1 and glsm[i].sum()==1]
noncoord_rays = [i for i in range(37) if i not in coord_rays]

print(f"Coord: {len(coord_rays)}, Noncoord: {len(noncoord_rays)} -> {noncoord_rays}")

# Check each mixed-ray assignment for c₁=0 with coord ray placement
print("\n--- Analysis: c₁(V) with coord rays in B/C ---")
# Each coord ray has charge e_a (0,...,1,...,0)
# If coord ray a goes to B, contribution to c₁[a] = +1
# If coord ray a goes to C, contribution to c₁[a] = -1  
# Total coord contribution to c₁ = 2*(n_B) - 1 for each component a where n_B=1 if ray in B

for mixed_mask in range(4):
    B_nc = [3, 7]
    C_nc = [0]
    if mixed_mask & 1: B_nc.append(4)
    else: C_nc.append(4)
    if mixed_mask & 2: B_nc.append(8)
    else: C_nc.append(8)
    
    # noncoord contribution to c₁
    c1_nc = sum(glsm[i] for i in B_nc) - sum(glsm[i] for i in C_nc)
    
    # For each U(1) a, we need: coord_contrib[a] + c1_nc[a] = 0
    # coord_contrib[a] = 2*n_a - 1 where n_a ∈ {0,1}
    # So: n_a = (1 - c1_nc[a]) / 2, must be 0 or 1
    
    needed = {}
    ok = True
    for a in range(32):
        n = (1 - c1_nc[a]) / 2.0
        r = int(round(n))
        if abs(n - r) > 0.01 or r not in (0, 1):
            ok = False
            needed[a] = f"IMPOSSIBLE: n={n:.3f}"
        else:
            needed[a] = r
    
    print(f"\n  mask={mixed_mask}: B_nc={B_nc}, C_nc={C_nc}")
    print(f"  c1_nc range: [{c1_nc.min()}, {c1_nc.max()}]")
    print(f"  Possible? {ok}")
    
    if not ok:
        bad = [(a, needed[a]) for a in range(32) if "IMPOSSIBLE" in str(needed[a])]
        print(f"  Problematic U(1) components (first 5):")
        for a, msg in bad[:5]:
            print(f"    a={a}: {msg}, c1_nc[a]={c1_nc[a]}, contrib from:")
            for i in B_nc:
                if glsm[i][a] != 0:
                    print(f"      B ray {i}: q={glsm[i][a]}")
            for i in C_nc:
                if glsm[i][a] != 0:
                    print(f"      C ray {i}: -q={-glsm[i][a]}")

# The implication: c₁(V)=0 with ONLY the 5 noncoord rays is IMPOSSIBLE
# because the coord rays can only contribute ±1 per component, which
# cannot cancel the large noncoord charges (up to ±64).

# This means: the monad MUST involve the coordinate rays as summands,
# or O(0) summands with MULTIPLICITY > 1.
# Or: the monad doesn't require c₁(V)=0 in the standard sense.

print("\n\n--- Alternative: O(m) summands (not just O(0)) ---")
# What if we use O(m) summands in B or C, with m being multiples of coord rays?
# Each O(k·e_a) has charge k under U(1)_a.
# This gives MORE flexibility: we can tune the charge contribution.

# Actually, the correct interpretation might be:
# The monad is NOT 0→V→B→C→0 but a longer complex.
# Or: The coordinate rays are AMBIENT SPACE coordinates, not monad summands.
# The monad only involves the 5 noncoord rays, and the coord rays
# only appear in the monad map as polynomial variables.

print("Key insight: if coord rays are ambient variables (not monad summands):")
print("  B = O(0)ⁿ ⊕ O(noncoord_pos)")
print("  C = O(noncoord_neg)")
print("  c₁(V) = Σ_B q_i - Σ_C q_i may NOT need to be zero!")
print()
print("In a heterotic compactification:")
print("  c₁(V) ≠ 0 is allowed if there are 5-branes or")
print("  if c₁(V) = c₁(TX) [standard embedding]")
print("  For CY₃, c₁(TX) = 0, so we need c₁(V)=0 for standard embedding")
print("  But non-standard embeddings with 5-branes allow c₁(V) ≠ 0")
print()

# So let's check: what if we DON'T require c₁=0?
print("Checking without c₁=0 constraint:")
for mixed_mask in range(4):
    B_nc = [3, 7]
    C_nc = [0]
    if mixed_mask & 1: B_nc.append(4)
    else: C_nc.append(4)
    if mixed_mask & 2: B_nc.append(8)
    else: C_nc.append(8)
    
    B_rk = len(B_nc)
    C_rk = len(C_nc)
    delta = 4 - (B_rk - C_rk)
    
    c1 = sum(glsm[i] for i in B_nc) - sum(glsm[i] for i in C_nc)
    
    if delta >= 0:
        print(f"\n  mask={mixed_mask}: B={B_nc}, C={C_nc}")
        print(f"    B_rk={B_rk}, C_rk={C_rk}, need O(0)^{delta} in B")
        print(f"    rk(V) = ({B_rk}+{delta})-{C_rk} = {4}")
        print(f"    c₁ nonzeros: {np.count_nonzero(c1)}/{32}")
        print(f"    c₁ range: [{c1.min()}, {c1.max()}]")
        print(f"    Status: {'✅ rank ok' if delta>=0 else '❌ rank fail'}")
