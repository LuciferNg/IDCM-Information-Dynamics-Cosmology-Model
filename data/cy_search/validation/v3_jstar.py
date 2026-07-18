#!/usr/bin/env python3
"""IDCM Validation v3: J* Fixed Point"""
import numpy as np, json
phi = (1+5**0.5)/2; kap = 1/16

print("="*60)
print("v3_jstar.py — J* Fixed Point")
print("="*60)

with open('../data/Jstar_36D.json') as f:
    data = json.load(f)
J = np.array(data['Jstar_36D'])

print(f"J* dimensions: {len(J)}")
print(f"Vol(J*) = {data['Vol']:.6e}")
print(f"Target: Vol = kap^3 = {kap**3:.6e}")
vol_match = abs(data['Vol'] - kap**3)/kap**3*100
print(f"Vol match: {vol_match:.2f}%")
print(f"Ind(J*) = {data['Ind']:.4f}")
print(f"Target: Ind = 48")
ind_match = abs(data['Ind']-48)/48*100
print(f"Ind match: {ind_match:.2f}%")
print(f"J* top 5: {[f'{x:.4f}' for x in J[np.argsort(-J)[:5]]]}")
print(f"Pass: {'YES' if vol_match < 1 and ind_match < 1 else 'NO'}")
print("="*60)
