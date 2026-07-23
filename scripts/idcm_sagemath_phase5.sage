"""
IDCM CY3(36,98) — PHASE 5: J* FIXED POINT IN 36D
==================================================
Using SageMath Chow ring:
1. Compute triple intersection numbers κ_ijk
2. Volume functional Vol(t) = (1/6)κ_ijk t^i t^j t^k
3. Find J* where Vol = κ³ = 1/4096
4. Compute divisor volumes → FN charges k_u, k_d, k_l
"""
import os, json, math, sys

DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
print("="*70)
print("PHASE 5: J* FIXED POINT IN 36D KÄHLER MODULI")
print("="*70)

# Load export data
with open(os.path.join(DATA_DIR, "cy36_98_sage_export.json")) as f:
    data = json.load(f)

points = data["points"]
simplices = data["simplices"]
glsm = matrix(ZZ, data["glsm_matrix"])
linrels_raw = data["glsm_linrels"]
sr_ideal_raw = data["sr_ideal"]
h11_cy = data["h11"]  # 36

PHI = (1 + math.sqrt(5))/2
PHI_INV = PHI - 1
BETA = PHI_INV/2
KAPPA = 1/16; KAPPA3 = KAPPA**3

# ============================================================
# BUILD FAN + TORIC VARIETY (from Phase 2-4)
# ============================================================
print("\n1. Building fan + toric variety...")
ray_indices = list(range(37))  # 0-36
fan_rays = [vector(ZZ, points[i]) for i in ray_indices]
idx_map = {old: new for new, old in enumerate(ray_indices)}
fan_cones = [[idx_map[i] for i in s if i in ray_indices] for s in simplices]
fan_cones = [c for c in fan_cones if len(c) == 5]

lattice = ToricLattice(4)
F = Fan(fan_cones, fan_rays, lattice=lattice, check=False)
print(f"  Fan: {F.nrays()} rays, {len(fan_cones)} maximal cones")

X = ToricVariety(F)
print(f"  X: {X}")

# ============================================================
# COHOMOLOGY / CHOW RING
# ============================================================
print("\n2. Computing cohomology ring...")
# Cox ring
n_rays = F.nrays()
S = PolynomialRing(QQ, 'x', n_rays)

# SR ideal
sr_gens = []
seen = set()
for (i, j) in sr_ideal_raw:
    if i < n_rays and j < n_rays:
        gen = S.gen(i) * S.gen(j)
        if gen not in seen:
            sr_gens.append(gen)
            seen.add(gen)
print(f"  SR ideal: {len(sr_gens)} unique generators")

# Linear relations from GLSM linrels
lin_gens = []
for row in linrels_raw:
    poly = sum(S.gen(j) * int(row[j]) for j in range(min(len(row), n_rays)))
    if poly != 0:
        lin_gens.append(poly)
print(f"  Linear ideal: {len(lin_gens)} generators")

# Chow ring
chow = S.quotient(S.ideal(sr_gens + lin_gens))
print(f"  Chow ring: {chow}")

# Anti-canonical class = sum of all toric divisors
# In Chow ring, this is the sum of all variables
antiK_class = sum(chow.gen(i) for i in range(n_rays))
print(f"  Anti-canonical class [sum x_i] computed")

# ============================================================
# TRIPLE INTERSECTION NUMBERS
# ============================================================
print("\n3. Computing triple intersection numbers κ_ijk...")
print(f"   This requires computing D_i * D_j * D_k * (-K) in Chow ring A⁴(X)")
print(f"   The degree map picks out the coefficient of the fundamental class.")
print(f"   For a complete toric variety, this is the top-degree coefficient.")
print(f"")

# We'll compute the intersection matrix by working in the Chow ring
# For divisors D_i, D_j, D_k:
# κ_ijk = ∫_CY D_i·D_j·D_k = ∫_X D_i·D_j·D_k·[-K_X]
#       = coefficient of volume form in A⁴(X)

# Build the list of divisor classes in the Chow ring
# Each x_i corresponds to divisor D_i
D = [chow.gen(i) for i in range(n_rays)]
antiK = sum(D)  # -K_X = sum of all toric divisors

# We'll compute κ_ijk for a subset of divisors
# Focus on the key GLSM charge carriers
# From GLSM: which rays have charges 12, 10, 9, 8, 7, 6?
glsm_coord3 = [glsm[i, 3] for i in range(glsm.nrows())]
charge_to_rays = {}
for i, c in enumerate(glsm_coord3):
    c_val = int(c)
    if c_val not in charge_to_rays:
        charge_to_rays[c_val] = []
    charge_to_rays[c_val].append(i)

print(f"  GLSM charge-to-ray mapping:")
for ch in [12, 10, 9, 8, 7, 6]:
    rays = charge_to_rays.get(ch, [])
    print(f"    charge {ch:2d}: rays {rays}")

# Compute the cubic intersection + degree for each triple of key divisors
print(f"\n  Computing intersection numbers for key divisors...")
print(f"  (This may take a while for 37-var polynomial computations)")

# For the top divisors (by charge), compute diagonal elements
try:
    # Test with one divisor first
    d0_sq = D[0] * D[0]
    print(f"  D_0^2 computed (in Chow ring)")
except Exception as e:
    print(f"  D_0^2 failed: {str(e)[:60]}")

# ============================================================
# VOLUME FUNCTIONAL AND J* OPTIMIZATION
# ============================================================
print(f"\n4. Volume functional and J* optimization:")
print(f"")
print(f"   Vol(t) = (1/6) * Σ κ_ijk * t_i * t_j * t_k")
kappa3_float = float(KAPPA3)
print(f"   CY volume constraint: Vol(J*) = κ³ = {kappa3_float:.10f}")
print(f"")
print(f"   Strategy: Use CYTools-computed CY volume at uniform scaling")
print(f"   and the divisor volumes at that point to extract κ_ijk.")

# Use CYTools data: compute the Kähler cone and find J*
# Since we already know Vol([1]*37) and can compute the scaling,
# the J* fixed point is at t* = scale * [1,...,1]
# with scale = (KAPPA3 / Vol([1]*37))^(1/3)

# We don't have Vol([1]*37) from CYTools directly (it uses 32D ambient)
# But we can compute it from the Chow ring intersection numbers

print(f"\n5. FN charge extraction:")
print(f"")
print(f"   k_u = -log_φ(Vol(D_u) / Vol(CY)) for divisor D_u (charge 10)")
print(f"   k_d = -log_φ(Vol(D_d) / Vol(CY)) for divisor D_d (charge 8)")
print(f"   k_l = -log_φ(Vol(D_l) / Vol(CY)) for divisor D_l (charge 6)")
print(f"")
print(f"   IDCM predicts:")
print(f"   k_u = 33β = {33*BETA:.4f}")
print(f"   k_d = 26β - φ⁻⁴ = {26*BETA - PHI_INV**4:.4f}")
print(f"   k_l = 19β = {19*BETA:.4f}")

# ============================================================
# SAVE PHASE 5 RESULTS
# ============================================================
print(f"\n6. Saving Phase 5 results...")
results = {}
results["h11"] = int(h11_cy)
results["n_rays"] = int(n_rays)
results["kappa3"] = float(KAPPA3)
with open(os.path.join(DATA_DIR, "sagemath_phase5.json"), "w") as f:
    json.dump(results, f, indent=2)

print(f"\n{'='*70}")
print(f"PHASE 5: J* FIXED POINT — SETUP COMPLETE")
print(f"{'='*70}")
print(f"""
The J* fixed point and FN charge computation require:
1. Complete Chow ring multiplication table for 37 divisors
2. Triple intersection numbers κ_ijk
3. 36D Kähler cone optimization

The Chow ring has been constructed with {chow.ngens()} generators.
To complete the computation, we need to evaluate the polynomial
products D_i * D_j * D_k * (-K) in the quotient ring.

Due to the 37-variable polynomial ring complexity,
this is best done with a targeted computation
focusing on the ~10 key divisors (charges 12,10,9,8,7,6).
""")
print(f"""
IDCM FN charge comparison when J* data is ready:
  k_u = 33β = {33*BETA:.6f}  vs  GLSM charge 10
  k_d = 26β - φ⁻⁴ = {26*BETA - PHI_INV**4:.6f}  vs  GLSM charge 8
  k_l = 19β = {19*BETA:.6f}  vs  GLSM charge 6
""")
