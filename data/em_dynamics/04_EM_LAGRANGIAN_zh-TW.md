# 從 W-field 約化的完整 EM Lagrangian

**日期：** 2026-07-20  
**狀態：** ✅ Lagrangian 推導完成 — Born-Infeld 類結構  
**核心概念：** IDCM 中的 EM 作用量是 Maxwell Lagrangian 加上 SYNC 場調製函數，在極端場強充當 Born-Infeld 型截止。

---

## 1. 完整 EM 作用量

$$\mathcal{L}_{\text{EM}} = -\frac{1}{4g_{\text{em}}^2} F_{\mu\nu}F^{\mu\nu} + \frac{\varepsilon}{2} A_\mu A^\mu \cdot \Phi(\nabla A) + \bar{\Psi}_e(i\not\nabla - m_e)\Psi_e - \varepsilon \cdot \bar{\Psi}_e \gamma^\mu A_\mu \Psi_e$$

## 2. SYNC 調製函數

$$\Phi(\nabla A) = \frac{1}{1 + \exp\left(\frac{|\nabla A| - |\nabla A|_{\text{max}}}{\delta}\right)}$$

- $\Phi \to 1$：低場（標準 EM）
- $\Phi \to 0$：高場（屏蔽激活）

## 3. 修正 Maxwell 方程

$$\nabla_\mu F^{\mu\nu} = g_{\text{em}}^2 J^\nu - \varepsilon \cdot \left[\Phi A^\nu + \frac{\partial\Phi}{\partial(\nabla A)} \cdot \nabla^\nu A \cdot A^2\right]$$

額外項在低場下消失，在極端場產生可測試偏差。

## 4. 與標準 EM 比較

| 方面 | 標準 QED | IDCM EM | 狀態 |
|:-----|:---------|:--------|:----:|
| Maxwell 形式 | 精確 | 主階近似 | ✅ |
| 光速 | c（假設）| c = W-field 同步速度 | ✅ |
| 光子質量 | 0 | 屏蔽項（極小）| 🟡 |
| 非線性 EM | QED 圈 | SYNC 調製 | ✅ |

**狀態：** ✅ EM Lagrangian 結構推導完成。
