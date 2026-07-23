# EM002: Electron Dynamics — Verification Report

**Date:** 2026-07-23
**Status:** 🔴 Two numerical failures — m_e formula broken, g-factor contradiction
**Topic:** Electron as W-field spinor excitation

---

## Theoretical Hypothesis

The electron is a quantized W-field spinor excitation. The Dirac equation emerges from the W-field spinor PDE at the J* fixed point.

## Purpose

Verify: (1) m_e = κ·φ⁵·M_P gives 0.511 MeV, (2) Dirac equation emergence, (3) Pauli exclusion from W-field, (4) g-factor formula a_e = α_em/2π + ε/4π.

## Complete Derivation Chain

**1. Mass formula (raw):** m_e = κ·φ⁵·M_P
**2. Mass formula (Phase I, actual):** m_e = ε⁷·v_EW
**3. Dirac equation:** (iγᵘ∇_μ - m_e)Ψ_e = ε·Φ(∇A)·Ψ_e
**4. g-factor:** a_e = α_em/2π + ε/4π

## Verification Method

Numerical computation of mass from both formulas. Comparison with PDG m_e = 0.51099895 MeV. Dimensional check of g-factor correction.

## Verification Process

### Check 1: m_e = κ·φ⁵·M_P 🔴
m_e = (1/16) × 11.09 × 1.22×10¹⁹ GeV = **2.99×10¹⁷ GeV**. This is NOT 0.511 MeV. Off by factor ~5.85×10²⁰. The document adds "Kählerian Normalization Z = 1.88±0.54" — but this normalisation factor is 5.85×10²⁰, not 1.88. The formula as stated is wrong.

### Check 2: m_e = ε⁷·v_EW 🟡
m_e = 0.1545⁷ × 246.22 GeV = **0.5294 MeV**. PDG: 0.5110 MeV. Error: 3.6% relative. σ is extreme (~1836) due to PDG precision on m_e. This is φ-fitting, not structural derivation.

### Check 3: g-factor correction 🔴
ε/4π = 0.0123. The Schwinger term α_em/2π = 0.00116. The W-field correction is **10× larger** than the entire QED contribution. The document says "suppressed at low energies" but provides no quantitative suppression mechanism. This contradicts precision QED measurements of a_e to 10⁻¹².

## Verification Result

| Check | Result | Status |
|:------|:-------|:------:|
| m_e = κ·φ⁵·M_P | 2.99×10¹⁷ GeV, not 0.511 MeV | 🔴 |
| m_e = ε⁷·v_EW | 0.5294 MeV (3.6% rel) | 🟡 |
| Dirac emergence | Structural mapping | 🔲 |
| Pauli exclusion | Claimed, not proven | 🔲 |
| g-factor | ε/4π = 0.0123 >> QED precision | 🔴 |

## Conclusion

The electron mass document has two serious problems: (1) the claimed formula κ·φ⁵·M_P is numerically wrong by ~20 orders of magnitude; (2) the g-factor correction contradicts established QED. The document's "✅ Structural derivation" is incorrect.

## Open Questions

1. What is the actual structural derivation of m_e?
2. Is ε⁷·v_EW a coincidence or a genuine structural relation?
3. Can the g-factor contradiction be resolved without introducing ad-hoc suppression?

## File Inventory

| File | Lines | Content |
|:-----|:-----:|:--------|
| verify.py | ~140 | Verification script |
| REPORT_en-US.md | ~100 | This report |
| REPORT_zh-TW.md | ~100 | Chinese version |
