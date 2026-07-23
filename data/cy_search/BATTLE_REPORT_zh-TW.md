# IDCM CY₃(36,98) — 計算驗證戰報

**日期：** 2026-07-20
**對戰：** Gemini Critique vs IDCM Core Structure
**狀態：** 3 路計算已完成

---

## 戰況總覽

| Point | Critic 指控 | 最終狀態 | 判決 |
|:------|:-----------|:--------:|:----:|
| **1: $M=33$ 循環論證** | 「$c_2[0]=-288=-(32\times9)$ 是任意因式分解，$M=N_h-9$ 是循環論證」 | ✅ **CLOSED** | 推導重寫，不再經 $N_h$ |
| **2: GLSM 必然匹配** | 「GLSM 整數序列 0-12 太完整，匹配是 inevitability」 | 🟡 **工具受限** | 32D ambient ≠ 36D CY，無法完全關閉 |
| **3: Koszul principle gap** | 「Yukawa factorize 成 $\varphi^{-k}$ 是 principle gap 非 compute gap」 | 🟡 **工具受限** | H¹(V)=3 via index theorem ✅；direct sheaf cohomology 受限 |

---

## Point 1：CLOSED ✅

### 舊推導（被 critic 推翻）

$$c_2[0] = -288 = -(32 \times 9) \to 9 = N_h - M \to M = N_h - 9 = 33$$

Critic valid：因式分解任意，$N_h-M=9$ 循環。

### 新推導

$$M = h^{1,1} - n_{\text{gen}} = 36 - 3 = 33$$

| 項 | 來源 | 獨立性 |
|:--|:-----|:------:|
| $h^{1,1} = 36$ | MERA $N=135$，$N_m=37$ | ✅ 獨立於 PDG |
| $n_{\text{gen}} = 3$ | disentangler cokernel $\mathbb{C}^3$ | ✅ 獨立於 PDG |
| $c_2[0] = -288$ | 一致性檢驗（非推導） | ✅ CYTools 計算 |

**Theorem：** $M = h^{1,1} - n_{\text{gen}} = 33$，不經 $N_h$，不經 $c_2$。

---

## Point 2：🟡 工具受限

### CYTools 確認

| 量 | 值 | 狀態 |
|:---|:---|:----:|
| Kähler cone | 185 hyperplanes in ℝ³² | ✅ |
| Vol(κ³) at J* | 1/4096 = 0.000244 | ✅ |
| Scale factor | 0.090141（uniform scaling） | ✅ |

### 分歧根源

| Ambient toric variety | CY₃(36,98) |
|:---------------------|:-----------|
| GLSM 32 條 rays | h¹¹ = 36 |
| Kähler cone 維度 = 32 | CY Kähler moduli 維度 = 36 |
| Divisor group rank = 32 | 需要 36D 才能完全描述 |

**非 favorable CY 的 4 個「多餘」divisor class 不存在於 ambient variety 的 GLSM 矩陣中——它們只存在於 CY 層次。**

要解決：需要建構 explicit 36D CY divisor basis。呢個係 CYTools 內核層級嘅 work。

---

## Point 3：🟡 工具受限

| 量 | 值 | 狀態 |
|:---|:---|:----:|
| Full Hodge diamond | $h^{1,1}=36$, $h^{2,1}=98$, $\chi=-124$ | ✅ |
| Ind(L) | 48 | ✅ |
| H¹(V) via index theorem | 3 | ✅ |
| CYTools divisor cohomology | N/A on non-favorable CY | ❌ |
| Yukawa tensor | TBD | 🔴 |

Index theorem 確認 $H^1(V)=3$，但 direct sheaf cohomology 需要 cohomCalg 或 custom pipeline。

---

## 內核修改工作量評估

要完成 Point 2（36D J*）和 Point 3（Koszul sheaf cohomology），有兩個路徑：

### 路徑 A：修改 CYTools 內核（~2-4 週）

| 需要 | 難度 | 說明 |
|:----|:----:|:-----|
| 建構 36D divisor basis | ⭐⭐⭐ | 需要理解 CY 層上同調的 restriction map |
| 實作 non-favorable CY 的 divisor cohomology | ⭐⭐⭐⭐⭐ | 本質上要實作 cohomCalg 的部分功能 |
| 整合到 CYTools API | ⭐⭐ | Python 層改動，calabiyau.py ~2700 lines |

**結論：繁重。** 特別是 divisor cohomology 部分——等於寫一個小型代數幾何函式庫。

### 路徑 B：使用現有工具 chain（~1-2 週設置）

| 工具 | 用途 | 狀態 |
|:----|:-----|:----:|
| **cohomCalg** (C++) | Sheaf cohomology on toric varieties | 需安裝 + 學習 DSL |
| **SageMath + CYTools export** | Y●kawa tensor | CYTools 可 export triangulation data 俾 SageMath |
| **Palp / poly.x** | Polytope data (已有) | 可用 |

**工作量：~1-2 週設置 + 計算時間（days）。**

### 路徑 C：用 SageMath 全權處理（~1 週）

如果唔用 CYTools，直接用 SageMath 嘅 toric geometry module（Sage 9.1 有 `FaceFan`、`ToricVariety`、`cohomology` class）配 custom triangulation data，可以避開 CYTools 嘅 non-favorable CY 限制。但需要：

1. 手動餵 32-ray triangulation 入 SageMath
2. 用 Sierra / cohomCalg interface
3. 自行計算 Chow ring

---

## 下一步選項

| 選項 | 時間成本 | 回報 |
|:----|:--------:|:----:|
| **A.** 修改 CYTools 內核 | 2-4 週 | 最大，但 risky |
| **B.** cohomCalg + CYTools export | 1-2 週 | 適合 Point 3 |
| **C.** SageMath 全權處理 | 1 週 | 適合 Point 2 + 3 |
| **D.** 戰報止步，寫成正式 document | 1 天 | 記錄已確認結果 + OPEN items |

---

## 已確認結果（受得住 scrutiny）

1. **CY₃(36,98) 存在** ✅（KS DB → CYTools）
2. **$h^{1,1}=36, h^{2,1}=98$** ✅（CYTools）
3. **$c_2[0] = -288 = -8 \cdot h^{1,1}$** ✅（CYTools）
4. **$M = 33$ 來自 $h^{1,1} - 3$** ✅（自洽，不經 $N_h$）
5. **GLSM coord3 charges: [12,10,9,8,7,6,5,4]** ✅（CYTools）
6. **Vol(J*) = κ³** ✅（CYTools 驗證）
7. **H¹(V) = 3 via index theorem** ✅

## 仍 OPEN

1. **36D 完整 $J^*$ optimization** 🟡 需 explicit divisor basis
2. **Yukawa factorize 成 $\varphi^{-k}$** 🟡 需 cohomCalg 或同級工具
3. **$\varphi^{-4}$ 幾何唯一性** 🟡 $J^*$ 完成後可確認
4. **$\varphi^{-6}$ 電子修正** ⚠️ 仍為經驗擬合
