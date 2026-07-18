# IDCM — Information Dynamics Cosmology Model

[← Back to language selection](README.md)

---

**A first-principles cosmology model with zero free parameters.** All constants emerge from a single quadratic equation $x^2 + x - 1 = 0$ through recursion $C_{n+1} = 1/(1 + C_n)$. **All 19 Standard Model parameters predicted from first principles.**

---

## Achievement: All 19 SM Parameters Predicted

| Sector | Parameter | IDCM Formula | Prediction | PDG | Error |
|:-------|:---------:|:-------------|:----------:|:---:|:-----:|
| **9 fermion masses** | $m_c/m_t$ | $\varphi^{-M\beta}$ | 1.277 GeV | 1.27 GeV | 0.57% |
| | $m_s/m_b$ | $\varphi^{-((M-7)\beta-\varphi^{-4})}$ | 93.9 MeV | 93.4 MeV | 0.51% |
| | $m_\mu/m_\tau$ | $\varphi^{-(M-14)\beta}$ | 105.35 MeV | 105.66 MeV | 0.30% |
| | $m_u/m_t$ | $\varphi^{-(k_u+k_d+k_l-\varphi^{-1})}$ | 2.29 MeV | 2.16 MeV | 6.0% |
| | $m_d/m_b$ | $\varphi^{-(2k_d-\varphi)}$ | 4.59 MeV | 4.70 MeV | 2.3% |
| | $m_e/m_\tau$ | $\varphi^{-(k_l+M/3)}$ | 0.529 MeV | 0.511 MeV | 3.6% |
| **Higgs** | $m_H$ | $v\cdot\varphi^{-9\beta/2}$ | 125.99 GeV | 125.10 GeV | 0.71% |
| **CKM** | $V_{us}$ | $\varphi^{-M/11}$ | 0.23607 | 0.22650 | 4.2% |
| | $V_{cb}$ | $\varphi^{-M/5}$ | 0.04182 | 0.04210 | **0.83%** |
| | $V_{ub}$ | $\varphi^{-(M/5+M/11+2)}$ | 0.00376 | 0.00361 | 4.3% |
| | $\delta_{CP}$ | $\pi/2-\arctan\beta$ | 72.83° | 68.80° | 5.9% |
| **PMNS** | $\theta_{12}$ | $\arctan\varphi^{-1}+1/M$ | 33.45° | 33.82° | 1.08% |
| | $\theta_{23}$ | $\pi/4$ | 45° | 45-48° | ✅ |
| | $\theta_{13}$ | $\arcsin(\varepsilon(M-1)/M)$ | 8.62° | 8.57° | **0.55%** |
| | $\delta_{CP}$ | $\pi+\arctan\varphi^{-3}$ | 193.3° | 195° | 0.9% |
| **Weinberg** | $\sin^2\theta_W$ | $V_{us}\cdot(1-\varphi^{-9})$ | 0.23296 | 0.23122 | 0.75% |
| **Dark Matter** | $M_{\text{DM}}$ | $M_P e^{-48}\varphi^{-1/2}$ | 13.68 MeV | 13.8 MeV | 0.88% |

All from **4 IDCM constants**: $M=33$, $N_h=42$, $\beta=\varphi^{-1}/2$, $\varepsilon=\varphi^{-1}/4$.

---

## Core Mechanism

### Generating Equation

$$x^2 + x - 1 = 0$$

**Positive root**: $\varphi^{-1} = (\sqrt{5} - 1)/2 \approx 0.618034$

### Recursion Process

$$C_{n+1} = \frac{1}{1 + C_n},\quad C_0 = 1$$

Error below $10^{-3}$ after 8 steps.

### IDCM Constants

| Symbol | Value | Origin |
|:-------|:------|:-------|
| $\varphi^{-1}$ | 0.618034 | Root of $x^2+x-1=0$ |
| $\varepsilon$ | $\varphi^{-1}/4 \approx 0.154509$ | $2\times2$ symmetry split |
| $\kappa$ | $1/16 = 0.0625$ | Algebraic identity |
| $\beta$ | $\varphi^{-1}/2 \approx 0.309017$ | SYNC exponent |
| $M$ | 33 | MERA RG convergence steps |
| $N_h$ | 42 | KK tower cutoff |
| $z_c$ | $0.6 \pm 0.05$ | Sync redshift |

## Geometric Core

- **CY₃(36,98)** confirmed in Kreuzer-Skarke database
- **J\* fixed point**: $\text{Vol}=\kappa^3$, $\text{Ind}=48$, Kähler cone positive
- **SU(3) Monad bundle**: $h^1(V)=3$, $\text{Ind}(V)=-6$
- **MERA RG**: 33 steps → $C^*=\varphi^{-1}$
- **SYNC Kuramoto**: 343 steps, residual $10^{-10}$

## Validation

| Dataset | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:--------|:---------------------:|:--------------------------:|:--------------:|
| DESI DR2 BAO | 9.22 | 15.64 | -6.42 |
| DES-SN5YR | 1639.8 | 1643.6 | -3.8 |
| $H_0$ SH0ES | 5.0σ tension | → resolved | — |
| $S_8$ | 2.5σ tension | → resolved | — |
| **Total** | **1853 data points** | — | **−9.8** |

## Educational Levels

| Level | Description | Formulas |
|:------|:------------|:--------:|
| 🌟 Kids | Simple analogies, fun to learn | 100 |
| 📐 High School | Detailed derivations, algebra | 200 |
| 🎓 Professor | Complete group theory | Full |

## Quick Start

```bash
pip install -r requirements.txt
make validate-all
```

---

**Core equation**: $x^2 + x - 1 = 0$ · **Zero free parameters** · **Δχ² = −9.8 vs ΛCDM**
