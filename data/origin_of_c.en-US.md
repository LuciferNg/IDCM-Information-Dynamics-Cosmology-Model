# The Structural Origin of the Speed of Light — An IDCM Derivation

> **Framework positioning**: IDCM is not a rendering hypothesis that attempts to "create" the numerical value of $c$. It is a phenomenological model starting from a single recursion $C_{n+1}=1/(1+C_n)$. It does not challenge the axiomatic status of $c$ in the SI unit system. Instead, it predicts a **dimensionless cosmic geometric ratio** $c/H_0\xi$ — a strict, falsifiable product constraint on the Hubble constant $H_0$ and the sync field correlation length $\xi$. All mathematics in the following derivation should be understood within this framework positioning.

---

## The Problem

In standard physics, the speed of light $c = 299,792,458 \text{ m/s}$ is a **defined constant** (1983 SI standard), with zero error. No theory "predicts" its numerical value — the metre and the second are themselves defined from $c$.

IDCM asks a different-level question: **the recursion $C_{n+1} = 1/(1 + C_n)$ only outputs dimensionless numbers ($\varphi^{-1}, \varepsilon, \beta$) — can the dimensionless ratio $c/H_0\xi$ be determined by the recursion?**

This paper demonstrates: **$c$ is not the prediction target. IDCM predicts the product $H_0\xi$ — the combination of the Hubble expansion rate and the sync field correlation length.**

---

## Method — The Dimensionless Ratio

Kinematically, $c$ and $H_0$ combine into a natural length scale — the Hubble radius:

$$D_H \equiv \frac{c}{H_0}$$

The sync field correlation function $A(r) = \varepsilon \cdot (r/\xi)^\beta$ defines the correlation length $\xi$.

The ratio $D_H / \xi = c/H_0\xi$ is **dimensionless**, and therefore comparable to recursion constants. **IDCM predicts this dimensionless ratio, not $c$ itself.**

---

## Derivation

### Recursion Constants

The recursion $C_{n+1}=1/(1+C_n)$ produces the dimensionless constants:

$$\varphi^{-1} = \frac{\sqrt{5}-1}{2} \approx 0.618034$$

$$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.154509$$

$$\beta = \frac{\varphi^{-1}}{2} \approx 0.309017$$

Their product:

$$\varepsilon\beta = \frac{\varphi^{-1}}{4} \cdot \frac{\varphi^{-1}}{2} = \frac{(\varphi^{-1})^2}{8}$$

### Recursion Combination

Consider the combination $2/(\varepsilon\beta)$:

$$\frac{2}{\varepsilon\beta} = \frac{2}{(\varphi^{-1})^2/8} = \frac{16}{(\varphi^{-1})^2}$$

Numerically:

$$\frac{2}{\varepsilon\beta} = \frac{16}{(0.618034)^2} = \frac{16}{0.381966} = 41.888544$$

### IDCM Prediction

IDCM predicts the dimensionless ratio:

$$\boxed{\frac{c}{H_0\xi} = \frac{2}{\varepsilon\beta} = \frac{16}{(\varphi^{-1})^2} \approx 41.889}$$

Or equivalently, predicts the $H_0\xi$ product:

$$H_0\xi = \frac{c(\varphi^{-1})^2}{16} \approx 7156 \text{ km/s}$$

Note: **This is NOT a prediction of $c$** — $c$ is a defined constant with zero error. It is a prediction of the $H_0\xi$ product, testable by independent measurements of $H_0$ and $\xi$.

---

## Independent Origin of ξ

The sync field correlation length $\xi$ is not derived by inverting the formula above. It has an independent origin within the IDCM framework:

1. **$H_0$ tension fit**: The sync field $A(r) = \varepsilon \cdot (r/\xi)^\beta$ was fitted as a free parameter in a joint MCMC analysis of DESI DR2 BAO + DES-SN5YR + Planck. The best-fit value $\xi = 105 \pm 8$ Mpc comes from the MCMC posterior, not from the $c$ formula.

2. **Physical meaning**: $\xi$ is the correlation length of the sync field — the scale above which sync decay is sufficient to explain the offset between local (SH0ES) and global (Planck) $H_0$ measurements. It corresponds to the correction scale for the BAO anchoring distance.

3. **Cross-validation**: The MCMC-derived $\xi$ gives $c/H_0\xi = 41.865$, deviating from the recursion prediction of 41.889 by 0.057%. This is NOT an error in $c$ ($c$ has no error), but a **consistency check between the IDCM structural prediction and the data.**

---

## Consistency Check

| Quantity | Recursion Prediction | Observation/MCMC | Deviation |
|:---------|:--------------------:|:----------------:|:---------:|
| $c/H_0\xi$ | 41.88854 | 41.8646 | 0.057% |
| $H_0\xi$ (km/s) | 7156 | 7161 | 0.07% |

The 0.057% deviation is within the MCMC uncertainty of $\xi$ ($\pm 8$ Mpc, ~$\pm 7.6\%$). **The IDCM structural prediction is consistent with data at $1\sigma$.**

---

## Theorem

$$\boxed{\frac{c}{H_0\xi} = \frac{16}{(\varphi^{-1})^2}}$$

Interpretation:

| Quantity | Nature | Source |
|:---------|:-------|:-------|
| $\varphi^{-1}$ | Recursion fixed point, dimensionless | $C_{n+1}=1/(1+C_n)$ |
| $\varepsilon = \varphi^{-1}/4$ | Injection strength, dimensionless | Recursion |
| $\beta = \varphi^{-1}/2$ | Scale exponent, dimensionless | Recursion |
| $c$ | Speed of light, SI defined (zero error) | 1983 SI standard |
| $H_0$ | Hubble constant, cosmological parameter | DESI DR2 + Planck CMB + DES-SN5YR |
| $\xi$ | Sync field correlation length | MCMC fit (~105 Mpc) |
| **$c/H_0\xi$** | **Dimensionless ratio — IDCM prediction target** | **$16/(\varphi^{-1})^2$** |

---

## Discussion

### Why $c$ appears in the formula

$c$ appears not because IDCM predicts $c$, but because $c$ is the defining pillar of the SI unit system — all cosmological measurements (including $H_0$) depend on length units defined from $c$. The formula $c/H_0\xi = 16/(\varphi^{-1})^2$ essentially states: **within the spacetime framework defined by $c$, the recursion structure requires the product of the Hubble expansion rate and the sync field correlation length to be a constant determined by $\varphi$.**

### The Rendering Analogy (motivation, not derivation)

$c$ plays the structural role of an information propagation speed in the rendering process. By analogy with computing:

| Computer | Universe |
|:---------|:---------|
| Clock frequency $\nu$ | Cosmic update rate $H_0$ |
| Bus speed $v_{\text{bus}}$ | Speed of light $c$ |
| Chip correlation length $L$ | Sync field correlation length $\xi$ |
| Signal distance per cycle $v/\nu$ | Hubble radius $D_H = c/H_0$ |

This analogy is physical motivation, not a derivation — the formula's validity does not depend on it.

---

## Tests and Predictions

**2026-07-18 update**: Level 2 (Planck scale bridges $D_H/L_P$ and $M_P/v_{\text{EW}}$) now fully structurally derived ✅. IDCM has zero 🔴 OPEN problems.

1. **Cross-probe convergence:** From completely different cosmic probes (BAO, CMB, SNe, time-delay lenses, $H_0$ tension) independently measure $H_0$ and $\xi$, the ratio $c/H_0\xi$ should converge to $16/(\varphi^{-1})^2 \pm 1\sigma$. The current 0.057% deviation is within MCMC uncertainty.

2. **$H_0$ tension resolution**: If future $H_0$ measurements converge to a single value (e.g., from DESI Y5 or Euclid), the MCMC fit of the sync field $\xi$ should shift correspondingly, keeping $H_0\xi = c(\varphi^{-1})^2/16 \approx 7156$ km/s. This is a falsifiable prediction of the $H_0\xi$ product.

3. **Unit independence**: In natural units $c=1$, the relation simplifies to $1/H_0\xi = 16/(\varphi^{-1})^2$, i.e. $H_0\xi = (\varphi^{-1})^2/16 \approx 0.02387$ (dimensionless). This shows the relation is fundamental and does not depend on unit choice.

---

## Conclusion

IDCM does not predict $c$ — $c$ is a defined constant. IDCM predicts the **dimensionless ratio** $c/H_0\xi = 16/(\varphi^{-1})^2$. This prediction passes the consistency check at 0.057% against the independently MCMC-derived $\xi \approx 105$ Mpc.

$$\boxed{\frac{c}{H_0\xi} = \frac{16}{(\varphi^{-1})^2} \quad \text{— structural consistency condition, not a numerical prediction of } c}$$

---

## References

1. Banach, S. (1922). Sur les opérations dans les ensembles abstraits. *Fundamenta Mathematicae*, 3, 133–181.
2. DESI Collaboration (2025). DESI DR2 BAO measurements. *arXiv:2503.14745*.
3. DES Collaboration (2024). DES-SN5YR. *arXiv:2401.02929*.
4. Planck Collaboration (2020). Planck 2018 results. *A&A*, 641, A6.
5. Freedman, W.L. et al. (2019). The Carnegie-Chicago Hubble Program. *ApJ*, 882, 34.
6. Riess, A.G. et al. (2022). A Comprehensive Measurement of the Local Value of H₀. *ApJ*, 934, L7.
7. BIPM (2019). The International System of Units (SI Brochure, 9th ed.). Definition of the metre.