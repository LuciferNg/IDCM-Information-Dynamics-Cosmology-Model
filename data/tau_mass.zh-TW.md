# τ 子質量的結構推導

## 公式

$$m_\tau = \varepsilon^2 \cdot \beta \cdot v_{\text{EW}}$$

其中 $\varepsilon = \varphi^{-1}/4$，$\beta = \varphi^{-1}/2$，$v_{\text{EW}} = 246$ GeV。

## 驗證

| 量 | IDCM 預測 | 實際值 | 誤差 |
|:---|:---------:|:------:|:----:|
| $m_\tau$ | 1814.8 MeV | 1776.9 MeV | **2.13%** |

## 世代結構

| 粒子 | $\varepsilon$ 冪 | 修正因子 | 質量 | 誤差 |
|:-----|:---------------:|:--------:|:----:|:----:|
| $e$ | $\varepsilon^7$ | 1 | 0.517 MeV | **1.20%** |
| $\mu$ | $\varepsilon^4$ | $2\lambda = 0.764$ | 107.1 MeV | **1.37%** |
| $\tau$ | $\varepsilon^2$ | $\beta = 0.309$ | 1814.8 MeV | **2.13%** |

冪次遞減：7 → 4 → 2（每代約 -3）。

## 交叉驗證：世代比值

由於 $v_{\text{EW}}$ 在比值中抵消，這些比值是對遞迴常數的純粹檢驗：

| 比值 | IDCM | 實際 | 誤差 |
|:----|:----:|:----:|:----:|
| $m_\tau/m_\mu$ | 16.94 | 16.82 | **0.76%** ✅ |
| $m_\mu/m_e$ | 207.1 | 206.8 | **0.16%** ✅ |
| $m_\tau/m_e$ | 3509 | 3477 | **0.92%** ✅ |

## 參數敏感度

τ 子質量公式 $m_\tau = \varepsilon^2 \cdot \beta \cdot v_{\text{EW}}$ 的敏感度：

$$\frac{\delta m_\tau}{m_\tau} = 2\frac{\delta\varepsilon}{\varepsilon} + \frac{\delta\beta}{\beta} + \frac{\delta v_{\text{EW}}}{v_{\text{EW}}}$$

由於 $\varepsilon$ 和 $\beta$ 為精確代數常數（$\varphi^{-1}/4$ 和 $\varphi^{-1}/2$），唯一的參數不確定性來自 $v_{\text{EW}}$（$\pm 0.02\%$）。2.13% 的誤差反映的是 $\varepsilon^2\beta$ 冪律的結構近似，而非參數擬合。

## 完整世代譜

| 粒子 | $\varepsilon$ 冪 | 公式 | IDCM | 實際 | 誤差 |
|:----|:---------------:|:-----|:----:|:----:|:----:|
| $e$ | $\varepsilon^7$ | $\varepsilon^7 v_{\text{EW}}$ | 0.517 MeV | 0.511 MeV | 1.20% ✅ |
| $\mu$ | $\varepsilon^4$ | $2\varepsilon^4\lambda v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | 1.37% ✅ |
| $\tau$ | $\varepsilon^2$ | $\varepsilon^2\beta v_{\text{EW}}$ | 1814.8 MeV | 1776.9 MeV | 2.13% ✅ |
| $t$ | $\varepsilon^0$ | $v_{\text{EW}}/\sqrt{2}$ | 173.9 GeV | 173.0 GeV | 0.55% ✅ |