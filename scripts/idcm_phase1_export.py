#!/usr/bin/env python3
"""Phase 1: Export CYTools triangulation → SageMath JSON"""
import sys, os, json
PACKAGE_DIR = "/tmp/cy_venv/lib/python3.11/site-packages"
if PACKAGE_DIR not in sys.path: sys.path.insert(0, PACKAGE_DIR)
import cytools.config
cytools.config.enable_experimental_features()
import warnings; warnings.filterwarnings("ignore")
from cytools import fetch_polytopes, calabiyau
import numpy as np

OUTDIR = "/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/cy_search/data"
os.makedirs(OUTDIR, exist_ok=True)

def convert(obj):
    if isinstance(obj, dict):
        return {k: convert(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert(v) for v in obj]
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return convert(obj.tolist())
    elif isinstance(obj, np.bool_):
        return bool(obj)
    return obj

P = list(fetch_polytopes(h11=36, h21=98, limit=1))[0]
tri = P.triangulate(make_star=True, verbosity=0)
pts = P.points(); verts = P.vertices()
simps = tri.simplices(); sr = tri.sr_ideal()
glsm = P.glsm_charge_matrix(); lrels = P.glsm_linear_relations()
cy = calabiyau.CalabiYau(tri.get_toric_variety())
pts_list = pts.tolist()

# Interior mask
try:
    interior = P.interior_points().tolist()
    interior_set = set(tuple(p) for p in interior)
except:
    interior_set = {(0,0,0,0)}
interior_mask = [tuple(p) in interior_set for p in pts_list]

export = convert({
    "n_vertices": len(verts), "n_points": len(pts),
    "vertices": [list(v) for v in verts],
    "points": pts_list,
    "n_simplices": len(simps),
    "simplices": [list(s) for s in simps],
    "n_sr": len(sr),
    "sr_ideal": [[int(g[0]), int(g[1])] for g in sr] if sr else [],
    "glsm_shape": list(glsm.shape),
    "glsm_matrix": glsm.tolist(),
    "glsm_linrels": lrels.tolist(),
    "h11": int(cy.h11()), "h21": int(cy.h21()), "chi": int(cy.chi()),
    "interior_mask": interior_mask
})

with open(os.path.join(OUTDIR, "cy36_98_sage_export.json"), "w") as f:
    json.dump(export, f, indent=2)

print(f"Exported: {len(pts)} pts, {len(simps)} simplices, {len(sr)} SR ideals")
print(f"GLSM: {glsm.shape}, h11={cy.h11()}, h21={cy.h21()}")
