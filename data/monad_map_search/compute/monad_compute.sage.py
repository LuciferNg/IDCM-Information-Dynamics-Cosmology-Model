#!/usr/bin/env python3
"""
Monad Map — Direct Computation on CY₃(36,98)
Step 1: Extract GLSM data and build ambient toric variety
Step 2: Search valid B/C decomposition
Step 3: Compute monad map entry dimensions  
Step 4: Determine if monad map with correct rank exists
"""
import os, sys, json, math, time
import numpy as np

os.environ["SAGE_ROOT"] = "/home/wsl/miniconda/envs/sage37"
sys.path.insert(0, "/home/wsl/miniconda/envs/sage37/lib/python3.7/site-packages")

import sage.all as sage
from sage.geometry.fan import Fan, Cone
from sage.schemes.toric.variety import ToricVariety
from sage.schemes.toric.divisor import ToricDivisor

from cytools import fetch_polytopes, config
config.enable_experimental_features()

BASE = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search"

print("=" * 75)
print("  MONAD MAP — DIRECT COMPUTATION v2")
print("=" * 75)

poly = list(fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
tri = poly.triangulate(backend="qhull")
cy = tri.get_cy()
print(f"\n  CY₃: h¹¹={cy.h11()}, h²¹={cy.h21()}, χ={cy.chi()}")

# GLSM: shape (32, 37) = 32 charges × 37 rays → transpose to (37, 32)
glsm_raw = np.array(cy.glsm_charge_matrix(), dtype=int)
print(f"  GLSM raw shape: {glsm_raw.shape}")
glsm = glsm_raw.T  # Now (37, 32): 37 rays × 32 charges
print(f"  GLSM transposed: {glsm.shape}")

# ─── BUILD FAN ───
print("\n--- Building ambient toric variety ---")
all_pts = list(poly.points())
rays_cytools = [list(pt) for pt in all_pts[1:38]]
print(f"  Rays: {len(rays_cytools)}")

sage_rays = [sage.vector(sage.ZZ, [int(x) for x in r[:4]]) for r in rays_cytools]

tri_simplices = tri.simplices()
print(f"  Triangulation simplices: {len(tri_simplices)}")

valid_cones = []
for s in tri_simplices:
    ray_indices = [i - 1 for i in s if i > 0]
    if len(ray_indices) >= 4:
        try:
            c = Cone([sage_rays[i] for i in ray_indices])
            if c.is_strictly_convex():
                valid_cones.append(c)
        except:
            pass

print(f"  Valid cones: {len(valid_cones)}")
fan = Fan(valid_cones)
print(f"  Fan dim: {fan.dim()}")

X = ToricVariety(fan)
print(f"  Toric variety dim: {X.dimension()}")
print(f"  Fan rays: {len(fan.rays())}")

# ─── CLASSIFY RAYS ───
print("\n--- Ray classification ---")
# Count which rays are non-negative / non-positive / mixed
nonneg_rays = [i for i in range(37) if np.all(glsm[i] >= 0)]
nonpos_rays = [i for i in range(37) if np.all(glsm[i] <= 0)]
zero_rays = [i for i in range(37) if np.all(glsm[i] == 0)]
mixed_rays = [i for i in range(37) if i not in nonneg_rays and i not in nonpos_rays]

coord_rays = [i for i in range(37) if np.count_nonzero(glsm[i])==1 and glsm[i].sum()==1]
noncoord_rays = [i for i in range(37) if i not in coord_rays]

print(f"  Coord rays: {len(coord_rays)}")
print(f"  Non-coord: {len(noncoord_rays)} -> {sorted(noncoord_rays)}")
print(f"  Non-neg: {len(nonneg_rays)}, Non-pos: {len(nonpos_rays)}, Mixed: {len(mixed_rays)}")

# ─── GET TORIC DIVISORS (needed for n_divs) ───
toric_divs = X.toric_divisor_group().gens()
n_divs = len(toric_divs)
print(f"  Toric divisor group rank: {n_divs}")

# Map U(1)_a → toric divisor index
u1_to_div = {}
for i in coord_rays:
    a = np.where(glsm[i] == 1)[0][0]
    u1_to_div[a] = i

print(f"  U(1)→Divisor mapping: {len(u1_to_div)}/{n_divs} mapped")

# ─── SEARCH B/C ───
print("\n" + "=" * 75)
print("  SEARCH: B/C with c₁(V)=0, rk(V)=4")
print("=" * 75)

total_charge = glsm.sum(axis=0)
print(f"\n  Total charge = 0? {np.all(total_charge==0)}")

valid_decomps = []
n_mixed = len(mixed_rays)

# Try ALL possible subsets of NON-NEGATIVE rays (including coord rays) going to C
# B gets the remaining non-negative rays, C gets non-positive + some non-negative
nonneg_list = sorted(nonneg_rays)  # 34 rays: 32 coord + rays 3, 7
n_nonneg = len(nonneg_list)

print(f"\n  Searching over {2**n_nonneg} nonneg-ray assignments...")

# To reduce search space, note that coord rays are equivalent under symmetry
# Try putting k coord rays in C for k = 0..min(32, required_for_c1)
# This is still 2^34 which is huge. Let's use a smarter approach.

# For c₁(V)=0: Σ_B q_i = Σ_C q_i  
# Since Σ_all q_i = 0: Σ_B q_i - Σ_C q_i = 0
# Rewrite: (Σ_nonneg_that_go_to_B + Σ_mixed_that_go_to_B) - 
#          (Σ_nonpos + Σ_nonneg_that_go_to_C + Σ_mixed_that_go_to_C) = 0
# Since Σ_all = 0: Σ_nonneg + Σ_nonpos + Σ_mixed = 0
# So: Σ_nonneg_that_go_to_B - Σ_nonneg_that_go_to_C + 
#     Σ_mixed_that_go_to_B - Σ_mixed_that_go_to_C + 
#     Σ_nonpos_B - Σ_nonpos_C = 0
# Where nonpos_B = 0 (no nonpos in B)
# And Σ_nonpos_C is just ray 0's charge (all negative)

# Let x_B subset of nonneg go to B, x_C subset go to C (complement)
# Then Σ_B = Σ_{i∈x_B} q_i + Σ_{mixed_B} q_i
# Σ_C = Σ_{i∈x_C} q_i + q_0 + Σ_{mixed_C} q_i

# For c₁=0: Σ_{i∈x_B} q_i + Σ_{mixed_B} q_i - Σ_{i∈x_C} q_i - q_0 - Σ_{mixed_C} q_i = 0
# => Σ_B = Σ_C

# Quick check: what charge distribution do we need for coord rays?
# Each coord ray i has charge e_a = (0,...,1_a,...,0)
# Σ_x_B e_a - Σ_x_C e_a = Σ_x_B e_a - (Σ_all e_a - Σ_x_B e_a) = 2·Σ_x_B e_a - Σ_all e_a
# where Σ_all e_a = (1,1,1,...,1) for all 32 coord rays

# So for each U(1) direction a:
# c₁[a] = (coord_contrib) + (noncoord_contrib)
# coord_contrib[a] = |x_B ∩ coord_rays_for_a| - (1 - |x_B ∩ coord_rays_for_a|) 
# Wait, each coord ray has exactly one +1 and rest 0.
# So there are 32 coord rays, each with charge e_a for a different component.
# The sum of all coord rays in B = (n₁, n₂, ..., n₃₂) where n_a = 1 if coord_ray_for_U(1)_a ∈ B, 0 if ∈ C

# So: Σ_B e_a = n_a (B gets n_a of the a-th coord ray's charge)
# Σ_C e_a = 1 - n_a (C gets the rest)
# coord contribution to c₁[a] = n_a - (1 - n_a) = 2·n_a - 1

# For this to cancel the noncoord contribution:
# 2·n_a - 1 + noncoord_B[a] - noncoord_C[a] - q_0[a] = 0
# 2·n_a = 1 - noncoord_B[a] + noncoord_C[a] + q_0[a]

# Since n_a ∈ {0,1}, the RHS must be 0 or 2

# Let's compute what value of n_a we need for each U(1) component
print(f"\n  Analyzing required n_a per U(1) component...")

# Noncoord contribution to c₁
# B has noncoord rays 3, 7 (all-nonneg) + possibly mixed 4, 8
# C has noncoord ray 0 (all-nonpos) + possibly mixed 4, 8

# Default: B = all nonneg noncoord (3,7), C = all nonpos noncoord (0)
# Mixed rays (4,8) can go either way

for mixed_to_B_mask in range(4):  # 2 mixed rays → 4 assignments
    B_noncoord = [3, 7]  # always in B
    C_noncoord = [0]     # always in C
    
    if mixed_to_B_mask & 1:
        B_noncoord.append(4)
    else:
        C_noncoord.append(4)
    if mixed_to_B_mask & 2:
        B_noncoord.append(8)
    else:
        C_noncoord.append(8)
    
    # Compute what Σ_B - Σ_C needs to be (from noncoord contributions)
    noncoord_c1 = (sum(glsm[i] for i in B_noncoord) - sum(glsm[i] for i in C_noncoord))
    
    print(f"\n  Mask {mixed_to_B_mask}: B_noncoord={B_noncoord}, C_noncoord={C_noncoord}")
    
    # For each U(1) a, we need 2·n_a - 1 + noncoord_c1[a] = 0
    # => n_a = (1 - noncoord_c1[a]) / 2
    # n_a must be 0 or 1
    
    forbidden = False
    B_coord_rays = []
    C_coord_rays = []
    
    for a in range(min(32, n_divs)):
        needed = (1 - noncoord_c1[a]) / 2
        if abs(needed - round(needed)) > 0.01:
            forbidden = True
            break
        n_a = int(round(needed))
        if n_a not in (0, 1):
            forbidden = True
            break
    
    if not forbidden:
        # Determine specific coord rays
        for a in range(32):
            needed = (1 - noncoord_c1[a]) / 2
            n_a = int(round(needed))
            # Find the coord ray for this U(1)
            for i in coord_rays:
                if np.count_nonzero(glsm[i]) == 1:
                    pos = np.where(glsm[i] == 1)[0][0]
                    if pos == a:
                        if n_a == 1:
                            B_coord_rays.append(i)
                        else:
                            C_coord_rays.append(i)
                        break
        
        total_B = len(B_noncoord) + len(B_coord_rays)
        total_C = len(C_noncoord) + len(C_coord_rays)
        base_rk = total_B - total_C
        delta = 4 - base_rk
        
        if delta >= 0:
            valid_decomps.append({
                "B_coord": B_coord_rays, "C_coord": C_coord_rays,
                "B_noncoord": B_noncoord, "C_noncoord": C_noncoord,
                "nB": total_B, "nC": total_C,
                "O0_B": delta,
                "total_rk": (total_B + delta) - total_C
            })

print(f"\n  Found {len(valid_decomps)} valid decompositions:")
for i, d in enumerate(valid_decomps):
    print(f"\n  [{i+1}] (mixed_mask={d.get('mixed_mask','?')})")
    print(f"    B: noncoord={d['B_noncoord']}, {len(d['B_coord'])} coord rays")
    print(f"    C: noncoord={d['C_noncoord']}, {len(d['C_coord'])} coord rays")
    print(f"    B total: {len(d['B_noncoord'])+len(d['B_coord'])}, + O(0)^{d['O0_B']}")
    print(f"    C total: {len(d['C_noncoord'])+len(d['C_coord'])}")
    print(f"    rk(V) = {d['nB']}+{d['O0_B']}-{d['nC']} = {d['total_rk']}")

# ─── SHEAF COHOMOLOGY ───
print("\n" + "=" * 75)
print("  COMPUTE: Sheaf cohomology of monad map entries")
print("=" * 75)

if valid_decomps:
    d = valid_decomps[0]
    B_rays_all = d['B_noncoord'] + d['B_coord']
    C_rays_all = d['C_noncoord'] + d['C_coord']
    O0_B = d['O0_B']
    
    print(f"\n  Using decomposition [1]:")
    print(f"    B has {len(B_rays_all)} charge rays + {O0_B} O(0)")
    print(f"    C has {len(C_rays_all)} charge rays")
    print(f"    B coord in: {len(d['B_coord'])}, C coord in: {len(d['C_coord'])}")
    print(f"  \n  Computing H⁰(X, O(charge_B - charge_C)) for each entry...")
    
    # Get toric divisors
    toric_divs = X.toric_divisor_group().gens()
    n_divs = len(toric_divs)
    print(f"  Toric divisor group rank: {n_divs}")
    
    # Map U(1)_a → toric divisor index
    # Coord ray i has charge e_a (1 at position a)
    # The divisor D_i on X is the i-th prime divisor
    # O(q_i) for coord ray = O(Σ e_a · D_a) = O(D_i)
    # For non-coord ray: O(q) = O(Σ q[a] · D_a) where D_a corresponds to coord ray a
    
    # Build mapping: U(1) index → divisor index
    u1_to_div = {}
    for i in coord_rays:
        a = np.where(glsm[i] == 1)[0][0]
        u1_to_div[a] = i
    
    print(f"  U(1)→Divisor mapping: {dict(sorted(u1_to_div.items())[:10])}... ({len(u1_to_div)} total)")
    
    def build_divisor(charge_vec):
        """Build divisor from GLSM charge vector."""
        coeffs = [0] * n_divs
        for a, val in enumerate(charge_vec):
            if val != 0 and a in u1_to_div and u1_to_div[a] < n_divs:
                coeffs[u1_to_div[a]] += int(val)
        if all(c == 0 for c in coeffs):
            return X.divisor(0)
        return X.divisor(coeffs)
    
    def h0_dim(charge_vec, label=""):
        """Compute h⁰(X, O(charge_vec))."""
        try:
            D = build_divisor(charge_vec)
            basis = X.cohomology_basis(0, D)
            return len(basis), str(basis)[:60]
        except Exception as e:
            return -1, str(e)[:60]
    
    print(f"\n  {'Entry':<15} {'Min deg':<10} {'Max deg':<10} {'H⁰':<8} {'Status':<10}")
    print(f"  {'-'*15} {'-'*10} {'-'*10} {'-'*8} {'-'*10}")
    
    # Check all charged B → C entries
    for bi in B_rays_all:
        qB = glsm[bi]
        for cj in C_rays_all:
            qC = glsm[cj]
            deg = qB - qC
            label = f"R{bi}→R{cj}"
            dim, info = h0_dim(deg, label)
            status = "✅" if dim > 0 else ("❌" if dim == 0 else "⚠️")
            print(f"  {label:<15} {deg.min():<10} {deg.max():<10} {dim:<8} {status}")
    
    # Check O(0) → C entries  
    for cj in C_rays_all:
        qC = glsm[cj]
        deg = -qC
        label = f"O(0)→R{cj}"
        dim, info = h0_dim(deg, label)
        status = "✅" if dim > 0 else ("❌" if dim == 0 else "⚠️")
        print(f"  {label:<15} {deg.min():<10} {deg.max():<10} {dim:<8} {status}")
    
    # Summary stats
    print(f"\n  {'─'*55}")
    all_dims = {}
    for bi in B_rays_all:
        for cj in C_rays_all:
            dim, _ = h0_dim(glsm[bi] - glsm[cj], "")
            all_dims[(bi,cj)] = dim
    for cj in C_rays_all:
        dim, _ = h0_dim(-glsm[cj], "")
        all_dims[('0',cj)] = dim
    
    n_pos = sum(1 for v in all_dims.values() if v and v > 0)
    n_zero = sum(1 for v in all_dims.values() if v == 0)
    n_err = sum(1 for v in all_dims.values() if v is None or v < 0)
    total = len(all_dims)
    
    print(f"  Entries with sections (h⁰>0): {n_pos}/{total}")
    print(f"  Zero sections (h⁰=0):        {n_zero}/{total}")
    print(f"  Errors:                       {n_err}/{total}")

print("\n" + "=" * 75)
print("  COMPUTATION COMPLETE")
print("=" * 75)
