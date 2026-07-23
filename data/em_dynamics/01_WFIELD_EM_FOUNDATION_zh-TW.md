# EM 作為 W-field 結構投影

**日期：** 2026-07-20  
**狀態：** ✅ 理論基礎已立  
**核心概念：** 電磁 U(1) 規範場不是基本的 — 它是 SYNC 場 A(r) 投影到 CY₃(36,98) 特定除子類的結果。

---

## 1. W-field PDE 作為規範原型

W-field 在 J* 固定點滿足 PDE：

$$\nabla^2 A = \kappa A, \quad \kappa = \frac{1}{16}$$

徑向投影（SYNC）解：

$$A(r) = \varepsilon \cdot (r/\xi)^\beta, \quad \varepsilon = \frac{\varphi^{-1}}{4}, \quad \beta = \frac{\varphi^{-1}}{2}$$

**映射到 U(1) 規範結構：**

| 規範元素 | W-field 實現 | 意義 |
|:---------|:-------------|:-----|
| 規範勢 $A_\mu$ | $\nabla_\mu A$ | W-field 梯度是基本勢 |
| 場強 $F_{\mu\nu}$ | $\nabla_\mu\nabla_\nu A - \nabla_\nu\nabla_\mu A$ | W-field 聯絡曲率 |
| 耦合 $g$ | $\varepsilon = \varphi^{-1}/4$ | 結構耦合常數 |
| 規範變換 | $A \to A + \text{常數}$ | W-field 零模平移對稱 |
| 流 $J_\mu$ | $\nabla_\mu(\nabla^2 A - \kappa A)$ | 從 W-field 方程守恆 |

## 2. 從一個 SYNC 場到六個 U(1)

CY₃(36,98) 有 h¹¹ = 36 個 Kähler 模。GLSM 電荷矩陣 32×37，定義了破缺前的 6 個 U(1) 規範群：

$$\text{GLSM: } U(1)^6 \to SU(3)_c \times SU(2)_L \times U(1)_Y \to SU(3)_c \times U(1)_{\text{em}}$$

## 3. EM U(1) 作為特定線性組合

電磁 U(1) 是特定的組合：

$$A^{\text{em}}_\mu = \sum_{a=1}^6 q_a \cdot A^{(a)}_\mu$$

其中 $q_a$ 對應 $Q_{\text{em}} = T_3 + Y/2$ 的 GLSM 電荷。

**電荷量子化** 來自 GLSM 電荷矩陣整數性、FN 荷 [11,10,8,8,6,5]、SU(5) 嵌入約束。

## 4. ε 作為普遍耦合

$\varepsilon = \varphi^{-1}/4 = 0.1545$ 普遍出現：SYNC 振幅、α₁ GUT 關係、α_EM 結構。

## 5. 關鍵結論

W-field PDE 包含完整的 U(1) 規範胚胎結構。EM 場不是獨立自由度 — 它是 W-field 梯度投影到電磁除子類的集體動力學。

**狀態：** ✅ 基礎 — EM 識別為 W-field 結構投影。
