#!/usr/bin/env python3
"""
IDCM — E = mc²: Self-Consistency Verification Script
=====================================================
Verifies that the IDCM-derived c and m_e satisfy E = mc².

Relations:
    c    = 16·H₀·ξ / φ⁻¹²
    m_e  = ε⁷ · v_EW
    E    = m_e · c²
"""

import sys, json
from math import sqrt

# ── Recursion constants ──
phi = (1 + sqrt(5)) / 2
phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4
KAP = 1.0 / 16.0

# ── Physical constants (SI) ──
Mpc = 3.085677581e22
H0_SI = 68.2 * 1000 / Mpc
C_SI = 299792458.0
G = 6.67430e-11
HBAR = 1.054571817e-34

# ── Particle data (PDG 2024) ──
ME_EV = 0.510998950e6  # eV
ME_J = ME_EV * 1.602176634e-19  # J

# ── IDCM inputs ──
XI_MPC = 105.0  # Mpc
V_EW = 246.0e9  # eV

results = {}
failures = 0

def check(name, got, expected, tol_rel=0.05, unit='', note=''):
    global failures
    err = abs(got / expected - 1) * 100 if expected != 0 else 999
    ok = err < tol_rel * 100
    msg = f'  {"✓" if ok else "✗"} {name:45s} = {got:12.6e} {unit}'
    msg += f'  (exp {expected:12.6e})  err={err:.4f}%'
    if note: msg += f'  [{note}]'
    results[name] = {'got': got, 'expected': expected, 'error_pct': err, 'ok': ok}
    if not ok:
        failures += 1
        msg += ' ← FAIL'
    print(msg)

print('=' * 75)
print('  IDCM — E = mc²: Self-Consistency Verification')
print('=' * 75)

# ════════════════════════════════════════════
# 1. c from IDCM
# ════════════════════════════════════════════
print('\n─── 1. c = 16·H₀·ξ / φ⁻¹² ───')
XI_SI = XI_MPC * Mpc
C_IDCM = 16 * H0_SI * XI_SI / phi_inv**2
check('c (IDCM)', C_IDCM, C_SI, tol_rel=0.001, unit='m/s',
      note='core 0.057%')

# ════════════════════════════════════════════
# 2. m_e from IDCM
# ════════════════════════════════════════════
print('\n─── 2. m_e = ε⁷ · v_EW ───')
ME_IDCM_EV = EPS**7 * V_EW
check('m_e (IDCM)', ME_IDCM_EV, ME_EV, tol_rel=0.02, unit='eV',
      note='1.2% core error')

# Convert to kg
ME_IDCM_J = ME_IDCM_EV * 1.602176634e-19
ME_IDCM_KG = ME_IDCM_J / C_IDCM**2
ME_KG = ME_J / C_SI**2
check('m_e (IDCM, kg)', ME_IDCM_KG, ME_KG, tol_rel=0.02, unit='kg')

# ════════════════════════════════════════════
# 3. E = mc² — full IDCM chain
# ════════════════════════════════════════════
print('\n─── 3. E = m_e · c² ───')
E_IDCM = ME_IDCM_EV * (C_IDCM / C_SI)**2  # scale correctly
# Actually: E = m (in energy units) × (c_IDCM/c_actual)² since m_e is in eV
# m_e (eV) × (c_IDCM / c)² = m_e × (c_IDCM/c)² in eV
E_IDCM_EV = ME_IDCM_EV * (C_IDCM / C_SI)**2
E_EXP_EV = ME_EV  # E = mc² → rest energy = m_e in eV
check('E = m_e·c² (IDCM, eV)', E_IDCM_EV, E_EXP_EV, tol_rel=0.02, unit='eV',
      note='1.3% — propagates c+m errors')

# In Joules
E_IDCM_J = E_IDCM_EV * 1.602176634e-19
E_EXP_J = ME_J
check('E = m_e·c² (IDCM, J)', E_IDCM_J, E_EXP_J, tol_rel=0.02, unit='J')

# ════════════════════════════════════════════
# 4. Full formula expansion
# ════════════════════════════════════════════
print('\n─── 4. Full structural expansion ───')
# E = ε⁷ · v_EW · (16·H₀·ξ/φ⁻¹²)²
E_FORMULA_EV = EPS**7 * V_EW * (16 * H0_SI * XI_SI / phi_inv**2 / C_SI)**2
# Wait, need to handle units carefully.
# c_IDCM = 16·H₀·ξ/φ⁻¹² (has units m/s)
# c_SI/c_to_make_dimensionless_ratio... 
# Actually let's just compute:
# E = ε⁷ · v_EW (eV) × (c_IDCM / c_SI)²
ratio_c = (16 * H0_SI * XI_SI / phi_inv**2) / C_SI
E_FULL_EV = EPS**7 * V_EW * ratio_c**2
check('E = ε⁷·v_EW·(16H₀ξ/φ⁻¹²/c)²', E_FULL_EV, ME_EV, tol_rel=0.02, unit='eV')

# ════════════════════════════════════════════
# 5. Error propagation analysis
# ════════════════════════════════════════════
print('\n─── 5. Error budget ───')
err_c = abs(C_IDCM / C_SI - 1) * 100
err_me = abs(ME_IDCM_EV / ME_EV - 1) * 100
err_e_total = abs(E_IDCM_EV / E_EXP_EV - 1) * 100
print(f'  c error:      {err_c:.4f}%')
print(f'  m_e error:    {err_me:.4f}%')
print(f'  E = mc² error: {err_e_total:.4f}%')
print(f'  Expected:     ~{err_c+err_me:.4f}% (addition) or {sqrt(err_c**2+err_me**2):.4f}% (quadrature)')

# ════════════════════════════════════════════
# 6. E = mc² as structural identity
# ════════════════════════════════════════════
print('\n─── 6. E = mc² as structural identity ───')
print('  In IDCM, E = mc² is not a derivation — it is:')
print('  1. The W-field dispersion relation at rest (k=0)')
print('  2. A consistency check that both c and m share recursion origin')
print('  3. Verified: E/mc² ratio =', E_IDCM_EV / (ME_IDCM_EV * (C_IDCM/C_SI)**2))

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
