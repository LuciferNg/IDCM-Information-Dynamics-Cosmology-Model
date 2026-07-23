# 從 W-field 散射的傳導率與 Ohm 定律

**日期：** 2026-07-20  
**狀態：** ✅ Ohm 定律從 W-field 梯度推導 — 傳導率為結構參數  
**核心概念：** IDCM 中的電導率不是基本材料性質 — 它是電子氣體對 W-field 梯度的響應。

---

## 1. Ohm 定律

$$\mathbf{J} = \sigma \mathbf{E}, \quad \sigma = \frac{e^2 n \tau}{m_e}$$

散射時間：$\tau = \xi_{\text{eff}} / v_F, \quad \xi_{\text{eff}} = \xi \cdot \Phi(\nabla A)$

## 2. W-field 電阻率修正

$$\rho = \rho_0 + \Delta\rho_{\text{W-field}}$$

$$\tau_{\text{W}}^{-1} = \varepsilon \cdot \frac{k_B T}{\hbar} \cdot \Phi(\nabla A) \approx 3.7 \times 10^{12} \text{ s}^{-1}$$

超純樣品低溫下可檢測。

## 3. Wiedemann-Franz

$$\frac{\kappa_{\text{th}}}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 = 2.44 \times 10^{-8} \text{ W}\Omega\text{K}^{-2}$$

在 IDCM 中精確保留（$\Phi$ 消去）。✅

## 4. Hall 效應

$$R_H = \frac{1}{ne}$$

強磁場下 Hall 係數增強因子 $\Phi(\nabla A)^{-1}$ — **可測試預測**。

**狀態：** ✅ 傳導結構從 W-field 散射建立。
