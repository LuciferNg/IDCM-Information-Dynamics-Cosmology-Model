#!/usr/bin/env python3
"""Generate proper cohomCalg input with one srideal per line"""
import sys, os, json, itertools
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)
import cytools.config
cytools.config.enable_experimental_features()
import warnings; warnings.filterwarnings("ignore")
from cytools import fetch_polytopes
import numpy as np

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"

P = list(fetch_polytopes(h11=36, h21=98, limit=1))[0]
tri = P.triangulate(make_star=True, verbosity=0)
glsm = np.array(P.glsm_charge_matrix())
pts = P.points()

# Get compatible edges from triangulation
simps = tri._simplices
compatible = set()
for s in simps:
    for i, j in itertools.combinations(sorted(s), 2):
        if i < 37 and j < 37:
            compatible.add((min(i,j), max(i,j)))

# Incompatible pairs = SR generators
sr_pairs = [(i,j) for i in range(37) for j in range(i+1,37) if (i,j) not in compatible]
print(f"SR generators: {len(sr_pairs)}")

# Write input
lines = []
lines.append("%% CY3(36,98) cohomCalg input")
lines.append("%% 37 vertices, 32 GLSM charges")
lines.append("monomialfile off;")
lines.append("")

for i in range(37):
    p = pts[i]
    coord = f"{int(p[0])}, {int(p[1])}, {int(p[2])}, {int(p[3])}"
    if i < glsm.shape[1]:
        q = ", ".join(str(int(glsm[j,i])) for j in range(glsm.shape[0]))
    else:
        q = ", ".join(["0"] * glsm.shape[0])
    lines.append(f"    vertex v{i} = ( {coord} ) | GLSM: ( {q} );")

lines.append("")
# Each SR generator on its own line
for i, j in sr_pairs:
    lines.append(f"    srideal [v{i}*v{j}];")

# Cohomology requests
lines.append("")
for i in range(37):
    lines.append(f"    ambientcohom O( v{i} );")
lines.append("    ambientcohom O( K );")
lines.append("    ambientcohom O( -K );")

fpath = os.path.join(OUTDIR, "cy36_98_chomcalg_sr.in")
with open(fpath, "w") as f:
    f.write("\n".join(lines))
print(f"Written: {fpath} ({len(lines)} lines)")
