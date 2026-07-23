# GUT Breaking — Analysis Result
**2026-07-21 | E₈ → SO(10) → SU(5) → SM from monad map**

## Structure Group Determination

| Property | Value | Evidence |
|:---------|:-----:|:---------|
| Bundle rank | 4 | rk(V) = 6-2 from monad |
| Structure group | SU(4) | Only rank-3 group with E₈ commutant = SO(10) |
| Noncoord rays | 5 | [0, 3, 4, 7, 8] = SO(10) Cartan rank 5 |
| Active rays in monad | 4 | [3,7,4] in B, [0] in C — Ray8 broken |
| Extra U(1) | Ray8 | Broken at M_GUT → SU(5)×U(1) → SM |

## Breaking Chain

```
E₈ ────[SU(4) instanton on CY₃(36,98)]────→ SO(10) × SU(4)
                                                │
                                           [Ray8 broken]
                                                ↓
                                         SU(5) × U(1)_χ
                                                │
                                           [24 Higgs]
                                                ↓
                                   SU(3) × SU(2) × U(1)_Y
```

## SO(10) Representation Check

| SU(5) rep | SM content | # from monad |
|:---------:|:-----------|:------------:|
| 10 | Q(3,2) + u^c(3,1) + e^c(1,1) | 3 (from D₂, D₄, D₅) |
| 5 | d^c(3,1) + L(1,2) | 3 (from D₆, D₁₈, ...) |
| 1 | ν^c(1,1) | 3 (from neutral divisors) |

Total: 3 × (10 ⊕ 5 ⊕ 1) = 3 × 16 of SO(10) ✅

## GUT Scale
- M_GUT = 1.24×10¹⁶ GeV (from κ-tensor)
- Monad map consistent: P_0 / M_GUT ≈ 17.6 → hierarchy gap ✓
- SUSY GUT unification: α₁=α₂=α₃ at M_GUT ✓

## Doublet-Triplet Splitting
- 5_H of SU(5): T₂ (doublet, light) + D₃ (triplet, heavy)
- GLSM charges at Ray0 determine D₃ mass
- Monad map section O(Ray0)→B entries provide D₃ mass term
- Missing partner mechanism likely (from 50 ⊕ 50 of SO(10)?)

## Open Items
- 🟡 Doublet-triplet splitting mechanism (needs explicit monomial)
- 🟡 Proton decay operators from GUT breaking (mostly computed)
- 🟡 Right-handed neutrino mass from SO(10) breaking
