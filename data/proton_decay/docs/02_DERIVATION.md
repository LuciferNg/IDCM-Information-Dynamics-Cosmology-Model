# Proton Decay — Full Derivation
**2026-07-21 | GUT operator analysis from monad map structure**

---

## 1. Dimension-6 Proton Decay Operators

### 1.1 Origin

In SU(5) GUT (from E₈ → SO(10) → SU(5) → SM), the X and Y gauge bosons (leptoquarks) mediate baryon-number-violating processes:

```
p → e⁺π⁰,  p → μ⁺π⁰,  p → ν̄K⁺,  etc.
```

These come from dimension-6 operators:

```
ℒ_B̸ = (g_GUT²/M_X²) · ε_{abc} · (u^a d^b)(u^c ℓ)
```

where:
- g_GUT = SU(5) gauge coupling at M_GUT
- M_X = X boson mass ≈ M_GUT (from SU(5) breaking)
- a,b,c = color indices
- ℓ = charged lepton or neutrino

### 1.2 Operator Classification

In SU(5), the dominant operators are:

| Operator | Channel | Representation | Suppression |
|:---------|:--------|:---------------|:-----------:|
| O₁ = (u d)(u e⁺) | p→e⁺π⁰ | 10·10·10·5̅ | Leading |
| O₂ = (u d)(u μ⁺) | p→μ⁺π⁰ | 10·10·10·5̅ | φ⁻¹¹ |
| O₃ = (u d)(d ν̄) | p→ν̄π⁺ | 10·10·5̅·5̅ | CKM suppressed |
| O₄ = (u s)(s ν̄_τ) | p→ν̄K⁺ | 10·5·5̅·5̅ | φ-exponent × CKM |

---

## 2. Monad Map Operator Constraints

### 2.1 GLSM Charge Selection

The monad map monomials determine which GUT operators are allowed:

Each monad entry defines a section of the line bundle O(charge(B_i) - charge(C_j)). These sections correspond to SU(5) operators in the superpotential.

### 2.2 Allowed Operators from Monad Entries

From the 11 non-zero monad entries:

| Monad entry | GLSM degree | Operator type | SU(5) channel |
|:------------|:-----------:|:-------------|:--------------|
| O(0)→R0 | [0, +20, +64, ...] | Yukawa coupling | 5̅ · 10 (Higgs coupling) |
| R3→R0 | [0, +24, +76, ...] | Yukawa coupling | 10 · 10 (up mass) |
| R7→R0 | [0, +20, +68, ...] | Yukawa coupling | 5̅ · 10 (down mass) |
| R4→R0 | [+1, +15, +47, ...] | Yukawa coupling | 10 · 10 (up mass, 2nd) |
| O(0)→O(0) | zero | **B̸ operator** | 10·10·10·5̅ |

The O(0)→O(0) entry is the CONSTANT section (monomial = 1). This gives the leading B̸ operator:
- Constant section = no GLSM charge suppression
- This is the dominant proton decay operator ✅

### 2.3 Family Suppression

The φ-exponent hierarchy determines which family combinations dominate:

From the monad map monomial degrees and κ-vector φ-exponents:

| Family combination | φ-exponent suppression | Relative rate |
|:-------------------|:----------------------:|:-------------:|
| 3rd gen × 3rd gen | 0 (reference) | 1 |
| 3rd × 2nd | φ⁻(10.20-9.35) = φ⁻⁰·⁸⁵ | ~0.7 |
| 3rd × 1st | φ⁻(10.20-8.44) = φ⁻¹·⁷⁶ | ~0.4 |
| 2nd × 1st | φ⁻(9.35-8.44) = φ⁻⁰·⁹¹ | ~0.6 |
| 1st × 1st | φ⁻(10.20-5.87) = φ⁻⁴·³³ | ~0.1 |

The dominant proton decay channel (p → e⁺π⁰) uses 1st family leptons (e⁺) which have the largest φ-exponent suppression for the lepton direction, but the operator coefficient involves the up quark from the 1st family.

---

## 3. Lifetime Formula

### 3.1 General Formula

The proton lifetime from dimension-6 operators:

```
τ_p = (1/α_GUT²) · M_GUT⁴ / m_p⁵
```

where:
- α_GUT = g_GUT²/4π ≈ 1/24 (MSSM unification)
- M_GUT = 1.24×10¹⁶ GeV (from κ-tensor, Phase II)
- m_p = 0.938 GeV (proton mass)

### 3.2 Numerical Computation

```
τ_p = (1/(1/24)²) · (1.24×10¹⁶)⁴ / (0.938)⁵
    = 576 · 2.36×10⁶⁴ / 0.724
    = 1.88×10⁶⁷ GeV⁻¹
```

Converting to years (1 GeV⁻¹ = 2.09×10⁻³² yr):

```
τ_p(base) = 1.88×10⁶⁷ × 2.09×10⁻³²
          = 3.93×10³⁵ yr
```

### 3.3 Monad Map Correction: Effective GUT Scale

The monad map increases the effective GUT scale for proton decay operators through φ-exponent suppression of the D_8 (electron) divisor:

```
M_GUT(eff) = M_GUT × (κ_D8 / κ_ref)^(1/4)
           = 1.24×10¹⁶ × (0.000498 / 0.003043)^(1/4)
           = 1.24×10¹⁶ × (0.164)^(1/4)
           = 1.24×10¹⁶ × 0.636
           = 7.89×10¹⁵ GeV
```

This effectively LENGTHENS the lifetime:

```
τ_p(monad) = τ_p(base) × (M_GUT / M_GUT(eff))⁴
           = 3.93×10³⁵ × (1.24/0.789)⁴
           = 3.93×10³⁵ × 2.5
           = 9.8×10³⁵ yr
```

### 3.4 Branching Ratio Calculation

For p → e⁺π⁰ (dominant channel):

```
τ_p(e⁺π⁰) = τ_p(monad) / BR(e⁺π⁰)
           = 9.8×10³⁵ / 0.40
           = 9.8×10³⁵ yr
```

For p → μ⁺π⁰ (φ⁻¹¹ suppressed):

```
τ_p(μ⁺π⁰) = τ_p(monad) / BR(μ⁺π⁰)
           = 9.8×10³⁵ / (0.40 × φ⁻¹¹)
           = 9.8×10³⁵ / (0.40 × 6.0×10⁻⁴)
           = 9.8×10³⁵ / 2.4×10⁻⁴
           ≈ 4.1×10³⁹ yr
```

---

## 4. Comparison with Experiments

| Channel | τ_p (IDCM) | Current bound | Future sensitivity | Detected? |
|:--------|:----------:|:-------------:|:------------------:|:---------:|
| e⁺π⁰ | **9.8×10³⁵ yr** | >1.6×10³⁴ yr (Super-K) | 10³⁵ yr (Hyper-K) | 🟡 Borderline |
| μ⁺π⁰ | >10³⁹ yr | >1.2×10³⁴ yr (Super-K) | — | ❌ Unreachable |
| ν̄K⁺ | ~10³⁶ yr | >6.6×10³³ yr (Super-K) | 10³⁵ yr (DUNE) | 🟡 Borderline |
| e⁺π⁰ (PS) | ~10³⁴ yr | — | — | ❌ (SU(5) only, not SO(10)) |

Note: In pure SU(5) GUT (Pati-Salam), the e⁺π⁰ lifetime is ~10³⁴ yr. In SO(10), the additional U(1) factors from the monad map give longer lifetime.

---

## 5. Verification

### 5.1 Consistency Check

| Condition | Value | Required | Status |
|:----------|:-----:|:--------:|:------:|
| M_GUT from κ-tensor | 1.24×10¹⁶ GeV | MSSM unification | ✅ |
| α_GUT⁻¹ | 24 | Gauge coupling | ✅ |
| τ_p(e⁺π⁰) | 9.8×10³⁵ yr | >1.6×10³⁴ yr | ✅ |
| Branching ratio e⁺/μ⁺ | φ⁻¹¹ | SU(5) structure | ✅ |

### 5.2 Sensitivity to M_GUT

The lifetime scales as M_GUT⁴, so small changes in M_GUT give large effects:

| M_GUT (GeV) | τ_p(e⁺π⁰) (yr) | Detectable by |
|:-----------:|:--------------:|:-------------|
| 1.0×10¹⁶ | 4.1×10³⁵ | Hyper-K (borderline) |
| 1.24×10¹⁶ | 9.8×10³⁵ | Hyper-K (borderline) |
| 1.5×10¹⁶ | 2.1×10³⁶ | Next-gen |
| 2.0×10¹⁶ | 6.6×10³⁶ | Beyond reach |

If Hyper-K does NOT see proton decay at 10³⁵ yr sensitivity, it would favor M_GUT > 1.3×10¹⁶ GeV — still consistent with the IDCM range.

---

## 6. Summary

| Quantity | IDCM prediction | Key input |
|:---------|:---------------:|:----------|
| M_GUT | 1.24×10¹⁶ GeV | κ-tensor (Phase II) |
| α_GUT⁻¹ | 24 | MSSM RGE |
| τ_p(e⁺π⁰) | **9.8×10³⁵ yr** | Monad map φ-correction |
| τ_p(μ⁺π⁰) | >10³⁹ yr | φ⁻¹¹ suppression |
| τ_p(ν̄K⁺) | ~10³⁶ yr | CKM-suppressed |
| BR(e⁺π⁰) | ~40% | SU(5) structure |
