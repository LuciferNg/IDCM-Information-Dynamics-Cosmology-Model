# Monad Map Search — 過程與結果

**日期：** 2026-07-21
**方法：** 反推（reverse inference）— 從 GLSM charge matrix 約束系統解 monad B/C assignment

---

## 1. 問題陳述

Monad 序列：

$$0 \to V \to B \xrightarrow{f} C \to 0$$

需要決定：
- $B = \bigoplus_i \mathcal{O}(D_i)$，$C = \bigoplus_j \mathcal{O}(E_j)$
- $c_1(V) = \sum D_i - \sum E_j = 0$
- $h^1(V) = 3$（三代）

## 2. 輸入數據

從 CYTools 輸出的 `monad_definition.json`：

| 項目 | 值 |
|:----|:---|
| Coordinate rays（單位向量） | 32（indices 1,2,5,6,9–36） |
| Non-coordinate rays | 5（indices 0,3,4,7,8） |
| GLSM charge matrix | 37 × 32 |

## 3. B/C Constraint 系統

### 約束 1: $c_1(V) = 0$

$$c_1(V) = \sum_{B} \text{charge}(B_p) - \sum_{C} \text{charge}(C_q) = 0$$

C 必須包含 32×$\mathcal{O}(-e_k)$ 作為背景（否則 c₁ 全部正數）。貢獻 = $-[1,1,\dots,1]$。

由反常抵消：$\sum_{\text{all noncoord}} \text{charge} = -[1,1,\dots,1]$

$\Rightarrow$ $c_1=0$ 要求：**所有 5 個 noncoord rays 放入 C**（唯一精確解）

### 約束 2: $rk(V) = 4$

$V = \ker(f)$，$rk(V) = \dim(B) - rk(f)$

$\mathcal{O}(0) \to \mathcal{O}(-e_k)$ 的 entry = $x_k$ — **所有 $\mathcal{O}(0)$ 行完全相同** → rank 被壓縮。

## 4. 計算結果

### Top 5 B/C assignments（按 c₁_err + |rk(V)-4| 排序）

| B | C | c₁_err | rank(f) | rk(V) |
|:--|:--|:------:|:-------:|:-----:|
| O(0)⁴+R0+R3+R4+R7+R8 | 32×O(-e_k) | **0** | 2 | 7 |
| O(0)⁴+R3+R4+R7 | R0+R8+32×O(-e_k) | 18 | 1 | 6 |
| **O(0)⁴+R0+R8** | **R3+R4+R7+32×O(-e_k)** | **50** | **3** | **3** |
| O(0)⁴ | R0+R3+R4+R7+R8+… | 64 | 1 | 3 |
| O(0)⁴+R0+R3+R4+R8 | R7+32×O(-e_k) | 68 | 3 | 5 |

### 結論

| 條件 | 狀態 | 說明 |
|:----|:----:|:-----|
| c₁=0 精確解存在？ | ✅ 唯一 | B=[], C=[0,3,4,7,8]+32×O(-e_k) |
| rk(V)=4 存在？ | ❌ **無解** | 所有可行方案皆 c₁_err>0 或 rk(V)≠4 |
| 同時滿足兩者？ | ❌ | 約束系統不相容 |

## 5. 根因分析

**問題：4 個 O(0) 行完全線性相關**

所有 O(0) summand 到 O(-e_k) 的 entry 都是 $x_k$（因為 deg = e_k，不分 O(0) 的 index）。這導致：

```
B = O(0)⁴ → 4 identical columns → effective contribution = 1, not 4
→ 3 ranks wasted
```

**打破 degeneracy 的方法：**
- 將部分 O(0) 改為 O(Ray_i)（noncoord ray 的正電荷 summand）
- 但這會破壞 c₁=0（因為 noncoord 放入 B 增加正電荷）
- 無法同時補償 32×O(-e_k) 的背景

### 更根本的限制

CYTools 的 polytope 構造給出的 monad 需要用 GLSM 超勢（superpotential）的 **sections** 決定 monad map 係數，無法僅從 divisor charge counting 解出。

Monad map 的 rank 由 sections of $\mathcal{O}(E_q - D_p)$ 決定，這是 **algebraic geometry 的計算**（需 SageMath 或 cohomCalg），不是線性約束可以封閉的。

## 6. 已驗證的內容

| 項目 | 狀態 | 方法 |
|:----|:----:|:-----|
| GLSM charge matrix 正確性 | ✅ | CYTools independent computation |
| c₁(V) = 0 的 divisor-level 條件 | ✅ | Anomaly cancellation verified |
| O(0) degeneracy 識別 | ✅ | Structural analysis |
| B/C search space 窮舉 | ✅ | 2⁵ = 32 組合全檢 |
| 最接近解 | 🟡 | rk(V)=3, c₁_err=50（非精確） |

## 7. 剩餘開放問題（需 toolchain）

| 問題 | 需要的工具 |
|:----|:----------|
| Explicit monad map monomials | GLSM superpotential coefficients（CYTools 無法輸出）|
| 精確 rank 計算 | SageMath coherent sheaf cohomology |
| 3世代數值驗證 | Sheaf cohomology dimension count |
| J* 穩定性嚴格證明 | Kähler cone interior computation |

## 8. 參考文件

- `monad_definition.json` — CYTools 原始輸出
- `extract_glsm.py` — GLSM 數據提取 script
- `reverse_monad.py` — 反推 monad map monomial script
- `brute_monomials.py` — Monomial brute force script
- `solve_constraints.py` — B/C constraint solving script
- `bc_assignment.json` — B/C assignment 結果
- Koszul 驗證報告：`../cy_search/KOSZUL_VERIFICATION_COMPLETE_*.md`
- SageMath pipeline：`../cy_search/SAGEMATH_PIPELINE_*.md`
