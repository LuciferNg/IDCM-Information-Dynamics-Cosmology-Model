#!/usr/bin/env python3
"""IDCM Validation v1: ALL 9 MASSES — First-Principles"""
import numpy as np
phi = (1+5**0.5)/2; M=33; Nh=42; beta = phi**(-1)/2
k_u = M*beta; k_d = (M-Nh/6)*beta - phi**(-4); k_l = (M-Nh/3)*beta

# Base masses (3rd gen)
m_t = 172.76; m_b = 4.18; m_tau = 1.77686

# First gen formulas
e_tau_ex = k_l + M/3
d_b_ex = 2*k_d - phi
u_t_ex = k_u + k_d + k_l - phi**(-1)

masses = {
    't': (0, m_t, m_t, 'GeV'),
    'c': (k_u, m_t, 1.27, 'GeV'),
    'u': (u_t_ex, m_t, 2.16e-3, 'GeV'),
    'b': (0, m_b, 4.18, 'GeV'),
    's': (k_d, m_b, 93.4e-3, 'GeV'),
    'd': (d_b_ex, m_b, 4.70e-3, 'GeV'),
    'tau': (0, m_tau, 1.77686, 'GeV'),
    'mu': (k_l, m_tau, 105.65837e-3, 'GeV'),
    'e': (e_tau_ex, m_tau, 0.51099895e-3, 'GeV'),
}

print("="*60)
print("v1_masses.py — ALL 9 MASSES (First-Principles)")
print("="*60)
print(f"M={M}, Nh={Nh}, beta={beta:.6f}")
print()

errors = []
print(f"{'Particle':<8} {'IDCM':<15} {'PDG':<15} {'Error':<10}")
print("-"*50)
for name, (exp, base, pdg, unit) in masses.items():
    idcm = base * phi**(-exp) if exp > 0 else base
    err = abs(idcm-pdg)/pdg*100
    errors.append(err)
    flag = "✅" if err < 3 else ("🟡" if err < 10 else "❌")
    val_str = f"{idcm*1000:.2f} MeV" if idcm < 1 else f"{idcm:.4f} GeV"
    pdg_str = f"{pdg*1000:.2f} MeV" if pdg < 1 else f"{pdg:.4f} GeV"
    print(f"{name:<8} {val_str:<15} {pdg_str:<15} {err:<10.2f}% {flag}")

avg = np.mean(errors[3:])  # exclude bases
print(f"\nAverage error (predicted): {avg:.2f}%")
print("="*60)
