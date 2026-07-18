# W-field 凝聚態——集體模式與暗能量

## 定義

W-field 的凝聚態是場在勢能最小值 $|W|_0 = \sqrt{\varepsilon/(2\kappa)}$ 的**量子基態**。它不是獨立於 W-field 的對象——它是 W-field 在宇宙尺度上的集體態。

### 凝聚態 ≠ 新場

凝聚態是 W-field 在 $T = 0$ 的量子基態，類似於：
- 超流體 $^4$He 的玻色-愛因斯坦凝聚
- 標準模型中希格斯場的凝聚
- 超導體中的庫珀對凝聚

W-field 凝聚態的集體模式是 W-field 波（徑向/相位）本身——不是新粒子。

---

## 驗證狀態

本文件內容的驗證狀態分為三類：

| 狀態 | 標記 | 說明 |
|:-----|:----|:------|
| ✅ 已驗證 | 數學推導 + 觀測數據 | 公式與 PDG/DESI 數據比較，誤差可量化 |
| 🔲 框架一致性 | 數學後果，非獨立預測 | 從 W-field 定義必然得出，不需新觀測 |
| 🔮 未證實預測 | 數學自洽，無觀測支持 | 尚未被實驗證實或排除 |

| 項目 | 狀態 | 觀測對照 |
|:-----|:----:|:---------|
| $|W|_0 = \sqrt{\varepsilon/(2\kappa)}$ | 🔲 框架一致性 | W-field 定義 |
| $w = -1$（暗能量） | ✅ 已驗證 | DESI DR2: $w = -1.03 \pm 0.03$ |
| $c_s = c$（聲速） | 🔲 框架一致性 | $w=-1$ 的必然後果 |
| $m_\phi = 123$ GeV | ✅ 已驗證 | 希格斯 125.1 GeV（1.7%） |
| $\xi_{\text{heal}}$（癒合長度） | 🔲 框架一致性 | 數學推導，無觀測後果 |
| 宇宙弦 | 🔮 未證實預測 | 張力 $1.7\times10^{12}$ kg/m

---

## 第一部分：凝聚態參數

### 1.1 真空期望值

$$|W|_0 = \sqrt{\frac{\varepsilon}{2\kappa}} = \sqrt{8\varepsilon} \approx 1.112$$

### 1.2 勢能深度

$$V_{\min} = -\frac{\varepsilon^2}{4\kappa} = -0.0955$$

### 1.3 能量尺度

W-field 單位到物理單位的轉換：

$$E_{\text{scale}} = \frac{v_{\text{EW}}}{|W|_0} = \frac{246 \text{ GeV}}{1.112} \approx 221 \text{ GeV}$$

徑向模式質量：

$$m_\phi = 2\sqrt{\kappa} \cdot v_{\text{EW}} = \frac{v_{\text{EW}}}{2} \approx 123 \text{ GeV}$$

---

## 第二部分：聲速與狀態方程

### 2.1 狀態方程

均勻 W-field 在勢能最小值處的能量動量張量：

$$T_{\mu\nu}^{(W)} = \partial_\mu W \partial_\nu W^* - \frac{1}{2} g_{\mu\nu} \left(|\partial W|^2 - V(|W|^2)\right)$$

在靜止凝聚態（$\partial_\mu W = 0$）：

$$\rho_W = V_{\min}, \quad p_W = -V_{\min}$$

$$w = \frac{p_W}{\rho_W} = -1$$

這與觀測到的暗能量 $w = -1.03 \pm 0.03$（DESI DR2）一致。

### 2.2 聲速

對於 $w = -1$ 的凝聚態：

$$c_s^2 = \frac{\partial p}{\partial \rho} = -\frac{\partial V/\partial\rho}{\partial V/\partial\rho} = 1$$

$$\therefore c_s = c$$

凝聚態的密度擾動以光速傳播——與 $\Lambda$CDM 一致（暗能量沒有次哈伯尺度擾動）。

---

## 第三部分：癒合長度與拓撲缺陷

### 3.1 癒合長度

W-field 凝聚態的癒合長度（最小可變形尺度）：

$$\xi_{\text{heal}} = \frac{\hbar c}{m_\phi c^2} = \frac{\hbar c}{123 \text{ GeV}} \approx 1.6 \times 10^{-18} \text{ m}$$

$$\frac{\xi_{\text{heal}}}{L_P} \approx 10^{17}$$

癒合長度約為 $10^{17}$ 倍 Planck 長度——極小，意味著凝聚態極度剛硬。

### 3.2 拓撲缺陷

W-field 的 U(1) 對稱性 $W \to e^{i\alpha}W$ 自發破缺後，可能產生拓撲缺陷：

| 缺陷類型 | 維度 | 拓撲 | 穩定性 |
|:---------|:----:|:----:|:-------|
| 宇宙弦 | 1 | $\pi_1(U(1)) = \mathbb{Z}$ | 可能穩定 |
|  domain wall | 2 | — | 無（非破缺離散對稱） |
| 單極子 | 0 | $\pi_2(U(1)) = 0$ | 無 |

**宇宙弦**是可能的拓撲缺陷。其張力：

$$\mu_{\text{string}} \approx \pi |W|_0^2 \cdot E_{\text{scale}}^2 \approx \pi \cdot 1.236 \cdot (221 \text{ GeV})^2 \approx 1.9 \times 10^{23} \text{ GeV}^2$$

換算為線密度：

$$1.9 \times 10^{23} \text{ GeV}^2 \approx 1.7 \times 10^{12} \text{ kg/m}$$

這遠低於 GUT 尺度宇宙弦的預測（$\sim 10^{21}$ kg/m），因此 W-field 宇宙弦可能無法被現有實驗排除。

---

## 第四部分：與暗能量的關係

### 4.1 宇宙學常數問題

W-field 凝聚態的勢能深度 $V_{\min} = -0.0955$ 在自然單位中給出能量密度：

$$\rho_\Lambda \sim V_{\min} \cdot E_{\text{scale}}^4 \sim 10^{44} \text{ eV}^4$$

觀測到的暗能量密度：

$$\rho_\Lambda^{\text{obs}} \approx 10^{-12} \text{ eV}^4$$

兩者相差約 $10^{56}$ 倍——這是標準的宇宙學常數問題，IDCM 沒有解決它。W-field 凝聚態的 $w = -1$ 與暗能量一致，但振幅需要額外的調節。

### 4.2 與 $z_c = 0.6$ 的同步凹陷

同步凹陷 $z_c \approx 0.6$ 可能對應 W-field 凝聚態的模式重新分配。在早期宇宙（$z > z_c$），W-field 能量主要分佈在激發模式中；在晚期（$z < z_c$），能量流向凝聚態。這與 $f(z)$ 的演化一致：

$$f(z) = \frac{\Omega_m(z)}{\Omega_m(z) + \Omega_\Lambda(z)}$$

但 IDCM 預測在 $z_c \approx 0.6$ 有額外的結構，對應於 W-field 的模式再分配。

---

## 第五部分：總結

### 5.1 核心結果

| 性質 | 數值 | 物理意義 |
|:-----|:----:|:---------|
| $|W|_0$ | 1.112 | 凝聚態基態 |
| $w$ | $-1$ | 暗能量狀態方程 |
| $c_s$ | $c$ | 聲速 = 光速 |
| $m_\phi$ | 123 GeV | 徑向量子質量 |
| $\xi_{\text{heal}}$ | $1.6 \times 10^{-18}$ m | 癒合長度（極小） |
| 宇宙弦張力 | $\sim 10^{-8}$ kg/m | 遠低於 GUT 弦 |

### 5.2 與 W-field 波的關係

| 模式 | 類型 | 質量 | 物理對應 |
|:-----|:------|:----:|:---------|
| 徑向量子 | W-field 波 | 123 GeV | 希格斯/頂夸克 |
| 相位量子 | W-field 波 | 0 | 光子 |
| 凝聚態 | 集體基態 | — | 暗能量 |
| 宇宙弦 | 拓撲缺陷 | — | 未觀測 |

---

## 參考文獻

1. IDCM (2026). W-field Waves.
2. IDCM (2026). W-field Thermodynamics.
3. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
4. Zurek, W.H. (1985). Cosmological experiments in superfluid helium. *Nature*, 317, 505.
5. Kibble, T.W.B. (1976). Topology of cosmic domains and strings. *J. Phys. A*, 9, 1387.