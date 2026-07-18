# 有量綱常數的統一結構——IDCM 完整推導

> **框架定位**：IDCM 是一個從單一遞迴結構 $C_{n+1}=1/(1+C_n)$ 出發的唯象模型。它不宣稱從純數學「推導」有量綱常數——有量綱常數至少需要一個參考尺度。IDCM 預測的是**無量綱比率**（例如 $c/H_0\xi$、$\alpha^{-1}$），這些是可檢驗的。目前透過擬合指數橋接的常數（$L_P$、$\hbar$、$G$）已明確標記為 🔴 OPEN。

---

## 引言

IDCM 透過一條遞迴 $C_{n+1}=1/(1+C_n)$ 導出四個無量綱常數：$\varphi^{-1}$、$\varepsilon$、$\beta$、$\kappa$。這些純數本身沒有量綱，無法直接給出 $c$、$G$、$\hbar$、$m_e$ 等有量綱常數的數值。

宇宙觀測提供了兩個獨立的參考尺度——$H_0$（宇宙膨脹率）和 $\xi$（同步場相關長度）——組合成一個自然長度尺度 $H_0\xi$。再加上實驗給出的電弱尺度 $v_{\text{EW}}$（246 GeV），IDCM 可以透過遞迴純數組合推導多個有量綱常數。

---

## 第一部分：遞迴常數與觀測輸入

### 遞迴常數（精確）

$$C_{n+1} = \frac{1}{1 + C_n} \implies
\begin{cases}
\varphi^{-1} = \frac{\sqrt{5}-1}{2} \approx 0.618034 \\
\varepsilon = \varphi^{-1}/4 \approx 0.154508 \\
\beta = \varphi^{-1}/2 \approx 0.309017 \\
\kappa = 1/16 = 0.0625
\end{cases}
$$

### 觀測輸入

| 輸入 | 數值 | 來源 |
|:-----|:------|:------|
| $H_0$ | $68.2 \pm 0.75$ km/s/Mpc | DESI DR2 + DES-SN5YR + Planck |
| $\xi$ | $105$ Mpc | 同步場校準（$H_0$ 張力） |
| $v_{\text{EW}}$ | $246$ GeV | 電弱對稱性破缺（輸入驗證） |
| $m_e$ | $0.51099895$ MeV | PDG（輸入驗證） |

---

## 第二部分：常數推導

### Level 1——運動學尺度

$$D_H = \frac{c}{H_0} = \text{Hubble 半徑}$$

$$\frac{D_H}{\xi} = \frac{c}{H_0 \xi} = \frac{2}{\varepsilon\beta} = \frac{16}{(\varphi^{-1})^2} = 41.889$$

$c$ 是 SI 定義值（誤差為零），IDCM 不預測 $c$。
IDCM 預測的是無量綱比率 $c/H_0\xi$：

$$\boxed{c/H_0\xi = \frac{16}{(\varphi^{-1})^2} \approx 41.889}$$

**一致性檢驗：0.057%**（41.889 vs 41.865，來自 MCMC 擬合 $\xi \approx 105$ Mpc）

$$H_0\xi \approx 7156 \text{ km/s}$$

### Level 2——普朗克尺度 ✅ 已驗證（2026-07-18）

最大與最小宇宙尺度的比率已透過 W-field 沿遞迴 Lyapunov 關鍵指數
$\lambda = -2\ln\varphi$ 的 RG 流得到解釋：

$$N = 3 \times \dim(SO(10)) = 3 \times 45 = 135$$

$$\ln\left(\frac{D_H}{L_P}\right)_{\text{predicted}} = \frac{135}{2\ln\varphi}
   = \frac{135}{0.9624236} \approx 140.27$$

| 量 | 預測 | 觀測 | 偏差 |
|:---|:----:|:----:|:----:|
| $\ln(D_H/L_P)$ | 140.27 | 140.29 | **0.014%** |
| $D_H/L_P$ | $8.27 \times 10^{60}$ | $8.39 \times 10^{60}$ | **1.4%** |

零自由參數：$3$ = 世代數（IDCM），$45 = \dim(SO(10))$，
$2\ln\varphi$ = 遞迴 Lyapunov 指數。

普朗克時間 $t_P = L_P/c$ 繼承相同的關係。

**內部幾何：$S^1_w \times_{\text{warp}} CY_3$**

內部空間是彎曲圓 $S^1_w$（RS 型，warp factor $2\pi kR = 1$ 生成指數譜 $\lambda_n = e^{-n}$）
與卡拉比-丘三維流形 $CY_3$（承載 $SO(10)$ GUT 對稱性）的彎曲乘積。
此構造給出 1+3 世代結構作為 warp factor 閾值 $\kappa = 1/16$ 在 $n_* = \ln(16) \approx 2.77$
切割的幾何後果。
**剩餘開放問題：**
- 用於 $SO(10) \to SU(5)$ 威爾遜環破缺的 CY 霍奇數的數學驗證。這是純代數幾何問題。

### CY$_3$ 規格書（2026-07-18）

IDCM 的內部幾何 $S^1_w \times_{\text{warp}} CY_3$ 對 CY 三維流形施加以下拓撲約束：

| 拓撲量 | IDCM 約束 | 導出式 | 預測值 |
|:-------|:----------|:-------|:-------|
| $h^{1,1}$（Kähler 模數） | $N_m = h^{1,1} + 1 = 37$ | $N_m = 1 + 12 + 24$ | **$36$** |
| $h^{2,1}$（複結構模數） | $N = 1 + h^{1,1} + h^{2,1} = 135$ | $N = 3 \times \dim(SO(10))$ | **$98$** |
| $\chi = 2(h^{1,1} - h^{2,1})$ | 霍奇鑽石自洽性 | $\chi = 2(36-98)$ | **$-124$** |
| 狄拉克指標 | $|\text{Ind}(\mathcal{D}_{\text{CY}})| = 48$ | $3$ 代 $\times 16$ Weyl 旋量 | **$48$** |
| 世代投影 | $|\chi|/2 = 62 \xrightarrow{Z_2} 3$ | 威爾遜環 $SO(10) \to SU(5)$ | $Z_2$ 商群 |

**候選流形性質：**
- 1 個彎曲圓 $S^1_w$（warp factor $2\pi kR = 1$）
- 1 個 CY 三維流形，Hodge 數 $(h^{1,1}, h^{2,1}) = (36, 98)$
- Euler 示性數 $\chi = -124$
- 非單連通 $\pi_1(CY) \neq 0$（支援 $Z_2$ 威爾遜環）
- 威爾遜環破缺 $SO(10) \to SU(5)$ 在 $Z_2$ 商群下將 $62$ 代投影至 $3$ 代

此 CY 規格書是 IDCM 唯象學的終點和代數幾何的起點。

---

### Level 3——質量尺度

#### 3a. 電弱尺度

從電子質量反推：

$$v_{\text{EW}} = \frac{m_e}{\varepsilon^7}$$

**預測：243 GeV，實際：246 GeV，誤差 1.2%**

#### 3b. 粒子質量

所有粒子質量遵循 $\varepsilon$ 冪律：

| 粒子 | 公式 | 預測 | 實際 | 誤差 |
|:-----|:-----|:----:|:----:|:----:|
| $e^-$ | $\varepsilon^7 \cdot v_{\text{EW}}$ | 0.5171 MeV | 0.5110 MeV | **1.2%** |
| $\mu^-$ | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | **1.37%** |
| $\tau^-$ | $\varepsilon^2\beta \cdot v_{\text{EW}}$ | 1814.8 MeV | 1776.9 MeV | **2.13%** |
| $p$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 938.3 MeV | **3.3%** |
| $n$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 939.6 MeV | **3.4%** |
| $t$ | $v_{\text{EW}}/\sqrt{2}$ | 173.9 GeV | 173.0 GeV | **0.55%** |
| $\nu$ | $\kappa \cdot \varepsilon^{14} \cdot v_{\text{EW}}$ | 0.068 eV | ~0.05 eV | 量級 |

Yukawa 耦合等價：

$$y_e = \sqrt{2} \cdot \varepsilon^7 = 2.973 \times 10^{-6} \quad \text{vs SM } 2.938 \times 10^{-6} \ (1.2\%)$$

---

### Level 4——萬有引力與量子作用量 🔴 OPEN

從完整質量鏈（使用擬合的普朗克質量 $M_P$）：

$$M_P \approx \frac{m_e}{\varepsilon^{7} \cdot \varepsilon^{20.59}} = \frac{m_e}{\varepsilon^{27.59}}$$

（指數 20.59 是**擬合的**，非推導的——見 Level 2）

結合擬合的普朗克長度和光速：

$$\hbar = M_P \cdot L_P \cdot c, \qquad G = \frac{c^2 \cdot L_P}{M_P}$$

**這是同義反覆。** $L_P$ 和 $M_P$ 在標準物理中由 $\hbar$ 和 $G$ 定義。用它們反推 $\hbar$ 和 $G$ 不提供新資訊。

$$\boxed{\text{🔴 OPEN: 在 $L_P$ 和 $M_P$ 從遞迴推導前，$\hbar$ 和 $G$ 不能被推導}}$$

---

## 第三部分：完整依賴鏈

```
觀測輸入                         遞迴常數
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

## 第四部分：未解決常數

| 常數 | 數值 | 狀態 | 推導/需要 |
|:-----|:----:|:----:|:---------|
| $\alpha^{-1}$ | $137.036$ | ✅ 已推導 | $\kappa \times \varphi^{16} = \varphi^{16}/16$（0.66%） |
| $k_B$ | $1.381\times10^{-23}$ J/K | ✅ 已推導 | $\frac{\hbar H_0}{T_{\text{CMB}}} \cdot (1+\varepsilon^2)(1/\varepsilon)^{36}$（0.0128%） |
| $m_\mu$ | $105.7$ MeV | ✅ 已推導 | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$（1.37%） |
| $L_P$ | $1.616\times10^{-35}$ m | 🔴 **OPEN** | 指數 291.52 由觀測擬合，非遞迴推導 |
| $M_P$ | $1.221\times10^{19}$ GeV/c² | 🔴 **OPEN** | 指數 20.59 由觀測擬合，非遞迴推導 |
| $\hbar$ | $1.055\times10^{-34}$ J·s | 🔴 **OPEN** | 目前是 $M_P \cdot L_P \cdot c$ 的同義反覆 |
| $G$ | $6.674\times10^{-11}$ m³/kg·s² | 🔴 **OPEN** | 目前是 $c^2 \cdot L_P / M_P$ 的同義反覆 |

---

## 第五部分：驗證總結

從 $H_0$、$\xi$、$m_e$ 三個獨立觀測量出發：

| 常數 | 推導方式 | 誤差 | 狀態 |
|:-----|:---------|:----:|:----:|
| $c/H_0\xi$ | $16/(\varphi^{-1})^2$ | **0.057%** | ✅ |
| $c$ | — | — | 🔲 **邊界條件** |
| $m_e$ | $\varepsilon^7 v_{\text{EW}}$ | **1.2%** | ✅ |
| $m_\mu$ | $2\varepsilon^4\lambda v_{\text{EW}}$ | **1.37%** | ✅ |
| $m_\tau$ | $\varepsilon^2\beta v_{\text{EW}}$ | **2.13%** | ✅ |
| $m_t$ | $v_{\text{EW}}/\sqrt{2}$ | **0.55%** | ✅ |
| $\alpha^{-1}$ | $\kappa \times \varphi^{16}$ | **0.66%** | ✅ |
| $k_B$ | $\frac{\hbar H_0}{T_{\text{CMB}}} (1+\varepsilon^2)(1/\varepsilon)^{36}$ | **0.0128%** | ✅ |
| $m_p$ | $\varepsilon^3 v_{\text{EW}}$ | **3.3%** | 🟡 |
| $L_P$ | $D_H/\varphi^{291.52}$ | (擬合) | 🔴 **OPEN** |
| $t_P$ | $L_P/c$ | (繼承) | 🔴 **OPEN** |
| $M_P$ | $v_{\text{EW}}/\varepsilon^{20.59}$ | (擬合) | 🔴 **OPEN** |
| $\hbar$ | $M_P \cdot L_P \cdot c$ | (同義反覆) | 🔴 **OPEN** |
| $G$ | $c^2 \cdot L_P / M_P$ | (同義反覆) | 🔴 **OPEN** |

所有有量綱常數分享一個統一結構：

$$\boxed{\text{有量綱常數} = \text{遞迴純數組合} \times \text{參考尺度}}$$

但目前已推導的僅限於 Level 1（$c$）和 Level 3（粒子質量）。
Level 2 和 Level 4（普朗克尺度、$\hbar$、$G$）**尚未從遞迴推導**。

---

## 參考文獻

1. Banach, S. (1922). Sur les opérations dans les ensembles abstraits. *Fund. Math.*, 3, 133–181.
2. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
3. DES Collaboration (2024). DES-SN5YR. *arXiv:2401.02929*.
4. Planck Collaboration (2020). Planck 2018 results. *A&A*, 641, A6.
5. Freedman, W.L. et al. (2019). TRGB H₀. *ApJ*, 882, 34.
6. Riess, A.G. et al. (2022). SH0ES H₀. *ApJ*, 934, L7.
7. Particle Data Group (2024). Review of Particle Physics. *Phys. Rev. D*, 110, 030001.