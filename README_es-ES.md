# IDCM — Modelo Cosmológico de Dinámica de la Información

[← Volver a selección de idioma](README.md)

---

**Modelo cosmológico de primeros principios con cero parámetros libres.** Todas las constantes emergen de una única ecuación cuadrática $x^2 + x - 1 = 0$ mediante la recursión $C_{n+1} = 1/(1 + C_n)$. **Los 19 parámetros del Modelo Estándar se predicen desde primeros principios.**

---

## Logro: 19 parámetros SM desde primeros principios

| Sector | Parámetro | Fórmula IDCM | Predicción | PDG | Error |
|:-------|:---------:|:-------------|:----------:|:---:|:-----:|
| **9 masas fermiónicas** | $m_c/m_t$ | $\varphi^{-M\beta}$ | 1.277 GeV | 1.27 GeV | 0.57% |
| | $m_s/m_b$ | $\varphi^{-((M-7)\beta-\varphi^{-4})}$ | 93.9 MeV | 93.4 MeV | 0.51% |
| | $m_\mu/m_\tau$ | $\varphi^{-(M-14)\beta}$ | 105.35 MeV | 105.66 MeV | 0.30% |
| **Higgs** | $m_H$ | $v\cdot\varphi^{-9\beta/2}$ | 125.99 GeV | 125.10 GeV | 0.71% |
| **CKM** | $V_{us}$ | $\varphi^{-M/11}$ | 0.23607 | 0.22650 | 4.2% |
| | $V_{cb}$ | $\varphi^{-M/5}$ | 0.04182 | 0.04210 | **0.83%** |
| | $V_{ub}$ | $\varphi^{-(M/5+M/11+2)}$ | 0.00376 | 0.00361 | 4.3% |
| | $\delta_{CP}$ | $\pi/2-\arctan\beta$ | 72.83° | 68.80° | 5.9% |
| **PMNS** | $\theta_{12}$ | $\arctan\varphi^{-1}+1/M$ | 33.45° | 33.82° | 1.08% |
| | $\theta_{23}$ | $\pi/4$ | 45° | 45-48° | ✅ |
| | $\theta_{13}$ | $\arcsin(\varepsilon(M-1)/M)$ | 8.62° | 8.57° | **0.55%** |
| | $\delta_{CP}$ | $\pi+\arctan\varphi^{-3}$ | 193.3° | 195° | 0.9% |
| **Ángulo de Weinberg** | $\sin^2\theta_W$ | $V_{us}\cdot(1-\varphi^{-9})$ | 0.23296 | 0.23122 | 0.75% |
| **Materia oscura** | $M_{\text{DM}}$ | $M_P e^{-48}\varphi^{-1/2}$ | 13.68 MeV | 13.8 MeV | 0.88% |

Todo desde **4 constantes IDCM**: $M=33$, $N_h=42$, $\beta=\varphi^{-1}/2$, $\varepsilon=\varphi^{-1}/4$.

---

## Mecanismo central

### Ecuación generadora

$$x^2 + x - 1 = 0$$

**Raíz positiva**: $\varphi^{-1} = (\sqrt{5} - 1)/2 \approx 0.618034$

### Proceso recursivo

$$C_{n+1} = \frac{1}{1 + C_n},\quad C_0 = 1$$

Error menor a $10^{-3}$ tras 8 pasos.

### Constantes IDCM

| Símbolo | Valor | Origen |
|:--------|:------|:-------|
| $\varphi^{-1}$ | 0.618034 | Raíz de $x^2+x-1=0$ |
| $\varepsilon$ | $\varphi^{-1}/4 \approx 0.154509$ | División $2\times2$ |
| $\kappa$ | $1/16 = 0.0625$ | Identidad algebraica |
| $\beta$ | $\varphi^{-1}/2 \approx 0.309017$ | Exponente SYNC |
| $M$ | 33 | Pasos RG de MERA |
| $N_h$ | 42 | Torre KK |
| $z_c$ | $0.6 \pm 0.05$ | Corrimiento sincrónico |

## Validación

| Dataset | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:--------|:---------------------:|:--------------------------:|:--------------:|
| DESI DR2 BAO | 9.22 | 15.64 | -6.42 |
| DES-SN5YR | 1639.8 | 1643.6 | -3.8 |
| $H_0$ SH0ES | 5.0σ | → resuelta | — |
| $S_8$ | 2.5σ | → resuelta | — |
| **Total** | **1853 puntos** | — | **−9.8** |

---

**Ecuación central**: $x^2 + x - 1 = 0$ · **Cero parámetros libres** · **Δχ² = −9.8 vs ΛCDM**
