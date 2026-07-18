# Structural Derivation of the Tau Mass

## Formula

$$m_\tau = \varepsilon^2 \cdot \beta \cdot v_{\text{EW}}$$

where $\varepsilon = \varphi^{-1}/4$, $\beta = \varphi^{-1}/2$, $v_{\text{EW}} = 246$ GeV.

## Verification

| Quantity | IDCM Prediction | Actual Value | Error |
|:---------|:---------------:|:------------:|:-----:|
| $m_\tau$ | 1814.8 MeV | 1776.9 MeV | **2.13%** |

## Generation Structure

| Particle | $\varepsilon$-power | Correction factor | Mass | Error |
|:---------|:------------------:|:-----------------:|:----:|:----:|
| $e$ | $\varepsilon^7$ | 1 | 0.517 MeV | **1.20%** |
| $\mu$ | $\varepsilon^4$ | $2\lambda = 0.764$ | 107.1 MeV | **1.37%** |
| $\tau$ | $\varepsilon^2$ | $\beta = 0.309$ | 1814.8 MeV | **2.13%** |

Power decreases: 7 → 4 → 2 (approx -3 per generation).

## Cross-validation: Generation Ratios

Since $v_{\text{EW}}$ cancels in ratios, these provide a pure test of the recursion-derived constants:

| Ratio | IDCM | Actual | Error |
|:------|:----:|:------:|:-----:|
| $m_\tau/m_\mu$ | 16.94 | 16.82 | **0.76%** ✅ |
| $m_\mu/m_e$ | 207.1 | 206.8 | **0.16%** ✅ |
| $m_\tau/m_e$ | 3509 | 3477 | **0.92%** ✅ |

## Parameter Sensitivity

The tau mass formula $m_\tau = \varepsilon^2 \cdot \beta \cdot v_{\text{EW}}$ has sensitivity:

$$\frac{\delta m_\tau}{m_\tau} = 2\frac{\delta\varepsilon}{\varepsilon} + \frac{\delta\beta}{\beta} + \frac{\delta v_{\text{EW}}}{v_{\text{EW}}}$$

Since $\varepsilon$ and $\beta$ are exact algebraic constants ($\varphi^{-1}/4$ and $\varphi^{-1}/2$), the only parametric uncertainty is $v_{\text{EW}}$ ($\pm 0.02\%$). The 2.13% error reflects the structural approximation of the $\varepsilon^2\beta$ power law, not parameter fitting.

## Full Generation Spectrum

| Particle | $\varepsilon$-power | Formula | IDCM | Actual | Error |
|:---------|:------------------:|:--------|:----:|:------:|:-----:|
| $e$ | $\varepsilon^7$ | $\varepsilon^7 v_{\text{EW}}$ | 0.517 MeV | 0.511 MeV | 1.20% ✅ |
| $\mu$ | $\varepsilon^4$ | $2\varepsilon^4\lambda v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | 1.37% ✅ |
| $\tau$ | $\varepsilon^2$ | $\varepsilon^2\beta v_{\text{EW}}$ | 1814.8 MeV | 1776.9 MeV | 2.13% ✅ |
| $t$ | $\varepsilon^0$ | $v_{\text{EW}}/\sqrt{2}$ | 173.9 GeV | 173.0 GeV | 0.55% ✅ |