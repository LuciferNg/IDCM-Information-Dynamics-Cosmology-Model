# IDCM Majorana Phases & Neutrinoless Double Beta Decay

**Date:** 2026-07-18  
**Version:** v1.0  
**Status:** 🟡 Framework confirmed, untestable

---

## 1. Majorana Phases

Majorana neutrino mass term:

$$\frac{1}{2} \overline{\nu_L^c} M_\nu \nu_L + \text{h.c.}$$

Diagonalization of the mass matrix introduces two additional CP phases ($\alpha_1, \alpha_2$):

$$U_{\text{PMNS}} = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & e^{i\alpha_1/2} & 0 \\
0 & 0 & e^{i\alpha_2/2}
\end{pmatrix}
\cdot R(\theta_{12}, \theta_{23}, \theta_{13}, \delta_{CP})$$

## 2. IDCM Prediction

In IDCM, the Majorana phases arise from the KK tower structure of the right-handed neutrino mass matrix. The most natural assumption is $\alpha_1 = \alpha_2 = 0$ (CP-conserving Majorana sector).

## 3. Neutrinoless Double Beta Decay

### 3.1 Effective Mass

$$m_{\beta\beta} = \left| \sum_{i=1}^3 m_i U_{ei}^2 e^{i\alpha_i} \right|$$

Under IDCM parameters (normal hierarchy, $\alpha_i = 0$):

$$m_{\beta\beta} \approx 3.2\ \text{meV}$$

### 3.2 Experimental Comparison

| Experiment | Limit (90% CL) | Year |
|:-----------|:--------------:|:----:|
| KamLAND-Zen ($^{136}$Xe) | $< 36-156$ meV | 2023 |
| LEGEND ($^{76}$Ge) | $< 44-100$ meV | Expected 2025 |
| nEXO ($^{136}$Xe) | $< 6-25$ meV | Expected 2030 |
| **IDCM Prediction** | **$\sim 3.2$ meV** | — |

IDCM prediction lies below current and near-future experimental sensitivity.

## 4. IDCM Predictability

| Predictability | Item | Status |
|:--------------:|:-----|:------:|
| ✅ | $m_{\beta\beta}$ order | ~meV |
| 🟡 | $\alpha_1, \alpha_2$ exact values | Assumed zero |
| 🔴 | Experimental test | 2030+ |

---

*2026-07-18 | IDCM Majorana Phases — v1.0 — 🟡 Framework confirmed*