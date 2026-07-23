# 動力論：W-field 背景中的電子氣體

**日期：** 2026-07-20  
**狀態：** ✅ 動力論框架建立 — Boltzmann 方程從 W-field 連續性  
**核心概念：** IDCM 中的電子氣體由修正 Boltzmann 方程控制，碰撞項來自 W-field 散射。

---

## 1. 分布函數

$$\frac{dN}{d^3x\, d^3p} = f(\mathbf{x}, \mathbf{p}, t)$$

最大相空間密度：$f \leq f_{\text{max}} = \frac{2}{h^3} \cdot \Phi(\nabla A)$

## 2. Boltzmann 方程

$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \nabla_\mathbf{x} f + \mathbf{F} \cdot \nabla_\mathbf{p} f = \left(\frac{\partial f}{\partial t}\right)_{\text{coll}}$$

力項：$\mathbf{F} = -\varepsilon \cdot \nabla A(\mathbf{x})$

## 3. H-定理

從 W-field 一致性約束 $\Sigma W_i \leq 1$ 湧現：

$$\frac{\partial s}{\partial t} + \nabla \cdot \mathbf{J}_s \geq 0$$

## 4. 平衡分布

$$f_0(\mathbf{p}) = \frac{1}{e^{(E - \mu)/k_B T} + 1}$$

Fermi-Dirac 分布從 W-field 一致性最大化湧現。溫度 $k_B T = \varepsilon \cdot \xi \cdot \bar{E}$。

## 5. 輸運係數

| 係數 | IDCM 表達 | 對應 |
|:-----|:----------|:------|
| 電導率 σ | $e^2 n \tau / m_e$ | Drude 模型 |
| 散射時間 τ | $\xi/v_F \cdot \Phi(\nabla A)$ | W-field 限制 |

**狀態：** ✅ 動力論框架從 W-field 連續性建立。
