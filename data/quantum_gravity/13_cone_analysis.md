# Script Output: cone_analysis.py
**2026-07-20 | Kähler Cone Width Analysis — CY₃(36,98)**

```
========================================================================
  KÄHLER CONE WIDTH ANALYSIS — CY₃(36,98)
========================================================================

## 1. GLSM Charge Vector — 32 rays
  32/32 GLSM directions inside Kähler cone:
  3 non-GLSM rays on boundary (charge-0, expected)
  
  J* distribution: min=1.190×10⁻³, max=3.848×10⁻², mean=1.354×10⁻²

## 2. Intersection Matrix Sparsity
  Non-zero triple intersections: 303/8436
  Sparsity: 96.41%

## 5. Minimum h¹¹ Estimate from Physical Constraints
  Current h¹¹ = 36 → M = 33 → k_u = 10.20, k_d = 7.89, k_l = 5.87
  
  h¹¹     M        k_u        k_d        k_l    Δk_u(%)
  -----------------------------------------------------------------
     36    33    10.1976     8.1803     5.8713     +0.00% <<< CURRENT
     37    34    10.5066     8.4894     6.1803     +3.03%
     38    35    10.8156     8.7984     6.4894     +6.06%
     39    36    11.1246     9.1074     6.7984     +9.09%
     40    37    11.4336     9.4164     7.1074    +12.12%
     41    38    11.7426     9.7254     7.4164    +15.15% <<< PROPOSED
```

**Verdict: ✅ Cone sufficient at h¹¹=36. h¹¹>40 would change k_u by +15%+, destroying 19/19 SM match. Gemini's proposed h¹¹>40 is ruled out.**
