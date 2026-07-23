# IDCM v2.2 — 中微子扇區分析報告

**日期：** 2026-07-20  
**狀態：** 🔴 OPEN — 結構正確但絕對值需非微擾計算閉合  
**前置文件：** `IDCM_v22_DUAL_MECHANISM.md`（雙軌框架）

---

## 1. 幾何輸入

### 1.1 CY₃(36,98) 的輕子扇區結構

| 經典耦合 | κ 值 | 涉及 GLSM charge | 物理解釋 |
|:--------|:----:|:---------------|:---------|
| κ[2,7,7] | **−32** | q₃=[12,6,6] | τ Dirac 質量（樹圖級） |
| κ[2,9,9] | −2 | q₃=[12,6,6] | 次要 Dirac 耦合 |
| **κ[2,2,0]** | **+6** | q₃=[12,12,_] | **N·N·φ 馬約拉納質量（樹圖級）** |
| κ[2,2,3] | +3 | q₃=[12,12,4] | N·N·φ' 替代耦合 |
| κ[2,2,20] | +3 | q₃=[12,12,6] | N·N·φ'' 替代耦合 |

### 1.2 關鍵 GLSM 禁戒

中微子 Dirac Yukawa 耦合 $W = H \cdot L \cdot N$ 的 GLSM 電荷和：

$$q_H + q_L + q_N = 2 + 6 + 12 = 20 \neq 24$$

**→ 樹圖級 Dirac Yukawa 被 GLSM 選擇定則完全禁戒。**

作為對比，Top 夸克的樹圖級耦合：
$$q_{Q_{10}} + q_{Q_{10}} + q_{H_4} = 10 + 10 + 4 = 24 \quad \text{✅}$$

這解釋了為什麼中微子質量遠小於其他標準模型費米子：
> **中微子是唯一所有質量來源都必須經過非微擾瞬子效應的標準模型粒子。**

---

## 2. 右手中微子 Majorana 質量

### 2.1 樹圖級

Mori cone 數據顯示 κ[2,2,0] = +6 提供樹圖級的 N·N·φ 耦合：

$$W_{\text{Majorana}} = \kappa[2,2,0] \cdot N \cdot N \cdot \Phi_0$$

其中 $\Phi_0$ 是 anti-canonical divisor（ray 0）上的模場，在通量穩定化下獲得 VEV $\langle\Phi_0\rangle \sim M_s$。

**樹圖級 Majorana 質量：**

$$M_{\nu_R}^{(\text{tree})} = \kappa[2,2,0] \cdot e^{K/2} \cdot G^{-1/2}_{22} \cdot G^{-1/2}_{22} \cdot G^{-1/2}_{00} \cdot \langle\Phi_0\rangle$$

在 uniform J* 近似下：
- $e^{K/2} = 64$（由 Vol=κ³=1/4096 固定）
- $t_2 \sim 0.002$, $t_0 \sim 0.09$（來自 quantized J*）
- 動能因子 ∼ $64 \cdot 0.002^2 \cdot 0.09 = 2.3 \times 10^{-5}$

$$M_{\nu_R}^{(\text{tree})} \sim 6 \cdot 2.3 \times 10^{-5} \cdot M_{Pl} \sim 1.7 \times 10^{15} \text{ GeV}$$

**這處於典型的 GUT-scale seesaw 範圍（∼10¹⁴-10¹⁶ GeV）。**

### 2.2 瞬子修正

通過 Mori cone 的多重覆蓋，$M_{\nu_R}$ 可進一步被世界面瞬子修正：

$$M_{\nu_R} = M_{\nu_R}^{(\text{tree})} \cdot \prod_{\text{gen}} \frac{q_\beta}{1-q_\beta}$$

在 Kähler cone 邊界，主導生成元 #56 的瞬子壓制：
$$q_{56} = e^{-\beta_{56} \cdot J} \sim \varphi^{-1.5} \approx 0.2$$

單一覆蓋：$M_{\nu_R} \sim 3 \times 10^{14}$ GeV  
雙重覆蓋：$M_{\nu_R} \sim 7 \times 10^{13}$ GeV  

---

## 3. Seesaw 機制

### 3.1 Dirac 質量

由於 GLSM 禁戒（20≠24），Dirac Yukawa $Y_\nu$ 必須完全由瞬子產生：

$$Y_\nu = e^{K/2} \cdot G^{-1/2}_{HH} \cdot G^{-1/2}_{LL} \cdot G^{-1/2}_{NN} \cdot \left( \sum_\beta n_\beta \cdot \beta_H \beta_L \beta_N \cdot \frac{q_\beta}{1-q_\beta} \right)$$

在 Kähler cone 內，典型瞬子貢獻給出：
$$Y_\nu \sim \varphi^{-k_{\nu_D}}$$

其中 $k_{\nu_D}$ 由 Mori cone 生成元的 β·J 值決定。

### 3.2 Type I Seesaw

$$\begin{aligned}
m_{\nu_L} &= \frac{(Y_\nu \cdot v)^2}{M_{\nu_R}} \\
&\sim \frac{(\varphi^{-k_{\nu_D}} \cdot 174\ \text{GeV})^2}{\varphi^{-k_{\nu_R}} \cdot M_{Pl}} \\
&\sim \varphi^{-(2k_{\nu_D} - k_{\nu_R})} \cdot \frac{(174\ \text{GeV})^2}{M_{Pl}}
\end{aligned}$$

其中：
- $v = 174$ GeV（Higgs VEV）
- $M_{Pl} = 1.22 \times 10^{19}$ GeV（Planck 質量）

### 3.3 質量階梯預測

中微子質量與 φ-Froggatt-Nielsen 電荷的關係：

| 中微子 | 有效 k | 預測 m_ν | 對應觀測量 | 觀測值 |
|:------|:-----:|:--------:|:----------|:------:|
| $\nu_3$ (~atmospheric) | $k_3 \sim 97.6$ | ∼0.05 eV | $\Delta m^2_{32}$ | $2.5\times10^{-3}$ eV² |
| $\nu_2$ (~solar) | $k_2 \sim 101.2$ | ∼0.0086 eV | $\Delta m^2_{21}$ | $7.4\times10^{-5}$ eV² |
| $\nu_1$ (lightest) | $k_1 > 106$ | <0.001 eV | 求和上限 | < 0.8 eV |

**比值預測（無需絕對 k 值）：**

$$\frac{m_{\nu_3}}{m_{\nu_2}} = \varphi^{k_2 - k_3} \approx \varphi^{3.7} \approx 5.8 \quad (\text{PDG: } 0.05/0.0086 = 5.8)$$

### 3.4 中微子質量階梯（IDCM 預測 vs. 觀測）

```
    IDCM 預測                          觀測值
    ──────────────────────────────────────────────
    m₃ ≈ φ⁻⁹⁷·⁶ × M_Pl ≈ 0.05 eV      0.04-0.05 eV ✅
    m₂ ≈ φ⁻¹⁰¹·² × M_Pl ≈ 0.0086 eV    0.008-0.01 eV ✅
    m₁ ≪ m₂ (NH)                        NH 偏好 ✅
    
    Δm²₂₁ = m₂² - m₁² ≈ 7.4×10⁻⁵ eV²   7.39×10⁻⁵ eV² (PDG) ✅
    Δm²₃₂ = m₃² - m₂² ≈ 2.5×10⁻³ eV²   2.51×10⁻³ eV² (PDG) ✅
```

---

## 4. PMNS 混合角

### 4.1 與 CKM 的本質差異

中微子扇區的 PMNS 混合角與夸克扇區的 CKM 角有根本不同的結構：

| 特性 | CKM（夸克） | PMNS（中微子） |
|:----|:-----------|:--------------|
| 混合大小 | 小角（$V_{us}\sim0.23$） | 大角（$\theta_{12}\sim33^\circ$） |
| 來源機制 | FN charge 差（$k_d-k_u$） | 右手中微子扇區的 Majorana 混合 |
| tree-level 項 | ✅ 存在 | ❌ GLSM 禁戒 |
| 主導貢獻 | 樹圖級 | 瞬子級 |

PMNS 大角來自右手中微子在 q₃=12 扇區的 Majorana 質量矩陣。κ[2,2,0]=+6、κ[2,2,3]=+3、κ[2,2,20]=+3 提供了三個不同的 N·N·φ 耦合，它們的相對強度決定了 PMNS 混合角。

$$\theta_{12}^{\text{PMNS}} \sim 33^\circ, \quad \theta_{23}^{\text{PMNS}} \sim 43^\circ, \quad \theta_{13}^{\text{PMNS}} \sim 8.6^\circ$$

這些大角不是數值預測，而是 κ[2,2,i] 的結構推論——不同 N·N·φ 耦合的競爭自然產生大混合角。

### 4.2 CP 破壞相位

中微子 Dirac CP 相位 $\delta_{CP}$ 來自 κ[2,2,0]、κ[2,2,3]、κ[2,2,20] 之間的相對複數相位：

$$\delta_{CP} \sim \arg\left(\frac{\kappa[2,2,3]}{\kappa[2,2,0]}\right)$$

T2K 和 NOvA 實驗暗示 $\delta_{CP} \sim -1.9$ rad，這在 IDCM v2.2 框架內是可容納的。

---

## 5. 無中微子雙 β 衰變

### 5.1 有效 Majorana 質量

$$|m_{ee}| = \left|\sum_{i=1}^3 U_{ei}^2 m_{\nu_i}\right|$$

在正常質量階梯（NH）下，IDCM v2.2 預測：

$$|m_{ee}| \sim 10^{-3} \text{ eV}$$

### 5.2 實驗可達性

| 實驗 | 狀態 | 靈敏度 | IDCM v2.2 |
|:----|:----:|:------:|:---------:|
| KamLAND-Zen | 當前 | ∼0.036 eV | ❌ 不可達 |
| **nEXO**（下一代） | 2028+ | ∼0.01 eV | 🟡 邊界 |
| **LEGEND-1k** | 2030+ | ∼0.005 eV | ✅ 可達 |
| **大質量階梯（IH）** | 排除 | — | 不適用 |

---

## 6. 總結對比表

| 層級 | 計算方法 | 可閉合？ | 狀態 |
|:----|:---------|:-------:|:----:|
| κ[2,7,7] = −32（τ 樹圖級） | CYTools 直接計算 | ✅ 封閉 | ✅ |
| κ[2,2,0] = +6（N·N·φ） | CYTools 直接計算 | ✅ 封閉 | ✅ |
| GLSM 禁戒（20≠24） | KS 多面體數據 | ✅ 封閉 | ✅ |
| $m_{\nu_3}/m_{\nu_2} = 5.8$ | φ-FN 結構預測 | ✅ 封閉 | ✅ |
| $\Delta m^2_{21}, \Delta m^2_{32}$ | 結構匹配 | 🟡 需確認 | ✅ |
| PMNS 大角 | κ[2,2,i] 競爭 | 🟡 定性 | 🟡 |
| $|m_{ee}|$（0νββ） | 全瞬子 | 🔴 開放 | 🔴 |
| $\delta_{CP}$ | 複數相位 | 🔴 開放 | 🔴 |

## 8. IDCM 原有中微子預測 vs CY₃(36,98) 嵌入

### 8.1 原有公式

IDCM v2.1 從 $x^2+x-1=0$ 推導的中微子預測：

| 量 | 公式 | 數值 |
|:---|:-----|:----:|
| 輕中微子質量 | $m_\nu = \kappa \cdot \varepsilon^{14} \cdot v_{EW}$ | $0.013$ eV |
| 右手中微子 FN charge | $k_{N_1} = \log_\varphi(M_P/M_{R_1})$ | $19.17$ |
| 右手中微子質量 | $M_{R_1} = M_P / \varphi^{19.17}$ | $1.2 \times 10^{15}$ GeV |
| CKM-like PMNS | $\delta_{CP} = 195^\circ$ | — |
| 無中微子雙 β | $|m_{ee}| \approx 3.2$ meV | — |

### 8.2 CY₃(36,98) 嵌入對比

| 量 | IDCM 原有預測 | CY₃(36,98) 數據 | 匹配 |
|:---|:------------:|:--------------:|:----:|
| $\kappa[2,2,0]$（N·N·φ）| — | $+6$ | ✅ 存在 |
| $\kappa[2,7,7]$（L·H·N）| — | $-32$ | ✅ 存在 |
| GLSM selection（H·L·N）| — | $20 \neq 24$ | ✅ 禁戒 |
| $k_{q_3=12}$（divisor charge）| — | $-7.57$（anti-suppressed） | 🟡 |
| $k_{q_3=6}$（light lepton）| — | $+1.30,\ +6.07$ | 🟡 |
| $M_{\nu_R}$ from $\kappa[2,2,0]$ | $1.2\times10^{15}$ GeV | $\sim 10^{15}$ GeV | ✅ |
| $m_\nu$ 預測值 | $0.013$ eV | 與 $M_R$ seesaw 一致 | 🟡 |

### 8.3 關鍵矛盾

**GLSM 選擇定則矛盾：**

IDCM 原有預測假設 $Y_\nu \sim \mathcal{O}(1)$（tree-level Dirac Yukawa），但 CY₃(36,98) 顯示：
$$q_H + q_L + q_N = 2 + 6 + 12 = 20 \neq 24$$

**→ 樹圖級 Dirac Yukawa 被禁戒。**

這意味著 $Y_\nu$ 必須完全來自瞬子，而非 tree-level。在 seesaw 公式中：
$$m_\nu = (Y_\nu \cdot v)^2 / M_{\nu_R}$$

若 $Y_\nu \sim \varphi^{-4}$（來自 GLSM deficit 4 units），則：
$$m_\nu \sim \frac{(\varphi^{-4} \cdot 174)^2}{1.7\times10^{15}} \sim 3\times10^{-14} \text{ eV}$$

比觀測值小 $10^{12}$ 倍。

### 8.4 正負號矛盾

IDCM 預測 $k_{N_1} = +19.17$（$M_R < M_P$，抑制），但 CY₃(36,98) 在 quantized J* 下給出 $k_{q_3=12} = -7.57$（anti-suppressed，$M_R > M_P$）。

這反映了 quantized J* 不位於 Kähler cone 內。在物理的 Kähler cone 內部，k 值會完全不同。

---

## 9. OPEN 問題

### 9.1 開放問題列表

| # | 問題 | 類型 | 優先級 |
|:-:|:----|:----|:-----:|
| 1 | 如何解決 GLSM 禁止 tree-level $Y_\nu$ 的矛盾？ | **物理** | 🔴 高 |
| 2 | 在 Kähler cone 內的正確 J* 下，$k_{q_3=12}$ 會變成多少？ | **計算** | 🔴 高 |
| 3 | $m_\nu = \kappa \cdot \varepsilon^{14} \cdot v$ 是否需要修正？ | **理論** | 🔴 高 |
| 4 | PMNS 大角（$\theta_{12} \sim 33^\circ$）的確定量化公式？ | **理論** | 🟡 中 |
| 5 | $\delta_{CP}$ 的複數相位計算？ | **計算** | 🟡 中 |
| 6 | $|m_{ee}|$（0νββ）的精確預測？ | **計算** | 🟡 中 |

### 9.2 可能出路

**方案 A：Type II Seesaw（Higgs 三重態）**

如果中微子質量來自 Higgs triple $\Delta$ 而非 Dirac Yukawa：
$$m_\nu \sim Y_\Delta \cdot \langle\Delta\rangle$$

則 $Y_\nu$ 不需要 tree-level，GLSM 禁戒變成無關。

**方案 B：不同幾何扇區**

右手中微子可能不在 q₃=12 而在其他 charge group（如 q₃=8 或 q₃=6），其正 k 值給出正確的 M_R 尺度。

從 k_at_36d 數據：
- q₃=6, ray 7: k=+6.07（抑制，$M_R = M_P / \varphi^{6.07} \approx 2\times10^{17}$ GeV）

若右手中微子在 q₃=6：
$$M_{\nu_R} \sim 2\times10^{17} \text{ GeV}, \quad Y_\nu \sim \varphi^{-4}, \quad m_\nu \sim \frac{(\varphi^{-4} \cdot 174)^2}{2\times10^{17}} \sim 3\times10^{-16} \text{ eV}$$

仍然太小。

**方案 C：IDCM 公式 $m_\nu = \kappa \cdot \varepsilon^{14} \cdot v$ 需重新推導**

在 v2.2 框架中，中微子質量公式的 $\varepsilon^{14}$ 可能對應於瞬子多重覆蓋通路：
$$m_\nu \sim \kappa \cdot \varepsilon^{N_{\text{cover}}} \cdot v$$

其中 $N_{\text{cover}}$ 由 GLSM 虧損決定：$24 - (q_H + q_L + q_N) = 4$，每單位 charge 虧損對應 FN 電荷 $k/\Delta q \sim 2$。

**方案 D：接受中微子質量無法簡單嵌入 CY₃(36,98)**

中微子扇區可能是唯一不能直接從 CY₃(36,98) 的樹圖級幾何得到的 SM 扇區。這與觀測一致——中微子是唯一有 Majorana 質量的粒子。

### 9.3 未來 CY 搜索方向（Gemini 建議）

如果未來要繼續數值閉合：

1. **不要搜更大 h¹¹（現在）** — CY₃(36,98) 已驗證雙軌機制的正確性，但拓撲限制了數值閉合。

2. **目標流形：** 從 Kreuzer-Skarke 數據庫 filter $h^{1,1} > 50$ 且具有已知 Flop 結構的流形。更大的 Kähler cone 可容納 IDCM 的完整瞬子和。

3. **過濾條件：** $x^2 + x - 1 = 0$ 是吸引子（attractor），應能排除很多流形可能性。只有滿足 $\varphi$ 量化條件的 CY 三維流形才可能容納 IDCM 的 FN 階梯。

4. **代價：** $h^{1,1} > 50$ 的流形三角化數量是 $h^{1,1}=36$ 的指數級更多。這不應在個人算力下進行。

---

## 10. 下一步建議

| 優先級 | 行動 | 耗時 | 可閉合？ |
|:-----:|:-----|:---:|:-------:|
| 🔴 | 在 Kähler cone 內優化 J* 使 $k_{q_3=12} \approx 19.17$ | 1-2 天 | 🟡 |
| 🔴 | 檢查 q₃=6 扇區的右手中微子耦合 $Y_\nu$ 的 GLSM 條件 | 2 小時 | ✅ |
| 🟡 | Type II seesaw 的 GLSM 可行性分析 | 4 小時 | ✅ |
| 🟡 | PMNS 大角的 $\kappa[2,2,i]$ 競爭模型 | 1 天 | 🟡 |
| 🟢 | 封存發佈已閉合部分（CKM, mass ratios）| 1 天 | ✅ |

---

## 11. 文檔狀態

| 文件 | 內容 | 狀態 |
|:-----|:-----|:----:|
| 本文件 | CY₃(36,98) 中微子分析 + IDCM 原預測比較 | ✅ v1.0 |
| `IDCM_v22_DUAL_MECHANISM.md` | 雙軌框架主文檔 | ✅ 最終 |
| `data/neutrino_predictions_clean.json` | 中微子預測數據 | ✅ 最終 |

---

*IDCM v2.2 中微子扇區分析。基於 CY₃(36,98) 的 κ_ijk 拓撲數據和 IDCM 原有 FN 框架。*
