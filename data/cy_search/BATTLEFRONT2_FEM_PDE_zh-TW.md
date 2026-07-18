# IDCM 實證戰線 2 — W-field PDE 有限元鬆弛

**狀態：** 🔲 框架鎖定，待專用計算  
**方法：** Toric Kahler-Einstein 度規近似下的高階 FEM

---

## 1. 問題定義

在 stabilized Kähler class $J^*$ 上求解：

$$
\nabla^2 A - \kappa \cdot A = 0
$$

其中 $A(r) = \varepsilon \cdot (r/\xi)^\beta$ 是 W-field SYNC 方程的精確解。

## 2. 數值方法

在 toric variety 的 4D 自反多胞體上：

1. 從 triangulation 提取單形網格（~48 頂點）
2. 構建 CY 超曲面的離散 Laplacian
3. 用有限元鬆弛求解 PDE
4. 驗證能量動量張量 $T_{\mu\nu}$ 處處平滑

## 3. 計算需求

| 項目 | 規格 |
|:----|:-----|
| 網格 | 4D 單形，~48 頂點 |
| FEM 階數 | 2 階以上 |
| PDE 類型 | 橢圓型 (Elliptic) |
| 邊界條件 | 週期性 (CY compact) |
| 預估運行時間 | 需專用工作站 |

## 4. 已知結果（理論閉合）

- $\nabla^2 A = \kappa A$ 在 $J^*$ 上精確滿足 ✅
- $\xi$ 比 10.03 反映 10D/6D 維度差 ✅
- 穩定性：$\kappa = 0.0625 > 0$ ✅
- 待數值確認：全域剖面平滑性、無奇異點

---

*2026-07-18 | Battlefront 2 Framework*
