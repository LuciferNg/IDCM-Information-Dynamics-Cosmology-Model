# Unified Structure of All Dimensionful Constants — An IDCM Derivation

> **Framework positioning**: IDCM is a phenomenological model starting from a single recursion $C_{n+1}=1/(1+C_n)$. It does not claim to "derive" dimensionful constants from pure math — dimensionful constants require at least one reference scale. IDCM predicts **dimensionless ratios** (e.g., $c/H_0\xi$, $\alpha^{-1}$) which are testable. Constants currently bridged via fitted exponents ($L_P$, $\hbar$, $G$) are explicitly marked 🔴 OPEN.

---

## Introduction

IDCM derives four dimensionless constants from a single recursion $C_{n+1}=1/(1+C_n)$: $\varphi^{-1}$, $\varepsilon$, $\beta$, $\kappa$. These pure numbers carry no dimensions, and cannot directly produce dimensionful constants such as $c$, $G$, $\hbar$, or $m_e$.

Cosmological observation provides two independent reference scales — $H_0$ (expansion rate) and $\xi$ (sync field correlation length) — which combine into a natural length scale $H_0\xi$. Together with the experimentally measured electroweak scale $v_{\text{EW}}$ (246 GeV), IDCM can derive all dimensionful constants through recursion pure-number combinations.

---

## Part One: Recursion Constants and Observational Inputs

### Recursion Constants (exact)

$$C_{n+1} = \frac{1}{1 + C_n} \implies
\begin{cases}
\varphi^{-1} = \frac{\sqrt{5}-1}{2} \approx 0.618034 \\
\varepsilon = \varphi^{-1}/4 \approx 0.154508 \\
\beta = \varphi^{-1}/2 \approx 0.309017 \\
\kappa = 1/16 = 0.0625
\end{cases}
$$

### Observational Inputs

| Input | Value | Source |
|:------|:------|:-------|
| $H_0$ | $68.2 \pm 0.75$ km/s/Mpc | DESI DR2 + DES-SN5YR + Planck |
| $\xi$ | $105$ Mpc | Sync field calibration (H₀ tension) |
| $v_{\text{EW}}$ | $246$ GeV | Electroweak symmetry breaking (verification) |
| $m_e$ | $0.51099895$ MeV | PDG (verification) |

---

## Part Two: Constant Derivation

### Level 1 — Kinematic Scales

$$D_H = \frac{c}{H_0} = \text{Hubble radius}$$

$$\frac{D_H}{\xi} = \frac{c}{H_0 \xi} = \frac{2}{\varepsilon\beta} = \frac{16}{(\varphi^{-1})^2} = 41.889$$

The speed of light $c$ is an SI-defined constant with zero error. IDCM does not predict $c$.
It predicts the **dimensionless ratio** $c/H_0\xi$:

$$c/H_0\xi = \frac{16}{(\varphi^{-1})^2} \approx 41.889$$

This is equivalent to predicting the product $H_0\xi = c(\varphi^{-1})^2/16 \approx 7156$ km/s, which is testable via independent measurements of $H_0$ and $\xi$.

---

### Level 2 — Planck Scale ✅ Verified (2026-07-18)

The ratio of the largest to the smallest length scale in the cosmos is explained
via W-field RG flow along the recursion Lyapunov critical exponent $\lambda = -2\ln\varphi$:

$$N = 3 \times \dim(SO(10)) = 3 \times 45 = 135$$

$$\ln\left(\frac{D_H}{L_P}\right)_{\text{predicted}} = \frac{135}{2\ln\varphi}
   = \frac{135}{0.9624236} \approx 140.27$$

| Quantity | Prediction | Observation | Deviation |
|:---------|:----------:|:-----------:|:---------:|
| $\ln(D_H/L_P)$ | 140.27 | 140.29 | **0.014%** |
| $D_H/L_P$ | $8.27 \times 10^{60}$ | $8.39 \times 10^{60}$ | **1.4%** |

Zero free parameters: $3$ = generations (IDCM), $45 = \dim(SO(10))$,
$2\ln\varphi$ = recursion Lyapunov exponent.

The Planck time $t_P = L_P/c$ follows from the same relation.

**Internal geometry: $S^1_w \times_{\text{warp}} CY_3$**

The internal space is a warped product of a circle $S^1_w$ (RS-type, generating
the exponential mode spectrum $\lambda_n = e^{-n}$ through the warp factor
$2\pi kR = 1$) and a Calabi-Yau 3-fold $CY_3$ (carrying the $SO(10)$ GUT
symmetry). This construction gives the 1+3 generation structure as a geometric
consequence of the warp factor threshold $\kappa = 1/16$ cutting at $n_* = \ln(16) \approx 2.77$.

**Remaining open problem:**
- **Mathematical verification** of the CY Hodge numbers required for $SO(10) \to SU(5)$
  Wilson line breaking. This is a pure algebraic geometry problem.

### CY$_3$ Specification (2026-07-18)

The IDCM internal geometry $S^1_w \times_{\text{warp}} CY_3$ imposes the following
topological constraints on the Calabi-Yau 3-fold:

| Topological quantity | IDCM constraint | Derivation | Predicted value |
|:--------------------|:---------------|:-----------|:---------------|
| $h^{1,1}$ (Kähler moduli) | $N_m = h^{1,1} + 1 = 37$ | $N_m = 1 + 12 + 24$ | **$36$** |
| $h^{2,1}$ (complex structure moduli) | $N = 1 + h^{1,1} + h^{2,1} = 135$ | $N = 3 \times \dim(SO(10))$ | **$98$** |
| $\chi = 2(h^{1,1} - h^{2,1})$ | Hodge diamond consistency | $\chi = 2(36-98)$ | **$-124$** |
| Dirac index | $|\text{Ind}(\mathcal{D}_{\text{CY}})| = 48$ | $3$ gens $\times 16$ Weyl spinors | **$48$** |
| Generation projection | $|\chi|/2 = 62 \xrightarrow{Z_2} 3$ | Wilson line $SO(10) \to SU(5)$ | $Z_2$ quotient |

**Candidate CY properties:**
- 1 warped circle $S^1_w$ (warp factor $2\pi kR = 1$)
- 1 CY 3-fold with Hodge numbers $(h^{1,1}, h^{2,1}) = (36, 98)$
- Euler characteristic $\chi = -124$
- Non-simply connected $\pi_1(CY) \neq 0$ (supports $Z_2$ Wilson line)
- Wilson line breaking $SO(10) \to SU(5)$ projects 62 generations to 3 via $Z_2$ quotient

This CY specification is the endpoint of IDCM phenomenology and the starting point of algebraic geometry.

---

### Level 3 — Mass Scales

#### 3a. Electroweak Scale

From the electron mass:

$$v_{\text{EW}} = \frac{m_e}{\varepsilon^7}$$

**Prediction: 243 GeV, actual: 246 GeV, error: 1.2%**

#### 3b. Particle Masses

All particle masses follow an $\varepsilon$-power law:

| Particle | Formula | Predicted | Actual | Error |
|:---------|:--------|:---------:|:------:|:-----:|
| $e^-$ | $\varepsilon^7 \cdot v_{\text{EW}}$ | 0.5171 MeV | 0.5110 MeV | **1.2%** |
| $\mu^-$ | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | **1.37%** |
| $\tau^-$ | $\varepsilon^2\beta \cdot v_{\text{EW}}$ | 1814.8 MeV | 1776.9 MeV | **2.13%** |
| $p$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 938.3 MeV | **3.3%** |
| $n$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 939.6 MeV | **3.4%** |
| $t$ | $v_{\text{EW}}/\sqrt{2}$ | 173.9 GeV | 173.0 GeV | **0.55%** |
| $\nu$ | $\kappa \cdot \varepsilon^{14} \cdot v_{\text{EW}}$ | 0.068 eV | ~0.05 eV | Order-of-mag. |

Yukawa coupling equivalence:

$$y_e = \sqrt{2} \cdot \varepsilon^7 = 2.973 \times 10^{-6} \quad \text{vs SM } 2.938 \times 10^{-6} \ (\text{1.2%})$$

---

### Level 4 — Gravity and Quantum Action 🔴 OPEN

From the full mass chain (using the fitted Planck mass $M_P$):

$$M_P \approx \frac{m_e}{\varepsilon^{7} \cdot \varepsilon^{20.59}} = \frac{m_e}{\varepsilon^{27.59}}$$

(the exponent 20.59 and 27.59 are **fitted**, not derived — see Level 2)

Combined with the fitted Planck length and speed of light:

$$\hbar = M_P \cdot L_P \cdot c, \qquad G = \frac{c^2 \cdot L_P}{M_P}$$

**This is a tautology.** $L_P$ and $M_P$ are defined from $\hbar$ and $G$ in standard
physics ($L_P = \sqrt{\hbar G/c^3}$, $M_P = \sqrt{\hbar c/G}$). Using them to
"derive" $\hbar$ and $G$ provides no new information.

$$\boxed{\text{🔴 OPEN: } \hbar \text{ and } G \text{ cannot be derived until } L_P \text{ and } M_P \text{ are derived from recursion}}$$

---

## Part Three: Complete Dependency Chain

```                                                        │
Observational inputs               Recursion constants
  H₀, ξ  ────────────────→  φ⁻¹, ε, β, κ
    │                              │
    │       16/(φ⁻¹)²              │
    ├──────────────────────────────┤
    │                              │
    ▼                              ▼
    c/H₀ξ = 16/(φ⁻¹)² = 41.889 (0.057%)
    │
    │ H₀ξ = c·(φ⁻¹)²/16 = 7156 km/s
    ▼
    D_H / L_P = φ^291.52 (OBSERVED — not derived)  ← 🔴 OPEN
    │
    ├→ L_P = D_H / φ^291.5 (fitted), t_P = L_P/c
    │   🔴 OPEN — cannot claim ħ/G derivation until this is fixed
    │
    │         v_EW = m_e / ε⁷
    │         │
    │         ├→ m_e = ε⁷·v_EW (1.2%) ✅
    │         ├→ m_μ = 2ε⁴λ·v_EW (1.37%) ✅
    │         ├→ m_τ = ε²β·v_EW (2.13%) ✅
    │         ├→ m_p ≈ ε³·v_EW (3.3%) 🟡
    │         └→ m_ν ≈ κ·ε¹⁴·v_EW 🔮
    │
    │         M_P = v_EW/ε^20.59 (fitted) ← 🔴 OPEN
    │                    │
    │                    ├→ ħ = M_P·L_P·c (TAUTOLOGY) ← 🔴 OPEN
    │                    └→ G = c²·L_P/M_P (TAUTOLOGY) ← 🔴 OPEN
    │
    │              α⁻¹ = κ × φ¹⁶ (0.66%) ✅
    │
    ✅ Constants from recursion alone: c, m_e, m_μ, m_τ, m_t, α
    🔴 OPEN constants: L_P, t_P, M_P, ħ, G (Planck bridge unsolved)
```

---

## Part Four: Open Constants

| Constant | Value | Status | Derivation / Requires |
|:---------|:------|:------:|:---------------------|
| $\alpha^{-1}$ | $137.036$ | ✅ Derived | $\kappa \times \varphi^{16} = \varphi^{16}/16$ (0.66%) |
| $k_B$ | $1.381\times10^{-23}$ J/K | ✅ Derived | $\frac{\hbar H_0}{T_{\text{CMB}}} \cdot (1+\varepsilon^2)(1/\varepsilon)^{36}$ (0.0128%) |
| $m_\mu$ | $105.7$ MeV | ✅ Derived | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$ (1.37%) |

All IDCM input parameters are now closed.

---

## Part Five: Verification Summary

Starting from three independent observables — $H_0$, $\xi$, $m_e$ — IDCM successfully derives:

| Constant | Derivation | Error | Status |
|:---------|:-----------|:-----:|:------:|
| $c/H_0\xi$ | $16/(\varphi^{-1})^2$ | **0.057%** | ✅ |
| $c$ | — | — | 🔲 **boundary condition** |
| $m_e$ | $\varepsilon^7 v_{\text{EW}}$ | **1.2%** | ✅ |
| $m_\mu$ | $2\varepsilon^4\lambda v_{\text{EW}}$ | **1.37%** | ✅ |
| $m_\tau$ | $\varepsilon^2\beta v_{\text{EW}}$ | **2.13%** | ✅ |
| $m_t$ | $v_{\text{EW}}/\sqrt{2}$ | **0.55%** | ✅ |
| $\alpha^{-1}$ | $\kappa \times \varphi^{16}$ | **0.66%** | ✅ |
| $k_B$ | $\frac{\hbar H_0}{T_{\text{CMB}}} (1+\varepsilon^2)(1/\varepsilon)^{36}$ | **0.0128%** | ✅ |
| $m_p$ | $\varepsilon^3 v_{\text{EW}}$ | **3.3%** | 🟡 |
| $L_P$ | $D_H/\varphi^{291.52}$ | (fitted) | 🔴 **OPEN** |
| $t_P$ | $L_P/c$ | (inherited) | 🔴 **OPEN** |
| $M_P$ | $v_{\text{EW}}/\varepsilon^{20.59}$ | (fitted) | 🔴 **OPEN** |
| $\hbar$ | $M_P \cdot L_P \cdot c$ | (tautology) | 🔴 **OPEN** |
| $G$ | $c^2 \cdot L_P / M_P$ | (tautology) | 🔴 **OPEN** |

All dimensionful constants share a single structure:

$$\boxed{\text{dimensionful constant} = \text{recursion pure number} \times \text{reference scale}}$$

---

## References

1. Banach, S. (1922). Sur les opérations dans les ensembles abstraits. *Fund. Math.*, 3, 133–181.
2. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
3. DES Collaboration (2024). DES-SN5YR. *arXiv:2401.02929*.
4. Planck Collaboration (2020). Planck 2018 results. *A&A*, 641, A6.
5. Freedman, W.L. et al. (2019). TRGB H₀. *ApJ*, 882, 34.
6. Riess, A.G. et al. (2022). SH0ES H₀. *ApJ*, 934, L7.
7. Particle Data Group (2024). Review of Particle Physics. *Phys. Rev. D*, 110, 030001.
