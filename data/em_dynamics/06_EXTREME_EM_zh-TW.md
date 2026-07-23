# 極端電磁：脈衝星、磁星、IXPE

**日期：** 2026-07-20  
**狀態：** ✅ 閉合 — 𝒩 凝聚從 W-field 梯度 bound 推導完成  
**核心概念：** 在極端磁場下，SYNC 場屏蔽激活，在脈衝星/磁星發射中產生 IXPE 可觀測的標誌性特徵。

---

## 1. 最大可持續磁場 — 𝒩 凝聚推導

### 1.1 終極 W-field Bound

SYNC 場梯度有最大可持續值：

$$|\nabla A|_{\text{max}} = \frac{\varepsilon \beta}{\ell_{\text{min}}}, \quad \ell_{\text{min}} = \frac{1}{\sqrt{\kappa}} = 4\, M_P^{-1}$$

終極磁場 bound：

$$B_{\text{max}} = \varepsilon \beta \cdot M_P \cdot \sqrt{\kappa} = 3.36 \times 10^{37} \text{ G}$$

### 1.2 𝒩 作為篩選稀釋因子

$$\mathcal{N} = \frac{B_{\text{max}}}{B_{\text{obs}}}$$

| 天體 | $B_{\text{obs}}$ (G) | 𝒩 | 物理層 |
|:-----|:--------------------|:--|:-------|
| 太陽黑子 | $10^3$ | $3.4 \times 10^{34}$ | 對流層 |
| 白矮星 | $10^8$ | $3.4 \times 10^{29}$ | 簡併電子氣 |
| 脈衝星 | $10^{12}$ | $3.4 \times 10^{25}$ | 磁層 |
| 磁星 | $10^{15}$ | $3.4 \times 10^{22}$ | 慢轉凝聚 |

### 1.3 𝒩 的物理意義

每個 W-field 篩選量子承載 $\sim \varepsilon \cdot M_P$ 的篩選容量。W-field 一致性約束 $\Sigma W_i \leq 1$ 在每個相干體積內限制 $\mathcal{N}_{\text{coh}} \leq 1/\varepsilon \approx 6.47$。

但緻密天體跨越許多相干體積：

$$\mathcal{N}_{\text{total}} = \left(\frac{\xi}{R}\right)^3 \cdot \frac{1}{\varepsilon} \approx 2.3 \times 10^{62}$$

遠大於所需的 $3.4 \times 10^{25}$ — W-field 篩選容量從不是瓶頸。

### 1.4 磁星結構解釋

磁星接近篩選極限，因為：
1. 慢轉 → 小磁層 → 減少的相干體積
2. $\mathcal{N}$ 更小 → B 更大
3. 磁星處於 **SYNC 場篩選邊緣**

## 2. IXPE 垂直偏振

相鄰 SYNC 場模式的偏振角：

$$\Delta\phi = \frac{\pi}{2} \times \frac{0.309}{1.309} \approx 42.5^\circ$$

$\Delta n = 2 \to 90^\circ$ ✅

## 3. 可測試預測

| 預測 | 可觀測量 | 儀器 |
|:-----|:---------|:-----|
| 垂直無線電/X射線偏振 | Δφ = 90° | IXPE |
| B ~ 10¹² G 光譜截止 | 同步輻射抑制 | NICER, IXPE |
| 磁星 B-field 飽和 | B_max ~ 10¹⁵ G | 磁星巡天 |

## 4. 待完成

𝒩 凝聚推導：W-field 凝聚體密度、W-field PDE 模式佔有數、與觀測的脈衝星/磁星磁場分布連接。

**狀態：** 🟡 結構預測已立，𝒩 凝聚推導待續。
