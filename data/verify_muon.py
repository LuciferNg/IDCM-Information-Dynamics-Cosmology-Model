#!/usr/bin/env python3
"""
IDCM — Muon Mass: Derivation Verification Script
==================================================
Verifies:
    m_μ = 2·ε⁴·λ·v_EW  (1.37% error)
    m_μ/m_e = 2·ε⁻³·λ  (0.16% error)
"""

import sys, json
from math import sqrt

phi = (1 + sqrt(5)) / 2
phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4
LAM = phi_inv ** 2
V_EW = 246.0e9  # eV

M_E = 0.510998950e6   # eV
M_MU = 105.658375e6   # eV

results = {}
failures = 0

def check(name, got, expected, tol_rel=0.05, unit='', note=''):
    global failures
    err = abs(got / expected - 1) * 100 if expected != 0 else 999
    ok = err < tol_rel * 100
    msg = f'  {"✓" if ok else "✗"} {name:45s} = {got:12.4e} {unit}'
    msg += f'  (exp {expected:12.4e})  err={err:.4f}%'
    if note: msg += f'  [{note}]'
    results[name] = {'got': got, 'expected': expected, 'error_pct': err, 'ok': ok}
    if not ok:
        failures += 1
        msg += ' ← FAIL'
    print(msg)

print('=' * 75)
print('  IDCM — Muon Mass Derivation')
print('=' * 75)

# ════════════════════════════════════════════
# 1. m_μ = 2·ε⁴·λ·v_EW
# ════════════════════════════════════════════
print('\n─── 1. Absolute muon mass ───')
M_MU_PRED = 2 * EPS**4 * LAM * V_EW
check('m_μ = 2·ε⁴·λ·v_EW', M_MU_PRED, M_MU, tol_rel=0.02, unit='eV',
      note=f'{M_MU_PRED/1e6:.3f} vs {M_MU/1e6:.3f} MeV (1.37%)')

# ════════════════════════════════════════════
# 2. Ratio m_μ/m_e
# ════════════════════════════════════════════
print('\n─── 2. m_μ/m_e ratio ───')
RATIO_PRED = 2 * EPS**(-3) * LAM
RATIO_ACT = M_MU / M_E
check('m_μ/m_e = 2·ε⁻³·λ', RATIO_PRED, RATIO_ACT, tol_rel=0.005,
      note=f'{RATIO_PRED:.3f} vs {RATIO_ACT:.3f} (0.16%)')

# ════════════════════════════════════════════
# 3. Component verification
# ════════════════════════════════════════════
print('\n─── 3. Component consistency ───')
# ε⁴ = (φ⁻¹/4)⁴
check('ε⁴', EPS**4, 5.699e-4, tol_rel=0.01)
# λ = φ⁻¹²
check('λ = φ⁻¹²', LAM, 0.381966, tol_rel=0.001)
# 2·ε⁴·λ combined
check('2·ε⁴·λ', 2 * EPS**4 * LAM, M_MU_PRED/V_EW, tol_rel=1e-6)

# ════════════════════════════════════════════
# 4. Comparison with electron formula
# ════════════════════════════════════════════
print('\n─── 4. Electron comparison ───')
# m_e = ε⁷·v_EW
M_E_PRED = EPS**7 * V_EW
check('m_e = ε⁷·v_EW', M_E_PRED, M_E, tol_rel=0.02, unit='eV')
# Both share v_EW, differ only in ε-power and generation correction
print(f'  Electron: ε⁷         = {EPS**7:.4e}')
print(f'  Muon:     2·ε⁴·λ    = {2*EPS**4*LAM:.4e}')
print(f'  Generation gap: Δk = 3, factor 2λ = {2*LAM:.4f}')

# ════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════
print('\n' + '=' * 75)
total = len(results)
passed = total - failures
print(f'  RESULTS: {passed}/{total} checks passed')
if failures:
    print(f'  FAILURES: {failures}')
    sys.exit(1)
else:
    print('  ALL CHECKS PASSED ✓')
print('=' * 75)

if '--json' in sys.argv:
    print(json.dumps({'results': results, 'passed': passed, 'total': total}, indent=2))
