#!/home/wsl/miniconda/envs/sage37/bin/python3
"""
cgal-triangulate-4d shim for CYTools
Input from CYTools: str(points) + str(heights).replace('[', '(').replace(']', ')')
i.e.: [[x1,y1,...],[x2,y2,...],...](h1,h2,...)
Output: Python repr of simplices list
"""
import sys, re, numpy as np

raw = sys.stdin.read().strip()

# Find the split: the last ']' separates points from heights
last_close = raw.rfind(']')
if last_close >= 0:
    pts_str = raw[:last_close+1]
    h_str = raw[last_close+1:]
else:
    pts_str = raw
    h_str = '()'

# Parse points
import ast
try:
    points = np.array(ast.literal_eval(pts_str), dtype=float)
except:
    # fallback for any edge cases
    pts_clean = pts_str.replace("(", "[").replace(")", "]")
    points = np.array(ast.literal_eval(pts_clean), dtype=float)

# Parse heights
h_clean = h_str.replace("(", "[").replace(")", "]")
try:
    heights = np.array(ast.literal_eval(h_clean), dtype=float)
except:
    heights = None

from scipy.spatial import Delaunay

if heights is not None and len(heights) == len(points) and not np.all(heights == heights[0]):
    lifted = np.hstack([points, heights.reshape(-1, 1)])
    tri = Delaunay(lifted)
else:
    tri = Delaunay(points)

simplices = [[int(x) for x in sorted(list(s))] for s in tri.simplices]

# Filter for star triangulation: all simplices must contain point 0 (origin)
star_simplices = [s for s in simplices if 0 in s]
if star_simplices:
    simplices = star_simplices

print(repr(simplices))
