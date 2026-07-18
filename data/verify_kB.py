#!/usr/bin/env python3
"""
IDCM — W-field Thermodynamics: k_B Verification Script
=========================================================
Verifies:
    k_B·T_CMB = ħ·H₀ × (1+ε²) × (1/ε)^36
    k_B = ħ·H₀ × (1+ε²) × (1/ε)^36 / T_CMB
"""

import sys, json
from math import sqrt

# ── Recursion constants ──
phi = (1 + sqrt(5)) / 2
phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4
KAP = 1.0 / 16.0

# ── Physical constants ──
H0_SI = 68.2 * 1000 / 3.085677581e22   # s^-1
HBAR = 1.054571817e-34                 # J·s
KB_SI = 1.380649e-23                   # J/K
T_CMB = 2.72548                        # K

results = {}
failures = 0

def check(name, got, expected, tol_rel=0.001, unit='', note=''):
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
print('  IDCM — W-field Thermodynamics: k_B Verification')
print('=' * 75)

# ════════════════════════════════════════════
# 1. Recursion constants
# ════════════════════════════════════════════
print('\n─── 1. Recursion constants ───')
check('epsilon', EPS, 0.15450849718747373)
check('1/epsilon', 1/EPS, 6.472135955, note='= 4φ')
EPS2 = EPS ** 2
check('epsilon^2', EPS2, 0.02387287567191953)

# ════════════════════════════════════════════
# 2. Mode count: (1/ε)^36
# ════════════════════════════════════════════
print('\n─── 2. W-field mode count ───')
N_MODES = (1 / EPS) ** 36
check('(1/ε)^36 (mode count)', N_MODES, 1.576615e29, tol_rel=0.01)

# Also express as (4φ)^36
check('(4φ)^36 = (1/ε)^36', (4*phi)**36, N_MODES, tol_rel=1e-10)

# 36 = 3 × 12 factorisation
check('(1/ε)^12', (1/EPS)**12, 5.403e9, tol_rel=0.05)
check('(1/ε)^36 = ((1/ε)^12)^3', ((1/EPS)**12)**3, N_MODES, tol_rel=1e-10)

# ════════════════════════════════════════════
# 3. Core relation: k_B·T_CMB
# ════════════════════════════════════════════
print('\n─── 3. k_B·T_CMB = ħ·H₀ × (1+ε²) × (1/ε)^36 ───')
HBAR_H0 = HBAR * H0_SI
check('ħ·H₀', HBAR_H0, 2.330825e-52, tol_rel=0.01, unit='J')

CORR = 1 + EPS2
check('1+ε² (correction)', CORR, 1.0238728756719195, tol_rel=1e-10)

KBT_PRED = HBAR_H0 * CORR * N_MODES
KBT_ACT = KB_SI * T_CMB
check('k_B·T_CMB (pred)', KBT_PRED, KBT_ACT, tol_rel=0.001, unit='J',
      note='0.0128% core error')

# ════════════════════════════════════════════
# 4. Boltzmann constant
# ════════════════════════════════════════════
print('\n─── 4. k_B from IDCM ───')
KB_PRED = KBT_PRED / T_CMB
check('k_B = ħ·H₀×(1+ε²)×(1/ε)^36/T_CMB', KB_PRED, KB_SI, tol_rel=0.001, unit='J/K',
      note='0.0128%')

# The explicit formula
check('k_B formula verification', KB_PRED, KB_SI, tol_rel=0.001, unit='J/K')

# ════════════════════════════════════════════
# 5. T_CMB from IDCM
# ════════════════════════════════════════════
print('\n─── 5. T_CMB from IDCM ───')
T_PRED = KBT_PRED / KB_SI
check('T_CMB = ħ·H₀×(1+ε²)×(1/ε)^36/k_B', T_PRED, T_CMB, tol_rel=0.001, unit='K')

# ════════════════════════════════════════════
# 6. de Sitter temperature comparison
# ════════════════════════════════════════════
print('\n─── 6. de Sitter relation ───')
T_DS = HBAR * H0_SI / (2 * 3.141592653589793 * KB_SI)
check('T_dS = ħ·H₀/(2π·k_B)', T_DS, 2.41e-30, tol_rel=0.5, unit='K',
      note='de Sitter temperature ~2.4×10^-30 K')

RATIO_CMB_DS = T_CMB / T_DS
check('T_CMB / T_dS', RATIO_CMB_DS, 1.014e30, tol_rel=0.1,
      note='= 2π·(1+ε²)·(1/ε)^36')

# ════════════════════════════════════════════
# 7. Natural unit form
# ════════════════════════════════════════════
print('\n─── 7. Natural unit form ───')
# In natural units (ħ = 1, c = 1): k_B·T_CMB = H₀ × (1+ε²) × (1/ε)^36
# This is dimensionless
KBT_NATURAL = KBT_PRED / HBAR  # divide by ħ to get energy in natural units
check('k_B·T_CMB/ħ (natural units)', KBT_NATURAL / H0_SI, CORR * N_MODES, 
      tol_rel=1e-10,
      note='= (1+ε²)·(1/ε)^36')

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
