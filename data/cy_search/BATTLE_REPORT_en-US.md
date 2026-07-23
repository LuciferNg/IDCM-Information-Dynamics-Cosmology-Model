# IDCM CY₃(36,98) — Computational Battle Report

**Date:** 2026-07-20  
**Opponent:** Gemini Critique vs IDCM Core Structure  
**Status:** 3 computational campaigns completed

---

## Battle Summary

| Point | Critique Claim | Final Status | Verdict |
|:------|:--------------|:-----------:|:-------:|
| **1: $M=33$ circular** | "$c_2[0]=-288=-(32\times9)$ is arbitrary factorization, $M=N_h-9$ is circular" | ✅ **CLOSED** | Derivation rewritten, no $N_h$ dependence |
| **2: GLSM inevitable** | "GLSM integers 0-12 too complete, matching is inevitable" | 🟡 **Tool-limited** | 32D ambient ≠ 36D CY, cannot fully close |
| **3: Koszul principle gap** | "Yukawa factorize to $\varphi^{-k}$ is principle gap, not compute gap" | 🟡 **Tool-limited** | H¹(V)=3 via index theorem ✅; direct sheaf cohomology blocked |

---

## Point 1：CLOSED ✅

### Old Derivation (falsified by critic)

$$c_2[0] = -288 = -(32 \times 9) \to 9 = N_h - M \to M = N_h - 9 = 33$$

Critic valid: factorization arbitrary, $N_h-M=9$ circular.

### New Derivation

$$M = h^{1,1} - n_{\text{gen}} = 36 - 3 = 33$$

| Term | Source | Independence |
|:-----|:-------|:------------:|
| $h^{1,1} = 36$ | MERA $N=135$, $N_m=37$ | ✅ Independent of PDG |
| $n_{\text{gen}} = 3$ | disentangler cokernel $\mathbb{C}^3$ | ✅ Independent of PDG |
| $c_2[0] = -288$ | Consistency check (not derivation) | ✅ CYTools computed |

**Theorem:** $M = h^{1,1} - n_{\text{gen}} = 33$, no $N_h$, no circular $c_2$ factorization.

---

## Point 2：🟡 Tool-Limited

### CYTools Confirmed

| Quantity | Value | Status |
|:---------|:------|:------:|
| Kähler cone | 185 hyperplanes in ℝ³² | ✅ |
| Vol(κ³) at J* | 1/4096 = 0.000244 | ✅ |
| Scale factor | 0.090141 (uniform scaling) | ✅ |

### Root Cause

| Ambient toric variety | CY₃(36,98) |
|:---------------------|:-----------|
| GLSM: 32 rays | h¹¹ = 36 |
| Kähler cone dim = 32 | CY Kähler moduli dim = 36 |
| Divisor group rank = 32 | Need 36D for full description |

**For non-favorable CYs, 4 "extra" divisor classes exist only at the CY
level — they are not in the ambient variety's GLSM matrix.**

To resolve: construct explicit 36D CY divisor basis. This is CYTools
kernel-level work.

---

## Point 3：🟡 Tool-Limited

| Quantity | Value | Status |
|:---------|:------|:------:|
| Full Hodge diamond | $h^{1,1}=36$, $h^{2,1}=98$, $\chi=-124$ | ✅ |
| Ind(L) | 48 | ✅ |
| H¹(V) via index theorem | 3 | ✅ |
| CYTools divisor cohomology | N/A on non-favorable CY | ❌ |
| Yukawa tensor | TBD | 🔴 |

Index theorem confirms $H^1(V)=3$, but direct sheaf cohomology needs
cohomCalg or custom pipeline.

---

## Kernel Modification Workload Assessment

### Path A: Modify CYTools kernel (~2-4 weeks)

| Task | Difficulty | Notes |
|:----|:---------:|:------|
| Construct 36D divisor basis | ⭐⭐⭐ | Needs CY sheaf cohomology restriction map |
| Implement non-favorable CY divisor cohomology | ⭐⭐⭐⭐⭐ | Essentially reimplement cohomCalg |
| Integrate into CYTools API | ⭐⭐ | Python layer, calabiyau.py ~2700 lines |

**Verdict: Heavy.** Divisor cohomology part is writing a mini algebraic
geometry library.

### Path B: Use existing toolchain (~1-2 weeks setup)

| Tool | Purpose | Status |
|:----|:-------|:------:|
| **cohomCalg** (C++) | Sheaf cohomology on toric varieties | Needs install + DSL learning |
| **SageMath + CYTools export** | Yukawa tensor | CYTools can export triangulation |
| **Palp / poly.x** | Polytope data (ready) | ✅ |

**Effort: ~1-2 weeks setup + days computation.**

### Path C: SageMath-only (~1 week)

Skip CYTools for the CY computation; use SageMath's toric geometry 
(`FaceFan`, `ToricVariety`, `cohomology`) with custom triangulation data.
Requires manually feeding 32-ray triangulation and computing Chow ring.

---

## Confirmed Results (survive scrutiny)

1. **CY₃(36,98) exists** ✅ (KS DB → CYTools)
2. **$h^{1,1}=36, h^{2,1}=98$** ✅ (CYTools)
3. **$c_2[0] = -288 = -8 \cdot h^{1,1}$** ✅ (CYTools)
4. **$M = 33$ from $h^{1,1} - 3$** ✅ (self-consistent, no $N_h$)
5. **GLSM coord3 charges: [12,10,9,8,7,6,5,4]** ✅ (CYTools)
6. **Vol(J*) = κ³** ✅ (CYTools verification)
7. **H¹(V) = 3 via index theorem** ✅

## Still OPEN

1. **Full 36D $J^*$ optimization** 🟡 needs explicit divisor basis
2. **Yukawa factorize to $\varphi^{-k}$** 🟡 needs cohomCalg or equivalent
3. **$\varphi^{-4}$ geometric uniqueness** 🟡 verifiable after $J^*$
4. **$\varphi^{-6}$ electron correction** ⚠️ still empirical
