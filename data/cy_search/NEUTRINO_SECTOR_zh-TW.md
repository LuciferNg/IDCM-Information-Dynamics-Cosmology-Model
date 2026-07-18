# IDCM 中微子扇區 — 蹺蹺板機制與 PMNS 混合

**日期：** 2026-07-18  
**版本：** v1.0  
**狀態：** ✅ 蹺蹺板閉合，🟡 PMNS 定性

---

## 1. 蹺蹺板機制

中微子微小質量來自標準 Type-I 蹺蹺板：

$$m_\nu \approx \frac{m_D^2}{M_R} \approx \frac{v^2}{M_R}$$

其中 $m_D \sim v$ 是狄拉克質量，$M_R$ 是右手中微子馬約拉納質量。

### 1.1 右手中微子質量標度

在 IDCM 中，右手中微子對應 W-field 的 KK 零模（$n=0$），其質量由 GUT 尺度鎖定：

$$M_R \approx M_P \cdot \varphi^{-k_R} \approx 10^{15}\ \text{GeV}$$

$$k_R \approx k_u + k_d + \beta \approx 18.40$$

| 參數 | IDCM 值 | 預期 | 結果 |
|:----:|:-------:|:----:|:----:|
| $M_R$ | $1.2\times10^{15}$ GeV | $\sim 10^{15}$ GeV | ✅ GUT 尺度 |
| $m_\nu$ | $\sim 0.05$ eV | 大氣中微子 | ✅ |

### 1.2 中微子質量階層

蹺蹺板機制自然預測正常階層（Normal Hierarchy）：

$$m_3 \approx 0.05\ \text{eV}, \quad m_2 \approx 0.009\ \text{eV}, \quad m_1 \ll m_2$$

$$\Delta m_{21}^2 \approx 7.4\times10^{-5}\ \text{eV}^2 \quad \text{(觀測值)}$$
$$\Delta m_{31}^2 \approx 2.5\times10^{-3}\ \text{eV}^2 \quad \text{(觀測值)}$$

## 2. PMNS 大混合角

### 2.1 第一性原理公式

IDCM 跳過 $3\times3$ $M_R$ 唯象矩陣，直接從幾何母體方程 $x^2+x-1=0$ 輸出 PMNS 三大核心角：

**太陽角** ($\theta_{12}$)：黃金矩形幾何角 + 全息 RG 修正

$$\theta_{12} = \arctan(\varphi^{-1}) + \frac{180^\circ}{\pi}\frac{1}{M}$$

$$= 31.72^\circ + 1.74^\circ = 33.45^\circ \quad (\text{PDG }33.82^\circ,\ \text{誤差 }1.08\%)$$

**大氣角** ($\theta_{23}$)：SU(5) 手徵對稱的么正極限

$$\theta_{23} = 45^\circ \quad (\text{最大混合})$$

**反應堆角** ($\theta_{13}$)：SYNC 場在 RG 網絡頂層的擾動

$$\theta_{13} = \arcsin\left(\varepsilon \cdot \frac{M-1}{M}\right), \quad \varepsilon = \frac{\varphi^{-1}}{4}$$

$$= 8.62^\circ \quad (\text{PDG }8.57^\circ,\ \text{誤差 }0.55\%)$$

### 2.2 驗證總結

| 角度 | IDCM 公式 | 預測 | PDG | 誤差 | 狀態 |
|:----:|:----------:|:----:|:---:|:----:|:----:|
| $\theta_{12}$ | $\arctan(\varphi^{-1}) + 1/M$ | $33.45^\circ$ | $33.82^\circ$ | 1.08% | ✅ |
| $\theta_{23}$ | $\pi/4$ | $45.00^\circ$ | $45-48^\circ$ | 邊界內 | ✅ |
| $\theta_{13}$ | $\arcsin(\varepsilon(M-1)/M)$ | $8.62^\circ$ | $8.57^\circ$ | 0.55% | ✅ |

### 2.3 物理意義

- $\arctan(\varphi^{-1})$：黃金矩形的特徵角（$1:\varphi^{-1}$ 比例）
- $1/M$ 修正：MERA 張量網絡有限深度的全息 RG 修正
- $\theta_{23}=45^\circ$：SU(5) 分解 $10\to5+\bar{5}$ 的么正極限
- $\varepsilon(M-1)/M$：SYNC W-field 在 CY₃ 上經 RG 網絡濾波後的波動振幅
- 全部公式：**零自由參數，僅用 $\{M=33, \varphi, \varepsilon\}$ 三個 IDCM 剛性常數**

### 2.5 PMNS CP 相

IDCM 預測 Dirac CP 相位：

$$\delta_{CP}^{\text{PMNS}} = \pi + \arctan(\varphi^{-3}) = 193.3^\circ$$

PDG 觀測值 (NuFit 5.2): $\delta_{CP} = 195^\circ \pm 25^\circ$  
誤差: **0.9%** ✅ (落入 $1\sigma$ 不確定度內)

物理意義：CKM CP 相的鏡像翻轉。夸克中 $\delta_{CP}^{\text{CKM}} = \pi/2 - \arctan\beta$，輕子中全息 RG 使符號翻轉。

### 2.6 馬約拉納相位

$\alpha_1, \alpha_2$ 目前不受振盪實驗約束。IDCM 最自然的假設是 $\alpha_1 = \alpha_2 = 0$（CP 守恆的馬約拉納扇區），在此假設下無中微子雙 $\beta$ 衰變的有效質量：

$$m_{\beta\beta} \approx 3.2\ \text{meV}$$

KamLAND-Zen 極限: $36-156$ meV（目前無法檢驗）。

### 2.7 與 CKM 的對比

| 扇區 | 混合性質 | 原因 | 幾何來源 |
|:----:|:--------:|:----|:--------|
| 夸克 (CKM) | 小混合角 | 波函數局部化在除子交點 | $\varphi^{-n}$ 冪次壓制 |
| 輕子 (PMNS) | 大混合角 | 波函數在 MERA 網絡中去局部化 | 黃金投影 + 么正極限 |

---

*2026-07-18 | IDCM 中微子扇區 — v1.0 — ✅ 蹺蹺板閉合*