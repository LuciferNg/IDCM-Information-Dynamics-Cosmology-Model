#!/usr/bin/env python3
"""IDCM Validation v1: CKM — New First-Principles Formulas"""
import numpy as np
phi = (1+5**0.5)/2; M=33; beta = phi**(-1)/2

V_us = phi**(-M/11)  # = phi^(-3)
V_cb = phi**(-M/5)   # = phi^(-6.6)
V_ub = phi**(-(M/5 + M/11 + phi**(-1)/beta))  # = phi^(-11.6)
delta_CP = np.pi/2 - np.arctan(beta)

# Jarlskog from standard param
s12 = V_us / np.sqrt(1 + V_us**2)
s23 = V_cb / np.sqrt(1 + V_cb**2)
s13 = V_ub
J = s12 * s23 * s13 * np.sin(delta_CP)

print("="*60)
print("v1_ckm.py — FIRST-PRINCIPLES CKM")
print("="*60)
print(f"Formulas: V_us = phi^(-M/11), V_cb = phi^(-M/5)")
print(f"          V_ub = phi^(-(M/5+M/11+2))")
print(f"          delta = pi/2 - arctan(beta)")
print()

data = [
    ("V_us", V_us, 0.22650),
    ("V_cb", V_cb, 0.04210),
    ("V_ub", V_ub, 0.00361),
    ("delta_CP", np.degrees(delta_CP), 68.80),
    ("Jarlskog J", J, 3.08e-5),
]

print(f"{'Param':<12} {'IDCM':<15} {'PDG':<15} {'Error':<10}")
print("-"*52)
for name, idcm, pdg in data:
    err = abs(idcm-pdg)/pdg*100
    flag = "✅" if err < 5 else ("🟡" if err < 20 else "❌")
    unit = "°" if name == "delta_CP" else ""
    print(f"{name:<12} {idcm:<15.5e} {pdg:<15.5e} {err:<10.2f}% {flag}")

print(f"\n=== OLD VS NEW COMPARISON ===")
print(f"{'Param':<12} {'Old IDCM':<12} {'New IDCM':<12} {'PDG':<12}")
print("-"*48)
for name, new_val, pdg in [(n, v, p) for n, v, p in data[:3]]:
    old_val = {'V_us': phi**(-3), 'V_cb': phi**(-7), 'V_ub': phi**(-10)}[name]
    print(f"{name:<12} {old_val:<12.4f} {new_val:<12.4f} {pdg:<12.4f}")

print("="*60)
