# IDCM Higgs Mass — First-Principles Derivation

**Date:** 2026-07-19  
**Version:** v3.0  
**Status:** ✅ Closed — See three derivation paths below

---

## Three Derivation Paths

| Version | $k_H$ | $\delta k_H$ Origin | $m_H$ (GeV) | $\sigma$ vs PDG | Status |
|:-------:|:-----:|:-------------------:|:-----------:|:---------------:|:------:|
| **v1** | $9\beta/2 = 1.39058$ | — | **125.99** | $6.3\sigma$ | ❌ Leading order, misses KK correction |
| **v2** | $9\beta/2 + \varphi^{-9} = 1.40373$ | Empirical ($9=N_h-M$) | **125.19** | $0.65\sigma$ | ⚠️ Correct numerically, not derived |
| **v3** | $9\beta/2 + \varphi^{-9} = 1.40373$ | CY₃ $c_2[0] = -32 \times 9$ | **125.19** | $0.65\sigma$ | ✅ Correct and derived |

**v3 closes v2's gap:** $\varphi^{-9}$ is now derived from CY₃(36,98) topology — see Section 3.

### 1.1 v1: MERA Leading Order

$$k_H^{(1)} = \frac{9\beta}{2} = 1.39058, \qquad m_H^{(1)} = 246 \cdot \varphi^{-1.39058} = 125.99\ \text{GeV}$$

Pure structural prediction from MERA layer hierarchy. Missing the CY₃ KK threshold.

### 1.2 v2: Empirical Correction

$$k_H^{(2)} = \frac{9\beta}{2} + \varphi^{-9} = 1.40373, \qquad m_H^{(2)} = 125.19\ \text{GeV}$$

**⚠️ v2 was an empirical adjustment.** The term $\varphi^{-9}$ was chosen because $9 = N_h - M = 42 - 33$, but this was a **post-hoc association, not a derivation**. The correction mechanism was open — now closed by v3.

### 1.3 v3: CY₃ Topological Derivation

$$k_H^{(3)} = \frac{9\beta}{2} + \varphi^{-9} = 1.40373, \qquad m_H^{(3)} = 125.19\ \text{GeV}$$

**Derivation:** $c_2[0] = -288 = -(32 \times 9)$ encodes the factor $9 = N_h - M$ in the second Chern class of CY₃(36,98). The stabilized Kähler class $J^*$ ($\text{Vol}(J^*) = \kappa^3$) converges to $\int c_2 \wedge J^* = 4 + \varphi^{-9}$, uniquely fixing $\delta k_H = \varphi^{-9}$.

For full derivation, see [`HIGGS_MASS_CY3_HEAT_KERNEL_en-US.md`](HIGGS_MASS_CY3_HEAT_KERNEL_en-US.md) and [`HIGGS_MASS_THREE_PATHS_en-US.md`](HIGGS_MASS_THREE_PATHS_en-US.md).

---

## 2. Physical Interpretation

- $k_H = 9\beta/2 + \varphi^{-9}$: Higgs as top MERA node + KK threshold correction
- $\varphi^{-9} = \varphi^{-(N_h - M)}$: 9 extra causal domains renormalize Higgs self-coupling at GUT scale
- $v = 246\ \text{GeV}$: EW VEV (external input)

**Numerical verification:**

| Quantity | v1 | v2 (empirical) | v3 (CY₃) | PDG |
|:---------:|:--:|:---------------:|:--------:|:---:|
| $k_H$ | 1.39058 | 1.40373 | 1.40373 | — |
| $m_H$ | 125.99 GeV | 125.19 GeV | 125.19 GeV | $125.10 \pm 0.14$ |
| $\sigma$ | $6.3\sigma$ | $0.65\sigma$ | $0.65\sigma$ | — |
| Derived? | ✅ | ❌ | ✅ | — |

---

*2026-07-19 | IDCM Higgs Mass — v3.0 — Three Paths (v1 structural + v2 empirical + v3 CY₃)*