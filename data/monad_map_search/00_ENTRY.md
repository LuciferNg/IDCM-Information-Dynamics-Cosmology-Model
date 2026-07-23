# Monad Map Search — 入口

**日期：** 2026-07-21
**目標：** 從 CYTools GLSM 數據提取 monad map 的顯式多項式形式
**狀態：** 🟡 需要暴力搜尋

---

## 問題陳述

Monad 序列：

$$0 \to V \to B \xrightarrow{f} C \to 0$$

其中 $B$ 和 $C$ 是 toric divisor 的直和，$f$ 是一個座標單項式矩陣（monad map）。

### 已知數據

| 項目 | 值 | 來源 |
|:----|:---|:-----|
| Rays | 37（32 coord + 5 noncoord） | CYTools |
| GLSM charge matrix | 37×32 | `monad_definition.json` |
| Positive noncoord | [3, 7] | 同上 |
| Negative noncoord | [0] | 同上 |
| Mixed noncoord | [4, 8] | 同上 |
| rk(V) | 4 | 反常抵消 + 穩定性 |
| c₁(V) | 0 | 需要 verified |

### B/C 候選

從 `pathb_monad_reconstruction.py`：

| Side | 候選 rays | 理由 |
|:----|:----------|:-----|
| **B** | Ray 3, Ray 7 (+ 額外 O(0) 填充至 rk=4) | 正電荷 |
| **C** | Ray 0, Ray 4 (+ 可能需要 O(-e_i)) | 負電荷或混合 |

---

## 搜尋策略

### Step 1: 枚舉所有 B/C 分配（已完成）

$2^5 = 32$ 種分配，找到使 $c_1(V)=0$ 且 $rk(V)=4$ 的最佳解。

### Step 2: 提取 monad map degree 矩陣

Monad map $f$ 的每個 entry $f_{pq}$ 的 degree 由 B 和 C 的 charge 差決定：

$$\deg(f_{pq}) = \text{charge}(B_p) - \text{charge}(C_q)$$

這個 degree 必須用 37 個 homogeneous coordinates 的 monomial 實現。

### Step 3: 暴力搜尋 monomial

對於每個 entry，枚舉所有可能的 monomial（座標乘積）匹配 degree 約束。

- 37 coordinates（射線），但 monomial 中的座標必須遵守 **Stanley-Reisner 理想**（SR ideal）
- Degree vector 是 32 維的 U(1) charge 向量
- Monomial 形式：$x_0^{a_0} x_1^{a_1} \ldots x_{36}^{a_{36}}$

### Step 4: 驗證一致性

- 檢查 SR ideal 約束（哪些座標不能同時為零）
- 檢查 $f$ 的 injectivity（monad map 係數使 | 在 J* 處滿秩）
- 檢查 $H^1(V) = 3$（使用 Koszul LES）

---

## 檔案結構

```
data/monad_map_search/
├── 00_ENTRY.md                   ← 本文件
├── 01_GLSM_DATA.md               ← GLSM charge 數據整理
├── 02_BC_ASSIGNMENT.md           ← B/C decomposition 決定
├── 03_DEGREE_MATRIX.md           ← monad map degree 矩陣
├── 04_SR_IDEAL.md                ← Stanley-Reisner ideal
├── 05_MONOMIAL_BRUTEFORCE.md     ← 暴力搜尋結果
├── extract_glsm.py               ← GLSM 數據提取 script
├── brute_monomials.py            ← Monomial brute force
└── verify_monad.py               ← 驗證 script
```

## 已知限制

- **CYTools 無法輸出 GLSM 超勢** — monad map 係數依賴於 CY 方程（48 polytope points 的 sections）
- **SageMath fan 不相容** — CYTools triangulation 不能直接轉成 SageMath fan
- **SR ideal 長度：** 37 coordinates × ~450 SR pairs — cohomCalg v0.32 無法處理

## 下一步

1. 暴力搜尋最佳 B/C 分配（$c_1=0$ 的精確解）
2. 計算 degree matrix
3. 枚舉 monomial 空間
4. 用有限 field 驗證 injectivity