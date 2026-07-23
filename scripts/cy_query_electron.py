#!/usr/bin/env python3
"""CYTools query for electron charge-5, charge-7 divisor data."""
import cytools, json, numpy as np
cytools.config.enable_experimental_features()

p = list(cytools.fetch_polytopes(h11=36, h21=98, limit=1, lattice="N"))[0]
print(f"Polytope: {p.Nvertices()} vertices, {p.Npoints()} lattice points")

tri = p.triangulate(make_star=True, verbosity=0)
cy = tri.get_cy()

Q = np.array(cy.glsm_charge_matrix(), dtype=int)
coord3 = Q[2]  # row 2 = Coordinate 3 charges

# Charge distribution
charges = {}
for i in range(37):
    c = int(coord3[i])
    charges.setdefault(c, []).append(i)

print("\nGLSM Coordinate 3 charge distribution:")
for c in sorted(charges.keys(), reverse=True):
    print(f"  q3={c:2d}: rays {charges[c]} (count={len(charges[c])})")

q5 = charges.get(5, [])
q7 = charges.get(7, [])
print(f"\nElectron sector (q3=5): rays {q5}")
print(f"Charge-7 sector: rays {q7}")

# Divisor basis
db = cy.divisor_basis()
ndiv = len(db)
print(f"\nDivisor basis dimension = {ndiv}")

# Check which q3=5 and q3=7 rays are in divisor basis
print(f"\nRay vs divisor_basis check:")
for c in [5, 7]:
    for r in charges.get(c, []):
        in_basis = r in db
        print(f"  q3={c}, ray {r}: in divisor_basis = {in_basis}")

# Kaehler cone & J*
tip = cytools.math.Cone.tip_of_stretched_cone(cy.toric_kahler_cone(), 1.0, ndiv)
vol_tip = cy.compute_cy_volume(list(tip))
kap3 = 1.0/4096.0
scale = (kap3 / vol_tip) ** (1.0/3.0)
t_star = [x * scale for x in tip]
vol_star = cy.compute_cy_volume(list(t_star))
print(f"\nJ* (uniform, 32D):")
print(f"  Scale: {scale:.6f}, Vol={vol_star:.6e} (target={kap3:.6e})")
print(f"  t[0] = {t_star[0]:.6f}")

# Check kappa vector - which divisors have non-zero volumes
kv = np.array(cy.compute_kappa_vector(list(t_star)))
print(f"\nKappa vector (divisor volumes at J*)")
print(f"  min={kv.min():.4e}, max={kv.max():.4e}")

# Map basis back to rays if possible
print(f"\nAll 37 rays: indices 0-36")
print(f"q3=5 rays: {q5}")
print(f"q3=7 rays: {q7}")
print(f"\nConclusion: q3=5 and q3=7 rays {'' if any(r in db for r in q5) else 'NOT'} in 32D divisor basis")
print(f"Need full 36D for complete charge-5×charge-7 intersection analysis")
