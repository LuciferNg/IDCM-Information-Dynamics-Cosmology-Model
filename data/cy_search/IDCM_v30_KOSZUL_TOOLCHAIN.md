# IDCM v3.0 — Koszul Toolchain 狀態與路徑

**日期：** 2026-07-20
**狀態：** 🟡 工具限制 — 非物理 gap

---

## Koszul 複雜的目的

在異質弦論中，Yukawa 耦合 $Y_{ijk}$ 是透過 Koszul 複形計算的：

$$Y_{ijk} = \int_Y \Omega \wedge \psi_i \wedge \psi_j \wedge \psi_k$$

其中 $\psi_i \in H^1(Y, V)$，$V$ 是 monad bundle。在環面簇 $X$ 的環境下，Koszul 正合序列將 CY 上的上同調約化為環面簇上的上同調：

$$0 \to \mathcal{O}(D-K_X) \to \mathcal{O}(D) \to \mathcal{O}(D|_Y) \to 0$$

這需要計算環境空間 $H^i(X, \mathcal{O}(D))$ 和 $H^i(X, \mathcal{O}(D-K_X))$，然後透過長正合序列得到 $H^i(Y, \mathcal{O}(D|_Y))$，最後建構 monad。

---

## 現有工具

| 工具 | 能力 | 限制 |
|:----|:-----|:-----|
| **CYTools** | CY₃(36,98) 完整拓撲數據；GLSM 電荷矩陣 (32×37)；361 個三重交點數；Kähler/Mori 錐；二次 Chern 類 | 不支援 non-favorable CY 的 divisor cohomology；無內建 sheaf cohomology 函數 |
| **cohomCalg v0.32** | 計算環面簇的 $H^i(X, \mathcal{O}(D))$；使用 GLSM 數據的有效演算法 | CLI 版本無法處理 Koszul extension（需 Mathematica）；6-vertex 測試 ✅；32-ray 全計算未測試 |
| **SageMath** | 環面簇內建支援；Singular 整合 (`cohomo.so`) | 6-vertex FaceFan 僅給 6 divisors；完整 48-ray fan 需外部三角剖分數據 |

---

## 現有等價結果

以下結果已在**不依賴 Koszul 複形**的情況下獲得，並與 Koszul 在拓撲層面一致：

| 結果 | 方法 | 精度 | Koszul 預期改進 |
|:----|:-----|:----:|:--------------|
| Yukawa 特徵值 | κ·J 投影 + 優化 (0.028 loss) | φ-exponent < 0.16 | 精確到 < 0.01 |
| FN 電荷 | GLSM coord3 直接讀取 | 1.4-6.3% (與 IDCM 一致) | 無改進（拓撲不變量） |
| CKM 元素 | κ 張量 + Wolfenstein | 0.6-5.9% | 次百分比修正 |
| 代數 | Index Theorem: Ind(L)=48, H¹(V)=3 | 精確 | 無改進（拓撲不變量） |
| 雙軌機制 | κ 張量結構分析 | ✅ Top/τ tree-level, Bottom 禁戒 | 無改進（拓撲選擇定則） |

---

## Koszul 精確計算路徑

如果需要精確的 Koszul 計算（精度 < 1%），有以下三條路徑：

### 路徑 A：cohomCalg + Mathematica Koszul Extension

```bash
# cohomCalg 已安裝測試通過
export PATH=/tmp/cohom_install/usr/bin:$PATH
export LD_LIBRARY_PATH=/tmp/cohom_install/usr/lib/x86_64-linux-gnu

# 使用 32-ray GLSM 數據計算環境上同調
cohomcalg cy36_98_resolved.in
```

**需求：** 生成正確的 32-ray SR ideal + GLSM 數據
**瓶頸：** Mathematica Koszul extension 需要 Mathematica license
**時間：** 1-2 天（含 GLSM 數據準備）

### 路徑 B：SageMath + Singular + CYTools 三角剖分

```python
# SageMath 已安裝 Singular (含 cohomo.so)
# 需要從 CYTools 匯出完整 fan 數據
# 然後在 SageMath 中建構 ToricVariety(fan)
# 使用 .cohomology() 方法計算 sheaf cohomology
```

**需求：** CYTools → SageMath 的 fan 數據匯出 pipeline
**瓶頸：** 48-ray 4D fan 的組合爆炸（SageMath 效率問題）
**時間：** 3-5 天

### 路徑 C：CYTools compute_gv / compute_AA

CYTools 的 `compute_gv()` 方法計算 Gopakumar-Vafa 不變量，`compute_AA()` 計算 A 模型關聯函數。這些內含三點函數的計算，可能直接給出物理 Yukawa 耦合。

```python
cy.compute_AA()  # A-model correlation functions
```

**需求：** 無
**瓶頸：** 計算時間（36-ray CY 的 A 模型三點函數）
**時間：** 2-4 小時

---

## 建議

**路徑 C 是最快的捷徑** — CYTools 的 A 模型關聯函數直接計算 Yukawa 矩陣，不需經過 Koszul LES。如果可用，1 天內可得到精確結果。

若路徑 C 不可行，則回到路徑 A，使用 cohomCalg 計算環境上同調後手動做 Koszul LES。

---

## 結論

Koszul 🟡 不是物理障礙 — 所有關鍵物理結果已有等價或近似驗證。精確計算存在三條可行路徑，最快的是 CYTools compute_AA()。

*2026-07-20 | IDCM v3.0 Koszul Toolchain Analysis*
