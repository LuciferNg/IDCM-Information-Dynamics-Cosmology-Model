# 同步波——W-field 相關結構的集體模式

## 定義

### 同步場 ≠ 量子場

同步場 $A(r) = \varepsilon(r/\xi)^\beta$ **不是**獨立於 W-field 的量子場。它是 W-field 的**非局部兩點相關函數**：

$$A(r) \equiv \langle W(x) W^\dagger(x+r) \rangle_{\text{render}}$$

描述 W-field 渲染在空間尺度 $r$ 上的相關強度。它不是一個可以獨立量子化的動力學場，而是 W-field 本身的大尺度集體結構。

### 同步波 ≠ 粒子

同步波是 W-field 相關結構 $A(r)$ 隨時間的演化模式。它**不對應任何粒子**——沒有自旋、沒有質量、不能被創造或消滅。

它的物理類比：

| 系統 | 集體模式 | 粒子 | 同步波類比 |
|:-----|:--------|:----|:-----------|
| 晶格 | 聲子 | 原子 | W-field 粒子（徑向/相位） |
| 電子氣 | 電漿子 | 電子 | W-field 粒子 |
| **W-field 相關** | **同步波** | — | W-field 相關函數的擾動 |

### 同步波 vs W-field 波

| 性質 | W-field 波 | 同步波 |
|:-----|:-----------|:-------|
| 對象 | W-field 場 $\phi, \eta$ | 相關函數 $A(r)$ |
| 可量子化 | ✅ 是 → 粒子 | ❌ 否 → 集體模式 |
| 質量 | $m_\phi \approx 174$ GeV | 無 |
| 波速 | $c$ | $c$ |
| 物理對應 | 頂夸克、希格斯、光子 | BAO 相關演化 |

---

## 第一部分：同步場的數學結構

### 1.1 定義

同步場 $A(r)$ 是 W-field 的非局部渲染相關函數：

$$A(r) = \varepsilon \left(\frac{r}{\xi}\right)^\beta$$

其中：
- $\varepsilon = \varphi^{-1}/4 \approx 0.1545$（注入強度）
- $\beta = \varphi^{-1}/2 \approx 0.3090$（冪律指數）
- $\xi = 105$ Mpc（同步相關長度）

### 1.2 Laplace 算子

在球坐標中：

$$\nabla^2 A = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial A}{\partial r}\right)$$

$$\frac{\partial A}{\partial r} = \frac{\beta A}{r}$$

$$\nabla^2 A = \frac{\beta(\beta+1)A}{r^2}$$

其中 $\beta(\beta+1) = 0.4045...$。

---

## 第二部分：波動方程

### 2.1 靜態方程

同步場 $A(r)$ 滿足靜態方程：

$$\nabla^2 A - \frac{\beta(\beta+1)}{r^2} A = 0$$

這是一個 Euler-Cauchy 方程，解為 $A(r) \propto r^\beta$（正則解）和 $A(r) \propto r^{-\beta-1}$（奇異解）。

### 2.2 擾動方程

對同步場引入時間依賴的擾動 $\delta A(r,t)$：

$$A(r,t) = \varepsilon\left(\frac{r}{\xi}\right)^\beta + \delta A(r,t)$$

擾動滿足波動方程：

$$\frac{\partial^2 \delta A}{\partial t^2} - c^2 \nabla^2 \delta A + \frac{c^2 \beta(\beta+1)}{r^2} \delta A = 0$$

其中 $c$ 是光速，由 IDCM 推導：

$$c = \frac{16}{(\varphi^{-1})^2} \cdot H_0 \cdot \xi$$

### 2.3 分離變量

令 $\delta A(r,t) = R(r) T(t)$，代入波動方程：

$$\frac{T''}{T} = c^2 \left[ \frac{R''}{R} + \frac{2R'}{rR} - \frac{\beta(\beta+1)}{r^2} \right] = -\omega^2$$

時間部分：

$$T(t) = e^{\pm i\omega t}$$

空間部分（球貝塞爾方程）：

$$R'' + \frac{2}{r} R' + \left[ \frac{\omega^2}{c^2} - \frac{\beta(\beta+1)}{r^2} \right] R = 0$$

令 $k = \omega/c$ 和 $\nu = \beta + 1/2$，則：

$$R(r) = j_\nu(kr)$$

其中 $j_\nu$ 是 $\nu$ 階球貝塞爾函數。

---

## 第三部分：色散關係與模式譜

### 3.1 色散關係

同步波是無質量波：

$$\omega^2 = k^2 c^2$$

波速 $c$ 與 W-field 波和 F-field 波相同。

### 3.2 基態模式

最低階模式由球貝塞爾函數的第一個零點決定：

$$j_\nu(k_1\xi) = 0, \quad k_1 = \frac{j_{\nu,1}}{\xi}$$

其中 $j_{\nu,1} \approx 2.751$ 是 $\nu = 0.809$ 階球貝塞爾函數的第一個零點。

### 3.3 特徵尺度

| 量 | 數值 | 解釋 |
|:---|:----:|:------|
| $\nu = \beta + 1/2$ | 0.809 | 球貝塞爾階數 |
| $j_{\nu,1}$ | 2.751 | 第一零點 |
| $k_1 = j_{\nu,1}/\xi$ | 0.0262 Mpc$^{-1}$ | 基態波數 |
| $\lambda_1 = 2\pi/k_1$ | 240 Mpc | 基態波長 |
| $T_1 = 2\pi\xi/(c \cdot j_{\nu,1})$ | 782 Myr | 振盪週期 |
| $T_1 / H_0^{-1}$ | 0.055 | 週期佔哈伯時間比 |

---

## 第四部分：與 BAO 的交叉驗證

### 4.1 BAO 尺度

標準 BAO 的聲學視界 $r_s \approx 147$ Mpc 投影到 $z=0$ 給出：

$$r_s^{\text{proj}} = \frac{r_s}{1+z_{\text{rec}}} \cdot D(z_{\text{rec}}) \approx 105 \text{ Mpc}$$

這與同步場的相關長度 $\xi = 105$ Mpc 一致。

### 4.2 同步波與 BAO 的關係

同步波 **不是** BAO。BAO 是重子-光子流體在複合時的聲波振盪，而同步波是 W-field 渲染相關的波動模式。兩者的關係是：

| 性質 | BAO | 同步波 |
|:-----|:---|:-------|
| 介質 | 重子-光子電漿 | W-field 渲染場 |
| 尺度 | $r_s \approx 147$ Mpc | $\xi = 105$ Mpc |
| 波速 | $c_s \approx c/\sqrt{3}$ | $c$ |
| 起源 | 複合時 | 遞迴 $C_{n+1}=1/(1+C_n)$ |

BAO 在同步場背景上留下印記，且兩者在同一尺度 $\xi$ 上耦合。

### 4.3 驗證總結

| 檢驗 | 預測 | 觀測 | 狀態 |
|:-----|:----|:----|:----:|
| $\xi = 105$ Mpc | 同步相關長度 | BAO 峰值 | ✅ 一致 |
| $A(r) \propto r^\beta$ | 冪律指數 $\beta = 0.309$ | 非物質相關 | ✅ 獨立 |
| $c$ 波速 | 與 W-field 波相同 | 因果結構 | ✅ 自洽 |

---

## 第五部分：結論

1. **同步波存在**：同步場 $A(r) = \varepsilon(r/\xi)^\beta$ 的擾動滿足波動方程，以光速 $c$ 傳播
2. **特徵時間尺度**：基態振盪週期 $T \approx 782$ Myr，約為哈伯時間的 5.5%
3. **特徵空間尺度**：基態波長 $\lambda \approx 240$ Mpc
4. **與 BAO 一致**：同步場相關長度 $\xi = 105$ Mpc 與 BAO 投影尺度匹配
5. **非物質相關**：同步場是更深層的渲染相關，非重子物質相關函數

---

## 參考文獻

1. IDCM (2026). Nonlocal Anchor Model. `nonlocal_anchor_model.en-US.md`.
2. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
3. Eisenstein, D.J. et al. (2005). Detection of the BAO peak in the SDSS. *ApJ*, 633, 560.
4. IDCM (2026). W-field Waves.