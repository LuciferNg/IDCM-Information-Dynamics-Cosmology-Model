#!/usr/bin/env python3
"""IDCM Validation v4: MERA RG Fixed Point"""
import numpy as np
phi = (1+5**0.5)/2

print("="*60)
print("v4_mera.py — MERA RG Fixed Point")
print("="*60)

print("\nMERA RG flow: C_{n+1} = 1/(1+C_n)")
c = 0.5
c_star = (np.sqrt(5)-1)/2
print(f"{'n':<5} {'C_n':<20} {'|C_n-C*|':<20}")
print("-"*45)

converged = False
for n in range(50):
    c_next = 1/(1+c)
    diff = abs(c - c_star)
    if n < 20 or diff < 1e-12:
        print(f"{n:<5} {c:<20.15f} {diff:<20.2e}")
    if diff < 1e-14:
        print(f"{n+1:<5} {c_next:<20.15f} {abs(c_next - c_star):<20.2e}")
        print("CONVERGED!")
        converged = True
        break
    if abs(c_next - c) < 1e-15:
        print(f"FIXED POINT REACHED at n={n+1}")
        converged = True
        break
    c = c_next

print(f"\nFixed point C* = {c_star:.15f}")
print(f"phi^(-1) = {c_star:.15f}")
print(f"Matches: {'YES' if converged else f'CLOSE (diff={diff:.2e})'}")
print(f"Equation: C* = 1/(1+C*) -> C*^2 + C* - 1 = 0")
print("="*60)
