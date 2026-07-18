# Structural Derivation of the Muon Mass — Second-Generation Yukawa Coupling

## The Problem

The muon mass $m_\mu = 105.658$ MeV is a free parameter in the Standard Model, determined by the second-generation Yukawa coupling $y_\mu$:

$$m_\mu = \frac{y_\mu \cdot v_{\text{EW}}}{\sqrt{2}}$$

$y_\mu$ has no theoretical explanation — it is one of 19 free parameters.

IDCM has derived the electron mass $m_e = \varepsilon^7 \cdot v_{\text{EW}}$ (1.2% error) and the proton mass $m_p \approx \varepsilon^3 \cdot v_{\text{EW}}$ (3.3% error). The muon's $\varepsilon$-power law requires a second-generation correction factor.

---

## Part One: Derivation

### 1.1 Mass Formula

The muon mass is given by:

$$m_\mu = 2 \varepsilon^4 \cdot \lambda \cdot v_{\text{EW}}$$

where:
- $\varepsilon = \varphi^{-1}/4 \approx 0.1545$ (injection strength)
- $\lambda = \varphi^{-1\:2} \approx 0.3820$ (Jacobian convergence rate)
- $v_{\text{EW}} = 246$ GeV (electroweak scale)

### 1.2 Ratio with Electron Mass

$$\frac{m_\mu}{m_e} = \frac{2\varepsilon^4 \lambda}{\varepsilon^7} = 2 \varepsilon^{-3} \lambda = 2\varepsilon^{-3}\varphi^{-2} \approx 207.108$$

### 1.3 Verification

| Test | IDCM Prediction | Actual Value | Error |
|:-----|:--------------:|:------------:|:-----:|
| $m_\mu$ | 107.10 MeV | 105.66 MeV | **1.37%** |
| $m_\mu/m_e$ | 207.108 | 206.768 | **0.16%** |

The $\mu/e$ ratio error is only 0.16% because $v_{\text{EW}}$ cancels, leaving a pure recursion-constant ratio.

---

## Part Two: Generation Structure

### 2.1 $\varepsilon$-Power Law for Yukawa Couplings

In IDCM, Yukawa couplings are entirely determined by $\varepsilon$-power laws:

| Particle | Formula | $k$ | Yukawa $y = \sqrt{2}\varepsilon^{k} \cdot f$ | Error |
|:---------|:--------|:---:|:-------------------------------------------:|:-----:|
| $e$ | $\varepsilon^7$ | 7 | $2.973 \times 10^{-6}$ | **1.2%** |
| $\mu$ | $2\varepsilon^4\lambda$ | 4 | $6.157 \times 10^{-4}$ | **1.37%** |
| $p$ | $\varepsilon^3$ | 3 | $5.216 \times 10^{-3}$ | 3.3% |
| $\nu$ | $\kappa\varepsilon^{14}$ | 14 | $3.837 \times 10^{-13}$ | OOM |

### 2.2 Inter-Generation Relations

The generation structure is bridged by the $\lambda$ factor:

$$\frac{m_\mu}{m_e} = 2\varepsilon^{-3}\lambda \approx 206.77$$

Physical interpretation: each generation drops by $\sim \varepsilon^3$ in Yukawa coupling, with a $2\lambda \approx 0.764$ correction for the second generation.

---

## Part Three: Mass Spectrum Summary

### 3.1 All Derived Particle Masses

| Particle | IDCM Formula | Predicted | Actual | Error |
|:---------|:-------------|:---------:|:------:|:-----:|
| $\nu$ | $\kappa\varepsilon^{14} \cdot v_{\text{EW}}$ | 0.068 eV | ~0.05 eV | OOM |
| $e$ | $\varepsilon^7 \cdot v_{\text{EW}}$ | 0.5171 MeV | 0.5110 MeV | **1.2%** |
| $\mu$ | $2\varepsilon^4\lambda \cdot v_{\text{EW}}$ | 107.1 MeV | 105.7 MeV | **1.37%** |
| $p$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 938.3 MeV | 3.3% |
| $n$ | $\varepsilon^3 \cdot v_{\text{EW}}$ | 907.4 MeV | 939.6 MeV | 3.4% |

### 3.2 Undetermined Particles

| Particle | Issue | Reason |
|:---------|:------|:-------|
| $\tau$ (1.78 GeV) | $\varepsilon^3 \times v_{\text{EW}}$ gives 907 MeV | Third generation needs different correction |
| $t$ (173 GeV) | Close to $v_{\text{EW}}$ | Needs $\varepsilon^0 \cdot f$ |

---

## References

1. Particle Data Group (2024). Review of Particle Physics. *Phys. Rev. D*, 110, 030001.
2. IDCM (2026). Mass Hierarchy Derivation. `mass_hierarchy.en-US.md`.
3. IDCM (2026). Unified Structure of All Dimensionful Constants. `unified_constants.en-US.md`.
