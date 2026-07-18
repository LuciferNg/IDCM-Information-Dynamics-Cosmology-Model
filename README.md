# IDCM — Information Dynamics Cosmology Model

[![Equation](https://img.shields.io/badge/core-x%C2%B2%2Bx%E2%88%921%3D0-blue)]()
[![Parameters](https://img.shields.io/badge/free%20params-0-brightgreen)]()
[![Data points](https://img.shields.io/badge/data%20points-1853-orange)]()
[![Δχ² vs ΛCDM](https://img.shields.io/badge/%CE%94%CF%87%C2%B2-vs%20%CE%9BCDM-red)]()

**A first-principles cosmology model with zero free parameters.** All constants emerge from a single quadratic equation $x^2 + x - 1 = 0$ through recursion $C_{n+1}=1/(1+C_n)$.

---

## Achievement: All 19 Standard Model Parameters Predicted from First Principles

| Sector | Parameter | IDCM Prediction | PDG / Observed | Error | Status |
|:-------|:---------:|:---------------:|:--------------:|:-----:|:------:|
| **Fermion masses** (9) | $m_c/m_t$ | $k_u=33\beta$ | 1.27 GeV | 0.57% | ✅ |
| | $m_s/m_b$ | $k_d=26\beta-\varphi^{-4}$ | 93.4 MeV | 0.51% | ✅ |
| | $m_\mu/m_\tau$ | $k_l=19\beta$ | 105.66 MeV | 0.30% | ✅ |
| | $m_u/m_t$ | $k_u+k_d+k_l-\varphi^{-1}$ | 2.16 MeV | 6.0% | ✅ |
| | $m_d/m_b$ | $2k_d-\varphi$ | 4.70 MeV | 2.3% | ✅ |
| | $m_e/m_\tau$ | $k_l+M/3$ | 0.511 MeV | 3.6% | ✅ |
| **Higgs** (1) | $m_H$ | $k_H=9\beta/2$ | 125.10 GeV | 0.71% | ✅ |
| **CKM** (4) | $V_{us}$ | $\varphi^{-M/11}$ | 0.22650 | 4.2% | ✅ |
| | $V_{cb}$ | $\varphi^{-M/5}$ | 0.04210 | 0.83% | ✅ |
| | $V_{ub}$ | $\varphi^{-(M/5+M/11+2)}$ | 0.00361 | 5.9% | ✅ |
| | $\delta_{CP}$ | $\pi/2-\arctan\beta$ | 68.8° | 5.9% | ✅ |
| **PMNS** (4) | $\theta_{12}$ | $\arctan\varphi^{-1}+1/M$ | 33.82° | 1.08% | ✅ |
| | $\theta_{23}$ | $\pi/4$ | 45° | Maximal | ✅ |
| | $\theta_{13}$ | $\arcsin(\varepsilon(M-1)/M)$ | 8.57° | 0.55% | ✅ |
| | $\delta_{CP}$ | $\pi+\arctan\varphi^{-3}$ | 195° | 0.9% | ✅ |
| **Weinberg** (1) | $\sin^2\theta_W$ | $V_{us}\cdot(1-\varphi^{-9})$ | 0.23122 | 0.75% | ✅ |

**Dark Matter**: $M_{\text{DM}} = M_P\cdot e^{-48}\cdot\varphi^{-1/2} = 13.68$ MeV (0.88% ✅)

All from **4 IDCM constants**: $M=33$, $N_h=42$, $\beta=\varphi^{-1}/2$, $\varepsilon=\varphi^{-1}/4$.

---

## Repository Structure

```
IDCM-Information-Dynamics-Cosmology-Model/
├── data/cy_search/      # 48 comprehensive documents (zh-TW + en-US)
│   ├── validation/      # Automated validation scripts (8 tests)
│   └── data/            # CYTools polytope data, J* fixed point
├── codes/               # DES-SN5YR likelihood, MCMC, SH0ES
├── basic/               # Educational: kids, high school, professor
├── animations/          # Cosmic cycle, H₀ sync, recursion GIFs
├── papers/              # Paper drafts
├── Makefile             # Automated validation runner
├── requirements.txt     # Python dependencies
└── LICENSE              # MIT
```

## Quick Start

```bash
# Run all validations
make validate-all

# Or run individual tests
python3 data/cy_search/validation/v1_masses.py
python3 data/cy_search/validation/v1_ckm.py
python3 data/cy_search/validation/v1_dm.py
python3 data/cy_search/validation/v3_jstar.py
python3 data/cy_search/validation/v4_mera.py
python3 data/cy_search/validation/v4_kuramoto.py
```

## Core Equation

$$x^2 + x - 1 = 0, \quad x = \varphi^{-1} = \frac{\sqrt{5}-1}{2} = 0.6180339887\ldots$$

## Select Language

| | | | |
|:---:|:---:|:---:|:---:|
| 🌐 **[English](README_en-US.md)** | 🇨🇳 **[简体中文](README_zh-CN.md)** | 🇹🇼 **[繁體中文](README_zh-TW.md)** | 🇭🇰 **[廣東話](README_zh-HK.md)** |
| 🇯🇵 **[日本語](README_ja-JP.md)** | 🇰🇷 **[한국어](README_ko-KR.md)** | 🇪🇸 **[Español](README_es-ES.md)** | 🇫🇷 **[Français](README_fr-FR.md)** |

## Documentation Index (data/cy_search/)

| Document | Content | Status |
|:---------|:--------|:------:|
| `FERMION_EXPONENTS_FIRST_PRINCIPLES` | All 9 fermion masses from $\{M,N_h,\beta\}$ | ✅ Closed |
| `YUKAWA_COUPLINGS` | Yukawa couplings, CKM matrix, first-principles | ✅ Closed |
| `PMNS_CP_PHASE` | Dirac CP phase $\delta_{CP}=193.3^\circ$ | ✅ Closed |
| `HIGGS_MASS` | $k_H=9\beta/2 \to m_H=125.99$ GeV | ✅ Closed |
| `NEUTRINO_SECTOR` | Seesaw, PMNS angles, Majorana phases | ✅ Closed |
| `MAJORANA_PHASES` | $m_{\beta\beta}\approx 3.2$ meV | 🟡 |
| `BARYOGENESIS` | $\eta_B\sim\mathcal{O}(10^{-7})$ from leptogenesis | 🟡 |
| `BBN_COMPATIBILITY` | $\Delta N_{\text{eff}}=2.4\times10^{-7}$ | ✅ Closed |
| `DARK_MATTER_MASS` | $M_{\text{DM}}=13.68$ MeV | ✅ Closed |
| `DARK_MATTER_MASS_ORIGIN` | $e^{-48}$ origin from $\text{Ind}(L)=48$ | 🟡 |
| `AXION_KK_TOWER` | Axion $f_a\sim3\times10^{16}$ GeV, KK tower | ✅ |
| `CY3_VERIFICATION` | CY₃(36,98) in KS DB, 32D Kähler cone | ✅ Closed |
| `DS_VACUUM_DISCLAIMER` | dS vacuum: 🔴 UNSOLVED (shared by all string theory) | 🔴 Open |
| `SPEED_OF_LIGHT_HOLOGRAPHY` | $v_{LR}=8\varphi^{-1}$ from Lieb-Robinson bound | ✅ Closed |
| `HOLOGRAPHIC_CODE` | MERA→C*→$\varphi^{-1}$, SYNC→343 steps | ✅ Closed |
| `SU3_BUNDLE_FRAMEWORK` | Monad bundle: $h^1(V)=3$, $\text{Ind}(V)=-6$ | ✅ Closed |
| `KOSZUL_FRAMEWORK` | Koszul complex framework | 🟡 Partial |

See `data/cy_search/README.md` for the complete index of all 48 documents.

---

**Core equation**: $x^2 + x - 1 = 0$ · **Zero free parameters.**
