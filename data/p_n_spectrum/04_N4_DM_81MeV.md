# n=4: 81.7 MeV Dark Matter Candidate

**日期：** 2026-07-21
**背景：** P_n spectrum 預測 n=4 在 81.7 MeV

---

## 1. Thermal Freeze-Out

81.7 MeV DM 在早期宇宙的 freeze-out 由標準熱 relic 機制決定：

### Relic Density Condition

$$\Omega_{DM}h^2 \approx \frac{3\times 10^{-27} \text{ cm}^3/\text{s}}{\langle\sigma v\rangle}$$

觀測值 $\Omega_{DM}h^2 \approx 0.12$ → 需要：

$$\langle\sigma v\rangle_{\text{freeze-out}} \approx 2.5 \times 10^{-26} \text{ cm}^3/\text{s}$$

### Freeze-Out 溫度

$$T_f \approx \frac{m_\chi}{20} \approx \frac{81.7\text{ MeV}}{20} \approx 4\text{ MeV}$$

即 freeze-out 發生在 **QCD phase transition 之前、BBN 期間**。

### 通道 (Annihilation Channels)

81.7 MeV DM 的可能的 annihilation 通道（取決於 mediator）：

| 通道 | 最終產物 | 阈值 | 狀態 |
|:----|:---------|:----:|:----:|
| $\chi\bar\chi \to e^+e^-$ | 電子－正電子 | $2m_e = 1.02$ MeV | ✅ | 
| $\chi\bar\chi \to \mu^+\mu^-$ | μ 子 | $2m_\mu = 211$ MeV | ❌ 高於質量 |
| $\chi\bar\chi \to \pi\pi$ | 強子 | $2m_\pi \approx 270$ MeV | ❌ |
| $\chi\bar\chi \to \gamma\gamma$ | 光子 | 0 | ✅ loop-suppressed |
| $\chi\bar\chi \to \nu\bar\nu$ | 中微子 | 0 | ✅ weak 耦合 |

**關鍵限制：** 81.7 MeV 低於 $2m_\mu$（211 MeV），所以 freeze-out 時只能 annihilation 到 $e^+e^-$、$\gamma\gamma$、$\nu\bar\nu$。$e^+e^-$ 通道受 CMB 晚期能量注入嚴格限制。

---

## 2. 現有實驗限制

### 2.1 CMB 能量注入

Planck 2018 限制 DM 在 recombination 後的 energy injection：

$$f_{\text{eff}} \times \frac{\langle\sigma v\rangle}{m_\chi} < \text{bound}$$

對於 81.7 MeV DM annihilation 到 $e^+e^-$，CMB 限制：

$$\langle\sigma v\rangle_{e^+e^-} \lesssim 2 \times 10^{-27} \text{ cm}^3/\text{s}$$

**這比 thermal relic 需要的 2.5×10⁻²⁶ 低一個數量級。**
→ 如果 DM 主要 annihilation 到 $e^+e^-$，CMB 會排除 thermal relic scenario。

### 2.2 Supernova Cooling

如果 DM 有 mediator 耦合到 SM，SN1987A 限制 mediator 的 coupling：

| Mediator 類型 | Coupling 上限 | 81.7 MeV 的影響 |
|:-------------|:-------------:|:----------------|
| Dark photon ($A'$) | $\varepsilon \lesssim 3\times 10^{-9}$ (for $m_{A'} \sim 100$ MeV) | 🟡 Tight but allowed |
| Scalar mediator | $g \lesssim 10^{-10}$ (for $m_\phi \sim 1$ MeV) | 🔴 Very tight |
| Neutrino portal | No SN bound | ✅ Weak interaction |

### 2.3 Direct Detection (Direct Detection)

對於 81.7 MeV，傳統的 nuclear recoil 探測器（XENONnT, LZ）靈敏度急劇下降：

| 實驗 | 最低質量 | 對 81.7 MeV 的靈敏度 |
|:----|:--------:|:-------------------|
| XENONnT | ~3 GeV | ❌ 不靈敏 |
| CRESST | ~0.1 GeV | 🟡 邊緣靈敏 |
| DAMIC | ~1 GeV | ❌ |
| LDMX (future) | ~10 MeV–1 GeV | ✅ 設計範圍 |

**結論：** 81.7 MeV 喺目前 nuclear recoil 探測器嘅 blind spot，但 LDMX 喺未來可以探測。

### 2.4 Accelerator / Beam-Dump

| 實驗 | 質量範圍 | 對 81.7 MeV 嘅靈敏度 |
|:----|:--------:|:-------------------|
| NA64 | ~1–100 MeV | 🟡 Dark photon |
| LSND | ~10–100 MeV | 🟡 Neutrino portal |
| MicroBooNE | ~10–500 MeV | 🟡 | 
| Belle II (invisible) | ~1–8 GeV | ❌ 太輕 |

---

## 3. IDCM-specific Scenario

考慮到 P_n formula 的結構，n=4 的 81.7 MeV DM 係 W-field loop cascade 的自然產物：

### Scenario A：Dark Photon (最自然的 IDCM 對應)

光子係 W-field collective mode（Phase III）。Dark photon 係同一 mechanism 在 n=4 loop order 的 projection：

$$m_{A'} = P_4 = 81.7\text{ MeV}$$

Kinetic mixing $\varepsilon$ 由 W-field 的 inter-mode coupling 決定：

$$\varepsilon \sim \mathcal{O}(10^{-8} - 10^{-6})$$

這與 SN1987A 限制一致且可被 LDMX/NA64 探測。

### Scenario B：W-field Bound State

81.7 MeV W-field 的拓撲激發形成 bound state DM：

- 類似 QCD 的「glueball」，但來自 W-field
- 自然 stable（由 symmetry 保護）
- Self-interaction 由 W-field 的非線性項決定

### 比較

| 屬性 | Dark Photon A' | W-field Bound State |
|:----|:--------------:|:-------------------|
| Mass | 81.7 MeV natural | 81.7 MeV natural |
| Stability | 需 extra symmetry | ✅ natural |
| Detectability | LDMX, NA64, Belle II | 更難探測 |
| Coupling to SM | $\varepsilon$ | $\sim \varepsilon^2$ |

---

## 4. 結論

| 項目 | 狀態 |
|:----|:----:|
| 81.7 MeV thermal relic | 🟡 可能但 CMB 限制 tight（需 $e^+e^-$ suppression） |
| Dark photon interpretation | ✅ 最自然的 IDCM match，與 SN bound 一致 |
| Direct detection | 🔴 目前 blind spot，未來 LDMX 可測試 |
| 與 PDG 已知粒子匹配 | 🟡 接近 $m_\pi \cdot \varphi^{-1}=83.4$ MeV (2.1% diff) |

**推薦 Model：** Dark photon（kinetic mixing $\varepsilon \sim 10^{-8}-10^{-6}$），質量 81.7 MeV 由 P_n formula 結構強制。

**下一步：** 計算 freeze-out 過程的詳細 Boltzmann equation + CMB bound 的精確數值。