# IDCM BBN Compatibility Report

**Date:** 2026-07-18  
**Status:** ✅ Fully Compatible

---

## Summary

IDCM dark matter (13.68 MeV sterile fermion) is fully compatible with Big Bang Nucleosynthesis (BBN). This document provides five independent numerical checks.

---

## 1. DM Lifetime

Gravitational decay (Planck-suppressed):

$$\Gamma_{\text{grav}} = \frac{m_{\text{DM}}^3}{16\pi M_P^2} \approx 3.4 \times 10^{-46}\ \text{GeV}$$

$$\tau_{\text{grav}} \approx 4.5 \times 10^{69}\ \text{s}$$

BBN timescale $\sim 1$ s. **DM is stable at BBN.**

---

## 2. SYNC Field Decay Temperature

W-field mass $m_W = \sqrt{\kappa} M_P \approx 3.05 \times 10^{18}$ GeV:

$$\Gamma_W = \frac{m_W^3}{16\pi M_P^2} \approx 3.8 \times 10^{15}\ \text{GeV}$$

Reheat temperature:

$$T_{\text{reheat}} = \sqrt{\Gamma_W M_P} \approx 1.9 \times 10^{8}\ \text{GeV}$$

BBN temperature $\sim 1$ MeV. **SYNC field decays $10^{11}$ times before BBN.**

---

## 3. Effective Neutrino Number $\Delta N_{\text{eff}}$

$$\rho_{\text{DM}}(T_{\text{BBN}}) = \Omega_{\text{DM}} \rho_{\text{crit},0} \left(\frac{T_{\text{BBN}}}{T_0}\right)^3 \approx 3.6 \times 10^{-19}\ \text{GeV}^4$$

$$\rho_\nu(T_{\text{BBN}}) = \frac{7}{8} \cdot 2 \cdot \frac{\pi^2}{30} \cdot 3 \cdot T_{\text{BBN}}^4 \approx 1.7 \times 10^{-12}\ \text{GeV}^4$$

$$\Delta N_{\text{eff}} = \frac{8}{7} \cdot \frac{\rho_{\text{DM}}}{\rho_\nu} \approx 2.4 \times 10^{-7}$$

Planck bound: $\Delta N_{\text{eff}} < 0.17$. **Safety margin: 716,000×.**

---

## 4. DM Coupling & Thermalization

Gravitational cross-section: $\sigma_{\text{grav}} \sim 1/M_P^2 \approx 6.7 \times 10^{-39}$ GeV$^{-2}$

Interaction rate at BBN:

$$\Gamma_{\text{int}} = n_{\text{DM}} \cdot \sigma_{\text{grav}} \cdot v \approx 1.8 \times 10^{-55}\ \text{GeV}$$

Hubble rate:

$$H_{\text{BBN}} = \frac{T_{\text{BBN}}^2}{M_P} \approx 8.2 \times 10^{-26}\ \text{GeV}$$

$$\frac{\Gamma_{\text{int}}}{H} \sim 10^{-30} \ll 1$$

**DM never thermalized—it is completely sterile at BBN.**

---

## 5. Light Element Abundances

| Channel | Impact | Note |
|:--------|:------:|:-----|
| Direct nuclear reactions | None | Sterile particle, no EM/strong interaction |
| Expansion rate | $\Delta H/H \sim 10^{-7}$ | Negligible |
| Neutrino energy ratio | $\Delta N_{\text{eff}} = 2.4 \times 10^{-7}$ | Negligible |
| SYNC decay products | None | Decays $10^{11}\times$ before BBN |

**All light element abundances ($^4$He, D, $^3$He, $^7$Li) completely unaffected.**

---

## 6. Conclusion

| Check | Result | Margin |
|:-----|:------:|:------:|
| DM stable at BBN? | ✅ | $10^{69}\times$ |
| SYNC field decays before BBN? | ✅ | $10^{11}\times$ |
| $\Delta N_{\text{eff}} < 0.17$? | ✅ | $7 \times 10^{5}\times$ |
| DM never thermalized? | ✅ | $10^{30}\times$ |
| Light element abundances unchanged? | ✅ | Complete |

**IDCM dark matter is fully compatible with BBN. No $N_{\text{eff}}$ crisis exists.**

---

*2026-07-18 | IDCM BBN Compatibility Report*
