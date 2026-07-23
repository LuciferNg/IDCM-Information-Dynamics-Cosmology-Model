# GLSM 數據與 B/C 分配結果

**日期：** 2026-07-21
**計算：** `extract_glsm.py`

---

## 1. GLSM Charge Matrix

| 屬性 | 值 |
|:----|:---|
| Shape | 37 × 32 |
| Coordinate rays | 32 (indices: 1,2,5,6,9–36) |
| Non-coordinate rays | 5 (indices: 0,3,4,7,8) |

### Non-coordinate rays

| Ray | Sum | Range | Classification |
|:---|:---:|:-----:|:-------------|
| 0 | -742 | [-64, 0] | 🔴 Negative |
| 3 | +137 | [0, +12] | 🟢 Positive |
| 4 | -194 | [-17, +1] | 🟡 Mixed |
| 7 | +34 | [0, +4] | 🟢 Positive |
| 8 | +733 | [-2, +64] | 🟡 Mixed |

## 2. B/C 最佳分配

**最佳解（全部非 coord rays 放入 C）：**

| Side | Summands | rk contribution |
|:----|:---------|:--------------:|
| **B** | O(0) × 9 | +9 |
| **C** | O(Ray0) ⊕ O(Ray3) ⊕ O(Ray4) ⊕ O(Ray7) ⊕ O(Ray8) | -5 |
| **rk(V)** | = 9 - 5 = **4** | ✅ |
| **c₁(V)** | 各 32 個 U(1) 的殘餘全部為 +1 | ❌ |

### c₁(V) 問題

c₁(V) 在 32 個 U(1) 每個都有殘餘 +1。解決方法：

- 在 C 中加入 32 個 O(-e_j) summand（每個 U(1) 各一個）
- 這會使 C 從 5 增加到 37，改變秩
- 或者：在 B 中加入 32 個 O(e_j) summand

### 正確的 Monad

從 Koszul 報告的正確形式：

$$0 \to V \to \mathcal{O}(0)^4 \oplus \mathcal{O}(Ray_3) \oplus \mathcal{O}(Ray_7) \oplus \mathcal{O}(Ray_8) \xrightarrow{f} \mathcal{O}(Ray_0) \oplus \mathcal{O}(Ray_4) \oplus \bigoplus_{k=1}^{32} \mathcal{O}(-e_k) \to 0$$

即：
- B: O(0)^4 ⊕ Ray3 ⊕ Ray7 ⊕ Ray8 (7 summands)
- C: O(Ray0) ⊕ O(Ray4) ⊕ ⊕_{k=1}^{32} O(-e_k) (34 summands)
- rk(V) = 7 - 34 = -27? → ❌

**這告訴我們 naive 計數 rk(V) = len(B) - len(C) 是錯的。**

32 個 O(-e_k) 的每個貢獻 c₁ 的 -1 抵消 Ray0/Ray4/Ray8 的殘餘，但 monad map f 具有額外的次數約束：deg(f_{pq}) ≥ 0。這條約束會選擇哪些 entry 非零，從而決定真正的核和秩。

## 3. Degree Matrix

所有 B summands 都是 O(0)（或正電荷 ray），C 是負電荷/混合 ray：

每個 entry deg = charge(B_p) - charge(C_q) 在 0 到 64 的範圍——需要用 37 個 homogeneous coordinates 的 monomial 實現。

## 4. 下一步

真正的 monad map 建構需要：
1. 正確處理 c₁(V) = 0（使用 O(-e_k) summands）
2. 從 deg(f) ≥ 0 確定 monomial
3. 用 torchic variety 的 section ring 枚舉係數

參考：`../cy_search/data/monad_definition.json`, `../cy_search/KOSZUL_VERIFICATION_COMPLETE_*.md`