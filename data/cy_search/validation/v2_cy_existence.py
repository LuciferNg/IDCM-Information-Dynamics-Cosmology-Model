#!/usr/bin/env python3
"""IDCM Validation v2: CY(36,98) Existence via CYTools"""
from cytools import fetch_polytopes, config
config.enable_experimental_features()

print("="*60)
print("v2_cy_existence.py — CY(36,98) Existence")
print("="*60)

polytopes = list(fetch_polytopes(h11=36, h21=98, limit=3))
print(f"Polytopes found: {len(polytopes)}")
if polytopes:
    p = polytopes[0]
    print(f"Dimension: {p.dimension()}")
    verts = p.vertices()
    print(f"Vertices: {verts.shape[1]}")
    pts = p.points()
    print(f"Points: {pts.shape[0]}")
    facets = p.facets()
    print(f"Facets: {facets.shape[1] if len(facets.shape) > 1 else facets.shape[0]}")
    print(f"Reflexive: Yes (from fetch_polytopes)")
    h11, h21 = p.h11, p.h21
    print(f"h11 = {h11}, h21 = {h21}")
    chi = 2*(h11 - h21)
    print(f"chi = 2*({h11}-{h21}) = {chi}")
    pass_flag = (h11 == 36) and (h21 == 98)
    print(f"Pass: {'YES' if pass_flag else 'NO'}")
print("="*60)
