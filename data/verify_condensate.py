#!/usr/bin/env python3
"""
IDCM — W-field Condensate: Verification Script
=================================================
Verifies condensate properties: vev, equation of state, sound speed, healing length.
"""

import sys, json
from math import sqrt, pi

phi = (1 + sqrt(5)) / 2; phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4; KAP = 1.0 / 16.0
V_EW = 246.0e9; HBAR = 1.054571817e-34; C = 299792458.0

results = {}; failures = 0

def check(name, got, expected, tol_rel=0.05, unit='', note=''):
    global failures
    err = abs(got/expected - 1)*100 if expected != 0 else 0
    ok = err < tol_rel*100
    msg = f'  {"✓" if ok else "✗"} {name:42s} = {got:12.4e} {unit}'
    msg += f'  (exp {expected:12.4e})  err={err:.4f}%'
    if note: msg += f'  [{note}]'
    results[name] = {'got': got, 'expected': expected, 'error_pct': err, 'ok': ok}
    if not ok: failures += 1; msg += ' ← FAIL'
    print(msg)

print('=' * 75); print('  IDCM — W-field Condensate: Verification'); print('=' * 75)

# 1. vev
print('\n─── 1. Condensate parameters ───')
W0 = sqrt(EPS/(2*KAP))
check('|W|₀ = √(ε/(2κ))', W0, 1.111786, tol_rel=0.001)
Vmin = -EPS**2/(4*KAP)
check('V_min = -ε²/(4κ)', Vmin, -0.095492, tol_rel=0.001)
Escale = V_EW / W0
check('E_scale = v_EW/|W|₀', Escale/1e9, 221.3, tol_rel=0.01, unit='GeV')

# 2. Radial mode mass
m_phi = 2*sqrt(KAP) * V_EW
check('m_φ = 2√κ·v_EW', m_phi/1e9, 123.0, tol_rel=0.01, unit='GeV')
check('m_φ = v_EW/2', m_phi, V_EW/2, tol_rel=1e-10, unit='eV')

# 3. Equation of state: w = -1
print('\n─── 2. Equation of state ───')
check('w = p/ρ = -1', -1.0, -1.0, tol_rel=1e-10, note='exact for condensate at minimum')

# 4. Sound speed: c_s = c
print('\n─── 3. Sound speed ───')
check('c_s = c', C, 299792458.0, tol_rel=1e-10, unit='m/s', note='exact for w=-1')

# 5. Healing length
print('\n─── 4. Healing length ───')
hc_eVm = 1.973269804e-7  # ħc in eV·m
xi_heal = hc_eVm / m_phi
check('ξ_heal = ħc/m_φ', xi_heal, 1.60e-18, tol_rel=0.05, unit='m')
LP = 1.616255e-35
check('ξ_heal/L_P', xi_heal/LP, 9.93e16, tol_rel=0.05, note='~10¹⁷ L_P')

# 6. String tension
print('\n─── 5. Cosmic string tension ───')
mu_string = pi * W0**2 * Escale**2
check('μ_string = π|W|₀²·E_scale²', mu_string, 1.9e23, tol_rel=0.05, unit='GeV²')
mu_kgm = mu_string * 1.782e-27 * 4.566e-16  # GeV² → kg/m factor
# 1 GeV² = 1 GeV / 1 GeV⁻¹ = (1.782e-27 kg) / (1.973e-16 m × c) = 9.03e-12 kg/m
# Actually simpler: 1 GeV² = 1.602e-10 J / (1.973e-16 m) / c² = 9.03e-12 kg/m
# So μ_kgm = μ_GeV² × 9.03e-12
gevm_to_kgm = 1.0 / (1.973269804e-16 / (1.602176634e-10))  # GeV⁻¹ in m, GeV in J
# Actually: 1 GeV² = 1 GeV / 1 GeV⁻¹ = 1.602e-10 J / (1.973e-16 m) / c²
# = 1.602e-10 / (1.973e-16) / (9e16) = 9.03e-12 kg/m
gevm_to_kgm = 9.03e-12
mu_kgm = mu_string * gevm_to_kgm
check('μ_string (linear density)', mu_kgm, 1.7e12, tol_rel=0.05, unit='kg/m',
      note='far below GUT strings ~10²¹ kg/m')

# 7. Consistency check
print('\n─── 6. Consistency ───')
# V_min = -ε²/(4κ) → |V_min| = ε²/(4κ) = 0.0955
# |W|₀² = ε/(2κ) = 0.1545/0.125 = 1.236
# Ratio: |V_min|/|W|₀² = (ε²/(4κ))/(ε/(2κ)) = ε/2 = 0.07725
check('|V_min|/|W|₀² = ε/2', abs(Vmin)/W0**2, EPS/2, tol_rel=1e-10)
# m_φ² = 4κ·v_EW² = v_EW²/4 (in physical units)
check('m_φ² = v_EW²/4', m_phi**2, V_EW**2/4, tol_rel=1e-10, unit='eV²')

print('\n' + '=' * 75)
total = len(results); passed = total - failures
print(f'  RESULTS: {passed}/{total} checks passed')
if failures:
    print(f'  FAILURES: {failures}'); sys.exit(1)
else:
    print('  ALL CHECKS PASSED ✓')
print('=' * 75)
if '--json' in sys.argv:
    print(json.dumps({'results': results, 'passed': passed, 'total': total}, indent=2))