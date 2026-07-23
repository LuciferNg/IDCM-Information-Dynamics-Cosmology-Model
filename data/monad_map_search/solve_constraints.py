#!/usr/bin/env python3
"""
Solve monad B/C constraint system.
Find B/C assignment satisfying:
  1. c₁(V) = Σ_B - Σ_C = 0
  2. rk(V) = dim(B) - rank(f_at_J*) = 4
  3. rank(f_at_J*) = dim(B) - 4 (from condition 2)
"""
import json, numpy as np, itertools
from pathlib import Path

BASE = Path("/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data")

with open(BASE / "monad_definition.json") as f:
    md = json.load(f)
glsm = np.array(md["glsm_charge_matrix"], dtype=int)

# Identify coord vs noncoord rays
coord_rays = []
noncoord_rays = []
for i in range(37):
    row = glsm[i]
    nnz = np.count_nonzero(row)
    if nnz == 1 and row.sum() == 1 and row.max() == 1:
        coord_rays.append(i)
    else:
        noncoord_rays.append(i)

coord_rays = sorted(coord_rays)  # [1,2,5,6,9..36] 32 rays
noncoord_rays = sorted(noncoord_rays)  # [0,3,4,7,8] 5 rays
print(f"Coord rays: {len(coord_rays)}")
print(f"Non-coord rays: {len(noncoord_rays)} → {noncoord_rays}")

# ── Constraint 1: c₁(V) = 0 ──
# c₁(V) = Σ charge(B_p) - Σ charge(C_q) = 0 (32-dim vector)
# 
# C MUST include O(-e_k) for coord rays to get cancellation.
# Without O(-e_k), all c₁ entries would be positive.
# 
# Each O(-e_k) in C contributes charge -e_k (negative unit vector in position k)
# 
# Key insight: we can think of the 32 O(-e_k) summands as "background" in C.
# The remaining structure (noncoord rays in B and C) must cancel each other.

# The background is: C includes 32 copies of O(-e_k), k=1..32
# This contributes c₁_background = -Σ e_k = -[1,1,...,1]
# 
# To cancel: noncoord contributions to c₁ must sum to +[1,1,...,1]
# Each noncoord ray put in B contributes +glsm[ray]
# Each noncoord ray put in C contributes -glsm[ray]

print(f"\n{'='*70}")
print("CONSTRAINT 1: c₁ cancellation")
print(f"{'='*70}")

c1_target = -np.ones(32, dtype=int)  # -[1,1,...,1] = what O(-e_k) gives
print(f"  c₁ from 32×O(-e_k) background = -[1,1,...,1]")
print(f"  Noncoord B/C must contribute +[1,1,...,1]")

# Each noncoord ray contributes either +glsm[i] (in B) or -glsm[i] (in C)
# Total from noncoord: Σ sign_i · glsm[i] for sign_i ∈ {+1, -1}
# We need: Σ sign_i · glsm[i] = -c1_target = [1,1,...,1]

nc_charges = {i: glsm[i] for i in noncoord_rays}

print(f"\n  Noncoord ray charges (sum over 32 U(1)):")
for i in noncoord_rays:
    print(f"    Ray {i}: sum={int(glsm[i].sum())}  min={int(glsm[i].min())}  max={int(glsm[i].max())}")

# Search for B/C assignments of noncoord rays that satisfy c₁ = target
print(f"\n  Searching 2⁵ = 32 assignments...")
solutions = []
for mask in range(1 << len(noncoord_rays)):
    B_nc = []
    C_nc = []
    for j, ray in enumerate(noncoord_rays):
        if (mask >> j) & 1:
            B_nc.append(ray)
        else:
            C_nc.append(ray)
    
    # Contribution to c₁ from noncoord
    c1_nc = sum(glsm[i] for i in B_nc) - sum(glsm[i] for i in C_nc)
    
    # Total c₁ including background
    c1_total = c1_nc - np.ones(32, dtype=int)  # minus O(-e_k) background
    c1_total = np.array(c1_total)
    
    # Check if exact zero
    if np.all(c1_total == 0):
        solutions.append((mask, B_nc, C_nc))
        print(f"    ✅ EXACT: B={sorted(B_nc)}, C={sorted(C_nc)}")

if not solutions:
    print(f"    No exact solution. Searching for closest match...")
    best_err = 1e9
    best_sol = None
    for mask in range(1 << len(noncoord_rays)):
        B_nc = []
        C_nc = []
        for j, ray in enumerate(noncoord_rays):
            if (mask >> j) & 1:
                B_nc.append(ray)
            else:
                C_nc.append(ray)
        c1_nc = sum(glsm[i] for i in B_nc) - sum(glsm[i] for i in C_nc)
        c1_total = np.array(c1_nc - np.ones(32, dtype=int))
        err = int(np.sum(np.abs(c1_total)))
        if err < best_err:
            best_err = err
            best_sol = (B_nc, C_nc, c1_total, mask)
    
    B_nc, C_nc, c1, mask = best_sol
    print(f"    Best: B={sorted(B_nc)}, C={sorted(C_nc)}, err={best_err}")
    nz = np.where(c1 != 0)[0]
    print(f"    Non-zero c₁ entries: {len(nz)}/{32}")
    if len(nz) > 0:
        vals = c1[nz]
        print(f"    c₁ values: min={int(vals.min())}, max={int(vals.max())}")
        print(f"    c₁ at first 5 non-zero: {c1[nz[:5]].tolist()}")

# ── Constraint 2: rank structure at J* ──
print(f"\n{'='*70}")
print("CONSTRAINT 2: Rank structure at J*")
print(f"{'='*70}")

# For a valid monad 0 → V → B → C → 0:
# - f is surjective: rank = dim(C)
# - V = ker(f): dim(V) = dim(B) - dim(C) = 4
# 
# But due to linear dependencies between O(0) summands:
# effective_rank = achievable rank at J*

# Strategy: compute effective rank for any B/C assignment
# 
# At J* (Kähler interior): all coord rays x_k ≠ 0
# So: monomials are non-zero unless forced zero
#
# The O(0) → O(-e_k) entries are all x_k — identical for every O(0)
# So N_identical O(0) rows contribute rank 1, not N_identical

# For a given B/C combo, the rank at J* is:
# Block1: O(0) rows → O(-e_k) → rank = 1 (regardless of #O(0))
# Block2: O(ray) rows → O(-e_k) → each distinct ray gives rank 1 (different charges)
# Block3: O(0) rows → O(noncoord) → depends on charge
# Block4: O(ray) rows → O(noncoord) → depends on charge

def estimate_rank_at_Jstar(B_list, C_list):
    """Estimate rank of f at J* for given B and C selections."""
    # B entries can be O(0) or O(ray_i) for noncoord ray i
    # C entries can be O(-e_k) for coord k, or O(ray_i) for noncoord i
    
    rank_blocks = []
    
    # Identify B summands
    B_types = []
    B_charges = []
    for b in B_list:
        if b == "O(0)":
            B_types.append("zero")
            B_charges.append(np.zeros(32, dtype=int))
        else:
            ray = int(b.replace("R", ""))
            B_types.append("ray")
            B_charges.append(glsm[ray])
    
    # Identify C summands  
    C_types = []
    C_charges = []
    for c in C_list:
        if c.startswith("e_"):
            k = int(c.split("_")[1])
            C_types.append("ek")
            vec = np.zeros(32, dtype=int)
            vec[k-1] = -1
            C_charges.append(vec)
        elif c.startswith("R"):
            ray = int(c.replace("R", ""))
            C_types.append("ray")
            C_charges.append(glsm[ray])
    
    # The monad map f has dim(C) × dim(B) entries
    # Each entry f_{qp} has degree charge(C_q) - charge(B_p)
    # At J*: entry is non-zero iff it's a valid global section (deg >= 0) and not SR-forced-zero
    
    # For rank estimation, we check linear independence of columns (maps B_p → C)
    # At J*, the rank is determined by the pattern of which entries vanish
    
    # The columns of f correspond to B_p, rows to C_q
    # f is: C × B matrix with f(q,p) = monomial of degree C_q - B_p
    
    # For O(0) → O(-e_k): degree = e_k, monomial = x_k
    # For O(0) → noncoord: degree = -charge(noncoord)
    # For O(ray) → O(-e_k): degree = e_k + charge(ray)  
    # For O(ray) → noncoord: degree = charge(noncoord) - charge(ray)
    
    # Actually let me think about the rank differently.
    # The key question is: does the monad map have full rank at J*?
    # For surjectivity, we need: rank(f) = dim(C)
    # For V = ker(f), dim(V) = dim(B) - dim(C) needs to be 4
    
    # The O(0) summands create identical columns — this is the degeneracy
    # Count distinct column patterns instead
    
    nB = len(B_list)
    nC = len(C_list)
    
    # Build column vectors (each column is the map from B_p to all C_q)
    # Two columns are linearly dependent if they're proportional at J*
    # For monomial entries, columns are proportional iff all entries are equal
    
    # For O(0) → O(-e_k): entry = x_k (same for ALL O(0) columns)
    # So ALL O(0) columns are IDENTICAL → rank contribution = 1
    
    # Count distinct columns
    col_signatures = []
    for p in range(nB):
        sig = []
        for q in range(nC):
            deg = C_charges[q] - B_charges[p]
            # Simple: entry = 0 if any deg < 0, non-zero if all deg >= 0
            valid = int(np.all(deg >= 0))
            sig.append(valid)
        col_signatures.append(tuple(sig))
    
    # Count unique column signatures
    unique_sigs = list(set(col_signatures))
    est_rank = len(unique_sigs)
    
    return est_rank, col_signatures

# Test various assignments
# The background C = 32×O(-e_k) is always present
# Plus some noncoord-dependent summands

print(f"\n  Searching assignments with rk(V) = 4...")
print(f"  Conditions: c₁=0 (or minimal), dim(B)-rank(f) = 4")

results = []
for mask in range(1 << len(noncoord_rays)):
    B_nc = []
    C_nc = []
    for j, ray in enumerate(noncoord_rays):
        if (mask >> j) & 1:
            B_nc.append(ray)
        else:
            C_nc.append(ray)
    
    # Build B and C
    B_list = ["O(0)"] * 4 + [f"R{b}" for b in B_nc]
    C_list = [f"R{c}" for c in C_nc] + [f"e_{k}" for k in range(1, 33)]
    
    nB = len(B_list)
    nC = len(C_list)
    
    # c₁ check
    B_ch = np.zeros(32, dtype=int)
    for b in B_list:
        if b != "O(0)":
            ray = int(b.replace("R", ""))
            B_ch += glsm[ray]
    
    C_ch = np.zeros(32, dtype=int)
    for c in C_nc:
        C_ch += glsm[c]
    for k in range(1, 33):
        C_ch[k-1] -= 1  # O(-e_k) contribution
    
    c1 = B_ch - C_ch
    c1_err = int(np.sum(np.abs(c1)))
    
    # Rank estimation
    est_rank, sigs = estimate_rank_at_Jstar(B_list, C_list)
    
    rkV = nB - est_rank
    
    results.append((c1_err, abs(rkV - 4), mask, sorted(B_nc), sorted(C_nc), nB, nC, est_rank, rkV, c1))

# Show best solutions sorted by c1_err then |rkV-4|
results.sort(key=lambda x: (x[0], x[1]))
print(f"\n  Top 5 solutions (sorted by c₁_err, then |rk(V)-4|):")
print(f"  {'B':<20} {'C':<20} {'c₁_err':<10} {'est_rank':<10} {'rk(V)':<8}")
print(f"  {'-'*68}")
for c1_err, rk_diff, mask, B_nc, C_nc, nB, nC, est_rank, rkV, c1 in results[:5]:
    B_str = "O(0)⁴" + ("+" + "+".join(f"R{i}" for i in B_nc) if B_nc else "")
    C_str = ("+".join(f"R{i}" for i in C_nc) + "+" if C_nc else "") + "32×O(-e_k)"
    if len(B_str) > 19: B_str = B_str[:18] + "…"
    if len(C_str) > 19: C_str = C_str[:18] + "…"
    print(f"  {B_str:<20} {C_str:<20} {c1_err:<10} {est_rank:<10} {rkV:<8}")

# Detailed analysis of best solution
if results:
    best = results[0]
    print(f"\n{'='*70}")
    print(f"BEST SOLUTION")
    print(f"{'='*70}")
    print(f"  B = O(0)⁴ + R{best[3]}")
    print(f"  C = R{best[4]} + 32×O(-e_k)")
    print(f"  nB = {best[5]}, nC = {best[6]}")
    print(f"  c₁_err = {best[0]}")
    print(f"  est_rank(f) = {best[7]}")
    print(f"  rk(V) = {best[8]}")
    print(f"  Required: rk(V) = 4")
    
    c1_vec = best[9]
    nz = np.where(np.abs(c1_vec) > 0)[0]
    if len(nz) > 0:
        print(f"\n  ⚠️ c₁ has {len(nz)} non-zero entries")
        print(f"  Need to adjust: add O(-e_k) at specific U(1) positions to cancel")
        print(f"  Non-zero indices: {nz[:10].tolist()}")
        print(f"  Values: {c1_vec[nz[:10]].tolist()}")
    
    print(f"\n{'='*70}")
    print(f"VERDICT")
    print(f"{'='*70}")
    
    if best[0] == 0 and best[8] == 4:
        print(f"  ✅ Exact solution found!")
    elif best[0] == 0:
        print(f"  🟡 c₁=0 satisfied but rk(V)={best[8]} (need 4)")
        print(f"  → Add more O(ray) to B to increase nB")
    elif best[8] == 4:
        print(f"  🟡 rk(V)=4 satisfied but c₁_err={best[0]}")
        print(f"  → Need additional O(-e_k) or O(e_k) to cancel c₁")
    else:
        print(f"  🔴 Neither constraint satisfied")
        print(f"  → This monad construction needs a different B/C composition")
        print(f"  → Try with different numbers of O(0) in B")
