# Absolute Yukawa Matrix
**2026-07-21 | Monad map Kähler normalization → absolute masses**

## Goal
Promote all mass ratios (currently φ-exponent hierarchy) to absolute mass predictions using the monad map's Kähler normalization factor Z.

## Current Status
- ✅ Mass ratios from φ-exponents (m_c/m_t, m_s/m_b, m_μ/m_τ, etc.)
- ✅ Z = 1.88 ± 0.54 (Kählerian normalization, 28.8% variability across sectors)
- ✅ SU(3) rotation (loss=0.028, 96% match)
- 🟡 Monad map closed → can fix Z per sector instead of global average
- 🔴 Absolute masses still have ~30% uncertainty from Z variability

## Key Questions
1. Does the monad map fix Z individually per sector?
2. What are the predicted absolute masses?
3. Does this improve the Down quark RG closure (currently 2.2% with 2-loop RG)?

## Plan
1. Extract per-sector Z from monad map section structure
2. Compute absolute mass predictions for all 9 SM fermions
3. Cross-check with RG running to 2 GeV scale
4. Compare with PDG values

## Dependencies
- Monad map closure ✅
- Mass ratio φ-exponents ✅
- RG running factors ✅ (2-loop MSSM)
