# μ 子質量的結構推導——第二世代 Yukawa 耦合

## 問題

μ 子質量 $m_\mu = 105.658$ MeV 是標準模型的自由參數，由第二世代 Yukawa 耦合 $y_\mu$ 決定：

$$m_\mu = \frac{y_\mu \cdot v_{\text{EW}}}{\sqrt{2}}$$

$y_\mu$ 沒有任何理論解釋——它是 19 個自由參數之一。

IDCM 已推導電子質量 $m_e = \varepsilon^7 \cdot v_{\text{EW}}$（1.2% 誤差）和質子質量 $m_p \approx \varepsilon^3 \cdot v_{\text{EW}}$（3.3% 誤差）。μ 子的 $\varepsilon$ 冪律需要第二世代修正因子。

---

## 第一部分：推導

### 1.1 質量公式

μ 子質量由以下公式給出：

$$m_\mu = 2 \varepsilon^4 \cdot \lambda \cdot v_{\text{EW}}$$

其中：
- $\varepsilon = \varphi^{-1}/4 \approx 0.1545$（注入強度）
- $\lambda = \varphi^{-1\:2} \approx 0.3820$（Jacobian 收斂率）
- $v_{\text{EW}} = 246$ GeV（電弱尺度）

### 1.2 與電子質量的比率

$$\frac{m_\mu}{m_e} = \frac{2\varepsilon^4 \lambda}{\varepsilon^7} = 2 \varepsilon^{-3} \lambda = 2\varepsilon^{-3}\varphi^{-2} \approx 207.108$$

### 1.3 驗證

| 檢驗 | IDCM 預測 | 實際值 | 誤差 |
|:-----|:---------:|:------:|:----:|
| $m_\mu$ | 107.10 MeV | 105.66 MeV | **1.37%** |
| $m_\mu/m_e$ | 207.108 | 206.768 | **0.16%** |

比率 $\mu/e$ 的誤差只有 0.16%，因為 $v_{\text{EW}}$ 互相抵消，剩下純遞迴常數的比率。

---

## 第二部分：世代結構

### 2.1 Yukawa 耦合的 $\varepsilon$ 冪律

IDCM 中 Yukawa 耦合完全由 $\varepsilon$ 冪律決定：

| 粒子 | 公式 | $k$ | Yukawa $y = \sqrt{2}\varepsilon^{k} \cdot f$ | 誤差 |
|:-----|:-----|:---:|:-------------------------------------------:|:----:|
| $e$ | $\varepsilon^7$ | 7 | $2.973 \times 10^{-6}$ | **1.2%** |
| $\mu$ | $2\varepsilon^4\lambda$ | 4 | $6.157 \times 10^{-4}$ | **1.37%** |
| $p$ | $\varepsilon^3$ | 3 | $5.216 \times 10^{-3}$ | 3.3% |
| $\nu$ | $\kappa\varepsilon^{14}$ | 14 | $3.837 \times 10^{-13}$ | 量級 |

### 2.2 世代間的關係

世代結構由 $\lambda$ 因子橋接：

$$\frac{m_\mu}{m_e} = 2\varepsilon^{-3}\lambda \approx 206.77 \varphi^{-1?} \times ...$$

物理意義：每個世代之間 Yukawa 耦合下降 $\sim \varepsilon^3$，但第二世代有 $2\lambda \approx 0.764$ 的額外修正。

---

## 第三部分：質量譜總結

### 3.1 所有已推導粒子質量

| 粒子 | IDCM 公式 | 預測 | 實際 | 誤差 |
|:-----|:----------|:----:|:----:|:----:|
| $\nu$ | $\kappa\varepsilon^{14} \cdot v_{\text{EW}}$ | 0.068 eV | ~0.05 eV | 量級 |
| $e$ | $\varepsilon^7 \cdot v_{\text{EW}}$ | 0.5171 MeV | 0.5110 MeV | **1.2%** |
| $\mu$ | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | **1.37%** |
| $p$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 938.3 MeV | 3.3% |
| $n$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 939.6 MeV | 3.4% |

### 3.2 未被推導的粒子

| 粒子 | 問題 | 原因 |
|:-----|:------|:------|
| $\tau$（1.78 GeV） | $\varepsilon^3 \times v_{\text{EW}}$ 給 907 MeV | 第三世代需要不同修正 |
| $t$（173 GeV） | 接近 $v_{\text{EW}}$ | 需要 $\varepsilon^0 \cdot f$ |

---

## 參考文獻

1. Particle Data Group (2024). Review of Particle Physics. *Phys. Rev. D*, 110, 030001.
2. IDCM (2026). Mass Hierarchy Derivation. `mass_hierarchy.en-US.md`.
3. IDCM (2026). Unified Structure of All Dimensionful Constants. `unified_constants.en-US.md`.
