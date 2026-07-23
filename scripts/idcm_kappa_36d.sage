"""
FINAL: 36D TRIPLE INTERSECTION TENSOR κ_ijk
=============================================
Compute ALL 8436 triple intersection entries in SageMath's
Chow ring (which already handles the 475 SR generators).
"""
import os, json, math, sys, time
from sage.all import *
from sage.schemes.toric.all import *
from sage.geometry.cone import *

DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
with open(os.path.join(DATA_DIR, "cy36_98_sage_export.json")) as f:
    data = json.load(f)
pts = data["points"]; simps = data["simplices"]

PHI = (1+math.sqrt(5))/2; PHI_INV = PHI-1; LN_PHI = math.log(PHI)
BETA = PHI_INV/2; KAPPA3 = (1/16)**3

print("="*70)
print("FINAL 36D TRIPLE INTERSECTION TENSOR")
print("="*70)

# Simplicial fan (36 non-origin rays, 4 rays per cone)
fan_pts = [vector(ZZ, pts[i]) for i in range(37)]
cones = [[i for i in s if i != 0] for s in simps if len([i for i in s if i != 0]) == 4]
F = Fan(cones, fan_pts, lattice=ToricLattice(4), check=True)
X = ToricVariety(F)
H = X.cohomology_ring()
D = [H(d) for d in X.toric_divisor_group().gens()]
nD = len(D)
antiK = H(-X.K())
print(f"  {nD} divisors, cohomology ring ready")

# ============================================================
# FULL TRIPLE INTERSECTION
# ============================================================
print(f"\n  Computing κ_ijk = ∫ D_i·D_j·D_k·(-K_X) for all {nD} divisors...")
print(f"  Total symmetric entries: {nD*(nD+1)*(nD+2)//6}\n")

kappa = {}
count = 0; nonzero = 0
t0 = time.time()
for i in range(nD):
    for j in range(i, nD):
        for k in range(j, nD):
            prod = D[i] * D[j] * D[k] * antiK
            val = X.integrate(prod)
            key = f"{i},{j},{k}"
            kappa[key] = int(val) if val else 0
            count += 1
            if val:
                nonzero += 1
    if (i+1) % 6 == 0 or i == nD-1:
        elapsed = time.time() - t0
        rate = count / elapsed if elapsed > 0 else 0
        print(f"    [{i+1:2d}/{nD}] {count} entries, {nonzero} non-zero, "
              f"{elapsed:.0f}s @ {rate:.0f}/s")

nz = int(nonzero)
cnt = int(count)
sparsity = (1.0 - float(nz)/float(cnt)) * 100.0
print(f"  Done: {cnt} entries, {nz} non-zero")
print(f"  Sparsity: {sparsity:.1f}% zero")

# Save raw kappa data
fpath = os.path.join(DATA_DIR, "kappa_36d_raw.json")
with open(fpath, "w") as f:
    json.dump({"kappa": {k: int(v) for k,v in kappa.items() if v},
               "shape": [int(nD), int(nD), int(nD)],
               "total": cnt, "nonzero": nz}, f)
scale = 0.090141

# Build the symmetric kappa matrix
kappa_mat = [[[0]*nD for _ in range(nD)] for __ in range(nD)]
for key, val in kappa.items():
    i, j, k = [int(x) for x in key.split(",")]
    val_int = int(val) if val else 0
    for (a,b,c) in [(i,j,k), (i,k,j), (j,i,k), (j,k,i), (k,i,j), (k,j,i)]:
        kappa_mat[a][b][c] = val_int

# Volume at any t
def vol_t(t):
    s = 0.0
    for i in range(nD):
        for j in range(i, nD):
            for k in range(j, nD):
                s += kappa_mat[i][j][k] * t[i] * t[j] * t[k]
    return s / 6.0

# Check uniform J*
t_uniform = [scale] * nD
v_uniform = vol_t(t_uniform)
print(f"\n  Uniform J*: Vol = {v_uniform:.6e} (target {KAPPA3:.6e})")

# GLSM charges
glsm = data["glsm_matrix"]
glsm_c3 = [int(glsm[i,3]) for i in range(min(glsm.shape[0], nD))]
charge_rays = {c: [i for i,r in enumerate(glsm_c3) if r==c] for c in [12,10,9,8,7,6]}

print(f"\n  FN charges at uniform J*:")
for c, rays in charge_rays.items():
    if not rays: continue
    for r in rays:
        # ∂Vol/∂t_i = (1/2) Σ κ_ijk t_j t_k
        dvol = 0.0
        for j in range(nD):
            for k in range(j, nD):
                dvol += kappa_mat[r][j][k] * t_uniform[j] * t_uniform[k]
        dvol /= 2.0
        # k = -ln(Vol(D_i)/Vol(CY)) / ln(φ)  
        vol_div = dvol  # This is the divisor volume (not normalized)
        k_fn = -math.log(vol_div / v_uniform) / LN_PHI if vol_div > 0 else 0
        print(f"    charge {c:2d} ray {r:2d}: Vol(D)={vol_div:.6e}, k={k_fn:.2f}")

print(f"\n{'='*70}")
print(f"36D TRIPLE INTERSECTION COMPLETE: {count} entries")
print(f"{'='*70}")

# Save
fpath = os.path.join(DATA_DIR, "kappa_36d_full.json")
with open(fpath, "w") as f:
    json.dump({"kappa": {k: int(v) for k,v in kappa.items() if v},
               "shape": [nD, nD, nD]}, f)
print(f"\nSaved to {fpath}")
