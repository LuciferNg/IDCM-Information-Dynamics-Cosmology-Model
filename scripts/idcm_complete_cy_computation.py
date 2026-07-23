#!/usr/bin/env python3
"""
IDCM CY₃(36,98) — CORRECTED FULL COMPUTATION
=============================================
"""
import sys, os, json, math
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)
from cytools import fetch_polytopes, calabiyau
from collections import Counter

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)
PHI = (1 + math.sqrt(5))/2; PHI_INV = PHI - 1; BETA = PHI_INV/2; LAT = "N"

print("="*70)
print("IDCM — CY₃(36,98) FULL COMPUTATION")
print("="*70)

# 1. Fetch
polys = list(fetch_polytopes(h11=36, h21=98, limit=5))
P = polys[0]
verts = P.vertices(); pts = P.points()
print(f"\n1. Polytope: {len(verts)}V, {len(pts)}P")
print(f"   h¹¹={P.h11()}, h²¹={P.h21()}, χ={P.chi(LAT)}")
print(f"   Reflexive={P.is_reflexive()}, Favorable={P.is_favorable(LAT)}")

# 2. GLSM charges
glsm = P.glsm_charge_matrix()
n_rays, n_rel = glsm.shape
print(f"\n2. GLSM: {n_rays}×{n_rel}")
for col in range(4):
    ch = glsm[:, col].tolist()
    unique_desc = sorted(set(ch), reverse=True)
    cnt = Counter(ch)
    print(f"   Coordinate {col}: unique={unique_desc[:8]}... counts={dict(sorted(cnt.items(), key=lambda x:-x[0]))}")

# 3. Triangulate
print(f"\n3. Triangulating (may take a minute)...")
tri = P.triangulate(make_star=True, backend='cgal', verbosity=0)
print(f"   {tri}")

# 4. CalabiYau
cy = calabiyau.CalabiYau(P, triang=tri)
print(f"\n4. CalabiYau: n_rays={cy.n_rays}, rays={cy.rays().shape}")

# 5. Divisor cohomology
print(f"\n5. Divisor cohomology:")
div_h = []
for i in range(min(cy.n_rays, 40)):
    try:
        ch = cy.divisor_cohomology(i)
        dims = [ch.get(j, 0) for j in range(5)]
        chi = sum((-1)**j * dims[j] for j in range(5))
        div_h.append({"idx": i, "dims": dims, "chi": chi})
    except Exception as e:
        div_h.append({"idx": i, "dims": [0]*5, "chi": 0, "err": str(e)[:60]})
nonz = [d for d in div_h if d["chi"] != 0]
for d in nonz:
    ds = d["dims"]
    print(f"   D_{d['idx']:2d}: h⁰={ds[0]} h¹={ds[1]} h²={ds[2]} h³={ds[3]} χ={d['chi']:3d}")

# 6. Intersections
print(f"\n6. Intersections:")
try:
    ints = cy.intersection_numbers()
    print(f"   {len(ints)} non-zero triple intersections")
    for i, (k, v) in enumerate(ints.items()):
        if i >= 8: break
        print(f"   D_{k[0]}·D_{k[1]}·D_{k[2]} = {v}")
except Exception as e:
    print(f"   {e}")

# 7. IDCM FN charges
k_u = 33 * BETA; k_d = 26 * BETA - PHI_INV**4; k_l = 19 * BETA
print(f"\n7. IDCM FN charges:")
print(f"   k_u = 33β = {k_u:.4f}")
print(f"   k_d = 26β - φ⁻⁴ = {k_d:.4f}")
print(f"   k_l = 19β = {k_l:.4f}")

# 8. GLSM → FN mapping
coord3 = glsm[:, 3].tolist()
charges = sorted(set(coord3), reverse=True)
print(f"\n8. GLSM coord3 → FN mapping:")
for c in charges:
    print(f"   charge {c:2d}: k_u/c={k_u/c:.4f}, k_d/c={k_d/c:.4f}, k_l/c={k_l/c:.4f}")

# Best matching charges
for name, k in [("k_u", k_u), ("k_d", k_d), ("k_l", k_l)]:
    best = sorted([(abs(c - round(k)), c) for c in charges if c > 0])
    print(f"   {name}={k:.2f}: best GLSM charges={[c for _,c in best[:4]]}")

# 9. Check CY intersection → φ⁻⁴
print(f"\n9. φ⁻⁴ verification:")
print(f"   φ⁻⁴ = {PHI_INV**4:.6f}")
print(f"   1/φ⁴ = {1/PHI**4:.6f}")
print(f"   Need to check if any divisor volume ratio = φ⁻⁴")
print(f"   (requires J* fixed point in 36D Kähler cone)")

# 10. Save
results = {
    "h11": P.h11(), "h21": P.h21(), "chi": P.chi(LAT),
    "n_verts": len(verts), "n_pts": len(pts),
    "n_rays_glsm": n_rays, "n_rays_cy": cy.n_rays,
    "glsm_shape": [n_rays, n_rel],
    "coord3_charges": coord3,
    "idcm_k_u": round(k_u, 6), "idcm_k_d": round(k_d, 6), "idcm_k_l": round(k_l, 6),
}
with open(os.path.join(OUTDIR, "cy36_98_results.json"), "w") as f:
    json.dump(results, f, indent=2)

print(f"\n{'='*70}")
print(f"✅ RESULTS SAVED")
print(f"{'='*70}")
