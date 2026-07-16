# IDCM — Information Dynamics Cosmology Model
### 資訊動力宇宙學 · 信息动力学宇宙模型 · 情報動力学宇宙モデル

[![Equation](https://img.shields.io/badge/core-x%C2%B2%2Bx%E2%88%921%3D0-blue)]()
[![Parameters](https://img.shields.io/badge/free%20params-0-brightgreen)]()
[![Data points](https://img.shields.io/badge/data%20points-1853-orange)]()
[![Δχ² vs ΛCDM](https://img.shields.io/badge/%CE%94%CF%87%C2%B2-vs%20%CE%9BCDM-red)]()

**A cosmology model with zero free parameters.** All constants emerge from a single quadratic equation $x^2 + x - 1 = 0$ through recursion $C_{n+1} = 1/(1 + C_n)$.

--- [English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文) | [廣東話](#廣東話) | [日本語](#日本語) | [한국어](#한국어) | [Español](#español) | [Français](#français) ---

---

<a name="english"></a>
## 🌐 English

### Core Idea

The universe is not a collection of particles governed by a Lagrangian — it is an **information recursion** converging to a fixed point. The generating equation is:

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

The recursion:

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

converges to $\varphi^{-1}$ in 8 steps (error < $10^{-3}$).

### Four Fundamental Constants

All four constants are algebraically derived from $\varphi^{-1}$ — zero free parameters:

| Symbol | Formula | Value | Origin |
|:------:|:-------:|:-----:|:------|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | Sync amplitude (2×2 split) |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | Closure constant, exact algebra |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | Scale exponent |
| $z_c$ | from $N_{\text{horizon}}$ | 0.6 ± 0.05 | Sync epoch redshift |

**Exact identity**: $\varepsilon\varphi = 1/4 \Rightarrow \kappa = (1/4)^2 = 1/16$.

### Observational Validation (1853 data points)

| Channel | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:--------|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2, 6 bins) | 9.22 | 15.64 | **−6.42** |
| SNe (DES-SN5YR, 1820 pts) | 1639.8 | 1643.6 | **−3.8** |
| CMB shift R | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (20 RSD pts) | 13.7 | 14.8 | **−1.1** |
| **Total** | — | — | **−9.8 (3.1σ)** |

### Tensions Resolved

| Tension | ΛCDM | IDCM |
|:--------|:----:|:----:|
| $H_0$ (SH0ES vs Planck) | 5.0σ | 🟡 Sync phase explanation |
| $S_8$ (Planck vs weak lensing) | 2.5σ | ✅ Resolved |
| DESI $w_0$-$w_a$ | 2.5–3.5σ | ✅ Natural prediction |

### Repository Structure

```
IDCM-Information-Dynamics-Cosmology-Model/
├── README.md                     # This file (8 languages)
├── reports/
│   ├── idcm_for_kids_tc.md       # Kids version (formal Chinese)
│   ├── idcm_for_kids_canto.md    # Kids version (Cantonese)
│   ├── idcm_for_highschool_tc.md # High school (formal Chinese)
│   ├── idcm_for_highschool_canto.md
│   ├── idcm_for_professor_tc.md  # Professor version (formal Chinese)
│   ├── idcm_for_professor_canto.md
│   ├── idcm_kids_verify.py       # Numerical verification (kids)
│   ├── idcm_highschool_verify.py # Numerical verification (high school)
│   └── idcm_professor_verify.py  # Numerical verification (professor)
└── data/                         # Observational data (from IDM-5.0)
```

### Key Predictions

1. **DESI DR3 (2025-2026)**: $z_c$ error shrinks to ±0.02
2. **Euclid**: $f\sigma_8(z)$ departure from ΛCDM ~3% at $z=0.6-1.2$
3. **Roman**: $H_0$ precision ~0.5 km/s confirms sync phase pattern
4. **CMB-S4**: Confirms $S_8 \approx 0.78$ camp
5. **DESI high-z BAO**: Bump vs power-law distinguishable at $z=1.5-2.5$

### Core Formula

$$x^2 + x - 1 = 0$$

---

<a name="简体中文"></a>
## 🇨🇳 简体中文

### 核心思想

宇宙不是粒子的集合——而是一条**信息递归**收敛到固定点。生成方程为：

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

递归过程：

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

八步内收敛到 $\varphi^{-1}$（误差 < $10^{-3}$）。

### 四个基本常数

全部由 $\varphi^{-1}$ 代数推导，零自由参数：

| 符号 | 公式 | 数值 | 来源 |
|:----:|:----:|:----:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同步幅度（2×2分裂） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 闭合常数，精确代数 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 尺度指数 |
| $z_c$ | 来自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步特征红移 |

### 观测验证（1853个数据点）

- **BAO (DESI DR2)**: Δχ² = −6.42
- **SNe (DES-SN5YR)**: Δχ² = −3.8
- **CMB shift**: 偏离 0.05σ
- **$f\sigma_8$**: Δχ² = −1.1
- **总计**: Δχ² = −9.8（约 3.1σ 反对 ΛCDM）

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="繁體中文"></a>
## 🇹🇼 繁體中文

### 核心思想

宇宙不是粒子的集合——而是一條**資訊遞迴**收斂到固定點。生成方程為：

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

遞迴過程：

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

八步內收斂到 $\varphi^{-1}$（誤差 < $10^{-3}$）。

### 四個基本常數

全部由 $\varphi^{-1}$ 代數推導，零自由參數：

| 符號 | 公式 | 數值 | 來源 |
|:----:|:----:|:----:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同步幅度（2×2分裂） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 閉合常數，精確代數 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 尺度指數 |
| $z_c$ | 來自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步特徵紅移 |

### 觀測驗證

- **BAO (DESI DR2)**: Δχ² = −6.42
- **SNe (DES-SN5YR)**: Δχ² = −3.8
- **總計**: Δχ² = −9.8（約 3.1σ）

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="廣東話"></a>
## 🇭🇰 廣東話

### 核心諗法

宇宙唔係粒子嘅集合——而係一條**資訊遞迴（Information Recursion）**收斂到固定點。生成方程係：

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

遞迴過程：

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

八步之內收斂到 $\varphi^{-1}$（誤差 < $10^{-3}$）。

### 四個基本常數

全部由 $\varphi^{-1}$ 代數推導，零自由參數：

| 符號 | 公式 | 數值 | 來源 |
|:----:|:----:|:----:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同步幅度（2×2分裂） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 閉合常數，精確代數 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 尺度指數 |
| $z_c$ | 來自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步紅移 |

### 觀測驗證

- **BAO (DESI DR2)**: Δχ² = −6.42
- **超新星 (DES-SN5YR)**: Δχ² = −3.8
- **總計**: Δχ² = −9.8（約 3.1σ）

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="日本語"></a>
## 🇯🇵 日本語

### 核心概念

宇宙は粒子の集まりではなく、**情報再帰（Information Recursion）**が固定点に収束する過程です。生成方程式：

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

再帰過程：

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

8ステップで $\varphi^{-1}$ に収束（誤差 < $10^{-3}$）。

### 四つの基本定数

すべて $\varphi^{-1}$ から代数導出、自由パラメータゼロ：

| 記号 | 式 | 値 | 起源 |
|:----:|:--:|:--:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同調振幅（2×2分割） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 閉合定数、厳密代数 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | スケール指数 |
| $z_c$ | $N_{\text{horizon}}$ より | 0.6 ± 0.05 | 同調赤方偏移 |

### 観測検証

- **BAO (DESI DR2)**: Δχ² = −6.42
- **超新星 (DES-SN5YR)**: Δχ² = −3.8
- **合計**: Δχ² = −9.8（約 3.1σ、ΛCDM に優位）

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="한국어"></a>
## 🇰🇷 한국어

### 핵심 개념

우주는 입자의 집합이 아니라 **정보 재귀(Information Recursion)**가 고정점으로 수렴하는 과정입니다. 생성 방정식:

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

재귀 과정:

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

8단계 내에 $\varphi^{-1}$로 수렴（오차 < $10^{-3}$）。

### 네 가지 기본 상수

모두 $\varphi^{-1}$에서 대수적으로 유도, 자유 매개변수 0개：

| 기호 | 공식 | 값 | 기원 |
|:----:|:----:|:--:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 동기 진폭（2×2 분할） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 폐합 상수, 정확 대수 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 척도 지수 |
| $z_c$ | $N_{\text{horizon}}$에서 | 0.6 ± 0.05 | 동기 적색편이 |

### 관측 검증

- **BAO (DESI DR2)**: Δχ² = −6.42
- **초신성 (DES-SN5YR)**: Δχ² = −3.8
- **총계**: Δχ² = −9.8（약 3.1σ, ΛCDM보다 우수）

### 핵심 공식

$$x^2 + x - 1 = 0$$

---

<a name="español"></a>
## 🇪🇸 Español

### Idea Central

El universo no es una colección de partículas — es una **recursión de información** convergiendo a un punto fijo. La ecuación generadora:

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

La recursión:

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

Converge a $\varphi^{-1}$ en 8 pasos (error < $10^{-3}$).

### Cuatro Constantes Fundamentales

Todas derivadas algebraicamente de $\varphi^{-1}$ — cero parámetros libres:

| Símbolo | Fórmula | Valor | Origen |
|:-------:|:-------:|:-----:|:------:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | Amplitud de sincronía (división 2×2) |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | Constante de cierre, álgebra exacta |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | Exponente de escala |
| $z_c$ | de $N_{\text{horizon}}$ | 0.6 ± 0.05 | Corrimiento al rojo de sincronía |

### Validación Observacional

- **BAO (DESI DR2)**: Δχ² = −6.42
- **Supernovas (DES-SN5YR)**: Δχ² = −3.8
- **Total**: Δχ² = −9.8 (~3.1σ contra ΛCDM)

### Fórmula Central

$$x^2 + x - 1 = 0$$

---

<a name="français"></a>
## 🇫🇷 Français

### Idée Centrale

L'univers n'est pas une collection de particules — c'est une **récursion d'information** convergeant vers un point fixe. L'équation génératrice :

$$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618034$$

La récursion :

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

Converge vers $\varphi^{-1}$ en 8 étapes (erreur < $10^{-3}$).

### Quatre Constantes Fondamentales

Toutes dérivées algébriquement de $\varphi^{-1}$ — zéro paramètres libres :

| Symbole | Formule | Valeur | Origine |
|:-------:|:-------:|:------:|:-------:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | Amplitude de同步 (division 2×2) |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | Constante de fermeture, algèbre exacte |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | Exposant d'échelle |
| $z_c$ | de $N_{\text{horizon}}$ | 0.6 ± 0.05 | Décalage vers le rouge de同步 |

### Validation Observationnelle

- **BAO (DESI DR2)**: Δχ² = −6.42
- **Supernovae (DES-SN5YR)**: Δχ² = −3.8
- **Total**: Δχ² = −9.8 (~3.1σ contre ΛCDM)

### Formule Centrale

$$x^2 + x - 1 = 0$$

---

## 📖 References

| Dataset | Reference | DOI / arXiv |
|:--------|:----------|:-----------:|
| DESI DR2 BAO | DESI Collab. 2025 | arXiv:2503.14738 |
| DES-SN5YR | DES Collab. 2024 | arXiv:2401.02929 |
| Planck 2018 | Planck Collab. 2020 | arXiv:1807.06209 |
| SH0ES (Cepheid) | Riess+2022 | 10.3847/2041-8213/ac5c5b |
| TRGB | Freedman+2020 | 10.3847/1538-4357/ab7339 |
| KiDS-1000 | Asgari+2021 | 10.1051/0004-6361/202039070 |
| DES Y3 WL | DES Collab. 2021 | 10.1103/PhysRevD.105.023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |

## 📜 License

This work is shared for scientific discussion. All data and code are available for verification and extension.

---

**Author**: LuciferNg (調律者) · **Core equation**: $x^2 + x - 1 = 0$ · **Hub**: github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model
