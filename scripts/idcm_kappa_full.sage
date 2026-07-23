"""
Compute full 36D triple intersection tensor and save as JSON.
FN charges computed separately in Python.
"""
import os, json, math, sys, time
from sage.all import *
from sage.schemes.toric.all import *
from sage.geometry.cone import *

DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
with open(os.path.join(DATA_DIR, "cy36_98_sage_export.json")) as f:
    data = json.load(f)
pts = data["points"]; simps = data["simplices"]

print("Building simplicial fan...")
fan_pts = [vector(ZZ, pts[i]) for i in range(37)]
cones = [[i for i in s if i != 0] for s in simps if len([i for i in s if i != 0]) == 4]
F = Fan(cones, fan_pts, lattice=ToricLattice(4), check=True)
X = ToricVariety(F)
H = X.cohomology_ring()
D = [H(d) for d in X.toric_divisor_group().gens()]
nD = len(D)
antiK = H(-X.K())
print(f"{nD} divisors, cohomology ring ready")

# Compute ALL triple intersections
print(f"Computing {nD*(nD+1)*(nD+2)//6} symmetric entries...")
kappa = {}
count = 0; nonzero = 0
t0 = time.time()
for i in range(nD):
    for j in range(i, nD):
        for k in range(j, nD):
            val = X.integrate(D[i] * D[j] * D[k] * antiK)
            ival = int(val) if val else 0
            if ival:
                kappa[f"{i},{j},{k}"] = ival
                nonzero += 1
            count += 1
    if (i+1) % 6 == 0:
        dt = time.time() - t0
        print(f"  [{i+1}/{nD}] {count} entries, {nonzero} non-zero, {dt:.0f}s")

# Save
sparsity = float(100.0 * (1.0 - float(nonzero) / float(count)))
print("\nDone: %d entries, %d non-zero, %.1f%% zero" % (count, nonzero, sparsity))
out = {"kappa": kappa, "shape": [nD, nD, nD], "total": int(count), "nonzero": int(nonzero)}
fpath = os.path.join(DATA_DIR, "kappa_36d_raw.json")
with open(fpath, "w") as f:
    json.dump(out, f)
print(f"Saved to {fpath}")
