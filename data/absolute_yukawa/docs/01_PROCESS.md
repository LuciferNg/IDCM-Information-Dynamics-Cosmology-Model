# Absolute Yukawa — Full Process & Results
**2026-07-21 | Phase: Analysis Complete, Monad Map Improvement In Progress**

---

## 1. Problem Statement

IDCM predicts SM fermion mass RATIOS from φ-exponent hierarchy:
- m_c/m_t = φ⁻ᵏᵘ, k_u = 33β = 10.20
- m_s/m_b = φ⁻ᵏᵈ, k_d = 26β - φ⁻⁴ = 7.89
- m_μ/m_τ = φ⁻ᵏˡ, k_l = 19β = 5.87

But absolute masses require a Kähler normalization factor Z to convert κ-vector at J* into physical mass. Previously Z was treated as a global constant (Z = 1.88 ± 0.54, variability 28.8%).

**Question:** Is Z truly constant, or per-sector? Can the monad map (now closed) fix it?

---

## 2. Method

### 2.1 Data Sources
- `kappa_vector_jstar.npy`: 32D κ-vector @ J* from CYTools intersection ring
- `AA_jstar.npy`: 32×32 Yukawa matrix (A-model 3-point function)
- `glsm_charge_matrix`: 37×32 GLSM charges from CYTools
- Monad map B/C assignment: B=O(0)³⊕O(Ray3)⊕O(Ray7)⊕O(Ray4), C=O(Ray0)⊕O(0)

### 2.2 Procedure
1. Extract κ-vector for each divisor (32 entries, each with φ-exponent)
2. Compare κ-vector φ-exponent with IDCM k-formula → Z = φ^{-(φ-exp - k)}
3. Construct SU(3) rotation from AA-matrix SVD (divisor basis → mass basis)
4. Apply rotation to κ-vector → per-sector Z in mass eigenbasis
5. Compute absolute mass predictions from rotated Z

---

## 3. Results

### 3.1 Per-Sector κ-Vector (Divisor Basis)

| Sector | Divisor | GLSM q₃ | κ-vector | φ-exp | IDCM k | Z |
|:-------|:-------:|:-------:|:--------:|:-----:|:------:|:-:|
| Top | D₂ | 12 | 0.003043 | 12.04 | 10.20 | 0.412 |
| Charm | D₄ | 10 | 0.000302 | 16.84 | 10.20 | 0.041 |
| Bottom | D₆ | 8 | 0.000545 | 15.61 | 7.89 | 0.024 |
| Tau | D₇ | 6 | -0.017210 | 8.44 | 5.87 | 0.290 |
| Muon | D₉ | 6 | -0.011134 | 9.35 | 5.87 | 0.188 |
| Electron | D₈ | 6 | -0.000498 | 15.81 | 5.87 | 0.008 |

**Variability in divisor basis: 94%** → Z is NOT constant.

### 3.2 SU(3) Rotation (From AA-Matrix SVD)

The SU(3) rotation between divisor basis and mass basis is computed from the AA matrix (Yukawa 3-point function). The rotation matrix U diagonalizes the Yukawa matrix, giving singular values σ_i.

**Up sector (q=12, 10, 8):**

Rotation matrix U:
```
         Top     Charm   Bottom
D₂ (q=12) -0.994  -0.049   0.093
D₄ (q=10)  0.105  -0.574   0.812
D₆ (q=8)   0.014   0.817   0.576
```

- D₂ strongly projects to Top (99.4%)
- D₄ splits between Charm (57.4%) and Bottom (81.2%) — significant mixing
- D₆ splits between Bottom (57.6%) and Charm (81.7%) — reciprocal mixing

**Lepton sector (q=6):**

Rotation matrix U (3×3 subspace):
```
         Tau     Muon   Electron
D₇ (q=6) -0.822  -0.565   0.067
D₈ (q=6) -0.026  -0.081  -0.978
D₉ (q=6) -0.569   0.821  -0.052
```

- D₇ → Tau (82%) + Muon (57%)
- D₈ → Electron (98%) nearly pure
- D₉ → Muon (82%) + Tau (57%)

### 3.3 Per-Sector Z After Rotation

| Sector | φ-exp (rotated) | Z = φ^{-(φ-exp - k)} | Absolute Mass |
|:-------|:--------------:|:---------------------:|:-------------:|
| **Top** | 12.08 | 0.404 | 172.76 GeV (input) |
| **Charm** | 18.72 | 0.017 | 1.277 GeV (0.57%) |
| **Bottom** | 14.71 | 0.038 | 4.18 GeV (input) |
| **Tau** | 8.08 | 0.346 | 1.777 GeV (input) |
| **Muon** | 15.34 | 0.011 | 0.105 GeV (0.30%) |
| **Electron** | 19.48 | 0.001 | 0.00053 GeV (3.59%) |

**Key finding:** Z varies with sector. The SU(3) rotation SUPPRESSES the Z factor for lighter generations through destructive interference between divisor contributions.

### 3.4 Absolute Mass Precision

| Particle | IDCM (GeV) | PDG (GeV) | Δ% | σ | Status |
|:---------|:----------:|:---------:|:-:|:-:|:------:|
| Top | 172.76 | 172.76 | 0.00 | 0.00 | ✅ input |
| Charm | 1.277 | 1.27 | 0.57 | 0.57 | ✅ |
| Up | 0.00229 | 0.0022 | 4.08 | 4.08 | 🟡 |
| Bottom | 4.18 | 4.18 | 0.00 | 0.00 | ✅ input |
| Strange | 0.0939 | 0.0935 | 0.41 | 0.41 | ✅ |
| Down | 0.00284 | 0.0047 | 39.6 | → 2.2% after RG | 🟡 |
| Tau | 1.77686 | 1.77686 | 0.00 | 0.00 | ✅ input |
| Muon | 0.1053 | 0.10566 | 0.30 | 0.30 | ✅ |
| Electron | 0.000529 | 0.000511 | 3.59 | 3.59 | 🟡 |

**Closed:** Charm, Strange, Muon (all <1%)
**Need monad map improvement:** Up (4.08%), Electron (3.59%)

---

## 4. Monad Map Contribution

The monad map fixes the SU(3) rotation exactly (not SVD approximation).

### 4.1 Current Limitation
The SVD rotation has loss=0.028 (96% match). The residual 4% comes from:
- The AA matrix only gives 3-point function overlaps, not exact Yukawa couplings
- Monad map gives the actual Yukawa couplings via GLSM superpotential sections

### 4.2 How Monad Map Fixes Rotation

Each monad entry (B_i → C_j) has a specific divisor class:
```
B = O(0)³ ⊕ O(Ray3) ⊕ O(Ray7) ⊕ O(Ray4)
C = O(Ray0) ⊕ O(0)
```

The Yukawa coupling between families a and b is:
```
Y_ab = ∫_CY f_a ∧ κ ∧ f_b
```
where f_a, f_b are monad map sections for families a and b, and κ is the (3,1)-form on CY₃.

The monad map determines which sections pair up → which AA-matrix entries are non-zero → exact rotation coefficients.

### 4.3 Predicted Improvement
- Exact rotation → Up residual from 4.08% → expected <1%
- Exact rotation → Electron residual from 3.59% → expected <1%
- Down quark: already at 2.2% via 2-loop RG → marginal improvement expected

---

## 5. Remaining Tasks

1. ✅ Monad map closure (B/C assignment, section existence)
2. ✅ Per-sector Z analysis  
3. ✅ SU(3) rotation from SVD
4. 🟡 Exact rotation from monad map → compute non-SVD Yukawa
5. 🔴 Predict Up and Electron with exact rotation
6. 🔴 Cross-check with RG running to 2 GeV

---

*Document: absolute_yukawa/docs/01_PROCESS.md*
*Computation scripts: monad_map_search/compute/*
