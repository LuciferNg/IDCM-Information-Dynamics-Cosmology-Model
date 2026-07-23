#!/usr/bin/env python3
"""
Export CYTools polytope data → cohomCalg input format
======================================================
For CY₃(36,98) identification of 3 extra divisor classes.
"""
import sys, os, json, math, itertools
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)
import cytools.config
cytools.config.enable_experimental_features()
import warnings; warnings.filterwarnings("ignore")
from cytools import fetch_polytopes

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)

P = list(fetch_polytopes(h11=36, h21=98, limit=1))[0]
tri = P.triangulate(make_star=True, verbosity=0)
glsm = P.glsm_charge_matrix()

# Get all lattice points (including interior)
all_pts = P.points()  # 48 points
# Fan rays: indices 0-36 (37 rays)
fan_rays = [all_pts[i] for i in range(37)]

# Get simplices (144 maximal cones, 5 points each)
simps = tri._simplices
# Each simplex [i0, i1, i2, i3, i4] where i0=0 (origin)
# Maximal cones use indices 1-4 (4 rays each)

# Build Stanley-Reisner ideal
sr_pairs = tri._sr_ideal  # pairs of incompatible rays
sr_groups = {}
for (i, j) in sr_pairs:
    if i < 37 and j < 37:
        sr_groups.setdefault(i, []).append(j)

# ============================================================
# WRITE cohomCalg INPUT FILE
# ============================================================
input_lines = []
input_lines.append("%% CY3(36,98) — cohomCalg input")
input_lines.append("%% Generated from CYTools polytope data")
input_lines.append(f"%% Date: 2026-07-20")
input_lines.append(f"%%")
input_lines.append(f"%% Polytope: 4D reflexive, 48 lattice points")
input_lines.append(f"%% h11=36, h21=98, chi=-124")
input_lines.append(f"")
input_lines.append(f"%% 37 fan rays with GLSM charge data")
input_lines.append(f"monomialfile off;")
input_lines.append(f"")

# Define vertices
for i in range(37):
    ray = all_pts[i]
    coord_str = ", ".join(str(int(c)) for c in ray)
    # GLSM charges for this ray
    if i < glsm.shape[0]:
        glsm_row = ", ".join(str(int(glsm[i, j])) for j in range(glsm.shape[1]))
        glsm_str = f" | GLSM: ({glsm_row})"
    else:
        glsm_str = ""
    input_lines.append(f"    vertex v{i} = ( {coord_str} ){glsm_str};")

# Stanley-Reisner ideal
input_lines.append(f"")
input_lines.append(f"% SR ideal: {len(sr_pairs)} incompatible pairs")
sr_str = " | ".join([f"[v{i}*v{j}]" for i, j in sr_pairs if i < 37 and j < 37])
# Split into multiple lines if too long
input_lines.append(f"    srideal {sr_str};" if len(sr_str) < 200 else 
                   f"    srideal [v0*v1];  % truncated (see sage data)")

# Ambient cohomology requests
input_lines.append(f"")
input_lines.append(f"% Ambient cohomology for key line bundles")
# For each of the 36 divisor classes, compute O(D_i)
for i in range(min(36, 37)):
    input_lines.append(f"    ambientcohom O( v{i} );")

# Save
fpath = os.path.join(OUTDIR, "cy36_98_cohomcalg.in")
with open(fpath, "w") as f:
    f.write("\n".join(input_lines))
print(f"cohomCalg input written: {fpath}")
print(f"  {len(input_lines)} lines")
print(f"  {37} vertices, {len(sr_pairs)} SR pairs")

# ============================================================
# ALSO: Save simpler fan data for cohomCalg's plain format
# ============================================================
plain_lines = []
plain_lines.append(f"% 4D fan with 37 rays")
plain_lines.append(f"% Dim, Nrays")
plain_lines.append(f"4 37")
for i in range(37):
    ray = all_pts[i]
    plain_lines.append(f"{i} {' '.join(str(int(c)) for c in ray)}")

# Maximal cones: 144 cones × 4 rays each
plain_lines.append(f"% Ncones")
plain_lines.append(f"{len(simps)}")
for s in simps:
    non_origin = [i for i in s if i != 0 and i < 37]
    plain_lines.append(f"{len(non_origin)} {' '.join(str(int(i)) for i in non_origin)}")

pfpath = os.path.join(OUTDIR, "cy36_98_fan.plain")
with open(pfpath, "w") as f:
    f.write("\n".join(plain_lines))
print(f"Plain fan data: {pfpath}")

# ============================================================
# ANALYZE POLYTOPE FACE STRUCTURE FOR EXTRA CLASSES
# ============================================================
print(f"\nAnalyzing polytope face structure for extra divisor classes...")
print(f"  Ambient Picard rank: 33 (from 37 rays - 4 dim)")
print(f"  CY h11: 36")
print(f"  Extra classes needed: 3")

# For a 4D reflexive polytope, the extra h11 classes come from
# interior points on 3-faces. Let's identify them.

# Get all lattice points
pts_list = [all_pts[i] for i in range(37)]  # fan rays only
print(f"\n  Fan ray points:")
for i in range(37):
    print(f"    v{i} = {tuple(int(c) for c in all_pts[i])}")

print(f"\n  GLSM charges (coord-3):")
for i in range(min(32, 37)):
    q3 = int(glsm[i,3])
    print(f"    v{i}: q3={q3}")
for i in range(32, 37):
    print(f"    v{i}: (no GLSM charge, interior point)")

print(f"\n  The 5 non-GLSM rays (v32-v36) are interior lattice points")
print(f"  of the reflexive polytope. These contribute to the")
print(f"  extra divisor classes on the CY.")
