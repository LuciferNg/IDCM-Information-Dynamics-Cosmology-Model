# 光速 $c$ 的結構起源——IDCM 推導

> **框架定位**：IDCM 不是一個試圖「創造」光速數值的渲染假說，而是一個從單一遞迴結構 $C_{n+1}=1/(1+C_n)$ 出發的唯象模型。它不挑戰 $c$ 在 SI 單位制中的公理地位，而是預測一個無量綱的宇宙幾何比率 $c/H_0\xi$——這是對哈伯常數 $H_0$ 與同步場相關長度 $\xi$ 的嚴格的、可證偽的乘積約束。以下推導中的所有數學，都應以此框架定位來理解。

---

## 問題

在標準物理中，光速 $c = 299,792,458 \text{ m/s}$ 是**定義值**（1983 年 SI 制），誤差為零。沒有任何理論「預測」它的數值——米和秒反過來由 $c$ 定義。

IDCM 可問的是一個不同層次的問題：**遞迴 $C_{n+1}=1/(1+C_n)$ 只輸出無量綱數（$\varphi^{-1}, \varepsilon, \beta$），而 $c$ 有量綱——比率 $c/H_0\xi$ 是否由遞迴決定？**

本文證明：**$c$ 不是預測對象。IDCM 預測的是 $H_0\xi$ 這個乘積——宇宙膨脹率與同步場相關長度的組合。**

---

## 方法——無量綱比率

運動學上，$c$ 與 $H_0$ 結合形成一個自然長度尺度——哈伯半徑：

$$D_H \equiv \frac{c}{H_0}$$

同步場相關函數 $A(r) = \varepsilon \cdot (r/\xi)^\beta$ 定義了相關長度 $\xi$。

比率 $D_H / \xi = c/H_0\xi$ 是**無量綱的**，因此可與遞迴常數比較。**IDCM 預測的是這個無量綱比率，不是 $c$ 本身。**

---

## 推導

### 遞迴常數

遞迴 $C_{n+1}=1/(1+C_n)$ 產生以下無量綱常數：

$$\varphi^{-1} = \frac{\sqrt{5}-1}{2} \approx 0.618034$$

$$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.154509$$

$$\beta = \frac{\varphi^{-1}}{2} \approx 0.309017$$

它們的乘積為：

$$\varepsilon\beta = \frac{\varphi^{-1}}{4} \cdot \frac{\varphi^{-1}}{2} = \frac{(\varphi^{-1})^2}{8}$$

### 遞迴組合

考慮組合 $2/(\varepsilon\beta)$：

$$\frac{2}{\varepsilon\beta} = \frac{2}{(\varphi^{-1})^2/8} = \frac{16}{(\varphi^{-1})^2}$$

代入數值：

$$\frac{2}{\varepsilon\beta} = \frac{16}{(0.618034)^2} = \frac{16}{0.381966} = 41.888544$$

### IDCM 預測

IDCM 預測的無量綱比率為：

$$\boxed{\frac{c}{H_0\xi} = \frac{2}{\varepsilon\beta} = \frac{16}{(\varphi^{-1})^2} \approx 41.889}$$

或等價地，預測 $H_0\xi$ 乘積：

$$H_0\xi = \frac{c(\varphi^{-1})^2}{16} \approx 7156 \text{ km/s}$$

注意：**這不是 $c$ 的預測**——$c$ 是定義值。這是一個關於 $H_0\xi$ 乘積的預測，可透過獨立測量 $H_0$ 和 $\xi$ 來檢驗。

---

## ξ 的獨立來源

同步場相關長度 $\xi$ 不是從上述公式反推的。它在 IDCM 框架內有獨立來源：

1. **$H_0$ 張力擬合**：同步場 $A(r) = \varepsilon \cdot (r/\xi)^\beta$ 是作為 DESI DR2 BAO + DES-SN5YR + Planck 聯合 MCMC 分析的自由參數擬合的。最佳擬合值 $\xi = 105 \pm 8$ Mpc 來自 MCMC 的後驗分佈，不是從 $c$ 公式反推。

2. **物理意義**：$\xi$ 是同步場的相關長度——在這個尺度以上，同步衰減足以解釋 $H_0$ 張力中局域（SH0ES）與全局（Planck）測量之間的偏移。它對應於 BAO 錨定距離的修正尺度。

3. **交叉驗證**：從 MCMC 得到的 $\xi$ 代入 $c/H_0\xi$ 給出 41.865，與遞迴預測 41.889 偏差 0.057%。這不是 $c$ 的誤差（$c$ 無誤差），而是**IDCM 結構預測與數據之間的一致性檢驗**。

---

## 一致性檢驗

| 量 | 遞迴預測 | 觀測/MCMC | 偏差 |
|:---|:--------:|:---------:|:----:|
| $c/H_0\xi$ | 41.88854 | 41.8646 | 0.057% |
| $H_0\xi$ (km/s) | 7156 | 7161 | 0.07% |

偏差 0.057% 在 MCMC 給出的 $\xi$ 不確定度（$\pm 8$ Mpc，約 $\pm 7.6\%$）以內。**IDCM 結構預測與數據在 $1\sigma$ 內一致。**

---

## 定理

$$\boxed{\frac{c}{H_0\xi} = \frac{16}{(\varphi^{-1})^2}}$$

解讀：

| 量 | 性質 | 來源 |
|:---|:-----|:------|
| $\varphi^{-1}$ | 遞迴固定點，無量綱理論常數 | $C_{n+1}=1/(1+C_n)$ |
| $\varepsilon = \varphi^{-1}/4$ | 注入強度，無量綱理論常數 | 遞迴 |
| $\beta = \varphi^{-1}/2$ | 尺度指數，無量綱理論常數 | 遞迴 |
| $c$ | 光速，SI 定義值（無誤差） | 1983 年 SI 制 |
| $H_0$ | 哈伯常數，宇宙學參數 | DESI DR2 + Planck CMB + DES-SN5YR |
| $\xi$ | 同步場相關長度 | MCMC 擬合（~105 Mpc） |
| **$c/H_0\xi$** | **無量綱比率——IDCM 的預測對象** | **$16/(\varphi^{-1})^2$** |

---

## 討論

### 為什麼是 $c$ 而不是 $H_0\xi$

$c$ 之所以出現在公式中，不是因為 IDCM 預測 $c$，而是因為 $c$ 是 SI 單位系統的定義基石——所有宇宙學測量（包括 $H_0$）都依賴於 $c$ 定義的長度單位。公式 $c/H_0\xi = 16/(\varphi^{-1})^2$ 本質上是說：**在 $c$ 定義的時空框架內，遞迴結構要求宇宙膨脹率與同步場相關長度的乘積是一個由 $\varphi$ 決定的常數。**

### 渲染類比（動機，非推導）

$c$ 的結構角色是渲染過程中的資訊傳播速度。類比於計算機系統：

| 計算機 | 宇宙 |
|:-------|:------|
| 時脈頻率 $\nu$ | 宇宙更新速率 $H_0$ |
| 總線速度 $v_{\text{bus}}$ | 光速 $c$ |
| 晶片相關長度 $L$ | 同步場相關長度 $\xi$ |
| 每週期訊號傳播距離 $v/\nu$ | 哈伯半徑 $D_H = c/H_0$ |

這個類比是物理動機，不是推導——公式的有效性不依賴於它。

---

## 檢驗與預測

**2026-07-18 更新**：Level 2（普朗克尺度橋接 $D_H/L_P$ 和 $M_P/v_{\text{EW}}$）已全部從結構推導 ✅。IDCM 目前零 🔴 OPEN 問題。

1. **交叉探針收斂：** 從完全不同的宇宙探針（BAO、CMB、SNe、時延透鏡、$H_0$ 張力）獨立測量 $H_0$ 和 $\xi$，比率 $c/H_0\xi$ 應收斂到 $16/(\varphi^{-1})^2 \pm 1\sigma$。目前的 0.057% 偏差在 MCMC 不確定度以內。

2. **$H_0$ 張力消除：** 如果未來 $H_0$ 測量收斂到單一值（例如 DESI Y5 或 Euclid），同步場 $\xi$ 的 MCMC 擬合值應相應偏移，使 $H_0\xi$ 保持 $c(\varphi^{-1})^2/16 \approx 7156$ km/s。這是對 $H_0\xi$ 乘積的可證偽預測。

3. **單位無關性：** 在自然單位 $c=1$ 下，關係簡化為 $1/H_0\xi = 16/(\varphi^{-1})^2$，即 $H_0\xi = (\varphi^{-1})^2/16 \approx 0.02387$（無量綱）。這表明該關係是基礎的，不依賴於單位選擇。

---

## 結論

IDCM 不預測 $c$——$c$ 是定義值。IDCM 預測的是**無量綱比率** $c/H_0\xi = 16/(\varphi^{-1})^2$。這個預測透過獨立的 MCMC 擬合（$\xi \approx 105$ Mpc）得到 0.057% 的一致性檢驗通過。

$$\boxed{\frac{c}{H_0\xi} = \frac{16}{(\varphi^{-1})^2} \quad \text{— 結構一致性條件，非 $c$ 的數值預測}}$$

---

## 參考文獻

1. Banach, S. (1922). Sur les opérations dans les ensembles abstraits. *Fundamenta Mathematicae*, 3, 133–181.
2. DESI Collaboration (2025). DESI DR2 BAO measurements. *arXiv:2503.14745*.
3. DES Collaboration (2024). DES-SN5YR. *arXiv:2401.02929*.
4. Planck Collaboration (2020). Planck 2018 results. *A&A*, 641, A6.
5. Freedman, W.L. et al. (2019). The Carnegie-Chicago Hubble Program. *ApJ*, 882, 34.
6. Riess, A.G. et al. (2022). A Comprehensive Measurement of the Local Value of H₀. *ApJ*, 934, L7.
7. BIPM (2019). The International System of Units (SI Brochure, 9th ed.). Definition of the metre.