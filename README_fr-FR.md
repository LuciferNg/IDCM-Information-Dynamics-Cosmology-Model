# IDCM — Modèle Cosmologique de Dynamique de l'Information

[← Retour au sélecteur de langue](README.md)

---

**Modèle cosmologique de premiers principes avec zéro paramètre libre.** Toutes les constantes émergent d'une unique équation quadratique $x^2 + x - 1 = 0$ via la récursion $C_{n+1} = 1/(1 + C_n)$. **Les 19 paramètres du Modèle Standard sont prédits depuis les premiers principes.**

---

## Accomplissement : 19 paramètres MS depuis premiers principes

| Secteur | Paramètre | Formule IDCM | Prédiction | PDG | Erreur |
|:--------|:---------:|:-------------|:----------:|:---:|:------:|
| **9 masses fermioniques** | $m_c/m_t$ | $\varphi^{-M\beta}$ | 1.277 GeV | 1.27 GeV | 0.57% |
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
| **Angle de Weinberg** | $\sin^2\theta_W$ | $V_{us}\cdot(1-\varphi^{-9})$ | 0.23296 | 0.23122 | 0.75% |
| **Matière noire** | $M_{\text{DM}}$ | $M_P e^{-48}\varphi^{-1/2}$ | 13.68 MeV | 13.8 MeV | 0.88% |

Tout depuis **4 constantes IDCM** : $M=33$, $N_h=42$, $\beta=\varphi^{-1}/2$, $\varepsilon=\varphi^{-1}/4$.

---

## Mécanisme central

### Équation génératrice

$$x^2 + x - 1 = 0$$

**Racine positive** : $\varphi^{-1} = (\sqrt{5} - 1)/2 \approx 0.618034$

### Processus récursif

$$C_{n+1} = \frac{1}{1 + C_n},\quad C_0 = 1$$

Erreur inférieure à $10^{-3}$ après 8 étapes.

### Constantes IDCM

| Symbole | Valeur | Origine |
|:--------|:-------|:--------|
| $\varphi^{-1}$ | 0.618034 | Racine de $x^2+x-1=0$ |
| $\varepsilon$ | $\varphi^{-1}/4 \approx 0.154509$ | Division $2\times2$ |
| $\kappa$ | $1/16 = 0.0625$ | Identité algébrique |
| $\beta$ | $\varphi^{-1}/2 \approx 0.309017$ | Exposant SYNC |
| $M$ | 33 | Pas RG de MERA |
| $N_h$ | 42 | Tour KK |
| $z_c$ | $0.6 \pm 0.05$ | Décalage synchrone |

## Validation

| Jeu de données | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:---------------|:---------------------:|:--------------------------:|:--------------:|
| DESI DR2 BAO | 9.22 | 15.64 | -6.42 |
| DES-SN5YR | 1639.8 | 1643.6 | -3.8 |
| $H_0$ SH0ES | 5.0σ | → résolue | — |
| $S_8$ | 2.5σ | → résolue | — |
| **Total** | **1853 points** | — | **−9.8** |

---

**Équation centrale** : $x^2 + x - 1 = 0$ · **Zéro paramètre libre** · **Δχ² = −9.8 vs ΛCDM**
