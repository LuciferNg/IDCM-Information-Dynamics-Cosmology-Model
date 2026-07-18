#!/usr/bin/env python3
"""IDCM Validation v4: Kuramoto Synchronization"""
import numpy as np
phi = (1+5**0.5)/2; eps = phi**(-1)/4; kap = 1/16
c_star = (np.sqrt(5)-1)/2

print("="*60)
print("v4_kuramoto.py — SYNC Synchronization")
print("="*60)

N = 10
np.random.seed(42)
C = np.random.random(N) * 2
print(f"Initial max|C-C*|: {max(abs(C-c_star)):.4f}")

converged = False
for t in range(500):
    C_old = C.copy()
    for i in range(N):
        neighbors = [(i-1)%N, (i+1)%N]
        sync = eps * sum(C_old[j] - C_old[i] for j in neighbors)
        relax = kap * (c_star - C_old[i])
        C[i] = C_old[i] + sync + relax
    
    residual = max(abs(C-c_star))
    if t % 50 == 0 or t < 3:
        print(f"  t={t:3d}: max|C-C*|={residual:.6e}")
    if residual < 1e-10:
        print(f"  t={t:3d}: CONVERGED (residual={residual:.2e})")
        converged = True
        break

if not converged:
    print(f"  Final (t=499): max|C-C*|={max(abs(C-c_star)):.6e}")

print(f"\nC* = {c_star:.6f}")
print(f"Final C: mean={np.mean(C):.6f}, max|C-C*|={max(abs(C-c_star)):.2e}")
print(f"Verified: {'YES' if converged else 'PARTIAL'}")
print("="*60)
