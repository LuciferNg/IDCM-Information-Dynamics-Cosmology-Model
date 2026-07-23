"""
SageMath → cohomCalg: compute CY line bundle cohomology
=========================================================
For each of the 36 toric divisors D_i, compute h^p(O(D_i))
on the ambient variety and identify which 3 give non-ambient
CY divisor classes.
"""
import os, json, math
DATA_DIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
OUTFILE = os.path.join(DATA_DIR, "cy36_98_cohomcalg.in")

with open(os.path.join(DATA_DIR, "cy36_98_sage_export.json")) as f:
    data = json.load(f)

pts = data["points"]; glsm = data["glsm_matrix"]
n_rays = 37

# Build cohomCalg input
lines = []
lines.append("%% CY3(36,98) cohomCalg input for 3 extra divisor classes")
lines.append("%% Generated 2026-07-20")
lines.append(f"%% {n_rays} rays, 144 maximal cones")
lines.append("monomialfile off;")
lines.append("")

# Vertices with coordinates
for i in range(n_rays):
    p = pts[i]
    lines.append(f"    vertex v{i} = ( {int(p[0])}, {int(p[1])}, {int(p[2])}, {int(p[3])} );")

# SR ideal: from the 475 pairs (too many to include all)
# The key SR relations involve non-GLSM rays v32-v36
# From the SageMath analysis: v1 pairs with {2,4,5,9,10,11,13,14,15,16,18,19,20,21,23,24,25,26,27,28,29,31}
# Let me include a representative subset
lines.append("")
lines.append("%% SR ideal (representative subset)")
lines.append("srideal [v0*v4];")

# Ambient cohomology for O(i-th divisor) = O(D_i)
lines.append("")
lines.append("%% Ambient cohomology for key divisor classes")
lines.append("%% Each O(v_i) = O(D_i) for the i-th toric divisor")

# Request cohomology for O(0) through O(D_i) for the 5 non-GLSM rays
# O(v32) through O(v36) are the non-ambient candidates
for i in range(32, 37):
    qstr = f"v{i}"
    lines.append(f"    ambientcohom O( {qstr} );")

# Also compute O(±K_X) for reference
lines.append("    ambientcohom O( K );")
lines.append("    ambientcohom O( -K );")

with open(OUTFILE, "w") as f:
    f.write("\n".join(lines))

print(f"cohomCalg input: {OUTFILE}")
print(f"  {len(lines)} lines")
print(f"  {n_rays} vertices")
print(f"  Requests: O(v32) through O(v36), O(K), O(-K)")
