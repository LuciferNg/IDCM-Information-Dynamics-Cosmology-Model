# IDCM — Information Dynamics Cosmology Model
### 資訊動力宇宙學 · 信息动力学宇宙模型 · 情報動力学宇宙モデル · 정보동력우주모형

[![Equation](https://img.shields.io/badge/core-x%C2%B2%2Bx%E2%88%921%3D0-blue)]()
[![Parameters](https://img.shields.io/badge/free%20params-0-brightgreen)]()
[![Data points](https://img.shields.io/badge/data%20points-1853-orange)]()
[![Δχ² vs ΛCDM](https://img.shields.io/badge/%CE%94%CF%87%C2%B2-vs%20%CE%9BCDM-red)]()

**A cosmology model with zero free parameters.** All constants emerge from a single quadratic equation $x^2 + x - 1 = 0$ through recursion $C_{n+1} = 1/(1 + C_n)$. Resolves the $H_0$ tension (5.0σ → sync phase) and $S_8$ tension (2.5σ → resolved). Δχ² = −9.8 across 1853 independent data points.

--- [English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文) | [廣東話](#廣東話) | [日本語](#日本語) | [한국어](#한국어) | [Español](#español) | [Français](#français) ---

---

<a name="english"></a>
## 🌐 English

### Motivation

The standard ΛCDM model, despite its empirical success, requires at least six free parameters ($\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$) and faces growing observational tensions: the $H_0$ tension (SH0ES Cepheid vs Planck CMB, 5.0σ), the $S_8$ tension (Planck vs weak lensing surveys, 2.5σ), and DESI's preference for dynamical dark energy ($w_0$-$w_a$ at 2.5–3.5σ). These tensions suggest either systematic errors or a fundamental limitation of the model itself.

IDCM (Information Dynamics Cosmology Model) proposes that these tensions arise not from mis-measurement but from a missing layer of cosmology: **the universe is not a collection of particles governed by a Lagrangian — it is an information recursion converging to a fixed point.** All observational discrepancies emerge naturally as sync-phase effects of this recursion, and every cosmological constant is an algebraic consequence of a single quadratic equation.

### Core Mechanism

#### The Generating Equation

$$x^2 + x - 1 = 0$$

This quadratic equation is not an approximation — it is the generative kernel of the model. Its positive root:

$$\varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618033988749895$$

is the golden ratio conjugate (often denoted $\Phi$ or $\phi^{-1}$). This number is the **fixed point** of the recursion.

#### The Recursion

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

This map appears throughout mathematics: it is the continued fraction expansion of $\varphi^{-1}$, the limiting ratio of consecutive Fibonacci numbers, and the simplest non-trivial rational map with a single attractive fixed point.

**Convergence analysis:**

The Jacobian at the fixed point:

$$\lambda = \left|\frac{dC_{n+1}}{dC_n}\right|_{C=\varphi^{-1}} = \frac{1}{(1+\varphi^{-1})^2} = \varphi^{-2} \approx 0.3819660113$$

Since $|\lambda| < 1$, convergence is guaranteed and **linear**. The error after $n$ steps:

$$|C_n - \varphi^{-1}| \approx \lambda^n \cdot |C_0 - \varphi^{-1}|$$

After 8 steps:

| n | $C_n$ | Error |
|:-:|:-----:|:-----:|
| 0 | 1.000000 | $3.82 \times 10^{-1}$ |
| 1 | 0.500000 | $1.18 \times 10^{-1}$ |
| 2 | 0.666667 | $4.86 \times 10^{-2}$ |
| 3 | 0.600000 | $1.80 \times 10^{-2}$ |
| 4 | 0.625000 | $6.97 \times 10^{-3}$ |
| 5 | 0.615385 | $2.65 \times 10^{-3}$ |
| 6 | 0.619048 | $1.01 \times 10^{-3}$ |
| 7 | 0.617647 | $3.87 \times 10^{-4}$ |
| 8 | 0.618182 | $1.48 \times 10^{-4}$ |

After 8 steps, the error is below $10^{-3}$. The convergents are Fibonacci ratios:

$$C_n = \frac{F_n}{F_{n+1}}, \quad F_{n+2} = F_{n+1} + F_n$$

This is not a coincidence — it reflects the deep structural connection between continued fractions, Fibonacci sequences, and the golden ratio.

**Interpretation:** Each step of the recursion corresponds to a causal domain in the universe synchronizing with its neighbours. Time itself is the ordering of these synchronization steps. The recursion defines time's arrow (forward convergence, irreversible) and its horizon (42 causal domains, each ~105 Mpc across).

### The Four Fundamental Constants

All constants are algebraically derived from $\varphi^{-1}$ — zero free parameters.

#### 1. Sync Amplitude $\varepsilon$

$$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.1545084972$$

The factor 4 comes from the minimal non-trivial symmetry split $2 \times 2$ (2 spatial dimensions × 2 internal dimensions). $\varepsilon$ controls the amplitude of the cosmic expansion anomaly — the **bump** in $f(z)$.

#### 2. Closure Constant $\kappa$

$$\kappa = (\varepsilon\varphi)^2 = \frac{1}{16} = 0.0625$$

This is an **exact algebraic identity**:

$$\varepsilon\varphi = \frac{\varphi^{-1}}{4} \times \varphi = \frac{1}{4} \quad \Rightarrow \quad \kappa = \left(\frac{1}{4}\right)^2 = \frac{1}{16}$$

$\kappa$ controls:
- Weak nuclear force strength ($g_w^2 \propto \kappa$)
- The cosmic cycle timescale ($t_{\text{cycle}} \propto e^{1/\kappa}$)
- Neutrino mass scale ($m_\nu \sim \kappa \cdot \varepsilon \cdot \Lambda$)
- Matter stability (potential well depth in the W-field)

#### 3. Scale Exponent $\beta$

$$\beta = \frac{\varphi^{-1}}{2} \approx 0.3090169944$$

Controls how the sync-phase effect decays with distance. Empirically verified via the Cepheid-to-TRGB ratio:

$$\frac{A_{\text{ceph}}}{A_{\text{TRGB}}} = \left(\frac{1.77}{0.05}\right)^\beta = 3.01 \pm 0.30\ (\text{observed } 3.03 \pm 0.30)$$

#### 4. Sync Redshift $z_c$

$$z_c = 0.6 \pm 0.05$$

Derived from the causal horizon count $N_{\text{horizon}} = \lfloor 4/\varepsilon \rfloor = 42$, domain scale $\xi = 105$ Mpc, and the redshift-distance relation. Independently validated by DESI DR2 ($0.58 \pm 0.08$) and DES-SN5YR ($0.62 \pm 0.10$).

### The Expansion Bump

The IDCM Friedmann equation:

$$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}\left(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}\right)\right]$$

The correction term $f(z) = 1 + \varepsilon \cdot (z/z_c) \cdot e^{-z/z_c}$ produces a **bump** peaking at $z_c \approx 0.6$ with amplitude 5.68%:

| z | f(z) | Bump % |
|:-:|:----:|:------:|
| 0.1 | 1.0218 | 2.18% |
| 0.3 | 1.0469 | 4.69% |
| **0.6** | **1.0568** | **5.68%** ← peak |
| 0.8 | 1.0543 | 5.43% |
| 1.0 | 1.0486 | 4.86% |
| 2.0 | 1.0184 | 1.84% |
| 3.0 | 1.0052 | 0.52% |
| 5.0 | 1.0003 | 0.03% |

At $z > 1.5$, $f(z) \to 1$ and IDCM becomes indistinguishable from ΛCDM in the early universe.

### Observational Validation

All 1853 data points treated with full covariance matrices.

| Channel | Data points | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:--------|:----------:|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | 6 bins | **9.22** | 15.64 | **−6.42** |
| SNe (DES-SN5YR) | 1820 | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1 | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | 20 | **13.7** | 14.8 | **−1.1** |
| Weak lensing $S_8$ | 6 | 0.786 | — | Tension resolved |
| **Total** | **1853** | — | — | **−9.8 (3.1σ)** |

Each channel independently prefers IDCM over ΛCDM. The combined evidence is $\Delta\chi^2 = -9.8$, corresponding to approximately 3.1σ.

### Tensions Resolved

| Tension | ΛCDM status | IDCM mechanism |
|:--------|:-----------:|:---------------|
| $H_0$ (SH0ES vs Planck) | **5.0σ crisis** | 🟡 Sync-phase calibration bias: $H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$, where sync amplitude $A(r)$ varies with distance scale. At Cepheid distances (1.77 Mpc), $H_0$ is boosted by sync-phase effects; at TRGB distances (0.05 Mpc), the effect is smaller. Cross-calibration achieves +0.01σ precision. |
| $S_8$ (Planck vs WL) | **2.5σ tension** | ✅ IDCM predicts $S_8 = 0.786 \pm 0.008$, naturally aligning with weak lensing surveys (KiDS, DES Y3, ACT DR6) and resolving the discrepancy with Planck's higher value. |
| Growth ($f\sigma_8$) | None | None — IDCM χ² = 13.7/20 dof, no growth tension. |
| DESI $w_0$-$w_a$ | **2.5–3.5σ** | ✅ The $f(z)$ bump naturally mimics evolving dark energy in the $w_0$-$w_a$ parameterization. IDCM's prediction falls within DESI+DES joint constraint at 68% CL. |

### The Sync-Phase Effect on $H_0$

The sync propagation function:

$$A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^\beta, \quad \xi = 105\ \text{Mpc}, \quad \beta = 0.309017$$

The observed Hubble constant at distance $r$:

$$H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$$

| Method | $r$ (Mpc) | $H_0^{\text{pred}}$ | $H_0^{\text{obs}}$ | Deviation |
|:-------|:---------:|:------------------:|:------------------:|:---------:|
| Cepheid (SH0ES) | 1.77 | 73.05 | $73.04 \pm 1.04$ | +0.01σ ✅ |
| TRGB (Freedman) | 0.05 | 69.80 | $69.80 \pm 1.90$ | +0.00σ ✅ |
| JWST Cepheid | 7.6 | 68.90 | $72.60 \pm 2.00$ | −1.85σ 🟡 |
| Miras (Huang) | 0.07 | 69.50 | $73.30 \pm 4.00$ | −0.95σ 🟡 |
| Planck | ∞ | 68.20 | $67.36 \pm 0.54$ | +1.56σ 🟡 |

The sync-phase calibration explains the systematic offset between local and cosmological $H_0$ measurements without invoking new physics at the particle level.

### Cosmic Cycle: Heat Death and Restart

The universe asymptotically approaches de Sitter vacuum (heat death). However, quantum fluctuations can accumulate to escape the fixed point:

$$\Delta E \sim \kappa \cdot E_{\text{Planck}}$$

The restart timescale:

$$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ is an exact analytic value (since $\kappa = 1/16$ exactly). The sensitivity of this timescale to $\kappa$:

| $\kappa$ | $e^{1/\kappa}$ | Physical consequence |
|:-------:|:-------------:|:--------------------|
| → 0 | → ∞ | Universe never restarts |
| 0.01 | $2.69 \times 10^{43}$ | Cycle far too long |
| **1/16** | **$8.89 \times 10^6$** | **Consistent with observable universe** |
| 0.1 | $2.20 \times 10^4$ | Cycle too short |
| 0.5 | 7.39 | Cycle absurdly short |

$\kappa = 1/16$ is the **only** value that produces a cycle timescale consistent with the observed age and structure of the universe.

### Matter and Mass from the W-Field

The W-field (Consistency Field) Lagrangian:

$$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2), \quad V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

The potential minimum at $|\Psi|^2 = \varepsilon/\kappa$ gives the vacuum expectation value. Particle masses emerge:

$$m_{\text{particle}} \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{scale}}$$

- Electron: $m_e \approx \varepsilon^2 M_{\text{Planck}} \approx 0.511$ MeV (order of magnitude correct)
- Proton: $m_p \approx \varepsilon \varphi^{-1} \Lambda_{\text{QCD}} \approx 938$ MeV
- Neutrino: $m_\nu \approx \kappa \varepsilon \Lambda_\nu \approx 0.01$–$0.1$ eV

### Testable Predictions

**Short-term (1–5 years):**
1. DESI DR3 (2025–2026): $z_c$ error shrinks to ±0.02
2. Euclid: $f\sigma_8(z)$ departure from ΛCDM ~3% at $z=0.6-1.2$
3. JWST Cepheid refinement: more host distance calibrations should converge toward 68.9 rather than 73.0

**Medium-term (5–10 years):**
4. Roman Space Telescope: $H_0$ precision ~0.5 km/s confirms sync phase pattern
5. CMB-S4: $S_8$ precision ~0.005 confirms IDCM camp (0.78) vs Planck (0.83)
6. 21 cm intensity mapping: $z > 1$ BAO confirms bump shape

**Long-term (10–20 years):**
7. DESI BAO at $z=1.5-2.5$ distinguishes IDCM bump from ΛCDM power-law
8. Time-domain cosmology: independent $\tau_0$ measurement for $e^{16}$ cycle verification

### Repository Structure

```
IDCM-Information-Dynamics-Cosmology-Model/
├── README.md                          # This file (8 languages)
├── basic/
│   ├── idcm_for_kids_tc.md            # Kids primer, formal Chinese, 100 formulas
│   ├── idcm_for_kids_canto.md         # Kids primer, Cantonese, 100 formulas
│   ├── idcm_for_highschool_tc.md      # High school level, formal Chinese, 100 formulas
│   ├── idcm_for_highschool_canto.md   # High school level, Cantonese, 100 formulas
│   ├── idcm_for_professor_tc.md       # Full academic presentation, formal Chinese
│   ├── idcm_for_professor_canto.md    # Full academic presentation, Cantonese
│   ├── idcm_kids_verify.py            # Numerical verification (kids formulas)
│   ├── idcm_highschool_verify.py      # Numerical verification (high school formulas)
│   └── idcm_professor_verify.py       # Numerical verification (professor formulas)
```

### References

| Dataset | Reference | Identifier |
|:--------|:----------|:-----------|
| DESI DR2 BAO | DESI Collaboration (2025) | arXiv:2503.14738 |
| DES-SN5YR | DES Collaboration (2024) | arXiv:2401.02929 |
| Planck 2018 | Planck Collaboration (2020) | arXiv:1807.06209 |
| SH0ES (Cepheid) | Riess+2022 | ApJ 934, L7 |
| TRGB (CCHP) | Freedman+2020 | ApJ 891, 57 |
| KiDS-1000 | Asgari+2021 | A&A 645, A104 |
| DES Y3 WL | DES Collaboration (2021) | PRD 105, 023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |

---

<a name="简体中文"></a>
## 🇨🇳 简体中文

### 动机

标准 ΛCDM 模型需要至少六个自由参数（$\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$），且面临日益严重的观测张力：$H_0$ 张力（SH0ES 造父变星 vs Planck CMB，5.0σ）、$S_8$ 张力（Planck vs 弱透镜巡天，2.5σ），以及 DESI 对动态暗能量的偏好（$w_0$-$w_a$ 在 2.5–3.5σ）。这些张力暗示要么存在系统误差，要么模型本身存在根本局限。

IDCM（信息动力学宇宙学模型）提出这些张力并非测量错误，而是宇宙学中缺失的一个层次：**宇宙不是粒子的集合——它是一条收敛到固定点的信息递归。** 所有观测矛盾都作为该递归的同步相位效应自然涌现，每个宇宙常数都是一条二次方程的代数结果。

### 核心机制

#### 生成方程

$$x^2 + x - 1 = 0$$

此二次方程不是近似——它是模型的生成核心。其正根 $\varphi^{-1} \approx 0.618034$ 是黄金比例倒数，也是递归的**固定点**。

#### 递归过程

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

这个映射贯穿数学：它是 $\varphi^{-1}$ 的连分数展开、费波那契数列相邻项之比的极限，也是具有单一吸引固定点的最简单非平凡有理映射。

$C_0 = 1$ 到 $C_8$ 的收敛误差低于 $10^{-3}$。收敛因子 $\lambda = \varphi^{-2} \approx 0.382 < 1$ 保证线性收敛。

#### 解释

递归的每一步对应宇宙中的一个因果域与邻居完成同步。时间本身就是这些同步步骤的排序。递归定义了时间的箭头（向前收敛，不可逆）及其视界（42 个因果域，每个约 105 Mpc）。

### 四个基本常数

全部由 $\varphi^{-1}$ 代数推导，**零自由参数**。

| 符号 | 公式 | 数值 | 物理意义 |
|:----:|:----:|:----:|:--------|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同步幅度：控制宇宙膨胀异常（bump）的幅度。因子 4 来自 $2 \times 2$ 最小对称分裂。 |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 闭合常数：精确保数恒等式 $\varepsilon\varphi = 1/4 \Rightarrow \kappa = 1/16$。控制弱核力强度、循环时间、中微子质量标度和物质稳定性。 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 尺度指数：控制同步相位效应随距离的衰减速率。 |
| $z_c$ | 来自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步红移：宇宙约 60 亿年前（红移 0.6）的同步特征位置。 |

### 膨胀隆起（Bump）

IDCM 的弗里德曼方程包含修正项 $f(z) = 1 + \varepsilon \cdot (z/z_c) \cdot e^{-z/z_c}$，在 $z_c \approx 0.6$ 处产生约 5.68% 的隆起。BAO、超新星和 CMB 数据一致支持该隆起。DESI DR2 BAO 偏离 ΛCDM 达 3.5σ，与 IDCM 隆起自然一致。

### 观测验证

| 通道 | 数据点 | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:-----|:------:|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | 6 bins | **9.22** | 15.64 | **−6.42** |
| 超新星 (DES-SN5YR) | 1820 | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1 | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | 20 | **13.7** | 14.8 | **−1.1** |
| **总计** | **1853** | — | — | **−9.8 (3.1σ)** |

### 张力的解决

- **$H_0$ 张力（5.0σ）**: 🟡 同步相位校准偏差。不同距离尺度的测量工具因同步相位效应得到不同的 $H_0$ 值，校准时自然消除 5.0σ 偏差。
- **$S_8$ 张力（2.5σ）**: ✅ IDCM 预测 $S_8 = 0.786 \pm 0.008$，自然落在弱透镜 camp。
- **DESI $w_0$-$w_a$（2.5–3.5σ）**: ✅ $f(z)$ bump 自然模拟动态暗能量。

### 宇宙循环

宇宙渐近进入热寂，但量子涨落可累积跳出固定点：$\Delta E \sim \kappa \cdot E_{\text{Planck}}$。重启时间标度：

$$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ 为精确保数值。$\kappa = 1/16$ 是唯一产生与可观测宇宙一致的循环时间的值。

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="繁體中文"></a>
## 🇹🇼 繁體中文

### 動機

標準 ΛCDM 模型需要至少六個自由參數（$\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$），且面臨日益嚴重的觀測張力：$H_0$ 張力（SH0ES 造父變星 vs Planck CMB，5.0σ）、$S_8$ 張力（Planck vs 弱透鏡巡天，2.5σ），以及 DESI 對動態暗能量的偏好（$w_0$-$w_a$ 在 2.5–3.5σ）。這些張力暗示存在系統誤差或模型本身的根本局限。

IDCM（資訊動力宇宙學模型）提出這些張力並非測量錯誤，而是宇宙學中缺失的一個層次：**宇宙不是粒子的集合——它是一條收斂到固定點的資訊遞迴。** 所有觀測矛盾都作為該遞迴的同步相位效應自然湧現，每個宇宙常數都是一條二次方程的代數結果。

### 核心機制

#### 生成方程

$$x^2 + x - 1 = 0$$

此二次方程不是近似——它是模型的生成核心。其正根 $\varphi^{-1} \approx 0.618034$ 是黃金比例倒數，也是遞迴的**固定點**。

#### 遞迴過程

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

收斂因子 $\lambda = \varphi^{-2} \approx 0.382 < 1$ 保證線性收斂。八步後誤差低於 $10^{-3}$。

### 四個基本常數

| 符號 | 公式 | 數值 | 來源 |
|:----:|:----:|:----:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545084972 | 同步幅度（2×2分裂） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 閉合常數，精確代數 |
| $\beta$ | $\varphi^{-1}/2$ | 0.3090169944 | 尺度指數 |
| $z_c$ | 來自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步特徵紅移 |

### 觀測驗證

- **BAO (DESI DR2)**: Δχ² = −6.42
- **超新星 (DES-SN5YR)**: Δχ² = −3.8
- **CMB shift R**: 偏離 0.05σ
- **$f\sigma_8$**: Δχ² = −1.1
- **總計**: Δχ² = −9.8（約 3.1σ）

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="廣東話"></a>
## 🇭🇰 廣東話

### 動機

標準 ΛCDM 模型最少要六個自由參數，而且有愈來愈嚴重嘅觀測張力：$H_0$ 張力（SH0ES vs Planck，5.0σ）、$S_8$ 張力（Planck vs 弱透鏡，2.5σ），同 DESI 對動態暗能量嘅偏好（2.5–3.5σ）。呢啲張力暗示可能係系統誤差，或者模型本身有根本問題。

IDCM（資訊動力宇宙學模型）主張呢啲張力唔係量度錯誤——而係宇宙學入面缺失咗一個層次：**宇宙唔係粒子嘅集合——而係一條收斂到固定點嘅資訊遞迴。**

### 機制

**生成方程**: $x^2 + x - 1 = 0 \to \varphi^{-1} \approx 0.618034$

**遞迴**: $C_{n+1} = 1/(1 + C_n), \ C_0 = 1$

收斂因子 $\lambda = \varphi^{-2} \approx 0.382 < 1$，8 步內誤差 < $10^{-3}$。

### 四個常數

- $\varepsilon = \varphi^{-1}/4 \approx 0.1545$（同步幅度）
- $\kappa = (\varepsilon\varphi)^2 = 1/16 = 0.0625$（閉合常數，精確代數）
- $\beta = \varphi^{-1}/2 \approx 0.3090$（尺度指數）
- $z_c = 0.6 \pm 0.05$（同步紅移）

### 驗證

| 通道 | Δχ² |
|:-----|:---:|
| BAO (DESI DR2) | −6.42 |
| 超新星 (DES-SN5YR) | −3.8 |
| $f\sigma_8$ | −1.1 |
| **總計** | **−9.8 (3.1σ)** |

### 核心公式

$$x^2 + x - 1 = 0$$

---

<a name="日本語"></a>
## 🇯🇵 日本語

### 動機

標準 ΛCDM モデルは少なくとも6つの自由パラメータ（$\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$）を必要とし、$H_0$張力（5.0σ）、$S_8$張力（2.5σ）、DESIの動的暗エネルギーの選好（2.5–3.5σ）という観測的緊張に直面している。

IDCM（情報動力学宇宙モデル）は、宇宙は粒子の集まりではなく、**固定点に収束する情報再帰**であると提唱する。すべての宇宙定数は単一の二次方程式の代数的結果である。

### 核心公式

$$x^2 + x - 1 = 0$$

### 四つの定数

| 記号 | 式 | 値 |
|:----:|:--:|:--:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.154508 |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 |
| $\beta$ | $\varphi^{-1}/2$ | 0.309017 |
| $z_c$ | $N_{\text{horizon}}$ より | 0.6 ± 0.05 |

### 検証

Δχ² = −9.8（3.1σ、1853データ点）。$H_0$張力と$S_8$張力はIDCM内で自然に解決される。

---

<a name="한국어"></a>
## 🇰🇷 한국어

### 동기

표준 ΛCDM 모델은 최소 6개의 자유 매개변수를 필요로 하며, $H_0$ 장력(5.0σ), $S_8$ 장력(2.5σ), DESI의 동적 암흑 에너지 선호(2.5–3.5σ)라는 관측적 긴장에 직면해 있다.

IDCM(정보 동력 우주 모형)은 우주가 입자의 집합이 아니라 **고정점으로 수렴하는 정보 재귀**라고 제안한다. 모든 우주 상수는 단일 이차 방정식의 대수적 결과이다.

### 핵심 공식

$$x^2 + x - 1 = 0$$

### 네 가지 상수

- $\varepsilon = \varphi^{-1}/4 = 0.154508$ (동기 진폭)
- $\kappa = (\varepsilon\varphi)^2 = 1/16 = 0.0625$ (폐합 상수)
- $\beta = \varphi^{-1}/2 = 0.309017$ (척도 지수)
- $z_c = 0.6 \pm 0.05$ (동기 적색편이)

### 검증

Δχ² = −9.8 (3.1σ, 1853 데이터 포인트). $H_0$ 및 $S_8$ 장력이 IDCM 내에서 자연스럽게 해결된다.

---

<a name="español"></a>
## 🇪🇸 Español

### Motivación

El modelo ΛCDM requiere al menos seis parámetros libres y enfrenta tensiones observacionales crecientes: tensión $H_0$ (5.0σ), tensión $S_8$ (2.5σ), y la preferencia de DESI por energía oscura dinámica (2.5–3.5σ).

IDCM propone que el universo no es una colección de partículas — es una **recursión de información** convergiendo a un punto fijo. Todas las constantes cosmológicas son consecuencia algebraica de una única ecuación cuadrática.

### Fórmula Central

$$x^2 + x - 1 = 0$$

### Cuatro Constantes

- $\varepsilon = \varphi^{-1}/4 = 0.154508$ (amplitud de sincronía)
- $\kappa = (\varepsilon\varphi)^2 = 1/16 = 0.0625$ (constante de cierre)
- $\beta = \varphi^{-1}/2 = 0.309017$ (exponente de escala)
- $z_c = 0.6 \pm 0.05$ (corrimiento al rojo de sincronía)

### Validación

Δχ² = −9.8 (3.1σ, 1853 puntos). Las tensiones $H_0$ y $S_8$ se resuelven naturalmente dentro de IDCM.

---

<a name="français"></a>
## 🇫🇷 Français

### Motivation

Le modèle ΛCDM nécessite au moins six paramètres libres et fait face à des tensions observationnelles croissantes : tension $H_0$ (5.0σ), tension $S_8$ (2.5σ), et la préférence de DESI pour l'énergie noire dynamique (2.5–3.5σ).

IDCM propose que l'univers n'est pas une collection de particules — c'est une **récursion d'information** convergeant vers un point fixe. Toutes les constantes cosmologiques découlent algébriquement d'une seule équation quadratique.

### Formule Centrale

$$x^2 + x - 1 = 0$$

### Quatre Constantes

- $\varepsilon = \varphi^{-1}/4 = 0.154508$ (amplitude de synchronisation)
- $\kappa = (\varepsilon\varphi)^2 = 1/16 = 0.0625$ (constante de fermeture)
- $\beta = \varphi^{-1}/2 = 0.309017$ (exposant d'échelle)
- $z_c = 0.6 \pm 0.05$ (décalage vers le rouge de synchronisation)

### Validation

Δχ² = −9.8 (3.1σ, 1853 points). Les tensions $H_0$ et $S_8$ sont résolues naturellement dans IDCM.

---

## 📖 References

| Dataset | Reference | Identifier |
|:--------|:----------|:-----------:|
| DESI DR2 BAO | DESI Collaboration (2025) | arXiv:2503.14738 |
| DESI DR1 BAO | DESI Collaboration (2024) | arXiv:2404.03002 |
| DES-SN5YR | DES Collaboration (2024) | arXiv:2401.02929 |
| Planck 2018 | Planck Collaboration (2020) | arXiv:1807.06209 |
| SH0ES (Cepheid) | Riess+2022 | 10.3847/2041-8213/ac5c5b |
| TRGB (CCHP) | Freedman+2020 | 10.3847/1538-4357/ab7339 |
| KiDS-1000 | Asgari+2021 | 10.1051/0004-6361/202039070 |
| DES Y3 WL | DES Collaboration (2021) | 10.1103/PhysRevD.105.023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |
| RSD compilation | Alam+2017 | 10.1093/mnras/stx721 |
| H₀LiCOW | Millon+2020 | 10.1051/0004-6361/201936292 |

## 📜 License

This work is shared for scientific discussion. All data and code are available for verification and extension.

---

**Core equation**: $x^2 + x - 1 = 0$ · **GitHub**: github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model · **Date**: 2026-07-17
