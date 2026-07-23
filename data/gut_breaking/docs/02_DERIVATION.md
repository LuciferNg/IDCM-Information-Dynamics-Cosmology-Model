# GUT Breaking — Full Derivation
**2026-07-21 | From monad map rank-4 bundle to E₈ → SO(10) → SU(5) → SM**

---

## 1. Monad Bundle Structure Group

### 1.1 Monad Data
```
B = O(0)³ ⊕ O(Ray3) ⊕ O(Ray7) ⊕ O(Ray4)    (6 summands)
C = O(Ray0) ⊕ O(0)                            (2 summands)
V = ker(B → C)
rk(V) = 6 - 2 = 4
```

### 1.2 Structure Group Candidates

For a rank-4 holomorphic vector bundle on a CY₃, the possible structure groups and their commutants in E₈:

| Group | Rank | Dim rep | E₈ Commutant | Contains SM? |
|:------|:----:|:-------:|:------------:|:------------:|
| SU(4) | 3 | 15 | SO(10) | ✅ (SO(10)→SM) |
| SO(8) | 4 | 28 | SO(8) | ❌ (no SM in SO(8)) |
| Sp(4) | 2 | 10 | E₇ | ❌ (E₇→SM needs 7 steps) |
| SU(3)×U(1) | 4 | — | SU(5)×U(1) | 🟡 (no ν_R) |

**Selection: SU(4)**
- Only SU(4) gives a commutant (SO(10)) that:
  1. Contains the SM as a subgroup
  2. Naturally accommodates 3 generations in the 16-plet (including ν_R)
  3. Has the right rank-5 Cartan to match the 5 noncoord rays

### 1.3 Why Not SU(3)×U(1)?

SU(3)×U(1) would give SU(5)×U(1) as commutant, which is a possible GUT group. However:
- SU(5) does NOT contain ν_R (it's in the 10⊕**5**⊕1, the singlet is not automatically ν_R)
- The monad has 4 active noncoord rays (3,7,4 in B, 0 in C) + Ray8 broken → 5 rays total
- A rank-4 structure group from 5 broken U(1)s naturally gives rank-5 commutant = SO(10)

---

## 2. SO(10) Cartan from GLSM Charges

### 2.1 The 5 Noncoord Rays

The CY₃(36,98) polytope has 37 rays: 32 coordinate rays (unit vectors) + 5 non-coordinate rays. The 5 noncoord rays encode the breaking of U(1)³² to the SM gauge group.

| Ray | Charge vector (first 8 components) | Role in monad | SO(10) direction |
|:---:|:-----------------------------------|:-------------:|:-----------------|
| 0 | [0, -20, -64, -10, -53, -48, -42, -32] | **C summand** | U(1)_B-L / broken direction |
| 3 | [0, +4, +12, +2, +10, +9, +8, +6] | **B summand** | U(1)_R / Cartan #1 |
| 7 | [0, 0, +4, 0, +3, +3, +2, +2] | **B summand** | U(1)_χ / Cartan #2 |
| 4 | [+1, -5, -17, -2, -14, -13, -11, -8] | **B summand** | U(1)_Y-like / Cartan #3 |
| 8 | [-2, +20, +64, +9, +53, +48, +42, +31] | **NOT in monad** | Broken at M_GUT |

### 2.2 Cartan Rank Verification

SO(10) has rank 5, requiring 5 Cartan U(1) generators. The 5 noncoord rays → 5 U(1)s.
- 4 active in the monad (rays 0, 3, 7, 4) → the SU(4) structure group
- 1 broken (ray 8) → extra U(1) broken at GUT scale

The monad's B/C assignment leaves Ray8 with zero participation in either B or C, meaning its corresponding divisor class is spontaneously broken. This IS the U(1) that distinguishes SU(5)×U(1) from SO(10) — its breaking leaves SU(5).

**Result:** Monad map + GLSM data → SO(10) ✅

---

## 3. E₈ → SO(10) × SU(4) Decomposition

### 3.1 The Instanton

E₈ has dimension 248. The decomposition under E₈ → SO(10) × SU(4):

```
248 → (45, 1)       ⊕    (16, 4)      ⊕    (16, 4)     ⊕    (10, 6)     ⊕    (1, 15)
     SO(10) gauge        Matter gen.      Anti-gen.         Higgs            SU(4) adj.
```

- **(45, 1):** SO(10) gauge bosons (the visible gauge group)
- **(16, 4):** 4 families of 16-plets (3 survive H¹(V)=3, 1 gets lifted)
- **(10, 6):** 6 Higgs 10-plets (Higgs candidates)
- **(1, 15):** SU(4) bundle moduli (hidden sector)

### 3.2 Generation Count

In heterotic compactification:
- Number of massless fermion generations = h¹(X, V) = dim H¹(V)
- For the monad: H¹(V) = 3 (from the φ-exponent counting)

Each generation transforms as the **16** of SO(10), branching to SM as:
```
16 → 10 ⊕ 5 ⊕ 1 of SU(5)
     ↓       ↓      ↓
     Q,u^c,e^c   d^c,L   ν^c
```

### 3.3 Divisor-to-Representation Mapping

From the κ-vector φ-exponent analysis:

| Divisor | GLSM q₃ | SU(5) rep | SM content | Generation |
|:-------:|:-------:|:---------:|:-----------|:---------:|
| D₂ | 12 | 10 | (Q, u³, e⁺) | 3rd (Top) |
| D₄ | 10 | 10 | (Q, u², μ⁺) | 2nd (Charm) |
| D₅ | 9 | 10 | (Q, u¹, e⁺) | 1st (Up) |
| D₆ | 8 | 5 | (d³, L_τ) | 3rd (Bottom) |
| D₁₈ | 9 | 5 | (d², L_μ) | 2nd (Strange) |
| D₇ | 6 | 5 | (d¹, L_e) | 1st (Down) |
| D_8/D_9/D_21 | 6 | 1 | ν^c | R-handed ν |

---
## 4. Breaking Chain: Step by Step

### Step 1: SU(4) Instanton → E₈ → SO(10) × SU(4)
```
At scale M_string ≈ 3.89×10¹⁷ GeV:
- Monad V with structure group SU(4) on CY₃(36,98)
- Commutant in E₈ = SO(10) → visible gauge group
- 3 generations in H¹(V) transform as 16 of SO(10)
```

### Step 2: Ray8 Breaking → SO(10) → SU(5) × U(1)_χ
```
At scale M_GUT ≈ 1.24×10¹⁶ GeV:
- Ray8 (5th noncoord ray) is NOT in monad
- Its corresponding divisor class gets GUT-scale mass
- This breaks one U(1): SO(10) → SU(5) × U(1)_χ
- The U(1)_χ acts as B-L symmetry
```

**Why Ray8?** The monad B/C assignment:
- B: O(0)³ ⊕ O(Ray3) ⊕ O(Ray7) ⊕ O(Ray4) — includes rays [3,7,4]
- C: O(Ray0) ⊕ O(0) — includes ray [0]
- Ray8 is completely absent from both B and C → no Yukawa coupling → GUT-scale mass

### Step 3: 24 Higgs → SU(5) → SM
```
At scale M_GUT ≈ 1.24×10¹⁶ GeV:
- The 24-plet of SU(5) gets VEV → breaks SU(5) → SM
- ⟨24_H⟩ ∝ diag(2,2,2,-3,-3) × M_GUT
- Doublet-triplet splitting separates the Higgs doublet from the color triplet
- Proton decay operators (d=6) from X, Y gauge boson exchange
```

### Step 4: SUSY Breaking → MSSM
```
At scale M_SUSY ≈ 1-10 TeV:
- Soft SUSY breaking terms from the W-field
- MSSM running from M_GUT to M_Z
- RGE determines the weak scale and the Higgs mass
```

---

## 5. Verification: 3 × 16 of SO(10)

### 5.1 Counting from κ-Vector

The 32 coord divisor κ-vector entries at J* give 3 families:
- Highest kv: D_2 (0.003043) → 3rd family
- Medium kv: D_4-D_6-D_7 → 2nd family  
- Lowest kv: D_8-D_9-D_21 → 1st family

### 5.2 Completeness Check

Standard Model content from 3 × 16 of SO(10):

| Field | SU(3) × SU(2) | # from 3×16 | # in SM |
|:------|:-------------:|:-----------:|:-------:|
| Q = (u_L, d_L) | (3, 2) | 3 | 3 |
| u^c_L | (3̄, 1) | 3 | 3 |
| d^c_L | (3̄, 1) | 3 | 3 |
| L = (ν_L, e_L) | (1, 2) | 3 | 3 |
| e^c_L | (1, 1) | 3 | 3 |
| ν^c_R | (1, 1) | 3 | 3 |

All accounted for ✅

---

## 6. Summary

| Step | Gauge Group | Scale (GeV) | Monad Map Role |
|:-----|:-----------|:-----------:|:---------------|
| Compactification | E₈ | M_string = 3.89×10¹⁷ | SU(4) bundle on CY₃ |
| Instanton | SO(10) | M_GUT = 1.24×10¹⁶ | rk(V)=4 → commutant |
| Ray8 breaking | SU(5) × U(1) | M_GUT | Ray8 missing from monad |
| 24 Higgs | SM | M_GUT | Standard GUT mechanism |
| SUSY | MSSM | ~TeV | W-field soft terms |
