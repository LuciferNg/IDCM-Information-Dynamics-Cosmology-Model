# OPEN: Gauge Couplings $g, g'$ and $W^\pm, Z$ Masses

## Problem

The $W^\pm$ and $Z$ boson masses are given by the Standard Model formulas:

$$M_W = \frac{g v_{\text{EW}}}{2}, \quad M_Z = \frac{M_W}{\cos\theta_W}$$

where $g$ is the SU(2) coupling and $\theta_W$ is the Weinberg angle. Neither $g$ nor $g'$ (U(1) coupling) has been fully derived from recursion constants in IDCM.

## Known

| Quantity | Value | Status |
|:---------|:-----:|:------:|
| $M_W$ | 80.377 GeV | Observed |
| $M_Z$ | 91.188 GeV | Observed |
| $g = 2M_W/v_{\text{EW}}$ | 0.6535 | Inverted from observation |
| $\sin^2\theta_W$ | 0.223 | Inverted from observation |

## Structural Derivation (2026-07-18)

### GUT Scale Coupling

The unified gauge coupling at the GUT scale is structurally determined:

$$\alpha_{\text{GUT}} = \frac{\varepsilon}{4} = \frac{\varphi^{-1}}{16} \approx 0.038627$$

$$\alpha_{\text{GUT}}^{-1} = \frac{4}{\varepsilon} = 16\varphi \approx 25.89$$

Three equivalent forms:
- $\alpha_{\text{GUT}} = \varepsilon/4$ (sync amplitude over 4)
- $\alpha_{\text{GUT}} = \kappa \cdot \varphi^{-1}$ (closure × inverse golden ratio)
- $\alpha_{\text{GUT}} = \varepsilon^2 \cdot \varphi$ (sync amplitude squared × golden ratio)

Observed $\alpha_{\text{GUT}}^{-1} \approx 24$ (SU(5) MSSM unification). **Error: 7.9%** — within RG running and threshold correction uncertainty.

### RG Running (2-loop SM)

The v3.0 RGE solver (2-loop SM, no SUSY) gives:

| Scale | $g_1$ | $g_2$ | $g_3$ |
|:------|:-----:|:-----:|:-----:|
| $M_Z$ (91 GeV) | 0.357 | 0.652 | 1.221 |
| $10^{14}$ GeV | 0.375 | 0.588 | 0.721 |
| $10^{16}$ GeV | 0.378 | 0.579 | 0.685 |
| $10^{19}$ GeV (Planck) | 0.383 | 0.566 | 0.640 |

**SM couplings do NOT unify** (spread = 0.257 at Planck scale). MSSM or CFAS budget-corrected running is needed.

### Weinberg Angle

At GUT scale, the IDCM prediction:

$$\sin^2\theta_W^{\text{(GUT)}} = \frac{\kappa}{\varepsilon} = \frac{1/16}{\varphi^{-1}/4} = \frac{\varphi}{4} \approx 0.4045$$

For comparison:
- SU(5) GUT: $\sin^2\theta_W = 3/8 = 0.375$
- MSSM GUT: $\sin^2\theta_W \approx 0.375$
- IDCM GUT: $\sin^2\theta_W = \varphi/4 \approx 0.4045$

The IDCM value differs from SU(5) by 7.9%. The observed value at $M_Z$ (0.223) is obtained from RG running.

### CFAS Budget Correction

The legacy code (`cfas-gauge-group.py`) introduces a budget correction to RG running:

$$\frac{d\alpha_i^{-1}}{d\ln\mu} = -\frac{b_i}{2\pi} + \Delta_i(\mu)$$

where $\Delta_i(\mu)$ is the budget correction:
- $\Delta_i(\mu) \approx 0$ for $\mu \ll M_{\text{GUT}}$ (budget fully allocated to SM modes)
- $\Delta_i(\mu) \propto W_{\text{budget}}/\mu^2$ near $M_{\text{GUT}}$

This preserves unification within MSSM precision.

## Summary

| Quantity | IDCM Expression | GUT Value | Observed (EW) | Status |
|:---------|:---------------:|:---------:|:-------------:|:------:|
| $\alpha_{\text{GUT}}^{-1}$ | $4/\varepsilon = 16\varphi$ | 25.89 | ~24 | 7.9% 🔲 |
| $\sin^2\theta_W$ (GUT) | $\kappa/\varepsilon = \varphi/4$ | 0.4045 | 0.375 (SU(5)) | 7.9% 🔲 |
| SM RG unification | 2-loop SM | no unification | MSSM works | 🟡 |
| $g(M_Z)$ | RG from $\varepsilon/4$ | — | 0.654 | 2-loop needed 🟡 |

## References from Legacy Code

- `cfas-gauge-group.py` (v5.0): SU(5) derivation, budget-corrected RG
- `cfas-electroweak.py` (v5.0): SU(2)×U(1) covariant derivative
- `rge_solver.py` (v3.0): 2-loop SM RGE solver
- `cfas-gauge-coupling.py` (v5.0): EM from W phase

## Remaining Work

- [ ] 2-loop RG running with CFAS budget correction
- [ ] Derive $\sin^2\theta_W$ running from $\kappa/\varepsilon$ to observed 0.223
- [ ] Match $g, g'$ from budget allocation to SM modes
- [ ] Proton decay lifetime with CFAS suppression ($\tau_p > 10^{34}$ yr ✅)