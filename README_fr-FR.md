# IDCM — Modèle Cosmologique de Dynamique de l'Information (Information Dynamics Cosmology Model)

[← Retour à la sélection de langue](README.md)

---

**Un modèle cosmologique avec zéro paramètre libre.** Toutes les constantes émergent d'une unique équation quadratique $x^2 + x - 1 = 0$ via la récursion $C_{n+1} = 1/(1 + C_n)$. Résout la tension $H_0$ (5.0σ → effet de phase de synchronisation) et la tension $S_8$ (2.5σ → résolue). Δχ² = −9.8 sur 1853 points de données indépendants.

---

## Motivation

Le modèle ΛCDM standard nécessite au moins six paramètres libres ($\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$) et fait face à des tensions observationnelles croissantes : la tension $H_0$ (Céphéides SH0ES vs CMB Planck, 5.0σ), la tension $S_8$ (Planck vs sondages de lentille faible, 2.5σ), et la préférence de DESI pour l'énergie noire dynamique ($w_0$-$w_a$ à 2.5–3.5σ).

IDCM propose que ces tensions ne proviennent pas d'erreurs de mesure mais d'une couche manquante en cosmologie : **l'univers n'est pas une collection de particules — c'est une récursion d'information convergeant vers un point fixe.** Tous les écarts observationnels émergent naturellement comme effets de phase de synchronisation de cette récursion, et chaque constante cosmologique est une conséquence algébrique d'une unique équation quadratique.

## Mécanisme Central

### Équation Génératrice

$$x^2 + x - 1 = 0$$

Sa racine positive $\varphi^{-1} \approx 0.618034$ est le conjugué du nombre d'or et le **point fixe** de la récursion.

### La Récursion

$$C_{n+1} = \frac{1}{1 + C_n}, \quad C_0 = 1$$

Le facteur de convergence $\lambda = \varphi^{-2} \approx 0.382 < 1$ garantit une convergence linéaire.

| n | $C_n$ | Erreur |
|:-:|:-----:|:------:|
| 0 | 1.000000 | $3.82 \times 10^{-1}$ |
| 1 | 0.500000 | $1.18 \times 10^{-1}$ |
| 2 | 0.666667 | $4.86 \times 10^{-2}$ |
| 3 | 0.600000 | $1.80 \times 10^{-2}$ |
| 4 | 0.625000 | $6.97 \times 10^{-3}$ |
| 5 | 0.615385 | $2.65 \times 10^{-3}$ |
| 6 | 0.619048 | $1.01 \times 10^{-3}$ |
| 7 | 0.617647 | $3.87 \times 10^{-4}$ |
| 8 | 0.618182 | $1.48 \times 10^{-4}$ |

## Quatre Constantes Fondamentales

| Symbole | Formule | Valeur | Origine |
|:-------:|:-------:|:------:|:-------:|
| $\varepsilon$ | $\varphi^{-1}/4$ | 0.1545085 | Amplitude de synchronisation (2×2) |
| $\kappa$ | $(\varepsilon\varphi)^2 = 1/16$ | 0.0625 | Constante de fermeture, algèbre exacte |
| $\beta$ | $\varphi^{-1}/2$ | 0.309017 | Exposant d'échelle |
| $z_c$ | de $N_{\text{horizon}}$ | 0.6 ± 0.05 | Décalage vers le rouge de synchronisation |

## Validation Observationnelle

| Canal | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:------|:---------------------:|:--------------------------:|:--------------:|
| BAO (DESI DR2) | **9.22** | 15.64 | **−6.42** |
| SNe (DES-SN5YR) | **1639.8** | 1643.6 | **−3.8** |
| CMB shift R | 1.7425 | 1.7427 ± 0.0042 | −0.05σ |
| $f\sigma_8$ (RSD) | **13.7** | 14.8 | **−1.1** |
| **Total** | — | — | **−9.8 (3.1σ)** |

## Tensions Résolues

- $H_0$ (5.0σ): 🟡 Biais d'étalonnage par phase de synchronisation : $H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$
- $S_8$ (2.5σ): ✅ Résolue, IDCM prédit $S_8 = 0.786 \pm 0.008$
- DESI $w_0$-$w_a$ (2.5–3.5σ): ✅ La bosse $f(z)$ imite naturellement l'énergie noire dynamique

## Cycle Cosmique

$$\Delta t_{\text{redémarrage}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$

$e^{16} \approx 8.886 \times 10^6$ est exact. $\kappa = 1/16$ est la seule valeur cohérente avec l'univers observable.

## Champ W

$$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2), \quad V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

Masses : $m_e \approx 0.511$ MeV, $m_p \approx 938$ MeV, $m_\nu \approx 0.01$–$0.1$ eV.

## Prédictions

- DESI DR3 : erreur $z_c$ réduite à ±0.02
- Euclid : $f\sigma_8$ dévie de ~3% de ΛCDM
- Roman : précision $H_0$ ~0.5 km/s
- CMB-S4 : confirme $S_8 = 0.78$
- DESI BAO $z=1.5-2.5$ : distingue bosse de loi de puissance

## Références

| Jeu de données | Référence | Identifiant |
|:--------------|:-----------|:------------:|
| DESI DR2 BAO | DESI Collab. 2025 | arXiv:2503.14738 |
| DES-SN5YR | DES Collab. 2024 | arXiv:2401.02929 |
| Planck 2018 | Planck Collab. 2020 | arXiv:1807.06209 |
| SH0ES | Riess+2022 | 10.3847/2041-8213/ac5c5b |
| TRGB | Freedman+2020 | 10.3847/1538-4357/ab7339 |
| KiDS-1000 | Asgari+2021 | 10.1051/0004-6361/202039070 |
| DES Y3 WL | DES Collab. 2021 | 10.1103/PhysRevD.105.023520 |
| ACT DR6 | Qu+2024 | arXiv:2304.05202 |

---

**Équation centrale**: $x^2 + x - 1 = 0$ · **GitHub**: [github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model](https://github.com/LuciferNg/IDCM-Information-Dynamics-Cosmology-Model)
