# 執行輸出：pmns_from_kappa.py

**日期：** 2026-07-20
**腳本：** `~/IDCM/pmns_from_kappa.py`
**狀態：** ✅ EXIT=0

```
/tmp/cy_venv/lib/python3.11/site-packages/cytools/config.py:151: UserWarning: 
**************************************************************
Warning: You have enabled experimental features of CYTools.
Some of these features may be broken or not fully tested,
and they may undergo significant changes in future versions.
**************************************************************

  warnings.warn(
/home/wsl/IDCM/pmns_from_kappa.py:64: RuntimeWarning: invalid value encountered in scalar divide
  s12 = abs(U[0,1]) / math.sqrt(abs(U[0,0])**2 + abs(U[0,1])**2)
/home/wsl/IDCM/pmns_from_kappa.py:65: RuntimeWarning: invalid value encountered in scalar divide
  s23 = abs(U[1,2]) / math.sqrt(abs(U[1,1])**2 + abs(U[1,2])**2)
========================================================================
  PMNS FROM CY₃(36,98) SEESAW DIAGONALIZATION
========================================================================

  Neutrino mass eigenvalues (eV):
    ν_1: m = -7.255098e-05 (|m| = 7.255098e-05)
    ν_2: m = -1.466894e-03 (|m| = 1.466894e-03)
    ν_3: m = -6.209509e-03 (|m| = 6.209509e-03)

  Δm²_21 = 2.1465e-06 eV² (PDG: 7.39e-5)
  Δm²_32 = 3.6406e-05 eV² (PDG: 2.51e-3)

  PMNS mixing matrix (U):
    [ +0.0000   +0.0000   +1.0000]
    [ +1.0000   +0.0000   +0.0000]
    [ +0.0000   +1.0000   +0.0000]

  Mixing angles:
    θ₁₂ = 0.00° (PDG: 33.82°)
    θ₂₃ = 0.00° (PDG: ~43°)
    θ₁₃ = 90.00° (PDG: 8.57°)
    δ_CP = 0° (PDG: ~195°)

  Jarlskog invariant:
    J_CP = 0.000000

========================================================================
  vs IDCM STRUCTURAL PMNS PREDICTION
========================================================================

  Angle      CY₃ Seesaw      IDCM formula    PDG             Status    
  ────────── ─────────────── ─────────────── ─────────────── ──────────
  θ₁₂        0.00            33.45           33.82           🔴         
  θ₂₃        0.00            45.00           43.20           🔴         
  θ₁₃        90.00           8.62            8.57            🔴         

========================================================================
  κ_VECTOR → MIXING HEURISTIC
========================================================================

  κ_vector relative magnitudes (q=6 sector):
    D_7: Y_rel = -0.3528, φ-exp = 2.17
    D_8: Y_rel = -0.0102, φ-exp = 9.53
    D_9: Y_rel = -0.2282, φ-exp = 3.07
    D_21: Y_rel = -0.0119, φ-exp = 9.20

  Mixing from φ-exp differences:
    D_7↔D_9: Δφ = 0.90, sinθ ≈ φ^-Δφ = 0.6470, θ ≈ 40.3°
    D_7↔D_8: Δφ = 7.36, sinθ ≈ φ^-Δφ = 0.0289, θ ≈ 1.7°
    D_9↔D_21: Δφ = 6.13, sinθ ≈ φ^-Δφ = 0.0524, θ ≈ 3.0°

========================================================================
  PMNS MASS ORDERING DIAGNOSTIC
========================================================================

  U_ei (ν_e content of each mass state):
    |U_e1|² = 0.0000  (0.0%)
    |U_e2|² = 0.0000  (0.0%)
    |U_e3|² = 1.0000  (100.0%)

  U_μi (ν_μ content):
    |U_μ1|² = 1.0000  (100.0%)
    |U_μ2|² = 0.0000  (0.0%)
    |U_μ3|² = 0.0000  (0.0%)

  U_τi (ν_τ content):
    |U_τ1|² = 0.0000  (0.0%)
    |U_τ2|² = 1.0000  (100.0%)
    |U_τ3|² = 0.0000  (0.0%)

  Mass ordering: Normal
    m₁=7.2551e-05, m₂=1.4669e-03, m₃=6.2095e-03

========================================================================
  NEXT: INSTANTON M_R CORRECTION
========================================================================

  Target M_R for m_ν₃=0.048eV: 1.60e+15 GeV
  Current M_R from κ tensor: 1.24e+16 GeV
  Reduction needed: ×0.129

  Single instanton correction q/(1-q) = 0.1290:
    q = 0.1143
    β·J = -ln(q) = 2.17

  Check: max β·J in Kähler cone ≈ 1.46
  β·J_needed = 2.17 > 1.46 → single instanton insufficient
  Need ~2 overlapping instantons: 2 × β·J ≈ 1.08 each → feasible! ✅

========================================================================

```
