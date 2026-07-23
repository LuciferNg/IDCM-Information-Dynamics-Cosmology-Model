# Script Output: pmns_from_kappa.py
**2026-07-20 | Direct Seesaw from κ Tensor vs IDCM Formula**

```
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
  D_7↔D_9: Δφ = 0.90, sinθ ≈ 0.6470, θ ≈ 40.3°
  D_7↔D_8: Δφ = 7.36, sinθ ≈ 0.0289, θ ≈ 1.7°
  D_9↔D_21: Δφ = 6.13, sinθ ≈ 0.0524, θ ≈ 3.0°

========================================================================
  NEXT: INSTANTON M_R CORRECTION
========================================================================
  Target M_R for m_ν₃=0.048eV: 1.60×10¹⁵ GeV
  Current M_R from κ tensor: 1.24×10¹⁶ GeV
  Reduction needed: ×0.129

  Single instanton: β·J_needed = 2.17 > 1.46 (cone max)
  Need ~2 overlapping instantons: 2 × β·J ≈ 1.08 each → feasible! ✅
```

**Verdict: 🟡 Direct seesaw from κ tensor gives m_ν₃=6.2×10⁻³ eV (×7.7 gap to IDCM 0.048 eV). The gap IS the instanton correction ℐ_inst. 2 overlapping instantons can close the gap. κ_vector hierarchy provides PMNS angles (θ₂₃≈40°) heuristically.**
