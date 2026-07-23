# 執行輸出：pmns_4x4_mixing.py

**日期：** 2026-07-20
**腳本：** `~/IDCM/pmns_4x4_mixing.py`
**狀態：** ✅ EXIT=0

```
/tmp/cy_venv/lib/python3.11/site-packages/cytools/config.py:151: UserWarning: 
**************************************************************
Warning: You have enabled experimental features of CYTools.
Some of these features may be broken or not fully tested,
and they may undergo significant changes in future versions.
**************************************************************

  warnings.warn(
========================================================================
  4×4 q=6 LEPTON κ-CONTRACTED YUKAWA
========================================================================

  Divisors: [7, 9, 8, 21]
    D_7:    -0.1046    +0.0000    +0.0000    -0.0151
    D_9:    +0.0000    -0.0156    +0.0007    +0.0000
    D_8:    +0.0000    +0.0007    -0.0157    +0.0000
    D_21:    -0.0151    +0.0000    +0.0000    +0.1081

  Singular values: [0.109172   0.10562238 0.01635328 0.01495687]
  Top 3 (light ν): [np.float64(0.1091719975331098), np.float64(0.10562238253368235), np.float64(0.016353283875247752)]

  Rows: 0=D_7(τ), 1=D_9(μ), 2=D_8(e), 3=D_21(?)

  PMNS matrix (columns: νₑ, ν_μ, ν_τ):
    D_7:  +0.0000  +0.0000  +0.0704
    D_9:  +0.6821  -0.7313  +0.0000
    D_8:  -0.7313  -0.6821  +0.0000
    D_21:  +0.0000  +0.0000  -0.9975

  PMNS angles:
    θ₁₂ = 43.01° (PDG: 33.82°)
    θ₂₃ = 0.00° (PDG: ~43°)
    θ₁₃ = 0.00° (PDG: 8.57°)

  Masses (from Y×v_EW):
    ν_1: 1.8996e+10 eV
    ν_2: 1.8378e+10 eV
    ν_3: 2.8455e+09 eV
  Δm²_21 = -2.3084e+19 eV² (PDG: 7.39e-5)
  Δm²_32 = -3.2967e+20 eV² (PDG: 2.51e-3)

  D₂₁ role:
    |U(D₂₁→νₑ)|² = 0.0000
    |U(D₂₁→ν_μ)|² = 0.0000
    |U(D₂₁→ν_τ)|² = 0.9950

  κ_vector φ-exponent hierarchy:
    D_7(q=6): κ_vec=-0.0172, φ^-2.17
    D_9(q=6): κ_vec=-0.0111, φ^-3.07
    D_8(q=6): κ_vec=-0.0005, φ^-9.53
    D_21(q=6): κ_vec=-0.0006, φ^-9.20

========================================================================
  CLOSURE: PMNS from 4×4 κ mixing
========================================================================
  θ₂₃ near-maximal > 35°                        🔴
  θ₁₂ > 10° (solar resolved)                    ✅
  θ₁₃ < 30° (small reactor)                     ✅
  NH mass ordering                              🔴

  Done.

```
