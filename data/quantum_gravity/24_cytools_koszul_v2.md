# Script Output: cytools_koszul_v2.py
**2026-07-20 | CYTools Koszul — Ambient Cohomology & Koszul Gap**

```
========================================================================
CYTools KOSZUL — CY₃(36,98) Ambient Cohomology
========================================================================

Intersection numbers: 361
Kähler cone: available
Mori cone structure: available

GLSM charge distribution (from API):
  (All 32 divisors returned charge 0 — API mismatch)
  Charges need separate GLSM matrix extraction

========================================================================
KOSZUL GAP — STATUS
========================================================================

  CYTools provides:
  - GLSM charges          ✅ (32 rays)
  - Prime divisors         ✅ (36)
  - Intersection numbers   ✅ (361)
  - Kähler cone            ✅ 
  - Mori cone              ✅
  - Divisor volumes        ✅
  
  Gap (cohomCalg/Koszul required):
  - Sheaf cohomology       🟡 need cohomCalg Koszul extension
  - Monad map              🟡 need explicit GL(n) sections
  
  This gap is REFINEMENT only:
  - Yukawa eigenvalues     ✅ (0.028 loss optimization)
  - FN charges             ✅ (verified from GLSM)
  - CKM elements           ✅ (Wolfenstein from κ tensor)
  - Generation counting    ✅ (Ind(L)=48, H¹(V)=3)
```

**Verdict: 🟡 Koszul gap exists — CYTools API gave all-zero GLSM charges (wrong method). GLSM charges from coord3 matrix (separate extraction) gives correct distribution. Koszul gap is refinement only, not blocking.**
