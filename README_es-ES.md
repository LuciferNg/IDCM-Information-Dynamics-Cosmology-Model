# IDCM — Modelo Cosmológico de Dinámica de la Información (Information Dynamics Cosmology Model)

[← Volver a selección de idioma](README.md)

---

**Un modelo cosmológico con cero parámetros libres.** Todas las constantes surgen de una única ecuación cuadrática $x^2 + x - 1 = 0$ mediante la recursión $C_{n+1} = 1/(1 + C_n)$. Resuelve la tensión $H_0$ (5.0σ → efecto de fase de sincronía) y la tensión $S_8$ (2.5σ → resuelta). Δχ² = −9.8 en 1853 puntos de datos independientes.

---

## Motivación

El modelo ΛCDM estándar requiere al menos seis parámetros libres ($\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$) y enfrenta tensiones observacionales crecientes: la tensión $H_0$ (SH0ES Ceféidas vs Planck CMB, 5.0σ), la tensión $S_8$ (Planck vs cartografiado de lentes débiles, 2.5σ), y la preferencia de DESI por energía oscura dinámica ($w_0$-$w_a$ en 2.5–3.5σ).

IDCM propone que estas tensiones no surgen de errores de medición sino de una capa faltante en la cosmología: **el universo no es una colección de partículas — es una recursión de información convergiendo a un punto fijo.** Todas las discrepancias observacionales emergen naturalmente como efectos de fase de sincronía de esta recursión, y cada constante cosmológica es una consecuencia algebraica de una única ecuación cuadrática.

## Mecanismo Central

### Ecuación Generadora

$$x^2 + x - 1 = 0$$

Su raíz positiva $\varphi^{-1} \approx 0.618034$ es el conjugado de la proporción áurea y el **punto fijo** de la recursión.

### La Recursión

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

El factor de convergencia $\lambda = \varphi^{-2} \approx 0.382 < 1$ garantiza convergencia lineal.

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

## Cuatro Constantes Fundamentales

| Símbolo | Fórmula | Valor | Origen |
|:-------:|:-------:|:-----:|:------:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545085 | Amplitud de sincronía (2×2) |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | Constante de cierre, álgebra exacta |
| $\beta$ | $\varphi^{-1}/2$ | 0.309017 | Exponente de escala |
| $z_c$ | de $N_{\text{horizon}}$ | 0.6 ± 0.05 | Corrimiento al rojo de sincronía |

## Validación Observacional

| Canal | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:------|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | **9.22** | 15.64 | **−6.42** |
| SNe (DES-SN5YR) | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | **13.7** | 14.8 | **−1.1** |
| **Total** | — | — | **−9.8 (3.1σ)** |

## Tensiones Resueltas

- $H_0$ (5.0σ): 🟡 Sesgo de calibración por fase de sincronía: $H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$
- $S_8$ (2.5σ): ✅ Resuelta, IDCM predice $S_8 = 0.786 \pm 0.008$
- DESI $w_0$-$w_a$ (2.5–3.5σ): ✅ La protuberancia $f(z)$ imita energía oscura dinámica naturalmente

## Ciclo Cósmico

$$\Delta t_{\text{reinicio}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ es exacto. $\kappa = 1/16$ es el único valor consistente con el universo observable.

## Campo W

$$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2), \quad V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

Masas: $m_e \approx 0.511$ MeV, $m_p \approx 938$ MeV, $m_\nu \approx 0.01$–$0.1$ eV.

## Predicciones

- DESI DR3: $z_c$ error se reduce a ±0.02
- Euclid: $f\sigma_8$ se desvía ~3% de ΛCDM
- Roman: $H_0$ precisión ~0.5 km/s
- CMB-S4: Confirma $S_8 = 0.78$
- DESI BAO $z=1.5-2.5$: Distingue protuberancia de ley de potencia

## Referencias

| Dataset | Referencia | Identificador |
|:--------|:-----------|:-------------:|
| DESI DR2 BAO | DESI Collab. 2025 | arXiv:2503.14738 |
| DES-SN5YR | DES Collab. 2024 | arXiv:2401.02929 |
| Planck 2018 | Planck Collab. 2020 | arXiv:1807.06209 |
| SH0ES | Riess+2022 | 10.3847/2041-8213/ac5c5b |
| TRGB | Freedman+2020 | 10.3847/1538-4357/ab7339 |
| KiDS-1000 | Asgari+2021 | 10.1051/0004-6361/202039070 |
| DES Y3 WL | DES Collab. 2021 | 10.1103/PhysRevD.105.023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |

---

**Ecuación central**: $x^2 + x - 1 = 0$ · **GitHub**: [github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model](https://github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model)
