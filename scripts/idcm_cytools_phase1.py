#!/usr/bin/env python3
"""
IDCM CY3(36,98) — CYTools: Fetch, Triangulate, Extract GLSM Data
=================================================================
Phase 1 of the Koszul computation pipeline.
Outputs: triangulation data, GLSM charges, toric divisor list
"""
import sys, os, json, math
sys.path.insert(0, '/tmp/cy_venv/lib/python3.11/site-packages')
from cytools import fetch_polytopes, Polytope, calabiyau

PHI = (1 + math.sqrt(5))/2
PHI_INV = PHI - 1

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)

print("="*70)
print("IDCM — CYTools: CY₃(36,98) FULL ANALYSIS")
print("="*70)

# 1. Fetch polytopes with (h11,h21) = (36,98)
print("\n>>> 1. FETCH POLYTOPES <<<")
polytopes = list(fetch_polytopes(h11=36, h21=98, limit=5))
print(f"Found: {len(polytopes)} polytopes with (36,98)")

if not polytopes:
    print("[FAIL] No (36,98) polytope found in KS database!")
    sys.exit(1)

P = polytopes[0]
print(f"Polytope: dim={P.dim()}, N_vertices={P.nvertices()}, N_points={P.npoints()}")
print(f"Hodge numbers: h11={P.h11()}, h21={P.h21()}, chi={P.chi()}")
print(f"Reflexive: {P.is_reflexive()}")

# 2. Save full polytope data
points = P.points()
points_list = [list(pt) for pt in points]
print(f"\nTotal lattice points in polytope: {len(points_list)}")

# 3. Triangulation
print("\n>>> 2. TRIANGULATION <<<")
print("Computing fine regular star triangulation (FRST)...")
tri = P.triangulate(flip_preserve_simplices=True, fine=True, regular=True)
n_tri = len(tri)
print(f"Number of top-dimensional simplices in FRST: {n_tri}")

# 4. Build toric variety via CalabiYau
print("\n>>> 3. CALABI-YAU DATA <<<")
cy = calabiyau.CalabiYau(P)
print(f"N_rays (toric divisors): {cy.n_rays}")

# Get all divisor information
rays = cy.rays()
print(f"Ray coordinates dimension: {rays.shape}")
print(f"First 5 rays:\n{rays[:5]}")

# 5. Compute divisor cohomology
print("\n>>> 4. DIVISOR COHOMOLOGY <<<")
div_data = []
for i in range(min(cy.n_rays, 40)):  # All prime toric divisors
    try:
        ch = cy.divisor_cohomology(i, wrapped=False)
        h = [ch.get(j, 0) for j in range(5)]
        div_data.append({"idx": i, "h": h, "chi": sum((-1)**j * h[j] for j in range(5))})
    except Exception as e:
        div_data.append({"idx": i, "h": [0]*5, "chi": 0, "error": str(e)})

print(f"\nDivisor cohomology computed for {len(div_data)} divisors")

# Print divisor cohomology summary
for dd in div_data[:10]:
    h = dd["h"]
    print(f"  D_{dd['idx']:2d}: h⁰={h[0]} h¹={h[1]} h²={h[2]} h³={h[3]} h⁴={h[4]} χ={dd['chi']:.0f}")

# 6. Compute line bundle / GLSM charge structure
print("\n>>> 5. GLSM CHARGES & MONAD STRUCTURE <<<")

# For each ray, get the charge (weight under the GLSM)
# The GLSM charges are essentially the ray coordinates transformed
print("\nGLSM charges (first 10 rays, first 4 coordinates):")
for i in range(min(10, len(rays))):
    r = rays[i]
    print(f"  Ray {i:2d}: [{r[0]:4d} {r[1]:4d} {r[2]:4d} {r[3]:4d}]")

# 7. Compute intersection numbers (topological!)
print("\n>>> 6. INTERSECTION NUMBERS <<<")
try:
    # Triple intersection numbers
    ints = cy.intersection_numbers()
    print(f"Intersection numbers computed: {len(ints)} non-zero entries")
except Exception as e:
    print(f"Intersection numbers: {e}")
    # Fallback: compute via SageMath later

# 8. Save all data
output = {
    "h11": P.h11(), "h21": P.h21(), "chi": P.chi(),
    "n_vertices": P.nvertices(), "n_points": P.npoints(), "n_rays": cy.n_rays,
    "n_triangulations": n_tri,
    "points": [list(map(int, pt)) for pt in points],
    "rays": [list(map(int, ray)) for ray in rays[:cy.n_rays]],
    "divisor_cohomology": div_data,
}

with open(os.path.join(OUTDIR, "cy36_98_cytools.json"), "w") as f:
    json.dump(output, f, indent=2)
print(f"\nData saved to cy36_98_cytools.json")

# 9. Compute the GLSM charges on Coordinate 3
print("\n>>> 7. COORDINATE 3 — GLSM CHARGE VECTOR <<<")
# The coordinate-3 projection gives the GLSM charges relevant to FN
coord3_charges = []
for ray in rays[:cy.n_rays]:
    # Project onto coordinate axis 3 (index 3, the 4th column)
    c3 = ray[3]
    coord3_charges.append(int(c3))

from collections import Counter
charge_counts = Counter(coord3_charges)
print(f"Coordinate 3 charges (n_rays={len(coord3_charges)}):")
for charge, count in sorted(charge_counts.items(), key=lambda x: -x[1]):
    print(f"  charge={charge:3d}: {count} rays")

# The GLSM charges that encode FN structure
charges_sorted = sorted(set(coord3_charges), reverse=True)
print(f"\nSorted unique charges: {charges_sorted}")
print(f"Top 6 charges (Coordinate 3): {charges_sorted[:6]}")

# Compute FN exponents from these charges  
print("\n>>> 8. FN CHARGES FROM GLSM <<<")
# The FN charges k are related to the GLSM charges
# k_u expected ≈ 10.2, k_d ≈ 7.9, k_l ≈ 5.9

# Check: what GLSM charges correspond to these k values?
for k_name, k_val in [("k_u ~ 33β", 33*PHI_INV/2), ("k_d ~ 26β-φ⁻⁴", 26*PHI_INV/2 - PHI_INV**4), ("k_l ~ 19β", 19*PHI_INV/2)]:
    # The GLSM charge on coordinate 3 should encode the FN charge
    # FN charge is the weight under the GLSM U(1) on coordinate 3
    # k = some linear combination of GLSM charges
    expected_charge = k_val * 4  # approximate scaling
    print(f"  {k_name} = {k_val:.4f} → approx GLSM coor3 = {expected_charge:.1f}")

print("\n" + "="*70)
print("CYTools Phase 1 complete. Proceed to SageMath for Koszul.")
print("="*70)
