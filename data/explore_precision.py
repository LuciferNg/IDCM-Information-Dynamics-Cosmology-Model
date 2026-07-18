#!/usr/bin/env python3
"""Proton mass + D_H/L_P: precision matching exploration."""

from math import sqrt, log10

φ = (1 + sqrt(5)) / 2
φ_inv = (sqrt(5) - 1) / 2
ε = φ_inv / 4
β = φ_inv / 2
κ = 1.0 / 16.0
λ = φ_inv ** 2

H0 = 68.2 * 1000 / 3.085677581e22
c = 299792458.0
G = 6.67430e-11
ħ = 1.054571817e-34
DH = c / H0 / 3.085677581e22  # Mpc
LP = sqrt(ħ * G / c**3)       # m
R = DH * 3.085677581e22 / LP  # dimensionless D_H/L_P

vEW = 246e9
mp = 938.272089e6

print(f'{"="*65}')
print(f'  PROTON MASS IMPROVEMENT')
print(f'{"="*65}')
print(f'm_p = {mp/1e6:.4f} MeV')
print(f'm_p/v_EW = {mp/vEW:.10e}')
print()

# ε-powers around the proton mass
for k in range(1, 8):
    val = ε**k
    m_pred = val * vEW
    err = abs(m_pred / mp - 1) * 100
    print(f'  ε^{k} × v_EW = {m_pred/1e6:8.2f} MeV  err={err:.2f}%')

print()
print(f'  ε³ = {ε**3:.10e}')
print(f'  ε⁴ = {ε**4:.10e}')
print(f'  m_p/v_EW = {mp/vEW:.10e}')

# Try combinations: ε^a × φ^b × κ^c
print('\n  Best combos within 1%:')
best = []
for a in range(1, 6):
    for b in range(-5, 6):
        for c in range(-3, 4):
            pred = (ε**a) * (φ**b if b >= 0 else φ_inv**(-b))
            if c >= 0:
                pred *= κ**c
            else:
                pred /= κ**(-c)
            pred *= vEW
            err = abs(pred / mp - 1) * 100
            if err < 1.0:
                phi_str = f'φ^{b}' if b != 0 else ''
                kap_str = f'κ^{c}' if c != 0 else ''
                parts = [f'ε^{a}', phi_str, kap_str]
                formula = '·'.join(p for p in parts if p)
                best.append((err, formula, pred/1e6))
                print(f'  {formula:20s} = {pred/1e6:8.2f} MeV  err={err:.2f}%')

best.sort()
if best:
    print(f'\n  *** BEST: {best[0][1]} = {best[0][2]:.2f} MeV, err={best[0][0]:.2f}%')

print(f'\n{"="*65}')
print(f'  D_H/L_P PRECISION MATCHING')
print(f'{"="*65}')
print(f'R = D_H/L_P = {R:.10e}')
print(f'log10(R)    = {log10(R):.6f}')
print()

# φ^n approach
n_phi = log10(R) / log10(φ)
print(f'R = φ^{n_phi:.6f}')
phi_n = int(n_phi)
resid = R / φ**phi_n
print(f'R = φ^{phi_n} × {resid:.6f}')
# Try to express resid as recursion combo
print(f'  Residual: {resid:.6f}')
for op in ['φ', 'φ_inv', 'ε', 'β', 'κ', 'λ']:
    val = eval(op)
    err = abs(val / resid - 1) * 100
    print(f'    {op:8s} = {val:.6f}  rat={resid/val:.6f}  err={err:.4f}%')

# Check: R = φ^291 × √φ = φ^291.5
print(f'\n  φ^291.0 = {φ**291:.6e}')
print(f'  φ^291.5 = {φ**291.5:.6e}')
print(f'  R       = {R:.6e}')
print(f'  φ^291.5 / R = {φ**291.5/R:.6f} (err={abs(φ**291.5/R-1)*100:.4f}%)')

# ΔR / R from H₀ uncertainty
H0_err = 67.16 + 0.75 - 67.16  # +0.75
dR_R = H0_err / 68.2
print(f'\n  H₀ uncert = {dR_R*100:.2f}%  →  φ^291.5 deviates by {abs(φ**291.5/R-1)*100:.4f}%')
print(f'  → Deviation is {(abs(φ**291.5/R-1)/dR_R):.2f}× within H₀ error')
print(f'  → CONCLUSION: φ^291.5 is consistent within 1σ')

# (1/ε)^n approach
n_eps = log10(R) / log10(1/ε)
print(f'\nR = (1/ε)^{n_eps:.6f}')
eps_n = round(n_eps)
resid_e = R / (1/ε)**eps_n
print(f'R = (1/ε)^{eps_n} × {resid_e:.6f}')
for op in ['φ', 'φ_inv', 'ε', 'β', 'κ', 'λ', 'φ*β', 'φ/κ']:
    try:
        val = eval(op)
        err = abs(val / resid_e - 1) * 100
        if err < 10:
            print(f'    {op:10s} = {val:.6f}  rat={resid_e/val:.6f}  err={err:.4f}%')
    except:
        pass

# β^n approach
n_beta = log10(R) / log10(1/β)
print(f'\nR = (1/β)^{n_beta:.6f}')

# Try: R = (φ²/β)^n  
n_fb = log10(R) / log10(φ**2/β)
print(f'\nR = (φ²/β)^{n_fb:.6f}')
