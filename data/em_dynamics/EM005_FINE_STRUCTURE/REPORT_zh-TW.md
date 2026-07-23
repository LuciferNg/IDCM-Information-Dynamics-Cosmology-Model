# EM005: Fine-Structure Constant — Verification Report

**Date:** 2026-07-23
**Status:** 🔴 Foundation formula broken. "0.00%" claim is misleading.
**Topic:** α_EM from structural parameters and RG running

---

## Theoretical Hypothesis

α_EM⁻¹(M_Z) = 127.95 is derived from α₁⁻¹(M_GUT) = 4π/ε·κ² = 40.8 with standard MSSM RG running.

## Purpose

Verify every step of the α_EM derivation chain numerically.

## Verification Result

| Step | Claim | Computed | Status |
|:-----|:------|:---------|:------:|
| α₁⁻¹(M_GUT) = 4π/ε·κ² | 40.8 | Ambiguous — no interpretation gives 40.8 | 🔴 |
| α₁⁻¹(M_GUT) vs MSSM | Within 10% of 24 | 40.8 is 70% above 24 | 🔴 |
| RG term b₁/2π·ln(M_GUT/M_Z) | 21.2 | 21.2 (OK, standard MSSM) | ✅ |
| α₁⁻¹(M_Z) = 40.8 + 21.2 | 62.0 | 62.0 (if GUT value were correct) | 🟡 |
| α_em⁻¹(M_Z) = 62.0 × sin²θ_W | 127.95 | 127.95 (sin²θ_W = 0.2312 is PDG input) | 🟡 |
| α_em⁻¹(0) leptons only | 130.37 | 130.37 (standard) | 🟡 |

## Critical Issues

1. **The formula 4π/ε·κ² is ambiguous** — it could mean (4π/ε)·κ² = 0.3177 or 4π/(ε·κ²) = 20826 or 4π·κ/ε = 5.08. NONE gives 40.8.
2. **The "within 10% of MSSM 24" is wrong** — 40.8 is 70% above 24.
3. **sin²θ_W = 0.2312 is PDG input, not IDCM-derived** — so the "0.00% accuracy" for α_em⁻¹(M_Z) is circular.
4. **The RG running is standard MSSM**, not IDCM-specific.

## Conclusion

The document's "✅ 0.00%" claim is misleading. Only the RG arithmetic itself is correct. The GUT-scale coupling formula is broken.

## File Inventory

| File | Lines | Content |
|:-----|:-----:|:--------|
| verify.py | ~160 | Verification script |
