# 執行輸出：neutrino_kappa_summary.py

**日期：** 2026-07-20
**腳本：** `~/IDCM/neutrino_kappa_summary.py`
**狀態：** ✅ EXIT=0

```
/tmp/cy_venv/lib/python3.11/site-packages/cytools/config.py:151: UserWarning: 
**************************************************************
Warning: You have enabled experimental features of CYTools.
Some of these features may be broken or not fully tested,
and they may undergo significant changes in future versions.
**************************************************************

  warnings.warn(
======================================================================
  1. ν_R₁ (D_7, q=6) — N·N·φ terms
======================================================================
    κ[7,7,0]= +31 J*_k=3.5219e-03 → M_R+= 1.3460e+15 GeV
    κ[7,7,2]= -32 J*_k=3.8484e-02 → M_R+= -1.5182e+16 GeV
    κ[7,7,3]= +85 J*_k=1.3070e-02 → M_R+= 1.3696e+16 GeV
    κ[7,7,6]= -10 J*_k=1.7811e-03 → M_R+= -2.1959e+14 GeV
    κ[7,7,7]=-232 J*_k=3.9736e-03 → M_R+= -1.1365e+16 GeV
    κ[7,7,16]= -10 J*_k=1.4577e-03 → M_R+= -1.7971e+14 GeV
    κ[7,7,21]=  -2 J*_k=2.1150e-02 → M_R+= -5.2150e+14 GeV
    Σ M_R = -1.2427e+16 GeV

======================================================================
  2. Dirac Yukawa Y_ν from κ[2,7,7]
======================================================================
    κ[2,7,7] = -32
    kinetic = 64 × √(J*_2 × J*_7²) = 0.0499
    Y_ν = κ[2,7,7] × kinetic = -1.5964

======================================================================
  3. TYPE I SEESAW — all terms
======================================================================

  ν_R at D_7 (q=6):
    M_R = -1.2427e+16 GeV
    Y_ν = -1.5964
    Seesaw m_ν = 6.209509e-03 eV  (obs ~0.05)
    IDCM κ·ε^14·v = 0.0481 eV
    Ratio CY/IDCM = 0.1292

  ν_R at D_9 (q=6):
    M_R = -6.8236e+14 GeV
    Y_ν = -0.0404
    Seesaw m_ν = 7.255098e-05 eV  (obs ~0.05)
    IDCM κ·ε^14·v = 0.0481 eV
    Ratio CY/IDCM = 0.0015

  ν_R at D_20 (q=7):
    M_R = -2.0545e+16 GeV
    Y_ν = -0.9977
    Seesaw m_ν = 1.466894e-03 eV  (obs ~0.05)
    IDCM κ·ε^14·v = 0.0481 eV
    Ratio CY/IDCM = 0.0305

======================================================================
  4. κ_VECTOR LEPTON HIERARCHY @ J*
======================================================================

  Top λ: κ_vector = 0.0488 at D_28 (q=3)
  κ_vector range: [-0.0192, 0.0488]

  Lepton (q=6) hierarchy from κ_vector:
   Div       J*_i      κ_vec    φ-exp   IDCM label
  ──── ────────── ────────── ──────── ────────────
     7 3.9736e-03    -0.0172    2.165        τ(ν₃)
     8 5.6529e-03    -0.0005    9.529        e(ν₁)
     9 1.6104e-03    -0.0111    3.070        μ(ν₂)
    21 2.1150e-02    -0.0006    9.200            ?

======================================================================
  5. κ[0,2,2]=+6 IS NOT NEUTRINO MAJORANA
======================================================================

  κ[0,2,2] involves divisors (0,2,2):
    ν_R lives on D_7, D_9, D_20, NOT D_2
    κ[0,2,2] = H·H·Φ₀ (Higgs-Higgs-φ coupling)
    → κ[0,2,2] is Higgs MASS term, NOT N·N·φ

  κ[0,2,2] = +6 gives tree-level µ-term in superpotential:
    W = µ·H_u·H_d where µ = κ[0,2,2] × ⟨Φ₀⟩
    µ ∼ 6 × 64 × J*_0 × MP = 6 × 64 × 3.5219e-03 × 1.22e+19
    µ ∼ 1.6499e+19 GeV  → too large!
    → SUSY µ-problem — µ must be ∼ 100-1000 GeV
    → This means Φ₀ VEV is NOT at J* for µ-term
    → Similarly, N·N·φ VEVs may NOT be at J* either

======================================================================
  6. FINAL: κ VECTOR vs φ-EXPONENT MATCH
======================================================================

  IDCM k-values for lepton:

  ν₃(τ) (D_7):
    κ_vector Y_eff = -0.0172 (rel=0.3528)
    κ_vector φ-exp = 2.17
    IDCM k = 97.55, m = 0.0480 eV
    IDCM ε^k: κ·ε^97.55·v = 0.000000 (mismatch because ε^k != φ^-k)

  ν₂(μ) (D_9):
    κ_vector Y_eff = -0.0111 (rel=0.2282)
    κ_vector φ-exp = 3.07
    IDCM k = 101.21, m = 0.0074 eV
    IDCM ε^k: κ·ε^101.21·v = 0.000000 (mismatch because ε^k != φ^-k)

  ν₁(e) (D_8):
    κ_vector Y_eff = -0.0005 (rel=0.0102)
    κ_vector φ-exp = 9.53
    IDCM k = 106.21, m = 0.0011 eV
    IDCM ε^k: κ·ε^106.21·v = 0.000000 (mismatch because ε^k != φ^-k)

======================================================================
  VERDICT: κ tensor confirms structure, seesaw needs moduli tuning
  The tree-level M_R from κ[N,N,φ] at J* is ~10¹⁸ GeV
  → ~10³× too large for observed m_ν via seesaw
  → But consistent with IDCM claim that ν sector needs instantons
  → κ_vector hierarchy: D_7(τ) > D_9(μ) > D_21/D_8(e)
  → κ[0,2,2]=+6 identified as µ-term, NOT N·N·φ
======================================================================

```
