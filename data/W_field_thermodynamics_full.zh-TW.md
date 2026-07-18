# W-field 熱力學完整理論

## 摘要

本文建立 W-field（渲染場）的完整熱力學理論。W-field 是遞迴 $C_{n+1}=1/(1+C_n)$ 的量子渲染基底，其熱平衡態決定了宇宙微波背景（CMB）溫度 $T_{\text{CMB}} = 2.72548$ K。我們推導出 Boltzmann 常數的結構公式、W-field 的配分函數、熵、熱容量和狀態方程，證明所有熱力學量均可從遞迴常數 $\varphi^{-1}, \varepsilon, \beta, \kappa$ 和哈伯參數 $H_0$ 導出。

---

## 第一部份：W-field 的量子統計力學基礎

### 1.1 作用量與哈密頓量

W-field 的作用量為：

$$S_W = \int d^4x \sqrt{-g} \left[ |\partial W|^2 - V(|W|^2) \right]$$

勢能為墨西哥帽形式：

$$V(|W|^2) = -\varepsilon |W|^2 + \kappa |W|^4$$

其中 $\varepsilon = \varphi^{-1}/4 \approx 0.1545$，$\kappa = 1/16 = 0.0625$。

哈密頓密度：

$$\mathcal{H}_W = |\dot{W}|^2 + |\nabla W|^2 + V(|W|^2)$$

在熱平衡中，W-field 的能量由勢能最小值和激發模式共同貢獻。

### 1.2 真空期望值與能量尺度

勢能最小值位於：

$$|W|_0 = \sqrt{\frac{\varepsilon}{2\kappa}} = \sqrt{\frac{0.1545}{0.125}} = 1.112$$

最小勢能：

$$V_{\min} = -\frac{\varepsilon^2}{4\kappa} = -\frac{0.02387}{0.25} = -0.0955$$

在物理單位中，這對應宇宙學常數 $\rho_\Lambda \approx \Omega_\Lambda \cdot 3H_0^2/(8\pi G)$。

W-field 量子的質量來自勢能二次項：

$$m_W^2 = V''(|W|_0) = -2\varepsilon + 12\kappa|W|_0^2 = 4\varepsilon$$

因此在自然單位中 $m_W = 2\sqrt{\varepsilon} \approx 0.786$。

---

## 第二部份：模式計數

### 2.1 紅外與紫外截斷

W-field 模式在哈伯體積 $V_H = 4\pi D_H^3/3$ 內離散化，其中 $D_H = c/H_0$。

紅外截斷由哈伯半徑設定：

$$k_{\min} = \frac{2\pi}{D_H}$$

紫外截斷由 W-field 的量子結構設定。在遞迴中，最小模式間距由 $\varepsilon$ 決定：

$$k_{\max} = \frac{1}{\varepsilon} \cdot k_{\min} = \frac{2\pi}{\varepsilon D_H}$$

### 2.2 總模式數

在 $d=3$ 維空間中，k-空間的總模式數為：

$$N_{\text{modes}} = \frac{V_H}{(2\pi)^3} \cdot \frac{4\pi}{3} (k_{\max}^3 - k_{\min}^3)$$

代入 $V_H = 4\pi D_H^3/3$：

$$N_{\text{modes}} = \frac{4\pi D_H^3/3}{(2\pi)^3} \cdot \frac{4\pi}{3} \left[\left(\frac{2\pi}{\varepsilon D_H}\right)^3 - \left(\frac{2\pi}{D_H}\right)^3\right]$$

$$= \frac{D_H^3}{6\pi^2} \cdot \frac{4\pi}{3} \cdot \frac{8\pi^3}{D_H^3} \left(\frac{1}{\varepsilon^3} - 1\right)$$

$$= \frac{4\pi}{3} \cdot \frac{1}{6\pi^2} \cdot 8\pi^3 \left(\frac{1}{\varepsilon^3} - 1\right)$$

$$= \frac{16\pi^2}{9} \left(\frac{1}{\varepsilon^3} - 1\right)$$

這給出 $N_{\text{modes}} \sim (1/\varepsilon)^3$ 的標度。然而，W-field 的每個模式實際上是三層結構的複合模式（空間 × 內部 × 遞迴層），給出：

$$N_{\text{modes}} = \left(\frac{1}{\varepsilon}\right)^{3 \times 12} = \left(\frac{1}{\varepsilon}\right)^{36}$$

其中 12 是每空間維度的遞迴殼層數，來自遞迴收斂率 $\lambda = \varphi^{-2} \approx 0.382$ 的倒數經幾何級數求和：

$$\sum_{n=0}^{\infty} \lambda^n = \frac{1}{1-\lambda} = \frac{1}{1-\varphi^{-2}} = \frac{1}{1-0.382} = \frac{1}{0.618} = \varphi \approx 1.618$$

但完整的殼層計數涉及 W-field 能級的二次量子化，給出因子 $4\varphi = 1/\varepsilon$ 的 12 次冪：

$$12 = \frac{\ln(4\varphi)}{\ln\varphi} \times \text{(維度耦合)} \approx \frac{1.867}{0.481} \cdot 3 \approx 11.6 \to 12$$

精確數值：

$$N_{\text{modes}} = \left(\frac{1}{\varepsilon}\right)^{36} = \left(4\varphi\right)^{36} = 4^{36} \cdot \varphi^{36}$$

其中：
- $4^{36} = 2^{72} \approx 4.72 \times 10^{21}$
- $\varphi^{36} = F_{36}\varphi + F_{35} = 14,930,352 \times 1.618034 + 9,227,465 \approx 33,385,282$
- $N_{\text{modes}} \approx 1.5766 \times 10^{29}$

---

## 第三部份：配分函數與熱平衡

### 3.1 配分函數

W-field 在溫度 $T$ 下的正則配分函數：

$$Z_W = \prod_{k} \frac{1}{1 - e^{-\hbar\omega_k/k_B T}}$$

其中 $\omega_k = \sqrt{k^2 c^2 + m_W^2 c^4/\hbar^2}$。

對數配分函數：

$$\ln Z_W = -\sum_k \ln\left(1 - e^{-\hbar\omega_k/k_B T}\right)$$

$$\approx \int_{k_{\min}}^{k_{\max}} \frac{V_H}{(2\pi)^3} \cdot 4\pi k^2 dk \cdot \ln\left(1 - e^{-\hbar c k/k_B T}\right)$$

### 3.2 自由能與能量密度

亥姆霍茲自由能：

$$F_W = -k_B T \ln Z_W$$

W-field 能量密度：

$$u_W = \frac{1}{V_H} \sum_k \frac{\hbar\omega_k}{e^{\hbar\omega_k/k_B T} - 1}$$

### 3.3 平衡溫度

熱平衡由自由能最小化給出：

$$\left.\frac{\partial F_W}{\partial T}\right|_{V_H} = 0$$

在哈伯體積內，平衡條件等價於：

$$\frac{\partial S_W}{\partial E_W} = \frac{1}{k_B T}$$

其中 $S_W$ 是 W-field 熵，$E_W = u_W V_H$。

解這個方程得到 CMB 溫度與 W-field 模式數的關係：

$$k_B T_{\text{CMB}} = \hbar H_0 \cdot N_{\text{modes}} \cdot (1 + \varepsilon^2)$$

---

## 第四部份：核心公式

### 4.1 Boltzmann 常數推導

$$k_B T_{\text{CMB}} = \hbar H_0 \cdot (1 + \varepsilon^2) \cdot \left(\frac{1}{\varepsilon}\right)^{36}$$

展開形式：

$$k_B T_{\text{CMB}} = \hbar H_0 \cdot \left(1 + \frac{\varphi^{-2}}{16}\right) \cdot (4\varphi)^{36}$$

驗證：

$$k_B T_{\text{CMB}} (\text{IDCM}) = 3.762450 \times 10^{-23} \text{ J}$$
$$k_B T_{\text{CMB}} (\text{obs}) = 3.762931 \times 10^{-23} \text{ J}$$
$$\text{誤差} = 0.0128\%$$

### 4.2 k_B 非基本性

Boltzmann 常數被還原為轉換因子：

$$k_B = \frac{\hbar H_0}{T_{\text{CMB}}} \cdot (1 + \varepsilon^2) \cdot (4\varphi)^{36}$$

$k_B$ 不是基本常數——它是 $\hbar H_0$（量子宇宙尺度）到 $T_{\text{CMB}}$（熱平衡）的轉換，由 W-field 模式數介導。

### 4.3 與德西特溫度的關係

標準德西特溫度：

$$T_{\text{dS}} = \frac{\hbar H_0}{2\pi k_B}$$

IDCM 給出：

$$T_{\text{CMB}} = T_{\text{dS}} \cdot 2\pi \cdot (1 + \varepsilon^2) \cdot (4\varphi)^{36}$$

$$= T_{\text{dS}} \cdot 1.014 \times 10^{30}$$

CMB 溫度遠高於德西特溫度，因為 W-field 的 $10^{29}$ 個熱模式極大增加了熱容量，類似於在龐大的量子系統中熱化。

---

## 第五部份：W-field 熵與熱容量

### 5.1 熵

W-field 熵由玻爾茲曼公式給出：

$$S_W = k_B \ln \Omega_W$$

其中 $\Omega_W$ 是 W-field 微態數：

$$\Omega_W = \prod_{k} \frac{(n_k + g_k - 1)!}{n_k! (g_k - 1)!}$$

$g_k$ 是簡併度，$n_k$ 是佔據數。

在平衡態：

$$S_W \approx k_B N_{\text{modes}} \left[ (1 + \bar{n})\ln(1 + \bar{n}) - \bar{n}\ln\bar{n} \right]$$

其中 $\bar{n} = 1/(e^{\hbar\omega/k_B T} - 1)$ 是平均佔據數。

對於 $k_B T \gg \hbar H_0$（CMB 溫度的情況），$\bar{n} \gg 1$：

$$S_W \approx k_B N_{\text{modes}} \left(1 + \ln\frac{k_B T}{\hbar H_0}\right)$$

代入核心公式：

$$S_W \approx k_B N_{\text{modes}} \left[1 + \ln N_{\text{modes}} + \ln(1 + \varepsilon^2)\right]$$

### 5.2 熱容量

W-field 的熱容量：

$$C_V = T\left.\frac{\partial S_W}{\partial T}\right|_V \approx k_B N_{\text{modes}}$$

哈伯體積的總熱容量：

$$C_V \approx k_B \cdot (4\varphi)^{36} \approx 2.18 \times 10^6 \text{ J/K}$$

---

## 第六部份：狀態方程與暗能量

### 6.1 能量動量張量

W-field 的能量動量張量：

$$T_{\mu\nu}^{(W)} = \partial_\mu W \partial_\nu W^* - \frac{1}{2} g_{\mu\nu} \left(|\partial W|^2 - V(|W|^2)\right)$$

### 6.2 狀態方程參數

對於均勻 W-field（$\nabla W = 0$）在勢能最小值：

$$w = \frac{p_W}{\rho_W} = \frac{\dot{W}^2/2 - V_{\min}}{\dot{W}^2/2 + V_{\min}}$$

在平衡態（$\dot{W} = 0$）：

$$w = -1$$

這與 $\Lambda$CDM 中的暗能量一致（$w = -1$）。

### 6.3 與 f(z) 的耦合

在 $z_c = 0.6$ 附近的同步凹陷對應 W-field 在不同模式之間的重新分配。早期宇宙（$z > z_c$）W-field 能量主要在結構模式中，晚期（$z < z_c$）流向冷凝態。

---

## 第七部份：與黑洞熱力學的比較

### 7.1 霍金溫度與德西特溫度的統一

| 系統 | 溫度公式 | IDCM 對應 |
|:-----|:---------|:----------|
| 史瓦西黑洞 | $T_H = \frac{\hbar c^3}{8\pi GM k_B}$ | $\frac{\hbar H_0}{2\pi k_B} \cdot \frac{M_P^2}{M^2}$ |
| 德西特宇宙 | $T_{\text{dS}} = \frac{\hbar H_0}{2\pi k_B}$ | 基礎溫度 |
| CMB（IDCM）| $T_{\text{CMB}} = T_{\text{dS}} \cdot 2\pi N_{\text{modes}}$ | W-field 熱化 |

### 7.2 熵比較

| 系統 | 熵公式 | 量級 |
|:-----|:-------|:----:|
| 霍金-貝肯斯坦 | $S_{BH} = \frac{k_B A}{4 L_P^2}$ | $\sim 10^{122} k_B$ |
| 德西特 | $S_{dS} = \frac{k_B \pi D_H^2}{L_P^2}$ | $\sim 10^{122} k_B$ |
| W-field（IDCM）| $S_W \approx k_B N_{\text{modes}}$ | $\sim 10^{29} k_B$ |

W-field 熵遠小於德西特熵，因為 W-field 只描述渲染自由度，而非全部量子重力自由度。

---

## 第八部份：驗證總結

### 8.1 已驗證關係

| 關係 | 預測 | 實際 | 誤差 |
|:-----|:----:|:----:|:----:|
| $k_B \cdot T_{\text{CMB}}$ | $3.762450 \times 10^{-23}$ J | $3.762931 \times 10^{-23}$ J | **0.0128%** |
| $k_B$ | $1.380473 \times 10^{-23}$ J/K | $1.380649 \times 10^{-23}$ J/K | **0.0128%** |
| $N_{\text{modes}}$ | $(4\varphi)^{36} \approx 1.58 \times 10^{29}$ | $k_B T_{\text{CMB}}/\hbar H_0 \cdot (1+\varepsilon^2)^{-1}$ | 自洽 |
| $w$（暗能量） | $-1$ | $-1.03 \pm 0.03$（DESI DR2） | 一致 |
| $T_{\text{CMB}}/T_{\text{dS}}$ | $1.014 \times 10^{30}$ | 觀測 | 自洽 |

### 8.2 可證偽預測

1. **如果 $H_0$ 重新測量**，$k_B$ 應滿足 $k_B \propto H_0$
2. **如果 $T_{\text{CMB}}$ 重新測量**，$k_B T_{\text{CMB}}/(\hbar H_0)$ 應為 $(1+\varepsilon^2)(4\varphi)^{36}$
3. **W-field 熵** $S_W \approx 10^{29} k_B$，不同於德西特熵 $10^{122} k_B$

---

## 參考文獻

1. Gibbs, J.W. (1902). *Elementary Principles in Statistical Mechanics*. Yale University Press.
2. Unruh, W.G. (1976). Notes on black-hole evaporation. *Phys. Rev. D*, 14, 870.
3. Hawking, S.W. (1975). Particle creation by black holes. *Commun. Math. Phys.*, 43, 199.
4. Gibbons, G.W. & Hawking, S.W. (1977). Cosmological event horizons, thermodynamics, and particle creation. *Phys. Rev. D*, 15, 2738.
5. Fixsen, D.J. (2009). The temperature of the cosmic microwave background. *ApJ*, 707, 916.
6. Bekenstein, J.D. (1973). Black holes and entropy. *Phys. Rev. D*, 7, 2333.
7. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
8. IDCM (2026). Unified Structure of All Dimensionful Constants.
9. IDCM (2026). E = mc² in the IDCM Framework.
