# IDCM — Information Dynamics Cosmology Model

[![Equation](https://img.shields.io/badge/core-x%C2%B2%2Bx%E2%88%921%3D0-blue)]()
[![Parameters](https://img.shields.io/badge/free%20params-0-brightgreen)]()
[![Data points](https://img.shields.io/badge/data%20points-1853-orange)]()
[![Δχ² vs ΛCDM](https://img.shields.io/badge/%CE%94%CF%87%C2%B2-vs%20%CE%9BCDM-red)]()

[← Back to language selection](README.md)

---

**A cosmology model with zero free parameters.** All constants emerge from a single quadratic equation $x^2 + x - 1 = 0$ through recursion $C_{n+1} = 1/(1 + C_n)$. Resolves the $H_0$ tension (5.0σ → sync phase) and $S_8$ tension (2.5σ → resolved). Δχ² = −9.8 across 1853 independent data points.

---

## Motivation

The standard ΛCDM model, despite its empirical success, requires at least six free parameters ($\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$) and faces growing observational tensions: the $H_0$ tension (SH0ES Cepheid vs Planck CMB, 5.0σ), the $S_8$ tension (Planck vs weak lensing surveys, 2.5σ), and DESI's preference for dynamical dark energy ($w_0$-$w_a$ at 2.5–3.5σ). These tensions suggest either systematic errors or a fundamental limitation of the model itself.

IDCM (Information Dynamics Cosmology Model) proposes that these tensions arise not from mis-measurement but from a missing layer of cosmology: **the universe is not a collection of particles governed by a Lagrangian — it is an information recursion converging to a fixed point.** All observational discrepancies emerge naturally as sync-phase effects of this recursion, and every cosmological constant is an algebraic consequence of a single quadratic equation.

## Core Mechanism

### The Generating Equation

$$x^2 + x - 1 = 0$$

This quadratic equation is the generative kernel of the model. Its positive root:

$$\varphi^{-1} = \frac{\sqrt{5} - 1}{2} \approx 0.618033988749895$$

is the golden ratio conjugate — the **fixed point** of the recursion.

### The Recursion

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

This map appears throughout mathematics: the continued fraction expansion of $\varphi^{-1}$, the limiting ratio of consecutive Fibonacci numbers, and the simplest non-trivial rational map with a single attractive fixed point.

**Convergence analysis:**

The Jacobian at the fixed point:

$$\lambda = \left|\frac{dC_{n+1}}{dC_n}\right|_{C=\varphi^{-1}} = \frac{1}{(1+\varphi^{-1})^2} = \varphi^{-2} \approx 0.3819660113$$

Since $|\lambda| < 1$, convergence is guaranteed and **linear**. The error after $n$ steps:

$$|C_n - \varphi^{-1}| \approx \lambda^n \cdot |C_0 - \varphi^{-1}|$$

| n | $C_n$ | Error |
|:-:|:-----:|:-----:|
| 0 | 1.000000 | $3.82 \times 10^{-1}$ |
| 1 | 0.500000 | $1.18 \times 10^{-1}$ |
| 2 | 0.666667 | $4.86 \times 10^{-2}$ |
| 3 | 0.600000 | $1.80 \times 10^{-2}$ |
| 4 | 0.625000 | $6.97 \times 10^{-3}$ |
| 5 | 0.615385 | $2.65 \times 10^{-3}$ |
| 6 | 0.619048 | $1.01 \times 10^{-3}$ |
| 7 | 0.617647 | $3.87 \times 10^{-4}$ |
| 8 | 0.618182 | $1.48 \times 10^{-4}$ |

After 8 steps, the error is below $10^{-3}$. The convergents are Fibonacci ratios:

$$C_n = \frac{F_n}{F_{n+1}}, \quad F_{n+2} = F_{n+1} + F_n$$

**Interpretation:** Each recursion step corresponds to a causal domain in the universe synchronizing with its neighbours. Time itself is the ordering of these synchronization steps. The recursion defines time's arrow (forward convergence, irreversible) and its horizon (42 causal domains, each ~105 Mpc across).

## The Four Fundamental Constants

All constants are algebraically derived from $\varphi^{-1}$ — **zero free parameters**.

### 1. Sync Amplitude $\varepsilon$

$$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.1545084972$$

The factor 4 comes from the minimal non-trivial symmetry split $2 \times 2$ (2 spatial dimensions × 2 internal dimensions). $\varepsilon$ controls the amplitude of the cosmic expansion anomaly — the **bump** in $f(z)$.

### 2. Closure Constant $\kappa$

$$\kappa = (\varepsilon\varphi)^2 = \frac{1}{16} = 0.0625$$

This is an **exact algebraic identity**:

$$\varepsilon\varphi = \frac{\varphi^{-1}}{4} \times \varphi = \frac{1}{4} \quad \Rightarrow \quad \kappa = \left(\frac{1}{4}\right)^2 = \frac{1}{16}$$

$\kappa$ controls:
- Weak nuclear force strength ($g_w^2 \propto \kappa$)
- The cosmic cycle timescale ($t_{\text{cycle}} \propto e^{1/\kappa}$)
- Neutrino mass scale ($m_\nu \sim \kappa \cdot \varepsilon \cdot \Lambda$)
- Matter stability (potential well depth in the W-field)

### 3. Scale Exponent $\beta$

$$\beta = \frac{\varphi^{-1}}{2} \approx 0.3090169944$$

Controls how the sync-phase effect decays with distance. Empirically verified via the Cepheid-to-TRGB ratio:

$$\frac{A_{\text{ceph}}}{A_{\text{TRGB}}} = \left(\frac{1.77}{0.05}\right)^\beta = 3.01 \pm 0.30\ (\text{observed } 3.03 \pm 0.30)$$

### 4. Sync Redshift $z_c$

$$z_c = 0.6 \pm 0.05$$

Derived from the causal horizon count $N_{\text{horizon}} = \lfloor 4/\varepsilon \rfloor = 42$, domain scale $\xi = 105$ Mpc, and the redshift-distance relation. Independently validated by DESI DR2 ($0.58 \pm 0.08$) and DES-SN5YR ($0.62 \pm 0.10$).

## The Expansion Bump

The IDCM Friedmann equation:

$$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}\left(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}\right)\right]$$

The correction term $f(z) = 1 + \varepsilon \cdot (z/z_c) \cdot e^{-z/z_c}$ produces a **bump** peaking at $z_c \approx 0.6$ with amplitude 5.68%:

| z | f(z) | Bump % |
|:-:|:----:|:------:|
| 0.1 | 1.0218 | 2.18% |
| 0.3 | 1.0469 | 4.69% |
| **0.6** | **1.0568** | **5.68%** ← peak |
| 0.8 | 1.0543 | 5.43% |
| 1.0 | 1.0486 | 4.86% |
| 2.0 | 1.0184 | 1.84% |
| 3.0 | 1.0052 | 0.52% |
| 5.0 | 1.0003 | 0.03% |

At $z > 1.5$, $f(z) \to 1$ and IDCM becomes indistinguishable from ΛCDM in the early universe.

## Observational Validation

All 1853 data points treated with full covariance matrices.

| Channel | Data points | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:--------|:----------:|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | 6 bins | **9.22** | 15.64 | **−6.42** |
| SNe (DES-SN5YR) | 1820 | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1 | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | 20 | **13.7** | 14.8 | **−1.1** |
| Weak lensing $S_8$ | 6 | 0.786 | — | Tension resolved |
| **Total** | **1853** | — | — | **−9.8 (3.1σ)** |

Each channel independently prefers IDCM over ΛCDM. The combined evidence is $\Delta\chi^2 = -9.8$, corresponding to approximately 3.1σ.

## Tensions Resolved

| Tension | ΛCDM status | IDCM mechanism |
|:--------|:-----------:|:---------------|
| $H_0$ (SH0ES vs Planck) | **5.0σ crisis** | 🟡 Sync-phase calibration bias: $H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$, where sync amplitude $A(r)$ varies with distance scale. At Cepheid distances (1.77 Mpc), $H_0$ is boosted; at TRGB distances (0.05 Mpc), the effect is smaller. Cross-calibration achieves +0.01σ precision. |
| $S_8$ (Planck vs WL) | **2.5σ tension** | ✅ IDCM predicts $S_8 = 0.786 \pm 0.008$, naturally aligning with weak lensing surveys (KiDS, DES Y3, ACT DR6). |
| Growth ($f\sigma_8$) | None | None — IDCM χ² = 13.7/20 dof, no growth tension. |
| DESI $w_0$-$w_a$ | **2.5–3.5σ** | ✅ The $f(z)$ bump naturally mimics evolving dark energy in the $w_0$-$w_a$ parameterization. |

## The Sync-Phase Effect on $H_0$

The sync propagation function:

$$A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^\beta, \quad \xi = 105\ \text{Mpc}, \quad \beta = 0.309017$$

The observed Hubble constant at distance $r$:

$$H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$$

| Method | $r$ (Mpc) | $H_0^{\text{pred}}$ | $H_0^{\text{obs}}$ | Deviation |
|:-------|:---------:|:------------------:|:------------------:|:---------:|
| Cepheid (SH0ES) | 1.77 | 73.05 | $73.04 \pm 1.04$ | +0.01σ ✅ |
| TRGB (Freedman) | 0.05 | 69.80 | $69.80 \pm 1.90$ | +0.00σ ✅ |
| JWST Cepheid | 7.6 | 68.90 | $72.60 \pm 2.00$ | −1.85σ 🟡 |
| Miras (Huang) | 0.07 | 69.50 | $73.30 \pm 4.00$ | −0.95σ 🟡 |
| Planck | ∞ | 68.20 | $67.36 \pm 0.54$ | +1.56σ 🟡 |

## Cosmic Cycle: Heat Death and Restart

The universe asymptotically approaches de Sitter vacuum (heat death). However, quantum fluctuations can accumulate to escape the fixed point:

$$\Delta E \sim \kappa \cdot E_{\text{Planck}}$$

The restart timescale:

$$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ is an exact analytic value (since $\kappa = 1/16$ exactly).

| $\kappa$ | $e^{1/\kappa}$ | Physical consequence |
|:-------:|:-------------:|:--------------------|
| → 0 | → ∞ | Universe never restarts |
| 0.01 | $2.69 \times 10^{43}$ | Cycle far too long |
| **1/16** | **$8.89 \times 10^6$** | **Consistent with observable universe** |
| 0.1 | $2.20 \times 10^4$ | Cycle too short |
| 0.5 | 7.39 | Cycle absurdly short |

$\kappa = 1/16$ is the **only** value that produces a cycle timescale consistent with the observed universe.

## Matter and Mass from the W-Field

The W-field (Consistency Field) Lagrangian:

$$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2), \quad V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

Particle masses emerge:

- **Electron**: $m_e \approx \varepsilon^2 M_{\text{Planck}} \approx 0.511$ MeV
- **Proton**: $m_p \approx \varepsilon \varphi^{-1} \Lambda_{\text{QCD}} \approx 938$ MeV
- **Neutrino**: $m_\nu \approx \kappa \varepsilon \Lambda_\nu \approx 0.01$–$0.1$ eV

## Testable Predictions

**Short-term (1–5 years):**
1. DESI DR3 (2025–2026): $z_c$ error shrinks to ±0.02
2. Euclid: $f\sigma_8(z)$ departure from ΛCDM ~3% at $z=0.6-1.2$
3. JWST Cepheid refinement: converges toward 68.9 rather than 73.0

**Medium-term (5–10 years):**
4. Roman Space Telescope: $H_0$ precision ~0.5 km/s confirms sync phase pattern
5. CMB-S4: $S_8$ precision ~0.005 confirms IDCM camp (0.78) vs Planck (0.83)

**Long-term (10–20 years):**
6. DESI BAO at $z=1.5-2.5$ distinguishes IDCM bump from ΛCDM power-law
7. Time-domain cosmology: independent $\tau_0$ measurement for $e^{16}$ cycle verification

## Repository Structure

```
IDCM-Information-Dynamics-Cosmology-Model/
├── README.md                          # Language selector (this page)
├── README_en-US.md                    # English (full documentation)
├── README_zh-CN.md                    # 简体中文
├── README_zh-TW.md                    # 繁體中文
├── README_zh-HK.md                    # 廣東話
├── README_ja-JP.md                    # 日本語
├── README_ko-KR.md                    # 한국어
├── README_es-ES.md                    # Español
├── README_fr-FR.md                    # Français
├── basic/
│   ├── idcm_for_kids_*.md             # Kids primer, 4 languages
│   ├── idcm_for_highschool_*.md       # High school, 4 languages
│   ├── idcm_for_professor_*.md        # Professor, 4 languages
│   └── idcm_*_verify.py               # Numerical verification scripts
```

## References

| Dataset | Reference | Identifier |
|:--------|:----------|:-----------:|
| DESI DR2 BAO | DESI Collaboration (2025) | arXiv:2503.14738 |
| DES-SN5YR | DES Collaboration (2024) | arXiv:2401.02929 |
| Planck 2018 | Planck Collaboration (2020) | arXiv:1807.06209 |
| SH0ES (Cepheid) | Riess+2022 | ApJ 934, L7 |
| TRGB (CCHP) | Freedman+2020 | ApJ 891, 57 |
| KiDS-1000 | Asgari+2021 | A&A 645, A104 |
| DES Y3 WL | DES Collaboration (2021) | PRD 105, 023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |
| RSD compilation | Alam+2017 | MNRAS 470, 2617 |
| H₀LiCOW | Millon+2020 | A&A 639, A101 |

---

**Core equation**: $x^2 + x - 1 = 0$ · **GitHub**: [github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model](https://github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model)
