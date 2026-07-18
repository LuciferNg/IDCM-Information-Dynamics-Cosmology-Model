# OPEN: 規範耦合 $g, g'$ 與 $W^\pm, Z$ 質量

## 問題

$W^\pm$ 和 $Z$ 玻色子的質量由標準模型公式給出：

$$M_W = \frac{g v_{\text{EW}}}{2}, \quad M_Z = \frac{M_W}{\cos\theta_W}$$

其中 $g$ 是 SU(2) 耦合，$\theta_W$ 是 Weinberg 角。$g$ 和 $g'$（U(1) 耦合）在 IDCM 中尚未從遞迴常數完全推導。

## 已知

| 量 | 數值 | 狀態 |
|:---|:----:|:----:|
| $M_W$ | 80.377 GeV | 觀測 |
| $M_Z$ | 91.188 GeV | 觀測 |
| $g = 2M_W/v_{\text{EW}}$ | 0.6535 | 從觀測反推 |
| $\sin^2\theta_W$ | 0.223 | 從觀測反推 |

## 結構推導（2026-07-18）

### GUT 尺度耦合

統一規範耦合在 GUT 尺度由結構決定：

$$\alpha_{\text{GUT}} = \frac{\varepsilon}{4} = \frac{\varphi^{-1}}{16} \approx 0.038627$$

$$\alpha_{\text{GUT}}^{-1} = \frac{4}{\varepsilon} = 16\varphi \approx 25.89$$

三種等價形式：
- $\alpha_{\text{GUT}} = \varepsilon/4$（同步幅度除以 4）
- $\alpha_{\text{GUT}} = \kappa \cdot \varphi^{-1}$（閉合常數 × 黃金比例倒數）
- $\alpha_{\text{GUT}} = \varepsilon^2 \cdot \varphi$（同步幅度平方 × 黃金比例）

觀測 $\alpha_{\text{GUT}}^{-1} \approx 24$（SU(5) MSSM 統一）。**誤差：7.9%**——在 RG 跑動和閾值修正不確定度範圍內。

### RG 跑動（2-loop SM）

v3.0 RGE 求解器（2-loop SM，無 SUSY）給出：

| 尺度 | $g_1$ | $g_2$ | $g_3$ |
|:-----|:-----:|:-----:|:-----:|
| $M_Z$ (91 GeV) | 0.357 | 0.652 | 1.221 |
| $10^{14}$ GeV | 0.375 | 0.588 | 0.721 |
| $10^{16}$ GeV | 0.378 | 0.579 | 0.685 |
| $10^{19}$ GeV (Planck) | 0.383 | 0.566 | 0.640 |

**SM 耦合不統一**（Planck 尺度 spread = 0.257）。需要 MSSM 或 CFAS 預算修正 RG。

### Weinberg 角

在 GUT 尺度，IDCM 預測：

$$\sin^2\theta_W^{\text{(GUT)}} = \frac{\kappa}{\varepsilon} = \frac{1/16}{\varphi^{-1}/4} = \frac{\varphi}{4} \approx 0.4045$$

比較：
- SU(5) GUT：$\sin^2\theta_W = 3/8 = 0.375$
- MSSM GUT：$\sin^2\theta_W \approx 0.375$
- IDCM GUT：$\sin^2\theta_W = \varphi/4 \approx 0.4045$

IDCM 值與 SU(5) 相差 7.9%。在 $M_Z$ 處觀測值 0.223 來自 RG 跑動。

### CFAS 預算修正

舊版代碼（`cfas-gauge-group.py`）引入預算修正到 RG 跑動：

$$\frac{d\alpha_i^{-1}}{d\ln\mu} = -\frac{b_i}{2\pi} + \Delta_i(\mu)$$

其中 $\Delta_i(\mu)$ 為預算修正：
- $\Delta_i(\mu) \approx 0$ 當 $\mu \ll M_{\text{GUT}}$（預算全部分配給 SM 模式）
- $\Delta_i(\mu) \propto W_{\text{budget}}/\mu^2$ 接近 $M_{\text{GUT}}$

這在 MSSM 精度內保持統一。

## 總結

| 量 | IDCM 表達式 | GUT 值 | 觀測 (EW) | 狀態 |
|:---|:-----------:|:------:|:---------:|:----:|
| $\alpha_{\text{GUT}}^{-1}$ | $4/\varepsilon = 16\varphi$ | 25.89 | ~24 | 7.9% 🔲 |
| $\sin^2\theta_W$ (GUT) | $\kappa/\varepsilon = \varphi/4$ | 0.4045 | 0.375 (SU(5)) | 7.9% 🔲 |
| SM RG 統一 | 2-loop SM | 不統一 | MSSM 可行 | 🟡 |
| $g(M_Z)$ | RG from $\varepsilon/4$ | — | 0.654 | 需 2-loop 🟡 |

## 舊版代碼參考

- `cfas-gauge-group.py` (v5.0)：SU(5) 推導、預算修正 RG
- `cfas-electroweak.py` (v5.0)：SU(2)×U(1) 協變導數
- `rge_solver.py` (v3.0)：2-loop SM RGE 求解器
- `cfas-gauge-coupling.py` (v5.0)：W 相位產生的 EM

## 剩餘工作

- [ ] 使用 CFAS 預算修正的 2-loop RG 跑動
- [ ] 推導 $\sin^2\theta_W$ 從 $\kappa/\varepsilon$ 到 0.223 的跑動
- [ ] 從預算分配到 SM 模式匹配 $g, g'$
- [ ] CFAS 壓制下的質子衰變壽命（$\tau_p > 10^{34}$ yr ✅）