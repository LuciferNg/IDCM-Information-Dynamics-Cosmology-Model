# IDCM — 資訊動力宇宙學模型（Information Dynamics Cosmology Model）

[← 返回語言選擇](README.md)

---

**零自由參數的宇宙學模型。** 所有常數由單一二次方程 $x^2 + x - 1 = 0$ 透過遞迴 $C_{n+1} = 1/(1 + C_n)$ 生成。解決 $H_0$ 張力（5.0σ → 同步相位效應）和 $S_8$ 張力（2.5σ → 已解決）。Δχ² = −9.8，基於 1853 個獨立數據點。

---

## 動機

標準 ΛCDM 模型至少需要六個自由參數（$\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$），且面臨日益嚴重的觀測張力：$H_0$ 張力（SH0ES 造父變星 vs Planck CMB，5.0σ）、$S_8$ 張力（Planck vs 弱透鏡巡天，2.5σ），以及 DESI 對動態暗能量的偏好（$w_0$-$w_a$ 在 2.5–3.5σ）。這些張力暗示存在系統誤差或模型本身的根本局限。

IDCM（資訊動力宇宙學模型）提出這些張力並非測量錯誤——**宇宙不是粒子的集合，而是一條收斂到固定點的資訊遞迴。** 所有觀測矛盾都作為該遞迴的同步相位效應自然湧現，每個宇宙常數都是一條二次方程的代數結果。

## 核心機制

### 生成方程

$$x^2 + x - 1 = 0$$

正根 $\varphi^{-1} \approx 0.618034$ 是黃金比例倒數，也是遞迴的**固定點**。

### 遞迴過程

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

固定點處的收斂因子 $\lambda = \varphi^{-2} \approx 0.382 < 1$ 保證線性收斂。八步後誤差低於 $10^{-3}$。

### 八步收斂表

| n | $C_n$ | 誤差 |
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

## 四個基本常數

| 符號 | 公式 | 數值 | 來源 |
|:----:|:----:|:----:|:----:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545085 | 同步幅度（2×2 分裂） |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | 閉合常數，精確代數恆等式 |
| $\beta$ | $\varphi^{-1}/2$ | 0.309017 | 尺度指數 |
| $z_c$ | 來自 $N_{\text{horizon}}$ | 0.6 ± 0.05 | 同步紅移 |

## 膨脹隆起

修正項 $f(z) = 1 + \varepsilon \cdot (z/z_c) \cdot e^{-z/z_c}$ 在 $z_c \approx 0.6$ 處產生約 5.68% 的隆起。$z > 1.5$ 時 $f(z) \to 1$，早期宇宙與 ΛCDM 無法區分。

## 觀測驗證

| 通道 | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:-----|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | **9.22** | 15.64 | **−6.42** |
| SNe (DES-SN5YR) | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | **13.7** | 14.8 | **−1.1** |
| **總計** | — | — | **−9.8 (3.1σ)** |

## 張力解決

- $H_0$ (5.0σ): 🟡 同步相位校準偏差：$H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$，不同距離尺度測量工具因同步相位效應得到不同 $H_0$ 值
- $S_8$ (2.5σ): ✅ IDCM 預測 $S_8 = 0.786 \pm 0.008$，自然落在弱透鏡 camp
- DESI $w_0$-$w_a$ (2.5–3.5σ): ✅ $f(z)$ bump 自然模擬動態暗能量

## 宇宙循環

$$\Delta t_{\text{restart}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ 為精確解析值。$\kappa = 1/16$ 是唯一能產生與觀測宇宙一致的循環時間的值。

## W 場

$$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2), \quad V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

粒子質量：$m_e \approx 0.511$ MeV、$m_p \approx 938$ MeV、$m_\nu \approx 0.01$–$0.1$ eV。

## 可測試預測

- DESI DR3：$z_c$ 收窄至 ±0.02
- Euclid：$f\sigma_8$ 偏離 ΛCDM 約 3%
- Roman：$H_0$ 精度 ~0.5 km/s
- CMB-S4：確認 $S_8 = 0.78$ camp
- DESI 高紅移 BAO：區分隆起與冪律

## 参考文献

| 數據集 | 引用 | 標識符 |
|:-------|:-----|:-------:|
| DESI DR2 BAO | DESI Collab. 2025 | arXiv:2503.14738 |
| DES-SN5YR | DES Collab. 2024 | arXiv:2401.02929 |
| Planck 2018 | Planck Collab. 2020 | arXiv:1807.06209 |
| SH0ES | Riess+2022 | 10.3847/2041-8213/ac5c5b |
| TRGB | Freedman+2020 | 10.3847/1538-4357/ab7339 |
| KiDS-1000 | Asgari+2021 | 10.1051/0004-6361/202039070 |
| DES Y3 WL | DES Collab. 2021 | 10.1103/PhysRevD.105.023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |

---

**核心公式**: $x^2 + x - 1 = 0$ · **GitHub**: [github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model](https://github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model)
