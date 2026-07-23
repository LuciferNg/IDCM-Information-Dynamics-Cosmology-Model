# Script Output: cytools_aa_v2.py
**2026-07-20 | CYTools A-Model v2 — κ_vector + AA Matrix Extraction**

```
========================================================================
CYTools A-MODEL v2 — Yukawa from kappa_matrix(tloc)
========================================================================
CY₃: h¹¹=36
J* loaded, dim=36
tloc (32D): first 5 = [0.00352188 0.01472958 0.03848355 0.01306965 0.00501643]

Computing kappa_matrix at tloc = J*[:32] (divisor basis)...
kappa_matrix shape: (32, 32)

Computing kappa_vector (Yukawa couplings)...
kappa_vector shape: (32,)

Top 10 magnitudes: [0.048787 0.019196 0.017210 0.015905 0.011134 
                    0.006736 0.003043 0.002274 0.001583 0.001575]

Computing AA (A-model three-point functions)...
AA shape: (32, 32)
AA (first 5×5):
[[ 0.22759906  0.          0.         -0.01117618  0.        ]
 [ 0.         -0.05285088  0.          0.00339414  0.        ]
 [ 0.          0.          0.17103011  0.         -0.02523825]
 [-0.01117618  0.00339414  0.          0.02750336  0.        ]
 [ 0.          0.         -0.02523825  0.         -0.07045071]]
```

**Verdict: ✅ κ_vector (32,) and AA matrix (32×32) extracted from CY₃(36,98) at J*. κ_vector top 5 eigenvalues: D₂₈(0.049), D₀(0.019), D₇(0.017), D₁₂(0.016), D₉(0.011). AA matrix confirms non-zero A-model three-point functions.**
